# "Know your unknowns" 연구 조사 분석

| 항목 | 내용 |
|------|------|
| 조사 대상 | https://thariqs.github.io/html-effectiveness/unknowns/ |
| 부모 페이지 | https://thariqs.github.io/html-effectiveness/ |
| 조사 일자 | 2026-07-11 (Asia/Seoul) |
| 조사 방법 | 대상 페이지 3회 독립 페치 + 부모 페이지 1회 페치, 결과 상호 대조. `ajitta/know-your-unknowns` 플러그인(구 field-guide) 전체 소스와 대조 분석 |
| 확실성 표기 | 【검증】= 복수 페치에서 일치 확인, 【단일】= 1회 페치에만 등장, 【추정】= 페이지에 명시되지 않은 해석 |

이 문서는 한 세션에서 수행한 조사·분석의 기록이다. 원문 페이지는 JS 렌더링 기반이라
텍스트 추출로 접근했으며, 인터랙티브 데모 내부의 모든 동작을 직접 실행해 본 것은
아니다(→ §9 한계).

---

## 1. 출처 식별과 맥락

페이지의 정확한 제목은 **"Know your *unknowns* — examples"**, 부제는 "Companion to
the blog post"다.【검증】 저자는 페이지 자체에 명시돼 있지 않으나, 도메인
(`thariqs.github.io`)과 부모 프로젝트로 보아 **Thariq Shihipar**(Anthropic, Claude
Code 팀)로 판단한다.【추정 — 신뢰도 높음. 동일 인물의 강연 "Field Guide to Fable"
(AI Engineer World's Fair 2026 키노트) 및 글 "HTML is the new markdown"(Lenny's
Newsletter, 2026-05-18)과 내용·용어가 일치】

이 페이지는 독립 문서가 아니라 블로그 글 **"The unreasonable effectiveness of
HTML"**의 컴패니언(예시 전시장)이다. 부모 페이지는 "AI 에이전트의 산출물은 마크다운이
아니라 자기완결(self-contained) HTML이어야 한다"는 테제의 예시 모음이고, unknowns
페이지는 그 테제를 **불확실성 관리**라는 영역에 적용한 병렬 전시다.【검증】

## 2. 핵심 프레임

페이지 서두의 프레임 문장:

> "The map is not the territory — the gap between them is your unknowns.
> Eleven self-contained `.html` artifacts for discovering them before, during,
> and after implementation." 【검증 — 3회 페치 일치】

두 가지 지적 계보가 결합돼 있다. "지도는 영토가 아니다"는 Alfred Korzybski(1931)의
일반의미론 명제이고, unknowns의 분류는 Johari window(1955) 및 Rumsfeld 브리핑(2002)
계열의 2×2 매트릭스다. 페이지는 네 사분면을 제시한다: **Known knowns / Known
unknowns / Unknown knowns / Unknown unknowns**.【검증 — 사분면 라벨. 각 사분면의
상세 설명 텍스트는 추출되지 않음】

방법론의 요지: 계획(지도)과 실제(영토)의 간극이 unknowns이며, 이를 **프로덕션에서
발견하는 대신 구현 전·중·후의 저렴한 아티팩트로 미리 발견**하라는 것. 페이지의
맺음 문장이 이를 압축한다:

> "Every explainer, brainstorm, interview, and prototype is a cheap way to find
> out what you didn't know." 【단일 — 3차 페치에서 확인】

구조는 구현 전 8개, 구현 중 1개, 구현 후 2개로 총 11개 아티팩트다.【검증】

## 3. 11개 예시 상세

각 예시에 대해 원문 제목, 시점, 내용, 데모의 인터랙션 장치, 방법론적 의미를 기록한다.
인터랙션 장치 목록은 2·3차 페치에서 일치 확인된 것 위주다.

### 3.1 Blindspot Pass (구현 전)

낯선 코드 모듈·시스템을 스캔해 사각지대를 찾는 데모. **7장의 blindspot 카드**로
결과를 제시하며, 각 카드에 **복사 가능한 "프롬프트 픽스"**가 붙어 있고 이것들이
더 나은 구현 지시문으로 조립된다.【검증】 방법론적 의미: unknown unknowns를 직접
없앨 수는 없으므로, 조사 결과를 "더 나은 프롬프트"라는 실행 가능한 형태로 환원한다.
강연에서의 원 프롬프트: "I'm working on X that I know nothing about. Do a blind-spot
pass to help me figure out my relevant unknown unknowns and help me prompt better."
(강연 10:48–11:39 — 별도 검증 자료 talk-source.md 참조)

### 3.2 Teach Me My Unknowns (구현 전)

색보정(color-grading)을 소재로 한 인터랙티브 설명서. **어휘 사다리(vocabulary
ladder)**, **라이브 before/after 프레임과 슬라이더**, 프리셋을 포함한다.【검증】
"make the video nicer" 같은 모호한 요청을 전문 언어의 정밀한 요청으로 바꾸는 것이
목적.【검증】 방법론적 의미: 모호한 요청의 원인을 취향 부족이 아니라 **어휘 부족**
으로 진단하고, 사용자를 가르쳐 요청 자체의 해상도를 올린다. unknown unknowns 중
개념·용어의 공백을 다루는 유일한 예시.

### 3.3 Four Design Directions (구현 전)

같은 리뷰 큐(review queue)를 **네 가지 다른 방식으로 렌더링** — ops 콘솔, 에디토리얼,
칸반, 터미널 스타일.【단일 — 4개 스타일 명칭은 2차 페치에만 등장】 각 안에
**채택/제외(steal/skip) 칩**이 있고, 선택이 **미리 채워진 회신(reply template)**으로
자동 생성된다.【검증】 방법론적 의미: 사용자가 말로 표현 못 하는 취향(unknown
knowns)을 "보고 반응"으로 추출한다. 강연 원문: "I have no visual taste. Make me an
HTML page with four widely different design decisions so I can react to them."

### 3.4 Mock before you wire (구현 전)

프레임 주석(frame-annotation) 툴바의 **클릭 가능한 프로토타입**. 프로덕션 코드 없이
**토글 가능한 배치 3종**, **A/B 결정 질문**, **자동 채움 회신 템플릿**을 포함한다.
【검증】 방법론적 의미: 인터랙션 설계는 정적 와이어프레임보다 클릭해 보는 목업이
정확하다 — 형태가 아니라 **행동**에 대한 반응을 수집한다.

### 3.5 Brainstorm the Intervention (구현 전)

이탈(churn) 감소 전략 **10개**를 **즉시 적용부터 분기 단위 베팅까지의 타임라인**에
배치한 데모. **공감(resonate) 체크박스**를 체크하면 구조화된 응답으로 조립된다.
【검증】 방법론적 의미: 문제를 받자마자 첫 해법에 뛰어들면 해법 공간의 나머지가
전부 unknown으로 남는다. 모델이 공간을 그리고 선택은 사용자가 한다.

### 3.6 The Interview (구현 전)

모델이 모호한 기능에 대해 **한 번에 하나씩, 아키텍처 영향 순으로** 질문을 던지는
인터페이스. 종료 시 **결정 테이블(decisions table)**과 **바로 쓸 수 있는 구현
프롬프트(implementation prompt export)**를 산출한다.【검증】 방법론적 의미: known
unknowns(빈 스펙)를 사용자와의 문답으로 결정으로 전환한다. 강연 원문: "prioritize
questions that would change the architecture."

### 3.7 Point at a Reference (구현 전)

레퍼런스 구현을 이식하기 전에 **이해했음을 증명하는 시맨틱스 맵(semantics map)**.
**대응된 코드 발췌(matched code excerpts)**, **gotcha 노트**, **엣지케이스 표**를
포함한다.【검증】 방법론적 의미: 레퍼런스는 정답이 아니라 또 하나의 지도다. 복사
전에 "무엇이 보존돼야 하는 동작인지"의 이해를 검증 가능한 형태로 먼저 내놓는다.
강연 원문: "give it another map."

### 3.8 The Tweakable Plan (구현 전)

구현 로드맵을 **실행 순서가 아니라 "수정될 확률(likelihood-of-tweaking)" 순으로
정렬**한 계획서. **스키마 결정에 대안 플래그**, **토글 가능한 대안**, **주석 달린
타입 인터페이스**, 그리고 기계적 작업은 접어서(collapsed) 처리한다.【검증】
방법론적 의미: 계획서의 목적은 실행 나열이 아니라 **사용자 개입 지점의 전진 배치**다.
사용자가 위에서부터 읽다 지쳐도 정말 봐야 할 결정은 이미 다 본 상태가 된다.
11개 중 가장 반직관적이고 독창적인 장치라고 판단한다.【추정 — 평가는 조사자 의견】

### 3.9 Implementation Notes (구현 중 — 유일)

**3시간 빌드 세션의 계획 이탈을 전부 기록한 러닝 로그**. 각 항목은 내린 보수적
선택(conservative choice)의 근거와 **다음 시도를 개선할 불릿 3개**를 담는다.【검증】
방법론적 의미: 에이전트가 계획에 없는 상황(unknown)을 만나 조용히 우회하는 것을
가시화한다. 이탈의 기록이 곧 지도-영토 간극의 실측 데이터가 된다. 강연 원문:
"If it runs into an unknown, ask it to log it, so you can see where the deviations
happened and figure out why."

### 3.10 The Buy-In Doc (구현 후)

출시 준비(ship-readiness) 피치 문서. **애니메이션 데모를 최상단에**, 이어서
**리뷰어의 예상 반론을 증거와 함께 선제 대응**, **사인오프가 필요한 이해관계자를
이름으로 명시**한다.【검증】 방법론적 의미: 구현이 끝나도 "타인의 승인"이라는
unknown이 남는다. 리뷰어가 물을 것을 미리 알면 그것은 known이 된다.

### 3.11 Quiz Me Before I Merge (구현 후)

멀티 파일 diff에 대한 머지 준비도 평가. **6문항 퀴즈**로 끝나며(통과 요구),
**오답을 고르면 다시 봐야 할 정확한 섹션으로 라우팅**된다.【검증】 방법론적 의미:
모델이 대부분 구현한 작업에서도 사용자는 결과를 설명할 수 있어야 한다("stay in the
loop"). 이해의 공백 자체를 unknown으로 취급해 머지 전에 측정한다. 강연 원문:
"quiz me… so I can represent this work when I'm creating a PR or merging it."

## 4. 11개 예시를 관통하는 설계 패턴

세 가지 공통 패턴이 관찰된다.【추정 — 패턴 추출은 조사자 분석, 개별 근거는 §3】

**패턴 1 — 자기완결 단일 HTML.** 11개 전부 "self-contained `.html` artifacts"로
명시된다. 외부 의존성 없이 파일 하나로 열리고, 저장·공유·재열람이 가능하다.

**패턴 2 — 반응-조립(reaction-to-reply) UI.** 거의 모든 데모가 사용자의 반응을
**구조화된 다음 입력으로 자동 조립**하는 장치를 갖는다: 복사 가능한 프롬프트 픽스
(3.1), 채택/제외 칩 → 회신 템플릿(3.3), A/B 선택 → 자동 채움 회신(3.4), 공감 체크
→ 구조화 응답(3.5), 결정 테이블 → 구현 프롬프트(3.6), 대안 토글(3.8), 오답 →
섹션 라우팅(3.11). 부모 글의 표현으로 "the loop stays tight" — 산출물을 읽는 행위가
곧 다음 에이전트 입력의 생산이 되도록 설계돼 있다. 이것이 이 페이지가 단순한
"HTML로 예쁘게"가 아닌 이유의 핵심이다.

**패턴 3 — 시점 분담.** 구현 전(8개)에 unknowns 발견 비용을 집중 투자하고, 구현 중
(1개)에는 이탈 기록만, 구현 후(2개)에는 이해 검증과 승인 획득을 배치한다. 비용
구조가 "저렴한 탐색을 앞에, 비싼 확정을 뒤에"로 일관된다.

## 5. 부모 글 "The unreasonable effectiveness of HTML"과의 관계

부모 페이지의 테제: AI 에이전트는 마크다운 문서 대신 자기완결 HTML을 산출해야 하며,
이는 "훑고 넘기는(skim) 문서를 실제로 읽는 문서로" 바꾼다.【검증】 부모 페이지는
9개 카테고리(탐색·계획 / 코드 리뷰·이해 / 디자인 / 프로토타이핑 / 일러스트·다이어그램
/ 덱 / 리서치·학습 / 리포트 / 커스텀 편집 인터페이스)에 걸쳐 별도의 데모 약 19개를
제시하고, unknowns 페이지를 "11개 추가 예시의 병렬 전시"로 링크한다.【단일 — 카테고리
구성은 1회 페치 기준】 즉 unknowns 페이지는 HTML-효과성 테제의 **불확실성 관리 특화
응용판**이다.

## 6. 강연 "Field Guide to Fable"과의 관계

같은 저자의 AI Engineer World's Fair 2026 키노트(영상: youtube.com/watch?v=9fubhllmsBU)
와 이 페이지는 동일 방법론의 두 표현이다. 강연은 blindspot pass, 발산형 프로토타입
4개, 구현 전 인터뷰, 레퍼런스=지도, implementation notes, 작업 후 퀴즈의 6개 기법을
구두로 설명했고(타임스탬프별 대조는 플러그인 레포의
`skills/loop/references/talk-source.md`), unknowns 페이지는 여기에 **teach-me,
brainstorm, tweakable plan, buy-in doc, mock-before-wireframe의 5개 아티팩트를
추가**하고 전부를 작동하는 데모로 구현했다. 강연이 원리 선언이라면 이 페이지가
실행 사양에 가깝다.【추정 — "실행 사양" 평가는 조사자 해석】

## 7. 세션 내 갭 분석: 플러그인 대조 (조사 시점 기준 v0.1.2)

이 조사는 `ajitta/field-guide` 플러그인(v0.1.2, 스킬 7종·에이전트 2종·훅 1종)을
원문과 대조하기 위해 수행됐다. 대조 결과:

| # | 원문 예시 | v0.1.2 스킬 | 판정 |
|---|-----------|-------------|------|
| 1 | Blindspot Pass | blindspot + unknowns-scout | 커버 |
| 2 | Teach Me My Unknowns | — | **누락** |
| 3 | Four Design Directions | prototypes | 커버 |
| 4 | Mock before you wire | prototypes(부분) | 부분 커버 |
| 5 | Brainstorm the Intervention | — | **누락** |
| 6 | The Interview | interview | 커버 |
| 7 | Point at a Reference | reference-map | 커버 (이해 증명 산출물은 미반영) |
| 8 | The Tweakable Plan | loop 5단계 한 줄 | **개념 미반영** |
| 9 | Implementation Notes | impl-notes + 훅 | 커버 |
| 10 | The Buy-In Doc | — | **누락** |
| 11 | Quiz Me Before I Merge | quiz | 커버 (오답→섹션 라우팅 미반영) |

커버리지 외 발견 문제:

1. **네이밍 불일치** — 플러그인명 `field-guide`는 강연 제목에서 온 것으로 기능을
   설명하지 못함. 방법론의 실핵심 개념은 원문 제목 그대로 "unknowns". 스킬
   `reference-map`은 "레퍼런스 지도 생성"으로 오독 가능(실제는 레퍼런스 분석),
   `impl-notes`는 축약어, `loop`는 네임스페이스 없이는 무슨 루프인지 불명.
2. **형식 갭** — 원문 11개 전부 반응-조립 UI가 달린 인터랙티브 HTML(§4 패턴 2)인데
   플러그인 산출물은 마크다운 테이블 중심. 방법론의 절반이 빠진 상태.
3. **문서 오프바이원** — loop SKILL.md와 README가 "9단계"라 쓰고 0~9단계(10개)를
   나열. "7단계에서 independent-reviewer 자동 호출" 참조도 ①~⑩ 번호와 어긋남.
4. **훅 결함** — session_id를 파일명에 무검증 사용(경로문자 포함 가능), 세션당 1회
   고정이라 긴 세션에서 리마인더 공백, 리마인더 메시지에 `/field-guide:impl-notes`
   플러그인명 하드코딩(리네임 시 파손).
5. **출처 누락** — talk-source.md에 강연·"HTML is the new markdown"은 있으나 정작
   이 unknowns 페이지 링크가 없었음.

## 8. 적용된 리팩토링 (v0.2.0, 2026-07-11)

위 분석에 따라 같은 세션에서 다음을 적용했다 (사용자 확인 후 진행):

- **이름**: 플러그인 `field-guide` → `unknowns` (호출 `/unknowns:<스킬>`), 레포
  `ajitta/field-guide` → `ajitta/know-your-unknowns`(원문 제목). 스킬
  `reference-map` → `reference`, `impl-notes` → `notes`. 근거: 짧은 네임스페이스가
  일상 사용성을 결정하고, 레포명은 GitHub에서 자기설명적이어야 함 — 두 요구를
  플러그인명/레포명 분리로 동시 충족.
- **신규 스킬 4종**: `teach-me`(§3.2), `brainstorm`(§3.5), `plan`(§3.8),
  `buy-in`(§3.10) — 원문 11개 예시와 1:1 대응 완성. §3.4는 `prototypes`의
  인터랙션 목업 변형으로 흡수.
- **HTML 우선 산출물 원칙**: 반응이 필요한 스킬마다 "산출물 형식(HTML 우선)" 절
  추가 — 단일 파일·인라인 CSS/JS·반응-조립 UI(채택/제외 칩, 공감 체크, 복사 가능한
  프롬프트 픽스, 선택→회신 자동 조립)·마크다운 폴백. §3.7의 이해 증명(semantics
  map), §3.9의 "다음 시도 개선점", §3.11의 오답→섹션 라우팅도 각 스킬에 반영.
- **버그 수정**: loop 1~10단계로 재번호. 훅 session_id 정규화
  (`[^A-Za-z0-9._-]` → `_`), `UNKNOWNS_NOTES_THRESHOLD`/`UNKNOWNS_NOTES_REPEAT`
  (임계값 배수 반복 옵션) 도입, 구 `FIELD_GUIDE_NOTES_THRESHOLD` 호환 유지.
  실행 테스트로 발동 시점(단발 3회차/반복 2·4·6회차) 검증.
- **출처 보강**: talk-source.md에 unknowns 페이지·부모 페이지 링크와 11개 예시
  매핑표 추가.

## 9. 조사의 한계와 확실성

- 원문은 JS 렌더링 페이지이며 텍스트 추출로 조사했다. 3회 페치 결과가 서로
  모순되지 않았고 핵심 사실(제목, 프레임 문장, 11개 구성, 시점 분류, 주요 인터랙션
  장치)은 전부 2회 이상 일치했다 — 이 부분은 높은 확신.
- 각 데모의 **내부 인터랙션 전체**(예: 슬라이더의 정확한 파라미터, 카드의 전체 문안)
  는 실행해 보지 않았으므로 기술 수준은 요약 정확도에 그친다. 【단일】 표기 항목
  (디자인 4종 스타일명, 부모 페이지 카테고리 구성, 맺음 문장)은 단일 페치 근거로
  오류 가능성이 상대적으로 높다.
- 저자 귀속은 정황 근거의 결합이며 페이지 내 명시가 아니다(§1).
- 2×2 매트릭스의 사분면별 설명 텍스트는 추출되지 않아 라벨만 기록했다.

## 10. 참고 자료

- Thariq Shihipar, "Know your unknowns — examples":
  https://thariqs.github.io/html-effectiveness/unknowns/
- Thariq Shihipar, "The unreasonable effectiveness of HTML — examples":
  https://thariqs.github.io/html-effectiveness/
- Thariq Shihipar, "Field Guide to Fable" 키노트 (AI Engineer World's Fair 2026):
  https://www.youtube.com/watch?v=9fubhllmsBU
- 플러그인 내 검증 문서: `skills/loop/references/talk-source.md`
  (강연 타임스탬프 대조, 외부 사실검증: Korzybski 1931, Johari 1955, Rumsfeld 2002,
  Jack Clark "capability overhang", Aschenbrenner "unhobbling", Olah "grown not
  designed" 등)
- Thariq Shihipar, "HTML is the new markdown" (Lenny's Newsletter, 2026-05-18)
