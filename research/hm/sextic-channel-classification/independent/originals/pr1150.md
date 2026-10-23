# Linear saturation of the complementary icosahedral sextic system

## Scope and public inputs

Work over C with G=SL2(F5), defining doublet W, nonstandard triplet V, and the multiplicity-one four-dimensional representation P in Sym6 W=V+P. Fix the determinant self-duality of W. The system P consists of its universal binary sextics, not selected actual HM coefficients. Public PR1147 at 176645bb2f022b68f86414ced87667a45e4930e2 establishes the complementary V net; its full proof and exact character source are retained. PR1148 at cc0b79801a3e9080d1a4f1d380cfa64db776dba9 supplies context for the partial-system apolar method. All three complete files are immutable-pinned and independently fetched in INPUTS.json.

We prove an exact syzygy sequence for P, sharp linear saturation, its graded resolution, and a corresponding universal apolar obstruction. None is counted as a new actual-profile exclusion. Actual profile coverage remains separate.

The character identities used are

    Sym6 W=V+P, V tensor W=T,
    P tensor W=W'+T=Sym7 W,
    P tensor Sym2 W=V+P+D, Sym8 W=P+D.

All symbols use the retained public convention. These identities are checked exactly; representation dimensions alone do not prove the polynomial multiplication maps below.

## 1. Basepoint-free evaluation and the linear multiplier

The system P has no common zero. Its common-zero divisor, if nonempty, would be invariant and have degree at most six. Projective G acts as A5; a finite point stabilizer on P1 embeds into the tangent multiplicative group and is cyclic. A5 has cyclic subgroups of order at most five, so every orbit has at least twelve points. An invariant divisor of degree at most six is impossible.

Hence evaluation is an exact sequence of equivariant vector bundles

    0 -> T_P -> P O -> O(6) -> 0.                  (1)

Its kernel has rank three and degree -6. Since P->H0(O(6)) is the coefficient inclusion, H0(T_P)=0. Every ordinary splitting degree of T_P is therefore at most -1, and every degree of T_P(1) is at most zero. In particular h0(T_P(1))<=3.

Consider the actual polynomial multiplier

    mu_1:P tensor W -> Sym7 W.

Both sides are W'+T, with multiplicity one. Its W' channel is nonzero: the full multiplication Sym6 W tensor W -> Sym7 W is surjective, while the complementary V tensor W=T has no W'. Its T channel is also nonzero: otherwise the six-dimensional T would lie in ker(mu_1)=H0(T_P(1)), contradicting the upper bound three. Thus Schur's lemma gives an isomorphism

    P tensor W -> Sym7 W.                          (2)

This uses actual multiplication and kernel geometry, not merely identical source and target characters.

## 2. Balanced kernel and exact character

Equation (2) implies H0(T_P(1))=0, so every splitting degree of T_P is at most -2. Since its rank is three and degree -6, T_P is ordinarily O(-2)^3. Therefore T_P(2) is trivial and evaluation identifies it equivariantly with its three-dimensional section representation U tensor O. Twisting (1) by two and taking sections gives

    0 -> U -> P tensor Sym2 W -> Sym8 W -> 0,

because H1(T_P(2))=0. The character identities above give U=V. Consequently

    0 -> V O(-2) -> P O -> O(6) -> 0               (3)

is the exact equivariant evaluation sequence. It is nonsplit, since Hom(O(6),P O)=0. No coefficient choice is used.

## 3. All multipliers and the finite quotient

For d>=0 let mu_d:P tensor Sym^d W -> Sym^(d+6) W be polynomial multiplication. Cohomology of (3) twisted by d gives

    0 -> V tensor H0(O(d-2)) -> P tensor Sym^d W
      -> Sym^(d+6) W -> V tensor H1(O(d-2)) -> 0.

Thus mu_0 is the coefficient inclusion with cokernel V; mu_1 is an isomorphism; and for every d>=2 the map is onto with kernel V tensor Sym^(d-2) W. In dimensions,

    rank(mu_d)=min(4(d+1),d+7),
    dim ker(mu_d)=max(3d-3,0),
    dim coker(mu_d)=max(3-3d,0).

The smallest surjective multiplier degree is one. Pure dth powers span Sym^d W in characteristic zero, so the span of l^d P for all parameter lines l is the entire Sym^(d+6) W for every d>=1.

Let R=Sym(W), R_n=Sym^n W for n>=0 and zero otherwise, and I=(P). The bundle isomorphism (3) identifies the whole graded syzygy module, compatibly with multiplication, with V tensor R(-8). Therefore the minimal equivariant free resolution is

    0 -> V tensor R(-8) -> P tensor R(-6)
      -> R -> R/I -> 0.                            (4)

The entries of the first map have positive degree two and the generators have degree six, proving minimality. Exactness follows from the kernel bundle in every graded degree, not a Hilbert-series fit. The quotient has Hilbert series

    (1-4t^6+3t^8)/(1-t)^2
      =1+2t+3t^2+4t^3+5t^4+6t^5+3t^6.

Its length is 24. Its equivariant pieces are Sym^n W for 0<=n<=5, then V in degree six, and zero for n>=7. In particular I contains every form of degree at least seven. This universal quotient is not an actual HM obstruction space.

## 4. Complementary partial-system apolar criterion

Fix d>=1, n=d+6 and k=d-1. Let F be an equivariant saturated negative subbundle of a constant ambient H O of dimension M, and put S=(H O/F)*. Assume H0(S)=0, an equivariant saturated line C=O(-n) in S with the standard linearization, and actual osculating containment of C through order k in S. Assume also an equivariant bundle decomposition

    F=F_high direct-sum P O(-d),

with all ordinary degrees of F_high greater than -d. The decomposition need not be horizontal. Then the coefficient map Sym^n W -> H* of C is injective and

    codim(F,H O)>=n-3.

If F_high is nonzero, the stronger bound codim(F,H O)>=n-2 holds. This nonzero-high case necessarily has d>=2, since at d=1 no negative integer degree exceeds -1.

Proof. Initially let q:Sym^n W -> R subset H* be the possibly partial coefficient quotient. Duality injects R* into (Sym^n W)*. Compose the actual projection of F into R* O with that injection. Its annihilation of the projected kth osculating directions pulls back to annihilation of the full universal fibers l^7 Sym^(d-1) W. The apolar annihilator of these fibers is l^d Sym6 W, a saturated bundle Sym6 W O(-d). Thus the projection factors into that bundle even before completeness is known.

Degree vanishing kills F_high. On P O(-d) the channel is scalar into the unique P in Sym6. It is nonzero: otherwise a nonzero constant R would lie in S, contrary to H0(S)=0. Hence R* contains l^d P for every l. Section 3 proves that these span the entire degree-n space for d>=1. Thus dim R=n+1. If r=rank F_high, this high block lies in the constant projection kernel of dimension M-(n+1), so r<=M-(n+1). Since rank F=r+4, the weak bound follows.

If r>0, equality is impossible. The high block is saturated in H O because it is a bundle summand of saturated F. Its quotient in the constant kernel is torsion-free and hence locally free. Equal ranks would force the high block to equal that constant kernel, contradicting its negative degrees. The strict integer inequality gives the stronger bound. This is actual saturation, not an assumption that the source decomposition commutes with differentiation.

Both bounds have sharp abstract models. For the first take F=P O(-d) in H=Sym^(d+6) W, with fiber l^d P. Multiplication is fiberwise injective and saturated; the span theorem gives H0(S)=0. The complete polynomial line l^n and derivatives through d-1 belong to its apolar annihilator. This gives codimension n-3. For d>=2, add W O(-1) in Sym2 W O by multiplication by l. It is saturated and spans its three-dimensional ambient, has degree -1>-d, and increases codimension by one. Thus the nonzero-high bound n-2 is attained. These are universal abstract models, not HM realizations. If H is center-even, n must be even; the even-n models respect this restriction.

## Evidence and limits

The verifier authenticates all full source files, proves exact character controls from the public recurrence, checks all finite ordinary kernel partitions, multiplication characters, Hilbert formulas, universal rank bounds and sharp models, and formal apolar monomial pairings. Normal and optimized Python must reproduce RESULT.json identically. The written bundle arguments establish the unbounded statements; finite checks support but do not formally certify them. No actual-source coefficients, parameter values, points, tensors, jets, matrices, instance ranks or stopped experiments are evaluated. This result neither selects an actual source nor closes profile11, global coverage, full-adjoint invertibility or the original repair.
