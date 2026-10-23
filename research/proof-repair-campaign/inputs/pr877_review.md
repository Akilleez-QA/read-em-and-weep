# Independent review of the source113 bb exclusion

## Verdict and reviewed object

**PASS. No mathematical blocker or required correction was found.** The frozen proof excludes the entire original source edge at source index 113 with tuple `(0,2,0,0,0,0,0,1)`. It does not by itself exclude the stable label, dispose of the separate bf source, or justify a frontier decrement.

Reviewed file: `PROOF.md`.

Exact SHA256 reviewed:

`33e9195434e1c57b8d33fcec2bd6e80f76daf4cf4cd77092c93dfff4f1b42e3e`

Review date: 2026-10-23 UTC.

The proof was read independently, including the universal bundle arguments rather than only its verifier. The supplied fixed verifier was also run successfully. No selected actual source coefficients, parameters, points, derivative values, matrices, source-instance ranks, models, scans, or large computation were used. No publication was performed and the frozen proof was not edited.

## 1. Input and scope audit

All four original audit-input Git blob hashes match those stated in the proof. The catalog entry at index 113 has exactly

- A_q = O(-10) + O(2) + O(16);
- B_q = O(-18) + O(-4) + O(8);
- original determinant defect zero;
- ten compatible source tuples, including the stated bb tuple.

The stable-label file associates `G3.11.ad509d55173f` with original source index 113. The original decoder's equations give R_2=P for this tuple, followed by two T(-3) atoms and one O(-10), so the asserted E has rank 17 and degree -54. The exact pinned actual presentation supplies the cohomology and full-span hypotheses used later; these are not inferred merely from the source's splitting character.

The local mathematical dependencies inspected were:

- high-P kernel classification, SHA256 `10030e0f7acc9ac4bb35efb29356c2a85132b88876983d58b8a359d2c660e07f`;
- divisor-twelve argument, SHA256 `0477e228a7253400fc80c58e484157a23cbadce559dcf252758155191f490f5f`;
- cf degree-38 obstruction, SHA256 `2c9faa4394d96c158530f90bbccd586d0685b47da63c34ad4c66b7fb65ad5553`.

The new proof restates the applicable universal arguments. It does not import a source127 internal-image exclusion into the different bb internal target, or assume the cf branch's quotient saturation without proving it here.

## 2. Divisor-twelve branch

Strict-top gives four independent degree-18 sections. After removing a common invariant divisor, their independence bounds its degree by 15. Minimal invariant-orbit degree, central parity, and the absence of an invariant in Sym14 W leave exactly degree 12.

The reduced P subsystem of Sym6 W has kernel V(-4): the H1 budget at twist two is the irreducible V, and the rank, parity, and degree bounds leave this single atom. The exact bb internal target is 2T(-5)+O(-12), so its entire internal derivative vanishes by degree.

Consequently the actual raw first span has rank 5 and degree -2, with quotient O(6) by F. A saturation defect has length at most 2 because the saturation is a subbundle of a trivial bundle. Its invariant determinant divisor would otherwise have degree at least 12. Thus the raw first span is saturated. There is no erroneous substitution of the saturated external O(16) for the actual divisor-branch O(4).

The polar characters give V O + Wp(-1). The V factor is the actual constant subspace H0(M), so quotienting by it commutes with the constant connection. The nonzero projected map P(-2) -> Wp(-1) is the unique equivariant Euler surjection. Local lifts then show that the projected Wp(-1) is preserved by the connection. Its negative degree contradicts horizontality. This step is valid and does not treat an arbitrary equivariant splitting as horizontal.

## 3. Complete kernel list and every internal channel

The rank-three decomposition alternatives are exhaustive: a three-dimensional even irreducible, an odd two-dimensional irreducible plus a scalar, or three scalar lines. H0(K(2))=0 excludes degrees above -3. Rank, total degree -24, central parity, and the lack of a trivial constituent in H1(K(2)) reduce these to exactly the thirteen stated candidates. The two fixed character constraints retain precisely the five listed kernels.

For the actual bb target 2T(-5)+O(-12), the only possible nonzero components are, respectively,

1. A(-8) -> 2T(-5);
2. O(-10) -> 2T(-5);
3. W(-9) -> 2T(-5);
4. O(-18) -> 2T(-5);
5. O(-10) -> 2T(-5).

Every map to O(-12) vanishes. In particular the potentially nonnegative-degree O(-18) -> O(-12) channel vanishes because Sym6 W has no invariant. Each channel to one T row has multiplicity one.

The multiplication maps by the universal tautological third, fifth, and fourth powers are fiberwise injective. A nonzero multiplicity vector across the two T rows preserves this property. The unique degree-13 T covariant has no common divisor: a nonempty invariant divisor would have degree 12 (odd degree 13 cannot be invariant), and division would put T in Sym1 W. Hence its line image is also saturated.

The saturated internal/external image lemma is applicable in all these basepoint-free cases. The zero internal image and the scalar O(-10) images give positive-degree first spans, which cannot embed in a constant bundle. The W(-9) image gives the nongenuine linear coefficient Wp+T-S. The two remaining first spans and internal intersections are exactly those in (6) and (8). The script's fixed Hom and character audit agrees with these deductions.

## 4. The A(-8) branch

### Actual coefficient spans

The rank-eight span M=(Wp+T)(-1) is exactly the polar image P W(-1). Its coefficient span is a quotient of P Sym2 W=V+P+D. It must have dimension at least 9: equality between its rank and its constant-span dimension would force this saturated negative bundle to equal the constant bundle. Multiplicity-freeness leaves only P+D or V+P+D.

### Nine-dimensional span

For C=P+D, M is the complete O(8) evaluation kernel. One direct justification is that C O/M is a line of degree 8 and H0(M)=H1(M)=0, so C -> H0(O(8)) is an isomorphism. Thus M^-=Sym6 W(-2).

N=E intersect M is saturated in M. If N lies in M^-, equality follows from their equal ranks and saturation, contradicting the absence of every equivariant V(-2) -> E channel. Otherwise the derivative of N has nonzero generic image in C O/M. Since N lies in E and M lies in E^+, saturation of E^+ forces the entire C O into E^+.

The lower-row map vanishes on M and then on C/M=O(8) by degree. The map to L=O(18) is already onto on M, so its kernel in C has rank 8 and degree -18. This contradicts the valid HN bound -20 for a rank-eight subbundle of the exact E. No saturation of a merely generically onto lower-row map is assumed.

### Twelve-dimensional span

The isomorphism from the actual quadratic coefficient space identifies the inclusion with P tensored with the complete quadratic system. Thus M/F=P O, C/M=P O(2), M^-=F, and the derivative M/F -> (C/M)(-2) is an isomorphism for the actual connection.

The saturated N/F=A(-6) consequently produces the saturated Y/M=A(-4). Since derivatives of F generate M, the raw first span of N already contains M; taking the inverse image of this saturated image gives exactly Y. In particular Y is saturated, has rank 11 and degree -20, and C/Y=O(20).

If C were contained in E^+, its lower-row map would factor through P O(2) and vanish. A rank-eleven degree-minus-18 subbundle of E would result, contradicting the HN bound -29. Therefore E^+ intersect C=Y, using saturation of both intersections. The lower-row map of Y vanishes because A is absent from Sym8 W and the other degree is negative. This gives X=E intersect C, rank 10 and degree -38.

The kernel diagram is exact because M -> L is onto. It gives

0 -> A(-6) -> X/F -> A(-4) -> 0.

The invariant extension space is one-dimensional. Its zero and nonzero classes give exactly A(-6)+A(-4) and A W(-5). In the first case the A(-4) summand has no map to E/F; in the second the W(-5) summand has no map to E/F. The relevant products are T W=V+P+D and T A=Wp+S+2T. The claimed contradiction to injectivity is therefore sound in both extension types.

## 5. Last kernel: actual cubic structure and saturation

The derivative-kernel formula for a saturated linear bundle gives M^-=K1(-2), where K1 is the kernel of the actual coefficient map T W -> C. Since F is killed by the derivative of M, P lies in K1. The negative rank-six M needs a constant span of dimension at least 7; hence C=V+D, K1=P, and dim C=8.

This identifies the actual model, not just its character. Indeed the coefficient map factors through the canonical quotient (T W)/P. The standard multiplication map

Wp Sym2 W tensor W -> Wp Sym3 W

has exactly the same kernel P and is onto. The two quotient identifications differ by a constant equivariant isomorphism of C, which preserves the ambient connection. This justifies the complete cubic sequences and derivative isomorphism in (13).

N/F=O(-16) is saturated in M/F because M -> L is onto. The derivative isomorphism therefore yields a saturated O(-14) in C/M. The exact first span Y has rank 7, degree -20, and quotient O(20), and is saturated in C and H.

The proposed containment C subset E^+ is impossible. It would imply a rank-three degree-minus-10 bundle X/F inside 2T(-3)+O(-10). All its degrees are at most -3. A degree-minus-three coefficient in rank three is necessarily W or Wp, but neither has any channel into that residual target. Thus all its degrees would be at most -4, contradicting the degree. With C not contained in E^+, saturation gives E^+ intersect C=Y.

The two potential lower-row maps out of Y/M=O(-14) have invariant degrees 18 and 6, both absent. Hence X has the asserted rank 6 and degree -38, and U0=C/X has the actual exact sequence 0 -> O(18) -> U0 -> O(20) -> 0.

The final saturation argument is correct and indispensable. U0 -> Q and E/X -> (H/C) O have the same cokernel, so their torsion defects agree. Writing its length as delta gives a saturated residual Z of rank 11 and degree -16+delta. Full span of the original E implies that Z spans the full 22-dimensional H/C. Since Z has nonpositive splitting degrees,

22 <= h0(Z*) = 27-delta.

Thus 0 <= delta <= 5. The invariant determinant divisor has no nonzero length in this interval, so delta=0. This proves that U0 is saturated in Q; saturation is not assumed from the extension alone.

## 6. Original dual endpoint

The two possible U types have the same equivariant K-class. The exact original presentation of Q* gives H1(Q*)=A+2V+3P+4D and its stated twist-three Euler character. In the exact dual sequence, all degree-zero cohomology groups vanish. Subtraction therefore gives H1(R)=D and the stated Euler character for R.

The small H1 budget permits precisely D(-2) or O(-6), plus degree-minus-one atoms. The D(-2) case requires a negative W multiplicity and is impossible. The other case uniquely forces the degree-minus-one coefficient 2Wp+T. This reproduces the degree-38 obstruction with the exact original B_q, not a replacement endpoint.

The original strict-top lemma applies to Q* because all its splitting degrees are at most -1. It injects H0(Q*(1)) into H0(B_q(1))=Sym9 W=S+T. The subbundle R supplies 2Wp+T inside the source, contradicting the absence of Wp in the target. The argument correctly does not assume the stronger and unavailable H0(Q*(1))=0.

## Corrections and presentation notes

No correction is required for acceptance. Two optional expansions would make the frozen proof more self-contained:

1. State the H0/H1 argument identifying the nine-dimensional linear system with the complete O(8) evaluation kernel.
2. State the actual coefficient-quotient identification with the cubic model, as above, to make explicit why the cubic Euler sequences describe the actual connection rather than only an abstract character.

These are explanatory expansions of valid inferences, not unresolved assumptions. The complete source-edge exclusion is established within the stated pinned actual-bundle hypotheses. This is a mathematical review and finite arithmetic audit, not formal proof-assistant certification.
