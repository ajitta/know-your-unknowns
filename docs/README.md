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
| `skills/`, `agents/`, `hooks/`, `.claude-plugin/`, `NOTICE`, `LICENSE` | 영어 | 모델이 읽는 지시문이고, 설치자가 누구든 읽어야 한다 |
| `README.md`, `CHANGELOG.md`, `tests/`, `evals/` | 영어 | 설치자·기여자 대상 |
| `README.ko.md` | 한국어 | README.md의 한국어 쌍둥이 |
| `docs/**`, `IMPLEMENTATION_NOTES.md` | 한국어 | 작성자 자신의 작업 기록. 번역 대상이 아니다 |

두 가지 예외가 정책의 일부다.

- **스킬 description은 이중 언어다.** 영어 트리거 문구 옆에 한국어 문구를 함께 싣는다.
  자연어 자동 발화는 문자열 매칭에 가깝게 동작하므로, 한국어 문구가 빠지면 한국어로 말할 때
  스킬이 뜨지 않는다. 목록은 [trigger-matrix.md](trigger-matrix.md).
- **런타임 산출물은 사용자의 언어를 따른다.** 카드·질문·프롬프트 초안 같은 사용자 대면 문장은
  사용자가 쓰고 있는 언어로 쓴다(파일명·템플릿 키·코드 식별자는 고정).
  근거: [`skills/loop/references/output-routing.md`](../skills/loop/references/output-routing.md) §3.

## 파일 색인

| 파일 | 무엇 | 언어 | 무엇이 만들었나 | 갱신·재생성 |
|------|------|------|----------------|------------|
| [README.md](README.md) | 이 색인 | 한국어 | 수기 | docs/에 파일이 늘거나 줄 때 |
| [open-questions.md](open-questions.md) | 결정 기록(A)과 재검증 대기(B). 왜 그렇게 결정했는지가 본문 | 한국어 | 수기 | 결정이 날 때마다. 항목은 B→A로 옮기고 삭제하지 않는다 |
| [trigger-matrix.md](trigger-matrix.md) | 11개 스킬의 트리거 문구 전수 + 충돌 쌍과 해소 상태 | 한국어 | 반자동 — 문서 안의 추출 스크립트 출력으로 표를 수기 갱신 | 문서 "갱신 방법" 절의 `python3` 블록을 저장소 루트에서 실행 |
| [trigger-eval-v0.3.0.md](trigger-eval-v0.3.0.md) | v0.3.0 시점 자동 발화율·루프 준수 실측 기록 | 한국어 | headless `claude -p` 실행 6건의 transcript에서 추출 | **동결** — 특정 시점 측정 기록. 재측정은 새 날짜의 새 파일로 (open-questions B5) |
| [research-know-your-unknowns.md](research-know-your-unknowns.md) | 원문 "Know your unknowns" 페이지 조사·대조 분석. 【검증】/【단일】/【추정】 확실성 표기 | 한국어 | 수기 — 원문 다회 페치 + 플러그인 소스 대조 | 원문을 다시 페치했을 때. 재확인 날짜를 헤더 표에 한 줄 추가 |
| [value-contract.md](value-contract.md) | 이 플러그인 자신에 대한 가치 계약 — 지표, 강등·제거 조건, 측정 시계 | 한국어 | 수기 | 수치를 고칠 때(잠정값), 그리고 측정 시계 확인 때마다 표에 한 행 |
| [value-scorecard.md](value-scorecard.md) | 실사용 1회 = 1행 기록. value-contract의 지표 원장 | 한국어 | 수기 | 실사용마다. 설치자는 자기 저장소의 `.unknowns/scorecard.md`에 따로 기록 |
| [intent-report-v0.2.0.html](intent-report-v0.2.0.html) | v0.2.0 의도 부합성 검증 리포트 (97,836 바이트) | 한국어 | 검증 워크플로 산출물 — `wf_1d569a3d`, `wf_ecf82b01`. 이 저장소 커밋을 인용하지 않는다(본문의 16진수 id는 git 객체가 아님) | **동결** — 재생성하지 않는다 |
| [intent-report-v0.3.0.html](intent-report-v0.3.0.html) | v0.3.0 의도 부합성 검증 리포트 (102,976 바이트). 17개 대상 · 반박 검증 | 한국어 | 검증 워크플로 산출물 — `wf_83310eb9`. 커밋 `f1f2930`·`c51a0fc` 대상 | **동결** — 재생성하지 않는다 |

## 두 HTML 리포트에 대한 결정

**결정: 저장소에 그대로 둔다. 릴리스 zip에는 넣지 않는다. 대신 이 색인에서 링크한다.**

배경. 두 파일은 합쳐 약 200 KB이고, `.claude-plugin/marketplace.json`의 `"source": "./"`가
플러그인 디렉터리 전체를 캐시로 복사하므로 **마켓플레이스 설치본에 그대로 따라 들어간다**.
반면 `scripts/build-plugin.sh`가 만드는 zip은 `.claude-plugin skills agents hooks
README.md README.ko.md CHANGELOG.md LICENSE NOTICE`만 담는다 — 즉 두 배포 경로의 파일 집합이
애초에 다르고, `docs/`와 `tests/`는 마켓플레이스 경로에만 있다.

왜 두는가.

- 이 리포트들은 CHANGELOG 0.2.0·0.3.0 항목이 근거로 삼는 **검증 증거**다. 저장소 밖으로 옮기면
  릴리스 노트가 가리킬 곳이 없어진다.
- 200 KB는 플러그인 설치 비용으로 무시할 만하다. 실제 문제는 용량이 아니라 **발견 불가능**이었고
  (어떤 `.md`도 이 둘을 링크하지 않았다), 그건 이 색인으로 해소된다.
- 원문 그대로가 가치다. 다시 만들 수 없는 특정 시점의 실행 기록이므로 재생성 대상이 아니라 동결 대상이다.

왜 릴리스 zip에는 안 넣는가. zip은 "플러그인이 동작하는 데 필요한 것"만 담는 경로다.
유지보수 기록은 저장소에서 읽으면 된다.

재검토 조건: `docs/`가 지금의 몇 배로 커져서 설치 캐시 크기가 실제로 문제가 되면,
그때 리포트를 별도 브랜치나 GitHub Release 자산으로 옮기고 이 표의 링크를 그쪽으로 돌린다.

## 알아둘 것

- 마켓플레이스로 설치하면 이 디렉터리와 `tests/`, `.github/`까지 캐시에 복사된다.
  설치본에서 이 문서들을 읽을 수 있다는 뜻이고, 반대로 여기 적는 내용은 설치자도 본다는 뜻이다.
- 저장소 루트의 `IMPLEMENTATION_NOTES.md`는 이 플러그인이 자기 자신에게 적용한 이탈 로그다.
  `docs/`에 있지 않지만 성격은 같은 계열이고, 언어도 한국어다.
