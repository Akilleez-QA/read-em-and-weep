# The global negative-quadratic kernel and its smoothing bundle

## Result

Let T=P(W*) parameterize hyperplanes containing the positive plane R, and let P=P(Sym^2 W) parameterize nonzero negative binary quadratics. Harmless self-dual identifications of the binary two-space are understood. Let Z subset T x P be the universal degree-two root divisor, with projections eta:Z->T and nu:Z->P. Define

    K=nu_* O_Z(-5),

where -5 denotes the pullback of O_T(-5). Then K is a rank-two vector bundle on all of P, with exact sequence

    0 -> K -> H1(T,O(-7)) tensor O_P(-1)
      -> H1(T,O(-5)) tensor O_P -> 0.                  (1)

Thus c1(K)=-6h and c2(K)=15h^2.

For the actual HM bundle B=End_0 F, the kernel sheaf of the actual negative-quadratic multiplication pencil is exactly

    ker[H1(B(2))_- tensor O_P(-1)
           -> H1(B(4))_- tensor O_P]
      = A tensor K,             A=Sym^2 W.             (2)

Equation (2) is global, including double roots and roots among the twelve exceptional hyperplanes. It is a sheaf identity, not an assertion that all individual fiber kernels have dimension six.

On the open set P^good where the root scheme avoids the twelve exceptional parameters, the actual cokernel is a rank-ten vector bundle C, and (2) commutes with fiber cohomology. Both statements include double roots supported at good parameters. On the further open set of distinct roots, positive quadratic directions give the canonical first smoothing obstruction

    (A tensor K) tensor Sym^2 V* tensor O_P(1)
       -> C.                                          (3)

For a fixed positive quadratic this is equivalently A tensor K -> C(-1). After choosing a representative of the negative quadratic, each fiber is the actual six-to-ten map. No rank assertion about (3) is made.

## 1. The adjacent universal hyperplane kernel

Write X=Bl_R P4 for the universal hyperplane, with maps p:X->P4 and pi:X->T. Let E_R be its exceptional divisor. The proven exact section bundle is

    pi_*p*B(3)=A tensor O_T(-6),

entirely even; see EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md.

The divisor R x T in X is E_R, and

    O_X(-E_R)=p*O_P4(-1) tensor pi*O_T(1).

The restriction sequence for p*B(4) is therefore

    0 -> p*B(3) tensor pi*O_T(1)
      -> p*B(4) -> B_R(4) external-tensor O_T -> 0.    (4)

The restriction on R is entirely even. The standard binary linearization on O_T(1) is center-odd. Taking the odd eigensheaf in (4), and pushing forward, gives the exact identity

    (pi_*p*B(4))_- = A tensor O_T(-5).                 (5)

This holds on all of T, including cohomology-jump parameters.

The universal hyperplane restriction sequence on P4 x T then identifies (5) with

    ker[H1(B(3))_+ tensor O_T(-1)
           -> H1(B(4))_- tensor O_T]
      = ker[46 O_T(-1) -> 48 O_T].                    (6)

Its cokernel has rank five and degree31, including possible torsion. In (6) the negative linear equation and the center-odd O(-1) account for the change from ambient positive to ambient negative parity. Equations (5)-(6) are the next actual linear pencil after the 44-to-46 pencil; no independent rank hypothesis is introduced.

## 2. The universal root bundle

The root divisor Z has bidegree (2,1). Twisting its defining sequence by O_T(-5) gives

    0 -> O_T(-7) external-tensor O_P(-1)
      -> O_T(-5) external-tensor O_P
      -> O_Z(-5) -> 0.

Both negative line bundles on T have no H0. The map nu is finite flat of degree two, so R1 nu_*O_Z(-5)=0. Taking direct images gives (1), with dimensions six and four. In particular K is locally free without a discriminant restriction. Its Chern classes follow from c(K)=(1-h)^6 in degrees at most two.

The other projection eta:Z->T is a P1 bundle: at a fixed root, quadratics vanishing there form a two-dimensional vector subspace. In particular eta is flat. This flatness will be important; it is not a claim that a fixed length-two root scheme is flat over T.

## 3. A uniform conductor sequence, including double roots

Let D subset P4 x P be the universal negative quadric, and put X_Z=X x_T Z. The natural map p_Z:X_Z->D is finite. Away from R it is an isomorphism. Over R its fibers are the length-two root schemes. Locally it is the finite algebra map

    A[u,v]/(q(u,v)) -> A[u,z]/(q(1,z)),  v |-> uz,

on a root chart, with the corresponding other chart covering all roots. In the double-root example q=v^2 this becomes v |-> uz with z^2=0; the nilpotent root structure is retained.

There is a uniform exact sequence

    0 -> B_D(4) -> (p_Z)_* B_XZ(4)
      -> B_R(4) external-tensor O_P(-1) -> 0.          (7)

Here is a derivation that fixes the twist and works also at double roots. On X x P the divisor X_Z has class pi*O_T(2) external-tensor O_P(1), namely p*O_P4(2)(-2E_R) external-tensor O_P(1). Its restriction sequence is

    0 -> p*B(2)(2E_R) external-tensor O_P(-1)
      -> p*B(4) -> B_XZ(4) -> 0.                      (8)

For the blowup of the codimension-two plane R,

    p_*O_X(2E_R)=O_P4,
    R1 p_*O_X(2E_R)=det N_R/P4=O_R(2) tensor det W,
    Rj p_*O_X(2E_R)=0  for j>=2.

To check the middle identity, use 0->O(E_R)->O(2E_R)->O_E_R(2E_R)->0; O(E_R) is p-acyclic, and along E_R=P(N_R/P4) the last term is the relative tautological O(-2), whose R1 is det N_R/P4. The binary determinant det W is the trivial representation. Also p_*O_X=O_P4 and all its positive direct images vanish.

Pushing (8) forward therefore gives (7), and no further direct image of B_XZ(4). The map B(2)O_P(-1)->B(4) occurring on the left is multiplication by the actual binary quadratic, so its cokernel is B_D(4).

The last term of (7) is entirely inversion-even: B_R(4) is even, and O_P(-1) is center-even because P parameterizes binary quadratics. Consequently (7) induces an isomorphism on odd direct images to P.

## 4. Proof of the global actual kernel identity

The flat map eta:Z->T permits flat base change in (5). Hence the odd relative section sheaf of B_XZ(4), first over Z and then over P, is

    nu_* eta*(A tensor O_T(-5)) = A tensor K.           (9)

Equation (7) identifies (9) with the odd direct image of B_D(4). On the other hand the actual universal quadric restriction sequence is

    0 -> B(2) external-tensor O_P(-1)
      -> B(4) external-tensor O_P
      -> B_D(4) -> 0.

The ambient H0 vanishings and H2(B(2))=0 give the exact sequence

    0 -> A tensor K -> 44 O_P(-1)
      -> 48 O_P -> C -> 0,                            (10)

where C is the actual odd R1 direct image of B_D(4). This proves (2), with actual multiplication maps throughout.

All assertions here are global sheaf identities. Additional individual-fiber sections at exceptional roots are compatible with (10) through failure of cohomology base change. A constant generic rank is not being asserted at those fibers.

For reference, the Grothendieck-class calculation gives

    ch(A tensor K)=6-18h+9h^2,
    ch(C)=10+26h-13h^2.

Thus the global cokernel sheaf has rank10,c1=26h,c2=351h^2 in the coherent-sheaf Chern-class convention. These invariants alone neither describe its singularities nor determine the smoothing rank.

## 5. The precise good-root open

Let T^good be T minus the twelve exceptional parameters. The hyperplane exhaustion theorem gives h0(B_H(3))=3 there. Equation (4) gives h0(B_H(4))_-=3 there as well. In the actual two-term presentation (6), the map consequently has constant rank on T^good; both kernel and cokernel are vector bundles and arbitrary base change is valid there.

Let P^good be the open set of quadratics whose entire root scheme is supported in T^good. Its complement is the union of the twelve lines of quadratics vanishing at an exceptional parameter. The discriminant conic need not be removed for the section-bundle assertion: a doubled good root is a length-two base change of the same constant-rank hyperplane complex. Thus for every q in P^good,

    H0(B_Dq(4))_-=(A tensor K)_q,
    h0(B_Dq(4))_-=6,
    H1(B_Dq(4))_-=C_q,       dim C_q=10.

In particular C is locally free of rank ten on P^good. To use q as the central member of a smooth inversion-even smoothing, additionally require q to have two distinct roots. A double negative root remains a rank-deficient negative block under addition of a positive quadratic, so that further restriction is essential for the smooth-quadric conclusion.

## 6. The canonical normal-direction obstruction and its twist

The ambient even quadratic parameter space has vector space Sym^2 W directsum Sym^2 V*. Along P=P(Sym^2 W), its normal bundle is

    N=Sym^2 V* tensor O_P(1).

Restrict to P^good. The first normal variation of the actual multiplication complex (10) is the canonical map

    (A tensor K) tensor N -> C.                       (11)

It is obtained by including A tensor K in H1(B(2))_- tensor O_P(-1), multiplying by the positive quadratic direction, and projecting to C. The O(1) in N cancels the tautological O(-1) in the source. Thus no arbitrary trivialization of the negative quadratic is built into (11).

For a fixed q_+ in Sym^2 V*, (11) is equivalently a map A tensor K -> C(-1). At a point q, choosing a nonzero representative of its tautological line identifies this fiber with the first Bockstein for q+s q_+. It is exactly the global six-to-ten obstruction previously compared with the weighted third differential, not a new matrix manufactured from the ranks.

Neither (11) nor its fibers have been evaluated. This construction organizes the remaining compatibility on an actual rank-six source bundle and rank-ten target bundle, while preserving the nonlinear higher-obstruction problem after a possible kernel of the first map.

## Dependencies and scope

The section-bundle identity (1) and its all-parameter interpretation depend on EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md. The good-root exhaustion and generic odd bound are HYPERPLANE-ADJOINT-EXHAUSTION-AND-SIX-TO-TEN.md. All use the checked actual geometry and ambient cohomology, not selected HM coefficients, rank scans, or moduli-density assumptions. The new global root and conductor constructions retain nonreduced root schemes explicitly.
