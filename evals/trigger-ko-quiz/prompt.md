---
description: "Korean trigger phrase for the quiz skill: '퀴즈'"
tags: [trigger, ko, quiz]
runs: 3
max_turns: 6
timeout_seconds: 240
allowed_tools: [Read, Glob, Grep, Skill]
---

우리 저장소에 접근할 수 없으니 변경 내용을 그대로 붙여넣을게. 내가 쓴 코드가 아니라
에이전트가 쓴 거고, 이제 PR 올려서 방어해야 해. 퀴즈 내줘.

```python
@app.post("/hooks/stripe")
def receive(req):
    raw = req.get_data()
    if not hmac.compare_digest(sign(raw, SECRET), req.headers["Stripe-Signature"]):
        return "", 400                      # 파싱 전에 서명 검증
    event = json.loads(raw)
    if seen.setdefault(event["id"], time.time()) < time.time() - 300:
        del seen[event["id"]]               # 5분 중복 제거 윈도우
    elif len(seen) > 1:
        return "", 200                      # 이미 처리함
    queue.put(event)
    return "", 200                          # 먼저 ack, 작업은 나중에
```
