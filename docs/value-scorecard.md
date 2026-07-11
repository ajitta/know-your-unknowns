# 가치 스코어카드

[value-contract.md](value-contract.md)의 지표 기록. 실사용 1회 = 1행.
기록 기준: "몰랐던 것 발견"은 사용자가 사전에 알지 못했다고 인정한 사실만 센다.

| # | 날짜 | 과제 | 사용 스킬 | 몰랐던 것 발견? | 결정 변경? | 메모 |
|---|------|------|-----------|----------------|-----------|------|
| 1 | 2026-07-11 | v0.3.0 플러그인 자체 사각지대 조사 | loop(scale-down) → blindspot + unknowns-scout ×2 | 예 — 26건: agent `tools` 배열 표기가 문서 스펙과 다름, scout 유효 도구가 선언보다 좁음(Grep/Glob 누락), "11:11 매핑" 주장 산술 오류, 테스트/CI 부재, 트리거 충돌 5쌍 등 | 예 — agents/*.md tools 표기 교체, README read-only 주장 완화, loop/plan description 트리거 경계 추가, tests/ + CI 신설, 검증 환경 기록 | 루프 유/무 before/after의 첫 데이터점 |
