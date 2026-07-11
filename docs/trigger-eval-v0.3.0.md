# 트리거 · 루프 준수 eval — v0.3.0 (2026-07-11)

사각지대 보고서 항목 4(자동 트리거 발화율)·항목 5(루프 준수) 전환 기록.
환경: Claude Code 2.1.207 (macOS), headless `claude -p`, 새 프로세스가 플러그인을
디스크에서 로드 — **loop/plan description 트리거 경계 수정 이후 상태를 측정**.

## 1. 자동 트리거 발화 (항목 4)

방법: 슬래시 없이 문서화된 트리거 문구가 담긴 자연어 프롬프트로 새 세션 실행
(`--max-turns 4`, Edit/Write/Bash 차단), transcript(stream-json)에서 Skill 호출 추출.

| 케이스 | 프롬프트 문구 | 발화 스킬 | 발화 위치 |
|--------|--------------|-----------|-----------|
| blindspot-en | "What am I missing?" | `unknowns:blindspot` | 첫 도구 호출 |
| blindspot-ko | "내가 놓친 게 뭐지?" | `unknowns:blindspot` | 첫 도구 호출 |
| plan-en | "plan this: add a --verbose flag …" | `unknowns:plan` | 첫 도구 호출 |
| plan-ko | "계획 세워줘: …" | `unknowns:plan` | 첫 도구 호출 |
| quiz-en | "quiz me on how the … hook works" | `unknowns:quiz` | 첫 도구 호출 |
| quiz-ko | "…이해했는지 퀴즈 내줘" | `unknowns:quiz` | 첫 도구 호출 |

**결과: 6/6 발화, 오발화 0.** 한국어 문구는 영어 본문 description 안에서도
정상 매칭(v0.3.0 혼합 언어 구성의 첫 런타임 증거 — CHANGELOG 주장 실측 확인).

한계: 문구당 n=1, 스킬 3/11종만 표본, 단일 모델·단일 머신. 결정적 테스트가 아니라
표본 관측. 미측정: teach-me/reference 등 나머지 8종, 유사 문구 오발화율(충돌 쌍),
타 플러그인 공존 환경에서의 경합.

## 2. 루프 준수 (항목 5)

방법: 격리된 scratch git repo(소형 `backup.py`)에서
`/unknowns:loop backup.py에 --dry-run 플래그 추가…(완료 기준 명시)` 실행,
`--max-turns 30`, transcript에서 도구 시퀀스·단계 추출.

관측 (6 turns, ~82s, exit success):

1. 모델 첫 발화: "Task small (1 file, clear done criteria). **Loop scale-down: skip
   full loop, use step-7 notes rules + verify.**" — SKILL.md의 scale-down 기준
   ("Small fix (1–2 files, clear spec): step-7 rules only")과 일치.
2. Read → Edit → 실행 검증(dry-run/일반 모드 모두, 완료 기준 대조) → 정리.
3. 최종 메시지에 검증 결과 + **Deviation notes** 섹션 포함.
4. 테스트 정리 중 tracked 파일 삭제 실수를 스스로 감지하고 `git checkout --`으로
   복구 — 이탈을 인지·보고함.

**결과: scale-down 규칙 준수 확인 (소형 과제 1건 기준).**

발견된 편차: 이탈 기록을 IMPLEMENTATION_NOTES.md **파일이 아닌 최종 메시지**로
전달 — notes 규칙의 파일 영속화("Location: IMPLEMENTATION_NOTES.md at project
root, create if missing")와 불일치. 소형 과제 단발 세션에서는 합리적 판단일 수
있으나, 규칙 문면과는 다름.

미측정: 중형(2→3→6→7→9)·대형(10단계 전체) 티어 — headless에서는 interview 단계가
사용자 부재로 성립하지 않아 대화형 세션 측정 필요.

## 재현

```bash
# 산출물: scratchpad/eval/*.jsonl, scratchpad/loop-run.jsonl (세션 임시 디렉토리)
claude -p "<트리거 문구 포함 프롬프트>" --output-format stream-json --verbose \
  --max-turns 4 --disallowedTools "Edit" "Write" "Bash"
```
