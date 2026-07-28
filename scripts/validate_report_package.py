#!/usr/bin/env python3
"""Validate a multi-note paper-summary output package."""

from __future__ import annotations

import argparse
import re
import struct
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path


FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*]\(([^)]+)\)")
IMAGE_LINK_RE = re.compile(r"!\[([^\]]*)]\(([^)]+)\)")
WIKI_LINK_RE = re.compile(r"\[\[([^]|#]+)(?:#[^]|]+)?(?:\|[^]]+)?]]")
PLACEHOLDER_RE = re.compile(
    r"\bTODO\b|<topic>|<term>|\[scientific topic]|\[Plain-language|\[figure-specific",
    re.IGNORECASE,
)

REQUIRED_NOTE_TYPES = {
    "index",
    "overview",
    "background",
    "methods",
    "critical_review",
    "research_application",
    "reproducibility",
    "source_coverage",
}

FIGURE_REQUIRED_HEADINGS = {
    "## 한 문장 주제",
    "## 논문에서의 역할",
    "## 패널 구성 지도",
    "## 패널별 상세 해설",
    "## 패널 간 논리",
    "## 통계와 시각 증거",
    "## 이 Figure가 확립하는 것",
    "## 한계",
}

MOJIBAKE_MARKERS = ("Ã", "Â", "â€", "ðŸ", "�")
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff"}


@dataclass
class Result:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER_RE.search(text)
    if not match:
        return {}
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line or line.startswith((" ", "\t", "-")):
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip("\"'")
    return values


def resolve_local_link(root: Path, source: Path, target: str) -> Path | None:
    target = target.strip().split("#", 1)[0]
    if not target or re.match(r"^[a-z]+://", target, re.IGNORECASE):
        return None
    target = target.replace("%20", " ")
    return (source.parent / target).resolve()


def strip_code(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    return re.sub(r"`[^`\n]*`", "", text)


def count_unescaped(text: str, token: str) -> int:
    return len(re.findall(rf"(?<!\\){re.escape(token)}", text))


def unescaped_pipe_count(line: str) -> int:
    return len(re.findall(r"(?<!\\)\|", line))


def png_dimensions(path: Path) -> tuple[int, int] | None:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) >= 24 and header[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">II", header[16:24])
    return None


def actual_entry_name(path: Path) -> str | None:
    if not path.parent.is_dir():
        return None
    expected = path.name.casefold()
    for child in path.parent.iterdir():
        if child.name.casefold() == expected:
            return child.name
    return None


def has_valid_image_signature(path: Path) -> bool:
    with path.open("rb") as handle:
        header = handle.read(16)
    suffix = path.suffix.lower()
    if suffix == ".png":
        return header.startswith(b"\x89PNG\r\n\x1a\n")
    if suffix in {".jpg", ".jpeg"}:
        return header.startswith(b"\xff\xd8\xff")
    if suffix == ".webp":
        return header.startswith(b"RIFF") and header[8:12] == b"WEBP"
    if suffix in {".tif", ".tiff"}:
        return header.startswith((b"II*\x00", b"MM\x00*"))
    return False


def validate_text_integrity(
    parsed: list[tuple[Path, dict[str, str], str]], result: Result
) -> None:
    for path, _, text in parsed:
        if unicodedata.normalize("NFC", text) != text:
            result.error(f"{path.name}: text is not Unicode NFC-normalized")
        if "\x00" in text:
            result.error(f"{path.name}: contains a NUL byte")
        for marker in MOJIBAKE_MARKERS:
            if marker in text:
                result.error(f"{path.name}: possible mojibake marker '{marker}'")

        math_text = strip_code(text)
        block_count = count_unescaped(math_text, "$$")
        if block_count % 2:
            result.error(f"{path.name}: unbalanced $$ MathJax delimiters")
        inline_text = re.sub(r"(?<!\\)\$\$.*?(?<!\\)\$\$", "", math_text, flags=re.DOTALL)
        if count_unescaped(inline_text, "$") % 2:
            result.error(f"{path.name}: unbalanced inline $ MathJax delimiters")
        if re.search(
            r"(?<!\\)\\\(|(?<!\\)\\\)|(?<!\\)\\\[|(?<!\\)\\\]",
            math_text,
        ):
            result.warn(
                f"{path.name}: use $...$ or $$...$$ instead of \\(...\\) or \\[...\\]"
            )

        lines = text.splitlines()
        index = 0
        while index < len(lines):
            if not lines[index].lstrip().startswith("|"):
                index += 1
                continue
            table_lines: list[str] = []
            while index < len(lines) and lines[index].lstrip().startswith("|"):
                table_lines.append(lines[index])
                index += 1
            if len(table_lines) >= 2:
                counts = [unescaped_pipe_count(line) for line in table_lines]
                if len(set(counts)) > 1:
                    result.error(
                        f"{path.name}: inconsistent Markdown table columns near "
                        f"'{table_lines[0][:60]}'"
                    )


def validate_links(root: Path, markdown_files: list[Path], result: Result) -> None:
    stems = {path.stem: path for path in markdown_files}
    for source in markdown_files:
        text = source.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK_RE.findall(text):
            resolved = resolve_local_link(root, source, target)
            if resolved is not None and not resolved.exists():
                result.error(f"{source.name}: broken Markdown link -> {target}")
            if resolved is not None and resolved.exists():
                requested_name = target.replace("\\", "/").split("#", 1)[0].rsplit("/", 1)[-1]
                actual_name = actual_entry_name(resolved)
                if requested_name and actual_name and requested_name != actual_name:
                    result.error(
                        f"{source.name}: filename case mismatch -> {target} "
                        f"(actual: {actual_name})"
                    )
        for target in WIKI_LINK_RE.findall(text):
            normalized = target.replace("\\", "/").rsplit("/", 1)[-1]
            normalized = normalized.removesuffix(".md")
            if normalized not in stems:
                result.error(f"{source.name}: broken wiki link -> [[{target}]]")


def validate_numbering(markdown_files: list[Path], result: Result) -> None:
    invalid_names = [
        path.name for path in markdown_files if not path.name.isascii() or " " in path.name
    ]
    if invalid_names:
        result.error(
            "Markdown filenames must be ASCII without spaces: "
            + ", ".join(sorted(invalid_names))
        )
    numbered = [path for path in markdown_files if re.match(r"^\d{2,3}_", path.name)]
    if len(numbered) != len(markdown_files):
        missing = sorted(path.name for path in markdown_files if path not in numbered)
        result.error(f"Markdown files without numeric prefix: {', '.join(missing)}")
    prefixes: dict[str, list[str]] = {}
    for path in numbered:
        prefix = path.name.split("_", 1)[0]
        prefixes.setdefault(prefix, []).append(path.name)
    for prefix, names in prefixes.items():
        if len(names) > 1:
            result.error(f"Duplicate numeric prefix {prefix}: {', '.join(sorted(names))}")


def validate_note_types(
    markdown_files: list[Path], result: Result
) -> tuple[list[tuple[Path, dict[str, str], str]], set[str]]:
    parsed: list[tuple[Path, dict[str, str], str]] = []
    found_types: set[str] = set()
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        metadata = parse_frontmatter(text)
        note_type = metadata.get("note_type", "")
        if not note_type:
            result.error(f"{path.name}: missing YAML note_type")
        else:
            found_types.add(note_type)
        if PLACEHOLDER_RE.search(text):
            result.error(f"{path.name}: unresolved template placeholder")
        parsed.append((path, metadata, text))
    missing = REQUIRED_NOTE_TYPES - found_types
    if missing:
        result.error(f"Missing required note types: {', '.join(sorted(missing))}")
    return parsed, found_types


def validate_figures(
    parsed: list[tuple[Path, dict[str, str], str]],
    expected: dict[str, int | None],
    result: Result,
) -> None:
    counts = {"main": 0, "extended": 0, "supplementary": 0}
    for path, metadata, text in parsed:
        if metadata.get("note_type") != "figure":
            continue
        figure_class = metadata.get("figure_class", "")
        if figure_class not in counts:
            result.error(f"{path.name}: invalid figure_class '{figure_class}'")
            continue
        counts[figure_class] += 1
        missing_headings = sorted(
            heading for heading in FIGURE_REQUIRED_HEADINGS if heading not in text
        )
        if missing_headings:
            result.error(
                f"{path.name}: missing Figure sections: {', '.join(missing_headings)}"
            )
        image_targets = [
            target
            for target in MARKDOWN_LINK_RE.findall(text)
            if re.search(r"\.(png|jpe?g|webp|tiff?)$", target, re.IGNORECASE)
        ]
        if not image_targets:
            result.error(f"{path.name}: no figure image embedded")
        elif not any(target.replace("\\", "/").startswith("assets/") for target in image_targets):
            result.error(f"{path.name}: figure image must be stored under assets/")
        if not re.search(r"^### Panel\s+\S+", text, re.MULTILINE):
            result.error(f"{path.name}: no panel-level subsection found")

    for figure_class, expected_count in expected.items():
        if expected_count is not None and counts[figure_class] != expected_count:
            result.error(
                f"{figure_class} Figure count mismatch: "
                f"expected {expected_count}, found {counts[figure_class]}"
            )
    print(
        "Figure notes: "
        f"main={counts['main']}, extended={counts['extended']}, "
        f"supplementary={counts['supplementary']}"
    )


def validate_index(root: Path, markdown_files: list[Path], result: Result) -> None:
    index = root / "00_Index.md"
    if not index.exists():
        result.error("Missing 00_Index.md")
        return
    text = index.read_text(encoding="utf-8")
    linked = {
        target.replace("\\", "/").rsplit("/", 1)[-1].removesuffix(".md")
        for target in WIKI_LINK_RE.findall(text)
    }
    expected = {path.stem for path in markdown_files if path != index}
    missing = sorted(expected - linked)
    if missing:
        result.error(f"00_Index.md does not link notes: {', '.join(missing)}")


def validate_assets(root: Path, parsed: list[tuple[Path, dict[str, str], str]], result: Result) -> None:
    assets = root / "assets"
    if not assets.is_dir():
        result.error("Missing assets/ directory")
        return
    referenced: set[Path] = set()
    for source, _, text in parsed:
        for target in MARKDOWN_LINK_RE.findall(text):
            resolved = resolve_local_link(root, source, target)
            if resolved is not None and assets.resolve() in resolved.parents:
                referenced.add(resolved)
    image_files = {
        path.resolve()
        for path in assets.iterdir()
        if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES
    }
    for path in sorted(image_files):
        if not path.name.isascii() or " " in path.name:
            result.error(f"Asset filename must be ASCII without spaces: {path.name}")
        if path.stat().st_size == 0:
            result.error(f"Empty image asset: assets/{path.name}")
        if not has_valid_image_signature(path):
            result.error(f"Invalid image signature: assets/{path.name}")
        dimensions = png_dimensions(path)
        if dimensions is not None and dimensions[0] < 900:
            result.warn(
                f"Potentially low-resolution Figure asset: assets/{path.name} "
                f"({dimensions[0]}x{dimensions[1]})"
            )

    for source, _, text in parsed:
        for alt_text, target in IMAGE_LINK_RE.findall(text):
            if not alt_text.strip():
                result.error(f"{source.name}: image alt text is empty -> {target}")
            normalized = target.replace("\\", "/")
            if not normalized.startswith("assets/"):
                result.error(f"{source.name}: image must be under assets/ -> {target}")

    for path in sorted(image_files - referenced):
        result.warn(f"Unreferenced asset: assets/{path.name}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paper_folder", type=Path)
    parser.add_argument("--expected-main", type=int)
    parser.add_argument("--expected-extended", type=int)
    parser.add_argument("--expected-supplementary", type=int)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = args.paper_folder.resolve()
    result = Result()
    if not root.is_dir():
        print(f"ERROR: paper folder not found: {root}", file=sys.stderr)
        return 2

    markdown_files = sorted(root.glob("*.md"))
    if not markdown_files:
        print(f"ERROR: no Markdown notes found in {root}", file=sys.stderr)
        return 2

    validate_numbering(markdown_files, result)
    parsed, _ = validate_note_types(markdown_files, result)
    validate_text_integrity(parsed, result)
    validate_links(root, markdown_files, result)
    validate_index(root, markdown_files, result)
    validate_assets(root, parsed, result)
    validate_figures(
        parsed,
        {
            "main": args.expected_main,
            "extended": args.expected_extended,
            "supplementary": args.expected_supplementary,
        },
        result,
    )

    print(f"Markdown notes: {len(markdown_files)}")
    print(f"Errors: {len(result.errors)}")
    for message in result.errors:
        print(f"ERROR: {message}")
    print(f"Warnings: {len(result.warnings)}")
    for message in result.warnings:
        print(f"WARNING: {message}")
    return 1 if result.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
