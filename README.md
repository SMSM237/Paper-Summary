# Paper Summary

`paper-summary` turns a scientific paper and its supplementary material into a Korean-led, Obsidian-compatible multi-note knowledge package.

## Version 2 workflow

- One self-contained folder per paper
- Numbered Overview, Background, Methods, Figure, Concept, Review, Application, Reproducibility, and Coverage notes
- One detailed note per reviewed Figure
- Panel-level purpose, design, observation, statistics, interpretation, limitation, and panel-to-panel logic
- Dedicated concept and method deep-dives linked from the Figures that require them
- PDF-derived figure crops under `assets/`
- UTF-8/NFC, MathJax, table escaping, image-format, and link-integrity safeguards
- Deterministic package validation with `scripts/validate_report_package.py`

Invoke it with:

```text
Use $paper-summary to turn this paper into a structured Obsidian paper atlas.
```
