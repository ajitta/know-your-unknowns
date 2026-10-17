---
feature: html-page-template
phase: complete
owner: ajitta
created: 2026-10-17
---
# html-page-template — 페이지 템플릿 출력 토큰 측정 (0.9.0)

## 무엇을 바꿨나

산출물 HTML을 만드는 9개 스킬(blindspot, brainstorm, buy-in, plan, prototypes, quiz, reference, teach-me, loop)은 0.8.4까지 페이지 전체를 매번 새로 생성했다. 테마 토큰(라이트/다크), 포커스·reduced-motion, 회신 조립 JS, 복사 버튼이 매 페이지 출력 토큰으로 반복됐다.

0.9.0은 그 공통부를 `skills/loop/assets/page.css`·`page.js`로 빼고, 모델은 본문 조각만 쓴 뒤 `skills/loop/scripts/render-page.py`가 제자리에서 완성 페이지로 감싼다(CSS/JS 인라인 — Artifact 규약의 "모두 인라인"은 유지). 셸이나 Python이 없으면 모델이 assets 두 파일을 그대로 인라인한다(폴백). 규약 위반(외부 리소스, `<title>` 누락, 회신 섹션 누락·중복·빈 값)은 스크립트가 거부한다.

## 측정

- 하네스: `harness/run_html.py`(생성, `claude -p --plugin-dir`, 매 실행 새 cwd, stream-json에서 usage·도구 호출 기록), `harness/analyze.py`(케이스별 중앙값, 양측 Mann-Whitney U 정확 검정), `harness/check.js`(헤드리스 Chromium 페이지 점검).
- 케이스 3개(`harness/cases/`): brainstorm(ko), teach-me(en), prototypes(ko). 모두 "페이지 파일로" 요청해 HTML 칸을 고정했다.
- 모델 Opus 5.5(`claude-opus-5-5`), Claude Code 2.1.301, Linux arm64. 2026-10-17 같은 날, 같은 하네스로 기준과 변형을 병렬 실행. 케이스당 6회.
- 팔: **base** = main(0.8.4 + 문서 커밋), **var** = 템플릿 1차(`feat/page-template`), **var3** = var + Windows 수정 + output-routing.md의 "§3–§4가 인터페이스 전부, 소스는 읽지 말 것" 한 문장. 출하본은 var3.

### 출력 토큰(사고 토큰 포함) 중앙값

| 케이스 | base | var | var3 | var3 Δ | var3 p |
|---|---|---|---|---|---|
| brainstorm-ko | 21,141 | 15,436 | 15,129 | −28% | 0.002 |
| prototypes-ko | 28,153 | 22,172 | 19,259 | −32% | 0.002 |
| teach-me-en | 59,339 | 41,888 | 40,187 | −32% | 0.041 |

전체 평균: base 36,201 → var 27,210(−25%) → var3 24,825(−31%).

### 모델이 쓴 바이트(Write/Edit 내용) 중앙값

| 케이스 | base | var3 | Δ | p |
|---|---|---|---|---|
| brainstorm-ko | 22,563 | 14,217 | −37% | 0.002 |
| prototypes-ko | 37,041 | 26,575 | −28% | 0.002 |
| teach-me-en | 61,371 | 44,380 | −28% | 0.002 |

### 비용과 턴

- 비용 합계(18회): base $22.53, var $19.15(−15%), var3 $16.76(−26%). var3 케이스별 중앙값 −21% / −23% / −27%, p 0.004 / 0.009 / 0.041.
- var는 턴이 50–70% 늘었다. 모델이 `page.js`·`render-page.py`를 `ls`/`grep`/`cat`으로 들여다봤기 때문(실행당 약 3회). 그래서 출력은 −25%인데 비용은 −15%에 그쳤다. var3의 한 문장이 이를 실행당 0.39회로 줄였고, 턴 증가는 +19–25%로 내려왔다(p > 0.05).

### 페이지 품질(`check.js`, 18쪽씩)

| 항목 | base | var3 |
|---|---|---|
| 다크 모드·`:focus-visible`·reduced-motion·`lang` | 18 | 18 |
| JS 꺼짐에도 기본 회신이 보임 | **16** | 18 |
| 반응하면 회신이 바뀜 | 16 | 18 |
| 복사 버튼, JS 오류 0, 원격 리소스 0 | 18 | 18 |

base의 미달 2건은 0.8.4 규약 위반(회신 textarea가 처음엔 비어 있음)이다. 템플릿이 그 규약을 코드로 고정한다.

### 스크립트 사용률

var 18/18, var3 17/18. 미사용 1건(teach-me run 1)은 셸이 있는데도 모델이 페이지 전체를 직접 썼다(45 KB). 페이지 점검은 통과했다. 폴백 경로가 작동한 사례로 기록하고 규칙은 추가하지 않는다.

## 회귀 확인

`evals/run-manual.py --case 'behavior-*' --runs 3` (6케이스, 기계 채점기만): base 32/33, 변형(var + Windows 수정) 33/33. `llm` 채점기는 채점하지 않았다.

## 측정하지 않은 것

- 다른 6개 스킬(blindspot, buy-in, plan, quiz, reference, loop)의 페이지. 같은 경로를 쓰지만 토큰을 재지 않았다.
- Artifact 도구 칸(`--artifact`). 헤드리스 실행에는 Artifact 도구가 없어 2칸(파일)만 측정했다. `--artifact` 출력 형식은 단위 테스트와 헤드리스 브라우저로만 확인했다.
- Windows 실기. 콘솔 인코딩(cp1252) 재현·수정과 LF 출력은 테스트로 덮고, CI windows-latest에서 단위 테스트가 돈다. Windows의 Claude Code에서 스킬을 실제로 돌린 적은 없다.
- Desktop/web 단독 스킬 zip(`build-skill-zips.py`)으로 설치한 환경에서의 실행.

## 재현

```bash
cd docs/features/html-page-template/harness
PLUGIN=<main 체크아웃> OUTDIR=b6-base RUNS=6 python3 run_html.py brainstorm-ko,teach-me-en,prototypes-ko
PLUGIN=<변형 체크아웃> OUTDIR=b6-var  RUNS=6 python3 run_html.py brainstorm-ko,teach-me-en,prototypes-ko
node check.js b6-base/*.html > b6-base.checks.jsonl   # playwright-core + Chromium headless shell 필요
node check.js b6-var/*.html  > b6-var.checks.jsonl
python3 analyze.py b6
```

원본 실행 기록(stream-json 요약, 생성된 페이지)은 저장소 밖 작업 디렉터리에 보관했다.
