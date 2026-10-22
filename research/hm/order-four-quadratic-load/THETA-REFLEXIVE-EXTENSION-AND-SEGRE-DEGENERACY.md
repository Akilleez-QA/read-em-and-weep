# The abelian theta kernel extends globally, and its fiber degeneracy is a Segre section

## Scope and actual inputs

Read GENERIC-BETA-ABELIAN-INTERPOLATION.md, including its parameter-line corrections and its actual sheaf-sequence construction. Let T=P(U*)=P3, P=H1(Q,F_Q(2)) of dimension5, V=det(U) tensor R20*, and

    theta: V tensor O_T -> P tensor O_T(1),
    Theta: V -> P tensor U.

Both source and target of Theta have dimension20. The abelian interpolation theorem identifies f_*M with ker(theta) off Gamma, and identifies ker(Theta) with the actual global section space K=H0(Q,B_Q(4)). Write r=dim K. No rank of Theta is assumed.

The independently checked Beilinson theorem writes Rf_*M as K tensor O plus a two-term complex of vector bundles in degrees0 and1. This note uses that theorem but does not assume that its differential has already been identified with the coefficient quotient of Theta.

## 1. The theta kernel is the entire pushforward, including Gamma

The kernel of a morphism between vector bundles on a smooth variety is reflexive. For completeness, its image is torsion-free as a subsheaf of the target bundle. The depth lemma then gives depth at least two for the kernel at local rings of dimension at least two; it is torsion-free and therefore reflexive on the normal base.

Beilinson gives f_*M=K tensor O directsum ker(vector-bundle map), hence f_*M is reflexive. The sheaf ker(theta) is reflexive by the same argument. The existing isomorphism on T minus Gamma therefore extends uniquely across Gamma, which has codimension two:

    f_*M = ker(theta) on all T.

This reflexive argument identifies the degree-zero direct image globally. The separate FINITE-EXCEPTION-DERIVED-COMPARISON.md now proves the stronger derived comparison and identifies coker(theta) with R1 f_*M everywhere.

## 2. The coefficient quotient gives an exact global diagram

Let W=im Theta and Rbar=(P tensor U)/W, of dimension r. Theta factors through W tensor O and the evaluation map P tensor U tensor O -> P tensor O(1). Its constant kernel is K tensor O. The Euler sequence therefore gives the exact sequence

    0 -> K tensor O -> f_*M -> P tensor Omega^1(1)
      -> Rbar tensor O -> coker(theta) -> 0.

These arrows retain the actual coefficient map. In particular the common rank and degree counts are not being substituted for the diagram. The quotient Rbar is kept distinct from H1(B_Q(4)) until compatibility with actual primary multiplication has been proved.

## 3. Exact fiber degeneracy criterion

Dualize the coefficient map, and regard Rbar* as the actual r-dimensional subspace ker(Theta*) of P* tensor U*. At the point [ell] in P(U*), the fiber of theta is contraction of Theta with ell. Thus

    coker(theta_[ell])* = {p in P*: p tensor ell belongs to Rbar*}.

Consequently the degeneracy locus is exactly the projection to P(U*) of

    P(Rbar*) intersect Segre(P(P*) times P(U*))

inside P(P* tensor U*)=P19. The projection statement is set-theoretic, and the vector-space formula records every fiber corank. No equality between a scheme-theoretic image and the maximal-minor degeneracy scheme, including its possible multiplicities, is asserted.

If r>=13, the projective dimension theorem forces this intersection to be nonempty: the Segre has dimension7 and P(Rbar*) has dimension r-1. Therefore theta cannot be surjective on every fiber. If r>=16, the reduced constant source W has dimension at most4, so theta has rank at most4 and fails surjectivity everywhere.

If a subspace P0 of P* satisfies U* tensor P0 contained in Rbar*, then every fiber corank is at least dim P0. This is a direct consequence of the same formula. Identifying this P0 with the earlier jet-kernel block requires the additional compatibility noted in Section2.

## 4. A precise limitation of fiberwise maximal rank

A nonzero constant kernel does not force any fiber degeneracy. This can be checked without any HM coefficient evaluation: in abstract vector spaces of dimensions5 and4, choose independent p1,p2 and ell1,ell2, and let Rbar* be the line spanned by

    p1 tensor ell1 + p2 tensor ell2.

Its nonzero tensors have rank two, so this line contains no decomposable tensor. Let W be its annihilator, and take a twenty-dimensional source mapping onto W with a one-dimensional kernel. The associated theta is surjective at every point by Section3, but its global coefficient map has a one-dimensional kernel.

This is an abstract compatibility example, not a model asserted to arise from HM and not a selected-instance experiment. It proves that the Beilinson structure and pointwise maximal rank alone cannot exclude the remaining constant kernel. An additional property of the actual coefficient map is indispensable.

## Boundary

The theorem strengthens the off-Gamma kernel presentation to a global reflexive identity and gives exact degeneracy restrictions. It does not prove r=0 or assert that a general-matrix model describes the actual HM boundary. The subsequent finite-exception derived comparison identifies the higher direct image across Gamma, as recorded in Section5.

## 5. Compatibility with jets and fiber specialness

FINITE-EXCEPTION-DERIVED-COMPARISON.md identifies Rbar with the actual H1(B_Q(4)) compatibly with primary multiplication. Thus Rbar* is exactly the actual subspace used in BASE-IDEAL-POWER-JETS-AND-ADJOINT-PROLONGATIONS.md. Its maximal full U*-block P0 is, up to the fixed determinant factor, J5.

If j=dim J5, the annihilator condition gives an actual quotient

    R1 f_*M=coker theta -> P0* tensor O(1) -> 0.

Derived base change of the global two-term theta complex identifies H1 of every curve fiber with coker(theta_[ell]). Consequently every fiber has h1(M|fiber)>=j and h0(M|fiber)>=15+j, since its Euler characteristic is15. In particular a single fiber with H1(M|fiber)=0 forces J5=0. This is not a proof that such a fiber exists.

Combined with the independently checked low-corank prolongation theorem, if r<=6 and some fiber is nonspecial, then both auxiliary jet kernels vanish. No actual bound r<=6 or existence of such a fiber is asserted. The point is that a nonzero J5 is a precise persistent-specialness obstruction across the entire beta family, rather than an unrelated interpolation failure.
