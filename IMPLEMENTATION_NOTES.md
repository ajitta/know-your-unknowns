# Implementation Notes — plan deviation log

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
