#!/usr/bin/env python3
"""[field-guide] PostToolUse(Edit|Write) hook.

파일 수정이 임계값(기본 10회)에 도달하면 세션당 1회, IMPLEMENTATION_NOTES.md에
계획 이탈을 기록하라는 리마인더를 systemMessage로 띄운다.

- 표준 라이브러리만 사용 (jq 등 외부 의존성 없음)
- 상태는 /tmp 에 세션별 파일로 저장
- FIELD_GUIDE_NOTES_THRESHOLD=0 으로 비활성화
"""
import json
import os
import sys
import tempfile


def main() -> int:
    try:
        threshold = int(os.environ.get("FIELD_GUIDE_NOTES_THRESHOLD", "10"))
    except ValueError:
        threshold = 10
    if threshold <= 0:
        return 0

    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0

    session_id = str(data.get("session_id", "default"))[:64]
    state_path = os.path.join(
        tempfile.gettempdir(), "field-guide-notes-%s.json" % session_id
    )

    state = {"count": 0, "reminded": False}
    try:
        with open(state_path, "r", encoding="utf-8") as fh:
            loaded = json.load(fh)
        if isinstance(loaded, dict):
            state.update(loaded)
    except Exception:
        pass

    state["count"] = int(state.get("count", 0)) + 1
    fire = state["count"] >= threshold and not state.get("reminded", False)
    if fire:
        state["reminded"] = True

    try:
        with open(state_path, "w", encoding="utf-8") as fh:
            json.dump(state, fh)
    except Exception:
        pass

    if fire:
        cwd = data.get("cwd") or ""
        notes_path = os.path.join(cwd, "IMPLEMENTATION_NOTES.md")
        exists = os.path.exists(notes_path)
        tail = (
            "." if exists
            else " (파일이 아직 없습니다 — /field-guide:impl-notes init 으로 시작)."
        )
        msg = (
            "[field-guide] 이번 세션에서 파일 수정이 %d회에 도달했습니다. "
            "계획·명세에 없던 결정(unknown)이 있었다면 IMPLEMENTATION_NOTES.md에 "
            "기록하세요%s" % (state["count"], tail)
        )
        print(json.dumps({"systemMessage": msg, "suppressOutput": True},
                         ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
