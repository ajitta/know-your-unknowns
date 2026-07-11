# 미결정 사항 — 2026-07-11 사각지대 전환 작업 이후

26건 전환(HIGH 10, MED 11, LOW 5) 후 남은 것. 두 종류로 구분:
**작성자 결정**(취향/정책 문제)과 **재검증 대기**(환경이 없어서 못 잰 것).
근거 문서: [trigger-eval-v0.3.0.md](trigger-eval-v0.3.0.md),
[trigger-matrix.md](trigger-matrix.md), [value-contract.md](value-contract.md),
`IMPLEMENTATION_NOTES.md`(저장소 루트).

## A. 작성자 결정 필요

| # | 질문 | 배경 | 선택지 |
|---|------|------|--------|
| A1 | 뷰어 없는 CLI에서 HTML 산출 허용? | plan 스킬이 headless CLI에서 markdown 폴백 대신 `*.html` 파일 생성 + "열어서 검토" 안내 (trigger-eval §3) | ① 현행 판단 허용 — 스킬 문면을 "파일 산출 가능하면 HTML"로 수정 ② markdown 강제 — 감지 규칙 명문화 |
| A2 | 가치 계약 수치 승인 | value-contract.md의 10회/50%/두 릴리스는 측정 시작용 임의 초기값 | 그대로 승인 / 조정 |
| A3 | 이탈 기록 매체 완화? | headless 루프가 notes를 파일 아닌 최종 메시지로 전달 (trigger-eval §2) | ① 소형 과제는 메시지 허용으로 규칙 완화 ② 파일 영속화 강제 문구 강화 |
| A4 | 배포 zip 릴리스 정책 | `scripts/build-plugin.sh` 신설, 단 HEAD ≠ v0.3.0 태그라 Releases 첨부 보류. 구버전 유통 zip(Cowork 카드)의 회수/공지 여부도 미정 | 다음 버전 범프 때 릴리스 자산 첨부 + Cowork 재공유 / Method A·Cowork 안내 삭제하고 marketplace 일원화 |
| A5 | 스코어카드 기록 습관 | value-scorecard.md는 실사용마다 1행 필요 — 작성자만 채울 수 있음 | 주간 사용 후 기록 / 릴리스 시점 일괄 회고 |

## B. 재검증 대기 (환경/시간 필요)

| # | 항목 | 방법 | 트리거 조건 |
|---|------|------|------------|
| B1 | scout 유효 도구 Grep/Glob 누락 | 새 세션에서 unknowns-scout 스폰, 도구 목록 프로브. 쉼표 문자열 수정 후에도 누락이면 Claude Code 이슈 보고 | 다음 세션 시작 시 |
| B2 | Windows python3 | 실기 테스트 또는 CI에 windows-latest job 추가(단 hook 실행 경로가 아닌 스크립트 단위 테스트만 유효) | Windows 사용자 제보 시 |
| B3 | Cowork 출력 분기 | Cowork에서 prototypes/plan 호출, 포맷 관측 | Cowork 접근 가능할 때 |
| B4 | 중·대형 루프 티어 준수 | 대화형 세션에서 medium(2→3→6→7→9)·large(10단계) 실측 — headless는 interview가 성립 안 함 | 다음 실전 중형 과제 |
| B5 | 나머지 8개 스킬 트리거 eval + 오발화율 | trigger-eval 방법 재사용, 충돌 쌍 유사 문구 negative 케이스 포함 | 여유 시 / description 변경 시 |
| B6 | $ARGUMENTS 빈 인자 동작 | 인자 없이 스킬 호출, "from \`$ARGUMENTS\`" 위치가 빈 문자열로 치환되는지 확인 | B5와 함께 |
| B7 | 방법론 효능 (전환 부분 잔여) | scorecard 10행 누적 후 결정-변경 비율 평가 | 실사용 누적 |

## 처리 규칙

각 항목은 해결 시 이 표에서 삭제하고, 결정은 CHANGELOG 또는 해당 문서에,
재검증 결과는 trigger-eval 후속 문서에 기록한다.
