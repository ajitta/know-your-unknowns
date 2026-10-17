---
feature: html-page-template
phase: complete
owner: ajitta
created: 2026-10-17
updated: 2026-10-18
---
# html-page-template — 페이지 템플릿 출력 토큰 측정 (0.9.0)

## 무엇을 바꿨나

산출물 HTML을 만드는 9개 스킬(blindspot, brainstorm, buy-in, plan, prototypes, quiz, reference, teach-me, loop)은 0.8.4까지 페이지 전체를 매번 새로 생성했다. 테마 토큰(라이트/다크), 포커스·reduced-motion, 회신 조립 JS, 복사 버튼이 매 페이지 출력 토큰으로 반복됐다.

0.9.0은 그 공통부를 `skills/loop/assets/page.css`·`page.js`로 빼고, 모델은 본문 조각만 쓴 뒤 `skills/loop/scripts/render-page.py`가 제자리에서 완성 페이지로 감싼다(CSS/JS 인라인 — "한 파일, 모두 인라인" 규약은 유지). 셸이나 Python이 없으면 모델이 assets 두 파일을 그대로 인라인한다(폴백). 흔한 규약 위반(외부 리소스, `<title>` 누락, 회신 섹션 누락·빈 값·중첩·중복)은 스크립트가 거부한다. 템플릿 경로는 `output-routing.md` 자신의 위치에서 찾는다 — 참조 파일 안의 `${CLAUDE_PLUGIN_ROOT}`는 치환되지 않고 셸 변수로도 비어 있기 때문이다.

## 측정

- 하네스: `harness/run_html.py`(생성, `claude -p --plugin-dir`, 매 실행 새 cwd, stream-json에서 usage·도구 호출 기록), `harness/analyze.py`(케이스별 중앙값, 양측 Mann-Whitney U 정확 검정), `harness/check.js`(헤드리스 Chromium 페이지 점검).
- 케이스 3개(`harness/cases/`): brainstorm(ko), teach-me(en), prototypes(ko). 모두 "페이지 파일로" 요청해 HTML 칸(파일)을 고정했다.
- 모델 Opus 5.5(`claude-opus-5-5`, 실행 환경변수로 확인), Claude Code 2.1.301, Linux arm64. 케이스당 6회.

### 출하 측정: b8 (main vs 출하 트리 e8d48cb, 동시 실행)

두 팔을 같은 시각(2026-10-18 01:10–01:47 KST)에 병렬로 돌렸다. 변형 팔은 측정 중 바뀌지 않도록 고정한 worktree에서 읽었다.

| 케이스 | 출력 토큰 중앙값 (base → 0.9.0) | Δ | p | 비용 중앙값 Δ | p |
|---|---|---|---|---|---|
| brainstorm-ko | 18,338 → 13,929 | −24% | 0.026 | −16% | 0.041 |
| prototypes-ko | 29,003 → 24,385 | −16% | 0.009 | −10% | 0.180 |
| teach-me-en | 56,222 → 36,883 | −34% | 0.002 | −33% | 0.002 |

- 전체: 평균 출력 토큰 35,822 → 24,959(−30%). 사고 토큰을 뺀 출력 평균 23,508 → 17,353(−26%). 비용 합계(18회) $22.57 → $16.59(−26%).
- 모델이 쓴 문자 수(Write 내용 + Edit new_string, 바이트 아님) 중앙값: −40% / −29% / −25%, p 0.002 / 0.009 / 0.002.
- 턴 중앙값: 4 → 4, 5 → 6.5, 9.5 → 7(모두 p > 0.05).
- 출력 토큰 절감의 일부는 사고 토큰이고, 사고 토큰은 실행마다 크게 흔들린다(특히 teach-me). 템플릿이 직접 겨냥한 몫은 사고 제외 출력(−26%)과 쓴 문자 수가 더 잘 보여 준다.
- 스크립트 사용: 18/18(페이지에 템플릿 표지 `<!-- unknowns-page -->`가 있음).

### 페이지 점검 (`check.js`, b8 18쪽씩)

| 항목 | base | 0.9.0 |
|---|---|---|
| 다크 모드·`:focus-visible`·reduced-motion·`lang` | 18 | 18 |
| 회신 상자에 기본 회신이 채워져 있음 | 15 | 18 |
| 반응하면 회신이 바뀜 | 15 | 18 |
| 복사 버튼, JS 오류 0, 원격 리소스 0 | 18 | 18 |

`check.js`는 존재 여부만 본다. 0.9.0의 18/18은 템플릿이 보장하는 값이다. base의 미달분은 페이지가 자체 회신 방식(다른 id, `<pre>` 폴백)을 써서 점검기가 못 찾은 경우이고, 규약 위반이라는 뜻이 아니다(독립 검토 확인).

### 거쳐 온 측정 (참고)

출하 전 변형들을 같은 base(b6, 2026-10-17 22:30–23:03)와 비교했다. var3·var4는 base보다 늦게 돌아 시간 차가 섞여 있으므로 출하 판단에는 b8만 쓴다.

| 팔 | 내용 | 평균 출력 Δ | 비용 Δ | 메모 |
|---|---|---|---|---|
| var | 템플릿 1차 | −25% | −15% | base와 동시. 모델이 템플릿 소스를 읽느라 턴 +50–70% |
| var3 | + "§3–§4가 인터페이스 전부" 한 문장 | −31% | −26% | base 이후 실행. 템플릿 소스 Read/cat/grep 실행당 2.2 → 0.1 |
| var4 | + 1차 검토 수정 | −25% | −18% | base 이후 실행. var3과 차이 유의하지 않음(p 0.18–0.70) |

1차 템플릿에는 회신 속성 이중 이스케이프 결함(B1)이 있어, var·var3 페이지 36쪽 중 4쪽의 회신에 `&quot;` 같은 문자열이 남았다. 출하본에서는 고쳤다(var4·b8에서 0쪽).

## 회귀 확인

`evals/run-manual.py --case 'behavior-*'`(6케이스, 기계 채점기만), main과 출하 트리 동시 실행, 3회: main 33/33, 0.9.0 31/33. 실패 2건은 둘 다 blindspot이 프롬프트 초안을 쓰기 전에 접수 질문(세 목록·저장소 경로)을 먼저 던진 경우다(`behavior-blindspot-ends-with-improved-prompt`의 `labels-the-prompt-draft`, 17–19초짜리 짧은 실행). 페이지를 만들기 전 단계라 템플릿과 닿지 않는다. 그 채점기만 두 팔 동시에 10회 다시 돌린 결과는 main 8/10, 0.9.0 8/10이다 — 원래 있던 변동이다.

## 측정하지 않은 것

- 다른 6개 스킬(blindspot, buy-in, plan, quiz, reference, loop)의 페이지. 같은 경로를 쓰지만 토큰을 재지 않았다.
- Artifact 도구 칸(`--artifact`). 헤드리스 실행에는 Artifact 도구가 없어 2칸(파일)만 측정했다. `--artifact` 출력 형식은 단위 테스트와 헤드리스 브라우저로만 확인했다.
- Windows 실기. 콘솔 인코딩(cp1252) 재현·수정, BOM, LF 출력은 테스트로 덮고, CI windows-latest에서 단위 테스트가 돈다. Windows의 Claude Code에서 스킬을 실제로 돌린 적은 없다.
- Desktop/web 단독 스킬 zip. `--target local` 폴더로는 독립 검토자가 1회 실행해 템플릿 경로가 풀리는 것을 확인했다.
- `behavior-*`의 `llm` 채점기.

## 독립 검토

별도 에이전트 프로필(reviewer)이 두 번 검토했다. 1차: 차단 1(B1)·수정 권고 5. 2차: 차단 0·수정 권고 3(JS를 마크업으로 읽는 리소스 검사 오탐, `page.js` 초기화 지연, 문서 수치). 모두 출하 트리에서 고쳤다.

## 재현

```bash
cd docs/features/html-page-template/harness
PLUGIN=<main 체크아웃> OUTDIR=b8-base RUNS=6 python3 run_html.py brainstorm-ko,teach-me-en,prototypes-ko &
PLUGIN=<변형 체크아웃> OUTDIR=b8-var  RUNS=6 python3 run_html.py brainstorm-ko,teach-me-en,prototypes-ko
node check.js b8-base/*.html > b8-base.checks.jsonl   # playwright-core + Chromium headless shell 필요
node check.js b8-var/*.html  > b8-var.checks.jsonl
python3 analyze.py b8
```

원본 실행 기록(stream-json 요약, 생성된 페이지)과 검토 보고서는 저장소 밖 작업 디렉터리에 보관했다.
