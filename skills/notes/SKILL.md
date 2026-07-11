---
name: notes
description: >
  Implementation notes — log every significant deviation from the plan while working.
  This skill should be used automatically whenever implementation encounters a
  situation not covered by the plan or spec (an "unknown") and a non-trivial decision
  is made, and when the user says "implementation notes", "impl notes", "이탈 기록",
  "임플 노트", "log deviations", or asks where/why the work diverged from the plan.
argument-hint: "[init | show | <기록할 내용>]"
---

# Notes — 계획 이탈 기록 (Implementation Notes)

작업 중 계획·명세에 없는 상황(unknown)을 만나면 **임의로 결정하고 조용히 지나가지 말고
기록한다**. 원 출처: Thariq Shihipar — "If it runs into an unknown, ask it to log it,
so you can see where the deviations happened and figure out why."
에이전트가 계획과 다른 방향으로 조용히 이동하는 것을 막는 핵심 장치다.

## 파일 규칙

- 위치: 프로젝트 루트의 `IMPLEMENTATION_NOTES.md` (없으면 생성).
- `$ARGUMENTS`가 `init`이면 빈 템플릿으로 파일을 만들고, `show`면 현재 노트를 요약한다.

## 기록 형식 (항목당)

```markdown
## [YYYY-MM-DD] <작업/기능 이름>
- **발견한 상황**: 계획에 없던 무엇을 만났는가
- **계획과 다른 점**: 원래 계획은 무엇이었는가
- **선택한 대응**: 무엇을 했는가 (보수적 선택이었다면 그 이유)
- **선택 이유**: 왜 그 방법인가
- **고려한 대안**: 버린 선택지와 버린 이유
- **위험/후속 확인**: 이 결정이 틀렸다면 어디서 드러나는가
- **다음 시도 개선점**: 다음에 같은 작업을 하면 무엇을 다르게 할 것인가 (1–3개)
```

## 기록 기준

- **기록한다**: 설계·동작·호환성에 영향을 주는 결정, 스펙 해석이 갈리는 지점,
  예상과 다른 기존 코드 구조, 우회(workaround), 새 의존성.
- **기록하지 않는다**: 사소한 문법 수정, 포맷팅, 변수명, 자명한 구현 세부.

## 에스컬레이션

기록으로 끝내지 않고 **작업을 멈추고 사용자에게 질문**해야 하는 경우:
- 아키텍처를 바꾸는 결정
- 사용자에게 보이는 동작(UX·API 계약)을 바꾸는 결정
- 데이터 손실·보안에 닿는 결정

## 마무리

세션을 마치거나 PR을 만들기 전, 노트에 쌓인 항목을 요약해 사용자에게 보고하고
`/unknowns:quiz`로 이어가기를 제안한다. 승인이 필요한 작업이면 `/unknowns:buy-in`
문서에 이 노트의 미해결 항목을 "알려진 한계"로 반영한다.
