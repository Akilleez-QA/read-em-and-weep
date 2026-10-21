# A Hessian-free formula for the residual cubic descent obstruction

Status: independently mathematically reviewed (PASS); see REVIEW.md. Not formally checked. Work over C. No selected coefficient, point, derivative value, obstruction matrix or numerical rank is evaluated. The symbolic local calculation applies to every paired mark using the universal character supports already proved.

## 1. Inputs and contribution

Use PR616, cf7a16cff86cf6cd7ee982b5fa6c309835d25eac, research/hm/cubic-residual-channels/PROOF.md, Sections2–4. Its normalization obstruction is the differential of cubic postulation; on its kernel the residual descent map has summands J_sigma=Hom(K_sigma,Q_sigma), with K_sigma the simultaneous singular-section line. For the normalized paired marks (0,1)/(4,3), this line has precisely the two cubic supports x_1^2 x_4 and x_3^2 x_0, with both coefficients nonzero and unevaluated. All paired marks are obtained by the universal affine character relabeling and normalizer transport there.

PR611, 12b28d33627cc0e8b283d142dc16439a51bb5e00, and PR615, 24bc9b741c287f8ac207bd9df4de4c07c50bea2f, identify the paired value fibers and the quotient by mark motions and line-gluing changes. PR618, 28f9ad6d73a557935366a9e9398a3ffcbc815c5d, resolves both normalization gates. The present lemma does not use a value for either descent gate.

The new statement is that the second jet of a simultaneous singular cubic has zero polar along each marked exceptional direction. Consequently the local residual descent discrepancy for that cubic has no center-motion Hessian term. It is exactly the difference of the first jets of its lifted cubic at the two paired directions. This gives a direct geometric formula for the remaining descent map, with all normalization lifting conditions imposed first.

## 2. Vanishing of the Hessian polar

Let sigma have paired normalization marks p,q, lying over centers z,w and corresponding to tangent lines xi in T_z P4 and eta in T_w P4. For s in K_sigma, the value and first jet of s at z and w vanish. Hence its second jets define intrinsic quadratic forms with values in the respective O(3) fibers. We assert

    Hess_z(s)(xi,-)=0,      Hess_w(s)(eta,-)=0.          (1)

Here the Hessian means the bilinear second derivative; its vanishing is independent of the harmless factor convention between second derivative and quadratic Taylor coefficient. Rescaling a local line-bundle frame multiplies this form by a unit because the value and first jet already vanish. Thus (1) is intrinsic.

It suffices to use the universal normalized pairing (0,1)/(4,3). A generator of K_sigma is

    s=a x_1^2 x_4 + b x_3^2 x_0,

where a,b are nonzero but are not evaluated. Near center L_0, use x_0=1. The quadratic Taylor term is b x_3^2, and the marked direction is the x_1-direction. Its polar in that direction is identically zero. Near center L_4, use x_4=1. The quadratic term is a x_1^2, and the marked direction is the x_3-direction. Again its polar is identically zero. This proves (1) for every section in the line K_sigma, and transport gives it at all sixty paired values.

This is stronger than the already known scalar equality Hess_z(s)(xi,xi)=0 required for singularity of the section on the blowup: the mixed polar with every center velocity vanishes.

## 3. The moving-center blowup formula

Represent a first-order normalization deformation by center velocities v=(v_z), and assume b_N(v)=0. By the postulation formula in PR616, each s in S admits a cubic lift

    s_epsilon=s+epsilon t_s,

with t_s(z)=-ds_z(v_z) at every center. One may choose these lifts linearly in s; choices differ by a map S->S. Fix s in K_sigma. Its first jets vanish at the two centers z,w, so t_s(z)=t_s(w)=0.

Choose affine coordinates near z, a local frame of O(3), and a nonzero vector xi representing the exceptional direction p. A chart of the blowup of the moving center is written locally as

    x=epsilon v_z + u xi(a),

where u is the normal parameter, a are direction parameters, and xi(0)=xi. The local section of D=3H-E is s_epsilon(x)/u; the numerator is divisible by u because s_epsilon vanishes at the moving center over C[epsilon]/(epsilon^2); all terms containing epsilon^2 are zero. Its value at the fixed lifted mark u=0,a=0 changes, to first order, by

    d t_s|z(xi) + Hess_z(s)(v_z,xi).                   (2)

This follows by taking the coefficient of u in the expansion of s(epsilon v_z+u xi)+epsilon t_s(epsilon v_z+u xi). The constant coefficient is zero, and the mixed epsilon-u coefficient is exactly (2). The same formula holds at w,eta.

By (1), both Hessian terms vanish. Therefore the two changes of section value are simply

    d t_s|z(xi),       d t_s|w(eta),                   (3)

interpreted in D_p and D_q using the chosen chart generators. These interpretations transform correctly when the generators are rescaled.

A different lift of the marks changes the section values by the first derivatives of the central section on M at p,q. Those derivatives vanish because s belongs to K_sigma. A change of line-gluing scalar multiplies the central value, which is also zero. Thus neither mark motion nor first-order fiber-gluing choice changes the residual class obtained from (3).

## 4. The intrinsic paired first-jet functional

Let P_(z,w) be the vector space of cubics vanishing at z and w. Using the central identification of D_p and D_q induced from L_sigma, define

    ell_sigma:P_(z,w) -> Q_sigma

as the difference of the first jets in the directions xi and eta, interpreted in those paired D-fibers. Equivalently, restrict the corresponding section of D to p and q and take its normalization quotient value. Only the local blowups at z,w are needed for this definition; a cubic in P_(z,w) need not vanish at the other centers.

All sections in S descend to V, so ell_sigma annihilates S. Hence it is a well-defined functional on P_(z,w)/S. For every normalization-compatible motion v and s in K_sigma, the canonical residual descent map is

    b_J(v)_sigma(s) = ell_sigma(t_s),                  (4)

up to the single uniform Cech sign used to define b. The right side is independent of the chosen cubic lift, since changing t_s by a section in S does not change ell_sigma(t_s). The preceding section proves independence of mark and gluing lifts as well. Thus (4) is an actual formula for the canonical quotient obstruction, not a choice of splitting of its target filtration.

It also visibly annihilates ambient projective-coordinate motions. For such a motion the compensating lift is t_s=-Lie_v(s), up to the chosen sign and an element of S. At z the first jet in xi is the negative of Hess_z(s)(v_z,xi) plus a term involving ds_z, both zero; the same holds at w. Thus ell_sigma(t_s)=0, consistently with the quotient by pgl(A).

## 5. Contribution and boundary

The remaining descent test can now be stated without any moving-center Hessian corrections: lift the normalization-compatible cubic system and compare the paired first jets of its simultaneous singular-section lines. The source is still ker b_N; applying (4) to arbitrary unsupported lifts without the postulation conditions would not define the obstruction.

The formula does not evaluate any of the lifted jets or the two coefficients a,b. It does not show that b_J is zero or nonzero. It replaces an implicit gluing discrepancy by a canonical functional of the lifted cubic and proves that all direct center-motion polar terms vanish identically. Higher-order lifting, full-adjoint and prescribed-source questions remain untouched.
