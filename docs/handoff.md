# 다음 라운드 인계 — 0.13.0

## 다음 세션: 여기서 시작

배포 중인 버전은 `unknowns--v0.13.0`이다(2026-11-13, PR #33, main `2ea4ae7`). 릴리스 자산 두 개의 sha256이 커밋된 zip과 일치하고, 빈 설정 설치가 자체 마켓플레이스와 `ajitta/claude-plugins` 두 경로 모두 0.13.0에 스킬 폴더 11개였다. 릴리스 본문은 워크플로가 머지 커밋 메시지로 채워서, 태그 메시지(CHANGELOG 0.13.0 내용)로 바꿔 넣었다. 남은 일은 소유자가 ChatGPT zip을 다시 올리는 것이다. 0.12.4의 작업 브랜치는 `IMPLEMENTATION_NOTES.md`가 그 커밋 해시를 인용하므로 지우지 않고 남겨 둔다. `short-descriptions`도 같은 이유로 남긴다(CHANGELOG 0.13.0과 `IMPLEMENTATION_NOTES.md`가 `63e0360`, `02484af`, `c515a4d`를 인용한다).

| 무엇 | 누가 | 어디서 시작 |
|---|---|---|
| 0.13.0 릴리스 뒤 ChatGPT에 `know-your-unknowns-openai.zip` 재업로드(스킬 설명이 바뀌어 목록 문구가 달라졌다), 모바일에서 스킬 호출 확인. 0.12.4 재업로드 여부는 이 문서에 기록이 없다 | 소유자 | GitHub Release `unknowns--v0.13.0` |
| claude.ai(Add marketplace 경로)가 새 버전을 받았는지 확인 | 소유자 | claude.ai Customize › Plugins |
| 두 번째 규칙 기반 리뷰에서 보류한 항목: 공용 문장, 파일 사이 이름, 스킬별 방법 결정. 설명 문구 10개에 대한 지적은 0.12.4의 긴 설명 기준이므로 짧은 설명에 맞춰 다시 읽어야 한다 | 소유자 결정 | `IMPLEMENTATION_NOTES.md` 2026-11-09·11-10의 Todo for human |
| 라우팅에서 닿지 않은 본문: prototypes(단일 HTML 목업 0/2), quiz("오늘 오후 제출" 0/3). 둘 다 긴 설명으로 잰 값이다. 짧은 설명으로 돌린 0.13.0 전체 실행 1회에서도 두 케이스 모두 스킬이 로드되지 않았다 | 소유자 결정 | 같은 문서 2026-11-10 |
| 중복 문장 제거를 한 문장씩, 그 스킬의 케이스를 돌리면서 다시 시도할지. 후보는 15개다(처음부터 남긴 9개와 지웠다가 되돌린 6개) | 소유자 결정(추천: 실행으로 필요 없음이 보일 때까지 유지) | `IMPLEMENTATION_NOTES.md` 2026-11-13의 "Removed at first, then back"·"Left as they were" 표 |
| 설명 속 "you"를 한 가지 뜻으로 정하기: quiz와 interview의 설명에서는 사용자를, reference의 설명에서는 모델을 가리킨다(독립 리뷰). 설명을 고치면 trigger·비코딩·네거티브 케이스를 다시 돌린다 | 소유자 결정 | 같은 문서 2026-11-13 Todo for human (a) |
| deviation-log 설명의 "as work hits unknowns": 0.12.4에서 뺀 "자동으로 시작" 조건처럼 읽힌다(독립 리뷰) | 소유자 결정 | 같은 곳 (b) |
| 붙여 넣기 문장을 쓰는 평가 케이스를 저장소에 둘지: 지금은 테스트의 상수만 그 문장을 고정하고, `evals/`에는 그 문장을 쓰는 케이스가 없다(독립 리뷰) | 소유자 결정 | 같은 곳 (c) |
| unknowns-loop 단계를 실제로 돌리는 다회차 평가 케이스 추가(체크리스트 도입 판단의 근거) | 에이전트(추천 1순위) | `evals/multiturn/`의 기존 케이스 형식, `docs/skill-authoring-guide.md` 체크리스트 행 |
| 지켜볼 칸 읽기 | 다음 측정 때 | 아래 "지켜볼 칸" |

릴리스 규칙: 지원 모델은 Opus 5.5·GPT-6.1 Sol, medium effort(소유자). 평가 러너는 기본 `--effort medium`. 실행 회수는 `docs/skill-authoring-guide.md`의 표를 따른다(수정 확인은 실패 케이스 2회, 이웃 1회, 릴리스는 Opus 전체 1회 + Sol trigger 1회). 배포 본문을 바꾸면 버전을 올리고, `[Unreleased]`가 비어 있지 않을 때만 같은 버전 재생성이 허용된다. 평가 보조 도구(판정 스크립트, 릴리스 실행 스크립트)는 저장소 밖 `C:/Users/ajitta/work/kyu-probes/`(README 있음), Sol 확인은 빌드 VM `~/work/kyu-review/rel0124/codex_rel.py`(0.12.3 때는 `rel0123`).

GPT-6.1 Sol 확인 때 지킬 것(0.13.0에서 발견): Codex 앱은 소유자 계정에 올려 둔 플러그인 사본(당시 0.12.4)을 격리한 홈의 `.codex/plugins/cache/created-by-me-remote`로 동기화한다. 0.13.0의 처음 세 번 시도에서는 22개 세션 중 7–8개가 빌드 옆에 그 사본을 나열하고 그 사본의 `SKILL.md`를 읽었으므로, 세 번 모두 무효로 했다. `config.toml`의 `[features] remote_plugin = false`와 `[plugins."unknowns@created-by-me-remote"] enabled = false`는 막지 못했다. 막은 방법: 플러그인을 추가하기 전에 격리한 홈에 그 캐시 폴더를 미리 만들고 읽기 전용(`chmod 555`)으로 둔다. 실행 뒤에는 세션 기록에서 `created-by-me-remote/unknowns`가 0건인지, 22개 실행이 모두 빌드 버전의 `SKILL.md`를 읽었는지 센다(0.13.0: 0건, 22/22). 이전 릴리스의 GPT-6.1 Sol 확인에는 이 장치가 없었다.

## 0.13.0에서 끝난 일 (2026-11-12–13, PR #33)

소유자 판단(2026-11-12, 11-13) 네 가지를 한 버전에 담았다. 수치와 표는 CHANGELOG 0.13.0과 `IMPLEMENTATION_NOTES.md` 2026-11-13.

- 설명 11개를 짧은 세트로 바꿨다. 각 `SKILL.md`의 설명은 `scripts/skill-descriptions.json`의 문구와 글자 단위로 같다(200자 이하). 방법 요약과 끝 문장 "Clear to both sides: no skill or method."는 없다. 모든 대화에 실리는 양이 949 → 475토큰(cl100k)이다. 플러그인, 두 릴리스 zip, 스킬별 업로드 zip이 같은 설명을 쓴다. 규칙은 `.claude/rules/skill-writing.md` 18번, 테스트가 길이와 두 사본의 일치를 본다. 18번은 설명이 경계 문구 하나와 "runs even when …" 문구를 가질 수 있다고 적는다(반드시 갖는 것은 아니다). tweakable-plan 설명에는 native plan mode와의 경계가 없고, 본문의 크기 기준이 그 경우를 처리한다.
- 본문의 되읽기 문단, 라우팅 문장, 칸 문장은 모든 스킬에 남긴다. 근거 실행: 이름으로 부른 스킬(interview·brainstorm·blindspot, 각 2회)에 자명한 요청("sort the import lines")을 주었다. 되읽기 문단을 본문 10개에서 뺀 문구는 6회 중 6회 방법을 실행했고, 배포 문구는 6회 중 4회 요청을 바로 처리했다. 실행 전에 적어 둔 기준(배포 문구 6회 중 5회 이상)에는 못 미쳤고, 놓친 2회는 모두 blindspot이다. interview와 brainstorm에서는 배포 문구가 4회 중 4회, 문단을 뺀 문구가 4회 중 0회 요청을 바로 처리했다.
- 같은 파일의 다른 문장이 같은 범위로 같은 지시를 하는 문장 3개를 지웠다(스킬 본문 1개: blindspot의 두 문장, 에이전트 1개: independent-reviewer의 한 구절). 지운 문장마다 그 지시를 여전히 말하는 문장을 CHANGELOG 표에 적었다. blindspot의 "; a missing pick is undecided."는 5단계로 옮겼다.
- 처음에는 9개를 지웠다가 6개를 되돌렸다. 그래서 brainstorm·teach-me·tweakable-plan·deviation-log의 본문은 0.12.4와 바이트 단위로 같다(설명만 다르다). 넷은 스킬의 목표나 단계의 이유를 말하는 문장이다: brainstorm "The user picks; you draw the space.", teach-me "This skill fills the vocabulary gap.", tweakable-plan "A plan's purpose is …"(이유 문장도 원래 자리로), deviation-log "The buy-in and quiz skills read that log." 그런 문장은 중복처럼 보여도 남긴다는 것이 이 저장소의 앞선 결과다(`docs/features/concise-plugin-text/06-results.md`). deviation-log의 문장은 범위도 같지 않았다(같은 말을 하는 듯한 마무리 4·5번에는 조건이 붙어 있다). 나머지 둘은 Iron Rule이다(brainstorm 2번, tweakable-plan 2번). tweakable-plan은 2번이 없을 때 `alternatives-are-lettered`가 4회 중 2회 통과했고, 같은 날 0.12.4 문구는 2회 중 2회 통과했다.
- 세션 전체에 걸리는 "mode" 스킬은 더하지 않는다. 대신 두 README의 시나리오 A에, `CLAUDE.md` 한 줄 팁 옆에, 한 대화에서만 쓰는 붙여 넣기 문장을 넣었다. 측정(각 4세션): 무게 있는 요청에서 확인 전 수정 없음은 아무것도 없을 때 0/4, 붙여 넣기 문장 4/4, `CLAUDE.md` 한 줄 4/4. 작업 뒤 성과 질문은 0/4, 4/4, 0/4. 붙여 넣기 문장은 저장소의 되읽기 채점을 4회 중 3회(1회는 확인을 묻지 않고 고칠 점만 물었다), 사소한 요청 채점을 4회 중 3회(1회는 다른 정렬 순서를 제안했다) 통과했다. `CLAUDE.md` 한 줄은 둘 다 4/4다. 컨텍스트 압축 뒤에는 되읽기만 확인했다(2/2, 성과 질문은 재지 않음). 약 800토큰의 스킬 초안은 같은 행동(4/4, 4/4)을 냈지만 되읽기가 약 1,100자로 길어 되읽기 채점이 0/4였다(사소한 요청 채점 4/4). 이 실행들은 0.12.4의 설명에 스킬 초안이 목록에 있는 빌드로 돌렸고, `CLAUDE.md` 한 줄은 `CLAUDE.md` 파일이 아니라 덧붙인 시스템 프롬프트로 넣었다.
- 짧은 설명 측정(Claude Code 2.1.322, Opus, medium, 케이스당 1회, 기계 판정만, 본문은 0.12.4): trigger 22/22, 비코딩 22/22, unknown 칸 4/4, 네거티브 13/13. 네거티브는 "스킬이 하나도 로드되지 않음"이 아니라 케이스마다의 채점 항목으로 읽었다. 셋은 케이스가 허용하는 이웃 스킬(tweakable-plan·prototypes·teach-me)을 로드했고, 인터벌 케이스는 의도대로 내장 `loop`를 로드했다.
- 릴리스 확인(같은 엔진, 전체 1회, 커밋 `63e0360`: 짧은 설명과 그때 지운 9문장): 단발 88케이스의 채점 항목 195/206(점수에 드는 항목 126/134), 다회차 24/28. 네거티브와 unknown 칸의 판사 채점 항목은 짧은 설명으로 처음 채점했고, 정보용 weighty 두 케이스만 실패했다. 실패 목록은 CHANGELOG 0.13.0 **Checked**.
- 재실행(네 문장을 되돌린 뒤, Iron Rule 둘을 되돌리기 전): `noncode-en-brainstorm` 2/2, `neg-open-quiz-en` 3/3, `trigger-en-brainstorm` 1/1, `behavior-brainstorm-scout-finds-unused` 1/1. 최종 문구 전체로는 다시 돌리지 않았다.
- GPT-6.1 Sol(medium, Codex CLI, 커밋 `02484af`): trigger 22/22, 22개 실행 모두 0.13.0 `SKILL.md`를 읽었다. 앞선 세 번의 시도는 무효다(위 "GPT-6.1 Sol 확인 때 지킬 것").
- 독립 리뷰(글쓴이가 아닌 검토자, 2026-11-13): 패키징과 테스트의 결함은 없고, 기록과 규칙의 문구를 고치라는 판정이었다. 반영한 것: 되읽기 실행을 실행 전 기준과 함께 보고, 붙여 넣기 문장의 채점 결과와 실행 조건 기록, deviation-log 문장 복원, 규칙 18번, 공개 기록에서 공개되지 않은 자료를 가리키던 문장 삭제. 소유자에게 남긴 항목은 위 표.
- 확인한 것: `tools/package.py --check`, 단위 테스트 94개, `evals/run-manual.py --verify`, `claude plugin validate --strict` 두 개.
- 재지 않은 것: 최종 문구 전체(위), 짧은 설명의 ChatGPT·claude.ai 실행(Codex는 trigger 22개만), 1–6회짜리 칸의 빈도.

## 0.12.4에서 끝난 일 (2026-11-09–10, PR #31)

- 두 번째 규칙 기반 리뷰(네 규칙, 새 결함이 없는 라운드까지 반복): 11개 스킬 본문 수정 50건(의미 변경 24건), 두 에이전트 리뷰(independent-reviewer 문구 3라운드, scout 수정 없음).
- 소유자 결정 반영: 루프 첫 답에 step 2 네 항목, blindspot ②·⑤ 가정 판정에 근거·상태, 고르지 않은 프롬프트 수정은 미정으로 남김, quiz 객관식 다섯 개 한 번에, teach-me 출처 줄, quiz 제안은 AI가 대부분 만든 작업에만.
- buy-in: 사용자가 고르지 않은 한계도 최종 문서에 남김(0/2 → 2/2).
- deviation-log: 설명에서 "자동으로 시작" 주장을 뺌(측정 5회 중 0회 자동 로드). 확인된 대로 나온 점검 항목은 기록하지 않음(Wi-Fi 비밀번호 2/2 → 1/3).
- 측정용 eval 케이스 25개(단발 18, 다회차 7). 결정 규칙과 케이스별 결과는 `IMPLEMENTATION_NOTES.md` 2026-11-10.
- 릴리스 확인: Opus medium 전체 1회(CHANGELOG 0.12.4 Checked), Sol medium trigger 22/22(릴리스 뒤 태그 커밋으로 1회). 릴리스 zip sha256 일치, 빈 설정 설치 0.12.4(자체 마켓플레이스·`ajitta/claude-plugins`, 스킬 폴더 11개).

## 0.12.3에서 끝난 일 (2026-11-03–04, PR #28)

- 공식 스킬 작성 모범 사례를 이 저장소에 대응시킨 `docs/skill-authoring-guide.md`(참조 파일로 뺄 내용 점검: 없음, 실행 회수 표). 패키저가 예약어·설명의 XML 태그·본문 500줄을 검사한다.
- medium 기준 측정(Opus 5.5): 단발 303/318, 다회차 16항목 중 12개 3/3. 수정: independent-reviewer `Outcome:` 줄, quiz 예시 답 줄 금지, reference·quiz 설명의 "Runs even when …"과 본문 이유 문장(한국어 비코딩 0/3·1/3 → 2/2).
- 러너 수정: Claude Code 2.1.31x부터 에이전트 보고가 SubagentHandback으로 오고 도구 결과에는 안내문만 남는다. `run-manual.py`가 에이전트 기록에서 보고를 읽는다. 이전 0/3은 이 때문이었다(재판정 2/3).
- 규칙 기반 문구 리뷰(조건은 그것이 거는 결과 옆에, 범위 단어, 이유 있는 적은 지시, 한 이름)를 전 스킬·에이전트에 적용: 이름 통일과 빠진 경로 보충.
- 릴리스 확인: Opus medium 전체 1회 단발 156/161·다회차 16/16(API 500으로 깨진 20건 재실행), Sol medium trigger 22/22. 릴리스 zip sha256 일치, 빈 설정 설치 0.12.3(자체 마켓플레이스·`ajitta/claude-plugins`).
- 문구 점검(writing-for-models)은 이제 고친 diff 한 번, 점검자 한 명.

## 지켜볼 칸 (0.13.0에서 새로, 관찰이며 고치지 않음)

- blindspot: 이름으로 부르고 자명한 요청("sort the import lines")을 주면, 되읽기 문단이 있는 배포 문구에서도 방법을 실행했다(2회 중 2회, 문단을 뺀 문구도 2회 중 2회). interview와 brainstorm은 배포 문구에서 요청을 바로 처리했다.
- `behavior-unknowns-loop-terms-only`(계획이 쉬운 말 설명을 사각지대 점검보다 앞에 둠): 2026-11-13의 재실행 5회 중 0회 통과(0.13.0 문구 2회, 0.12.4 문구 3회), 전체 실행의 1회도 실패. 0.12.4의 기록은 "the loop's teach-me order 3/3"이다. 이번 릴리스에서 생긴 실패가 아니고, 원인은 모른다.
- 짧은 설명에서 빠진 문구: blindspot의 "run it even when you could answer directly"(0.7.1에서 로드 실패를 고친 문구), tweakable-plan의 "Not native plan mode" 문장. 전체 실행 1회에서 `trigger-ko-blindspot`과 `noncode-ko-blindspot`은 blindspot을 로드했고, 한 파일짜리 케이스의 `defers-to-plan-mode`는 1/1이었다.
- quiz 다회차 `key-hidden-until-answered`: 한 문항의 정답 보기가 다른 보기의 약 두 배 길이였다(1회 중 0회 통과). 0.12.3부터 보던 "정답 보기가 다른 보기보다 김"과 같은 모양이다.
- quiz 설명: 범위 문구("work the model largely produced")가 빠지고 "runs even when a quiz is easy to write"가 "quiz me" 옆에 남았다. 상식 퀴즈 요청 `neg-open-quiz-en`은 3/3이었다.
- brainstorm `noncode-en-brainstorm`: 사용자가 고르기 전에 후보 하나를 추천했다(전체 실행 0/1, 문장을 되돌린 뒤 2/2).
- tweakable-plan `alternatives-are-lettered`: Iron Rule 2가 없을 때 4회 중 2회 통과(놓친 실행마다 결정 항목 하나의 대안에 문자 표기가 없었다). 규칙을 되돌렸고, 되돌린 본문은 0.12.4와 같다(그 본문은 같은 날 2회 중 2회 통과).

## 지켜볼 칸 (0.12.4에서 새로, 각 1회 또는 소수 회차의 실수)

- brainstorm: 후보 제목을 "Fix the metric first"처럼 지시형으로(4회 중 2회).
- teach-me: 와인 어휘를 말없이 구매 상황으로 틀 잡음(3회 중 2회 통과), 초안에 가정한 세부를 일부만 표시(0/2).
- unknowns-loop(영어): 첫 답에 변경 범위 누락(9회 중 8회 통과).
- quiz(한국어): 해설이 Q2의 수치를 그대로 풀어 줌.
- blindspot: 부분 선택 뒤 가정 판정(4회 중 2회 통과).
- deviation-log: 계획대로 확인된 비밀번호를 기록(3회 중 1회).
- interview: 깊은 인터뷰 첫 답에 질문 40개(2회 중 1회).

## 지켜볼 칸 (0.12.3 기준, 각 3회 중 1회 또는 1회 중 1회)

- prototypes: 이유 없는 skip에 대비 질문을 하지 않음.
- quiz: 정답 보기가 다른 보기보다 김.
- blindspot: *inferred* 카드에 근거를 적지 않음.
- interview: 3라운드 질문 순서.
- tweakable-plan: 대안 문자 표기, plan mode로 넘기는 작은 작업.
- buy-in: 근거 없는 수치를 근거로 사용(1회, 재확인 2/2).
- `neg-open-text-en`: 교정 뒤 긴 변경 목록. `trigger-ko-blindspot`: 1회 스킬 없이 직접 답(재확인 3/3).

작성 2026-10-28, 0.12.2 릴리스(PR #26) 뒤 갱신. 새 세션은 이 문서의 **상태**를 git·태그·릴리스·CI와 먼저 대조하고 시작한다. 이 문서는 작업 지시가 아니라 출발점이다. 소유자 판단이 필요한 항목은 그 번호로 묻는다.

## 상태 (2026-10-28, 0.12.2 기준 — 위 0.12.3 항목이 우선)

- 배포: `unknowns--v0.12.2`, GitHub Release에 `know-your-unknowns.zip`·`know-your-unknowns-openai.zip`. 카탈로그 `ajitta/claude-plugins`는 `git-subdir` `plugins/unknowns`를 가리킨다.
- 0.12.2와 0.12.1은 본문 수정판이다(0.12.2: interview·blindspot, 0.12.1: blindspot·brainstorm·interview·quiz). 설명·스킬 이름·항상 로드되는 토큰은 0.12.0과 같다.
- 0.12.0은 범위 재정의 판이다. 플러그인은 사용자와 AI가 아는 것의 세 칸(사용자는 모르고 AI는 아는 것, AI가 모르는 것, 둘 다 모르는 것)을 어떤 분야에서든 다루고, 산출물이 아니라 성과로 판단한다(`.claude/rules/skill-writing.md` 0번). 둘 다 아는 요청은 범위 밖이고 바로 처리한다.
- **Breaking(0.12.0):** `loop` → `unknowns-loop`, `notes` → `deviation-log`, `plan` → `tweakable-plan`. 설명 11개는 영어로만 쓰고, 끝 문장은 "Clear to both sides: no skill or method." (0.13.0에서 설명을 짧은 세트로 바꾸면서 이 끝 문장은 없어졌다.)
- 요청 되읽기(read-back)는 각 스킬 본문과 unknowns-loop 1단계에 있다(소유자 판단으로 유지, 2026-10-28). 스킬이 뜨지 않는 무거운 요청에서도 되읽기를 원하는 사용자는 README가 안내하는 한 줄을 자기 `CLAUDE.md`에 넣는다(측정 9/9).
- 구조: 원본 `skills/`(스킬마다 SKILL.md 하나, 공유 참조 파일 없음), `claude-code/agents/` → `tools/package.py`가 `plugins/unknowns/`와 두 zip을 생성(커밋됨). 코드 없음, 목록 아이콘 PNG 하나.
- 작성 원칙: `.claude/rules/skill-writing.md` 0번(목적)과 17번 — 금지 문장·읽기 전용 약속·도구 허용 목록·정체성 문장("You are …")을 쓰지 않는다. 강제는 사용자 하네스의 몫이다. 두 에이전트는 모든 도구를 물려받고, 플러그인은 git 절차를 따로 두지 않는다.
- 측정 기록: CHANGELOG 0.12.0·0.12.1·0.12.2의 **Checked**·**Not measured** 절.
- 평가: 단발 70케이스(`evals/run-manual.py`), 다회차 5케이스(`evals/run-multiturn.py`, 시뮬레이션 사용자와 2–5턴). 입력 자료가 필요한 케이스는 CLI 형식 그대로 `files/` + `place-files.sh` + `case.yaml`의 `context: scaffold_script:`를 쓰고(`claude plugin eval --scaffold`와 같음), 러너가 실행 전에 그 스크립트를 실행한다. 생성된 에이전트가 돌려준 보고서는 `agent_reports`로 남아 `focus: trace` 채점에 쓰인다.

## 0.12.1에서 끝난 일

- 검토 에이전트(independent-reviewer) 평가 케이스 두 개: 완료 기준 하나를 몰래 빠뜨린 git 저장소, 수치가 기록과 어긋나는 시범 사업 보고서. 각 3회, 30/30.
- reference 다회차 케이스(사용자가 2턴에서 의미 지도의 한 행을 번호로 고침): 3회, 6/6.
- 얇은 칸 3회씩: prototypes 단발 5케이스·다회차, blindspot 근거 상태, brainstorm 판단 보류, interview 이유·순서, 한국어 blindspot 트리거 10회. 실패를 읽고 고친 결과는 CHANGELOG 0.12.1.
- Codex 실행 확인(격리 HOME+CODEX_HOME): 이름이 바뀐 세 스킬, 이름·영어·한국어 트리거 각 2회 18/18.
- skill-creator 기준 점검: 16개 항목, 형식 수정 3개 반영.

## 0.12.2에서 끝난 일 (2026-10-28, PR #26)

- interview 다회차 순서 칸(소유자 판단: 다른 수정 하나, 3회): 라운드를 쓰기 전에 질문을 Question Priority 순으로 정렬하는 하위 단계를 두 번 시도했다. 4단계에 두면 2·3라운드 순서는 3/3이었지만 1라운드가 "확실한 것·가정한 것" 질문을 3회 중 2회 빠뜨렸다. 2단계 맨 앞으로 옮기고 그 질문을 이름으로 부르자 1라운드는 3/3이었지만 why 후속 질문이 해악 질문 아래로 내려갔다(3회 중 1회). 두 번 모두 3/3이 아니어서 0.12.1 문구로 되돌렸고, 되돌린 문구는 이번 6회에서 순서 6/6이었다.
- interview 넷 이하 칸: "why it matters" 줄 안에 다섯 번째 결정 질문이 들어간 실행이 다시 나와(6회 중 1회) 2a에 "이유 줄 안의 물음표"도 넷에 센다고 넣었다. 다회차 6회 24/24, 단발 다섯 케이스 18/18.
- blindspot 근거 상태 칸: 0.12.1 본문에서 3회 중 1회 *unchecked* 카드가 카드와 집계에 남아, 카드를 쓰는 4단계에 조건을 넣었다(카드 상태는 *confirmed*·*inferred*, *unchecked*는 **Needs checking**으로, 집계는 카드 수). 다회차 6회 24/24, 단발 여섯 케이스 30/30.
- buy-in이 검토 에이전트 보고서를 옮기는지(소유자 판단: 본문은 고치지 않고 지켜봄): 기존 buy-in 케이스 넷은 Agent 도구를 허용하지 않아 검토 에이전트를 부를 수 없었으므로, 시범 사업 보고서 자료를 쓰는 `behavior-buy-in-relays-reviewer`를 더했다. 3회 모두 에이전트를 불렀고, 써낸 buy-in 문서가 에이전트의 성과 판정과 기록에서 다시 센 수치·근거 없는 주장·보증금 문제를 담았다(9/9). 문서를 가리키는 짧은 채팅 답은 3회 중 1회만 성과를 언급했지만 산출물은 문서이므로 본문은 고치지 않았다.
- writing-for-models(Claude): interview·blindspot 파일별 점검과 diff 점검, 지적 19개 모두 인용 확인, 확정 0.

## 소유자 대기 (에이전트가 할 수 없음)

- O1 (해결, 2026-10-28, 0.12.2): 소유자가 확인했다고 보고. claude.ai 계정 설치는 Add marketplace 경로였다. 빌드 VM에 동기화된 계정 사본(마켓플레이스 `know-your-unknowns`, 버전 0.12.2)의 본문 13개가 `plugins/unknowns`와 바이트 단위로 같다(frontmatter는 동기화가 한 줄 문자열로 다시 씀). ChatGPT zip 업로드와 ChatGPT 모바일의 스킬 호출, 그리고 Add marketplace 설치가 Claude 모바일에 이어진다는 것은 소유자 보고이며 화면 증거는 기록하지 않았다. claude.ai zip 업로드는 마켓플레이스 경로가 모바일까지 이어지므로 하지 않는다(소유자 판단). README 두 언어의 확인 범위를 이에 맞췄다. 확인하지 않은 경로: claude.ai zip 업로드, Claude 데스크톱, Codex CLI, ChatGPT 데스크톱 마켓플레이스.

## 소유자 판단 기록 (2026-10-28)

- 업로드용 짧은 설명의 대리 측정(520회): 승인, 0.12.1 릴리스 뒤 실행해 통과(아래 "짧은 설명의 측정 기록과 다시 재는 방법"). 0.13.0부터 이 짧은 설명이 배포 설명이다.
- 설명을 skill-creator 권고대로 더 적극적으로("pushy") 쓰지 않는다. 이 빌드의 라우팅은 이름 44/44(0.12.0), 한국어 blindspot 트리거 10/10, Codex 18/18이다.
- teach-me의 예(색 보정 한 분야)는 유지한다. 비교 표가 글·코드·절차를 다루고 비코딩 케이스가 통과한다.
- 본문의 되읽기 문장은 유지한다(아래 "측정이 얇은 곳" 마지막 항목).
- interview 다회차 순서 칸은 이번 릴리스에서는 편차로 두고, 다음 라운드에 다른 수정 하나를 3회로 시도한다.
- 검토 에이전트 보고서를 호출한 모델이 옮기면서 성과 판정을 빠뜨린 건: 본문은 고치지 않고 buy-in 실행에서 지켜본다.
- (0.12.2 릴리스 때) 0.12.2를 O1 재업로드 전에 릴리스한다. interview 다회차 순서 칸은 더 고치지 않고 지켜보기만 한다(배치가 2/3 아래로 떨어지거나 실패 모양이 바뀔 때만 다시 다룬다). `behavior-buy-in-relays-reviewer`는 평가에 남긴다. buy-in 문서를 가리키는 짧은 채팅 답에 성과가 빠지는 것은 고치지 않는다(산출물은 문서).

## 다음 라운드 작업 (브랜치에서, main 직접 수정 금지)

버전은 소유자가 릴리스를 승인할 때까지 0.12.2에 둔다(CHANGELOG `## [Unreleased]`에 기록 — `package.py`가 이 경우에만 같은 버전 재빌드를 허용).

### 지켜볼 칸

- interview 다회차 순서: 두 라운드 동안 배치마다 2/3이었고 이번 라운드에는 같은 문구로 6/6이었다. 3–6회 배치로는 수정과 변동을 가를 수 없다. 정렬 하위 단계는 두 위치 모두 다른 칸을 흔들었으므로(위) 다시 시도하지 않는다.
- 이번 라운드의 두 수정(interview 이유 줄의 물음표, blindspot 4단계의 *unchecked*)은 원래 3–9회에 1회꼴로 나오던 실수다. 6회 무실패는 사라졌다는 증거가 아니다. 다음 배치에서도 지켜본다.

### 측정이 얇은 곳

- 검토 에이전트를 buy-in을 거치지 않고 이름으로 부를 때, 호출한 모델이 사용자에게 전하는 요약에서 에이전트의 성과 판정이 빠진 적이 있다(첫 실행 3/3). 에이전트 보고서 자체에는 있었다. buy-in 실행에서는 문서가 판정을 3/3 담았다(위). 이름으로 부르는 경우는 다시 돌리지 않았다.
- Codex에서만 보인 것(Claude에서는 통과, 본문은 고치지 않음): interview 1라운드가 다음 라운드가 이어진다고 말하지 않았다(1회 중 1회). tweakable-plan은 완료 기준을 "completion criteria"로 써서 정규식 채점만 놓쳤다(방법은 지킴).
- 본문의 "둘 다 이해한 요청이면 방법 없이" 문장을 스킬 산출물을 직접 요청한 경우("quiz me")까지 건너뛰라는 뜻으로 읽는 검사자 지적이 이번에도 나왔다(quiz). 실행에서 건너뛴 적은 없다. 건너뛰는 실행이 나오면 범위를 "이 스킬 자체의 산출물 요청이 아닌 경우"로 좁힌다.

### 짧은 설명의 측정 기록과 다시 재는 방법

0.13.0부터 `scripts/skill-descriptions.json`의 짧은 설명이 각 `SKILL.md`의 설명이다(소유자 판단 2026-11-12). 업로드용 설명이 따로 있지 않으므로 변형 플러그인을 만들어 대리 측정할 필요가 없고, `plugins/unknowns`를 그대로 재면 된다.

- 기록 1(2026-10-28, Claude Code 대리 측정, 케이스 26개 × 10회): 짧은 설명 259/260, 당시의 긴 설명 260/260(Fisher p = 1.0, Wilson 하한 97.9%), 충돌 케이스 40/40 대 40/40. 놓친 1회는 한국어 blindspot에서 스킬 없이 바로 답한 경우다. CHANGELOG 0.12.2.
- 기록 2(0.13.0, 짧은 설명을 `SKILL.md` 설명으로 넣은 빌드, 케이스당 1회, 기계 판정만): trigger 22/22, 비코딩 22/22, unknown 칸 4/4, 네거티브 13/13. CHANGELOG 0.13.0.
- 기록 3(0.13.0 릴리스 확인, 전체 1회): 네거티브와 unknown 칸의 판사 채점 항목을 짧은 설명으로 처음 채점했다. 정보용 weighty 두 케이스만 실패했다. CHANGELOG 0.13.0.
- 다시 잴 때: `evals/run-manual.py`로 `trigger-*` 22개, `noncode-*` 22개, `unknown-*` 4개, `neg-*` 13개를 케이스당 1회(설명을 고친 뒤의 확인) 또는 의심 가는 케이스만 3회(`docs/skill-authoring-guide.md`의 실행 회수 표). 설명을 고치면 `SKILL.md`와 `scripts/skill-descriptions.json`을 함께 고친다(테스트가 두 사본의 일치를 본다).
- 스킬별 업로드 zip(`scripts/build-skill-zips.py`)은 frontmatter를 JSON 따옴표 형식으로 다시 쓴다. `run-manual.py --verify --plugin-dir <zip을 푼 디렉터리>`는 그 형식의 description을 읽지 못해 거짓 실패를 낸다(실행 경로에는 영향 없음).
- claude.ai 자체의 라우팅과 업로드 화면은 headless로 돌릴 수 없어 어느 기록도 보여 주지 않는다.

## 규칙

- 모든 판단은 `.claude/rules/skill-writing.md` 0번(세 칸, 어떤 분야든, 성과)을 따른다. 코딩은 여러 예 중 하나다.
- 스킬 설명은 200자 이하이고 `scripts/skill-descriptions.json`과 같은 문구다(`.claude/rules/skill-writing.md` 18번). 설명을 고치는 것은 라우팅을 고치는 것이므로 trigger·비코딩·네거티브 케이스를 다시 돌린다.
- 본문의 되읽기 문단, 라우팅 문장, 칸 문장은 모든 스킬에 남긴다(소유자 판단 2026-11-13).
- 스킬의 목표·산출물이나 단계의 이유를 말하는 문장은 중복처럼 보여도 지우지 않는다(`docs/features/concise-plugin-text/06-results.md`; 0.13.0에서 그런 문장 넷을 지웠다가 되돌렸다).
- 모델이 읽는 파일을 고치면 writing-for-models 점검: 파일당 검사자 하나, 고친 뒤 diff 점검. 이 플러그인은 소유자 판단으로 Claude 검사만 한다. 검사자가 금지 문장을 제안하면 할 일 문장으로 바꾸거나 버린다(17번).
- 소유자는 버전 간 A/B 비교를 원하지 않는다. 플러그인 자체의 실행에서 실패를 읽고 고친다.
- 공개 텍스트(커밋 메시지, PR 제목·본문, README, CHANGELOG, docs)에 소유자 개인 약칭이나 내부 작업 용어를 쓰지 않는다.
- 릴리스: 소유자 승인 후 `plugin-manifest.json` 버전 → CHANGELOG 이동 → 재생성 → CI → 머지 → 주석 태그 `unknowns--vX.Y.Z` → 릴리스 자산 sha256 대조 → 빈 설정 설치 확인 → 카탈로그 확인.
