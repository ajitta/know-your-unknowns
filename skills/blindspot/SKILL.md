---
name: blindspot
description: >
  Blind-spot pass — investigate unknown unknowns BEFORE implementation. This skill
  should be used when the user says "blind spot pass", "blindspot", "사각지대 조사",
  "내가 모르는 게 뭐지", "find my unknowns", "unknown unknowns", or is about to start
  work in an unfamiliar domain, library, or codebase area and wants to discover what
  they are missing before writing a fuller prompt or spec. Do NOT trigger for routine
  tasks the user clearly understands.
argument-hint: "<작업 설명 또는 대상 영역> [컨텍스트 소스: git/docs/slack 등]"
---

# Blindspot Pass — 사각지대 조사

구현 전에 **지도(계획·프롬프트)와 영토(실제 코드베이스·도메인·제약)의 간극**을 찾는다.
원 출처: Thariq Shihipar — "I'm working on X that I know nothing about. Do a blind-spot
pass to help me figure out my relevant unknown unknowns and help me prompt better."

## 철칙

1. **아직 구현하지 마라.** 이 스킬이 활성화된 동안 코드를 수정하지 않는다.
2. 조사 결과는 사용자가 **더 나은 프롬프트를 쓰도록 돕는 것**이 최종 목적이다.

## 절차

1. `$ARGUMENTS`에서 작업 설명과 컨텍스트 소스를 파악한다. 소스가 지정되면(git 히스토리,
   docs, 특정 모듈 등) 그곳을 우선 조사한다.
2. 조사 범위가 코드베이스 전반이거나 크면 **unknowns-scout 에이전트**에 위임한다.
   범위가 파일 몇 개 수준이면 직접 Read/Grep/Glob으로 조사한다.
3. 다음 6가지를 정리한다:
   - 사용자가 놓치고 있을 가능성이 높은 **전제(assumption)**
   - 예상되는 **unknown unknowns** (계획에 없는 결정 지점)
   - 기존 구조·관례와 **충돌할 수 있는 부분**
   - 변경 시 **회귀 가능성이 높은 영역** (테스트 커버리지 포함)
   - 구현 전에 **답해야 할 질문**
   - 프롬프트를 더 정확하게 만들기 위해 **필요한 정보**
4. **중요도 × 영향도** 기준으로 정렬해 제시한다.
5. 마지막에 조사 결과를 반영한 **개선된 프롬프트 초안**을 제시한다 — 이것이 이 스킬의
   핵심 산출물이다.
6. 아키텍처를 바꿀 수 있는 미결정 사항이 발견되면 `/unknowns:interview`로 이어가기를
   제안한다. 낯선 도메인의 어휘 자체가 부족하면 `/unknowns:teach-me`를 제안한다.

## 산출물 형식 (HTML 우선)

렌더링 가능한 환경(Cowork·아티팩트 뷰어)에서는 **단일 파일 인터랙티브 HTML**로 만든다:
발견 1건 = 카드 1장(분류·발견·왜 중요한가·권장 조치), 각 카드에 그 발견을 반영한
**복사 가능한 "프롬프트 픽스"** 버튼, 카드 선택 시 선택된 픽스들이 하단에서
**개선된 프롬프트 초안으로 자동 조립**되는 구조. CSS/JS 인라인, 외부 의존성 없음.
뷰어가 없는 CLI 환경이면 같은 구조의 마크다운 테이블 + 프롬프트 초안으로 폴백한다.

## 적용 범위

코드에 한정되지 않는다. 새로운 분야 학습(예: 색보정, 결제, 인증, 물리엔진)에도 동일하게
적용한다 — 모델이 사용자보다 그 분야를 더 알고 있는 경우가 많으므로, 끌어내는 것이 목적이다.
