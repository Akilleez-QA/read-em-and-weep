# Independent audit of universal constant-connection feasibility

## Verdict and reviewed version

The proof is mathematically sound within its expressly bounded abstract scope. It constructs, for every balanced endpoint parameter, one simultaneous saturated constant-connection realization of the listed source2 data and the common commuting-pencil interface. It does not identify that realization with the fixed HM multiplication tensors or the full adjoint module.

Reviewed file: `PROOF.md` in this directory.

Reviewed proof SHA-256:

`81bb2d40705fa1e35f5719ef59323cd60af675ebe74015651dda9590a2488f29`

This review includes the PR787 compatibility paragraph and the universal square-rank-27 paragraph. Its verdict concerns the mathematical argument and the explicitly stated scope.

## 1. Construction, saturation, and the parameter family

The construction is legitimate because the three blocks are direct summands of the constant ambient representation before any differentiation. Every inclusion is saturated in its own constant block. The two required constant projections therefore have exactly the displayed intersections and locally free quotients, not merely the correct generic ranks.

Apolarity gives `ann(U_8^10)=U_1^10` and `ann(U_2^8)=U_5^8`. The balanced endpoint sequence supplies the remaining `(P+D)O(-2)` summand. Thus both source splittings, ranks, degrees, and the ambient character agree exactly. Negativity of both bundles proves the absence of constant subbundles and, by annihilator duality, their full ambient spans.

The revised family paragraph correctly distinguishes a family of constant spaces over the endpoint parameter from one canonically fixed constant representation. The tautological P-multiplicity line in the ten-section system dualizes to relative P-multiplicity `O_B(1)` in `F_t`. The coefficient identifications in the endpoint quotient and E splitting are explicitly fiberwise. The connection is relative in the X direction only. No global parameter trivialization, parameter selection, or identification with an actual HM endpoint is needed.

## 2. Complete flags and boundary conventions

Direct sums commute with the forward and backward operations here because both the original connection and the relevant quotient maps are componentwise. The revised equation (8) correctly restricts the backward formula to `j<e`; the full constant top block is fixed by backward transformation, not sent to its preceding osculating subbundle.

The formulas for the entire Q* flags give the stated E rank sequences:

- Backward: `17,14,11,9,7,5,3,2,1,0`.
- Forward: `17,20,22,24,25,26,27,28,29,30`.

Hence the central maximal rank-three profile is exactly `(2,1)`, with adjacent outward increments two. The forced dual height vector `(8,2,0)` is realized. The central A, B, and J2 quotients and both zero torsion defects follow from the genuine component symbols, not just degree matching. The residual backward flag and the four-jet consequences agree with the cited source chain.

The proof correctly avoids asserting uniform higher backward degrees. If `a_i(p)` is the endpoint vanishing sequence and `rho_j=sum_p sum_(i<=j)(a_i(p)-i)`, then the degree of the saturated endpoint osculating bundle is `-(j+1)(18-j)+rho_j`. Thus backward E degrees after order four can vary even though its entire generic rank flag is uniform. Equation (12), formulated with saturated endpoint transforms, remains correct in every ramification branch.

The PR787 fifth/sixth branches are compatible with this direct-sum construction, including their differing saturation corrections and defects. The stated conclusion that at least one low-jet exceptional parameter belongs to the balanced locus is an application of PR787, not an identification of an actual HM branch.

## 3. Source characters and presentation twists

The four cohomology characters in equation (17) follow exactly from the displayed summands and symmetric-power decompositions. In particular they are not only equalities of dimensions.

Equation (18) is correct. Its revised explanation now uses the full degree-`(d-1)` evaluation sequence, dualized and twisted by `O(-1)`. This produces, on `O(-d)`, precisely

`0 -> O(-d) -> H1(O(-d-1)) O(-1) -> H1(O(-d)) O -> 0`.

The invariant symplectic identification deals with the parameter-line duality. Applying this to E and Q* yields the stated source presentations with the correct twists and duals.

## 4. Independent check of the common-pencil lemma

For the exact sequence `0 -> E -> H O -> Q -> 0`, negativity gives `H0(E)=0`; positivity of Q gives `H1(Q(-2))=0`. The twist by `O(-1)` has acyclic middle term, so `N3=H0(Q(-1))` is canonically `H1(E(-1))`.

Multiplication by a nonzero linear form makes `A_l` injective. Naturality identifies `B_l` with multiplication on `H1(E(-1)) -> H1(E)`, which is surjective by the divisor sequence. Polynomial commutativity proves `B_u A_v=B_v A_u`.

The Koszul exact sequence on Q proves both parts needed for the middle-cohomology identification. A cycle maps to a section `ux+vy` in the kernel of the connecting map, hence to a unique element of H. Its kernel is exactly the first Koszul image. The vanishing `H1(Q(-2))=0` proves surjectivity onto H. This last vanishing is essential and is present in the hypotheses.

The fiber map is also correct: for `l=u+zv`, the cycle `(k,zk)` corresponds to the section `lk`. Its constant lift lies in `E_p` for `p=(l=0)`. Conversely every such fiber element has a unique divisible section. Keeping the tautological `O(-1)` factor identifies the original saturated inclusion, not only an abstract isomorphic bundle.

The dual presentation has the correct twist: the cokernel of `N2 O(-1) -> N3 O` is `Q(-1)`, not Q. Dualizing and twisting by `O(-1)` gives `0 -> Q* -> N3* O(-1) -> N2* O -> 0`. Serre duality gives `N2=M2`, `N3=M3`, and `N4=M4` exactly as asserted.

In the affine quotient coordinates, a Koszul boundary changes `y-zx` by `-A_l r`, so the quotient formula is well-defined. Differentiating a kernel representative `(k,zk)` gives quotient class `[k]`. Thus the common-pencil reconstruction recovers the original constant-connection Gauss map.

## 5. Square rank and the remaining source interface

The rank identity is correct. Since A is injective,

`dim ker(B_l A_l)=dim(ker B_l intersect im A_l)`.

The quotient map from `ker B_l` to `coker A_l` has the Gauss rank, so with dimensions 41,54,37 one obtains `rank(B_l A_l)=24+rank(SF_l)`. The three constructed central component symbols are nonzero everywhere, hence the square rank is 27 everywhere. This is a universal deduction, not an actual-instance rank experiment.

The final scope section is appropriately explicit. The proof does not claim that the actual source splits horizontally, that the endpoint parameter determines the original embedding, or that the constructed pencils extend to the fixed full adjoint module. The correct consequence is that no contradiction can follow solely from the jointly realized abstract axioms. Identification with the fixed HM tensors remains a distinct problem.

## 6. Corrections incorporated

The substantive audit corrections were both incorporated in the reviewed bytes: the constant-top exception in equation (8), and the evaluation-degree correction in the proof of (18). The family-versus-fixed-space clarification was also incorporated. Neither correction changes the theorem.

The citation-range exception in Section 1 also correctly includes PR787 in the final reviewed version. No mathematical correction remains outstanding.

The argument and this audit are structural: no selected source coefficients, parameter values, points, derivatives, matrices, or ranks are evaluated. This is a written mathematical review, not proof-assistant certification.
