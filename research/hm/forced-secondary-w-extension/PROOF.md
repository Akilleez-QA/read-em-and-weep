# The secondary W-extension is nonzero: a rank-five homogeneous subbundle of K

Work over C with G=SL2(F5), T=P(W*), and the actual first-cup kernel bundle K for the negative hyperplane pencil. All O(d) below are on T with the standard binary linearization. Set A=Sym2 W, D=Sym4 W, V=Sym2 W', and let P be the even four-space. No selected actual coefficient, point, jet, matrix, derivative, or instance rank is evaluated.

## 1. Immutable inputs and result

The repository is Akilleez-QA/read-em-and-weep. INPUTS.json records exact original bytes and immutable identities.

- QUOTIENT: PR968, commit 148e2eed1fbf50729941365c8fd3ae56a115fe62, research/hm/secondary-quotient-splitting/PROOF.md. It proves

      0 -> A O(-6) -> K -> Q6 -> 0,
      Q6 = P O(2) directsum W O(-1),                         (1)

  with unique G-equivariant complementary subbundle to the canonical P O(2) Harder–Narasimhan term. It retains the actual first-cup sequence

      0 -> K -> H O --mu--> J O(2) -> 0,
      H=H0(B_R(3))=Sym2 D=1+P+2D,   J=H1(B_R(1))=A+V,      (2)

  and the actual nonzero map y:D O -> A O(2), with kernel W O(-3). It proves the P component of (1) is nonzero and its equivariant Ext space has dimension two; the W Ext space has dimension one but its actual value was not selected.
- FIRST: at commit db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/ODD-FIRST-SCALING-OBSTRUCTION.md. Sections 6–7 identify the actual cup as

      mu_y(de) = class of y(d) tensor e + y(e) tensor d
                     in (A tensor D)/im(phi),                (3)
      phi: Lambda2 A tensor V -> A tensor D.

  The quotient is J=A+V; therefore phi is injective and im(phi)=P+D. The actual second-normal coefficient injection is a nonzero G-map A -> Hom(D,A), namely the unique A-channel, up to a nonzero scalar. This is an actual-map statement, not just a character equality.

We prove the remaining W component of (1) is NONZERO. Its pulled-back middle bundle K_W is consequently

      K_W = D O(-4),
      0 -> D O(-4) -> K -> P O(2) -> 0.                    (4)

The subbundle K_W is intrinsic to the canonical W complement of Q6. Identifying it with a named D O(-4) permits the usual scalar choice. The extension (4) is nonsplit, and its equivariant Ext space is two-dimensional. This reduces the actual extension problem to a nonzero class in that two-dimensional space, without choosing its direction or splitting K.

## 2. The invariant quadratic has a nonzero actual first cup

Choose the invariant nondegenerate symmetric form on the irreducible D, and let q_D in Sym2 D be its inverse tensor. Its span is the unique trivial constituent of H. This is an abstract invariant tensor construction, not a choice of actual HM coefficients.

Under the self-duality D*=D induced by this form, applying the symmetric Leibniz map in (3) to q_D gives a nonzero universal scalar times the tensor corresponding to y in A tensor D. In a dual pair of bases this follows by contracting one factor of the inverse form; the two Leibniz terms agree. The scalar is 2 with the ordinary symmetric-product normalization, and is nonzero in characteristic zero.

As y ranges through the actual second-normal coefficient space, these tensors form the nonzero A-subrepresentation of A tensor D. But im(phi)=P+D has no A constituent. Their images in J are therefore nonzero; indeed the A-channel maps isomorphically to the A constituent of J, up to scalar. Thus the restriction of the ACTUAL first-cup map to the invariant line is nonzero:

      mu|_(C q_D O): O -> J O(2)  is nonzero.               (5)

No surjectivity of a map with the same dimensions has been substituted for (3). The conclusion uses the concrete inverse-form contraction and the actual quotient by im(phi).

## 3. No equivariant W O(-1) can lift into K

An equivariant map W O(-1) -> H O corresponds to

      Hom_G(W, H tensor H0(O(1)))
        = Hom_G(W tensor W, H)
        = Hom_G(1+A, 1+P+2D) = C.                         (6)

Every such map is a scalar multiple of the canonical evaluation map

      W O(-1) -> O

followed by the invariant-line inclusion C q_D O -> H O. The evaluation is fiberwise onto, so composing any nonzero such map with (5) cannot give the zero bundle map. By exactness of (2),

      Hom_G(W O(-1), K)=0.                                (7)

On the other hand, QUOTIENT's unique equivariant splitting gives

      Hom_G(W O(-1),Q6)=C,

because the Hom into P O(2) vanishes and End_G(W O(-1))=C. Apply Hom_G(W O(-1),-) to (1). Equivariant Ext is ordinary Ext followed by invariants, since G is finite over C. The connecting map

      C -> Ext1_G(W O(-1), A O(-6))=C                    (8)

is injective by (7), hence nonzero. Its value on the inclusion of the W summand is exactly the pulled-back actual extension class. Therefore the W extension component is nonzero. This does not determine it as a numerical scalar in a chosen basis.

## 4. Identify the actual pulled-back middle bundle

The established section-kernel sequence is

      0 -> W O(-3) -> D O -> A O(2) -> 0.

Dualize it and tensor by O(-4), retaining self-duality of W,A,D. This gives an actual equivariant vector-bundle sequence

      0 -> A O(-6) -> D O(-4) -> W O(-1) -> 0.             (9)

Sequence (9) is nonsplit even nonequivariantly: a splitting would give a nonzero map W O(-1) -> D O(-4), whereas H0(O(-3))=0. It thus represents a nonzero element of the same one-dimensional equivariant Ext space in (8).

All nonzero elements of a one-dimensional extension space have isomorphic middle bundles, after a scalar automorphism of one endpoint. Consequently the actual pullback K_W of (1) along the canonical W O(-1) summand is isomorphic to D O(-4). Its inclusion in K is the actual preimage subbundle, not an arbitrarily chosen copy. Taking the quotient yields (4).

This does not make its embedding into K a constant coefficient map, and does not identify K with a direct sum.

## 5. The remaining extension is a nonzero two-dimensional class

The fixed character identities give

      P tensor D = A+V+P+2D,
      Ext1_G(P O(2),D O(-4))
        = Hom_G(P tensor D,Sym4 W) = C^2.                (10)

The actual class in (10) is nonzero, even after forgetting equivariance. Otherwise (4) would embed P O(2) into K and then into the trivial bundle H O, contradicting H0(O(-2))=0 as in QUOTIENT.

The remaining class also retains exactly the prior P-extension information. Indeed apply Hom_G(P O(2),-) to (9). Both

      Hom_G(P O(2),W O(-1))=0,
      Ext1_G(P O(2),W O(-1))
         = Hom_G(P tensor W,Sym1 W)=0                  (11)

vanish; the second uses P tensor W=W'+T6. Therefore pushout along A O(-6) -> K_W induces an isomorphism

      Ext1_G(P O(2),A O(-6))
          --> Ext1_G(P O(2),K_W).                       (12)

Let K_P be the pullback of (1) along P O(2). Since Q6 is the direct sum of its two canonical equivariant subbundles, K is the pushout of K_P along A O(-6) -> K_W. Concretely the natural addition map from K_P directsum K_W onto K has kernel the anti-diagonal common A O(-6); this follows locally from the direct-sum quotient and is compatible with the actual inclusions. Thus (12) carries the old nonzero P class to precisely the class of (4), not merely to an equal-dimensional extension space.

The identification of K_W with D O(-4) is up to scalar, so no projective direction of this nonzero class has been selected. The two-dimensional residual space is retained with its actual extension rather than replaced by a chosen split model.

## 6. A forced nonzero V component of the residual connecting map

Taking cohomology of (4) identifies the actual connecting map

    partial: H0(P O(2))=V+P+D
        -> H1(D O(-4))=A+V+P+D.                          (13)

The kernel is H0(K), because H0(D O(-4))=0. But the actual inclusion K -> H O in (2) embeds H0(K) into H=1+P+2D, which has no V constituent. Therefore the V summand of the source of (13) cannot meet its kernel. Both source and target contain V once, so the restriction of partial to V is a nonzero isomorphism onto the target V summand.

The construction of a connecting map is linear in the extension class. Thus the actual class of (4) lies outside the kernel of the linear V-channel functional from its two-dimensional equivariant Ext space to Hom_G(V,V)=C. That functional is itself nonzero, as witnessed by this structural argument. This is more precise than nonvanishing of the whole extension class, but selects no basis, scalar, or projective direction. No conclusion about the P or D components of (13) is made.

## 7. Contribution and scope

PR968 left a potentially zero W-extension component. The inverse-form/actual-cup argument excludes its vanishing and identifies the corresponding actual rank-five preimage bundle. The resulting exact sequence (4) is a new actual normal form for the first-cup kernel, with a forced nonzero residual class and natural transfer of the original P-extension.

The actual secondary boundary still factors through Q6; neither its rank nor its values are computed. No full K splitting, particular residual extension direction, opposite-pencil C splitting, vertex scalar, global odd-quadric section or source/frontier exclusion follows. The argument uses only universal tensor contraction, exact actual maps and bounded abstract character arithmetic.
