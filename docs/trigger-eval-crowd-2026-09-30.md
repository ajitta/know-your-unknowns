# 트리거 eval — 붐비는 스킬 목록 (2026-09-30)

- 환경: Claude Code 2.1.285, 이 세션의 클라우드 컨테이너. 모델은 고정하지 않았다(환경 기본값).
  같은 설정의 탐침 실행 디버그 로그에는 `claude-sonnet-5-5`가 찍혔다. 측정 실행은 모델을
  기록하지 않았으므로 같은 기본값이었을 것으로 **추정**한다(러너는 이제 실행마다 모델을 기록한다).
- 방법: 경로 B — `python3 evals/run-manual.py --case 'trigger-en-*' --runs 1`, 두 조건.
  `llm` 채점기는 채점하지 않았다. 아래는 `tool: Skill` 발화 여부(표시 전용 채점기)만이다.
- 브랜치: `fix/unknown-unknowns-audit` (0.8.1 이후, 미릴리스).

## 왜 쟀나

Claude Code는 스킬 목록에 예산을 둔다(기본 컨텍스트 창의 1%). 넘치면 사용 횟수(최근성 가중)가
낮은 스킬부터 **설명을 빼고 이름만** 남긴다. 깨끗한 eval 환경에서는 거의 넘치지 않으므로,
지금까지의 트리거 측정은 "설명이 보일 때"만 잰 것이다.

## 조건

| 조건 | 명령 | 설명 목록 상태 |
|---|---|---|
| crowd | `--crowd 60 --budget-fraction 0.002` | 필러 스킬 60개를 먼저 로드, 실행마다 빈 `CLAUDE_CONFIG_DIR`(사용 이력 없음 — 단 이 환경에 동기화된 design·finance·cowork-plugin-management 플러그인은 그래도 로드됐다, 탐침 디버그 로그 기준). CLI 디버그 로그: `Skill listing over budget: 124 skills, 35443 chars > 6000 budget`. 같은 설정의 탐침 실행에서 모델은 unknowns 스킬 11개 **전부 이름만** 보인다고 보고했다 |
| plain | 옵션 없음 | 이 컨테이너의 기본 설정 그대로(격리 안 함). 목록 예산 안쪽 |

## 결과 (케이스당 1회)

| 케이스 | plain | crowd |
|---|---|---|
| trigger-en-blindspot | 발화 | **미발화** — 스킬 없이 바로 답함(멱등성·이중 청구 위험을 짚는 좋은 답이지만 카드·개선 프롬프트 없음) |
| trigger-en-brainstorm | 발화 | 발화 |
| trigger-en-buy-in | 발화 | 발화 |
| trigger-en-interview | 발화 | 발화 |
| trigger-en-loop | 발화 | 발화 |
| trigger-en-notes | 발화 | **미발화** — 스킬 없이 Glob/Grep 후 이탈 항목을 직접 쓰려 했다(Write가 막힌 케이스라 채팅에 붙여 넣을 형태로 반환) |
| trigger-en-plan | 발화 | 발화 |
| trigger-en-prototypes | 발화 | 발화 |
| trigger-en-quiz | 발화 | 발화 |
| trigger-en-reference | 발화 | 발화 |
| trigger-en-teach-me | 발화 | 발화 |
| **합계** | **11/11** | **9/11** |

## 읽는 법과 한계

- 설명이 빠져 이름만 남아도 대부분은 발화했다. 이름이 곧 요청어인 스킬(plan, quiz,
  interview, teach-me…)은 이름만으로도 맞았다고 볼 수 있다 — **추론**이지 측정이 아니다.
- 빠진 둘 중 blindspot은 v0.7.1 측정에서도 "스킬 없이 답할 수 있다"고 판단해 미발화한 전력이
  있다([trigger-eval-v0.7.1-opus-5-5.md](trigger-eval-v0.7.1-opus-5-5.md)). 설명의 "run it even when
  you could answer directly" 문장이 그 보정인데, 설명이 빠지면 보정도 같이 빠진다.
- **일반화 금지.** 케이스당 1회다. 두 조건은 예산만이 아니라 사용 이력·설치된 플러그인도
  다르다(plain은 격리하지 않았다). 실사용자 환경에서 어떤 설명이 빠질지는 그 사람의 사용
  이력이 정한다.
- 측정 실행 자체에는 디버그 로그가 없었다(이 기능은 측정 뒤에 러너에 추가). 예산 초과는 같은
  설정의 탐침 실행 로그로 확인했다. 다음 측정부터는 러너가 실행마다 CLI 로그를 기록한다.
- 이 파일은 **동결** 기록이다. 재측정은 새 날짜의 새 파일로, 가능하면 `--runs 3`과 격리된
  plain 조건(같은 `CLAUDE_CONFIG_DIR` 방식)으로.

## 같은 날 먼저 돌린 실행에 대한 정정

같은 날 앞서 `--crowd 60`(예산 기본값, 격리 없음)으로 5케이스를 돌려 5/5를 얻었고, 그때는
"예산이 넘쳤는데도 unknowns 설명은 유지됐다"고 기록했다. 독립 리뷰가 두 가지를 지적했다:
헤드리스 실행도 `~/.claude.json`의 `skillUsage`를 올리므로 앞선 eval 실행이 테스트 대상 스킬에
사용 이력을 쌓아 줬고, 넘친 원인은 필러가 아니라 이 환경에 깔린 다른 플러그인일 수 있다.
그래서 격리와 강제 예산을 넣은 위 측정으로 대체한다.
