---
name: paper-summary
description: Produce a rigorous, readable Korean-first review of a scientific paper PDF, with verified bibliographic metadata and DOI, direct figure and panel interpretation, supplementary-material retrieval, methods extraction, translational relevance, and peer-review critique. Use when asked to summarize, explain, critically evaluate, or connect biomedical, life-science, clinical, organoid, MPS, drug-response, or multi-omics papers to ongoing research.
---

# Paper Summary

Create a source-grounded reading report, not a paraphrase of the abstract. Preserve the distinction between what the data show, what the authors infer, and what remains unproven. Default to Korean when the request is Korean; preserve technical terms in English where that improves precision.

## Start with inputs and scope

1. Inventory every supplied item: main PDF, supplementary PDF, extended-data PDF, supplementary tables/data, DOI/link, and user research context. Record the filenames and access date in the report.
2. Identify the paper from PDF metadata and the first pages: title, authors, journal, year, and any DOI string. Confirm the identity with the title and author list before searching externally.
3. Verify bibliographic metadata and DOI from the most authoritative available source, preferring the publisher or journal page, then DOI resolution/Crossref, PubMed, PMC/Europe PMC, or a trusted institutional record. Never invent a DOI. If sources disagree, report the discrepancy and use the publisher record as the primary reference when available.
4. List every main, extended-data, and supplementary figure/table mentioned in the paper before analysis. This is the coverage checklist.
5. State the analysis boundary up front: materials reviewed, materials unavailable, and any figure or page whose resolution prevents reliable reading.

Use the PDF skill for text extraction, rendering, and visual checks when it is available. Read the actual figure pages at sufficient resolution; legends, OCR, and extracted text are aids rather than substitutes for inspecting panels, axes, scale bars, labels, images, and statistical annotations.

## Retrieve supplementary material deliberately

When supplementary material is not supplied, attempt legitimate public routes in this order, documenting each successful or failed route:

1. Publisher/journal article page and its supplementary/extended-data links.
2. The DOI landing page and journal-hosted asset links.
3. PMC or Europe PMC full text and associated files.
4. Preprint servers, institutional repositories, or an openly available author manuscript.
5. Public data/accession repositories explicitly cited in the paper.

Download and analyze public supplementary PDFs, figures, tables, and data that are relevant and accessible. Do not bypass paywalls, access controls, or terms of use. If material remains unavailable, list: item, routes tried, outcome, and which conclusions cannot be checked without it. Do not claim that unavailable supplementary data were reviewed.

## Use resilient document inspection

Do not stop at the first parser failure. Use only the methods needed to resolve a real problem, and log the method that produced the usable evidence.

| Problem | Escalation path |
|---|---|
| Text extraction fails | Try a second PDF parser; inspect embedded metadata; render relevant pages; use OCR on rendered pages. |
| Figures are unclear | Render the original page at higher resolution; crop/zoom the panel; compare with legend and Results text. |
| DOI is missing | Search exact title plus first/last author; search title variants and journal/year; query trusted bibliographic indexes. |
| Supplement links fail | Recheck the publisher record, DOI page, PMC/Europe PMC, preprint/repository records, and cited accessions. |
| Panel labels or statistics remain unreadable | State the limitation exactly; do not reconstruct labels or numbers from context. |

When a conclusion depends on an unresolved item, downgrade the claim rather than filling the gap with plausible detail.

## Analyze the paper in evidence order

### 1. Reconstruct the study logic

Identify the knowledge gap, hypothesis, biological/clinical question, samples and models, controls, cohort design, assays, endpoints, and causal chain. Express the chain compactly:

`question → model/cohort → observation → mechanism candidate → perturbation/validation → translational implication`

Evaluate model fitness for the question. Distinguish tumour-intrinsic effects from microenvironment-, immune-, vascular-, or pharmacokinetic-dependent effects. For patient-derived systems, keep patient count, model count, technical replicate count, and independent validation cohorts separate.

### 2. Build claim-to-evidence links

For every major conclusion, map the direct data, figure(s), evidence level, and caveat. Use these calibrated terms consistently:

- **shows**: directly measured in the reported data.
- **supports**: convergent evidence is consistent with the conclusion.
- **suggests**: plausible but not directly established.
- **authors propose**: interpretation exceeds, or is not fully matched by, the direct evidence.

Classify support as descriptive observation, association, functional association, causal evidence, independent replication, or clinical validation. Correlation, expression association, and a single model should not be represented as mechanism or general clinical utility.

### 3. Read every figure as an argument

For each main figure, and for extended/supplementary figures when available, follow the embedded report template below. Start with one sentence that says what the figure establishes and how it advances the whole paper.

For each panel, identify purpose, experimental system and condition, measurement, axes/scale/colours/groups, direct observation, author interpretation, justified inference, limitation, and transition to the next panel. Then explicitly explain how the panels combine into the figure-level conclusion. Treat representative images as illustrative unless independently quantified with suitable sampling and replication.

Place a short **Important concept** note immediately after the first result whose interpretation requires it. Give the definition, the paper-specific role, and the key interpretive caution. Maintain a compact concept index only as a navigation aid; do not make readers search the document for essential definitions.

### 4. Check statistics, reproducibility, and methods

Assess the unit of analysis, biological versus technical replicates, `n` definition, controls, randomization/blinding where relevant, effect size and uncertainty, individual data display, test selection, multiple-testing control, pre-specified thresholds, missing-data handling, batch effects, and external validation. Do not condemn a study merely for a modest sample size; judge adequacy against the biological unit, effect size, and stated claim.

Extract reproducibility-critical details without guessing: models/patients, inclusion/exclusion, culture matrix and medium, seeding density, drugs and concentrations, exposure time, assay endpoint, imaging and antibody/marker settings, preprocessing and software, statistics, repository accessions, and code/data availability. Mark absent information as `미기재`.

### 5. Translate, critique, and propose

Connect findings only when scientifically justified to the user's work in large patient cohorts, organoids/PDC/PDO, MPS, in-vitro drug screening, multi-omics/spatial analysis, ADCs, and immunotherapy. Separate:

- **Immediate**: analyses or readouts feasible with existing data/materials.
- **Conditional**: work needing a new assay, cohort, collaboration, or MPS redesign.
- **Strategic**: a future biomarker, validation, or precision-oncology programme.

For a relevant proposal specify question, samples/data, design, controls, expected readout, scientific value, primary risk, and a sensible manuscript figure location. In drug studies, do not infer IC50 from a single concentration; specify whether evidence is single-point, dose-response, time course, or combination-matrix based. In multi-omics/spatial work, label associations as associations unless perturbation or an appropriate causal design supports more.

Write a reviewer-style assessment with major comments first. Each major comment must contain: the issue, why it matters to the central claim, what the current data establish, the minimum decisive experiment/analysis, and how possible outcomes would change interpretation. Prioritize each request as required, recommended, or optional. Give an editorial assessment only after showing its evidence basis.

## Write for two reading depths

Use the YAML frontmatter and full reporting structure embedded below. Keep the report navigable:

1. **Core**: title/metadata, one-sentence conclusion, five key takeaways, study logic, claim–evidence table, and concise verdict.
2. **Deep dive**: figure-by-figure and panel-by-panel interpretation, concepts placed in context, application ideas, and critical review.
3. **Appendix**: methods/reproducibility extraction, statistics detail, concept index, source/access log, and coverage audit.

Put the conclusion before detail. Use tables for repeated fields, bullets for decision points, and nested headings or `<details>` for panel-level depth. Remove duplicated explanations; link back to an earlier concept rather than redefining it. A long paper may require a long appendix, but the Core should remain independently intelligible.

## Mandatory final quality gate

Before delivering, verify and report:

- Bibliographic metadata and DOI were checked against a cited trustworthy source, or are explicitly unresolved.
- Main, extended, and supplementary figures/tables were inventoried; each item is marked reviewed, unavailable, or not applicable.
- Every reported figure has a one-sentence message, panel interpretation, panel-to-panel logic, and stated evidence boundary.
- Concepts appear next to the conclusion they enable.
- Claims, author interpretation, and reviewer inference are visibly separated.
- Quantitative details, labels, and experimental conditions were not fabricated.
- Supplementary retrieval attempts and access limitations are recorded.
- Research connections and proposed experiments are proportional to the actual evidence.
- The report includes a figure-coverage count, such as `Main 6/6; Extended Data 4/5; Supplementary 8/12`, with reasons for omissions.

## Output and citation rules

Use an Obsidian-compatible Markdown file with YAML frontmatter. Cite the paper and external metadata/supplement sources as direct links near the relevant claim. Clearly distinguish information obtained from the paper from external context. Use the following explicit uncertainty labels where appropriate: `PDF 해상도로 인해 판독 불가`, `본문 또는 범례에 미기재`, `보충자료 공개 접근 불가`, and `저자 설명을 바탕으로 한 해석`.

## Embedded report template

Use this template for the output report. Omit a section only when it is genuinely inapplicable, and state why. Keep the **Core** readable without opening the deeper sections.

```yaml
---
title: ""
authors: []
journal: ""
year:
doi: ""
paper_type: []
cancer_type: []
model_system: []
data_types: []
key_topics: []
materials_reviewed: []
materials_unavailable: []
review_status: completed
tags:
  - paper-summary
  - literature-review
---
```

### Core

#### 1. Paper at a glance

| Field | Verified information |
|---|---|
| Title / authors / journal / year | |
| DOI and verification source | |
| Study type / disease / model | |
| Materials reviewed | |
| Materials unavailable and impact | |

#### 2. One-sentence conclusion

> **This paper shows/supports/suggests that [system] [main finding], with [biological, clinical, or technical implication].**

#### 3. Five things to remember

1. Core discovery.
2. Strongest evidence.
3. Key mechanism or biological interpretation.
4. Main limitation.
5. Most actionable research connection.

#### 4. Research question and logic

- **Knowledge gap / hypothesis:**
- **Study design:**
- **Causal chain:** question → model/cohort → observation → validation → implication
- **Model-fit assessment:** what is captured, absent, and not distinguishable.

#### 5. Claim–evidence map

| Major claim | Direct evidence | Figure(s) | Evidence level | Boundary / caveat |
|---|---|---|---|---|
| | | | observation / association / functional / causal / replication / clinical | |

#### 6. Bottom line

> **[Major value], but [main limitation]; interpret the central claim as extending no further than [supported scope].**

### Deep dive

#### 7. Figure-by-figure analysis

Repeat for every reviewed main, extended, and supplementary figure.

##### Figure X — [short title]

**One-sentence message:** Figure X [does what] and therefore [supports which part of the paper's argument].

**Role in the paper:** discovery / model validation / mechanism / functional causality / clinical link / generalization.

| Panel | Purpose and design | Direct observation | Interpretation and evidence boundary | Link to next panel |
|---|---|---|---|---|
| X-a | model, condition, readout, axes/scale | | author interpretation; justified inference; limitation | |

**Panel-to-panel logic:** Explain how the ordered evidence arrives at the figure conclusion.

**Statistics and visual evidence:** `n` unit, biological/technical replicates, test, correction, effect/uncertainty, image quantification, and unresolved details.

**Figure conclusion:** What this figure establishes; what it supports only partially; what it does not establish.

> **Important concept — [term]:** Definition; role in this paper; interpretive caution.

#### 8. Relevance to ongoing research

| Priority | Opportunity | Question / design / controls | Needed samples or data | Readout and value | Risk / boundary |
|---|---|---|---|---|---|
| Immediate / Conditional / Strategic | cohort, PDO/PDC, MPS, screening, multi-omics/spatial, ADC, immunotherapy | | | | |

#### 9. Strengths and limitations

Separate design, model, analysis/statistics, interpretation, and reproducibility limitations. Identify evidence rather than relying on generic criticism.

#### 10. Peer-review assessment and revision plan

**Overall assessment:** novelty, completeness, claim-evidence alignment, likely impact, and editorial judgement.

##### Major comments

1. **Issue:**
   - **Why it matters:**
   - **What current data establish:**
   - **Minimum decisive revision:**
   - **Interpretation if positive/negative:**
   - **Priority:** required / recommended / optional

##### Minor comments

- Statistics, labels, terminology, legends, reporting, or supplementary placement.

#### 11. Additional experiments or analyses

| Priority | Claim tested | Design and controls | Expected readout | Interpretation by outcome | Feasibility |
|---|---|---|---|---|---|

### Appendix

#### A. Reproducibility extraction

| Category | Reported detail | Source location | Missing or ambiguous information |
|---|---|---|---|
| Cohort/model | | | |
| Culture and matrix | | | |
| Drug and exposure | | | |
| Assay/imaging/markers | | | |
| Analysis software/statistics | | | |
| Data/code/accession | | | |

#### B. Statistics and reproducibility audit

- Unit of analysis and independence:
- Replicate structure and `n` definition:
- Control, blinding/randomization, missing data, batch handling:
- Multiple testing and threshold choice:
- Data/code/material availability:

#### C. Important concept index

| Concept | Where introduced | Paper-specific meaning and caution |
|---|---|---|

#### D. Source and access log

| Item | Source or route | Status | What it enabled or limited |
|---|---|---|---|
| DOI metadata | publisher / DOI / Crossref / PubMed | verified / unresolved | |
| Supplementary PDF / table / data | routes attempted | reviewed / unavailable | |

#### E. Coverage audit

| Material class | Found | Reviewed | Unavailable / unreadable | Reason |
|---|---:|---:|---:|---|
| Main figures | | | | |
| Extended Data | | | | |
| Supplementary figures | | | | |
| Supplementary tables/data | | | | |

**Final anti-hallucination check:** Do not state any panel, value, label, experimental condition, DOI, or supplementary item as verified unless directly observed in the paper/material or supported by the cited metadata source.
