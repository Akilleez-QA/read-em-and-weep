# Exceptional carriers: fixed seed 4, row 2, standards (3,11,15), E12

## Exact result

The remaining 106336 source-first full-owner triples containing carrier 0 or star 5 have identically zero selected contraction. No support-envelope overlap remains unresolved in this exceptional domain. This proof uses the pinned source matrix directly and spends zero physical products.

Ordering scope is the existing fresh consistent source definition in fresh_source_order_contract.py: key (-1 if star else carrier, legal_mask, standard_tag). No new historical fullMask/fullStandard ordering witness was found, and no historical values are imported or reindexed. The exceptional column-zero identity itself survives arbitrary ordering within each carrier block; the exact combined counts use the stated fresh canonical order.

There are 96 carrier/mask pairs in canonical order (star 5,0,1,2,3,4), each with 16 masks. Increasing standard tags (3,11,15) permit repeated carrier/mask pairs, so the complete domain has binomial(98,3)=152096 triples. The previously audited primary-only domain has binomial(66,3)=45760. Their disjoint difference is 106336.

Every exceptional-containing ordered triple begins with star 5, or with carrier 0 if no star occurs. In both charts the pinned P[:,6] column consists of two empty polynomial lists. Therefore the full selected contraction

sum over u,w of I[12,u] tf(R)[w,u] P[w,6]

is literally zero for every rational current R. This uses the transpose correctly, makes no carrier-1 selector substitution, and does not assume the current is already trace-free. It covers all four E12 terms and both A/B scalar multipliers before edge differentiation or outer multiplication. Scalar restriction of the zero expression remains zero on the legal source domain.

Of the exceptional tuples, 101962 already have an outer weight structurally zero; 4374 are not excluded by that outer test. All 106336 are independently annihilated by the selected-column identity. “Not structurally zero” is not a nonvanishing assertion.

## Denominator authentication

The separate module authenticates the pinned model hash and actual di, dp, dh lists for all six carriers. For carrier 0 the denominator is -h0 = v1*v2*v3*v4 - 1, with finite v0=1 and pivot 0. For star the denominator is -v1*a = -v1^2*v3*v4, not -a. Both exceptional charts use pivot 0. On D(a), v1 is a unit because a=v0*v1*v3*v4; its inverse is v0*v3*v4/a. The finite chart has v0=1.

The new rational AST lowers I and P over their actual owned D factors and inherits only the exact matrix/current operations. The old edge-denominator, quotient and outer-cancellation entry points are explicitly blocked: no general exceptional clearance theorem is claimed or needed. The zero-column proof precedes all such clearance questions. Existing primary files remain untouched.

## Files and scope

- lower_exceptional_carrier_sector.py: authenticated exceptional rational AST, full transpose selector, exhaustive source-order partition
- exceptional-carrier-domain-partition.json: complete counts and source certificates
- test_exceptional_carrier_sector.py: independent physical-label enumeration, exact source metadata checks, every exceptional carrier sector and all equal-owner masks, source-order guards
- exceptional-carrier-test.log: validation result

Together with the existing primary-carrier certificate, this gives a fixed-seed/fixed-row/fixed-staircase E12 zero result, subject to independent review of this new proof. It does not certify E34, other seeds, rows or staircases, the full detector, or factorization.

Physical products spent: 0. Private resource configuration is omitted; execution release remains false. Execution release and actual factorization acceptance remain false. No physical polynomial evaluation or expansion was performed.
