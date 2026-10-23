# Independent review: O(26) basepoint-free internal-channel lemma

## Verdict

**PASS**, for the exact `PROOF.md` version identified below, including the E0 residual corollary in Section 6 and both horizontal residual corollaries in Section 7. No substantive mathematical gap remains in the reviewed argument. The result is a conditional structural lemma, not an exclusion of all O(26) labels or of the degree-28 constant quotient system.

The review independently checks the kernel-support classification, both nonzero internal-image obstructions, every saturation transition, and the exact constant projection. It also checks all three residual exclusions and the exact boundary that remains.

The hypothesis that the entire external derivative of F factors through the selected O(26), not merely that its projection is onto, is explicit and sufficient. It is automatic when all other actual Gauss-quotient summands have degree below -2.

Exact versions audited on 2026-10-23:

- `PROOF.md` SHA-256: `90cccbb65eb90f7ca366ee23ecc699b2370ff939914f6b266d989d644d6d1659`.
- `verify.py` SHA-256: `e2d9aa2ee61fe5a7519293320869d3c4678a261c3f6bc905d1c6e22b5e2a7c3d`.

The latest proof bytes were read in full, and the standalone verifier was rerun successfully for this exact-version audit.

## 1. Exact kernel and character support

The kernel sequence has rank(K0)=13 and degree(K0)=-54. Strict-top vanishing gives splitting degrees at most -3. Its exact cohomology yields

- H1(K0(2))=A+V+P+D, of dimension 15;
- chi(K0(3))=-W.

For a block U O(-j), j>=4, its H1(K0(2)) contribution is U tensor Sym(j-4)W, with no virtual cancellation. Central parity and the dimension bound show that all blocks of degree at most -10 have trivial coefficient and even j between 10 and 18. Their allowed contributions are exactly those stated in the proof; j=16 fails because of its trivial constituent.

I independently implemented the nine McKay products and the symmetric-power recurrence, without importing the earlier verifier or its envelopes. The bounded calculation gives 22 allowable support rows, 18 complete kernels, and exactly the five displayed kernels with a degree-at-most-minus-ten tail. The only allowable rows contributing W to H1(K0(3)) are O(-6), W O(-7), A O(-8), and O(-18). Thus the exclusion of O(-14) and the five surviving tail configurations are complete, not illustrative cases.

The subsequent equivariant Hom calculations are correct. An O(-10) tail has only its constant target channel. An O(-12) tail has either its constant O(-12) target or the unique tautological channel to W O(-11). O(-18) has no channel into either internal target. Every possible nonzero image is therefore an everywhere-saturated O(-10) or O(-12), with no omitted torsion correction.

The supplied standalone `verify.py` was inspected and run successfully. Its arithmetic is restricted to the same fixed representation ring and dimension-15 support budget.

## 2. Derivative-image saturation and first-polar generation

Because the whole external derivative lands in O(26), the image of the internal kernel is exactly the kernel of I -> O(26). Surjectivity of p makes this a short exact sequence. The quotient of the ambient derivative target by I is an extension of two locally free bundles: the internal target modulo J and Q(-2) modulo O(26). Thus I is saturated.

The inverse image I(2) in H O is consequently the actual saturated F^+. The universal quadratic first polar has image equal to the raw value-plus-derivative image, so it is onto F^+. This establishes global generation of F^+(1), while its subbundle inclusion in a constant bundle bounds all degrees above by zero. Therefore the only degrees are zero and minus one. The stated Euler characters correctly force

- J=O(-10): F^+=(A+D) O+(Wp+T) O(-1);
- J=O(-12): F^+=(A+V) O+(S+T) O(-1).

In each case C=H0(F^+) is an actual constant subspace, and Rlin=F^+/C O is saturated in the constant quotient. Since C is constant, derivatives of the projected F remain in Rlin. If the projected image contains a nonzero pure linear subbundle, local lifts show that its derivatives also lie in Rlin. Its first polar is a nonzero constant coefficient space, contradicting H0(Rlin)=0. This use of the first-polar consequence is valid.

## 3. O(-10) obstruction

The two D copies have only the multiplicity-one projected channel to T O(-1), so a full D O(-2) copy lies in the constant (A+D) O. Both quadratic Hom spaces from D into A and D are one-dimensional. Their usual SL2 maps are nonzero and therefore span these G-equivariant Hom spaces.

The map to A is second contraction by the annihilating covector, and the map to D is first contraction followed by multiplication by the tautological vector. Both annihilate the tautological fourth power. Hence every combined map kills the universal line O(-6) inside D O(-2). This contradicts the required bundle embedding. No fiber evaluation or selected model is needed.

## 4. O(-12) obstruction

The three allowed projected channels are exactly P-to-T, D-to-S, and D-to-T, all with multiplicity one. If the two D multiplicity forms are independent, a D copy surjects onto the pure linear S summand, contradicting Section 2. The dimension bounds and the same pure-linear obstruction then force both dependent D forms and the P channel to be nonzero.

Their common kernel is an actual direct-summand copy F0=D O(-2). The remaining three-channel graph P--T--D--S is a tree, so constant source/target scalings identify any nonzero triple with the standard multiplication map Sym8 W O(-2) -> Sym9 W O(-1). All three standard components are indeed nonzero: otherwise injectivity of the standard multiplication map fails by the exact source/target dimensions indicated in the proof. Thus the comparison is not based on an unchecked genericity assertion.

The standard multiplication sequence gives an everywhere-injective map with locally free cokernel O(8). Consequently F intersect C O=F0 as sheaves. F0 is saturated in H O because it is a direct summand of the saturated F, so C O/F0 is the line O(10). Passing to X=F^+/F yields the exact extension

0 -> O(10) -> X -> O(8) -> 0.

H1(O(2))=0 and finite-group averaging split it equivariantly. There is no extra line-character ambiguity for the binary icosahedral group.

The derivative-image sequence simultaneously requires a saturated O(-10) subline of X with quotient O(28). Its O(8) component vanishes because Sym18 W has no trivial constituent. Its O(10) component is an invariant degree-20 section. If zero, it cannot embed; if nonzero, its positive degree gives a nonempty zero divisor. Thus it cannot define a saturated subline. This contradiction is correct.

## 5. Constant projection and Section 6 corollary

After both internal images are excluded, F^+ has degree zero and rank 15 in a constant bundle. It is therefore an actual constant space C with character A+V+P+D. The vanishing internal image identifies C O/F with the actual saturated positive O(28) in Q. This proves both E intersect C O=F and saturation of E+C O. The projected E/F is therefore a genuine saturated residual bundle, not just an abstract quotient with the correct splitting.

For the extra Section 6 hypotheses E=E0 and A_q=O(26)+2 O(-8) with original defect zero, the raw derivative of E is saturated and constant projection gives exactly the residual Gauss quotient 2 O(-8). The invariant quadratic vanishing removes the O(-10)-to-O(-8) channel, so its exact kernel is L=O(-10).

The internal derivative of L is either zero, giving an impossible negative horizontal subbundle, or an everywhere-saturated constant-column O(-10) in 2 O(-10). The internal target is saturated in the full ambient target, so this is also the full saturated derivative image. Therefore L^+ lies in Z and has rank 2 and degree -18.

The first polar of an embedded degree-ten line has universal domain W O(-9). The saturated raw-image conclusion makes this domain surject onto L^+; equal rank and degree give an isomorphism. But its maps to the two O(-8) summands of Z are multiples of the same unique channel, and the O(-10) component is zero by degree. Every such map factors through a single O(-8), contradicting the required rank-two embedding. The additional exclusion is valid and is correctly limited to this E0 source branch.

## 6. Section 7 horizontal residual corollaries and remaining scope

Original determinant defect zero ensures that the raw derivative image of E is saturated. Since C is constant and its image in E^+/E is exactly the saturated positive O(28), projection commutes with the actual connection and gives Z^+=E^+/C O and Z^+/Z=A_neg(2). Thus Z -> A_neg is the genuine surjective Gauss map and its kernel is Z^-, not merely a formal quotient kernel. This is the precise condition needed by both added horizontal arguments.

For G3.11.dc58cc54f352 with E0, the exact map is

2 O(-8)+O(-10) -> O(-8)+O(-10).

Both cross-degree channels vanish: one by ordinary degree and the other by absence of an invariant quadratic. Surjectivity forces an isomorphism on the O(-10) summand and a nonzero constant row on 2 O(-8). Its kernel is therefore a direct top O(-8). Its internal derivative targets O(-10)+O(-12), so it vanishes by ordinary degree. This is a saturated negative horizontal subbundle of the constant ambient quotient, which is impossible in characteristic zero.

For G3.11.4b6dad66f329 with E10, the exact map is

O(-8)+W O(-9) -> W O(-9).

The O(-8) channel vanishes by degree, while the W-to-W map is a scalar isomorphism by surjectivity. The exact kernel is O(-8), with internal derivative targeting W O(-11). That derivative also vanishes by degree, giving the same negative-horizontal contradiction.

The auxiliary source exclusions are correct. For the W-tail label, E0 has only its one O(-10) summand capable of mapping to W O(-9), so it cannot surject onto this rank-two negative quotient. For the O(-8)+O(-10) label, E10 has no summand of degree at most -10 and therefore cannot surject onto the O(-10) factor. The local pinned catalog entries 112, 115, and 126 and the local frontier label records were read directly and agree with the labels, negative quotient parts, zero defects, and source-overlist statements. This was inspection of fixed input records, not execution of an envelope or scan.

Together with Section 6, these arguments leave exactly G3.11.8ae96830fd21 with E10 among the specified rank14-top E0/E10 entries with delta=0. They do not exclude that residual, the unramified degree-28 constant block, any nonzero-defect top-system case, or other source strata. The final statement preserves these limitations accurately.

## Scope of verification

Only supplied proof text, relevant local structural dependencies, and bounded abstract representation arithmetic were used. No selected actual HM/source coefficients, parameters, points, derivatives, matrices, source-instance rank calculations, model experiments, scans, large computation, or old numerical-envelope execution occurred. The review certifies the mathematical argument under the stated immutable inputs; it does not independently authenticate remote repository history or claim additional label exclusions.
