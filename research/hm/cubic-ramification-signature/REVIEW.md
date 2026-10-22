# Independent review

Verdict: PASS. No mathematical correction is required. The result identifies the exceptional kernel of the actual upper connection without asserting nonvanishing of the full corrected operator.

## Source verification

Both named files were fetched read-only at commit `d7a6ad65f2142d39fbacc01784b7620fc3a9e42c` of `Akilleez-QA/read-em-and-weep` and checked against the proof. The cubic-support file supplies smooth integral genus four, the faithful projective actions, and the nowhere-zero quintic. The upper-connection file supplies the actual formula, the finite pushforward multiplication map, and the quadratic restriction isomorphism. No actual coefficients, points, matrices, or ranks were evaluated.

## Independent checks

1. Each trigonal ramification divisor has degree 12. Every orbit on the curve has at least 12 points because its projection is an orbit for a faithful projective A5 action. Invariance consequently forces one reduced 12-point ramification orbit for each projection, with index two. Smooth embedding in the product excludes a common ramification point.
2. The two stabilizer-five orbits contribute 96 to the quotient Riemann–Hurwitz sum. Genus at least one would force the right side to exceed 6; genus zero leaves contribution 30. Stabilizer orders 2, 3, 5 give orbit contributions 30, 40, 48, so the remaining orbit has stabilizer two. The signature (2,5,5) follows.
3. Both ramification orbits map bijectively onto the relevant exceptional 12-point orbit. Their weighted degrees exhaust each pullback of degree 36, giving precisely 2R_1+R_2 and R_1+2R_2. Their scheme-theoretic common zero divisor is the reduced divisor R_1+R_2, not empty.
4. The derivative along the second factor vanishes on R_1. Over an exceptional second-projection fiber 2r+s, it is a unit at r in R_2 and has a simple zero at s in R_1. Completion gives C[[u]] × C[[t]], with t=u² on the first factor. After trivializing the relevant invertible sheaves, multiplication is invertible on that rank-two summand and t times a unit on the other. Thus its Smith factors are (1,1,t); its specialized kernel is the s summand, not the doubled point's nilpotent direction.
5. On every length-three fiber F, restriction H0(P1,O(2)) → H0(F,O_F(2)) is an isomorphism: its kernel sequence has O(-1), whose H0 and H1 vanish. This identifies the entire vector n_h(ell) with h·kappa on F. At the exceptional fiber its vanishing is exactly h|_(2r)=0. Since p1 is unramified at r, this is a double zero at p1(r), imposing two independent conditions on five-dimensional quartics and leaving dimension three. Off the exceptional orbit, cubic divisibility leaves dimension two.
6. The descended cubic's ramification-index formula follows by comparing local indices in the quotient square. It gives profiles (2,1), (3), (2,1), whose total ramification is four. No assertion that the original trigonal covers are cyclic is made.

## Optional clarity improvement

In Section 4, specify that the restriction isomorphism used to identify n_h(ell) is the quadratic restriction H0(O(2)) → H0(O_F(2)), not the earlier quartic restriction map. The quartic restriction is surjective with a two-dimensional kernel, whereas the quadratic restriction is an isomorphism. The current proof's citation is correct, but making this explicit avoids a possible misreading.

## Scope

The conclusion concerns the actual upper-entry vector only. Its scalar factor a² and exceptional double-root criterion do not determine the diagonal/scalar cancellation or the normal cochain. The proof correctly leaves the higher obstruction unresolved.

## Added Section 6: independently checked

PASS. The correspondence ell → r → p1(r) is a bijection between the two exceptional orbits because each projection restricts to a bijection on R_2. A nonzero degree-four section has at most two distinct zeros of multiplicity at least two. The criterion from Section 4 therefore gives at most two exceptional zeros of n_h. A nonzero quadratic a vanishes at at most two additional exceptional points. With k and rho nonzero, the union bound leaves at least 12−2−2=8 exceptional points where A12 is nonzero. All necessary nonzero assumptions appear in Section 6. This is uniform nonvanishing of an entry at some fibers, not a nonvanishing assertion for the normal obstruction or a proof that contributions cannot cancel in the normal class.

## Final reviewed artifact

PROOF.md SHA-256: c26cd1b2b96ac2cea48025cb61be832a916ea7e8f4b54f279a7945ef8ef2a498. The quadratic-versus-quartic restriction clarification is present in this version. Mathematical review, not formal proof-assistant certification.
