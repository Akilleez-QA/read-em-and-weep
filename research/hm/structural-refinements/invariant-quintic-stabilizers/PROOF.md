> Scope: read CURRENT-SCOPE.md and DEPENDENCIES.json with this complete historical derivation. Historical open-case wording is qualified there.

# Classification of positive-dimensional Heisenberg-invariant quintic stabilizers

## Statement and inputs

Work over C with the standard five-dimensional Schrödinger representation V of H₅⊂SL(V). Put R=Sym⁵V=S₅*, so the objects here are quintic FUNCTIONALS. Import the audited weight and Lie-support arguments of [heisenberg-vertex-obstructions](https://github.com/Akilleez-QA/read-em-and-weep/blob/1cd5d26e86d0d48bb994ebd9635c77b909b7aa5b/research/hm/heisenberg-vertex-obstructions/PROOF.md). In particular

    sl(V)=⊕_{a∈F₅²\{0}} C E_a,   E_(r,s)=X^r Z^s,

and the Lie stabilizer of every nonzero H₅-fixed q is proper, H₅-stable, and supported on at most one F₅-line. Also import its HM notation K=ker Ψ, dim K=123, T=K⊥⊂R^{H₅}, dim T=3, and its derivative duality.

The new conclusions are:

1. There are exactly six exceptional projective points in P(R^{H₅}) with positive-dimensional SL(V) stabilizer. They are indexed by the six lines ℓ⊂F₅². The exceptional point q_ℓ is the product of the five eigenvectors of any E_a with 0≠a∈ℓ, considered in Sym⁵V and up to a nonzero scalar.
2. At every exceptional point the vector and projective Lie stabilizers are the same four-dimensional Cartan subalgebra ⊕_{a∈ℓ\{0}} C E_a. At every other invariant point both Lie stabilizers vanish. Vector and projective orbit dimensions are respectively 20 at the exceptions and 24 elsewhere.
3. With no assumption about which exceptions lie in P(T), both the nonsurjectivity and common-zero bad loci in P(K) have codimension at least 20. If P(T) avoids all six exceptions, these bounds improve to 22 and 23 respectively. For the common-zero bound 23 it suffices that the Veronese conic in P(T) avoids them.

This proof does not assert linear independence of the six exceptional forms, nor their avoidance by T.

## 1. Spectrum of a nontrivial Heisenberg weight

For 0≠a=(r,s), the multiplication law gives

    E_a^k = ζ^{rs k(k−1)/2} X^{kr} Z^{ks}.

Thus E_a⁵=1. For k=1,2,3,4, the matrix on the right is a scalar multiple of a nontrivial Heisenberg weight, hence has trace zero. Since t⁵−1 has distinct roots, E_a is diagonalizable. If m_i denotes the multiplicity of ζ^i, then Σm_i=5 and Σm_i ζ^{ik}=0 for 1≤k≤4. Fourier inversion gives m_i=1 for every i. Equivalently the characteristic polynomial is t⁵−1.

Choose an eigenbasis f_0,…,f_4 of V with E_a f_i=ζ^i f_i. In Sym⁵V the monomial f_0^{n_0}⋯f_4^{n_4}, with n_i≥0 and Σn_i=5, has infinitesimal E_a-weight

    Σ n_i ζ^i.

This is the Lie-algebra action by the Leibniz rule, not the finite-group eigenvalue ζ^{Σ i n_i}. If its infinitesimal weight is zero, the rational polynomial N(t)=Σn_i t^i of degree at most four vanishes at ζ. Since the fifth cyclotomic polynomial is 1+t+t²+t³+t⁴, N(t) is a rational multiple of it. Evaluation at t=1 shows the multiple is one. Consequently all n_i=1, and

    ker(E_a : Sym⁵V→Sym⁵V)=C(f_0 f_1 f_2 f_3 f_4).       (1)

The distinction between finite weight and infinitesimal weight is essential.

## 2. The six products exist and are invariant

Fix a line ℓ and a nonzero a∈ℓ. The matrices E_{ka}, 1≤k≤4, are nonzero scalar multiples of E_a^k. They have the same eigenlines and span the full trace-zero diagonal subalgebra in the eigenbasis f_i: the four vectors of diagonal entries (ζ^{ik})_i are linearly independent and have coordinate sum zero. Denote this Cartan by h_ℓ. Its elements all kill q_ℓ=f_0⋯f_4. Changing a within ℓ changes neither the eigenlines nor the projective product.

For h∈H₅, conjugation sends E_a to ζ^t E_a for some t∈F₅. Thus h permutes its five eigenlines by a translation of their eigenvalue indices. Such a permutation is either the identity or a five-cycle, hence has sign +1. Write h f_i=c_i f_{π(i)}. Since det h=1,

    ∏ c_i=det(h)/sgn(π)=1.

It follows that h q_ℓ=q_ℓ. In particular these are actual H₅-fixed vectors, not merely H₅-invariant projective lines. All assertions also work on the dual model after consistently reversing the action; here the functional representation is Sym⁵V itself.

## 3. Exhaustion, exact stabilizer, and distinctness

Let 0≠q∈R^{H₅}. If its vector Lie stabilizer is nonzero, its H₅-character decomposition contains C E_a for some a≠0. Equation (1) then forces q to be a nonzero multiple of q_ℓ, where ℓ=F₅a. Conversely h_ℓ kills q_ℓ. The imported support bound gives stabilizer dimension at most four, so its stabilizer is exactly h_ℓ.

Distinct ℓ give distinct h_ℓ, by the direct weight decomposition. Their exceptional projective products must therefore be distinct. As F₅² has (25−1)/(5−1)=6 lines, the exceptional set has exactly six elements. There are no stabilizer dimensions one, two, or three.

One may also check the entire exceptional stabilizer directly. Unique factorization in Sym(V) implies that any g preserving the projective product must permute its five linear factors, so it is monomial in the f_i basis. In SL(V), if g f_i=c_i f_{π(i)}, then ∏c_i=sgn(π). Therefore the projective stabilizer consists of all determinant-one monomial matrices, whereas the vector stabilizer is its subgroup with even permutation. Both have identity component the determinant-one diagonal torus. This group-level distinction does not alter the equality of their Lie algebras.

## 4. Projective versus vector stabilizers at every invariant point

The derivative map

    sl(V)→R,   v↦v·q

is H₅-equivariant, with conjugation on its source, because q is H₅-fixed. Every character of the source is nontrivial, so its image D_q has no invariant part. In particular D_q∩Cq=0. Thus v·q∈Cq implies v·q=0, proving that the projective and vector Lie stabilizers agree at every invariant point, including the nonexceptional ones. Since dim SL(V)=24, the orbit dimensions follow. Zero Lie stabilizer means a finite algebraic stabilizer over C; it need not mean the stabilizer group is trivial.

The same character argument gives D_q∩T=0, as used in the imported derivative duality.

## 5. Refined incidence bounds

Let E⊂P(R^{H₅}) be the exceptional six-point set, and set E_T=E∩P(T). For 0≠q∈T, define

    A_q:K→sl(V)*,   A_q(p)(v)=q(v·p).

Restriction R→K* is injective on D_q, because its kernel is T and D_q∩T=0. The transpose identity therefore gives

    rank A_q = dim D_q = 20 if [q]∈E_T, and 24 otherwise.

The projective incidence I⊂P(K)×P(T), defined by all equations q(v·p)=0, has fibers P(ker A_q). These have dimension 102 over E_T and 98 elsewhere. Over P(T)\E_T its dimension is at most 98+2=100; over the finite exceptional set its dimension is at most 102. Hence dim I≤102. The proper projection to P(K) has closed image B, exactly the nonsurjectivity locus of L_p, and

    codim_{P(K)} B ≥ 122−102=20.

If E_T is empty the stronger bound is 122−100=22.

For the common-zero locus use the Veronese conic C⊂P(T) of the imported proof. Its nonexceptional incidence has dimension at most 98+1=99, and its exceptional incidence has dimension at most 102. Its closed projected image B₀ therefore has codimension at least 20. If C∩E is empty it has codimension at least 122−99=23, whether or not other exceptional points lie in P(T).

If E_T is nonempty, any one exceptional fiber is a projective linear space of dimension 102 contained in B. The upper bound already proved then gives dim B=102, so codim B=20 exactly. Likewise, if C∩E is nonempty, codim B₀=20 exactly. Thus the bounds yield a genuine dichotomy: codimension exactly 20 when the relevant parameter space contains an exception, and codimension at least 22 (respectively 23) when it does not.

These arguments use a finite stratification by the rank of A_q. The open-stratum image need not be closed; the full projective incidence is closed and its projection is proper. Outside the stated exceptional-intersection case, no equality or nonemptiness is claimed. Existing generic smooth-vertex obstruction and normal-form conclusions continue to hold with these smaller possible bad loci.

## 6. What is not yet settled

The six exceptional products form one set with an intrinsic Heisenberg-line indexing. Their distinctness does not imply their linear independence. Normalizer transitivity alone likewise does not show that a specified invariant three-dimensional summand T avoids them: a six-point projective orbit can in principle lie in a projective plane. Any stronger conclusion requires an additional proved structural argument, for example a compatible Galois descent argument, not an assumption about these six products or a selected quintic evaluation.
