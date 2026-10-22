# No off-diagonal divisor forces residual injectivity in types I, II, V

## Theorem

If the actual target F4 has type I,II orV, the actual residual map

    m_res: W tensor S6* -> K8

has generic rank four. This does not select the actual target type, and it does not prove full-adjoint maximal rank.

More generally, in the zero-leading-scalar branch, a residual generic rank-two map with no off-diagonal divisorial common zero of the pure raw cross block must have exact generic diagonal order eight.

## 1. The leading scalar controls every same-root residual block

Use affine ell(z)=u+zv. Write a(z):Sym^2 W->Sym^2 D5 for the actual square map and b(z)=ell(z)^4 symmetric-product ell(z)^4. At a fixed root r, the residual coefficient space is ell_r W. The same-root block is delta_r(q0 a'(r)c).

For c=ell_r^2, a'(r)c=6 ell_r^4 symmetric-product ell_r^3 v is itself a same-root square product, so the boundary kills it.

For c=ell_r v, put

    S=ell_r^3 v symmetric-product ell_r^3 v,
    T=ell_r^4 symmetric-product ell_r^2 v^2.

Differentiation in the actual symmetric-square space gives

    a'(r)(ell_r v)=3S+3T,
    b''(r)=32S+24T.

The actual boundary kills S, a same-root square. Consequently

    delta_r(q0 a'(r)(ell_r v))
       =delta_r(q0 b''(r))/8.                       (1)

The leading diagonal scalar lambda controls delta_r(q0 b''(r))/2 as an invariant section. Thus lambda=0 makes every same-root residual block zero, identically in r. This calculation retains the low component of S; it does not replace an actual square by its Cartan projection.

If lambda is nonzero, the previously proved Hermite and divisor theorem already gives generic rank four in types I,II,V. It remains to exclude rank two when lambda=0.

## 2. Rank two makes each cross block rank one

At distinct roots, the residual source is the sum of two independent two-dimensional root spaces, and the target is the sum of two independent four-dimensional root targets. With (1), its only nonzero blocks are the two cross blocks. Invertible complementary-root normalization factors change neither block ranks nor the conclusion.

Let

    R(r,s)=delta_r(q0 b(s)).

At source s, write a W-vector as alpha ell_s+beta v. Its leading residual square is

    alpha b(s)+beta b'(s)/8.

The cross-block image at target r is therefore spanned by

    R(r,s), partial_s R(r,s),                       (2)

up to nonzero scalar factors. The derivative holds r and its target boundary fixed.

The two cross blocks have equal generic rank, since exchanging r and s exchanges them. Their target summands are disjoint. Hence residual generic rank two forces each generic cross rank to be one. Nonzero R is already established by actual pure-square nonvanishing, so (2) implies

    R wedge partial_s R = 0

over the function field of the ordered-root surface.

## 3. Constant projective direction produces a divisor unless k=8

Set K=C(T_r). Trivialize the target at its generic point. Then R is a nonzero vector-valued section of O_P1(8) over K. The preceding wedge identity says that every ratio of two nonzero components has zero s derivative. In characteristic zero the constants of K(s) under this derivative are exactly K. Thus

    R(r,s)=v(r) f(r,s),

where v is a nonzero target vector over K and f is a homogeneous scalar section of O_P1(8) over K.

Let k be the exact generic order of R along the diagonal s=r. Divide f by the corresponding diagonal factor to order k. The result is a nonzero scalar section of O_P1(8-k), with nonzero value at s=r.

If k<8, its zero divisor is nonempty after algebraic closure of K, with degree8-k, and is disjoint from s=r. Taking its closure in T_r x T_s gives a nonempty divisorial common-zero cycle of R away from the diagonal. Dividing R by D^2 does not change that off-diagonal cycle.

This uses homogeneous degree, so a zero at infinity is retained. Rational choices of the target vector or frame may add or remove vertical divisors over nongeneric r, but cannot remove this divisor over the generic r-fiber. The conclusion therefore descends to an actual off-diagonal divisor of the cross section.

Consequently absence of off-diagonal divisorial common zeros forces k=8.

## 4. Apply the actual target-type restrictions

The established divisor theorem excludes off-diagonal divisorial common zeros for types I,II,V. Their universal diagonal-order lists are

    I,II: k in {2,4,5};
    V:    k in {2,4,6}.

In the lambda=0 branch, k=2 is excluded, but k=8 is unavailable in every case. Section 3 therefore contradicts the residual rank-two assumption.

The actual residual map is already known to have generic rank two or four. Thus its generic rank is four for each of these three possible target types. This eliminates their rank-two alternatives without selecting lambda, k, or any actual coefficient.

## 5. Two further conditional target-component exclusions

In type III, F4=V O(4) plus O(12), the only possible off-diagonal common-divisor bidegree is(9,3). Such a divisor would force the V O(4) component of T2 to vanish. Therefore if that actual component is nonzero, there is no off-diagonal common divisor. Type III has maximal raw diagonal order five, so the same argument gives residual generic rank four.

In type VI, F4=O plus W' O(5) plus O(14), the only possible off-diagonal common-divisor bidegrees are(10,2) and(14,6). Either forces the W' O(5) component of T2 to vanish. Therefore a nonzero actual W' O(5) component excludes all such divisors. Type VI has maximal raw diagonal order six, so again the residual generic rank is four.

For both statements, if lambda is nonzero the exact Hermite calculation excludes discriminant torsion, and no off-diagonal torsion remains; the previously proved torsion necessity excludes rank two. If lambda is zero, Sections 1-3 apply directly. Neither component is asserted to be nonzero here.

## Sources and limits

THREE-TARGET-TYPES-WITHOUT-OFF-DIAGONAL-TORSION.md gives the off-diagonal divisor exclusions and the nonzero-scalar rank-four implication. CONDITIONAL-DISCRIMINANT-FACTOR-AND-EXACT-TORSION.md gives the finite diagonal-order lists. TWO-ROOT-DIVIDED-DIFFERENCE-SMOOTHING-FORMULA.md and the pure cross-block theorem give the actual block formulas and their normalization.

The argument is over generic roots and proves generic rank. It does not assert every individual fiber has full rank, select the actual target splitting, or settle the positive adjoint excess. No selected coefficients, actual matrices, numerical ranks or experiments are evaluated.
