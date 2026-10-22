# Quadric jet divisibility excludes the high vertical image degrees

## New conclusion

Under the primitive twist-two spectral hypotheses and the nondominant classification of TWIST-TWO-VERTICAL-IMAGE-CLASSIFICATION.md, the degree-five and degree-ten image alternatives are impossible. The only remaining nondominant image has degree two, with five evaluation base points of eigenquotient multiplicity two. Consequently the forced cubic on Q, double at the other forty-five marked points, is the sole remaining nondominant alternative established here.

## 1. An elementary global jet lemma on a smooth quadric

Let p be a point on a smooth quadric threefold Q, and let s be a nonzero section of O_Q(d). Then ord_p(s)<=2d. More precisely, if ord_p(s)>=m>d, the divisor of s contains the tangent-hyperplane section at p with multiplicity at least m-d.

Proof: use homogeneous coordinates with p=[1:0:0:0:0] and

    Q: x0*x4=q(x1,x2,x3),

where q is a nondegenerate quadratic form. On x0=1 the three coordinates y=(x1,x2,x3) are regular parameters and x4=q(y). Represent s by a homogeneous polynomial of degree d. Each monomial x0^i y^alpha x4^j has i+|alpha|+j=d and becomes a homogeneous polynomial in y of ordinary degree

    w=|alpha|+2j=d-i+j<=2d.

Group the original polynomial into its weight-w pieces. The order hypothesis says the substituted polynomial of each weight w<m is identically zero. Such a homogeneous piece therefore restricts to the zero section on the dense affine chart of Q, hence is globally zero on Q. Remove these pieces. Every remaining monomial has w>=m, so

    j=w-d+i>=m-d.

Thus the remaining representative is divisible by x4^(m-d), proving the assertion. The bound 2d follows from the maximum possible weight. The section x4 cuts out the tangent hyperplane at p; its quadric surface is integral, and distinct points have distinct tangent hyperplanes because Q is smooth and its polar form nondegenerate.

## 2. Eigenquotient multiplicity controls the endomorphism jet

In the affine quotient chart [u:1] at an evaluation base point over p, write the trace-free endomorphism in a base-dependent frame as [[a,b],[c,-a]]. Its eigenquotient equation, up to signs and a unit, is

    c+2a*u-b*u^2.

The coefficients a,b,c depend only on regular parameters on Q, not on u. If this equation has multiplicity m in the fourfold X at (p,u=0), its distinct powers of u imply

    ord_p(c)>=m, ord_p(a)>=m-1, ord_p(b)>=m-2.

In particular ord_p(psi)>=m-2. More sharply, both a^2 and bc have order at least 2m-2, so ord_p(det psi)>=2m-2. The orders of the section psi and of its determinant are intrinsic; the separate entry bounds are used in this adapted quotient frame, not asserted invariant under arbitrary frame changes. No actual jet value is evaluated.

## 3. Stronger one-point exclusion: every multiplicity is at most four

If m>=5, the determinant has order at least eight at that point. Section 1, with d=4 and m=8, says it is divisible by the fourth power of the tangent-hyperplane section. Their degrees already agree, so the nonzero determinant must be a constant times that fourth power. Equivalently, in the affine weight proof the only possible weight-eight monomial of total homogeneous degree four is x4^4; all lower-weight pieces restrict to zero.

Such a determinant has square negative over C, contradicting the nonsquare spectral polynomial. If its order were greater than eight, section 1 would instead imply the determinant is zero, also impossible. Thus EVERY actual evaluation base-point multiplicity in the primitive twist-two case satisfies

    m_i<=4.

This does not require nondominance. It is weaker than the earlier bound m_i<=2 in the dominant case, but applies before selecting either branch.

## 4. Application to the vertical classification

The degree-five image alternative has two multiplicities equal to five, and the degree-ten image alternative has one multiplicity equal to ten. Both contradict section 3. Hence the only nondominant image is a quadric with precisely five positive multiplicities, all equal to two.

As an independent consequence of the general jet lemma, even the weaker estimate ord(det)>=2(m-2) would suffice for the two-point degree-five alternative: it forces squared tangent factors at each of its two distinct points, whose total degree is already four, again making the discriminant a square. The one-point argument above is stronger and is the main proof.

## Boundary

The remaining quadratic-image case is not excluded. In particular no bound on singular points of a possibly reducible or nonnormal cubic surface section is invoked. The argument is universal quadric-jet and divisor geometry, not a selected HM coefficient calculation, matrix-rank test, scan, or experiment. No external write was made.
