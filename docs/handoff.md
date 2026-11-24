# 다음 라운드 인계 — 0.13.3 준비

새 세션은 이 문서의 상태를 git·태그·릴리스·CI와 먼저 대조하고 시작한다. 이 문서는 작업 지시가 아니라 출발점이다.

## 상태

0.13.3 준비(2026-11-24, 브랜치 `cleanup/stale-docs-2026-11-24`, 소유자의 병합과 태그 대기): 0.13.2 기준 저장소 문서 정리(감사 252건, 반박 8건, 고유 200건), 설명 여섯 개(quiz·interview는 "you"를 모델로, teach-me "Not a blind-spot pass on a plan.", blindspot "an improved prompt", brainstorm "NOT for design options.", deviation-log 자동 시작처럼 읽히던 구절 교체), deviation-log 2단계 코드 행(사용자가 지정한 파일 우선), 평가 케이스 20개, 다회차 러너의 한국어 요청 인식. quiz의 "or before merging"은 뺐다가 규칙대로 되살렸다(없이 0/3, 있으면 3/3). 실행 결과와 판정은 `CHANGELOG.md` 0.13.3, 결정과 실행 전 규칙은 `IMPLEMENTATION_NOTES.md` 2026-11-24 두 항목. 원자료는 `evals/results/round-2026-11-24/`(로컬, gitignore). GPT-6.1 Sol trigger는 태그 전에 커밋 `31249e4`에서 22/22(WSL, 격리한 홈, 모든 세션이 0.13.3 빌드의 `SKILL.md`를 읽음, 계정 사본 언급 0건).

배포 중인 버전은 `unknowns--v0.13.2`이다(2026-11-22, PR #40, main `dfb0bb9`). 릴리스 자산 두 개의 sha256이 커밋된 zip과 일치하고(`know-your-unknowns.zip` `55c80740…`, `know-your-unknowns-openai.zip` `0233cc69…`), 빈 설정 설치가 자체 마켓플레이스와 `ajitta/claude-plugins` 두 경로 모두 0.13.2에 스킬 폴더 11개, 에이전트 2개였다. 릴리스 본문은 이번에도 워크플로가 머지 커밋 메시지로 채워서 태그 메시지로 바꿔 넣었다. 원격 작업 브랜치 `audit-fixes-2026-11-22`는 지우지 않았다.

0.13.2에 들어간 것(스킬 본문 열 개와 unknowns-scout, 설명은 그대로): deviation-log(Don't log에서 비밀번호 절 삭제), quiz(teach-back은 키의 요점 전부, 채점과 해설은 여섯 답 뒤, 입력이 없을 때의 문장), blindspot·brainstorm(scout는 직접 다 읽을 수 없을 만큼 많은 자료일 때), blindspot·scout(가정마다 held / wrong / still unchecked 판정을 돌려받음, 첫 초안은 모든 fix 적용), tweakable-plan(interview를 제안하고 같은 답에서 계획), unknowns-loop(1단계 제목, "nothing is scored" 삭제), prototypes(옵션 둘이면 triad 대신 차이 질문), reference(입력이 없을 때의 문장, Output을 5단계에 맞춤), buy-in·quiz·unknowns-loop(공용 deviation log 문장에 비코드 파일), teach-me·brainstorm·deviation-log·tweakable-plan(문구만). OpenAI 목록의 긴 설명 한 문장이 바뀌었다("labeled passes" 삭제).

소유자가 확인한 표면(2026-10-28, 0.12.2, 소유자 보고이며 화면 증거는 기록하지 않음): ChatGPT zip 업로드와 ChatGPT 모바일의 스킬 호출, claude.ai의 Add marketplace 설치가 Claude 모바일로 이어지는 것. claude.ai zip 업로드는 마켓플레이스 경로가 모바일까지 이어지므로 하지 않는다(소유자 판단). 소유자가 확인하지 않은 경로: claude.ai zip 업로드, Claude 데스크톱, Codex CLI, ChatGPT 데스크톱 마켓플레이스. 소유자 확인이 아닌 기록된 자동 실행: Codex CLI 실행(0.10.0, 0.12.1, 그리고 0.12.3부터 릴리스마다 GPT-6.1 Sol trigger), 두 마켓플레이스에서의 빈 설정 Claude Code 설치(0.12.3부터 릴리스마다).

### 0.13.2 릴리스에서 (2026-11-22, PR #40)

- 시작: 소유자가 `skills/`에 프롬프트 감사를 요청했다. 감사는 낡은 문구 패턴을 거의 찾지 못했고, 소유자가 요청한 독립 리뷰 둘(감사를 결론 없이 다시 돌린 것, 본문을 실행하는 모델 쪽에서 읽은 것)이 기록된 실행을 열어 본문 문장이 행동을 바꾸거나 정하지 못하는 곳을 찾았다. 감사의 첫 결론("깨끗함")은 그 뒤에 고쳤다.
- 소유자 결정(2026-11-22): 네 묶음 승인(비밀번호 절 삭제, quiz 두 문장, scout 조건, README·OpenAI 목록의 사실 수정), quiz 두 질문의 답(teach-back은 요점 전부, 채점은 여섯 답 뒤), 이어서 남은 지적 처리와 릴리스 지시.
- 독자 확인: 글쓴이가 아닌 독자가 두 묶음을 각각 전후 비교했고, 실행 전에 여덟 문장을 그 지적대로 고쳤다(첫 묶음 다섯, 둘째 묶음 셋).
- 수정 확인(격리, Opus 5.5, medium, Claude Code 2.1.330, 기준은 실행 전에 적음): 답사 케이스 2회 중 2회가 비밀번호를 계획서에 적고 로그에는 넣지 않았다. quiz 다회차 3회 중 3회가 여섯 답 뒤에 채점했고 키가 요점 전부를 요구했다(`key-hidden-until-answered`는 3회 중 2회, 놓친 1회는 선택지 길이 쪽). scout 케이스 둘은 점수 항목 1회 중 1회, scout 호출 0회.
- 릴리스 점검(전체 1회): 단발 88케이스 채점 항목 194/206(점수에 드는 항목 125/134, 0.13.1과 같은 수), 다회차 13케이스 29/32. 0.13.1 때 통과했다가 놓친 `logs-the-public-rename`과 `free-text-corrections-applied`는 2회씩 다시 돌려 2회 중 2회였다(후자는 첫 실행과 다시 돌린 2회 모두 가상 사용자가 한 번도 답하지 않은 대화였고, 다시 돌린 2회는 판정할 정정 없이 통과했다). 나머지 누락은 0.13.1과 같은 칸이다.
- GPT-6.1 Sol medium: trigger 22/22. 릴리스 뒤 같은 날 태그 `unknowns--v0.13.2`(커밋 `dfb0bb9`)에서 돌렸다. Codex CLI 0.164.0, WSL(Ubuntu), 격리한 HOME과 `CODEX_HOME`, 읽기 전용 캐시 폴더 가드 사용. 22개 실행 모두 0.13.2의 `SKILL.md`를 읽었고 계정 사본을 읽은 세션은 0건이다. 태그 메시지와 릴리스 본문은 "Sol 미실행"이라고 적고 있고(릴리스 시점에는 사실), CHANGELOG는 그 뒤에 고쳤다.
- Sol 확인을 WSL에서 한 것은 이번이 처음이다(방법은 아래 '릴리스 절차').
- 감사와 리뷰가 그대로 두기로 한 것: 되읽기 문단, 설명 속 "NOT", 개수 지정(질문 4개, 6문항 등), interview의 "start with a short plan", buy-in의 리뷰어 호출과 unknowns-loop 5a의 Verify(Opus 5의 "검증 지시를 지워라" 행에 걸리지만 방법의 일부), teach-me의 색보정 예시(비코드 실행에 새지 않음).

## 남은 일

열린 일은 이 표 하나로 추적한다. '소유자 결정 대기'는 2026-11-24 정리에서 소유자가 아직 정하지 않은 항목이고, 행 안의 '권고'는 그 정리의 권고다. 끝난 행은 지우고, 결과는 `CHANGELOG.md`와 `IMPLEMENTATION_NOTES.md`에 남긴다. `IMPLEMENTATION_NOTES.md`의 Todo for human 가운데 이 표에 없는 것은 풀렸거나 무의미해졌다(2026-11-24 판정).

| 남은 일 | 누가 | 어디서 시작 |
|---|---|---|
| ChatGPT에 `know-your-unknowns-openai.zip` 재업로드. 0.13.2에서 목록 문장 하나와 스킬 본문 열 개가, 0.13.3에서 설명 여섯 개와 예시 프롬프트의 `$unknowns:` 표기가 바뀌었다. 올릴 때 예시 프롬프트가 목록에서 어떻게 보이는지 본다 | 소유자(직접 하기로 함) | GitHub Release `unknowns--v0.13.3`(태그 뒤) |
| claude.ai(Add marketplace 경로)가 0.13.3을 받았는지 확인(태그 뒤) | 소유자 | claude.ai Customize › Plugins |
| 평가 실행이 계정에 만든 문서 "On-call rotation bot: requirements" 삭제(소유자가 직접 지우기로 함, 2026-11-17, 완료 기록 없음) | 소유자 | Claude Code `/artifacts` 또는 claude.ai |
| 저장소 밖 판사 보조 도구의 프롬프트 고치기: "one line of reasoning per numbered criterion"이 Opus 5.5의 안전 분류기(`reasoning_extraction`)에 막힌다(0.13.2 릴리스에서 한 채점 항목이 두 번 막힘). 저장소 안의 다회차 판사 프롬프트(`evals/run-multiturn.py`)는 2026-11-24 정리에서 번호 기준마다 근거를 인용한 한 줄 판정을 묻도록 바꿨고, 채점기 둘(`deeper-not-padded`, `every-round-at-most-four`)은 "In your reasoning" 대신 판정 줄에 근거를 인용해 적게 했다. 같은 방향으로 바꾼다 | 소유자(저장소 밖) | 소유자의 사설 프로브 스크립트(저장소 밖) |
| 동결 기록 `docs/protocol-alignment.md` 3행에 소유자의 개인 볼트 경로가 남아 있다. 동결 기록이라 2026-11-24 정리에서 그대로 두었다. 지울지 정한다 | 소유자 결정 | `docs/protocol-alignment.md` 3행 |
| B8 brainstorm 충돌 재현(`docs/open-questions.md`에서 옮김, 2026-11-24): 소유자 보고("review·brainstorm 같은 스킬이 의도하지 않게 트리거") 중 brainstorm 쪽은 Claude Code CLI 기록(Skill 호출 270건, 의도하지 않은 것 0)과 dia·design·SuperClaude 동반 단발 스크린에서 재현되지 않았다. 소유자가 본 문장과 표면(claude.ai·데스크톱·모바일 포함)을 받아 그 조건으로 재현한 뒤에만 설명을 고친다 | 소유자가 사례를 줄 때 | `docs/open-questions.md` B8, `docs/features/agent-collision/` |
| ChatGPT·claude.ai에서 짧은 설명의 라우팅. claude.ai의 라우팅은 헤드리스로 돌릴 수 없고, Codex는 trigger 22개만 돌렸다 | 소유자 | `IMPLEMENTATION_NOTES.md` 2026-11-13 |
| 소유자가 손으로 확인하지 않은 표면(Claude 데스크톱, ChatGPT 데스크톱 마켓플레이스) 확인. 필요하다고 볼 때만 | 소유자 | 위 '상태'의 표면 문단 |
| interview의 두 규칙을 함께 다루기: (1) 정한 항목은 다시 묻지 않는다(사용자의 두 결정이 함께 성립할 수 없을 때만 둘을 이름 대고 다시 묻는 예외 포함). 2b에 "Settled items are not asked again"은 있지만 4b 문장은 0.13.1 릴리스 전에 뺐다. (2) 바로 쓸 프롬프트는 사용자가 정한 것만 정해진 것으로 보인다(모델이 덧붙인 요구를 표시한다. 지금 Final Deliverables는 건너뛴 질문만 표시한다). 소유자 결정(2026-11-24): 다음 interview 변경 때 함께 다룬다 | 에이전트, 다음 interview 변경 때 | `IMPLEMENTATION_NOTES.md` 2026-11-17, `CHANGELOG.md` 0.13.1 |
| teach-back 인용(Johnson & Johnson 1987)을 확인하지 않았다. 동결 기록 `docs/value-contract.md`의 'B7의 측정 대상을 좁힐 수 있다' 절(지금 77행)이 표시 없이 인용한다. 확인할 후보: L. Johnson & N. E. Johnson (1987), "Knowledge elicitation involving teachback interviewing". 소유자 결정(2026-11-24): 동결 기록이므로 이 표에만 미검증으로 둔다 | 확인할 사람이 있을 때 | `IMPLEMENTATION_NOTES.md` 2026-09-30(사각지대 리뷰 반영) |
| teach-me 7b 초안의 가정 표시: `draft-with-assumptions`를 저장된 대화 6개에 지금 판사로 다시 매기면 6개 중 1개, 제안 문장("…and any default or choice you fill in from what you know of the domain…")을 넣은 사본으로 2회 돌리면 0회, 0.13.3 라운드 1회도 놓침. 실행은 세부 대부분에 표시를 붙이고 두세 개(대화 상자 동작, 대상 플랫폼, 코덱 값)를 확정처럼 적는다. 제안 문장은 채택하지 않았다. 권고(작성자): 문장을 늘리지 말고 지켜본다. 다시 손댄다면 초안 뒤에 '가정' 목록을 따로 두는 구조를 실행 전 규칙과 함께 2회 시험한다 | 소유자 결정 대기 | `evals/results/rejudge-teach-me-7b/`, `evals/results/h3-trial-2026-11-24/`(로컬), `IMPLEMENTATION_NOTES.md` 2026-11-24 |
| blindspot 2단계의 "more sources than you can read in full": 공급 계약 214건(약 820 KB, 레이아웃 넷과 문구 변형)에서도 blindspot은 스크립트로 직접 조사하고 scout를 부르지 않았다(2회, 두 번째가 이 자료, 두 번 다 판정은 맞음). 문장을 '문서마다 본문을 맥락에 읽기'로 볼지 '검색으로 모든 문서를 훑기'로 볼지 정한다(규칙 8). 앞 읽기면 조건을 그쪽으로 고치고, 뒤 읽기면 케이스의 scout 채점기 넷을 지시자로 바꾼다 | 소유자 결정 대기 | `evals/behavior-blindspot-scout-many-contracts`, `CHANGELOG.md` 0.13.3 **Checked** |
| tweakable-plan: 트리거 문구로 자동 로드된 명확하고 무게 있는 한 줄 변경("make a plan", 오늘 밤 배포할 nginx 설정)에서 되읽기 대신 3단계 첫 행의 짧은 계획(완료 기준 줄, 자기 모름 목록, 단계 여덟)을 냈다. 절차 위 되읽기 문단과 행동 자리의 3단계 첫 행이 같은 요청을 다르게 다룬다(규칙 1·2). 3단계 첫 행을 '둘 다 이해한 요청이 아닐 때'로 좁힐지, 무게 있는 명확한 요청은 크기 관문 앞에서 되읽을지 정한다 | 소유자 결정 대기 | `skills/tweakable-plan/SKILL.md` 3단계, `evals/behavior-tweakable-plan-autoloaded-reads-back` |
| 0.13.3 실행이 찾은 본문 지적(이번 라운드 규칙상 본문은 고치지 않음, 각 1–3회): tweakable-plan 1b(사용자가 말한 빈칸 넷 중 날짜와 이동이 '자기 모름' 목록 없이 모델이 고른 선택지로만 나옴)와 2단계(다시 보인 계획에 '지켜야 할 것'이 채워지지도 "not set"이지도 않음, `tweakable-plan-after-interview-accepted`), unknowns-loop 3단계 d(사용자만 할 수 있는 탐침을 계획 안으로 접어 넣어 계획이 탐침 결과 위에 서지 않음)와 루프 안 deviation-log 항목의 필드(Response chosen·Attributed 없음, `unknowns-loop-every-stage-to-outcome-check`), unknowns-loop 3단계 a(사용자가 작업을 설명할 수 있고 용어만 모를 때도 용어 안내를 조사 앞에 둠, `behavior-unknowns-loop-terms-only` 3회 중 0회이고 0.13.2 설명 빌드에서도 3회 중 0회, 0.13.2 릴리스 1회는 통과), buy-in(근거 없는 답을 한계로 옮기지 않고 빈칸이나 "확인 필요"로 남김, 한국어 두 케이스에서 이번 빌드 9회 중 3회·0.13.2 설명 빌드 7회 중 2회 통과), interview 1라운드(항목 안의 두 번째 질문, 3회 중 1회), brainstorm 2c(scout의 열린 항목 둘이 답에 오지 않음, scout를 부른 첫 기록된 실행), prototypes 1단계(대상이 없을 때 개수와 취향도 물음), blindspot `findings-labelled-by-evidence-status`와 buy-in `final-doc-keeps-unpicked-limits`(추가 2회 중 1회). 권고: 다음 측정에서 같은 칸이 또 놓치면 그 스킬의 다음 변경 때 한 문장씩 실행 전 규칙과 함께 고친다 | 소유자 결정 대기, 그 뒤 에이전트 | `CHANGELOG.md` 0.13.3 **Checked**, `evals/results/round-2026-11-24/`(로컬) |
| 붐비는 목록(다른 플러그인 스킬 60개, 목록이 설명 예산을 넘음)에서 blindspot이 로드되지 않는다: 2026-09-30 첫 측정과 2026-11-24 재측정(영어·한국어 6회 중 0회, 나머지 열 스킬은 60회 중 60회). 이름만 남는 조건에서 "blindspot"이라는 이름이 요청과 이어지지 않는 것으로 보인다(추정) | 소유자 결정 대기 | `CHANGELOG.md` 0.13.3 **Checked**, `docs/trigger-eval-crowd-2026-09-30.md` |
| 닿지 않은 새 케이스 둘: `behavior-buy-in-autoloaded-reads-back`(3회 모두 스킬 로드 없음. 지난해 조건 그대로의 갱신 메일에는 승인자가 모르는 것이 없어 buy-in의 목적에 들지 않고, 요청을 명확하게 두면서 buy-in에 닿게 할 문구가 없다), `behavior-reference-asks-for-the-reference`(3회 중 1회 로드, 로드된 실행은 질문 하나). 권고: buy-in 케이스는 은퇴, reference 케이스는 정보용 | 소유자 결정 대기 | 두 케이스 폴더 |
| `unknowns-loop-every-stage-to-outcome-check`는 다회차 러너의 사용자 차례 최대치 8을 다 썼다. 탐침 단계에 한 차례를 쓰는 실행은 성과 질문 전에 끊긴다. 본문을 고친 뒤 다시 돌리기 전에 러너 최대치와 케이스의 `user_turns`를 올린다 | 에이전트, 그 케이스를 다시 돌리기 전 | `evals/run-multiturn.py` `MAX_USER_TURNS` |
| 릴리스 본문이 태그 메시지가 아니라 머지 커밋 메시지로 채워진다(0.13.0·0.13.1·0.13.2 세 번 손으로 바꿈). 2026-11-24 정리에서 `release.yml`의 `gh release create` 앞에, 태그를 원격에서 다시 받아 주석 태그인지 확인하는 두 줄을 넣었다(검증하지 않은 가설: checkout이 태그를 경량 태그로 남겨 `--notes-from-tag`가 커밋 메시지를 읽는다). 확인 줄이 실패하면 Release 단계는 릴리스를 만들기 전에 멈춘다. 0.13.3 릴리스에서 워크플로가 통과하는지, 본문이 태그 메시지인지 보고, 두 줄을 남길지와 '릴리스 절차'의 수동 확인을 뺄지 정한다 | 0.13.3 릴리스 때 | `.github/workflows/release.yml`, 아래 '릴리스 절차' |

## 지켜볼 칸 (칸마다 최신 수치)

- deviation-log 답사 케이스(`behavior-deviation-log-logs-unplanned-difference`): 비밀번호 절을 뺀 뒤 로그 5회 중 1회(HTML 주석), 계획서 5회 중 5회(0.13.2). 다시 나오면 Don't log에 "비밀 값" 항목을 따로 두는 문장을 2회 돌린다.
- tweakable-plan `alternatives-are-lettered`: 0.13.2 릴리스에서 판사 호출 거부로 판정 없음. 스크립트로 세면 결정 항목 일곱 개 모두 글자 붙은 대안과 기각 이유가 있었다.
- blindspot 다회차 `assumption-verdicts-carry-status`(4a 단계): 0.13.2 4회 중 1회, 0.13.3 라운드 `blindspot-partial-pick` 1회 놓침, `blindspot-reaches-improved-prompt` 3회 중 2회 놓침. 놓친 실행은 자기 가정 하나에 판정이 없거나, 사용자의 말에 없는 사실을 "held"로 사용자에게 돌렸다.
- blindspot·brainstorm의 scout: 0.13.2까지 기록된 실행 14회에서 호출 0회. 0.13.3 라운드에서 `behavior-brainstorm-scout-inventory-monorepo`(서비스 41개 모노레포)가 처음으로 scout를 불렀고 패킷과 목록이 본문대로였다. `behavior-blindspot-scout-many-contracts`는 2회 모두 직접 조사(위 '남은 일'의 소유자 결정).
- interview `ends-at-the-two-deliverables`(`interview-then-work`): 0.13.3 라운드 1회 놓침, 추가 2회 통과.
- unknowns-loop `unconfirmed-criteria-stay-assumed`(`unknowns-loop-criteria-unanswered`): 0.13.3 라운드 1회 놓침, 추가 2회 통과(그중 1회는 러너가 자른 실행을 대신함).
- reference `noncode-en-reference`의 `moves-toward-the-outcome`: 0.13.3 라운드 1회 놓침, 추가 2회 통과.
- prototypes 두 옵션(`prototypes-two-options-contrast`): 첫 실행이 5b 배치·5c 포화 판단·6단계 목록을 답을 받기 전에 한 답에 냈다(가상 사용자의 종료 조건을 고친 뒤 1회 통과).
- interview: 늦은 라운드의 재질문(`deeper-not-padded`, 0.13.1에서 4b 문장 전 5회 중 2회, 0.13.2 릴리스 1회 통과), 3라운드의 why 후속 순서(`questions-carry-reasons-in-priority-order`, 0.13.1 릴리스에서 놓침, 0.13.2 릴리스 1회 통과), 2b의 "Settled items are not asked again"이 1라운드에만 걸리는 것으로 읽히는지. 정렬 하위 단계는 두 위치 모두 다른 칸을 흔들었으므로 다시 시도하지 않는다(0.12.2).
- quiz `key-hidden-until-answered`: 정답 보기가 다른 보기보다 길다(0.13.2 3회 중 2회, 0.12.3부터 보던 모양).
- brainstorm: 후보 제목을 지시형으로 씀(0.13.1 릴리스에서 놓침, 0.13.2 릴리스에서 그 케이스 1회 통과). `finds-the-unused-module`: 0.13.3 라운드 1회 놓침(첫 후보를 "먼저 할 것"처럼 씀), 추가 2회 통과.
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
