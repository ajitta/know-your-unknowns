# know-your-unknowns

**Language**: [English](README.md) | 한국어

> 지도는 영토가 아니다 — 그 간극이 당신의 unknowns다.

**강한 모델의 병목은 모델이 아니라, 지도(계획)와 영토(실제 코드·도메인·제약)를 일치시키는
당신의 능력이다.** 이 플러그인은 그 간극을 구현 전·중·후에 걸쳐 찾고 관리하는 운영 루프를
제공합니다 — 스킬 11종과 Claude Code 에이전트 2종.

구체적으로 얻는 것:

- 몰랐던 것을 PR 이후가 아니라 **프롬프트를 쓰기 전에** 발견합니다.
- 보고 반응해야 하는 산출물은 **대화의 마크다운**으로 나오며, 번호가 붙은 항목과 복사할 수 있는 조립된 회신을 담습니다. 항목 번호를 고르거나 원하는 수정을 말하면 됩니다.
- 스킬 지시가 단계 경계와 턴을 끝내기 전에 계획 이탈을 기록합니다. 자동 리마인더는 실행되지 않습니다.

> **측정 상태: 미측정(unmeasured).** 가치 계약([`docs/value-contract.md`](docs/value-contract.md))은
> 이 플러그인이 "사용자가 몰랐던 것을 드러내고 **그것이 결정을 바꿀 때**"만 제 값을 한다고
> 못 박았습니다. 지표는 10행 롤링 윈도우인데 스코어카드는 2행(2026-07-11, 2026-09-20)이고,
> 그 사이 공백이 계약 자신의 60일 경계를 넘겼습니다. 위 세 항목은 측정된 결과가 아니라
> 설계 의도입니다.

Thariq Shihipar(Anthropic, Claude Code 팀)의 방법론을 패키징했습니다. 두 자료가 원 출처입니다:
강연 **"Field Guide to Fable"**(AI Engineer World's Fair 2026 키노트)과 예시 모음
**"Know your unknowns"**(11개 인터랙티브 예시) —
https://thariqs.github.io/html-effectiveness/unknowns/. 스킬 11종이 원문 11개 예시를 모두
커버합니다(prototypes가 2개를 커버, loop는 원문 대응이 없는 오케스트레이터). 사실검증
상세는 [`docs/talk-source.md`](https://github.com/ajitta/know-your-unknowns/blob/main/docs/talk-source.md) 참조.

---

## 빠른 시작

Claude Code 세션 안에서 마켓플레이스로 설치합니다:

```
/plugin marketplace add ajitta/know-your-unknowns
/plugin install unknowns@know-your-unknowns
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

나머지 설치 경로(클론·개별 복사·데스크톱)는 아래 [설치](#설치)에 있습니다.

---

## 스킬 한눈에 보기

원문 11개 예시 커버 — prototypes가 2개 커버, loop는 오케스트레이터.

| 시점 | 스킬 | 하는 일 | 원문 예시 |
|---|---|---|---|
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

플러그인은 `unknowns`입니다. Claude Code에서는 `/unknowns:<skill>`을 쓰고, 다른 표면에서는 스킬 이름이나 트리거 문구로 부릅니다.

**ChatGPT와 Codex 동작: 예상이며 소유자가 아직 확인하지 않았습니다.** 재구성한 패키지의 업로드·모바일 로딩·기기 간 동작도 미측정입니다.

### claude.ai 웹과 Claude 데스크톱

1. Customize › Plugins › Add › Add marketplace에서 `ajitta/know-your-unknowns`를 입력합니다.
2. Discover에서 `unknowns` 플러그인을 선택하고 Add를 누릅니다. 마켓플레이스만 추가하면 플러그인은 설치되지 않습니다.
3. "blind spot pass"처럼 스킬 이름이나 문구로 요청합니다.

1·2단계 대신 Customize › Plugins › Add › Upload plugin에서 [know-your-unknowns.zip](https://github.com/ajitta/know-your-unknowns/releases/latest/download/know-your-unknowns.zip)을 올려도 됩니다. Skills가 아니라 Plugins 업로드를 쓰세요. [Claude 공식 설치 안내](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)는 웹·데스크톱 플러그인이 계정에 저장되고 지원 표면에 따라온다고 설명합니다. 이 플러그인의 모바일·데스크톱 동기화는 소유자가 아직 확인하지 않았습니다.

### Claude 모바일

1. 위 절차대로 claude.ai 웹에 플러그인을 설치합니다.
2. 같은 계정의 모바일 앱을 열고 스킬 이름이나 트리거 문구로 요청합니다.
3. 스킬 절차를 따르는지 확인합니다. 재구성한 패키지의 로딩과 계정 동기화는 소유자 확인이 아직 필요합니다.

### Claude Code

1. Claude Code 세션 안에서 실행합니다:

   ```
   /plugin marketplace add ajitta/know-your-unknowns
   /plugin install unknowns@know-your-unknowns
   ```

2. 새 세션을 시작하거나 `/reload-plugins`를 실행합니다.
3. `/unknowns:blindspot 테스트`를 호출해 구현 전에 조사하는지 확인합니다.

### Codex CLI

1. 마켓플레이스와 플러그인을 추가합니다:

   ```
   codex plugin marketplace add ajitta/know-your-unknowns
   codex plugin add unknowns@know-your-unknowns
   ```

2. `$unknowns:plan`처럼 스코프가 있는 스킬 이름 뒤에 작업을 적어 요청합니다.
3. 절차와 도구 폴백을 확인합니다. 이 경로는 예상이며 소유자가 아직 확인하지 않았습니다.

### ChatGPT 데스크톱(Codex 포함)과 모바일

두 경로에서의 동작은 **이 플러그인에서는 소유자가 아직 확인하지 않았습니다**.

1. **웹에서 zip 업로드(웹·모바일).** [know-your-unknowns-openai.zip](https://github.com/ajitta/know-your-unknowns/releases/latest/download/know-your-unknowns-openai.zip)을 내려받아 chatgpt.com의 플러그인 zip 업로드로 올립니다. 플러그인은 계정에 저장되어 ChatGPT 웹·모바일에서 사용합니다. 이 zip에는 OpenAI 매니페스트·스킬·목록용 자산이 들어 있습니다. 업로드는 자동으로 갱신되지 않으므로 새 릴리스마다 다시 올립니다.
2. **데스크톱 앱에서 마켓플레이스 추가.** 앱의 Codex 플러그인 화면에서 GitHub 마켓플레이스 `ajitta/know-your-unknowns` 또는 로컬 클론을 추가하고 `unknowns`를 선택해 설치합니다. 이 경로는 데스크톱 앱의 로컬 Codex 폴더에 설치하며 웹·모바일용 계정에 저장되지 않습니다. 업데이트는 마켓플레이스로 받습니다.

### Windows

1. 위에서 사용하는 호스트의 경로를 같은 패키지로 따릅니다.
2. 설치된 플러그인은 지시문과 목록용 자산만 싣기 때문에 Python이나 셸이 필요 없습니다.
3. 소스에서 빌드하는 개발자에게는 Python이 필요합니다. 아래 개발 명령의 `python3` 대신 `py -3`을 쓰세요. 재구성한 패키지는 Windows에서 로컬 실행하지 않았으며, 이전 Windows 훅 검사는 CI에서만 했고 이제 훅은 삭제되었습니다.

### 표면별 지원

- 스킬 11종은 모두 대화에 마크다운을 내고 번호로 반응을 받아 회신을 조립합니다. 질문·파일·검색·실행 도구가 없을 때의 폴백이 명시되어 있습니다.
- 이름 있는 에이전트 2종은 Claude Code에서만 실행됩니다. 다른 표면에서는 어시스턴트가 스카우트 패스를 직접 수행하고, 독립 검증은 같은 패킷을 새 대화에 붙여 넣도록 전달하여 그 리뷰가 에이전트를 대신합니다. 리뷰가 돌아올 때까지 해당 단계는 미완료로 둡니다.
- 어떤 표면에서도 설치된 패키지에 훅이나 스크립트는 없습니다. 작업 중 요청한 실행 가능한 프로토타입은 호스트가 지원하면 여전히 코드 파일로 쓸 수 있습니다.
- 트래커·스코어카드·이탈 로그는 파일을 쓸 수 있으면 파일에 저장합니다. 그렇지 않으면 전체 기록을 마크다운으로 출력하고 사용자가 무엇을 저장해야 하는지 말합니다.

### 클론에서 바로 실행

생성된 플러그인 폴더를 사용합니다:

```bash
git clone https://github.com/ajitta/know-your-unknowns.git
claude --plugin-dir ./know-your-unknowns/plugins/unknowns
```

커밋된 생성물은 바로 로드할 수 있습니다. 소스를 고친 뒤에는 개발 절의 명령으로 다시 생성하세요.

### 개별 스킬 복사

`plugins/unknowns/skills/<name>/`의 폴더 전체를 `references/`와 `agents/openai.yaml`까지 복사합니다. `skills/`의 소스 폴더는 빌드가 복사해 넣는 공용 loop 참조에 의존할 수 있습니다.

Claude Code의 `.claude/skills/`에 복사하면서 에이전트 이름의 네임스페이스를 빼려면:

```bash
python3 scripts/build-skill-zips.py --target local
```

`dist/local/`에서 원하는 폴더를 복사합니다. 선택적으로 에이전트 프롬프트를 `claude-code/agents/*.md`에서 `.claude/agents/`로 복사할 수 있습니다. 호출은 `/blindspot`, `/quiz`처럼 짧아집니다.

Customize › Skills에서 스킬을 하나씩 받는 호스트용으로는:

```bash
python3 scripts/build-skill-zips.py
```

원하는 `dist/<skill>.zip`을 올리세요. `scripts/skill-descriptions.json`의 짧은 설명을 쓰며, 트리거 포함 테스트가 그 설명도 확인합니다.

### 업데이트

자체 마켓플레이스용 명령입니다:

```
/plugin marketplace update know-your-unknowns
/plugin update unknowns@know-your-unknowns
/reload-plugins
```

설치본 업데이트에는 플러그인 버전 변경이 필요합니다. 업로드 설치본은 새 아카이브로 교체해야 합니다. 카탈로그 [ajitta/claude-plugins](https://github.com/ajitta/claude-plugins)도 대안 마켓플레이스이며, 그쪽 설치명은 계속 `unknowns@ajitta`입니다.

### 0.1.x(field-guide)에서 업그레이드

옛 플러그인 이름은 `field-guide`였습니다. 해당 설치본을 지우고 `unknowns`를 추가합니다:

```
/plugin uninstall field-guide@ajitta
/plugin marketplace add ajitta/know-your-unknowns
/plugin install unknowns@know-your-unknowns
```

옛 저장소 URL(`ajitta/field-guide`)은 리다이렉트됩니다. 스킬 대응은 `reference-map` → `reference`, `impl-notes` → `notes`이며 나머지 이름은 같습니다.

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
`/unknowns:loop resume`은 멈춘 지점에서 이어갑니다. 스킬이 컴팩션 후나 재개 시 트래커를 읽으며 자동 리마인더는 없습니다. 파일 시스템이 없으면 전체 트래커를 마크다운으로 다시 출력하므로 저장해 두었다가 다음 대화에 제공하세요.

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
호스트가 시작할 수 있으면 `unknowns:unknowns-scout`에 위임하고, 아니면 직접 구분된 scout 패스를 수행합니다. 먼저 대비를 보여줍니다 — 내가 요청한 것
vs 실제로 들어가는 곳, 종류별 집계와 함께. 그다음 발견 1건 = 카드 1장을 밟을 가능성×피해 범위
순으로, 종류를 달아서: **지뢰**(건드리면 티 안 나게 뭔가 깨짐), **관례**(코드베이스가
강제하는 암묵 규칙), **없는 개념**(내 프롬프트에 단어가 없는 메커니즘),
**이력**(코드가 지금 모양이 된 이유를 설명하는 이전 시도·되돌림·막다른 길).

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

**진행 방식**: 라운드당 **4개 이하** 질문에 선택지 2–4개를 붙여 고정 우선순위(아키텍처 → 데이터 손실·보안 → 호환성 → 성능·비용 → 취향)로 묻습니다. 질문 도구가 있으면 쓰되 도구가 더 적게 받으면 호출을 나누고, 없으면 대화에 번호를 붙여 묻습니다. 각 질문에 "왜 중요한지" 한 줄, 각 선택지에
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
이름 + 철학 한 줄 + 장단점 + 적합 조건이 붙습니다. 번호를 붙인 마크다운 비교에서 각 요소에 **채택(steal)/제외(skip)**로 반응하면 선택이 요구사항 목록 초안으로 조립됩니다. 호스트가 지원하면 실행 가능한 프로토타입을 파일로 쓰되 비교 자체는 대화에 남깁니다.

**반응하는 법**: `"2안의 레이아웃 + 4안의 색 + 1안의 필터"` 처럼 조합을 말하면
그것을 **명시적 요구사항 목록**으로 변환한 뒤에야 본 구현을 시작합니다.

**팁**: `"wild하게"` 라고 하면 철학 간 거리를 더 벌립니다. 코드 아키텍처 비교에도
사용 가능: `"이벤트 기반 vs 폴링 vs 푸시, 스켈레톤으로 나란히"`. 인터랙션 자체가
쟁점이면(툴바 위치 등) 파일 도구가 있을 때 클릭 가능한 목업과 A/B 선택 버튼을 만들고, 전부 가짜 데이터라는 사실과 실제 배선이 들어갈 자리를 명시합니다. 파일이나 실행 도구가 없으면 제안 코드나 목업 상태를 보여 주고 실행하지 못한 것을 밝힙니다.

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
효과×노력 표로 quick win과 big bet을 구분하고, **공감(resonate)**한 항목 번호가 각 개입의 첫 실행 프롬프트까지 내려간 구조화된 다음 단계로 조립됩니다.

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
부분**. 구현 전에는 **이해 증명(semantics map)** — 번호가 붙은 레퍼런스 발췌 ↔ 대응
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

**진행 방식**: 먼저 규모 게이트가 있습니다 — 계획된 구현이 파일 2개 이하를 만들거나 수정하고 스키마·인터페이스·UX 계약
결정이 없는 작업은 문서를 만들지 않고 네이티브 플랜 모드로 넘깁니다. 그 외에는 실행
순서가 아니라 **수정될 확률 순**으로 제시합니다: 스키마·인터페이스·UX 계약 같은 결정
항목이 맨 위, 각 항목에 고려한 대안과 파급 범위가 붙고, 새로 생기거나 바뀌는 공개
타입·스키마는 주석 달린 코드로 제시하며, 기계적 작업은 결정 항목 뒤에 요약과 상세로 둡니다. 승인/변경 요청
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
막지 않고 아키텍처·사용자에게 보이는 동작·데이터·보안을 건드리지 않는 판단 — 건드리면 멈추고
묻습니다).

**지속성**: 파일 시스템을 쓸 수 있으면 노트 파일에 덧붙이고, 파일이 없으면 만듭니다. buy-in과 quiz가 그 기록을 씁니다. 파일 시스템이 없으면 전체 갱신 로그를 마크다운으로 출력하고 IMPLEMENTATION_NOTES.md로 저장하라고 안내합니다. 턴 종료 전, 단계 경계, 커밋 전에 직접 이탈 여부를 확인합니다.

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
정답**(객관식 5개는 4 + 1로 나누되 도구 제한이 더 작으면 호출을 더 나누고, 1개는 자기 말로 설명하는 티치백), 장애 대응 > 설계 이유 >
동작 예측 순이며 암기는 지양; IMPLEMENTATION_NOTES.md가 있으면 기록된 이탈 지점 최소 1개
포함 → ③ 채점 — 오답·무응답은 다시 읽을 변경 지점을 정확히 가리키고 재시도를 줍니다. 채점은 대화에서 하며, 티치백 키는 답변 전까지 숨기고 사전 키 파일이 없으면 이를 밝힙니다 →
④ 6/6이면 **머지 가능(cleared to merge)** 체크리스트(퀴즈 6/6 통과, CI 그린,
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

이름 있는 에이전트는 Claude Code에서만 실행됩니다. **실효** 도구 집합은 선언된 목록을 호스트가 노출하는 도구로 좁힌 결과입니다. scout은 Read·Grep·Glob·WebFetch·WebSearch만 가지며 Bash나 쓰기 도구는 없습니다. 읽을 수 있는 이력 기록을 보고 명령 실행이 필요한 질문은 호출자에게 돌려줍니다. 다른 호스트에서는 구분된 스카우트 패스를 사용하고, 독립 검증은 패킷을 새 대화에 붙여 넣도록 사용자에게 전달한 뒤 그 리뷰를 기다립니다.

**unknowns-scout** (읽기 전용 정찰):
```
Use the unknowns-scout agent — 마이그레이션 계획에서 내가 놓친 것 조사
unknowns-scout 에이전트로 인증 모듈 정찰해줘
```
blindspot 스킬이 큰 조사에서 자동으로 이 에이전트를 부르고, brainstorm 스킬이 기존 코드
목록을 만들 때 쓰기도 합니다. 그 밖에는 이름으로 부를 때만 돕니다 — 다른 워크플로가 조사용
서브에이전트를 찾으면 그 워크플로의 에이전트, Explore 또는 일반 에이전트로 갑니다. 대상 영역 구조를
훑고, 읽을 수 있는 이력 기록에서 지저분한 막다른 길과 되돌려진 커밋을 보고, 테스트 커버리지와 암묵
관례를 확인하며, 낯선 라이브러리라면 *설치된* 버전의 공식 문서·체인지로그까지 봅니다
(그래서 읽기 도구와 함께 WebFetch·WebSearch를 가집니다). 밟을 가능성×피해 범위 순 조사 테이블과
개선된 프롬프트 초안을 돌려줍니다. 도구 목록이 읽기와 검색만 허용하고, 프롬프트도 파일 수정과 발견 사항의 날조를 금지합니다.

**independent-reviewer** (독립 검증):
```
Use the independent-reviewer agent — 방금 구현 머지 전 검증
unknowns independent-reviewer로 이 브랜치를 계획 대비 검증해줘
```
구현한 세션의 설명을 **주장으로만 취급**하고 코드·테스트 실행으로 직접 확인합니다. 다섯 가지
점검 항목은 일반 코드 리뷰가 다루지 않는 것들로 의도적으로 좁혀져 있습니다:
**계획·스펙 부합**(요구사항마다 충족/부분/누락 판정), **기록된 이탈을 혼자 결정해도
괜찮았는지**, **테스트는 통과하는데 현실은 깨지는 경우**(목이 가린 실제 의존성, 구현을
그대로 비추기만 하는 테스트), **확인 완료 목록**(침묵은 검토 안 함과 구분되지 않기
때문), 그리고 **주장 유형별 검증**(사실 주장은 원출처와 대조하고, 추론은 전제와 반례를
검사). 패킷에 완료 조건이 없으면 추측하지 않고 "부합 판정 불가"로 보고하고, 확인하지 못한
영역을 끝에 따로 적습니다. 일반적인 버그·보안 사냥은 같은 diff에 대한 `/code-review`와
`/security-review`의 몫이니 함께 돌리세요. 에이전트도 늘 에러
처리·보안·성능·불필요한 복잡도를 2차 패스로 직접 커버합니다. 테스트·린트·빌드용 Bash는 유지하되 편집·커밋·의존성 설치·임시 디렉터리 밖 쓰기를 금지합니다. 이 읽기 전용 계약은 지시문뿐이며 훅이나 permission mode가 강제하지 않습니다. loop 스킬 8단계에서 자동
호출됩니다. 그 밖에는 이름으로 부를 때만 돕니다 — 이름 없는 "독립 리뷰" 요청은 다른 리뷰
도구나 일반 에이전트로 갑니다.

---

## 추천 시나리오

**시나리오 A — 작은 수정** (파일 1–2개, 명확한 스펙):
루프 불필요. 그냥 구현하되 notes 규칙을 적용하고 턴 종료 전에 중요한 이탈을 기록합니다.

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
`/unknowns:blindspot`. 설치 직후라면 새 세션을 시작하거나 `/reload-plugins`. 스킬을 많이
설치했다면 원인이 하나 더 있습니다: Claude Code는 스킬 목록에 예산(기본 컨텍스트 창의 1%)을
두고, 넘치면 **많이 쓰는 스킬(최근성 가중)만** 설명을 남기고 나머지는 이름만 보여 줍니다.
위험한 것은 내가 드물게 쓰는 unknowns 스킬이고, 스스로 떠야 하는 notes에서 특히 큽니다.
unknowns 설명이 전부 빠진 조건(초과는 CLI 로그로 확인, 11개 모두 빠졌다는 것은 탐침 실행의
자기 보고)에서 영어 트리거 11건 중 9건은 여전히 발화했고 notes와
blindspot은 발화하지 않았습니다(1회 측정,
[docs/trigger-eval-crowd-2026-09-30.md](docs/trigger-eval-crowd-2026-09-30.md)).
`/doctor`로 목록 비용을 보고,
`skillListingBudgetFraction` 설정(예: `0.02`)으로 예산을 늘리거나, 드물게 쓰는 다른 스킬을
`skillOverrides`에서 `"name-only"`로 두세요(플러그인 스킬에는 적용되지 않으므로 이 스킬들을
보호하는 게 아니라 자리를 비우는 방법입니다). eval의 `--crowd N` 옵션이 이 경우를 잽니다.

**Q. `/unknowns:blindspot` 대신 `/blindspot`이라고 쳐도 되나요?**
대부분은 됩니다. 플러그인 스킬은 스코프 이름으로도, 맨 이름으로도 호출됩니다 — 같은 이름을
쓰는 다른 명령이 없는 한. 그래서 `/blindspot`, `/quiz`는 그냥 동작합니다. 예외는 `loop`로,
Claude Code가 자체 `loop` 스킬(반복 인터벌 러너)을 싣고 있어 맨 `/loop`는 그쪽으로 가고 이
플러그인의 루프는 항상 `/unknowns:loop`가 필요합니다. 스코프 형식은 절대 모호하지 않아서
이 README는 그쪽을 씁니다.

**Q. 예전에 field-guide로 설치했는데요.**
0.1.x의 옛 이름입니다. 위 "0.1.x(field-guide)에서 업그레이드"를 따라 제거 후 재설치하세요.

**Q. 인터랙티브 페이지는 어디 있나요?**
이제 산출물은 대화의 마크다운입니다. 항목 번호나 원하는 수정을 답하면 어시스턴트가 다음 프롬프트나 요구사항 목록을 조립합니다. 작업용 실행 프로토타입은 여전히 파일로 쓸 수 있지만, 공용 프레젠테이션 페이지를 생성하지는 않습니다.

**Q. 원문과 플러그인이 다른 부분은?**
[`docs/talk-source.md`](https://github.com/ajitta/know-your-unknowns/blob/main/docs/talk-source.md)에 "원문에서 직접 검증된 부분"과
"제작 시 확장한 부분"이 표로 구분되어 있습니다.

---

## 저장소 구조

```
skills/<name>/                 소스: SKILL.md, references/, agents/openai.yaml
skills/loop/references/         빌드가 전이적으로 복사하는 공용 참조
claude-code/agents/             소스: Claude Code 에이전트 프롬프트
plugin-manifest.json           소스 매니페스트, 현재 0.10.0
packaging/                     배포 README, 목록 아이콘, OpenAI 인터페이스와 SVG
.claude-plugin/marketplace.json 마켓플레이스 -> ./plugins/unknowns
plugins/unknowns/               생성된 Claude 플러그인; 설치되는 페이로드
releases/know-your-unknowns.zip 생성된 Claude 아카이브, 최상위 unknowns/
releases/know-your-unknowns-openai.zip
                               생성된 OpenAI 아카이브, 스킬과 목록 자산만 포함
plugin-release.json            생성된 버전과 콘텐츠 다이제스트
tools/package.py               검증, 재생성, 커밋된 생성물 검사
scripts/build-skill-zips.py     선택적인 개별 스킬 업로드/로컬 복사
tests/                         개발용 검사
evals/                         모델 eval 케이스와 수동 러너
docs/                          과거 측정과 방법론 기록
```

## 개발

소스를 고친 뒤 다시 생성하세요. `plugins/unknowns/`나 아카이브를 직접 고치지 않습니다:

```bash
python3 tools/package.py
python3 tools/package.py --check
python3 -m unittest discover -s tests -v
claude plugin validate --strict plugins/unknowns
claude plugin validate --strict .
python3 evals/run-manual.py --verify
```

CHANGELOG.md에 내용이 있는 `## [Unreleased]` 항목이 있으면 배포 콘텐츠가 바뀌어도 같은 버전으로 빌드하고 `plugin-release.json`을 갱신할 수 있습니다. 해당 항목이 없으면 콘텐츠 변경에 버전 올림이 필요합니다. `--check`는 언제나 오래된 생성 파일·아카이브·다이제스트 기록을 거부하므로 먼저 다시 빌드하세요.

릴리스: `plugin-manifest.json`의 버전을 올리고, Unreleased 항목을 새 버전 아래로 옮기고, 다시 빌드한 뒤 CI가 통과하면 머지합니다. 그다음 주석 태그 `unknowns--vX.Y.Z`가 릴리스 워크플로를 실행해 커밋된 zip 둘을 검증하고 첨부합니다. 로컬 빌드로 릴리스가 생성되지는 않습니다.

텍스트는 UTF-8과 LF를 씁니다. 릴리스 아카이브는 바이트 재현성을 위해 ZIP_STORED와 고정 시각·모드를 사용합니다. 패키저는 표준 라이브러리만 사용하고 Python 3.7+를 지원하며, 선택적인 개별 스킬 도우미는 Python 3.9+를 사용합니다.

현재 CI 개발 도구 테스트는 Ubuntu와 Windows를 대상으로 하며, 엄격한 플러그인 검증은 Ubuntu에서 실행됩니다. 새 Windows CI 작업의 실행 결과는 아직 확인하지 않았습니다. 이전 Windows 근거는 삭제된 훅을 CI에서만 검사한 것이며, 재구성한 패키지의 Windows 동작은 미측정입니다. `docs/`의 과거 라우팅 결과는 각 문서가 명시한 버전의 것입니다. 구조 검사는 갱신된 스킬의 동작·로딩·업로드를 측정하지 않습니다.

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
- 검증 상세와 관련 문헌: [`docs/talk-source.md`](https://github.com/ajitta/know-your-unknowns/blob/main/docs/talk-source.md)
