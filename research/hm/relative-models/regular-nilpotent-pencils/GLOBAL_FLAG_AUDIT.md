# Independent check of the global quadratic flag argument

Audited source: ../../local-defect/rank-one-quadratic-flag-nef/PROOF.md, together with ../../local-defect/rank-one-normal-obstruction/PROOF.md.

## Verdict

The global dimension argument is valid under its stated structural imports. In particular it proves actual generic absence of quadratic normal directions, without requiring any classification or realization of the abstract nilpotent pencil in this directory.

1. Under u'=a u, p'=b p+c u, the recovered class q modulo P transforms by b²/a. Thus W/P=M²⊗L^(-1) and det W=M³. The cross term 2bc/a lies in P and causes no descent problem.
2. Since W is a subbundle of a fixed trivial bundle, its Plucker dual determinant is globally generated. Therefore (M*)³ is nef, and M* is nef numerically. No positivity of M* on the full flag variety is assumed.
3. For the line convention F=P(V/L), with t=c1(M*), the relation is exactly t⁴+h t³+h²t²+h³t+h⁴=0. There is no alternating-sign error.
4. The incidence embedding into P(V)×Gr(2,V) makes 2h+t ample. On an integral component of dimension d≥4, intersect the relation with (2h+t)^(d−4). All five summands are nonnegative, hence vanish individually. Their positive linear combination (2h+t)^d then has degree zero, contradicting ampleness. This works on singular components using operational Chern classes, or on a projective resolution in characteristic zero.
5. The proper image of B in P(V) consequently has dimension at most three. Outside that image the normal-cone argument isolates the rank-one reduced support. This proves the rank-one cone is an irreducible component; its boundary inside the all-inputs-nonzero rank-one stratum has dimension at most six.

## Generic length refinement

Let k be the function field of the rank-one component. After the exact elimination, the completed local ring is k[[p1,p2,p3,p4]]/I, where I⊂(p)². At the generic point the homogeneous quadratic components of I have no nonzero common zero even after algebraic closure, by the global flag argument. Their ideal Q⊂k[p1,p2,p3,p4] is therefore homogeneous and (p)-primary.

Over the infinite field k, four general k-linear combinations of these quadratic forms form a homogeneous system of parameters. Since the polynomial ring is Cohen–Macaulay, they form a regular sequence. Their quotient has Hilbert series (1+z)^4 and length 16.

There are graded surjections from this complete-intersection quotient to k[p]/Q and then to gr_m(O_Z,ηD). Consequently

    5 ≤ length(O_Z,ηD) ≤ 16,
    m^5=0,

and the graded dimensions are bounded termwise by (1,4,6,4,1). The first two dimensions are exactly 1 and 4 because I has no linear terms. These conclusions do not assert that the quadratic ideal equals the full initial ideal; possible higher initial equations only lower the length.

The lower bound and nonreducedness at every point of the rank-one cone follow as in the source. No exact multiplicity is determined, and no operation values or actual matrices are evaluated.
