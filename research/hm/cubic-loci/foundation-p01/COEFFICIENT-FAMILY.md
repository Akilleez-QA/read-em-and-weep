# A seventy-nine-dimensional full coefficient family

## Theorem and conditional premise

Let k be a field of characteristic zero, let C be the smooth projective elliptic curve with affine equation y²=z³−z and origin O at infinity, and set

    X=C⁴,   Y=(P¹)⁴,
    N=⊠ᵢ O_C(O),   L=O_Y(1,1,1,1).

Let q:X→Y be the product of the degree-two morphisms defined by the complete linear series |2O|, with coordinates (1:z) in the finite divisor frame. Fix the resulting identification q*L≅N². Let

    v=(v₀,…,v₄)=(1,e₁(z),e₂(z),e₃(z),e₄(z))

be the five global sections of N² obtained as the coefficients of the product of the four binary linear forms. Equivalently they are pulled back from five sections of L. They generate L on Y and N² on X, and define f:X→P⁴.

Assume the accepted four-term locally free presentation of the specified bundle H on P⁴,

    5O(−1) → 15O → 10O(1) → 2O(2),

in degrees −1,0,1,2, whose sole cohomology is the locally free bundle H in degree zero. Assume its first differential is the literal homogeneous γ recorded in Section 5 below. This is the exact-presentation premise of the target-projective variation argument; in particular the exact-presentation theorem is supplied by the preceding normalizer foundation, not by a historical contraction certificate. The name “HM” alone, without this specific exact presentation and first differential, is not the hypothesis.

Put W=H⁰(Y,L). There is a nonempty open subscheme

    U ⊂ P(W⁵),   [v]∈U,   dim U=79,

parameterizing generating five-tuples modulo a common scalar. The universal maps f_s:X→P⁴ give a geometric bundle family

    E_s=N⊗f_s*H

on the fixed variety X, with E_[v]=E=N⊗f*H. Its Kodaira–Spencer map at [v]

    κ:T_[v]U → Ext¹_X(E,E)

is injective. Thus this family supplies a 79-dimensional subspace of genuine background bundle-deformation classes. In particular dim_k Ext¹_X(E,E)≥79 under the stated premise.

This family exhausts the generating five-tuples for the fixed polarization line bundle N²: the pullback map H⁰(Y,L)→H⁰(X,N²) is an isomorphism. The statement does not include deformations of the polarization in Pic(X), variations of X, a quotient by source automorphisms, or a claim that the entire bundle-deformation space is 79-dimensional.

## 1. Sixteen sections, and why none are missing upstairs

On C, the line bundle O_C(2O) has degree 2. Riemann–Roch on the genus-one curve and Serre duality give

    h⁰(C,O_C(2O))=2,   H¹(C,O_C(2O))=0.

Indeed the canonical line bundle is trivial, and a negative-degree line bundle has no nonzero section. The rational functions 1 and z represent linearly independent global sections of O_C(2O): z has its sole pole at O, of order 2. They therefore form a basis. The corresponding complete linear series is basepoint-free: away from O the section 1 does not vanish in its divisor frame, and at O the section z is nonvanishing in the local frame for O_C(2O).

The degree-zero Künneth isomorphisms give

    H⁰(Y,L)=⊗ᵢ H⁰(P¹,O(1)),
    H⁰(X,N²)=⊗ᵢ H⁰(C,O_C(2O)).

Each factor pullback is an isomorphism carrying the homogeneous coordinate basis to (1,z). Their tensor product q* is consequently an isomorphism, and both spaces have dimension 2⁴=16. Each degree-two map C→P¹ is surjective, so q is surjective. A tuple of sections of L generates L if and only if its pullback generates N²: a common geometric zero downstairs has a geometric preimage upstairs, and a generating tuple remains generating after pullback. In the common finite divisor frame, a basis consists of the squarefree monomials ∏_{i∈I}z_i for I⊆{1,2,3,4}. This is a statement about global sections of the indicated line bundle, not a claim that these rational functions are globally regular functions on X.

The five original sections v₀,…,v₄ are linearly independent. In the squarefree-monomial basis, v_j is the sum of the monomials indexed by subsets of cardinality j. These five supports are nonempty and pairwise disjoint.

## 2. The open parameter space and its universal map

Use the convention that P(W⁵) parameterizes one-dimensional subspaces of W⁵. Set V=W⁵, so dim V=80 and dim P(V)=79. For a point [s] with s=(s₀,…,s₄), the condition that the sections generate L is independent of the nonzero scalar used to represent [s].

On Y×P(V), let p_Y and p_P denote the projections. The tautological line in V defines five universal sections of

    p_Y*L ⊗ p_P*O_P(V)(1).

Let Z be their common zero subscheme. This is closed. The projection Y×P(V)→P(V) is proper, since Y is projective over k, so its image |Z| is closed. Its complement U is exactly the locus of five-tuples with no common geometric zero, or equivalently of five-tuples generating L. This proves openness without relying on a coefficient specialization or an evaluated rank test.

The original tuple belongs to U. At any geometric point of Y each of the four binary linear forms is nonzero. Their product is a nonzero binary quartic because a polynomial ring over a field is an integral domain. Its five coefficients therefore cannot all vanish.

Over Y×U the universal sections generate the indicated invertible sheaf, hence define a morphism

    F_Y:Y×U→P⁴,
    F_Y*O_P⁴(1)≅p_Y*L⊗p_U*O_U(1).

Composing with q×id_U gives F_X:X×U→P⁴ and

    F_X*O_P⁴(1)≅p_X*N²⊗p_U*O_U(1).

The bundle family is globally well defined as

    𝓔=p_X*N⊗F_X*H.

To work with fixed presentation terms, choose a linear functional ℓ:V→k with ℓ(v)=1 and restrict to the affine chart ℓ(s)≠0. The unique normalized representative ℓ(s)=1 trivializes O_U(1) there, compatibly with the chosen tuple v at the base point. On this chart the pulled-back, N-twisted presentation has fixed terms

    K_s: 5N⁻¹ → 15N → 10N³ → 2N⁵,

pulled back from X. Its sole cohomology is E_s. To justify arbitrary pullback, the assumed bounded locally free presentation with sole locally free cohomology is locally split into that cohomology and contractible complexes. Pullback preserves such a splitting. No flatness assumption on F_X is needed.

This also explains the scope of “all maps with the fixed polarization.” A morphism X→P⁴ with an identification of its pullback of O(1) with N² is the same as a generating ordered five-tuple of sections of N². Changing that identification multiplies the whole tuple by an element of k×, because H⁰(X,O_X)=k. Thus forgetting the choice of identification gives precisely U(k). The same description works locally on a parameter base when the relative polarization is isomorphic to the fixed N², up to a line bundle from that base. It does not cover a polarization moving nontrivially in Pic(X).

## 3. Tangents and the strict-lift consequence of zero Kodaira–Spencer class

Let R=k[ε]/(ε²). After choosing the representative v, the projective tangent space identifies as

    T_[v]U ≅ V/kv.

Intrinsically it is Hom(kv,V/kv); the displayed identification sends a homomorphism to its value on v. A tangent is represented by an arbitrary tuple

    δv=(δv₀,…,δv₄)∈H⁰(X,N²)⁵,

with representatives differing by a common scalar multiple cv. The corresponding family is obtained by substituting v+εδv into the homogeneous presentation. Every tangent lies in the generating locus because U is open and its closed point is [v].

For clarity, the strict-lift argument from the strict-lift proof included below applies unchanged to these arbitrary section variations. If K_0 and K_δ are the constant and varying complexes on X_R, their sheaf Hom complex in internal degree r is a direct sum of N_R^(2r), with −3≤r≤3. Elliptic-curve cohomology and Künneth imply:

- for r>0, N^(2r) has cohomology only in degree 0;
- for r<0, N^(2r) has cohomology only in degree 4;
- for r=0, the cohomological degrees range from 0 to 4.

These statements remain valid over R by flat base change from k. In the hypercohomology spectral sequence, no term has negative total degree; the sole position with total degree zero is (r,q)=(0,0). The negative internal degrees have r+q=r+4≥1. The only differential leaving (0,0) that can be nonzero is the first differential to (1,0), which imposes the strict chain-map condition. Higher incoming differentials originate in total degree −1, and higher outgoing differentials have negative cohomological degree. Global degree −1 sections vanish. Consequently strict global degree-zero chain maps identify bijectively with derived maps, and hence with bundle maps E⊗R→E_δ.

The four diagonal blocks of any such strict chain map have entries in H⁰(X_R,O)=R. The bijection is compatible with reduction to k. A bundle isomorphism reducing to identity_E therefore lifts uniquely to a strict chain map reducing to identity_K.

If κ([δv])=0, the first-order bundle deformation admits such an identity-reducing trivialization. Write its first two blocks as I₅+εQ and I₁₅+εP, where Q and P have entries in k. The first chain equation gives, with a consistent choice of map direction,

    δγ=Pγ−γQ.                                            (1)

There is no restriction on the constant matrices P,Q beyond this necessary equation. In particular, the argument covers bundle trivializations initially described by nonconstant local gauges.

## 4. The decisive reduction: arbitrary section variations become target variations

Write S=span_k(v₀,…,v₄)⊂H⁰(X,N²). Every entry of γ lies in S. Since P and Q are constant, every entry of Pγ−γQ also lies in S.

For each i=0,…,4 the literal differential has singleton row 10+i, with its sole nonzero entry γ[10+i,i]=v_i. Therefore

    δγ[10+i,i]=δv_i.

Equation (1) implies δv_i∈S for every i. By the established linear independence of v₀,…,v₄, there is a unique constant 5×5 matrix B such that

    δv_i=Σ_j B_ij v_j.                                   (2)

Thus every zero-class tangent in the full coefficient family reduces to exactly the symbolic target-variation problem already treated by the target sparse lemma. This deduction uses only membership in a five-dimensional subspace of global sections. It does not evaluate the source, a point, a matrix, or a polynomial instance.

## 5. The target sparse lemma, recalled with its proof

All subscripts below are modulo 5. The literal nonzero entries of γ are

    row i:       (column i+2, +v_(i+1)),
                 (column i+3, +v_(i+4));
    row 5+i:     (column i+1, −v_(i+3)),
                 (column i+4, −v_(i+2));
    row 10+i:    (column i, +v_i).

Each pair (column j, variable label l) occurs exactly once among these entries. In each double-entry row the labels are distinct; if one column is i, the label at the other column is not i.

Suppose (1) and (2) hold. In row 10+i, column j≠i, the expression δγ+γQ has only label v_i. Every double-entry row s has an entry in some column j≠i whose label l is not i: if neither column is i, use the distinctness of its labels; if one column is i, use the preceding support property. At that (column,label) pair, uniqueness forces P_(10+i,s)=0. Likewise the singleton row 10+j for j≠i forces P_(10+i,10+j)=0. Thus the whole right side Pγ in row 10+i has only its column-i term, a multiple of v_i. It follows that Q_ij=0 for j≠i and δv_i is a multiple of v_i. Hence Q and B are diagonal.

Now δγ+γQ in any row has support within that row's original support. The uniqueness of every (column,label) pair forces P to be diagonal as well. Write a_i=B_ii and q_i=Q_ii. The two double-entry row types give

    q_(j+1)−q_j = a_(j−1)−a_(j+2),
    q_(j+3)−q_j = a_(j+2)−a_(j+1).

Sum the first relation at j,j+1,j+2 and compare with the second. The result is

    a_j+2a_(j+1)−2a_(j+2)−a_(j+3)=0.

For the formal cyclic shift T this says

    (1−T)(T²+3T+1)a=0,   (T⁵−1)a=0.

The gcd of the two polynomials is t−1 in characteristic zero. A coefficient-only verification is as follows: for h=t²+3t+1 and Φ₅=t⁴+t³+t²+t+1,

    Φ₅ ≡ −5(3t+1) mod h,
    9h−(3t+8)(3t+1)=1,
    h=(t−1)(t+4)+5,
    Φ₅=(t−1)(t³+2t²+3t+4)+5.

These formal identities and Bézout give (T−1)a=0. All a_i are equal, so B=cI and δv=cv. This is the complete symbolic sparse argument; it contains no evaluated polynomial instance or computed rank.

## 6. Injectivity, dimension, and relation to the smaller families

A zero Kodaira–Spencer class forces δv=cv, which is zero in V/kv. Thus κ is injective. Conversely, a common scalar rescaling does not change the map to P⁴, and so gives the constant bundle family, as expected from the projective parameter space.

Since U is a nonempty open subscheme of P(V) and dim V=80,

    dim T_[v]U=79,   dim im κ=79.

The target-projective family is contained in this coefficient family by taking s=Gv. The 24 target directions are already contained in this 79-dimensional image; they must not be added to it again.

The theorem asserts injectivity at the original tuple [v]. It does not assert that every point of U has injective Kodaira–Spencer map, that the family is a moduli-space chart, that it is versal, or that Ext¹_X(E,E) has dimension exactly 79. It makes no assertion concerning star-module admission, residual/detector response, mixed Yoneda products, or additional structures on these bundles. The parameter ε is a background first-order family parameter, not a star-order parameter.

