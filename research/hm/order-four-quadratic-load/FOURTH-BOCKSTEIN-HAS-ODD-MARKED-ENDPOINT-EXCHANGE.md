# The fourth Bockstein has odd marked endpoint exchange

## Result and scope

Let `phi` multiply the negative coordinate block W by `mu`, where `mu^2=-1`, and fix the positive block V. Put `F'=phi^*F`, with the established determinant-preserving cone marking. Fix the physical equation q0 and a nilpotent section N on the cone. At EACH actual ambient endpoint use the boundary normalization

    xi_F=delta_(q0,F)(N),   xi_F'=delta_(q0,F')(N).

Use the pencil `q0-t a`, and the canonical cyclic probes defined by

    q0 zeta_a=a xi,   zeta_a=k At_F(D_a).

Then the actual D5 fourth gates satisfy, in the SAME actual second-symbol cokernel,

    beta4_F'(a,h)=-beta4_F(a,h).                       (1)

Here a and h on the two sides are the same coefficient vectors: a is a negative quadratic in A, and h is a positive quadratic in D5. In these boundary-normalized coordinates the actual second-symbol tensors agree, and the actual raw cubic D5 tensors agree before their second-symbol quotient.

This is a naturality constraint, not an evaluation. It does not imply that either fourth gate is zero or nonzero. In particular, it is not an oddness assertion for a fourth operation on a first-normal affine line: the midpoint does not extend to `3Q`, and no such operation at the midpoint is supplied here. The argument retains the already required third source correction. It uses no actual-instance coefficient, matrix, rank, or scan.

## 1. The marked source and target characters

The Serre involution theorem proves that the cone marking has subline/quotient ratio `-1`, and therefore sends the naturally pulled-back nilpotent to `-N`. Boundary naturality with q0 fixed gives

    phi^*xi_F=-xi_F'.                                 (2)

The coefficient polynomials transform as

    phi^*q0=q0,   phi^*a=-a,   phi^*h=h.

Consequently the D5 source `h xi` has character `-1`, whereas the A source `b xi`, for a negative quadratic b, has character `+1`. This extra cyclic-source sign is why counting only the fourth power of a would be incorrect.

The actual target `P=H1(B_Q(4))_+` has character `+1`. For completeness, its square quotient is `H1(I_Z^2(6))_+=P4`, whose sole degree-one piece comes from cover degree eight. The intrinsic block character of that piece is `mu^(6-8/2)=mu^2=-1`. The adjoint-to-square-quotient identification contributes the inverse subline/quotient ratio, also `-1`. Their product is `+1`. This is the actual identification, using the two vanishings for `G(2)`, not an identification of representations with an unspecified scalar.

These source and target markings are exactly those proved in POSITIVE-CUBIC-NORMAL-VARIATION-VANISHES-BY-SERRE-INVOLUTION.md, with the boundary normalization of xi made explicit as in ACTUAL-BLOCK-EULER-ATIYAH-CLASS-AND-ENDPOINT-SCALE.md.

## 2. The Hamiltonian determinant factor and the fixed probe

Choose the fixed volume form on W, and write `D_a=J grad(a)` for its Hamiltonian field, where `J=[[0,-1],[1,0]]`. For any invertible linear change g of the negative coordinates, pullback of vector fields obeys

    g^*D_a=(det g)^(-1) D_(g^*a).                    (3)

Indeed `g^(-1)J=(det g)^(-1)J g^t`, and the chain rule proves (3). The determinant factor must not be dropped. For `g=mu I_W`, it yields

    phi^*D_a=D_a=-D_(-a).

Both D0 and each fixed D_a commute with phi. The preceding normalization theorem writes

    xi_F=r_F At_F(D0),
    a At_F(D0)=q0 kappa_F At_F(D_a),
    k_F=r_F kappa_F.

Under the marked exchange, (2) gives `r_F'=-r_F`, while (3) and multiplication give `kappa_F'=-kappa_F`. Thus

    k_F'=k_F,   phi^*zeta_a^F=zeta_a^F'.              (4)

In contrast, the probe attached to the transformed parameter is `zeta_(-a)^F'=-zeta_a^F'`. Equation (4) compares fixed coefficient a, not the transformed polynomial. If xi were transported naturally instead of being redefined as the boundary of the fixed N, k would change sign and the scalar-coordinate version of (1) would change accordingly. The invariant naturality identity would be unchanged.

No value of r, kappa, k, or the normal displacement has been assigned.

## 3. The second image and the canonical third correction agree

The actual second symbol on A is represented by

    beta2_a(b)=[a b zeta_a] in P.

Using the two negative polynomial factors and (4), pullback of this expression is `[a b zeta_a^F']`. Since pullback acts as the identity on P, the two actual tensors beta2 agree for fixed coefficient vectors a and b. Their image subspaces and cokernel sheaves therefore agree, including every rank-drop fiber. No inverse of a specialized second-symbol matrix is used.

Choose actual ambient v_h satisfying

    q0 v_h=a h zeta_a.

For the exchanged endpoint one may choose

    v_h^F'=-phi^*v_h^F,                              (5)

since the right side of its division equation has precisely that sign. Thus the raw cubic classes `[a v_h]` are the same in P. Any allowed kernel change of v changes this class by an element divisible by q0, so it does not affect this equality.

The proven third vanishing and sheaf-injectivity of the actual second symbol give the unique global linear correction b(a,h), characterized by

    [a v_h]=beta2_a(b(a,h)).                          (6)

Since both tensors in (6) agree at the two endpoints, their corrections agree as coefficient families:

    b_F'(a,h)=b_F(a,h).

This uses the global factorization, not injectivity on an exceptional fiber. As an ambient polynomial, this same b is a negative quadratic and its pullback is `-b`. Arbitrary Schur-gauge correction coefficients are not being identified with this canonical fixed-probe correction.

## 4. Exact corrected-chain comparison

Retain all four actual ambient identities

    q0 xi=0,
    q0 zeta_a=a xi,
    q0 v_h=a h zeta_a,
    q0 w_h=a(v_h-b zeta_a).                          (7)

The last division exists by the proved third vanishing; its explicit construction and evaluation remain unresolved. Naturality does not solve it; it compares any compatible choices at the two endpoints. Given (5), choose

    w_h^F'=phi^*w_h^F.

This is valid because both a and `v_h-b zeta_a` acquire a minus sign. The source chain is

    C_F(t)=h xi+t(h zeta_a-b xi)
             +t^2(v_h-b zeta_a)+t^3 w_h,

and (7) gives the exact identity

    (q0-t a) C_F(t)=-t^4 a w_h.                     (8)

Under the marked pullback, with coefficient a and h identified as above,

    phi^*C_F(t)=-C_F'(-t).                           (9)

In particular, the terms involving b are retained in both (8) and (9). Pulling back the last obstruction gives

    phi^*[a w_h^F]=-[a w_h^F'].

The target marking is the identity, and Section 3 identifies the actual second-image quotient. This proves (1). A different choice of division changes the representative only by the established second-symbol indeterminacy, so (1) is an equality of actual fourth classes rather than a special choice of cochains.

Equivalently, naturality of any defined r-th filtered obstruction on this cyclic D5 source reads

    phi_P beta_r^F(a,h xi_F)
       =beta_r^F'(-a,-h xi_F')
       =(-1)^(r+1) beta_r^F'(a,h xi_F').              (10)

For r=3 the sign is positive; for r=4 it is negative. The second-symbol A source has the different character `+1`, as treated separately above.

## 5. Consequences and limitations

The two actual fourth gates have the same vanishing locus and the same restriction-zero conditions on the discriminant, its square fibers, and the canonical third-correction kernel. This follows from equality up to the single nonzero scalar `-1`, not from any value calculation. Formula (1) also holds in the actual cokernel fiber at a rank-drop direction, not merely as an ordinary polynomial value after embedding the ideal sheaf into O.

No fourth value, fourth rank, absolute normal scale, or extension of the midpoint is inferred. In particular, an odd exchange between two distinct actual endpoints does not make either endpoint a fixed point, and cannot itself force vanishing.

## Verification

Run `python verify_fourth_marked_endpoint_exchange.py`. It checks the full universal GL2 Hamiltonian identity, both cyclic-source normalizations, the exact corrected-chain identity, the exchange of every term including b, and the induced obstruction signs. All polynomial and group parameters remain formal. The proof uses the fixed-probe fourth reduction, the actual third factorization, the Serre target character, and the independently checked block-Euler endpoint normalization; no frozen artifact is modified.
