# 트리거 × 스킬 매트릭스 (0.13.0 description, 2026-11-13 — 0.13.1·0.13.2에서 description 변경 없음)

각 `skills/<name>/SKILL.md`의 frontmatter `description` 안에 큰따옴표로 들어 있는 문구
**전부**와, 스킬 간 충돌 지점 및 해소 상태.

## 0.5.1 — 한국어 문구는 이 표에서 빠졌다

`description`은 이제 **영어 전용**이다. 한국어 트리거가 사라진 것이 아니라, 보증 방식이
바뀌었다.

- **영어 문구**: `description`에 적혀 있어야 한다. 매칭 근거가 그 텍스트다.
- **한국어 문구**: `description`에 없다. 대신 `evals/trigger-ko-*` 케이스가 실제로 발화하는지
  측정한다. `tests/test_trigger_containment.py`가 "한국어 문구를 광고하는 스킬은 그 문구를
  쓰는 eval 케이스를 가져야 한다"를 강제한다.

근거: 같은 한국어 프롬프트를 한국어 있는 설명문과 영어 전용 설명문에 각각 돌린 A/B에서
발화율 차이가 없었다. 한국어 문구는 글자로는 5%(4,001자 중 221자)인데 항상 로딩 토큰의
22%(1,698 중 381)를 차지했다. 측정 모델은 기본 모델이며 **sonnet 이상 기준**이다.
한계: 스킬당 대표 문구 1개만 실측했다(광고 문구는 28개).

한국어 문구 목록 자체는 `README.ko.md`의 각 스킬 절이 계속 유지한다.

구버전 문서는 `description`·`argument-hint`·역트리거를 한 목록에 섞어 놓고 "전수"라고
불렀는데 실제로는 일부 문구가 빠져 있었다. 이 판은 셋을 분리한다:

- **트리거 문구** — `description`의 따옴표 안 문구. 아래 표에 한 개도 빼지 않고 싣는다.
- **역트리거·경계** — 같은 `description`에 있지만 발화를 *막는* 문장. 별도 열.
- **`argument-hint`** — 0.10.0부터 어느 스킬에도 없다(`tests/test_portability.py`가 설치본에서 금지한다).

## 갱신 방법

저장소 루트에서 아래를 돌리고, 출력 그대로 표를 고친다(스크립트와 표 모두 스킬 이름
알파벳순). 괄호 안 숫자는 접힌 `description`의 글자 수이며, 0.13.0부터 스킬당 200자 이하다(`.claude/rules/skill-writing.md` 18번, 테스트가 강제).

```bash
python3 - <<'EOF'
import os, re
for name in sorted(os.listdir("skills")):
    path = os.path.join("skills", name, "SKILL.md")
    if not os.path.exists(path):
        continue
    fm = re.match(r"^---\n(.*?)\n---\n", open(path, encoding="utf-8").read(), re.DOTALL).group(1)
    keep, on = [], False
    for line in fm.split("\n"):
        if line.startswith("description:"):
            on = True
            continue
        if on:
            if line[:1].strip():          # 다음 최상위 키를 만나면 끝
                break
            keep.append(line.strip())
    desc = " ".join(keep)
    print("%-11s (%3d자) %s" % (name, len(desc), " | ".join(re.findall(r'"([^"]+)"', desc))))
EOF
```

출력에는 역트리거도 섞여 나온다(unknowns-loop의 `"loop"`). 표에서는 그것만
역트리거 열로 옮겼고, 그 밖에 옮기거나 뺀 문구는 없다.

`tests/test_trigger_containment.py`는 **README가 광고하는 문구가 description에 실제로 있는지**를
CI에서 강제한다. 반대 방향(description에만 있고 README에 없는 문구)은 검사하지 않으므로,
이 표가 그 방향의 유일한 기록이다.

## 스킬별 트리거 문구

| 스킬 | 영어 (description 내) | 한국어 (eval로 보증, README.ko.md 참조) | 역트리거·경계 | 길이 |
|------|------|--------|--------------|------|
| blindspot | blind spot pass · what am I missing | 사각지대 조사해줘 · 내가 놓친 게 뭐지 | — | 182자 |
| brainstorm | brainstorm interventions · show me options | 브레인스토밍 · 해법 후보 펼쳐줘 · 옵션 보여줘 | 디자인 변형에는 쓰지 않음("NOT for design variants.") | 192자 |
| buy-in | buy-in doc · prep me for review · get sign-off | 설득 문서 만들어줘 · 리뷰 준비 | — | 181자 |
| deviation-log | implementation notes · record a deviation · where did we diverge from the plan? | 이탈 기록 · 임플 노트 · 어디서 계획이랑 달라졌어? | — | 171자 |
| interview | interview me · ask me questions before implementing · ask me before you decide | 인터뷰해줘 · 스펙 질문 | — | 198자 |
| prototypes | divergent prototypes · design options · versions to react to · know it when I see it | 시안 4개 · 프로토타입 여러 개 · 보면 안다 | — | 184자 |
| quiz | quiz me · test my understanding | 퀴즈 · 내가 이해했는지 확인해줘 | — | 188자 |
| reference | use this as a reference · make it like this | 레퍼런스로 써 · 이 코드처럼 만들어줘 · 이거 참고해서 | — | 194자 |
| teach-me | teach me · make me an explainer | 가르쳐줘 · 설명서 만들어줘 · 이 분야 용어를 모르겠어 | 계획 조사가 아님("Not a plan investigation.") | 181자 |
| tweakable-plan | plan this · make a plan · tweakable plan | 계획 세워줘 · 구현 계획 · 수정확률순으로 계획 | — | 150자 |
| unknowns-loop | unknowns loop · run the operating loop · know your unknowns | 운영 루프로 진행 · 풀 루프로 해줘 | **"loop"** — 맥락 없는 "loop"는 이 스킬이 아님 | 176자 |

0.13.0 (2026-11-13): description은 짧은 세트로, 스킬마다 200자 이하다(소유자 결정 2026-11-12, `.claude/rules/skill-writing.md` 18번). 합계 1,997자, 475토큰(cl100k)으로, 이전의 4,318자·949토큰에서 줄었고 위 표를 갱신했다. 끝 문장 "Clear to both sides: no skill or method."와 방법 요약은 모든 description에서 빠졌고, 되읽기는 본문에 남았다. description에서 빠진 따옴표 문구: blindspot의 "unknown unknowns"(단어는 따옴표 없이 남았다). description에서 빠진 경계·범위 절: blindspot의 "run it even when you could answer directly", tweakable-plan의 "Not native plan mode" 문장(크기 게이트는 본문에 남았다), blindspot·brainstorm·buy-in·interview·reference·teach-me의 상황 절("or when …", "or before …"). 짧게 남은 것: prototypes의 "know it when I see it"(따옴표 문구), quiz의 "or before merging", teach-me의 경계 "Not a plan investigation.", quiz와 reference의 "runs even when …" 절. 짧은 세트를 넣은 빌드에서 케이스당 1회 쟀다: 의도한 스킬이 트리거 케이스 22/22, 비코딩 케이스 22/22에서 떴다(`CHANGELOG.md` 0.13.0).

**따옴표 밖 문구 주의**: teach-me의 description은 `Teach me my unknowns — …`로 시작한다.
따옴표 트리거는 아니지만 문자열로는 description 안에 있으므로, README가
"teach me my unknowns"를 광고해도 containment 테스트는 통과한다. 위 표에는 따옴표 문구만 실었다.

## 충돌 지점과 해소 상태

| # | 충돌 쌍 | 상태 (0.13.0 description 기준) |
|---|---------|-------------------|
| 1 | brainstorm "show me options" vs prototypes "design options" | **유지.** 경계 문장은 brainstorm 쪽에만 한 방향으로 둔다("NOT for design variants."). prototypes에는 반대 방향 문장을 넣지 않았다 — 양쪽에 넣으면 두 description 모두 예산을 쓰면서 같은 경계를 두 번 말하게 된다 |
| 2 | blindspot vs teach-me ("my unknowns" 계열) | **문구 충돌 해소.** blindspot에서 "find my unknowns"가 삭제됐다. teach-me의 구분 문장은 0.13.0에서 "Not a plan investigation."으로 짧아져 남았다 — description 첫머리가 여전히 "Teach me my unknowns"이기 때문 |
| 3 | tweakable-plan "plan this" · "계획 세워줘" (범용 문구) vs native plan mode | **유지 — 경계는 본문에.** 0.13.0부터 description에 native plan mode 경계 문장이 없다(`.claude/rules/skill-writing.md` 18번). 본문 3단계 크기 게이트가 처리한다: 사용자가 바꾸고 싶어 할 결정이 없는 작업(코드면 예: 2파일 이하, 스키마·인터페이스·UX 계약 결정 없음)에는 문서를 쓰지 않고 2단계의 첫 줄과 질문, 실행 순서 단계만 답한다(코드면 native plan mode가 맞다고 말한다). 측정: `neg-one-file-tweakable-plan-defers-to-plan-mode`의 판사 그레이더 `defers-to-plan-mode` 0.13.0 1/1, 0.13.1 표 형식에서 저장된 응답 재채점 4/4(`CHANGELOG.md` 0.13.1) |
| 4 | unknowns-loop "know your unknowns" = 플러그인 이름, 맥락 없는 "loop" | **유지.** 0.12.0에서 `loop`를 `unknowns-loop`로 바꿔 맨 이름 `loop`는 Claude Code 내장 인터벌 러너에 넘겼고, description 끝의 역트리거("A bare "loop" is NOT this.")가 남아 있다. 0.4.0에서 legacy 별칭 "field guide"/"필드 가이드"가 삭제됐다. 측정: 0.13.0 인터벌 케이스는 내장 `loop`를 띄웠다(`CHANGELOG.md` 0.13.0) |
| 5 | interview "질문해줘" vs quiz "퀴즈" | **해소.** "질문해줘"가 interview description에서 삭제됐다. 남은 한국어 문구는 "인터뷰해줘"·"스펙 질문"으로, quiz와 겹치지 않는다 |
| 6 | 에이전트 independent-reviewer·unknowns-scout vs 다른 워크플로의 리뷰어·조사 에이전트(SuperClaude `/sc:review`의 `self-review`, 프로젝트 스킬의 "서브에이전트로 독립 검토", "서브에이전트로 먼저 조사") | **해소(0.9.2).** independent-reviewer는 실제 세션 두 건에서 가로챘고, scout는 실제 사례 없이 측정에서만 가로챘다. 두 description에서 "Use proactively"와 트리거 문구를 빼고 "이름으로 부르거나 unknowns 스킬이 부를 때만"으로 좁혔다. 이름 없는 리뷰 요청 30회 중 가로챔 21 → 0, 이름 없는 영어 조사 요청 20회 중 scout 가로챔 20 → 0(한국어·구조·라이브러리 조사 30회는 두 팔 모두 0), 이름 호출은 두 에이전트 모두 20/20 유지 — [features/agent-collision/](features/agent-collision/README.md). 0.12.0에서 두 description이 다시 쓰인 뒤로는 이름 없는 요청을 다시 재지 않았다(마지막 측정은 0.11.0 description으로 이름 없는 리뷰·조사 요청 18회 중 unknowns 에이전트 0회, `CHANGELOG.md` 0.11.0) |
| 7 | teach-me "teach me" (두 단어짜리 범용 영어 문구) vs 답이 정해진 how-to 요청 | **재현 안 됨.** `neg-generic-howto-does-not-fire-teach-me`(2026-09-06 신설): 답이 정해져 있고 출력 형식까지 지정된 "teach me how to center a div"에서 teach-me는 뜨지 않고 답이 바로 나왔다. 0.13.0의 네거티브 13/13에 들어 있다(`CHANGELOG.md` 0.13.0) |

## 남은 위험

- **`tweakable-plan`의 크기 게이트**: 한 파일짜리 변경 케이스(`neg-one-file-tweakable-plan-defers-to-plan-mode`)의 판사 그레이더 `defers-to-plan-mode`가 계획 문서의 부분(가능성 순 결정, 롤백, 가장 약한 부분 절)을 금지한다. 0.13.1에서 크기 게이트를 두 경우의 표로 바꾼 현재 본문은, 고친 그레이더로 저장된 응답을 다시 채점해 4회 중 4회 통과했다(새 실행이 아니라 재채점; 표 이전 본문은 격리 실행 3회 중 2회, 놓친 1회는 가장 약한 부분 절). 0.13.1·0.13.2 릴리스 점검(격리 설정, 전체 스위트 1회)의 놓친 그레이더 목록에도 이 케이스는 없다. 표본이 작아 지켜볼 칸이다. 근거: CHANGELOG 0.11.0·0.13.0·0.13.1·0.13.2 **Checked**.
- 플러그인 외부 충돌(내장 loop 스킬, 다른 플러그인의 plan 계열)은 0.12.0의 이름 변경(`loop`→`unknowns-loop`, `plan`→`tweakable-plan`)과 unknowns-loop description 끝의 역트리거로 완화했고, native plan mode와의 경계는 tweakable-plan 본문 3단계의 크기 게이트가 맡는다(`.claude/rules/skill-writing.md` 18번). 최종 판별은 여전히 호출 시점 문맥에 달려 있다.
- [trigger-eval-v0.3.0.md](trigger-eval-v0.3.0.md)의 "6/6 정발화, 오발화 0"은 **v0.3.0 시점의 긴
  description을 측정한 값**이다. 0.4.0과 0.5.1에서 description이 두 번 짧아졌으므로 그 수치는 현재
  상태의 측정치가 아니다 — 인용하지 말 것.
- 현재 description(0.13.0, 0.13.1·0.13.2에서 변경 없음)의 측정치는 `CHANGELOG.md` 0.13.0이다: Claude Opus, `--effort medium`, 케이스당 1회, 트리거 22/22, 비코딩 22/22, unknown-cell 4/4, 네거티브 13/13. 이 실행은 기계 그레이더만 채점했고, `llm` 그레이더는 같은 릴리스의 전체 점검에서 별도 판사 모델이 채점했다. GPT-6.1 Sol 트리거 22/22는 `CHANGELOG.md` 0.13.2. [trigger-eval-v0.5.1.md](trigger-eval-v0.5.1.md)는 0.5.1 description의 동결 기록이다.
