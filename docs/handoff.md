# 다음 라운드 인계 — 0.11.0 이후

작성 2026-10-27. 새 세션은 이 문서의 **상태**를 git·태그·릴리스·CI와 먼저 대조하고 시작한다. 이 문서는 작업 지시가 아니라 출발점이다. 소유자 판단이 필요한 항목은 그 번호로 묻는다.

## 상태 (2026-10-27)

- 배포: `unknowns--v0.11.0`, GitHub Release에 `know-your-unknowns.zip`·`know-your-unknowns-openai.zip`. 0.11.0은 플러그인을 방법만 남기고 압축한 판이다(CHANGELOG 0.11.0의 **Breaking** 절). 카탈로그 `ajitta/claude-plugins`는 `git-subdir` `plugins/unknowns`를 가리킨다.
- 구조: 원본 `skills/`(스킬마다 SKILL.md 하나, 공유 참조 파일 없음), `claude-code/agents/` → `tools/package.py`가 `plugins/unknowns/`와 두 zip을 생성(커밋됨). 코드 없음, 목록 아이콘 PNG 하나.
- 작성 원칙: `.claude/rules/skill-writing.md` 17번 — 금지 문장·읽기 전용 약속·도구 허용 목록·정체성 문장("You are …")을 쓰지 않는다. 강제는 사용자 하네스의 몫이다. 두 에이전트는 모든 도구를 물려받고, 플러그인은 git 절차를 따로 두지 않는다.
- 측정 기록: CHANGELOG 0.11.0의 **Checked**·**Not measured** 절.
- 평가: 단발 33케이스(`evals/run-manual.py`), 다회차 4케이스(`evals/run-multiturn.py`, 시뮬레이션 사용자와 2–5턴).

## 소유자 대기 (에이전트가 할 수 없음)

- O1. claude.ai Customize › Plugins에 0.11.0 zip 재업로드(또는 Check for updates), ChatGPT에 OpenAI zip 업로드, 모바일에서 스킬 하나 호출. 결과가 오면 README 두 언어의 확인 범위 문구를 확인된 범위로만 고친다.

## 다음 라운드 작업 (브랜치에서, main 직접 수정 금지)

버전은 소유자가 릴리스를 승인할 때까지 0.11.0에 둔다(CHANGELOG `## [Unreleased]`에 기록 — `package.py`가 이 경우에만 같은 버전 재빌드를 허용).

### 한국어 blindspot 트리거

`trigger-ko-blindspot`에서 10회 중 3회는 스킬을 부르지 않고 바로 답했다. 고치려면 description을 바꿔야 하고, 바꾸면 11개 스킬의 라우팅 셀(트리거 en/ko, neg 케이스)을 다시 돌린다.

### interview 잔여

- 이유 없는 취향 질문이 더 큰 반경의 질문보다 먼저 오는 경우가 약 3회 중 1회(`questions-carry-reasons-in-priority-order`).
- 거절된 선택지가 확정 결정에 섞인 경우 1회(`asks-before-deciding`).
- 최종 1회 점검에서 `trigger-ko-buy-in`이 한 번 실패했고 원인을 아직 보지 않았다.

### 업로드용 짧은 설명의 호출 측정

claude.ai Customize › Skills에 올리는 짧은 설명(`scripts/skill-descriptions.json`)은 모델로 측정한 적이 없다. 테스트는 길이(200자 이하)와 README 문구 포함만 본다. 업로드 화면 자체는 headless로 돌릴 수 없으므로 Claude Code 대리 측정으로 한다.

- 변형 만들기: `python3 scripts/build-skill-zips.py --out <절대 경로>/dist`, 새 디렉터리에 `plugins/unknowns/`의 `.claude-plugin`·`agents`·`LICENSE`·`NOTICE`·`README.md`를 복사하고 zip을 그 `skills/`에 푼다. `unknowns:` 이름공간이 유지되고 본문은 같으며 설명만 다르다. `claude plugin validate --strict`로 확인.
- 실행: 긴 설명(`plugins/unknowns`) 대 짧은 설명 두 arm을 같은 날 병렬로, `trigger-*` 22케이스와 발동하면 안 되는 `neg-*` 4케이스, 케이스당 10회 이상(약 520회). 케이스별과 합산으로 Fisher 정확검정. 케이스당 10회로는 큰 하락만 보이므로 합산 비교가 핵심이다.
- 주의: `run-manual.py --verify --plugin-dir <변형>`은 JSON 따옴표 형식의 description을 읽지 못해 거짓 실패 11건을 낸다(실행 경로에는 영향 없음).
- 결과는 "claude.ai 업로드 설명의 Claude Code 대리 측정"으로 기록하고, 통과하면 `scripts/skill-descriptions.json`의 `_comment` 배열에 측정 날짜와 결과를 한 줄 추가한다. claude.ai 자체의 라우팅은 이 측정이 보여 주지 않는다.

### 검토 에이전트(independent-reviewer) 평가 케이스

평가 케이스가 없다. 완료 기준 하나를 몰래 빠뜨린 작은 git 저장소로 손으로 두 번 돌렸을 때(압축 전)는 두 번 모두 빠진 기준을 잡았다. 케이스로 만들려면 실행 전에 임시 작업 디렉터리에 고정 저장소를 깔아 두는 기능이 러너에 필요하다. 채점: 각 완료 기준 판정, 빠진 기준 적발, 주장 점검 절.

### Codex 실행 확인

0.11.0을 Codex에서 돌린 적이 없다. 격리 HOME+CODEX_HOME으로 라우팅과 동작 케이스 몇 개를 확인한다.

### 작성 스킬 기준 점검

소유자가 말한 스킬·에이전트 작성 스킬이 Anthropic 조직 스킬 `skill-creator`라면 그 기준으로 한 번 점검한다(Claude Code 내장 `plugin-authoring`은 훅과 UI 확장용이라 해당 없음).

## 규칙

- 모델이 읽는 파일을 고치면 writing-for-models 점검: 파일당 검사자 하나, 글을 쓴 엔진과 다른 엔진도 검사, 고친 뒤 diff 점검. 검사자가 금지 문장을 제안하면 할 일 문장으로 바꾸거나 버린다(17번).
- 소유자는 버전 간 A/B 비교를 원하지 않는다. 플러그인 자체의 실행에서 실패를 읽고 고친다.
- 공개 텍스트(커밋 메시지, PR 제목·본문, README, CHANGELOG, docs)에 소유자 개인 약칭이나 내부 작업 용어를 쓰지 않는다.
- 릴리스: 소유자 승인 후 `plugin-manifest.json` 버전 → CHANGELOG 이동 → 재생성 → CI → 머지 → 주석 태그 `unknowns--vX.Y.Z` → 릴리스 자산 sha256 대조 → 빈 설정 설치 확인 → 카탈로그 확인.
