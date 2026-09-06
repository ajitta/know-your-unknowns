---
description: "Korean trigger phrase for the blindspot skill: '내가 놓친 게 뭐지'"
tags: [trigger, ko, blindspot]
runs: 3
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill]
---

저장소를 볼 수 없으니 구조를 여기 적을게. 결제 서비스는 카드 처리사(승인·매입·환불),
사기 탐지 스코어러, 그리고 우리 원장 서비스로 외부 호출을 해. 나는 이 호출 전부에
공통 재시도 + 백오프 데코레이터를 씌우려고 해. 일시적인 502 때문에 결제가 실패하는 걸
막으려는 거야. 이 부분 코드는 처음 봐. 내가 놓친 게 뭐지?
