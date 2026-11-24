#!/usr/bin/env bash
# The garden centre group's 214 supplier agreements, as contracts/ in the run's working
# directory, written from the two templates in templates/, plus policies/ and notes/ from
# files/. The same 214 files every time: each field comes from the contract's number.
# 36 contracts, picked by a fixed hash of the number (GC-0009, GC-0013, GC-0014, ...
# GC-0211) and signed in 2019 and 2020, are on the 2019 template, whose clause 7.3 allows
# a change to the payment terms only by a written amendment signed by both parties; the
# other 178, signed from 2022 to 2025 on the GC-SUP-2022 template, let the buyer change
# them by 30 days' written notice. Clause 7.1 of every contract sets payment within 30
# days.
set -eu
here="$(cd "$(dirname "$0")" && pwd)"
shopt -u patsub_replacement 2>/dev/null || true

cp -R "$here/files/." .
mkdir -p contracts

old_template="$(cat "$here/templates/contract-2019.md")"
new_template="$(cat "$here/templates/contract-2022.md")"

names=(Ashby Brook Calder Dunmore Elmfield Fairhaven Glenroy Hartwell Ivybridge Juniper
       Kestrel Larchwood Marsden Northfield Oakridge Pennine Quarrybank Rowan Severn
       Thornbury Upland Valley Willowmere Yewdale)
slugs=(ashby brook calder dunmore elmfield fairhaven glenroy hartwell ivybridge juniper
       kestrel larchwood marsden northfield oakridge pennine quarrybank rowan severn
       thornbury upland valley willowmere yewdale)
# category|name suffix|suffix slug|what the agreement supplies (clause 3)
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
  # a fixed hash of the number spreads the 2019 template and the supplier sizes
  h=$(( (i * 1103515245 + 12345) % 2147483648 / 65536 ))

  if (( h % 6 == 0 )); then
    template="$old_template"
    year=$(( 2019 + (h / 6) % 2 ))
  else
    template="$new_template"
    year=$(( 2022 + i % 4 ))
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

  text="$template"
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
  printf '%s\n' "$text" > "contracts/$number-$slug.md"
done
