# The unique remaining 600-point orbit

## Statement and dependencies

Work over C with the Schrödinger representation V, projective normalizer N=A⋊SL2(F5) of order 3000, and the actual equivariant linear matrix b of the preceding rank-locus results. Assume the audited conclusions in ../../rank-four/rank-three-250-plane-exclusion/ADDENDUM.md: Z3 is finite, is cut out by degree-eight minors of b, avoids the thirty Heisenberg eigenpoints E, and avoids all projective fixed points of all involutions of N. Also use the established fact that A acts freely outside E. These assumptions follow from the cited operation hypotheses; no source coefficients or operation are evaluated here.

**Theorem.** Among points eligible for Z3, all those with stabilizer of order five belong to one specific N-orbit M of size 600. The other fixed loci of order-five stabilizers are excluded. Consequently

    |Z3,red| = 600a + 1000b + 3000c ≤ 4000,   a∈{0,1}, b,c≥0.

In particular, if Z3 meets M it contains all of M. Its possible nonzero cardinalities are reduced to

    600, 1000, 1600, 2000, 2600, 3000, 3600, 4000.

This theorem classifies the remaining 600-point candidate; it does not assert its presence in Z3 or exclude rank three there.

## 1. Order-five subgroups and their cocycles

Use coordinates (x,y) on A=F5². Let U be the subgroup of lower unipotents

    u(t)(x,y)=(x,y+tx).

A subgroup C of N mapping isomorphically to U has a unique generator g=(a,u(1)) projecting to u(1). Every a=(α,β) is possible: the fifth power has translation component

    Σ_{i=0}^4 u(i)a = (5α, 5β+10α)=0.

Thus there are 25 such subgroups over each U. Conjugation by (v,1) changes a to a+(1−u(1))v, varying β arbitrarily and leaving α fixed. These are exactly the five cocycle classes, not just the zero class.

For h_s=diag(s,s^−1), one has h_s u(1)h_s^−1=u(s^−2). Conjugate by h_s and then take the s²-th power to restore projection u(1). The first translation coordinate becomes s³α. Hence the four nonzero α classes are permuted transitively by the diagonal torus. Since SL2(F5) acts transitively on its six Sylow-five subgroups, all nonzero-class complements form one N-conjugacy class, consisting of 6·20=120 subgroups. The zero-class complements form one conjugacy class of 6·5=30 subgroups.

An order-five point stabilizer outside E injects into SL2(F5), so it is one of precisely these subgroups. Order-five subgroups contained in A fix only E, already excluded.

## 2. Zero-class fixed loci are excluded

A zero-class complement is conjugate to C0=⟨D⟩, where

    D e_j=ζ^(j²)e_j.

Its projective fixed locus is [e0] together with the two lines

    L1=P⟨e1,e−1⟩,   L2=P⟨e2,e−2⟩.

The point [e0] is in E. On either line, the clock Z e_j=ζ^j e_j and inversion R e_j=e−j act effectively as a dihedral group of order ten. Its nonfree orbits consist of the two coordinate endpoints (in E) and points fixed by one of its five involutions Z^kR. Each Z^kR is an involution of N, whose entire projective fixed locus is excluded by hypothesis. Every remaining point on either line therefore has a ten-point orbit under ⟨Z,R⟩.

If a remaining point p of either line belonged to Z3, all ten orbit points would belong to Z3. Each degree-eight minor restricted to that projective line would vanish at ten distinct points and hence identically. The line would be contained in Z3, contradicting its finiteness. Thus no fixed point of any zero-class complement belongs to Z3.

## 3. Nonzero-class complements have five simple eigenpoints

Fix a nonzero-class complement C=⟨g⟩. A projective lift of g has the form X^α Z^β D^3, up to a nonzero scalar and an immaterial change of β, where α≠0 and X e_j=e_(j+1). The factor D³ induces u(1). This is a monomial matrix whose permutation is a single five-cycle. Its characteristic polynomial is t^5−c for c≠0, so it has five distinct eigenvalues and exactly five projective fixed points. Every eigenvector has all five coordinates nonzero.

The subgroup B=A^U=⟨Z⟩ commutes projectively with C. Since C∩B=1, BC has order 25 and is contained in N_N(C). The 120-subgroup conjugacy-class count in Section 1 gives |N_N(C)|=3000/120=25, so

    N_N(C)=BC≅C5×C5.

For the chosen linear lifts, Zg=ζ^α gZ. Because α≠0, Z cyclically permutes the five eigenvalues and their eigenlines. Consequently this normalizer acts transitively on the five fixed points of C.

## 4. Each simple eigenpoint has stabilizer exactly C

Let p be one of these eigenpoints. First p∉E. Indeed if p∈E its nontrivial A-stabilizer is a one-dimensional subgroup B' of A. Since g fixes p, it normalizes B'. Its unipotent projection has the unique invariant line B, so B'=B. But the B-eigenpoints are the coordinate endpoints [ej], none of which is fixed by a monomial five-cycle. This is a contradiction. Thus A_p=1, by the established freeness outside E, and S=N_p injects into SL2(F5).

Suppose S contained an involution t. Its projection is the unique involution −I of SL2(F5), hence commutes with the projection of g. Therefore [t,g] belongs to A∩S=1, and t centralizes C. This would put t in N_N(C), a group of odd order 25, impossible. So S has odd order dividing 120, and contains C. Its order is therefore 5 or 15. Order 15 is impossible: an odd-order subgroup injects into A5; a subgroup of A5 of order 15 has a unique Sylow-five subgroup and would lie in its order-ten normalizer. Hence S=C and the orbit of p has size 600.

All 120 subgroups C are conjugate, and each normalizer is transitive on its five eigenpoints, so all their eigenpoints form one N-orbit M. Equivalently, stabilizer uniqueness proves the 120 sets of five points are disjoint. This establishes both the count and uniqueness, without assuming away the nonzero cocycles.

A concrete representative of M is

    [Σ_{j∈F5} ζ^(j³)e_j].

Indeed g=X Z³ D³ sends this vector to ζ^−1 times itself, because (j+1)³−j³=3j²+3j+1. The first translation coordinate of this g is 1, so its cocycle class is nonzero.

## 5. Scope and remaining question

Equivariance makes rank Q constant on M. The currently proved assumptions therefore leave exactly two possibilities: M is disjoint from Z3, or M is an entire 600-point component of its reduced support. Determining its actual residual rank remains open here. Neither the simple eigenvalue calculation nor the order-five stabilizer alone forces that rank to be at least four.

The distinct orbit-size counts from the cited addendum now have at most one 600-point summand. Combining a∈{0,1} with the degree bound gives the stated cardinality list. Scheme multiplicities are not computed or bounded separately by this classification.

## Audit request

Please independently audit: (1) the cocycle and torus s³ action, (2) the effective dihedral orbit argument on both D-eigenlines, (3) the order-25 normalizer and transitivity of eigenpoints, and (4) stabilizer exactness and the cardinality list. All computations are finite symbolic group/linear algebra; no external writes or large computation were used.
