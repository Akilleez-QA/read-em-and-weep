# Independent review: three degree-twenty-eight residual templates

## Verdict and exact version

**PASS.** The proof establishes exactly three equivariant constant-gauge classes under its stated saturated, full-span residual hypotheses. Each displayed class has a universal actual subbundle construction with the asserted saturated derivative image, and the equivariant constant endomorphism algebras are correct. No substantive mathematical defect was found.

Audited on 2026-10-23:

- `PROOF.md` SHA-256: `dddfb627c7ff27a68cf887f4e98ee8ba1195181168f9ff5a63f01d8cc5d2d8c9`.
- `verify.py` SHA-256: `16af76ef19ffcc3407925b55f6cb213166de8853c6802fd292614ee7b69ec5da`.

The complete proof was read, including the final contextual paragraph citing PR856. The verifier was inspected before being run; it passed. The proof and verifier were not edited during this review.

The conclusion is a classification of residual inclusions, not realization of any of the three rows by the actual HM tensors and not a full-label exclusion. “Degree-twenty-eight” refers to the complementary positive quotient block; the residual itself has degree -26, as the proof and verifier correctly use.

## 1. Exact imported hypotheses

The following immutable repository files were fetched through the read-only GitHub connector and compared byte-for-byte with the local copies inspected in this review:

1. PR817, commit `a0b7cbd7a53c1603f284cf0e1a29fff106d02cb3`, `research/hm/profile11-o26-basepoint-free-top/PROOF.md`. SHA-256: `90cccbb65eb90f7ca366ee23ecc699b2370ff939914f6b266d989d644d6d1659`.
2. Commit `db51525015bb7c5e825833d550d08dedf6f6ea96`, `research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`. SHA-256: `a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256`.
3. PR856, commit `cee45480686c39a321feaa77d4b669682cc71efe`, `research/hm/profile11-degree28-constant-separation/PROOF.md`. SHA-256: `b971cac17174bb609f096e3bb4a89a14d8f518bd01b1f0a99a9010b59ccfd1c3`.

PR817 Section 5 identifies C O/F with the saturated positive O(28) inside E^+/E. It supplies E intersect C O=F and saturation of E+C O, not merely an abstract quotient of the correct character. Section 7 uses the original zero determinant defect to identify the projected actual forward quotient with A_neg(2), and its derivative map is onto. For the remaining E10 branch, this gives precisely the saturated R=O(-8)+W O(-9), the quotient R^+/R=2 O(-6), and the onto actual map R -> 2 O(-8) required here.

The original input states that E spans H. Consequently its constant projection spans H/C. Its two actual bundle presentations also give the ambient character directly: chi(E)=-M4, chi(Q)=M3 W-M2, hence H=M3 W-M2-M4=2A+2V+2P+2D. Removing C=A+V+P+D therefore yields the stated multiplicity-free Hbar.

The final PR856 paragraph accurately states the published constant-separation conclusion. This strengthens the interpretation of the residual as an actual complementary inclusion, but none of the classification, existence, or endomorphism arguments depends on reproving that separation. PR813 and PR822 are contextual inputs identifying the surviving source branch; their older exclusions are not needed for the conditional residual theorem audited here.

## 2. Intrinsic tail and completeness

The top X=O(-8) is canonical by the slope filtration. After an equivariant abstract splitting R=X+T with T=W O(-9), the actual derivative has the form (a,b e), where e is the unique Euler quotient T -> O(-8). Surjectivity forces the two constant columns a and b to be independent. Thus the actual backward kernel is the Euler kernel L=O(-10), and R/L=2 O(-8).

The internal derivative of L takes values in 2 O(-10). It cannot be zero: a horizontal saturated line in a constant bundle is constant and cannot have negative degree. A nonzero map here is a nonzero constant column, so its image is saturated. Saturation of R in the ambient constant bundle promotes this to saturation in the full derivative target. Consequently the actual L^+ has rank two and degree -18.

The universal first-polar map W O(-9) -> Hbar O generates the raw value-and-first-derivative sheaf of L. The preceding saturation identifies that image with L^+, and equal rank and degree make the map an isomorphism. Projection to T is a scalar endomorphism of W O(-9), and it is nonzero because a rank-two subbundle cannot lie in X. Hence R=X direct-sum Y with the actual canonical Y=L^+.

This resolves the possible Euler graph correctly. The argument does not assume an arbitrary source complement is horizontal, nor discard its possible P component by an invalid Hom-space vanishing. Instead Y has no P component because the coefficients of its actual generating line L lie in Sym10 W=A+V+D.

The coefficient maps of L and X factor respectively through A+V+D and P+D, with each constituent occurring once. Full span forces nonzero A and V coefficients for L and a nonzero P coefficient for X. The only remaining choices are whether the two D coefficients vanish; at least one must be nonzero. This gives precisely the three stated support pairs, with dimensions (11,4), (11,9), and (6,9). No other residual support type is omitted.

## 3. Constant-gauge normalization

Every equivariant constant automorphism of Hbar is an independent nonzero scalar on A,V,P,D. Uniqueness of each constituent coefficient map leaves only these scalars and the irrelevant scalar choices of parametrizing either line.

If L has no D coefficient, its A,V scalars and X's P,D scalars normalize independently. If L has a nonzero D coefficient, its three coefficients normalize to the complete degree-ten line. A simultaneous scalar on A,V,D preserves that line as a subbundle; together with the independent P scalar and the irrelevant scalar parametrization of X, it normalizes every nonzero relative D coefficient of X to one common value. Zero remains a separate case. Thus there is no continuous modulus in any of the three support cases.

All these operations are constant ambient gauges. The canonical Y follows functorially from L; no extra nonconstant source operation is used to identify different inclusions. The intrinsic support dimensions distinguish the three resulting orbits.

## 4. Universal jet saturation

For an h-dimensional independent subsystem of H0(O(d)), the nonzero characteristic-zero Wronskian has degree h(d-h+1). Failure to generate jets through order j implies a_j >= j+1. Strict increase of the vanishing sequence then gives a_i >= i+1 for every i >= j, so the Wronskian weight is at least h-j.

Both systems used here are basepoint-free: their common base divisors would be invariant of degree at most 8 or 10, smaller than the minimum nonempty orbit size 12. Their jet-failure loci are invariant. For the P-valued degree-eight system, failure of first-jet generation would contribute at least 3 at each point of an orbit of size at least 12, exceeding the total Wronskian degree 20. For the (A+V)-valued degree-ten system, failure of second-jet generation would similarly contribute at least 48, exceeding total degree 30.

Under the invariant apolar identification, these jet-generation statements are exactly fiberwise injectivity of the projected U_1^8 and U_2^10 maps. The lower projected osculating bundles are consequently also fiberwise injective and saturated. Constant projection commutes with differentiation, so their actual raw next transforms agree with the stated projected osculations; no unexamined ramification divisor is introduced.

## 5. Saturation and actual Gauss quotient in all three constructions

Types I and III use disjoint constant ambient summands. Their line, first-polar, and second-polar maps are saturated by the complete osculating formulas and the preceding projected-jet arguments, so their direct sums are saturated.

Type II requires a separate argument because its constant spans share D. The proof supplies the necessary stronger condition: projection of X^+=U_1^8 to P is injective on every fiber, whereas Y^+=U_2^10 has zero P component. A vector in the intersection must therefore have zero X^+ component and then zero Y^+ component. The direct-sum map U_1^8+U_2^10 is everywhere injective and has locally free cokernel. Its subbundle X+Y is also saturated because it has locally free quotient within that saturated direct sum. This proves actual transversality, not only generic disjointness or a character identity.

For complete osculating bundles, U_1^8/U_0^8=O(-6) and U_2^10/U_1^10=O(-6), with onto standard derivatives. The proved fiberwise projected embeddings transport the same exact quotients in Types I and III. Thus in every row the raw first derivatives generate the already saturated X^++Y^+, and R^+/R=2 O(-6). After twisting by O(-2), the actual derivative is onto 2 O(-8).

The X derivative is an isomorphism onto its O(-8) quotient, and the Y derivative has kernel the degree-ten generating line. Hence the actual backward kernel is exactly L and its actual first transform is Y, as needed to recover the classification invariants. The union of the coefficient supports spans all of Hbar in each construction.

## 6. Endomorphism algebras and scope

An equivariant constant endomorphism preserving R is diagonal on A,V,P,D. It preserves X by the slope filtration, L by commutation with the actual derivative, and Y by commutation with first-polar generation. This is valid for noninvertible endomorphisms as well as automorphisms.

Its restriction to either invariant line is a constant scalar. Therefore it must take a common scalar on every nonzero constituent in that line's constant span. Conversely those equalities preserve both X and Y. The conditions are exactly:

- Type I: t_A=t_V=t_D, with t_P free, giving C times C.
- Type II: t_A=t_V=t_D=t_P, giving C.
- Type III: t_A=t_V and t_P=t_D, giving C times C.

The assertion concerns equivariant constant endomorphisms of the residual inclusion only. It does not infer an endomorphism of any larger fixed module, a lift of a projector, or realization by an actual HM instance.

## Verification boundary

The standalone verifier checks only fixed nine-rule representation-ring arithmetic, the stated coefficient supports and dimensions, Euler channels, osculating degrees, and Wronskian integer inequalities. It passed with the recorded exact hash. The geometric completeness, saturation, and quotient arguments were independently checked in prose rather than treated as consequences of that program.

No selected actual HM/source coefficients, parameters, points, evaluated derivatives, matrices, selected-instance ranks, model experiments, scans, large computations, or source-app writes were used. Only this review artifact was created.
