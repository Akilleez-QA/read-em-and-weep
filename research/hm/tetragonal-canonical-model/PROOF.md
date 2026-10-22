# The actual Gram operator gives the tetragonal quotient a smooth (4,4) model

Status: independently mathematically reviewed (PASS), conditional on the pinned input; see REVIEW.md. Work over C. This is not a proof-assistant certificate. No selected HM coefficient, point, matrix, rank, or scan is evaluated.

## Inputs

Use the actual self-adjoint Gram operator and spectral module of [PR654](https://github.com/Akilleez-QA/read-em-and-weep/blob/f0c94ff7979652c094da3efaa11fea4629dbf59a/research/hm/gram-spectral-geometry/PROOF.md), commit f0c94ff7979652c094da3efaa11fea4629dbf59a, and the covers of [PR655](https://github.com/Akilleez-QA/read-em-and-weep/blob/b33a4f9c86a370ad4e96ba3cc1843ed9ef70bfe7/research/hm/spectral-deck-obstruction/PROOF.md), commit b33a4f9c86a370ad4e96ba3cc1843ed9ef70bfe7.

Write L=P1, E=V tensor O_L with dim V=3, and let b be the fixed nondegenerate symmetric form with respect to which M:E->E(4) is self-adjoint. Its characteristic polynomial is lambda^3-d, where d has twelve simple zeros. At these zeros M is regular nilpotent; elsewhere its three eigenvalues are distinct. The smooth spectral curve pi:S->L has lambda^3=d. The spectral line bundle B satisfies pi_*B=E, and T=B tensor pi^*O_L(-4) is nontrivial two-torsion. The associated connected etale double cover X_T->S has A4 normal closure Y->L. Every quotient Y/H for H of order three is a smooth genus-nine tetragonal curve over L; these quotients are isomorphic over L since the subgroups are conjugate.

The result below identifies that quotient with a concrete global construction from the actual M. It does not rely on a general Casnati--Ekedahl or Recillas theorem.

## 1. A global complete intersection and its generic fiber

In P(V) times L, where P(V) denotes lines, set

    q0(v)=b(v,v),
    q1(v,z)=b(v,M(z)v),
    Z={q0=q1=0}.

Their divisor classes are (2,0) and (2,4), respectively. The fixed conic Q={q0=0} is smooth because b is nondegenerate. Over C it is isomorphic to P1, and O_P(V)(1)|Q=O_Q(2). Thus Z is a divisor of bidegree (4,4) on Q times L.

No fiber q1|Q is identically zero. Otherwise the degree-two form q1 on that fiber would be a scalar multiple of q0, since the homogeneous ideal of a smooth plane conic in degree two is one-dimensional. Polarization and nondegeneracy of b would imply that M on that fiber is scalar. This contradicts distinct eigenvalues away from d=0 and regular nilpotence at d=0. Consequently Z->L is finite of degree four, flat: a nonzero degree-four equation on every P1 fiber is a relative effective Cartier divisor of constant length four.

Over an algebraic closure of C(L), the three distinct eigenspaces of the self-adjoint operator are mutually orthogonal and nonisotropic. In an orthogonal eigenbasis the two equations say that the three squared coordinates lie in the kernel of the two rows (1,1,1) and (a1,a2,a3), with the ai distinct. This kernel is spanned by (a2-a3,a3-a1,a1-a2), whose entries are all nonzero. There are exactly four projective choices of their square roots, all reduced. Thus the generic fiber is etale of degree four. This is a symbolic argument valid for every such self-adjoint operator, not an evaluation of an actual selected matrix.

## 2. The component double cover is exactly the actual T-cover

On S put A=pi^*O_L(4) and N=pi^*M-lambda Id. The symmetric A-valued form b(-,N-) has rank two at every point. Indeed its kernel has dimension one at distinct eigenvalues and at the regular-nilpotent branch fibers.

The evaluation map pi^*pi_*B -> B is surjective. The spectral-module action implies that its composite with N is zero. Dualizing evaluation and using b to identify pi^*E with its dual gives an inclusion

    B^{-1} -> pi^*E

whose image is ker N. The rank-two statement shows equality as subbundles, including above ramification. Let U=pi^*E/B^{-1}. Then det U is isomorphic to B, and b(-,N-) descends to a nondegenerate A-valued binary quadratic form on U.

Let X_comp->S parametrize its two isotropic lines. It is finite etale of degree two. These two lines correspond exactly to the two line components of the singular plane conic b(v,Nv)=0: each component is the projectivization of the inverse image in pi^*E of an isotropic line in U.

For completeness, the double-cover line bundle is computed directly. With p:P_lines(U)->S, the isotropic divisor has exact sequence

    0 -> O_p(-2) tensor p^*A^{-1} -> O -> O_X_comp -> 0.

Since R^1 p_*O_p(-2)=det U and the trace splits off O_S in characteristic zero, its trace-free direct-image line is

    (det U) tensor A^{-1} = B tensor pi^*O_L(-4) = T.

Nondegeneracy makes the multiplication on this line a nowhere-zero square trivialization. On the connected projective complex curve S, two such trivializations differ by a nonzero complex scalar, which has a square root. Hence X_comp->S is isomorphic to X_T->S, not just a double cover of the same degree or genus. In particular X_comp is connected.

## 3. Identification with the order-three A4 quotient

Over the geometric generic point of L, the pencil q1-lambda q0 has three singular conics, given by det(M-lambda Id)=0. There is no singular member at infinity because q0 is nonsingular. Each rank-two singular conic is a pair of distinct lines. Each line contains exactly two of the four base points: restriction of q0 to the line has degree two; the four base points are distinct; and none is the conic vertex, since that vertex is a nonisotropic eigenline. Thus the three singular members give the three partitions of the four points into pairs, and their six individual line components give the six two-element subsets.

This correspondence is Galois-equivariant. The action of S4 on the six two-element subsets is faithful, so the splitting field of this degree-six component cover equals the splitting field of the degree-four generic fiber of Z. Section 2 identifies the degree-six cover with X_T->L, whose normal closure is the A4 extension Y->L by the pinned input. Therefore the generic permutation group of Z is a subgroup of S4 isomorphic to A4. The unique order-twelve subgroup of S4 is its alternating subgroup; its action on four letters is transitive and its point stabilizers have order three. Hence the generic fiber of Z is a field and its normalization is isomorphic over L to Y/H for an order-three subgroup H. This establishes the desired identification without presupposing smoothness of Z or of a singular-conic resolvent model.

## 4. Smoothness follows from genus, with no branch-fiber calculation

The divisor Z on the smooth surface Q times L has no embedded associated points, since it is Cartier. Every component dominates L, because the morphism to L is finite and there is no vertical divisor component. Its generic fiber is integral and reduced by Section 3. These facts imply that Z itself is integral and reduced.

Adjunction on P1 times P1 gives arithmetic genus

    p_a(Z)=(4-1)(4-1)=9.

Its normalization is Y/H and has genus nine by PR655. For an integral projective curve the length of the normalization quotient equals the arithmetic genus minus the normalization genus. Here that length is zero, so Z is normal. A normal curve over C is smooth. Thus Z itself is the tetragonal quotient, and its degree-four map to L has exactly the twelve (3,1) branch fibers already proved in PR655.

In particular no singular or double fixed conic is hidden in the construction: the fixed conic is the original nondegenerate Gram pairing, and smoothness of the complete intersection follows without any chosen branch coordinate or selected actual matrix normal form.

## 5. Canonical twists and the bundle of quadrics

On Q times L the two coordinates have the usual P1 degrees. Adjunction gives

    omega_Z = O_Z(2,2),
    omega_{Z/L} = O_Z(2,4).

Equivalently in P(V) times L the relative dualizing line is O_Z(1,4). The degree-two Veronese embedding of Q followed by its product with L is precisely the relative canonical plane embedding: the relative residue sequence obtained by twisting the divisor sequence on Q times L by O(2,4) is

    0 -> H^0(Q,O_Q(2)) tensor O_L(4)
      -> h_*omega_{Z/L} -> O_L -> 0.

By relative duality its last map is dual to the unit O_L->h_*O_Z, up to a nonzero scalar depending on the adjunction trivialization. Thus its kernel is the Tschirnhausen bundle E_h=O_L(4)^3, and its evaluation is the displayed plane embedding. This also agrees with the exact splitting in PR655.

Let H denote the relative canonical plane hyperplane, so H=O_P(V)(1) tensor O_L(4). The original quadrics have classes

    2H-8f and 2H-4f,

where f is the base class. Consequently the bundle of quadrics, defined as the kernel of Sym^2 E_h -> h_*(omega_{Z/L}^2), is

    F = O_L(8) plus O_L(4).

Indeed the complete-intersection ideal has Koszul generators q0 and q1 of classes (2,0) and (2,4); twisting by (2,8) and pushing to L gives precisely these two summands, with no contribution from the Koszul relation: its plane factor is O_P2(-2), whose cohomology vanishes in every degree. The same vanishing gives surjectivity onto h_*(omega_{Z/L}^2). This proves the splitting from the actual equations, rather than guessing it from the normalized cubic resolvent.

The other projection Z->Q is also finite of degree four, since Z is integral of bidegree (4,4), and provides a second tetragonal pencil. The two maps together are the closed embedding Z into Q times L; no uniqueness claim for tetragonal pencils is made.

## 6. The gonality is exactly four

The displayed degree-four projections show gonality at most four. Suppose there were a map f:Z->P1 of degree n=2 or 3. Let e be the degree from Z to the normalization of its image under (f,h). Function-field degrees show e divides both n and 4. If e=1, the image is an integral curve of bidegree (4,n) on P1 times P1, so its normalization has genus at most its arithmetic genus 3(n-1), at most six. This contradicts g(Z)=9. The only remaining case is n=e=2, which gives a nontrivial intermediate degree-two field in the degree-four extension defined by h. By Galois correspondence in its A4 normal closure, this would require a subgroup of order six containing the order-three point stabilizer. There is no order-six subgroup of A4: such a subgroup would be index two and give a nontrivial homomorphism A4->C2, while A4 is generated by its three-cycles, all of which must map trivially. A degree-one map is also impossible for a genus-nine curve. Hence gonality(Z)=4.

## Contribution and limits

The genus-nine quotient is now explicitly the smooth (4,4) curve cut out by the fixed Gram conic and its actual M-quadric. Its singular-conic component cover is exactly the original spectral T-cover, not an unrelated cover with matching dimensions. The calculation resolves the relative canonical twists and gives F=O(4) plus O(8), as well as a second degree-four pencil and exact gonality four.

No extra A5 action, Prym identification, or torsion transfer to the original genus-four support D is needed or claimed. No actual R-class, final contraction, second-symbol quotient, third Bockstein, source-instance evaluation, or algebraicity claim is resolved. Those remain separate dependencies.
