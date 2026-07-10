---
name: loop
description: >
  Field-guide operating loop — orchestrate the full explore → question → prototype →
  implement-with-notes → verify → quiz → value-check workflow for significant or
  ambiguous work. This skill should be used when the user says "field guide", "필드
  가이드", "field-guide loop", "운영 루프로 진행", "풀 루프로 해줘", or starts a
  substantial/ambiguous feature and wants the whole methodology applied end to end.
  For a single technique, use the individual skills instead (blindspot, interview,
  prototypes, reference-map, impl-notes, quiz).
argument-hint: "<작업 설명>"
---

# Field-Guide Loop — 강한 모델과 일하는 운영 루프

핵심 원리: **강한 모델의 병목은 모델이 아니라, 지도(계획)와 영토(실제)를 일치시키는
사용자의 능력이다.** 좋은 프롬프트 한 번보다 탐색 → 질문 → 구현 → 이탈 기록 → 검증의
루프를 설계하는 것이 중요하다. 배경과 출처는 `references/talk-source.md` 참조.

## 단계 (기본 9단계 — 규모에 따라 축소)

### 0. 가치·완료 조건 정의
작업 시작 전에 사용자와 함께 확정한다: 목적 / 사용자가 얻을 가치 / 완료 판정 기준 /
절대 깨지면 안 되는 기존 동작 / 허용 비용·변경 범위.
**성공 기준이 없으면 구현량을 성과로 착각하게 된다.**

### 1. 사각지대 조사 → `/field-guide:blindspot`
구현 없이 조사만. unknown unknowns, 충돌 지점, 회귀 위험을 찾고 개선된 프롬프트를 만든다.

### 2. 인터뷰 → `/field-guide:interview`
아키텍처를 바꿀 질문부터, 라운드당 5개 이하.

### 3. 취향·형태 탐색 (필요시) → `/field-guide:prototypes` 또는 `/field-guide:reference-map`
말로 설명 못 하는 요구는 발산형 프로토타입으로, 예시가 있으면 레퍼런스 분석으로.

### 4. 위험 가정 프로토타입 (필요시)
전체 구현 전에 **가장 불확실한 기술 가정만 검증하는 최소 프로토타입**을 만든다.
검증할 가정과 성공·실패 기준을 먼저 명시한다.

### 5. 계획 수립
단계별로: 수정 파일 / 변경 목적 / 검증 방법 / 예상 위험 / 롤백 방법.

### 6. 구현 + 이탈 기록 → `/field-guide:impl-notes` 규칙 적용
계획에 없는 상황을 만나면 기록하고, 아키텍처·사용자 동작·데이터·보안에 닿는 결정이면
멈추고 질문한다.

### 7. 독립 검증 → **independent-reviewer 에이전트**
구현자의 설명을 신뢰하지 않는 별도 검토를 돌린다. 가능하면 구현과 검토의 컨텍스트를
분리한다(에이전트 사용이 곧 분리다).

### 8. 이해도 검증·인수인계 → `/field-guide:quiz`
사용자가 이 작업을 PR·인수인계에서 설명할 수 있는지 확인한다.

### 9. 가치 검토
코드 품질이 아니라 실제 가치 기준으로: 누구의 어떤 문제가 줄었나 / 얼마나 빨라졌나 /
사용되지 않을 이유 / 측정 지표 / 제거 조건. **Building is easier, generating value
is still hard.**

## 규모별 축소 기준

- **작은 수정** (파일 1–2개, 명확한 스펙): 6단계만 (impl-notes 규칙) — 루프 불필요.
- **중간 작업**: 1 → 2 → 5 → 6 → 8.
- **크거나 낯선 작업**: 전체 9단계.
- 판단이 애매하면 사용자에게 어느 수준으로 돌릴지 묻는다.

## 운영 원칙 (압축)

1. 목적을 정의한다. 2. 구현 전에 사각지대를 찾는다. 3. 모델에게 질문하게 한다.
4. 말 대신 레퍼런스와 프로토타입을 준다. 5. unknown과 계획 이탈을 기록한다.
6. 테스트와 독립 검토로 확인한다. 7. 사용자가 결과를 설명할 수 있는지 확인한다.
8. 코드량이 아니라 실제 가치를 측정한다.
