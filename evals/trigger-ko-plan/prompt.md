---
description: "Korean trigger phrase for the plan skill: '수정확률순으로 계획'"
tags: [trigger, ko, plan]
runs: 3
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill]
---

단일 테넌트 Postgres 스키마를 모든 테이블에 tenant_id 컬럼을 두는 구조로 바꾸려고 해.
row-level security랑 이미 예전 구조로 들어와 있는 고객 3곳 마이그레이션까지 포함이야.
수정확률순으로 계획 세워줘.
