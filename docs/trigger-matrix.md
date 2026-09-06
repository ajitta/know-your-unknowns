# 트리거 × 스킬 매트릭스 (v0.4.0, 2026-09-06)

각 `skills/<name>/SKILL.md`의 frontmatter `description` 안에 큰따옴표로 들어 있는 문구
**전부**와, 스킬 간 충돌 지점 및 해소 상태.

구버전 문서는 `description`·`argument-hint`·역트리거를 한 목록에 섞어 놓고 "전수"라고
불렀는데 실제로는 일부 문구가 빠져 있었다. 이 판은 셋을 분리한다:

- **트리거 문구** — `description`의 따옴표 안 문구. 아래 표에 한 개도 빼지 않고 싣는다.
- **역트리거·경계** — 같은 `description`에 있지만 발화를 *막는* 문장. 별도 열.
- **`argument-hint`** — 트리거가 아니라 호출 후 인자 힌트. 이 표에서 제외.

## 갱신 방법

저장소 루트에서 아래를 돌리고, 출력 그대로 표를 고친다(스크립트와 표 모두 스킬 이름
알파벳순). 괄호 안 숫자는 접힌 `description`의 글자 수이며, 목표는 스킬당 약 300자 이내다.

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

출력에는 역트리거도 섞여 나온다(loop의 `"loop"` / `"루프 돌려줘"`). 표에서는 그 둘만
역트리거 열로 옮겼고, 그 밖에 옮기거나 뺀 문구는 없다.

`tests/test_trigger_containment.py`는 **README가 광고하는 문구가 description에 실제로 있는지**를
CI에서 강제한다. 반대 방향(description에만 있고 README에 없는 문구)은 검사하지 않으므로,
이 표가 그 방향의 유일한 기록이다.

## 스킬별 트리거 문구

| 스킬 | 영어 | 한국어 | 역트리거·경계 | 길이 |
|------|------|--------|--------------|------|
| blindspot | blind spot pass · what am I missing · unknown unknowns | 사각지대 조사해줘 · 내가 놓친 게 뭐지 | 일상적·이미 잘 아는 작업에는 쓰지 않음(따옴표 없는 문장) | 301자 |
| brainstorm | brainstorm interventions · show me options | 브레인스토밍 · 해법 후보 펼쳐줘 · 옵션 보여줘 | UI/디자인 변형은 prototypes로 | 291자 |
| buy-in | buy-in doc · prep me for review | 설득 문서 만들어줘 · 리뷰 준비 | — | 293자 |
| interview | interview me · ask me questions before implementing | 인터뷰해줘 · 스펙 질문 | — | 301자 |
| loop | unknowns loop · run the operating loop · know your unknowns | 운영 루프로 진행 · 풀 루프로 해줘 | **"loop" · "루프 돌려줘"** — 맥락 없는 이 둘은 내장 인터벌 러너 | 292자 |
| notes | implementation notes · record a deviation · where did we diverge from the plan? | 이탈 기록 · 임플 노트 · 어디서 계획이랑 달라졌어? | — | 284자 |
| plan | plan this · make a plan · tweakable plan | 계획 세워줘 · 구현 계획 · 수정확률순으로 계획 | native plan mode가 아니라 검토용 사전 문서를 쓰는 스킬 | 292자 |
| prototypes | divergent prototypes · design options · know it when I see it | 시안 4개 · 프로토타입 여러 개 · 보면 안다 | — | 298자 |
| quiz | quiz me · test my understanding | 퀴즈 · 내가 이해했는지 확인해줘 | — | 285자 |
| reference | use this as a reference · make it like this | 레퍼런스로 써 · 이 코드처럼 만들어줘 · 이거 참고해서 | — | 297자 |
| teach-me | teach me · make me an explainer | 가르쳐줘 · 설명서 만들어줘 · 이 분야 용어를 모르겠어 | blindspot=코드베이스 조사, teach-me=도메인 어휘 | 314자 |

합계 3,248자. teach-me만 300자를 넘는데(314자), 넘긴 몫이 teach-me↔blindspot 경계 문장과
세 번째 한국어 문구다 — 더 줄이면 둘 중 하나를 잃는다.

**따옴표 밖 문구 주의**: teach-me의 description은 `Teach me my unknowns — …`로 시작한다.
따옴표 트리거는 아니지만 문자열로는 description 안에 있으므로, README가
"teach me my unknowns"를 광고해도 containment 테스트는 통과한다. 위 표에는 따옴표 문구만 실었다.

## 충돌 지점과 해소 상태

| # | 충돌 쌍 | 상태 (2026-09-06) |
|---|---------|-------------------|
| 1 | brainstorm "show me options" vs prototypes "design options" | **유지.** 경계 문장은 brainstorm 쪽에만 한 방향으로 둔다("UI/디자인 변형은 prototypes"). prototypes에는 반대 방향 문장을 넣지 않았다 — 양쪽에 넣으면 두 description 모두 예산을 쓰면서 같은 경계를 두 번 말하게 된다 |
| 2 | blindspot vs teach-me ("my unknowns" 계열) | **문구 충돌 해소.** blindspot에서 "find my unknowns"가 삭제됐다. teach-me의 구분 문장은 그대로 두었다 — description 첫머리가 여전히 "Teach me my unknowns"이기 때문 |
| 3 | plan "plan this" · "계획 세워줘" (범용 문구) | **유지.** description의 경계 문장에 더해, 본문에 크기 게이트가 생겼다(2파일 이하 + 스키마·인터페이스·UX 계약 결정 없음 → 문서를 쓰지 않고 native plan mode로 넘긴다). 과발화 여부는 여전히 **미측정** — [open-questions.md](open-questions.md) B5 |
| 4 | loop "know your unknowns" = 플러그인 이름 | **유지.** 맥락 없는 "loop"/"루프 돌려줘"를 내장 인터벌 러너로 넘기는 역트리거로 완화. 0.4.0에서 legacy 별칭 "field guide"/"필드 가이드"가 삭제돼 표면이 더 좁아졌다 |
| 5 | interview "질문해줘" vs quiz "퀴즈" | **해소.** "질문해줘"가 interview description에서 삭제됐다. 남은 한국어 문구는 "인터뷰해줘"·"스펙 질문"으로, quiz와 겹치지 않는다 |

## 남은 위험

- **`teach me`는 두 단어짜리 범용 영어 문구**다. 도메인 어휘와 무관한 "teach me how to X" 요청까지
  잡을 수 있고, 이 방향은 측정된 적이 없다. plan의 과발화와 함께 B5에서 같이 잰다.
- 플러그인 외부 충돌(내장 loop 스킬, 다른 플러그인의 plan 계열)은 description 경계 문장으로만
  완화 가능하며, 최종 판별은 호출 시점 문맥에 달려 있다.
- [trigger-eval-v0.3.0.md](trigger-eval-v0.3.0.md)의 "6/6 정발화, 오발화 0"은 **v0.3.0 시점의 긴
  description을 측정한 값**이다. 0.4.0에서 11개 description이 전부 짧아졌으므로 그 수치는 현재
  상태의 측정치가 아니다 — 재측정 전까지 인용하지 말 것.
