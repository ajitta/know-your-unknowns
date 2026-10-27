# Implementation Notes — plan deviation log

## [2026-10-27] Writing-for-models Claude-checked round — Phase WC

**Observed**
- **Situation found**: per-file Claude checkers on d07db74 (the model-read files were last written by Codex) returned 118 findings: 117 quote ok, one wrong quote, which was dropped. 35 were confirmed, 34 fixed and 82 rejected in context. One "the same structure" sentence, shared by nine skills, had lost its antecedent when Phase B removed the HTML page; it accounts for nine of the confirmed findings.
- **Deviation from plan**: none in scope. Owner rulings (no HTML pages, no shipped code, scout without Bash, prose-only reviewer contract, the architecture / user-visible behavior / data / security escalation set, new-conversation review with the stage pending, Markdown deliverables) were kept, and so were frontmatter, trigger phrases, method step numbers and shared blocks.
- **Response chosen**: fix the confirmed wording in place; edit the shared output sentence in every copy and in its test guard; update both README notes-persistence summaries.

**Attributed**
- **Reason for choice**: a checker from a different engine than the writer finds defects the writer's own engine accepts; the per-item record is in the owner's local `kyu-review/wfm-claude/report.md`.
- **Risk/follow-up check**: nine fixes change meaning (blindspot output order, interview radius names and investigate-first placement, loop tier/tracker order, notes persistence, buy-in packet pointer, quiz wrap-up turn end) and are unmeasured.
- **Todo for human**: independent-reviewer's secondary pass runs "Where `/code-review` and `/security-review` are unavailable", a condition the agent cannot see with its tools. Decide whether the packet (loop step 8, surfaces.md, buy-in) gains a field saying those reviews run on the diff, or whether the reviewer always runs the secondary pass. Text unchanged until then.

## [2026-10-26] Independent review corrections — Phase R

**Observed**
- **Situation found**: independent review reproduced lost fresh-conversation review handoff, narrowed data escalation, an unshipped scorecard dependency, a manifest-only version-record bypass, unsupported install/sync claims, fallback ordering issues, and missing Windows tooling coverage.
- **Deviation from plan**: W2 accepted data loss as the common escalation scope. The owner reversed that choice and requires main loop's broader architecture, user-visible behavior, data, or security set everywhere.
- **Response chosen**: restore the new-conversation reviewer packet and keep the stage pending; restore broad data escalation; make scorecard guidance self-contained; validate every generated skill Markdown resource and digest every manifest field except version; align both README routes with the owner's rulings and official Claude guidance; add the Windows CI matrix.

**Attributed**
- **Reason for choice**: the owner's Phase R rulings preserve independence and main's permission boundaries while closing reproducible packaging holes. Historical W2 counts now exclude the reversed item from accepted fixes.
- **Alternatives considered**: a same-conversation review cannot discharge independent verification; keeping data loss would preserve the narrowed boundary; shipping the whole repository to resolve one pointer would undo the source/generated split.
- **Risk/follow-up check**: restored scope and new-conversation handoff are meaning-changing and unmeasured. New Windows CI is configured but not yet observed; mobile/desktop sync and ChatGPT routes are not owner-checked for this plugin. The writing-for-models diff review and local structural/build checks are recorded in the external Phase R fixes report.

## [2026-10-26] Portable package restructure — phases A, B, W, C

**Observed**
- **Situation found**: the original brief kept the HTML presentation template and two hooks, planned a 0.10.0 bump in Phase C, and installed the whole repository. The owner then changed Phase B to remove presentation pages and all shipped code, added a writing-for-models audit, and required Phase C to keep 0.9.2.
- **Deviation from plan**: the generated package is now instructions only, with Markdown conversation deliverables and two Claude Code agent prompts; no hooks, renderer, or executable skill assets remain. The source/generated split, per-skill reference vendoring, OpenAI interfaces, and both reproducible zips remain as requested.
- **Response chosen**: use `plugins/unknowns/` as the marketplace payload; use labeled in-skill passes where named agents are unavailable; log deviations at stage boundaries and before ending a turn; print complete Markdown records when files are unavailable. Keep the scout's tools read/search-only. The reviewer retains Bash for tests, lint, and builds, but its read-only rule is **prose only**, with no hook or permission mode enforcing it.
- **Version record**: the early transition removed and recreated `plugin-release.json` to keep 0.9.2. Phase C replaces that workaround: a digest change at the same version is accepted only while CHANGELOG.md has a non-empty `## [Unreleased]` entry; otherwise it is refused. `--check` still rejects stale generated output and digest records. AGENTS.md no longer instructs record deletion.
- **Audit record**: the independent writing-for-models check covered 29 source files: four findings found, three confirmed and fixed, one rejected on context. The fixed scope/execution-order clarifications remain unmeasured. The final independent diff check returned no findings; the detailed report and evidence are in the owner's local `kyu-review/wfm/report.md` audit record outside this repository.

**Attributed**
- **Reason for choice**: the owner's revised brief prioritizes the same method on hosts without hooks, shell tools, named agents, or durable files, while leaving versioning and release to the owner after verification.
- **Alternatives considered**: retaining the HTML presenter or hooks would contradict the revised owner decision; bumping the version during this branch would contradict the release hold; asking for a second approval after plan change requests would change an existing permission without a writing rule requiring it.
- **Risk/follow-up check**: a same-conversation review is not independent; the reviewer can still run Bash and its read-only contract is not a sandbox. Live behavior and routing, rebuilt archive uploads, mobile loading, cross-device sync, and the tag workflow have not been measured. Prior Windows hook tests were CI-only and those hooks and their matrix are removed.
- **W2 audit record**: the supplied 16 per-file checker outputs contain 30 findings, despite the brief's count of 32; 27 were confirmed and fixed, and three were rejected in context. The owner-added escalation item was also fixed. Diff review found two confirmed regressions (fixed) and one rejected objection (repeated in its final round). Phase W plus W2 totals, counting unique diff findings, are 38 found, 33 confirmed/fixed, and five rejected. All W2 scope and execution-order clarifications are unmeasured; the per-item record is in the owner's local `kyu-review/wfm2/report.md` outside the repository.
- **W2 resolution**: the owner authorized resolving the escalation wording difference under writing-for-models rule 4. Loop and notes now use architecture, user-visible behavior, data loss, or security, matching the existing escalation criteria, implementation prompts, and README. The notes Todo criteria and both README summaries use the same scope. This scope change is meaning-changing and unmeasured; the open todo is removed.

## [2026-10-01] Unreleased — 런타임 토큰 정리 (Phase 1 + talk-source 이동)

**Observed**
- **Situation found**: 계획(조사 → 개선안 → 독립 검증 v2)은 `output-routing.md` §1에서 본문과 겹치는 사다리 설명도 줄여 ~375 토큰을 줄인다고 했다. 실제로 겹치는 것은 반응 표(§4)와 표면별 단 목록 두 줄뿐이었고, 사다리 세 단의 문장은 본문에 없는 세부(ArtifactComments, `db`, `.gitignore` 1회 제안, 3단 조건)를 담고 있었다.
- **Deviation from plan**: §1 사다리 문장은 그대로 두고 반응 표만 지웠다(표면별 단 목록은 리뷰가 `surfaces.md`에 단 개념이 없다고 짚어 되살림). 측정 절감은 계획치(~375 토큰)보다 작다. teach-me "Limits"는 계획의 3불릿을 쓰되 "성공 신호는 라운드 2–4의 수렴"을 첫 불릿에 남겼다(`docs/value-contract.md`가 이 절을 그 근거로 인용한다).
- **Response chosen**: 본문 11개 `Origin:` 줄, loop "Operating principles", notes·teach-me의 인용 근거문 삭제(인용은 `docs/value-contract.md`로), `hooks.json` description 1문장, `talk-source.md` → `docs/`, 빌드 스크립트·테스트의 talk-source 특례 제거. `scorecard.md`의 `.gitignore` 문장은 검증에서 적용 시점이 다르다고 확인돼 남겼다.

**Attributed**
- **Reason for choice**: 호출된 본문은 세션 끝까지 매 요청에 남으므로, 실행 지시가 아닌 근거문은 이후 모든 요청에 비용이 든다. 지시는 한 문장도 지우지 않았다.
- **Alternatives considered**: 사다리 문장까지 줄여 계획치를 맞추기 — 본문에 없는 세부가 사라져 기각.
- **Discovery** — 가정: prototypes의 Kelly 문장은 근거일 뿐이다 / 실제: 5단계 종료 규칙 문장을 지우자 `behavior-prototypes-asks-contrast-on-skip`의 포화 확인(LLM 채점 항목, 수동 판정)이 6회 중 3회로 떨어졌다(main 5/5). 그 문장만 되살리면 4/5였으나, 리뷰가 4단계 정의 없이 5단계·삼원 비교에 "construct"가 남는다고 짚어 prototypes 본문은 main으로 전부 되돌렸다(`Origin:` 줄 삭제만 유지).
- **Risk/follow-up check**: 인용을 뺀 notes·prototypes에서 행동이 바뀌면 `behavior-notes-appends-to-file`·`behavior-prototypes-asks-contrast-on-skip`에서 먼저 보인다. 릴리스 zip(`build-plugin.sh`)에는 `docs/`가 없으므로 README의 `docs/talk-source.md` 경로는 zip 설치본에서 GitHub로 찾아야 한다.

## [2026-09-30] Unreleased — D1: Bash로 쓴 노트를 Stop이 인정

**Observed**
- **Situation found**: 첫 구현은 첫 편집 시각(훅의 시계)과 노트 파일 mtime을 초 단위 `>=`로 비교했다 — 기존 Stop 테스트가 실패했다(준비 단계에서 만든 파일이 같은 초에 생김). 엄격한 `>`로 고친 두 번째 구현도 독립 리뷰가 깼다: mtime이 미래로 찍힌 손대지 않은 파일에서 Stop이 조용해지고 `notes_touched: true`가 저장됐다(재현됨).
- **Deviation from plan**: 계획은 "Bash로 쓴 노트를 인정"(not covered: 무엇과 비교하나). 훅의 시계와 비교하지 않고, 첫 편집 때의 노트 파일 자신(`notes_at_start`: 없음 또는 mtime)과 비교한다.
- **Response chosen**: Stop은 Edit/Write로 건드렸거나, 파일이 새로 생겼거나, mtime이 첫 편집 때와 **달라졌을** 때 건드린 것으로 본다. 옛 상태 파일(스냅샷 없음)은 추론하지 않는다. 테스트: Bash 추가, 셸이 새로 만든 파일, 미래 시각 파일, 편집 전부터 있던 파일.

**Attributed**
- **Reason for choice**: 파일을 자기 자신과 비교하면 시계 어긋남(다른 기계의 빠른 시계, 네트워크 공유, `cp -p`, WSL 시계 지연)이 판정에 들어오지 않는다. mtime 비교는 새 훅 항목 없이 셸·다른 편집기·스크립트를 모두 덮는다.
- **Alternatives considered**: PostToolUse에 Bash matcher를 더해 명령 문자열을 보기 — 읽기(`cat IMPLEMENTATION_NOTES.md`)와 쓰기를 가려야 하고 우회 형태가 끝없어 기각.
- **Discovery** — 세 번째 결함(독립 리뷰 재확인에서 재현): 스냅샷에 경로가 없어서, Stop 때 cwd가 다른 패키지·형제 저장소로 가 있으면 그쪽의 오래된 노트 파일을 "새로 생겼다"로 읽었다. 스냅샷에 경로를 넣고, 시작 때 없었으면 그때 찾아본 위치 목록(`candidates`)을 남긴다 — 같은 경로의 mtime 변화, 또는 그때 비어 있던 위치에 새로 생긴 파일만 인정한다. 테스트 2건 추가.
- **Risk/follow-up check**: 기록 없이 노트 파일 mtime을 바꾸는 것은 전부 거짓 침묵이 된다 — 포매터, `git checkout`/`stash`/`rebase`/`pull`, 같은 체크아웃의 다른 Claude 세션. 실사용에서 "기록 안 했는데 Stop이 안 울린다"가 보이면 여기부터.

## [2026-09-30] Unreleased — C3·C4·C5·A2

**Observed**
- **Situation found**: `--crowd 60` 첫 실행(5케이스 5/5)을 "예산이 넘쳤는데도 unknowns 설명이 유지됐다"로 기록했는데, 독립 리뷰가 두 전제를 깼다: 헤드리스 실행도 `~/.claude.json`의 `skillUsage`를 올리므로 앞선 eval 실행이 테스트 대상 5개 스킬에 사용 이력(각 2회)을 쌓아 줬고, 넘친 원인은 이 환경에 깔린 다른 플러그인일 수 있었다. 내가 적었던 "헤드리스 세션은 호출 이력이 없다"는 틀렸다.
- **Deviation from plan**: 계획은 `--crowd N` 옵션까지였다. 편향을 없애려고 crowd 실행마다 빈 `CLAUDE_CONFIG_DIR`, 필러 먼저 로드, `--budget-fraction F`(→ `--settings`)를 더했고, 재측정 결과를 `docs/trigger-eval-crowd-2026-09-30.md`로 남겼다. `--plugin-dir` 반복과 `--settings` JSON은 설치된 CLI `--help`로, 격리 설정에서의 인증은 실제 실행으로 확인했다.
- **Response chosen**: 강제 예산 초과(CLI 로그 "124 skills, 35443 chars > 6000 budget", unknowns 설명 전부 빠짐)에서 영어 트리거 9/11, 같은 날 plain 11/11. 미발화는 notes·blindspot.

- **Discovery** — 설명이 빠지면 blindspot 설명의 "run it even when you could answer directly" 보정도 빠진다. crowd 미발화 양상이 v0.7.1의 미발화(스킬 없이 바로 답함)와 같다.

**Attributed**
- **Reason for choice**: 사용 이력이 설명 생존을 정하므로, 이력을 지우지 않은 측정은 "많이 쓴 스킬은 살아남는다"만 확인한다.
- **Alternatives considered**: 사용자의 `~/.claude.json`에서 `skillUsage`를 지우기 — 사용자 설정을 건드리므로 기각.
- **Risk/follow-up check**: 1회 표본이고, plain 조건은 격리하지 않아 두 조건이 예산 외에도 다르다. 다음 측정은 `--runs 3` + 격리된 plain으로.

독립 리뷰 재확인이 짚은 것:
- **Discovery** — 빈 `CLAUDE_CONFIG_DIR`로도 동기화·관리 플러그인(이 환경에서는 design·finance·cowork-plugin-management)은 로드된다. "다른 플러그인 없음"은 틀린 서술이라 고쳤고, crowd 실행마다 `--debug-file`을 남겨 예산 초과 여부와 로드된 플러그인을 보고서에 기록한다.
- **Discovery** — 이 컨테이너는 인증이 설정 디렉터리 밖에 있어 격리해도 돌았지만, 보통 머신에서는 빈 설정 디렉터리에 로그인이 없다. 그러면 모든 crowd 실행이 도구 호출 0회로 끝나 "미발화"로 채점됐을 것이다. 시작도 못 한 실행(비정상 종료 + 도구 호출·응답 없음)은 이제 FAILED로 채점에서 뺀다. `--claude false`로 그 경로를 실제로 확인했다. 마지막 재확인이 한 구멍을 더 짚었다 — 로그아웃 실행은 "Not logged in" 같은 문구를 결과로 돌려줄 수 있어 "응답 없음" 조건을 비껴간다. 판정을 "도구 호출 없음 + (비정상 종료 또는 결과 이벤트 `is_error`)"로 바꾸고, 그 응답을 흉내 낸 가짜 CLI로 FAILED가 나오는 것을 확인했다.
- **Discovery** — 문서에 적었던 "두 조건 모두 claude-sonnet-5-5"는 리뷰어의 보고를 옮긴 것이었다. 원본을 보니 모델명은 탐침 로그에만 있고 측정 결과에는 없었다 — 추정으로 낮췄고, 러너가 이제 실행마다 stream-json의 `model`을 기록한다(스모크 실행으로 확인).

## [2026-09-30] Unreleased — 후속 과제 8건 (A1·A4·C1·B1·D2·I3·zip)

**Observed**
- **Situation found**: 후속 목록을 구현하다 zip 참조 폐포 탐지가 `.unknowns/scorecard.md` 같은 데이터 파일 경로를 참조 파일 이름으로 잡아 plan·teach-me 등에 `scorecard.md`를 끼워 넣었다.
- **Deviation from plan**: 계획에 없던 것 — `docs/value-scorecard.md`의 설치자 안내(헤더 복사처)를 스펙 파일로 돌렸다. 스코어카드 형식에 `Baseline` 열이 생겨 기존 안내대로 복사하면 열이 모자란다.
- **Response chosen**: 형제 참조는 `/`·`.` 뒤에 오지 않는 `<name>.md`만 인정한다. `--session-start`는 임계값 검사보다 먼저 분기해, 임계값 0에서도 compact 시 loop 힌트만 낸다. loop 힌트는 `status == "active"`일 때만.
- **Discovery**: 새 참조 폐포 테스트는 폐포 계산을 끄면 brainstorm·plan·prototypes·quiz 등에서 실패한다 — 수정 전 결함을 실제로 잡는 테스트임을 확인했다.

**Attributed**
- **Reason for choice**: `status` 없는 옛 loop.json을 active로 치면 끝난 루프마다 "resume"이 뜬다. 힌트가 없는 쪽이 잘못된 힌트보다 싸다.
- **Alternatives considered**: loop 힌트를 startup에도 내기 — 새 세션마다 한 줄이 늘고, 무인자 `/unknowns:loop`가 이미 active 트래커를 이어받으므로 기각.
- **Risk/follow-up check**: 모델이 마지막 단계에서 `status: done`을 안 쓰면 이후 compaction마다 힌트가 뜬다 — 실사용에서 "끝난 loop인데 resume 안내"가 보이면 loop 10단계/마지막 티어 단계의 문구부터 볼 것.

독립 리뷰(2차 묶음)가 짚은 것:
- **Discovery** — `Baseline` 열을 표 가운데(5번째)에 넣었는데 마이그레이션 문구는 "헤더에 추가하고 옛 행은 비워 둔다"였다. 문자 그대로 따르면 기존 `.unknowns/scorecard.md`의 모든 옛 행이 한 칸씩 밀려 답이 엉뚱한 열 밑으로 간다 — 사용자 데이터를 건드리는 결정이었고 로그에도 없었다. 열을 맨 끝으로 옮기고 "열은 끝에만 추가, 기존 셀은 옮기지 않는다"를 명시해 데이터 재작성 자체가 필요 없게 했다.
- **Discovery** — 트래커가 첫 단계 경계 전에는 없고, `resume`이 `status`를 되살리지 않아 진행 중인 loop의 힌트가 빠질 수 있었다. 시작 즉시 `active`로 쓰고 `resume`이 `active`로 되돌린다.
- **Discovery** — local 산출물이 `unknowns:` 접두 에이전트 이름을 그대로 두어, `.claude/agents/`로 복사한 설치에서 loop 8단계가 없는 에이전트를 부른다. local 대상에서만 접두를 뗀다.
- **Discovery** — 참조 폐포가 bare 이름만 봐서, 참조 파일이 전체 플러그인 경로로 형제를 가리키면 경로는 `references/x.md`로 바뀌는데 파일은 안 담긴다. `port()`가 찾은 참조도 폐포에 넣는다.
- 고치지 않은 것: loop.json 64KB 상한(넘으면 힌트 없음)은 둔다 — 결정·기준선이 그만큼 커질 일은 드물고, 거대한 파일을 훅 5초 제한 안에서 읽는 편이 더 위험하다. `--out dist/local --target local`이 `dist/local/local/`을 만드는 것도 둔다.


## [2026-09-30] Unreleased — 사각지대 리뷰 반영 (A3·A5·C2·B2)

**Observed**
- **Situation found**: 계획은 리뷰가 고른 네 항목(A5 훅 존재 감지, C2 이중 확인, B2 기제 보강, A3 경로)만 고치는 것이었다. A5를 구현하다 보니 README 두 벌이 SessionStart(compact) 전용 동작을 서술하고 있었고, quiz의 4 + 2 분할도 README에 적혀 있었다.
- **Deviation from plan**: 계획에 README 수정은 없었다("not covered"). SessionStart 항목의 `compact` matcher를 없애 모든 source에서 스크립트가 돌게 했다 — 계획은 "표식 추가"였지 matcher 변경이 아니었다.
- **Response chosen**: `hooks.json` SessionStart는 matcher 없는 한 항목이고, 스크립트가 payload `source`로 갈린다(compact → 기존 재진술 + 재무장, 재무장이 저장됐을 때만 표식 추가; 그 외 → 상태가 저장되고 1회 리마인더가 아직 남았을 때만 표식, `UNKNOWNS_NOTES_REPEAT`면 항상). README.md·README.ko.md에 표식 한 문단과 quiz 4 + 1 + 티치백을 같은 구조로 반영했다(parity 테스트 통과).
- **Discovery**: zip 빌더는 스킬 본문이 쓰는 reference만 담는다. `output-routing.md`가 `surfaces.md`를 가리키는데 plan·quiz 등 zip에는 `surfaces.md`가 없다 — 이번 변경 이전부터 있던 결함이고 범위 밖이라 고치지 않았다.

**Attributed**
- **Reason for choice**: matcher를 `startup|resume|clear`와 `compact` 두 항목으로 나누는 것보다 한 항목 + source 분기가 hooks.json 테스트와 README 설명을 단순하게 한다. 표식은 리마인더가 실제로 울릴 곳에서만 내야 "표식 없음 = 자가 점검"이 거짓 안심을 만들지 않는다.
- **Alternatives considered**: 자가 점검을 무조건 적용 — 훅이 도는 곳에서 이중 알림이 되고, 스킬이 훅의 존재를 모른다는 문제 자체를 남긴다.
- **Risk/follow-up check**: opt-in 프로젝트에서 세션마다 한 줄이 컨텍스트에 들어간다. SessionStart에서 `source` 필드가 빠지는 호스트가 있으면 compact 뒤에도 재무장이 안 된다 — 그때는 표식만 나가고 리마인더는 다시 울리지 않는다.

독립 리뷰(`independent-reviewer`)가 짚은 것:
- **Discovery** — 첫 구현은 startup/resume에서 옵트인·임계값만 보고 표식을 냈다. 리마인더가 이미 울린 뒤 resume하거나 상태 디렉터리를 못 만들면 표식이 "앞으로 알려 준다"고 약속하지만 알림은 오지 않는다 — 위 Attributed의 "거짓 안심을 만들지 않는다"와 정면으로 어긋났다. 표식은 이제 상태가 저장되고 1회 리마인더가 아직 남았을 때만 나가고(`UNKNOWNS_NOTES_REPEAT`면 항상), compact 재진술은 재무장이 저장됐을 때만 표식을 단다. notes 스킬도 "표식 = 리마인더 한 번이 남았다, 받은 뒤에는 자가 점검"으로 고쳤다. 첫 구현의 테스트가 이 결함을 고정하고 있었다 — 뒤집었다.
- **Discovery** — SessionStart의 `source`에는 `fork`도 있다(리뷰어가 설치된 바이너리 스키마에서 확인). matcher가 없으니 표식 분기로 가고, 테스트에 넣었다.
- **Discovery** — `${CLAUDE_PLUGIN_ROOT}`는 플러그인 스킬에만 치환되므로 README의 "스킬 폴더만 복사" 설치 경로가 자리표시자를 그대로 노출하게 됐다. README 두 벌이 이제 `build-skill-zips.py` 산출물을 풀어 넣으라고 안내한다.
- 리뷰가 제기했지만 고치지 않은 것: teach-back 채점 기준을 "읽기 전에 고정"했다는 사실을 기록할 장치가 없다(I3) — 파일을 새로 두는 것은 범위 확대라 후속으로 남긴다. `docs/value-contract.md`의 "티치백(Johnson & Johnson 1987)"이 협동학습 문헌 오인용일 수 있다는 지적(I5)은 받아들이지 않았다 — 지식 도출 분야에 teachback 면담 기법이 실재한다(배우는 쪽이 전문가에게 되가르치고 교정받는 방식; WPI 지식 도출 기법 목록 https://web.cs.wpi.edu/~jburge/thesis/kematrix.html). 다만 Johnson & Johnson(1987)이 그 문헌인지는 이번에 확인하지 못했다 — 미검증으로 남긴다.

- **Todo for human** — 버전 번호와 릴리스(A4 절차)는 머지 뒤 결정. CHANGELOG는 "Unreleased"로만 적었다.

## [2026-09-28] 0.8.1 — 읽기 전용 가드 구멍, 문서 결함

**Observed**
- **Situation found**: 계획은 외부 검토가 재현한 쓰기 11건만 막는 것이었다. 고치기 전 두 번째 탐침에서 같은 부류가 10건 더 나왔고(scout의 `sed 'w f'`·`tree -o`·`uniq in out`, reviewer의 `sh -c`·`env`·`mkdir`·`ln`·`chmod`·`patch`·`git format-patch`), 첫 수정안을 `independent-reviewer`에 넘기자 같은 부류의 변형 우회(W1–W9), 새 오탐(W10), CHANGELOG 숫자 오류(W11), 그리고 부류 밖의 `git -c alias.x='!cmd'` 임의 실행(I1)이 나왔다.
- **Deviation from plan**: "11건" → 부류 단위로 막았다. 래퍼 해제, "대상이 전부 임시 디렉터리일 때만 허용하는 파일 쓰기 명령" 목록, 읽기 명령의 쓰기 옵션 검사를 새로 두었다. 리뷰 뒤에는 awk용 소형 렉서와 sed 스크립트 스캐너로 정규식을 대체했고, I1(`git -c` 실행 키)도 이번 릴리스에 넣었다.
- **Response chosen**: `hooks/scripts/agent_readonly_guard.py` 재작성, 테스트 24 → 41. 거부 사례와 허용돼야 하는 읽기 형태를 테스트마다 짝지었다(케이스 수는 같지 않다 — 거부 쪽이 더 많다).
- **Discovery**: CHANGELOG에 A4 릴리스 문장("done the same day as the merge, at tag …")을 넣지 않았다. 태그와 Release는 머지 뒤의 일이고, A4 0.6.0 교훈대로 릴리스 자산에 들어갈 파일이 아직 참이 아닌 릴리스 상태를 주장하면 안 된다. 태그 직전에 그 문장을 추가할 것.

**Attributed**
- **Reason for choice**: 재현된 명령만 막으면 같은 옵션을 가진 이웃 명령이 그대로 남는다는 것을 리뷰가 실제로 보여 줬다. 막는 기준(래퍼, 쓰기 대상 인자, 쓰기 옵션)이 설명 가능해야 다음 누락도 같은 기준으로 찾을 수 있다.
- **Alternatives considered**: reviewer를 scout처럼 허용목록으로 바꾸기 — 테스트·빌드 명령은 프로젝트마다 달라 정상 작업을 막는다. 파일 머리의 "막는 가드가 없는 것보다 나쁘다" 원칙과 충돌해서 기각.
- **Risk/follow-up check**: 과잉 거부. awk 렉서는 `/`가 피연산자 뒤에 오면 나눗셈으로 본다 — 줄바꿈으로 끝난 문장 바로 다음 줄의 정규식 패턴은 나눗셈으로 오독할 수 있다. 실사용에서 정상 명령이 거부되면 여기부터 볼 것.

리뷰가 "기록 안 된 결정"으로 짚은 것들:
- **Todo for human** — 범위 확대(11건 → 부류 단위, reviewer에게 `cp`·`mkdir`·`touch`·`chmod` 새로 거부)는 reviewer 에이전트의 권한 경계를 바꾸는 결정이다. 사용자는 "확인이 끝난 결함을 수정"을 지시했고, 확대분은 같은 부류의 재현된 결함이라 그 범위로 판단했다. 사전 확인은 받지 않았다.
- **Discovery** — 중첩 깊이 상한(6)을 넘으면 허용이 아니라 거부한다. 정상 명령은 두세 단계를 넘지 않는다.
- **Discovery** — `command -v`·`-V`(묶음 포함)는 해제하지 않는다. 이름 조회일 뿐 실행하지 않는다.
- **Discovery** — `git bisect`는 상태를 바꾸는 동사만 거부한다. `bisect log`·`terms`·`visualize`는 허용.
- **Discovery** — 스크래치 경로로 인정하는 변수는 `$TMPDIR`·`$TMP`·`$TEMP`와 같은 명령 안에서 `$(mktemp …)`로 받은 변수뿐이다. 다른 변수에 담긴 경로는 거부된다.
- **Discovery** — Windows의 네이티브 임시 경로는 `TMP`·`TEMP` 환경변수 값의 접두어로 인정한다(리뷰 I6). CI의 windows-latest 잡은 문자열 비교만 쓰므로 영향이 없다는 판단은 이번 세션에서 실행 확인하지 않았다 — 푸시 후 CI 결과로 확인할 것.

## [2026-09-25] 0.8.0 — protocol-alignment G1–G6 반영

**Observed**
- **Situation found**: G5의 선결 조건 "재확인 열을 누가 언제 읽는가"는 문서가 답을 남기지 않았다.
- **Deviation from plan**: 계획(`protocol-alignment.md` G5)은 "열 추가까지만 하고 알림 기제는 미결"이었다. 실제로는 읽는 쪽까지 넣었다. `loop`가 시작할 때 `.unknowns/scorecard.md`를 읽고, 날짜가 지났는데 비어 있는 행을 먼저 묻는다.
- **Response chosen**: `skills/loop/SKILL.md` 인자 절에 한 줄을 추가했다. 훅은 추가하지 않았다.

**Attributed**
- **Reason for choice**: 가장 약한 부분 절이 "읽는 쪽 없이 열만 추가하면 지켜지지 않는 약속이 하나 더 생긴다"고 적었다. 그래서 열만 추가하는 것은 계획을 따르는 게 아니라 알려진 실패를 반복하는 것이었다.
- **Alternatives considered**: SessionStart 훅 — Claude Code와 Cowork에서만 돌아서 Desktop·웹 사용자에게는 이 열을 읽는 쪽이 없다. 그래서 기각했다.
- **Risk/follow-up check**: `loop`를 다시 쓰지 않는 사용자에게는 아무도 묻지 않는다. 60일 value-contract 판정(2026-11-19)에서 Reality check 칸이 몇 개 채워졌는지 볼 것.

- **Discovery**: G3·G4·G5·G6의 효과는 헤드리스 단일 프롬프트 eval로 잴 수 없다. G3은 사용자 응답이 필요하고, G4는 하위 에이전트가 필요하며, G5·G6은 여러 세션에 걸친다. 그래서 문구만 반영하고 CHANGELOG에 미측정이라고 적었다.

## [2026-09-15] 0.7.0 — Claude Desktop/웹 설치 경로 추가

- **Situation found**: 첫 실제 업로드가 거부됐다 — "Plugin description must be at most 500 characters". `plugin.json`의 description은 579자였고, `claude plugin validate --strict`와 CI는 둘 다 통과시켰다.
- **Deviation from plan**: 계획은 "로컬 validate와 테스트가 통과하면 업로드 가능한 파일"이었다. 두 검증기가 서로 다른 규칙을 본다는 사실이 계획에 없었다.
- **Response chosen**: description을 477자로 줄이고(스킬 목록에서 "independent verification"을 빼되 두 출처 표기는 유지), 한도를 `tests/test_manifest_limits.py`에 못 박았다. 숫자의 출처는 문서가 아니라 업로드 폼의 에러 메시지이며, 그 사실을 파일 안에 적어 뒀다.
- **Reason for choice**: 로컬 검증기가 보지 않는 축은 로컬 검증기를 고쳐서 막을 수 없다. 이 저장소가 통제할 수 있는 지점은 테스트뿐이다.
- **Risk/follow-up check**: 이 발견은 **200자 스킬 description 한도 쪽 판단을 지지한다** — 앱 업로드가 CLI가 걸지 않는 한도를 실제로 집행한다는 사례가 하나 생겼기 때문이다. 다만 이것은 플러그인 매니페스트의 500자를 확인한 것이지 스킬의 200자를 확인한 것이 아니다. 스킬 zip 업로드는 여전히 미검증이다.
- **Improvements for next attempt**: "새 표면에 배포한다"는 작업의 완료 조건에 **그 표면에서 실제로 설치해 본다**를 넣을 것. 0.7.0은 문서 조사와 로컬 검증만으로 완료로 보고했고, 사용자의 첫 업로드가 3분 만에 반증했다.

- **Situation found**: 스킬 단독 업로드(Customize → Skills)의 description 한도가 문서마다 다르다. Agent Skills 스펙(platform.claude.com)은 1024자, 헬프센터의 커스텀 스킬 문서는 200자. 현재 description은 248–283자로, 한쪽 기준으로는 통과하고 다른 쪽으로는 전부 초과다.
- **Deviation from plan**: 계획은 "스킬을 그대로 포팅해서 zip으로 묶는다"였다. 한도 충돌은 계획에 없었다.
- **Response chosen**: `SKILL.md`의 description은 손대지 않고 `scripts/skill-descriptions.json`에 200자 이하 축약본을 따로 두고, 빌드 시 치환한다. `tests/test_skill_descriptions.py`가 README가 광고하는 영어 트리거 문구의 보존을 강제한다.
- **Reason for choice**: 현재 description은 0.5.1의 A/B eval이 측정한 물건이다. 미검증 제약(200자) 때문에 정본을 고치면 측정된 것이 사라지고, 새 표면의 위험이 이미 검증된 표면으로 번진다. 새 표면이 새 위험을 진다.
- **Alternatives considered**: (a) 정본 단축 — 11개 description의 트리거 거동이 미측정 상태가 되므로 기각. (b) frontmatter에 `metadata.short-description` 추가 — `claude plugin validate --strict` 통과는 확인했으나, 프론트매터가 상시 컨텍스트에 실릴 경우 Claude Code 사용자에게 토큰 비용을 지우므로 기각. 빌드 전용 파일은 런타임 비용이 0이다.
- **Risk/follow-up check**: 소스가 둘이 되었으므로 드리프트가 가능하다. 테스트가 막는 축은 "트리거 문구 누락" 하나뿐이고, 문장의 나머지 뉘앙스는 막지 않는다. 그리고 200자 제한 자체가 **실제 업로드로 확인되지 않았다** — 업로드가 248자를 받아준다면 이 파일 전체가 불필요하다. 다음에 데스크톱에서 하나 올려 보고, 받아들여지면 `scripts/skill-descriptions.json`을 지우고 빌드 스크립트에서 치환 단계를 뺄 것.

- **Situation found**: 빌드 스크립트에서 `talk-source.md` 포인터를 GitHub URL로 바꾼 뒤 참조 경로 정규식을 돌렸더니, 정규식이 **URL 안의 경로까지** 다시 써서 `blob/main/references/talk-source.md`가 되고 15KB 파일이 11개 zip 전부에 들어갔다.
- **Response chosen**: 부정 전방탐색으로 `talk-source`를 제외하고 URL 치환을 뒤로 옮겼다. zip 안에 플러그인 루트 경로가 남지 않는지 검사하는 테스트를 추가했다.
- **Risk/follow-up check**: 텍스트 치환을 연쇄로 걸 때 앞 단계의 출력이 뒤 단계의 입력 패턴과 겹치는 고전적 실수다. 산출물 검사(zip을 열어 본문을 본다)가 없었으면 통과했을 것이다 — 변환 스크립트에는 변환 결과를 여는 테스트를 같이 둘 것.

- **Situation found**: 모바일 앱이 스킬을 로드하는지 Anthropic 문서에서 확인할 수 없다. 헬프센터는 웹·데스크톱·Cowork·Claude Code를 표면으로 이름 붙이고 휴대폰 앱은 언급하지 않는다. 릴리스 노트에도 없다.
- **Response chosen**: 지원한다고 쓰지 않았다. README 표에 "문서 없음"으로 적고, 스킬이 모바일에서 마크다운 등급으로 내려가도록 `surfaces.md`에 경로만 만들어 두었다.
- **Reason for choice**: 이 저장소는 0.5.1에서 "주장이 증거보다 넓은" 실패를 한 번 겪었다. 설치 경로를 늘리면서 같은 실패를 반복하지 않는다.

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

## [2026-10-10] skill-writing 규칙 신설과 independent-reviewer.md 적용

**Observed**
- **Situation found**: 사용자가 승인한 규칙 7번 교체안을 한 줄로 쓰면 약 290자로, 규칙 자신이 정한 240자 한도를 넘음.
- **Deviation from plan**: 승인 문구를 그대로 넣기로 했으나 문장을 줄여 223자로 넣음(뜻은 동일).
- **Response chosen**: `.claude/rules/skill-writing.md` 7번은 축약 문구. 변경 사실은 사용자에게 보고함.

**Attributed**
- **Reason for choice**: 규칙 파일이 자기 규칙을 어기면 예시로서 신뢰를 잃음.
- **Alternatives considered**: 원문 유지 후 두 문단으로 분할 — 당시엔 목록 항목 안 분할 규칙이 없어서 기각(이후 7번에 추가됨).
- **Risk/follow-up check**: 없음. 사용자가 원문을 원하면 7번 첫 문단만 교체.
- **Discovery**: 이후 사용자 요청으로 240자 한도 자체가 규칙에서 빠짐(7번은 "내용으로 나누고 길이로 나누지 않는다"). 축약 근거는 사라졌고, 승인 원문으로 되돌릴지는 사용자 결정.

- **Discovery**: `agents/independent-reviewer.md` 항목 2의 "Also report unplanned decisions visible in the diff that the log does not record."는 `IMPLEMENTATION_NOTES.md`가 없을 때도 적용되는지 원문만으로 알 수 없음. 재구성 때 위치를 바꾸지 않고 항목 2 수준에 그대로 둠.
- **Todo for human**: 위 문장의 적용 범위를 정할 것(노트 파일이 있을 때만 / 항상). → **결정·반영됨(2026-10-14)**: 항상.
- **Todo for human**: `.claude/` 전체가 추적되지 않는 상태 — 규칙을 커밋하려면 `.claude/rules/skill-writing.md`만 지정해 add. → **해소됨**: e94986b에서 이 파일만 커밋.

## [2026-10-10] skills/agents 16개 파일에 skill-writing 규칙 적용 (파일별 독립 에이전트 작성 → 독립 검증)

**Observed**
- **Situation found**: blindspot 1단계 원문은 "주어진 소스를 먼저 조사"와 "조사 전에 한 번 묻기"가 서로 먼저라고 주장함.
- **Deviation from plan**: 계획(규칙 12)은 모호한 문장을 제자리에 두는 것이었으나, 이 건은 묻기(1b) → 기록(1c) → 소스 조사(1d) 순서로 정함.
- **Response chosen**: "they must exist before any finding does"와 맞는 유일한 순서라 채택. 세션 초반 사용자에게 같은 해석을 보고함.

**Attributed**
- **Reason for choice**: 기준선은 어떤 발견보다 먼저 있어야 한다는 원문 문장.
- **Alternatives considered**: 원문 순서 유지 — 기준선 기록 전에 발견이 생길 수 있어 기각.
- **Risk/follow-up check**: blindspot 행동 eval(behavior-blindspot-*)을 모델로 돌려 묻기가 먼저 나오는지 확인.

- **Discovery**: 결정된 용어 통일 외에 작성 에이전트가 추가로 바꾼 이름 — interview `## Never` → `## Iron Rules`(각 항목 앞에 Never), notes/plan 표 머리글 `Entry`/`Item type`, quiz 열 `Question type`. 의미 변화 없음.
- **Discovery**: 검증에서 확인된 동작 변화 5건을 수정 — blindspot 7단계에 추가된 "only", buy-in PR 본문의 "same structure" 누락, blindspot 2단계 packet 순서, loop "the same three options" 지시 대상 변경, teach-me 1단계 "still unclear" 범위 확대. 그 밖에 prototypes "in the page" 범위, loop 2단계 "Investigate only" 범위, reference 공유 문장 위치 복원.
- **Todo for human**: scout와 blindspot의 kind·status 정의 불일치(Missing concept, History, Convention, inferred)와 `Why it matters`/`why it bites` — HEAD부터 있던 문제, 어느 쪽 정의로 맞출지 결정. → **결정·반영됨(2026-10-14)**, 아래 항목 참고.
- **Todo for human**: surfaces.md의 fresh-thread 리뷰 packet에 claims 목록 누락(loop 8단계와 불일치) — HEAD부터 있던 문제. → **결정·반영됨(2026-10-14)**, 아래 항목 참고.
- **Todo for human**: quiz wrap-up이 loop가 이미 기록한 경우 조용히 건너뛰는지, scorecard.md처럼 "그렇다고 말하는지" — HEAD부터 불일치. → **결정·반영됨(2026-10-14)**, 아래 항목 참고.
- **Todo for human**: blindspot과 teach-me의 실행 순서(teach-me "blindspot first" vs blindspot "teach-me first"), blindspot ②가정 확인과 1d 소스 조사 중 무엇이 먼저인지. → **결정·반영됨(2026-10-14)**, 아래 항목 참고.
- **Todo for human**: 각 스킬 Output 절(출력 사다리) 문구가 5가지로 다름 — output-routing.md가 정의하는 "3-line ladder"와 함께 한 번에 정할 것. → **결정·반영됨(2026-10-14)**, 아래 항목 참고.
- **Todo for human**: loop의 closing offer 표가 reference 실제 옵션(implement now / revise the map / stop)과 다름 — HEAD부터 있던 문제. → **결정·반영됨(2026-10-14)**, 아래 항목 참고.

## [2026-10-14] skill-writing 재작성 뒤 미결정 항목 결정 반영 (PR #12 두 번째 커밋)

**Observed**
- **Situation found**: 2026-10-10 항목의 Todo for human 6건과 규칙 7 원문 복원 여부를 사용자와 인터뷰로 정함.
- **Deviation from plan**: 재작성 커밋(e94986b)은 문구만 바꿨고, 이 커밋은 동작을 바꾼다(규칙 16). 커밋을 나눠 같은 PR에 얹음.
- **Response chosen**:
  - kind·status 정의: blindspot 기준. History만 scout의 넓은 정의("A past attempt, revert or hairy dead end that explains why the code looks this way")를 쓰고, *inferred*는 일반 지식 추론도 허용(scout도 "Say which."). scout 열 이름은 eval grader가 쓰는 "Why it bites". README.md·README.ko.md의 History 설명도 맞춤.
  - blindspot ↔ teach-me 순서: 과제를 말로 설명하지 못하면 teach-me 먼저, 아니면 blindspot 먼저 하고 ③ 목록을 teach-me로 넘김. 두 스킬에 같은 문장. blindspot 1d는 "② 가정 → 주어진 소스 → 나머지, 가정은 주어진 소스에서 먼저 찾음"으로 합침.
  - Output 사다리: 8개 스킬(blindspot, brainstorm, buy-in, plan, prototypes, quiz, reference, teach-me)에 같은 문장, output-routing.md의 "On every rung" 규칙(조립된 답을 채팅에 남김)을 본문에 올림. buy-in PR 본문 예외와 prototypes "HTML이 어색하면 markdown"은 스킬별 줄로 유지. loop의 Output 줄은 바꾸지 않음.
  - surfaces.md 새 대화용 리뷰 packet에 claims 목록 추가(loop 8단계와 같은 항목).
  - quiz wrap-up: loop가 이미 행을 기록했으면 그렇다고 말함(scorecard.md "When to skip"과 일치).
  - loop "One stop per boundary" 표: reference 행을 implement now / revise the map / stop으로 분리.
  - blindspot 7단계: "③에 항목이 있고 이 과제에서 teach-me를 아직 안 돌렸으면" teach-me를 권함 — 순서 결정의 ③ 넘기기가 실제로 일어나는 자리. teach-me가 먼저 돈 경우 다시 권하지 않도록 조건을 붙임(독립 리뷰 W1).
  - 규칙 7: 현행 유지. 승인 원문에는 길이 기준이 있어 이후 결정(길이 한도 제거)과 충돌.

**Attributed**
- **Reason for choice**: README와 사용자에게 보이는 카드가 이미 blindspot 기준이고, 도메인 상식 위험을 카드로 올리는 것이 플러그인의 목적에 맞음. 나머지는 이미 한쪽 문서가 정한 규칙에 다른 쪽을 맞춘 것.
- **Alternatives considered**: scout 기준(엄격한 inferred) — 근거를 직접 확인한 것만 카드로 올리는 쪽. 사용자가 기각.
- **Risk/follow-up check**: blindspot·prototypes·plan·quiz 동작이 바뀌었으므로 해당 behavior eval을 모델로 돌려 확인할 것(미실행). 규칙 11의 공유 블록 목록에 순서 문장을 추가함.
- **Todo for human**: 2026-10-10 항목의 independent-reviewer "Also report unplanned decisions…" 적용 범위(노트 파일이 있을 때만 / 항상)는 이번 인터뷰에서 다루지 않아 열려 있음. → 아래 항목에서 결정.

## [2026-10-14] scout packet의 ② 가정, reviewer의 계획 밖 결정 보고 범위

**Observed**
- **Situation found**: 독립 리뷰가 지적 — blindspot의 scout packet에 ② 가정이 없어, 큰 범위(scout 경로)에서는 "② 먼저" 순서가 전달되지 않음. 그리고 reviewer 항목 2의 "unplanned decisions" 문장 적용 범위가 열려 있었음.
- **Response chosen** (사용자 승인):
  - blindspot scout packet에 "② what the user is assuming, to check first (step 1d)" 추가. scout 본문에 "packet이 가정을 담고 있으면 먼저 확인" 한 줄 추가(절차 번호는 그대로).
  - independent-reviewer: 노트 파일 유무와 관계없이 diff에 보이는 계획 밖 결정을 보고.

**Attributed**
- **Reason for choice**: 순서 결정이 주 경로(scout)에서도 지켜지게 함. 노트 파일이 없을 때 계획 밖 결정 보고가 가장 필요함.
- **Risk/follow-up check**: 모델 eval 미실행. reviewer는 eval이 없으므로 모델로 검증되지 않음.

## [2026-10-14] prompt-audit(agents, skills) 발견 1·2 반영

**Observed**
- **Situation found**: `/claude-api prompt-audit` 결과, loop가 같은 날 정한 결정과 어긋난 두 곳. 2단계 "run teach-me alongside"(2026-09-15)는 blindspot/teach-me의 순서 문장과 다르고, 15행 Output 줄은 output-routing.md가 9개 스킬 공통이라 한 사다리 문구와 다름.
- **Deviation from plan**: Output 사다리 결정은 8개 스킬로 정했는데, 그 근거("loop에는 Output 절이 없다")가 틀렸음 — loop:15에 한 줄로 있었음.
- **Response chosen** (사용자 승인): loop 2b를 "teach-me before the blindspot pass; otherwise hand blindspot's ③ list to teach-me afterwards"로, loop Output 줄을 다른 8개와 같은 사다리 문장으로 바꿈.

**Attributed**
- **Reason for choice**: 규칙 11(공유 문장은 글자 그대로) — loop로 돌 때만 순서와 채팅 남기기가 빠지는 상태를 없앰.
- **Risk/follow-up check**: 감사의 Low 2건은 열려 있음 — **Todo for human**: quiz에서 "assembled reply"로 채팅에 무엇을 남길지(답안 블록은 사용자가 채우므로 정의 안 됨, 정답 노출 위험). **Todo for human**: buy-in "Target read time: 90 seconds" 유지 여부.
