# 트리거 × 스킬 매트릭스 (v0.3.x, 2026-07-11)

frontmatter description에서 추출한 스킬별 트리거 문구 전수 + 스킬 간 충돌 지점과
해소 상태. 갱신 방법: `tests/test_trigger_containment.py`가 README ↔ frontmatter
정합을 CI에서 강제하고, 이 문서는 아래 스크립트 출력 기준으로 수동 갱신.

```bash
python3 - <<'EOF'
import os, re
for name in sorted(os.listdir("skills")):
    p = os.path.join("skills", name, "SKILL.md")
    if not os.path.exists(p): continue
    m = re.match(r"^---\n(.*?)\n---\n", open(p, encoding="utf-8").read(), re.DOTALL)
    print(name + ": " + " | ".join(re.findall(r'"([^"]+)"', re.sub(r"\s+", " ", m.group(1)))))
EOF
```

## 스킬별 트리거 문구

| 스킬 | 영어 | 한국어 |
|------|------|--------|
| blindspot | blind spot pass · blindspot · what am I missing · do a blind-spot investigation · find my unknowns · unknown unknowns | 사각지대 조사해줘 · 내가 놓친 게 뭐지 · 내가 모르는 게 뭐지 |
| teach-me | teach me · make me an explainer · I don't know the vocabulary of this field · teach me my unknowns · make it pop | 가르쳐줘 · 설명서 만들어줘 · 이 분야 용어를 모르겠어 |
| interview | interview me · ask me questions about the spec · ask me questions before implementing | 인터뷰해줘 · 질문해줘(구현 전) · 스펙 질문 |
| prototypes | divergent prototypes · design options · give me different designs · design directions · know it when I see it | 프로토타입 여러 개 · 시안 4개 · 다양한 디자인으로 보여줘 · 보면 안다 |
| brainstorm | brainstorm interventions · spread out solution candidates · lay out candidate solutions · not sure what to do · show me options | 브레인스토밍 · 해법 후보 펼쳐줘 · 뭘 해야 할지 모르겠어 · 옵션 보여줘 |
| reference | use this as a reference · use it as a reference · use this code as reference · make it like this | 레퍼런스로 써 · 이 코드처럼 만들어줘 · 이거 참고해서 · 이 코드 참고해서 · 이거랑 비슷하게 |
| plan | plan this · tweakable plan · sort plan by tweak likelihood · make a plan · plan ordered by likelihood of change | 계획 세워줘 · 구현 계획 · 수정확률순 계획 · 수정확률순으로 계획 |
| notes | implementation notes · impl notes · log deviations · record a deviation · where did we diverge from the plan? | 이탈 기록 · 임플 노트 · 어디서 계획이랑 달라졌어? |
| quiz | quiz me · give me a quiz · test my understanding · check whether I understood this | 퀴즈 · 내가 이해했는지 확인해줘 |
| buy-in | buy-in doc · prep me for review · prepare for merge approval · pitch this work | buy-in 문서 · 설득 문서 만들어줘 · 리뷰 준비 · 머지 승인 준비해줘 |
| loop | unknowns loop · know your unknowns · run the operating loop · do the full loop | 운영 루프로 진행 · 풀 루프로 해줘 |

## 충돌 지점과 해소 상태

| # | 충돌 쌍 | 위험 | 해소 |
|---|---------|------|------|
| 1 | brainstorm "show me options" vs prototypes "design options" | UI 요청이 brainstorm으로 오발화 | brainstorm에 경계 문장 추가: "NOT for choosing between UI/design variants — design options belongs to the prototypes skill" |
| 2 | blindspot "find my unknowns" vs teach-me "teach me my unknowns" | 도메인 학습 요청이 blindspot으로 | teach-me에 구분 문장 추가: blindspot=코드베이스/계획 조사, teach-me=도메인 어휘 학습 |
| 3 | plan "plan this"/"계획 세워줘" (범용 문구) | 일반 계획 요청·native plan mode 가로채기 | plan에 구분 문장: 수정확률순 사전 계획 문서 전용, plan mode/스케줄러/일반 분해는 내장 도구로 |
| 4 | loop "know your unknowns" = 플러그인 이름 | 메타 언급이 10단계 루프 발화 | loop에 경계 문장: 맥락 없는 "loop"/"루프 돌려줘"는 범용 반복 실행기로 해석 |
| 5 | interview "질문해줘" vs quiz "퀴즈" | 구현 전/후 혼동 | interview는 "(before implementation)" 한정, quiz는 사후 전용으로 이미 분리 — 문면 유지 |

플러그인 외부 충돌(내장 loop 스킬, 타 플러그인의 plan 계열)은 description 경계
문장으로 완화하되, 최종 판별은 호출 시점 문맥에 달려 있음 — 발화율 표본은
[trigger-eval-v0.3.0.md](trigger-eval-v0.3.0.md) 참조 (수정 후 6/6 정발화, 오발화 0).
