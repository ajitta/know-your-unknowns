---
name: loop
description: >
  Know-your-unknowns operating loop — orchestrate the full explore → question →
  prototype → plan → implement-with-notes → verify → quiz → value-check workflow for
  significant or ambiguous work. This skill should be used when the user says "unknowns
  loop", "know your unknowns", "운영 루프로 진행", "풀 루프로 해줘", "field guide"/"필드
  가이드"(구버전 호칭), or starts a substantial/ambiguous feature and wants the whole
  methodology applied end to end. For a single technique, use the individual skills
  instead (blindspot, teach-me, interview, prototypes, brainstorm, reference, plan,
  notes, quiz, buy-in).
argument-hint: "<작업 설명>"
---

# Unknowns Loop — 강한 모델과 일하는 운영 루프

핵심 원리: **강한 모델의 병목은 모델이 아니라, 지도(계획)와 영토(실제)를 일치시키는
사용자의 능력이다. 그 간극이 곧 unknowns다.** 좋은 프롬프트 한 번보다 탐색 → 질문 →
계획 → 구현 → 이탈 기록 → 검증의 루프를 설계하는 것이 중요하다.
배경과 출처는 `references/talk-source.md` 참조.

산출물 공통 원칙: 사용자가 **보고 반응해야 하는** 산출물(조사 결과, 시안, 계획,
설득 문서)은 가능하면 반응-조립 UI가 달린 단일 파일 인터랙티브 HTML로 만든다.
뷰어가 없는 환경이면 같은 구조의 마크다운으로 폴백한다.

## 단계 (기본 10단계 — 규모에 따라 축소)

### 1. 가치·완료 조건 정의
작업 시작 전에 사용자와 함께 확정한다: 목적 / 사용자가 얻을 가치 / 완료 판정 기준 /
절대 깨지면 안 되는 기존 동작 / 허용 비용·변경 범위.
**성공 기준이 없으면 구현량을 성과로 착각하게 된다.**

### 2. 사각지대 조사 → `/unknowns:blindspot`
구현 없이 조사만. unknown unknowns, 충돌 지점, 회귀 위험을 찾고 개선된 프롬프트를 만든다.
낯선 **도메인 자체**를 배워야 하면(용어를 몰라 요청이 모호해지는 상태)
`/unknowns:teach-me`를 병행한다.

### 3. 인터뷰 → `/unknowns:interview`
아키텍처를 바꿀 질문부터, 라운드당 5개 이하.

### 4. 해법·형태 탐색 (필요시)
- **무엇을 할지**가 안 정해졌으면 → `/unknowns:brainstorm` (해법 공간 지도)
- **어떤 모양일지** 말로 설명 못 하면 → `/unknowns:prototypes` (발산형 시안)
- **닮고 싶은 예시**가 있으면 → `/unknowns:reference` (레퍼런스 분석)

### 5. 위험 가정 프로토타입 (필요시)
전체 구현 전에 **가장 불확실한 기술 가정만 검증하는 최소 프로토타입**을 만든다.
검증할 가정과 성공·실패 기준을 먼저 명시한다.

### 6. 계획 수립 → `/unknowns:plan`
실행 순서가 아니라 **수정될 확률 순**으로 정렬한 tweakable plan을 만든다.
사용자가 개입할 결정(스키마·인터페이스·UX 계약)이 맨 위로 온다.

### 7. 구현 + 이탈 기록 → `/unknowns:notes` 규칙 적용
계획에 없는 상황을 만나면 기록하고, 아키텍처·사용자 동작·데이터·보안에 닿는 결정이면
멈추고 질문한다.

### 8. 독립 검증 → **independent-reviewer 에이전트**
구현자의 설명을 신뢰하지 않는 별도 검토를 돌린다. 가능하면 구현과 검토의 컨텍스트를
분리한다(에이전트 사용이 곧 분리다).

### 9. 이해도 검증·인수인계 → `/unknowns:quiz`
사용자가 이 작업을 PR·인수인계에서 설명할 수 있는지 확인한다.
리뷰어·이해관계자의 **승인**이 필요한 작업이면 `/unknowns:buy-in` 문서를 추가로 만든다.

### 10. 가치 검토
코드 품질이 아니라 실제 가치 기준으로: 누구의 어떤 문제가 줄었나 / 얼마나 빨라졌나 /
사용되지 않을 이유 / 측정 지표 / 제거 조건. **Building is easier, generating value
is still hard.**

## 규모별 축소 기준

- **작은 수정** (파일 1–2개, 명확한 스펙): 7단계 규칙(notes)만 — 루프 불필요.
- **중간 작업**: 2 → 3 → 6 → 7 → 9.
- **크거나 낯선 작업**: 전체 10단계.
- 판단이 애매하면 사용자에게 어느 수준으로 돌릴지 묻는다.

## 운영 원칙 (압축)

1. 목적을 정의한다. 2. 구현 전에 사각지대를 찾는다. 3. 모델에게 질문하게 한다.
4. 말 대신 레퍼런스와 프로토타입을 준다. 5. 계획은 수정될 확률 순으로 쓴다.
6. unknown과 계획 이탈을 기록한다. 7. 테스트와 독립 검토로 확인한다.
8. 사용자가 결과를 설명할 수 있는지 확인한다. 9. 산출물은 반응할 수 있는 형태로 준다.
10. 코드량이 아니라 실제 가치를 측정한다.
