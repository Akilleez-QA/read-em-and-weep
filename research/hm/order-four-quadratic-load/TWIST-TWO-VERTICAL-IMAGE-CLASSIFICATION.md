# Classification of a nondominant twist-two eigenquotient image

Use the notation and hypotheses of EIGENQUOTIENT-PROJECTION-BOUNDS.md, now published at 3c4ab4b2cdfb9e54012f92f798a8da34768413d0. In particular Xhat is the blowup of the fifty reduced evaluation base points, A=L-sum E_i resolves f:Xhat->P3, each E_i maps isomorphically to P3, and the primitive irreducible twist-two eigenquotient divisor has class

    That=2L-3H-sum m_i E_i.

Assume f|That is not dominant. The exact intersection identity gives sum m_i=10.

## 1. Its image must be a surface

Let D=f(That), with reduced structure. This is integral because That is integral. Since That is not an exceptional divisor E_i, its restriction to E_i is either empty or an effective divisor of degree m_i on E_i=P3. This restriction maps into D under the isomorphism f|E_i.

If dim(D)<=1, there is no such nonempty divisor on E_i, so every m_i=0. This contradicts sum m_i=10. Hence dim(D)=2. This argument does not require a uniform Bertini theorem, irreducibility of all fibers, or all-parameter claims about the fixed-beta surfaces.

## 2. Exact degree and multiplicity alternatives

Write e=degree(D). The effective Cartier pullback f*D has That as a component of some coefficient n>=1. None of the E_i is a component of f*D because each maps onto P3.

For m_i>0, the divisor That|E_i is supported on the integral surface D inside E_i=P3, hence equals r_i D for an integer r_i>=1. Restrict the effective divisor f*D-n That to E_i. This restriction is effective because E_i is not a component, and gives

    D-n r_i D >= 0.

Thus n=r_i=1. Consequently every positive m_i equals e, and e divides ten. Moreover f*D-That is effective; intersecting with the nef class H^3 gives

    0 <= H^3(f*D-That)=2e-4.

Therefore e>=2, leaving exactly

    (e, number of positive m_i) = (2,5), (5,2), or (10,1).

In each alternative every positive multiplicity is exactly e. This sharply separates the nondominant branch from the dominant branch's at-most-five multiplicities of size at most two.

## 3. The quadratic-image alternative forces a cubic double at forty-five points

If e=2, let J be the five indices with m_i=2. Then

    f*D-That = 3H - 2 sum_{i not in J} E_i

as a divisor class. This effective divisor contains no E_i as a component. Its pushforward to X is an effective divisor of class 3H. Since the projection p:X=P_Q(E)->Q has p_*O_X=O_Q, every section of O_X(3H) is pulled back from a section of O_Q(3). Therefore there exists a nonzero cubic section g on Q whose pullback's strict transform is f*D-That.

Uniqueness of the exceptional coefficients under blowup gives multiplicity exactly two at each of the other forty-five evaluation base points and zero at the five indexed by J. Pullback by the smooth bundle projection preserves multiplicity at these points. Thus g has order exactly two at those forty-five points of Z, and is nonzero at the remaining five.

One can use the weaker consequence 'order at least two at forty-five points' without the exact-multiplicity assertion. Neither version is asserted impossible here. Cubic divisors on Q may be reducible or nonreduced, and no isolated-singularity bound or unsupported interpolation generality may be substituted.

## Status and boundaries

This is a necessary classification of the nondominant twist-two case, not its exclusion. It avoids the delicate uniform-in-B Bertini issue entirely. The quadratic-image branch has the additional concrete cubic-jet obstruction above; the quintic and degree-ten image branches remain. All calculations are symbolic divisor/intersection arguments. No actual coefficients, source ranks, scans, or external writes were used.
