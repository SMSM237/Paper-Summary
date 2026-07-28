# Figure note schema

## Contents

1. Frontmatter
2. Required section order
3. Panel analysis standard
4. Composite panels
5. Statistical and visual audit
6. Evidence boundaries

## Frontmatter

Use:

```yaml
---
note_type: figure
figure_id: "Figure 1"
figure_class: main
source_pages: [4]
source_file: "paper.pdf"
review_status: reviewed
linked_concepts: []
linked_methods: []
---
```

Allowed `figure_class` values are `main`, `extended`, and `supplementary`.

## Required section order

```markdown
[[00_Index|Index]]

# Figure 1 — [scientific topic]

![Figure 1](assets/figure-01.png)

## 한 문장 주제

> Figure 1은 [핵심 관찰]을 보여주며, 이를 통해 [논문 전체 주장 중 역할]을 지지한다.

## 논문에서의 역할

- 단계: model validation / discovery / mechanism / perturbation / generalization / clinical link
- 앞 Figure 또는 질문에서 넘어온 이유:
- 다음 Figure에 넘기는 미해결 질문:

## 패널 구성 지도

| Panel | 핵심 질문 | System/condition | Readout | 논리적 역할 |
|---|---|---|---|---|

## 패널별 상세 해설

### Panel a — [panel-specific title]

- **목적:**
- **모델·표본·조건:** biological unit와 control을 포함한다.
- **무엇을 측정했는가:** assay, marker, axes, colour, scale bar, time point를 기록한다.
- **직접 관찰:** 이미지나 수치에서 실제로 읽히는 결과만 쓴다.
- **저자 해석:** 저자가 주장한 의미를 구분한다.
- **정당화되는 해석:** 관찰이 허용하는 범위로 보정한다.
- **통계·반복:** `n`의 단위, biological/technical replicate, test, correction, uncertainty를 기록한다.
- **한계·대안 설명:** 해당 panel만으로 배제되지 않는 설명을 적는다.
- **다음 panel로의 연결:** 왜 다음 증거가 필요한지 설명한다.

## 패널 간 논리

[a가 설계를 정의하고 -> b가 현상을 보여주고 -> c가 정량화하고 -> d가 perturbation으로 검증한다]처럼 순서를 논증으로 재구성한다.

## 통계와 시각 증거

- 분석 단위와 독립성:
- representative image와 정량화의 관계:
- effect size와 uncertainty:
- test와 multiple-comparison control:
- 읽을 수 없거나 보고되지 않은 정보:

## 이 Figure가 확립하는 것

- **확립한다:**
- **부분적으로 지지한다:**
- **확립하지 않는다:**

## 연결 개념과 방법

- 개념:
- 방법:

## 우리 연구에서의 의미

- 바로 가져올 수 있는 readout 또는 design:
- 그대로 적용하면 위험한 부분:

## 한계

[figure-specific limitation과 paper-level limitation을 구분한다.]
```

## Panel analysis standard

For every labelled panel:

1. Identify the question, not only the graphic type.
2. Identify sample/model, treatment, control, and time.
3. Decode axes, colours, symbols, scale, normalization, and units.
4. State the direct observation before interpretation.
5. Name the biological or computational unit represented by `n`.
6. Explain whether the panel is representative, quantified, replicated, or externally validated.
7. State what ambiguity remains.
8. Explain why the next panel follows.

Use one or more paragraphs after the bullets when mechanism or design requires deeper explanation. Tables are navigation aids, not substitutes for prose.

## Composite panels

If a panel contains multiple images or plots:

- describe each meaningful subpanel in display order;
- distinguish overview, zoom, overlay, quantification, and validation views;
- preserve channel names, colour mapping, scale bars, and time points;
- explain whether images and quantification come from the same experimental unit;
- split the figure capture into readable crops when labels are too small.

Do not invent subpanel labels that are not present in the source.

## Statistical and visual audit

Record:

- exact `n` and its unit;
- patient/donor/model count separately from cells, fields, sections, wells, and devices;
- paired/repeated versus independent design;
- central tendency and uncertainty;
- individual data visibility;
- statistical test, sidedness, correction, and threshold;
- whether assumptions or effect sizes were reported;
- image sampling, segmentation, normalization, and exclusion where relevant.

For nested measurements, explicitly state the nesting and whether the analysis accounts for it.

## Evidence boundaries

Use:

- `PDF 해상도에서 판독 불가`
- `본문·Methods·범례에 보고되지 않음`
- `저자 설명에 기반한 해석`
- `대표 이미지이며 독립 정량 근거는 제한적`
- `연관성은 지지하지만 인과성은 확립하지 않음`
- `단일 환자/모델에서의 proof-of-concept`

Never upgrade a panel from association to mechanism because it visually fits the proposed model.
