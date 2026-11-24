#!/usr/bin/env bash
# The garden centre group's 214 supplier agreements, as contracts/ in the run's working
# directory, plus policies/ and notes/ from files/. The same 214 files every time: every
# choice below is arithmetic on the contract number, with no randomness.
#
# Each agreement is written from one of the four layouts in templates/, which differ in
# title, section order, numbering and headings, and most of its sentences are picked from
# two or three wordings written inline as [[one|two|three]]. No boilerplate line is shared
# by more than about a quarter of the files, so `sort | uniq -c` over the set does not
# fold it into a few documents.
#
# The facts the graders rely on. The payment clause of every agreement (7.1, 9.1, 5(a) or
# 8.1, by layout) sets payment within 30 days of receiving a valid invoice. 36 agreements,
# picked by a fixed hash of the number (GC-0009, GC-0013, GC-0014, ... GC-0211) and signed
# in 2019 and 2020, allow a change to the payment terms only by a written amendment signed
# by both parties; the other 178, signed from 2022 to 2025, let the Buyer change them by
# written notice of 30 days or one month. Each rule comes in five wordings and sits either
# in the payment clause (7.3, 9.3, 5(c) or 8.3) or in the general clause on variation
# (14.2, 13.2, 10(b) or 12.2); the slot it does not use holds an unrelated clause.
set -eu
here="$(cd "$(dirname "$0")" && pwd)"
shopt -u patsub_replacement 2>/dev/null || true

cp -R "$here/files/." .
mkdir -p contracts

# The four layouts' lines in one array: layout k (templates/layout-<k+1>.md) is lines
# first[k] to first[k+1] - 1.
tpl=()
first=()
for n in 1 2 3 4; do
  first+=("${#tpl[@]}")
  while IFS= read -r line || [[ -n $line ]]; do
    tpl+=("${line%$'\r'}")
  done < "$here/templates/layout-$n.md"
done
first+=("${#tpl[@]}")
# the clause of each layout that sets the payment period
payref=("clause 7.1" "clause 9.1" "clause 5(a)" "clause 8.1")
# how a template line offers its wordings: [[one|two|three]]
open='[['
close=']]'

# A change to the payment terms only by an amendment both parties sign: wordings for the
# payment clause, then for the general clause.
amend_pay=(
  "The payment terms in @PAYREF@ may be changed only by a written amendment signed by both parties."
  "The period for payment in @PAYREF@ may not be changed except by a written agreement signed on behalf of both the Buyer and the Supplier."
  "Neither party may change the payment terms alone: a change to @PAYREF@ takes effect only when both parties have signed it in writing."
  "The time for payment in @PAYREF@ cannot be extended or otherwise changed without the Supplier's consent, given in an amendment to this Agreement that both parties sign."
  "The payment terms are fixed for the life of this Agreement and can be varied only by a document in writing signed by both parties."
)
amend_gen=(
  "No variation of this Agreement, including any change to the payment terms in @PAYREF@, is effective unless it is in writing and signed by both parties."
  "This Agreement, including its payment terms, may be amended only by a written instrument signed by an authorised representative of each party."
  "Variations to this Agreement, the payment terms included, bind the parties only when they are recorded in writing and signed by both of them."
  "Neither party may vary any term of this Agreement, including @PAYREF@, by notice; a variation must be agreed in writing and signed by both parties."
  "Any change to this Agreement, the time for payment included, requires a written amendment signed by both parties."
)
# A change to the payment terms by the Buyer's written notice: the same two places.
notice_pay=(
  "The Buyer may change the payment terms in @PAYREF@ by giving the Supplier at least 30 days' written notice."
  "The Buyer may vary the period for payment in @PAYREF@ on not less than one month's notice in writing to the Supplier."
  "On giving the Supplier 30 days' notice in writing, the Buyer may replace the period in @PAYREF@ with a different period, which then applies to invoices received after the notice expires."
  "The Buyer may revise the payment terms from time to time by written notice to the Supplier, taking effect 30 days after the notice is given."
  "The Buyer may, by notice in writing given at least 30 days in advance, change the time within which it pays invoices under @PAYREF@."
)
notice_gen=(
  "No variation of this Agreement is effective unless it is in writing and signed by both parties, except that the Buyer may change the payment terms in @PAYREF@ by giving the Supplier at least 30 days' written notice."
  "This Agreement may be amended only in writing signed by both parties, but the Buyer may vary the payment terms in @PAYREF@ alone, by written notice to the Supplier given at least one month before the change takes effect."
  "The Buyer may vary @PAYREF@ by written notice to the Supplier given not less than 30 days before the variation takes effect. Any other variation must be agreed in writing and signed by both parties."
  "Variations bind the parties only when signed by both of them, other than a change to the payment terms, which the Buyer may make by giving the Supplier 30 days' notice in writing."
  "The Buyer may change the payment terms by written notice of at least 30 days; every other change to this Agreement needs a written amendment signed by both parties."
)
# what fills the slot the rule does not use
pay_filler=(
  "The Buyer pays by bank transfer to the account the Supplier has confirmed in writing to the Buyer's accounts payable team."
  "The Buyer may set off against any invoice any sum the Supplier owes it under this Agreement."
  "The Supplier sends a statement of account to the Buyer's accounts payable mailbox by the fifth working day of each month."
  "All prices and invoices are exclusive of VAT, which the Buyer pays in addition at the rate in force."
)
gen_filler=(
  "No failure or delay by a party in exercising a right under this Agreement waives that right."
  "Neither party may assign or transfer this Agreement without the other's prior written consent, which may not be unreasonably withheld."
  "If a court finds any provision of this Agreement invalid, the rest of this Agreement continues in force."
  "A person who is not a party to this Agreement has no right to enforce any of its terms."
)

names=(Ashby Brook Calder Dunmore Elmfield Fairhaven Glenroy Hartwell Ivybridge Juniper
       Kestrel Larchwood Marsden Northfield Oakridge Pennine Quarrybank Rowan Severn
       Thornbury Upland Valley Willowmere Yewdale)
slugs=(ashby brook calder dunmore elmfield fairhaven glenroy hartwell ivybridge juniper
       kestrel larchwood marsden northfield oakridge pennine quarrybank rowan severn
       thornbury upland valley willowmere yewdale)
# category|name suffix|suffix slug|what the agreement supplies
categories=(
  "Live plants|Nurseries|nurseries|Container-grown shrubs, perennials and bedding plants, delivered on trolleys that the Buyer returns with the next delivery."
  "Seeds and bulbs|Seeds|seeds|Packeted seeds and spring and autumn bulbs, in display units the Supplier provides and restocks."
  "Compost and growing media|Composts|composts|Bagged compost, bark and growing media, delivered on pallets."
  "Garden tools|Tools|tools|Hand tools, hoses and watering equipment, with point-of-sale stands."
  "Outdoor furniture|Furniture|furniture|Garden furniture sets, parasols and cushions, with the first order of each season assembled for display."
  "Pots and planters|Pottery|pottery|Glazed, terracotta and plastic pots and planters."
  "Pet supplies|Pet Supplies|pet-supplies|Pet food, bedding and accessories for the Stores' pet departments."
  "Cafe food|Foods|foods|Chilled and frozen food for the Buyer's cafes, delivered at the temperatures in the Supplier's food safety statement."
  "Cafe drinks|Beverages|beverages|Coffee, tea and soft drinks, and the loan and servicing of two coffee machines for each cafe."
  "Haulage|Haulage|haulage|Transport of goods between the Buyer's central yard and the Stores, on the weekly schedule the Buyer sets."
  "Cleaning|Cleaning|cleaning|Daily cleaning of the Stores' shop floors, cafes and toilets."
  "IT support|IT|it|Support for the tills, the stock system and the Stores' networks, with a response within 4 working hours."
  "Waste collection|Waste Management|waste-management|Collection of general waste, recycling and green waste from each Store, weekly or when the Store asks."
  "Timber and fencing|Timber|timber|Fence panels, posts, sleepers and decking boards."
  "Aquatics|Aquatics|aquatics|Pond liners, pumps, fish food and live fish for the Stores' aquatic departments."
  "Seasonal decorations|Decorations|decorations|Christmas trees, lights and seasonal decorations, ordered by 31 July for delivery from 1 November."
  "Signage and print|Print|print|Printed signs, plant labels and leaflets."
  "Garden care|Garden Care|garden-care|Lawn feed, weed control and plant care products."
)
towns=(Shrewsbury Kendal Ludlow Hereford Worcester Leominster Telford Malvern Stafford
       Lichfield Ashbourne Buxton)
firsts=(Alice Ben Chloe Dev Emma Farid Grace Harry Isla Jack Kiran Lucy Mo Nina Owen Priya)
lasts=(Ahmed Baker Clarke Davies Evans Fisher Green Hughes Iqbal Jones Khan Lewis Morgan)
months=(January February March April May June July August September October November
        December)

for ((i = 1; i <= 214; i++)); do
  a=$(( (i - 1) % 24 ))
  b=$(( (i - 1) / 24 ))
  c=$(( (a + 5 * b) % 18 ))
  IFS='|' read -r category suffix suffix_slug goods <<< "${categories[$c]}"
  supplier="${names[$a]} $suffix"
  slug="${slugs[$a]}-$suffix_slug"
  printf -v number 'GC-%04d' "$i"
  # a fixed hash of the number spreads the signed-amendment agreements and the sizes
  h=$(( (i * 1103515245 + 12345) % 2147483648 / 65536 ))
  layout=$(( (i * 3 + i / 6) % 4 ))
  wording=$(( (i * 2 + i / 4) % 5 ))

  if (( h % 6 == 0 )); then
    year=$(( 2019 + (h / 6) % 2 ))
    pay_rule="${amend_pay[$wording]}"
    gen_rule="${amend_gen[$wording]}"
  else
    year=$(( 2022 + i % 4 ))
    pay_rule="${notice_pay[$wording]}"
    gen_rule="${notice_gen[$wording]}"
  fi
  if (( (i * 4 + i / 6) % 5 < 2 )); then
    pay_slot="${pay_filler[$(( (i * 3 + i / 2) % 4 ))]}"
    gen_slot="$gen_rule"
  else
    pay_slot="$pay_rule"
    gen_slot="${gen_filler[$(( (i * 5 + i / 2) % 4 ))]}"
  fi

  month=$(( i % 12 ))
  day=$(( (i * 7) % 27 + 1 ))
  signed="$day ${months[$month]} $year"
  if (( month == 11 )); then
    start="1 January $(( year + 1 ))"
  else
    start="1 ${months[$(( month + 1 ))]} $year"
  fi

  case $(( (h / 7) % 3 )) in
    0) size="Small (fewer than 50 staff)" ;;
    1) size="Medium (50 to 249 staff)" ;;
    *) size="Large (250 staff or more)" ;;
  esac
  value="$(( (i * 37) % 190 + 8 )),000"
  lead=$(( i % 5 + 2 ))
  contact="${firsts[$(( i % 16 ))]} ${lasts[$(( i % 13 ))]}"
  email="orders@$slug.example"

  # the layout's lines, each [[...|...]] resolved by a hash of the number and the line
  text=""
  end=${first[$(( layout + 1 ))]}
  for ((ln = ${first[$layout]}; ln < end; ln++)); do
    line="${tpl[$ln]}"
    if [[ $line == *"$open"*"$close"* ]]; then
      pre=${line%%"$open"*}
      rest=${line#*"$open"}
      body=${rest%%"$close"*}
      post=${rest#*"$close"}
      count=1
      tmp="$body"
      while [[ $tmp == *'|'* ]]; do
        tmp="${tmp#*|}"
        count=$(( count + 1 ))
      done
      pick=$(( ((i * 7919 + ln * 104729) * 2654435761 >> 16) % count ))
      tmp="$body"
      for ((j = 0; j < pick; j++)); do
        tmp="${tmp#*|}"
      done
      line="$pre${tmp%%|*}$post"
    fi
    text+="$line"$'\n'
  done

  text="${text//@PAYSLOT@/$pay_slot}"
  text="${text//@GENSLOT@/$gen_slot}"
  text="${text//@PAYREF@/${payref[$layout]}}"
  text="${text//@NO@/$number}"
  text="${text//@SUPPLIER@/$supplier}"
  text="${text//@TOWN@/${towns[$(( i % 12 ))]}}"
  text="${text//@SIZE@/$size}"
  text="${text//@CATEGORY@/$category}"
  text="${text//@VALUE@/$value}"
  text="${text//@SIGNED@/$signed}"
  text="${text//@START@/$start}"
  text="${text//@GOODS@/$goods}"
  text="${text//@LEAD@/$lead}"
  text="${text//@CONTACT@/$contact}"
  text="${text//@EMAIL@/$email}"
  printf '%s' "$text" > "contracts/$number-$slug.md"
done
