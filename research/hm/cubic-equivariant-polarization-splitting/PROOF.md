# Equivariant splitting of polarization classes and their symmetry sectors

Work over C. Put V=V51, L0=O_V(1), Gamma=Aut(V), and U=(Z/5)^2 subset Gamma. Let F and G be the marked polarized and abstract Artin deformation isomorphism-class functors respectively. Every group fixes the Artin base. A marked pair includes an identification of its central line bundle with L0. We work with classes, not with a groupoid or a chosen linearization of L0.

## Pinned inputs

All PRs belong to https://github.com/Akilleez-QA/read-em-and-weep.

- PR610, e4898406ed2552dd40e9695f9fda3d9f1d270301, and PR611, 12b28d33627cc0e8b283d142dc16439a51bb5e00: the normalization M=Bl_30(P4) has sixty double fibers. In each of the six eigenbasis pentads the twenty marks (i,j), i!=j in F5, are paired by tau(i,j)=(2i-j,3i-2j). The normalization sequence is 0 -> O_V -> nu_*O_M -> K -> 0, with K the direct sum of the sixty one-dimensional difference-of-values quotients. H0(O_M)=H0(O_V)=C, H1(O_M)=0, and h1(O_V)=60.
- PR624, 4fc9f009922b51369bfcaf4953919cb2f4c6c334: Gamma has order 3000 and every automorphism of V preserves the isomorphism class of L0. This does not supply an honest Gamma-linearization of L0.
- PR626, 8c25863b2c17de5c652fc2ced74163c0a6364a0a: the six pentads correspond to the six order-five subgroups G0 of U. On each, U/G0 acts by simultaneous translation of i,j; each mark has stabilizer G0. The abstract tangent module T=H1(Theta_V) is 24 Reg0(U), where Reg0 is the sum of the 24 nontrivial U-characters.
- PR627, 7c3f76f2e55c5cc0c3356972b5d7d676544c943a: the normalizer contains the involution J induced by e_i -> e_(-i), which conjugates U by inversion.
- PR632, fcb0300e36bd3b023e00a872c78207901392e7c8: H0(X_A,O)=A for every Artin deformation, so line-bundle automorphisms over a fixed underlying scheme are A*.
- PR634, 895e3a61098f50eccc0a4dc22b58606a28125355, research/hm/cubic-algebraic-deformation-slices/PROOF.md: F and G are prorepresented by complete regular local C-algebras R_F and R_G of dimensions 636 and 576. The forgetful map is formally smooth and its tangent sequence is 0 -> P -> T_F -> T -> 0, with P=H1(O_V). Marked scheme automorphisms are trivial; marked pair automorphisms are the liftable scalars 1+m_A.
- PR635, 71e35caf75753046d8508724f33ba463698718ae, research/hm/cubic-formal-symmetry-strata/PROOF.md: the Gamma-action on G is formally linearizable, and G^H is the smooth formal vector germ T^H for every subgroup H. In particular dim T^H=96 for order-five H subset U, while T^U=0. Underlying scheme actions extending specified central automorphisms are unique when they exist.

## 1. The action on pair classes does not require a linearization

Transporting a central scheme marking by gamma requires transporting the central line-bundle identification along an isomorphism between gamma's pullback of L0 and L0. Such an isomorphism exists by PR624. Any two choices differ by a nonzero constant, since Aut(L0)=C*. Multiplication of the deformed line bundle by that constant gives an isomorphism between the two resulting marked pairs. Thus the resulting transformation on F(A) is independent of the choice. This works naturally in A.

The chosen isomorphisms for two group elements need not compose coherently. Their discrepancy is again a constant scalar, and hence vanishes on marked pair isomorphism classes by the same argument. We therefore obtain a genuine Gamma-action on F, and F -> G is equivariant. The central class is fixed. The action on P is the natural action on H1(O_V): changing a line-bundle identification by a constant does not change the additive units sequence or its cohomology. Consequently the tangent exact sequence in the inputs is Gamma-equivariant. As in PR635, use inverse pullback for a left action on representing rings; the cotangent representations are dual to the tangent representations.

This argument asserts no coherent Gamma-action on the line bundle itself. It distinguishes the scalar-insensitive class functor from the scalar-sensitive linearization problem.

## 2. Compatible equivariant parameters

Write E_G=m_G/m_G^2 and E_F=m_F/m_F^2. The local continuous homomorphism i:R_G -> R_F induced by forgetting polarization gives the injective cotangent map

    0 -> E_G -> E_F -> P* -> 0.

Since Gamma is finite in characteristic zero, choose a Gamma-stable complement C to E_G in E_F. The quotient identifies C equivariantly with P*. Choose a C-linear lift s:C -> m_F of this complement and replace it by

    s_eq(c) = |Gamma|^(-1) sum_gamma gamma(s(gamma^(-1)c)).

This remains a lift and is equivariant. Independently choose equivariant parameters for R_G by the same averaging construction of PR635. The images under i of those parameters, together with s_eq(C), have classes forming a basis of E_F. The formal inverse function theorem for power-series rings now gives an isomorphism

    R_G completed-tensor_C completed-Sym_C(P*)  ->  R_F.

Here the R_G factor maps by i, and the second factor maps by s_eq after C=P*. More explicitly, after any power-series coordinates for the two regular rings, the displayed parameters have invertible linear coefficient matrix; solving successive homogeneous degrees gives a continuous inverse. Each construction is equivariant, so the isomorphism respects Gamma, its action on R_G, and its linear action on P*. This is a relative statement: it does not replace i by an unrelated homomorphism.

Dually, for every local Artin A, there is one noncanonical natural Gamma-equivariant identification

    F(A) = G(A) times (P tensor_C m_A),

under which forgetting is the first projection. Setting the second coordinate to zero gives a Gamma-equivariant section G -> F. Combining with PR635 gives compatible linearization of the entire forgetful morphism, not only the two individual formal germs. In particular every H-fixed abstract class admits an H-fixed polarization class, naturally after this choice. No algebraic or convergent equivariant section, Gamma-stable algebraic slice, or canonical additive structure on F is asserted.

## 3. The actual signed conductor representation under U

The map H0(O_M) -> H0(K) is zero: a constant has equal values on the two branches at every double value. The normalization sequence therefore canonically identifies P=H1(O_V) with H0(K). On a quotient fiber K_y, an automorphism preserving the two branches acts trivially; one exchanging them acts by -1. Thus the full Gamma-representation must initially be treated as a signed permutation module, not an ordinary permutation module.

Fix one pentad with stabilizer direction G0. Write j=i+d. The paired marks are (i,i+d) and (i-d,i-2d); tau changes d to -d. Quotienting the twenty marks by tau therefore gives two sets of five nodes, distinguished by d modulo sign in F5*/{+1,-1}. Translation of i acts transitively on each set. A nonzero translation cannot fix a pair: it cannot fix either mark, and a permutation of two marks induced by an element of odd order cannot exchange them. Thus each node orbit has length five and stabilizer exactly G0.

The same odd-order argument shows that this stabilizer cannot exchange the branches. Its action on the difference-of-values fiber is consequently trivial, with no additional character: residue-field constants are fixed. Choosing an orientation at one node and transporting it along its orbit is consistent because the stabilizer acts trivially. Each orbit therefore contributes Ind_(G0)^U(1). There are two such orbits for each of the six directions, whence

    P restricted to U = 2 sum_(|G0|=5) Ind_(G0)^U(1)
                      = 12 times 1 + 2 Reg0(U).

For the last equality, the trivial character occurs once in every induced summand, while each nontrivial character has exactly one order-five kernel and occurs in precisely that summand. Dimensions give 12+2*24=60, as required. This proves the absence of a sign twist for U from its actual paired-mark action; it makes no analogous assertion for Gamma.

Together with the equivariantly split tangent sequence this gives

    T_F restricted to U = 12 times 1 + 26 Reg0(U).

## 4. Fixed pair-class germs and their intersections

For every subgroup H of Gamma, the compatible splitting gives

    F^H(A) = G^H(A) times (P^H tensor_C m_A).

Invariants commute with tensoring the trivial finite-dimensional C-space m_A. Hence F^H is a smooth formal germ of dimension dim T^H + dim P^H. These are fixed-point subfunctors; their representing rings are the quotients by all h(r)-r, not the invariant subrings.

For U, P^U has dimension twelve and T^U=0. Thus F^U is a twelve-dimensional formal germ of polarization classes on the constant underlying abstract deformation. For an order-five H, precisely four nontrivial U-characters are trivial on H. Consequently

    dim P^H = 12+2*4 = 20,
    dim T_F^H = 96+20 = 116.

If H and K are distinct order-five subgroups, they generate U. A class fixed by both is fixed by U, over every Artin algebra. Therefore

    F^H intersection F^K = F^U,

as functors and as closed formal subschemes, and their common intersection has dimension twelve. This differs from the abstract fixed germs, whose intersection is only the constant point.

More precisely, after linearization let Q=(T_F)^U, dimension twelve, and let W_H be the sum of the nontrivial U-character spaces with kernel H. Then

    T_F = Q direct-sum (direct-sum_(|H|=5) W_H),
    dim W_H=26*4=104, and (T_F)^H=Q direct-sum W_H.

This simultaneously describes all six fixed germs and their common polarization directions to every Artin order. It does not assert that an arbitrary deformation lies in one of these fixed germs.

## 5. Inversion eliminates the common invariant polarization directions

The involution J of PR627 preserves each subgroup G0 of U. On that subgroup's eigencharacter affine line, conjugation by inversion makes its action i -> a-i for some a in F5; the possible translation a depends on the choice of origin and need not be zero. It therefore preserves each of the two node orbits indexed by d modulo sign.

To determine its action on a conductor difference, begin with the ordered branch pair given by the flag (i,i+d) and its partner (i-d,i-2d). The translation b=a-2i+d sends the partner flag to (a-i,a-i-d), precisely J applied to the first flag. The same translation sends the first flag to (a-i+d,a-i+2d), precisely J applied to the partner. Thus J, compared with transport by U on this node orbit, exchanges the two ordered branches. On the one-dimensional U-invariant subspace of the orbit's conductor module it consequently acts by -1. This argument works for both node orbits of every pentad, independently of a.

It follows that J acts as -Id on P^U, so P^Gamma=0. Since T^U=0 as well, the compatible equivariant linearization proves

    F^Gamma(A) = {the constant marked pair class}

for every local Artin A. Indeed the same assertion already holds for the subgroup generated by U and J. Thus U alone allows twelve pure-polarization formal directions, whereas retaining inversion with U eliminates all of them at every Artin order. This is a fixed-class statement and does not give a Gamma-linearization even of the constant line bundle.

## 6. What the fixed-class assertion does and does not linearize

If a pair class is H-fixed, its underlying scheme carries the unique H-action extending the prescribed central one. For each h, its line bundle is individually isomorphic to its h-pullback. Choices of these isomorphisms compose only up to units in A*. Their scalar defect is a group two-cocycle, and a coherent H-linearization exists exactly when its class in H^2(H,A*) vanishes. This follows directly by comparing triple compositions and observing that rescaling the chosen isomorphisms changes the defect by a coboundary. H acts trivially on A*, since it fixes the base and H0(X_A,O)=A.

There is no new infinitesimal obstruction beyond the central one: A* is canonically C* times (1+m_A), and logarithm identifies the second factor with the additive C-vector space m_A. Positive-degree cohomology of a finite group with C-vector-space coefficients vanishes by averaging. Hence H^2(H,A*) -> H^2(H,C*) is an isomorphism. The latter class is the central linearization obstruction of L0 under H. We neither assume nor claim its vanishing for Gamma or U. Thus an equivariant section of class functors cannot by itself be advertised as a functorial choice of honestly linearized line bundles.

For a cyclic order-five H there is a further distinction: H^2(H,C*)=C*/(C*)^5=0, since every nonzero complex number has a fifth root. Thus every H-fixed pair class does admit an H-linearization. Without choosing a central linearization this is not canonical, since it may be twisted by a character of H. Once a central H-linearization is specified, its lift exists and is unique up to an isomorphism of linearized line bundles: the obstruction and ambiguity groups with coefficients 1+m_A vanish in degrees two and one by the same logarithm and averaging argument. Scalar automorphisms still remain; uniqueness of an isomorphism is not asserted. No corresponding vanishing of the central obstruction for U or Gamma is inferred.

## Contribution and boundaries

The new result is a compatible full-Gamma formal splitting of polarization forgetting, followed by an exact U-representation calculation yielding six 116-dimensional fixed pair-class germs with common twelve-dimensional intersection, which inversion reduces to the constant fixed class. The final scalar-cocycle analysis separates these statements from genuine line-bundle linearizations. All results are conditional on the pinned geometric and representability inputs. No selected actual HM/source evaluation, large computation, generic-fiber automorphism claim, original Weil-class algebraicity conclusion, or proof-assistant verification is involved.
