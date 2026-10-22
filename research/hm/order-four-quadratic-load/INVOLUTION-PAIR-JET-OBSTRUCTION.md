# Exact two-jet obstruction along the exceptional pairing involution

## Setup

After fixing the first eight double points on Gamma and removing their double-zero divisor, suppose the remaining restriction space is

    W=span{a^2,ab,b^2,c} inside H^0(P^1,O(8)),

where a,b are coprime binary quartics and the four displayed sections are independent. These are conditional hypotheses for this lemma, not established assertions about the actual residual system. In particular, removing the first eight roots from the actual quadratic restrictions has not yet been shown to leave coprime a,b. The exceptional block relation restricts the last quadratic factor f to a projective line (a pencil) in P(H^0(O(2))). When this pencil is base-point-free it defines a degree-two map P^1 -> P^1, hence a deck involution T. A general member has roots p and Tp. No genericity of T relative to W is assumed.

Let V_8 denote the ambient quartics double at the first eight marked points. Its restriction to Gamma can have a kernel consisting of quartics containing Gamma. The space W here is the restriction image after dividing by the eight double base zeros, not automatically an isomorphic copy of V_8. Vanishing of a restriction twice at a point is necessary for ambient double vanishing, but does not impose its normal derivatives. Neither that restriction kernel nor the normal-jet conditions are addressed by this determinant lemma.

## 1. The intrinsic obstruction has degree ten

On P^2=P(H^0(O(2))), multiplication by the square of the universal quadratic gives a vector-bundle exact sequence

    0 -> H^0(O(4)) tensor O_P2(-2)
      -> H^0(O(8)) tensor O_P2
      -> E -> 0.

Multiplication by a nonzero quadratic squared is injective on binary quartics, so E is locally free of rank four. Its fiber at f is H^0(O(8))/(f^2 H^0(O(4))). Its determinant is O_P2(10).

The map W tensor O -> E therefore has a determinant Delta_W, a homogeneous degree-ten polynomial in the three coefficients of f, up to a nonzero scalar depending on the chosen basis of W. It vanishes exactly when a nonzero element of W is divisible by f^2. For a reduced factor with roots p,Tp, this says exactly that some W-section vanishes doubly at both points. Repeated-root factors are also treated correctly: then divisibility means a quadruple zero.

Restricting Delta_W to the actual last-factor pencil gives a binary degree-ten polynomial. If it is not identically zero, only finitely many (at most ten, counting multiplicity) members of that pencil permit the double pair. Thus nonidentity of this explicitly specified polynomial excludes, for a general last pair, every candidate with NONZERO restriction in this four-dimensional W. To exclude ambient candidates as well, one also needs injectivity of V_8 -> W or a separate exclusion of its Gamma-containing kernel by normal-jet conditions. Identity is a genuine possibility, as Section 4 shows.

## 2. Explicit rational-function identity

On a dense affine open where a does not vanish, divide the four sections by a^2 and put u=b/a, v=c/a^2. For two distinct points x,y where u'(x) and u'(y) are nonzero, elementary row elimination gives the jet determinant

    det[ values and derivatives of 1,u,u^2,v at x and y ]
      = u'(x)u'(y)(u(y)-u(x))
        * ((u(y)-u(x))((dv/du)(x)+(dv/du)(y))
           -2(v(y)-v(x))).

Here the derivative at y is with respect to its own local coordinate, not the derivative of the composite v(Tx). Restoring a^2 multiplies this expression by a(x)^4 a(y)^4 and nonzero jet-trivialization factors.

If u(Tx)=u(x) identically, the first three columns have rank at most two on the paired jets, so the full determinant is identically zero for every v. Otherwise the nontrivial obstruction vanishes identically precisely when

    (u(x)-u(Tx))((dv/du)(x)+(dv/du)(Tx))
      =2(v(x)-v(Tx))

as a rational-function identity. This is the exact condition, with no assumption that c lies in the span of the three squares.

## 3. Even/odd description

Choose a coordinate x with T(x)=-x, and put z=x^2. Write uniquely

    u(x)=E(z)+x O(z),
    v(x)=F(z)+x G(z),

with rational E,O,F,G. Assume O is nonzero, so u is not T-invariant. A direct substitution into the identity in Section 2 gives

    (O+2z O')(O G'-G O')
      +2E'(G E'-O F')=0,

where primes now mean differentiation in z. Equivalently, putting R=G/O, it is

    2E' F' = 2R(E')^2 + O(O+2z O')R'.

This form also shows why a naive classification by invariant u or quadratic v fails. If E is constant, the equation reduces to R'=0 (the factor O+2zO' is not the zero rational function for nonzero rational O in characteristic zero). Thus in that case precisely

    v=F(x^2)+lambda (u-E)

satisfies the identity, with arbitrary rational F subject to the original degree and pole constraints. Many such v are not quadratic polynomials in u.

## 4. A base-point-free quartic-pencil counterexample

Take homogeneous coordinates [s:t] and

    a=s^4+t^4,
    b=s^3 t,
    c=t^8,
    T([s:t])=[s:-t].

The quartics a and b have no common zero. The four sections a^2,ab,b^2,c are linearly independent: ab is odd in t, while among the even sections the s^8 term occurs only in a^2 and s^6t^2 only in b^2, leaving c independent. The three even sections span a three-dimensional space. For every nonfixed pair p,Tp, requiring an even section to vanish doubly at p automatically imposes the same condition at Tp, and gives at most two linear conditions on this three-space. Hence a nonzero section exists, and the paired-jet determinant is identically zero.

In this example u=x/(1+x^4) is nonconstant and T-anti-invariant, not T-invariant, while v=x^8/(1+x^4)^2 is even and not in span{1,u,u^2}. Thus the proposed implication that identity forces invariant u or redundant c is false even with coprime quartics of the required degree.

## 5. Lower-dimensional restriction images

If the actual restriction image W has dimension r<4, its map W tensor O -> E is represented locally by a 4 by r matrix. The condition for a nonzero restricted section divisible by f^2 is rank less than r, defined by its maximal r by r minors. One cannot use a 4 by 4 determinant by adding dependent or nonexistent sections. The same distinction between nonzero restrictions and ambient Gamma-containing candidates remains necessary.

## Conclusion and remaining actual input

Under the displayed four-dimensional hypotheses, the restriction-level double-pair question is equivalent to vanishing of the degree-ten determinant Delta_W on the last-factor pencil. If its restriction to that pencil is nonzero, it excludes nonzero restricted candidates for a general pair. This alone does NOT exclude ambient quartics containing Gamma. An ambient exclusion additionally requires injectivity of V_8 restriction, or a separate normal-jet exclusion for its kernel. No actual coprimeness of the residual quartics a,b is claimed here.

Even within the conditional coprime, four-dimensional setting, nontriviality does not follow from the degree data: the counterexample exhibits an involution-compatible system with identically zero determinant. Additional actual geometry of the restriction image and the block involution is needed, and the normal-jet issue is separate. This note proves no exceptional-block geometric exclusion.
