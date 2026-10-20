# Every nonzero invariant degree-fifteen hypersurface is integral

## Theorem

For the full HM normalizer N=H5⋊SL2(F5)⊂SL(V), dim V=5, every nonzero polynomial

    F ∈ (Sym^15 V*)^N

is irreducible over C. In particular its projective zero scheme is reduced and irreducible.

Together with PROOF.md, this gives a projective pencil of integral degree-fifteen hypersurfaces. If the equivariant outer determinant δ is nonzero, its divisor Δ is an integral member of that pencil, and the generic rank of Φ along Δ is exactly nineteen. These conclusions remain conditional on δ≢0; the argument does not prove that condition.

The only inputs are the Heisenberg structure, the perfection of N, the absence of N-invariant quintics established in ../quintic-normalizer-exclusion/PROOF.md, and unique factorization. No actual polynomial, operation, input, source matrix, or rank instance is evaluated.

## 1. The Heisenberg quotient cannot permute fewer than 25 factors nontrivially

Factor F in the polynomial ring C[V] as

    F=c·∏_(i=1)^r f_i^(m_i),

with pairwise nonassociate homogeneous irreducible factors f_i of positive degrees d_i. The group N permutes their projective lines [f_i], preserving multiplicities and degrees. Since Σ m_i d_i=15, there are at most fifteen distinct factors.

The central subgroup Z=Z(H) acts on every homogeneous polynomial by a scalar, so it fixes every factor line. Thus the permutation action of H factors through

    P=H/Z≅F5².

The P-orbits on the finite factor set have sizes 1,5, or 25. An orbit of size 25 is impossible. Suppose there is a size-five orbit O. Its stabilizer in P is a one-dimensional subspace L⊂P. Because P is abelian, every point of O has exactly the same stabilizer L.

The whole group N permutes the P-orbits. If n∈N acts on P by a∈SL2(F5), then the orbit nO has stabilizer aL. The group SL2(F5) is transitive on the six one-dimensional subspaces of F5². Hence the existence of O forces at least six distinct size-five P-orbits, one for each stabilizer line. This requires at least thirty distinct factors, a contradiction.

Therefore every P-orbit is a singleton: H stabilizes every irreducible factor line.

The proof in fact rules out a nontrivial such action on any set of fewer than 25 points: a possible size-25 orbit is the first exception. Only the bound fifteen is needed here.

## 2. Each factor degree is divisible by five

Since H stabilizes the line C f_i, its action on that line is a one-dimensional character χ_i. Every character kills the commutator subgroup [H,H]=Z. On the other hand, a central scalar ζ acts on a degree-d_i polynomial by ζ^(−d_i). Hence

    5 | d_i.

There are consequently at most three distinct factors.

Now N acts on their set through a homomorphism N→S_r, with r≤3. Because N is perfect, its image is perfect. The group S_r is solvable for r≤3, and its only perfect subgroup is trivial. Therefore N stabilizes each factor line. Perfection again makes each one-dimensional character trivial, so every f_i is itself N-invariant.

There are no nonzero invariant quintics. Since each d_i is a positive multiple of five, each d_i is therefore at least ten. The equality

    Σ m_i d_i=15

now forces r=1, d_1=15, and m_1=1. This proves irreducibility and reducedness.

## 3. The invariant pencil has a complete-intersection base scheme

By PROOF.md, choose any basis F_0,F_1 of the two-dimensional space (Sym^15 V*)^N. Every nonzero linear combination sF_0+tF_1 is irreducible by the theorem. In particular F_0 and F_1 are nonassociate irreducible polynomials and have no common factor.

The scheme

    B=V(F_0,F_1) ⊂ P(V)

is therefore a complete intersection of type (15,15). It has pure codimension two, dimension two, and degree 225, and is Cohen–Macaulay. It is the base scheme of the invariant pencil and does not depend on the choice of basis. Every two distinct members of the pencil have scheme-theoretic intersection B.

No reducedness, irreducibility, normality, or smoothness of B is asserted. The theorem concerns the individual hypersurface members.

## 4. Consequences for a nonzero outer determinant

Assume the genuine N-equivariance required in PROOF.md and suppose δ=det Φ is nonzero. Its zero divisor Δ is then an integral degree-fifteen hypersurface. It contains the pencil base scheme B.

At the generic point η of Δ, the local ring R=O_(P(V),η) is a discrete valuation ring. Since Δ is reduced, δ has valuation one. After trivializing source and target bundles, Φ is a square rank-twenty presentation over R. Its Smith normal form has exactly nineteen unit entries and one uniformizer entry; any other pattern would give determinant valuation zero or at least two. Therefore

    rank(Φ|_η)=19.

Equivalently, the generic cokernel on Δ is one-dimensional over its function field, and the determinant degeneracy is generically simple. This is an abstract consequence of irreducibility and determinant order, not a rank evaluation at a chosen point.

If one also imports the prior global rank-ten package ensuring codim(P(V)\U_10)≥2, the generic point η lies in U_10. There Φ has its rank-fourteen isomorphism on D_sym and the rank-six quotient map α. It follows that

    rank(α|_η)=5.

Thus, under that additional hypothesis, the alternating quotient loses exactly one rank generically along the integral divisor Δ. Nothing here classifies the special points of Δ or determines the full outer zero ideal there.

## Logical boundary

The symmetry calculation proves that the possible nonzero determinants lie in a two-dimensional invariant space, and the factor argument proves that every nonzero member is integral. Neither result proves that the particular determinant supplied by the stipulated operation is nonzero. The alternatives remain:

- δ=0, so Ω is empty and its vanishing scheme is all of P(V); or
- δ≠0, so Δ is integral of degree fifteen, Φ has generic rank nineteen on Δ, and Ω=P(V)\Δ is a nonempty dense open.

The second alternative is structurally more constrained than the earlier conditional degree-fifteen statement, but it is still conditional.
