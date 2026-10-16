# Primary carrier support audit: seed 4, row 2, standard tags (3,11,15), E12

## Result and exact scope

The implemented primary-carrier domain is carriers **1,2,3,4 only**. Within that domain every source-first full-owner triple is excluded. Carrier 0 and star (physical index 5) are outside this lowering and are not covered. This is not a global detector/factorization certificate.

Full owner keys are `(seed=4, ordinal, carrier, legal_mask, standard_tag)`, with ordinal retained separately from source ordering `(carrier, legal_mask, standard_tag)`. Tags are assigned in order `(3,11,15)`. Because these tags strictly increase, source-first triples correspond to nondecreasing triples of 64 `(carrier, legal_mask)` pairs. There are `binomial(66,3)=45760` triples; equal carrier/mask pairs still have distinct standard-tag owners.

- 43584 triples have an outer-inactive owner. Exact quotient AST returns literal zero if the legal mask has a finite-standard bit, the carrier exceeds the standard popcount, or the all-infinite owner has carrier other than 4.
- 832 outer-active triples have first carrier 2: (2,2,4), 320; (2,3,4), 512. The pinned chart's entire I[12] row and P[:,6] column are empty, so every selected contraction is literally zero before outer multiplication.
- 1344 remaining outer-active triples have first carrier 1. The previous fixed-carrier artifact certifies all 512 tuples in (1,2,4). The new artifact checks all 320 tuples in (1,1,4) and all 512 tuples in (1,3,4), totaling 6656 new A/B multiplier certificates. Every multiplier separates from its complete numerator domain.

## Discriminating cause and proof repair

Reusing the original two normals does not uniformly work in the next carrier sector. In (1,3,4), legal(0,0,0), the original U normal `(0,-1,0,1)` overlaps the numerator domain; that is unresolved, not nonzero. The normal `(0,-1,1,1)` separates and works for all 2048 U multipliers in that sector, with minimum strict integer gap 145. The L normal `(0,0,-1,-1)` certifies 2040 of its 2048 L multipliers; the original `(1,0,1,1)` certifies the other eight, with sector minimum gap 31.

For (1,1,4), all 1280 L multipliers use `(1,0,1,1)` with minimum gap 131; all 1280 U multipliers use `(0,-1,0,1)` with minimum gap 635. Thus carrier changes alter the useful supporting direction, while support exclusion survives across the entire implemented primary domain.

The bound arithmetic uses exact integers on the AST and its bounded-composition index domains. It never enumerates physical composition sums, evaluates physical polynomials, expands them, or extracts coefficients. Each certificate includes the exact root, full owner labels, full numerator degree, B derivative lower bound, support normal, and strict gap. Cancellation-blind support envelopes only prove zero by separation. No overlap is promoted to nonvanishing.

## Files and verification

- `lower_primary_carrier_sector.py`: separate copy of the audited parameterized lowering, with only carrier substitution, explicit range guard, and scope text changed.
- `preflight_primary_carrier_sector.py`: exact support scanner over all 832 new legal tuples, with fallback over all 80 nonzero ternary normals.
- `primary-carrier-sector-support.json`: all 6656 certificates and exact owner/AST hashes.
- `test_primary_carrier_sector.py`: independent simplex-vertex bound replay, independent domain partition, literal-zero outer-owner check, pinned chart row/column check, and exact source-change comparison.
- `primary-carrier-independent-test.log`: all four tests passed in 146.440 seconds, including independent replay of every new separator.

The prior 512-tuple sector is incorporated by its separately audited `legal-mask-sector-support.json` and `test_legal_mask_sector.py`; the new audit does not claim to replace that test.

Physical products spent: 0. Private resource configuration is omitted; execution release remains false. Execution release and actual factorization acceptance remain false.
