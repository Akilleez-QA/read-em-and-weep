# Rank is constant on the hypothetical twenty-five-line orbit

## Statement and precise dependencies

Work over C. Retain the five-dimensional Schrödinger representation V of H₅, A=H₅/Z(H₅)≅F₅², and the projective normalizer subgroup N with N/A≅SL₂(F₅), acting on A in the standard way. Assume the conclusions and hypotheses of ../rank-three-curve-constraints/PROOF.md. In particular, if the reduced curve part Γ₃ of Z₃ is nonempty, its components are exactly twenty-five lines, forming one free A-orbit and one N-orbit.

Also invoke the previously established finiteness of Z₂; the weaker hypothesis actually needed below is that each of these lines has generic residual rank three. This is an additional dependency, not a consequence of the twenty-five-line classification alone. The N-equivariant linear matrix b has size 20 by 15 and satisfies rank bᵤ=4+rank Qᵤ.

**Theorem.** On every one of the hypothetical twenty-five lines L, rank Qᵤ=3 at every point [u]∈L. Equivalently, rank bᵤ=7 everywhere on L. Thus none of these lines meets Z₂.

No existence of these lines is asserted. No actual source map or numerical tensor instance is evaluated. The proof uses only the abstract Heisenberg normalizer and its Schrödinger representation.

## 1. Each line stabilizer is a complement

Fix a component L and let Γ=N_L. Since A acts freely on the component set, Γ∩A=1. Since the N-orbit of L has twenty-five elements,

    |Γ|=|N|/25=120.

Consequently Γ maps isomorphically onto N/A=G=SL₂(F₅), and N=AΓ. In particular Γ is a complement to A.

We will prove that Γ acts on L through a faithful A₅-action. It is essential to prove this, rather than assume that a setwise line stabilizer acts nontrivially on the line.

## 2. The canonical projective splitting and two explicit operators

Choose ζ a primitive fifth root of unity and a Schrödinger basis e_j indexed by j∈F₅. Put

    X e_j=e_(j+1),     Z e_j=ζ^j e_j,
    W_(a,b)=ζ^(ab/2) X^a Z^b,

where exponents are interpreted in F₅. Direct multiplication gives

    W_(a,b) W_(c,d)=ζ^((bc−ad)/2) W_(a+c,b+d).

Thus every s∈SL₂(F₅) acts on this abstract Heisenberg group by W_v↦W_(sv), fixing its center. By uniqueness of the irreducible five-dimensional Heisenberg representation with the chosen nontrivial central character, there is an invertible intertwiner R_s, unique up to scalar, with

    R_s W_v R_s⁻¹=W_(sv).

The classes [R_s] form a homomorphism G→PGL(V), and it is injective because its conjugation action on A is the faithful standard action. Write G₀ for its image. Moreover A∩G₀=1.

For completeness, this splitting is the relevant splitting of N, not a potentially different normalizer. Given any projective transformation n normalizing A and inducing s, a linear lift satisfies

    n W_v n⁻¹=χ(v) W_(sv)

for a character χ:A→μ₅. The scalar is a fifth root because W_v⁵=I, and the multiplication formula makes it a character. The nondegenerate commutator pairing identifies A with its character group, so multiplication of n by a suitable W_a removes χ. Uniqueness of the intertwiner then gives n∈A G₀. Hence the full projective normalizer is A⋊G₀. The given subgroup N has this same order 25·120 and is therefore that normalizer.

Only two elements of G₀ are needed. Define

    D e_j=ζ^(j²)e_j,     T e_j=e_(2j).

Direct calculation yields

    D W_(a,b) D⁻¹=W_(a,b+2a),
    T W_(a,b) T⁻¹=W_(2a,3b).

Both induced matrices have determinant one, so [D],[T]∈G₀ by the exact intertwining characterization. Crucially, their chosen linear representatives obey

    T D T⁻¹=D⁻¹,     D⁵=I,
    dim ker(D−I)=1.                                      (1)

Indeed 2⁻²=4=−1 in F₅, and j²=0 only for j=0. This avoids any need to choose a linear Weil representation or to determine scalar normalizations of an order-five lift in such a representation.

## 3. Every complement is A-conjugate to G₀

Use additive notation for A and identify N=A⋊G through Section 2. A complement is the graph of a cocycle c:G→A:

    c(gh)=c(g)+g c(h).

Let z=−I∈G. It is central and acts on A by minus the identity. Comparing c(zg) and c(gz) gives

    c(z)−c(g)=c(g)+g c(z),
    2c(g)=(1−g)c(z).

Since 2 is invertible in F₅, set a=c(z)/2. Then c(g)=a−g a, which means that the complement is aG₀a⁻¹. This proves the required conjugacy directly, without a coprime-order complement theorem.

After conjugating L and Γ by an element of A, we may therefore assume Γ=G₀.

## 4. The action on the line cannot be trivial

Let W⊂V be the two-dimensional vector subspace with P(W)=L. Suppose every element of G₀ fixes L pointwise. Since D and T stabilize W and [D] is trivial on P(W),

    D|_W=λ I_W

for some λ∈C*. Restricting the exact relation TDT⁻¹=D⁻¹ in (1) to W gives λ=λ⁻¹. Also D⁵=I gives λ⁵=1. Hence λ=1. But then W⊂ker(D−I), contradicting dim W=2 and (1).

Thus Γ→PGL(W)≅PGL₂(C) is nontrivial.

## 5. Its image is A₅, and every point orbit has at least twelve elements

Here are elementary details of the group-theoretic step. The group G=SL₂(F₅) is perfect: upper and lower elementary unipotents generate G; conjugation of an upper unipotent u(t) by diag(2,3) sends it to u(4t), so the resulting commutators include every u(t), and the same holds for lower unipotents. The quotient G/⟨z⟩ is the simple group A₅.

Any proper normal subgroup K of G is contained in ⟨z⟩. Indeed its image in A₅ is either trivial or all of A₅; in the latter case G=K⟨z⟩ would make G/K abelian, so perfectness would force K=G. Consequently the nontrivial homomorphism G→PGL₂(C) has kernel either 1 or ⟨z⟩.

The kernel cannot be 1. If the action were faithful, the central involution z would have exactly two fixed points on P¹. Centrality makes this two-point set G-invariant; perfectness forces G to fix each point individually. A finite group of automorphisms of a smooth curve fixing a point injects into the multiplicative group through its action on the tangent line, and is therefore cyclic. To justify the injection, a finite-order local automorphism with derivative one is the identity in characteristic zero, by considering its first nonzero higher-order power-series coefficient. Faithfulness would therefore make G cyclic, a contradiction.

The kernel is exactly ⟨z⟩ and the effective group is A₅. Its point stabilizers are cyclic by the same tangent-line argument. The only possible cyclic-subgroup orders in A₅ are 1,2,3,5, so every orbit has size 60,30,20, or 12. In particular,

    every nonempty finite Γ-invariant subset of L has at least 12 points.  (2)

## 6. Degree-seven minors exclude every rank drop

Restrict b to L≅P¹. Each entry is a homogeneous linear form on L. Since L⊂Z₃, its rank is at most seven everywhere, and the additional generic-rank hypothesis says it is generically seven. Therefore at least one of its 7-by-7 minors is a nonzero section of O_L(7).

The nonzero restricted minors have a common zero divisor E: at each point its multiplicity is the minimum of their vanishing orders. Equivalently, their common homogeneous gcd defines E. Since E is bounded by the zero divisor of any one nonzero minor,

    0≤deg E≤7.                                            (3)

Its support is exactly the set of points where rank b≤6, equivalently rank Q≤2. Equivariance makes this rank-drop set Γ-invariant. In fact the determinantal ideal is invariant, so the divisor E is invariant with multiplicities; set invariance alone already suffices.

If E were nonzero, its support would contain a Γ-orbit of at least twelve distinct points by (2). This contradicts deg E≤7. Thus E=0, and rank b=7 at every point of L. The identity rank b=4+rank Q proves the theorem.

## Dependency boundary

The representation and line-action argument in Sections 1–5 is unconditional for any free A-orbit of twenty-five N-stable-as-a-set lines in this Schrödinger projective space. Section 6 requires generic rank seven, supplied here by the separate finiteness of Z₂. Without that input, the same argument still proves that any N-equivariant linear matrix pencil on one of these lines whose generic rank is r≤11 has constant rank r: its r-minors give a common-zero divisor of degree at most r<12. It does not identify that generic rank without additional information.

## 7. Optional identification: the orbit consists of the odd reflection lines

The abstract representation also identifies the twenty-five lines uniquely, without asserting that they lie in Z₃.

Let R e_j=e_(−j). It is the canonical intertwiner for z=−I, with eigenspaces V₊ and V₋ of dimensions three and two. Every canonical intertwiner R_s commutes with R as an actual linear operator. Indeed centrality of z gives R_s R R_s⁻¹=cR for a scalar c; taking traces gives 1=c because tr R=1. Thus both eigenspaces are invariant.

There is no G₀-invariant one-dimensional vector subspace of V. Such a subspace would be stable under D and T; the exact relation in (1) forces D to have eigenvalue one there, so the subspace would be Ce₀. But the Fourier intertwiner

    F e_j=Σ_(k∈F₅) ζ^(jk)e_k

also belongs projectively to G₀: it sends X to Z and Z to X⁻¹ and satisfies the exact corresponding relations for the W_v. It does not preserve Ce₀.

The projective G₀-action is completely reducible in the sense needed here: the inverse image of G₀ under SL(V)→PGL(V) is a finite group, so Maschke's theorem applies to its ordinary linear representation on V. Therefore V₊ contains no invariant two-dimensional subspace, since its invariant complement would have dimension one. Also V₋ contains no invariant line.

If W is any G₀-invariant two-dimensional subspace of V, R-stability and actual commutation give an invariant direct sum

    W=(W∩V₊) ⊕ (W∩V₋).

The mixed case would give invariant one-dimensional subspaces; W⊂V₊ is excluded by the previous paragraph. Thus necessarily W=V₋. This proves uniqueness of the G₀-stable projective line.

Its A-stabilizer is a G₀-stable subgroup of A, hence an invariant F₅-subspace of the standard irreducible two-dimensional G-module. It is either 0 or A. The latter would make V₋ invariant under the irreducible Heisenberg representation and is impossible. Thus the A-orbit of P(V₋) has exactly twenty-five lines. Since G₀ stabilizes P(V₋), this is also one N-orbit.

By complement conjugacy and uniqueness, any twenty-five-line orbit of the type in the theorem is precisely

    { P(aV₋) : a∈A }.

Equivalently these are the two-dimensional-eigenspace lines of the twenty-five projective involutions a[z]a⁻¹. More concretely, using W_a to represent a, the operator W_a R W_a⁻¹ has a two-dimensional (−1)-eigenspace W_a V₋ and a three-dimensional (+1)-eigenspace. The projective involutions are distinct because C_A(z)=0. This supplies an abstract geometric description of the sole possible line orbit, not a rank-locus existence proof.

## 8. The twenty-five canonical lines are pairwise disjoint

For a∈A, use the actual linear involution

    R_a=W_a R W_a⁻¹=W_(2a) R.

It satisfies R_a²=I and tr R_a=1, and its two-dimensional (−1)-eigenspace is W_aV₋. The displayed formula follows from R W_v R⁻¹=W_(−v) and W_a²=W_(2a).

Take distinct a,b∈A and put D_ab=R_aR_b. Then

    D_ab=W_(2a) W_(−2b)=ε W_(2a−2b),    ε∈μ₅.

The Weyl label 2a−2b is nonzero. For every nonzero v∈A, W_v has trace zero: if its shift coordinate is nonzero it has zero diagonal in the Schrödinger basis, and otherwise its diagonal entries sum to Σ_j ζ^(bj)=0 for b≠0. Also W_v^k=W_(kv). Consequently

    D_ab⁵=I,     tr(D_ab^k)=0 for k=1,2,3,4.

Since the operator is diagonalizable and has dimension five, these character identities show that its eigenvalues are all five fifth roots, each with multiplicity one. Indeed the multiplicity of ζ^j is (1/5)Σ_(k=0)^4 ζ^(−jk)tr(D_ab^k)=1.

The involution R_a satisfies the exact relation

    R_a D_ab R_a=D_ab⁻¹.

Thus it interchanges the two eigenspaces in each pair of nontrivial reciprocal eigenvalues. Its trace on each such two-dimensional sum is zero. The only remaining eigenspace is the one-dimensional D_ab=1 eigenspace. Since tr R_a=1, R_a acts on that eigenspace by +1.

If a nonzero vector v lay in the (−1)-eigenspaces of both R_a and R_b, then D_ab v=R_aR_bv=v but R_a v=−v. This contradicts the preceding paragraph. Hence those two-dimensional eigenspaces intersect only at zero, and their projectivizations are disjoint.

Therefore all twenty-five canonical lines are pairwise disjoint. If the reduced curve part Γ₃ is nonempty, it is their disjoint union as a reduced curve. This says nothing about possible nonreduced structure or embedded components of the full determinantal scheme Z₃.

## Verification record

An independent verifier checked the full proof, including Section 7, and found no mathematical errors. In particular the Weyl signs, the exact Fourier relation F W_(a,b) F⁻¹=W_(−b,a), the complement cocycle calculation, the nontriviality argument, the effective A₅-action, and the invariant rank-drop divisor were checked. The finite preimage of G₀ in SL(V) has order 5·120=600, validating the use of Maschke's theorem. This verification concerns the deduction from the stated dependencies; it does not independently re-prove the imported curve classification or Z₂ finiteness.

A second independent audit also verified Section 8, including the normalized reflection formulas, the five simple eigenvalues of R_aR_b, and the trace-one argument proving disjointness. See AUDIT.md in this directory for the independent audit record.
