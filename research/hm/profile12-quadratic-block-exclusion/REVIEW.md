# Independent review: saturated quadratic-block exclusion

## Decision and exact version

**PASS.** The proof establishes the complete exclusion of the profile-(1,2) label `G3.12.34bc2083d563`, and the stated additional source reductions for the two other named profile-(1,2) labels. The separate quadratic Gauss-gap lemma is also correct. No mathematical gap was found in the saturation argument, the use of the original connection, or the short equivariant syzygy classifications.

Reviewed file: `PROOF.md`.

Reviewed SHA256:

    622763aac375db7e17bc7cab472f1afda0477b0f769371a3b3ef845cd5c9e3b1

Review date: 2026-10-22 UTC.

The original version was also checked. One source-provenance imprecision was reported before this review was written: the pinned second-span theorem establishes two exclusions but does not itself state the cumulative 23-label count. The reviewed version now separates that immutable theorem from the cumulative accounting reported in the linked PR757 review. This correction does not change any mathematics.

The exact scope of the count is important: **relative to the reported cumulative baseline of 23 labels with counts 19/3/1, this new theorem removes one profile-(1,2) label, giving 22 and 19/2/1.** This review verifies that conditional accounting. It does not claim to reconstruct every older exclusion in the cumulative frontier from scratch, and the new exclusion does not depend on that numerical baseline.

## 1. Public inputs were checked at the stated commit

The mathematical sources were independently fetched from the public repository at commit

    db51525015bb7c5e825833d550d08dedf6f6ea96

under

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The following checks were made against the fetched contents, not merely against the new proof's description of them.

1. `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md` supplies the actual saturated inclusion in the constant ambient bundle, the vanishing H0(E(1))=0, the 28-type equivariant classification, and the interior-stage kernel/forward-transform convention.
2. `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md` supplies H0(E^-(2))=0 for this actual E. Its argument applies to the original constant connection and does not require a horizontal splitting.
3. `ONE-TWO-FINITE-QUOTIENT-PAIRS-AND-ZERO-DEFECT.md` identifies the original quotient A_q with B_q^*(-2) in profile (1,2), with zero original determinant defect. Its associated JSON gives these complete necessary source lists:

       pair 0:  {0,3,6}
       pair 6:  {0,10,18}
       pair 12: {0,3,6,10,12,13}

4. `rank-three-quotient-frontier-144.json` identifies those three source indices, respectively, with `G3.12.37914c53373c`, `G3.12.34bc2083d563`, and `G3.12.eed6acb13f3e`. Their displayed A and B splittings agree with the new proof. In particular pair 6 really has A_q=2O(-8)+O(14) and B_q=O(-16)+2O(6).
5. `PRIMAL-SECOND-SPAN-ANNIHILATOR-RANK-OBSTRUCTION.md` and its JSON exclude `G3.11.942927348917` and `G3.12.8e9af2d08af9`, as now stated in input 5. The separately linked [PR757 review](https://github.com/Akilleez-QA/read-em-and-weep/pull/757#pullrequestreview-5617908618) was retrieved and checked: it is attached to the same commit and reports the cumulative transition 25 to 23, with profile counts 20/4/1 to 19/3/1.

All seven displayed E splittings were independently reconstructed from the JSON's eight-parameter tuples using the formula in the splitting theorem. They agree exactly, and each has rank 17 and degree -54. In particular, entry 18 has top block 2D O(-2) and lower blocks Wp O(-3)+V O(-4)+2O(-8); entries 6 and 13 have top block (P+D)O(-2).

The source lists are necessary overlists. Exhausting an overlist is sufficient for an exclusion; no realizability claim about its members is needed.

## 2. The two crucial geometric inputs are valid

### Absence of sections in the interior stage

For maximal profile (1,2), E^+ is an interior plateau stage and its negative transform is E. A global section of E^+ maps, under its inclusion in H O, to a constant vector. Its derivative is zero, so it lies in the actual Gauss kernel E. Since H0(E(1))=0 implies H0(E)=0, this proves H0(E^+)=0.

This is stronger than a formal rank-degree condition. It applies to every subsheaf of E^+ and, in particular, to every saturated forward transform F^+ constructed in the proof.

### Saturation of the original positive line

The bundle B_q is an actual locally free quotient of Q*. Dualizing gives a saturated inclusion B_q* into Q. After twisting, and using the zero-defect identification A_q=B_q^*(-2), the actual derivative image A_q is saturated in Q(-2). The O(14) top line is a direct bundle summand of A_q, so its inclusion in Q(-2) is saturated as well.

Thus saturation of the positive line is not deduced from generic rank alone. It uses precisely the original zero-defect theorem. No assumption about a distinct second-dual defect enters here.

## 3. The degree-sixteen system is genuinely basepoint-free

Let F=R O(-2) be the canonical highest-slope block. Its map to each negative summand of A_q vanishes by degree. The restriction therefore factors through O(14).

Twisting the actual quotient sequence by two and using H0(E^-(2))=0 proves that R=H0(E(2)) injects into H0(O(16)). This establishes linear independence of the system, rather than presuming it from the fiber rank of F.

Its common zero divisor, if nonzero, is invariant under the projective A5 action. Every projective orbit has at least 12 points, so that divisor would have degree at least 12. After removing it, all sections would belong to a space of dimension at most 5. This contradicts dim R in {14,12,10,9}. Consequently the bundle map p:F to O(14) is surjective everywhere.

The resulting sequence

    0 -> K0(2) -> R O -> O(16) -> 0

has H0(K0(2))=0. Every ordinary splitting degree of K0 is therefore at most -3. Its cohomology also gives H1(K0(2))=Sym16 W/R, as an actual quotient representation.

The orbit argument is uniform over the hypothetical branch and selects no parameter or point.

## 4. The derivative-image saturation argument is complete

Use the actual ambient constant connection throughout. Set

    M=(H O/F)(-2),
    N=(E/F)(-2),
    B=Q(-2),
    L=O(14) subset B.

Then 0 to N to M to B to 0 is an exact sequence of bundles. Let I be the image of the actual second fundamental form of F in M. Its projection to B is exactly L, since p is onto. The kernel of I to L is precisely the image J of K0 in N. This proves

    0 -> J -> I -> L -> 0.

In particular, the equality of the kernel with J does not assume a splitting of the connection: a local derivative-image section projects to zero precisely when its preimage under F to I belongs to K0.

If J is saturated in N, the quotient sequence is

    0 -> N/J -> M/I -> B/L -> 0.

Both end terms are locally free. Hence M/I is locally free and I is saturated. This verifies the decisive step with no omitted torsion divisor.

The saturated first forward transform consequently has the exact sequence

    0 -> F -> F^+ -> I(2) -> 0.

If J has rank u and degree v, its quotient has rank u+1 and degree v+14+2(u+1). Therefore the rank and degree formulas in the proof are correct.

Finally, F is an actual saturated subbundle of E, not an abstract bundle of the same splitting type. Differentiation preserves the inclusion in the forward transform, and saturation preserves it because E^+ is saturated in H O. Thus F^+ is contained in E^+. This justifies h0(F^+)=0 and chi(F^+)<=0.

The map K0 to N is O-linear because the Leibniz term belongs to F and disappears in the quotient. The proof never defines a connection on an arbitrary abstract complement or quotient.

## 5. Independent character and syzygy checks

A separate small abstract-representation check used the binary-icosahedral McKay multiplication graph and the recurrence

    Sym(n+1) W = W tensor Sym(n) W - Sym(n-1) W.

This checked the universal identities and enumerated only the small dimension/parity bounds explicitly appearing in the proof. It did not evaluate an actual HM/source map.

The checked identities include

    Sym16 W = V+P+2D,
    Sym17 W = Wp+S+2T,
    Sym6 W = V+P,
    D tensor W = S+T,
    Wp tensor W = P.

They give the claimed Euler characters S-Wp for entry 18 and T for entries 3 and 12.

### Entry 18

For an irreducible block R' O(-j) with j>=4, its contribution at twist two is R' tensor Sym(j-4) W. Since this contribution must fit inside V+P, it has dimension at most 7 and the required central parity. Exhausting those bounds yields exactly

    V O(-4), P O(-4), Wp O(-5), O(-10).

Their twist-two contributions are V, P, P, V+P, and their twist-three H1 contributions are 0, 0, Wp, T, respectively.

There are therefore exactly three ways to fill the V+P budget: the first two blocks together, the first and third together, or the last block alone. Combining each with chi_G(K0(3))=S-Wp rejects the first and third assemblies, because the resulting H0 character has a negative Wp multiplicity. The second gives H0(K0(3))=S. The remaining degree -3 block is therefore exactly S O(-3), proving

    K0 = S O(-3)+V O(-4)+Wp O(-5).

No block of degree below -10, or unlisted block within the bound, can have been omitted: its positive H1 contribution either exceeds dimension 7, violates central parity, or contains a forbidden irreducible.

### Entries 3 and 12

Here the H1 budget at twist two is D, of dimension 5. The same complete bound gives exactly D O(-4) or O(-8). Their twist-three H1 characters are respectively 0 and S. Combining with chi_G(K0(3))=T gives precisely the two displayed kernels

    T O(-3)+D O(-4),
    (S+T)O(-3)+O(-8).

The ranks and degrees agree with the kernel sequence in each case. No cancellation between positive H1 contributions is available, so the classification is exhaustive.

## 6. Each Euler-characteristic contradiction was checked

For entries 0 and 10, K0(2) has rank 13, degree -16, and strictly negative ordinary degrees. Each of its negative degrees has magnitude at most 4. Thus K0 has degrees between -6 and -3. Every target degree in (E/F)(-2) is at most -10, so J=0. The resulting forward bundle has

    rank 15, degree -12, Euler characteristic 3.

For entry 18, the only possible component of K0 to (E/F)(-2) is the constant equivariant map from Wp O(-5) to the identical block. Schur's lemma makes it zero or an isomorphism. The image is therefore either zero or the full direct summand, both saturated. The two resulting triples are

    rank 11, degree -4, Euler characteristic 7;
    rank 13, degree -10, Euler characteristic 3.

For entries 3 and 12, every component is ruled out by degree except the possible O(-8) to V O(-6) map. Its equivariant Hom is zero since Sym2 W=A and A is not V. Hence J=0 and the resulting forward bundle has

    rank 13, degree -8, Euler characteristic 5.

All four Euler characteristics are positive, contradicting their inclusions in E^+. All arithmetic agrees with the stated formulas.

The complete source list for pair 6 is exhausted by entries 0, 10, and 18. This is why the result excludes the whole label, rather than merely an individual source stratum. The other complete lists reduce to {6} and {6,13}, exactly as stated. Those residual sources are not excluded here.

## 7. The separate quadratic Gauss-gap lemma is sound

For a saturated F=O(-2)^r in a constant bundle, an affine trivialization expresses its inclusion by r vector-valued polynomials of degree at most two. Their values and first two derivatives span their constant coefficient space by an invertible triangular change of generators. Thus the second saturated forward transform is the full constant span V O. Saturation justifies extension across ramification and the omitted affine point.

If the first derivative has generic rank one and F^+/F=O(b), the second fundamental form of F^+ annihilates F by the definition of F^+. It therefore factors through this actual line quotient. Consequently the second forward increment has rank at most one and

    r+1 <= dim V <= r+2.

If dim V=r+1, saturation forces F^+=V O, giving b=2r. Otherwise V O/F^+ is the line O(2r-b), and the nonzero second fundamental form gives a nonzero map

    O(b) -> O(2r-b-2).

The degree inequality is 2b<=2r-2, or b<=r-1. This proves the claimed dichotomy. The case r=14, b=16 is indeed impossible. This proof uses the actual ambient derivative, not a connection assigned to an abstract splitting.

## 8. Final scope and restrictions

This review certifies the written structural argument, conditional on its explicitly cited established bundle and plateau inputs. It is not proof-assistant certification.

The proof establishes one new complete label exclusion and the additional necessary source-list reductions. Its frontier arithmetic is relative to the separately cited cumulative baseline. It does not exclude either remaining profile-(1,2) label, does not concern the distinct source2 label `G3.21.d610e381ed75`, and does not establish SF>=4, square rank>=28, or the original research goal.

No actual HM coefficients, source parameters, selected points, derivatives, matrices, source-instance ranks, model experiments, or large computation were used in this review. The only computation was small universal representation and integer bookkeeping, supplementing the explicit geometric proof checks above.
