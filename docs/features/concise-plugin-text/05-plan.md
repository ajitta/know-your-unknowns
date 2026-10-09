---
status: draft
revised: 2026-10-09
---
# Concise plugin text Implementation Plan

**Goal:** 배포되는 plugin 텍스트(skill·agent 본문, hook 메시지, manifest 설명, README.md)를 동작과 트리거를 바꾸지 않고 간략하고 명료한 영어 문장으로 다듬는다.

**Architecture:** 코드 변경 없이 산문만 고친다. 트리거를 결정하는 frontmatter(`description:` 등)는 byte 단위로 고정하고, 모델이 행동으로 옮기는 규칙·숫자·용어는 남기고, 같은 말의 반복·행동을 바꾸지 않는 설명·군더더기만 덜어낸다. 파일 묶음마다 한 커밋이고, 기존 테스트와 eval을 편집 전후로 같은 명령으로 돌려 비교한다.

**Tech Stack:** Markdown, Python 3 (hook scripts, unittest), `evals/run-manual.py` (headless `claude -p`), Claude Code CLI `claude plugin validate`.

Input: [00-intent.md](./00-intent.md), [01-discovery.md](./01-discovery.md) (caveman-compress 파일럿). 브랜치: `docs/concise-plugin-text-intent` (intent 커밋 위에 이어서).

## 먼저 확인할 결정 (바뀔 가능성 높은 순)

1. **eval 범위와 비용.** 기본안: `behavior-*` 5케이스 × 3회를 편집 전후 1번씩(30 실행) + `trigger-*` 22케이스 × 1회 전후(44 실행). 줄이면 Phase 2·3의 회귀를 놓칠 수 있다.
2. **skill·agent `description:` 고정.** 기본안: 손대지 않는다. 0.7.1에서 description 한 문장이 blindspot 발화율을 3/8 → 6/6으로 바꿨다(`docs/trigger-eval-v0.7.1-opus-5-5.md`). 트리거 불변이 제약이므로 본문만 고친다.
3. **README.ko.md.** 기본안: 산문은 손대지 않고, 표 구분행 서식만 README.md와 함께 고친다(구분행의 `-` 개수는 번역이 아니라 서식이고, parity 테스트는 표 행 개수만 센다). README.md는 구조(heading·fence·table row·URL·`/unknowns:` 명령·`UNKNOWNS_*`)를 그대로 두고 산문만 줄여 `tests/test_readme_parity.py`를 통과시킨다. 결과적으로 한국어판 산문이 영어판보다 길어진다.
4. **목표 수치.** intent에 없다. 기본안: 기준을 두지 않고 파일별 `wc -w` 전후 표를 보고한다.

## 편집 규칙 (모든 Phase 공통)

남긴다:
- SKILL.md·agent 파일의 frontmatter 전체(첫 `---`부터 둘째 `---`까지)
- 번호 단계와 그 명령문, 숫자·임계값(질문 최대 4개, 후보 ~10개, 기본 4개 등), 출력 필드와 순서
- 파일 사이에서 재사용되는 용어: Landmine / Convention / Missing concept / History, confirmed / inferred / unchecked, **Needs checking**, improved prompt draft, done criteria, stage checkpoint
- eval regex grader가 출력에서 찾는 말: `improved prompt|prompt draft`, `inferred|unchecked|needs checking`, `done criteria|acceptance criteria|done when`
- 경로와 치환자: `$ARGUMENTS`, `${CLAUDE_PLUGIN_ROOT}/skills/loop/references/*.md`, `.unknowns/...`, `IMPLEMENTATION_NOTES.md`, `unknowns:unknowns-scout`, `unknowns:independent-reviewer` (`scripts/build-skill-zips.py`가 이 문자열을 바꾼다)
- loop 안에서 skill의 마지막 질문을 loop checkpoint로 접는 문장(0.8.2 Fixed 항목)
- #4 리뷰에서 되살린 문장: prototypes 5단계의 Kelly stopping rule과 "construct", teach-me의 "Step 6 is what buys those later rounds", output-routing.md의 rung-per-surface 줄

덜어낸다:
- 같은 규칙을 두 번 설명하는 문장, 본문과 references가 겹치는 내용(한쪽만 남기고 다른 쪽은 경로로 가리킨다)
- 모델의 행동을 바꾸지 않는 배경 설명, 예시가 둘 이상이면 하나만
- 겹 조건절과 괄호 속 부연. 긴 문장은 나누고 수동태는 명령형으로
- 표 구분행의 남는 `-`: 칸마다 `---`(정렬이 필요하면 `:---`, `---:`)만 쓴다

## 파일 맵

| 파일 | 역할 | Phase |
|---|---|---|
| `agents/unknowns-scout.md`, `agents/independent-reviewer.md` | sub-agent 지시문 | 1 |
| `skills/{blindspot,brainstorm,buy-in,interview,notes,plan,prototypes,quiz,reference,teach-me}/SKILL.md` | skill 본문 | 2 |
| `skills/loop/SKILL.md`, `skills/loop/references/{output-routing,scorecard,surfaces}.md` | loop와 공유 references | 3 |
| `hooks/scripts/impl_notes_reminder.py`, `hooks/scripts/agent_readonly_guard.py` (메시지 문자열만), `hooks/hooks.json` (`description`), `.claude-plugin/plugin.json`·`marketplace.json` (`description`) | hook 출력·manifest 설명 | 4 |
| `README.md`, `README.ko.md` (표 구분행만) | 설치·사용 안내 | 5 |
| `CHANGELOG.md` (Unreleased), 이 문서의 Deviations | 기록 | 6 |

## Phase 0: 기준선 기록

**Files:** 없음 (결과는 `evals/results/`, git-ignored)
- [ ] Step 1: `claude plugin list`로 unknowns가 켜져 있으면 `claude plugin disable unknowns`
- [ ] Step 2: `python -m unittest discover -s tests -v` → 통과 수를 기록
- [ ] Step 3: `python evals/run-manual.py --verify` → exit 0
- [ ] Step 4: `wc -w` 대상 파일 전체(위 파일 맵 Phase 1~5) → 표로 기록
- [ ] Step 5: `python evals/run-manual.py --case 'behavior-*' --runs 3 --arm with`, `python evals/run-manual.py --case 'trigger-*' --runs 1 --arm with` → 결과 디렉터리 이름과 grader별 통과율 기록
- [ ] Step 6: `behavior-blindspot-*` 6회의 `llm` rubric 2개(`ends-with-a-pasteable-prompt`, `claims-nothing-confirmed-unseen`)를 결과 디렉터리의 `summary.md`에서 손으로 채점해 기록

## Phase 0.5: caveman-compress 파일럿 (blindspot)

**Files:** Modify: `skills/blindspot/SKILL.md` (본문만). 상세 설계와 통과 조건: [01-discovery.md](./01-discovery.md) "파일럿 설계"
- [ ] Step 1: `skills/blindspot/SKILL.md`를 scratchpad로 복사하고, caveman-compress 디렉터리(`~/.claude/plugins/marketplaces/caveman/plugins/caveman/skills/caveman-compress/`)에서 `CAVEMAN_COMPRESS_MODEL=claude-sonnet-5-5 python3 -m scripts <사본 절대경로>` 실행. 사용한 모델 ID, caveman 검증 결과, 원본·caveman 출력의 `wc -w` 기록
- [ ] Step 2: caveman 출력과 원본의 diff에서 "남긴다" 목록에 걸리는 삭제를 모두 적는다
- [ ] Step 3: caveman 출력을 기준으로 편집 규칙에 맞춰 문법이 온전한 짧은 영어 문장으로 다시 쓰고, Step 2의 삭제는 원본에서 되살린다. 결과를 `skills/blindspot/SKILL.md`에 적용하고 `wc -w` 기록
- [ ] Step 4: Proof 1·2·3, `independent-reviewer`에 diff를 주고 누락 확인, `python evals/run-manual.py --case 'behavior-blindspot-*' --runs 3 --arm with`, `llm` rubric 2개 손 채점
- [ ] Step 5: 통과 조건(01-discovery) 판정. 통과 → 단어 수 세 개와 Step 2 목록을 보여 주고 Phase 1~3에 파이프라인을 쓸지 사용자에게 묻는다. 실패 → `git checkout -- skills/blindspot/SKILL.md`로 되돌리고 Phase 1~3은 직접 편집. 어느 쪽이든 Step 2 목록 중 "남긴다"에 없는 항목을 편집 규칙에 추가
- [ ] Step 6: 통과했으면 Commit `docs(blindspot): tighten skill body (caveman pilot)`, 결과는 아래 Deviations에 기록

## Phase 1: agents

**Files:** Modify: `agents/unknowns-scout.md`, `agents/independent-reviewer.md` (본문만)
- [ ] Step 1: 편집 전 frontmatter 고정 확인 명령(Proof 1)이 깨끗한지 확인
- [ ] Step 2: Phase 0.5에서 사용자가 파이프라인을 채택했으면 파일마다 Phase 0.5 Step 1~3 방식으로, 아니면 직접 편집 규칙대로 본문 수정. scout의 출력 표 열, status 정의, "Never invent findings", packet이 반환 형태를 바꾼다는 단락은 남긴다. `agents/unknowns-scout.md:30` 표 구분행은 칸마다 `---`로
- [ ] Step 3: Proof 1·2 실행
- [ ] Step 4: Commit `docs(agents): tighten agent instructions`

## Phase 2: 10개 skill 본문

**Files:** Modify: Phase 2 행의 SKILL.md 10개 (본문만). Phase 0.5가 통과했으면 blindspot은 이미 끝났으므로 9개
- [ ] Step 1: 파일마다 편집 규칙 적용(Phase 0.5에서 파이프라인을 채택했을 때만 그 방식으로). notes(867 words)·blindspot(799)·teach-me(644)부터
- [ ] Step 2: Proof 1·2·3 실행
- [ ] Step 3: `independent-reviewer` agent에 `git diff HEAD -- skills` 를 주고 "삭제된 지시·숫자·용어·조건이 있는가"만 묻는다. 지적된 것은 되살린다
- [ ] Step 4: Commit `docs(skills): tighten skill bodies`

## Phase 3: loop와 references

**Files:** Modify: `skills/loop/SKILL.md`, `skills/loop/references/*.md`
- [ ] Step 1: 편집 규칙 적용(Phase 0.5에서 파이프라인을 채택했을 때만 그 방식으로). stage 순서, tier별 분기, checkpoint 접기, `.unknowns/loop.json` 필드, references가 서로를 "in this folder"로 부르는 문장은 남긴다. `skills/loop/references/scorecard.md:40` 템플릿 구분행은 칸마다 `---`로(렌더링 결과는 같고, 기존 scorecard 파일에 행을 덧붙이는 데 영향 없음)
- [ ] Step 2: Proof 1·2·3 실행 (`test_bundled_references_bring_the_siblings_they_name` 포함)
- [ ] Step 3: Phase 2 Step 3과 같은 방식으로 reviewer 확인
- [ ] Step 4: Commit `docs(loop): tighten loop and its references`

## Phase 4: hook 메시지와 manifest 설명

**Files:** Modify: 파일 맵 Phase 4 행. Test: `tests/test_impl_notes_reminder.py`, `tests/test_agent_readonly_guard.py`, `tests/test_manifest_limits.py`
- [ ] Step 1: 테스트가 고정한 부분 문자열을 유지한다: `[unknowns]`, `[unknowns] hooks active`, `reached %d`, `IMPLEMENTATION_NOTES.md.`, `was not updated`, `/unknowns:notes init`, `A loop is in progress`, `arrives at`, `read-only`, `report the needed change`, `unknowns-scout`, `independent-reviewer`
- [ ] Step 2: 메시지 문자열과 `description` 값만 수정. 분기·포맷 인자(`%d`, `%s`) 개수는 그대로
- [ ] Step 3: `python -m unittest discover -s tests -v` → Phase 0과 같은 통과 수. plugin.json description은 81~500자, "unknowns" 포함
- [ ] Step 4: Commit `docs(hooks): shorten hook and manifest text`

## Phase 5: README.md

**Files:** Modify: `README.md`, `README.ko.md` (표 구분행만). Test: `tests/test_readme_parity.py`, `tests/test_trigger_containment.py`, `tests/test_skill_descriptions.py`
- [ ] Step 1: heading·fence·table row 수, URL, `/unknowns:` 명령, `UNKNOWNS_*` 이름, "Auto-triggers:" 블록의 따옴표 문구는 그대로 두고 산문만 줄인다. 표 구분행 `README.md:73`, `README.md:603`, `README.ko.md:66`, `README.ko.md:551`은 칸마다 `---`로
- [ ] Step 2: 위 세 테스트 실행 → 통과
- [ ] Step 3: Commit `docs(readme): tighten README prose`

## Phase 6: 재측정과 기록

**Files:** Modify: `CHANGELOG.md`, 이 문서
- [ ] Step 1: Phase 0 Step 2~6을 같은 명령으로 다시 실행
- [ ] Step 2: grader별 통과율 비교. 3회 중 2회 이상 떨어진 grader는 해당 skill의 바뀐 문장을 이전 문구로 되돌리고 그 케이스만 3회 재실행. 1회 차이는 3회 더 돌려 6회로 판단
- [ ] Step 3: `CHANGELOG.md` Unreleased에 항목 하나(대상 파일, 전후 단어 수, eval 비교 결과). 버전 bump와 release는 하지 않는다
- [ ] Step 4: 계획과 달라진 점을 아래 `## Deviations`에 기록, 모든 체크박스가 찼으면 `status: complete`
- [ ] Step 5: Commit `docs: record concise-plugin-text results`

## Risks

- **가장 위험한 단계는 Phase 3.** loop 본문(1,238 words)이 가장 길고 다른 skill과 references를 가장 많이 참조하는데, loop 동작을 기계적으로 채점하는 behavior eval이 없다(`trigger-*-loop`의 `stages-the-work`는 `llm` grader라 경로 B에서 채점되지 않는다). 그래서 reviewer 확인에 기대는 비중이 크다.
- 산문 축약이 행동을 바꾼 전례가 있다: #4에서 prototypes 5단계를 줄이자 saturation check가 5/5에서 3/6으로 떨어졌다. 같은 유형의 문장(정지 조건, 되묻기 조건)이 가장 깨지기 쉽다.
- caveman 압축 모델이 지운 규칙을 Phase 0.5 Step 3(문장 복원)에서 놓칠 수 있다. caveman 프롬프트에는 지시·숫자·용어 보존 규칙이 없고, caveman 검증기는 heading·코드·URL·경로·bullet 수만 본다. Step 2 삭제 목록과 reviewer 확인으로 막는다.
- n=3 측정은 노이즈가 크다. 1회 차이는 회귀로 판정하지 않고 재실행한다.
- README.md만 줄이면 README.ko.md와 내용 길이가 어긋난다(결정 3).
- hook 메시지를 줄이면 Python 포맷 인자 개수가 틀어질 수 있다. 테스트가 잡지만 Phase 4 Step 2에서 먼저 확인한다.

## Alternatives not taken

- description까지 줄이기: 트리거 불변 제약과 충돌하고, 바꾸면 `trigger-*` 전체를 3회씩 다시 재야 한다.
- 파일별 규칙 목록 문서를 먼저 만들고 대조하기: 17개 파일 규칙을 손으로 옮기는 비용이 크다. reviewer agent에 diff를 주는 방식으로 대신한다.
- README.ko.md 산문 동시 수정: intent의 "영어 유지" 범위를 넘는다. 표 구분행 서식만 함께 고친다.
- 단어 수 목표치 설정: intent에 근거가 없다.

## Proof

1. frontmatter 불변:
   `for f in skills/*/SKILL.md agents/*.md; do diff <(git show main:$f | awk '/^---$/{n++} {print} n==2{exit}') <(awk '/^---$/{n++} {print} n==2{exit}' $f) >/dev/null || echo "CHANGED $f"; done` → 출력 없음
2. `python -m unittest discover -s tests -v` → `OK`, Phase 0과 같은 테스트 수
3. `python evals/run-manual.py --verify` → exit 0
4. `claude plugin validate . --strict`, `claude plugin validate ./.claude-plugin/plugin.json --strict` → 둘 다 통과
5. Phase 6 Step 2 비교에서 회귀로 판정된 grader 0개
6. `wc -w` 전후 표: 대상 파일 합계가 Phase 0보다 작다
7. 표 구분행: `grep -nE '^\s*\|[ :|-]*-{4,}' skills/*/SKILL.md skills/loop/references/*.md agents/*.md README.md README.ko.md CHANGELOG.md` → 출력 없음

## Deviations

(구현 중 기록)
