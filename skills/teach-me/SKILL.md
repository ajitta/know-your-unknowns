---
name: teach-me
description: >
  Teach me my unknowns — build an interactive explainer that teaches the user the
  vocabulary and mental model of an unfamiliar domain, so vague requests become
  precise ones. This skill should be used when the user says "teach me", "가르쳐줘",
  "설명서 만들어줘", "이 분야 용어를 모르겠어", "teach me my unknowns", or asks for
  work in a domain where they cannot yet name what they want (e.g. "영상 더 좋게
  해줘", "make it pop") and better vocabulary would make the request precise.
argument-hint: "<배우려는 분야/작업> [현재 수준]"
---

# Teach Me — 도메인 어휘 설명서 (Teach Me My Unknowns)

모호한 요청("더 좋게 해줘")의 원인은 취향 부족이 아니라 **어휘 부족**인 경우가 많다.
원문 "Teach Me My Unknowns": 색보정을 모르는 사용자에게 어휘 사다리와 before/after
비교를 주자, "make the video nicer"가 전문 언어의 정밀한 요청으로 바뀌었다.
이 스킬은 unknown unknowns 중에서도 **개념·용어의 공백**을 메운다.

## 철칙

1. **아직 작업을 시작하지 마라.** 먼저 사용자가 요청을 정밀하게 만들 수 있게 가르친다.
2. 백과사전이 아니라 **결정에 필요한 어휘만** 가르친다 — 이 작업에서 사용자가
   선택해야 할 축이 무엇인지에서 출발한다.

## 절차

1. `$ARGUMENTS`에서 분야·목표·현재 수준을 파악한다. 불명확하면 한 번만 짧게 묻는다.
2. 이 작업에서 사용자가 내리게 될 **결정 축**을 3–7개 뽑는다
   (예: 색보정이면 노출/화이트밸런스/대비 곡선/채도 vs 자연스러움/룩).
3. **어휘 사다리**를 만든다: 축마다 일상어 → 전문어 순으로, 각 용어에
   "이 용어로 무엇을 요청할 수 있는지" 예문 1개를 붙인다.
4. 개념마다 **before/after 비교**를 보여준다 — 같은 대상에 그 개념을 적용했을 때와
   아닐 때의 차이. 시각 분야면 실제 비교 이미지를, 코드·글이면 비교 예시를.
5. 마무리: 사용자의 **원래 요청을 새 어휘로 다시 쓴 정밀 요청 초안**을 제시한다.
   사용자가 항목을 고르고 수치·방향을 조정하면 그대로 다음 프롬프트가 된다.

## 산출물 형식 (HTML 우선)

**단일 파일 인터랙티브 HTML** 설명서: 어휘 사다리(용어 클릭 → 정의·예문 펼침),
가능하면 **라이브 before/after 슬라이더·토글**(CSS filter, 인라인 SVG/캔버스 등으로
실제 시연), 각 개념에 "내 요청에 포함" 체크 → 하단에서 **정밀 요청 프롬프트가 자동
조립**되어 복사 가능. CSS/JS 인라인, 외부 의존성 없음.
뷰어가 없는 환경이면 어휘 사다리 표 + 비교 설명 + 요청 초안의 마크다운으로 폴백한다.

## 연계

- 코드베이스의 사각지대가 문제면 `/unknowns:blindspot`이 먼저다 — teach-me는
  도메인 **개념**의 사각지대를 다룬다. 둘을 병행해도 된다.
- 어휘를 얻은 뒤 요구가 여전히 갈리면 `/unknowns:interview`로 결정을 굳힌다.
