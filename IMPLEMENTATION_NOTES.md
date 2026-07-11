# Implementation Notes — plan deviation log

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
