---
name: quiz
description: >
  Post-work comprehension quiz — after finishing significant work, explain what changed
  and quiz the user so they stay in the loop and can represent the work in a PR or
  handoff. This skill should be used when the user says "quiz me", "퀴즈", "내가 이해했는지
  확인해줘", "test my understanding", or right before creating/merging a PR for work the
  model largely implemented.
argument-hint: "[대상 작업/PR 범위]"
---

# Quiz — 작업 후 이해도 검증 (Stay in the Loop)

작업을 맡겨도 **사용자는 결과를 설명할 수 있어야 한다**. 원 출처: Thariq Shihipar —
"I like to get it to quiz me about what happened, to make sure I understand what I'm
doing and can represent this work when I'm creating a PR or merging it."

## 절차 — 1부: 먼저 설명한다

퀴즈 전에 다음을 간결하게 설명한다:

1. 변경된 **전체 구조** (무엇이 어디에 생겼/바뀌었는가)
2. 가장 중요한 **설계 결정 3개**와 그 이유
3. **실패 가능성이 높은 부분** (틀렸다면 어디서 먼저 드러나는가)
4. 사용자가 **직접 확인해야 하는 부분** (모델이 보장 못 하는 것)

## 절차 — 2부: 퀴즈

1. 질문 **5개**를 낸다. AskUserQuestion 도구가 있으면 선택지형으로 활용한다.
2. 질문 우선순위: **장애 대응**("X가 죽으면 어디를 먼저 보는가") >
   **설계 이유**("왜 A가 아니라 B인가") > **동작 예측**("이 입력이면 결과는") >
   단순 암기 (지양).
3. 답을 받으면 채점하고, 틀리거나 빈 부분은 **그 부분만 다시 설명**한다 —
   원문 "Quiz Me Before I Merge"처럼 오답이 정확히 어느 변경 지점을 다시 봐야
   하는지 가리키게 한다.
4. IMPLEMENTATION_NOTES.md가 있으면 기록된 이탈 지점을 퀴즈에 반드시 1개 이상 포함한다.

## 산출물 형식 (HTML 옵션)

머지 직전 큰 변경이면 **머지 준비도 리포트**를 단일 파일 HTML로 만들 수 있다:
변경 요약(파일별 접기) + 퀴즈 UI, 오답 선택 시 해당 변경 섹션으로 스크롤·하이라이트.
일반적인 경우는 대화 안에서 진행하면 충분하다.

## 마무리: 인수인계 요약

퀴즈 후 다음을 담은 인수인계 요약을 제시한다 — 다른 개발자가 내일 인수받는다고 가정:
구조 요약 / 핵심 결정 / 실행·테스트 방법 / 장애 시 확인 순서 / 남은 위험.
사용자가 원하면 PR 본문 초안으로 변환하고, 리뷰어 승인이 필요한 작업이면
`/unknowns:buy-in` 문서 작성을 제안한다.
