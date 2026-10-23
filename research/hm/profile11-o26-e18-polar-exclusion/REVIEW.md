# Independent exact-version review: E18 at the zero-defect O(26) label

## Verdict

**PASS.** The argument in the reviewed version proves that source E18 cannot occur for the zero-original-defect label `G3.11.8ae96830fd21`. Its support classification, actual derivative-image analysis, saturation arguments, first-polar characters, and six remaining geometric contradictions are sound under the stated immutable geometric inputs.

This is a source-branch exclusion. It does not exclude E10, the full label, source2, or the global rank problem. Combining it with the cited divisor reduction and E0 result leaves precisely E10 for this label, with the basepoint-free degree-28 top system and genuine constant fifteen-space supplied by PR817.

This review binds exactly these SHA256 values:

- `PROOF.md`: `cf1d14aebb5bf4e2e154d8fd3d7db478f708223fadc41a709fcaa367a053fb5a`
- `verify.py`: `6f38e9005473ea5bda51143f8fa44179376aced6a44f42672d600b8de20fe333`

The proof and verifier were not modified during this review.

## 1. Immutable input and scope checks

The exact public versions of PR796, PR799, PR813, and PR817 were checked against the local texts read for this audit. Their Git blob identities agree:

- PR796, commit `d2b43060c83328dd5118aee6b9288fcfa0c873ac`: `46a0de762000f21182f6d3168f3ecfd63adaf75f`.
- PR799, commit `2172e4a7abbbe232f9f448bea6fa01dee7927460`: `a62a56f6b8f97e02b3eab6fe3a47ec3bedb6c6b1`.
- PR813, commit `3f99ecf539a3a3da61743df0dff409e54270c865`: `c5237be81f13d72776ba117548038f4c2c11b6b4`.
- PR817, commit `a0b7cbd7a53c1603f284cf0e1a29fff106d02cb3`: `891b037953e54cac798819afb23d8e64c6e2bb95`.

All five named original input files were likewise matched by Git blob identity to commit `db51525015bb7c5e825833d550d08dedf6f6ea96`. The original JSON row at source index 126 has exactly the stated quotient pair, defect zero, and three source tuples. The actual-bundle input explicitly gives center-even bundles, equivariant splitting, rank 17, degree -54, and the required strict-top hypotheses.

Only the portions of the predecessor results identified in the proof are imported. In particular, PR796's profile-(1,2) interior vanishing is not transferred to this endpoint problem. PR813 excludes the degree-12 common divisor; the degree-20 alternative cannot contain the E18 top coefficient 2D. PR817 is needed only for the cumulative E0/E10 statement, not for the new E18 contradiction.

## 2. Kernel, raw first span, and saturation

The strict-top vanishing makes the 2D coefficient map into Sym28 W injective. After the divisor reduction, the map F -> O(26) is onto everywhere. The resulting K0 has rank 9 and degree -46. Twisting the kernel sequence gives

    H1(K0(2)) = Sym28 W - 2D = A+V+2P+D,
    chi_G(K0(3)) = 2D tensor W - Sym29 W = -W-Wp-T.

The lack of sections at twist two makes every splitting degree at most -3.

The two raw-image sequences in Section 2 are correct without first assuming saturation of J or B. The full derivative image I maps onto the external O(26), and its kernel is exactly the image of the actual internal derivative of K0. Taking the preimage of I(2) in the constant ambient bundle gives B, with kernel F. All these image sheaves are locally free on the smooth curve, even before their ambient inclusions are known to be saturated.

Euler's identity identifies the raw value-and-first-derivative sheaf with the image of the quadratic first-polar map. Thus B(1) is globally generated, while B injects into a trivial bundle. Its splitting degrees are consequently 0 or -1. If t is the saturation length, its support and multiplicities are invariant; a nonzero such length is at least 12. Since deg(F^+) <= 0,

    0 <= t <= -deg B.

This establishes the claimed saturation whenever -12 < deg B <= 0. Once B is saturated, its canonical degree-zero evaluation is an actual constant subspace, and its pure linear quotient is an actual saturated subbundle of the corresponding constant ambient quotient. The subsequent connection arguments therefore concern genuine constant projections.

## 3. Independent completeness check of the small support argument

For a summand U O(-j), j >= 4, its first cohomology contribution is U tensor Sym^(j-4) W. It is a genuine subcharacter of A+V+2P+D, with dimension (j-3) dim U <= 19. Together with central parity, this gives exactly the 31 bounded atoms tested by the verifier. The 24 surviving atoms are exactly those in Section 3; the seven rejected atoms either introduce the trivial constituent or exceed the D multiplicity.

Completeness of the 17 splittings is not inferred from checking 17 examples. The second Euler character forces a W in the next-twist tail. Precisely O(-6), W O(-7), A O(-8), and O(-18) can supply it within the first budget, and each consumes its unique A. Hence exactly one of those four occurs.

- W O(-7) leaves V+2P. Supplying the missing T and Wp forces O(-10) and Wp O(-5), with degree-three coefficient S.
- A O(-8) leaves P. Supplying Wp forces Wp O(-5), again with degree-three coefficient S.
- O(-18) leaves P. The two completions are P O(-4) or Wp O(-5), with degree-three coefficient S or S+Wp.
- O(-6) leaves V+2P+D. There is exactly one D-consuming atom. The nine possibilities listed in the proof give respectively 1,1,1,2,2,1,1,1,3 completions, because the entire D-free atom list is V O(-4), P O(-4), Wp O(-5), and O(-10).

This independently gives 1+1+2+13 = 17, exactly the displayed list. The degree-three coefficient is determined by the second character equation and must be genuine. No support with a missing or extra degree-three block is omitted. The numerical rank and degree also follow from the two character equations and agree with all displayed candidates.

## 4. Actual internal images and their saturation

The 60 atomic Hom checks give precisely the ten nonzero per-target channels stated in Section 4. Reviewing their possible simultaneous occurrence in each of the 17 supports produces exactly the eleven J types in the table, not additional abstract extension types.

The scalar and constant-column channels are saturated. The P O(-6) -> Wp O(-5) channel is the Wp-tensor Euler quotient and is everywhere onto. A nonzero O(-12) channel has coefficient degree 7 or 6, too small for a nonempty invariant zero divisor. For O(-18) -> Wp O(-5), the only possible nonempty invariant zero divisor of degree at most 13 would have degree 12; dividing by it would require Wp in Sym1 W, which is impossible. Diagonal line images remain saturated when any such component is nonzero.

When a full Wp O(-5) image occurs together with an O(-12) channel, quotienting by that full block leaves either zero or the saturated O(-12) image in V O(-6). The resulting extension splits because H1(Wp O(7)) = 0; averaging gives an equivariant splitting. The O(-10) images occupy the separate trivial target block. These observations justify all sums used in the table.

The W O(-11) case is correctly treated separately:

- A rank-one image must be an equivariant O(-j) quotient, with j even and 6 <= j <= 10. Among these j, W occurs in Sym^(11-j) W only at j=10. Its target inclusion can then only be a constant column in 2 O(-10), hence is saturated.
- A rank-two image is isomorphic as an image sheaf to W O(-11), without assuming a fiberwise injective ambient map. Its raw first span has degree -10, forcing saturation by the orbit-length bound. Saturation of B makes I saturated; J = I intersect (E/F)(-2) is then saturated in the internal target. Thus possible initial zeros are eliminated by an actual saturation argument, not silently discarded.

## 5. First-polar characters and elementary geometry

For every row, the two character formulas follow from the actual exact sequences and the fact that B has only degrees 0 and -1. The verified C and L characters, ranks, and degrees agree with the table. Five rows have negative L multiplicities and are impossible. All six remaining rows have degree between -10 and 0, so their B is saturated before any constant projection is used.

The linear-block obstruction in Section 5 is valid in this setting: local sections of a whole linear block in the projected image lift locally to F, so their derivatives remain in the projected B. But the values and first derivatives of an embedded linear bundle span its nonzero constant coefficient space. This cannot lie in a pure degree-minus-one bundle. No abstract complement is assigned a connection.

The D-to-S contraction is everywhere onto; the D-to-T multiplication map is everywhere injective. Their Hom channels have multiplicity one. Independence of the two multiplicity rows therefore supplies a whole S O(-1) block in the projected image, while dependence with a nonzero T row gives exactly one D O(-2) kernel.

The second elementary obstruction also holds: the tautological O(-6) inside D O(-2) has quadratic coefficient span Sym6 W = V+P. Every map into the constant A+D annihilates it, because neither V nor P occurs in A+D. Thus no such map can embed D O(-2).

## 6. Check of every surviving row

1. **J = O(-10).** Here B is the constant rank-12 space A+P+D. The quotient X = B/F is globally generated of rank 2 and degree 20. Equivariant splitting and center parity leave exactly O(a)+O(20-a), for a = 0,2,4,6,8,10. An irreducible odd two-dimensional coefficient would require the equal degree 10 to be odd, so is impossible. The six invariant degree pairs in the proof exhaust all maps X -> O(28). Four pairs have no channel; the (24,12) pair is divisible by f12; the (20,16) pair has only a degree-20 entry and therefore has zeros. No map is everywhere onto.

2. **J = Wp O(-5)+O(-10).** The projection to T O(-1) cannot vanish by rank. Its exact D O(-2) kernel would embed in the constant A+D, contrary to the tautological-line obstruction.

3. **J = O(-10)+O(-12).** Dependence of the S and T rows would put a rank-5 D block into the constant rank-3 A. Independence forces the forbidden full S O(-1) block. Both alternatives are impossible.

4. **J = W O(-11).** The same argument applies after the separately established saturation step. There is no unaccounted torsion correction distinguishing this row from the preceding one.

5. **J = V O(-6).** If the S projection vanished, the saturated rank-10 F would equal the constant rank-10 A+V+P, contradicting its degree. A nonzero projection is onto S O(-1), giving the linear-block contradiction.

6. **J = Wp O(-5)+V O(-6).** Independent rows are forbidden. If the T row vanished, a nonzero S row would give the same forbidden linear block, while both zero would contradict rank. Thus the rows are dependent with nonzero T row, and F intersect (A+V) O is exactly D O(-2). Saturation of F makes its quotient in the constant rank-6 space the line O(10). This line injects into B/F. Its composite to O(28) vanishes because there is no invariant of degree 18. It must therefore inject into J(2) = Wp O(-3)+V O(-4), which admits no nonzero map from O(10). This is a valid contradiction without assuming any additional splitting of B/F.

Every surviving row is excluded. There is no remaining actual internal-image type.

## 7. Reproduction and verification boundary

The included bounded verifier was run successfully and reported:

    PASS: 31 bounded atom identities; 24 admissible and 7 rejected; all 17 declared supports satisfy the exact input identities.
    Completeness is the four-case budget proof in PROOF.md Section 3, not an enumeration claim.
    PASS: all 60 atomic Hom channels and all 17 total Hom dimensions; 10 atomic channels are nonzero, each one-dimensional per target copy.
    PASS: all eleven first-polar characters, ranks and degrees; low invariant degrees and the two D channels.

The support completeness and all saturation and geometric arguments were reviewed independently of that output. No old all-twist envelope, selected actual source evaluation, selected coefficient or point, model calculation, or source-instance rank computation was run. The only mathematical program executed was the included bounded universal verifier. Immutable source reads and file-identity checks were used to verify provenance.

No mathematical defect or blocking dependency was found in the exact reviewed version.
