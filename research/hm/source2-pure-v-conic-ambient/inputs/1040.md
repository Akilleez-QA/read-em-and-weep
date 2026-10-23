# The rank-three lift line has exactly fifteen additional simple basepoints

## Theorem and boundary

Use the immutable quadratic-lift basis of PR1036 and write a universal gate
as alpha R1+beta R2, with alpha,beta independent coefficient coordinates.
Its nonic row is alpha F1+beta F2, where Fi=N L Ri in that same normalization.
The unique fifteen-point orbit of order-two rotation axes belongs to its
base scheme if and only if

    alpha+beta=0.

For a nonzero gate on this line, all fifteen AMBIENT basepoints are reduced.
Consequently the complete nonic base scheme on the exceptional rank-three
lift line is the disjoint union of the fixed Z and those fifteen reduced
axes. Its total length is

    34+15=49.

Every nonzero gate off this line has no order-two-axis basepoint. In
particular the uniform curvilinear-double possibility for that orbit in
the earlier necessary support bounds never occurs in this universal pencil.
No actual gate coefficient is selected; neither membership in this line
nor nonvanishing of the actual gate is asserted. The theorem classifies an
entire universal coefficient subspace, not an actual source evaluation.

## 1. Immutable inputs and exact polynomial interface

INPUTS.json authenticates:

- PR1036 at bb22e239e9423b54487236dba8c4f70f9e6b738f, including its unchanged
  model.py: the fixed apolar pairings, projection Pi:Sym6 W->P, lift matrices,
  nonic row formula, whole-axis ideals, and four distinct coefficient lines.
- PR1035 at 6effcd9b61b1942447a2c3f136a6776dda213c15: possible additional
  off-conic support is the fifteen-axis orbit OR a thirty-point orbit, never
  both; no free orbit occurs. It retains the conic-base dichotomy.
- PR1000 at 260cd6a777b23dc7ccd5ed956fcf65e17ff56145: the intrinsic axis orbits
  and their stabilizers in the rotation plane.

Write a=p x^2+q xy+t y^2 and delta=q^2-4pt. All p,q,t remain symbolic.
The model defines

    cP(a)=Pi(a^3),        f6(a)=cP(a)^T GP cP(a),

where GP is the invariant nondegenerate P pairing. Thus f6 and delta are
invariant homogeneous polynomials. No new arbitrary source coefficient or
normalization is introduced. The fixed model is universal representation
algebra already pinned in the prior theorem.

As in PR1036, let B(h)=Pi(a^2 h) and let N be its signed maximal-minor row.
The exact determinant identification of the torsion-free cokernel gives

    F1=N L R1,             F2=N L R2.

These are the actual two nonic component rows of the universal gate, up to
a common harmless nonzero target normalization. Their four components are
not surrogate equations selected only by representation type.

## 2. An intrinsic reduced scheme of all thirty-one axes

Consider the homogeneous critical scheme K cut out by the three minors
of the two-column Jacobian matrix (df6,d delta). Equivalently the invariant
quadratic pairing identifies df6 with a degree-five vector-valued form;
its class modulo the radial vector is a section of T_X(4), X=P(A).
Its zero scheme is exactly K.

This zero scheme is finite. On the WHOLE affine chart p=1, exact Groebner
reduction in lexicographic order q>t gives leading monomials

    q^5, q^4 t^2, q^2 t^4, q t^8, t^12.

There are 30 standard monomials. On the boundary p=0, the two projective
coordinate charts have reduced bases (t) in q=1 and (1) in t=1. Hence the
boundary has just one point and no curve component. These are polynomial
ideal calculations on full charts, not substitutions at selected axes.
The finite zero scheme of a rank-two bundle section on a smooth surface
is a regular zero locus, so its length is its top Chern number:

    c2(T_P2(4))=c2(T_P2)+4c1(T_P2)+16=3+12+16=31.

Every one of the six order-five, ten order-three and fifteen order-two
axes lies in K. Indeed delta is nonzero at these non-isotropic axes, so
f6/delta^3 is a regular invariant function near each. Its differential
at a fixed axis must be fixed by its projective stabilizer. The tangent
plane has no invariant cotangent vector: cyclic rotations give two
nontrivial opposite weights at the order-five/order-three axes, and the
Klein four gives two independent nontrivial characters at an order-two
axis. Thus that differential vanishes. This is exactly the stated critical
equation there, using Euler homogeneity.

There are 31 distinct such points, so the length31 scheme K consists of
exactly those axes, all reduced. No other critical point or hidden
nonreduced structure is possible.

## 3. The whole fifteen-axis ideal, including its chart boundary

Cut K further by the invariant sextic

    g15=f6+(3/80) delta^3.

Let J15 be the resulting homogeneous ideal. In the chart p=1 its reduced
Groebner basis is

    q^4+8q^2t-(3sqrt5/2)t^5-(3/2)t^4+sqrt5 t^3+5t^2
       +(sqrt5/2)t-7/2,
    q^2t^2+(2sqrt5/5)q^2t+q^2-(3/2)t^5-(sqrt5/10)t^4
       +t^3+(3sqrt5/5)t^2+t/2-sqrt5/2,
    qt^4-(4sqrt5/15)qt^3+(2/3)qt^2-(4sqrt5/15)qt+q,
    t^6-(4sqrt5/15)t^5-t^4/3+t^2/3+(4sqrt5/15)t-1.

Its leading ideal is (q^4,q^2t^2,qt^4,t^6), of colength14. This is the
exact basis produced from the homogeneous generators, not an assumed
radical ideal chosen to contain convenient points.

The chart omits one point of K. PR1036's exact whole-orbit computations
show all six order-five and all ten order-three axes lie inside this chart.
Therefore its omitted axis belongs to the fifteen-point orbit. Because
J15 is invariant and K is the reduced union of the three complete orbits,
J15 cuts out a union of entire such orbits. The only union having14 points
in this chart is the full fifteen-point orbit, of which fourteen lie here.
Thus the associated projective ideal sheaf of J15, equivalently its
saturation, is the reduced ideal sheaf of all fifteen order-two axes.
No equality of the raw homogeneous ideal with its saturation is asserted.
This proves the projective identification; the chart's missing point is
not silently discarded and no selected orbit point is evaluated.

Denote its affine chart ideal by I15. All local calculations below concern
the entire fourteen-point chart scheme, and equivariance transports the
result to the fifteenth point. This transport is justified by the just
proved single-orbit identification, not by an assumed extrapolation from
a numerical example.

## 4. Full coefficient-remainder certificate for the unique line

Reduce every component of F1 and F2 by the displayed basis of I15. Exact
arithmetic over Q(sqrt5), with q,t still independent, gives

    rem_I15(F1)=rem_I15(F2) != 0.                         (1)

Every coefficient of all four remainder polynomials is checked. One
compact nonzero witness in the first component is

    [q^2 t] rem_I15(F1)_0 = 1458176 sqrt5 / 3375.

Consequently all four components of alpha F1+beta F2 lie in I15 exactly
when alpha+beta=0. The zero-locus condition for an equivariant component
system is orbit-stable; it either contains all fifteen axes or none of
them. Equation(1) therefore gives the stated exact projective coefficient
line for occurrence of that entire orbit. This line is R1-R2, the already
known unique generic rank-three lift line, but the basepoint assertion
does not follow from its rank alone.

## 5. A bounded whole-orbit Nakayama certificate gives reduced ambient points

Put Fminus=F1-F2. In the same exact polynomial ring the checker verifies

    (components of Fminus) + I15^2 = I15.                  (2)

It does so by constructing the finite ordinary-square ideal and comparing
the entire reduced Groebner basis, not by evaluating any root. The quotient
by I15 has dimension14, and that by I15^2 has dimension42, since I15 is
the reduced ideal of fourteen points on the smooth affine surface.
Thus this is a bounded first-jet certificate for the entire chart orbit.

Localize (2) at any of those points. If A is the component ideal, then
A subset m and A+m^2=m. Nakayama's lemma gives A=m. Hence every chart
basepoint is reduced as a scheme in the AMBIENT plane. Equivariance gives
the same local ideal at the remaining orbit point. This conclusion is
stronger than a reduced intersection with any auxiliary line or conic.

## 6. The complete rank-three-line base scheme

PR1036 places R1-R2 off ell5, off ell3 and off ellDelta. Its local ideal
at each of the sixteen prescribed axes is therefore exactly I_Z, and it
has no conic basepoints. Sections4-5 supply its fifteen additional reduced
order-two axes. PR1035 forbids an additional thirty-point orbit when the
fifteen-point orbit is present, and forbids all other additional off-conic
support. Thus nothing else remains. The complete base scheme is

    B_rank3 = Z disjoint-union (fifteen reduced order-two axes),
    length(B_rank3)=34+15=49.

Off the coefficient line alpha+beta=0 there is no point of the fifteen-axis
orbit in the base scheme, so the earlier possible curvilinear double
structure on that orbit is now excluded throughout this universal pencil.
Nothing here identifies the actual unknown gate with any coefficient line.

## Verification and novelty limits

The new results are the whole-orbit occurrence line and reduced ambient
fifteen-axis scheme, hence the COMPLETE rank-three-line length49 scheme.
Old lift ranks, old coefficient-line placements, the fixed length34 target,
and prior orbit support exclusions are inputs, not new progress claims.
The critical-scheme construction is an exact route to the orbit ideal.

verify.py authenticates all inputs, checks the finite critical scheme and
its chart boundary, derives the complete I15 basis, reconstructs both
nonic rows, checks every coefficient in(1), and verifies the bounded
ideal equality(2). All computation is in universal symbolic variables.
There are no selected actual HM coefficients, parameter instances, orbit
root evaluations, or actual map/rank measurements. The geometric proof
of the orbit identification and the Nakayama conclusion are not replaced
by a numerical test.
