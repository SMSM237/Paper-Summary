# Markdown integrity

## Contents

1. Encoding and filenames
2. Scientific text
3. MathJax equations
4. Tables
5. Figures and captions
6. Links and Obsidian compatibility
7. Render validation

## Encoding and filenames

- Save every Markdown file as UTF-8 without lossy conversion.
- Normalize Unicode text to NFC.
- Reject the Unicode replacement character `�`, NUL bytes, and obvious mojibake.
- Use ASCII filenames without spaces for notes and assets.
- Preserve Korean and scientific symbols inside file contents, not filenames.
- Quote YAML values containing `:`, `#`, brackets, or leading special characters.

Do not trust text extraction that produces garbled units or symbols. Cross-check the rendered PDF. If the exact character remains uncertain, state `PDF 해상도에서 판독 불가`.

## Scientific text

- Keep gene/protein names, Greek letters, superscripts, subscripts, and units faithful to the source.
- Use Unicode only for stable prose symbols such as `µm`, `±`, `≤`, `≥`, `α`, and `β`.
- Use MathJax when symbol grouping or sub/superscripts affect meaning: `$IC_{50}$`, `$R^2$`, `$10^6$ cells/mL`.
- Put literal filenames, commands, package names, and code tokens in backticks.
- Escape literal Markdown control characters when they are not syntax: `\*`, `\_`, `\#`, `\[`, `\]`.
- Write literal comparison signs as prose or math. Avoid raw `<text>` constructs that could be parsed as HTML tags.
- Do not paste soft hyphens, zero-width spaces, ligatures, or PDF line-break hyphenation into scientific terms.

## MathJax equations

Use Obsidian-compatible MathJax delimiters:

- inline: `$y = ax + b$`
- block:

```text
$$
y = ax + b
$$
```

Rules:

- Balance every `$` and `$$`.
- Do not use `\(...\)` or `\[...\]` delimiters.
- Keep punctuation outside display equations when practical.
- Do not place complex display equations inside Markdown tables.
- Escape literal currency dollar signs as `\$`.
- Preserve `\mathrm{}`, `\text{}`, subscripts, superscripts, fractions, and Greek symbols exactly.
- Do not infer a missing exponent, sign, denominator, or Greek letter from context.
- If OCR and the rendered equation disagree, trust the visually inspected source.
- When transcription is unsafe, embed a high-resolution equation crop and explain the unresolved symbol.

## Tables

- Use a consistent number of columns in every row.
- Escape a literal pipe inside a cell as `\|`.
- Use `<br>` only for deliberate line breaks inside a cell.
- Keep multi-paragraph interpretation outside tables.
- Move long equations, nested lists, and large citations below the table.
- Avoid raw line breaks inside a cell.
- Do not use tabs for alignment.

## Figures and captions

- Store images only under `assets/`.
- Use ASCII lowercase filenames without spaces, for example `figure-03-panel-c-detail.png`.
- Prefer PNG for PDF-derived plots, microscopy, diagrams, and text-heavy figures.
- Convert to RGB or RGBA; avoid CMYK-only images.
- Render at a resolution where the smallest relevant label and scale bar remain readable. Split a dense Figure into overview and detail crops when necessary.
- Never stretch an image by changing only one dimension.
- Use meaningful alt text: `![Figure 3 — CAF-induced invasion](assets/figure-03.png)`.
- Put the caption and interpretation in normal Markdown below the image, not inside HTML or a table.
- Preserve the scientific image content. Cropping, resolution conversion, and lossless format conversion are allowed; recolouring, redrawing, and content-aware edits are not.

## Links and Obsidian compatibility

- Use wiki links for local notes: `[[04_Methods|Methods]]`.
- Use Markdown links for images and external URLs.
- Match filename case exactly even on Windows.
- Keep anchors simple; prefer linking to the note rather than a fragile translated heading anchor.
- Avoid absolute local paths inside the saved package.
- Do not use `file://`, base64 data URIs, or viewer-specific links.
- Verify every local note and image link after the final renumbering.

## Render validation

Before delivery:

1. Run `scripts/validate_report_package.py`.
2. Render or preview `00_Index.md`.
3. Render or preview the most complex Figure note.
4. Render or preview one note containing equations, one wide table, and Korean/English mixed text.
5. Check that formulas, table columns, wiki links, image captions, panel labels, superscripts/subscripts, and special units display correctly.
6. Re-run validation after any filename or numbering change.

If no Obsidian-compatible renderer is available, report that visual rendering remains unverified; a successful static validator alone is not equivalent to a render check.
