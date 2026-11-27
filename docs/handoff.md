# 다음 라운드 인계 — 0.16.0

새 세션은 이 문서의 상태를 git·태그·릴리스·CI와 먼저 대조하고 시작한다. 이 문서는 작업 지시가 아니라 출발점이다.

## 상태

2026-11-28 라운드(브랜치 `open-rows-2026-11-28`, 릴리스 전): 소유자가 남은 일 표의 행을 모두 진행하라고 했다(2026-11-28). 남긴 것: prototypes 1단계(입력 없는 호출은 질문 하나가 답 전체, 두 번째 문구 3회 중 2회), buy-in 4b(대화에만 있는 입력은 글 그대로 패킷에, 3회 중 2회). 되돌린 것: tweakable-plan 5b(0/2), blindspot 4b(셈한 실행 2회 중 0회). 저장소 밖 단발 판사 보조 도구의 프롬프트를 고쳤다. 실행 전 규칙과 결과는 `IMPLEMENTATION_NOTES.md` 2026-11-28, 수치는 `CHANGELOG.md` `[Unreleased]`. 버전 올림, 머지, 전체 릴리스 실행·Sol은 소유자 결정 대기(아래 표).

0.16.0(2026-11-26, PR #55, main `faa5bfc`, 태그 `unknowns--v0.16.0`, 소유자 승인으로 병합과 태그; 자산 sha256 일치, 두 마켓플레이스 빈 설정 설치 0.16.0·스킬 11·에이전트 2): 열린 본문 행을 다섯 갈래로 나눠 고쳤다(interview 세 규칙, buy-in 4b·최종 문서, loop deviation 필드, tweakable-plan 2단계, brainstorm·blindspot scout 항목, quiz·reference 입력 없는 질문 하나). 결과와 되돌린 것은 `CHANGELOG.md` 0.16.0. 소유자가 0.15.0의 Codex·업로드 빌드 라우팅을 확인했다(정상, 2026-11-26).

0.15.0(2026-11-26, 소유자 결정): 모든 스킬은 사용자가 unknowns 방법을 청할 때만 실행된다. 설명마다 `Use only if the user says "unknowns" [or "<label>"] or an unknowns skill calls it.`로 끝나고, 일상 문구 트리거("make a plan", "teach me", "quiz me" 등)는 모두 뺐다. 라벨을 다른 말로 한 것(`record a deviation`, 라벨의 한국어 번역)은 시작해도 된다(소유자 판정, 측정 뒤). 배포: `unknowns--v0.15.0`(PR #53, main `92bbf88`, 소유자 승인으로 병합과 태그). 릴리스 자산 두 개의 sha256이 커밋된 zip과 일치하고(`0ef56ec3…`, `c0fa9458…`), 빈 설정 설치가 두 마켓플레이스 모두 0.15.0에 스킬 11개, 에이전트 2개였다. 카탈로그 설명과 README 행을 맞췄다(`ajitta/claude-plugins` `2e01e1c`). 측정은 `CHANGELOG.md` 0.15.0 **Checked — runs**, 결정과 실행 전 규칙은 `IMPLEMENTATION_NOTES.md` 2026-11-26 맨 위 항목. 이 결정으로 아래 0.14.0 문단의 B8 행(의도하지 않은 트리거)은 닫았다.

0.14.0(2026-11-26, PR #48, main `e1c33e9`, 소유자 승인으로 병합과 태그). 릴리스 자산 두 개의 sha256이 커밋된 zip과 일치하고(`know-your-unknowns.zip` `ae7f3be9…`, `know-your-unknowns-openai.zip` `d047d91d…`), 릴리스 본문은 워크플로가 태그 메시지로 채웠다. 빈 설정 설치가 자체 마켓플레이스와 `ajitta/claude-plugins` 두 경로 모두 0.14.0에 스킬 폴더 11개, 에이전트 2개였고, 설치된 unknowns-loop에 `disable-model-invocation: true`와 새 3단계 문장이 있었다. 설명은 바뀌지 않아 카탈로그는 손대지 않았다. 소유자가 0.14.0에서 확인했다(2026-11-26, 소유자 보고이며 화면 증거는 기록하지 않음): claude.ai Add marketplace, Codex CLI 마켓플레이스, ChatGPT 데스크톱 마켓플레이스 설치에서 플러그인이 설치되고 루프가 시작된다. Claude 데스크톱에서도 된다. ChatGPT에 0.14.0 zip을 다시 올렸다. 원격 작업 브랜치 `owner-decisions-2026-11-26`은 지우지 않았다(`IMPLEMENTATION_NOTES.md` 2026-11-26이 그 브랜치 커밋을 인용한다).

0.14.0에 들어간 것(2026-11-26, 바깥 감사와 독립 리뷰 뒤 소유자 결정): unknowns-loop 3단계의 단계별 체크포인트(a–e 단계마다 결과를 따로 보이고, 질문했으면 답을 기다리고, 건너뛴 질문은 가정으로 넘김)와 d 탐침 주체·판정, Claude Code에서 unknowns-loop는 이름으로만 실행(`claude-code/skill-frontmatter.json`), unknowns-loop 5a와 tweakable-plan 3단계에서 문장 하나씩 삭제(interview 삭제는 실행 전 규칙대로 되돌림). 전체 릴리스 실행과 Sol 실행은 소유자 결정으로 하지 않았다(`CHANGELOG.md` 0.14.0 **Not measured**). 결정·실행 전 규칙·결과는 `IMPLEMENTATION_NOTES.md` 2026-11-26, 원자료는 공개하지 않은 로컬 작업 폴더에 있다.

0.13.4(2026-11-24, PR #44, main `4f274bd`)의 인계 문단은 지웠다. `CHANGELOG.md` 0.13.4와 커밋 `bba5b4e`의 `docs/handoff.md`에 있다.

0.13.3(2026-11-24, PR #42, main `9ad4179`)의 인계 문단은 지웠다. `CHANGELOG.md` 0.13.3과 커밋 `e23dc3d`의 `docs/handoff.md`에 있다.

0.13.2(2026-11-22, PR #40, main `dfb0bb9`): 릴리스 자산 두 개의 sha256이 커밋된 zip과 일치하고(`know-your-unknowns.zip` `55c80740…`, `know-your-unknowns-openai.zip` `0233cc69…`), 빈 설정 설치가 자체 마켓플레이스와 `ajitta/claude-plugins` 두 경로 모두 0.13.2에 스킬 폴더 11개, 에이전트 2개였다. 릴리스 본문은 이번에도 워크플로가 머지 커밋 메시지로 채워서 태그 메시지로 바꿔 넣었다. 원격 작업 브랜치 `audit-fixes-2026-11-22`는 지우지 않았다.

0.13.2에 들어간 것(스킬 본문 열 개와 unknowns-scout, 설명은 그대로): deviation-log(Don't log에서 비밀번호 절 삭제), quiz(teach-back은 키의 요점 전부, 채점과 해설은 여섯 답 뒤, 입력이 없을 때의 문장), blindspot·brainstorm(scout는 직접 다 읽을 수 없을 만큼 많은 자료일 때), blindspot·scout(가정마다 held / wrong / still unchecked 판정을 돌려받음, 첫 초안은 모든 fix 적용), tweakable-plan(interview를 제안하고 같은 답에서 계획), unknowns-loop(1단계 제목, "nothing is scored" 삭제), prototypes(옵션 둘이면 triad 대신 차이 질문), reference(입력이 없을 때의 문장, Output을 5단계에 맞춤), buy-in·quiz·unknowns-loop(공용 deviation log 문장에 비코드 파일), teach-me·brainstorm·deviation-log·tweakable-plan(문구만). OpenAI 목록의 긴 설명 한 문장이 바뀌었다("labeled passes" 삭제).

소유자가 확인한 표면(2026-10-28, 0.12.2, 소유자 보고이며 화면 증거는 기록하지 않음): ChatGPT zip 업로드와 ChatGPT 모바일의 스킬 호출, claude.ai의 Add marketplace 설치가 Claude 모바일로 이어지는 것. 0.14.0(2026-11-26)에서 claude.ai Add marketplace, Codex CLI·ChatGPT 데스크톱 마켓플레이스 설치, Claude 데스크톱, ChatGPT zip 재업로드. claude.ai zip 업로드는 마켓플레이스 경로가 모바일까지 이어지므로 하지 않는다(소유자 판단). 소유자가 확인하지 않은 경로: claude.ai zip 업로드. 소유자 확인이 아닌 기록된 자동 실행: Codex CLI 실행(0.10.0, 0.12.1, 그리고 0.12.3부터 릴리스마다 GPT-6.1 Sol trigger), 두 마켓플레이스에서의 빈 설정 Claude Code 설치(0.12.3부터 릴리스마다).

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

열린 일은 이 표 하나로 추적한다. '소유자 결정 대기'는 소유자가 아직 정하지 않은 항목이고(2026-11-24 정리 또는 그 뒤 라운드에서 올림), 행 안의 '권고'는 그 행을 올린 쪽의 권고다. 끝난 행은 지우고, 결과는 `CHANGELOG.md`와 `IMPLEMENTATION_NOTES.md`에 남긴다. `IMPLEMENTATION_NOTES.md`의 Todo for human 가운데 이 표에 없는 것은 풀렸거나 무의미해졌다(2026-11-24 판정).

| 남은 일 | 누가 | 어디서 시작 |
|---|---|---|
| 2026-11-28 라운드의 릴리스: 배포 본문이 바뀌었으므로(prototypes, buy-in) 버전을 올려 머지한다. 권고: 0.17.0, 전체 릴리스 실행과 Sol은 0.14.0–0.16.0처럼 하지 않음(바뀐 두 스킬은 고친 케이스와 이웃을 돌렸고, 설명은 그대로) | 소유자 결정 대기 | `CHANGELOG.md` `[Unreleased]` |
| tweakable-plan 1b: 자기 모름 목록이 큰 빈칸을 다 담지 않음. 2026-11-28 5b 문장(답 없는 빈칸을 채운 선택에 *assumed — not decided by you* 표시, 그 빈칸은 Your own unknowns에 남김)은 0/2로 되돌림: 표시는 일부 선택에만 고르지 않게 붙었고(1회는 이동 항목에 없음, 1회는 짧은 *assumed*), 목록에는 장소·날짜·이동이 끝내 오지 않았다. 소유자가 정할 것: 결정 항목 안의 표시로 1b를 채운 것으로 볼지(그러면 채점기 `first-reply-suggests-and-plans` 3번 기준을 바꾸고 5b 문장의 앞 절만 다시 시험), 목록을 계속 요구할지 | 소유자 결정 대기, 그 뒤 에이전트 | `IMPLEMENTATION_NOTES.md` 2026-11-28 |
| blindspot: scout 발견이 카드로 오는지. 2026-11-28 4b 문장은 채점기 전체로 셈한 실행 2회 중 0회라 되돌렸다. 그 문장이 겨눈 기준 2(발견마다 카드)는 두 실행 모두 통과했고, 놓친 것은 기준 3(scout의 Needs checking 한 항목, 0.16.0의 4d 문구)과 기준 1(held 판정에 scout의 근거 없음, 4a)이다. 소유자가 정할 것: 같은 문장을 기준별 실행 규칙으로 다시 시험할지 | 소유자 결정 대기, 그 뒤 에이전트 | 같은 항목 |
| blindspot `assumption-verdicts-carry-status`: 2026-11-28 다회차 이웃 4회 중 0회(scout 호출 없음). 자기 가정 하나에 판정이 없거나, 추론(휴일 달력)에 *confirmed*를 붙였다. 지켜볼 칸에서 옮김 | 에이전트, blindspot 다음 변경 때 | 같은 항목, 아래 지켜볼 칸의 같은 행 |

## 지켜볼 칸 (칸마다 최신 수치)

- 입력 없는 호출의 질문 하나(`asks-one-question-for-the-target`·`-for-the-work`·`-for-the-reference`): 0.15.0 실행에서 셋 다 한 질문 옆에 선택적 추가 요청 하나(버전 수, deviation log, 고른 이유)를 붙여 놓쳤다. `-for-the-reference`는 0.14.0에서 1회 통과. 다시 놓치면 그 스킬의 다음 변경 때 다룬다. 0.16.0 뒤 quiz·reference 2/2, 2026-11-28 prototypes 두 번째 문구 3회 중 2회(놓친 1회는 "파일이나 초안을 알려 달라"를 덧붙임).
- unknowns-loop `outcome-check-ends-the-loop`(`unknowns-loop-every-stage-to-outcome-check`): 0.14.0 문구로 3회 중 2회. 놓친 1회는 5c에서 "성과를 이뤘나" 대신 "이걸로 끝난 걸로 할까요"를 물었다. 3단계 체크포인트 뒤로 이 케이스는 실행 3회 중 2회가 사용자 차례 10개를 다 썼다(`user_turns`). 다음 실행에서 차례 상한에 걸려 끊기면, 상한을 바꾸기 전에 실행 전 규칙을 먼저 적는다(`IMPLEMENTATION_NOTES.md` 2026-11-26).
- unknowns-loop `hands-on-both-picks`(`unknowns-loop-blindspot-then-teach-me`): 2026-11-26 라운드 8회 중 6회. 놓친 2회 중 1회는 어시스턴트가 사용자가 고른 용어를 자기 프리셋으로 바꿨다("Choosing between technical terms is my job, not yours"). 나머지 1회는 러너가 따옴표 붙은 응답 신호에서 대화를 끊은 것이고, 러너는 고쳤다(`42c4988`).
- interview `behavior-interview-max-four-questions`: 2026-11-26 2회 연속 놓침(1라운드 항목에 닫힌 선택지, 항목 안의 겹친 질문). 0.16.0 interview 수정(2b·4b)이 겨눈 모양이고, 그 수정 뒤 `at-most-four-questions-this-round` 2/2.
- deviation-log 답사 케이스(`behavior-deviation-log-logs-unplanned-difference`): 비밀번호 절을 뺀 뒤 로그 5회 중 1회(HTML 주석), 계획서 5회 중 5회(0.13.2). 다시 나오면 Don't log에 "비밀 값" 항목을 따로 두는 문장을 2회 돌린다.
- tweakable-plan `alternatives-are-lettered`: 0.13.2 릴리스에서 판사 호출 거부로 판정 없음. 스크립트로 세면 결정 항목 일곱 개 모두 글자 붙은 대안과 기각 이유가 있었다. 0.13.4 릴리스 1회 통과(판사 판정).
- blindspot 다회차 `assumption-verdicts-carry-status`(4a 단계, 2026-11-28 4회 중 0회로 '남은 일' 표에 올림): 0.13.2 4회 중 1회, 0.13.3 라운드 `blindspot-partial-pick` 1회 놓침, `blindspot-reaches-improved-prompt` 3회 중 2회 놓침. 놓친 실행은 자기 가정 하나에 판정이 없거나, 사용자의 말에 없는 사실을 "held"로 사용자에게 돌렸다. 0.13.3 라운드 `blindspot-reaches-improved-prompt`의 `findings-labelled-by-evidence-status` 실패 중 사용자가 가정으로 적은 것을 "Held, you confirmed it"으로 돌린 1회도 같은 모양이다. 0.13.4 릴리스 `blindspot-partial-pick` 1회 놓침(조사와 함께 덧붙인 자기 가정 "UK에 있다고 가정"에 판정 없음, 그리고 처음 보는 모양: 추론에 기댄 "Wrong" 판정에 *confirmed*를 붙임).
- blindspot·brainstorm의 scout: 소유자 판정(2026-11-24, 아래 '규칙')으로 호출 여부는 점수에 들지 않고 두 scout 케이스가 지시자로 보고한다. 기록: 0.12.x("many sources" 문구)에 blindspot이 문서 20개에서 scout를 부른 실행이 있다(`CHANGELOG.md` 0.12.x). 0.13.2 문구 뒤로 blindspot의 scout 케이스에서 호출은 기록되지 않았고(계약서 214건 2회 모두 스크립트로 직접 조사, 판정은 맞음), brainstorm은 0.13.3 라운드 `behavior-brainstorm-scout-inventory-monorepo`(서비스 41개 모노레포)에서 처음 불렀다(패킷과 목록은 본문대로, scout의 열린 항목 둘은 답에 오지 않음). 0.13.4 릴리스에서 blindspot이 계약서 214건에 처음으로 scout를 불렀고(판정은 맞음), brainstorm도 불렀다. 두 실행 모두 scout의 열린 항목 일부가 답에 오지 않았다(지표 `reply-uses-scout-rows`·`reply-uses-inventory`, 위 본문 지적 행).
- interview `ends-at-the-two-deliverables`(`interview-then-work`): 0.13.3 라운드 1회 놓침, 추가 2회 통과. 0.13.4 릴리스 통과.
- unknowns-loop `unconfirmed-criteria-stay-assumed`(`unknowns-loop-criteria-unanswered`): 0.13.3 라운드 1회 놓침, 추가 2회 통과(그중 1회는 러너가 자른 실행을 대신함). 2026-11-24 3단계 a 수정의 이웃 실행에서 통과. 0.13.4 릴리스 통과.
- unknowns-loop `done-criteria-carry-to-verification`(`unknowns-loop-every-stage-to-outcome-check`): 2026-11-24 3단계 a 수정의 이웃 1회 놓침(5단계 확인이 지켜야 할 것과 비용에 상태를 매기지 않고 이메일 기준을 충족으로 적음), 추가 2회 통과. 같은 세 실행에서 `stages-run-in-order`(3단계 d 탐침을 사용자에게 물음)는 3회 중 2회, `deviation-logged`는 3회 중 3회 통과했다(위 '남은 일'의 본문 지적 행의 다음 측정). 세 실행 중 둘이 사용자 차례 10 중 9를 썼다. 0.13.4 릴리스 통과. 같은 실행에서 `stages-run-in-order`와 `deviation-logged`는 놓쳤다(위 본문 지적 행).
- reference `noncode-en-reference`의 `moves-toward-the-outcome`: 0.13.3 라운드 1회 놓침, 추가 2회 통과. 0.13.4 릴리스 통과.
- reference `reference-correction-revises-plan`의 `map-before-building`: 0.13.4 릴리스 1회 놓침(의미 지도의 몇 행이 추정 표시 없이 Riverside 규칙을 짐작), 추가 2회 통과.
- tweakable-plan `trigger-en-tweakable-plan`의 `orders-by-tweak-likelihood`: 0.13.4 릴리스 1회 놓침(결정 항목 하나의 대안에 기각 이유 없음, 판사 셋 중 둘이 실패로 판정), 추가 2회 통과.
- prototypes 두 옵션(`prototypes-two-options-contrast`): 첫 실행이 5b 배치·5c 포화 판단·6단계 목록을 답을 받기 전에 한 답에 냈다(가상 사용자의 종료 조건을 고친 뒤 1회 통과). 0.13.4 릴리스 1회 놓침(같은 모양: 포화 판단 전에 요구사항 목록).
- interview: 늦은 라운드의 재질문(`deeper-not-padded`, 0.13.1에서 4b 문장 전 5회 중 2회, 0.13.2 릴리스 1회 통과), 3라운드의 why 후속 순서(`questions-carry-reasons-in-priority-order`, 0.13.1 릴리스에서 놓침, 0.13.2 릴리스 1회 통과), 2b의 "Settled items are not asked again"이 1라운드에만 걸리는 것으로 읽히는지. 정렬 하위 단계는 두 위치 모두 다른 칸을 흔들었으므로 다시 시도하지 않는다(0.12.2). 0.13.4 릴리스 `deeper-not-padded` 1회 놓침(5라운드에서 사용자가 이미 준 이유를 다시 물음). `questions-carry-reasons-in-priority-order`는 0.13.4 릴리스 통과.
- quiz `key-hidden-until-answered`: 정답 보기가 다른 보기보다 길다(0.13.2 3회 중 2회, 0.12.3부터 보던 모양). 0.13.4 릴리스 통과.
- brainstorm: 후보 제목을 지시형으로 씀(0.13.1 릴리스에서 놓침, 0.13.2 릴리스에서 그 케이스 1회 통과). `finds-the-unused-module`: 0.13.3 라운드 1회 놓침(첫 후보를 "먼저 할 것"처럼 씀), 추가 2회 통과. `finds-the-unused-module` 0.13.4 릴리스 통과.
- blindspot: 이름으로 부르고 자명한 요청("sort the import lines")을 주면 되읽기 문단이 있어도 방법을 실행했다(0.13.0, 2회 중 2회). 다시 돌리지 않았다.
- 짧은 설명에서 빠진 문구(blindspot "run it even when you could answer directly", tweakable-plan "Not native plan mode")와 quiz 설명의 범위 문구("work the model largely produced"), 0.13.0부터. 0.13.1·0.13.2 릴리스 실행에서 `trigger-ko-blindspot`과 `neg-open-quiz-en`은 놓치지 않았다. 0.13.4 릴리스에서도 놓치지 않았다.
- buy-in 3단계 "실행되는 데모나 스크린샷"과 대화 안 Markdown 문서가 어긋날 수 있다(독립 검토 지적, 2026-11-17). 그날 buy-in 실행 넷은 채점을 모두 통과했다.
- 되읽기 문단: "둘 다 이해한 요청이면 방법 없이"를 스킬 산출물을 직접 요청한 경우("quiz me")까지 건너뛰라는 뜻으로 읽는 검사자 지적이 있다. 실행에서 건너뛴 적은 없다. 건너뛰는 실행이 나오면 범위를 "이 스킬 자체의 산출물 요청이 아닌 경우"로 좁힌다. 2026-11-24: 트리거 문구로 자동 로드된 "make a plan"(오늘 밤 배포할 nginx 한 줄)은 2회 모두 크기 관문의 짧은 계획을 냈다(건너뜀 없음). 소유자 판정으로 이것이 맞는 경로다(아래 '규칙'). 0.13.3 라운드 1회는 단계가 여러 줄·하위 항목으로 늘었고, 고친 케이스 `behavior-tweakable-plan-autoloaded-weighty-plan` 1회는 한 줄씩이었다. 0.13.4 릴리스: `behavior-buy-in-autoloaded-reads-back`(informative)이 처음으로 buy-in을 로드했고 되읽기로 답해 채점을 통과했다(4회 중 1회 로드).
- 검토 에이전트를 buy-in을 거치지 않고 이름으로 부를 때, 호출한 모델이 사용자에게 전하는 요약에서 에이전트의 성과 판정이 빠진 적이 있다(0.12.1, 3회 중 3회). 그 뒤 채점기는 에이전트 보고서를 보고, 요약 쪽은 따로 재지 않았다.
- 0.12.3의 1회 실수: prototypes가 이유 없는 skip에 대비 질문을 하지 않음, blindspot *inferred* 카드에 근거 누락. 뒤의 것은 0.13.3 라운드 `findings-labelled-by-evidence-status` 1회에서 다시 나왔다("Inferred"만 있고 무엇에서 추론했는지 없음).
- unknowns-loop(영어): 첫 답에 변경 범위 누락(0.12.4, 9회 중 8회 통과). `noncode-en-unknowns-loop`의 `first-reply-covers-step-2`: 0.13.1 최종 문구 2회 중 1회(놓친 1회는 완료 기준을 사용자의 일이 아니라 루프 산출물 기준으로 물었다), 0.13.2 릴리스 1회 통과. 0.13.4 릴리스 통과.
- quiz(한국어): 해설이 Q2의 수치를 그대로 풀어 줌(0.12.4).
- teach-me: 와인 어휘를 말없이 구매 상황으로 틀 잡음(0.12.4, 3회 중 2회 통과).
- interview(한국어) `noncode-ko-interview`: 1라운드 이유 줄이 두세 문장(0.13.1, 1회 중 0회, 0.13.2 릴리스 1회 통과).
- Codex에서만(Claude에서는 통과, 본문은 고치지 않음): interview 1라운드가 다음 라운드를 예고하지 않음, tweakable-plan이 완료 기준을 "completion criteria"로 써서 정규식 채점만 놓침(0.12.1).

## 릴리스 절차

- 지원 모델은 Opus 5.5·GPT-6.1 Sol, medium effort(소유자). 평가 러너는 기본 `--effort medium`. 실행 회수는 `docs/skill-authoring-guide.md`의 표를 따른다(수정 확인은 실패 케이스 2회, 이웃 1회, 릴리스는 Opus 전체 1회 + Sol trigger 1회). 배포 본문을 바꾸면 버전을 올리고, `[Unreleased]`가 비어 있지 않을 때만 같은 버전 재생성이 허용된다. 같은 버전 재생성은 작업 브랜치에서만 쓰고, 배포 본문을 바꾼 PR은 버전 올림과 함께 머지한다. Claude Code에서는 두 마켓플레이스 경로 모두 새 설치가 main을 받고 기존 설치는 `plugin.json`의 버전이 바뀔 때만 갱신되므로, 올림 없는 머지는 태그와 다른 내용을 같은 버전 이름으로 내보낸다(code.claude.com/docs/en/plugins/loading.md 'Versions and updates', `docs/open-questions.md` A4의 0.8.2·0.8.3, 0.13.1 릴리스가 되돌린 #37 문장). claude.ai와 Codex가 갱신을 무엇으로 판단하는지는 확인하지 않았다(소유자 결정 2026-11-24, `AGENTS.md`에도 같은 규칙).
- Claude Code 플러그인에서 unknowns-loop는 이름으로만 실행된다(`claude-code/skill-frontmatter.json`의 `disable-model-invocation`, 소유자 결정 2026-11-26). 릴리스 zip에는 이 키가 없다. 그래서 `trigger-*-unknowns-loop` 두 케이스와 `neg-interval-loop-does-not-fire-unknowns-loop`는 `upload-build-only` 태그가 붙어 Claude 전체 실행에서 빠지고, Sol trigger 실행은 `--tag upload-build-only`로 따로 넣는다(Sol 22개 = 기본 20개 + 이 둘). 마켓플레이스 설치(claude.ai Add marketplace, Codex, ChatGPT 데스크톱)는 모두 `plugins/unknowns/`를 받으므로 이 키도 받는다. 이 키를 담은 첫 릴리스 전에 소유자가 claude.ai Add marketplace 설치에서 플러그인과 루프가 그대로 보이는지 확인한다. Sol 실행이 마켓플레이스 경로로 설치한다면 그 실행이 Codex에서 이 키를 측정하는 것이므로 그렇게 기록한다.
- 측정 결과는 그 버전 `CHANGELOG.md`의 **Checked**·**Not measured** 절에 적는다(원자료 `evals/results/`는 gitignore). `docs/trigger-eval-*.md`는 동결된 기록이다.
- 평가 보조 도구(판정 스크립트, 릴리스 실행 스크립트, Sol 확인 스크립트)는 소유자의 사설 프로브 스크립트(저장소 밖)다. 단발 판정 스크립트는 2026-11-28에 다회차 러너와 같은 꼴(번호 기준마다 판정을 가르는 부분을 인용한 한 줄)로 바꿨고, 판정 전문을 남기고, 판사 호출이 막힌 것을 실패가 아니라 미판정으로 세고, `focus: trace` 채점기에 Agent 패킷을 넣는다. 그 라운드에서 막힌 것은 `alternatives-are-lettered` 하나(두 번 모두, 0.13.2에도 막힌 채점기)이고, 독립 에이전트가 세션 안에서 판정했다(통과, 판정은 원자료 옆에 저장). 판사 호출도 러너와 같은 격리 환경으로 돈다(2026-11-17). 다음 릴리스의 실행 스크립트는 결과 폴더 설정만 고쳐 쓰면 된다(러너 기본값이 격리다).
- 순서: 소유자 승인 후 `plugin-manifest.json` 버전 → CHANGELOG 이동 → 재생성 → CI → 머지 → 주석 태그 `unknowns--vX.Y.Z` → 릴리스 자산 sha256 대조 → 빈 설정 설치 확인 → 카탈로그 확인. 릴리스 본문은 워크플로가 태그 메시지로 채운다. `actions/checkout`이 주석 태그를 커밋을 가리키는 가벼운 참조로 덮고, `release.yml`이 태그를 원격에서 다시 받아 주석 태그인지 확인한 뒤(아니면 `::error::`로 실패) `--notes-from-tag`를 쓴다(0.13.2·0.13.3 실행 로그로 확인, 소유자 결정 2026-11-24로 수동 확인 삭제).
- teach-me `draft-with-assumptions`(`teach-me-stops-at-draft`)는 알려진 미스로 닫았다(소유자 결정 2026-11-24 뒤 실행 규칙대로): 지금 7b 문장 7회 중 1회, 넓힌 문장 2회 중 0회, '초안엔 준 것·고른 것만, 나머지는 아래 목록' 문장 3회 중 1회. 채점기는 점수에 남기고, 릴리스마다 **Checked**에 알려진 미스로 적는다. 세 번째 문구는 시도하지 않는다.
- GPT-6.1 Sol 확인은 0.13.2부터 WSL에서, 격리한 HOME과 `CODEX_HOME`으로 돌린다. Codex 로그인이 ChatGPT 로그인이라 환경 변수로 넘길 토큰이 없어서 `auth.json`을 격리한 홈에 복사한다. 사본이 혼자 갱신되면 원래 로그인이 끊길 수 있으므로, 먼저 평소 홈에서 `codex exec`를 한 번 돌려 토큰을 거기서 갱신시킨 뒤 복사하고, 끝나면 두 파일의 `last_refresh`가 같은지 본 다음 사본을 지운다.
- GPT-6.1 Sol 확인 때 지킬 것(0.13.0에서 발견): Codex 앱은 소유자 계정에 올려 둔 플러그인 사본(당시 0.12.4)을 격리한 홈의 `.codex/plugins/cache/created-by-me-remote`로 동기화한다. 0.13.0의 처음 세 번 시도에서는 22개 세션 중 7–8개가 빌드 옆에 그 사본을 나열하고 그 사본의 `SKILL.md`를 읽었으므로, 세 번 모두 무효로 했다. `config.toml`의 `[features] remote_plugin = false`와 `[plugins."unknowns@created-by-me-remote"] enabled = false`는 막지 못했다. 막은 방법: 플러그인을 추가하기 전에 격리한 홈에 그 캐시 폴더를 미리 만들고 읽기 전용(`chmod 555`)으로 둔다. 실행 뒤에는 세션 기록에서 `created-by-me-remote/unknowns`가 0건인지, 22개 실행이 모두 빌드 버전의 `SKILL.md`를 읽었는지 센다(0.13.0: 0건, 22/22). 이전 릴리스의 GPT-6.1 Sol 확인에는 이 장치가 없었다.

### 설명을 고친 뒤 다시 재는 방법

- `evals/run-manual.py`로 `trigger-*` 22개(기본 실행 20개 + `upload-build-only` 둘), `noncode-*` 22개, `unknown-*` 4개, `neg-*` 18개(2026-11-24에 넷, 2026-11-26에 하나 추가, 그중 `upload-build-only` 하나)를 케이스당 1회(설명을 고친 뒤의 확인) 또는 의심 가는 케이스만 3회(`docs/skill-authoring-guide.md`의 실행 회수 표). 설명을 고치면 `SKILL.md`와 `scripts/skill-descriptions.json`을 함께 고친다(테스트가 두 사본의 일치를 본다).
- 스킬별 업로드 zip(`scripts/build-skill-zips.py`)은 frontmatter를 JSON 따옴표 형식으로 다시 쓴다. `run-manual.py --verify --plugin-dir <zip을 푼 디렉터리>`는 그 형식의 description을 읽지 못해 거짓 실패를 낸다(실행 경로에는 영향 없음).
- claude.ai 자체의 라우팅과 업로드 화면은 headless로 돌릴 수 없어 어느 기록도 보여 주지 않는다.

## 규칙

- 모든 판단은 `.claude/rules/skill-writing.md` 0번(세 칸, 어떤 분야든, 성과)을 따른다. 코딩은 여러 예 중 하나다.
- 구조: 원본 `skills/`(스킬마다 SKILL.md 하나, 공유 참조 파일 없음), `claude-code/agents/` → `tools/package.py`가 `plugins/unknowns/`와 두 zip을 생성(커밋됨). 코드 없음, 목록 아이콘 PNG 하나.
- 작성 원칙: `.claude/rules/skill-writing.md` 0번(목적)과 17번 — 금지 문장·읽기 전용 약속·도구 허용 목록·정체성 문장("You are …")을 쓰지 않는다. 강제는 사용자 하네스의 몫이다. 두 에이전트는 모든 도구를 물려받고, 플러그인은 git 절차를 따로 두지 않는다.
- 스킬 설명은 200자 이하이고 `scripts/skill-descriptions.json`과 같은 문구다(`.claude/rules/skill-writing.md` 18번). 설명을 고치는 것은 라우팅을 고치는 것이므로 trigger·비코딩·네거티브 케이스를 다시 돌린다.
- 설명을 skill-creator 권고대로 더 적극적으로("pushy") 쓰지 않는다(소유자 판단 2026-10-28). 판단 당시 빌드(0.12.0–0.12.1)의 라우팅은 이름 44/44(0.12.0), 한국어 blindspot 트리거 10/10, Codex 18/18이었다.
- 본문의 되읽기 문단, 라우팅 문장, 칸 문장은 모든 스킬에 남긴다(소유자 판단 2026-11-13).
- blindspot 2단계·brainstorm 2a의 "more sources than you can read in full"은 모델 자신의 판단이다. 직접 조사로 결과에 이르면 맞고 scout를 불러도 맞다. 평가 케이스는 자료 크기를 이유로 scout 호출을 요구하지 않는다(소유자 판정 2026-11-24).
- tweakable-plan 자신의 산출물(계획)을 요청하면, 계획하는 일이 아무리 무거워도 크기 관문을 거친다. 되읽기 문단은 일을 하라는 요청에 적용된다(소유자 판정 2026-11-24). 이 모호함을 문장으로 없애는 길은 지켜볼 칸의 되읽기 문단 좁히기(본문 11개)이고, 지금은 하지 않는다.
- 스킬의 목표·산출물이나 단계의 이유를 말하는 문장은 중복처럼 보여도 지우지 않는다(`docs/features/concise-plugin-text/06-results.md`; 0.13.0에서 그런 문장 넷을 지웠다가 되돌렸다).
- teach-me의 예(색 보정 한 분야)는 유지한다. 비교 표가 글·코드·절차를 다루고 비코딩 케이스가 통과한다(소유자 판단 2026-10-28).
- unknowns-loop·tweakable-plan 2단계의 "Outcome, as stated / as read" 두 줄은 같은 문장으로 다시 시도하지 않는다. 두 줄이 있을 때 `noncode-en-unknowns-loop`의 `first-reply-covers-step-2`가 성과 항목을 3회 중 2회 놓쳤다(요청문을 성과로 인용하고 사용자가 궁극적으로 바라는 것까지 가지 않음, 2026-11-17). 다시 한다면 산출물의 말과 성과의 말을 가르는 문장이 필요하다는 것이 그 실행의 읽기다(작성자 해석).
- 모델이 읽는 파일을 고치면 writing-for-models 점검: 고친 diff를 글쓴이가 아닌 검사자 한 명이 한 번 읽는다(파일별 점검 없음, `docs/skill-authoring-guide.md` 실행 회수 표). 이 플러그인은 소유자 판단으로 Claude 검사만 한다. 검사자가 금지 문장을 제안하면 할 일 문장으로 바꾸거나 버린다(17번).
- 한 릴리스에 스킬 변경을 하나만 넣는 규칙은 폐기했다(소유자 결정 2026-11-26).
- 소유자는 버전 간 A/B 비교를 원하지 않는다. 플러그인 자체의 실행에서 실패를 읽고 고친다.
- 공개 텍스트(커밋 메시지, PR 제목·본문, README, CHANGELOG, docs)에 소유자 개인 약칭이나 내부 작업 용어를 쓰지 않는다.
- main에 직접 커밋하지 않는다. 작업은 브랜치에서, 푸시·태그는 소유자 승인 뒤(AGENTS.md Release).
- 기록이 인용하는 커밋이 squash 머지로 main에 없는 작업 브랜치는 지우지 않는다: `docs/dia-regula-audit`(0.12.4, `IMPLEMENTATION_NOTES.md` 2026-11-10이 `0cbbf69`·`e4f05dd`·`3221f7d`를 인용), `short-descriptions`(0.13.0, CHANGELOG 0.13.0과 `IMPLEMENTATION_NOTES.md`가 `63e0360`·`02484af`·`c515a4d`를 인용), `cleanup/stale-docs-2026-11-24`(0.13.3, `IMPLEMENTATION_NOTES.md` 2026-11-24가 `2b92dd5`와 실행 전 규칙을 담은 `d65123b`를, CHANGELOG 0.13.3이 Sol을 돌린 `31249e4`를 인용), `owner-decisions-2026-11-24`(0.13.4, `IMPLEMENTATION_NOTES.md` 2026-11-24 두 항목이 실행 전 규칙을 담은 `ef08b56`·`1d70fe6`·`00c7b2c`·`6e6fe96`을, CHANGELOG 0.13.4가 릴리스 점검을 돌린 `794ed0d`를 인용).

0.13.1 이전의 인계 문단, 끝난 일 서술, 릴리스별 지켜볼 칸 목록(`IMPLEMENTATION_NOTES.md` 2026-11-17 항목이 가리키는 목록 포함)은 2026-11-24 정리에서 지웠다. 커밋 `d9daf07`의 `docs/handoff.md`에 있다.
