---
name: brainstorm
description: >
  Brainstorm the intervention — map the whole solution space before committing to one
  approach. Generates ~10 candidate interventions spread across a time/effort horizon,
  with impact, risk, and a selection UI that assembles picks into a structured next
  step. This skill should be used when the user says "브레인스토밍", "해법 후보 펼쳐줘",
  "뭘 해야 할지 모르겠어", "옵션 보여줘", "brainstorm interventions", or names a problem
  (churn, slow builds, flaky tests, low conversion) without having chosen an approach.
argument-hint: "<해결하려는 문제> [제약: 기간/인력/비용]"
---

# Brainstorm — 해법 공간 지도 (Brainstorm the Intervention)

문제를 받자마자 첫 해법을 구현하면 **해법 공간의 나머지가 전부 unknown**으로 남는다.
원문 "Brainstorm the Intervention": 이탈(churn) 문제에 대해 즉시 적용부터 분기 단위
베팅까지 10개 전략을 타임라인에 펼치고, 공감(resonate) 체크가 구조화된 응답으로
조립되게 했다. 선택은 사용자가 하고, 모델은 공간을 그린다.

## 철칙

1. **아직 아무것도 구현하지 마라.** 이 스킬의 산출물은 해법이 아니라 해법의 지도다.
2. 서로 비슷한 안 10개가 아니라 **시간축·접근 방식이 다양한** 안을 펼친다.

## 절차

1. `$ARGUMENTS`에서 문제 정의와 제약(기간·인력·비용)을 확인한다. 문제 정의가
   흐리면 한 라운드만 짧게 되묻는다 (측정 가능한 형태로: "무엇이 얼마나 나쁜가").
2. 후보 개입(intervention)을 **10개 내외** 생성하되, 시간축에 분산시킨다:
   즉시 적용(오늘) / 단기(1–2주) / 중기(분기) / 장기 베팅.
3. 각 후보에 붙일 것: **이름 / 한 줄 설명 / 기대 효과(무엇이 얼마나 좋아지나) /
   노력·비용 / 주요 리스크 / 성공 측정법**.
4. **효과 × 노력** 관점으로 배치해 보여준다 — quick win과 big bet이 한눈에
   구분되게.
5. 사용자의 선택을 받은 뒤: 선택된 개입들을 **구조화된 다음 단계**로 변환한다 —
   각 개입의 첫 실행 프롬프트(또는 실험 설계)까지.

## 산출물 형식 (HTML 우선)

**단일 파일 인터랙티브 HTML**: 후보들을 시간축 타임라인(즉시 → 장기)에 카드로 배치,
효과×노력 매트릭스 뷰 전환, 카드마다 **공감(resonate) 체크박스** — 체크한 항목이
하단에서 **"이것들을 이 순서로 진행하자" 구조화 응답으로 자동 조립**되어 복사 가능.
CSS/JS 인라인, 외부 의존성 없음. 뷰어가 없는 환경이면 시간축별 표 + 선택 안내의
마크다운으로 폴백한다.

## 연계

- 개입을 고른 뒤: 형태가 쟁점이면 `/unknowns:prototypes`, 스펙 확정은
  `/unknowns:interview`, 구현 계획은 `/unknowns:plan`으로 잇는다.
