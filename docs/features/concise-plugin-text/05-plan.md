---
status: draft
revised: 2026-10-09
---
# Concise plugin text Implementation Plan

**Goal:** 배포되는 plugin 텍스트(skill·agent의 description과 본문, hook 메시지, manifest 설명, README.md)를 동작과 트리거를 바꾸지 않고 간략하고 명료한 영어 문장으로 다듬는다.

**Architecture:** 코드 동작은 바꾸지 않고 문장만 고친다. 모델이 행동으로 옮기는 규칙·숫자·용어는 남기고, 반복·행동을 바꾸지 않는 설명·군더더기를 덜어낸다. 본문 편집과 description 편집은 커밋을 나눈다: 본문은 발화 뒤에 로드되므로 behavior eval로, description은 발화를 정하므로 trigger·negative eval로 확인한다.

**Tech Stack:** Markdown, Python 3 (hook scripts, unittest), `evals/run-manual.py` (headless `claude -p`), `claude plugin validate`.

Input: [00-intent.md](./00-intent.md), [01-discovery.md](./01-discovery.md) (caveman-compress 파일럿). 브랜치: `docs/concise-plugin-text-intent`.

## 결정

1. **eval 범위**: `behavior-*` 5케이스 × 3회를 편집 전후로(30회), 파일럿 `behavior-blindspot-*` 6회. 트리거는 "Sonnet 5.5에서 발화하는지 확인되면 된다"(사용자 확인): 기준선 없이 Phase 3.5 뒤에 description을 바꾼 skill의 `trigger-*`·`neg-*` 케이스만 × 3회(최대 81회). 통과 기준 trigger 2/3 이상·neg 0/3(사용자 승인).
2. **description은 고칠 수 있다** (사용자 확인). 트리거 불변 제약은 Phase 3.5의 규칙과 trigger·neg eval로 지킨다. `name`, `argument-hint`, `tools`, `model`, `color`는 고정.
3. **README.ko.md**: 산문은 손대지 않고 표 구분행 서식만 README.md와 함께 고친다(사용자 승인).
4. **단어 수는 목적도 기준도 아니다** (사용자 확인). 판단 기준은 문장이 간략하고 명료한지, 그리고 동작·트리거가 그대로인지다.

## 편집 규칙 (모든 Phase 공통)

남긴다:
- 번호 단계와 그 명령문, 숫자·임계값(질문 최대 4개, 후보 ~10개, 기본 4개 등), 출력 필드와 순서
- 파일 사이에서 재사용되는 용어: Landmine / Convention / Missing concept / History, confirmed / inferred / unchecked, **Needs checking**, improved prompt draft, done criteria, stage checkpoint
- eval regex grader가 찾는 말: `improved prompt|prompt draft`, `inferred|unchecked|needs checking`, `done criteria|acceptance criteria|done when`
- 경로와 치환자: `$ARGUMENTS`, `${CLAUDE_PLUGIN_ROOT}/skills/loop/references/*.md`, `.unknowns/...`, `IMPLEMENTATION_NOTES.md`, `unknowns:unknowns-scout`, `unknowns:independent-reviewer` (`scripts/build-skill-zips.py`가 바꾸는 문자열)
- loop 안에서 skill의 마지막 질문을 loop checkpoint로 접는 문장(0.8.2 Fixed)
- #4 리뷰에서 되살린 문장: prototypes 5단계의 Kelly stopping rule과 "construct", teach-me의 "Step 6 is what buys those later rounds", output-routing.md의 rung-per-surface 줄
- skill의 결과물·최종 목표를 가리키는 문장. 중복처럼 보여도 남긴다(파일럿: blindspot 5단계 "the core deliverable of this skill"을 Iron Rule 2와 중복으로 지우자 `labels-the-prompt-draft`가 3/6 → 0/6)

덜어낸다:
- 같은 규칙을 두 번 설명하는 문장, 본문과 references의 중복(한쪽만 남기고 경로로 가리킨다)
- 행동을 바꾸지 않는 배경 설명, 같은 패턴의 두 번째 예시
- 겹 조건절과 괄호 속 부연. 긴 문장은 나누고 수동태는 명령형으로
- 표 구분행의 남는 `-`: 칸마다 `---`(정렬은 `:---`, `---:`)

## eval 실행 규칙

설치된 `unknowns@synced`가 켜져 있으면 작업 트리(`--plugin-dir .`)와 섞여 측정된다. 이 설치본이 reviewer agent도 제공하므로 eval 동안만 끈다.
- eval 직전: `claude plugin disable unknowns` 후 `claude plugin list`로 꺼졌는지 확인. 꺼지지 않았으면 멈추고 사용자에게 알린다.
- eval 직후: `claude plugin enable unknowns` 후 다시 켜졌는지 확인. reviewer 확인은 켜진 상태에서만.
- eval 모델: `run-manual.py`마다 `ANTHROPIC_MODEL=claude-sonnet-5-5`를 붙인다(모델 인자가 없고 `model:` 케이스도 없음). `manual-result.json`의 run별 `model`이 이 값이 아니면 그 결과는 버린다.
- 판정: 3회 중 2회 이상 떨어진 grader는 회귀. 1회 차이는 3회 더 돌려 6회로 판단.

## 파일 맵

| 파일 | 역할 | Phase |
|---|---|---|
| `agents/*.md` 2개 본문 | sub-agent 지시문 | 1 |
| `skills/{blindspot,brainstorm,buy-in,interview,notes,plan,prototypes,quiz,reference,teach-me}/SKILL.md` 본문 | skill 본문 | 0.5, 2 |
| `skills/loop/SKILL.md`, `skills/loop/references/*.md` | loop와 공유 references | 3 |
| `skills/*/SKILL.md`·`agents/*.md`의 `description:`, `docs/trigger-matrix.md`(description 인용) | 트리거 문구 | 3.5 |
| `hooks/scripts/*.py`(메시지 문자열만), `hooks/hooks.json`·`.claude-plugin/*.json`의 `description` | hook 출력·manifest 설명 | 4 |
| `README.md`, `README.ko.md`(표 구분행만) | 설치·사용 안내 | 5 |
| `docs/features/concise-plugin-text/06-results.md` | 측정 결과 | 0~6 |
| `CHANGELOG.md`(Unreleased), 이 문서의 Deviations(계획과 달라진 점만) | 기록 | 6 |

## Phase 0: 기준선 기록

**Files:** Create: `06-results.md`(feature README에 항목 추가). eval 원본 출력은 `evals/results/`(git-ignored)
- [x] Step 1: `claude plugin list`의 unknowns 상태를 06-results에 기록(복구 기준)
- [x] Step 2: `python -m unittest discover -s tests -v` → 통과 수 기록
- [x] Step 3: `python evals/run-manual.py --verify` → exit 0
- [x] Step 4: eval 실행 규칙대로 `python evals/run-manual.py --case 'behavior-*' --runs 3 --arm with` → grader별 통과율 기록
- [x] Step 5: `behavior-blindspot-*` 6회의 `llm` rubric 2개(`ends-with-a-pasteable-prompt`, `claims-nothing-confirmed-unseen`)를 `summary.md`에서 손으로 채점해 기록

## Phase 0.5: caveman-compress 파일럿 (blindspot 본문)

**Files:** Modify: `skills/blindspot/SKILL.md` 본문. 설계와 통과 조건: 01-discovery "파일럿 설계"
- [x] Step 1: 원본을 scratchpad로 복사, caveman-compress 디렉터리(`~/.claude/plugins/marketplaces/caveman/plugins/caveman/skills/caveman-compress/`)에서 `CAVEMAN_COMPRESS_MODEL=claude-sonnet-5-5 python3 -m scripts <사본 절대경로>`. 모델 ID와 caveman 검증 결과 기록
- [x] Step 2: caveman 출력과 원본의 diff에서 "남긴다"에 걸리는 삭제를 모두 06-results에 적는다
- [x] Step 3: caveman 출력을 편집 규칙대로 문법이 온전한 짧은 영어 문장으로 다시 쓰고, Step 2의 삭제는 되살려 `skills/blindspot/SKILL.md`에 적용
- [x] Step 4: Proof 1·2·3, reviewer 누락 확인, eval 실행 규칙대로 `--case 'behavior-blindspot-*' --runs 3`, `llm` rubric 2개 손 채점
- [x] Step 5: 통과 → 원본 대비 diff와 Step 2 목록을 보여 주고 Phase 1~3에 파이프라인을 쓸지 사용자에게 묻는다. 실패 → `git checkout -- skills/blindspot/SKILL.md`, Phase 1~3은 직접 편집. 어느 쪽이든 Step 2 목록 중 "남긴다"에 없는 항목을 편집 규칙에 추가
- [x] ~~Step 6: 통과했으면 Commit `docs(blindspot): tighten skill body (caveman pilot)`~~ (파일럿 실패, Deviations 참고)

## Phase 1: agents 본문

**Files:** Modify: `agents/unknowns-scout.md`, `agents/independent-reviewer.md` 본문
- [x] Step 1: Phase 0.5에서 파이프라인을 채택했으면 그 방식으로, 아니면 직접 편집. scout의 출력 표 열, status 정의, "Never invent findings", packet이 반환 형태를 바꾼다는 단락은 남긴다. `agents/unknowns-scout.md:30` 표 구분행은 칸마다 `---`
- [x] Step 2: Proof 1·2
- [x] Step 3: Commit `docs(agents): tighten agent instructions`

## Phase 2: skill 본문

**Files:** Modify: 파일 맵 Phase 2 행 SKILL.md 본문(Phase 0.5가 통과했으면 blindspot 제외 9개)
- [ ] Step 1: 파일마다 편집(파이프라인은 채택했을 때만)
- [ ] Step 2: Proof 1·2·3
- [ ] Step 3: reviewer(켜진 상태)에 `git diff HEAD -- skills`를 주고 삭제된 지시·숫자·용어·조건만 묻는다. 지적된 것은 되살린다
- [ ] Step 4: Commit `docs(skills): tighten skill bodies`

## Phase 3: loop와 references

**Files:** Modify: `skills/loop/SKILL.md`, `skills/loop/references/*.md`
- [ ] Step 1: 편집(파이프라인은 채택했을 때만). stage 순서, tier별 분기, checkpoint 접기, `.unknowns/loop.json` 필드, references끼리 "in this folder"로 부르는 문장은 남긴다. `skills/loop/references/scorecard.md:40` 템플릿 구분행은 칸마다 `---`
- [ ] Step 2: Proof 1·2·3 (`test_bundled_references_bring_the_siblings_they_name` 포함)
- [ ] Step 3: Phase 2 Step 3과 같은 reviewer 확인
- [ ] Step 4: Commit `docs(loop): tighten loop and its references`

## Phase 3.5: description

**Files:** Modify: 11개 SKILL.md와 2개 agent의 `description:`, `docs/trigger-matrix.md`의 description 인용. Test: `tests/test_trigger_containment.py`, `tests/test_skill_descriptions.py`
- [ ] Step 1: description 규칙: README "Auto-triggers:"의 영어 따옴표 문구, `evals/trigger-*` 케이스가 선언한 문구, 반대 조건("Not for", "Do NOT"), blindspot의 "run it even when you could answer directly"(0.7.1에서 발화율 3/8 → 6/6)는 남긴다. agent는 발화 eval 케이스가 없으므로 트리거 문구(`Triggers: ...`, "Use proactively ..." 문장)를 그대로 두고 나머지 문장만 다듬는다(사용자 결정 B). agent는 reviewer 확인만 한다
- [ ] Step 2: 편집. `scripts/skill-descriptions.json`(zip용 짧은 설명)은 바꾸지 않는다
- [ ] Step 3: Proof 1·2·3. `--verify`가 trigger 케이스 문구가 description에 남았는지 본다
- [ ] Step 4: eval 실행 규칙대로(Sonnet 5.5) description을 바꾼 skill의 `trigger-*`·`neg-*` 케이스 × 3회. 통과: trigger 케이스는 3회 중 2회 이상 발화, neg 케이스는 0회 발화. 통과하지 못한 skill은 description을 이전 문구로 되돌리고 다시 잰다
- [ ] Step 5: `docs/trigger-matrix.md`의 description 인용 갱신
- [ ] Step 6: Commit `docs(skills): tighten skill and agent descriptions`

## Phase 4: hook 메시지와 manifest 설명

**Files:** Modify: 파일 맵 Phase 4 행. Test: `tests/test_impl_notes_reminder.py`, `tests/test_agent_readonly_guard.py`, `tests/test_manifest_limits.py`
- [ ] Step 1: 테스트가 고정한 부분 문자열 유지: `[unknowns]`, `[unknowns] hooks active`, `reached %d`, `IMPLEMENTATION_NOTES.md.`, `was not updated`, `/unknowns:notes init`, `A loop is in progress`, `arrives at`, `read-only`, `report the needed change`, `unknowns-scout`, `independent-reviewer`
- [ ] Step 2: 메시지 문자열과 `description` 값만 수정. 포맷 인자(`%d`, `%s`) 개수는 그대로
- [ ] Step 3: Proof 2. plugin.json description은 81~500자, "unknowns" 포함
- [ ] Step 4: Commit `docs(hooks): shorten hook and manifest text`

## Phase 5: README

**Files:** Modify: `README.md`, `README.ko.md`(표 구분행만). Test: `tests/test_readme_parity.py`, `tests/test_trigger_containment.py`, `tests/test_skill_descriptions.py`
- [ ] Step 1: heading·fence·table row 수, URL, `/unknowns:` 명령, `UNKNOWNS_*`, "Auto-triggers:" 블록의 따옴표 문구는 그대로 두고 산문만 다듬는다. 구분행 `README.md:73`, `:603`, `README.ko.md:66`, `:551`은 칸마다 `---`
- [ ] Step 2: 위 세 테스트 → 통과
- [ ] Step 3: Commit `docs(readme): tighten README prose`

## Phase 6: 재측정과 기록

**Files:** Modify: `CHANGELOG.md`, `06-results.md`, 이 문서
- [ ] Step 1: Phase 0 Step 2·3·4(`behavior-*` 전체)·5를 다시 실행. trigger·neg는 Phase 3.5 Step 4 결과를 쓴다
- [ ] Step 2: 06-results에서 grader별 비교. 회귀는 해당 skill의 바뀐 문장을 이전 문구로 되돌리고 그 케이스만 다시 잰다
- [ ] Step 3: `CHANGELOG.md` Unreleased에 항목 하나(대상 파일, eval 비교 결과). 버전 bump와 release는 하지 않는다
- [ ] Step 4: Deviations 기록, 모든 체크박스가 찼으면 `status: complete`. `claude plugin list`의 unknowns 상태가 Phase 0 Step 1 기록과 같은지 확인
- [ ] Step 5: Commit `docs: record concise-plugin-text results`

## Risks

- **가장 위험한 단계는 Phase 3.5.** description은 발화를 직접 정한다. 0.7.1에서 한 문장이 blindspot 발화율을 3/8에서 6/6으로 바꿨다. 짧아진 description이 너무 넓어지면 neg 케이스가 잡고, 좁아지면 trigger 케이스가 잡는다. 기준선이 없고 n=3이라, 발화율이 3/3에서 2/3으로 떨어지는 정도의 변화는 통과로 본다.
- Phase 3: loop 본문이 가장 길고 다른 파일을 가장 많이 참조하는데, 경로 B로 기계 채점되는 loop behavior eval이 없다. reviewer 확인에 기대는 비중이 크다.
- 산문 축약이 행동을 바꾼 전례: #4에서 prototypes 5단계를 줄이자 saturation check가 5/5에서 3/6으로 떨어졌다. 정지 조건·되묻기 조건 문장이 가장 깨지기 쉽다.
- caveman이 지운 규칙을 Phase 0.5 Step 3에서 놓칠 수 있다(caveman 프롬프트·검증기 모두 지시·숫자·용어를 보지 않음). Step 2 목록과 reviewer로 막는다.
- hook 메시지의 포맷 인자 개수가 틀어질 수 있다(Phase 4 Step 2).

## Alternatives not taken

- 본문과 description을 한 커밋으로: 발화가 바뀌었을 때 원인을 가를 수 없다.
- 파일별 규칙 목록 문서를 먼저 만들어 대조: 비용이 크다. reviewer에 diff를 주는 방식으로 대신한다.
- `scripts/skill-descriptions.json` 함께 수정: intent의 대상 파일 목록에 없다.

## Proof

1. description 외 frontmatter 불변:
   `fm() { awk '/^---$/{n++; print; if(n==2) exit; next} /^description:/{s=1; next} s && /^[^ ]/{s=0} !s{print}'; }; for f in skills/*/SKILL.md agents/*.md; do diff <(git show main:$f | fm) <(fm < $f) >/dev/null || echo "CHANGED $f"; done` → 출력 없음
2. `python -m unittest discover -s tests -v` → `OK`, Phase 0과 같은 테스트 수
3. `python evals/run-manual.py --verify` → exit 0
4. `claude plugin validate . --strict`, `claude plugin validate ./.claude-plugin/plugin.json --strict` → 둘 다 통과
5. Phase 3.5 Step 4: 바꾼 skill의 trigger 케이스 모두 2/3 이상 발화, neg 케이스 0/3. Phase 6 Step 2: 회귀로 판정된 behavior grader 0개
6. 표 구분행: `grep -nE '^\s*\|[ :|-]*-{4,}' skills/*/SKILL.md skills/loop/references/*.md agents/*.md README.md README.ko.md CHANGELOG.md` → 출력 없음

## Deviations

- Phase 0 Step 1 / eval 실행 규칙: `claude plugin disable unknowns`는 "not found in any editable settings scope"로 실패한다. synced 설치본은 `claude plugin disable unknowns@synced`, `claude plugin enable unknowns@synced`로 끄고 켰다.
- Phase 0 Step 4: `behavior-*`는 5케이스가 아니라 6케이스(`--list`)여서 18회를 돌렸다.
- Phase 0.5 Step 4: 기계 grader 차이가 1회라 "6회로 판단" 규칙을 적용하면서, 기준선도 원본 파일로 3회 더 돌려 6회 대 6회로 비교했다(규칙이 기준선 추가 실행을 정하지 않았다).
- Phase 0.5: 파일럿 실패(`labels-the-prompt-draft` 3/6 → 0/6). reviewer 확인은 eval 실패가 먼저 확정되어 돌리지 않았다. Step 6 커밋은 하지 않고 `git checkout`으로 되돌렸다. Phase 1~3은 직접 편집. 근거: 06-results "Phase 0.5".
- 편집 규칙: Step 2 삭제 목록은 비었고(caveman은 기능어만 지웠다), 대신 회귀에서 나온 "결과물·최종 목표 문장은 남긴다"를 "남긴다"에 추가했다.
