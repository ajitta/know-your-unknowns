---
name: reference
description: >
  Point at a reference — treat a provided example as a map, not an answer. Analyze
  reference code, mockups, or docs and prove comprehension before implementing. This
  skill should be used when the user provides reference material and says "use this
  as a reference", "레퍼런스로 써", "이 코드처럼 만들어줘", "이거 참고해서", or passes
  example code in another language/system, an HTML mockup, a screenshot, or a
  competitor's UX as the basis for new work.
argument-hint: "<레퍼런스 파일/경로/설명>"
---

# Reference — 레퍼런스는 또 하나의 지도

모델에게 지도를 주는 가장 좋은 방법은 **다른 지도를 주는 것**이다.
원 출처: Thariq Shihipar — "Here's some code that represents what I want. It could be
in a different system or language. Read this code, understand it, and use that to
start your work." 말로 수백 줄을 설명하는 것보다 작동하는 예제 하나가 더 정확하다.

## 철칙

**레퍼런스는 그대로 복사할 정답이 아니라, 의도와 동작을 이해하기 위한 자료다.**
구현 전에 **이해했음을 증명**한다 — 원문 "Point at a Reference"의 semantics map.

## 절차

1. 레퍼런스를 끝까지 읽고 **의도·핵심 동작·불변식**을 요약한다.
2. 4분류 분석을 제시한다:
   - **반드시 보존할 동작** — 레퍼런스의 존재 이유
   - **현재 환경에 맞게 변환할 부분** — 언어/프레임워크/규모 차이
   - **불필요하거나 위험한 부분** — 현재 프로젝트에 가져오면 안 되는 것
   - **더 나은 방식으로 개선할 수 있는 부분** — 레퍼런스보다 잘할 수 있는 것
3. 이식·변환 작업이면 **이해 증명(semantics map)**을 함께 제시한다:
   레퍼런스의 핵심 발췌 ↔ 새 환경에서의 대응 방식을 나란히, 동작이 미묘하게 달라지는
   지점(gotcha)과 엣지케이스 표 포함.
4. 현재 프로젝트의 관례(코드 스타일, 의존성, 테스트 방식)와 대조해 **적용 계획**을
   제시한다.
5. 사용자 확인 후 구현을 시작한다. 레퍼런스와 의도적으로 달라지는 지점은
   `/unknowns:notes` 규칙에 따라 기록한다.

## 산출물 형식 (HTML 우선)

분석이 크면(다수 파일·언어 이식) **단일 파일 인터랙티브 HTML**로: 좌우 대조
(레퍼런스 발췌 ↔ 대응 계획), gotcha 노트, 엣지케이스 표, 항목별
**승인/변경요청 선택이 회신으로 조립**되는 UI. 작은 분석은 마크다운으로 충분하다.

## 레퍼런스가 될 수 있는 것

기존 구현 코드, 다른 언어로 된 같은 알고리즘, 작동하는 HTML 목업, 경쟁 제품 UX,
과거 프로젝트 설계 문서, 테스트 코드, 스크린샷·영상, 원하는 출력의 실제 예시.
React 컴포넌트를 만들 때 HTML 목업이 지도가 되는 식이다.
