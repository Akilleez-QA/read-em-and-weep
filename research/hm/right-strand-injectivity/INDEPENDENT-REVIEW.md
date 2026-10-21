# Independent mathematical review

Conditional PASS for PROOF.md, SHA256 7db78c67fd887d5b4e61e4ae25ff1252a0bccd97ebf077402a57edb9ed6b5ca9. The condition is the exact published inputs linked in the proof. This is mathematical review, not formal proof-assistant checking.

## Checks

1. PR490's universal relation inclusion identifies the coefficient space S_2 with E tensor Sym^2 W and gives the two row formulas stated in the proof, up to a common nonzero scalar and determinant orientation. Those choices do not affect injectivity. The argument does not identify multiplication in S with multiplication in the auxiliary binary variables.

2. In divided-power degree one, the coefficients of e_j x^2 and e_j y^2 force R into Lambda^r B and P into Lambda^r A. For r>=2, their mixed-coefficient contractions lie in distinct exterior summands. Vanishing of all contractions then forces both exterior tensors to be zero. The r=1 exception is correctly excluded. The signed exterior-contraction convention is consistent across all three coefficient families.

3. For arbitrary divided-power degree p>=1, contraction of x*^[p-j] y*^[j] lowers the appropriate exponent without a binomial coefficient. Thus each output coefficient is the same degree-one map on adjacent exterior coefficients. Its injectivity forces all coefficients to vanish. This proves the extension to every positive divided-power order, not merely the first such differential.

4. In the PR507 normalization, the source at homological degree i on this strand has exterior degree i+1, divided-power degree i-a-1, and minimum internal degree 2i+2. The determinant line is common to source and target and causes no rank change. The proof asserts injectivity only at that initial internal degree; it does not claim the whole free S-module differential is injective.

5. For ordinary Eagon–Northcott, Q_6=0 gives image dimension dim S_6=210. The degree-six kernel in 45S(-4) has dimension 675-210=465. The initial image from 240S(-6) has dimension 240 by the universal proof. Consequently the first homology component has dimension 225. This is not a minimal-generator count.

6. Complementary homology reciprocity reverses internal degrees across total degree fifteen. Together with the left-strand minimum-degree vanishing of PR508, the new right-strand vanishing gives exactly the support intervals and reflected dimensions stated. In particular ordinary second homology lies in degrees 7..10, its complementary second homology in 5..8, ordinary and Buchsbaum–Rim third homology in 9..12, and the first homology of C^7 and C^8 in 3..6. No unsupported vanishing below degree nine is inferred for the distinct module M_3^8.

## Source verification and limits

The exact public proof files at PR490, PR495, PR507 and PR508 were retrieved for the tensor inclusion, quotient Hilbert function, complex normalization, reciprocity and earlier component/support claims. No substantive correction was needed. The extension from divided-power degree one to every positive divided-power degree was separately checked.

No selected actual HM/source-instance coefficients, numerical multiplication matrices or ranks, coefficient searches, or large computation were used. The complete defect modules, remaining determinantal parameter, fixed-source vanishing, higher-order lifting and algebraicity remain unresolved.
