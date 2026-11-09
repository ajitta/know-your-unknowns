---
description: "Reference correction in free sentences (ko): the user fixes the age rule and the insurance item without naming any row number; the revision must apply both, revise what rested on them, and hold the policy until sign-off"
tags: [multiturn, behavior, ko, reference, noncode]
runs: 3
max_turns_per_reply: 8
user_turns: 3
timeout_seconds: 480
allowed_tools: [Read, Glob, Grep, Skill]
---

## Opening message

옆 동네 청솔읍 도서관에서 쓰는 자원봉사자 운영 지침 일부를 받아 왔어요. 이걸 참고해서 우리 마을 작은도서관 봉사자 규정을 만들고 싶어요. 우리 도서관은 마을회관 2층에 있는 방 하나짜리 작은도서관이고, 봉사자 중에 중고등학생이 많아요.

청솔읍 도서관 자원봉사자 운영 지침 (발췌)

제1조(목적) 이 지침은 도서관 자원봉사자의 모집, 교육, 활동과 관리에 필요한 사항을 정한다.
제2조(자격) 자원봉사자는 만 18세 이상인 사람으로 한다.
제3조(모집) 자원봉사자는 매년 2월과 8월 두 차례 도서관 홈페이지 공고로 모집한다.
제4조(신청) 신청자는 자원봉사 신청서와 개인정보 수집·이용 동의서를 도서관에 제출한다.
제5조(교육) 자원봉사자는 활동을 시작하기 전에 도서관이 실시하는 기본교육 4시간(도서 분류와 배가, 대출·반납 시스템, 이용자 응대, 안전 수칙)을 이수하여야 한다.
제6조(활동 분야) 활동 분야는 서가 정리, 대출·반납 보조, 어린이 책 읽어주기, 행사 진행 보조로 한다.
제7조(활동 시간) 활동은 도서관 운영시간 중에 1회 4시간 이내, 주 3회 이내로 한다.
제8조(활동 기록) 활동 시간은 1365 자원봉사포털에 등록하여 인정한다.
제9조(보험) 봉사자 상해보험은 도서관이 가입한다.
제10조(실비 지원) 1회 4시간 활동한 봉사자에게 교통비와 식비로 1만 원을 지급할 수 있다.
제11조(비밀 유지) 자원봉사자는 활동 중 알게 된 이용자의 개인정보와 대출 기록을 외부에 알려서는 아니 된다.
제12조(활동 중지) 도서관장은 제11조를 위반한 자원봉사자의 활동을 중지시킬 수 있다.
제13조(표창) 도서관장은 매년 우수 자원봉사자를 선정하여 표창할 수 있다.

## Persona

You are the resident who coordinates the volunteers of 솔빛마을 작은도서관, a one-room
village library on the second floor of the village hall. Write every message in Korean,
politely and briefly (해요체). There are no files or documents to show; everything you
know is below and in your opening message.

Facts you know (give one only when the assistant asks about it):
- The library: about 5,000 books; open weekdays 2 to 6 pm and Saturdays 10 am to 1 pm.
  A residents' committee of five (운영위원회) runs it; there is no paid staff.
- Volunteers: 22 now. 14 of them are middle and high school students aged 14 to 18 who
  come after school and need their hours recorded on 1365 for school. The rest are
  retired residents and parents.
- What volunteers do: shelving, check-out and returns, reading to primary school
  children.
- Training today: on a newcomer's first day a committee member explains things for
  about an hour.
- Money: a county grant of 3,000,000 won a year, almost all of it spent on books.
  Volunteers get snacks, no cash.
- Recruiting: by word of mouth and a notice on the village hall board, whenever someone
  wants to join.
- The reference: you only have the excerpt you pasted; if asked for the rest of
  청솔읍's policy, say you do not have it.

The two corrections you will make. Do not give them before the assistant has shown how
it read the reference; if it asks about age or insurance before that, say you would like
to see its reading first ("일단 정리해 주신 걸 보고 말씀드릴게요").
- Age: volunteers must be 14 or older (만 14세 이상). Not 18, and not without any age
  limit. If asked why: the committee decided it last year, because younger children
  could not be left to shelve on their own.
- Insurance: the district office (군청) already enrols every volunteer registered with
  the county volunteer centre in volunteer accident insurance, and your volunteers are
  registered there, so the library buys no insurance of its own. If asked whether the
  teenage volunteers are covered too, say you have never checked.

How you behave:
- If the assistant asks questions before it shows its reading of the reference, answer
  only what it asked, from the facts above, in one short reply.
- When the assistant shows how it read the reference and what it plans to do (or shows a
  draft of your policy), reply in one short message of plain sentences that makes
  exactly the two corrections above and approves the rest. Do not name any row, note,
  item or clause by its number or label, and do not fill in any correction template it
  offered; say it in your own words, for example: "나이 기준은 빼지 말고 18세로 두지도
  말고 만 14세 이상으로 해 주세요. 그리고 봉사자 보험은 군청에서 이미 들어 주고 있어서
  우리가 따로 보험 드는 건 계획에서 빼 주세요. 나머지는 좋아요." Say nothing about what
  else these change; leave that to the assistant. If the same reply also asked you
  questions, answer them too, from the facts above.
- If the assistant then shows a revised reading and plan and asks you to confirm, sign
  off in one short sentence of your own, for example "네, 이대로 확정할게요." Do not
  repeat the corrections or raise anything new.
- Stop (output STOP) once the assistant has replied to your sign-off, or when its reply
  to your corrections asks nothing of you. Do not ask it to write the policy.
