# 트리거 eval — v0.5.1 (2026-09-06)

`docs/open-questions.md`의 **B5(트리밍 이후 트리거 발화율 재측정)** 부분 기록.
0.5.1이 11개 스킬 + 2개 에이전트의 `description`에서 한국어 문구를 전부 뺐고,
그 제거가 안전한지를 재기 위해 돌린 측정이다.

이 문서가 존재하는 이유는 하나 더 있다: **`evals/results/`는 gitignore된다.**
실행 산출물은 로컬에만 남고 저장소에는 아무 증거도 남지 않는다. 아래 표가
저장소에 남는 유일한 기록이다.

## 방법

- 경로 B — `python3 evals/run-manual.py` (`claude -p` + stream-json). 경로 A(`claude plugin eval`)는
  이 계정에서 여전히 early access.
- **판정은 기계적**이다: 응답의 첫 `Skill` 도구 호출이 기대한 스킬인가. `llm` 루브릭
  (`ends-with-improved-prompt` 등)은 판사 모델이 없어 사람 채점 대기 상태로 남으며,
  아래 수치에 반영되지 않았다. 즉 이 표는 **"올바른 스킬이 떴는가"**만 말하고
  **"그 스킬이 제대로 수행했는가"**는 말하지 않는다.
- 두 arm, 같은 프롬프트, 같은 케이스 파일, 바이트 동일한 스킬 본문:
  - **shipped** — 저장소 그대로(`--plugin-dir .`), description에 한국어 있음
  - **stripped** — frontmatter에서 한국어만 뺀 사본(`plugin-noko`), `claude plugin validate --strict` 통과
- 기본 모델. 지원 하한은 sonnet 이상이고 haiku는 범위 밖.
- arm당 케이스당 1회.

## 결과 — stripped arm (핵심 근거, 완전)

실행 `manual-20260906T101603Z`. **11/11 정발화, 타임아웃 0.**

| 케이스 | 발화한 스킬 | 소요 |
|---|---|---|
| trigger-ko-blindspot | `unknowns:blindspot` | 188.4s |
| trigger-ko-brainstorm | `unknowns:brainstorm` | 324.4s |
| trigger-ko-buy-in | `unknowns:buy-in` | 216.4s |
| trigger-ko-interview | `unknowns:interview` | 78.7s |
| trigger-ko-loop | `unknowns:loop` | 96.0s |
| trigger-ko-notes | `unknowns:notes` | 101.1s |
| trigger-ko-plan | `unknowns:plan` | 581.8s |
| trigger-ko-prototypes | `unknowns:prototypes` | 384.4s |
| trigger-ko-quiz | `unknowns:quiz` | 120.2s |
| trigger-ko-reference | `unknowns:reference` | 426.3s |
| trigger-ko-teach-me | `unknowns:teach-me` | 267.9s |

**이 arm이 결정의 근거다.** 검증 대상 명제는 "description에 한국어가 없어도 한국어
프롬프트가 올바른 스킬을 띄우는가"이고, 그 명제를 직접 시험하는 것이 stripped arm이다.

## 결과 — shipped arm (대조군, 보존된 산출물은 불완전)

| 케이스 | 보존된 결과 | 소요 |
|---|---|---|
| trigger-ko-blindspot | `unknowns:blindspot` | 171.7s |
| trigger-ko-loop | `unknowns:loop` | 125.8s |
| trigger-ko-notes | `unknowns:notes` | 83.4s |
| trigger-ko-plan | 240s 상한에서 타임아웃, 도구 호출 없음 | 240.1s |
| trigger-ko-prototypes | 〃 | 240.0s |
| trigger-ko-quiz | 〃 | 240.0s |
| trigger-ko-reference | 〃 | 240.0s |
| trigger-ko-teach-me | 〃 | 240.0s |
| trigger-ko-brainstorm / buy-in / interview | 보존된 실행 없음 | — |

**증거 격차, 그대로 적는다.** 릴리스 커밋과 `CHANGELOG.md` 0.5.1은 "양쪽 arm에서 11/11"이라고
적었다. 오늘 디스크에 남아 있는 산출물로 뒷받침되는 것은 stripped arm 11/11과 shipped arm 3/11이다.
나머지 8건은 재실행됐더라도 결과 디렉터리가 남아 있지 않다(빈 디렉터리 2개
`manual-20260906T101129Z`·`manual-20260906T101403Z`가 중단된 실행의 흔적).
5건의 240초 타임아웃은 0.5.1이 고친 바로 그 버그의 증상이며(타임아웃 실행을 채점하지 않도록
수정 + `--timeout` 오버라이드 추가), 그 수정 이후 재실행분이 보존되지 않은 것으로 보인다.

이 격차는 **결정을 뒤집지 않는다** — shipped arm은 대조군이고, 결정을 지탱하는 것은
stripped arm이다. 하지만 "양쪽 11/11"은 지금 저장소가 증명할 수 있는 문장이 아니므로,
인용할 때는 이 문서의 수치를 쓴다.

## 아직 측정되지 않은 것

- **영어 케이스 11건**(`trigger-en-*`) — 0.5.1에서 영어 description도 짧아졌는데 재측정 없음.
- **네거티브 케이스 4건** — `neg-interval-loop-does-not-fire-unknowns-loop` 1건만 시도했고
  8초 타임아웃으로 결과 없음. 나머지 3건 미실행.
- **행동 케이스 3건**(`behavior-*`) — 미실행.
- **과발화** — `docs/trigger-matrix.md` "남은 위험"의 두 항목, 즉 `teach me`가 도메인 어휘와
  무관한 요청까지 잡는지, `plan this`가 일반 계획 요청까지 잡는지. 여전히 미측정.
- **`llm` 루브릭 채점** — 경로 A 게이트가 열리기 전까지는 사람 채점이거나 미채점.

따라서 B5는 **닫히지 않았다.** 한국어 축만 닫혔다.

## 인용 규칙

- "한국어 문구는 description에서 빠져도 발화한다" → 이 문서, stripped arm 11/11. 인용 가능.
- "트리거 발화율 6/6, 오발화 0" → [trigger-eval-v0.3.0.md](trigger-eval-v0.3.0.md)의 v0.3.0
  측정치. description이 두 번(0.4.0, 0.5.1) 바뀐 뒤이므로 **현재 상태의 측정치가 아니다.**
- 다음 측정에서는 `evals/results/`가 지워지기 전에 이 문서의 표부터 갱신한다.
