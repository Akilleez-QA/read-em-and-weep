# Independent review of the source113 cf reduction

## Verdict and hash binding

**PASS for the stated conditional reduction, with no gap found in Sections 1–7.**

This review binds exactly to:

- `PROOF.md`, SHA256 `8157ffa4a39882a8bc4a0b2f1c5200d01e1fc8d9d336904fce63464e672d2204`;
- `verify.py`, SHA256 `3f3e1d0807ba25f19df75407604c1f8f028bb05681bef5becc0f69bd513c394a`.

The proof excludes the basepoint-free high-line branch for the one cf tuple at original source index113, forces the degree-twelve divisor branch, constructs its actual constant nine-space, and proves both stated exact intersections. It does **not** exclude the remaining divisor branch, the whole source, or the label, and gives no frontier decrement. No saturation claim for the projected residual follows from this review.

`NEXT-DEFECT-BOUND.md`, any former Section 8, and stronger defect claims are outside the reviewed artifact and verdict.

## Input audit

I read the actual-bundle and strict-top inputs, the original source and label catalogs, and PR796/PR802 in the supplied pinned-input directory. The catalog record at index113 has `A=[[-10,"one"],[2,"one"],[16,"one"]]`, defect zero, and exactly ten compatible tuples, including `(0,0,1,0,0,1,0,1)`. The label record identifies precisely `G3.11.ad509d55173f` with source index113 and original defect zero. Applying the original splitting formula to the tuple gives the displayed E, of rank17 and degree−54.

Hashes of the independently read inputs:

- Actual equivariant splitting: `a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256`.
- Strict-top lemma: `53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08`.
- PR796: `622763aac375db7e17bc7cab472f1afda0477b0f769371a3b3ef845cd5c9e3b1`.
- PR802: `a18a6990f719592d71853692157161a9ca5fe6b7f2a78edacbfa060bb3513459`.
- Original one-one catalog: `6002ad138a41d98c351130a29703722979f31b8da90d7c75a120f28bf89480eb`.
- Stable-label catalog: `a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad`.

The review relies on the pinned actual inclusion and original zero-defect identification; it does not independently reconstruct the underlying HM geometry.

## Independent mathematical checks

### 1. The low row and complete basepoint-free support

If the D-to-O(2) row were zero, the entire rank12 top block would map only to O(16). Strict-top injectivity and the minimum invariant divisor degree make this onto. The two PR802 kernels have no internal derivative channel into the remaining E-tail, including the equal-degree trivial-to-V exception. The actual raw image is saturated by zero defect. The quadratic gap therefore applies with `(r,b)=(12,18)`, and both allowed alternatives fail.

For F of rank7, independence bounds the common divisor by degree12. Thus only degree0 and the reduced degree12 orbit are possible.

I independently checked the support exhaustion in Section 3 using the nonnegative H1 budget A+P+D and `(j−3)dim U≤12`, rather than merely checking the proposed kernels. The parity-compatible degrees are bounded by j≤15. The only surviving blocks are the eleven listed atoms. In the second Euler character, a W constituent must be supplied by O(−6) or W O(−7). The latter consumes A+D, leaving just the two P choices. The former consumes A, so S can only be supplied by O(−8), again leaving the two P choices. This proves the four-kernel list is exhaustive, with the degree−3 coefficients forced by the Euler character.

Every internal Hom was checked. The only nonzero channels are W O(−7)→D O(−4) and O(−8)→D O(−4). Their universal multiplication descriptions make them injective on every fiber, not merely generically injective. Thus J is saturated in every case. Combining that with the saturated external O(16) proves actual saturation of I and of the raw first span. The first-polar splitting restriction is therefore legitimate. The character computations exclude J=O(−8), while J=0 has positive degree. The remaining actual first span is P O+T O(−1).

### 2. The projected linear bundle and its constant span

The actual constant P is obtained from global sections of M, so projecting by it preserves the constant connection. If the projected P channel vanished, its injection into the constant P would have a nonzero invariant degree8 determinant, impossible. If both channels were nonzero, their multiplicity-one property identifies the map with the complete Euler contraction after rescaling the two source factors. Surjectivity would make the negative projected bundle horizontal. Thus only the P channel survives.

I independently derived formula (9): for an embedded L=R O(−1) with coefficient map `R⊗W→C1` and kernel K1, quotienting the constant sequence by L gives

    0 → K1 O → R O(1) → C1 O/L → 0.

Fiberwise injectivity of L is exactly what makes the first arrow injective on every fiber. Twisting by −2 identifies the second arrow with the actual derivative and gives `L⁻=K1 O(−2)`. This establishes the formula without assigning a connection to a chosen splitting complement.

The nonzero projected P channel therefore injects P into K1. Since the coefficient span of a negative saturated rank6 bundle has dimension at least7, `dim K1≤5`. Multiplicity-freeness of T⊗W=V+P+D forces K1=P and C1=V+D. Tensoring the complete cubic Euler sequence with Wp gives all the quotient identities and the derivative isomorphism in (10). Adding back the actual constant P gives the claimed Ctot, dimension12, and rank8 derivative kernel of M.

### 3. The decisive rank-two argument

The exact image sequence gives `(E∩M)/F=J(2)=W O(−5)`. Its map to `M/M⁻=Wp O(1)` cannot be zero because E∩M has rank9 while M⁻ has rank8.

The proof's exclusion of generic rank1 is complete. A saturated invariant image line has the unique linearization O(d), since G has no characters. Nonzero maps require −5≤d≤1 and W in Sym^(d+5)W. In that full range only d=−4 is possible. The necessary second map O(−4)→Wp O(1) is zero. Hence the channel has generic rank2.

Differentiation of E∩M stays in E⁺, while the rank-two image fills Ctot/M generically. Since M⊂E⁺ and E⁺ is saturated in the original constant ambient bundle, this implies the actual sheaf containment Ctot O⊂E⁺. The two low quotient components vanish after factoring through Wp O(3), by degree and the Wp-versus-W mismatch. The kernel of the resulting nonzero high-line map has rank11 and degree at least−18. Its injection into E forces every splitting degree to be at most−2, hence total degree at most−22. This is the required contradiction. No assertion about a new abstract connection is used.

### 4. The divisor branch and exact intersections

In the degree12 branch, the residual complete degree6 evaluation has kernel T O(−3). Its internal derivative vanishes by degree. Therefore the raw first span has rank8, degree−8, and quotient O(6) by F. If its saturation has defect δ, its degree is −8+δ≤0, so δ≤8. An equivariant nonzero torsion defect has invariant support and length at least12. Thus δ=0. This is the essential saturation proof; raw local freeness alone would not suffice.

First-polar generation now forces M=Sym7 W O(−1). Its derivative kills F and is nonzero, so has rank1. A linear bundle reaches its coefficient span after one derivative, yielding an actual constant rank9 space. The quotient line has degree8, and the cohomology of M identifies the quotient map with complete evaluation. Consequently C=Sym8 W, M⁻=F, and the ordinary complete first-jet/Euler sequence yields `C O/F=W O(7)`.

If C O were contained in E⁺, its quotient by F would map nontrivially to O(18) alone. Nontriviality follows because C cannot lie in the negative bundle E. The two degree11 sections are independent by irreducibility and have no common invariant divisor, hence the map is onto. Its kernel is O(−4), whose map into E/F vanishes in every component. This contradicts the induced injection.

Thus C O∩E⁺ has rank8 and equals M by saturation of M. Then N=E∩C O lies in M, and differentiation of its sections lies in both C O and E⁺, hence in M. Therefore N⊂M⁻=F; the reverse inclusion is already established. Both exact intersection statements are justified without assuming saturation of the projection E/F into (H/C) O.

## Executable check and limits

I inspected and ran the fixed universal-character verifier. It passed. Its exact character calculations corroborate the support atoms, displayed kernels, internal Hom support, polar characters, small rank-one obstruction, and original catalog membership. Kernel exhaustion and the geometric derivative/saturation steps were additionally checked in prose above; executing the verifier alone would not establish them.

No actual selected source coefficients, parameters, points, derivatives, instance matrices, instance ranks, models, scans, or large computations were used. This is an independent written mathematical review, not proof-assistant certification. No publication was performed.
