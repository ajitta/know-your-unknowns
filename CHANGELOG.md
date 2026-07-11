# Changelog

## 0.2.0 — 2026-07-11
- **이름 변경**: 플러그인 `field-guide` → `unknowns` (호출: `/unknowns:<스킬>`),
  레포 `ajitta/field-guide` → `ajitta/know-your-unknowns`.
  이름의 근거: 방법론의 실제 핵심 개념이 원문 제목 그대로 "Know your unknowns"이기 때문.
  기존 설치자는 `field-guide` 제거 후 재설치 필요 (README "구버전에서 업그레이드" 참고).
- **스킬명 정리**: `reference-map` → `reference`, `impl-notes` → `notes`.
- **스킬 4종 추가** — 원문 "Know your unknowns" 11개 예시와 1:1 대응:
  `teach-me`(도메인 어휘 설명서), `brainstorm`(해법 공간 지도),
  `plan`(수정확률순 tweakable plan), `buy-in`(리뷰어 설득 문서).
- **산출물 형식 업그레이드**: 반응을 구조화된 답변으로 조립하는 UI가 달린
  단일 파일 인터랙티브 HTML 우선, 뷰어 없는 환경은 마크다운 폴백.
- loop 단계 표기 오류 수정("9단계"인데 10개 나열 → 1~10단계로 정리) 및 신규 스킬 연결.
- 훅 개선: 세션 ID 정규화, `UNKNOWNS_NOTES_THRESHOLD`/`UNKNOWNS_NOTES_REPEAT`
  환경변수 (구 `FIELD_GUIDE_NOTES_THRESHOLD` 호환 유지).
- 출처 문서(talk-source.md)에 "Know your unknowns" 페이지와 11개 예시 매핑 추가.

## 0.1.2 — 2026-07-10
- GitHub 레포 공개 (`ajitta/field-guide`) 및 마켓플레이스 매니페스트 추가
  (`/plugin marketplace add ajitta/field-guide` 지원)
- plugin.json에 homepage/repository 필드 추가

## 0.1.1 — 2026-07-10
- README 사용법 상세화: 설치 3종, 스킬별 호출 예시·자동 트리거·팁,
  에이전트 지명법, 훅 설정표, 규모별 시나리오 4종, FAQ

## 0.1.0 — 2026-07-10
- 최초 릴리스: skill 7종(loop, blindspot, interview, prototypes, reference-map,
  impl-notes, quiz), agent 2종(unknowns-scout, independent-reviewer),
  hook 1종(이탈 기록 리마인더)
- 기반: Thariq Shihipar, "Field Guide to Fable" (AI Engineer World's Fair 2026) —
  강연 원문 대조 및 외부 사실검증 완료 (`skills/loop/references/talk-source.md`)
