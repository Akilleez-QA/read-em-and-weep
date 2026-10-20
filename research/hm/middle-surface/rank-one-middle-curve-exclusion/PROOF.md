# The residual-rank-one middle locus is finite

## Statement and precise dependencies

Work over C. Let dim V=5, dim J=20, and let f:V^3→J be the established N-equivariant, outer-symmetric, cyclic-zero trilinear map. Assume the established repeated-input injectivity: for every nonzero u, the map V/Cu→J, a↦f(u,u,a), is injective. Let Q be the established residual middle map. Import these two conclusions:

1. dim Z_3≤1 for Z_3={ [u] : rank Q_u≤3 }, proved in /research/hm/rank-four/quintic-surface-classification/RANK_AT_MOST_THREE_COROLLARY.md under its stated global bundle, normalizer, (H), and delta hypotheses.
2. No nonzero N-invariant effective curve cycle in P(V) has degree at most 20, proved in /research/hm/rank-four/normalizer-small-curve-exclusion/PROOF.md.

Then Z_1={ [u] : rank Q_u≤1 } has dimension at most zero, hence is finite as a support. In particular the rank-exactly-one locus is finite. This argument does not need the absence of rank-zero points, the decic-surface exclusion, or any generic smoothness assumption on a rank stratum.

All statements are conditional on the established source/equivariance hypotheses; no actual source operation or numerical instance is evaluated here.

## 1. The genuinely linear global matrix and its rank

Put X=P(V), U=O_X(-1), E=(V⊗O_X)/U. Outer symmetry gives the global bundle map

    b: U⊗Sym² V → J⊗O_X,
    b(u⊗ab)=f(a,u,b).

Here ab denotes the symmetric product, with associated symmetric bilinear map f(a,u,b). Since dim Sym²V=15, b is a 20-by-15 matrix of homogeneous linear forms in fixed bases. In particular its 8-by-8 minors are sections of O_X(8), not higher-degree expressions coming from a nonconstant frame of E.

Cyclic zero gives f(u,u,u)=0. The repeated-input map is

    A: U²⊗E → J⊗O_X,
    A(u²⊗a)=f(u,u,a).

It has constant rank four by hypothesis, and its image F is a rank-four subbundle. For every u, the image of b contains F_u: use the outer products ua. Modulo F, b descends to

    Q̃: U⊗Sym²E → (J⊗O_X)/F.

This is precisely Q, up to the harmless presentation convention of tensoring both sides by U*; compare ../rank-nine-independent-incidence/PROOF.md, Section 1. Therefore, at every geometric point,

    rank b_u = 4 + rank Q_u.                                  (1)

More concretely, choose a local frame u of U and a local complement to U in V⊗O. The source has columns u², ua_1,...,ua_4, and a_i a_j. The first column is zero and the next four map isomorphically onto F. Splitting F off the target and eliminating the F-components of the last ten columns produces the block matrix diag(I_4,Q̃), together with one zero column. This also verifies the residual-map identification locally, without only comparing dimensions.

Let L⊂H⁰(X,O_X(8)) be the vector space spanned by all 8-by-8 minors of b. Its set-theoretic base locus is

    Bs(L)={rank b≤7}=Z_3.                                    (2)

Thus Bs(L) has dimension at most one. The minors may satisfy dependencies and their base scheme may be nonreduced or nonpure; neither changes (2).

## 2. Three degree-eight members forming a complete intersection

There exist g_1,g_2,g_3∈L whose common zero scheme W is a codimension-three complete intersection in P⁴. Here is a direct construction that treats base points and embedded structure.

Choose any nonzero g_1. Its zero scheme is a hypersurface with finitely many irreducible components of dimension three. No such component lies in Bs(L), so for each component the sections of L vanishing identically on it form a proper linear subspace. Over the infinite field C choose g_2 outside their union. Then g_1,g_2 form a regular sequence in S=C[x_0,...,x_4]; their quotient is Cohen–Macaulay and unmixed, and their projective intersection has pure dimension two.

No irreducible component of this two-dimensional intersection lies in Bs(L). Choose g_3 outside the finitely many proper linear subspaces of L vanishing on those components. The Cohen–Macaulay quotient by g_1,g_2 has no embedded associated primes, so g_3 is a nonzerodivisor on it. Hence g_1,g_2,g_3 form a homogeneous regular sequence. This also shows the property holds for a nonempty open set of choices; generality is not required beyond avoiding these components.

Consequently W is a pure one-dimensional projective complete intersection, and

    deg W = 8·8·8 = 512.                                     (3)

For example its Hilbert series is (1-t⁸)³/(1-t)⁵, whose multiplicity is 512. Every curve in Z_1 is contained in W and is an irreducible component of its support. Nothing here asserts that W is reduced or irreducible, or that the g_i are N-invariant.

## 3. Order at least three along a rank-at-most-one curve

Let C be any reduced integral curve in Z_1, with generic point η. Since X is smooth of dimension four and C has dimension one,

    R=O_{X,η}

is a regular local ring of dimension three, with maximal ideal m and residue field C(C). After trivializing the line bundles, b is a matrix over R whose reduction modulo m has rank s≤5, by (1).

Invert an s-by-s minor and apply invertible row and column operations over R. The matrix becomes diag(I_s,M), with every entry of M in m. (For s=0 this means simply b=M.) Every 8-by-8 minor of this block matrix is either zero or a signed minor of M of size at least 8-s≥3. Hence its ideal of 8-minors is contained in m³. Invertible row and column operations preserve determinantal ideals by the Cauchy–Binet formula and their inverses, so

    I_8(b)R ⊂ m³.                                           (4)

In particular the three local equations g_i all belong to m³. This uses the rank of b at the generic point only; it does not assume C smooth, nor constant rank on all of C.

Because C is a component of the pure curve W, the ideal q=(g_1,g_2,g_3)R is m-primary. It is a parameter ideal generated by a regular sequence in the regular local ring R. Its colength is the generic multiplicity of W along C.

## 4. Elementary multiplicity bound: the colength is at least 27

Here is an explicit Hilbert–Samuel argument, including the facts needed instead of an unsourced local Bézout assertion.

For a regular sequence of length three generating q, the associated graded ring is

    gr_q(R) ≅ (R/q)[T_1,T_2,T_3].

This is the standard regular-sequence graded calculation: the monomials of degree j in the generators form a basis of q^j/q^(j+1) over R/q; injectivity follows successively from the nonzerodivisor property of the generators. Thus, writing ℓ for module length,

    ℓ(R/q^n) = ℓ(R/q)·binom(n+2,3)  for n≥1.                 (5)

Because R is regular local of dimension three, its maximal-ideal associated graded ring is the polynomial ring in three variables over R/m. Therefore

    ℓ(R/m^a) = binom(a+2,3).                                 (6)

By (4), q⊂m³ and hence q^n⊂m^(3n), which gives a surjection R/q^n→R/m^(3n). Equations (5) and (6) imply

    ℓ(R/q)·binom(n+2,3) ≥ binom(3n+2,3).

Divide by n³ and let n tend to infinity. The result is

    ℓ(R/q) ≥ 27.                                            (7)

Equivalently this is e(q,R)≥e(m³,R)=27 together with e(q,R)=ℓ(R/q). The explicit proof explains why nontransverse intersections and higher-order vanishing only increase the needed multiplicity.

## 5. The invariant curve cycle and contradiction

Let C_1,...,C_t be all one-dimensional irreducible components of the reduced closed locus Z_1. There are finitely many, since Z_1 is a closed subscheme of a noetherian projective variety; by Z_1⊂Z_3 they are all its positive-dimensional components. Set

    Γ = [C_1]+...+[C_t].

Equivariance of f implies equivariance of b and Q (or directly invariance of their rank conditions). Thus N preserves Z_1 and permutes its one-dimensional components. Hence Γ is an actual N-invariant effective cycle, not merely an invariant numerical class. All multiplicities in Γ are one.

Each C_i is a component of W with generic multiplicity at least 27 by (7). The degree formula for the fundamental cycle of a projective pure curve, together with (3), gives

    512 = deg W ≥ 27∑ deg C_i = 27 deg Γ.

Thus deg Γ≤floor(512/27)=18. If t>0 this contradicts the established exclusion of nonzero N-invariant effective curve cycles of degree at most 20. Therefore t=0. Since dim Z_1≤1, this means dim Z_1≤0, as asserted.

The choice of W need not respect N: invariance is required only for Γ, which is intrinsically extracted from Z_1. Additional components of W, isolated base points, and nilpotent structure do not affect the inequality.

## 6. Consequence for independent zero triples

Using the previously established projective fiber bound of three over residual rank one (/research/hm/universal-polar/rank-one-residual-fiber-model/PROOF.md), finiteness of its middle locus yields

    affine dimension over residual rank one ≤0+3+3=6,

where the last three parameters are the independent nonzero scalings of the inputs. Together with /research/hm/rank-four/quintic-surface-classification/RANK_AT_MOST_THREE_COROLLARY.md, residual ranks one, two, and three therefore all contribute affine independent-zero dimension at most six.

This proof alone does not treat the remaining residual-rank-four or residual-rank-five surface cases. It is independent of their subsequent decic analysis.

## 7. Stronger consequence once the rank-at-most-five locus is at most a curve

Assume additionally the independently established conclusion

    dim Z_5≤1,   Z_5={ [u] : rank Q_u≤5 }.                    (8)

This is the separate decic-closure input, now integrated explicitly in /research/hm/middle-surface/independent-dimension-six/PROOF.md, Section1. The genus-eleven closing step is /research/hm/middle-surface/decic-hyperplane-deficiency/PROOF.md, independently audited in /research/hm/middle-surface/decic-deficiency-audit/AUDIT.md; the full-normalizer ACM contradiction is /research/hm/middle-surface/acm-decic-exclusion/PROOF.md. The earlier surface reduction and other genus exclusions are required to obtain (8); this section takes (8) as an explicit additional premise rather than claiming the genus-eleven step alone proves it.

Replace L by the span L_10 of the 10-by-10 minors of b. These are homogeneous degree-ten forms, and their common base support is

    {rank b≤9}=Z_5.

Exactly the regular-sequence construction in Section 2, now using (8), produces a pure complete-intersection curve W_10 of degree 10³=1000 from three members of L_10.

At the generic point of any curve C⊂Z_2={rank Q≤2}, equation (1) gives rank b≤6. Cancelling a maximal invertible rank-s block as in Section 3 shows

    I_10(b)R ⊂ m^(10-s) ⊂ m⁴.

The three defining equations of W_10 therefore generate an m-primary parameter ideal q⊂m⁴ in the three-dimensional regular local ring R. Replacing 3n by 4n in Section 4 proves

    length(R/q)≥4³=64.

Let Γ_2 be the reduced sum of all curve components of Z_2. It is an actual N-invariant effective cycle, and

    64 deg Γ_2 ≤1000,
    deg Γ_2 ≤15.

The small invariant-cycle exclusion forces Γ_2=0. Since Z_2⊂Z_5, this proves

    dim Z_2≤0: the entire rank-at-most-two middle locus is finite.  (9)

This stronger result uses (8), whereas the rank-at-most-one finiteness of Sections 1–5 remains independent of decic closure.

Finally, retain the previously proved independent-zero fiber bounds collected in /research/hm/rank-four/quintic-surface-classification/RANK_AT_MOST_THREE_COROLLARY.md, Section 2, including impossibility of residual rank zero. Equations (8) and (9) then give:

- residual rank one: affine independent-zero dimension ≤0+3+3=6;
- residual rank two: affine independent-zero dimension ≤0+2+3=5;
- residual ranks three, four, or five: affine independent-zero dimension ≤1+2+3=6;
- residual ranks at least six: affine independent-zero dimension ≤6 by /research/hm/middle-surface/rank-six-surface-reduction/COROLLARY.md.

Thus, with the additional established premise (8), every independent-zero component has affine dimension at most six. Dependent triples and tuples with a zero input are outside this last assertion and require their separate established analysis.
