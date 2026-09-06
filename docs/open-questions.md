# 결정 기록과 미결 사항

작성: 2026-07-11(사각지대 26건 전환 직후) · 개정: 2026-09-07(리뷰 웨이브 결과 + 0.5.1·0.6.0 릴리스 위생 반영).

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
| A4 | 배포 zip 릴리스 정책 | **전제가 틀렸다.** `v0.3.0` 태그는 존재한 적이 없다(로컬·origin 모두 태그 0개) — "HEAD ≠ v0.3.0 태그"라는 보류 사유 자체가 성립하지 않았고, 0.3.0은 커밋 `622c32b`를 가리킨다. 그리고 CLI가 만드는 태그 이름은 `v0.4.0`이 아니라 **`unknowns--v0.4.0`**(`claude plugin tag`의 `{name}--v{version}` 형식)이다. 결정: 이 이름으로 태그를 만들고, 그 태그에서 만든 Release에 `unknowns-v0.4.0.plugin`을 첨부한다. `scripts/build-plugin.sh`가 깨끗한 트리 + 버전이 일치하는 태그를 강제하므로 태그 없이는 애초에 빌드되지 않는다. 스크립트의 기본 태그 이름은 이제 `plugin.json`의 `name`에서 `{name}--v{version}`으로 만들어지므로 인자 없이 `scripts/build-plugin.sh`만 돌리면 된다. **실행 완료**: 태그 `unknowns--v0.4.0`(커밋 `5c7bf04`) 푸시, Release 생성, `unknowns-v0.4.0.plugin`(88K, 43파일 — 페이로드만) 첨부. 저장소 루트에 남아 있던 `unknowns-v0.3.0.plugin`은 커밋되지 않은 트리에서 만든 것이라 릴리스 자산이 아니다 — 세션 스크래치패드로 치웠다. **0.5.x 소급 집행(2026-09-06)**: 이 정책은 두 릴리스 연속 지켜지지 않았다 — 0.5.0은 태그만 있고 Release 없음, 0.5.1은 태그도 Release도 없음. 0.5.1을 소급 집행했다: 주석 태그 `unknowns--v0.5.1`(커밋 `0a2adf4`) 푸시 + Release(Latest) + `unknowns-v0.5.1.plugin` (86,212 B, 42파일) 첨부. 0.4.0 자산 대비 빠진 파일은 `.claude-plugin/marketplace.json` 하나뿐이고 그것은 0.5.0이 의도한 제거다. **0.5.0에는 Release를 만들지 않기로 했다** — 27분 만에 0.5.1로 대체됐고, 존재하지 않는 설치 경로를 가리키는 `README.ko.md` 결함(0.5.1이 수정)을 담고 있어 내려받을 수 있는 자산으로 공개할 이유가 없다. 태그는 역사 포인터로 남긴다. **주의**: 카탈로그 소스가 git `url`(기본 브랜치 클론)이라 설치는 태그가 아니라 main HEAD를 따라간다. 태그는 배포 경로가 아니라 "그 버전이 무엇이었는가"의 유일한 불변 포인터다 — 그래서 건너뛰면 안 된다. **0.6.0(2026-09-07) — 소급이 아니라 제때 집행한 첫 사례**: 태그 `unknowns--v0.6.0`(커밋 `7103f4e`) 푸시 + Release(Latest) + `unknowns-v0.6.0.plugin`(90,447 B, 42파일) 첨부. 업로드된 자산의 sha256이 로컬 빌드와 일치함을 확인했다(`13e16922…0759d`). 순서를 하나 배웠다: **CHANGELOG를 먼저 고치고 태그를 만들어야 한다.** 0.6.0 커밋(`72d1f66`)의 CHANGELOG는 "릴리스 단계는 아직 안 됐다"고 적고 있었고, 그 파일은 페이로드에 그대로 들어간다 — 자기 자신을 반증하는 자산이 배포될 뻔했다. 태그가 아직 push되지 않은 상태였으므로 로컬 태그를 옮기는 비용은 0이었다(원격 이력 재작성 아님). 일반화: **릴리스 자산에 들어가는 파일이 릴리스 상태를 주장하면, 그 주장은 태그 이전에 참이 되어야 한다.** | `CHANGELOG.md` 0.4.0·0.5.1·0.6.0, [scripts/build-plugin.sh](../scripts/build-plugin.sh), [Release unknowns--v0.5.1](https://github.com/ajitta/know-your-unknowns/releases/tag/unknowns--v0.5.1), [Release unknowns--v0.6.0](https://github.com/ajitta/know-your-unknowns/releases/tag/unknowns--v0.6.0) |
| A5 | 스코어카드 기록 습관 | **제품 내 캡처 + 릴리스 시점 회고, 둘 다.** 사용 직후 loop 10단계·quiz 마무리에서 `AskUserQuestion` 한 번으로 한 행을 받아 `.unknowns/scorecard.md`에 적고, 릴리스 때 누적분을 한 번에 회고한다. 어느 한쪽만으로는 안 된다 — 즉시 캡처만 하면 추세를 아무도 안 보고, 회고만 하면 그때 가서 기억이 없다. 즉시 캡처는 v0.4.0에서 배선됐다 — loop 10단계와 quiz 마무리가 `AskUserQuestion` 2문항으로 물어보고 `.unknowns/scorecard.md`에 1행을 append한다. 둘 다 "아니오"인 행도 반드시 쓴다(계약 4·5번은 0건 기록으로만 발동). | [skills/loop/references/scorecard.md](../skills/loop/references/scorecard.md), [skills/loop/SKILL.md](../skills/loop/SKILL.md) 10단계, [skills/quiz/SKILL.md](../skills/quiz/SKILL.md) 마무리 |
| A6 | 에이전트 `memory` frontmatter 사용? | **v0.4.0에서는 두 에이전트 모두 끈다.** 필드 자체는 플러그인 에이전트에서 지원된다(미지원이라 못 쓰는 게 아니라 안 쓰기로 한 것). 켜면 메모리 파일을 관리하라고 `Read`/`Write`/`Edit`가 자동으로 활성화되는데, 이는 두 에이전트의 "저장소 파일을 절대 만들거나 고치지 않는다" 지시, README의 read-only 서술, 그리고 이번에 넣은 `PreToolUse` Bash 가드와 정면으로 충돌한다. 재검토 조건: `.claude/agent-memory/<agent>/`로 범위를 좁힌 PreToolUse 가드와 README 정정을 **함께** 준비할 때만 | `agents/*.md`(변경 없음이 결정 내용), `CHANGELOG.md` 0.4.0 |
| A7 | 플러그인 페이로드를 `plugins/unknowns/`로 이동? (PKGSPEC-8) | **0.4.0에서는 하지 않는다 — 실측 후 되돌림.** 실제로 옮겨 봤고, 그 즉시 실행 중이던 세션의 모든 Bash 호출이 깨졌다: 디렉터리 소스로 설치된 플러그인은 세션 시작 시점에 `${CLAUDE_PLUGIN_ROOT}`를 저장소 루트로 고정하므로, `hooks/`가 사라지면 `PreToolUse` 가드가 `[Errno 2] No such file` 로 exit 2 → 도구 호출 차단. GitHub 마켓플레이스 설치자는 `/plugin marketplace update` 후 새 `source`를 읽으므로 무사하지만, 개발용 디렉터리 설치는 마켓플레이스 재등록 전까지 깨진다. 편익 쪽은 이미 줄었다 — 이 이동의 주 목적이던 "plugin-form 검증 불가"는 CI에 `claude plugin validate .claude-plugin/plugin.json --strict`를 넣어 해결했고(PKGSPEC-1), 남은 편익은 설치 용량(docs·tests·evals·.github 약 500KB)과 로컬 strict 검증에서 뜨는 `CLAUDE.local.md` 경고뿐이다. 공개 저장소 push 직전에 30개 파일 변경 위에 25곳의 경로 변경을 얹을 값어치가 없다고 판단. **재개 조건**: 독립 릴리스로 분리하고, CHANGELOG에 "마켓플레이스 재등록 필요"를 명시하고, 격리 HOME 설치 테스트를 먼저 통과시킬 것 | 되돌림(변경 없음이 결정 내용), `IMPLEMENTATION_NOTES.md` 2026-09-06 |

## B. 재검증 대기

| # | 항목 | 방법 | 트리거 조건 |
|---|------|------|------------|
| B3 | Cowork 출력 분기 | Cowork에서 prototypes/plan 호출, A1 사다리의 어느 칸이 잡히는지 관측 | Cowork 접근 가능할 때 |
| B4 | 중·대형 루프 티어 준수 | 대화형 세션에서 medium(1→2→3→6→7→9)·large(전 단계) 실측 — 헤드리스는 interview가 성립 안 함 | 다음 실전 중형 과제 |
| B7 | 방법론 효능 | scorecard 10행 누적 후 결정-변경 비율 평가 | 실사용 누적 (A5 배선이 선행) |

## 해소되어 표에서 내린 항목

- **B6 `$ARGUMENTS` 빈 인자 동작** — 스킬 문면으로 해소. 인자가 없을 때의 동작을 각 스킬이 직접
  정의한다(blindspot·teach-me·interview·prototypes·brainstorm·plan·buy-in·loop). `notes`는
  리터럴 치환 사고를 피하려고 `$ARGUMENTS` 토큰을 아예 두지 않고 산문으로 모드를 묶었다.
  빈 문자열 치환이 무엇을 만들든 문면이 그 경우를 덮는다.
- **CI 최초 실행 확인** — `origin/main`에 성공한 CI 실행이 3건 있다(2026-07-11).
  `IMPLEMENTATION_NOTES.md`의 "push 후 첫 실행 확인 필요"는 이것으로 닫힌다.
  단 이 3건은 개정 전 워크플로의 실행이다. 이번에 추가된 `windows-latest` 잡과 plugin-form
  검증 스텝의 첫 실행은 아래 B2 항목에 기록했다.
- **B5 트리밍 이후 트리거 발화율 재측정 — 해소(기계 판정 범위에서).**
  2026-09-06에 0.5.1 description을 대상으로 30개 케이스 중 30건을 돌렸다:
  한국어 11건(stripped arm), 영어 11건, 네거티브 5건, 행동 3건.
  **타임아웃 0, 기계 판정 그레이더 23/23 통과, 영어 트리거 11/11 정발화.**
  충돌 쌍이 실제로 갈린다는 것도 확인됐다 — 맥락 없는 "loop"는 스킬을 띄우지 않고,
  UI 옵션 요청은 brainstorm이 아니라 prototypes로, "이 단어들을 모른다"는 blindspot이
  아니라 teach-me로 간다. 전체 표는 [trigger-eval-v0.5.1.md](trigger-eval-v0.5.1.md).
  **`teach me` 과발화는 재현되지 않았다** — 그 방향을 재는 케이스가 없어서
  `evals/neg-generic-howto-does-not-fire-teach-me`를 새로 만들어 돌렸고,
  답이 정해진 "teach me how to center a div"에서 스킬은 뜨지 않고 답이 바로 나왔다.
  **남는 것 두 가지**(B5로 되돌리지 않고 여기 적는다 — 트리거 발화율 질문 자체는 답이 나왔다):
  ① `llm` 루브릭 14건이 미채점이다. 경로 A(`claude plugin eval`)가 early access라
  판사 모델이 없고, 기계 판정은 "올바른 스킬이 떴는가"까지만 말한다.
  ② `plan`의 크기 게이트가 애매하다 — 한 파일짜리 변경에서 계획 문서는 쓰지 않았지만
  본문에 결정 카드·기각 대안·검증·롤백·가장 약한 부분을 인라인으로 재현했다.
  루브릭이 금지한 구성 요소이되 문면은 "문서"를 금지하므로 위반 여부가 갈린다.
  **스스로 채점하지 않고 판사 모델 대기로 남긴다.**

- **B1 scout 유효 도구에서 Grep/Glob 누락 — 해소. 결함이 아니었다.**
  2026-09-06 프로브에서 `unknowns-scout`가 **Grep과 Glob을 실제로 호출해 성공**했다.
  호스트가 그 두 도구를 실제로 가지고 있음을 먼저 증명하는 것이 관건이었고, 프로브는
  이렇게 구성했다: 부모 세션이 먼저 Grep/Glob을 직접 호출해 성공시키고(전제조건 충족을
  자기 보고가 아니라 호출로 증명), 그다음 scout를 스폰해 같은 두 호출을 시켰다.
  **Bash·WebFetch·WebSearch는 `--disallowedTools`로 막아** scout가 셸 `grep`으로 대체하거나
  기억으로 지어내지 못하게 했다.
  결과: scout가 반환한 `NOTES_NAME` 매치 7건(2파일, 줄번호 37·236·266·282·360·401 +
  `docs/open-questions.md:50`)과 `skills/*/SKILL.md` 11개 경로가 호스트 결과 및 저장소
  ground truth와 **정확히 일치**했다. Read만으로는 만들 수 없는 답이다.
  → `agents/*.md`의 `tools: Read, Grep, Glob, Bash, WebFetch, WebSearch`는 **정상 동작한다.**
  2026-07-11과 2026-09-05의 관측은 전부 **호스트 도구 풀과의 교집합 artifact**였다.
  **교집합 가설이 역으로 확증됐다**: 부모에서 Bash·WebFetch·WebSearch를 막자 scout의
  자기 보고 목록에서 정확히 그 셋이 사라졌다 — 선언 ∩ 호스트 풀이 유효 도구라는 규칙 그대로다.
  **방법 이탈**: 이 문서의 재프로브 조건 1은 "대화형 세션, 헤드리스 금지"였는데 헤드리스
  `claude -p`로 돌렸다. 조건 1은 조건 2("호스트가 Grep/Glob을 실제로 가질 것")의 대리
  지표였고, 헤드리스 세션이 그 두 도구를 실제로 가지고 있다는 것이 같은 실행 안에서
  직접 증명됐으므로 대리 지표가 필요 없어졌다. 조건 2와 3은 그대로 충족했다.
  **후속으로 하지 않은 것**: `hooks/scripts/agent_readonly_guard.py`의 scout 허용 목록에서
  `grep`/`rg`/`find`를 빼지 않는다. Grep/Glob이 있다고 Bash 검색이 해로워지는 것은 아니고,
  없애야 할 이유가 생긴 것이 아니다.
  근거 로그: 세션 스크래치패드 `b1-run.jsonl`(gitignore 밖, 세션 종료 시 소멸).

- **B2 Windows 훅 스크립트** — 해소. 0.4.0 푸시(`3e6a1aa`)의 CI 실행 `34008269747`에서
  `hook-tests (windows-latest)` 27초 성공. POSIX 전용 검사(퍼미션 비트 `0o700`/`0o600`,
  symlink 소유권 확인) 2건은 `skipUnless(hasattr(os, "getuid"))`로 건너뛰고 나머지는 전부 실행됐다.
  같은 실행에서 plugin-form 검증 스텝(`claude plugin validate .claude-plugin/plugin.json --strict`)도
  처음으로 돌아 통과했다. **남은 미검증**: 훅이 Windows에서 실제로 *발화*하는 경로(`python3`가
  기본 PATH에 없는 문제)는 여전히 실사용자 제보가 필요하다 — 이번에 증명된 것은 스크립트 단위 동작뿐이다.
- **마켓플레이스 설치 경로 실측** — 해소. 2026-09-06에 카탈로그 경유로 재실행했다:
  `/plugin marketplace add ajitta/claude-plugins` + `/plugin install unknowns@ajitta` →
  `unknowns@ajitta` **0.5.1 / local 스코프 / enabled**, 캐시
  `~/.claude/plugins/cache/ajitta/unknowns/0.5.1`. 캐시의 `skills/`는 작업 트리와 바이트 동일
  (`.DS_Store` 제외).
  **이전 판의 주의는 이제 무효다** — `~/.claude`의 `ajitta` 마켓플레이스는 0.5.0 이후
  `github: ajitta/claude-plugins`이고 더 이상 작업 트리를 가리키는 `directory` 소스가 아니다.
  즉 일상 도그푸딩은 이제 실제 배포본을 돌린다.
  **대신 생긴 것**: 캐시가 작업 트리를 가린다. 이 저장소의 `skills/`를 고쳐도 이 프로젝트 세션에는
  반영되지 않으며, 반영하려면 push → `/plugin marketplace update ajitta` → 재설치가 필요하다
  (카탈로그 소스가 git `url`이라 push하지 않은 편집은 어떤 경로로도 보이지 않는다).
  개발 중 즉시 반영이 필요하면 `directory` 스코프 설치를 따로 둬야 하고, 그때는 A7의
  `${CLAUDE_PLUGIN_ROOT}` 고정 함정이 다시 적용된다.

## 처리 규칙

항목이 결정되면 B에서 A로 옮기고 반영된 파일을 함께 적는다. 삭제하지 않는다 —
"왜 이렇게 됐는지"가 나중에 가장 비싼 정보다.
결정은 `CHANGELOG.md` 또는 해당 문서에, 재검증 결과는 trigger-eval 후속 문서에 기록한다.
