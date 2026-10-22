# Exact factorization types at the twelve order-five parameters

## Theorem

At each of the twelve order-five fixed parameters of the actual determinant-cubic family, the plane cubic is either

- a smooth conic together with its tangent line, or
- a double line together with a distinct simple line.

It is never an irreducible cubic, three distinct lines, or a triple line. The same alternative occurs at all twelve parameters, by A5 transitivity. This statement is independent of whether the generic family is irreducible or a three-line family.

## Universal weight proof

Let zeta be a primitive fifth root and choose coordinates on the positive plane so an order-five stabilizer acts on point coordinates by

    (x,y,z) |-> (x,zeta^(-1)y,zeta z).

Its unique nonisotropic axis is p=[1:0:0]. The other two fixed points are isotropic for the invariant conic q0. After scaling coordinates, q0 has the form x^2+k yz with k nonzero.

The actual representation distinction Sym^2 W=A != V allows the fixed parameter lift in W* to be chosen with weight zeta. The actual cubic family is the degree-six Veronese followed by its nonzero equivariant map, so its equation at that parameter is a cubic eigenvector of weight zeta^6=zeta.

The coordinate functions have weights 0,+1,-1. The only degree-three monomials with weight +1 modulo five are

    x^2 y,       y^2 z.

Thus the actual cubic has the form

    c=y(a x^2+b yz),       (a,b)!=(0,0),              (1)

after possibly interchanging y and z. These coordinates express the universal eigenspace; no actual values of a or b are selected or evaluated.

If ab is nonzero, the quadratic factor is nonsingular and meets the line y=0 twice at [0:0:1]. It is a smooth conic with its tangent line. If a=0, (1) is a nonzero multiple of y^2 z. If b=0, it is a nonzero multiple of x^2 y. In either case its factors are a double line and a distinct simple line. This proves all stated exclusions.

The special parameters form one A5 orbit of size twelve. The group carries each entire cubic and its factorization to the next, so the factorization type is uniform over this orbit.

## The two nonreduced geometries

The two possible double-line configurations are geometrically distinct, without requiring coordinate values.

- For y^2 z, both component lines are tangent to q0 at its two order-five fixed points, and they meet at the nonisotropic axis p. The cubic is singular at p.
- For x^2 y, the double line is the polar line of p with respect to q0, and the simple line is tangent to q0 at one of the isotropic fixed points. The point p lies only on the simple line and is a smooth point of the cubic.

For the reduced tangent-line-plus-conic case, p is also smooth because a is nonzero. Thus a singularity of the special cubic at its associated axis is equivalent to the first double-line configuration, not to the triple multiplicity of parameter incidence. The latter parameter multiplicity alone never implied a plane singularity.

If a separate theorem establishes that every reduced determinant member is three distinct lines, the reduced alternative in (1) is excluded, and all twelve special members must be double-plus-simple lines. That additional premise is not proved or silently assumed here.

## Inputs and boundary

DETERMINANT-CUBIC-FAMILY-RATIONAL-SEXTIC.md supplies the actual degree-six equivariant family, the representation distinction, and the twelve-parameter orbit. This proof uses only its universal order-five weights. No generic singularity hypothesis, normalization, coefficient evaluation, actual matrix rank, scan, or experiment is involved. It does not decide which of the two nonreduced configurations occurs in the actual family.
