# Concept and method deep-dive notes

## Contents

1. Selection rules
2. Concept note
3. Method deep-dive
4. Source discipline
5. Linking and duplication control

## Selection rules

Create a separate note only when the term is load-bearing, reused, assumption-critical, easily confused, or directly relevant to the user's research. Prefer one coherent note over several overlapping notes.

Do not create deep notes for:

- a gene mentioned once without interpretive importance;
- standard vocabulary already defined adequately in one sentence;
- a method whose implementation does not affect the paper's claims;
- generic background that cannot be connected to a Figure or conclusion.

## Concept note

Use:

```yaml
---
note_type: concept
concept: ""
aliases: []
introduced_in: []
external_sources: []
---
```

Required sections:

```markdown
[[00_Index|Index]]

# [Concept]

## 30초 설명

[Plain-language definition in two to four sentences.]

## 핵심 원리

[Mechanism, mathematical intuition, biological pathway, or conceptual model.]

## 이 논문에서의 역할

- 어디서 등장하는가:
- 어떤 claim을 이해하게 하는가:
- 저자들이 실제로 측정한 것은 무엇인가:
- 측정하지 않았지만 가정한 것은 무엇인가:

## Figure와 연결

| Figure/panel | 관찰 | 이 개념이 필요한 이유 | 해석 한계 |
|---|---|---|---|

## 혼동하기 쉬운 개념과 비교

| Concept A | Concept B | 핵심 차이 | 이 논문에서 중요한 이유 |
|---|---|---|---|

## 우리 연구에 적용

- 가능한 분석/실험:
- 필요한 control:
- 실패하거나 오해하기 쉬운 지점:

## 근거와 추가 읽기

- focal paper evidence
- external primary or authoritative source
```

For computational concepts, include input, transformation, output, objective/loss, supervision, and failure mode. For biological concepts, include molecular/cellular mechanism, context dependence, measurement proxy, and causal evidence required.

## Method deep-dive

Use:

```yaml
---
note_type: method
method: ""
introduced_in: []
implementation_status: reported
---
```

Required sections:

```markdown
[[00_Index|Index]]

# Method Deep Dive — [Method]

## 무엇을 해결하는 방법인가

## Input → Processing → Output

## 이 논문에서의 실제 구현

| Parameter | Reported value | Source location | Missing/ambiguous |
|---|---|---|---|

## 왜 이 방법을 선택했는가

## 가정과 failure modes

## Controls and validation

## 대안 방법과 trade-off

## 결과 해석에 미치는 영향

## 우리 연구에서 재현하려면
```

Separate a general explanation from the exact implementation in the paper. Mark every absent parameter as `논문 및 범례에 보고되지 않음`; do not fill gaps with standard defaults.

## Source discipline

- Use the focal paper for paper-specific implementation and claims.
- Use primary papers, official documentation, reporting guidelines, or authoritative databases for external explanation.
- Put direct links near external claims.
- Label inference explicitly.
- Do not silently repair an incorrect citation from the paper.

## Linking and duplication control

- Give a one-sentence definition at first use in Overview or a Figure note.
- Add a wiki link to the deep note.
- Do not repeat the full explanation in several Figure notes.
- In the concept note, link back to every Figure that depends on it.
- If two concepts cannot be separated without duplication, merge them and list aliases.
