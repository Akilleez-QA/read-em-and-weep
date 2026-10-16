# Independent review: seed-4 carrier-block order invariance

## Verdict

The new conditional zero theorem is mathematically supported: for the same refined seed-4 construction, any order preserving the declared carrier blocks gives zero E12 contribution when the reindexed scalar edge input belongs to the certified complete edge domain and its curvature belongs to the stated three-owner N14 domain. This closes that explicit curvature-defect target under these hypotheses. It does not authenticate an historical order or source or identify the historical scalar-41 detector.

The three requested prose clarifications below have been applied and checked; none changes the support calculation or zero conclusion. In particular, the local kernel built in fresh orientation is the negative of the operator comparison remainder on a reversed pair. Its vanishing proves the desired result with either sign.

The inspected independent metadata replay passed all three tests in 13.909 seconds on 2026-10-16, and passed again in 11.696 seconds after the final pre-import pin guard and prose corrections. It rebuilt all 256 new tuple ASTs and independently replayed all 512 A/B support associations. Minimum strict gap: 30. Only factored syntax, integer degree/denominator metadata, small support-polytope vertex calculations, and source/hash reads were used. No physical polynomial was expanded, multiplied as a polynomial representation, evaluated, or coefficient-extracted. No external post was made.

## Independent checks

### Exhaustive activity and reorder reduction

The total number of assignments is 96^3=884736. Exceptional assignments number 96^3-64^3=622592. The active primary carrier choices at fixed standard owners 3,11,15 are respectively {1,2}, {1,2,3}, {4}. Each such choice has 4*8*16=512 active mask assignments. Thus active primary assignments number 6*512=3072, and inactive primary assignments number 64^3-3072=259072.

Of the six primary carrier choices, two have minimum carrier 2, giving 1024 zero-selector assignments. Four have minimum 1. Three of those four have distinct carriers, yielding 1536 assignments on which every carrier-block order induces the same relative order. The remaining carrier pattern is (1,1,4), with 512 assignments.

Both carrier-1 owners have legal bit 1 zero; the standard-3 owner also has bit 0 zero. Exactly 256 assignments have bit 0 zero on the standard-11 owner and therefore zero complementary current difference. The other 256 are exactly {0,4,8,12} x {1,5,9,13} x {0,...,15}. The saved records equal that set without duplicates.

An arbitrary internal block order can either preserve or reverse the two carrier-1 owners. It cannot move the carrier-4 owner ahead of them. Consequently the only relevant local permutations are 012 and 102, irrespective of the behavior of the order on other vertices. Nonadjacent pairs in the global enumeration still give these same two triangle orientations. Arbitrary internal standard-tag reorderings introduce no additional triangle case. The fresh sorting split is 160 tuples with standard order (3,11,15) and 96 with order (11,3,15), both included in the rebuilt artifacts.

### Physical current and selected coefficient

The contraction identity P_a I_a=1 and equality of bare I/P within one carrier give K_ab=1. With physical transitions D_b D_a^(-1), the normalized current is Q_b-Q_a. The two logarithmic terms are both retained by `log(second)-log(first)`. Their bit difference is ±1 on the 256 remaining tuples, with the denominator attached to the actual bit-one owner. No constant-frame substitution is used.

The authenticated carrier-1 entries give I[12,1]=v1^2(v1^2+v2^2*v3)/h1 and P[1,6]=1/v1, while P[0,6]=0. For a diagonal trace-free R, R11=-R00; the terminal coefficient -2 therefore gives exactly gamma*R00 with gamma=2*v1*(v1^2+v2^2*v3)/h1. This verifies the reduced selector algebraically from the pinned factored entries. Matching physical inclusion/projection removes the outer diagonal conjugation, as in the previously reviewed naturality proof.

The new builder retains gamma's h1 denominator on the actual first owner. It does not merge the repeated carrier occurrences. The physical selector coefficient is included once; the additional factor 1/2 is the curvature-defect factor.

### Curvature domain and derivative

For each of the three actual primary owners, H^14 contributes homogeneous degree 70 per coordinate and the legal section contributes degree 1+2*bit. Thus the complete F numerator degree is exactly character_i + sum(71+2*bit_i). In the global finite frame the bit-zero legal sections equal 1, but their homogeneous degrees still count. Standard-boundary degree 5250 is absent by the separately stipulated whole-curvature domain, not by an unproved cancellation from an arbitrary edge solution.

The AST constructs the inverse product of all three actual F-owner denominators and syntactically differentiates it in coordinate 1. Its A and B roots are therefore the whole-rational-function product-rule terms. Outer weights are not differentiated. The derivative-numerator B coefficient uses the original exponent n, target kappa+e1, and n1>=1, which is the correct coefficient shift. Its multiplier support is paired with the full numerator box rather than a source-specific coefficient sample.

Actual rebuilt denominator ledgers remain within carrier 16/legal 3, with no standard-boundary denominator. The owner-aware cancellation routine checks that no legal factor is charged to a bit-zero owner. The original outer54/legal29 formulas and frame pullback are retained.

### Independent support replay

The vertex replay computes extrema on the bounded-composition polytope by choosing active bounds, independently of the builder's greedy optimizer. The domain is a box intersected with one integral sum hyperplane, so its vertices have all but at most one coordinate at a bound; the enumeration covers them. Literal zero bases impose zero exponents. Remaining power exponents are checked nonnegative. Sum/product envelopes are cancellation-blind outer bounds, sufficient for exclusion.

All 512 freshly rebuilt roots agree with their saved records and pass the independently recomputed strict inequality with w=(-1,-1,0,1). The smallest gap is 30. A signs-only change of a complete local multiplier cannot change these support bounds or exclusion. Each assignment vanishes separately; no globally consistent choice of which pairs reverse is needed for the argument beyond the block-preservation assumption.

## Resolved review corrections

All three corrections were confirmed in the revised note and builder comments. The requests and their mathematical reasons were:

1. **Local sign label.** The builder uses N-sorted owners. Its kernel is C_102(N)=signed E_O-E_N=-B_01(F_N)/2 on a reversed pair. The operator C_ON=E_N R1-R2 E_O is the negative of that kernel in N orientation. State this explicitly in sections 1 and 4, or negate the built multiplier consistently. No numerical certificate changes are needed if the local kernel is clearly named, since both signs vanish.
2. **Domain implication.** Section 3 should say that the N14 bound justifies this numerator domain for curvature inputs possessing that bound. Do not suggest that membership in the large scalar edge domain alone implies boundary-free three-owner N14 curvature membership. The theorem's opening already correctly requires both hypotheses.
3. **Pinned link.** Replace the speculative `null-order-comparison` source link and fallback-path sentence with the verified pinned release path `research/hm/null-source-integration/order-comparison/source-order-curvature-comparison.md` at commit `9a4eda0d2251f0a89a677018188d5f9ea9269c5e`.

## Artifact identity and remaining limits

Reviewed final note/executable/certificate SHA256 values:

- `carrier-block-order-invariance.md`: `e9e9aa650b83ac873e076324faf68c391848d61d7aba2cf88841c9e5d0de92e6`

- `probe_direct_curvature.py`: `da608ead6fc96f134ed5021aee9bd63930f812a416c65c98ef551c6806abdc34`
- `test_direct_curvature.py`: `670ccf74acb6b4cab8fa0a0d952d772b7938af97ed9707a76592fe55ba67f22f`
- `direct-curvature-support.json`: `270d17ef219c1bc6fa0072a75dec930f13e0717ed9ad9369ef66029d1987a78a`

The revised builder additionally refuses changed pinned Git blobs before importing the public dependency code. All declared public dependency hashes passed, and the source/contraction provenance checks passed. The replay relies on the existing authenticated outer quotient identities and prior fresh support theorem; it does not re-prove them by physical arithmetic. The review inspected the imported lowering and support code, not only the saved certificate claims.

No actual historical order, actual historical t, real-source equality, historical domain witness, scalar-41 identification, other seed/component zero, full-source primitive, full detector homotopy, arithmetic admission, or global obstruction value follows from this review.
