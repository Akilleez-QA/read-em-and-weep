# Structural nonvanishing of the canonical cubic Massey operation

## Statement

Under the established locally split HM presentation, derivative-product embedding, transgression theorem, and canonical cubic operation, one has

    f(u,u,w) != 0 whenever u,w in U1 are linearly independent.

In particular the unique symmetry-eligible cubic scalar is nonzero. The argument uses universal geometric injectivity and perfect trace duality. It does not calculate any derivative-product matrix, inverse-transgression matrix, selected point value, or scalar Massey value.

Notation below avoids confusing the several spaces called V, A, or W in the imported representation-theoretic proofs. Write

    K^(-1)=A O(-1), K^0=C O, K^1=E O(1), K^2=W O(2),
    dim(A,C,E,W)=(5,15,10,2).

Let L be the five-dimensional homogeneous coordinate-direction space, so the linear differential is the linear map D:L -> coefficient maps of internal degree one. The derivative theorem identifies L with U1. Write gamma_u:A -> C for the first coefficient block of D_u.

## 1. Hypotheses already proved

The imported results are precisely:

1. K is locally split with only locally free degree-zero cohomology H. In particular gamma:A O(-1) -> C O is a subbundle injection.
2. D_u D_v + D_v D_u=0, and D_u gives the derivative lift of the corresponding U1 class. Thus D_u^2=0 in characteristic zero.
3. All ordered U1 pair products vanish. The transgression d5 is injective, with image the derivative-product subspace, and the map Lambda^2 L -> global degree-two cocycles, u wedge w |-> D_u D_w, is injective.
4. For every phi in Hom(W,A), the universal Cech primitive h_phi has total degree one and twist -2, satisfies delta h_phi=d5(phi), and has top component phi/(v0 v1 v2 v3 v4), of internal degree -3 and Cech degree 4. Here d5 includes the fixed generator of H^4(O(-5)).
5. Every B:C -> W extends uniquely to a closed global internal-degree-two twist--2 cochain eta_B. Its other block A -> E is uniquely forced by ev(v) eta_A=B gamma(v).
6. H^1(End H(-2))=0, so the operation f=m111 is a canonical singleton in H^2(End H(-3)).

Sources: [the hm presentation independent manuscript](../../../hm-presentation-independent/PROOF.md); [the derivative transgression relations manuscript](../../../derivative-transgression-relations/PROOF.md) and EXPLICIT-COEFFICIENT-QUOTIENT.md; [the cech transgression primitives manuscript](../../foundation-p05/CECH-PRIMITIVES.md); [the cubic massey module reduction manuscript](../../canonical-cubic-extension/cubic-massey-module-reduction/PROOF.md).

## 2. Geometric injectivity, without a selected-point computation

The subbundle statement in (1) is essential. Mere injectivity of a morphism of sheaves would not suffice to infer injectivity on fibers. The imported proof gives local splitting of the entire complex, hence the stronger statement needed here.

Equivalently, on P(L), the universal coefficient morphism

    A tensor O(-1) -> C tensor O

is injective after every pullback. Pulling back to any line ell in L gives an injection A tensor ell -> C. Trivializing ell by any nonzero u in ell identifies this map with gamma_u. Thus gamma_u is injective for every nonzero u. This is a universal consequence of the subbundle theorem, not a computation or rank test at any chosen geometric point. It remains true after every field extension.

## 3. A canonical repeated-input defining system

Fix independent abstract vectors u,w in L. The exterior-product embedding gives D_u D_w != 0 as a global cocycle. Its unique transgression antecedent

    phi_uw = d5^(-1)(D_u D_w) in Hom(W,A)

is consequently nonzero. This definition specifies an abstract antecedent; no entries or scalar components are extracted.

Use h_uu=0 and h_uw=h_(phi_uw) as the defining system. They satisfy delta h_uu=D_u^2=0 and delta h_uw=D_u D_w. Hence

    F_uw=D_u h_uw

represents f(u,u,w). Indeed the degree-one Leibniz rule gives delta F_uw=-D_u^2 D_w=0. The canonical-operation theorem eliminates dependence on any primitive choices.

The top component of F_uw is

    (D_u phi_uw)/(v0 v1 v2 v3 v4).

Left multiplication by a global Cech-degree-zero cochain introduces no cup-product sign in the imported totalization convention.

## 4. Exact Serre-pairing calculation as a universal identity

For any B:C -> W use the global closed dual cocycle eta_B supplied by (5). The target of F_uw is H^2(End H(-3)); its Serre dual is H^2(End H(-2)). Their product lies in hypercohomology degree four and twist -5.

The trace on a perfect complex is represented by supertrace: it is zero on nonzero internal degrees, and on internal degree zero it is the alternating trace over K^t. This is a morphism of complexes and induces the ordinary trace on End H, since K has cohomology only in degree zero. Therefore its Cech cup-composition followed by the normalized residue computes the Serre pairing. This is the perfect-complex version of the residue certificate, and is independent of whether one uses the Cech or Thom--Whitney model.

A component of F_uw in Cech degree p has internal degree 2-p. Multiplication by eta_B gives internal degree 4-p. Consequently supertrace kills every component except p=4. For p=4 the total cup-product sign is (-1)^(4*2)=+1.

At that top component, phi_uw only maps W=K^2 coefficients to A=K^(-1) coefficients. Thus D_u phi_uw only maps W to C=K^0 coefficients, using gamma_u. Composing with eta_B, whose two blocks are A -> E and C -> W, leaves precisely one diagonal block:

    C -> W -> A -> C, namely gamma_u phi_uw B.

There is no diagonal block on any other K^t. Since t=0, its supertrace sign is +1. Hence the exact universal identity is

    <f(u,u,w), [eta_B]>
      = tr_C(gamma_u phi_uw B)
      = tr_W(B gamma_u phi_uw).

Here residue sends [1/(v0 v1 v2 v3 v4)] to 1. Different coherent orientation conventions can change both descriptions by a common nonzero factor, and cannot affect the nonvanishing argument. With the declared imported convention the sign is positive.

No choice of numerical B, u, w, phi_uw, or scalar output is evaluated in this identity.

## 5. Nonvanishing

By Section 2, gamma_u is injective. By Section 3, phi_uw is nonzero. Therefore

    T=gamma_u phi_uw in Hom(W,C)

is nonzero. The ordinary trace pairing

    Hom(W,C) x Hom(C,W) -> k, (T,B) |-> tr_W(BT)

is perfect. It follows abstractly that some B has tr_W(BT) != 0. The corresponding eta_B is closed by (5), so Section 4 proves f(u,u,w) != 0.

This argument does not require preselecting an actual dual cohomology basis, computing the quotient class of eta_B, or evaluating a scalar residue. A B with nonzero trace automatically represents a nonzero dual cohomology class: if eta_B were a boundary, the pairing with the closed F_uw would vanish.

The one-dimensional eligible-operation theorem now implies that the actual cubic scalar is nonzero. Since its target J3 is irreducible under the imported group, the nonzero equivariant operation spans J3. Section 7 applies the separately established multiplication-survival and retained-projection statements to obtain the full retained span; cubic nonvanishing alone is not a replacement for those inputs.

## 6. Coordinate-independence audit

The derivative lift is canonically attached to the given linear presentation as the linear map from homogeneous directions. Coordinate changes transport its argument, the differential, and all coefficient spaces together. The subbundle property, exterior-product injectivity, transgression, composition, and trace pairing are intrinsic under these transports.

Writing phi as a bare coefficient map uses a generator of H^4(O(-5)). Changing that generator inversely rescales the coefficient phi representing the same transgression antecedent. The associated residue functional rescales compatibly. Thus the nonzero pairing, and especially the nonzero cohomology class, cannot be created or destroyed by a coordinate or volume normalization. Arbitrary constant changes of bases in A,C,E,W merely conjugate the composed endomorphism whose trace is taken.

The proof uses the existing literal presentation only to import its established geometric and cohomological properties. It does not presume that arbitrary vector bundles admit this presentation, that a sheaf monomorphism is automatically a subbundle, or that every spectral-sequence antecedent is a global primitive.

## 7. Both actual mixed channels and the complete retained test family

The precise additional imports are:

- [the full hm image symmetry manuscript](../../../full-hm-image-symmetry/PROOF.md): normalizer irreducibility of J2, and hence of its Serre-dual J3.
- [the cubic massey module reduction manuscript](../../canonical-cubic-extension/cubic-massey-module-reduction/PROOF.md), Sections 1, 3: naturality/equivariance of f, scalar-linearity identities, and the one-dimensional eligible cubic space.
- [the koszul cohomology multiplication manuscript](../../foundation-p05b/KOSZUL-MULTIPLICATION.md), Sections 3--4: surjectivity of the actual coordinate multiplications mu32:H^0(O(1)) tensor J3 -> J2 and mu21:H^0(O(1)) tensor J2 -> J1. The mixed-Massey consequences are deduced below using the separate scalar-linearity theorem.
- [the weight two massey manuscript](../../foundation-p04/WEIGHT-TWO-TRANSFER.md), Sections 1--5: surjective coefficient multiplication Sym^2 V1 -> V2, filtered defining systems, and the exact upper-symbol transfer into the retained quotient.
- [the lower weight image symmetry manuscript](../../foundation-p05b/LOWER-TRANSFER.md), Sections 4 and 6: lower-symbol transfer and the subspace-plus-quotient criterion for full retained span.
- [the filtered massey target manuscript](../../foundation-p04/FILTERED-TARGET.md), Sections 4--5: the canonical retained detector filtration of dimensions 4 and 8, and its perfect sign-valued Serre duality with the physical retained twelve-dimensional sector.
- [the canonical massey detector manuscript](../../foundation-p04/CANONICAL-MASSEY.md): the canonical invariant operation M and the correct retained dual projector e_D8,triv e_[22] e_+; its standing ordered-product hypothesis is retained unchanged.

Since f is nonzero and its target J3 is irreducible, its linearized image is J3. For every linear section ell, scalar-linearity gives

    m011(ell u,v,w)=ell f(u,v,w).

The span of the right sides is im(mu32)=J2. Thus the actual upper mixed operation has full twenty-dimensional downstairs image. Applying a second linear section m gives

    m001(ell u,m v,w)=ell m f(u,v,w),

whose span is im(mu21)=J1 because mu32 is surjective. Thus the actual lower mixed operation has full ten-dimensional downstairs image. These identities concern the actual operations, not arbitrary elements of their eligible parameter spaces.

Let Tret be the twelve-dimensional retained dual target, L=Tret,<=1 its canonical four-dimensional subspace, and I the span of all retained canonical M-values. The lower transfer theorem gives L subset I. The upper transfer theorem and surjective coefficient multiplication show that I maps onto Tret/L, of dimension eight. For any t in Tret choose i in I with the same quotient class. Then t-i lies in L subset I, so t lies in I. Consequently

    span{ e_D8,triv e_[22] e_+ M(a,b,c) : a,b,c in K } = Tret,
    dim Tret = 12.

No splitting of the 4+8 filtration is chosen or needed.

Let Pphys be the physical retained twelve-dimensional sector. The imported perfect sign-valued Serre pairing identifies Tret with its full dual. Therefore, for every rho in Pphys,

    rho=0  if and only if
    <e_D8,triv e_[22] e_+ M(a,b,c),rho>=0 for all a,b,c in K.

This is completeness of the canonical test family on the stipulated retained sector. In particular a finite subfamily of twelve linearly independent detector values exists. The proof does not construct such an explicit subfamily, calculate its pairings, decide the value of an actual physical retained class, or prove that an actual physical residual is zero or nonzero. The physical sector carries the D8 sign character; the detector uses the D8 trivial character, as required by the sign-valued pairing.

