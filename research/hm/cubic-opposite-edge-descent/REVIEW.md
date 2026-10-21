# Independent review of the Hessian-free descent formula

Reviewed PROOF.md SHA256: `c77b4de149cd94c40d2df3312ef54602996d99eebc8a2d20badd5b96cbef153d`.

Verdict: **PASS**, conditional on the explicitly pinned inputs from PR611, PR615, and PR616. This is an independent mathematical audit, not formal verification. No selected HM/source coefficients, derivative values, point evaluations, matrices, or numerical ranks were computed.

## 1. The stronger polar vanishing

The input simultaneous singular-section line has support a x_1^2 x_4+b x_3^2 x_0 for the normalized pair (0,1)/(4,3). At L_0 the quadratic term is b x_3^2 and the marked direction is x_1. At L_4 it is a x_1^2 and the marked direction is x_3. In both cases the mixed bilinear polar with the marked direction and an arbitrary tangent vector is identically zero. This uses the monomial supports, not either coefficient's value or ratio. The claim is stronger than vanishing on the marked direction twice.

The value and ambient first jet vanish at both centers. This is immediate from those same supports; it is also consistent with singularity of the corresponding D-section along the exceptional divisor. Therefore the second jet is intrinsic as a fiber-valued quadratic form. A local frame change contributes no lower-order corrections. Normalizer and affine character transport give the same assertion at every paired mark.

## 2. Moving-center expansion

For a normalization-compatible motion, every s has a lift s+epsilon t_s with t_s(z)=-ds_z(v_z). For s in the simultaneous singular line, both ambient first jets vanish at its paired centers, so t_s vanishes there too.

In a moving blowup chart x=epsilon v+u xi(a), the constant coefficient in the numerator s(x)+epsilon t_s(x) vanishes because the lifted cubic vanishes at the moving center. Dividing by u gives a regular local D-section. Its epsilon coefficient at u=a=0 is the coefficient of epsilon-u before division, namely

    Hess_s(v,xi)+dt_s(xi).

There is no omitted term from epsilon t_s(epsilon v+u xi), because its dependence on epsilon v is multiplied by epsilon and vanishes modulo epsilon squared. The Hessian convention in the proof is the bilinear second derivative, so the mixed Taylor term has the displayed coefficient without an extra factor. The previously established polar vanishing kills the first term for arbitrary v.

## 3. Choice independence and the quotient

Changing the lifted normalization marks changes the section value by a first derivative of the central D-section. Those derivatives vanish at both marks by the definition of K_sigma. Changing the line-gluing scalar contributes the central value, also zero. Hence these choices disappear on K_sigma, exactly as required by the quotient J_sigma=Hom(K_sigma,Q_sigma).

For a cubic vanishing at the paired centers, its first jets in their exceptional directions define values in the corresponding D-fibers. The central identification supplied by L_sigma then gives a canonical difference in Q_sigma. Such a cubic need not be a global section of D at all thirty centers; only the two local blowups enter the functional. The proof explicitly makes this distinction, so its definition on P_(z,w) is legitimate.

Every s in the actual complete system S descends, making the difference functional zero on S. Two linear choices of lifted cubic differ by a map S->S. Consequently the value of ell_sigma(t_s) does not depend on the chosen lift. No splitting of the target obstruction filtration is assumed.

The description of b_J in PR616 as the local discrepancy restricted to K_sigma now identifies the formula with the actual canonical residual map, up to its uniform Cech sign. This is not merely a formula for an abstract map with matching source and target.

## 4. Ambient-coordinate motions

For a projective vector field, the compensating cubic is its negative Lie derivative, modulo S and the harmless scalar-linearization term. Differentiation in the marked direction yields the mixed Hessian polar and a term containing the first jet of s; both vanish. Frame-linearization terms contain the value or first jet and likewise vanish. Thus the formula annihilates pgl(A), as it must to descend from center motions to H1(Theta_M).

## 5. Scope

The result removes all direct center-motion Hessian corrections from the residual descent test and supplies a canonical paired first-jet functional on lifted cubics. It does not compute such a lifted first jet, prove descent nonvanishing, or decide an exact tangent dimension. It applies only after normalization compatibility. The proof makes those boundaries explicit and uses only universal symbolic support and first-order deformation algebra, with no prohibited selected-instance evaluation.
