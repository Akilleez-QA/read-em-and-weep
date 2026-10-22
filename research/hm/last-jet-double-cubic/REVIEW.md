# Independent review: corrected double-cubic / last-jet bridge

Status: PASS for the stated structural bridge, conditional on the explicitly pinned actual-family theorems. This is an independent mathematical review, not formal verification or an operator-value computation.

Reviewed PROOF.md SHA256: c03b43cea341967da3bff0c955087fcba918f3d11f8c57ba1f10b37136119028.

## Sources actually checked

Repository: Akilleez-QA/read-em-and-weep.

- PR543, commit 14fc90d90f74998c10ea9f2b45cf5b8aeac96bae: ACTUAL-DEGREE-EIGHT-NORMAL-OPERATOR-QUOTIENT.md, ACTUAL-DEGREE-EIGHT-DEFECT-AS-DOUBLE-CUBIC-PUSHFORWARD.md, ACTUAL-CUBIC-SUPPORT-IS-GENUS-FOUR-WITH-EXACT-FIVE-TORSION.md, and ACTUAL-THIRD-VALUE-AS-MIDPOINT-DUALIZING-OPERATOR-DEFECT.md, all under research/hm/order-four-quadratic-load/.
- PR648, commit 83eb365e87fe3aef3488aa339b73636fa845f630: research/hm/positive-boundary-duality/PROOF.md, particularly its definition of d by descent of delta through the intrinsic restriction map.
- PR649, commit d46dafc564e1ba97b0813491d16c32bd2e73e12f: research/hm/positive-restriction-channel/PROOF.md.
- PR1 scope README at 2531056eae05fdf31e8fb4ca3affc5907073ad73 and latest coordination, including the PR648/649 reports. The absolute positive operator remainder remains a separate open calculation.

## Checks

1. Reduced lifting is an actual surjection, not a dimension inference. Multiplication by the invertible g_D turns R into pi_*O_D(3,7). Its restriction sequence has kernel O_L(4), with zero H1. Both cohomology groups of T6 O_L(-1) vanish, so H0(E8) maps isomorphically to the cubic coefficient sections. H0(J8)=0 embeds these sections into H0(M8). This gives the exact 5-to-32-to-27 sequence.

2. The five-dimensional kernel is the actual scalar subspace. Under tau(sigma)=2N, rho sigma gives diagonal 2rho fg. Its nilpotent section is twice the class-of-N section; this is invertible in characteristic zero. Thus differences between reduced lifts lie in H0(C), not an unidentified copy of D5.

3. The extractor Q is well-defined and onto. Subtracting a reduced lift leaves a section of N; changing that lift changes it by C. H1(C)=0 permits the quotient on global sections. Its kernel is exactly K. No preferred splitting of the 32-to-27 map is needed.

4. The line factors and quotient are correct: division by f produces O_D(-5,9); multiplying by g_D^2 produces O_D(5,-1). The scalar class rho/g_D becomes rho g_D. The actual quotient is Sym^5(Wprime) O(-1)/K5(-1), not a globally split choice of g. Changes g to g+fp preserve it. The explicit output [(r-fu-gv)/f] modulo (f,g) is valid only after the reduced lift correction. An ambiguity modulo f^2 dies after division and quotienting.

5. Pure-u normalization is exact. For v=af, subtracting diag(a,-a)sigma changes (v,u) to (0,u+ag), and the diagonal residue divided by f is precisely u+ag. The scalar class rho N, represented by rho sigma/2, becomes (0,rho g), so it vanishes on Z. There is no additional factor two in the nonscalar quintic restriction map.

6. The last-layer comparison is genuinely map-level. The intrinsic map rho:M_global(4)->G|Z(4) sends tangent classes to restriction. Gauge tangents and scalar tangents vanish there. On N8/C this gives the actual pure-u quintic class. The deepest positive layer is the last odd layer, so no higher odd correction survives. The ordinary line factors, nonsplit triangular changes, and determinant-one stabilizers are addressed without claiming a homogeneous subbundle of G on a neighborhood.

7. Boundary compatibility now has an explicit route: PR543 identifies the degree-eight boundary with delta by the actual square-ideal diagram; PR648 defines delta=d H0(rho); restriction to N8 yields b|N8=(d|T)H0(rho_N). PR649 makes d|T an isomorphism. Therefore this is the same canonical corrected last-jet remainder, not merely an equivariant isomorphism between two four-dimensional representations. The 32-dimensional K here and PR649's 31-dimensional full restriction kernel are not being identified: scalar classes disappear under rho, and the comparison is through the actual restriction map.

## Review correction and boundary

The initial draft's boundary-naturality sentence was too compressed for an independently auditable normalization claim. The final draft supplies the intrinsic rho sequence, the precise descent identity, the v=af calculation, and deepest-layer/frame safeguards. These resolve that concern.

No actual selected HM coefficients, source matrices, point ranks, parameter scans, or large computations were performed. No external writes were made. The proof does not evaluate the corrected harmonic operator, prove nonzero/zero obstruction, remove the actual second-symbol image, establish higher lifting, or resolve the original algebraicity target. Those limitations are correctly retained.
