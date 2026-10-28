# docs/ 색인

이 디렉터리는 **유지보수 기록**이다 — 조사·검증·측정·미결정 사항을 남긴 곳이지,
사용법 문서가 아니다. 설치와 사용법은 저장소 루트의
[README.md](../README.md)(English) / [README.ko.md](../README.ko.md)(한국어)에 있다.

이 색인이 필요한 이유: 여기 파일 중 둘은 100 KB짜리 생성 HTML이고, 어떤 실행이
언제 무엇을 근거로 만들었는지 파일 안에서만 알 수 있었다. 마크다운 어디에서도
링크되지 않아 사실상 발견 불가능한 상태였다.

## 언어 정책

0.3.0 릴리스 노트는 "docs/research-know-your-unknowns.md만 의도적으로 한국어"라고 적었지만,
그 뒤로 한국어 문서가 다섯 개, 한국어 이탈 로그가 하나 더 생겼다. 실제 정책은 이렇다.

| 범위 | 언어 | 이유 |
|------|------|------|
| `skills/`, `claude-code/agents/`, `packaging/`, `.claude-plugin/`, `NOTICE`, `LICENSE` | 영어 | 모델이 읽는 지시문이고, 설치자가 누구든 읽어야 한다 |
| `README.md`, `CHANGELOG.md`, `tests/`, `evals/` | 영어 | 설치자·기여자 대상 |
| `README.ko.md` | 한국어 | README.md의 한국어 쌍둥이 |
| `docs/**`, `IMPLEMENTATION_NOTES.md` | 한국어 | 작성자 자신의 작업 기록. 번역 대상이 아니다 |

두 가지 예외가 정책의 일부다.

- **스킬 description은 0.5.1부터 영어 전용이다.** 그전까지는 영어 트리거 문구 옆에 한국어
  문구를 함께 실었다. 한국어로 말해도 스킬은 그대로 뜬다 — 다만 보증 방식이 "description에
  써 두는 것"에서 "eval로 재는 것"으로 옮겨졌다(`evals/trigger-ko-*` 11건 + `tests/`의 회귀 가드).
  근거는 [trigger-eval-v0.5.1.md](trigger-eval-v0.5.1.md), 문구 목록은
  [trigger-matrix.md](trigger-matrix.md)와 [README.ko.md](../README.ko.md).
- **런타임 산출물은 사용자의 언어를 따른다.** 카드·질문·프롬프트 초안 같은 사용자 대면 문장은
  사용자가 쓰고 있는 언어로 쓴다(파일명·템플릿 키·코드 식별자는 고정).
  근거: [`skills/loop/references/output-routing.md`](../skills/loop/references/output-routing.md) §3.

## 파일 색인

| 파일 | 무엇 | 언어 | 무엇이 만들었나 | 갱신·재생성 |
|------|------|------|----------------|------------|
| [README.md](README.md) | 이 색인 | 한국어 | 수기 | docs/에 파일이 늘거나 줄 때 |
| [handoff.md](handoff.md) | 0.12.2 이후 다음 라운드 인계: 상태, 소유자 대기(O1), 소유자 판단, 남은 작업, 규칙 | 한국어 | 수기 | 라운드를 시작·마칠 때 상태 절을 git·태그와 대조해 갱신 |
| [open-questions.md](open-questions.md) | 결정 기록(A)과 재검증 대기(B). 왜 그렇게 결정했는지가 본문 | 한국어 | 수기 | 결정이 날 때마다. 항목은 B→A로 옮기고 삭제하지 않는다 |
| [features/agent-collision/](features/agent-collision/README.md) | 0.9.2 두 에이전트(independent-reviewer·unknowns-scout) 가로챔 수정의 라우팅 측정: 소유자 설치 조합(dia·design·SuperClaude)에서 main 대비 리뷰 7셀·scout 9셀 × 10회(Opus), 첫 scout 배치(Sonnet) 기록, 단발 스크린, 하네스 포함 | 한국어 | 수기 + `harness/tally.py` 출력 | 에이전트 description이나 다른 플러그인 조합이 바뀔 때 재측정 |
| [features/html-page-template/](features/html-page-template/README.md) | 0.9.0 페이지 템플릿(`render-page.py`)의 출력 토큰 측정: main 대비 3케이스 × 6회, 하네스 포함 | 한국어 | 수기 + `harness/analyze.py` 출력 | 페이지 템플릿이나 output-routing.md §3–§4를 바꿀 때 재측정 |
| [trigger-matrix.md](trigger-matrix.md) | 11개 스킬의 트리거 문구 전수 + 충돌 쌍과 해소 상태 | 한국어 | 반자동 — 문서 안의 추출 스크립트 출력으로 표를 수기 갱신 | 문서 "갱신 방법" 절의 `python3` 블록을 저장소 루트에서 실행 |
| [trigger-eval-v0.3.0.md](trigger-eval-v0.3.0.md) | v0.3.0 시점 자동 발화율·루프 준수 실측 기록 | 한국어 | headless `claude -p` 실행 6건의 transcript에서 추출 | **동결** — 특정 시점 측정 기록. 재측정은 새 날짜의 새 파일로 — 첫 후속은 trigger-eval-v0.5.1.md |
| [trigger-eval-v0.5.1.md](trigger-eval-v0.5.1.md) | 0.5.1이 description에서 한국어를 뺀 뒤의 트리거 측정. 한국어 축 11/11, 나머지 축은 미측정임을 명시 | 한국어 | `evals/run-manual.py` 실행의 `manual-result.json`에서 추출 | **동결** — 단 `evals/results/`가 gitignore되므로, 다음 실행 때는 결과가 지워지기 전에 새 날짜의 새 파일을 만들 것 |
| [trigger-eval-v0.7.1-opus-5-5.md](trigger-eval-v0.7.1-opus-5-5.md) | Claude Opus 5.5 첫 측정 — 31케이스 기계 채점, blindspot 발화 3/8 → 6/6 수정 | 한국어 | `evals/run-manual.py` (`ANTHROPIC_MODEL=claude-opus-5-5`) 실행의 `manual-result.json`에서 추출 | **동결** |
| [trigger-eval-crowd-2026-09-30.md](trigger-eval-crowd-2026-09-30.md) | 스킬 목록 예산 초과(설명 없이 이름만) 조건의 첫 트리거 측정 — 영어 11건 중 9건 발화, notes·blindspot 미발화 | 한국어 | `evals/run-manual.py --crowd 60 --budget-fraction 0.002` 실행의 `manual-result.json`과 CLI 디버그 로그에서 추출 | **동결** |
| [research-know-your-unknowns.md](research-know-your-unknowns.md) | 원문 "Know your unknowns" 페이지 조사·대조 분석. 【검증】/【단일】/【추정】 확실성 표기 | 한국어 | 수기 — 원문 다회 페치 + 플러그인 소스 대조 | 원문을 다시 페치했을 때. 재확인 날짜를 헤더 표에 한 줄 추가 |
| [talk-source.md](talk-source.md) | 원문 강연·"Know your unknowns" 11개 예시와 플러그인 구성 요소의 대응, 예시별 원문 프롬프트와 출처, 강연에서 직접 검증한 기법 | **영어** (예외 — 0.8.1까지 `skills/loop/references/`에 있던 파일을 그대로 옮김) | 수기 — 원문 페치 + 강연 대조 | 원문을 다시 대조했을 때. 스킬 본문은 이 파일을 참조하지 않는다(런타임 미로드) |
| [protocol-alignment.md](protocol-alignment.md) | 인간-AI 협업 프로토콜(볼트 노트 3편) 대조에서 나온 격차 G1~G7 + 구조 항목 S1, 결정 표와 다음 세션용 프롬프트 | 한국어 | 수기 — 프로토콜 대조 + `unknowns:interview` 4문항 | 항목을 반영할 때마다 해당 절에 집행 기록. 전부 반영되면 open-questions.md A절로 요약 이관 |
| [value-contract.md](value-contract.md) | 이 플러그인 자신에 대한 가치 계약 — 지표, 강등·제거 조건, 측정 시계 | 한국어 | 수기 | 수치를 고칠 때(잠정값), 그리고 측정 시계 확인 때마다 표에 한 행 |
| [value-scorecard.md](value-scorecard.md) | 실사용 1회 = 1행 기록. value-contract의 지표 원장 | 한국어 | 수기 | 실사용마다. 설치자는 자기 저장소의 `.unknowns/scorecard.md`에 따로 기록 |
| [intent-report-v0.2.0.html](intent-report-v0.2.0.html) | v0.2.0 의도 부합성 검증 리포트 (97,836 바이트) | 한국어 | 검증 워크플로 산출물 — `wf_1d569a3d`, `wf_ecf82b01`. 이 저장소 커밋을 인용하지 않는다(본문의 16진수 id는 git 객체가 아님) | **동결** — 재생성하지 않는다 |
| [intent-report-v0.3.0.html](intent-report-v0.3.0.html) | v0.3.0 의도 부합성 검증 리포트 (102,976 바이트). 17개 대상 · 반박 검증 | 한국어 | 검증 워크플로 산출물 — `wf_83310eb9`. 커밋 `f1f2930`·`c51a0fc` 대상 | **동결** — 재생성하지 않는다 |

## 두 HTML 리포트에 대한 결정

**결정: 저장소에 그대로 둔다. 설치 페이로드와 릴리스 zip에는 넣지 않는다. 대신 이 색인에서 링크한다.**

배경. 두 파일은 합쳐 약 200 KB다. 0.10.0 전에는 마켓플레이스 설치가 저장소 전체를 플러그인
캐시로 복사했으므로 이 리포트들도 설치본에 따라 들어갔다(0.9.2 설치본 2.0 MB). 0.10.0부터
설치되는 플러그인은 생성물 `plugins/unknowns/`뿐이다(49파일, 약 157 KB). 자체 마켓플레이스
`.claude-plugin/marketplace.json`은 `./plugins/unknowns`를, 카탈로그
[ajitta/claude-plugins](https://github.com/ajitta/claude-plugins)는 `git-subdir`
`plugins/unknowns`를 가리킨다. 두 릴리스 zip(`releases/know-your-unknowns.zip`,
`releases/know-your-unknowns-openai.zip`)도 같은 생성물에서 만든다. 그래서 `docs/`는 어느
설치 경로의 플러그인에도 들어가지 않는다.

왜 두는가.

- 이 리포트들은 CHANGELOG 0.2.0·0.3.0 항목이 근거로 삼는 **검증 증거**다. 저장소 밖으로 옮기면
  릴리스 노트가 가리킬 곳이 없어진다.
- 설치본에 들어가지 않으므로 설치 비용이 없다. 남은 문제는 **발견 불가능**이었고
  (어떤 `.md`도 이 둘을 링크하지 않았다), 그건 이 색인으로 해소된다.
- 원문 그대로가 가치다. 다시 만들 수 없는 특정 시점의 실행 기록이므로 재생성 대상이 아니라 동결 대상이다.

재검토 조건: 저장소 클론 크기가 문제가 되면(자체 마켓플레이스를 추가하면 마켓플레이스 클론에는
저장소 전체가 있다), 그때 리포트를 별도 브랜치나 GitHub Release 자산으로 옮기고 이 표의 링크를
그쪽으로 돌린다.

## 알아둘 것

- 이 디렉터리는 공개 저장소에 있다. 0.10.0부터 플러그인 설치본에는 들어가지 않지만, 저장소를
  보는 사람은 누구나 읽는다. 여기 적는 내용은 공개 문서로 쓴다.
- 저장소 루트의 `IMPLEMENTATION_NOTES.md`는 이 플러그인이 자기 자신에게 적용한 이탈 로그다.
  `docs/`에 있지 않지만 성격은 같은 계열이고, 언어도 한국어다.
