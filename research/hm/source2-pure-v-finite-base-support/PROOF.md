# Finite support and multiplicity constraints for the pure-V nonic gate

## Statement and boundary

Retain the two-dimensional nonic gate and its finite base scheme B_s for
nonzero s. Write ell5,ell3 for the distinct jet lines of PR1030 and ellDelta
for the unique conic-base line. The fixed subscheme Z has six length-four
order-five axis schemes and ten simple order-three axes.

The following are necessary constraints, not occurrence statements.

1. Additional OFF-CONIC support is either empty, the unique orbit of fifteen
   order-two axes, or one orbit of thirty points with cyclic order-two
   stabilizer. The fifteen- and thirty-point alternatives never coexist.
   No point with trivial stabilizer occurs in the base scheme.
2. On either ell5 or ell3, there is NO additional off-conic support. The only
   possible additional support is the conic orbit of twelve points, and
   when present those twelve AMBIENT basepoints are reduced. Their presence
   is exactly the condition that the chosen jet line equals ellDelta; this
   packet does not identify those lines with each other.
3. Off ell5 union ell3, the base scheme equals Z locally at the sixteen axes.
   Any additional thirty-point orbit is reduced. At an additional fifteen-
   point orbit the scheme is uniformly curvilinear of length l=1 or2. At
   the conic orbit, when present, its AMBIENT local length is a uniform
   integer k between1 and3; it is curvilinear but need not be reduced.

More precisely, off the two jet lines put k=0 if the conic orbit is absent,
l=0 if the fifteen-point orbit is absent, and m=1 or0 according as a
thirty-point orbit is present or absent. Then

    0<=k<=3, 0<=l<=2, m in {0,1},  l*m=0,
    12k+15l+30m <= 47,
    length(B_s)=34+12k+15l+30m.                       (1)

Thus the necessary total-length list in this range is

    {34,46,49,58,61,64,70,73,76}.

This list does NOT assert that any or all entries occur. In particular k
is an ambient local length, not the already known simple intersection
length on the conic. Exact special-line local ideals, the location of a
possible thirty-point orbit, relations between the three distinguished
lines, and the actual gate coefficient remain undetermined.

## 1. Inputs and separation from existing results

The immutable inputs are listed in INPUTS.json:

- PR1030 at 418a7d9ebedaae9b5d00db9f69e449b5d8767108, the no-divisor
  theorem, the two jet lines, and the prescribed
  local ideals and lower vanishing orders.
- PR1033 at 7065160df56ffa7de1bea7e02c01dd98a6219781, the conic-base
  classification: B_s intersects Delta in the twelve reduced
  order-five fixed points if s belongs to ellDelta minus zero, and has
  empty conic intersection otherwise. This is a statement about the
  intersection scheme, not the ambient local scheme.
- PR1000 at 260cd6a777b23dc7ccd5ed956fcf65e17ff56145, for the off-conic
  stabilizer classification and the unique six-
  and ten-axis orbits already included in Z.

No new no-divisor or conic-base theorem is counted here. The new restrictions
use the degree-nine plane system, involution-fixed-line incidences, and local
algebra. No actual gate coefficient, axis representative, or source instance
is selected or evaluated.

## 2. The finite intersection budget

The four nonics of a nonzero s have no common divisor by PR1030. Two general
linear combinations can therefore be chosen with no common component:
after choosing the first, choose the second outside the finite union of
linear subspaces that would contain one of its curve components. Bezout
bounds the sum of their local intersection multiplicities by81, in fact
equality when all intersections are counted.

At the fixed Z points, a gate off ell5 union ell3 has component ideal
(u^2,v^2) at each of six points and m at each of ten points. Two general
members generate those two-generated local ideals, so their local
intersection multiplicities are respectively4 and1. Their total is34.
The remaining budget is at most47.

On ell5, the prescribed local orders are at least3 at the six points and1
at the ten, giving contribution at least6*9+10=64. On ell3, the orders are
at least2 at both orbits, giving at least6*4+10*4=64. Thus the residual
budget on either jet line is at most17.

For any additional basepoint, local intersection multiplicity is at least
the colength of the component ideal, since the ideal of the two selected
members is contained in that component ideal. Group equivariance makes
local base lengths equal along each orbit. Whenever the component ideal
is two-generated, two sufficiently general members generate it locally
by Nakayama; its contribution then equals that local length. All these
finitely many generic conditions can be imposed simultaneously. These
uses of general members are existence arguments, not actual parameter
substitutions or sampled rank calculations.

## 3. Off-conic orbits and the fifteen involution-fixed lines

For each involution h in A5, its rotation action on A has eigenspaces of
dimensions1 and2, with eigenvalues+1 and-1. Denote the projectivized minus
plane by H_h. There are fifteen such lines. Its isolated plus eigenpoint
is the order-two rotation axis.

The off-conic classification of PR1000 leaves orbit sizes6,10,15,30,60.
The six and ten orbits are unique and are already in Z. The thirty-point
orbits have stabilizer of order two. A point in one cannot be the isolated
plus eigenpoint, whose stabilizer is larger; it belongs to H_h for its
unique nontrivial stabilizing involution h. Thus each such orbit meets
each H_h in exactly30/15=2 points and none of its points belongs to another
involution-fixed line.

There is exactly one orbit of size fifteen. Its stabilizer is a Klein four
group, and its points are the fifteen involution axes. To see uniqueness,
restriction of A to a Klein four decomposes into its three distinct
nontrivial characters. Its only stable projective lines are the three
corresponding eigenaxes, each the plus axis of one involution. Each axis
lies on the minus planes of the other two involutions in its Klein four,
so it lies on exactly two of the H_h. Counting gives two order-two axis
points on every H_h.

Each H_h also contains precisely two of the six order-five axes and two
of the ten order-three axes. Indeed, the projective stabilizer of an
order-five axis is its dihedral normalizer of order ten, containing five
involutions. Those involutions negate, rather than fix, its representative
axis vector, and hence their minus planes contain the axis. There are
6*5=30 incidences, uniformly distributed among fifteen involutions. The
order-three normalizer has order six and three involutions, giving10*3=30
incidences in exactly the same manner. All the named axis orbits are
disjoint. These counts concern whole group orbits, not chosen coordinates.

A free orbit would have sixty points. Even the baseline fixed contribution
34 plus60 exceeds81. Thus no such orbit can occur in B_s.

## 4. Restriction to fixed lines excludes competing orbits

On any H_h, the prescribed Z conditions require every component nonic to
vanish to order at least2 at two order-five axes and at least1 at two
order-three axes. Their total is at least6. An extra fifteen-point orbit
would supply two more zeros on H_h, and an extra thirty-point orbit would
also supply two more. If both occurred, every component would have at
least10 zeros on H_h counting multiplicity, exceeding its degree9.
Therefore every component would vanish identically on H_h, making that
line a common divisor. PR1030 forbids this. Two distinct thirty-point
orbits are excluded by the same argument (and also by the total budget).
This proves the off-conic alternatives in the theorem.

On ell5, the prescribed total on H_h is at least2*3+2*1=8. On ell3 it is
at least2*2+2*2=8. Either additional off-conic orbit would add2, again
forcing the forbidden common line. Hence neither jet line permits any
additional off-conic point. The conic classification leaves only its
unique twelve-point orbit as possible additional support there. Residual
budget17 forces its ambient local length to be1: length at least2 at
each of twelve points would already require24. Thus these points, when
present, are reduced in the plane, not only on Delta.

## 5. Off the jet lines: ambient lengths at the conic and thirty-point orbits

Assume s lies off ell5 union ell3. If a thirty-point orbit occurs, a local
length at least2 would cost at least60, larger than the residual47. Thus
this orbit is reduced.

At a conic basepoint the restriction ideal on the smooth conic is its
maximal ideal, by the input conic theorem. Consequently the ambient ideal
contains an element whose derivative along the conic is nonzero. It is
a smooth local equation f. Modulo f the regular local surface ring becomes
a one-dimensional regular local ring, so the remaining finite ideal is
principal there. In completed coordinates the ambient component ideal
therefore has the form

    (f,w^k),                 k>=1.

It is curvilinear and a complete intersection, of length k. Equivariance
makes k constant along the twelve-point orbit. Its contribution to the
intersection budget equals12k, so k<=3. This does NOT prove k=1; simple
conic intersection and possible transverse thickening are distinguished.

## 6. The fifteen-point orbit has local length at most two

Continue off the jet lines and suppose the fifteen-point orbit occurs.
Every H_h has prescribed order at least6 from Z. Since not all components
vanish identically on H_h, their common vanishing divisor on that line has
degree at most9. The additional budget summed over all fifteen lines is
therefore at most15*(9-6)=45.

Each additional axis point lies on exactly two such lines. If its component
ideal were contained in m^2, its restrictions to both lines would have
order at least2 (or be identically zero, which only strengthens the bound).
Equivariance would give this at all fifteen points, costing at least60,
a contradiction. Thus the linear part of the local ideal is nonzero.

At such an axis, its Klein four stabilizer acts on the two mirror equations
u,v by two independent nontrivial order-two characters. These equations
are actual affine linear coordinates: the two mirror lines through the
axis are u=0 and v=0, and the Klein four acts diagonally on their ratios.
If the ideal has two independent linear terms it is m and has length1.
Otherwise its one-dimensional linear part is one of those two characters,
say that of u. Average a local generator to obtain f of exactly the u
character and with nonzero u coefficient. Every monomial of this character
has u to an odd power and v to an even power. Therefore

    f=u times a unit.

In particular u itself belongs to the completed ideal; this is not merely
an assertion about its tangent line or an unjustified straightening of a
possibly bending branch. Modulo u the remaining ideal is (v^l), so the
component ideal is exactly (u,v^l) for an integer l>=2. Its length is l.

Its restrictions to its two mirror lines have orders1 and l. The same
local length occurs at all fifteen axes. Summing their contributions to
the mirror-line bound gives

    15*(1+l) <=45,

hence l<=2. Thus only the reduced case and the curvilinear double case
remain. This proof does not choose which mirror direction is the tangent
of a possible double point and does not assert that the double case occurs.

## 7. Exhaustive necessary numerical constraints

All possible additional supports have now been classified: the unique
conic orbit, at most one fifteen- or thirty-point off-conic orbit, and no
others. Off the jet lines the prescribed scheme is exactly Z locally.
The additional local ideals above are complete intersections, so general
pairs of nonics compute their lengths. Bezout yields (1), and adding the
local lengths gives the displayed exact expression for length(B_s).
Enumerating those bounded integers gives the necessary list in the theorem.

At the level of support alone, the possible additional cardinalities off
the jet lines are

    {0,12,15,27,30,42}.

On either jet line they are only0 or12, with any additional points reduced.
All lists are one-way necessary conditions. No scheme with a listed length
is constructed here, no actual s is evaluated, and no original obstruction
is shown zero or nonzero by these bounds.

## Verification limits

The checker authenticates inputs, enumerates A5 involutions, Klein four
centralizers and cyclic normalizers to verify every incidence count, checks
the elementary mirror-character monomial constraint, and exhausts the
integer budgets and length lists. The written geometric and local-algebra
arguments are the proof; finite checks do not replace them or select an
actual instance.
