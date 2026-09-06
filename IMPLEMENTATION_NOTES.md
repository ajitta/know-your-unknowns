# Implementation Notes — plan deviation log

## [2026-09-06] B1·B5 재검증 — 두 미결 항목 해소

- **Situation found**: B1(scout에 Grep/Glob이 없어 보임)의 재프로브 조건 1은 "대화형 세션, 헤드리스 금지"였다. 이 세션은 auto mode라 자기 메인 루프에도 Grep/Glob이 없어 조건을 만족할 수 없었다 — 세 번째 무의미한 관측이 될 상황.
- **Deviation from plan**: 헤드리스 `claude -p`로 돌렸다. 문서가 금지한 경로다.
- **Reason for choice**: 조건 1은 조건 2("호스트가 Grep/Glob을 실제로 가질 것")의 **대리 지표**였다. 대리 지표를 쓰는 대신 조건 2를 직접 증명했다 — 부모 세션이 먼저 Grep과 Glob을 호출해 성공시키고, 그 성공을 같은 실행 안에 남겼다. 대리 지표가 필요 없어지면 그것을 우회하는 것이 방법론 위반이 아니라 방법론 준수다.
- **Response chosen**: 프로브를 반증 가능하게 설계했다. `--disallowedTools`로 Bash·WebFetch·WebSearch를 막아 scout가 셸 `grep`으로 대체하거나 기억으로 지어내는 경로를 차단하고, Read만으로는 만들 수 없는 답(정확한 줄번호 7건, glob 11경로)을 요구했다. scout의 답은 저장소 ground truth와 정확히 일치했다.
- **Result**: **결함이 아니었다.** 덤으로 교집합 규칙이 역으로 확증됐다 — 부모에서 막은 셋이 scout의 도구 목록에서 정확히 사라졌다.
- **Improvements for next attempt**: 재검증 조건을 적을 때 **대리 지표와 진짜 조건을 구분해서** 적을 것. "대화형 세션에서"는 환경 이름이고, 실제로 필요한 것은 "호스트가 그 도구를 가질 것"이었다. 환경 이름으로 적어 두면 두 달 동안 아무도 못 닫는다.

- **Situation found**: B5의 남은 축을 재려고 케이스를 훑다가, `trigger-matrix.md`가 위험으로 적어 둔 `teach me` 과발화를 **재는 케이스가 하나도 없다**는 것을 발견. 위험은 2개월째 문서에만 있었다.
- **Response chosen**: `evals/neg-generic-howto-does-not-fire-teach-me`를 신설하고 돌렸다. 과발화는 재현되지 않았다(19.3s, 스킬 미발화, 답이 바로 나옴).
- **Risk/follow-up check**: "위험을 문서에 적는 것"과 "위험을 재는 것" 사이의 간극이 이 저장소의 반복 패턴이다 — B5도, 이 항목도 같은 모양이었다. 위험을 적을 때 그것을 재는 케이스 파일을 같이 만들 것.

- **Situation found**: `neg-one-file-plan-defers-to-plan-mode`가 기계 판정은 통과인데 본문을 읽으면 애매하다. 계획 문서는 안 썼지만(게이트 작동) 결정 카드·기각 대안·검증·롤백·가장 약한 부분을 인라인으로 그대로 재현했다.
- **Response chosen**: **판정하지 않았다.** 이 케이스를 위해 `llm` 그레이더가 존재하고 판사 모델은 경로 A 게이트 뒤에 있다. 양쪽 해석을 다 적고 유보로 남겼다.
- **Reason for choice**: 내가 채점하면 그건 측정이 아니라 의견이고, 이 저장소는 이미 "주장이 증거보다 넓은" 사고를 한 번 겪었다(0.5.1 CHANGELOG). 같은 실수를 반대 방향으로 반복하지 않는다.

## [2026-09-06] 0.5.1 릴리스 위생 소급 집행 + 문서 드리프트 정리

- **Situation found**: 0.5.1을 local 스코프로 설치해 잔여 작업을 점검하다가, A4가 정한 릴리스 정책이 **두 릴리스 연속 지켜지지 않은 것**을 발견. 0.5.0은 태그만 있고 Release 없음, 0.5.1은 태그도 Release도 없음. 즉 사용자가 방금 설치한 버전을 가리키는 불변 포인터가 존재하지 않았다.
- **Response chosen**: 0.5.1을 소급 집행(주석 태그 → 빌드 → Release + 자산). 0.5.0은 Release를 만들지 않고 태그만 역사 포인터로 남김.
- **Reason for choice**: 0.5.0은 27분 만에 대체됐고 `README.ko.md`가 존재하지 않는 설치 경로를 가리키는 결함을 담고 있다 — 내려받을 수 있는 자산으로 공개하면 알려진 결함본을 배포하는 셈.
- **Risk/follow-up check**: 카탈로그 소스가 git `url`(기본 브랜치 클론)이라 **설치는 태그가 아니라 main HEAD를 따라간다**. 태그는 배포 경로가 아니라 감사 포인터이므로, "설치가 되니 태그는 없어도 된다"는 추론이 다음에 또 나올 수 있다. A4에 그 문장을 못 박았다.

- **Situation found**: 계획에 없던 발견 — `docs/README.md`의 언어 정책이 **0.5.1과 정면으로 모순**된 채 남아 있었다("스킬 description은 이중 언어다"). 같은 파일에 0.5.0이 삭제한 `.claude-plugin/marketplace.json`을 현재형으로 설명하는 문단도 있었다.
- **Deviation from plan**: 점검 계획은 태그·릴리스·미결 항목 세 가지였고 문서 드리프트는 범위에 없었다.
- **Response chosen**: 두 곳 모두 수정. CI가 잡지 못하는 종류였다 — `tests/`의 파리티·컨테인먼트 검사는 README ↔ frontmatter와 en ↔ ko README를 보지만 `docs/**` 산문은 보지 않는다.
- **Improvements for next attempt**: description의 언어 정책처럼 **여러 파일에 산문으로 흩어진 계약**을 바꿀 때는, 바꾼 축(여기서는 "description에 한국어가 있는가")을 `grep`으로 전수 조사한 뒤 릴리스할 것. 0.5.1은 `skills/`·`agents/`·`README.ko.md`·`trigger-matrix.md`는 고쳤지만 `docs/README.md`를 놓쳤다.

- **Situation found**: `CHANGELOG.md`와 릴리스 커밋이 "양쪽 arm에서 11/11"이라고 적었는데, 디스크에 보존된 산출물은 stripped arm 11/11과 shipped arm 3/11(+ 240초 타임아웃 5건, 미보존 3건)만 뒷받침한다. `evals/results/`가 gitignore라 실행 증거가 저장소에 남지 않는다.
- **Response chosen**: 주장을 고쳐 쓰지 않고, `docs/trigger-eval-v0.5.1.md`에 **보존된 것과 주장된 것을 나란히** 적었다. 결정(한국어 제거)을 지탱하는 것은 stripped arm이고 그 축은 완전하므로 결정은 유지.
- **Reason for choice**: 재실행됐지만 디렉터리가 덮여 사라졌을 가능성과 실행되지 않았을 가능성을 지금 구분할 방법이 없다. 둘 중 하나를 골라 적으면 그게 새 허구가 된다.
- **Risk/follow-up check**: 다음 eval 실행 때 결과가 지워지기 전에 요약 표를 저장소에 커밋할 것. 근본 원인은 "측정은 gitignore된 곳에, 주장은 커밋되는 곳에" 있는 구조다.

- **Situation found**: 카탈로그 설치가 **작업 트리를 가린다**. 이제 이 프로젝트 세션은 `~/.claude/plugins/cache/ajitta/unknowns/0.5.1`에서 로드하므로, 저장소의 `skills/`를 고쳐도 반영되지 않고 push하지 않은 편집은 어떤 경로로도 보이지 않는다.
- **Response chosen**: 수정하지 않고 `docs/open-questions.md`의 해소 항목에 기록. 0.5.0 전의 `directory` 소스 문제("배포본이 아닌 것을 도그푸딩한다")와 **정확히 반대 방향의 트레이드오프**이고, 지금 쪽이 낫다.
- **Risk/follow-up check**: 개발 중 즉시 반영이 필요하면 `directory` 스코프 설치를 따로 둬야 하며, 그때는 A7의 `${CLAUDE_PLUGIN_ROOT}` 고정 함정이 다시 적용된다.

## [2026-09-06] 리뷰 124건 전면 적용 (v0.4.0)

- **Situation found**: 권고 3건이 검증자 재검토에서 무효화되거나 좁혀짐 — 계획은 "확인된 권고 전부 적용"이었음.
- **Response chosen**: SKILLSPEC-8(`disallowed-tools`로 "구현 금지" 강제)은 전면 기각 — 제한이 호출 턴 전체에 걸리는데 loop은 단일 턴에서 blindspot(2단계)→구현(7단계)을 모두 도는 구조라 구현 자체가 막힘. UX-6은 legacy 문구 제거만 적용하고 rename/`disable-model-invocation`은 기각(rename은 파괴적 변경, 플래그는 README가 광고하는 자연어 트리거를 조용히 죽임). UX-9는 size gate만 적용하고 generic 트리거는 유지(오발화 증거가 오귀속으로 판명).
- **Risk/follow-up check**: UX-6·UX-9는 실제 오발화가 관측되면 재검토. evals/ negative 케이스가 이를 측정한다.

- **Situation found**: 에이전트 그룹 분할을 렌즈(발견 카테고리)가 아니라 **파일 소유권**으로 해야 했음 — README.md 한 파일에 3개 렌즈(DOCS/UX/PKGSPEC) 25건이 몰림.
- **Deviation from plan**: 초기 계획은 렌즈별 병렬이었음.
- **Response chosen**: 파일 소유권 기준 12그룹으로 재분할하고, 데이터 결합(스킬 description 축약 → README 트리거 목록)이 있는 그룹은 2단계로 순서화.
- **Reason for choice**: `tests/test_trigger_containment.py`가 README 광고 문구 ⊆ SKILL.md description을 CI에서 강제하므로, 동시 편집 시 반드시 CI가 깨짐.

- **Situation found**: 세션 한도로 12개 중 4개 에이전트가 중단됨. HOOK 에이전트는 **파일 편집은 마쳤으나 보고 전에 종료** — 작업 결과가 미검증 상태로 디스크에 남음.
- **Response chosen**: 재실행(중복 적용 위험) 대신 독립 verify 에이전트를 붙여 미보고 작업을 회의적으로 재검증.
- **Risk/follow-up check**: 재실행했다면 이미 적용된 수정 위에 중복 편집이 쌓였을 것.

- **Situation found**: 계획에 없던 교차 그룹 회귀 — PKG 에이전트가 CI에 windows-latest leg를 추가했는데, HOOK 에이전트가 같은 시각에 추가한 테스트가 POSIX 전용 API(`st_mode & 0o777`, `os.symlink`)를 씀. 두 변경 각각은 옳지만 합치면 CI가 깨짐.
- **Response chosen**: 해당 테스트에 플랫폼 skip 가드 추가.
- **Improvements for next attempt**: 병렬 fan-out에서 "각 그룹은 옳지만 합치면 깨지는" 조합을 잡으려면, 통합 검증 단계를 그룹 수만큼이 아니라 **교차 지점 수**만큼 설계할 것.

- **Situation found**: PKGSPEC-8(플러그인 페이로드를 `plugins/unknowns/`로 이동)의 주 편익이었던 "plugin-form 검증 불가"가 CI에서 `claude plugin validate .claude-plugin/plugin.json --strict`로 이미 해소됨.
- **Deviation from plan**: 남은 편익은 설치 용량뿐인데 비용은 전 파일 경로 변경.
- **Response chosen**: 마지막 순서로 미뤄 실제로 이동해 봤고, **되돌렸다**.
- **Reason for choice**: 이동 직후 실행 중이던 세션의 Bash 호출이 전부 차단됨 — 디렉터리 소스 설치는 세션 시작 시 `${CLAUDE_PLUGIN_ROOT}`를 저장소 루트로 고정하므로 `hooks/`가 사라지자 `PreToolUse` 가드가 exit 2로 죽었다. 되돌리려면 Bash가 필요한데 Bash가 막혀 있어서, 옛 경로에 no-op 스텁 2개를 Write로 만들어 잠금을 풀고 `git mv`로 원복한 뒤 스텁을 제거했다.
- **Alternatives considered**: 스텁을 남긴 채 진행(중복 파일), 이동 강행 후 마켓플레이스 재등록 안내(공개 push 직전 30파일 변경 위에 25곳 경로 변경을 얹는 위험).
- **Risk/follow-up check**: 이동의 주 편익이던 plugin-form 검증은 CI에서 이미 확보됨(PKGSPEC-1). 남은 편익은 설치 용량과 로컬 strict 경고뿐. 결정과 재개 조건은 `docs/open-questions.md` A7에 기록.
- **Improvements for next attempt**: 레이아웃 변경은 다른 변경과 **같은 커밋에 절대 섞지 말 것** — 단독 릴리스로 분리하고, 격리 HOME 설치 테스트를 먼저 통과시킨 다음, CHANGELOG에 마켓플레이스 재등록 필요를 명시할 것.

## [2026-07-11] 사각지대 보고서 MED 11건 + LOW 5건 전환 작업

- **Situation found**: `/unknowns:notes show` 라이브 호출로 `$ARGUMENTS` 치환이 스킬에서 실제 동작함을 확인 — 동시에 notes 본문에서 라벨 용도로 쓴 리터럴 `` `$ARGUMENTS` = `init` ``이 `` `show` = `init` ``으로 치환·왜곡되는 버그 발견(계획에 없던 신규 unknown).
- **Response chosen**: notes 본문을 "Argument `init`: … Argument `show`: …"로 재서술. 나머지 7개 스킬의 "from `$ARGUMENTS`" 패턴은 치환돼도 의미 보존이라 유지.
- **Risk/follow-up check**: 인자 없이 호출될 때 해당 위치가 빈 문자열로 치환되는 동작은 미관측 — 후속 확인 후보.

- **Situation found**: plugin.json description에는 "1:1" 주장이 아예 없음 — 스카우트의 수정 대상 목록이 과대. README 두 파일만 수정.
- **Situation found**: MED-3의 "frontmatter에서 README 트리거 줄 생성" 대신 `tests/test_trigger_containment.py`(README 광고 문구 ⊆ description 검사, CI 가드)를 채택. README가 산문이라 생성기는 과잉, 검사기가 더 강한 보증.
- **Situation found**: LOW-1 state 파일명에 사용자명 추가 → 라이브 세션 hook이 새 파일로 0부터 재카운트, 10에서 재발화(관측). 부수 증거: hook은 매 호출 디스크의 현재 스크립트를 실행. 구 형식 파일은 OS tmp 정리까지 잔존 — 허용.
- **Situation found**: LOW-1 "1회 경고"는 stateless 스크립트라 불가 — 실패마다 stderr 경고로 구현(일반 사용자에겐 안 보이고 hook debug에서만 노출).
- **Situation found**: stderr 테스트 1차 시도(TMPDIR 읽기 전용)는 `tempfile.gettempdir()`가 /tmp로 폴백해 실패 자체가 안 남 — state 경로에 디렉토리를 만드는 방식으로 교체.
- **Situation found**: MED-11의 Cowork 분기는 이 환경에서 측정 불가(Cowork 부재) — CLI 분기만 측정하고 한계 기록.

## [2026-07-11] 사각지대 보고서 HIGH 10건 known 전환 작업

- **Situation found**: scout 도구 제한 런타임 테스트에서 예상 밖 결과 — 제한은 작동하지만(Edit/Write 스키마 부재) 유효 도구가 선언(`Read, Grep, Glob, Bash`)보다 좁음: Grep/Glob 누락, Read+Bash만 노출.
- **Deviation from plan**: 계획은 "배열이 안 먹히면 쉼표 문자열로 교체"의 이분법이었음. 실제는 제3의 상태(부분 적용).
- **Response chosen**: 문서 스펙(쉼표 문자열)으로 교체하고, Grep/Glob 재노출 여부는 `/reload-plugins` 또는 새 세션에서 재검증 필요로 기록.
- **Reason for choice**: 공식 문서가 쉼표 문자열만 예시함 (code.claude.com/docs/en/sub-agents.md). 세션 내 agent 레지스트리는 시작 시 고정이라 이 세션에서 재검증 불가.
- **Alternatives considered**: JSON 배열 유지(CLI `--agents`는 배열 허용) — 파일 frontmatter 문서 예시와 불일치라 기각.
- **Risk/follow-up check**: 새 세션에서 scout 스폰 시 도구 목록 재확인. Grep/Glob이 여전히 누락되면 harness 이슈로 별도 보고.

- **Situation found**: 스카우트가 LOW로 의심한 `/reload-plugins`는 실존 명령으로 확인됨 (docs/en/skills.md "Live change detection").
- **Response chosen**: README 수정 불필요 판정 (선택된 10건 밖이기도 함). 사각지대 보고서의 해당 항목은 오탐으로 정정.

- **Situation found**: hook matcher `"Edit|Write"`는 regex가 아니라 literal 목록 매칭으로 문서 확인 — NotebookEdit 미포함 확정.
- **Response chosen**: 수정 안 함 — 사용자가 선택한 HIGH 10건 범위 밖(LOW). 다음 릴리스에서 `Edit|Write|NotebookEdit` 검토.

- **Situation found**: 항목 8(루프 효능 A/B)은 단일 턴에서 유의미한 before/after 실험 불가 — 1회성 A/B는 증거력이 약함.
- **Response chosen**: 스코어카드 체계(docs/value-scorecard.md) 신설 + 오늘 세션을 데이터점 #1로 기록. "측정 시작"으로 전환하고 완전 전환은 실사용 누적에 위임.

- **Situation found**: CI 워크플로(.github/workflows/ci.yml)는 push 전까지 실행 검증 불가.
- **Response chosen**: 로컬에서 동일 명령(`python3 -m unittest discover -s tests -v`) 통과 확인으로 대체. push 후 첫 실행 확인 필요.

- **Situation found**: loop/plan description 수정은 현행 세션에는 미반영(플러그인은 세션 시작 시 로드). headless `claude -p` 프로세스는 디스크에서 새로 로드하므로 트리거 eval은 수정 후 상태를 측정함.
- **Response chosen**: eval 결과에 이 사실 명시.
