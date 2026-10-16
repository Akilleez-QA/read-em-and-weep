# Six standard-permutation inventory and primary-carrier extension

## Exact domain and ordering

For fixed pre-sort staircase tags (3,11,15), independently assigning a carrier/mask pair to each position gives 96^3=884736 full assignments or 64^3=262144 primary-carrier assignments. Source sorting uses (auxiliary-first carrier rank, low-bit integer mask, standard tag). Every assignment gives distinct full owners, even when physical carrier/mask pairs coincide. No factorial division is valid here.

The sorted standard permutations, signs and full/primary counts are:

- (3,11,15): +1; 152096 / 45760
- (3,15,11): -1; 147440 / 43680
- (11,3,15): -1; 147440 / 43680
- (11,15,3): +1; 147440 / 43680
- (15,3,11): +1; 147440 / 43680
- (15,11,3): -1; 142880 / 41664

For N available physical pairs, a specified tag permutation with d adjacent descents has binomial(N+2-d,3) assignments. Adjacent descent requires a strict increase of physical pair; an ascent permits equality. Subtracting the preceding descent count reduces this to a weak sequence. This also independently verifies the finite-label inventory counts. Signs count all inversions, not descents.

The prior slice omitted 732640 full-domain assignments, including 216384 primary assignments. The full label inventory is in permuted-standard-domain-inventory.json. Its exceptional-first activity counts are metadata only; the separate exceptional-carrier audit owns their contraction proof.

## Uniform reduction before scanning

Outer activity requires each primary carrier c<=popcount(tag), each legal bit supported on an infinity standard bit, and carrier 4 at tag15. Thus the tag15 owner must sort last among primary owners: tag3 has carrier<=2, tag11 carrier<=3. Four of the five omitted tag permutations are entirely outer-zero, accounting for 172704 primary assignments.

The remaining (11,3,15) slice has 43680 primary assignments: 42784 outer-inactive, 192 active (2,2,4) assignments, and 704 active first-carrier1 assignments. Carrier2 has an empty pinned I[12] row and P[:,6] column. The 704 remaining tuples consist exactly of (1,1,4), 192, and (1,2,4), 512. For same-carrier first two owners, tag11>tag3 requires a strictly increasing mask; this is why there are 192 rather than 320.

There is no asserted coordinate symmetry taking this slice to the old slice. Such a claim would risk changing kappa, derivatives, edge characters or selector owner. Instead, new lowering retains actual source-first vertices, the actual kappa=(-1,-2,-2,-2), E12 input character=(0,0,-2,-2), each exact derivative coordinate, and the selector -2*(I_first transpose(tf(R)) P_first)[12,6]. The fixed staircase remains pre-sort (3,11,15); the source-sorted labels are (11,3,15), with external sorting sign -1. A global scalar sign does not affect support bounds, but is retained explicitly rather than dropped from the source contract.

## New finite-label support certificates

All 704 new tuples have 8 certified-zero A/B multipliers, 5632 total. Only two normals are needed:

- L edge (1,2): (0,0,-1,-1). Minimum gap 658 for (1,1,4), 317 for (1,2,4).
- U edge (0,1): (0,-1,0,1). Minimum gap 635 in both sectors.

The first new checked case is carriers(1,1,4), masks(0,4,0), sorted tags(11,3,15); all 8 multipliers separate. The other representative is carriers(1,2,4), masks(0,0,0). Overlap would remain unresolved; none occurs in this exact primary remainder.

The lowering class is an exact copy of the audited original with only the ordered-standard guard changed to an equal-multiset guard. The build function is separately parameterized over sorted tags and records the permutation sign. The original lowering and prior certificates are unchanged. Tests check source-copy equivalence, independently derive permutation counts, authenticate the selector owner/entry/coefficient for all six permutations, and independently replay every support separator with the simplex-vertex implementation.

## Boundary

This audit closes the omitted primary-carrier label slices only, subject to the accompanying independent test log. It does not itself certify the exceptional carriers, other seeds, other detector rows, other characters, historical-order comparison, global factorization, or arithmetic resource admission. It supplies no nonvanishing claim.

Only finite labels and factored AST metadata were manipulated. Physical polynomial evaluation, expansion and composition-summand enumeration: none. Private resource configuration is omitted; execution release remains false. Execution release and actual factorization acceptance remain false.

Verification completed: all four main tests passed, including independent replay of all 5632 saved separators. The two added tests (exact build-function change check and exhaustive primary owner/tag outer-zero check) also passed separately; see permuted-standard-test.log and permuted-standard-additional-test.log. No new primary tuple remains unresolved.
