> Historical mathematical review of the source manuscript. This is not a new independent review or a formal verification certificate. Original source-byte hashes refer to the archived manuscript; public-byte hashes are in SOURCE-BINDINGS.json.

# Independent audit: invariant quintic stabilizers

## Verdict and audited version

**Pass, conditional only on the explicitly imported audited HM inputs. No mathematical correction is required.** There are exactly six exceptional projective invariant quintic functionals. Their vector and projective Lie stabilizers are the four-dimensional Cartan subalgebras indexed by the six lines of F₅². Every other nonzero invariant functional has zero Lie stabilizer. The finite-exception incidence argument gives the claimed codimension bounds 20, conditionally 22 and 23, and the exact-codimension-20 assertions when the relevant parameter space meets the exceptional set.

Audited [PROOF.md](PROOF.md), SHA-256:

`5de8f18428507c19bf414ff67dbafe04a7cfd0724083768d3165d81fb1a76ad2`.

The immediate imported files were read in full:

- [heisenberg-vertex-obstructions](https://github.com/Akilleez-QA/read-em-and-weep/blob/1cd5d26e86d0d48bb994ebd9635c77b909b7aa5b/research/hm/heisenberg-vertex-obstructions/PROOF.md), SHA-256 `6a2abcbae2506e47d5b28808449a9c3fb2a55de854ff8252e734e83b7b7d3d7d`.
- `https://github.com/Akilleez-QA/read-em-and-weep/blob/1cd5d26e86d0d48bb994ebd9635c77b909b7aa5b/research/hm/heisenberg-vertex-obstructions/AUDIT.md`, SHA-256 `bb6c0f7fed4a4c6f2237f9d5fd586e927922ed36f20e491384fe9a66599a3847`.

The imported proof hash agrees with the version recorded in its audit. This audit independently checks the new classification and refined incidence argument. It also checks the immediate weight/support and derivative-duality arguments on which they depend. It does not re-prove the earlier HM cohomology, scalar nonvanishing, or smooth-member theorems.

## 1. Imported representation-theoretic input

With ZX=ζXZ, the matrices E_(r,s)=X^rZ^s have pairwise distinct conjugation characters. The identity supplies the unique trivial character, and the other 24 matrices are trace zero and form a basis of sl(V). The commutator is nonzero precisely for independent labels in F₅² and then has label their sum.

The imported support-closure proof is valid: two independent supported labels generate all four affine lines with nonzero coefficient of one label, and their brackets subsequently generate its four missing nonzero multiples. Thus any proper H₅-stable Lie subalgebra has support in one F₅-line and dimension at most four. An invariant nonzero q has a proper stabilizer because Sym⁵V has no SL(V)-fixed vector. These facts apply to the vector stabilizer used by the new proof.

The central μ₅ acts trivially on Sym⁵V. Consequently the finite-character decompositions used here really are decompositions for the abelian conjugation quotient, with no central-character mismatch.

## 2. Universal spectrum and infinitesimal kernel

The power identity

    E_(r,s)^k = ζ^(rs k(k−1)/2) X^(kr) Z^(ks)

follows by induction from the multiplication law. For k=5 the scalar is ζ^(10rs)=1 and the two generator powers are identities. For 1≤k≤4 the label k(r,s) is nonzero, so the trace vanishes. Since t⁵−1 is separable, E_a is diagonalizable; Fourier inversion of its traces gives each fifth root of unity with multiplicity one.

In an eigenbasis f_i with eigenvalues ζ^i, the differential of the Sym⁵ action sends a monomial with exponents n_i to itself times Σ n_iζ^i. This is correctly distinguished from the group action, which multiplies it by the product of the eigenvalues with those exponents. The differential is the relevant action because E_a is being used as an element of sl(V).

For nonnegative integers n_i summing to five, the vanishing of Σn_iζ^i forces the degree-at-most-four polynomial Σn_it^i to be a rational multiple of Φ₅(t). Its value at one makes that multiple exactly one. Thus the only monomial in the differential kernel is f_0f_1f_2f_3f_4. Monomials form an eigenbasis for this diagonal differential operator, so there are no further kernel vectors formed by cancellation. Equation (1) is exact.

## 3. Existence, invariance, exhaustion, and distinctness

For a nonzero a on a fixed line, the four E_(ka) are scalar multiples of the powers E_a^k. They have the same five eigenlines. Their four diagonal-entry vectors form the nonconstant Fourier vectors, so they are independent and span the whole trace-zero diagonal algebra. This proves that the Cartan h_ℓ is well-defined and kills the product q_ℓ.

Conjugation by a Heisenberg element changes E_a by a fifth-root scalar. Its permutation of eigenlines is therefore a translation of F₅, either the identity or a five-cycle, hence even. In a monomial matrix for this action, determinant one then forces the product of the five factor scalars to equal one. The product q_ℓ is fixed as a vector, not only up to scalar. No choice of eigenbasis normalization changes its projective point.

Conversely, a nonzero vector Lie stabilizer of an invariant q contains a whole nontrivial character line C E_a. The kernel calculation forces q to be proportional to q_ℓ. The constructed four-dimensional Cartan, together with the imported upper bound four, gives the exact Lie stabilizer. Distinct lines have different Cartans by the direct weight decomposition, so their products cannot have the same projective class. There are exactly (25−1)/(5−1)=6 lines. This proves both exhaustion and distinctness, without assuming independence of the six products.

## 4. Full groups and projective versus vector Lie stabilizers

Unique factorization in Sym(V) shows that a linear transformation preserving the projective class of the squarefree product must permute its five linear-factor lines. Therefore its stabilizer in SL(V) is precisely the determinant-one monomial group in the chosen eigenbasis. If the associated permutation is π and the factor scalars are c_i, then

    1 = det(g) = sgn(π) ∏c_i,
    g·q_ℓ = (∏c_i)q_ℓ = sgn(π)q_ℓ.

Thus every such monomial matrix is a projective stabilizer, while exactly those with even permutation are vector stabilizers. Both identity components are the determinant-one diagonal torus. The group-level distinction in the proof is necessary and correctly stated. It would be incorrect to identify the entire vector and projective stabilizer groups, but the proof does not do so.

For any invariant nonzero q, equivariance of sl(V)→Sym⁵V, v↦v·q, shows that its image D_q contains only nontrivial H₅ characters. Since q is fixed, D_q∩Cq=0. Hence an infinitesimal projective stabilizer, characterized by v·q∈Cq, is already a vector stabilizer. Both orbit dimensions are 24−4=20 at the six exceptions and 24 elsewhere. Over C a zero-dimensional algebraic stabilizer is finite; the proof correctly avoids calling it trivial. In particular, invariant vectors retain their finite Heisenberg stabilizers.

All these groups are being taken inside SL(V). Passing to PSL(V) divides out the central μ₅, which already acts trivially in degree five, and does not change any stated dimension.

## 5. Restricted derivative rank and finite-exception dimensions

The imported pairing gives

    A_q transpose: v ↦ −(v·q)|_K.

Restriction to K has kernel T. Since T is fixed by H₅ and D_q has only nontrivial characters, D_q∩T=0. Thus the restriction loses no rank, and rank A_q is exactly 20 at an exceptional point and 24 otherwise. This uses neither an SL(V)-equivariance assertion about Ψ nor a selected rank computation.

With dim K=123, the respective projective fibers P(ker A_q) have dimensions 102 and 98. Over the nonexceptional open subset of P(T), the fiber bound gives dimension at most 98+2=100. Over its finite exceptional subset, the dimension is at most 102. The complete incidence therefore has dimension at most 102 and its image in the 122-dimensional P(K) has codimension at least 20. If P(T) has no exceptional point, only the first stratum remains and the codimension bound is 22.

For the common-zero condition the base is the one-dimensional Veronese conic. The nonexceptional incidence dimension is at most 98+1=99; the finite exceptional part still has dimension at most 102. The unconditional codimension bound is consequently 20. Avoidance by the conic alone improves it to 23, even when P(T) contains an exceptional point elsewhere.

The full incidences are closed and projective over P(K). Their projected images are closed. A locally closed nonexceptional stratum need not have closed image; the proof correctly does not rely on that. The imported duality identifies the first image exactly with nonsurjectivity of L_p and the conic image exactly with a common projective zero of its binary quadratics. Thus no containing-locus versus exact-locus ambiguity enters the bounds.

The final exactness assertions in Section 5 also hold: if E∩P(T) is nonempty, any one of its fibers maps isomorphically onto a 102-dimensional projective linear subspace of the first bad locus. The upper bound then shows that this bad locus has codimension exactly 20. Likewise, if E meets the conic, the common-zero bad locus has codimension exactly 20. These conditional equalities establish the stated dichotomy without deciding either intersection.

## 6. Limits and scope

The final caution is valid: six distinct projective points need not be linearly independent, and normalizer transitivity alone does not prevent all of them from lying in a particular projective plane. Neither avoidance by T nor avoidance by its conic has been proved here. The refined conclusions are appropriately conditional where they use avoidance.
