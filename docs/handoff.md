# 다음 라운드 인계 — 0.12.1 이후

작성 2026-10-28, 0.12.1 릴리스(PR #24) 뒤 갱신, 같은 날 브랜치 `next`(초안 PR #26) 라운드 결과 반영. 새 세션은 이 문서의 **상태**를 git·태그·릴리스·CI와 먼저 대조하고 시작한다. 이 문서는 작업 지시가 아니라 출발점이다. 소유자 판단이 필요한 항목은 그 번호로 묻는다.

## 상태 (2026-10-28)

- 배포: `unknowns--v0.12.1`, GitHub Release에 `know-your-unknowns.zip`·`know-your-unknowns-openai.zip`. 카탈로그 `ajitta/claude-plugins`는 `git-subdir` `plugins/unknowns`를 가리킨다.
- 0.12.1은 본문 수정판이다(blindspot·brainstorm·interview·quiz). 설명·스킬 이름·항상 로드되는 토큰은 0.12.0과 같다.
- 브랜치 `next`(초안 PR #26, 머지·태그 전, 버전 0.12.1 유지): interview·blindspot 본문 수정 두 개와 buy-in 평가 케이스 하나. 기록은 CHANGELOG `[Unreleased]`.
- 0.12.0은 범위 재정의 판이다. 플러그인은 사용자와 AI가 아는 것의 세 칸(사용자는 모르고 AI는 아는 것, AI가 모르는 것, 둘 다 모르는 것)을 어떤 분야에서든 다루고, 산출물이 아니라 성과로 판단한다(`.claude/rules/skill-writing.md` 0번). 둘 다 아는 요청은 범위 밖이고 바로 처리한다.
- **Breaking(0.12.0):** `loop` → `unknowns-loop`, `notes` → `deviation-log`, `plan` → `tweakable-plan`. 설명 11개는 영어로만 쓰고, 끝 문장은 "Clear to both sides: no skill or method."
- 요청 되읽기(read-back)는 각 스킬 본문과 unknowns-loop 1단계에 있다(소유자 판단으로 유지, 2026-10-28). 스킬이 뜨지 않는 무거운 요청에서도 되읽기를 원하는 사용자는 README가 안내하는 한 줄을 자기 `CLAUDE.md`에 넣는다(측정 9/9).
- 구조: 원본 `skills/`(스킬마다 SKILL.md 하나, 공유 참조 파일 없음), `claude-code/agents/` → `tools/package.py`가 `plugins/unknowns/`와 두 zip을 생성(커밋됨). 코드 없음, 목록 아이콘 PNG 하나.
- 작성 원칙: `.claude/rules/skill-writing.md` 0번(목적)과 17번 — 금지 문장·읽기 전용 약속·도구 허용 목록·정체성 문장("You are …")을 쓰지 않는다. 강제는 사용자 하네스의 몫이다. 두 에이전트는 모든 도구를 물려받고, 플러그인은 git 절차를 따로 두지 않는다.
- 측정 기록: CHANGELOG 0.12.0과 0.12.1의 **Checked**·**Not measured** 절.
- 평가: 단발 70케이스(`evals/run-manual.py`), 다회차 5케이스(`evals/run-multiturn.py`, 시뮬레이션 사용자와 2–5턴). 입력 자료가 필요한 케이스는 CLI 형식 그대로 `files/` + `place-files.sh` + `case.yaml`의 `context: scaffold_script:`를 쓰고(`claude plugin eval --scaffold`와 같음), 러너가 실행 전에 그 스크립트를 실행한다. 생성된 에이전트가 돌려준 보고서는 `agent_reports`로 남아 `focus: trace` 채점에 쓰인다.

## 0.12.1에서 끝난 일

- 검토 에이전트(independent-reviewer) 평가 케이스 두 개: 완료 기준 하나를 몰래 빠뜨린 git 저장소, 수치가 기록과 어긋나는 시범 사업 보고서. 각 3회, 30/30.
- reference 다회차 케이스(사용자가 2턴에서 의미 지도의 한 행을 번호로 고침): 3회, 6/6.
- 얇은 칸 3회씩: prototypes 단발 5케이스·다회차, blindspot 근거 상태, brainstorm 판단 보류, interview 이유·순서, 한국어 blindspot 트리거 10회. 실패를 읽고 고친 결과는 CHANGELOG 0.12.1.
- Codex 실행 확인(격리 HOME+CODEX_HOME): 이름이 바뀐 세 스킬, 이름·영어·한국어 트리거 각 2회 18/18.
- skill-creator 기준 점검: 16개 항목, 형식 수정 3개 반영.

## 브랜치 next에서 끝난 일 (2026-10-28, 초안 PR #26)

- interview 다회차 순서 칸(소유자 판단: 다른 수정 하나, 3회): 라운드를 쓰기 전에 질문을 Question Priority 순으로 정렬하는 하위 단계를 두 번 시도했다. 4단계에 두면 2·3라운드 순서는 3/3이었지만 1라운드가 "확실한 것·가정한 것" 질문을 3회 중 2회 빠뜨렸다. 2단계 맨 앞으로 옮기고 그 질문을 이름으로 부르자 1라운드는 3/3이었지만 why 후속 질문이 해악 질문 아래로 내려갔다(3회 중 1회). 두 번 모두 3/3이 아니어서 0.12.1 문구로 되돌렸고, 되돌린 문구는 이번 6회에서 순서 6/6이었다.
- interview 넷 이하 칸: "why it matters" 줄 안에 다섯 번째 결정 질문이 들어간 실행이 다시 나와(6회 중 1회) 2a에 "이유 줄 안의 물음표"도 넷에 센다고 넣었다. 다회차 6회 24/24, 단발 다섯 케이스 18/18.
- blindspot 근거 상태 칸: 0.12.1 본문에서 3회 중 1회 *unchecked* 카드가 카드와 집계에 남아, 카드를 쓰는 4단계에 조건을 넣었다(카드 상태는 *confirmed*·*inferred*, *unchecked*는 **Needs checking**으로, 집계는 카드 수). 다회차 6회 24/24, 단발 여섯 케이스 30/30.
- buy-in이 검토 에이전트 보고서를 옮기는지(소유자 판단: 본문은 고치지 않고 지켜봄): 기존 buy-in 케이스 넷은 Agent 도구를 허용하지 않아 검토 에이전트를 부를 수 없었으므로, 시범 사업 보고서 자료를 쓰는 `behavior-buy-in-relays-reviewer`를 더했다. 3회 모두 에이전트를 불렀고, 써낸 buy-in 문서가 에이전트의 성과 판정과 기록에서 다시 센 수치·근거 없는 주장·보증금 문제를 담았다(9/9). 문서를 가리키는 짧은 채팅 답은 3회 중 1회만 성과를 언급했지만 산출물은 문서이므로 본문은 고치지 않았다.
- writing-for-models(Claude): interview·blindspot 파일별 점검과 diff 점검, 지적 19개 모두 인용 확인, 확정 0.

## 소유자 대기 (에이전트가 할 수 없음)

- O1. claude.ai Customize › Plugins에 0.12.1 zip 재업로드(0.12.0에서 이름이 바뀐 세 스킬 때문에 기존 업로드를 교체), ChatGPT에 OpenAI zip 업로드, 모바일에서 스킬 하나 호출. 짧은 설명의 대리 측정은 통과했다(259/260 대 260/260, 아래). 결과가 오면 README 두 언어의 확인 범위 문구를 확인된 범위로만 고친다.

## 소유자 판단 기록 (2026-10-28)

- 업로드용 짧은 설명의 대리 측정(520회): 승인, 0.12.1 릴리스 뒤 실행해 통과(아래 "업로드용 짧은 설명의 호출 측정").
- 설명을 skill-creator 권고대로 더 적극적으로("pushy") 쓰지 않는다. 이 빌드의 라우팅은 이름 44/44(0.12.0), 한국어 blindspot 트리거 10/10, Codex 18/18이다.
- teach-me의 예(색 보정 한 분야)는 유지한다. 비교 표가 글·코드·절차를 다루고 비코딩 케이스가 통과한다.
- 본문의 되읽기 문장은 유지한다(아래 "측정이 얇은 곳" 마지막 항목).
- interview 다회차 순서 칸은 이번 릴리스에서는 편차로 두고, 다음 라운드에 다른 수정 하나를 3회로 시도한다.
- 검토 에이전트 보고서를 호출한 모델이 옮기면서 성과 판정을 빠뜨린 건: 본문은 고치지 않고 buy-in 실행에서 지켜본다.

## 다음 라운드 작업 (브랜치에서, main 직접 수정 금지)

버전은 소유자가 릴리스를 승인할 때까지 0.12.1에 둔다(CHANGELOG `## [Unreleased]`에 기록 — `package.py`가 이 경우에만 같은 버전 재빌드를 허용).

### 지켜볼 칸

- interview 다회차 순서: 두 라운드 동안 배치마다 2/3이었고 이번 라운드에는 같은 문구로 6/6이었다. 3–6회 배치로는 수정과 변동을 가를 수 없다. 정렬 하위 단계는 두 위치 모두 다른 칸을 흔들었으므로(위) 다시 시도하지 않는다.
- 이번 라운드의 두 수정(interview 이유 줄의 물음표, blindspot 4단계의 *unchecked*)은 원래 3–9회에 1회꼴로 나오던 실수다. 6회 무실패는 사라졌다는 증거가 아니다. 다음 배치에서도 지켜본다.

### 측정이 얇은 곳

- 검토 에이전트를 buy-in을 거치지 않고 이름으로 부를 때, 호출한 모델이 사용자에게 전하는 요약에서 에이전트의 성과 판정이 빠진 적이 있다(첫 실행 3/3). 에이전트 보고서 자체에는 있었다. buy-in 실행에서는 문서가 판정을 3/3 담았다(위). 이름으로 부르는 경우는 다시 돌리지 않았다.
- Codex에서만 보인 것(Claude에서는 통과, 본문은 고치지 않음): interview 1라운드가 다음 라운드가 이어진다고 말하지 않았다(1회 중 1회). tweakable-plan은 완료 기준을 "completion criteria"로 써서 정규식 채점만 놓쳤다(방법은 지킴).
- 본문의 "둘 다 이해한 요청이면 방법 없이" 문장을 스킬 산출물을 직접 요청한 경우("quiz me")까지 건너뛰라는 뜻으로 읽는 검사자 지적이 이번에도 나왔다(quiz). 실행에서 건너뛴 적은 없다. 건너뛰는 실행이 나오면 범위를 "이 스킬 자체의 산출물 요청이 아닌 경우"로 좁힌다.

### 업로드용 짧은 설명의 호출 측정

claude.ai Customize › Skills에 올리는 짧은 설명(`scripts/skill-descriptions.json`)은 2026-10-28 아래 방법으로 Claude Code 대리 측정을 했다. 결과: 짧은 설명 259/260, 플러그인 설명 260/260(Fisher p = 1.0, Wilson 하한 97.9%), 충돌 케이스 40/40 대 40/40. 놓친 1회는 한국어 blindspot에서 스킬 없이 바로 답한 경우다. 기록은 CHANGELOG `[Unreleased]`. 같은 측정을 다시 할 때의 방법: 테스트는 길이(200자 이하)와 README 문구 포함만 본다. 업로드 화면 자체는 headless로 돌릴 수 없으므로 Claude Code 대리 측정으로 한다.

- 변형 만들기: `python3 scripts/build-skill-zips.py --out <절대 경로>/dist`, 새 디렉터리에 `plugins/unknowns/`의 `.claude-plugin`·`agents`·`LICENSE`·`NOTICE`·`README.md`를 복사하고 zip을 그 `skills/`에 푼다. `unknowns:` 이름공간이 유지되고 본문은 같으며(11개 모두 바이트 단위로 같음을 확인) 설명만 다르다. `claude plugin validate --strict`로 확인(통과).
- 실행: 긴 설명(`plugins/unknowns`) 대 짧은 설명 두 arm을 같은 날 병렬로, `trigger-*` 22케이스와 발동하면 안 되는 충돌 케이스 4개(`neg-generic-howto-does-not-fire-teach-me`, `neg-interval-loop-does-not-fire-unknowns-loop`, `neg-ui-options-does-not-fire-brainstorm`, `neg-vocabulary-does-not-fire-blindspot`), 케이스당 10회 = 520회. 원하면 `neg-open-*` 8케이스(160회)를 더한다. 케이스별과 합산으로 Fisher 정확검정. 케이스당 10회로는 큰 하락만 보이므로 합산 비교가 핵심이다.
- 주의: `run-manual.py --verify --plugin-dir <변형>`은 JSON 따옴표 형식의 description을 읽지 못해 거짓 실패를 낸다(실행 경로에는 영향 없음).
- 결과는 "claude.ai 업로드 설명의 Claude Code 대리 측정"으로 기록하고, 통과하면 `scripts/skill-descriptions.json`의 `_comment` 배열에 측정 날짜와 결과를 한 줄 추가한다. claude.ai 자체의 라우팅은 이 측정이 보여 주지 않는다.

## 규칙

- 모든 판단은 `.claude/rules/skill-writing.md` 0번(세 칸, 어떤 분야든, 성과)을 따른다. 코딩은 여러 예 중 하나다.
- 모델이 읽는 파일을 고치면 writing-for-models 점검: 파일당 검사자 하나, 고친 뒤 diff 점검. 이 플러그인은 소유자 판단으로 Claude 검사만 한다. 검사자가 금지 문장을 제안하면 할 일 문장으로 바꾸거나 버린다(17번).
- 소유자는 버전 간 A/B 비교를 원하지 않는다. 플러그인 자체의 실행에서 실패를 읽고 고친다.
- 공개 텍스트(커밋 메시지, PR 제목·본문, README, CHANGELOG, docs)에 소유자 개인 약칭이나 내부 작업 용어를 쓰지 않는다.
- 릴리스: 소유자 승인 후 `plugin-manifest.json` 버전 → CHANGELOG 이동 → 재생성 → CI → 머지 → 주석 태그 `unknowns--vX.Y.Z` → 릴리스 자산 sha256 대조 → 빈 설정 설치 확인 → 카탈로그 확인.
