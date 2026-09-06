---
description: "Korean trigger phrase for the buy-in skill: '설득 문서 만들어줘'"
tags: [trigger, ko, buy-in]
runs: 3
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill]
---

저장소를 볼 수 없으니 작업 상태를 여기 적을게. 직접 만든 세션 쿠키를 15분짜리 액세스
토큰 + 리프레시 로테이션이 있는 서명된 JWT로 옮겼고, 기존 쿠키 경로는 플래그 뒤에서
한 릴리스 동안 계속 받아. 인증 테스트는 61/61 통과(이전 48개), 부하 테스트는 2,400 req/s
에서 p99 41ms, 아직 리프레시 토큰 재사용 탐지와 여러 기기 동시 로그아웃은 처리 못 했어.
배포 전에 시니어 엔지니어 3명한테 승인을 받아야 해. 설득 문서 만들어줘.
