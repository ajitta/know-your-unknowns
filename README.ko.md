# know-your-unknowns

**Language**: [English](README.md) | 한국어

> 지도는 영토가 아니다 — 그 간극이 당신의 unknowns다.

**강한 모델의 병목은 모델이 아니라, 지도(계획)와 영토(실제 상황: 규칙·사람·자료·제약)를
일치시키는 일이다.** 그 간극의 일부는 당신이 모르는 것, 일부는 AI가 당신의 상황에 대해
모르는 것이고, 가장 넓은 부분은 둘 다 아직 모르는 것입니다. 이 플러그인은 그 간극을 작업
전·중·후에 걸쳐 찾고 관리하는 운영 루프를 제공합니다. 분야는 가리지 않습니다 — 지원사업,
규정, 행사, 연구, 채용, 코드베이스. 스킬 11종과 Claude Code 에이전트 2종.

구체적으로 얻는 것:

- 당신과 AI가 몰랐던 것을 넘긴 뒤가 아니라 **작업을 시작하기 전에** 발견합니다.
- 산출물만이 아니라 당신이 원하던 성과로 작업을 판단합니다: 루프는 결과가 성과를 이뤘는지 당신에게 묻는 것으로 끝납니다.
- 자명한 요청은 자명하게: 스킬은 방법을 거치지 않고 바로 처리합니다.
- 보고 반응해야 하는 산출물은 **대화의 마크다운**으로 나오며, 번호가 붙은 항목과 복사할 수 있는 조립된 회신을 담습니다. 항목 번호를 고르거나 원하는 수정을 말하면 됩니다.
- 스킬 지시가 단계 경계와 턴을 끝내기 전에 계획 이탈을 기록합니다. 자동 리마인더는 실행되지 않습니다.

> **측정 상태: 미측정(unmeasured).** 가치 계약([`docs/value-contract.md`](docs/value-contract.md))은
> 이 플러그인이 "사용자가 몰랐던 것을 드러내고 **그것이 결정을 바꿀 때**"만 제 값을 한다고
> 못 박았습니다. 플러그인은 이를 세션 안에서 측정하는 장치를 싣지 않으므로, 위 항목들은
> 측정된 결과가 아니라 설계 의도입니다.

Thariq Shihipar(Anthropic, Claude Code 팀)의 방법론을 패키징했습니다. 두 자료가 원 출처입니다:
강연 **"Field Guide to Fable"**(AI Engineer World's Fair 2026 키노트)과 예시 모음
**"Know your unknowns"**(11개 인터랙티브 예시) —
https://thariqs.github.io/html-effectiveness/unknowns/. 스킬 11종이 원문 11개 예시를 모두
커버합니다(prototypes가 2개를 커버, unknowns-loop는 원문 대응이 없는 오케스트레이터). 사실검증
상세는 [`docs/talk-source.md`](https://github.com/ajitta/know-your-unknowns/blob/main/docs/talk-source.md) 참조.

---

## 목적: 당신과 AI가 아는 것의 세 칸

모든 작업에는 아는 쪽이 둘 있습니다. 당신과 AI입니다. 이 플러그인은 조하리의 창(Johari window)의 네 칸(열린 칸, 보이지 않는 칸, 숨겨진 칸, 미지의 칸)을 빌려 옵니다. 변형해서 "나"는 당신, "타인"은 AI, 아는 대상은 그 작업입니다. 그중 세 칸을 다룹니다. 분야는 가리지 않습니다. 연구, 정책, 행사, 채용, 개인적 결정, 그리고 코드도 그중 하나입니다.

| 당신 : AI | 플러그인 없이 | 스킬이 하는 일 | 스킬 |
|---|---|---|---|
| 앎 : 앎 — 둘 다 앎 | 요청이 자명하고 AI가 그냥 잘 합니다. | 없음: 이런 요청은 방법 없이 바로 처리합니다. | — |
| 모름 : 앎 — 당신은 모르고 AI는 앎 | AI가 제대로 만들어도 당신(또는 승인할 사람)이 판단하지 못합니다. | 당신이나 승인자가 모르는 것을 드러냅니다. | teach-me, quiz, buy-in |
| 앎 : 모름 — AI는 모르고 당신은 앎 | 당신이 계속 AI를 고쳐 가며 결과를 끌어냅니다. | 결정 전에 AI가 모르거나 판단할 수 없는 것을 묻거나 되읽어 확인합니다. | interview, reference |
| 모름 : 모름 — 둘 다 아직 모름 | 산출물은 나와도 원하던 성과일 가능성은 낮습니다. 가장 넓은 칸입니다. | 양쪽의 미지를 드러냅니다: 당신의 것과 AI 자신의 것. | blindspot, brainstorm, prototypes, deviation-log, tweakable-plan, unknowns-loop |

**산출물(output)**은 AI가 만든 것이고, **성과(outcome)**는 당신이 실제로 이루려던 것입니다. 결과가 완료 조건을 모두 채워도 성과를 놓칠 수 있으므로, 루프는 성과를 이뤘는지 당신에게 묻는 것으로 끝납니다.

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

스킬이 개선된 프롬프트로 끝나는 조사 절차로 응답하면 정상입니다. 그다음부터는:

- 분야와 상관없이 크고 낯선 작업 → `/unknowns:unknowns-loop <작업 설명>` 하나면 됩니다. 나머지는
  Claude가 단계별로 끌고 갑니다.
- 특정 기법만 필요 → 해당 스킬을 직접 호출하거나, 자연어로 말하면 자동 트리거됩니다.
- 슬래시 없이도 동작: "사각지대 조사해줘", "인터뷰해줘", "시안 4개", "퀴즈" 같은 말이 곧
  트리거입니다.

나머지 설치 경로(클론·개별 복사·데스크톱)는 아래 [설치](#설치)에 있습니다.

---

## 스킬 한눈에 보기

원문 11개 예시 커버 — prototypes가 2개 커버, unknowns-loop는 오케스트레이터.

| 시점 | 스킬 | 칸 | 하는 일 | 원문 예시 |
|---|---|---|---|---|
| 전 | `blindspot` | 둘 다 모름 | 사각지대 조사 → 개선된 프롬프트 | Blindspot Pass |
| 전 | `teach-me` | 당신이 모름 | 도메인 어휘 설명서 → 정밀한 요청 | Teach Me My Unknowns |
| 전 | `interview` | AI가 모름 | 모델이 자신이 알 수 없는 것을 물음 → 결정 테이블 | The Interview |
| 전 | `prototypes` | 둘 다 모름 | 철학이 다른 시안 N개 → 요구사항 조립 | Four Design Directions / Mock |
| 전 | `brainstorm` | 둘 다 모름 | 해법 공간 지도 → 개입 선택 | Brainstorm the Intervention |
| 전 | `reference` | AI가 모름 | 레퍼런스 분석·이해 증명 | Point at a Reference |
| 전 | `tweakable-plan` | 둘 다 모름 | 수정확률순 계획서 | The Tweakable Plan |
| 중 | `deviation-log` | 둘 다 모름 | 계획 이탈 기록 | Implementation Notes |
| 후 | `quiz` | 당신이 모름 | 이해도 퀴즈 | Quiz Me Before I Merge |
| 후 | `buy-in` | 당신이 모름 | 승인자가 모르는 것을 근거로 답하는 문서 | The Buy-In Doc |
| 전체 | `unknowns-loop` | 둘 다 모름 | 위 전부를 꿰는 운영 루프 | — |

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
3. `/unknowns:blindspot 테스트`를 호출해 조사 전에 먼저 묻는지 확인합니다.

### Codex CLI

1. 마켓플레이스와 플러그인을 추가합니다:

   ```
   codex plugin marketplace add ajitta/know-your-unknowns
   codex plugin add unknowns@know-your-unknowns
   ```

2. `$unknowns:tweakable-plan`처럼 스코프가 있는 스킬 이름 뒤에 작업을 적어 요청합니다.
3. 절차를 확인합니다. 이 경로는 예상이며 소유자가 아직 확인하지 않았습니다.

### ChatGPT 데스크톱(Codex 포함)과 모바일

두 경로에서의 동작은 **이 플러그인에서는 소유자가 아직 확인하지 않았습니다**.

1. **웹에서 zip 업로드(웹·모바일).** [know-your-unknowns-openai.zip](https://github.com/ajitta/know-your-unknowns/releases/latest/download/know-your-unknowns-openai.zip)을 내려받아 chatgpt.com의 플러그인 zip 업로드로 올립니다. 플러그인은 계정에 저장되어 ChatGPT 웹·모바일에서 사용합니다. 이 zip에는 OpenAI 매니페스트·스킬·목록용 자산이 들어 있습니다. 업로드는 자동으로 갱신되지 않으므로 새 릴리스마다 다시 올립니다.
2. **데스크톱 앱에서 마켓플레이스 추가.** 앱의 Codex 플러그인 화면에서 GitHub 마켓플레이스 `ajitta/know-your-unknowns` 또는 로컬 클론을 추가하고 `unknowns`를 선택해 설치합니다. 이 경로는 데스크톱 앱의 로컬 Codex 폴더에 설치하며 웹·모바일용 계정에 저장되지 않습니다. 업데이트는 마켓플레이스로 받습니다.

### Windows

1. 위에서 사용하는 호스트의 경로를 같은 패키지로 따릅니다.
2. 설치된 플러그인은 지시문과 목록용 자산만 싣기 때문에 Python이나 셸이 필요 없습니다.
3. 소스에서 빌드하는 개발자에게는 Python이 필요합니다. 아래 개발 명령의 `python3` 대신 `py -3`을 쓰세요. 재구성한 패키지는 Windows에서 로컬 실행하지 않았으며, 이전 Windows 훅 검사는 CI에서만 했고 이제 훅은 삭제되었습니다.

### 표면별 지원

- 스킬 11종은 모두 대화에 마크다운을 내고 번호로 반응을 받아 회신을 조립합니다. 단계에 필요한 도구가 호스트에 없으면 그 단계를 대화에서 하고 확인하지 못한 것을 밝힙니다.
- 이름 있는 에이전트 2종은 Claude Code에서만 실행됩니다. 다른 표면에서는 에이전트를 부르는 단계가 위의 도구 부재 규칙을 따르고, buy-in의 독립 근거 검증은 쓸 수 없습니다.
- 어떤 표면에서도 설치된 패키지에 훅이나 스크립트는 없습니다. 작업 중 요청한 실행 가능한 프로토타입은 호스트가 지원하면 여전히 코드 파일로 쓸 수 있습니다.
- 이탈 기록은 파일을 쓸 수 있으면 파일(코드 작업이면 `IMPLEMENTATION_NOTES.md`, 그 밖에는 산출물 옆의 `DEVIATIONS.md`)이고, 그렇지 않으면 기록이 대화에 남습니다.

### 클론에서 바로 실행

생성된 플러그인 폴더를 사용합니다:

```bash
git clone https://github.com/ajitta/know-your-unknowns.git
claude --plugin-dir ./know-your-unknowns/plugins/unknowns
```

커밋된 생성물은 바로 로드할 수 있습니다. 소스를 고친 뒤에는 개발 절의 명령으로 다시 생성하세요.

### 개별 스킬 복사

`plugins/unknowns/skills/<name>/`의 폴더 전체를 `agents/openai.yaml`까지 복사합니다. 스킬 폴더마다 자기 완결적입니다.

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

0.12.0에서 스킬 두 개의 이름이 바뀌었습니다: `loop`는 `unknowns-loop`, `notes`는 `deviation-log`입니다. `/unknowns:unknowns-loop`와 `/unknowns:deviation-log`로 부르고(Codex: `$unknowns:unknowns-loop`, `$unknowns:deviation-log`), 업로드한 스킬 zip은 교체하세요. 트리거 문구는 그대로입니다.

### 0.1.x(field-guide)에서 업그레이드

옛 플러그인 이름은 `field-guide`였습니다. 해당 설치본을 지우고 `unknowns`를 추가합니다:

```
/plugin uninstall field-guide@ajitta
/plugin marketplace add ajitta/know-your-unknowns
/plugin install unknowns@know-your-unknowns
```

옛 저장소 URL(`ajitta/field-guide`)은 리다이렉트됩니다. 스킬 대응은 `reference-map` → `reference`, `impl-notes` → `notes`(0.12.0에서 다시 이름 변경, 아래 참고)이며 나머지 이름은 같습니다.

---

## 스킬별 상세 사용법

### 1. `/unknowns:unknowns-loop` — 전체 운영 루프

**언제**: 목표가 흐릿한 크거나 낯선 일: 프로그램 신설, 행사 기획, 연구, 제품 기능. 또는
"제대로 각 잡고" 진행하고 싶을 때.

**호출**:
```
/unknowns:unknowns-loop 우리 아파트 단지에 자원봉사자가 운영하는 공구 도서관 만들기
```
자동 트리거 문구: "unknowns loop", "run the operating loop", "know your unknowns",
"운영 루프로 진행", "풀 루프로 해줘"

맨 `/loop`는 이 스킬이 아니라 Claude Code 내장 인터벌 러너입니다. 이 스킬은
`/unknowns-loop`나 `/unknowns:unknowns-loop`로 부릅니다. 대화 중의 맨 "loop"나 "루프
돌려줘"도 마찬가지입니다.

**진행 방식**: Claude가 당신이 이루려는 성과와 완료 조건을 한 번의 주고받기로 합의하고,
당신의 상황에 대해 자신이 모르는 것을 밝히고, 단계를 먼저 알려 줍니다. 작업 전:
blindspot(분야 용어가 낯설면 teach-me 먼저) → interview → 필요하면
brainstorm/prototypes/reference → 가장 위험한 가정 하나만 시험하는 가장 싼 프로브(전화
한 통, 시범 운영, 스파이크) → 수정확률순 계획(plan). 작업 중에는 deviation-log가 이탈을
기록합니다. 작업 뒤에는 결과를 완료 조건마다 근거와 함께 확인한 뒤 quiz, 리뷰어나
이해관계자의 승인이 필요하면 buy-in, 그리고 마지막으로 **성과 확인**: 결과가 조건을
채웠는지만이 아니라 원하던 성과를 이뤘는지 Claude가 당신에게 묻습니다. 이미 답이 나온
단계는 건너뛰고 그렇다고 말합니다. 자명한 작업에는 루프가 필요 없습니다.

---

### 2. `/unknowns:blindspot` — 작업 전 사각지대 조사

**언제**: 확인해 보지 않은 영역에서 일을 시작하기 전: 지원사업 공고, 새 규정, 낯선
모듈이나 라이브러리. "내가 뭘 모르는지 모르는" 상태일 때.

**호출**:
```
/unknowns:blindspot 첫 시 문화예술 지원사업 신청: 도서관 세 곳 벽화 프로그램
```
자동 트리거: "blind spot pass", "what am I missing", "unknown unknowns",
"사각지대 조사해줘", "내가 놓친 게 뭐지"

**진행 방식**: 먼저 확실히 아는 것, 가정하는 것, 판단할 수 없는 것을 묻고, 그 옆에 자신의
세 목록도 내놓습니다: 당신의 상황에 대해 모르는 것, 자신이 가정하는 것, 여기서 확인할 수
없는 것. 그다음 양쪽의 가정부터 확인하며 조사하고, 작업 자체는 시작하지 않습니다. 작업이
여러 자료에 걸치면(코드베이스 전체, 많은 문서) Claude Code에서 `unknowns:unknowns-scout`
에이전트를 씁니다. 세 목록 어디에도 없던 발견은 **새로 안 것**으로 표시하고, 먼저 대비를
보여 줍니다 — 요청한 것 대 실제로 들어가게 될 것, 그리고 집계 — 그다음 발견 하나당 카드
하나를 가능성 × 폭발 반경순으로 정렬해 종류를 붙입니다: **지뢰**(건드리면 뜻밖의 것이
깨짐), **관례**(그 영역이 지키는 불문율), **빠진 개념**(프롬프트에 이름이 없는 메커니즘),
**이력**(지금 모양이 된 이유를 설명하는 이전 시도·막다른 길). 정리하지 못한 것은 당신에게
물을 질문과 확인할 것으로 남깁니다.

**핵심 산출물**: 카드의 "프롬프트 픽스"들이 조립된 **개선된 프롬프트 초안**. 실행 순서를
밝히고 명시적 체크포인트로 끝납니다. 그것을 복사해 실제 지시로 쓰는 것이 이 스킬의
전부입니다.

**팁**: 코드에도 똑같이 됩니다 — 예: `"auth 모듈에 카카오 OAuth 추가, 먼저 blind spot pass,
git 이력과 tests/ 위주로"`. 분야 어휘 자체를 배워야 한다면 아래 teach-me가 더 맞습니다.

---

### 3. `/unknowns:teach-me` — 도메인 어휘 설명서

**언제**: "더 좋게 해줘"밖에 말할 수 없을 때. 그 분야의 용어를 몰라 요청이 모호해지거나
결과를 판단할 수 없을 때.

**호출**:
```
/unknowns:teach-me 영상 색보정. 완전 초보야
```
자동 트리거: "teach me", "make me an explainer", "가르쳐줘", "설명서 만들어줘",
"이 분야 용어를 모르겠어"

**진행 방식**: 그 도메인의 멘탈 모델을 3–5단계 파이프라인으로 → 이 작업에서 내리게 될 결정
축 3–7개 → 축마다 어휘 사다리(일상어 → 전문 용어, 용어마다 요청 예문 하나, 확인하지 못한
용어는 *미검증* 표시) → 축마다 전후 비교와 전체 룩을 한 번에 느낄 수 있는 이름 붙은
프리셋 2–3개 → 새 어휘로 쓴 "좋은 결과의 기준" 4–6개 → 마지막으로 **정밀 요청 초안: 원래
요청을 새 어휘로 다시 쓴 것**. 전세 계약, 연구 방법론, 커피 로스터의 용어에도 똑같이
됩니다.

---

### 4. `/unknowns:interview` — 결정 전 인터뷰

**언제**: 일이 덜 정해졌고 답은 당신에게 있을 때: 당신의 제약, 관련된 사람들, 지역 규칙,
우선순위. blindspot 조사 직후.

**호출**:
```
/unknowns:interview 4개국에서 오는 친척 40명의 이틀짜리 가족 모임. 아무것도 안 정해졌어
```
자동 트리거: "interview me", "ask me questions before implementing", "ask me before you
decide", "인터뷰해줘", "스펙 질문"

**진행 방식**: 무엇이든 정하기 전에 당신의 상황에 대해 자신이 알 수 없거나 판단할 수 없는
것을 묻습니다. 라운드당 **4개 이하** 질문에 선택지 2–4개를 붙여, 잘못 정하면 무엇이
깨지는지의 고정 순서(구조 → 되돌릴 수 없는 피해 → 기존 것과의 호환 → 비용 → 취향)로
묻습니다. 질문 도구가 더 적게 받으면 라운드를 여러 호출로 나눕니다. 각 질문에 "왜
중요한지" 한 줄, 각 선택지에 트레이드오프를 붙입니다. 끝나면 **결정 표와 바로 쓸 수 있는
작업 프롬프트**를 내놓습니다. 건너뛴 질문을 표시하고, 구조와 피해 쪽 결정을 고정으로
선언하며, 이탈은 이탈 기록(코드라면 IMPLEMENTATION_NOTES.md)에 남기라고 적습니다.

**팁**: 심층 인터뷰를 원하면 `"40문항 수준으로 탈탈 털어줘"` — 우선순위를 유지하며
라운드를 반복합니다. 기능 개발이라면: `"OAuth 작업에 대해 인터뷰해줘, 아키텍처 질문
먼저"`.

---

### 5. `/unknowns:prototypes` — 발산형 프로토타입 팬아웃

**언제**: 원하는 걸 말로 설명 못 하겠을 때("보면 안다"): 채용 공고, 행사 형식, 캠페인,
보고서 양식, 대시보드, API.

**호출**:
```
/unknowns:prototypes 첫 운영 총괄 채용. 직무 기술서를 못 쓰겠어, 4개 보여줘
```
자동 트리거: "divergent prototypes", "design options", "versions to react to", "know it
when I see it", "시안 4개", "프로토타입 여러 개", "보면 안다"

**진행 방식**: 잔변형이 아니라 **설계 철학이 다른** 안 4개(개수 조정 가능)를 대상에 맞는
축으로 만듭니다(화면이면 정보 구조·흐름·밀도·상호작용, 문서·직무·행사면 구조·범위·
어조·대상·형식). 각 안에는 이름 + 한 줄 철학 + 장단점 + 맞는 조건이 붙습니다. 당신의
상황에 대해 모르는 것도 밝힙니다. 번호 붙은 마크다운 비교로 요소별 **가져감 / 버림**
반응을 모아 요구사항 목록 초안으로 조립합니다. 실행되는 프로토타입이나 전체 초안은
호스트가 지원하면 파일로 쓰고, 비교는 대화에 남습니다.

**반응하는 법**: `"2안의 범위 + 4안의 어조 + 1안의 보고 라인"` 처럼 조합을 말하면
**명시적 요구사항 목록**으로 바꿉니다. 스킬은 거기서 끝나고, 작업은 그 목록에서
시작합니다.

**팁**: `"wild하게"` 라고 하면 철학 간 거리를 더 벌립니다. 코드 아키텍처 비교에도
됩니다: `"이벤트 기반 vs 폴링 vs 푸시를 스켈레톤으로 나란히"`. 상호작용 자체가 쟁점이면
(툴바 위치 등) A/B 선택 버튼이 있는 클릭 가능한 목업을 만들고, 전부 가짜 데이터라고
밝히며, 실제 연결이 들어갈 자리를 짚습니다.

---

### 6. `/unknowns:brainstorm` — 해법 공간 지도

**언제**: 문제는 아는데 뭘 해야 할지 모를 때. 첫 아이디어에 바로 뛰어들기 전에.

**호출**:
```
/unknowns:brainstorm 동네 독립서점 매출이 3년째 매년 15%씩 줄어. 임대 1년 남음
```
자동 트리거: "brainstorm interventions", "show me options", "브레인스토밍",
"해법 후보 펼쳐줘", "옵션 보여줘"

**진행 방식**: 먼저 당신의 상황에 대해 모르는 것을 밝히고, 이미 있는데 이 문제에 쓰이지
않는 것을 찾습니다 — 손닿는 자원·프로그램·사람, 코드베이스라면 연결되지 않은 기계장치.
가장 싼 후보는 대개 있는 것을 잇는 일이고, 그런 후보에는 `Already exists — <where>`
표시가 붙습니다. 그다음 **오늘 오후부터 분기짜리 승부수까지의 시간 축** 위에 후보
개입안 10개 안팎을 펼치고, 각각에 기대 효과 / 노력 크기 / 주요 위험 / 문제가 움직였는지
보는 법을 붙입니다. **공감(resonate)**한 항목 번호가 복사할 수 있는 "이것들을 이 순서로 진행"으로 조립되고, 거기서 멈춥니다.

---

### 7. `/unknowns:reference` — 레퍼런스 분석

**언제**: 본뜰 예시가 있을 때: 다른 기관의 규정, 지난 제안서, 계약서 양식, 경쟁 제품,
예시 코드, 목업.

**호출**:
```
/unknowns:reference 옆 학교 학부모회 회칙. 우리 학교는 훨씬 작아, 우리 것 만들어줘
```
자동 트리거: "use this as a reference", "make it like this", "레퍼런스로 써",
"이 코드처럼 만들어줘", "이거 참고해서"

**진행 방식**: 레퍼런스를 그대로 복사하지 않고 4분류 분석부터 제시합니다 —
**반드시 보존할 동작 / 당신의 맥락에 맞게 바꿀 부분 / 불필요·위험한 부분 / 개선 가능한
부분**. 그 위에 무엇을 쌓기 전에 **이해 증명(의미 대응표)** 을 냅니다 — 번호 붙은 레퍼런스
발췌와 당신 작업의 대응물, gotcha 노트, Match 열이 있는 엣지케이스 표이며, 당신의 상황에
대한 추측에 기댄 행은 *가정*으로 표시합니다. 당신의 승인에서 멈춥니다: `semantics
confirmed`라고 답하거나 행 번호로 고치면 됩니다. 적용 계획은 레퍼런스가 스스로를 확인하는
방식(테스트, 체크리스트, 인수 기준)부터 옮겨 오고, 작업은 승인된 대응표에서 시작합니다.

**팁**: 코드 포팅도 같은 방식입니다 — 예: `legacy/billing.py, 새 서비스에서 TypeScript로
포팅`. 스크린샷이나 원하는 산출물의 실제 예시도 "지도"가 됩니다.

---

### 8. `/unknowns:tweakable-plan` — 수정확률순 계획

**언제**: 조사·인터뷰가 끝나고 작업 전 계획이 필요할 때.

**호출**:
```
/unknowns:tweakable-plan 시 소유 공터에 공동체 텃밭 열기: 상자 텃밭 20개, 창고, 수도, 대기 50가구
```
자동 트리거: "plan this", "make a plan", "tweakable plan", "계획 세워줘", "구현 계획",
"수정확률순으로 계획"

**진행 방식**: 계획은 목적과 완료 조건 한 줄로 시작하며, 주어지지 않은 것은 "미설정"이라고
적고, 당신의 상황에 대해 모르는 것을 밝힙니다. 크기 관문이 있습니다: 바꾸고 싶을 만한
결정이 없는 일(코드라면 파일 2개 이하에 스키마·인터페이스·UX 계약 결정이 없는 변경, 즉
기본 plan mode에 맞는 일)은 문서 대신 그 한 줄, 빠진 완료 조건에 대한 질문, 실행 순서의
단계만 받습니다. 그 밖에는 항목을 실행 순서가 아니라 **바뀔 가능성이 높은 순서**로
제시합니다. 다른 부분이 기대는 결정 항목 — 텃밭 배정 방식이나 시와의 협약, 코드라면
스키마와 인터페이스 — 이 맨 위에 오고, 각각 검토한 대안, 폭발 반경, 검증 방법, 틀리면
깨지는 것을 담습니다. 중심 산출물(예산표, 진행표, 코드라면 공개 타입)에는 각 선택이 이긴
대안을 주석으로 붙입니다. 기계적 작업은 결정 항목 뒤에 요약과 검증을 붙여 둡니다.
승인/수정 요청 선택이 당신의 회신으로 조립됩니다. 계획은 스스로 가장 약한 부분을 짚고,
복사해 보낼 수 있는 미리 쓴 회신 2–3줄로 끝납니다.

---

### 9. `/unknowns:deviation-log` — 계획 이탈 기록

**언제**: 작업 중 계획·스펙에 없던 상황을 만났을 때. 사실상 **항상 켜두는 규칙**에
가깝습니다.

**호출**:
```
/unknowns:deviation-log 구민회관 보수공사로 송년 행사를 초등학교 강당으로 옮김(엘리베이터 없음)
```
자동 트리거: "implementation notes", "record a deviation", "where did we diverge from
the plan?", "이탈 기록", "임플 노트", "어디서 계획이랑 달라졌어?"

Claude는 작업 중 이탈을 감지하면 스스로도 기록합니다.

**기록되는 것**: 설계·동작·호환성에 영향을 주는 결정만 (문구·서식·이름은 제외). 전체
항목은 마주친 상황 / 계획과 어떻게 다른지 / 택한 대응 / 이유 / 버린 대안 / 위험과 후속
확인(당신만 판단할 수 있는 것 포함)을 담습니다. 한 줄짜리 가벼운 **발견(Discovery)** 도
같은 파일에 들어갑니다: 계획이 가정한 것과 실제가 다르지만 아직 결정은 필요 없을 때.

**지속성**: 항목은 이탈 기록 파일에 덧붙이며, 파일이 없으면 만듭니다. 코드 작업이면
프로젝트 루트의 IMPLEMENTATION_NOTES.md, 그 밖에는 산출물 옆의 DEVIATIONS.md나 당신이
지정한 파일입니다. buy-in과 quiz가 그 기록을 씁니다.

**계속 진행, 마무리에 검토**: 계획에 없는 상황에서는 Claude가 보수적인 쪽을 고르고 기록한 뒤
계속 갑니다. 이탈 때문에 무효가 된 계획의 결정은 계획서에서 대체됨으로 표시합니다. 마무리
때는 작업의 구조, 남이 보거나 약속받은 것, 데이터나 돈, 안전에 닿는 항목을 먼저 올려
검토받는데, 당신만 아는 것에 기댄 판단부터 올립니다. 이어서 **계획에 되먹이기**
블록 — 두 번째 시도에서 무엇이 달라지는지 복사할 수 있는 세 줄 — 이 붙습니다.

---

### 10. `/unknowns:quiz` — 작업 후 이해도 검증

**언제**: 맡긴 큰 작업이 끝난 직후, 발표·제출·서명·머지 직전. "내가 이걸 설명할 수 있나?"
싶을 때.

**호출**:
```
/unknowns:quiz 아까 정리해 준 전세 계약 검토. 내일 계약하러 가
```
자동 트리거: "quiz me", "test my understanding", "퀴즈", "내가 이해했는지 확인해줘"

**진행 방식**: ① 먼저 설명(작업의 구조 / 핵심 결정 3개 / 실패 가능성 높은 곳 / 직접
확인해야 할 것), 각 부분에 위치(코드면 `file:line`, 아니면 절이나 쪽)를 붙임 → ② **6문항,
합격은 6개 모두**(객관식 5개를 4 + 1로 묻되 도구가 더 적게 받으면 나눠 묻고, 자기 말로
설명하는 teach-back 1개), 잘못됐을 때 할 일 > 결정 근거 > 결과 예측 순으로 우선하고 단순
암기는 피함, 이탈 기록이 있으면 기록된 이탈에 대한 문항 최소 1개 → ③ 채점 — 틀리거나 빈
답마다 다시 읽을 정확한 위치를 짚고 재도전 기회를 줌. 채점은 대화에서 하며, teach-back
키는 답을 받을 때까지 숨김 → ④ 6/6이면 통과, 리뷰어 승인이 필요하면 buy-in을 제안. 6/6
미만이면 "아직"으로 남고 다시 읽을 부분을 나열합니다.

---

### 11. `/unknowns:buy-in` — 승인자의 미지 문서

**언제**: 작업이 끝났고, 그 작업을 보지 못한 사람의 **승인**이 필요할 때: 이사, 재단,
고객, 위원회, 코드 리뷰어.

**호출**:
```
/unknowns:buy-in 하이브리드 근무 규정. 결재는 내 상사, 작년 봄 COO가 비슷한 안을 반려함
```
자동 트리거: "buy-in doc", "prep me for review", "get sign-off", "설득 문서 만들어줘",
"리뷰 준비"

**진행 방식**: 승인자마다 결정에 필요한데 모르는 것과 반대할 지점을 정리합니다. Claude는
그들에 대해 당신이 아는 것(우선순위, 과거 반대, 사내 정치)을 묻고, 둘 다 모르는 것은 미리
알아볼 질문으로 올립니다 → 결과를 먼저 보여 줌(데모, 샘플, 시범 결과. 없으면 그렇다고
밝히고 한계에 올림) → 각 항목에 대한 답, 승인자가 따라가 볼 수 있는 근거(스펙 §, 이탈
기록 날짜, 지표, 원문 문서, 테스트 실행, `file:line`)를 붙이고 Claude Code에서는
independent-reviewer 에이전트가 확인 — 근거 없는 답은 한계로 옮김 → 알려진 한계와 풀리지
않은 미지, 이탈 기록에서 가져옴 → 결재가 필요한 사람들과 각자 확인할 것. quiz가 당신의
빈칸을 채운다면, buy-in은 승인자의 빈칸을 채웁니다.

---

## 에이전트 사용법

에이전트는 별도 컨텍스트에서 도는 전문가입니다. 자연어로 지명하거나, 플러그인 스코프
id — `unknowns:unknowns-scout`, `unknowns:independent-reviewer` — 로 부르면 됩니다.
Agent 도구의 `subagent_type`과 `@agent-unknowns:unknowns-scout` 멘션 형식이 요구하는 것이
이 id입니다. `subagent_type`에 스코프 없는 `unknowns-scout`을 주면 거부됩니다.

이름 있는 에이전트는 Claude Code에서만 실행됩니다. 둘 다 도구 목록을 선언하지 않으므로 세션이 허용하는 모든 도구를 물려받고, 프롬프트에도 읽기 전용 규칙이 없습니다. 제한이 필요하면 자신의 권한 설정이나 샌드박스를 쓰세요.

**unknowns-scout** (정찰):
```
unknowns-scout 에이전트로 지원사업 공고와 우리 초안에서 놓친 게 뭔지 조사해줘
unknowns-scout 에이전트로 auth 모듈 정찰해줘
```
blindspot 스킬도 큰 조사에서 이 에이전트를 자동으로 부르고, brainstorm 스킬은 이미 있는
것을 목록으로 만들 때 쓸 수 있습니다. 그 밖에는 이름을 불렀을 때만 돕니다: 다른
워크플로가 탐색·조사용 서브에이전트를 찾으면 그 워크플로의 에이전트, Explore, 일반
에이전트가 갑니다. 작업이 가진 자료라면 무엇이든 조사합니다 — 문서, 데이터, 웹, 코드베이스와
그 이력: 무엇이 있고 무엇이 그것을 규율하는지, 이전 시도와 되돌림, 확인 장치가 있는 곳과
없는 곳, 불문율. 낯선 라이브러리·분야·규정이면 지금 적용되는 판의 공식 원문을 읽습니다.
가능성 × 폭발 반경순 조사 표와 개선된 프롬프트 초안을 돌려주며, 찾은 것만 보고하고 아직
확인해야 할 것을 나열합니다.

**independent-reviewer** (독립 검증):
```
independent-reviewer 에이전트로 이 갈라 행사 계획을 이사회 목표 네 가지에 비춰 검토해줘
이 브랜치를 계획에 비춰 unknowns independent-reviewer로 돌려줘
```
만든 쪽의 설명을 **주장으로만** 취급하고 작업 자체에 직접 비춰 검증합니다: 문서, 수치와
출처, 코드라면 코드를 읽고 테스트를 돌려서. 다섯 가지 확인은 일부러 일반 리뷰가 다루지
않는 것들입니다: **계획·성과 부합**(완료 조건마다 충족/부분/누락 판정, 산출물이 밝힌
성과를 이룰 것 같은지), **기록된 이탈을 혼자 결정해도 됐는지**, **서류상 통과, 현실에서
실패**(맞지 않는 수치, 인용한 내용을 말하지 않는 출처, 코드라면 실제 의존성을 숨기는 목과
구현을 그대로 베낀 테스트), **검증 완료 목록** — 침묵은 검토 안 함과 구별되지 않으니까 — ,
그리고 **주장 유형별 확인**: 사실 주장은 원 출처에, 추론 주장은 전제와 반례로 확인합니다.
패킷에 완료 조건이나 성과가 없으면 추측하지 않고 판단 불가로 보고하며, 확인하지 못한 것으로
끝맺습니다. 코드의 일반 버그·보안 점검은 `/code-review`와 `/security-review`의 몫이니
함께 돌리세요. buy-in 스킬이 답의 근거를 확인하려고 이 에이전트를 부릅니다. 그 밖에는
이름을 불렀을 때만 돕니다: 이름 없는 "독립 리뷰"는 다른 리뷰 도구나 일반 에이전트로
갑니다.

---

## 추천 시나리오

**시나리오 A — 자명한 요청** (오타 수정, 변수 이름 바꾸기, 분명한 한 단계 작업):
스킬도 루프도 필요 없습니다. Claude가 바로 합니다. 중요한 이탈이 생기면 기록하세요.

**시나리오 B — 중간 규모 코드 작업** (버그 원인 애매, 모듈 반쯤 아는 상태):
```
/unknowns:blindspot 장바구니 합계가 가끔 틀림. checkout/ 모듈
→ (조사에서 나온 개선된 프롬프트 검토)
/unknowns:interview
/unknowns:tweakable-plan
→ 구현
/unknowns:quiz
```

**시나리오 C — 크고 낯선 일** (새 프로그램, 행사, 처음 해 보는 절차):
```
/unknowns:unknowns-loop 직원 80명 회사에 사내 멘토링 프로그램 도입. 인사 담당은 나 혼자
```
Claude가 조사, 인터뷰, 가장 위험한 가정의 프로브, 계획, 이탈 기록, 퀴즈, 승인이 필요하면
buy-in, 그리고 성과 확인까지 단계별로 이끕니다.

**시나리오 D — 새 분야** (디자인, 연구, 아직 틀을 못 잡은 결정):
```
/unknowns:teach-me 유튜브 썸네일 디자인. 어휘부터
/unknowns:prototypes 채널 아트 4안, 철학이 다르게
/unknowns:brainstorm 채널 성장이 멈췄어. 이번 달에 해볼 것들
```

---

## 문제 해결 (FAQ)

**Q. 스킬이 자동으로 안 뜹니다.**
자동 트리거는 문맥 판단이라 보수적입니다. 확실하게는 슬래시로 직접 호출하세요:
`/unknowns:blindspot`. 설치 직후라면 새 세션을 시작하거나 `/reload-plugins`. 스킬을 많이
설치했다면 원인이 하나 더 있습니다: Claude Code는 스킬 목록에 예산(기본 컨텍스트 창의 1%)을
두고, 넘치면 **많이 쓰는 스킬(최근성 가중)만** 설명을 남기고 나머지는 이름만 보여 줍니다.
위험한 것은 내가 드물게 쓰는 unknowns 스킬이고, 스스로 떠야 하는 deviation-log에서 특히 큽니다.
unknowns 설명이 전부 빠진 조건(초과는 CLI 로그로 확인, 11개 모두 빠졌다는 것은 탐침 실행의
자기 보고)에서 영어 트리거 11건 중 9건은 여전히 발화했고 notes(현 deviation-log)와
blindspot은 발화하지 않았습니다(1회 측정,
[docs/trigger-eval-crowd-2026-09-30.md](docs/trigger-eval-crowd-2026-09-30.md)).
`/doctor`로 목록 비용을 보고,
`skillListingBudgetFraction` 설정(예: `0.02`)으로 예산을 늘리거나, 드물게 쓰는 다른 스킬을
`skillOverrides`에서 `"name-only"`로 두세요(플러그인 스킬에는 적용되지 않으므로 이 스킬들을
보호하는 게 아니라 자리를 비우는 방법입니다). eval의 `--crowd N` 옵션이 이 경우를 잽니다.

**Q. `/unknowns:blindspot` 대신 `/blindspot`이라고 쳐도 되나요?**
대부분은 됩니다. 플러그인 스킬은 스코프 이름으로도, 맨 이름으로도 호출됩니다 — 같은 이름을
쓰는 다른 명령이 없는 한. 그래서 `/blindspot`, `/quiz`는 그냥 동작합니다. Claude Code는
자체 `loop` 스킬(반복 인터벌 러너)을 싣고 있어 맨 `/loop`는 그쪽으로 갑니다. 이 플러그인의
루프는 `unknowns-loop`라서 `/unknowns-loop`로 부를 수 있습니다. 스코프 형식은 절대 모호하지 않아서
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
skills/<name>/                 소스: SKILL.md, agents/openai.yaml
claude-code/agents/             소스: Claude Code 에이전트 프롬프트
plugin-manifest.json           소스 매니페스트, 현재 0.11.0
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
