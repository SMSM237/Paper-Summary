---
name: paper-summary
description: Build a rigorous Korean-led Obsidian knowledge package for a scientific paper, organized as linked multi-note files with verified metadata, dedicated background and methods notes, concept and method deep-dives, one detailed note per main/extended/supplementary figure, panel-by-panel interpretation, reproducibility audit, critical review, and research applications. Use when asked to summarize, explain, critically evaluate, or organize biomedical, life-science, clinical, organoid, MPS, drug-response, imaging, AI, or multi-omics papers from PDFs, links, or supplementary materials.
---

# Paper Summary

Create a source-grounded **paper atlas**, not one long abstract-like summary. Make the result useful at two scales: a fast overview and a linked knowledge base that supports deep reading.

Use Korean for substantive explanation. Retain precise English terminology for genes, proteins, drugs, assays, algorithms, statistics, and figure labels. Separate direct observation, author interpretation, reviewer inference, and unverified hypothesis.

## Read the required references

Before creating output:

1. Read [references/output-architecture.md](references/output-architecture.md) completely.
2. Read [references/figure-note-schema.md](references/figure-note-schema.md) completely whenever the paper contains figures.
3. Read [references/concept-method-notes.md](references/concept-method-notes.md) completely whenever load-bearing concepts or methods require dedicated notes.
4. Read [references/markdown-integrity.md](references/markdown-integrity.md) completely for every saved Markdown package.

## Establish the evidence boundary

1. Inventory the main PDF, supplements, extended data, tables, data/code links, DOI, and user research context.
2. Identify title, authors, journal, year, DOI, and article type from the paper itself.
3. Verify bibliographic metadata against the publisher or journal page; use DOI/Crossref, PubMed, PMC/Europe PMC, or an institutional record only as needed.
4. Build a coverage manifest before writing: every main, extended-data, and supplementary figure/table must be listed as `reviewed`, `unavailable`, `unreadable`, or `not applicable`.
5. State unavailable evidence and its impact. Never imply that an inaccessible supplement was reviewed.

Use the PDF skill for extraction, rendering, and visual inspection when available. Inspect the actual panels, axes, scale bars, group labels, legends, and statistical annotations. Text extraction and OCR support inspection but do not replace it.

## Reconstruct the paper before splitting notes

Build a private evidence map first:

`knowledge gap -> question/hypothesis -> model/cohort -> observation -> mechanism candidate -> perturbation/validation -> implication`

Record:

- biological and computational unit of analysis;
- patient/donor/model count separately from devices, wells, images, cells, fields, and technical repeats;
- controls, perturbations, endpoints, and time points;
- which claims are observation, association, functional evidence, causal evidence, independent replication, or clinical validation;
- which concepts and methods are prerequisites for understanding the results.

Use calibrated language:

- **보여준다**: directly measured.
- **지지한다**: convergent evidence is consistent with the claim.
- **시사한다**: plausible but not directly established.
- **저자들은 제안한다**: interpretation extends beyond direct evidence.

## Create a multi-note paper atlas

Create one folder per paper. Do not default to a single monolithic Markdown file.

- Put numbered Markdown notes in the paper folder.
- Put PDF-derived figure crops only in `assets/`.
- Create `00_Index.md` as the navigation hub.
- Create separate Overview, Background, Methods, Figure, Critical Review, Research Application, Reproducibility, and Source/Coverage notes.
- Create concept or method deep-dive notes only when they materially improve understanding; do not create a note for every gene or acronym.
- Assign numeric prefixes by reading order, not by a rigid universal count.
- Use ASCII filenames and concise topic slugs; Korean prose may remain inside the notes.
- Connect related notes with Obsidian wiki links and include backlinks to `[[00_Index]]`.
- Write UTF-8 Markdown that obeys the MathJax, escaping, image, and filename rules in `references/markdown-integrity.md`.

Follow the exact architecture and naming rules in `references/output-architecture.md`.

## Promote concepts into deep-dive notes

Create a dedicated concept note when at least one condition holds:

1. The concept is load-bearing for a central claim.
2. It appears in multiple figures or sections.
3. Misunderstanding it would change interpretation.
4. It is directly relevant to the user's research.
5. It requires external background beyond what the paper explains.

Examples include EMT, MSI, antibody–drug conjugate bystander effect, cGAN versus GAN, U-Net, spatial transcriptomics, hazard ratio, organ-on-chip shear stress, or ECM stiffness.

Introduce the concept briefly at first use and link to the deep note. In the deep note, explain definition, mechanism or algorithm, role in this paper, evidence locations, assumptions, common confusions, limits, and research relevance. Cite external primary or authoritative sources separately from the focal paper.

Do not use a concept note to inflate the report. Merge overlapping terms and keep project-specific interpretation traceable to the paper.

## Treat each figure as a self-contained scientific argument

Create one note for every reviewed main figure. Create one note for each reviewed extended or supplementary figure unless the user explicitly requests a shorter appendix.

For each figure:

1. Capture the original figure from the PDF at readable resolution and save it under `assets/`.
2. Place the image near the top of the figure note.
3. State one Korean sentence that identifies the figure's scientific topic and its role in the paper.
4. Explain why the figure appears at this point in the argument.
5. Analyze every labelled panel and meaningful subpanel.
6. Describe the panel's question, model/sample, condition/control, measurement, visual encoding, direct observation, justified interpretation, statistics, limitation, and transition to the next panel.
7. Explain the panel-to-panel logic rather than listing panels independently.
8. End with what the figure establishes, supports only partially, and does not establish.
9. Link prerequisite concept and method notes.

Use the complete schema in `references/figure-note-schema.md`. A phrase such as “패널 a는 실험 모식도다” is insufficient unless followed by what is being compared, why that design is necessary, and how it frames the later panels.

Treat representative images as illustrative unless suitable independent quantification accompanies them. If a label or statistic is unreadable, mark it as such instead of reconstructing it.

When a formula cannot be transcribed reliably, preserve it as a readable PDF-derived crop and mark the transcription as unresolved. Never replace an unreadable symbol with a plausible one.

## Separate Methods overview from method deep-dives

In the Methods note, reconstruct the full experimental workflow and extract reproducibility-critical details:

- cohort/model and inclusion/exclusion;
- matrix/substrate/device material and geometry;
- cell source, seeding density, medium, exposure, drug concentration, and time;
- controls and perturbations;
- imaging/assay settings, markers, preprocessing, software, and versions;
- statistics, batch handling, missing data, repositories, and code.

Create a method deep-dive for a technique whose assumptions determine interpretation, such as RNAscope, scRNA-seq integration, cGAN, U-Net, spatial deconvolution, dose-response modeling, or vascular perfusion measurement. Follow `references/concept-method-notes.md`.

Mark missing details as `논문 및 범례에 보고되지 않음`.

## Critique and connect without overclaiming

In `Critical_Review`, prioritize claim-changing issues. For each major issue state:

- why it matters;
- what the current data establish;
- the minimum decisive experiment or analysis;
- how positive and negative outcomes would change interpretation;
- priority: required, recommended, or optional.

In `Our_Research_Application`, separate:

- **Immediate**: feasible with existing data/materials;
- **Conditional**: needs a new assay, cohort, collaboration, or device redesign;
- **Strategic**: future validation or precision-medicine program.

For each proposal specify question, samples/data, experimental unit, design, controls, readout, scientific value, main risk, and sensible manuscript figure placement. Do not infer IC50 from single-point data or mechanism from association alone.

## Validate before delivery

Run:

```text
python scripts/validate_report_package.py <paper-folder> --expected-main N --expected-extended N --expected-supplementary N
```

Use only counts that were established by the coverage manifest. Fix every validation error. Review warnings and either resolve them or disclose why they remain.

Then verify manually:

- `00_Index.md` links to every note in reading order;
- every reviewed figure has the correct PDF-derived capture;
- every panel label in the source has a corresponding explanation;
- concept links resolve and essential definitions remain understandable at first use;
- claims, numbers, conditions, and DOI are directly supported;
- the true experimental unit is not replaced by nested observations;
- the Core notes remain useful without opening every deep-dive;
- the source/coverage note reports exact reviewed and unavailable counts.
- Markdown files decode as UTF-8 without replacement characters and are NFC-normalized;
- inline and block MathJax delimiters are balanced;
- table pipes, underscores, angle brackets, and backslashes are escaped or placed in code/math contexts correctly;
- image names are ASCII without spaces, every image has useful alt text, and every image link resolves with exact filename case;
- final Index, one concept/method note, and at least one dense Figure note render correctly in an Obsidian-compatible preview.

Deliver the paper folder path, the Index path, validation result, coverage counts, and unresolved limitations.
