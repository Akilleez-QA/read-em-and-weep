# Independent whole-proof review: the actual top-three boundary

## Verdict and exact reviewed artifact

PASS, conditional on the explicitly imported actual-geometric and source premises. I read the complete new proof, independently reconstructed its character calculations and cohomology alternatives, and checked the actual-connection argument at the point where formal splitting information is promoted to an obstruction. I found no missing quotient case, cohomology case, or required assumption in the written theorem.

Reviewed artifact: `PROOF.md`.

SHA256: `55e241f3277bb261d0cbc81f1d957a839e22dd525c0d24d821edf0d6a16014fe`.

The valid conclusion is exactly necessary boundary structure: when the actual rank-four maximal profile (1,1) quotient has maximum ordinary degree three, its source is D, its quotient is W O(3)+O(2)+O(-8), and its derivative kernel has one of the three displayed forms. This does not prove existence of any form, exclude the boundary, close the profile, or improve a global rank bound.

## Evidence and independence

I inspected the retained actual inclusion, strict-top lemma, four-source theorem, double-channel theorem, the arbitrary-rank plateau argument, the capacity construction and the preceding low-top proof. I authenticated all nine retained complete input files against their recorded byte length, SHA256 and Git blob identity. The ninth file is the preceding proof at public head 236e0a3723c3d73ea7fb9e549376540a8e70508b. The author reports a fresh direct immutable-source fetch of that file; my independent authentication is of the retained bytes against the immutable-source manifest, not a second network fetch. The older eight originals retain the same immutable identities as in the reviewed low-top packet.

`verify_independent.py` does not import the author's `characters.py`, `verify.py`, or result data. It uses exact arithmetic in Q(sqrt(5)), the nine binary-icosahedral class traces and class sizes, and the closed binomial formula for symmetric-power traces. This is algorithmically independent of the author's McKay recurrence. It checks character orthogonality, the physical P and W' marking, source Hom spaces, Euler characters, actual derivative target characters, every relevant cohomology atom, all explicitly written lower-block alternatives, and final rank/degree arithmetic.

Both ordinary and optimized Python runs pass and produce identical JSON. All acceptance checks are explicit exceptions, so optimization cannot disable them. The review is mathematical and computational, not proof-assistant certification of the transitive HM source premises.

## 1. Actual geometry and inheritance of the hypotheses

The actual ambient is the thirty-dimensional constant plane-section space. It is not the 54-dimensional coefficient presentation of E. The source proof and the rank-strata proof identify the same physical parameter line, determinant convention, central parity and actual saturated inclusion. The four-source and double-channel inputs are independent of the derivative rank and may therefore be used here; no rank-three ledger or rank-three coverage theorem is transferred.

For generic rank four and maximal plateau (1,1), K and L have ranks 13 and 9 and derivative ranks at most three. The preceding three-column capacity argument therefore supplies a+13u>=16 and a+9v<=-8-t, with t>=0 retained. In particular v<0. The new proof only uses these consequences, not zero defect or saturation of either image into the opposite quotient. Its stronger boundary hypothesis u=3 is explicit.

Strict top applies to E because it is saturated in the actual constant ambient and has top degree at most -2. Thus K has top at most -3. The actual derivative of K lands in (E/K)(-2), because beta_E kills K. Applying strict top to K gives the coefficient injection H0(K(3))->H0(A_q(1)). All saturation statements needed for this iteration follow from locally free successive quotients on the smooth curve.

## 2. Quotient reduction is exhaustive without a global search

A degree-three coefficient block is odd. Rank four and v<0 rule out the odd four-dimensional irreducible and rule out two degree-three doublets. Thus exactly one W or W' block occupies rank two at degree three. The other rank two is either one negative odd doublet or two even scalar blocks. There are no missing one-dimensional odd characters: G is perfect and its only one-dimensional representation is trivial.

For a negative doublet of degree -1, a=4 and v=-1, so a+9v=-5>-8-t. This is a valid exclusion for every nonnegative defect. Global generation of E(8), and hence A_q(8), gives the genuine lower bound -8, leaving only odd degrees -3,-5,-7.

The independent Hom calculation confirms exactly the three nonzero mechanisms written in Section 2. The W(-7) map is supported only on D's one scalar O(-8), so it cannot be onto a rank-two quotient. This rank restriction is essential: nonzero Hom alone is not enough. The remaining doublets are W'(-3) or, for P only, W'(-5).

For scalar complements the only negative scalar quotient is O(-8), forcing D. Degree zero has zero source Hom as well as degrees -2,-4,-6. Two O(-8) copies cannot be supplied by one scalar source line. The other scalar is consequently O(2). Cubic visibility then removes W' as the positive doublet in the negative-doublet cases, since it supplies only one T6. This proves that the four displayed quotients exhaust the boundary at this stage.

## 3. The near-top coefficient obstruction is valid for the actual connection

For any chosen equivariant Birkhoff splitting K=R3 O(-3)+R4 O(-4)+N, a nonzero vector in the kernel of R4->H0(A_q(2)) gives a constant-coefficient line C=O(-4) inside the displayed degree-minus-four block. It is a saturated direct summand of K, and K is saturated in the constant ambient, so C is saturated there too.

Because the actual beta_K kills C, beta_C factors through (K/C)(-2). The quotient K/C still has all degrees at most -3, so this target has all degrees at most -5. Hence Hom(O(-4),(K/C)(-2))=0. The line is horizontal in the actual constant ambient, which forces its Grassmannian map to be constant over C. Saturation makes it a constant line subbundle, contradicting degree -4.

Thus the coefficient map on R4 is injective, including combinations among repeated irreducibles. This does not say that the full derivative is fiberwise injective or that all H0(K(4)) injects. In particular degree-minus-four sections arising from the R3 block are not falsely included in this conclusion. No ordinary Birkhoff splitting has been declared horizontal.

## 4. Independent Euler and small-cohomology check

All four sources have chi(E(3))=W'+2T6 and chi(E(4))=3V+2D+3P. Subtracting each exact quotient's Euler character gives the following verified values:

- Q_a: chi(K(3))=-W', chi(K(4))=2V+D; H0(A_q(2))=D+V+P.
- Q_b: chi(K(3))=W', chi(K(4))=2V+D+P; H0(A_q(1))=S4+T6.
- Q_c: chi(K(3))=-W, chi(K(4))=D+V+P-1; H0(A_q(2))=A_std+2D+P.
- Q_d: chi(K(3))=S4-T6, chi(K(4))=A_std+D+V; H0(A_q(2))=2D+V+P.

The proof correctly uses Euler rather than H0 where a negative scalar contributes H1. For example, Q_d's O(-8) contributes S4 to H1(A_q(3)); omitting it would destroy the forced S4 cubic kernel.

For every lower block R O(-j), j>=5, H1 at twist three is R tensor Sym^(j-5)W of dimension (j-4)dim R. After the cubic-kernel and strict-top reductions, the required total is W', W, S4+W', S4+W or T6, always of dimension at most six. Thus j<=10 is proved, not an empirical cutoff. The independent calculation checks all nine physical irreducibles at every parity-compatible j=5,...,10 and confirms precisely the union of eleven atoms in the proof. This only classifies irreducible cohomology atoms under a proved six-dimensional constraint, not global bundles or quotient candidates.

## 5. Every exclusion and surviving kernel is checked

Q_b forces the P-source W' cubic kernel and no H1(K(3)); its absence from H0(A_q(1)) excludes it.

For Q_a the same strict-top injection excludes the nonzero P cubic kernel. If the cubic kernel is zero, H1(K(3))=W' forces lower part W'(-5) and R4=2V+D. If it is S4, the two possible lower parts are S4(-5)+W'(-5) and O(-8)+W'(-5), yielding respectively R4=2V-A_std and 2V. The first is nongenuine; the other two violate near-top injectivity because the target contains only one V.

For Q_c, cubic kernel zero gives lower W(-5) or O(-6); the former yields a negative trivial coefficient in R4 and the latter R4=D+V+P. With cubic kernel S4, the proof lists all six decompositions of H1(K(3))=S4+W. Four have a negative A_std or trivial coefficient in R4. The other two yield R4=V+P. Every genuine option has a V absent from the target, and is excluded.

For Q_d, the positive S4 Euler coefficient forces H0(K(3))=S4, and H1(K(3))=T6. Since T6 is irreducible, the lower part is exactly one of T6(-5), V(-6), W'(-7), O(-10). Quartic Euler then gives R4=V, 2V, V+P, V+D respectively. The V(-6) option violates the one-copy V capacity of the derivative target. The remaining three are precisely the theorem's K_T, K_W and K_1. Each has rank 13, degree -54, H0(K(3))=S4 and H1(K(3))=T6, matching a=0 and the exact source/quotient Euler relation.

## Boundary of this verification

No substantive correction was required. The complete written proof already includes the additional cohomology atoms that must be discarded by nongenuineness, rather than silently omitting them. No actual HM coefficient, parameter, point, jet, instance rank, matrix or scan was used. No public write was performed by this reviewer.

The remaining three forms are necessary data only. They do not imply a horizontal splitting, construct the actual quotient map, fix t, or certify realization. Further exclusion requires additional actual image/filtration information or another genuine obstruction; the present proof deliberately does not claim it.
