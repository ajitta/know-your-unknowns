---
name: prototypes
description: >
  Divergent prototype fan-out — generate N (default 4) prototypes with clearly
  different design philosophies so the user can react to them. This skill should be
  used when the user says "divergent prototypes", "프로토타입 여러 개", "시안 4개",
  "design options", "design directions", "다양한 디자인으로 보여줘", or cannot
  articulate what they want ("보면 안다", "know it when I see it") for a UI,
  dashboard, document, or API design.
argument-hint: "<만들 대상> [개수, 기본 4]"
---

# Prototypes — 발산형 프로토타입 팬아웃 (Design Directions)

사람은 원하는 것을 말로 설명하지 못해도 **결과를 보면 판단할 수 있다** (unknown knowns).
원 출처: Thariq Shihipar — "I have no visual taste. Make me an HTML page with four
widely different design decisions so I can react to them."

## 철칙

1. **최종 구현을 시작하지 마라.** 프로토타입은 반응을 끌어내기 위한 도구다.
2. 서로 **작은 변형이 아니라 설계 철학이 명확히 다른** 안을 만든다.

## 절차

1. `$ARGUMENTS`에서 대상과 개수(기본 4)를 파악한다.
2. 각 안이 다음 축에서 서로 달라지도록 설계한다:
   - 정보 구조 (무엇을 먼저 보여주는가)
   - 사용자 흐름 (어떤 순서로 조작하는가)
   - 시각적 밀도 (밀집 vs 여백)
   - 상호작용 방식 (클릭/드래그/키보드/자동)
   - 구현 복잡도 (단순-견고 vs 풍부-복잡)
3. 각 안에 붙일 것: **이름 + 설계 철학 한 줄 + 장단점 + 적합한 사용 조건**.
4. 사용자 반응을 받은 뒤: 선택된 요소들을 조합한 **명시적 요구사항 목록**으로
   변환한다 — 말로 못 하던 취향(unknown knowns)이 이제 스펙이 된다.
5. 조합안 확정 후에만 본 구현으로 진행한다.

## 산출물 형식 (HTML 우선)

**단일 파일 인터랙티브 HTML** 안에서 N개 안을 전환하며 비교할 수 있게 만든다.
원문 "Four Design Directions"의 장치를 포함할 것: 각 안(또는 안의 개별 요소)에
**채택(steal) / 제외(skip) 칩**을 달고, 선택 결과가 하단에서
**회신 템플릿("2안의 레이아웃 + 4안의 색…" 형태의 요구사항 목록 초안)으로 자동
조립**되어 복사 가능하게 한다. CSS/JS 인라인, 외부 의존성 없음.
정적 문서·API 설계처럼 HTML이 부자연스러우면 각 안을 같은 형식으로 나란히
제시하는 마크다운으로 폴백한다.

인터랙션 자체가 쟁점이면(툴바 위치, 클릭 흐름 등) 원문 "Mock Before You Wireframe"
방식으로: 실제 코드 없이 **클릭 가능한 목업**에 배치 토글·A/B 선택 버튼을 넣어
반응을 수집한다.

## 변형

- 코드 아키텍처에도 적용 가능: 같은 기능의 접근법(예: 이벤트 기반 vs 폴링 vs 푸시)을
  최소 스켈레톤으로 나란히 제시.
- 사용자가 "wild하게"를 요구하면 철학 간 거리를 더 벌린다.
