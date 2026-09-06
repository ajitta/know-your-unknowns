# 트리거 eval — v0.5.1 (2026-09-06)

`docs/open-questions.md`의 **B5(트리밍 이후 트리거 발화율 재측정)** 기록. 한국어 축을 먼저 재고, 같은 날 나머지 축을 전부 이어서 쟀다.
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

## 결과 — 영어·네거티브·행동 (2026-09-06 후속 실행)

같은 0.5.1 description을 대상으로 나머지 19건을 5개 배치 병렬로 돌렸다. `--runs 1`,
`--timeout 900`(0.5.1이 고친 타임아웃 버그의 재발을 막기 위해 상한을 크게 잡음).
**19/19 실행, 타임아웃 0, 기계 판정 그레이더 23/23 통과.**

### 영어 트리거 11/11

| 케이스 | 발화 | 소요 |
|---|---|---|
| trigger-en-blindspot | `unknowns:blindspot` | 144.0s |
| trigger-en-brainstorm | `unknowns:brainstorm` | 182.4s |
| trigger-en-buy-in | `unknowns:buy-in` | 247.2s |
| trigger-en-interview | `unknowns:interview` | 54.2s |
| trigger-en-loop | `unknowns:loop` | 97.7s |
| trigger-en-notes | `unknowns:notes` | 90.7s |
| trigger-en-plan | `unknowns:plan` | 448.1s |
| trigger-en-prototypes | `unknowns:prototypes` | 498.7s |
| trigger-en-quiz | `unknowns:quiz` | 161.1s |
| trigger-en-reference | `unknowns:reference` | 359.1s |
| trigger-en-teach-me | `unknowns:teach-me` | 634.9s |

### 네거티브 5/5 — 충돌 쌍이 실제로 갈린다

| 케이스 | 결과 | 판정 |
|---|---|---|
| neg-interval-loop-does-not-fire-unknowns-loop | 스킬 발화 없음 | 통과 — 맥락 없는 "loop"는 내장 인터벌 러너로 감 |
| neg-ui-options-does-not-fire-brainstorm | `unknowns:prototypes` 발화 | 통과 — UI 옵션은 brainstorm이 아니라 prototypes |
| neg-vocabulary-does-not-fire-blindspot | `unknowns:teach-me` 발화 | 통과 — "이 단어들을 모른다"는 blindspot이 아니라 teach-me |
| neg-one-file-plan-defers-to-plan-mode | `unknowns:plan` 발화, **문서는 쓰지 않음** | 기계 판정 통과 / 아래 단서 참조 |
| **neg-generic-howto-does-not-fire-teach-me** (신규) | 스킬 발화 없음, CSS 답을 바로 줌 | 통과 — 19.3s |

마지막 케이스는 이번에 **새로 만들었다.** `trigger-matrix.md`가 "`teach me`는 두 단어짜리
범용 영어 문구"라는 과발화 위험을 적어 두고도 그것을 재는 케이스가 하나도 없었기 때문이다.
"teach me how to center a div" — 답이 정해져 있고 사용자가 출력 형식까지 지정한 요청에서
teach-me는 **뜨지 않았다.** 이 방향의 과발화는 재현되지 않는다.

### 행동 3/3

`behavior-blindspot-ends-with-improved-prompt`, `behavior-interview-max-four-questions`,
`behavior-notes-appends-to-file` 모두 올바른 스킬이 뜨고 기계 그레이더 6건 전부 통과.
notes 케이스는 `IMPLEMENTATION_NOTES.md`를 실제로 만들었는지까지 파일 존재로 확인됐다.

## 남은 단서 — `plan`의 크기 게이트 (판정 유보)

`neg-one-file-plan-defers-to-plan-mode`는 기계 판정으로는 통과다: 계획 문서도
`.unknowns/` 산출물도 쓰지 않았다. 그런데 응답 본문을 읽으면 애매하다.

- 잘한 것: "크기 게이트가 걸린다, 전체 문서는 과하다"고 **명시하고** 문서를 쓰지 않았다.
- 걸리는 것: 그러면서도 본문에 "바꾸고 싶을 가능성 순 결정 3건", "기각한 대안", "검증",
  "롤백", "이 계획의 가장 약한 부분"을 **그대로 인라인으로 재현했다**(3,788자).
  루브릭 2번은 바로 그 구성 요소들이 나오면 안 된다고 적혀 있다 — 다만 "**문서**를
  내놓지 말 것"이라는 문면이라, 파일을 안 쓴 이번 경우가 위반인지 아닌지가 갈린다.

**판정하지 않고 남긴다.** `llm` 그레이더가 이 케이스를 위해 존재하고, 판사 모델은
경로 A 게이트 뒤에 있다. 스스로 채점하면 그게 새 허구다.

## 아직 측정되지 않은 것

- **`llm` 루브릭 14건** — 경로 A(`claude plugin eval`)가 이 계정에서 early access라
  판사 모델이 없다. 기계 판정은 "올바른 스킬이 떴는가"까지만 말하고
  "그 스킬이 제대로 수행했는가"는 말하지 않는다.
- 위의 `plan` 크기 게이트 단서.
- arm당 케이스당 1회(n=1). 스킬당 대표 문구 하나씩이며 README가 광고하는 문구 전체가 아니다.

## 인용 규칙

- "한국어 문구는 description에서 빠져도 발화한다" → 이 문서, stripped arm 11/11. 인용 가능.
- "영어 트리거 11/11, 네거티브 5/5, 행동 3/3, 기계 그레이더 23/23" → 이 문서. 인용 가능.
  단 **기계 판정 한정**임을 함께 적을 것.
- "트리거 발화율 6/6, 오발화 0" → [trigger-eval-v0.3.0.md](trigger-eval-v0.3.0.md)의 v0.3.0
  측정치. description이 두 번(0.4.0, 0.5.1) 바뀐 뒤이므로 **현재 상태의 측정치가 아니다.**
- 다음 측정에서는 `evals/results/`가 지워지기 전에 이 문서의 표부터 갱신한다.
