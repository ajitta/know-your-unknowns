---
status: approved-for-plan
revised: 2026-10-09
---
# Discovery: caveman-compress를 이용해보는 방안

Seed: "'caveman-compress'를이용해보는 방안". Anchor: [00-intent.md](./00-intent.md). 기존 플랜: [05-plan.md](./05-plan.md).

## Intent coverage

| Intent 항목 | 이 discovery가 구체화한 것 |
|---|---|
| Problem: "내용이 길고 장황한 서술이 많아" | 변경 없음. caveman-compress는 줄이는 수단 후보 |
| Proposed outcome: "간략하고 명료한 문장으로 다듬고 싶어" | caveman 문체(관사 생략, 단편 문장)는 "문장"에 맞지 않는다고 확인됨(Q1). caveman 출력은 초안으로만 쓰고 배포본은 문법이 온전한 문장 |
| Affected users and systems | `.md`만 해당: skill·agent 본문, references, README. hook 스크립트(`.py`)와 manifest(`.json`)는 도구가 거부하므로 05-plan Phase 4대로 수작업 |
| Constraints: 동작·트리거 그대로, 영어 유지 | frontmatter는 도구가 떼었다가 그대로 붙인다. 동작 불변은 도구가 보장하지 않으므로 eval로 확인 |
| Open questions | 아래 Open questions |

## caveman-compress에 대해 확인한 사실

출처: `~/.claude/plugins/marketplaces/caveman/plugins/caveman/skills/caveman-compress/`

- 실행: SKILL.md가 있는 디렉터리에서 `python3 -m scripts <절대경로>`. 원본을 덮어쓰고 백업은 트리 밖(`%LOCALAPPDATA%\caveman-compress\backups\<부모 폴더명>\`)에 둔다.
- 대상: `.md`, `.txt` 등 자연어 파일만. `.py`, `.json`, `.yaml` 등은 수정하지 않는다.
- frontmatter: `split_frontmatter()`로 분리해 압축하지 않고 그대로 다시 붙인다(`compress.py:52`). 05-plan Proof 1과 충돌하지 않는다.
- 모델 호출: 기본 provider는 `claude` CLI이고, `CAVEMAN_COMPRESS_MODEL`이 비어 있으면 `--model`을 넘기지 않아 Claude Code의 기본 모델이 쓰인다(`compress.py:597`). 코드에 박힌 `claude-sonnet-4-5`(`compress.py:389`)는 `anthropic` SDK provider의 기본값이고(`compress.py:570`), 이 모델은 더 이상 쓰이지 않는다.
- 압축 프롬프트(`compress.py:742`): "Compress this markdown into caveman format" + 코드·heading·URL·경로 보존 규칙 + "Never restructure, add formatting, or improve organization". 지시·숫자·용어를 보존하라는 규칙은 없다.
- 검증(`validate.py`): heading, fenced·indented 코드 블록, URL, 경로, bullet 개수, inline code만 원본과 비교한다. 실패하면 대상 오류만 고치는 재시도를 최대 2회 하고, 그래도 실패하면 원본을 그대로 둔다.
- 하지 않는 것: 표 구분행 정리, 파일 사이 중복 제거(restructure 금지), eval grader 용어 보호.
- 이 머신에서 실행 가능: `claude` 2.1.295, Python 3.14.7.

## Resolved Decisions

| # | 질문 | 결정 | mode |
|---|---|---|---|
| Q1 | caveman 문체가 "간략하고 명료한 문장"에 맞는가 | 안 맞다 | confirmed |
| Q2 | 사용 방식 | 파일럿 먼저 | confirmed |
| Q3 | 파일럿으로 알아낼 것 | 초안 파이프라인 검증: caveman 출력을 문법이 온전한 문장으로 되돌린 버전이 원본과 같은 eval 결과를 내면서 더 짧은가 | confirmed |
| Q4 | 파일럿 대상 | `skills/blindspot/SKILL.md` | confirmed |
| Q5 | 압축에 쓸 모델 | Sonnet 5.5 이상. `claude-sonnet-4-5`는 더 이상 쓰이지 않는 모델이다. 실행할 때마다 `CAVEMAN_COMPRESS_MODEL=claude-sonnet-5-5`(또는 그 이상)를 지정하고, 실행 기록에 모델 ID를 남긴다 | confirmed |
| Q6 | 파이프라인이 직접 편집보다 시간을 줄이는지 잴 것인가 | 재지 않는다 | confirmed |

## 초안 파이프라인 (검증 대상)

1. 원본을 scratchpad로 복사한다.
2. `CAVEMAN_COMPRESS_MODEL=claude-sonnet-5-5`(Q5)를 지정하고 복사본에 caveman-compress를 실행한다. 원본은 건드리지 않는다.
3. caveman 출력을 기준으로, 05-plan의 편집 규칙("남긴다"/"덜어낸다")을 지키며 문법이 온전한 짧은 영어 문장으로 다시 쓴다. caveman이 지운 내용 중 "남긴다" 목록에 걸리는 것은 원본에서 되살린다.
4. 결과를 원본 경로에 적용하고 05-plan의 검증(Proof 1·2·3, eval)을 돌린다.

## 파일럿 설계

전제: 05-plan Phase 0(기준선)을 먼저 끝낸다. 파일럿은 그 결과 중 `behavior-blindspot-*` 2케이스 × 3회를 기준선으로 쓴다. 이 6회의 `llm` rubric 2개(`ends-with-a-pasteable-prompt`, `claims-nothing-confirmed-unseen`)는 경로 B가 채점하지 않으므로, 결과 디렉터리의 `summary.md`를 보고 손으로 채점해 기준선에 넣는다.

`trigger-*-blindspot`은 돌리지 않는다. 파일럿은 본문만 고치고(description은 05-plan Phase 3.5에서 따로 고친다) 본문은 발화한 뒤에 로드되므로 본문 편집은 발화율을 바꾸지 못하고, 이 케이스의 나머지 grader(`ends-with-improved-prompt`)는 `llm`이라 경로 B에서 채점되지 않는다.

1. 위 파이프라인 1~3단계를 `skills/blindspot/SKILL.md`에 적용한다. 사용한 모델 ID와 caveman 검증 결과를 기록한다.
2. caveman 출력과 원본의 diff에서 "남긴다" 목록에 걸리는 삭제를 모두 적는다. 파이프라인이 실패하더라도 이 목록은 05-plan의 "남긴다"를 보강하는 데 쓴다.
3. 3단계 결과를 브랜치의 `skills/blindspot/SKILL.md`에 적용한다.
4. 검증: Proof 1·2·3, `independent-reviewer`에 diff를 주고 빠진 지시·숫자·용어·조건 확인, `python evals/run-manual.py --case 'behavior-blindspot-*' --runs 3 --arm with`, 그리고 그 6회의 `llm` rubric 2개를 `summary.md`에서 손으로 채점.

통과 조건(모두 만족):
- Proof 1·2·3 통과
- reviewer가 지적한 누락 0건(지적되면 되살린 뒤 다시 확인)
- 기계 채점 grader 4개(`fires-unknowns-blindspot` × 2, `labels-the-prompt-draft`, `uses-status-labels`) 중 3회 기준 2회 이상 떨어진 것 0개. 1회 차이는 3회 더 돌려 6회로 판단
- 손 채점한 `llm` rubric 2개(`ends-with-a-pasteable-prompt`, `claims-nothing-confirmed-unseen`)의 통과 수가 기준선보다 낮지 않다

결과에 따른 다음 단계:
- 통과: 원본 대비 최종본의 diff와 2단계의 삭제 목록을 사용자에게 보여 주고, 문장이 간략하고 명료해졌는지 보고 Phase 1~3에 파이프라인을 쓸지는 사용자가 정한다. 채택하든 안 하든 blindspot 편집은 Phase 2 결과로 그대로 쓴다.
- 실패: blindspot을 원본으로 되돌리고 05-plan대로 직접 편집한다. 2단계의 삭제 목록은 "남긴다" 보강에 쓴다.

## 05-plan에 미칠 변경 (review 후 반영)

- Phase 0과 Phase 1 사이에 "파일럿" Phase 추가
- Phase 1~3의 Step 1에 "파일럿이 통과하고 사용자가 채택했을 때만 초안 파이프라인 사용" 조건 추가
- Phase 0 Step 5에 `behavior-blindspot-*` 6회의 `llm` rubric 2개 손 채점 추가
- Risks에 "caveman 압축 모델이 지운 규칙을 3단계에서 놓치는 경우" 추가
- Phase 4(`.py`, `.json`)와 Phase 5의 표 구분행은 변경 없음(도구 대상 밖이거나 restructure 금지)

## Open questions

없음.

## Self-Review Iteration Log

**v1 → v2 (2026-10-09, `/sc:review`, 사용자 승인 후 반영)**
- 통과 조건이 blindspot의 핵심 결과물을 채점하지 않던 문제: `llm` rubric 2개(`ends-with-a-pasteable-prompt`, `claims-nothing-confirmed-unseen`)를 기준선과 파일럿 모두 `summary.md`에서 손으로 채점하고, 통과 조건에 "기준선보다 낮지 않다"를 넣었다. 기계 채점 grader 4개의 이름도 정확히 적었다.
- 통과하면 Phase 1~3에 자동으로 채택하던 부분: 단어 수 세 개(원본·caveman·최종)와 삭제 목록을 보여 주고 사용자가 채택 여부를 정하도록 바꿨다. "단어 수 < 799"는 어떤 편집이든 통과하므로 파이프라인의 가치를 가려내지 못한다.
- `trigger-*-blindspot` 실행을 뺐다. 본문 편집은 발화율을 바꾸지 못하고, 남은 grader는 경로 B에서 채점되지 않는다.
- 확인만 하고 바꾸지 않은 것: eval 글롭이 각각 2케이스를 고른다(`--list`), `.md`는 압축 대상이다(`detect.py:13`), frontmatter는 그대로 다시 붙는다.

**v2 → v3 (2026-10-09, 사용자 결정 반영)**
- "목적이 단어수 줄이는 것이 아니다": 통과 조건에서 "단어 수 < 799"를, 기록 항목에서 `wc -w`를 뺐다. 채택 판단 자료는 단어 수 대신 원본 대비 diff와 삭제 목록이다.
- "description은 손댈 수 있어": 파일럿은 여전히 본문만 고친다. description 편집은 05-plan Phase 3.5에서 trigger·neg eval과 함께 따로 한다.
