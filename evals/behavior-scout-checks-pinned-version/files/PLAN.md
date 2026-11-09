# Request validation for the two unchecked endpoints

## Why

PATCH /customers/<id> and POST /orders/<id>/pickup-time take the JSON body as it
comes and write it into the stored record. Last week a typo in the website's form sent
`{"emial": "..."}` and the customer record kept a field nobody reads, and a pickup time
of "tomorrow" was stored as text and broke the shop's morning printout.

## Change

1. app/models.py: add `CustomerUpdate` (name, email, phone, all optional, unknown fields
   rejected) and `PickupChange` (pickup_at, inside opening hours).
2. Validate each body using pydantic's model_validate and @field_validator, like the rest
   of the codebase.
3. A bad body gets a 422 with the error list, as POST /customers and POST /orders do now.
4. Tests for both endpoints: a good body, an unknown field, a bad value.

## Done when

- Both endpoints reject an unknown field and a bad value with a 422.
- A pickup time outside 07:00-18:00 is rejected the same way as on POST /orders.
- `python -m unittest` passes.

Owner: Priya. Estimate: half a day.
