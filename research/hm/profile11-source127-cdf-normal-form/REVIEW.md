# Independent review: canonical constant tower on the source127 c-d-f edge

## Verdict and exact object reviewed

**PASS.** The proof establishes the stated necessary normal form for an actual saturated full-span inclusion satisfying the displayed source and original defect-zero quotient data. I found no unresolved mathematical gap in the actual quotients, the derivative pullback, the residual classification, the constant-tower construction, the complete osculating reconstruction, or the final scalar-space separation.

The conclusion remains conditional on the actual inclusion having this source edge. It neither excludes the edge nor realizes the fixed HM object. In particular, the review does not promote the nonempty abstract family of PR876 to a classification of the off-diagonal lifts or to an actual HM realization.

This review binds the following exact files, read and checked on 2026-10-23:

- `PROOF.md`, 20,293 bytes, SHA256 `5cc83c225a03ba670b7859d1a64aec161611ec9cc35fffe79479fdd5b7dadf62`.
- `verify.py`, 7,469 bytes, SHA256 `9314db298a36d487412b2fc49112179e46f7d1fc49b68804623437c5b6fd8df7`.
- `REPRODUCE.md`, 4,065 bytes, SHA256 `8ae08ebff115194f68ac98478ad6690b7097813a9240ca096711eb708ad0d894`.
- `audit-inputs/manifest.json`, 2,160 bytes, SHA256 `df46fcc811dff8d1e56550cb1b2e8195a7a7a13757241f23a79e59dd150fa8d6`.

The proof and verifier were not edited during this review. The only added deliverable is this review.

## 1. Immutable inputs and the actual interface

I read the actual-presentation and strict-top notes and the entire PR876 proof, loaded both source catalogs, and inspected their exact source127 and stable-label records. The verifier authenticates all five complete source byte streams by their Git object hashes before using them. The independently checked SHA256 values are:

- `ACTUAL.md`: `a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256`; Git blob `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
- `STRICT-TOP.md`: `53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08`; Git blob `d7506dae49b4be43230450c4132bd5db91f137ef`.
- `pairs.json`: `6002ad138a41d98c351130a29703722979f31b8da90d7c75a120f28bf89480eb`; Git blob `fe0afa410d89340d3082dc814277f89fbb582c19`.
- `frontier.json`: `a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad`; Git blob `8b5971092f9ef762584912609fd5e9301c4e271d`.
- `OPEN-FAMILY.md`: `181c81c415427abef3b0e046a2791eea39bbbb65084c64afdab9227c515d1547`; Git blob `659a90911244172b222f366d8b7dea9b88e88814`.

The first four inputs are pinned to `db51525015bb7c5e825833d550d08dedf6f6ea96`; PR876 is pinned to `7c7f25911ae1df3590c2b4ffe541c21bae9b1574`. Their immutable source URLs are the ones recorded in the authenticated manifest.

The tuple `(0,0,1,1,0,1,0,0)` expands under the actual note's equations (7)-(8) to exactly

    E = (P+D)(-2) + (V+P)(-4) + O(-8).

The relevant pair is index 127, with original defect zero and scalar quotient degrees `(-8,2,16)` and `(-18,-4,6)`. The frontier record identifies it as `G3.11.cce6e3ba4eeb`, profile `11`, still `not_excluded`. These catalogs do not assert actual realization. The new proof correctly treats them as necessary data for a hypothetical actual inclusion.

With the original zero-defect convention, the actual derivative image is the saturated bundle `O(-8)+O(2)+O(16)` in `Q(-2)`. Its untwist is the saturated `E^+/E = O(-6)+O(4)+O(18)` in `Q`. Its top line `L=O(18)` and positive HN subbundle are therefore genuine subbundles, not only lists of degrees. This is the actual interface required in the proof. The frozen presentation and strict-top results are inputs, not purportedly rederived from the new normal form.

## 2. The forced A and its exact kernel

The positive preimage is saturated because it is the inverse image of a saturated subbundle in the locally free quotient. Its Euler characteristic `A-V-2P-D` forces a copy of A in its sections. Those sections are constant vectors in H. The map from the A-isotypical space to the quotient by the high line is zero: that quotient is `O(4)`, and `Hom_G(A,Sym4 W)=0`. Since `H0(E)=0`, the resulting map to `H0(L)` is injective. The A multiplicity there is one. This proves both existence and uniqueness of the actual A subspace, without choosing a noncanonical splitting of the positive quotient.

Its coefficient map has three independent sections. A common divisor therefore has degree at most 16. Equivariance makes the divisor invariant; perfection of G removes a possible nontrivial semi-invariant character. The only positive possibility in this range is degree 12: odd degrees and degrees 14 and 16 cannot occur, and smaller positive invariant divisors do not occur. Dividing by the degree-12 equation would embed A in `Sym6 W=V+P`, impossible. Thus `A O -> L` is onto everywhere.

The rank-two kernel is consequently negative of degree -18, with `H1=V+2P+D`. Equivariant splitting and central parity give exactly the four distinct even scalar pairs listed in the proof, or `W(-9)` or `Wp(-9)`. There is no missing odd scalar pair, zero-degree summand, or rank-two mixed irreducible case. The character comparison leaves only `O(-8)+O(-10)` and `W(-9)`. The former cannot embed in `A O`, since `Hom_G(O(-8),A O)=0`. Hence the actual kernel is `N_A=W(-9)`.

This kernel is saturated in E as the kernel of the map from E to the constant quotient by A. Saturation here is not inferred from its character.

## 3. Scalar splitting and the essential derivative pullback

The original external `O(-8)` row receives no map from either higher-degree source block. Its restriction to the original scalar line is therefore a nonzero scalar isomorphism. The derivative of `N_A` remains in the constant A, whose image modulo E is only L; consequently its negative external row vanishes. This forces the actual scalar component of `N_A -> E` to be zero. It proves the coherent containment `N_A subset E_hat` and the direct quotient decomposition

    E/N_A = E0 direct-sum O(-8),
    E0 = E_hat/N_A.

The projection of E by A is saturated: `(E+A)/E=L` is saturated in Q. Its direct summand E0 is therefore also saturated. These are actual quotient statements; no splitting has been inferred from Euler-character additivity.

The generation of `E_hat(4)` and the embedding of E0 in a constant bundle bound every splitting degree of E0 between -4 and 0. Projection by A removes exactly the high derivative line. The external low row of E0 is onto `O(2)`: the projected whole derivative is onto `O(-8)+O(2)`, E0 has zero negative row, and the original scalar has zero low row because `Sym10 W` has no invariant.

This alone would not justify the standalone derivative assertion. Section 4 supplies the missing argument correctly. In `Q0(-2)`, the inverse image of the low line is the actual extension

    0 -> O(-10) -> Z -> O(2) -> 0.

Its equivariant extension class is in `H1(O(-12))^G = (Sym10 W)^G = 0`. Finite-group averaging in characteristic zero is applicable. Moreover `Hom(O(2),O(-10))=0`, so the equivariant splitting is unique. Under it, the internal component of the derivative is a regular map `E0 -> O(-10)`, which vanishes by the already established splitting bounds. The remaining component is onto the actual `O(2)` summand.

The latter is saturated inside Z because its complementary quotient is `O(-10)`, and Z is saturated in `Q0(-2)` because it is the inverse image of the saturated low line. This checks both the existence and saturation of the complete standalone derivative image. No assumed connection-compatible source splitting is used.

## 4. Exhaustiveness of the three residual bundles

The exact sequence with `N_A=W(-9)` gives the stated three Euler identities and the injection

    H0(E0(1)) -> Wp+2T.

In a splitting with degrees from -4 to 0, the nonnegative-section budget is `C0 W+C1`. The tensor-with-W identities force C0 to use only V and P, and C1 only Wp and T. The derivative of `C0 O+C1(-1)` has zero external component; its possible internal component goes to degrees at most -4 and also vanishes. This is a saturated preserved subbundle of the trivial connection. Its classifying map is constant in characteristic zero, so it has degree zero. Thus `C1=0`. The constant space C0 is exactly `H0(E0)`, not an arbitrarily chosen zero-degree formal term.

Quotienting by this actual constant space preserves saturation and the standalone derivative quotient. For the degree-minus-two block of the negative quotient, a coefficient in the kernel of the map on sections to `H0(O(4))=D` would itself form a preserved negative subbundle: the internal degree targets are too low. Thus `C2` injects into the irreducible D and is either zero or D.

Writing `C0=pV+qP`, the section budget gives exactly `(0,0),(1,0),(2,0),(0,1),(1,1)`. The identity at twist one forces `C3+C4 W=C0 W`, so C4 also uses only V and P. Substitution in the untwisted Euler identity gives exactly equation (13). Requiring C2 to be zero or D fixes `u=q` and `v=p+q-1`. The zero case is nongenuine; the `2V` case would require `C3=T-Wp`. The three surviving bundles in (14) are therefore exhaustive under the established hypotheses.

This classification uses bundle splitting only for representation and cohomology calculations. It never treats such a splitting as horizontal.

## 5. Actual top-P obstruction and canonical C10

The original `P(-2)` summand has identically zero component in A for every equivariant constant complement: `Hom_G(P(-2),A O)=0`, since `A tensor Sym2 W=1+A+D`. Hence projection by A does not merely preserve its generic rank; it gives an actual injection into E0.

For either of the first two residual possibilities, the projected P has zero map to E1 by degree and irreducible type. It must then inject into `C0 O`. With `C0=V` this is a rank contradiction. With `C0=P`, its determinant would be a nonzero invariant degree-eight scalar form. The determinant characters are trivial, and that invariant space is zero. This eliminates the two alternatives without assuming a nonzero low row of the original D block.

In the remaining alternative the whole F maps to `C0 O`, since it has no map to `E1=(V+P)(-4)`. Its kernel has rank at least two and is contained in `N_A`. Equality of generic ranks first implies that the map `N_A -> E_hat/F` vanishes generically; because the target is torsion-free, it vanishes as a sheaf map. Thus `N_A subset F` coherently. It is saturated there. The resulting `F/N_A -> C0 O` has equal ranks and degree zero, so its determinant is a nonzero constant and it is an isomorphism everywhere.

This establishes the actual splitting `E0=(F/N_A) direct-sum B_src` and identifies E1 with the projection of the original B block. The inverse image of C0 in H is therefore the actual constant C10. Its intersection with E is exactly F. Locally lifting C0 through E0 shows that C10 is contained in `E+A`; since it contains A, its image in Q is precisely the saturated L. Thus

    0 -> F -> C10 O -> L=O(18) -> 0

is exact as a sequence of bundles.

The asserted canonicity is justified. A is the unique A-isotypical section space described above; `E_hat` is the intrinsic HN part of E of slopes at least -4; and C0 is the entire constant-section space of its quotient by `N_A`. Taking its inverse image in H does not require a constant-complement choice. The tower, unlike a choice of later off-diagonal lift coordinates, is canonical for the given inclusion.

## 6. Every actual negative kernel and reverse polar equality

After quotienting by C10, the original B is the actual E1 just identified. Its standalone derivative remains the saturated `O(2)` established through the pullback calculation. It is not inferred anew from the external derivative of `B direct-sum O(-8)`.

Both irreducible components of `B=(V+P)(-4) -> O(2)` are nonzero. A zero component would have no internal derivative into the equal-degree complementary block after the -2 twist, and would be a preserved negative subbundle. Since `Sym6 W=V+P` multiplicity-freely, the coefficient map is an isomorphism onto the complete degree-six system, up to its allowed equivariant coefficient isomorphism. The map is onto everywhere and its exact kernel is `T(-5)`.

For each subsequent kernel K, being the preceding derivative kernel makes its derivative land in the preceding source twisted by -2. Modulo K, the possible derivative target is exactly the preceding line quotient twisted by -2. Zero derivative is impossible for a saturated negative subbundle of a constant bundle. The relevant nonzero Hom is one-dimensional and gives the complete degree-j evaluation for j=5,4,3,2,1. Hence each map is onto, not merely generically onto, and its kernel is the next listed Euler kernel:

    T(-5), D(-6), S(-7), A(-8), W(-9), O(-10).

Every kernel is saturated in its predecessor and therefore in the constant ambient bundle. No later rank, kernel type, or absence of a defect divisor is extrapolated from the original Gauss rank.

For the last line `ell=O(-10)`, the derivative target inside `W(-9)` is another `O(-10)`. Its nonzero map is an isomorphism. Thus the raw first span of ell equals `W(-9)` as a sheaf. For every preceding stage the corresponding onto derivative has as target precisely `(parent/child)(-2)`; untwisting and taking the preimage proves the next raw first span equals that parent. This explicitly verifies every reverse equality through B.

Finally B's own saturated derivative image proves that its raw first span B+ is saturated, with rank 8 and degree -24. This last saturation is essential to the next step and is established before that step is used.

## 7. Full degree-ten span and exact scalar separation

The coefficient span of ell is an actual quotient representation of `Sym10 W=A+V+D`. All raw polar images, including B+, lie in its constant bundle. Every proper quotient has dimension at most eight. A smaller dimension cannot contain rank-eight B+. If its dimension were eight, the quotient of that constant bundle by B+ would be torsion, but would inject into the locally free ambient quotient by B+; hence it would be zero. This would identify B+ with a constant rank-eight bundle, contradicting degree -24.

Thus the coefficient map has full dimension 11. Under the resulting equivariant coefficient isomorphism, ell is the full degree-ten Veronese line, and the proved raw polar equalities identify B exactly with `U_6^10`.

The projected scalar line has coefficient span C9 of dimension at most nine, a quotient of `Sym8 W=P+D`. Full span of the original E descends to full span in the 20-dimensional quotient by C10. Since the coefficient span of the projected B is the full C11, this gives `C11+C9=H''`. The dimension formula now forces `dim C9=9` and `C11 intersect C9=0`. This proves an actual constant direct sum, not merely a representation-character equality. The scalar coefficient isomorphism identifies its inclusion with `U_0^8`; its universal polar saturation follows from its complete system.

The argument would fail without ambient saturation of B+ or without full span of E. Both hypotheses are present and are used at the exact required points.

## 8. PR876's exact open set and the top derivative

The map on constants `C10 -> Sym18 W` is injective because `H0(F)=0`. Its A and V are the unique corresponding constituents, and its P is one line in the two-dimensional P multiplicity space. Therefore it determines an unspecified projective parameter p with exactly the meaning used in PR876.

Twisting the exact C10 quotient sequence by one makes F acyclic. The induced multiplication `C10 W -> Sym19 W` is consequently an isomorphism. This is a consequence of the actual bundle sequence, not an evaluated rank test on a selected parameter.

I checked PR876's definition of Omega and its nonemptiness proof. Its fixed A-to-W and A-to-S channels are nonzero by the stated Euler sequence and fiberwise multiplication; the V-to-T channel is nonzero through `V W=T`. The P-to-Wp map is onto by its Euler sequence, while the P-to-T map is injective on covariants and has equal two-dimensional source and target. Hence multiplication is invertible exactly when the two stated nonzero linear channel conditions hold. Its isomorphism here proves that the actual unspecified p lies in that same Omega. No point is chosen, and the nonemptiness argument is not used to claim actual realization.

The top F's standalone raw first span also has no defect. It is a rank-ten raw polar image in C10 because a preserved negative hyperplane is impossible. The quadratic first-polar construction generates that image after twist one. Its splitting degrees are therefore only zero and minus one, so its determinant defect has degree at most ten. Equivariance and the degree-twelve minimum for a nonempty invariant divisor force the defect to be empty. Thus the asserted standalone derivative surjection to `O(16)` is global. The argument begins with generic rank only where appropriate and then separately proves saturation; it does not conflate the two.

## 9. Computation, reproducibility, and limits

Running `python3 verify.py` succeeded with the stated PASS output after all five Git blob authentications. I also performed a separate small fixed representation-ring check using the affine-E8 tensor-with-W graph and the recurrence `Sym(n+1)=W Sym(n)-Sym(n-1)`. It independently confirmed the symmetric powers through 19 needed here, the rank-two kernel comparison, the `Wp+2T` twist-one budget, the absent scalar invariants in degrees 8, 10, 14 and 16, and the V/P tensor-A identities. These are universal character checks only.

The verifier is useful evidence for arithmetic, source identity, and immutable provenance. It is not by itself evidence for actual sheaf saturation, derivative targets, horizontal-subspace contradictions, or reverse polar equalities; those have been checked mathematically above. The reproduction instructions correctly require the original blob bytes, not rendered GitHub HTML, and the verifier uses only the standard library.

The final constant splitting of H is an allowed equivariant choice, not a new assertion that the original B and scalar lifts have zero C10 components. The maps u and v remain in the stated regular Hom spaces, subject to any further actual conditions. This normal-form proof does not establish removal of all such maps; that question is left to a separate argument. The zero-lift case matches PR876's architecture, but exhaustion and removal of arbitrary couplings remain unproved and are not claimed.

No selected actual HM/source coefficient, parameter, point, derivative, matrix, instance rank, model, scan, or large computation was used in this audit. No external or publication write was made. No stable-label or whole-source decrement is justified by the result. The tangible contribution is the canonical constant tower and the exact residual osculating decomposition, with its still-open lift and actual-HM compatibility problem explicitly retained.
