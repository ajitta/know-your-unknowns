---
description: "Korean trigger phrase for the notes skill: '이탈 기록'"
tags: [trigger, ko, notes]
runs: 3
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill]
---

계획서에는 내보내기 잡 상태를 Redis에 24시간 TTL로 저장한다고 되어 있었어.
그런데 스테이징에 Redis가 없어서 기존 jobs 테이블에 status 컬럼을 추가해서 넣었어.
이탈 기록해줘.
