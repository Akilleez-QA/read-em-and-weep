# Mathematical review: the adjoint primary–Rao extension

Reviewed proof: `PROOF.md`, SHA-256
`0325c7b3cf237e27d4466e17c50cdb7f1a5cd874c310f32c03516acc250a2a38`.

## Verdict and scope

The argument is mathematically consistent, conditional on its stated geometric and cohomological dependencies. The new deductions were checked independently: the all-degree module extension, its nonsplitting, the comparison of minimal cubic relations, and the fixed-ideal Tor correction. This is mathematical review, not formal proof-assistant verification. It does not independently reprove every result cited from the preceding papers or establish any value at the original fixed polynomial pair.

## Checked derivations

1. **Twists and actual maps.** The Eagon–Northcott terms agree with det F=O(-1): its first term is B(d-10), and its next term is Lambda^3 U tensor F(d-7), after the declared determinant trivializations. Splitting the resolution gives M_d=H^2(Z_d). Serre duality yields the exact-at-the-middle sequence U tensor A_(j-3) -> K_j -> P_j for j=6-d. Naturality gives the asserted graded S-actions. The degree-zero isomorphism and generation of K identify its image with N=SP_0, not merely a module of the same dimension.

2. **Dimensions and injection.** The stated line Hilbert function gives Rao dimensions (24,45,60,65,55,30,5). Subtracting the six degree-one generators of P/N gives the displayed Hilbert function of N. Its difference from that of K is exactly the Hilbert function of U tensor A(-3), including the zero tails. Exactness therefore proves injectivity of the already constructed map.

   The added h^1(B(3))=100 calculation can be made directly in the displayed resolution at d=2: H^2(F(-5))=0 and H^3(Z_2)=H^2(I_C(2))=H^1(O_C(2))=0 give

   0 -> M_2 -> H^3(B(-8)) -> Lambda^3 U tensor H^3(F(-5)) -> 0.

   Duality then gives h^1(B(3))=60+4 h^1(F(1))=100. This independently checks the draft's computation using the symmetric evaluation resolution for B(5+t) at t=-2; its twist parameter differs from the Eagon–Northcott parameter d.

3. **Nonsplitting and cubic relations.** Any graded splitting would give a projection K -> L vanishing on K_0, hence on all of K, a contradiction. The common free cover gives 0 -> R_K -> R_N -> L -> 0. Since both relation modules coincide below degree three, their degree-three products of lower relations coincide. Quotienting gives exactly the asserted short exact sequence of minimal cubic relation spaces, with quotient U tensor A_0 of dimension twenty. No vanishing of cubic relations of K is needed or proved.

4. **Fixed-ideal correction.** Tensoring the extension yields the stated Tor sequence, with kernel (L intersect JK)/JL. For J=(u,v), its degree-six primary quotient is U tensor [A_3/(uA_1+vA_0)]; in degree five it is U tensor (A_2/uA_0). For J=(u^2,v), the degree-six quotient is U tensor (A_3/vA_0). Each retains its own Tor image. These formulas follow from the degree-three shift and the vanishing A_j=0 for j<0.

5. **Koszul lift formula.** When u,v are an S-regular sequence, differential (a,b) -> ua+vb and boundary c -> (-vc,uc) give the stated connecting class. Changing lifts adds JL; lifting a Koszul boundary gives zero. The regularity requirement is correctly placed on S, not on the finite-length modules. The final two-part vanishing criterion is an immediate consequence of the resulting short exact sequence.

## Conditional dependencies and remaining questions

The review takes as inputs the evaluation-degeneracy geometry and its exact Eagon–Northcott resolution; the primary HM cohomology table and determinant characters; the adjoint cohomology table and tails; PR476's actual degree-zero generation; PR471's line Hilbert function and Rao endpoint; and PR475's actual quotient P/N. The local proofs of the five-generator and dual-Rao-generation results were consulted, but their complete external dependency chains were not reverified here.

The proof does not settle the cubic ghost, the ranks or Tor image for a specified pair, source membership, higher-order lifting, or algebraicity. Its contribution is the exact nonsplit module extension and the rigorous relation and quotient consequences stated above.
