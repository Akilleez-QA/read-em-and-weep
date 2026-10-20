# Integral Schrödinger-normalizer curves have degree divisible by fifty

## Theorem

Let V be the five-dimensional complex Schrödinger representation of H_5, and let N=A semidirect SL_2(F_5) be its standard projective normalizer in PGL(V), with A=F_5^2 and |N|=3000. If C is an integral N-invariant curve in P(V), then

    50 divides deg C.

In particular, the smooth integral degree-seventy candidates in ../degree-seventy-smooth-frontier/PROOF.md do not exist. Conditional on that proof's stated dependencies, there is no N-invariant reduced curve of total degree seventy without line or conic components.

This is a polarization obstruction. It uses neither the actual source tensor nor any rank-locus-specific equations, and does not require a Rao-module computation or the candidate genus classification.

## 1. Canonical linearization of the fifth power

Let Ntilde be the inverse image of N under SL(V) -> PGL(V). Its central kernel is mu_5. The tautological O(-1) is Ntilde-linearized, with the kernel acting by its scalar character. Therefore O(5) has trivial kernel action and inherits an N-linearization. Let nu:X -> C be the smooth normalization, to which the N-action lifts uniquely. The pullback

    M=nu*O_C(5),     deg M=5 deg C,

is consequently an N-linearized line bundle on X. Pullback under normalization preserves the degree of a line bundle.

No choice of linear Weil representation or split central extension is needed here.

## 2. Every projective order-five element admits an order-five SL(V) lift

Use a Schrödinger basis e_j, j in F_5, a primitive fifth root zeta, and operators

    X e_j=e_(j+1),   Z e_j=zeta^j e_j,   D e_j=zeta^(j^2)e_j.

Each of X,Z,D has determinant one and fifth power identity. For D, det D=zeta^(sum j^2)=1, since sum j^2=0 in F_5. The projective D induces a nontrivial unipotent on A. Every nontrivial unipotent in SL_2(F_5) is conjugate to the action induced by D^t for some t in F_5^*. This follows by choosing an oriented basis beginning with its invariant line; allowing all nonzero t covers both conjugacy classes.

The projective splitting and exact intertwining description are proved in ../rank-three-line-rank-constancy/PROOF.md, Section 2. Hence every projective element whose quotient in SL_2(F_5) has order five is conjugate in N to an element represented by

    B = zeta^c X^a Z^b D^t

for a,b,c in F_5 and t nonzero. All these representatives have determinant one. They act as

    B e_j = zeta^(c+bj+tj^2) e_(j+a).

If a=0, B is diagonal with fifth-root entries, so B^5=I. If a is nonzero, iteration traverses every element of F_5, and

    B^5 e_j = zeta^[sum_(k in F_5)(c+bk+tk^2)] e_j = e_j,

because sum 1=sum k=sum k^2=0 in F_5. Thus B^5=I again. The same calculation with t=0 covers pure translations in A.

An order-five element of N has quotient either identity or order five, so these cases exhaust it. Conjugation by any linear representative preserves determinant and order. Consequently every order-five element of N has an SL(V) lift of order five. In fact every SL(V) lift has order five, since the lifts differ by mu_5.

At a fixed projective point, such a lift acts on its tautological line by a fifth root of unity. Its action on O(5) at that point is therefore trivial. We conclude:

    Every order-five subgroup of a point stabilizer on X acts trivially on the fibre of M: its image in C is a fixed projective point, and the pullback fibre has the same action.

## 3. Stabilizer orders

The curve spans P(V): its linear span is H_5-invariant, and V is irreducible. The N-action on C, and hence on X, is faithful. Indeed, if a projective transformation fixes C pointwise, the irreducible curve lies in one projective eigenspace of a lift; nondegeneracy makes that eigenspace all of V.

A stabilizer of a point of X is cyclic, since its derivative acts faithfully on the tangent line. The nontrivial element orders of N are among

    2,3,4,5,6,10.

Here is a direct verification. Write an element as (a,s) in A semidirect G. If s-I is invertible, a translation conjugates it to (0,s). Element orders in G are 1,2,3,4,5,6,10, from the eigenvalues of determinant-one matrices over F_5. If s has eigenvalue one, it is either identity or s=I+J with J^2=0. In the latter case

    (a,s)^5=((I+s+s^2+s^3+s^4)a,I)=(0,I),

because the sum is 5I+10J=0 in F_5. The identity case gives a pure translation. Thus there is no larger cyclic stabilizer.

## 4. Equivariant divisor arithmetic

There exists a nonzero invariant rational section sigma of M. One can obtain it by Galois descent of the one-dimensional semilinear k(X)-space of rational sections, or directly by Hilbert theorem 90. This does not assert existence of an invariant regular section. Its divisor is an integral N-invariant divisor, with negative coefficients permitted.

At a point p of X with stabilizer order e, choose a local parameter t such that a generator acts with a primitive e-th-root derivative. The leading term of sigma shows that the multiplicity m_p of its divisor agrees, up to sign, with the fibre character exponent modulo e. In particular, when 5 divides e, triviality of the order-five fibre character forces

    5 divides m_p.

Equivalently, restrict to the order-five subgroup and compare the leading Laurent term t^(m_p) with its invariant image. This avoids any character-sign convention.

Since each orbit has size 3000/e and the divisor coefficient is constant on it, each orbit contributes to deg M as follows:

    e=1:  3000 m
    e=2:  1500 m
    e=3:  1000 m
    e=4:   750 m
    e=5:   600 m, with 5|m, hence a multiple of 3000
    e=6:   500 m
    e=10:  300 m, with 5|m, hence a multiple of 1500.

Every contribution is divisible by 250, even for negative m. Summing the finitely many contributions yields

    250 divides deg M = 5 deg C,

and therefore 50 divides deg C, as claimed.

## 5. Degree seventy and narrower signature consequences

The component argument in Section 2 of the cited degree-seventy smooth-frontier theorem proves that every N-invariant reduced degree-seventy curve without line or conic components is integral. The present theorem contradicts its degree. No use of its smoothness argument, final genus pair, or tensor-multiplicity refinement is needed.

For comparison, its genus326 case necessarily has full-N signature (3,4,5). At that signature the effective orbit contributions are 1000,750,3000, again giving 250|deg M. At genus351 the possible signatures are (3,3,10) and (2,6,10); the latter cannot generate N because its projected involution in G is central, and a product-one triple containing it generates an abelian subgroup of G. Signature (3,3,10) yields contributions1000,1000,1500, hence the stronger100|deg C. These observations are optional and are not used in the general theorem.

To verify the short signature list without computation, RH gives quotient genus zero and either three or four branch points: its positive value is13/60 or7/30, both less than1/4. Four branch points have smallest positive value1/6, next1/4, so neither value occurs. For triples, solve the reciprocal sums47/60 and23/30 with entries in{2,3,4,5,6,10}. With smallest entry at least4 the sum is at most3/4. With smallest entry3, the only solutions are(3,4,5) and(3,3,10); with smallest entry2, the only solution is(2,6,10).

## 6. Scope and next step

The theorem applies to integral invariant embedded curves, whether smooth or singular, because the argument takes place on their smooth normalization. It does not by itself imply degree divisibility by fifty for components permuted nontrivially by N; their individual stabilizer groups can be smaller. A reduced reducible curve must first be analyzed by its component orbits.

The immediately needed next step is an independent audit of the SL(V) order-five lift calculation and the invariant rational divisor argument, followed by incorporation of the degree-seventy exclusion into the existing frontier. Only local proof files and abstract finite-group/curve calculations were used. No actual source-instance evaluation is claimed.
