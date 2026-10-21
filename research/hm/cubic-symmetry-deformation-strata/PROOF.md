# Six cyclic-symmetry deformation sectors of the cubic image

Work over C. Let V=V51 be the cubic image with its specified projective Heisenberg action U=(Z/5)^2. Deformations have an identified special fiber V. All group actions considered extend specified special-fiber automorphisms and act trivially on the local Artin C-algebra base.

## Pinned inputs

- PR614, commit 73fbf75838c91804ca637b5916d6aac217240958, research/hm/cubic-global-deformations/PROOF.md: the normalization M=Bl_Z(P4), the 120 reduced conductor marks Omega, H0(Theta_V)=H0(Theta_M)=0, T1(V)=H1(Theta_V), and the natural U-equivariant exact sequences

      0 -> pgl(A) -> C_Z -> H1(Theta_M) -> 0,
      0 -> C_Omega -> T1(V) -> H1(Theta_M) -> 0,

  where C_Z is the direct sum of T_z(P4) over the 30 centers and C_Omega is the direct sum of T_p(M) over the 120 marks. Every abstract Artin deformation of V is locally trivial, and the abstract deformation functor is unobstructed. Its affine lemma and overlap description give the global marked-lift torsor described in Section 3 below; relative infinitesimal automorphisms are H0(Theta_V) tensor I.
- PR625, commit 1f86c5920eda1e586bde1252ad2a4f313596d6ac, research/hm/cubic-equivariant-rigidity/PROOF.md: the universal exceptional-chart weights at each mark and the all-order rigidity of deformations retaining U.
- The six center pentads correspond to the six order-five subgroups G of U. For each G, its five centers are one U/G orbit. In eigenline labels i in F5, marks are p_ij for i!=j, and U/G acts by simultaneous translation of i,j. Thus the twenty marks of this pentad comprise four orbits indexed by d=j-i!=0, each with stabilizer G. This is the Heisenberg eigenline configuration used in PR610 and PR625.

Write Reg0(U) for the sum of the 24 nontrivial complex characters of U, not its full regular representation.

## 1. Full tangent representation

Fix G and a generator g acting on the five eigenlines L_i with eigenvalues zeta^i. At a center z_i the four tangent weights are k-i for k!=i, each nonzero residue once. Consequently the center-motion representation for this pentad is Ind_G^U Reg0(G).

For every nontrivial character chi of U, its kernel is one of the six order-five subgroups. It is nontrivial on the other five. Frobenius reciprocity therefore gives

    C_Z = 5 Reg0(U).

Conjugation on End(A) in the five-dimensional Heisenberg representation has every U-character once: the 25 Heisenberg monomials are eigenvectors with the 25 distinct characters supplied by the nondegenerate commutator pairing. Removing scalars gives pgl(A)=Reg0(U). The first exact sequence, and semisimplicity over C, yield

    H1(Theta_M) = 4 Reg0(U).

Now fix a mark orbit indexed by d!=0 and take i=0,j=d. In the universal blowup chart its four tangent weights are d and k-d for k not in {0,d}. The latter three weights comprise all nonzero residues except -d. Across the four possible d, any fixed nonzero residue r occurs once as the first weight d, and three times among the other weights (all d except -r). Hence the sum of the four stabilizer representations is 4 Reg0(G). Inducing from G gives the entire mark-motion representation for this pentad. Counting again the five directions on which each nontrivial chi is nontrivial gives

    C_Omega = 20 Reg0(U).

There is no trivial character in either sum. The second exact sequence now proves

    T1(V) = 24 Reg0(U).

These equalities are isomorphisms of representations; no canonical splitting of either exact sequence is asserted. Their dimensions are respectively 120, 96, 480 and 576, in agreement with PR614.

## 2. The six tangent sectors

For an order-five subgroup H of U, exactly five U-characters restrict trivially to H. Removing the trivial U-character leaves four. Therefore

    dim T1(V)^H = 24 times 4 = 96.

Each nontrivial U-character has exactly one such kernel H. It follows that the natural inclusions give the canonical vector-space decomposition

    T1(V) = direct-sum_{|H|=5} T1(V)^H.

In particular distinct sectors intersect in zero, and T1(V)^U=0. Canonical here refers to these invariant subspaces inside T1(V), not to chosen bases in their character multiplicity spaces.

## 3. Actual cyclic-equivariant lifts across every small extension

Let Def_H denote the functor of marked deformations with an H-action extending the specified action, modulo equivariant isomorphisms respecting the marking. We prove that Def_H is formally smooth, not just that its tangent space has dimension 96.

Let B'->B be a small extension of local Artin C-algebras with kernel I annihilated by the maximal ideal of B'. Given an H-equivariant deformation X over B, forget its action. PR614 guarantees at least one underlying lift to B'. The isomorphism classes of lifts with a fixed identification of their reduction with X form a nonempty affine torsor L under T1(V) tensor_C I.

For clarity, the global torsor assertion follows directly from the affine lemma of PR614: on a common affine cover, compare two lifts through local trivializations compatible with their fixed reduction, so their transition maps differ by a Cech one-cocycle in Theta_V tensor I, with changes of compatible trivializations giving exactly coboundaries. Conversely every such cocycle modifies the transition maps of a chosen lift to another lift, since I is square-zero and the transitions act trivially on this coefficient sheaf; this identifies the differences of lift classes with H1(Theta_V) tensor I, and relative automorphisms with H0(Theta_V) tensor I.

Transport of the reduction identification by the given H-action on X defines an affine H-action on L. Its linear part is the specified action on T1(V), tensored with the trivial action on I. The small-extension deformation theory is natural in automorphisms; since I is killed by the maximal ideal, this linear part depends only on the special-fiber action. A finite affine group action on a nonempty C-vector-space torsor has a fixed point: for any l in L, the affine barycenter |H|^{-1} sum_h h(l) is well-defined independently of a choice of origin and is invariant. Choose a lift X' representing that fixed class.

For every h, invariance of its lift class supplies an automorphism of X' reducing to the prescribed h-action on X. Such a lift is unique: the difference of two lifts is a relative infinitesimal automorphism in H0(Theta_V) tensor I=0. Compositions therefore satisfy the H group law, since both sides reduce to the same automorphism of X. Thus X' acquires an H-action lifting that on X.

This proves surjectivity Def_H(B')->Def_H(B) for every small extension. Its tangent space is T1(V)^H. More precisely, with a fixed equivariant reduction, the set of equivariant lift classes is a torsor under T1(V)^H tensor I: once a fixed lift supplies an origin, the invariant points of the affine torsor are exactly this invariant vector space. Hence the cyclic-symmetry functor is formally smooth with 96 independent first-order parameters and no higher Artin lifting obstruction.

We do not identify a representing ring or claim an analytic or algebraic family merely from this calculation. The statement about parameters means the formally smooth functor and its explicit small-extension lift torsors, not an unproved universal-moduli assertion.

## 4. Higher-order intersection of distinct sectors

The vanishing H0(Theta_V)=0 implies, by induction on a small-extension filtration of any Artin base B, that an automorphism of a deformation inducing identity on its marked special fiber is identity. Consequently a lift, when it exists, of any specified special-fiber automorphism is unique. In particular forgetting an H-action embeds Def_H as the subfunctor of underlying marked deformations that admit such an action.

Suppose one underlying marked deformation admits actions of two distinct order-five subgroups H and K of U. For h in H and k in K, the commutator of their unique lifts reduces to identity, since U is abelian. It is therefore identity. Their lifts commute and generate an action of H times K, identified with U through multiplication because H and K are distinct lines in F5^2. PR625 then makes this deformation uniquely equivariantly constant. Conversely the constant deformation retains every subgroup. Thus the intersection of these two subfunctors consists exactly of the constant deformation over every local Artin base, not just at first order.

Equivalently, every nonconstant marked Artin deformation can retain at most one of the six specified cyclic directions. This closes the next higher-order question after the tangent decomposition. It does not claim that the entire abstract deformation functor is the product of these six subfunctors, nor that every deformation retains a direction.

## Contribution and scope

The unrestricted 576-dimensional tangent space is 24 copies of the nontrivial regular U-module. Its six cyclic-symmetry subfunctors are formally smooth with tangent dimension 96, and any two intersect only in the constant deformation to all Artin orders. This sharpens full-U rigidity by constructing the lifting theory for surviving single-direction symmetry.

All calculations are structural character arithmetic and universal blowup charts. No selected actual source coefficient, point, derivative, kernel, matrix or rank is evaluated, and no large computation is used. This concerns abstract deformations of V51 with fixed specified subgroup actions and trivial base actions. It makes no assertion about algebraicity or convergence, about varying special-fiber group embeddings, about the original adjoint system or T75, or about formal machine verification.
