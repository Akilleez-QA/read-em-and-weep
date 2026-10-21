# Algebraic slices with universal marked formal deformation classes

Work over C. Let V=V51 and L0=O_V(1). All deformation functors below are on local Artin C-algebras with residue C. Objects have a fixed identification of their special fiber with V, and pairs also have a fixed identification of the special-fiber line bundle with L0. Morphisms preserve those markings. Functor values are isomorphism classes, not groupoids.

## Pinned inputs

All PRs are in https://github.com/Akilleez-QA/read-em-and-weep.

- PR611, 12b28d33627cc0e8b283d142dc16439a51bb5e00: V is integral projective, H0(O_V)=C, h1(O_V)=60, H2(O_V)=0, and L0 is ample.
- PR614, 73fbf75838c91804ca637b5916d6aac217240958: all abstract Artin deformations are Zariski locally trivial; on every affine open their chosen local trivializations and identity-reducing automorphisms lift across small extensions. Abstract deformations are unobstructed, H0(Theta_V)=0 and h1(Theta_V)=576.
- PR615, 24bc9b741c287f8ac207bd9df4de4c07c50bea2f: the sheaf A_L0 of infinitesimal pair automorphisms is the Atiyah sheaf, with 0 -> O_V -> A_L0 -> Theta_V -> 0. Its H1 classifies first-order pair deformations.
- PR631, 4954b42e25592cf4b66a28d6a232fbe6b528f72e: for m sufficiently large, L0^m is very ample, H1(L0^m)=0, n=h0(L0^m), and the corresponding Hilbert germ is smooth of dimension D=n^2+635. Its forgetful map to powered pair classes is formally smooth, with tangent kernel pgl_n. The pair-to-abstract map is formally smooth, with tangent kernel H1(O_V).
- PR632, fcb0300e36bd3b023e00a872c78207901392e7c8: H0(X_A,O)=A for every Artin deformation; taking the m-th power induces an isomorphism between the original and powered marked pair class functors over the abstract functor. Scalar automorphisms remain.
- PR633, da25e13f7b55067e5da3008b1ab6fb3f2a38d18f, Section 5: an actual smooth pointed etale scheme chart (H',h') of that Hilbert germ carries a projective flat family Y with an actual relatively ample L, central marking L0, and actual L^m=O(1). Its dimension is D.

These inputs supply tangent exact sequences, for F=Def_(V,L0) and G=Def_V,

    0 -> pgl_n -> T_h'H' -> T_F -> 0,
    0 -> H1(O_V) -> T_F -> T_G -> 0,
    T_F=H1(A_L0), dim T_F=636, T_G=H1(Theta_V), dim T_G=576.

The first sequence for the original polarization follows by the power-functor isomorphism. No quotient by PGL_n is assumed.

## Theorem

After shrinking H', there are smooth pointed locally closed subschemes

    (S_576,s) subset (S_636,s) subset (H',h'),

of dimensions 576 and 636 respectively, with the following properties.

1. Restriction of (Y,L) to S_636 is an actual algebraic polarized family whose completed pointed base represents F: for every local Artin A, its pullback map from pointed Spec A -> S_636 to F(A) is bijective, naturally in A.
2. Restriction to S_576, after forgetting L, similarly represents G on the completed pointed base. It still carries the actual relatively ample L and its power relation, so chooses a polarization functorially on these abstract deformation classes.
3. Consequently the marked class functors are prorepresented by the completed local rings, noncanonically C[[x_1,...,x_636]] and C[[y_1,...,y_576]]. The nested inclusion induces a section of F -> G on Artin class functors, not a canonical section.

These are universal assertions for marked Artin isomorphism classes. They do not assert that either algebraic scheme is a fine moduli space over arbitrary bases, or that the pair deformation groupoid is represented by a scheme. In particular scalar pair automorphisms are not eliminated.

## 1. Automorphisms and the precise small-extension torsors

A small extension means A' -> A with kernel J and m_(A') J=0. All identifications of J-valued sheaves below follow from flatness.

First every marked automorphism of an abstract deformation X_A is the identity. Induct through a small-extension filtration of A. If its reduction over A is the identity, its difference from the identity over A' is an A'-linear derivation O_(X_A') -> J O_(X_A')=O_V tensor J. It thus belongs to H0(Theta_V) tensor J=0. The induction starts with the fixed central marking. This proof applies to arbitrary deformations, not only to a chosen family.

A marked pair automorphism therefore acts identically on X_A and multiplies its line bundle by a global unit. By PR632 these units are A*, and preservation of the special-fiber marking restricts them to 1+m_A. Every such scalar lifts to 1+m_(A') on every pair lift. Hence reduction maps of marked pair automorphism groups are surjective. Scalar automorphisms exist; their liftability, rather than their nonexistence, is the relevant fact.

Fix a deformation object E over A. Consider lifts to A' together with a specified isomorphism of their reduction to E, modulo isomorphisms compatible with that specified reduction. For abstract objects this set, when nonempty, is a torsor under H1(Theta_V) tensor J. For pairs it is a torsor under H1(A_L0) tensor J. Here is a direct gluing verification applicable to our singular V.

Choose a finite affine cover of V trivializing L0, with affine intersections. By PR614 each restricted scheme deformation is trivial, compatibly with any prescribed lower-order trivialization. On such an affine, a line bundle lifting a fixed trivial line bundle is trivial, and chosen lower-order trivializations lift: the units sequence has additive kernel O_V tensor J, whose H1 on the affine is zero, and units lift across a nilpotent ideal. Thus any two lifts of E are locally isomorphic by isomorphisms inducing the prescribed reduction. For pairs, the underlying local scheme comparison lifts by PR614 and the line comparison lifts by the preceding units argument.

Compare the two systems of transition maps after these local identifications. Their discrepancy is 1+c_ij, with c_ij a section of Theta_V tensor J in the abstract case, or A_L0 tensor J in the pair case. For pairs the central line transitions are retained: they give precisely the gluing law of A_L0, not that of a globally split O_V plus Theta_V. The small-extension condition kills products of discrepancies and all higher-order coefficients. The cocycle conditions imply the additive Cech one-cocycle condition in the stated sheaf. Changing local comparisons adds a coboundary. Conversely every such one-cocycle modifies the transitions to a lift, and a coboundary gives an isomorphism compatible with reduction. Affine intersections compute coherent H1. This proves freeness and transitivity, not merely the dimension of a tangent space. The corresponding affine deformation and automorphism principle is [Stacks 08SM](https://stacks.math.columbia.edu/tag/08SM), as used in PR614.

The lifts in question exist by abstract unobstructedness and, for pairs on a prescribed abstract lift, H2(O_V)=0. Finally remove the specified reduction identification and retain only the central marking, as in F and G. Any ambiguity in a reduction identification is a marked automorphism of E. For G there are none. For F each is a scalar which lifts to an automorphism of any given pair lift. Composing with that lifted scalar shows that changing the reduction identification leaves its class in the identified-lift torsor unchanged. Consequently each fiber F(A') -> F(A), and respectively G(A') -> G(A), is itself the torsor just described. This explicitly prevents a hidden automorphism quotient from invalidating uniqueness below.

## 2. Realizing tangent complements algebraically

We use an elementary smooth-slice fact. If B is smooth of dimension d at a C-point b and W subset T_bB has dimension e, choose d-e elements f_i of m_b whose classes in m_b/m_b^2 form a basis of the annihilator of W. Represent them by regular functions on a neighborhood. Complete their differentials to a cotangent basis. The resulting d functions give etale coordinates at b; equivalently the Jacobian is invertible there. Their first d-e zero equations define a smooth subscheme of dimension e through b with tangent W, after shrinking. This is the local-coordinate criterion for smooth schemes; see [Stacks 039P](https://stacks.math.columbia.edu/tag/039P). In particular this constructs an actual finite-type slice rather than just a formal linear subspace. The choice is existential and makes no evaluation of a selected source instance.

Choose a vector-space complement W_636 to pgl_n in T_h'H'. Apply the fact to obtain S_636 whose tangent maps isomorphically to T_F. Inside T_sS_636 the inverse image K of H1(O_V) has dimension 60. Choose a complement W_576 to K and apply the fact within S_636 to obtain the nested smooth S_576. Its tangent map to T_G is an isomorphism. Restrict the actual family and line bundle; flatness, projectivity, relative ampleness and the actual power isomorphism persist under these base changes. Shrink the schemes around their points whenever needed.

## 3. Why the slices are formally universal, not just tangent-isomorphic

We prove a general induction specialized to the torsors of Section 1. Let (S,s) be one of the smooth slices and E_S its indicated family. Write h_S(A) for pointed morphisms Spec A -> S and D for its target functor F or G. By smoothness, for each a in h_S(A), its A'-lifts are nonempty and form a torsor under T_sS tensor J: two ring-map lifts differ by a derivation to J, which factors through m_s/m_s^2. All these derivations yield lifts because J is square zero.

The induced map between this lift torsor and the torsor of deformation lifts of E_a is equivariant for

    KS_s tensor id_J: T_sS tensor J -> T_D tensor J.

This assertion involves the full small extension, not an assertion that a first-order calculation alone proves universality. To check it, compare the two base ring maps: their difference is the preceding derivation. In local trivializations of the pulled-back families, the change of transition maps is their differential applied to this derivation. Since m_(A') J=0, that differential is evaluated on the central fiber and is exactly the Cech cocycle defining KS_s. Coboundary changes of trivialization have no effect on its H1 class. This proves equivariance for arbitrary a and arbitrary small extension.

KS_s is an isomorphism by construction, so these maps of nonempty torsors are bijections. Induct on the length of A to prove h_S(A) -> D(A) bijective. At C both sets have their single marked central class. For a small extension A' -> A and any class over A', induction gives exactly one lower-order base map a. Pick an isomorphism identifying the lower-order class with E_a. The torsor bijection gives exactly one base-map lift inducing the desired upper-order class. Section 1 shows independence of this chosen isomorphism. For injectivity, two base maps with the same upper-order class have the same lower-order map by induction, and then are equal by the same torsor bijection. Every local Artin algebra admits such a small-extension filtration. The pullback transformation was natural throughout, so these bijections are natural.

Pointed maps from Artin spectra factor through the completed local ring. This proves the asserted prorepresentability directly, without assuming it or invoking a quotient theorem. Smoothness identifies the two completions with power-series rings of their respective dimensions.

## 4. A compatible choice of polarization for every abstract formal family

The nested inclusion S_576 -> S_636, composed with the two just-proved natural bijections, gives a natural transformation sigma:G -> F. Forgetting the line bundle after this inclusion is exactly restriction of the same underlying family on S_576, whose classifying transformation is the isomorphism with G. Thus the composite G -> F -> G is the identity. This choice depends on the slices and is not a canonical polarization assignment. It is not a claim that a fixed abstract deformation has only one polarization: its other choices still have the 60-dimensional Picard directions.

In particular a compatible sequence of marked abstract Artin deformations has compatible unique classifying base maps into the completion of S_576. Pulling back L supplies compatible polarization classes, realized by the pulled-back actual line bundle family. Arbitrary formal arcs into this completed base need not be algebraic or convergent. The conclusion is instead that a single algebraic family has the universal marked formal germ. This improves individual finite-jet curve realization without claiming algebraization of every arc.

## Boundaries and contribution

The new dependency is an actual algebraic realization of the universal marked formal germs, with a noncanonical formal section of the polarization-forgetting map. Scalar pair automorphisms remain, and no unmarked quotient by Aut(V), global moduli-space construction, uniqueness of the algebraic slices, generic-fiber automorphism assertion, recovery of the original ten sections, or identification with original HM/source deformations is asserted. No selected HM/source coefficient, point, matrix, derivative or rank evaluation and no large computation occurs. This is an authored mathematical argument conditional on the pinned inputs, not proof-assistant verification; it does not resolve the original full-adjoint or Weil-class algebraicity problem.
