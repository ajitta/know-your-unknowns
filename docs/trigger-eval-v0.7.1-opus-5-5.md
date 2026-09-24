# 트리거 eval — v0.7.1 on Claude Opus 5.5 (2026-09-25)

- 모델: `claude-opus-5-5` (`ANTHROPIC_MODEL`), Claude Code 2.1.281, Linux aarch64
- 방법: 경로 B — `python3 evals/run-manual.py --arm with`, 31개 케이스 전부. `llm` 채점기는
  judge 모델이 필요해서 채점하지 않았다. 아래 표는 기계 채점(`tool_used`·`regex`·`file_exists`)
  결과만이다.

## 1차 — 0.7.0 그대로 (케이스당 1회)

| 묶음 | 결과 |
|---|---|
| trigger (22) | 20/22 발화. **blindspot만 en·ko 둘 다 미발화** |
| negative (5) | 5/5 통과 |
| behavior (4) | 발화 4/4, 기계 채점 전부 통과 |

`trigger-ko-buy-in`에서 러너가 `AttributeError`로 죽었다. 2.1.281의 stream-json에는
`message`가 문자열인 이벤트가 있다. 러너를 고친 뒤 나머지 9개 케이스를 이어서 돌렸다.

## blindspot 재현 (0.7.0, 케이스당 3회)

| 케이스 | 발화 |
|---|---|
| trigger-en-blindspot | 2/3 |
| trigger-ko-blindspot | 1/3 |

1차 결과까지 합치면 **3/8**이다. 미발화한 실행은 전부 스킬 없이 바로 답했다. 멱등성, "502는
실패가 아니라 결과를 모른다는 뜻" 같은 내용은 좋았다. 하지만 카드 종류 태그, what-you-asked vs
walking-into 대비, 개선된 프롬프트가 모두 없었다. 모델이 스킬 없이도 답할 수 있다고 판단한 것이다.

## 수정 후 (0.7.1, 케이스당 3회)

description에 "바로 답할 수 있어도 실행하라. 결과물은 답이 아니라 개선된 프롬프트다"를 넣었다.

| 케이스 | 결과 |
|---|---|
| trigger-en-blindspot | 3/3 발화 |
| trigger-ko-blindspot | 3/3 발화 |
| neg-vocabulary-does-not-fire-blindspot | 3/3 미발화(통과) — 과발화 없음 |

## 전체 반복 측정 (0.7.1, 31케이스 × 3회, 같은 날)

1차가 1회뿐이었던 한계를 메우려고 0.7.1 전체를 케이스당 3회 다시 돌렸다.

| 묶음 | 결과 |
|---|---|
| 기계 채점 전체 | **104/105** |
| 발화·미발화 채점만 | 89/90 |
| 유일한 실패 | `trigger-ko-blindspot` 2/3 |

수정 후 ko-blindspot을 모두 합치면 **8/9**다(수정 직후 3/3, 이 측정 2/3, 0.8.0 회귀 측정 3/3).
en-blindspot은 9/9다. 수정 전 3/8에서 크게 올랐지만, 한국어 쪽에 가끔 직접 답하는 경우가 남아
있다. 다음 측정에서 다시 볼 것. description에 한국어를 넣지 않는다는 0.5.1 결정이 있으므로,
문구를 더 고치지는 않았다.

## 한계

- 1차는 케이스당 1회뿐이었다. 위 반복 측정으로 보완했다.
- `llm` 채점기(품질)는 채점하지 않았다. 경로 A(`claude plugin eval --judge-model sonnet`)가
  열리면 다시 돌린다.
