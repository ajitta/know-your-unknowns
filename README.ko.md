# know-your-unknowns

**Language**: [English](README.md) | 한국어

> 지도는 영토가 아니다 — 그 간극이 당신의 unknowns다.

**강한 모델의 병목은 모델이 아니라, 지도(계획)와 영토(실제 코드·도메인·제약)를 일치시키는
당신의 능력이다.** 이 플러그인은 그 간극을 구현 전·중·후에 걸쳐 찾고 관리하는 운영 루프를
제공합니다 — 스킬 11종, 에이전트 2종, 훅 2종.

구체적으로 얻는 것:

- 몰랐던 것을 PR 이후가 아니라 **프롬프트를 쓰기 전에** 발견합니다.
- 보고 반응해야 하는 산출물은 **반응을 구조화된 답변으로 조립해 주는 단일 파일 인터랙티브
  페이지**로 나옵니다 — 문단을 쓰는 것보다 칩을 누르는 편이 빠릅니다. 뷰어가 없는
  환경에서는 마크다운으로 폴백합니다.
- 계획 이탈은 아직 값이 쌀 때 기록되고, 세션이 표류하면 훅이 찔러 줍니다.

Thariq Shihipar(Anthropic, Claude Code 팀)의 방법론을 패키징했습니다. 두 자료가 원 출처입니다:
강연 **"Field Guide to Fable"**(AI Engineer World's Fair 2026 키노트)과 예시 모음
**"Know your unknowns"**(11개 인터랙티브 예시) —
https://thariqs.github.io/html-effectiveness/unknowns/. 스킬 11종이 원문 11개 예시를 모두
커버합니다(prototypes가 2개를 커버, loop는 원문 대응이 없는 오케스트레이터). 사실검증
상세는 `skills/loop/references/talk-source.md` 참조.

---

## 빠른 시작

Claude Code 세션 안에서 마켓플레이스로 설치합니다:

```
/plugin marketplace add ajitta/claude-plugins
/plugin install unknowns@ajitta
```

새 세션을 시작하거나 `/reload-plugins` 후, 로드되었는지 확인합니다:

```
/unknowns:blindspot 테스트
```

스킬이 "아직 구현하지 마라" 원칙과 조사 절차로 응답하면 정상입니다. 그다음부터는:

- 크고 낯선 작업 → `/unknowns:loop <작업 설명>` 하나면 됩니다. 나머지는 Claude가 단계별로
  끌고 갑니다.
- 특정 기법만 필요 → 해당 스킬을 직접 호출하거나, 자연어로 말하면 자동 트리거됩니다.
- 슬래시 없이도 동작: "사각지대 조사해줘", "인터뷰해줘", "시안 4개", "퀴즈" 같은 말이 곧
  트리거입니다.

나머지 설치 경로(클론·개별 복사·Cowork)는 아래 [설치](#설치)에 있습니다.

---

## 스킬 한눈에 보기

원문 11개 예시 커버 — prototypes가 2개 커버, loop는 오케스트레이터.

| 시점 | 스킬 | 하는 일 | 원문 예시 |
|------|------|---------|-----------|
| 전 | `blindspot` | 사각지대 조사 → 개선된 프롬프트 | Blindspot Pass |
| 전 | `teach-me` | 도메인 어휘 설명서 → 정밀한 요청 | Teach Me My Unknowns |
| 전 | `interview` | 모델이 사용자를 인터뷰 → 결정 테이블 | The Interview |
| 전 | `prototypes` | 철학이 다른 시안 N개 → 요구사항 조립 | Four Design Directions / Mock |
| 전 | `brainstorm` | 해법 공간 지도 → 개입 선택 | Brainstorm the Intervention |
| 전 | `reference` | 레퍼런스 분석·이해 증명 | Point at a Reference |
| 전 | `plan` | 수정확률순 계획서 | The Tweakable Plan |
| 중 | `notes` | 계획 이탈 기록 | Implementation Notes |
| 후 | `quiz` | 이해도 퀴즈·인수인계 | Quiz Me Before I Merge |
| 후 | `buy-in` | 리뷰어 설득 문서 | The Buy-In Doc |
| 전체 | `loop` | 위 전부를 꿰는 운영 루프 | — |

---

## 설치

플러그인 이름은 `unknowns`입니다 (호출: `/unknowns:<스킬>`).

### 마켓플레이스 (권장)

위 [빠른 시작](#빠른-시작)의 두 줄이 전부입니다. 마켓플레이스는 카탈로그 저장소
[ajitta/claude-plugins](https://github.com/ajitta/claude-plugins)이고, 이 플러그인을
목록에 올린 뒤 여기를 가리킵니다 — 따라서 `/plugin install unknowns@ajitta`는 이 저장소의
`plugin.json`이 선언한 버전으로 설치합니다. 이 프로젝트가 실제로 검증하는 유일한 경로입니다.

### 클론에서 바로 실행

릴리스 전 브랜치를 시험하거나 플러그인 자체를 손볼 때:

```bash
git clone https://github.com/ajitta/know-your-unknowns.git
claude --plugin-dir ./know-your-unknowns
```

해당 세션에만 로드됩니다. 세션 안에서 `/unknowns:loop` 등이 보이면 성공입니다.
(`--plugin-dir`는 `.zip` 아카이브도 받습니다.)

### 스킬만 골라서 복사 (플러그인 없이)

특정 스킬만 원하면 `skills/<이름>` 폴더를 볼트나 프로젝트의 `.claude/skills/`에,
`agents/*.md`를 `.claude/agents/`에 복사합니다. `skills/loop/references/`도 함께
복사하세요 — 대부분의 스킬이 `skills/loop/references/output-routing.md`와
`talk-source.md`를 가리키는데, 이 경로는 플러그인 루트 기준으로 해석되므로 스킬 폴더만
복사하면 없는 파일을 가리키게 됩니다. 이 경우 호출명은 네임스페이스 없이
`/blindspot`, `/quiz`처럼 짧아집니다. 훅은 플러그인 형태일 때만 자동 활성화되므로,
수동 설정은 [훅 동작과 설정](#훅-동작과-설정)을 참고하세요.

### Cowork / Claude Desktop

채팅으로 `unknowns` 플러그인 카드를 받았다면 그 설치 버튼이 가장 빠릅니다. 그렇지 않다면
문서화된 경로는 **Customize → Plugins → 플러그인 파일 업로드**이고, 이렇게 추가한
플러그인은 내 컴퓨터에 로컬로 저장됩니다. 이 레포는 빌드된 플러그인 파일을 배포하지
않으며(`scripts/build-plugin.sh`가 릴리스 태그에서 만듭니다), 두 경로 모두 이 프로젝트가
직접 확인한 적이 없으므로 데스크톱 경로는 미검증으로 보세요. 리마인더 훅은 그 환경의
PATH에 `python3`가 있어야 하는데, 이 역시 미검증입니다.

### 업데이트

```
/plugin marketplace update ajitta
/plugin update unknowns@ajitta
/reload-plugins
```

업데이트는 플러그인 버전 번호가 바뀔 때만 도착합니다. 서드파티 마켓플레이스는 자동
업데이트가 기본 꺼짐이므로, 손으로 돌리기 싫다면 `/plugin` → Marketplaces에서 `ajitta`에
대해 켜 두세요.

### 0.1.x(field-guide)에서 업그레이드

0.1.x는 `field-guide`라는 이름으로 배포되었습니다. 이름이 바뀌었으므로 제거 후 재설치합니다:

```
/plugin uninstall field-guide@ajitta
/plugin marketplace update ajitta
/plugin install unknowns@ajitta
```

GitHub 레포 리네임으로 옛 URL(`ajitta/field-guide`)은 자동 리다이렉트됩니다. 스킬 대응:
`reference-map`→`reference`, `impl-notes`→`notes`, 나머지는 이름 동일. 환경변수
`FIELD_GUIDE_NOTES_THRESHOLD`는 계속 인식하지만 `UNKNOWNS_NOTES_THRESHOLD` 사용을
권장합니다.

---

## 스킬별 상세 사용법

### 1. `/unknowns:loop` — 전체 운영 루프

**언제**: 크거나 낯선 기능 개발, 스펙이 흐릿한 작업, "제대로 각 잡고" 진행하고 싶을 때.

**호출**:
```
/unknowns:loop 결제 모듈에 구독 갱신 기능 추가
```
자동 트리거 문구: "unknowns loop", "run the operating loop", "know your unknowns",
"운영 루프로 진행", "풀 루프로 해줘"

맨 `/loop`는 이 스킬이 아니라 Claude Code 내장 인터벌 러너입니다 — 항상
`/unknowns:loop`로 부르세요. 대화 중의 맨 "loop"나 "루프 돌려줘"도 마찬가지입니다.

**진행 방식**: Claude가 10단계를 순서대로 끌고 갑니다 —
① 가치·완료 조건 정의(사용자와 합의) → ② blindspot 조사(+필요시 teach-me) →
③ 인터뷰 → ④ 해법·형태 탐색(brainstorm/prototypes/reference, 필요시) →
⑤ 위험 가정 최소 검증 → ⑥ 수정확률순 계획(plan) → ⑦ 구현 + 이탈 기록(notes) →
⑧ 독립 검증 → ⑨ 퀴즈·인수인계(+필요시 buy-in) → ⑩ 가치 검토.

**세 단계 규모**: 작은 수정(파일 1–2개, 명확한 스펙)은 루프 자체가 불필요하고 ⑦의 notes
규칙만 적용됩니다. 중간 작업은 ① → ② → ③ → ⑥ → ⑦ → ⑨. 크거나 낯선 작업은 전체를 돌되
④·⑤는 필요할 때만. ①은 모든 규모에서 실행됩니다. 규모를 말해주면 알아서 고릅니다:
```
/unknowns:loop 이건 중간 규모야. 버그 수정인데 원인이 애매함
```

**진행 상태 유지**: 루프는 `.unknowns/loop.json` 트래커(작업·규모·단계·결정·산출물)를
단계 경계마다 다시 씁니다. 그래서 컴팩션, `/resume`, 새 세션을 넘어 살아남습니다.
`/unknowns:loop status`는 규모·현재 단계·남은 단계를 보고하고,
`/unknowns:loop resume`은 멈춘 지점에서 이어갑니다.

---

### 2. `/unknowns:blindspot` — 구현 전 사각지대 조사

**언제**: 잘 모르는 모듈·라이브러리·도메인을 건드리기 전. "내가 뭘 모르는지 모르는" 상태일 때.

**호출**:
```
/unknowns:blindspot 인증 모듈에 카카오 OAuth 추가. git 히스토리랑 tests/ 위주로 봐줘
```
자동 트리거: "blind spot pass", "what am I missing", "unknown unknowns",
"사각지대 조사해줘", "내가 놓친 게 뭐지"

**진행 방식**: 코드를 **수정하지 않고** 조사만 합니다. 범위가 코드베이스 전체거나 크면
`unknowns:unknowns-scout` 에이전트에 위임합니다. 먼저 대비를 보여줍니다 — 내가 요청한 것
vs 실제로 들어가는 곳, 종류별 집계와 함께. 그다음 발견 1건 = 카드 1장을 중요도×영향도
순으로, 종류를 달아서: **지뢰**(건드리면 티 안 나게 뭔가 깨짐), **관례**(코드베이스가
강제하는 암묵 규칙), **없는 개념**(내 프롬프트에 단어가 없는 메커니즘),
**이력**(이 작업의 이전 시도 또는 되돌려진 시도).

**핵심 산출물**: 카드의 "프롬프트 픽스"들이 조립된 **개선된 프롬프트 초안**. 실행 순서를
명시하고 명시적 체크포인트로 끝납니다. 이걸 복사해서 실제 구현 지시로 쓰는 것이 이 스킬의
목적입니다.

**팁**: 코드가 아니어도 됩니다. `"영상 색보정을 처음 해보는데 blind spot pass 해줘"`처럼
새 분야에도 적용됩니다 — 용어 자체를 배워야 하면 아래 teach-me가 더 맞습니다.

---

### 3. `/unknowns:teach-me` — 도메인 어휘 설명서

**언제**: "더 좋게 해줘"밖에 말할 수 없을 때. 그 분야의 용어를 몰라 요청이 모호해질 때.

**호출**:
```
/unknowns:teach-me 영상 색보정. 나 완전 초보
```
자동 트리거: "teach me", "make me an explainer", "가르쳐줘", "설명서 만들어줘",
"이 분야 용어를 모르겠어"

**진행 방식**: 그 도메인의 멘탈 모델을 3–5단계 파이프라인으로 → 이 작업에서 내리게 될 결정
축 3–7개 → 축마다 어휘 사다리(일상어→전문어, 용어별 요청 예문) → 개념별 before/after 비교,
그리고 룩 전체를 한 번에 느낄 수 있는 이름 붙은 프리셋 2–3개 → 새 어휘로 서술된 "잘된
것의 기준" 4–6개 → 마지막에 **원래 요청을 새 어휘로 다시 쓴 정밀 요청 초안**.

---

### 4. `/unknowns:interview` — 구현 전 인터뷰

**언제**: 스펙이 불완전한데 뭘 물어봐야 할지 모를 때. blindspot 조사 직후.

**호출**:
```
/unknowns:interview 방금 조사한 OAuth 작업에 대해. 아키텍처 관련 우선으로
```
자동 트리거: "interview me", "ask me questions before implementing", "인터뷰해줘",
"스펙 질문"

**진행 방식**: 라운드당 **4개 이하** 질문 — AskUserQuestion 다이얼로그 정확히 한 번이며,
그 하드 캡이 질문 1–4개·선택지 2–4개입니다 — 고정 우선순위(아키텍처 → 데이터 손실·보안 →
호환성 → 성능·비용 → 취향)로 묻습니다. 각 질문에 "왜 중요한지" 한 줄, 각 선택지에
트레이드오프가 붙습니다. 종료 시 **결정 테이블 + 바로 쓸 구현 프롬프트**를 제시하는데,
건너뛴 질문은 표시하고 아키텍처·데이터 결정은 확정으로 선언합니다.

**팁**: 심층 인터뷰를 원하면 `"40문항 수준으로 탈탈 털어줘"` — 우선순위를 유지하며
라운드를 반복합니다.

---

### 5. `/unknowns:prototypes` — 발산형 프로토타입 팬아웃

**언제**: 원하는 걸 말로 설명 못 하겠을 때("보면 안다"). 대시보드, UI, 문서 양식, API 설계 등.

**호출**:
```
/unknowns:prototypes 운동 기록 대시보드. 나 시각적 취향 없음, 알아서 4개
```
자동 트리거: "divergent prototypes", "design options", "know it when I see it",
"시안 4개", "프로토타입 여러 개", "보면 안다"

**진행 방식**: 잔변형이 아니라 **설계 철학이 다른** 안 4개(개수 조정 가능)를 만듭니다.
정보 구조·사용자 흐름·시각 밀도·상호작용·복잡도가 서로 다르고, 각 안에
이름 + 철학 한 줄 + 장단점 + 적합 조건이 붙습니다. HTML이면 한 파일에서 전환하며
비교하고, 각 요소에 **채택(steal)/제외(skip) 칩**을 눌러 반응하면 그 선택이 요구사항 목록 초안으로
자동 조립됩니다.

**반응하는 법**: `"2안의 레이아웃 + 4안의 색 + 1안의 필터"` 처럼 조합을 말하면
그것을 **명시적 요구사항 목록**으로 변환한 뒤에야 본 구현을 시작합니다.

**팁**: `"wild하게"` 라고 하면 철학 간 거리를 더 벌립니다. 코드 아키텍처 비교에도
사용 가능: `"이벤트 기반 vs 폴링 vs 푸시, 스켈레톤으로 나란히"`. 인터랙션 자체가
쟁점이면(툴바 위치 등) 클릭 가능한 목업 + A/B 선택 버튼으로 만들어 주고, 페이지에 전부
가짜 데이터라는 사실과 실제 배선이 들어갈 자리를 명시합니다.

---

### 6. `/unknowns:brainstorm` — 해법 공간 지도

**언제**: 문제는 아는데 뭘 해야 할지 모를 때. 첫 아이디어에 바로 뛰어들기 전에.

**호출**:
```
/unknowns:brainstorm 신규 가입자 첫 주 이탈이 40%. 2주 안에 쓸 수 있는 것 위주로
```
자동 트리거: "brainstorm interventions", "show me options", "브레인스토밍",
"해법 후보 펼쳐줘", "옵션 보여줘"

**진행 방식**: 코드베이스가 범위에 있으면 먼저 검색합니다 — 가장 싼 후보는 대개 새로
만드는 게 아니라 이미 있는 장치를 배선하는 것이고, 그런 후보에는
`Found in code — <경로>` 표시가 붙습니다. 그다음 후보 개입 10개 내외를 **즉시 적용~장기
베팅의 시간축**에 펼치고, 각각 기대 효과/노력 크기/핵심 리스크/측정법을 붙입니다.
효과×노력 토글로 quick win과 big bet을 구분하고, **공감(resonate) 체크**한 항목이 각
개입의 첫 실행 프롬프트까지 내려간 구조화된 다음 단계로 조립됩니다.

---

### 7. `/unknowns:reference` — 레퍼런스 분석

**언제**: 예시 코드·목업·스크린샷·경쟁 제품이 있고 "이것처럼" 만들고 싶을 때.

**호출**:
```
/unknowns:reference legacy/billing.py — 파이썬인데 이걸 TypeScript로 새 서비스에
```
자동 트리거: "use this as a reference", "make it like this", "레퍼런스로 써",
"이 코드처럼 만들어줘", "이거 참고해서"

**진행 방식**: 레퍼런스를 그대로 복사하지 않고 4분류 분석부터 제시합니다 —
**반드시 보존할 동작 / 현재 환경에 맞게 변환할 부분 / 불필요·위험한 부분 / 개선 가능한
부분**. 이식 작업이면 **이해 증명(semantics map)** — 번호가 붙은 레퍼런스 발췌 ↔ 대응
계획 대조, gotcha 노트, Match 열이 있는 엣지케이스 표 — 를 함께 냅니다. 사용자가 승인하기
전에는 아무것도 구현하지 않습니다: `semantics confirmed`라고 답하거나 번호로 행을
정정하세요. 승인 후에는 레퍼런스의 기존 테스트부터 이식하고 구현합니다.

**팁**: 레퍼런스는 코드가 아니어도 됩니다 — HTML 목업, 테스트 코드, 스크린샷,
원하는 출력의 실제 예시 전부 "지도"가 됩니다.

---

### 8. `/unknowns:plan` — 수정확률순 계획

**언제**: 조사·인터뷰가 끝나고 구현 전 계획이 필요할 때.

**호출**:
```
/unknowns:plan 방금 확정한 OAuth 스펙으로
```
자동 트리거: "plan this", "make a plan", "tweakable plan", "계획 세워줘", "구현 계획",
"수정확률순으로 계획"

**진행 방식**: 먼저 규모 게이트가 있습니다 — 파일 2개 이하에 스키마·인터페이스·UX 계약
결정이 없는 작업은 문서를 만들지 않고 네이티브 플랜 모드로 넘깁니다. 그 외에는 실행
순서가 아니라 **수정될 확률 순**으로 제시합니다: 스키마·인터페이스·UX 계약 같은 결정
항목이 맨 위, 각 항목에 고려한 대안과 파급 범위가 붙고, 새로 생기거나 바뀌는 공개
타입·스키마는 주석 달린 코드로 렌더링되며, 기계적 작업은 접어서 뒤로. 승인/변경 요청
선택이 회신으로 조립됩니다. 검증 방법·위험·롤백을 포함하고, **이 계획에서 가장 약한
부분**을 표시하며, 복사해 보낼 수 있는 회신 문구 2–3개로 마칩니다.

---

### 9. `/unknowns:notes` — 계획 이탈 기록

**언제**: 구현 중 계획·스펙에 없던 상황을 만났을 때. 사실상 **항상 켜두는 규칙**에 가깝습니다.

**호출**:
```
/unknowns:notes init     ← 프로젝트에 IMPLEMENTATION_NOTES.md 템플릿 생성
/unknowns:notes show     ← 지금까지 기록된 이탈 요약
/unknowns:notes 토큰 갱신을 lib 대신 직접 구현함 — 라이브러리가 PKCE 미지원
```
자동 트리거: "implementation notes", "record a deviation", "where did we diverge from
the plan?", "이탈 기록", "임플 노트", "어디서 계획이랑 달라졌어?"

구현 중 Claude가 스스로 이탈을 감지하면 알아서 기록하기도 합니다. `init`은 추가로 —
절대 조용히가 아니라 물어본 뒤 — 프로젝트의 `CLAUDE.md`나 `.claude/rules/unknowns.md`에
짧은 이탈 기록 규칙을 덧붙이자고 제안합니다. 그러면 이 스킬을 부를 때만이 아니라 이후 모든
세션의 컨텍스트에 규칙이 남습니다.

**기록되는 것**: 설계·동작·호환성에 영향을 주는 결정만 (문법·포맷팅·변수명은 제외).
정식 항목은 발견 상황 / 계획과 다른 점 / 선택한 대응 / 이유 / 버린 대안 / 위험·후속 확인을
담습니다. 같은 파일에 한 줄짜리 가벼운 종류 둘이 함께 들어갑니다: **Discovery**(계획이
가정한 것과 현실이 다름, 아직 결정은 불필요)와 **Todo for human**(사용자 몫이지만 아무것도
막지 않는 판단).

**지속성**: 파일이 존재하거나 `init`을 돌린 뒤에는 파일에 append하는 것이 의무입니다 —
채팅 요약만으로는 규칙을 만족하지 않습니다(훅·buy-in·quiz가 모두 이 파일을 읽습니다).
파일이 없으면 채팅 요약도 허용되지만, 그때는 마지막 메시지에 노트 파일이 없다고 밝혀야
합니다.

**에스컬레이션**: 아키텍처·사용자 가시 동작·데이터·보안에 닿는 결정은 기록 후
**작업을 멈추고 질문**하게 되어 있습니다. 마무리 단계에서는 **계획에 되먹이기** 블록 —
시도 #2에서 무엇이 달라지는지 복사 가능한 3줄 — 을 열린 Todo for human 항목과 함께
씁니다.

---

### 10. `/unknowns:quiz` — 작업 후 이해도 검증

**언제**: 큰 작업이 끝난 직후, PR 만들기·머지 직전. "내가 이걸 설명할 수 있나?" 싶을 때.

**호출**:
```
/unknowns:quiz 오늘 한 OAuth 작업 범위로
```
자동 트리거: "quiz me", "test my understanding", "퀴즈", "내가 이해했는지 확인해줘"

**진행 방식**: ① 먼저 설명(변경 구조 / 핵심 설계 결정 3개 / 실패 가능성 높은 곳 / 직접
확인해야 할 곳), 설명한 동작마다 `file:line` 앵커 → ② **질문 6개, 합격선은 6개 전부
정답**(AskUserQuestion이 한 번에 최대 4개라 4 + 2로 나눠 진행), 장애 대응 > 설계 이유 >
동작 예측 순이며 암기는 지양; IMPLEMENTATION_NOTES.md가 있으면 기록된 이탈 지점 최소 1개
포함 → ③ 채점 — 오답·무응답은 다시 읽을 변경 지점을 정확히 가리키고 재시도를 줍니다 →
④ 6/6이면 **머지 가능(cleared to merge)** 체크리스트(이해도 검증, CI 그린,
마이그레이션·롤아웃 검토, 머지 방식, 배포 후 관찰 대상), 6/6 미만이면 "아직"으로 두고 다시
읽을 절을 나열합니다. 마지막은 다른 개발자가 내일 인수받는다고 가정한 인수인계 요약이며,
원하면 PR 본문 초안으로 변환합니다.

---

### 11. `/unknowns:buy-in` — 리뷰어 설득 문서

**언제**: 구현·검증이 끝나고 리뷰어나 이해관계자의 **승인**을 받아야 할 때.

**호출**:
```
/unknowns:buy-in 이번 결제 리팩토링. 리뷰어는 백엔드 리드와 보안팀
```
자동 트리거: "buy-in doc", "prep me for review", "설득 문서 만들어줘", "리뷰 준비"

**진행 방식**: 최상단에 데모 먼저, 목표 읽기 시간 90초 → 리뷰어의 예상 반론 5개 내외에
선제 대응하되 각 답변에 리뷰어가 따라갈 수 있는 근거(스펙 §, IMPLEMENTATION_NOTES.md 항목
날짜, 지표, 테스트 실행, `file:line`)를 붙이고, 근거 없는 답변은 한계 항목으로 옮깁니다 →
결정 한눈에 보기 표 → IMPLEMENTATION_NOTES.md에서 끌어온 알려진 한계·미해결 unknown →
사인오프가 필요한 사람·팀과 각자의 확인 항목 → 롤백 계획. quiz가 나의 이해를 검증한다면,
buy-in은 타인의 신뢰를 준비합니다.

---

## 에이전트 사용법

에이전트는 별도 컨텍스트에서 도는 전문가입니다. 자연어로 지명하거나, 플러그인 스코프
id — `unknowns:unknowns-scout`, `unknowns:independent-reviewer` — 로 부르면 됩니다.
Agent 도구의 `subagent_type`과 `@agent-unknowns:unknowns-scout` 멘션 형식이 요구하는 것이
이 id입니다. `subagent_type`에 스코프 없는 `unknowns-scout`을 주면 거부됩니다.

에이전트의 **실효** 도구 집합은 선언된 목록을 호스트 세션이 실제로 노출하는 도구로 좁힌
결과입니다. 예컨대 Grep·Glob이 없는 환경에서는 두 에이전트 모두 Bash `grep`/`find`로
폴백합니다.

**unknowns-scout** (읽기 전용 정찰):
```
Use the unknowns-scout agent — 마이그레이션 계획에서 내가 놓친 것 조사
unknowns-scout 에이전트로 인증 모듈 정찰해줘
```
blindspot 스킬이 큰 조사에서 자동으로 이 에이전트를 부르기도 합니다. 대상 영역 구조를
훑고, git 히스토리에서 지저분한 막다른 길과 되돌려진 커밋을 보고, 테스트 커버리지와 암묵
관례를 확인하며, 낯선 라이브러리라면 *설치된* 버전의 공식 문서·체인지로그까지 봅니다
(그래서 읽기 도구와 함께 WebFetch·WebSearch를 가집니다). 중요도×영향도 순 조사 테이블과
개선된 프롬프트 초안을 돌려줍니다. 파일을 수정하지 않도록 지시되어 있고, 도구 목록에서
Edit/Write가 빠져 있으며, 번들된 PreToolUse 훅이 변경성 Bash 명령을 거부합니다 — 다만
Bash는 읽기 전용 조회용으로 남아 있어 샌드박스 수준의 보장은 아닙니다.

**independent-reviewer** (독립 검증):
```
Use the independent-reviewer agent — 방금 구현 머지 전 검증
독립 검증 돌려줘
```
구현한 세션의 설명을 **주장으로만 취급**하고 코드·테스트 실행으로 직접 확인합니다. 네 가지
점검 항목은 일반 코드 리뷰가 다루지 않는 것들로 의도적으로 좁혀져 있습니다:
**계획·스펙 부합**(요구사항마다 충족/부분/누락 판정), **기록된 이탈을 혼자 결정해도
괜찮았는지**, **테스트는 통과하는데 현실은 깨지는 경우**(목이 가린 실제 의존성, 구현을
그대로 비추기만 하는 테스트), 그리고 **확인 완료 목록** — 침묵은 검토 안 함과 구분되지
않기 때문입니다. 일반적인 버그·보안 사냥은 같은 diff에 대한 `/code-review`와
`/security-review`의 몫이니 함께 돌리세요. 그 둘을 쓸 수 없는 환경에서는 에이전트가 에러
처리·보안·성능·불필요한 복잡도를 2차 패스로 직접 커버합니다. loop 스킬 8단계에서 자동
호출됩니다.

---

## 훅 동작과 설정

플러그인은 훅 2종을 싣고 있고, 둘 다 순수 표준 라이브러리 파이썬입니다.

**노트 리마인더**는 한 세션의 파일 수정(Edit / Write / NotebookEdit)을 세다가
**10회에 도달하면 1회만**, "계획 이탈이 있었다면 IMPLEMENTATION_NOTES.md에 기록하라"를
사용자 화면과 Claude 컨텍스트 양쪽에 전달합니다 — 실제로 기록하는 주체인 Claude도 받도록.
아무것도 차단하지 않습니다. 컴팩션이 리마인더를 요약해 없애면 한 번 다시 말해 주고,
임계값을 넘겼는데 노트 파일을 끝내 건드리지 않았으면 Stop에서 한 번 더 말합니다.
IMPLEMENTATION_NOTES.md 자체를 수정한 것은 카운트에 들어가지 않고, 서브에이전트의 수정은
리마인더를 소비하지 않습니다 — 서브에이전트 컨텍스트는 반환과 함께 버려지기 때문입니다.

**프로젝트별 옵트인입니다**: 그 프로젝트가 이미 이 방법론을 쓰고 있어야 울립니다 —
`IMPLEMENTATION_NOTES.md`가 있거나, 스킬들이 산출물을 쓰는 `.unknowns/` 디렉터리가 있거나
(프로젝트 디렉터리 → Claude의 cwd 순으로, 레포 루트까지 거슬러 올라가며 탐색). 옵트인은
됐는데 노트 파일이 아직 없으면 리마인더에 `/unknowns:notes init`을 돌리라는 힌트가 붙습니다.
`UNKNOWNS_NOTES_ALWAYS=1`이면 어디서나 울립니다.

**Bash로 한 수정은 카운트되지 않습니다.** `sed`, 히어독, `python -c`는 PostToolUse
Edit/Write 이벤트 없이 파일을 고치므로, 그렇게 작업한 세션은 카운터가 0에 가까운 채로
끝납니다. 리마인더가 안 뜨는 가장 흔한 이유입니다.

**서브에이전트 읽기 전용 가드**는 모든 Bash 호출에서 돌지만 호출 주체가 `unknowns-scout`
또는 `independent-reviewer`가 아니면 즉시 빠지고, 사용자 트리를 바꾸는 명령(`rm`, `mv`,
쓰기성 `git` 서브커맨드, 패키지 설치 등)을 거부합니다. scout은 읽기 명령 화이트리스트로
묶이고, reviewer는 테스트·린트·빌드를 유지합니다. 파싱하지 못한 것은 통과시킵니다 —
샌드박스가 아니라 가드레일입니다.

**설정**:

| 하고 싶은 것 | 방법 |
|--------------|------|
| 임계값 변경 (예: 20회) | `UNKNOWNS_NOTES_THRESHOLD=20` |
| 리마인더 끄기 | `UNKNOWNS_NOTES_THRESHOLD=0` |
| 임계값 배수마다 반복 리마인드 | `UNKNOWNS_NOTES_REPEAT=1` |
| 아직 플러그인을 쓰지 않는 프로젝트에서도 울리기 | `UNKNOWNS_NOTES_ALWAYS=1` |
| 서브에이전트 Bash 가드 끄기 | `UNKNOWNS_AGENT_GUARD=0` |
| 위 값을 프로젝트 단위로 지정 | `.claude/settings.json` → `{"env": {"UNKNOWNS_NOTES_THRESHOLD": "20"}}`, 팀과 커밋 (각자 폴더를 신뢰해야 적용) |
| 위 값을 나만 지정 | `.claude/settings.local.json`, 같은 `env` 블록, git 무시 |
| 구버전 변수 | `FIELD_GUIDE_NOTES_THRESHOLD`도 계속 인식 (새 변수가 우선) |
| 요구사항 | `python3` (표준 라이브러리만, 외부 의존성 없음) |
| 검증 환경 | Claude Code 2.1.261, macOS (2026-09-06): `claude plugin validate` 통과, 리마인더는 실제 PostToolUse 파이프라인 경유 확인, 두 스크립트 모두 `tests/`로 커버 |
| 플랫폼 | CI가 ubuntu-latest와 windows-latest에서 스크립트 테스트를, ubuntu-latest에서 플러그인 검증을 돌립니다. macOS는 로컬 실행으로만 커버됩니다. Windows에서는 훅 명령이 `python3`인데 기본 PATH에는 보통 없음 — `python3` alias를 만들거나 명령을 조정하세요 |

**플러그인 없이 수동 설치** (스킬만 복사한 사용자): `hooks/scripts/impl_notes_reminder.py`를
프로젝트에 복사하고 아래를 `.claude/settings.json`에 추가합니다 — 이미 `hooks` 객체가
있다면 최상위 `hooks` 키를 하나 더 붙이지 말고 그 안에 합치세요:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write|NotebookEdit",
        "hooks": [
          {
            "type": "command",
            "command": "python3",
            "args": ["<스크립트 경로>/impl_notes_reminder.py"],
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

플러그인은 같은 스크립트를 SessionStart(compact)·Stop·SessionEnd에도 등록합니다. 컴팩션 후
재진술, 세션 종료 점검, 상태 파일 정리가 필요하면 같은 방식으로 항목을 추가하세요.

---

## 추천 시나리오

**시나리오 A — 작은 수정** (파일 1–2개, 명확한 스펙):
루프 불필요. 그냥 구현하되 notes 규칙만 적용됩니다. 훅이 안전망.

**시나리오 B — 중간 작업** (버그 원인 애매, 모듈 반쯤 아는 상태):
```
/unknowns:blindspot 장바구니 합계가 가끔 틀림. checkout/ 모듈
→ (조사 결과의 개선된 프롬프트 확인)
/unknowns:interview
/unknowns:plan
→ 구현
/unknowns:quiz
```

**시나리오 C — 크고 낯선 작업** (신규 기능, 처음 쓰는 라이브러리):
```
/unknowns:loop 실시간 협업 편집 기능 추가. CRDT는 처음 써봄
```
10단계 전체 — 조사·인터뷰·계획·독립 검증·buy-in까지 Claude가 순서대로 안내.

**시나리오 D — 비코딩** (디자인·문서·새 분야):
```
/unknowns:teach-me 유튜브 썸네일 디자인. 용어부터
/unknowns:prototypes 채널 아트 시안 4개, 철학 다르게
/unknowns:brainstorm 채널 성장 정체. 이번 달에 시도할 것들
```

---

## 문제 해결 (FAQ)

**Q. 스킬이 자동으로 안 뜹니다.**
자동 트리거는 문맥 판단이라 보수적입니다. 확실하게는 슬래시로 직접 호출하세요:
`/unknowns:blindspot`. 설치 직후라면 새 세션을 시작하거나 `/reload-plugins`.

**Q. `/unknowns:blindspot` 대신 `/blindspot`이라고 쳐도 되나요?**
대부분은 됩니다. 플러그인 스킬은 스코프 이름으로도, 맨 이름으로도 호출됩니다 — 같은 이름을
쓰는 다른 명령이 없는 한. 그래서 `/blindspot`, `/quiz`는 그냥 동작합니다. 예외는 `loop`로,
Claude Code가 자체 `loop` 스킬(반복 인터벌 러너)을 싣고 있어 맨 `/loop`는 그쪽으로 가고 이
플러그인의 루프는 항상 `/unknowns:loop`가 필요합니다. 스코프 형식은 절대 모호하지 않아서
이 README는 그쪽을 씁니다.

**Q. 예전에 field-guide로 설치했는데요.**
0.1.x의 옛 이름입니다. 위 "0.1.x(field-guide)에서 업그레이드"를 따라 제거 후 재설치하세요.

**Q. 훅이 안 울립니다.**
순서대로 확인하세요. (1) 프로젝트에 `IMPLEMENTATION_NOTES.md`나 `.unknowns/` 디렉터리가
있나요? 둘 다 없으면 설계상 꺼져 있습니다 — `/unknowns:notes init`을 돌리거나
`UNKNOWNS_NOTES_ALWAYS=1`을 켜세요.
(2) 수정을 Bash(`sed`, 히어독, `python -c`)로 했나요? 그건 PostToolUse Edit/Write 이벤트를
발생시키지 않아 카운터가 올라가지 않습니다. (3) 기본값이 정말 세션당 1회·수정 10회입니다 —
`UNKNOWNS_NOTES_THRESHOLD`와 `python3 --version`을 확인하세요. (4) `/hooks`를 실행해
PostToolUse 아래에 항목이 보이는지 확인하세요. (5) 스크립트를 직접 스모크 테스트하세요:

```bash
echo '{"session_id":"x","tool_name":"Edit","cwd":"'$PWD'"}' \
  | UNKNOWNS_NOTES_THRESHOLD=1 UNKNOWNS_NOTES_ALWAYS=1 \
    python3 hooks/scripts/impl_notes_reminder.py
```
`systemMessage`가 든 JSON 객체를 출력하고 exit 0이면 정상입니다. (6) `claude --debug`로
실행한 뒤 `~/.claude/debug/<session-id>.txt`를 읽으세요. 스크립트는
`[unknowns] state persist failed` 같은 경고를 stderr로만 쓰고, 그건 디버그 로그에만
남습니다.

**Q. 카운트가 이상하거나 리마인더가 두 번 떴습니다.**
세션별 상태는 작은 JSON 파일 하나에 있습니다. `$CLAUDE_PLUGIN_DATA`가 설정되어 있으면
`$CLAUDE_PLUGIN_DATA/state/` 아래, 아니면 임시 디렉터리의 `0700` 사용자 전용 디렉터리
(`unknowns-notes-<user>/<session-id>.json`)입니다. 지우면 카운트가 초기화됩니다. "1회만"이
두 번 울리는 경우는 둘입니다. 세션 도중 임시 디렉터리가 청소되면 카운트가 다시 시작되고,
설계상 SessionStart(compact)가 리마인더를 다시 무장하므로 컴팩션 때마다 한 번 더
울립니다. SessionEnd가 알아서 파일을 지웁니다.

**Q. 훅이 거슬립니다.**
`UNKNOWNS_NOTES_THRESHOLD=0` 또는 임계값을 30 정도로 올리세요 — `.claude/settings.json`의
`env` 블록으로 프로젝트 단위로 지정하면 전역을 건드리지 않아도 됩니다.

**Q. 원문과 플러그인이 다른 부분은?**
`skills/loop/references/talk-source.md`에 "원문에서 직접 검증된 부분"과
"제작 시 확장한 부분"이 표로 구분되어 있습니다.

---

## 출처 표기와 라이선스

이 플러그인은 독립적인 서드파티 저작물입니다. **Anthropic PBC와 제휴·후원·보증 관계가
없습니다.**

토대가 된 방법론, 예시 제목, 인용된 프롬프트 문구는 "Know your unknowns" 예시 모음에서
왔습니다. Copyright 2026 Anthropic PBC, Apache License, Version 2.0 —
https://www.apache.org/licenses/LICENSE-2.0. "Field Guide to Fable" 강연에서 가져온 짧은
문구는 출처를 밝힌 인용으로 사용했습니다. 플러그인 자체의 코드와 문서는 MIT입니다.
`LICENSE`에 MIT 전문이 있고, `NOTICE`에는 Apache-2.0 고지와 전문 링크가 있습니다.

---

## 출처

- 예시 모음: https://thariqs.github.io/html-effectiveness/unknowns/ ("Know your unknowns")
- 원본 저장소: https://github.com/ThariqS/html-effectiveness
- 부모 글: https://thariqs.github.io/html-effectiveness/ ("The unreasonable effectiveness of HTML")
- 강연: https://www.youtube.com/watch?v=9fubhllmsBU (AI Engineer World's Fair 2026)
- 이 플러그인: https://github.com/ajitta/know-your-unknowns
- 검증 상세와 관련 문헌: `skills/loop/references/talk-source.md`
