# Independent audit: exclusion of full-normalizer invariant ACM decic surfaces

## Status

The proposed argument is mathematically sound over the complex numbers, subject to the standard setup specified below. It applies to singular integral surfaces, and does not require any sectional-genus hypothesis. This initial audit independently reconstructs the proof; the final proof review is recorded below.

## Precise setup

Let V be the five-dimensional Schrödinger representation of the order-125 Heisenberg group H. Its center Z has order five and acts by a primitive scalar. Write A=H/Z, an elementary abelian group of order 25. Let N be a linear normalizer acting on V such that its conjugation action on A contains SL_2(F_5). In the usual full projective normalizer, this condition holds; passing to its inverse image in SL(V) supplies a finite linear lift. Work over C. Let S=Sym(V^*) and let Y be an integral, nondegenerate, N-invariant surface in P(V), of degree 10.

The only representation-theoretic inputs are:

1. For each nontrivial character of Z, H has a unique irreducible representation of dimension five with that central character, and every representation with that scalar central character is a direct sum of its copies.
2. SL_2(F_5) acts transitively on the 24 nonzero elements of the dual group A^*. This follows directly by extending a nonzero vector to a determinant-one basis; the same statement holds in the contragredient representation.
3. Finite-group representations over C are completely reducible.

## Independent verification

### 1. No equations of degrees one, two, or three

Nondegeneracy gives I_1=0. The center acts on S_d, hence on I_d, through the d-th power of its character on V^*. For d=2 or 3 this is nontrivial. Therefore a nonzero I_d has dimension divisible by five, in particular at least two.

If I_2 were nonzero, any nonzero quadratic equation in I_2 would be irreducible. Indeed, any factorization would place a linear factor in the prime ideal I(Y), contradicting nondegeneracy. Choose linearly independent quadrics f,g in I_2. They are irreducible and nonassociate, hence coprime. Their complete intersection is a pure two-dimensional scheme of degree 4. Since it contains the integral surface Y, Y is a component of its support and its degree cannot exceed 4, a contradiction.

Now suppose I_3 were nonzero. Any cubic in I_3 is irreducible, since a proper factor in the prime ideal would have degree one or two. Two independent cubics are coprime; their complete intersection has degree 9 and contains Y, contradicting deg(Y)=10.

This proof uses integrality but no smoothness or local complete-intersection property of Y.

### 2. ACM forces the pure resolution

Assume R=S/I is Cohen–Macaulay. Its Krull dimension is three. Quotient by a regular sequence of three sufficiently general linear forms to obtain a standard graded Artinian algebra B over C on two generators. Because I has no elements in degrees at most three, its Hilbert function begins

  (1,2,3,4).

The length of B is deg(Y)=10, already equal to the sum of those four entries. Thus all subsequent entries vanish, and B is isomorphic as a graded algebra to C[u,v]/(u,v)^4.

The graded Betti numbers of R over S equal those of B over C[u,v]: tensoring a minimal free resolution by the quotient by the regular linear forms remains exact and minimal. The latter quotient has the resolution

  0 -> C[u,v](-5)^4 -> C[u,v](-4)^5 -> C[u,v] -> B -> 0.

For example, the five generators u^4,u^3v,u^2v^2,uv^3,v^4 have four adjacent linear relations; this is the standard resolution of the fourth power of the maximal ideal in two variables. Consequently

  0 -> S(-5)^4 -> S(-4)^5 -> I -> 0.

Equivalently, regularity(R)=3 proves that all ideal generators have degree four, after which the Hilbert series and minimality give the same pure resolution. It is important to include this argument: the alternating Hilbert-series numerator alone would not rule out canceled Betti degrees in an arbitrary resolution.

In particular, U=I_4 has dimension five. The multiplication map U tensor S_1 -> I_5 is onto, with a four-dimensional kernel W. Both U and W are canonically N-stable, so no equivariant-choice issue arises.

### 3. The representation contradiction

Let chi denote the central character of S_1. Then U has central character chi^4 and dimension five, so U is the unique irreducible H-module with that character. As chi has order five, chi^4=chi^(-1), and therefore U is isomorphic as an H-module to S_1^*.

The center acts trivially on U tensor S_1, so this tensor product and its N-stable subspace W descend to representations of A. Decompose W into its A-character spaces. Conjugation by N permutes these spaces with equal dimensions on each orbit. Any nonzero A-character occurring in W would force all 24 nonzero characters to occur. Since dim(W)=4, only the trivial character can occur. Therefore W is contained in (U tensor S_1)^A.

But A-invariants here equal H-invariants, and Schur's lemma gives

  dim (U tensor S_1)^A = dim Hom_H(U^*, S_1) = 1.

This contradicts the injection of the four-dimensional space W into that invariant subspace.

## Audit verdict

PASS, under the specified characteristic-zero Heisenberg/full-normalizer setup. The theorem is stronger than a genus-specific exclusion: there is no integral nondegenerate full-normalizer invariant ACM surface of degree 10 in P^4.

## Scope cautions

- The conclusion is conditional on the quotient action containing SL_2(F_5), or at least having no nonzero dual-character orbit of size at most four. H-invariance alone is insufficient for this proof.
- A projective action should be converted to a linear lift or handled via the inverse image in GL(V); silently treating the projective group as acting linearly on polynomial spaces would obscure central characters.
- Integrality cannot simply be dropped: it is used to infer irreducibility of low-degree equations and hence the Bézout bound.
- The proof has been audited over C. No positive-characteristic extension is asserted here.

## Completed artifact review

Reviewed the full `acm-decic-exclusion/PROOF.md` after its creation. PASS without a mathematical correction required. In particular:

- Its prime-ideal gcd argument correctly replaces an unsupported assertion that arbitrary low-degree equations are coprime.
- Its Artinian-reduction/Koszul argument explicitly establishes the pure resolution, addressing the only preliminary detail flagged in this audit.
- Its intrinsic multiplication kernel avoids any need to choose an N-equivariant minimal resolution or extend the H-isomorphism U ≅ S_1^* to N.
- Its stronger statement omitting a nondegeneracy hypothesis is valid: H-invariance and irreducibility of S_1 force I_1=0 automatically.
- The Hilbert polynomial 5n^2-5n+5, forced sectional genus 11, and chi(O_Y)=5 are correct.
- The cohomological deficiency consequence is valid: some H^1(I_Y(t)) or H^2(I_Y(t)) must be nonzero. It makes no unwarranted claim of a local non-Cohen–Macaulay singularity.
- The extra representation restrictions on deficiency dimensions are consistent with the degree-t central character.

I independently opened Hartshorne's original Berkeley notes at https://math.berkeley.edu/~robin/math274root.pdf and verified Proposition 8.7 (printed page 49, PDF page 55) and Theorem 8.8 (printed page 50, PDF page 56). These support precisely the ACM cohomology criterion and general graded codimension-two resolution context cited by the proof.

A finite N is not necessary: complete reducibility is used only for the finite groups H and A; arbitrary linear normalizer elements permute the A-character spaces. The final proof formulation correctly allows this greater generality.
