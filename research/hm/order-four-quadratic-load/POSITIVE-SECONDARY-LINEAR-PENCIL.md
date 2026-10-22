# The positive secondary obstruction is an actual linear pencil in the positive quadratic

## Theorem

Fix a nondegenerate negative quadratic q in Sym^2 W. Let

    S=H0(R,B_R(2)),  dim S=3,
    T_q=H1(R,B_R) tensor (Sym^4 W/q Sym^2 W),
    L_q:S tensor Sym^2 W -> T_q.

The established actual first scaling boundary has rank six and kernel S tensor <q>. Put U_q=T_q/im L_q, so dim U_q=18.

The next positive scaling obstruction, with the source identified with S by s |-> q s, varies LINEARLY with the positive quadratic f:

    D_q:H0(R,O_R(2)) -> Hom(S,U_q),
    f |-> d_secondary(f,q).                            (1)

Thus the remaining first-survivor test is an actual six-parameter linear pencil of maps from a three-space to an eighteen-space. This does not prove that the pencil is nonzero.

## 1. Common source and target

For every nonzero plane quadratic f, the normal scaling construction is carried out on Q_(f,q):f+q=0, with the positive part of (I^2/I^10) B(4). The relevant plane restriction cohomology depends only on the degree of f:

    H0(B_R(2)) -> H0(B_R(2)|4(f=0)) is an isomorphism,
    H1(B_R) -> H1(B_R|3(f=0)) is injective.

Both follow from H0(B_R(-6))=H1(B_R(-6))=0. The exact harmonic decomposition therefore identifies the limiting section space with S tensor Sym^2 W for all these f. The first obstruction L_q and its kernel are independent of f: lower harmonic terms vanish through H1(B_R(2))=0.

Likewise T_q and its injection into the finite obstruction space are independent of f under the displayed restriction maps. Quotienting by the fixed image of L_q gives the fixed eighteen-dimensional space U_q. This identifies actual deformation groups through natural maps, not through arbitrary bases of equally sized vector spaces.

Smooth f are the main application. The linear formula below extends to f=0, where it is zero; this extension is an algebraic formula, not an assertion that the same finite-neighborhood geometric description applies to the degenerate equation f=0.

## 2. A linear primitive can be chosen

Choose actual inversion-equivariant projective transition representatives once, before selecting f. With t=epsilon squared, write

    exp(t ad zeta_ij+t^2 ad rho_ij) modulo t^3.

Here zeta has normal degree two, rho normal degree four, and the actual cocycle identity determines delta rho through the quadratic Baker–Campbell–Hausdorff term. These data are ambient and independent of f.

For the first survivor q s, the first correction k(f,s) satisfies

    delta k(f,s)=-f[zeta,s].                            (2)

The right side has coefficients in B_R(2) and normal degree two. Since H1(B_R(2))=0, it is a coboundary for every f and s. Choose a linear right inverse to the Cech coboundary map on the finite-dimensional span of all the right sides in (2). This makes k linear in f and in s. This is a choice of proof representatives, not a selection or evaluation of actual bundle coefficients.

The residual quartic cocycle is

    tau(f,s)=[zeta,k(f,s)] - f[rho,s]
                         - one-half f[zeta,[zeta,s]].    (3)

Every term is linear in f. Projection to the quartic harmonic quotient and then to U_q gives (1).

## 3. Choice independence and equivariance

A different solution of (2) differs by a global section of B_R(2) tensor Sym^2 W. Its contribution to (3), after harmonic projection, is exactly the first boundary L_q. Hence the class in U_q is unchanged.

Changing the actual local projective frames changes both zeta, rho and the chosen correction. The associated isomorphism of deformation complexes is the identity on the limiting bundle, so it induces the identity on the first kernel and first cokernel. Naturality of the next lifting obstruction therefore leaves (1) unchanged. Equivalently, the frame-change terms in (3) consist of Cech coboundaries and first-boundary terms. Thus linearity holds for the intrinsic secondary map, not only for one representative formula.

The entire construction is equivariant as q varies: an element g of the actual binary normalizer carries D_q(f) to D_(gq)(gf) under the induced source and quotient identifications. A fixed general q is not A5-invariant. One must not treat its eighteen-dimensional target as a fixed A5 representation or impose full A5 equivariance on a single member D_q.

## 4. Exact consequences of the linear-pencil structure

For fixed q, let r be the largest rank attained by D_q(f). Then r is one of 0,1,2,3. The locus on which that rank is attained is Zariski open; its complement is cut out by homogeneous minors of the linear pencil. If r>0, this nonempty open meets the dense open of smooth plane conics.

The verified two-step lifting argument consequently gives

    generic h0(I_C^2 B_Q(4))_+ <= 3-r                 (4)

along the corresponding scaling families. Thus even a coefficient-free nonzero secondary class for one nonzero, possibly singular, positive quadratic would imply a generic improvement of the bound. Injectivity for one member would eliminate all three first survivors generically.

No such member or rank is established here. Neither generic rank nor maximal rank is inferred merely because six parameters are available.

## 5. Why ambient H0(B(2))=0 does not supply the missing nonvanishing

There is a separate FIRST normal obstruction to extending a section of B_R(2) itself into the ambient space:

    J:S -> H1(B_R) tensor Sym^2 W,
    J(s)=[zeta,s].                                    (5)

This map is injective. Indeed, the actual cup-commutator S tensor A -> H1(B_R) has already been proved nonzero, with image the unique five-dimensional constituent. Under A=Sym^2 W and 5=Sym^4 W, it is a nonzero multiple of binary multiplication. For any nonzero s, multiplication by s on Sym^2 W is nonzero (in fact injective), so not all coefficients of (5) can vanish. Equivalently (5) is a nonzero equivariant map from the irreducible three-space S.

Therefore every nonzero section of B_R(2) already fails the first ambient extension test. In particular there are no ambient formal sections restricting nontrivially to S, independently of the secondary pencil (1).

The residual section q s behaves differently. Multiplication by q becomes multiplication by -f on Q, and f kills the relevant first cohomology through H1(B_R(2))=0. This creates its first correction k; it does not make s extend as an ambient B(2) section. Even if every map in (1) vanished, the injective obstruction (5) would remain present. Hence the established ambient vanishing H0(P4,B(2))=0 gives no contradiction to that possibility by the proposed lifting argument.

The actual lower-twist vanishing H0(Q,B_Q(2))=0 likewise cannot be applied without a division theorem: a section whose scaling-limit reduction is q s may acquire a nondivisible actual normal jet at higher parameter order. The companion cone-division theorem applies only once actual jet divisibility has been established.

## Remaining interface

The missing statement is that the ACTUAL secondary tensor D_q is nonzero, or has a specified rank. Its formula involves the fourth-normal comparison term required by the actual transition cocycle, as well as the primitive in (2). The Steiner cohomology and nonzero first cup provide the formula and its source/target but do not, in the arguments given here, force this next tensor to be nonzero.

This is a precise remaining obstruction, not a claim that the tensor vanishes. The secure generic bound stays at most three. No selected HM/source coefficients, actual evaluated matrices or ranks, scans, or experiments are used.

Dependencies: SECOND-NORMAL-POSITIVE-BOUND-THREE.md proves the nonzero actual cup and rank-six first boundary. POSITIVE-RESIDUAL-SECONDARY-AND-CONE-DIVISION.md constructs the intrinsic secondary map, its eighteen-dimensional target, and the distinct actual-jet division theorem.
