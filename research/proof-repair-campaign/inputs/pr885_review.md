# Independent review: PASS

## Exact reviewed artifact

This review concerns only the following frozen files:

- `PROOF.md`, SHA-256 `3e3a994defbeea2cefff4b0a64a93f70e0059417f8850a79d85069c1d45ab169`.
- `verify.py`, SHA-256 `f4f12ad03c1f8e0e8df6cb70e62ffa37c30a9f50c0f5264a6eb70fa1eac9d187`.
- `audit-inputs/manifest.json`, SHA-256 `dfcc684dec14cec2068af124f225cfaa323e6e7768995ddc19f7cbc7d8c19f8f`.

The proof and verifier were not edited during this review. All nine input files were read locally from the supplied immutable snapshots, and the verifier independently recomputed their Git blob hashes against the manifest. All matched. In particular, the review uses the exact source127 tuple `(0,1,0,0,0,1,0,1)`, not the source113 endpoint or a different source127 splitting.

The proof establishes a necessary branch reduction for this source edge. It does not exclude the entire edge, establish realizability of the surviving branch, exclude the stable label, or change a frontier count. The surviving negative row is essential and is retained.

## Verification performed

The command `python3 verify.py` completed successfully. Its checks cover the thirteen fixed rank-three candidates, the five surviving high-P kernels, all internal Hom channels for the h-b-f target, first-polar characters, exact lower-row vanishings and the surviving scalar row, the dual endpoint characters, and the original catalog identity.

I separately checked the mathematical arguments rather than treating that executable result as proof of the connection or saturation claims. Additional small fixed character checks verified

- `M3 W - M2 - M4 = 2A+2V+2P+2D`, deriving the asserted ambient character from the pinned actual presentations;
- `Wp Sym3 W = V+D`, `Wp Sym2 W = T`, and `Wp W = P`, for the cubic Euler system;
- the rank, degree and saturation-defect arithmetic for the degree-38 quotient in both relevant constant dimensions.

No actual HM/source coefficients, parameters, points, derivative values, matrices or ranks were selected or evaluated. There was no selected model, source scan or large computation. No publication or external mutation was performed.

## 1. Input transfer and kernel/internal-image classification

PR859 explicitly covers the displayed h-b-f tuple, so the onto high-P map is a valid input here. The five-kernel classification from PR867 Section 2 uses only the same onto `P O(-2) -> O(16)` sequence, rank and degree, center parity, and two fixed characters. Its transfer does not import that other proof's different internal target.

The current target is correctly retained as `D O(-4)+T O(-5)+O(-10)+O(-12)`. The full multiplicity-one Hom list in Section 2 is correct. The descriptions of the nonzero images are also sufficient to establish their saturation:

- a nonzero T component in cases I and III is an everywhere-injective universal multiplication map;
- the D-only components factor through the stated Euler quotient and then an everywhere-injective tautological multiplication;
- the case-II and case-V scalar image is saturated by either its complete quintic T component or its scalar isomorphism;
- the case-IV covariant cannot have a common invariant divisor, since the only possible positive divisor degree is twelve and the residual D/Sym2 or T/Sym1 Hom is zero.

These observations also handle graphs with both permitted components. The resulting list of J, all positive-degree exclusions, and the nongenuine `Wp+T-S` linear coefficient are correct. The only first-span alternatives remaining at that stage are precisely those in equation (5).

## 2. The projected scalar-plane lemma

The new Section 3 is valid, including its sheaf-theoretic step.

The nonzero complete T-to-O(2) row has kernel D(-4). Its internal component toward the scalar tail vanishes by degree, so this is the actual derivative kernel. Repeating the nonhorizontal-kernel argument gives the stated backward chain. The bottom O(-8) line has coefficient space a quotient of `Sym8 W=P+D`; because its span contains the rank-six T subsystem, neither proper irreducible quotient suffices. Consequently the span is the full nine-space C, the subsystem is the standard `U5^8`, and `C O/T(-3)=A O(6)`.

The original scalar O(-10) cannot disappear under projection by C. Otherwise its map to `A O(6)` would vanish by `Hom_G(A,Sym16 W)=0`, placing it in the distinct T direct summand. Its projected line has no zero divisor, since any such invariant divisor would have degree at most ten. Its constant span has dimension at least three because the constant quotient has character `A+V+D`.

The derivative containment used next is an actual coherent-image containment. The negative external row of the O(-10) line is zero by the invariant-quadratic test; the remaining external O(2) row has local lifts in the T derivative subsystem inside C. After constant projection, derivatives therefore lie in the coherent image of the original scalar plane. If that image had generic rank one, the nonzero projected line would have constant projective image, contrary to its coefficient span. Thus the scalar-plane map has generic rank two and is injective as a sheaf. Its image N is isomorphic to the original lattice `O(-8)+O(-10)`, without any assertion that N is saturated in the constant quotient.

Within that lattice, the projected O(-10) is a direct summand. Its derivative toward the quotient O(-8), twisted by -2, is a nonzero endomorphism of O(-10), hence an isomorphism everywhere. The raw first span therefore equals N as a coherent image, not merely generically. Euler's identity makes this same raw image a quotient of `W O(-9)`. Its subsequent projection onto the O(-10) direct summand would contradict ordinary degree. This completes the obstruction without assuming projection saturation.

## 3. The low-D and constant-first-span alternatives

When the D-to-O(2) row is zero, the P+D kernel list and nonzero internal-image obstruction used from PR802 are genuinely endpoint-independent at the stated interface: they require only the high-only top block, its saturated `J=O(-10)`, and the three projected Euler channels. If J is zero, the actual constant ten-space has image exactly the saturated O(18) in Q. This proves, rather than presumes, the saturation of its projected residual. The projected residual has precisely the Section 3 scalar-plane form and derivative image.

For `M=(V+P) O`, the quotient `N/F=W O(-5)` can enter E/F only through D(-2). The universal multiplication has quotient `A O`; after the first justified constant projection, this degree-zero summand is an actual constant A. Projecting by it gives the same prohibited scalar plane. Both uses of Section 3 are consequently legitimate.

## 4. C9, C12 and C8 intersections

For the rank-eight linear span, the coefficient representation is a quotient of `P Sym2 W=V+P+D`. Its dimension is at least nine, so only C9=P+D or C12=V+P+D is possible.

For C9, the linear derivative kernel is `(V+P) O(-2)`. A rank-seven N contained in that kernel would equal it by saturation, contradicting the missing V top coefficient of E. Otherwise derivatives of N force all of C9 into E-plus. The lower rows then vanish on M/F and on C9/M. The high-only kernel has rank eight and degree -18, so its degree-minus-two coefficient has dimension six or seven, neither possible inside P+D. This exclusion is sound.

For C12, the complete quadratic Euler system gives `M/F=P O`, `C/M=P O(2)`, `M-minus=F`, and the indicated derivative isomorphism. Saturation of N/F transfers across that isomorphism, proving the stated saturated Y and `C/Y=O(20)`. C cannot lie in E-plus: the exact lower-row tests would leave a rank-eleven, degree-minus-eighteen kernel inside a bundle whose degrees are at most -2. Thus `E-plus intersect C=Y` follows from saturation and the codimension-one rank comparison, not from an abstract splitting.

For C8, the coefficient kernel must contain P and the negative rank-six M must span at least seven constants, forcing `C=V+D`. The Wp-tensored cubic Euler system gives the displayed quotients and derivative isomorphism. If C lay in E-plus, its high-only kernel X would make X/F a rank-three, degree-minus-ten subbundle of E/F. It has no degree-minus-two coefficient and no possible degree-minus-three coefficient; hence degree at most -12, a contradiction. The resulting exact intersection with Y and the invariant-degree eighteen/eight lower-row tests are correct.

## 5. The endpoint-specific row and original scalar component

In C12 case I, both lower rows of Y vanish, producing the degree-38 quotient. In case II, the O(4) row still vanishes, but the negative target is exactly O(-6): the O(-6) factor of Y/M has a genuine same-degree scalar channel. It is not discarded. Its vanishing would produce the same degree-38 quotient, so it must be nonzero.

The identification with the original internal scalar is also correct. Under the quadratic derivative isomorphism, this row is the twist by two of the negative external derivative on N/F. The O(-8) factor of N/F has only the retained T(-3) and original scalar O(-8) components. Only the latter can reach the negative external O(-8) quotient. Moreover, that quotient is supplied only by the original O(-8) source summand: the top/T rows vanish by degree and the O(-10) row is excluded by the invariant-quadratic test. Surjectivity of the original Gauss quotient makes the original scalar source-to-negative-quotient map nonzero. Therefore the surviving negative row is nonzero exactly when the internal `O(-10) -> O(-10)` scalar component is nonzero. Nothing forces the accompanying T component to vanish.

## 6. Uniform degree-38 dual obstruction

The two projected image sheaves have the same cokernel and hence the same torsion defect. For X of rank c-2 and degree -38, the projected E/X has rank 19-c and degree -16. Its saturation still spans the full constant quotient of dimension 30-c. Dual global sections bound the invariant defect by five, forcing zero because the minimum positive invariant divisor has degree twelve. This establishes the required saturation before the dual argument is applied.

The extension types are exactly `O(18)+O(20)` and `W O(19)`. The pinned actual dual presentation then gives `H1(R)=D` and the displayed Euler character. The small H1 budget permits only `D O(-2)` or `O(-6)` below the linear part. The first yields a negative W multiplicity; the second uniquely forces `H0(R(1))=2Wp+T`. Finally, strict-top is applied to the actual Q-star with the exact source127 quotient `B_q=O(-18)+O(-4)+O(6)`, giving only `Wp+T` at twist one. The resulting Wp multiplicity contradiction is valid.

## Verdict

PASS. No mathematical correction is required for the frozen statement. The complete conclusion is the stated necessary h-b-f branch: nonzero low-D row, high-P kernel `W O(-7)+O(-10)`, nonzero W-to-D and internal scalar components, full twelve-dimensional constant span, and the nonzero negative O(-6) row. The proof appropriately stops there and does not claim a whole-source exclusion.
