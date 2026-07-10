---
name: interview
description: >
  Pre-implementation interview — the model interviews the user to convert known
  unknowns into decisions. This skill should be used when the user says "interview me",
  "인터뷰해줘", "질문해줘" (before implementation), "ask me questions about the spec",
  "스펙 질문", or when requirements are visibly incomplete and implementation has not
  started yet. Prioritize architecture-changing questions first.
argument-hint: "[작업/스펙 설명] [우선순위 힌트]"
---

# Interview — 구현 전 인터뷰

요구사항이 불완전할 때 바로 구현하지 말고 **모델이 사용자를 인터뷰**한다.
원 출처: Thariq Shihipar — 질문에 컨텍스트를 줄수록 좋다. 특히
"prioritize questions that would change the architecture."

## 질문 우선순위 (고정)

1. 답변에 따라 **전체 아키텍처가 바뀌는** 질문
2. **데이터 손실·보안 문제**를 유발할 수 있는 질문
3. **외부 API·기존 코드와의 호환성** 질문
4. **성능·운영비용**에 영향을 주는 질문
5. UI 취향·사소한 구현 세부사항 (마지막)

## 절차

1. `$ARGUMENTS`와 대화 맥락에서 스펙의 빈 곳(known unknowns)을 나열한다.
2. 우선순위에 따라 **한 라운드에 5개 이하**로 질문한다. 각 질문에
   **왜 중요한지 한 줄 근거**를 붙인다.
3. AskUserQuestion 도구가 사용 가능하면 선택지형 질문에 활용한다. 각 선택지에는
   결과(트레이드오프)를 짧게 설명한다.
4. 답변을 받으면: 결정된 사항을 **갱신된 스펙 요약**으로 재제시하고, 남은 미결정
   사항이 있으면 다음 라운드를 제안한다.
5. 사용자가 심층 인터뷰를 원하면(예: "40개 질문 수준으로") 라운드를 반복하되,
   아키텍처 → 데이터 → 호환성 → 성능 → 취향 순서를 유지한다.

## 금지

- 답이 이미 대화·코드베이스에 있는 질문을 하지 않는다 (먼저 조사한다).
- 우선순위 5(취향)부터 시작하지 않는다.
- 인터뷰 없이 추측으로 구현을 시작하지 않는다.
