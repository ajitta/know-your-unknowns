# 다음 라운드 인계 — 0.13.2

새 세션은 이 문서의 상태를 git·태그·릴리스·CI와 먼저 대조하고 시작한다. 이 문서는 작업 지시가 아니라 출발점이다.

## 상태

배포 중인 버전은 `unknowns--v0.13.2`이다(2026-11-22, PR #40, main `dfb0bb9`). 릴리스 자산 두 개의 sha256이 커밋된 zip과 일치하고(`know-your-unknowns.zip` `55c80740…`, `know-your-unknowns-openai.zip` `0233cc69…`), 빈 설정 설치가 자체 마켓플레이스와 `ajitta/claude-plugins` 두 경로 모두 0.13.2에 스킬 폴더 11개, 에이전트 2개였다. 릴리스 본문은 이번에도 워크플로가 머지 커밋 메시지로 채워서 태그 메시지로 바꿔 넣었다. 원격 작업 브랜치 `audit-fixes-2026-11-22`는 지우지 않았다.

0.13.2에 들어간 것(스킬 본문 열 개와 unknowns-scout, 설명은 그대로): deviation-log(Don't log에서 비밀번호 절 삭제), quiz(teach-back은 키의 요점 전부, 채점과 해설은 여섯 답 뒤, 입력이 없을 때의 문장), blindspot·brainstorm(scout는 직접 다 읽을 수 없을 만큼 많은 자료일 때), blindspot·scout(가정마다 held / wrong / still unchecked 판정을 돌려받음, 첫 초안은 모든 fix 적용), tweakable-plan(interview를 제안하고 같은 답에서 계획), unknowns-loop(1단계 제목, "nothing is scored" 삭제), prototypes(옵션 둘이면 triad 대신 차이 질문), reference(입력이 없을 때의 문장, Output을 5단계에 맞춤), buy-in·quiz·unknowns-loop(공용 deviation log 문장에 비코드 파일), teach-me·brainstorm·deviation-log·tweakable-plan(문구만). OpenAI 목록의 긴 설명 한 문장이 바뀌었다("labeled passes" 삭제).

소유자가 확인한 표면(2026-10-28, 0.12.2, 소유자 보고이며 화면 증거는 기록하지 않음): ChatGPT zip 업로드와 ChatGPT 모바일의 스킬 호출, claude.ai의 Add marketplace 설치가 Claude 모바일로 이어지는 것. claude.ai zip 업로드는 마켓플레이스 경로가 모바일까지 이어지므로 하지 않는다(소유자 판단). 소유자가 확인하지 않은 경로: claude.ai zip 업로드, Claude 데스크톱, Codex CLI, ChatGPT 데스크톱 마켓플레이스. 소유자 확인이 아닌 기록된 자동 실행: Codex CLI 실행(0.10.0, 0.12.1, 그리고 0.12.3부터 릴리스마다 GPT-6.1 Sol trigger), 두 마켓플레이스에서의 빈 설정 Claude Code 설치(0.12.3부터 릴리스마다).

### 0.13.2 릴리스에서 (2026-11-22, PR #40)

- 시작: 소유자가 `skills/`에 프롬프트 감사를 요청했다. 감사는 낡은 문구 패턴을 거의 찾지 못했고, 소유자가 요청한 독립 리뷰 둘(감사를 결론 없이 다시 돌린 것, 본문을 실행하는 모델 쪽에서 읽은 것)이 기록된 실행을 열어 본문 문장이 행동을 바꾸거나 정하지 못하는 곳을 찾았다. 감사의 첫 결론("깨끗함")은 그 뒤에 고쳤다.
- 소유자 결정(2026-11-22): 네 묶음 승인(비밀번호 절 삭제, quiz 두 문장, scout 조건, README·OpenAI 목록의 사실 수정), quiz 두 질문의 답(teach-back은 요점 전부, 채점은 여섯 답 뒤), 이어서 남은 지적 처리와 릴리스 지시.
- 독자 확인: 글쓴이가 아닌 독자가 두 묶음을 각각 전후 비교했고, 실행 전에 여덟 문장을 그 지적대로 고쳤다(첫 묶음 다섯, 둘째 묶음 셋).
- 수정 확인(격리, Opus 5.5, medium, Claude Code 2.1.330, 기준은 실행 전에 적음): 답사 케이스 2회 중 2회가 비밀번호를 계획서에 적고 로그에는 넣지 않았다. quiz 다회차 3회 중 3회가 여섯 답 뒤에 채점했고 키가 요점 전부를 요구했다(`key-hidden-until-answered`는 3회 중 2회, 놓친 1회는 선택지 길이 쪽). scout 케이스 둘은 점수 항목 1회 중 1회, scout 호출 0회.
- 릴리스 점검(전체 1회): 단발 88케이스 채점 항목 194/206(점수에 드는 항목 125/134, 0.13.1과 같은 수), 다회차 13케이스 29/32. 0.13.1 때 통과했다가 놓친 `logs-the-public-rename`과 `free-text-corrections-applied`는 2회씩 다시 돌려 2회 중 2회였다(후자의 첫 실행은 가상 사용자가 한 번도 답하지 않은 대화). 나머지 누락은 0.13.1과 같은 칸이다.
- GPT-6.1 Sol medium: trigger 22/22. 릴리스 뒤 같은 날 태그 `unknowns--v0.13.2`(커밋 `dfb0bb9`)에서 돌렸다. Codex CLI 0.164.0, WSL(Ubuntu), 격리한 HOME과 `CODEX_HOME`, 읽기 전용 캐시 폴더 가드 사용. 22개 실행 모두 0.13.2의 `SKILL.md`를 읽었고 계정 사본을 읽은 세션은 0건이다. 태그 메시지와 릴리스 본문은 "Sol 미실행"이라고 적고 있고(릴리스 시점에는 사실), CHANGELOG는 그 뒤에 고쳤다.
- Sol 확인을 WSL에서 한 것은 이번이 처음이다(방법은 아래 '릴리스 절차').
- 감사와 리뷰가 그대로 두기로 한 것: 되읽기 문단, 설명 속 "NOT", 개수 지정(질문 4개, 6문항 등), interview의 "start with a short plan", buy-in의 리뷰어 호출과 unknowns-loop 5a의 Verify(Opus 5의 "검증 지시를 지워라" 행에 걸리지만 방법의 일부), teach-me의 색보정 예시(비코드 실행에 새지 않음).

## 남은 일

열린 일은 이 표 하나로 추적한다. '소유자 결정 대기'는 2026-11-24 정리에서 소유자가 아직 정하지 않은 항목이고, 행 안의 '권고'는 그 정리의 권고다. 끝난 행은 지우고, 결과는 `CHANGELOG.md`와 `IMPLEMENTATION_NOTES.md`에 남긴다. `IMPLEMENTATION_NOTES.md`의 Todo for human 가운데 이 표에 없는 것은 풀렸거나 무의미해졌다(2026-11-24 판정).

| 남은 일 | 누가 | 어디서 시작 |
|---|---|---|
| ChatGPT에 `know-your-unknowns-openai.zip` 재업로드. 0.13.2에서 목록 문장 하나와 스킬 본문 열 개가 바뀌었다. 다음 릴리스는 `packaging/openai/interface.json` 예시 프롬프트를 `openai.yaml` 11개처럼 `$unknowns:` 표기로 바꾼다(2026-11-24 정리). 그 zip을 올릴 때 목록에서 어떻게 보이는지 본다 | 소유자(직접 하기로 함) | GitHub Release `unknowns--v0.13.2` |
| claude.ai(Add marketplace 경로)가 0.13.2를 받았는지 확인 | 소유자 | claude.ai Customize › Plugins |
| 평가 실행이 계정에 만든 문서 "On-call rotation bot: requirements" 삭제(소유자가 직접 지우기로 함, 2026-11-17, 완료 기록 없음) | 소유자 | Claude Code `/artifacts` 또는 claude.ai |
| 저장소 밖 판사 보조 도구의 프롬프트 고치기: "one line of reasoning per numbered criterion"이 Opus 5.5의 안전 분류기(`reasoning_extraction`)에 막힌다(0.13.2 릴리스에서 한 채점 항목이 두 번 막힘). 저장소 안의 다회차 판사 프롬프트(`evals/run-multiturn.py`)는 2026-11-24 정리에서 번호 기준마다 근거를 인용한 한 줄 판정을 묻도록 바꿨고, 채점기 둘(`deeper-not-padded`, `every-round-at-most-four`)은 "In your reasoning" 대신 판정 줄에 근거를 인용해 적게 했다. 같은 방향으로 바꾼다 | 소유자(저장소 밖) | 소유자의 사설 프로브 스크립트(저장소 밖) |
| 동결 기록 `docs/protocol-alignment.md` 3행에 소유자의 개인 볼트 경로가 남아 있다. 동결 기록이라 2026-11-24 정리에서 그대로 두었다. 지울지 정한다 | 소유자 결정 | `docs/protocol-alignment.md` 3행 |
| B8 brainstorm 충돌 재현(`docs/open-questions.md`에서 옮김, 2026-11-24): 소유자 보고("review·brainstorm 같은 스킬이 의도하지 않게 트리거") 중 brainstorm 쪽은 Claude Code CLI 기록(Skill 호출 270건, 의도하지 않은 것 0)과 dia·design·SuperClaude 동반 단발 스크린에서 재현되지 않았다. 소유자가 본 문장과 표면(claude.ai·데스크톱·모바일 포함)을 받아 그 조건으로 재현한 뒤에만 설명을 고친다 | 소유자가 사례를 줄 때 | `docs/open-questions.md` B8, `docs/features/agent-collision/` |
| ChatGPT·claude.ai에서 짧은 설명의 라우팅. claude.ai의 라우팅은 헤드리스로 돌릴 수 없고, Codex는 trigger 22개만 돌렸다 | 소유자 | `IMPLEMENTATION_NOTES.md` 2026-11-13 |
| 소유자가 손으로 확인하지 않은 표면(Claude 데스크톱, ChatGPT 데스크톱 마켓플레이스) 확인. 필요하다고 볼 때만 | 소유자 | 위 '상태'의 표면 문단 |
| 설명 라운드: 0.13.1에서 보류한 설명 지적 넷(quiz "or before merging", teach-me "Not a plan investigation", blindspot "a better prompt", brainstorm "NOT for design variants"), 설명 속 "you"를 한 뜻으로 정하기(quiz·interview는 사용자, reference는 모델), deviation-log 설명의 "as work hits unknowns"(0.12.4에서 뺀 자동 시작 조건처럼 읽힘), 라우팅이 닿지 않는 본문(prototypes 단일 HTML 목업, quiz "오늘 오후 제출" — 0.13.2 릴리스 점검에서도 로드 안 됨. `behavior-quiz-on-submit`을 정보용으로 돌릴지, 은퇴시킬지, quiz 설명에 "submitting"을 되돌릴지 포함), 보류한 본문 지적 둘(prototypes 6단계 요구사항 목록이 사용자의 말을 나란히 보이지 않음, README 붙여 넣기 문장이 되읽기에는 "what counts as done", 끝에는 "the outcome"이라고 이름이 다름). 권고: 다음 릴리스에서 한 번에, trigger·비코딩·네거티브 케이스를 함께 돌린다 | 소유자 결정 대기 | `CHANGELOG.md` 0.13.1 **Not measured**, `IMPLEMENTATION_NOTES.md` 2026-11-13 Todo for human (a)(b), 2026-11-10 |
| 0.13.2에서 에이전트가 방향을 정한 여섯 곳의 확인 또는 번복: tweakable-plan 1b(제안과 계획을 같은 답에), blindspot 5(첫 초안은 모든 fix), reference Output(5단계대로), unknowns-loop 1단계 제목, prototypes 5a(옵션 둘), scout의 판정 어휘("unsupported" 삭제). 권고: 확인(모두 기록된 실행이 이미 하던 행동을 문장으로 적은 것이다) | 소유자 결정 대기 | `IMPLEMENTATION_NOTES.md` 2026-11-22 |
| 로그 속 비밀 값이 계획서에서 빠진 값보다 나쁜가(0.13.2에서 Don't log의 비밀번호 절을 뺐다). 권고: 지금 문장을 두고 지켜본다. 값이 로그에 다시 나오면 Don't log에 "비밀 값" 항목을 따로 두는 문장을 2회 돌린다 | 소유자 결정 대기 | `IMPLEMENTATION_NOTES.md` 2026-11-22, 아래 '지켜볼 칸' |
| interview의 두 규칙을 함께 다루기: (1) 정한 항목은 다시 묻지 않는다(사용자의 두 결정이 함께 성립할 수 없을 때만 둘을 이름 대고 다시 묻는 예외 포함). 2b에 "Settled items are not asked again"은 있지만 4b 문장은 0.13.1 릴리스 전에 뺐다. (2) 바로 쓸 프롬프트는 사용자가 정한 것만 정해진 것으로 보인다(모델이 덧붙인 요구를 표시한다. 지금 Final Deliverables는 건너뛴 질문만 표시한다). 권고: 다음 interview 변경 때 함께 다룬다 | 소유자 결정 대기, 그 뒤 에이전트 | `IMPLEMENTATION_NOTES.md` 2026-11-17, `CHANGELOG.md` 0.13.1 |
| 분류이거나 섞인 a·b·c 묶음 13개(0.13.1 읽기의 22개 중 interview 1은 변환함)를 바꿀지. 분류 9: blindspot 3, brainstorm 2, buy-in 1, interview 2, quiz 3, teach-me 1·5, tweakable-plan 1·5. 섞임 4: blindspot 4, buy-in 2, interview 4, quiz 1. 메모: buy-in 3(세 번째 단계인데 내용은 "open with")과 tweakable-plan 2·3·6(실행 순서와 문서 순서가 섞임)은 번호 목록 자체가 섞인 곳이다. interview 2a–2d는 가장 전형적인 분류 묶음이지만 이 스킬은 앞선 두 번의 시도에서 다른 칸이 흔들렸다. 권고: 케이스가 실패하는 자리만 바꾼다 | 소유자 결정 대기 | `.claude/rules/skill-writing.md` 1번, `CHANGELOG.md` 0.13.1 |
| 0.13.1 읽기(Fable 5.2)에서 나온 나머지 후보 넷: quiz 키 파일의 위치, blindspot에서 목록이 한 턴에 두 번 나오는 것, brainstorm 3단계의 "quarter-long bets (longer)", interview 2b(1라운드 첫 질문)가 두 가지(확실한 것·가정한 것)를 묻는 것(실행에서는 한 질문으로 묻는다, 8회 중 8회). tweakable-plan 1b와 quiz 채점 순서는 0.13.2에서 고쳤다. 권고: 놓침이 관찰된 것만 실행과 함께 고친다 | 소유자 결정 대기 | `IMPLEMENTATION_NOTES.md` 2026-11-17 |
| README 시나리오 A의 붙여 넣기 문장을 쓰는 평가 케이스를 저장소에 둘지(케이스 전에는 테스트 상수만 그 문장을 고정했다), 중복 문장 제거를 한 문장씩 그 스킬의 케이스를 돌리면서 다시 시도할지(후보 15개: 처음부터 남긴 9개와 지웠다가 되돌린 6개). 권고: 케이스는 더하고(`evals/neg-open-weighty-memory-line-en`의 `append_system_prompt` 틀로), 중복 문장은 실행으로 필요 없음이 보일 때까지 그대로 둔다. **케이스 추가, 첫 실행 대기**(2026-11-24): `evals/neg-open-weighty-pasted-sentence-en` — memory-line 케이스와 같은 마이그레이션 요청에 README 문장을 글자 그대로 `append_system_prompt`로 넘기고(메시지로 붙여 넣는 것보다 무게가 클 수 있다), 채점 문구도 memory-line 케이스와 같다(2–3줄 되읽기, 확인 대기, 방법 없음, unknowns 스킬 로드 없음). 문장의 뒤 절반(완료 기준마다 근거, 성과 질문)은 한 턴에 닿지 않아 채점하지 않는다. `tests/test_portability.py`는 이제 테스트 상수 대신 이 케이스의 문장을 두 README의 코드 블록과 대조한다. 중복 문장 제거는 권고대로 그대로 둔다 | 소유자 결정 대기 | `IMPLEMENTATION_NOTES.md` 2026-11-13 Todo for human (c)(d)와 "Removed at first, then back"·"Left as they were" 표 |
| 두 번째 규칙 기반 리뷰(0.12.4)에서 보류한 항목(공용 문장, 파일 사이 이름, 스킬별 방법 결정)이 2026-11-10 "the rest kept"로 닫혔는지. 권고: 닫혔다고 확인한다. interview 프롬프트 내용과 deviation-log의 "where did we diverge" 갈래는 다른 행에 열려 있다 | 소유자 결정 대기 | `IMPLEMENTATION_NOTES.md` 2026-11-09 Todo for human, 2026-11-10 |
| 붐비는 설정(다른 플러그인 스킬이 많이 실린 목록)에서의 라우팅 재측정. 0.13.1 때 소유자 설정(스킬 98개)에서 `interview-deep-grill`이 interview를 로드하지 못했다(1회 중 0회, 격리 설정은 3회 중 3회). 권고: 다음 릴리스에서 `evals/run-manual.py --crowd`를 3회 돌린다(마지막 측정 2026-09-30, 그 뒤 0.13.0에서 설명이 크게 줄었다) | 소유자 결정 대기 | `docs/trigger-eval-crowd-2026-09-30.md`, `IMPLEMENTATION_NOTES.md` 2026-09-30·2026-11-17 |
| teach-back 인용(Johnson & Johnson 1987)을 확인하지 않았다. 동결 기록 `docs/value-contract.md`의 'B7의 측정 대상을 좁힐 수 있다' 절(지금 77행)이 표시 없이 인용한다. 확인할 후보: L. Johnson & N. E. Johnson (1987), "Knowledge elicitation involving teachback interviewing". 권고: 동결 기록이므로 이 표에만 미검증으로 적어 둔다 | 소유자 결정 대기 | `IMPLEMENTATION_NOTES.md` 2026-09-30(사각지대 리뷰 반영) |
| 0.13.2 리뷰에서 나왔고 손대지 않은 지적: quiz의 missing-tool 문장 위치(Part 1에 있고 파일 쓰기는 Part 2), deviation-log 1단계에 "where did we diverge" 질문용 갈래가 없음, teach-me 7b 초안의 가정 표시(0.13.2 실행은 통과, 아래 '지켜볼 칸') | 소유자 결정 | 이 행 |
| 공용 deviation log 문장(`.claude/rules/skill-writing.md` 11번의 공용 블록, buy-in·quiz·unknowns-loop 본문)은 코드 작업의 로그를 "`IMPLEMENTATION_NOTES.md` by default"라고 적지만, deviation-log 2단계의 로그 파일 표에는 코드 작업에 사용자가 지정하는 파일이 없다. 2026-11-24 정리는 interview 붙여 넣기 프롬프트의 문장을 11번의 예외로 적었을 뿐(소유자 결정) 이 차이는 그대로 두었다. 권고: 다음 deviation-log 변경 때 함께 맞춘다 | 소유자 결정 대기 | `skills/deviation-log/SKILL.md` 2단계 표, `.claude/rules/skill-writing.md` 11번 |
| 실행이 닿지 않는 문장에 평가 케이스 추가: 스킬이 scout를 부르는 큰 작업(조건과 판정 패킷), interview 제안을 받아들인 뒤의 tweakable-plan, 옵션 둘인 prototypes, 입력 없는 quiz·reference, 비코드 작업의 quiz·unknowns-loop 로그 찾기(0.13.2), brainstorm의 scout 목록, 대상을 이름하지 않은 prototypes의 질문, 부분 재시도 뒤 quiz 점수(0.12.4). **케이스 추가, 첫 실행 대기**(2026-11-24, 모두 아직 돌리지 않음): 스킬이 scout를 부르는 큰 작업 → `behavior-blindspot-scout-many-contracts`(공급 계약 214건, 패킷이 양쪽 가정을 싣고 scout가 가정마다 held / wrong / still unchecked로 판정), brainstorm의 scout 목록 → `behavior-brainstorm-scout-inventory-monorepo`(서비스 41개 모노레포, 패킷이 기존 장치 목록을 요청하고 후보가 그 행 위에 선다), interview 제안을 받아들인 뒤의 tweakable-plan → 다회차 `tweakable-plan-after-interview-accepted`(수락 뒤에는 계획 대신 질문이 오고, 다시 보인 계획이 답 위에 선다), 옵션 둘인 prototypes → 다회차 `prototypes-two-options-contrast`(5a의 차이 질문이 triad를 대신한다), 입력 없는 quiz·reference → `behavior-quiz-asks-for-the-work`·`behavior-reference-asks-for-the-reference`(작업이나 참고 자료를 묻는 질문 하나), 대상을 이름하지 않은 prototypes의 질문 → `behavior-prototypes-asks-target-first`(대상을 묻는 질문 하나, 버전 없음), 비코드 작업의 로그 찾기 → `behavior-quiz-finds-noncode-log`(여섯 질문 중 하나 이상이 산출물 옆 `DEVIATIONS.md`에 적힌 벗어남)·`behavior-unknowns-loop-finds-noncode-log`(사용자가 알린 벗어남을 산출물 옆 기존 `DEVIATIONS.md`에 덧붙임), 부분 재시도 뒤 quiz 점수 → 다회차 `quiz-partial-retry-score`(놓친 문항만 다시 묻고, 놓친 부분을 모두 맞혀야 6/6). scout 케이스 둘의 채점 항목 셋(`packet-carries-both-sides-assumptions`, `scout-marks-each-assumption`, `packet-asks-for-inventory`)은 scout를 부른 Agent 호출의 `prompt`(패킷)를 봐야 하는데, 저장소 밖 판사 보조 도구는 그것을 넘기지 않는다. 판사에 넘기거나 `manual-result.json`의 `tool_calls`를 읽고 손으로 판정한다 | 에이전트, 다음 릴리스 점검 때 | 각 케이스 폴더, `evals/README.md` 'What the suite covers' |
| unknowns-loop 단계를 끝까지 돌리는 다회차 평가 케이스(체크리스트 도입 판단의 근거). `unknowns-loop-criteria-unanswered`(0.12.4)는 2단계와 다음 답까지만 본다. **케이스 추가, 첫 실행 대기**(2026-11-24): 다회차 `unknowns-loop-every-stage-to-outcome-check` — 독서 모임을 휠체어로 갈 수 있는 도서관 방으로 옮기는 비코드 작업에서, 단계가 순서대로 돌거나 건너뛴다고 이유와 함께 말하는지, 2단계의 완료 기준이 검증까지 이어지는지, 작업이 부딪친 벗어남(도서관은 다음 달 예약만 받는다)이 기록되는지, 루프가 사용자가 정하는 성과 확인으로 끝나는지 본다. `user_turns`가 러너 최대치 8이라 한 번만 더 주고받아도 끝까지 못 갈 수 있으니, 판정을 읽기 전에 멈춘 이유를 본다 | 에이전트, 다음 릴리스 점검 때 | `evals/multiturn/unknowns-loop-every-stage-to-outcome-check`, `docs/skill-authoring-guide.md` 체크리스트 행 |
| 자동 로드된 스킬에서의 되읽기 문단 측정(0.13.0의 되읽기 실행은 이름으로 부른 스킬만). **케이스 추가, 첫 실행 대기**(2026-11-24): `behavior-tweakable-plan-autoloaded-reads-back`("make a plan", 오늘 밤 배포하는 nginx 설정 한 줄)과 `behavior-buy-in-autoloaded-reads-back`("get sign-off", 오늘 보내는 라이선스 갱신 메일, 비코드). 둘 다 2–3줄 되읽기와 확인 대기, 방법 없음을 보고, 스킬이 로드된 실행에서만 읽는다(트리거 문구로 로드될지 자체가 불확실하다). tweakable-plan 쪽은 3단계 크기 관문과 맞선다 | 에이전트, 다음 릴리스 점검 때 | 두 케이스 폴더, `CHANGELOG.md` 0.13.0 **Checked** |
| 2026-11-24 정리에서 소유자가 따로 정하지 않은 두 가지를 확인하거나 바꾼다: (1) 언어 규칙에 붙인 절 "기존 한국어 문서 안의 편집(동결 배너 포함)은 그 문서의 언어를 따른다"(`AGENTS.md` 3행), (2) 감사 결정 5–22와 33을 권고대로 적용한 것 | 소유자 결정 대기 | `IMPLEMENTATION_NOTES.md` 2026-11-24 |
| 2026-11-24 정리에서 채점이나 판사 동작이 바뀐 케이스를 다음 릴리스 점검에서 다시 돌리고, 결과를 그 릴리스의 **Checked** 절에 적는다: `behavior-tweakable-plan-opens-with-done-criteria`, `behavior-interview-max-four-questions`(채점기 문구), 다회차 `quiz-hides-key-and-gates-on-six`(가상 사용자의 스코어카드 질문 분기 삭제), `interview-deep-grill`, `interview-rounds-stay-at-four`(`--judge`, 판사 프롬프트와 채점기의 판정 줄 문구) | 에이전트, 다음 릴리스 점검 때 | `CHANGELOG.md` [Unreleased] **Not measured** |
| 릴리스 본문이 태그 메시지가 아니라 머지 커밋 메시지로 채워진다(0.13.0·0.13.1·0.13.2 세 번 손으로 바꿈). 2026-11-24 정리에서 `release.yml`의 `gh release create` 앞에, 태그를 원격에서 다시 받아 주석 태그인지 확인하는 두 줄을 넣었다(검증하지 않은 가설: checkout이 태그를 경량 태그로 남겨 `--notes-from-tag`가 커밋 메시지를 읽는다). 확인 줄이 실패하면 Release 단계는 릴리스를 만들기 전에 멈춘다. 다음 릴리스에서 워크플로가 통과하는지, 본문이 태그 메시지인지 보고, 두 줄을 남길지와 '릴리스 절차'의 수동 확인을 뺄지 정한다 | 다음 릴리스 때 | `.github/workflows/release.yml`, 아래 '릴리스 절차' |
| 이름 없는 리뷰·조사 요청이 두 에이전트(independent-reviewer, unknowns-scout)에 가로채이는지: 0.12.0 설명 변경 뒤 다시 재지 않았다. 네거티브 케이스 두세 개를 만들어 릴리스 점검에 넣는다(소유자 결정 2026-11-24, `docs/features/agent-collision/`은 0.9.2 기록으로 동결). **케이스 추가, 첫 실행 대기**(2026-11-24): `neg-unnamed-review-does-not-spawn-reviewer`(0.9.2 `f-rv-indep-en`, 병합 전 브랜치의 독립 리뷰, git 저장소), `neg-unnamed-investigation-does-not-spawn-scout`(0.9.2 `s-pre-en`에서 "for risks" 대신 이름 붙은 검색 대상. "for risks"는 blindspot의 영역에 가까워 스킬 가드를 판정할 수 없게 하므로 바꿨고, 그래서 0.9.2에서 10회 중 10회 가로채인 문구보다 약한 탐침이다), `neg-unnamed-report-check-does-not-spawn-reviewer`(`behavior-independent-reviewer-report-vs-records`의 자료를 에이전트 이름 없이, 비코드). 셋 모두 두 에이전트를 부르지 않고 unknowns 스킬도 로드하지 않아야 하며, 결과 채점기가 요청이 처리됐는지 본다. 하위 에이전트를 하나도 부르지 않은 실행은 가드를 그냥 통과하므로 `spawns-a-subagent` 지시자를 함께 읽는다 | 에이전트, 다음 릴리스 점검 때 | `evals/neg-*`의 기존 형식, `docs/features/agent-collision/` |

## 지켜볼 칸 (칸마다 최신 수치)

- deviation-log 답사 케이스(`behavior-deviation-log-logs-unplanned-difference`): 비밀번호 절을 뺀 뒤 로그 5회 중 1회(HTML 주석), 계획서 5회 중 5회(0.13.2). 다시 나오면 Don't log에 "비밀 값" 항목을 따로 두는 문장을 2회 돌린다.
- tweakable-plan `alternatives-are-lettered`: 0.13.2 릴리스에서 판사 호출 거부로 판정 없음. 스크립트로 세면 결정 항목 일곱 개 모두 글자 붙은 대안과 기각 이유가 있었다.
- blindspot 다회차 `assumption-verdicts-carry-status`(4a 단계): 0.13.2 4회 중 1회. 놓친 실행은 자기 가정 하나에 판정이 없거나, 사용자의 말에 없는 사실을 "held"로 사용자에게 돌렸다.
- blindspot·brainstorm의 scout: 기록된 실행 14회(케이스 둘, Fable 5.2 1회 포함, 0.13.2 때 집계)에서 호출 0회. 직접 다 읽을 수 없을 만큼 큰 작업의 케이스 둘(`behavior-blindspot-scout-many-contracts`, `behavior-brainstorm-scout-inventory-monorepo`)을 2026-11-24에 더했고, 아직 돌리지 않았다.
- interview: 늦은 라운드의 재질문(`deeper-not-padded`, 0.13.1에서 4b 문장 전 5회 중 2회, 0.13.2 릴리스 1회 통과), 3라운드의 why 후속 순서(`questions-carry-reasons-in-priority-order`, 0.13.1 릴리스에서 놓침, 0.13.2 릴리스 1회 통과), 2b의 "Settled items are not asked again"이 1라운드에만 걸리는 것으로 읽히는지. 정렬 하위 단계는 두 위치 모두 다른 칸을 흔들었으므로 다시 시도하지 않는다(0.12.2).
- quiz `key-hidden-until-answered`: 정답 보기가 다른 보기보다 길다(0.13.2 3회 중 2회, 0.12.3부터 보던 모양).
- brainstorm: 후보 제목을 지시형으로 씀(0.13.1 릴리스에서 놓침, 0.13.2 릴리스에서 그 케이스 1회 통과).
- teach-me 7b: 초안의 가정 표시(`draft-with-assumptions`, 0.13.1 놓침, 0.13.2 통과).
- blindspot: 이름으로 부르고 자명한 요청("sort the import lines")을 주면 되읽기 문단이 있어도 방법을 실행했다(0.13.0, 2회 중 2회). 다시 돌리지 않았다.
- 짧은 설명에서 빠진 문구(blindspot "run it even when you could answer directly", tweakable-plan "Not native plan mode")와 quiz 설명의 범위 문구("work the model largely produced"), 0.13.0부터. 0.13.1·0.13.2 릴리스 실행에서 `trigger-ko-blindspot`과 `neg-open-quiz-en`은 놓치지 않았다.
- buy-in 3단계 "실행되는 데모나 스크린샷"과 대화 안 Markdown 문서가 어긋날 수 있다(독립 검토 지적, 2026-11-17). 그날 buy-in 실행 넷은 채점을 모두 통과했다.
- 되읽기 문단: "둘 다 이해한 요청이면 방법 없이"를 스킬 산출물을 직접 요청한 경우("quiz me")까지 건너뛰라는 뜻으로 읽는 검사자 지적이 있다. 실행에서 건너뛴 적은 없다. 건너뛰는 실행이 나오면 범위를 "이 스킬 자체의 산출물 요청이 아닌 경우"로 좁힌다.
- 검토 에이전트를 buy-in을 거치지 않고 이름으로 부를 때, 호출한 모델이 사용자에게 전하는 요약에서 에이전트의 성과 판정이 빠진 적이 있다(0.12.1, 3회 중 3회). 그 뒤 채점기는 에이전트 보고서를 보고, 요약 쪽은 따로 재지 않았다.
- 0.12.3의 1회 실수: prototypes가 이유 없는 skip에 대비 질문을 하지 않음, blindspot *inferred* 카드에 근거 누락.
- unknowns-loop(영어): 첫 답에 변경 범위 누락(0.12.4, 9회 중 8회 통과). `noncode-en-unknowns-loop`의 `first-reply-covers-step-2`: 0.13.1 최종 문구 2회 중 1회(놓친 1회는 완료 기준을 사용자의 일이 아니라 루프 산출물 기준으로 물었다), 0.13.2 릴리스 1회 통과.
- quiz(한국어): 해설이 Q2의 수치를 그대로 풀어 줌(0.12.4).
- teach-me: 와인 어휘를 말없이 구매 상황으로 틀 잡음(0.12.4, 3회 중 2회 통과).
- interview(한국어) `noncode-ko-interview`: 1라운드 이유 줄이 두세 문장(0.13.1, 1회 중 0회, 0.13.2 릴리스 1회 통과).
- Codex에서만(Claude에서는 통과, 본문은 고치지 않음): interview 1라운드가 다음 라운드를 예고하지 않음, tweakable-plan이 완료 기준을 "completion criteria"로 써서 정규식 채점만 놓침(0.12.1).

## 릴리스 절차

- 지원 모델은 Opus 5.5·GPT-6.1 Sol, medium effort(소유자). 평가 러너는 기본 `--effort medium`. 실행 회수는 `docs/skill-authoring-guide.md`의 표를 따른다(수정 확인은 실패 케이스 2회, 이웃 1회, 릴리스는 Opus 전체 1회 + Sol trigger 1회). 배포 본문을 바꾸면 버전을 올리고, `[Unreleased]`가 비어 있지 않을 때만 같은 버전 재생성이 허용된다.
- 측정 결과는 그 버전 `CHANGELOG.md`의 **Checked**·**Not measured** 절에 적는다(원자료 `evals/results/`는 gitignore). `docs/trigger-eval-*.md`는 동결된 기록이다.
- 평가 보조 도구(판정 스크립트, 릴리스 실행 스크립트, Sol 확인 스크립트)는 소유자의 사설 프로브 스크립트(저장소 밖)다. 판사 호출도 러너와 같은 격리 환경으로 돈다(2026-11-17). 다음 릴리스의 실행 스크립트는 결과 폴더 설정만 고쳐 쓰면 된다(러너 기본값이 격리다).
- 순서: 소유자 승인 후 `plugin-manifest.json` 버전 → CHANGELOG 이동 → 재생성 → CI → 머지 → 주석 태그 `unknowns--vX.Y.Z` → 릴리스 자산 sha256 대조 → 빈 설정 설치 확인 → 카탈로그 확인 → 릴리스 본문이 태그 메시지인지 확인(아니면 태그 메시지로 바꿔 넣는다. 0.13.0–0.13.2는 워크플로가 머지 커밋 메시지로 채웠다).
- GPT-6.1 Sol 확인은 0.13.2부터 WSL에서, 격리한 HOME과 `CODEX_HOME`으로 돌린다. Codex 로그인이 ChatGPT 로그인이라 환경 변수로 넘길 토큰이 없어서 `auth.json`을 격리한 홈에 복사한다. 사본이 혼자 갱신되면 원래 로그인이 끊길 수 있으므로, 먼저 평소 홈에서 `codex exec`를 한 번 돌려 토큰을 거기서 갱신시킨 뒤 복사하고, 끝나면 두 파일의 `last_refresh`가 같은지 본 다음 사본을 지운다.
- GPT-6.1 Sol 확인 때 지킬 것(0.13.0에서 발견): Codex 앱은 소유자 계정에 올려 둔 플러그인 사본(당시 0.12.4)을 격리한 홈의 `.codex/plugins/cache/created-by-me-remote`로 동기화한다. 0.13.0의 처음 세 번 시도에서는 22개 세션 중 7–8개가 빌드 옆에 그 사본을 나열하고 그 사본의 `SKILL.md`를 읽었으므로, 세 번 모두 무효로 했다. `config.toml`의 `[features] remote_plugin = false`와 `[plugins."unknowns@created-by-me-remote"] enabled = false`는 막지 못했다. 막은 방법: 플러그인을 추가하기 전에 격리한 홈에 그 캐시 폴더를 미리 만들고 읽기 전용(`chmod 555`)으로 둔다. 실행 뒤에는 세션 기록에서 `created-by-me-remote/unknowns`가 0건인지, 22개 실행이 모두 빌드 버전의 `SKILL.md`를 읽었는지 센다(0.13.0: 0건, 22/22). 이전 릴리스의 GPT-6.1 Sol 확인에는 이 장치가 없었다.

### 설명을 고친 뒤 다시 재는 방법

- `evals/run-manual.py`로 `trigger-*` 22개, `noncode-*` 22개, `unknown-*` 4개, `neg-*` 17개(2026-11-24에 넷 추가)를 케이스당 1회(설명을 고친 뒤의 확인) 또는 의심 가는 케이스만 3회(`docs/skill-authoring-guide.md`의 실행 회수 표). 설명을 고치면 `SKILL.md`와 `scripts/skill-descriptions.json`을 함께 고친다(테스트가 두 사본의 일치를 본다).
- 스킬별 업로드 zip(`scripts/build-skill-zips.py`)은 frontmatter를 JSON 따옴표 형식으로 다시 쓴다. `run-manual.py --verify --plugin-dir <zip을 푼 디렉터리>`는 그 형식의 description을 읽지 못해 거짓 실패를 낸다(실행 경로에는 영향 없음).
- claude.ai 자체의 라우팅과 업로드 화면은 headless로 돌릴 수 없어 어느 기록도 보여 주지 않는다.

## 규칙

- 모든 판단은 `.claude/rules/skill-writing.md` 0번(세 칸, 어떤 분야든, 성과)을 따른다. 코딩은 여러 예 중 하나다.
- 구조: 원본 `skills/`(스킬마다 SKILL.md 하나, 공유 참조 파일 없음), `claude-code/agents/` → `tools/package.py`가 `plugins/unknowns/`와 두 zip을 생성(커밋됨). 코드 없음, 목록 아이콘 PNG 하나.
- 작성 원칙: `.claude/rules/skill-writing.md` 0번(목적)과 17번 — 금지 문장·읽기 전용 약속·도구 허용 목록·정체성 문장("You are …")을 쓰지 않는다. 강제는 사용자 하네스의 몫이다. 두 에이전트는 모든 도구를 물려받고, 플러그인은 git 절차를 따로 두지 않는다.
- 스킬 설명은 200자 이하이고 `scripts/skill-descriptions.json`과 같은 문구다(`.claude/rules/skill-writing.md` 18번). 설명을 고치는 것은 라우팅을 고치는 것이므로 trigger·비코딩·네거티브 케이스를 다시 돌린다.
- 설명을 skill-creator 권고대로 더 적극적으로("pushy") 쓰지 않는다(소유자 판단 2026-10-28). 판단 당시 빌드(0.12.0–0.12.1)의 라우팅은 이름 44/44(0.12.0), 한국어 blindspot 트리거 10/10, Codex 18/18이었다.
- 본문의 되읽기 문단, 라우팅 문장, 칸 문장은 모든 스킬에 남긴다(소유자 판단 2026-11-13).
- 스킬의 목표·산출물이나 단계의 이유를 말하는 문장은 중복처럼 보여도 지우지 않는다(`docs/features/concise-plugin-text/06-results.md`; 0.13.0에서 그런 문장 넷을 지웠다가 되돌렸다).
- teach-me의 예(색 보정 한 분야)는 유지한다. 비교 표가 글·코드·절차를 다루고 비코딩 케이스가 통과한다(소유자 판단 2026-10-28).
- unknowns-loop·tweakable-plan 2단계의 "Outcome, as stated / as read" 두 줄은 같은 문장으로 다시 시도하지 않는다. 두 줄이 있을 때 `noncode-en-unknowns-loop`의 `first-reply-covers-step-2`가 성과 항목을 3회 중 2회 놓쳤다(요청문을 성과로 인용하고 사용자가 궁극적으로 바라는 것까지 가지 않음, 2026-11-17). 다시 한다면 산출물의 말과 성과의 말을 가르는 문장이 필요하다는 것이 그 실행의 읽기다(작성자 해석).
- 모델이 읽는 파일을 고치면 writing-for-models 점검: 고친 diff를 글쓴이가 아닌 검사자 한 명이 한 번 읽는다(파일별 점검 없음, `docs/skill-authoring-guide.md` 실행 회수 표). 이 플러그인은 소유자 판단으로 Claude 검사만 한다. 검사자가 금지 문장을 제안하면 할 일 문장으로 바꾸거나 버린다(17번).
- 소유자는 버전 간 A/B 비교를 원하지 않는다. 플러그인 자체의 실행에서 실패를 읽고 고친다.
- 공개 텍스트(커밋 메시지, PR 제목·본문, README, CHANGELOG, docs)에 소유자 개인 약칭이나 내부 작업 용어를 쓰지 않는다.
- main에 직접 커밋하지 않는다. 작업은 브랜치에서, 푸시·태그는 소유자 승인 뒤(AGENTS.md Release).
- 기록이 인용하는 커밋이 squash 머지로 main에 없는 작업 브랜치는 지우지 않는다: `docs/dia-regula-audit`(0.12.4, `IMPLEMENTATION_NOTES.md` 2026-11-10이 `0cbbf69`·`e4f05dd`·`3221f7d`를 인용), `short-descriptions`(0.13.0, CHANGELOG 0.13.0과 `IMPLEMENTATION_NOTES.md`가 `63e0360`·`02484af`·`c515a4d`를 인용).

0.13.1 이전의 인계 문단, 끝난 일 서술, 릴리스별 지켜볼 칸 목록(`IMPLEMENTATION_NOTES.md` 2026-11-17 항목이 가리키는 목록 포함)은 2026-11-24 정리에서 지웠다. 커밋 `d9daf07`의 `docs/handoff.md`에 있다.
