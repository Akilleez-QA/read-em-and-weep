# The 750-point candidate is excluded by plane quintic interpolation

## Result and dependencies

Under the standing hypotheses and audited dependencies of
`../../rank-four/rank-five-finite-support-constraints/PROOF.md`, no orbit of size 750 belongs to Z5.
Consequently its support-cardinality alternatives sharpen to

    |Z5,red| in {0,250,375,600,625}.

The 600-point case remains the distinguished nonzero-cocycle orbit M. The 625-point case remains O250 union O375. No assertion of occurrence is made.

The new argument uses only:

1. A 750-point candidate has stabilizer C4 and, after translation conjugacy, lies in the positive plane P(T) of the central involution c in K=SL2(F5). It avoids the invariant conic C={q=0}, and the canonical eigenpoint set E.
2. Outside E the translation group A acts freely. A point outside E is fixed by at most one involution of N=A semidirect K.
3. The effective action of K on T is the irreducible orthogonal three-dimensional A5 representation.
4. On C both the even and odd blocks have rank at least five, proved in `../../rank-four/rank-five-canonical-conic-exclusion/PROOF.md` and its audited dependencies.
5. Both parity blocks over P(T) are linear matrices. Their five-minors are homogeneous plane quintics, and their ranks are constant on each K-orbit because the central involution commutes with K. Rank b = rank b_even + rank b_odd, and rank Q = rank b - 4.

In fact, the proof excludes any Z5 point in the positive plane whose A5 orbit has more than 25 points and avoids C and E.

## 1. There are no new invariants of degree at most five

For the action of A5 on T, the multiplicities of the trivial representation in Sym^d(T*) for d=0,...,5 are

    1, 0, 1, 0, 1, 0.

For a direct check, use class sizes 1,15,20,12,12 with element orders 1,2,3,5,5. The generating series for symmetric-power characters at a given element g is

    sum_d trace(g | Sym^d T) t^d = 1/det(1-tg).

The eigenvalues are (1,1,1), (1,-1,-1), (1,omega,omega^-1), and (1,zeta,zeta^-1), (1,zeta^2,zeta^-2). For d=0,...,5 the respective character rows are

    identity:       1, 3, 6, 10, 15, 21
    involution:     1,-1, 2, -2,  3, -3
    order three:    1, 0, 0,  1,  0,  0
    order five A:   1,phi,1,  0,  0,  1
    order five B:   1,phibar,1,0,  0,  1,

where phi+phibar=1. Averaging with the displayed class sizes gives the asserted multiplicities. The same counts hold for T* since T is orthogonal.

The invariant quadratic q is nonzero, so the invariants in degrees two and four are exactly Cq and Cq^2. Thus every nonconstant homogeneous invariant of degree at most five is a scalar multiple of q or q^2.

### Geometric verification without characters

There is also a shorter verification, supplied by the independent auditor. Every A5 orbit on the invariant conic C has at least twelve points. If an invariant homogeneous form F of degree 1<=d<=5 restricts nontrivially to C, its zero divisor is invariant of positive degree 2d<=10, impossible. Thus q divides F. The quotient F/q is again invariant, since q is invariant. Induction shows that an invariant of degree at most five is a scalar power of q; odd degrees have no invariants. This gives exactly the invariant statement used below, independently of the trace table.

## 2. Quintic interpolation for large off-conic orbits

**Lemma.** If O is an A5 orbit in P(T), O is disjoint from C, and |O|>25, no nonzero homogeneous quintic vanishes on O.

Suppose otherwise, and let L=I(O)_5 be the nonzero vector space of all quintics vanishing on O. It is A5-stable. Let D be its homogeneous greatest common divisor, defined up to scalar. The line CD is A5-stable, and hence affords a character. A5 is perfect, so that character is trivial. By Section 1, D is constant or is proportional to q or q^2.

Since q never vanishes on O, division by D yields a nonzero linear system L' of forms of degree m=5-deg D, every one of which still vanishes on O. By definition of D their gcd is constant. Choose a nonzero F in L'. For each of its finitely many irreducible factors, the subspace of L' divisible by that factor is proper. Over C, choose G outside the union of those subspaces. Thus F and G have no common component.

Bezout now gives

    |O| <= m^2 <= 25,

a contradiction. This proves the lemma. The same reasoning includes a one-dimensional L': a nonconstant single polynomial cannot have constant gcd, so that case would already force D to have degree five, which Section 1 excludes.

## 3. The candidate's plane orbit has exactly 30 points

Let p be in a genuine N-orbit of size 750. Its stabilizer S has order four. The central-involution cocycle conjugation places S in K, and the previous location theorem puts p in P(T), away from C and E. Hence its K-stabilizer is exactly S, and

    |K p| = 120/4 = 30.

Equivalently its effective A5-stabilizer has order two. Denote this plane orbit by O. Since C and E are invariant, O is disjoint from both. No off-conic parity-rank lower bound is needed.

For completeness, each point of the full orbit belongs to only one canonical positive plane: membership in two such planes would give two distinct fixing involutions, contradicting free A-action outside E. Therefore the 750-point orbit distributes as 30 points in each of the 25 positive planes. Only the standard plane's 30-point orbit is needed below.

## 4. Parity quintics give the contradiction

If p belongs to Z5, then rank b_p<=9. Because the parity ranks add to this total, at least one of the two blocks has rank at most four at p. Fix such a block. Each block is K-equivariant separately, since c is central in K, so that same block has rank at most four throughout O.

All five-minors of this fixed block therefore vanish on O. They are homogeneous quintics on P(T). The interpolation lemma forces every such minor to be the zero polynomial on the entire plane. Thus this block has rank at most four at every point of P(T), including every point of C.

This contradicts the established pointwise rank lower bound five on C for each of the two parity blocks. Therefore p cannot belong to Z5, excluding the 750-point alternative. In particular, this proof does not assume an even-rank lower bound away from the conic.

## 5. Why the isolated polar-line argument alone is weaker

If u is the C4 generator, its -1 eigenspace U in T has dimension two. The setwise stabilizer of P(U) inside K is the inverse image of the centralizer of its involution in A5, namely Q8 of order eight. Its effective action on P(U) has order two; it is not the order-24 binary tetrahedral normalizer of a whole Q8 subgroup. The latter permutes its three associated polar lines.

Indeed P(U) is the polar line of the unique +1 axis of u, so its setwise stabilizer equals that axis's stabilizer. The axis belongs to O375 and has K-stabilizer Q8. On U, Q8 factors through V4, with the chosen involution scalar and the remaining quotient acting by an involution. A generic point thus contributes only two points to this line.

Consequently the constant binary-image quotient and its degree-eight minors alone give only an eight-point bound, compatible with such a pair. The new proof uses all fifteen translates of the line simultaneously through their 30-point plane orbit, and uses degree-five parity minors rather than degree-eight total quotient minors. No matrix evaluation is involved.

## Evidence boundary

This is a representation-theoretic and plane-interpolation argument. It evaluates no actual source coefficient, source tensor, chosen-input value, operation matrix, rank instance, jet, or residue. It performs no external write or large computation. The only new artifact is this proof file.
