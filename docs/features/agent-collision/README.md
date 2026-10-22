---
feature: agent-collision
phase: complete
owner: ajitta
created: 2026-10-22
updated: 2026-10-22
---
# agent-collision — 다른 워크플로가 unknowns 에이전트를 가로채던 문제 (0.9.2)

## 증상

소유자 보고: "review, brainstorm 같은 스킬이 다른 스킬과 충돌해서 의도하지 않게 트리거된다."

이 VM의 실제 Claude Code 기록(`~/.claude/projects/**/*.jsonl`)에서 측정용 실행을 빼고 unknowns 스킬·에이전트가 호출된 경우를 전수로 뽑았다. 의도하지 않은 호출은 두 건이었고 둘 다 `unknowns:independent-reviewer`였다.

| 시각(UTC) | 무엇이 부르는 중이었나 | 무엇을 원했나 |
|---|---|---|
| 2026-10-19 17:27 | 볼트 프로젝트 스킬 `/extract-permanent` 3단계 "서브에이전트 하나로 독립 검토" | 노트 주장 비교(코드 아님) |
| 2026-10-20 13:52 | SuperClaude `/sc:intent --through` → `/sc:review` | `/sc:review`가 명시한 `self-review` 에이전트 |

원인은 0.9.1까지의 에이전트 description이다: "Use proactively before merging…", "Triggers: \"independent review before merge\"". 워크플로가 "독립 검토"·"격리된 리뷰어"를 찾을 때 이름과 설명이 가장 잘 맞는 이 에이전트가 뽑힐 수 있었다. 늘 그런 것은 아니다 — 이 에이전트를 고를 수 있었던 세션의 리뷰·검증 성격 dispatch 32건 중 2건이었다(general-purpose 20, self-review 8). 독립 검토(reviewer 프로필)가 다시 셌다.

brainstorm 쪽은 같은 기록에서 의도하지 않은 호출이 한 건도 없었고, 아래 단발 스크린에서도 재현되지 않았다.

## 바꾼 것

두 에이전트의 description만 바꿨다(본문 그대로).

`agents/independent-reviewer.md`:

- "Use proactively" 문장과 `Triggers: "independent review before merge"`를 뺐다.
- 호출 조건: 사용자가 이 에이전트를 이름으로 부를 때, 또는 unknowns 스킬(loop 8단계, buy-in)이 부를 때만.
- 경계: 그 밖의 코드·PR·"독립" 리뷰, 또는 다른 스킬·명령·워크플로가 리뷰어나 격리된 서브에이전트를 찾을 때는 그 워크플로가 지정한 에이전트, 없으면 general-purpose.

`agents/unknowns-scout.md`: 같은 구조("Use proactively BEFORE implementation…", `Triggers: "blind-spot pass", "what am I missing"`)를 같은 규칙으로 바꿨다 — 이름으로 부르거나 blindspot·brainstorm이 부를 때만, 다른 조사·리서치 서브에이전트 요청은 그 워크플로의 에이전트, Explore, general-purpose로. 트리거 문구는 blindspot 스킬이 계속 갖는다. 실제 기록에 의도하지 않은 scout 호출은 없었다(조사형 dispatch 116건 중 scout 3건, 모두 의도된 탐침). 소유자 결정으로 같은 위험을 미리 막는다.

`tests/test_agent_descriptions.py`가 두 description에 "proactively"·`Triggers:`가 없고 이름 호출 규칙이 남아 있는지 검사한다.

README 두 언어의 호출 예시 "Run an independent verification" / "독립 검증 돌려줘"는 이제 이 에이전트를 부르지 않으므로 이름을 넣은 예시로 바꿨다.

## 측정

- 모델 `claude-opus-5-5`, Claude Code 2.1.307, Linux arm64, 2026-10-22. 두 팔(base = main `f35a8a0`, var = 이 변경)을 고정 worktree에서 같은 시각에 병렬로 돌렸다.
- 환경: 소유자의 설치 조합을 재현했다 — unknowns + dia 1.3.0 + design(claude.ai 동기화 사본)을 `--plugin-dir`로, SuperClaude(`~/.claude`의 `CLAUDE.md`·`superclaude/`·`commands/`·`agents/`·`skills/sc-*`·`settings.json` 훅)를 새 `CLAUDE_CONFIG_DIR`에 복사. `ENABLE_CLAUDEAI_MCP_SERVERS=false`. fixture 저장소 자체에도 프로젝트 수준 SuperClaude(`.claude/`의 CLAUDE.md, commands/sc, agents/self-review, 훅)가 들어 있어 SuperClaude는 두 수준에서 로드된다. "SuperClaude 없음"을 재현하려면 둘 다 빼야 한다.
- 작업 디렉터리: 매 실행마다 새로 복사한 작은 todo CLI 저장소(`main` + `feature/todo-due-dates` 브랜치, 계획·요구사항 문서는 브랜치에 있음).
- 비용 절감: `PreToolUse` 훅이 Agent 호출을 거부한다. 거부 전에 tool_use가 기록되므로 "어느 에이전트를 골랐나"는 그대로 남고, 서브에이전트는 실제로 돌지 않는다. 판정(`tally.py`): "unknowns 아님" 셀은 실행 어디에도 unknowns 스킬·에이전트가 없으면 통과, 양성 셀은 기대한 에이전트가 호출 목록에 있으면 통과.

### 리뷰 라우팅 (셀당 10회)

| 셀 | 요청 | 기대 | base | var | p |
|---|---|---|---|---|---|
| f-rv-indep-en | "Get an independent review of the … branch before I merge it." | unknowns 아님 | 0/10 (10회 모두 independent-reviewer) | 10/10 (10회 모두 `sc:review`) | 1.1e-5 |
| f-rv-indep-ko | "…브랜치를 머지 전에 독립적으로 리뷰해줘." | unknowns 아님 | 1/10 (9회 independent-reviewer) | 10/10 (`sc:review` 6, 직접 답 4) | 1.2e-4 |
| f-rv-sub-ko | "README가 todo.py와 맞는지 서브에이전트 하나 띄워서 독립 검토해줘." | unknowns 아님 | 8/10 (2회 independent-reviewer) | 10/10 (general-purpose 10) | 0.47 |
| f-rv-plain-ko | "…머지해도 되는지 리뷰해줘." | unknowns 아님 | 10/10 | 10/10 | 1.0 |
| f-rv-pos-ko | "unknowns의 independent-reviewer 에이전트로 … 검토해줘." | independent-reviewer | 10/10 | 10/10 | 1.0 |
| f-rv-pos-en | "Use the independent-reviewer agent — verify … before merge." | independent-reviewer | 10/10 | 10/10 | 1.0 |
| f-rv-loop | "/unknowns:loop resume … 8단계 독립 검증부터" | independent-reviewer | 8/10 (2회는 권한 거부로 8단계 전에 멈춤) | 10/10 | 0.47 |

이름 없는 리뷰 요청 30회 중 unknowns 에이전트가 가로챈 횟수: base 21, var 0. 이름으로 부르거나 loop가 부르는 경로는 줄지 않았다.

검열 주의: var의 0/30 중 7회(en 1·2·7, ko 3·6·7·8)는 `sc:review`를 먼저 부른 뒤 리뷰어를 고르기 전에 `--max-turns 10`에 걸려 끝났다. base에서 같은 식으로 잘린 것은 1회다. 독립 검토가 max-turns 20으로 두 셀을 셀당 5회씩 다시 돌렸다.

| 조건 | 요청 | base | var |
|---|---|---|---|
| fixture 그대로(프로젝트 수준 SuperClaude) | indep-en | unknowns 5/5 | sc:review → self-review 4, → general-purpose 1 |
| 〃 | indep-ko | unknowns 5/5 | sc:review → self-review 2, → general-purpose 1, 직접 답 2 |
| SuperClaude 완전 제거 | indep-en | unknowns 5/5 | general-purpose 5/5 |
| 〃 | indep-ko | unknowns 5/5 | 직접 답 5/5 |
| 〃 | pos-en("Use the independent-reviewer agent — …") | unknowns 5/5 | unknowns 5/5 |
| 원 설정 | `/sc:review --scope branch feature/todo-due-dates` | Agent 호출 0, 인라인 리뷰 5/5 | Agent 호출 0, 인라인 리뷰 5/5 |

가로챔 20/20 → 0/20. 단 base는 실제 사고의 경로(`/sc:review` 안에서 리뷰어 고르기)를 한 번도 타지 않았다 — base의 가로챔은 모두 최상위 첫 호출이었다. `/sc:review` 뒤 선택은 var에서만 관측됐고(out-fx2 8회 + 재측정 8회), unknowns는 0회였다. 증거 사본: 측정 디렉터리 `review/rv1-evidence/`.

### loop·buy-in 경로 (권한 허용, 셀당 5회)

`fixture-feat`(브랜치 체크아웃 상태), `--permission-mode acceptEdits`, git·make·python3 허용, `--max-turns 20`.

| 셀 | 요청 | base | var |
|---|---|---|---|
| l-loop-ko | "/unknowns:loop resume … 8단계 독립 검증부터" | 5/5 independent-reviewer | 5/5 |
| l-buyin-ko | "/unknowns:buy-in 이 브랜치 머지 승인 받을 설득 문서" | 5/5 independent-reviewer | 5/5 |

스킬 안에서 부르는 경로는 두 팔 모두 매번 이 에이전트에 닿았다.

### unknowns-scout 라우팅

SCOUT_RESULTS

### 단발 스크린 (base만, 셀당 3회)

변경 전에 충돌 후보를 찾느라 돌린 것이다. 의도하지 않은 unknowns 호출은 저장소 안 리뷰 세 셀(indep-en 3/3, indep-ko 3/3, sub-ko 1/3)뿐이었다.

- dia + design 동반(19셀, 빈 디렉터리): 빵집 이름·워크숍·블로그 주제 브레인스토밍, "옵션 보여줘", PR·함수 리뷰, 머지 전 리뷰, 운동 계획, 한국사 퀴즈, 모의 면접, 회의 노트, 참고문헌 형식 — 모두 unknowns 0회. 아이디어 브레인스토밍 2셀은 `dia:dia-brainstorm`, 초안 재검토는 `dia:dia-refine`, 디자인 리뷰는 `design:design-critique`로 갔다. 양성 대조(brainstorm·buy-in)는 3/3.
- SuperClaude 동반(12셀): `/sc:brainstorm`·`/sc:review`·`/sc:plan` 명령과 같은 뜻의 자연어 요청 — unknowns 0회. 자연어 브레인스토밍 요청이 `sc:brainstorm`으로 간 적은 없다(직접 답). 양성 대조 brainstorm 2/3, buy-in 3/3.
- 저장소 안(SuperClaude 동반): "브레인스토밍 해보자", "어떻게 하면 좋을까?", "선택지 보여줘", `/sc:brainstorm` — unknowns 0회.

### 측정하지 않은 것

- claude.ai·데스크톱 앱·모바일(스킬 이름이 네임스페이스 없이 보이는 표면). brainstorm 충돌이 거기서 났다면 이 측정은 그것을 보지 못했다.
- 여러 턴짜리 대화 중간의 라우팅. 실제 두 사례는 긴 워크플로 중간이었고, 측정은 단발 요청이다.

## 하네스

`harness/`의 스크립트는 측정 디렉터리(`arms/base`, `arms/var`, `arms/dia`, `arms/design`, `fixture/`, `fixture-feat/`)를 스크립트 옆에 두고 돌린다. 저장소에는 들어 있지 않다.

- `screen_single_turn.py <arm> [runs] [cell-prefix…]` — dia + design 동반 단발 스크린
- `screen_superclaude.py` — 같은 것에 SuperClaude 설정 복사를 더한 것(빈 디렉터리)
- `screen_repo.py` — SuperClaude 동반, 저장소 fixture 안 단발 스크린(리뷰·브레인스토밍 12셀)
- `run_scout_routing.py` — scout 라우팅 표
- `run_review_routing.py` — 위 리뷰 라우팅 표(저장소 fixture, Agent 거부 훅)
- `run_loop.py` — loop·buy-in 경로(`--permission-mode acceptEdits`, git/make/python3 허용)
- `tally.py <out-dir>` — 셀별 base/var 통과 수와 Fisher 정확 검정
