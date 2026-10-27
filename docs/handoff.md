# 다음 라운드 인계 — 0.10.0 이후

작성 2026-10-27. 새 세션은 이 문서의 **상태**를 git·태그·릴리스·CI와 먼저 대조하고 시작한다. 이 문서는 작업 지시가 아니라 출발점이다. 소유자 판단이 필요한 항목은 그 번호로 묻는다.

## 상태 (2026-10-27)

- 배포: `unknowns--v0.10.0` (main `59d7324`), GitHub Release에 `know-your-unknowns.zip`·`know-your-unknowns-openai.zip`. 카탈로그 `ajitta/claude-plugins`는 `git-subdir` `plugins/unknowns`로 갱신(`b9dae37`).
- 구조: 원본 `skills/`, `claude-code/agents/` → `tools/package.py`가 `plugins/unknowns/`와 두 zip을 생성(커밋됨). 설치 페이로드 49파일·약 157 KB, 코드 없음.
- 확인된 설치: Claude Code 2.1.309·Codex CLI 0.164.0 빈 설정에서 GitHub 마켓플레이스 설치, 11개 스킬. CI(ubuntu·windows·strict validate) 통과.
- 측정 기록: `CHANGELOG.md` 0.10.0의 **Checked**·**Not measured** 절.

## 소유자 대기 (에이전트가 할 수 없음)

- O1. claude.ai Customize › Plugins에 0.10.0 zip 재업로드(또는 Check for updates), ChatGPT에 OpenAI zip 업로드, 모바일에서 스킬 하나 호출. 결과가 오면 README 두 언어의 "not yet checked by the owner" 문구를 확인된 범위로만 좁힌다.

## 다음 라운드 작업 (브랜치에서, main 직접 수정 금지)

`main`에서 `next` 같은 브랜치를 따고, 버전은 소유자가 릴리스를 승인할 때까지 0.10.0에 둔다(CHANGELOG `## [Unreleased]`에 기록 — `package.py`가 이 경우에만 같은 버전 재빌드를 허용).

### N1–N5. 두 버전 모두 낮게 나온 동작 (0.10.0 이전부터 있던 약점)

Claude Code 2.1.309, claude-opus-5-5, `evals/run-manual.py` 케이스, `llm` 채점은 arm을 모르는 별도 `claude -p`. 0.9.2 대 0.10.0 직전 빌드, 같은 시각 병렬, 셀당 3–6회:

| # | 케이스 · 채점 항목 | 0.9.2 | 0.10.0 직전 | 시작점 |
|---|---|---|---|---|
| N1 | `neg-one-file-plan-defers-to-plan-mode` · defers-to-plan-mode | 0/3 | 1/3 | `skills/plan/SKILL.md` 3단계 Size gate(≤2파일이면 plan mode로 넘김)가 있는데도 결정 카드·대안·롤백을 갖춘 문서를 낸다. "짧은 계획"이라고 말하면서 형식은 그대로. |
| N2 | `behavior-prototypes-asks-contrast-on-skip` · states-saturation-check | 1/6 | 1/6 | `skills/prototypes/SKILL.md` 5단계 c(마지막 안이 새 반응을 끌어내면 2개 더 제안). 첫 응답에서 집합이 충분한지 묻거나 넓힐 길을 열지 않는다. |
| N3 | `trigger-en/ko-loop` · stages-the-work | 0/3, 0/3 | 0/3, 1/3 | loop가 조사·질문·계획 단계를 이름으로 나열하지 않는다. 채점 기준이 요구하는 최소 단계 이름과 `skills/loop/SKILL.md` 단계 표의 이름이 일치하는지부터 볼 것. |
| N4 | `behavior-notes-appends-to-file` · entry-has-the-required-fields | 1/3 | 1/3 | `skills/notes/SKILL.md`의 Observed/Attributed 항목 형식. 파일은 3/3 생성하지만 필수 필드가 빠진다. 채점자가 파일 본문을 받는지도 확인(채점 하네스는 `file_text`를 넘긴다). |
| N5 | `behavior-blindspot-ends-with-improved-prompt` · ends-with-a-pasteable-prompt | 0/3 | 0/3 | blindspot 1b단계가 조사 전에 목록 세 개를 한 번 묻고 멈춘다. 단발 케이스에서는 프롬프트 초안까지 가지 못한다 → N6 다회차 케이스로 판정해야 한다. |

각 항목: 원인 가설을 기록 → 본문 수정 → 0.10.0 태그 대 변형, **케이스당 10회 이상, 같은 날 병렬, Fisher 정확검정**으로만 개선을 주장한다. 3회 차이는 잡음이었다(prototypes 2/3 대 0/3 → 재측정 1/6 대 1/6). 주변 라우팅 케이스(같은 스킬의 trigger 2건, 인접 neg 케이스)를 3회씩 같이 돌려 회귀를 본다.

### N6. 다회차 평가 케이스

현재 33케이스가 모두 단발이라 "질문하고 멈추는" 스킬(blindspot·interview·quiz·prototypes)의 핵심 동작을 판정하지 못한다. 시뮬레이션 사용자(페르소나: 사실, 양보 방식, 언제 "정리해"라고 하는지)로 2–4턴 대화를 돌리는 케이스를 추가한다. 우선순위: blindspot(프롬프트 초안 도달), interview(라운드당 4문항 이하 유지), quiz(답 전에 키 비공개, 6/6 판정), prototypes(포화 점검). 스크립트형 사용자가 질문을 무시하면 측정이 안 된다는 점에 주의.

### N7. 채점 기준 정비

- 정확한 문구만 찾는 regex: `behavior-blindspot-ends-with-improved-prompt`의 "improved prompt|prompt draft|…"는 Codex 실행에서 내용은 있는데 문구가 달라 떨어졌다. 기능으로 판정하도록 llm 채점으로 옮기거나 문구 목록을 넓힌다.
- `tool_used` 채점이 Skill 호출만 보고 방법 실행 여부는 보지 않는다(로드 후 거절도 통과).

### N8. 목록 아이콘

`claude plugin validate --strict plugins/unknowns`가 ICON_MISSING 경고를 낸다. `packaging/`에 512–2048 px 정사각 PNG를 두고 `package.py`가 `.claude-plugin/icon.png`로 넣게 한다. 검증기 문구상 개발자 포털에서는 처음 저장할 때의 아이콘만 목록 아이콘이 된다.

### N9. 작은 문서 정리

- `docs/README.md` "두 HTML 리포트에 대한 결정" 절은 "설치가 저장소 전체를 캐시한다"는 0.10.0 이전 전제로 쓰였다. 지금은 `plugins/unknowns/`만 설치된다.

## 측정하지 않은 것 (0.10.0 기준, 다음 라운드에서 다룰 수 있으면 다룸)

- claude.ai·ChatGPT·모바일에서의 라우팅과 동작(O1 이후).
- 0.10.0에서 의미가 바뀐 본문 수정(W2·WC 라운드 약 20건)과 reviewer의 상시 2차 점검의 효과.
- reviewer의 읽기 전용 규칙은 이제 지시문뿐이다(플러그인 에이전트는 Bash를 명령 단위로 막을 수 없다).

## 규칙

- 모델이 읽는 파일을 고치면 writing-for-models 점검: 파일당 검사자 하나(묶음 하나로 돌리면 크게 덜 찾는다: 4건 대 30건), 글을 쓴 엔진과 다른 엔진이 검사, 고친 뒤 diff 점검.
- 공개 텍스트(커밋 메시지, PR 제목·본문, README, CHANGELOG, docs)에 소유자 개인 약칭이나 내부 작업 용어를 쓰지 않는다.
- 릴리스: 소유자 승인 후 `plugin-manifest.json` 버전 → CHANGELOG 이동 → 재생성 → CI → 머지 → 주석 태그 `unknowns--vX.Y.Z` → 릴리스 자산 sha256 대조 → 빈 설정 설치 확인 → 카탈로그 확인.
