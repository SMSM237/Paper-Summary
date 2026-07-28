# Output architecture

## Contents

1. Folder contract
2. Numbering and naming
3. Required note contracts
4. Linking rules
5. Adaptive structures

## Folder contract

Create one self-contained folder per paper:

```text
<first-author>-<year>-<short-title>/
├── assets/
│   ├── figure-01.png
│   ├── figure-02.png
│   ├── extended-data-01.png
│   └── supplementary-figure-01.png
├── 00_Index.md
├── 01_Overview.md
├── 02_Background.md
├── 03_Concept_<topic>.md
├── 04_Methods.md
├── 05_Method_DeepDive_<topic>.md
├── 06_Figure1_<one-sentence-topic-slug>.md
├── 07_Figure2_<one-sentence-topic-slug>.md
├── ...
├── XX_ExtendedData1_<topic>.md
├── XX_SupplementaryFigure1_<topic>.md
├── XX_Critical_Review.md
├── XX_Our_Research_Application.md
├── XX_Reproducibility.md
└── XX_Source_Coverage.md
```

The example numbers show reading order, not fixed positions. A paper with several essential concepts may place multiple `Concept` notes before `Methods`. A method-heavy paper may place several `Method_DeepDive` notes after `Methods`. Keep all numbered notes in one flat folder so the Obsidian file explorer remains scannable. Use only `assets/` as a child folder.

Do not copy the source PDF into the output unless the user asks. Record its absolute source path and access date in `Source_Coverage`.

## Numbering and naming

- Use two-digit prefixes beginning with `00_Index.md`.
- Number files consecutively with no duplicate prefix.
- Use ASCII filenames: letters, digits, underscores, and hyphens.
- Keep Figure numbers identical to the paper.
- Use a meaningful topic slug, not only `Figure1`.
- Preserve stable names after delivery; update links instead of renumbering casually.
- If more than 99 notes are necessary, switch all prefixes to three digits.

Recommended reading order:

1. Index
2. Overview
3. Background
4. load-bearing concepts
5. Methods
6. method deep-dives
7. main figures in order
8. extended and supplementary figures
9. Critical Review
10. Our Research Application
11. Reproducibility
12. Source Coverage

## Required note contracts

Every note begins with YAML frontmatter containing `note_type`. Use:

| Note | `note_type` |
|---|---|
| Index | `index` |
| Overview | `overview` |
| Background | `background` |
| Concept | `concept` |
| Methods overview | `methods` |
| Method Deep-Dive | `method` |
| Figure | `figure` |
| Critical Review | `critical_review` |
| Our Research Application | `research_application` |
| Reproducibility | `reproducibility` |
| Source Coverage | `source_coverage` |

### `00_Index.md`

Include:

- verified citation and DOI;
- one-sentence conclusion;
- five key takeaways;
- study logic chain;
- reading map grouped as `Core`, `Concepts`, `Methods`, `Figures`, and `Evaluation`;
- claim-to-evidence table linking Figure notes;
- concept map linking Concept and Method Deep-Dive notes;
- coverage badge such as `Main 6/6 | Extended 4/5 | Supplementary 8/12`;
- unresolved evidence boundary.

### `01_Overview.md`

Include:

- research question and knowledge gap;
- model/cohort and study design;
- major findings in evidence order;
- claim–evidence map;
- concise strengths, limitations, and bottom line.

Keep this note readable without opening other files. Link rather than duplicate deep explanations.

### `02_Background.md`

Include:

- field context before the paper;
- exact gap addressed;
- competing models or explanations;
- why the selected model/method fits or fails to fit the question;
- links to dedicated concept notes.

Separate external background sources from statements made by the focal paper.

### `Methods`

Include a workflow from sample acquisition to analysis, experimental units, controls, perturbations, endpoints, and a reproducibility table. Link assumption-heavy techniques to Method Deep-Dive notes.

### `Critical_Review`

Organize by design, model validity, measurement, statistics, interpretation, reproducibility, and translational scope. Put claim-changing major comments before generic limitations.

### `Our_Research_Application`

Translate findings to the user's research using Immediate, Conditional, and Strategic tiers. Each proposal must name the experimental unit, controls, readout, value, and risk.

### `Reproducibility`

Extract exact parameters and cite their location. Include `reported`, `ambiguous`, and `not reported` fields. Do not use plausible defaults.

### `Source_Coverage`

Include:

- bibliographic verification source;
- all supplied and retrieved files;
- source/access log;
- figure/table coverage manifest;
- inaccessible items and routes attempted;
- link and image validation results;
- anti-hallucination audit.

## Linking rules

- Add `[[00_Index|Index]]` near the top of every non-index note.
- Link concepts at first substantive use: `[[03_Concept_EMT|EMT]]`.
- Link methods where the readout first depends on them.
- In `00_Index`, link every numbered note exactly once in the primary reading map.
- Use Markdown image links for assets: `![Figure 1](assets/figure-01.png)`.
- Use direct web links for DOI, publisher, repositories, and external references.
- Do not use wiki links for files outside the paper folder.

## Adaptive structures

### Concept-heavy computational paper

Use several early concept notes, for example:

```text
01_Overview
02_GAN_and_cGAN
03_UNet
04_PatchGAN
05_Transformer
06_Modern_Virtual_Staining
07_Methods
08_Figure1_...
```

### Phenotype-first biological paper

Keep background and methods early, then follow the experimental narrative:

```text
01_Overview
02_Background
03_Methods
04_Figure1_Phenotypic_Landscape
05_Figure2_RXR_Mechanism
06_Figure3_RNase_InVivo
07_Method_DeepDive_RNase_Assay
```

Choose the order that best supports reading, while retaining all required note types and exact Figure order.
