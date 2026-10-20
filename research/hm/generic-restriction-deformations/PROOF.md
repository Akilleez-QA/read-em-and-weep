# Actual unobstructedness of generic HM restrictions

## Theorem and scope

Work over C. Let F be the normalized Horrocks–Mumford bundle on P⁴, B=End₀F. Let X=Xₚ be a smooth quintic with Q(p)≠0, where Q is the determinant quadric in ../quintic-restriction-jump-loci/PROOF.md and NONZERO-COROLLARY.md. Put E=F|X.

1. The projective stabilizer of F is finite. This is proved below; it is not inferred from the existence of its finite normalizer subgroup.
2. The algebraic family g↦g*F, g∈PGL₅, has Kodaira–Spencer isomorphism sl₅→H¹B. F has a smooth 24-dimensional miniversal deformation base although h²B=2.
3. On the FIXED variety X, the algebraic family g↦(g*F)|X has Kodaira–Spencer isomorphism sl₅→H¹End₀E. The ordinary bundle deformation functor and fixed-determinant deformation functor of E are formally unobstructed. Their miniversal base is Spf C[[t₁,…,t₂₄]], although Ext²(E,E) has dimension 24.
4. More concretely, every deformation over a local Artinian C-algebra, with special fiber E, is induced up to isomorphism by the completed group family. The same holds for F.

These assertions concern ordinary commutative-base deformations of the bundle on a fixed variety. They do not calculate the original mixed-source obstruction, arbitrary Massey products, constrained deformations, or deformations on the determinant quadric. Nor do they imply vanishing of the entire derived deformation complex.

## 1. Precise inputs

The audited restriction/scalar results cited above supply h¹B=24, h²B=2, simplicity of F and E, and, for Q(p)≠0, the isomorphism

    H¹(P⁴,B) → H¹(X,B|X),

with both spaces of dimension 24. They also give H¹O_X=H²O_X=0. The analogous scalar groups vanish on P⁴.

The following classical HM inputs suffice for the stabilizer argument: N⊂SL₅ acts on F; the trace-zero representation sl₅ is irreducible for N; h⁰(F(3))=4 and h⁰(F(t))=0 for t<3. Horrocks–Mumford, Topology 12 (1973), 63–81, §1 p.66 proves the representation assertion, §2 constructs the equivariant bundle, and §4 computes the section spaces: printed p.73 equation (4.11) and p.74 cohomology table (their unnormalized bundle is F(3)). Primary source:

https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

The independent numerical source h¹End F=24 is Decker–Schreyer, J. reine angew. Math. 382 (1987), 215–220, unnumbered proposition p.218; the source verification and exact page link are ../hm_primary_source_verification.md.

## 2. An intrinsic proper subspace forces the full stabilizer finite

Set G=F(3), so det G=O(5), and define

    W = image(Λ²H⁰G → H⁰(det G)) ⊂ S₅=H⁰O(5).

Choosing det G≅O(5) changes this image by a scalar, hence does not change W. Its dimension is at most 6, whereas dim S₅=126. We need only that W≠0, not its exact dimension.

If W=0, the evaluation image H⁰G⊗O→G has generic rank one. Its saturation L in G is rank-one reflexive: a saturated subsheaf of a locally free sheaf with torsion-free quotient has depth at least two at points of codimension at least two, hence is reflexive. On smooth P⁴ such an L is a line bundle O(a). All four sections factor through L. If a<0 there are no sections; if a=0 there is at most one. If a>0, the inclusion O(a)→G gives a nonzero section of F(3−a), contradicting the input vanishing. Thus W≠0.

Let K⊂PGL₅ be the scheme-theoretic stabilizer of W in the Grassmannian of dim W subspaces of S₅. The action on S₅ is well-defined: the central μ₅ of SL₅ acts trivially in degree five. K is a closed finite-type algebraic subgroup. Intrinsic construction and N-equivariance give image(N)⊂K. Hence Lie K⊂sl₅ is an N-invariant linear subspace. Irreducibility says it is either zero or all sl₅.

The second case is impossible. In characteristic zero a closed algebraic subgroup with full Lie algebra contains the connected group PGL₅. It would follow that W is invariant under SL₅. But Sym⁵(V*) is an irreducible SL₅ representation, and 0<dim W≤6<126. Consequently Lie K=0, and K is finite (indeed reduced in characteristic zero).

Any projective transformation h with h*F≅F also satisfies h*G≅G and preserves the intrinsic wedge image W, because the induced determinant isomorphism is unique up to a scalar. Therefore the actual projective stabilizer of F is contained in K and is finite. This does not identify its exact order or assert it equals image(N).

## 3. The infinitesimal orbit is an isomorphism

Consider the action map a:PGL₅×P⁴→P⁴ and the bundle a*F. Its derivative at the identity is

    κ:sl₅ → H¹(P⁴,End F)=H¹B.

We explicitly check injectivity, rather than relying only on set-theoretic stabilizers. Suppose v∈ker κ. Pullback by the corresponding dual-number point g of PGL₅ gives a bundle g*F isomorphic to the constant F over C[ε]/(ε²). Lift g uniquely near the identity to SL₅, which supplies the standard O(3) linearization, and twist by O(3). No global PGL₅-linearization of O(3) is being assumed. Global sections of this particular group-pullback family commute with this base change, since the action over the parameter base is an automorphism of the product and the constant family has section module H⁰G⊗C[ε]. An isomorphism with the constant family therefore makes its wedge-image submodule the constant W, up to an invertible scalar from the determinant identification. Equivalently the derivative at the identity of the orbit map PGL₅→Gr(dim W,S₅) vanishes on v. Thus v∈Lie K=0.

Since dim sl₅=h¹B=24, κ is an isomorphism. This is an intrinsic argument using section spaces, not an evaluation of a selected HM multiplication matrix.

Restriction of a*F to PGL₅×X is an algebraic family on the fixed X. A transformation g need not preserve X: its member is the bundle (g*F)|X on the original X. Functoriality of first-order deformation classes makes its Kodaira–Spencer map the composite

    sl₅ --κ→ H¹B → H¹(B|X).

The second arrow is an isomorphism for Q(p)≠0, hence so is the composite.

## 4. Why a smooth tangent-complete family kills ALL ordinary obstructions

Here is a direct Artinian argument, avoiding the incorrect implication that matching tangent dimensions alone proves smoothness.

Let Y be a fixed proper C-variety, E₀ a vector bundle on Y, and let a family over a smooth pointed scheme (T,t) have surjective Kodaira–Spencer map T_tT→Ext¹(E₀,E₀). Then the formal family is formally versal on isomorphism classes, and Def(E₀) is formally smooth.

Indeed use induction on the length of an Artinian local algebra A. Choose a small quotient A→A₀ with kernel I killed by the maximal ideal. For a deformation E_A, induction gives a map Spec A₀→T specializing to t and an isomorphism between its induced family and E_A|A₀. Smoothness of T lifts the map to Spec A→T, giving one lift of that same identified A₀-object. The difference between this lift and E_A is an element of Ext¹(E₀,E₀)⊗I. Changing the parameter lift by an element of T_tT⊗I changes this difference by the Kodaira–Spencer map. Surjectivity therefore removes the difference. This proves every Artinian deformation is induced by the family.

For any small extension A'→A and any E_A, first represent E_A by a parameter over A as just proved, then lift that parameter by smoothness of T. Its induced family is the required lift of E_A. Factoring an Artinian surjection into small extensions proves formal smoothness. The argument also allows a prescribed parameter over A: the same difference correction proves the smoothness of the map from the formal parameter functor to Def(E₀).

The lift-difference torsor is the standard module-deformation theorem, Stacks Project Lemma 91.4.3 (08L7), together with its flat-family application in §91.6. For vector bundles it can equally be checked on an affine trivializing cover: ratios of two lifted transition systems are 1+c_ij with c_ij∈End(E₀)⊗I; the cocycle equation and changes of trivialization give respectively Čech cocycles and coboundaries. The same calculation identifies change of parameter with κ⊗I.

https://stacks.math.columbia.edu/tag/08L7
https://stacks.math.columbia.edu/tag/08KW

Apply this with T=PGL₅ and E₀=F or E. Its formal completion is a 24-variable power-series formal scheme, and the tangent map is an isomorphism, so it is a miniversal family (smooth map on deformation functors with tangent isomorphism). In particular a minimal hull has no nonzero equations.

A ring cross-check: write any minimal hull R=C[[x₁,…,x₂₄]]/J. A compatible classifying map R→C[[t₁,…,t₂₄]] exists by the smooth lifting property of the hull, successively over powers of the maximal ideal. The composite from C[[x₁,…,x₂₄]] has invertible linear term, hence is an isomorphism of power-series rings. Its kernel is zero, so J=0. This explains why Ext²≠0 does not contradict the conclusion.

## 5. Determinants, automorphisms, and algebraic meaning

On Y=P⁴ or X, H¹O_Y=H²O_Y=0. Every infinitesimal deformation of the determinant is isomorphic to the constant determinant, uniquely as an isomorphism class; this follows inductively from 1+I O_Y≅I O_Y. Adding a specified determinant isomorphism does not alter the deformation parameter space. A change of determinant trivialization by a unit congruent to 1 is realized by a scalar automorphism: every such unit has a square root in an Artinian C-algebra.

For an actual algebraic family carrying a determinant identification, replace the parameter PGL₅ by SL₅: its standard linearization of O(−1) identifies the determinant of the pullback family with the constant determinant. SL₅→PGL₅ is finite étale and induces an isomorphism of completions at the identity, so this does not change any tangent or formal argument. Thus the preceding unobstructedness and miniversal dimension apply also to fixed determinant. Unrestricted simple bundles have scalar automorphism group G_m; fixing an identification of the determinant leaves μ₂. For marked infinitesimal deformations (identification of the special fiber fixed), there are no nontrivial determinant-preserving automorphisms reducing to identity. The unmarked fixed-determinant moduli stack still has μ₂ inertia; the unrestricted stack has G_m inertia. One must not call the latter a 24-dimensional stack merely because its miniversal parameter space has dimension 24 (its local stack dimension is 23). The fixed-determinant stack has local dimension 24.

The family itself is algebraic, not merely a formal construction. The bundle stack is an open substack of the algebraic coherent-sheaf stack, locally of finite presentation; see Stacks Project §§99.5 and 108.4. Formal unobstructedness therefore gives smoothness of this stack near the point by the infinitesimal smoothness criterion, precisely Stacks Project Lemma 107.2.7 (0DQT); Lemma 107.2.6 there gives smoothness near the identity of the algebraic formally versal family map to the stack. A local rigidification by scalar automorphisms, or the usual local moduli space for simple bundles, has smooth 24-dimensional deformation germ. No stability of E is used or asserted, and no particular global coarse GIT moduli space is asserted without its existence hypotheses. The stable ambient bundle has the usual smooth 24-dimensional coarse moduli germ.

https://stacks.math.columbia.edu/tag/08KA
https://stacks.math.columbia.edu/tag/0DLX
https://stacks.math.columbia.edu/tag/0DQT

Algebraicity here means that the miniversal formal family is supplied by an actual finite-type algebraic family. It does not mean that every arbitrary formal parameter power series comes from a convergent or algebraic curve, nor that all global deformations are projective transforms, nor that a universal bundle descends to a global coarse moduli space.

## 6. Obstruction interpretation and boundary

The ambient obstruction space H²B remains two-dimensional. On X with Q(p)≠0 the obstruction space Ext²(E,E) remains 24-dimensional. Every actual obstruction to an ordinary small-extension lift vanishes, since a lift has just been constructed. Consequently a minimal ordinary Kuranishi equation system has zero ideal. This is strictly stronger than a tangent-space calculation.

No claim is made at Q(p)=0: there the group family supplies 24 independent tangent directions, while the full tangent dimension is 25 or 26. Nor does this theorem imply that every ordered Yoneda/Massey expression vanishes, that the full controlling dg algebra is formal, or that mixed/source-dependent lifting problems are unobstructed. The scope is the ordinary bundle deformation functor on the fixed ambient space or on a fixed smooth quintic off Q.

No source/cofactor selected matrix, rank, polynomial-instance, or numerical coefficient evaluation was performed.
