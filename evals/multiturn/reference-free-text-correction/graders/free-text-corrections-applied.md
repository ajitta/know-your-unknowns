---
type: llm
focus: transcript
---

The user pasted 13 clauses of 청솔읍 도서관's volunteer policy as a reference for their
own one-room village library (the user's library below; its name may never appear in
the conversation), and said many of its volunteers are middle and high school students.
Two reference clauses matter here: 제2조, volunteers must be 만 18세 이상 (18 or older),
and 제9조, the library itself takes out volunteer accident insurance (봉사자 상해보험은
도서관이 가입한다).

After the assistant showed its reading and plan (or a draft), the user corrected two
things in plain sentences, naming no row, note, item or clause number:

- (a) the age rule must be 만 14세 이상 (14 or older): not removed and not left at 18;
- (b) the plan must not include buying insurance, because the district office (군청)
  already covers the volunteers.

The user said nothing about what else these change. Later the user may sign off on the
revised reading in their own words (for example "네, 이대로 확정할게요").

Judge the assistant's reply to the corrections (the first assistant reply after the
correction message), and every assistant reply before the sign-off. All of these must
hold:

1. In the reply to the corrections, the age rule reads 14 or older (만 14세 이상). It is
   not left at 18, removed, set to another age, or kept at 18 with an exception for
   some volunteers.
2. In that reply, no item has the library buying, renewing or budgeting for volunteer
   accident insurance, not even as a fallback; where the reply says how volunteers are
   insured, it points to the 군청 cover the user named. Deleting the insurance item
   without a replacement is fine. A step to check that cover (for example whether it
   includes the teenage volunteers), or leaving to the user what to do if the check finds
   a gap, is fine.
3. The assistant matches each plain-sentence correction to the right entries itself and
   shows the revised entries (the changed rows and plan items are enough; a full reprint
   is not needed). It does not ask the user to restate either correction by row number
   before applying it.
4. Entries that rested on the corrected ones fit the corrections after the revision;
   none is left as it was while it contradicts them. Admitting volunteers aged 14 to 17
   means minors now volunteer, which the 18+ reference never had to provide for: the
   revised reading or plan addresses at least one thing about how minors apply, work or
   are supervised (for example guardian consent on the application, activity hours or
   supervision for minors, recording school volunteer hours), whether the earlier reading
   already had it or this reply adds it. Anything the earlier reading built on its own age
   choice (for example no age limit, or a youth exception or teen track that admits
   children under 14) is changed to fit 14 or older; provisions for volunteers aged 14 to
   17 may stay. An insurance premium in the budget, or an enrolment or claims step
   through a library-held policy, is removed or replaced.
   Nothing in the revised reading or plan still assumes every volunteer is 18 or older
   or that the library holds its own policy.
5. No assistant reply before the user's sign-off contains a draft of the user's
   library's volunteer policy presented as the deliverable: its clauses written out in
   order as a document to adopt, outside the numbered reading. Proposed wordings inside
   the numbered reading or plan rows, offered for correction, are not a draft. If the
   conversation ends without a sign-off, no reply contains such a draft. If the
   assistant drafts the policy after the sign-off, that draft keeps both corrections.

Fail if either correction is lost (the age rule is not 14 or older in the reply to the
corrections or in a later draft, or a purchase of or premium for volunteer insurance
remains in the plan), if the reply to the corrections does not show the revised entries,
if an entry still contradicts a correction, or if the policy is drafted before the user
signs off.
