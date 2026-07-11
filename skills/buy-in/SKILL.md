---
name: buy-in
description: >
  The buy-in doc — after implementation, produce a ship-readiness pitch that leads
  with a working demo, pre-answers likely reviewer objections with evidence, states
  known limitations, and names the stakeholders who must sign off. This skill should
  be used when the user says "buy-in 문서", "설득 문서 만들어줘", "리뷰 준비",
  "머지 승인 준비해줘", "pitch this work", or before requesting review/approval/merge
  of significant work.
argument-hint: "[대상 작업/PR] [설득 대상: 팀/리뷰어]"
---

# Buy-in — 리뷰어 설득 문서 (The Buy-In Doc)

구현이 끝나도 **타인의 승인**이라는 unknown이 남는다. 리뷰어가 무엇을 물을지 미리
알면 그건 known이 된다. 원문 "The Buy-In Doc": 작동하는 데모를 먼저 보여주고,
리뷰어의 반론을 증거와 함께 선제 대응하고, 사인오프가 필요한 사람을 이름으로 명시했다.
`/unknowns:quiz`가 **나의 이해**를 검증한다면, buy-in은 **타인의 신뢰**를 준비한다.

## 절차

1. `$ARGUMENTS`에서 대상 작업과 설득 대상(리뷰어·팀·의사결정자)을 파악한다.
2. **데모 먼저**: 문서 최상단에 작동하는 결과를 배치한다 — 실행 결과, 스크린샷·GIF,
   가능하면 문서 안에서 직접 조작 가능한 인터랙티브 데모.
3. **반론 선제 대응**: 이 변경에 대해 리뷰어가 물을 법한 질문·반론을 5개 내외로
   예상하고, 각각에 **증거**(테스트 결과, 벤치마크 수치, 코드 위치, 설계 근거)를
   붙여 미리 답한다. 근거 없는 반박은 쓰지 않는다 — 증거가 없으면 한계로 옮긴다.
4. **알려진 한계와 미해결 unknown**: IMPLEMENTATION_NOTES.md가 있으면 기록된 이탈과
   미해결 위험을 여기로 가져온다. 숨기지 않는 것이 신뢰의 근거다.
5. **사인오프 목록**: 승인이 필요한 사람·팀을 역할과 함께 명시하고, 각자가 확인해야
   할 부분을 지정한다.
6. **롤백 계획**: 문제가 생기면 어떻게 되돌리는지 한 단락.

## 산출물 형식 (HTML 우선)

**단일 파일 인터랙티브 HTML**: 최상단 데모(애니메이션·실행 예), 반론별 펼침 카드
(반론 → 증거), 한계 섹션, 사인오프 체크리스트(확인 항목별 체크 → **리뷰 코멘트
초안으로 조립**). CSS/JS 인라인, 외부 의존성 없음.
뷰어가 없는 환경이나 PR 본문이 목적이면 같은 구조의 마크다운으로 폴백한다.

## 연계

- 작성 전 `/unknowns:quiz`를 먼저 돌리면 좋다 — 사용자가 설명 못 하는 작업은
  buy-in 문서로도 방어할 수 없다.
- independent-reviewer 에이전트의 검증 결과("확인 완료" 목록 포함)는 반론 대응의
  가장 강한 증거가 된다.
