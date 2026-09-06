---
description: "Korean trigger phrase for the reference skill: '레퍼런스로 써'"
tags: [trigger, ko, reference]
runs: 3
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill]
---

Linear의 커맨드 팔레트 검색은 이렇게 동작해: 입력창 하나, 이슈·프로젝트·사람에 대한
퍼지 매칭, 종류별로 묶인 결과, 키보드만으로 이동, 연속 동작을 위해 열린 상태 유지.

우리 어드민 콘솔은 지금 `users` 테이블 하나에 대한 평범한 텍스트 입력창이고, 키를 칠
때마다 서버에서 LIKE 쿼리를 돌리고 엔터를 누르면 페이지가 넘어가. 이걸 레퍼런스로 써.
