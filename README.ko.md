# know-your-unknowns

**Language**: [English](README.md) | 한국어

> 지도는 영토가 아니다 — 그 간극이 당신의 unknowns다.

Thariq Shihipar(Anthropic, Claude Code 팀)의 방법론을 Claude에서 바로 쓸 수 있게 만든
플러그인입니다. 두 자료가 원 출처입니다:

- 강연 **"Field Guide to Fable"** (AI Engineer World's Fair 2026 키노트)
- 예시 모음 **"Know your unknowns"** (11개 인터랙티브 예시) —
  https://thariqs.github.io/html-effectiveness/unknowns/

핵심 아이디어: **강한 모델의 병목은 모델이 아니라, 지도(계획)와 영토(실제)를 일치시키는
사용자의 능력이다.** 이 플러그인은 그 간극(unknowns)을 구현 전·중·후에 걸쳐 찾고
관리하는 운영 루프를 제공합니다 — 원문 11개 예시와 1:1 대응하는 스킬 11종 +
에이전트 2종 + 훅 1종. 사실검증 상세는 `skills/loop/references/talk-source.md` 참조.

산출물 철학(원문의 절반이 이것입니다): 사용자가 보고 반응해야 하는 산출물은
**반응을 구조화된 답변으로 조립해 주는 단일 파일 인터랙티브 HTML**로 만들고,
뷰어가 없는 환경에서는 마크다운으로 폴백합니다.

---

## 설치

플러그인 이름은 `unknowns`입니다 (호출: `/unknowns:<스킬>`).

### Cowork (데스크톱 앱)

채팅에 전달된 `unknowns.plugin` 카드에서 **설치 버튼**을 누르면 끝입니다.

### Claude Code (CLI)

세 가지 방법 중 하나를 선택합니다.

**방법 A — 로컬 테스트 (가장 빠름)**
```bash
unzip unknowns.plugin -d ~/plugins/unknowns
claude --plugin-dir ~/plugins/unknowns
```
세션 안에서 `/unknowns:loop` 등이 바로 보이면 성공입니다.

**방법 B — 마켓플레이스 설치 (영구 설치, 권장)**

이 레포는 마켓플레이스 매니페스트를 포함하고 있어 바로 설치됩니다:
```
/plugin marketplace add ajitta/know-your-unknowns
/plugin install unknowns@ajitta
```
업데이트는 `/plugin marketplace update ajitta` 후 재설치.

**방법 C — 스킬만 골라서 복사 (플러그인 없이)**
특정 스킬만 원하면 `skills/<이름>` 폴더를 볼트나 프로젝트의 `.claude/skills/`에 복사합니다.
이 경우 호출명은 네임스페이스 없이 `/blindspot`, `/quiz`처럼 짧아지고,
에이전트는 `agents/*.md`를 `.claude/agents/`에 복사하면 됩니다.
단, 훅은 플러그인 형태일 때만 자동 활성화됩니다(수동 설정은 아래 "훅" 절 참고).

### 구버전(field-guide)에서 업그레이드

0.1.x는 `field-guide`라는 이름으로 배포되었습니다. 이름이 바뀌었으므로 제거 후 재설치합니다:
```
/plugin uninstall field-guide@ajitta
/plugin marketplace update ajitta
/plugin install unknowns@ajitta
```
GitHub 레포 리네임으로 옛 URL(`ajitta/field-guide`)은 자동 리다이렉트됩니다.
환경변수 `FIELD_GUIDE_NOTES_THRESHOLD`는 계속 인식하지만 `UNKNOWNS_NOTES_THRESHOLD`
사용을 권장합니다.

### 설치 확인

```
/unknowns:blindspot 테스트
```
스킬이 로드되어 "아직 구현하지 마라" 원칙과 조사 절차로 응답하면 정상입니다.

---

## 빠른 시작 (10초 요약)

- 크고 낯선 작업 → `/unknowns:loop <작업 설명>` 하나면 됩니다. 나머지는 Claude가 단계별로 안내합니다.
- 특정 기법만 필요 → 아래 개별 스킬을 직접 호출하거나, 자연어로 말하면 자동 트리거됩니다.
- 슬래시 없이도 동작: "사각지대 조사해줘", "인터뷰해줘", "시안 4개 보여줘", "quiz me" 같은 말이 곧 트리거입니다.

**스킬 한눈에 보기** (원문 11개 예시와 1:1):

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

## 스킬별 상세 사용법

### 1. `/unknowns:loop` — 전체 운영 루프

**언제**: 크거나 낯선 기능 개발, 스펙이 흐릿한 작업, "제대로 각 잡고" 진행하고 싶을 때.

**호출**:
```
/unknowns:loop 결제 모듈에 구독 갱신 기능 추가
```
자동 트리거 문구: "운영 루프로 진행해줘", "풀 루프로 해줘", "know your unknowns로"

**진행 방식**: Claude가 10단계를 순서대로 끌고 갑니다 —
① 가치·완료 조건 정의(사용자와 합의) → ② blindspot 조사(+필요시 teach-me) →
③ 인터뷰 → ④ 해법·형태 탐색(brainstorm/prototypes/reference, 필요시) →
⑤ 위험 가정 최소 검증 → ⑥ 수정확률순 계획(plan) → ⑦ 구현 + 이탈 기록(notes) →
⑧ 독립 검증 → ⑨ 퀴즈·인수인계(+필요시 buy-in) → ⑩ 가치 검토.

**팁**: 작업 규모를 말해주면 단계를 알아서 줄입니다. 예:
```
/unknowns:loop 이건 중간 규모야. 버그 수정인데 원인이 애매함
```
→ blindspot → interview → plan → 구현 → quiz 로 축소 진행.

---

### 2. `/unknowns:blindspot` — 구현 전 사각지대 조사

**언제**: 잘 모르는 모듈·라이브러리·도메인을 건드리기 전. "내가 뭘 모르는지 모르는" 상태일 때.

**호출**:
```
/unknowns:blindspot 인증 모듈에 카카오 OAuth 추가. git 히스토리랑 tests/ 위주로 봐줘
```
자동 트리거: "사각지대 조사해줘", "blind spot pass", "내가 놓친 게 뭐지"

**진행 방식**: 코드를 **수정하지 않고** 조사만 합니다. 범위가 크면 unknowns-scout
에이전트에 위임합니다. 결과는 발견 1건 = 카드 1장(HTML) 또는 중요도×영향도 테이블 —
위험 전제 / unknown unknowns / 구조 충돌 / 회귀 위험 / 구현 전 질문 / 프롬프트 보강 정보.

**핵심 산출물**: 카드의 "프롬프트 픽스"들이 조립된 **개선된 프롬프트 초안**.
이걸 복사해서 실제 구현 지시로 쓰는 것이 이 스킬의 목적입니다.

**팁**: 코드가 아니어도 됩니다. `"영상 색보정을 처음 해보는데 blind spot pass 해줘"`
처럼 새 분야에도 적용됩니다 — 용어 자체를 배워야 하면 아래 teach-me가 더 맞습니다.

---

### 3. `/unknowns:teach-me` — 도메인 어휘 설명서

**언제**: "더 좋게 해줘"밖에 말할 수 없을 때. 그 분야의 용어를 몰라 요청이 모호해질 때.

**호출**:
```
/unknowns:teach-me 영상 색보정. 나 완전 초보
```
자동 트리거: "가르쳐줘", "설명서 만들어줘", "이 분야 용어를 모르겠어"

**진행 방식**: 이 작업에서 내리게 될 결정 축 3–7개 → 축마다 어휘 사다리
(일상어→전문어, 용어별 요청 예문) → 개념별 before/after 비교(가능하면 라이브
슬라이더) → 마지막에 **원래 요청을 새 어휘로 다시 쓴 정밀 요청 초안**.

---

### 4. `/unknowns:interview` — 구현 전 인터뷰

**언제**: 스펙이 불완전한데 뭘 물어봐야 할지 모를 때. blindspot 조사 직후.

**호출**:
```
/unknowns:interview 방금 조사한 OAuth 작업에 대해. 아키텍처 관련 우선으로
```
자동 트리거: "인터뷰해줘", "구현 전에 질문해줘", "ask me questions about the spec"

**진행 방식**: 라운드당 **5개 이하** 질문, 고정 우선순위(아키텍처 → 데이터 손실·보안 →
호환성 → 성능·비용 → 취향). 각 질문에 "왜 중요한지" 한 줄이 붙고, 선택지형 질문은
AskUserQuestion 다이얼로그로 나옵니다. 종료 시 **결정 테이블 + 바로 쓸 구현 프롬프트**를
제시합니다.

**팁**: 심층 인터뷰를 원하면 `"40문항 수준으로 탈탈 털어줘"` — 우선순위를 유지하며
라운드를 반복합니다.

---

### 5. `/unknowns:prototypes` — 발산형 프로토타입 팬아웃

**언제**: 원하는 걸 말로 설명 못 하겠을 때("보면 안다"). 대시보드, UI, 문서 양식, API 설계 등.

**호출**:
```
/unknowns:prototypes 운동 기록 대시보드. 나 시각적 취향 없음, 알아서 4개
```
자동 트리거: "시안 4개 보여줘", "다양한 디자인으로", "design options"

**진행 방식**: 잔변형이 아니라 **설계 철학이 다른** 안 4개(개수 조정 가능)를 만듭니다.
정보 구조·사용자 흐름·시각 밀도·상호작용·복잡도가 서로 다르고, 각 안에
이름 + 철학 한 줄 + 장단점 + 적합 조건이 붙습니다. HTML이면 한 파일에서 전환하며
비교하고, 각 요소에 **채택(steal)/제외(skip) 칩**을 눌러 반응하면 그 선택이 요구사항 목록 초안으로
자동 조립됩니다.

**반응하는 법**: `"2안의 레이아웃 + 4안의 색 + 1안의 필터"` 처럼 조합을 말하면
그것을 **명시적 요구사항 목록**으로 변환한 뒤에야 본 구현을 시작합니다.

**팁**: `"wild하게"` 라고 하면 철학 간 거리를 더 벌립니다. 코드 아키텍처 비교에도
사용 가능: `"이벤트 기반 vs 폴링 vs 푸시, 스켈레톤으로 나란히"`. 인터랙션 자체가
쟁점이면(툴바 위치 등) 클릭 가능한 목업 + A/B 선택 버튼으로 만들어 줍니다.

---

### 6. `/unknowns:brainstorm` — 해법 공간 지도

**언제**: 문제는 아는데 뭘 해야 할지 모를 때. 첫 아이디어에 바로 뛰어들기 전에.

**호출**:
```
/unknowns:brainstorm 신규 가입자 첫 주 이탈이 40%. 2주 안에 쓸 수 있는 것 위주로
```
자동 트리거: "브레인스토밍", "해법 후보 펼쳐줘", "옵션 보여줘"

**진행 방식**: 후보 개입 10개 내외를 **즉시 적용~장기 베팅의 시간축**에 펼치고,
각각 기대 효과/노력/리스크/측정법을 붙입니다. 효과×노력 배치로 quick win과 big bet을
구분하고, **공감(resonate) 체크**한 항목이 구조화된 다음 단계로 조립됩니다.

---

### 7. `/unknowns:reference` — 레퍼런스 분석

**언제**: 예시 코드·목업·스크린샷·경쟁 제품이 있고 "이것처럼" 만들고 싶을 때.

**호출**:
```
/unknowns:reference legacy/billing.py — 파이썬인데 이걸 TypeScript로 새 서비스에
```
자동 트리거: "이 코드 참고해서", "레퍼런스로 써", "이거랑 비슷하게"

**진행 방식**: 레퍼런스를 그대로 복사하지 않고 4분류 분석부터 제시합니다 —
**반드시 보존할 동작 / 현재 환경에 맞게 변환할 부분 / 불필요·위험한 부분 / 개선 가능한
부분**. 이식 작업이면 **이해 증명(semantics map)** — 레퍼런스 발췌 ↔ 대응 계획 대조,
gotcha 노트, 엣지케이스 표 — 를 함께 냅니다. 승인 후 구현합니다.

**팁**: 레퍼런스는 코드가 아니어도 됩니다 — HTML 목업, 테스트 코드, 스크린샷,
원하는 출력의 실제 예시 전부 "지도"가 됩니다.

---

### 8. `/unknowns:plan` — 수정확률순 계획

**언제**: 조사·인터뷰가 끝나고 구현 전 계획이 필요할 때.

**호출**:
```
/unknowns:plan 방금 확정한 OAuth 스펙으로
```
자동 트리거: "계획 세워줘", "tweakable plan", "수정확률순으로 계획"

**진행 방식**: 실행 순서가 아니라 **수정될 확률 순**으로 제시합니다 — 스키마·인터페이스·
UX 계약 같은 결정 항목이 맨 위, 각 항목에 고려한 대안과 파급 범위가 붙고, 기계적 작업은
접어서 뒤로. 승인/변경 요청 선택이 회신으로 조립됩니다. 검증 방법·위험·롤백 포함.

---

### 9. `/unknowns:notes` — 계획 이탈 기록

**언제**: 구현 중 계획·스펙에 없던 상황을 만났을 때. 사실상 **항상 켜두는 규칙**에 가깝습니다.

**호출**:
```
/unknowns:notes init     ← 프로젝트에 IMPLEMENTATION_NOTES.md 템플릿 생성
/unknowns:notes show     ← 지금까지 기록된 이탈 요약
/unknowns:notes 토큰 갱신을 lib 대신 직접 구현함 — 라이브러리가 PKCE 미지원
```
자동 트리거: 구현 중 Claude가 스스로 이탈을 감지하면 자동 기록합니다. "이탈 기록해줘",
"어디서 계획이랑 달라졌어?"도 트리거.

**기록되는 것**: 설계·동작·호환성에 영향을 주는 결정만 (문법·포맷팅·변수명은 제외).
항목마다 발견 상황 / 계획과 다른 점 / 선택한 대응 / 이유 / 버린 대안 / 위험 /
다음 시도 개선점.

**에스컬레이션**: 아키텍처·사용자 가시 동작·데이터·보안에 닿는 결정은 기록 후
**작업을 멈추고 질문**하게 되어 있습니다.

---

### 10. `/unknowns:quiz` — 작업 후 이해도 검증

**언제**: 큰 작업이 끝난 직후, PR 만들기·머지 직전. "내가 이걸 설명할 수 있나?" 싶을 때.

**호출**:
```
/unknowns:quiz 오늘 한 OAuth 작업 범위로
```
자동 트리거: "quiz me", "퀴즈 내줘", "내가 이해했는지 확인해줘"

**진행 방식**: ① 먼저 설명(변경 구조 / 핵심 설계 결정 3개 / 실패 가능성 높은 곳 /
직접 확인해야 할 곳) → ② 질문 5개(장애 대응 > 설계 이유 > 동작 예측 순, 암기 지양;
IMPLEMENTATION_NOTES가 있으면 이탈 지점 최소 1개 포함) → ③ 채점 — 오답은 다시 봐야 할
변경 지점을 정확히 가리킴 → ④ 인수인계 요약(다른 개발자가 내일 인수받는다고 가정).
원하면 PR 본문 초안으로 변환.

---

### 11. `/unknowns:buy-in` — 리뷰어 설득 문서

**언제**: 구현·검증이 끝나고 리뷰어나 이해관계자의 **승인**을 받아야 할 때.

**호출**:
```
/unknowns:buy-in 이번 결제 리팩토링. 리뷰어는 백엔드 리드와 보안팀
```
자동 트리거: "buy-in 문서", "리뷰 준비해줘", "머지 승인 준비"

**진행 방식**: 데모 먼저(최상단) → 리뷰어의 예상 반론 5개 내외에 증거(테스트·벤치마크·
코드 위치)로 선제 대응 → 알려진 한계·미해결 unknown(IMPLEMENTATION_NOTES 연동) →
사인오프 필요한 사람·팀과 각자의 확인 항목 → 롤백 계획. quiz가 나의 이해를 검증한다면,
buy-in은 타인의 신뢰를 준비합니다.

---

## 에이전트 사용법

에이전트는 별도 컨텍스트에서 도는 전문가입니다. 자연어로 지명하면 됩니다.

**unknowns-scout** (읽기 전용 정찰):
```
Use the unknowns-scout agent — 마이그레이션 계획에서 내가 놓친 것 조사
unknowns-scout 에이전트로 인증 모듈 정찰해줘
```
blindspot 스킬이 큰 조사에서 자동으로 이 에이전트를 부르기도 합니다.
파일을 절대 수정하지 않고, 조사 테이블 + 개선된 프롬프트 초안을 돌려줍니다.

**independent-reviewer** (독립 검증):
```
Use the independent-reviewer agent — 방금 구현 머지 전 검증
독립 검증 돌려줘
```
구현한 세션의 설명을 **주장으로만 취급**하고 코드·테스트 실행으로 직접 확인합니다.
Critical/Warning/Info로 분류된 결과와 "확인 완료" 목록(침묵≠검토 안 함 구분)을 돌려줍니다.
loop 스킬 8단계에서 자동 호출됩니다.

---

## 훅 동작과 설정

**무엇을 하나**: 한 세션에서 파일 수정(Edit/Write)이 **10회에 도달하면 1회만**,
"계획 이탈이 있었다면 IMPLEMENTATION_NOTES.md에 기록하라"는 리마인더를 사용자 화면과
Claude 컨텍스트 양쪽에 전달합니다(실제로 기록하는 주체인 Claude도 받도록).
차단·간섭 없음, 메시지 한 줄이 전부입니다.

**설정**:

| 하고 싶은 것 | 방법 |
|--------------|------|
| 임계값 변경 (예: 20회) | 환경변수 `UNKNOWNS_NOTES_THRESHOLD=20` |
| 끄기 | `UNKNOWNS_NOTES_THRESHOLD=0` |
| 임계값 배수마다 반복 리마인드 | `UNKNOWNS_NOTES_REPEAT=1` |
| 구버전 변수 | `FIELD_GUIDE_NOTES_THRESHOLD`도 계속 인식 (새 변수가 우선) |
| 요구사항 | `python3` (표준 라이브러리만, 외부 의존성 없음) |

**플러그인 없이 수동 설치** (방법 C 사용자): `hooks/scripts/impl_notes_reminder.py`를
프로젝트에 복사하고 `.claude/settings.json`(또는 볼트의 hooks.json)에 추가:
```json
"PostToolUse": [{
  "matcher": "Edit|Write",
  "hooks": [{ "type": "command",
    "command": "python3 <스크립트 경로>/impl_notes_reminder.py", "timeout": 5 }]
}]
```

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

**Q. `/blindspot`이 아니라 왜 `/unknowns:blindspot`인가요?**
플러그인 스킬은 이름 충돌 방지를 위해 `플러그인명:스킬명`으로 네임스페이스가 붙습니다.
짧은 이름을 원하면 방법 C(개별 복사)로 설치하세요.

**Q. 예전에 field-guide로 설치했는데요.**
0.1.x의 옛 이름입니다. 위 "구버전에서 업그레이드" 절을 따라 제거 후 재설치하세요.
스킬 대응: `reference-map`→`reference`, `impl-notes`→`notes`, 나머지는 이름 동일.

**Q. 훅이 안 울립니다.**
정상일 가능성이 높습니다 — 기본값은 세션당 1회, 수정 10회 도달 시에만 발동합니다.
`python3 --version`으로 파이썬 확인, `UNKNOWNS_NOTES_THRESHOLD` 값 확인.

**Q. 훅이 거슬립니다.**
`UNKNOWNS_NOTES_THRESHOLD=0` 또는 임계값을 30 정도로 올리세요.

**Q. 원문과 플러그인이 다른 부분은?**
`skills/loop/references/talk-source.md`에 "원문에서 직접 검증된 부분"과
"제작 시 확장한 부분"이 표로 구분되어 있습니다.

---

## 출처

- 예시 모음: https://thariqs.github.io/html-effectiveness/unknowns/ ("Know your unknowns")
- 부모 글: https://thariqs.github.io/html-effectiveness/ ("The unreasonable effectiveness of HTML")
- 강연: https://www.youtube.com/watch?v=9fubhllmsBU (AI Engineer World's Fair 2026)
- 검증 상세와 관련 문헌: `skills/loop/references/talk-source.md`
