---
name: plan
description: >
  The tweakable plan — write implementation plans sorted by likelihood-of-tweaking,
  not by execution order, so the user reviews the decisions most likely to change
  first. This skill should be used when the user says "계획 세워줘", "구현 계획",
  "plan this", "tweakable plan", "수정확률순 계획", or when a plan is needed after
  blindspot/interview and before implementation.
argument-hint: "<작업 설명 또는 확정된 스펙>"
---

# Plan — 수정확률순 계획 (The Tweakable Plan)

계획서의 목적은 실행 순서 나열이 아니라 **사용자가 개입할 지점을 앞으로 끌어오는 것**이다.
원문 "The Tweakable Plan": 로드맵을 실행 순서가 아니라 **"수정될 확률(likelihood of
tweaking)" 순**으로 정렬하고, 스키마 결정에는 대안을 달고, 기계적 작업은 접었다.
사용자가 계획서를 위에서부터 읽다 지쳐도, 정말 봐야 할 결정은 이미 다 본 상태가 된다.

## 철칙

1. **실행 순서 ≠ 제시 순서.** 제시는 수정될 확률 순, 실행 순서는 각 항목에 번호로만.
2. 결정에는 반드시 **고려한 대안**을 붙인다 — 대안 없는 결정은 검토할 수 없다.

## 절차

1. `$ARGUMENTS`와 대화 맥락(blindspot 조사, 인터뷰 결정)에서 스펙을 확정한다.
   빈 곳이 크면 `/unknowns:interview`를 먼저 제안한다.
2. 작업을 항목으로 쪼개고 각 항목을 두 부류로 나눈다:
   - **결정 항목** — 스키마/데이터 모델, 공개 인터페이스(API·타입), UX 계약,
     의존성 선택, 마이그레이션 방식 등 바뀌면 파급이 큰 것
   - **기계적 항목** — 결정이 정해지면 따라오는 작업 (CRUD, 배선, 보일러플레이트)
3. **결정 항목을 수정될 확률 × 파급 범위 순으로 정렬**해 앞에 배치한다. 각 항목에:
   선택안 / 고려한 대안과 버린 이유 / 이 결정을 바꾸면 영향받는 범위 / 검증 방법.
4. 기계적 항목은 뒤로 접어서(요약 1줄 + 펼침) 배치한다.
5. 공통 필수 항목: 단계별 **검증 방법** / **예상 위험** / **롤백 방법**.
6. 사용자의 승인·수정 요청을 받아 계획을 갱신한 뒤에만 구현으로 진행한다.
   구현 중 이탈은 `/unknowns:notes` 규칙으로 기록한다.

## 산출물 형식 (HTML 우선)

**단일 파일 인터랙티브 HTML** 계획서: 결정 항목이 위에서부터 카드로, 카드마다
**대안 토글**(선택안 ↔ 대안 비교)과 **승인 / 변경 요청 선택** — 선택 결과가 하단에서
**"3번은 대안 B로, 나머지 승인" 형태의 회신으로 자동 조립**되어 복사 가능.
기계적 작업은 접힌 섹션으로. CSS/JS 인라인, 외부 의존성 없음.
뷰어가 없는 환경이면 같은 정렬 원칙의 마크다운(결정 테이블 + 접힌 목록)으로 폴백한다.
