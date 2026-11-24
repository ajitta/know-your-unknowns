# docs/ 색인

이 디렉터리는 **유지보수 기록**이다 — 조사·검증·측정·미결정 사항을 남긴 곳이지,
사용법 문서가 아니다. 설치와 사용법은 저장소 루트의
[README.md](../README.md)(English) / [README.ko.md](../README.ko.md)(한국어)에 있다.
예외: index.html은 공개 소개 페이지(GitHub Pages)이고, skill-authoring-guide.md는 스킬 작성 지침이다.

이 색인이 필요한 이유: 여기 파일 중 둘은 100 KB짜리 생성 HTML이고, 어떤 실행이
언제 무엇을 근거로 만들었는지 파일 안에서만 알 수 있었다. 마크다운 어디에서도
링크되지 않아 사실상 발견 불가능한 상태였다.

## 언어 정책

0.3.0 릴리스 노트는 "docs/research-know-your-unknowns.md만 의도적으로 한국어"라고 적었지만,
실제 정책은 이렇다(`AGENTS.md`의 규칙, 2026-11-24 소유자 결정으로 확인).

| 범위 | 언어 | 이유 |
|------|------|------|
| `skills/`, `claude-code/agents/`, `packaging/`, `.claude-plugin/`, `.claude/rules/`, `AGENTS.md`, `NOTICE`, `LICENSE` | 영어 | 모델이 읽는 지시문이거나 배포되는 파일 |
| `README.md`, `CHANGELOG.md`, `tests/`, `evals/`, `tools/`, `scripts/` | 영어 | 설치자·기여자 대상 |
| `README.ko.md` | 한국어 | README.md의 한국어 쌍둥이 |
| `docs/handoff.md` | 한국어 | 소유자가 읽고 고치는 인계 문서. `AGENTS.md`가 소유자가 한국어로 유지하는 문서로 정했다(예외) |
| 새 파일과 새 기록(`docs/`의 새 문서, `IMPLEMENTATION_NOTES.md`의 새 항목) | 영어 | `AGENTS.md`: 새 저장소 파일과 새 `IMPLEMENTATION_NOTES.md` 항목은 영어로 쓰고, 기존 기록과 번역은 보존한다 |
| 이미 한국어로 쓴 문서와 기록(이 색인, open-questions.md, protocol-alignment.md, trigger-matrix.md, trigger-eval-*, value-*, research, features/agent-collision·html-page-template, features/concise-plugin-text의 00·01·05, intent-report-*, 2026-10-26 전 `IMPLEMENTATION_NOTES.md` 항목) | 한국어 그대로 | 보존 대상이고 번역하지 않는다. 그 안을 고칠 때는(동결 배너 포함) 그 문서의 언어로 써서 파일마다 한 언어를 지킨다 |

두 가지를 덧붙인다.

- **스킬 description은 0.5.1부터 영어 전용이다.** 그전까지는 영어 트리거 문구 옆에 한국어
  문구를 함께 실었다. 한국어로 말해도 스킬은 그대로 뜬다 — 다만 보증 방식이 "description에
  써 두는 것"에서 "eval로 재는 것"으로 옮겨졌다(`evals/trigger-ko-*` 11건 + `tests/`의 회귀 가드).
  근거는 [trigger-eval-v0.5.1.md](trigger-eval-v0.5.1.md), 문구 목록은
  [trigger-matrix.md](trigger-matrix.md)와 [README.ko.md](../README.ko.md).
- **런타임 산출물의 언어는 배포 텍스트가 정하지 않는다.** 이 규칙을 담던 `output-routing.md`(옛 loop
  스킬의 참조 파일) §3은 0.11.0에서 지워졌고, 지금 스킬 본문에는 산출물 언어를 정하는 문장이 없다.
  `evals/trigger-ko-*`·`evals/noncode-ko-*`는 한국어 요청의 라우팅과 행동을 재지만, 답의 언어를
  채점하는 항목은 없다.

## 파일 색인

| 파일 | 무엇 | 언어 | 무엇이 만들었나 | 갱신·재생성 |
|------|------|------|----------------|------------|
| [README.md](README.md) | 이 색인 | 한국어 | 수기 | docs/에 파일이 늘거나 줄 때, 문서를 동결할 때 |
| [handoff.md](handoff.md) | 0.13.3 준비와 다음 라운드 인계: 상태, 남은 일(소유자 할 일·소유자 결정·에이전트 작업을 한 표에), 지켜볼 칸, 릴리스 절차, 규칙 | 한국어 | 수기 | 릴리스 뒤마다 상태 절을 git·태그·릴리스와 대조해 다시 쓴다. 끝난 일은 CHANGELOG.md·IMPLEMENTATION_NOTES.md에만 남긴다 |
| [index.html](index.html) | GitHub Pages 소개 페이지: 설치, 시작 질문, 작업 루프 | 영어 | 수기 | README의 스킬 목록이나 설치 경로가 바뀔 때 |
| [skill-authoring-guide.md](skill-authoring-guide.md) | Anthropic 스킬 작성 모범 사례를 이 저장소에 대응시킨 표, 지원 모델·effort, 실행 횟수 표, 스킬 변경 체크리스트 | 영어 | 수기(2026-11-03 공식 문서와 대조) | 공식 문서나 지원 모델·실행 횟수 정책이 바뀔 때 |
| [open-questions.md](open-questions.md) | 0.9.2까지의 결정 기록(A)과 재검증 대기(B). 왜 그렇게 결정했는지가 본문 | 한국어 | 수기 | **동결**(2026-11-24) — 0.9.2까지의 기록. B3·B4·B7은 2026-11-24에 닫았고 남은 B8은 handoff.md 남은 일 표로 옮겼다. 0.10.0 이후의 결정은 IMPLEMENTATION_NOTES.md·handoff.md, 측정은 CHANGELOG **Checked** 절 |
| [features/agent-collision/](features/agent-collision/README.md) | 0.9.2 두 에이전트(independent-reviewer·unknowns-scout) 가로챔 수정의 라우팅 측정: 소유자 설치 조합(dia·design·SuperClaude)에서 main 대비 리뷰 7셀·scout 9셀 × 10회(Opus), 첫 scout 배치(Sonnet) 기록, 단발 스크린, 하네스 포함 | 한국어 | 수기 + `harness/tally.py` 출력 | **동결** — 0.9.2 시점 기록. 0.11.0 description의 라우팅 확인은 CHANGELOG 0.11.0 **Checked**(36회)에 있고, 0.12.0 description 변경 뒤에는 이름 없는 리뷰·조사 요청의 가로챔을 다시 재지 않았다(handoff.md 남은 일 표). 하네스의 loop 셀(옛 loop 스킬의 `resume`과 8단계 독립 검증)은 0.11.0·0.12.0에서 없어진 경로이고 `arms/`·`fixture/`는 저장소에 없어 그대로는 다시 돌릴 수 없다 |
| [features/html-page-template/](features/html-page-template/README.md) | 0.9.0 페이지 템플릿(`render-page.py`)의 출력 토큰 측정: main 대비 3케이스 × 6회, 하네스 포함 | 한국어 | 수기 + `harness/analyze.py` 출력 | **동결** — 0.9.0 시점 기록. 측정한 페이지 템플릿(`render-page.py`·`page.css`·`page.js`)은 0.10.0에서, `output-routing.md`는 0.11.0에서 제거됐다(산출물은 대화 안의 Markdown). 재측정 대상이 없다. CHANGELOG 0.9.0이 근거로 인용하므로 하네스와 함께 남긴다 |
| [features/concise-plugin-text/](features/concise-plugin-text/README.md) | 0.8.3 플러그인 텍스트 간결화의 의도·발견·계획·측정(Sonnet 5.5, `behavior-*` 6케이스 × 3회 전후 비교). caveman-compress 파일럿 실패(`labels-the-prompt-draft` 3/6 → 0/6)와 "결과물·최종 목표를 가리키는 문장은 중복처럼 보여도 남긴다" 규칙의 근거 | 한국어(00·01·05) · 영어(README·06) | 수기 | **동결** — 0.8.3 시점 기록. CHANGELOG 0.8.3·0.13.0과 handoff.md가 06-results.md를 근거로 인용한다 |
| [trigger-matrix.md](trigger-matrix.md) | 11개 스킬의 트리거 문구 전수 + 충돌 쌍과 해소 상태 | 한국어 | 반자동 — 문서 안의 추출 스크립트 출력으로 표를 수기 갱신 | 스킬 description이 바뀔 때. 문서 "갱신 방법" 절의 `python3` 블록을 저장소 루트에서 실행 |
| [trigger-eval-v0.3.0.md](trigger-eval-v0.3.0.md) | v0.3.0 시점 자동 발화율·루프 준수 실측 기록 | 한국어 | headless `claude -p` 실행 6건의 transcript에서 추출 | **동결** — 특정 시점 측정 기록. 후속 기록은 trigger-eval-v0.5.1.md부터이고, 0.9.0부터 측정은 각 릴리스 CHANGELOG의 **Checked** 절에 있다 |
| [trigger-eval-v0.5.1.md](trigger-eval-v0.5.1.md) | 0.5.1이 description에서 한국어를 뺀 뒤의 트리거 측정. 한국어 축 11/11, 나머지 축은 미측정임을 명시 | 한국어 | `evals/run-manual.py` 실행의 `manual-result.json`에서 추출 | **동결** — 이후 측정 기록은 새 trigger-eval 파일이 아니라 CHANGELOG의 **Checked**·**Not measured** 절에 남긴다(원자료 `evals/results/`는 gitignore) |
| [trigger-eval-v0.7.1-opus-5-5.md](trigger-eval-v0.7.1-opus-5-5.md) | Claude Opus 5.5 첫 측정 — 31케이스 기계 채점, blindspot 발화 3/8 → 6/6 수정 | 한국어 | `evals/run-manual.py` (`ANTHROPIC_MODEL=claude-opus-5-5`) 실행의 `manual-result.json`에서 추출 | **동결** |
| [trigger-eval-crowd-2026-09-30.md](trigger-eval-crowd-2026-09-30.md) | 스킬 목록 예산 초과(설명 없이 이름만) 조건의 첫 트리거 측정 — 영어 11건 중 9건 발화, notes·blindspot 미발화 | 한국어 | `evals/run-manual.py --crowd 60 --budget-fraction 0.002` 실행의 `manual-result.json`과 CLI 디버그 로그에서 추출 | **동결** |
| [research-know-your-unknowns.md](research-know-your-unknowns.md) | 원문 "Know your unknowns" 페이지 조사·대조 분석. 【검증】/【단일】/【추정】 확실성 표기 | 한국어 | 수기 — 원문 다회 페치 + 플러그인 소스 대조 | 원문을 다시 페치했을 때. 재확인 날짜를 헤더 표에 한 줄 추가 |
| [talk-source.md](talk-source.md) | 원문 강연·"Know your unknowns" 11개 예시와 플러그인 구성 요소의 대응, 예시별 원문 프롬프트와 출처, 강연에서 직접 검증한 기법 | 영어 (0.8.1까지 옛 loop 스킬의 references 폴더에 있던 파일을 옮겨 왔다) | 수기 — 원문 페치 + 강연 대조 | 원문을 다시 대조했을 때, 그리고 스킬 이름이나 동작이 바뀔 때(두 README가 "원문과 다른 점"의 답으로 이 파일을 가리킨다). 스킬 본문은 이 파일을 참조하지 않는다(런타임 미로드) |
| [protocol-alignment.md](protocol-alignment.md) | 인간-AI 협업 프로토콜 대조의 격차 G1~G7 + 구조 항목 S1, 결정 표, 0.8.0 집행 기록 | 한국어 | 수기 — 프로토콜 대조 + `unknowns:interview` 4문항 | **동결** — G1–G7은 0.8.0까지 반영했고 G5는 0.11.0에서 제거됐다. S1은 하지 않았고, 2026-11-24에 README 스킬 표의 Cell 열(rule 0의 세 칸)로 대체된 것으로 보고 닫았다 |
| [value-contract.md](value-contract.md) | 이 플러그인 자신에 대한 가치 계약 — 지표, 강등·제거 조건, 측정 시계 | 한국어 | 수기 | **동결** — 0.11.0부터 제품 안에 데이터 원천이 없다(파일 맨 위 상태 줄). 측정 시계는 2026-11-24 행으로 닫았고 B7도 같은 날 닫았다 |
| [value-scorecard.md](value-scorecard.md) | 실사용 1회 = 1행 기록. value-contract의 지표 원장 | 한국어 | 수기 | **동결** — 0.11.0에서 제품 안의 스코어카드가 제거됐다. 마지막 행 2026-09-20 |
| [intent-report-v0.2.0.html](intent-report-v0.2.0.html) | v0.2.0 의도 부합성 검증 리포트 (97,836 바이트) | 한국어 | 검증 워크플로 산출물 — `wf_1d569a3d`, `wf_ecf82b01`. 이 저장소 커밋을 인용하지 않는다(본문의 16진수 id는 git 객체가 아님) | **동결** — 재생성하지 않는다 |
| [intent-report-v0.3.0.html](intent-report-v0.3.0.html) | v0.3.0 의도 부합성 검증 리포트 (102,976 바이트). 17개 대상 · 반박 검증 | 한국어 | 검증 워크플로 산출물 — `wf_83310eb9`. 커밋 `f1f2930`·`c51a0fc` 대상 | **동결** — 재생성하지 않는다 |

## 두 HTML 리포트에 대한 결정

**결정: 저장소에 그대로 둔다. 설치 페이로드와 릴리스 zip에는 넣지 않는다. 대신 이 색인에서 링크한다.**

배경. 두 파일은 합쳐 약 200 KB다. 0.10.0 전에는 마켓플레이스 설치가 저장소 전체를 플러그인
캐시로 복사했으므로 이 리포트들도 설치본에 따라 들어갔다(0.9.2 설치본 2.0 MB). 0.10.0부터
설치되는 플러그인은 생성물 `plugins/unknowns/`뿐이다(0.13.3 기준 29파일, 107,096 B). 자체 마켓플레이스
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
  `docs/`에 있지 않지만 성격은 같은 계열이다. 2026-10-26 항목부터는 영어로, 그 전 항목은 한국어로
  쓰여 있다. 열린 일은 [handoff.md](handoff.md)의 남은 일 표 하나로 추적한다.
- 측정 기록은 각 릴리스 `CHANGELOG.md`의 **Checked**·**Not measured** 절에 남긴다(2026-11-24 소유자
  결정). **Checked** 절은 0.9.0부터 모든 릴리스에 있다. `trigger-eval-*` 시리즈는 동결했고 새 파일을
  만들지 않는다.
