# 출처와 검증 — Know your unknowns

이 플러그인은 Thariq Shihipar(Anthropic, Claude Code 팀)의 두 자료를 기반으로 한다:

1. **강연** — AI Engineer World's Fair 2026 키노트 "Field Guide to Fable"
   (2026-06-29~07-02, 샌프란시스코). 영상: https://www.youtube.com/watch?v=9fubhllmsBU
2. **예시 모음** — "Know your unknowns" (블로그 "The unreasonable effectiveness of
   HTML"의 컴패니언 페이지, 11개 인터랙티브 예시):
   https://thariqs.github.io/html-effectiveness/unknowns/
   부모 페이지: https://thariqs.github.io/html-effectiveness/

플러그인·레포 이름(unknowns / know-your-unknowns)은 2번 자료의 제목에서 왔다 —
방법론의 핵심 프레임이 "지도는 영토가 아니다; 그 간극이 unknowns"이기 때문이다.

## "Know your unknowns" 11개 예시 ↔ 플러그인 매핑

| # | 원문 예시 | 시점 | 플러그인 구성요소 |
|---|-----------|------|------------------|
| 1 | Blindspot Pass | 구현 전 | `blindspot` skill + `unknowns-scout` agent |
| 2 | Teach Me My Unknowns | 구현 전 | `teach-me` skill |
| 3 | Four Design Directions | 구현 전 | `prototypes` skill |
| 4 | Mock Before You Wireframe | 구현 전 | `prototypes` skill (인터랙션 목업 변형) |
| 5 | Brainstorm the Intervention | 구현 전 | `brainstorm` skill |
| 6 | The Interview | 구현 전 | `interview` skill |
| 7 | Point at a Reference | 구현 전 | `reference` skill |
| 8 | The Tweakable Plan | 구현 전 | `plan` skill |
| 9 | Implementation Notes | 구현 중 | `notes` skill + reminder hook |
| 10 | The Buy-In Doc | 구현 후 | `buy-in` skill |
| 11 | Quiz Me Before I Merge | 구현 후 | `quiz` skill |

`loop` 스킬은 위 기법들을 순서대로 꿰는 오케스트레이터, `independent-reviewer`
에이전트는 8번과 11번 사이의 독립 검증(플러그인 확장분)이다.

원문 예시들의 공통 형식 — **반응-조립 UI가 달린 단일 파일 인터랙티브 HTML**
(채택/제외 칩, 공감 체크박스, 복사 가능한 프롬프트 픽스, 선택 → 회신 템플릿 자동
조립) — 은 0.2.0부터 문서형 산출물을 내는 스킬들의 "산출물 형식 (HTML 우선)" 절에
반영되어 있다 (`quiz`는 "HTML 옵션" 절). 의도적 예외 둘: `interview`는
AskUserQuestion 대화로 반응-조립을 직접 수행하므로 별도 HTML이 필요 없고,
`notes`는 원문대로 마크다운 파일 로그(`IMPLEMENTATION_NOTES.md`)가 산출물이다.
근거: 부모 글의 주장 "읽지 않고 넘기는(skim) 문서를 실제로 읽는 문서로 바꾸고,
반응을 다시 에이전트가 읽을 수 있는 형태로 내보내 루프를 짧게 유지한다."

## 강연에서 직접 검증된 기법 (강연 시점)

| 기법 | 강연 시점 | 플러그인 구성요소 |
|------|-----------|------------------|
| Blind-spot pass ("unknown unknowns를 찾아 프롬프트를 개선") | 10:48–11:39 | `blindspot` skill + `unknowns-scout` agent |
| 발산형 프로토타입 4개 ("I have no visual taste… four widely different design decisions") | 11:39–12:28 | `prototypes` skill |
| 구현 전 인터뷰 ("prioritize questions that would change the architecture") | 12:28–12:58 | `interview` skill |
| 레퍼런스 = 다른 지도 ("give it another map") | 12:58–13:35 | `reference` skill |
| Implementation notes ("runs into an unknown, ask it to log it") | 13:35–13:57 | `notes` skill + reminder hook |
| 작업 후 퀴즈 ("quiz me… so I can represent this work") | 13:57–14:23 | `quiz` skill |

## 강연의 핵심 개념 (외부 사실검증 완료)

- **Capability overhang** — 모델은 스파이크형으로 똑똑해지며, 도구(harness)가 잠재 능력을
  해방한다. 용어는 Jack Clark(Anthropic 공동창업자, Import AI #321, 2023)가 대중화.
- **Unhobbling** — Leopold Aschenbrenner, "Situational Awareness" (2024-06)에서 정립.
  컴퓨트·알고리즘과 함께 진보의 3대 동력으로 제시.
- **"Models are grown, not designed"** — Chris Olah(Anthropic 공동창업자, 해석가능성 책임자)
  의 표현. "On the Biology of a Large Language Model" (Transformer Circuits, 2025-03-27,
  Claude 3.5 Haiku 회로 추적) 제목의 배경.
- **포켓몬 사례** — 영어 이름이 "aw"로 끝나는 포켓몬은 전 세대(1,025종, Gen 9까지) 중
  정확히 2종: Croconaw(#159), Drednaw(#834). PokeAPI 정본 데이터로 프로그램 검증.
- **시스템 프롬프트 80% 감축** — The Decoder(2026-07-02) 등 복수 매체가 강연을 인용 보도.
  "예제가 모델의 상상력을 제약한다 — 금지 대신 컨텍스트를." 공식 Anthropic 프롬프팅 문서도
  최신 모델에 대해 "give context, not constraints"와 과잉 지시 완화를 권고.
- **지도-영토** — Alfred Korzybski(1931). known/unknown 매트릭스 — Rumsfeld(2002) 브리핑
  형식 + Johari window(1955) 계열.
- **Good/fast/cheap** — 프로젝트 관리 삼각형("pick two")의 의도적 전복: "이제는 pick three.
  현실이 트레이드오프를 증명하게 하라."
- **관련 후속 자료** — Thariq, "HTML is the new markdown" (Lenny's Newsletter, 2026-05-18);
  Anthropic, "Claude Code: Best practices for agentic coding".

## 플러그인 제작 시 확장한 부분 (원문에 없음 — 설계 판단)

- 각 스킬의 구체적 프롬프트 템플릿·절차·우선순위 목록 (원문은 예시 시연)
- `IMPLEMENTATION_NOTES.md` 파일명·항목 형식 (강연은 "log it"만 언급)
- `loop` 스킬의 10단계 워크플로와 규모별 축소 기준
- `independent-reviewer` 에이전트 (강연의 "stay in the loop" 정신의 확장)
- 파일 수정 횟수 기반 리마인더 훅

주의: "트레이드오프는 없다"는 문자 그대로가 아니라 **과거의 비용 구조를 근거로 너무 일찍
타협하지 말라**는 뜻으로 적용한다. 모델 사용료, 검증 시간, 보안, 기술부채는 여전히 실재한다.
