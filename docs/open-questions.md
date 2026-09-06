# 결정 기록과 미결 사항

작성: 2026-07-11(사각지대 26건 전환 직후) · 개정: 2026-09-06(리뷰 웨이브 결과 반영).

2026-07-11에는 전부 "미결정"이었다. 2026-09-06 리뷰 웨이브에서 A1–A5와 B6이 결정됐고,
결정 내용은 각각 근거 파일에 실제로 반영돼 있다. 이 문서는 그 결정의 색인이자,
아직 결정할 수 없는 항목(B)의 대기 목록이다.

근거 문서: [README.md](README.md)(이 디렉터리의 색인),
[trigger-eval-v0.3.0.md](trigger-eval-v0.3.0.md), [trigger-matrix.md](trigger-matrix.md),
[value-contract.md](value-contract.md), [value-scorecard.md](value-scorecard.md),
`CHANGELOG.md`·`IMPLEMENTATION_NOTES.md`(저장소 루트).

## A. 결정 완료

| # | 질문 | 결정 | 반영된 곳 |
|---|------|------|-----------|
| A1 | 뷰어 없는 CLI에서 HTML 산출 허용? | **3단 사다리로 확정.** ① Artifact 도구가 있으면 게시하고 링크를 준다 ② 없고 파일 쓰기가 되면 `.unknowns/<YYYY-MM-DD>-<skill>-<slug>.html`을 쓰고 열어보라고 안내한다 ③ 둘 다 안 되면 markdown. 가능한 가장 높은 칸이 이긴다. 어느 칸이든 조립된 기본 회신은 대화에 평문으로 남긴다 — 탭을 닫아도 산출물이 살아남게. "HTML 강제"도 "markdown 강제"도 아니라 환경 판정으로 결정된다 | [skills/loop/references/output-routing.md](../skills/loop/references/output-routing.md) §1, 산출물을 만드는 9개 `SKILL.md`의 출력 블록(`interview`·`notes`는 원래부터 예외) |
| A2 | 가치 계약 수치 승인 | **릴리스 계수를 달력 창으로 교체하고 승인.** 강등은 "처음 5회 사용에서 결정 변경 0회", 제거 계열은 "신규 행 60일간 0건 → README에 미측정 표기 / 120일간 0건 → 유지보수 모드". 미사용 상태에서는 릴리스가 안 나오므로 릴리스 계수기는 조건이 필요한 바로 그 순간에 멈춰 있다는 것이 교체 이유. 전부 잠정값이며 실측 10행에서 재검토 | [value-contract.md](value-contract.md) 핵심 계약 4·5, "측정 시계 현황" |
| A3 | 이탈 기록 매체 완화? | **완화하지 않고 강화.** `IMPLEMENTATION_NOTES.md`가 이미 있거나 `init`을 돌린 뒤에는 파일 append가 필수이고, 대화 요약만으로는 규칙을 만족하지 않는다(리마인더 훅·buy-in·quiz가 전부 이 파일을 읽는다). 파일이 아예 없는 경우에만 대화 요약을 허용하되, 마지막 메시지에 "노트 파일이 없다"고 반드시 밝힌다 | [skills/notes/SKILL.md](../skills/notes/SKILL.md) File Rules |
| A4 | 배포 zip 릴리스 정책 | **전제가 틀렸다.** `v0.3.0` 태그는 존재한 적이 없다(로컬·origin 모두 태그 0개) — "HEAD ≠ v0.3.0 태그"라는 보류 사유 자체가 성립하지 않았고, 0.3.0은 커밋 `622c32b`를 가리킨다. 그리고 CLI가 만드는 태그 이름은 `v0.4.0`이 아니라 **`unknowns--v0.4.0`**(`claude plugin tag`의 `{name}--v{version}` 형식)이다. 결정: 이 이름으로 태그를 만들고, 그 태그에서 만든 Release에 `unknowns-v0.4.0.plugin`을 첨부한다. `scripts/build-plugin.sh`가 깨끗한 트리 + 버전이 일치하는 태그를 강제하므로 태그 없이는 애초에 빌드되지 않는다. 단 그 스크립트의 **기본 태그 이름은 `v0.4.0`**이므로 `scripts/build-plugin.sh unknowns--v0.4.0`처럼 인자로 넘겨야 한다 (또는 스크립트의 기본값을 CLI 형식에 맞추거나). 저장소 루트에 남아 있는 `unknowns-v0.3.0.plugin`은 커밋되지 않은 트리에서 만든 것이라 릴리스 자산이 아니다 — 삭제 대상 | `CHANGELOG.md` 0.4.0, [scripts/build-plugin.sh](../scripts/build-plugin.sh) |
| A5 | 스코어카드 기록 습관 | **제품 내 캡처 + 릴리스 시점 회고, 둘 다.** 사용 직후 loop 10단계·quiz 마무리에서 `AskUserQuestion` 한 번으로 한 행을 받아 `.unknowns/scorecard.md`에 적고, 릴리스 때 누적분을 한 번에 회고한다. 어느 한쪽만으로는 안 된다 — 즉시 캡처만 하면 추세를 아무도 안 보고, 회고만 하면 그때 가서 기억이 없다. **잔여**: 즉시 캡처는 아직 스킬에 배선되지 않았고 수동 절차만 있다 | [value-scorecard.md](value-scorecard.md) "직접 기록하는 법", 배선은 미구현 |
| A6 | 에이전트 `memory` frontmatter 사용? | **v0.4.0에서는 두 에이전트 모두 끈다.** 필드 자체는 플러그인 에이전트에서 지원된다(미지원이라 못 쓰는 게 아니라 안 쓰기로 한 것). 켜면 메모리 파일을 관리하라고 `Read`/`Write`/`Edit`가 자동으로 활성화되는데, 이는 두 에이전트의 "저장소 파일을 절대 만들거나 고치지 않는다" 지시, README의 read-only 서술, 그리고 이번에 넣은 `PreToolUse` Bash 가드와 정면으로 충돌한다. 재검토 조건: `.claude/agent-memory/<agent>/`로 범위를 좁힌 PreToolUse 가드와 README 정정을 **함께** 준비할 때만 | `agents/*.md`(변경 없음이 결정 내용), `CHANGELOG.md` 0.4.0 |
| A7 | 플러그인 페이로드를 `plugins/unknowns/`로 이동? (PKGSPEC-8) | **0.4.0에서는 하지 않는다 — 실측 후 되돌림.** 실제로 옮겨 봤고, 그 즉시 실행 중이던 세션의 모든 Bash 호출이 깨졌다: 디렉터리 소스로 설치된 플러그인은 세션 시작 시점에 `${CLAUDE_PLUGIN_ROOT}`를 저장소 루트로 고정하므로, `hooks/`가 사라지면 `PreToolUse` 가드가 `[Errno 2] No such file` 로 exit 2 → 도구 호출 차단. GitHub 마켓플레이스 설치자는 `/plugin marketplace update` 후 새 `source`를 읽으므로 무사하지만, 개발용 디렉터리 설치는 마켓플레이스 재등록 전까지 깨진다. 편익 쪽은 이미 줄었다 — 이 이동의 주 목적이던 "plugin-form 검증 불가"는 CI에 `claude plugin validate .claude-plugin/plugin.json --strict`를 넣어 해결했고(PKGSPEC-1), 남은 편익은 설치 용량(docs·tests·evals·.github 약 500KB)과 로컬 strict 검증에서 뜨는 `CLAUDE.local.md` 경고뿐이다. 공개 저장소 push 직전에 30개 파일 변경 위에 25곳의 경로 변경을 얹을 값어치가 없다고 판단. **재개 조건**: 독립 릴리스로 분리하고, CHANGELOG에 "마켓플레이스 재등록 필요"를 명시하고, 격리 HOME 설치 테스트를 먼저 통과시킬 것 | 되돌림(변경 없음이 결정 내용), `IMPLEMENTATION_NOTES.md` 2026-09-06 |

## B. 재검증 대기

### B1 — scout 유효 도구에서 Grep/Glob 누락 (미해결, 최우선)

**관측**: `unknowns-scout`는 `tools: Read, Grep, Glob, Bash, WebFetch, WebSearch`를 선언하는데,
스폰해서 보면 Grep/Glob이 유효 도구에 없는 것처럼 보인다(2026-07-11 최초 관측,
`IMPLEMENTATION_NOTES.md` 2026-07-11 항목 / 2026-09-06 리뷰에서 재관측).

**왜 두 프로브 모두 결론이 못 되는가**: 두 번 다 **자기 메인 루프에도 Grep/Glob이 없는 세션**에서
프로브를 돌렸다. 서브에이전트의 유효 도구는 선언 목록과 호스트 세션 도구 풀의 교집합이므로,
이 조건에서는

- ① 유효 도구가 호스트 세션의 풀로 좁혀진 것(플러그인은 정상)
- ② 플러그인 agent frontmatter 결함

이 둘이 **같은 관측을 만든다**. 관측은 두 가설 모두와 정합적이고, 따라서 아무것도 구분하지 못한다.
덧붙여 에이전트가 스스로 나열한 도구 목록은 증거가 아니다 — 자기 보고이지 실행 결과가 아니다.

**재프로브 조건 (셋 다 만족해야 유효)**

1. **대화형 `claude` 세션**에서 돌린다. `-p` 헤드리스도, auto mode 하네스도 아니다.
2. 그 세션의 **메인 루프가 Grep과 Glob을 실제로 가지고 있음을 먼저 확인**한다. 이 확인이
   프로브의 전제조건이고, 빠지면 다시 같은 교집합 함정에 빠진다.
3. scout에게 도구 목록을 **말하게 하지 말고 실제로 호출**시킨다. 예: "Grep으로 이 저장소에서
   `NOTES_NAME`을 찾고, Glob으로 `skills/*/SKILL.md`를 나열해라." 호출 성공/거부가 증거다.
   더 강하게 잡으려면 `--settings`의 PreToolUse 훅으로 `agent_type` + `tool_name`을 기록한다.

**결론 전까지 하지 않을 것**

- `agents/*.md`의 `tools` 줄을 건드리지 않는다. 현재의 쉼표 문자열 형식은 공식 문서 스펙과 일치한다.
- Claude Code 버그로 보고하지 않는다. 재현 조건이 아직 분리되지 않았다.
- `hooks/scripts/agent_readonly_guard.py`의 scout 허용 목록에서 `grep`/`rg`/`find`를 빼지 않는다.
  Grep/Glob이 정말 없다면 Bash 검색이 scout의 유일한 탐색 경로이고, 여기를 막으면 에이전트가 무력해진다.

결과는 trigger-eval 후속 문서에 기록한다.

### 그 밖의 대기 항목

| # | 항목 | 방법 | 트리거 조건 |
|---|------|------|------------|
| B2 | Windows에서 훅 스크립트 동작 | CI에 `windows-latest` 잡이 추가됐다(스크립트 단위 테스트만 — 훅 실행 경로는 아님). **아직 푸시 전이라 실행된 적 없다**; 첫 실행 결과로 판정 | 0.4.0 푸시 직후 |
| B3 | Cowork 출력 분기 | Cowork에서 prototypes/plan 호출, A1 사다리의 어느 칸이 잡히는지 관측 | Cowork 접근 가능할 때 |
| B4 | 중·대형 루프 티어 준수 | 대화형 세션에서 medium(1→2→3→6→7→9)·large(전 단계) 실측 — 헤드리스는 interview가 성립 안 함 | 다음 실전 중형 과제 |
| B5 | 트리밍 이후 트리거 발화율 재측정 | trigger-eval 방법 재사용. 이번에 11개 description이 전부 짧아졌으므로 v0.3.0 eval의 6/6 결과는 더 이상 현재 상태의 측정치가 아니다. 충돌 쌍 유사 문구 negative 케이스와, `plan this`가 일반 계획 요청까지 잡는지(과발화) 포함 | 0.4.0 푸시 후 / description 변경 시 |
| B7 | 방법론 효능 | scorecard 10행 누적 후 결정-변경 비율 평가 | 실사용 누적 (A5 배선이 선행) |

## 해소되어 표에서 내린 항목

- **B6 `$ARGUMENTS` 빈 인자 동작** — 스킬 문면으로 해소. 인자가 없을 때의 동작을 각 스킬이 직접
  정의한다(blindspot·teach-me·interview·prototypes·brainstorm·plan·buy-in·loop). `notes`는
  리터럴 치환 사고를 피하려고 `$ARGUMENTS` 토큰을 아예 두지 않고 산문으로 모드를 묶었다.
  빈 문자열 치환이 무엇을 만들든 문면이 그 경우를 덮는다.
- **CI 최초 실행 확인** — `origin/main`에 성공한 CI 실행이 3건 있다(2026-07-11).
  `IMPLEMENTATION_NOTES.md`의 "push 후 첫 실행 확인 필요"는 이것으로 닫힌다.
  단 이 3건은 개정 전 워크플로의 실행이다 — 이번에 추가된 `windows-latest` 잡과 plugin-form
  검증 스텝은 아직 실행된 적이 없다(B2).
- **마켓플레이스 설치 경로(Method B) 실측** — 격리된 `HOME`에서
  `claude plugin marketplace add ajitta/know-your-unknowns`(HTTPS 클론) +
  `claude plugin install unknowns@ajitta` 성공, `claude plugin list --json`이 0.3.0 / user 스코프 /
  enabled로 보고. 캐시 416K, `.serena/`도 빌드 zip도 없음 — 로컬 `directory` 소스 캐시와 내용이
  다르다는 것까지 확인. 0.4.0 푸시 후 재실행 필요.
  (관련 주의: 작성자 `~/.claude`의 `ajitta` 마켓플레이스는 여전히 작업 트리를 가리키는 `directory`
  소스라, 일상 도그푸딩은 배포되는 트리가 아닌 것을 실행한다.)

## 처리 규칙

항목이 결정되면 B에서 A로 옮기고 반영된 파일을 함께 적는다. 삭제하지 않는다 —
"왜 이렇게 됐는지"가 나중에 가장 비싼 정보다.
결정은 `CHANGELOG.md` 또는 해당 문서에, 재검증 결과는 trigger-eval 후속 문서에 기록한다.
