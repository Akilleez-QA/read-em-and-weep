# No divisorial defect and two distinguished jet lines in the pure-V nonic gate

## Statement and scope

Let G act through the icosahedral group A5 on A=Sym2 W, let X=P(A), and retain
PR1025's two-dimensional universal space

    Vgate=Hom_G(P O_X(-3),J),       J=I_Z(6).

The fixed scheme Z of PR1000 consists of six length-four order-five axis
schemes with completed ideal (u^2,v^2), and ten reduced order-three axes.
It is disjoint from the discriminant conic Delta. All representations and
polynomial variables retain their pinned identifications.

For EVERY nonzero s in Vgate:

1. Its four degree-nine component polynomials have no common divisor.
   Its image is I_Bs(6) for a finite scheme Bs containing Z. In particular
   J/im(s) has finite support: there is no divisorial image defect.
2. There are two distinct intrinsic lines ell5 and ell3 in Vgate. Outside
   their union, Bs agrees with Z locally at every one of the sixteen axes.
   On ell5 minus zero, the six axis ideals are contained in m^3 while the
   ten other axes remain reduced, so length(Bs)>=46. On ell3 minus zero,
   the six axis ideals equal those of Z while each of the ten other axis
   ideals is contained in m^2, so length(Bs)>=54.

Neither statement determines additional basepoints, the exact exceptional
local ideals, or the actual gate coefficients. In particular no value of
the original fourth Bockstein, no actual compatible radical, and no source
occurrence is selected. These are universal restrictions on all nonzero
members of the already established two-dimensional space, not experiments
at selected members.

## 1. Inputs, existing results, and coefficient interpretation

INPUTS.json records exact immutable originals:

- PR1025, 09f1377f83b027ca27eea0b3a9f40a1b92c6c466: the actual pure-V
  quotient-third gate, its exact target J, its two-dimensionality, and
  the resolution

      0 -> A O(-2) + O(-5) -> D O(-1) -> J -> 0.

- PR1000, 260cd6a777b23dc7ccd5ed956fcf65e17ff56145: the target section's
  exact zero scheme Z and its local ideals, not merely its support.
- PR1005, 4a50853a6b6a4f18f1a7aac06a90e33e78e7787e, Section2: the unique
  cubic P-covariant cP has base scheme precisely the six REDUCED order-five
  axes. Its component ideal there is m; it is nonzero at every other point.

The old length34 target scheme and cubic base scheme are imported results,
not new outputs. The present object is the four-component nonic system of
an arbitrary nonzero member of the new pure-V gate, not the older octic
source126 generator or its degree-four source row.

Compose s with J -> O(6), then twist the source and target by three. This
gives a G-map P -> H0(I_Z(9)). Since P is irreducible and s is nonzero,
its four component polynomials are linearly independent and span a copy
of P. Their base ideal defines Bs once absence of a common divisor has
been proved. The coefficient pairing uses the fixed self-duality of P.

## 2. The only possible non-conic common divisor would be a sextic

Let g be the homogeneous greatest common divisor of the four components.
Its line is G-stable. A5 has no nontrivial characters, so g is invariant,
up to its irrelevant nonzero normalization.

Exact character arithmetic for the rotation representation A gives

    dim (Sym^d A)^G, d=0,...,9:
    1,0,1,0,1,0,2,0,2,0.

Let delta be the invariant quadratic defining Delta. Multiplication by
delta is injective on the polynomial ring. These dimensions show that
all degree-four invariants are multiples of delta^2 and every degree-eight
invariant is delta times a degree-six invariant. The degree-two invariant
space is the line spanned by delta. There are no positive odd-degree
invariants through degree nine.

The conic cannot divide the component system: delta is a unit on Z, so
if all components were divisible by delta their quotients would give a
nonzero P-map into H0(I_Z(7)). The PR1025 resolution, twisted by one, gives
H0(I_Z(7))=H0(J(1))=D, and Hom_G(P,D)=0. This elementary conic exclusion
is included only as a necessary lemma; the stronger square-restriction
comparison is not claimed or re-derived here.

It follows that any positive-degree gcd must have degree exactly six and
must not be divisible by delta. Its residual component system is the
unique cubic P-covariant cP, up to a nonzero scalar, because

    dim Hom_G(P,Sym^3 A)=1.

We now exclude this sextic case globally.

## 3. A sextic gcd would have sixteen singular points

At each order-five axis, the component ideal of cP is m=(u,v), by PR1005,
and that of Z is (u^2,v^2), by PR1000. Since g cP vanishes on Z,

    g m subset (u^2,v^2).

In the completed local ring this forces g in m^2. Indeed a nonzero constant
term would give a linear term in the product; for linear part alpha u+beta v,
the uv coefficients in g u and g v force beta=alpha=0. Equivalently the
colon ideal ((u^2,v^2):m) is exactly m^2. Thus all six axes are singular
points of the sextic g=0.

At each of the ten order-three axes, cP has a unit component. Hence g
vanishes there. A cyclic order-three rotation fixes a representative vector
a of the axis in A, not merely its projective line. In an invariant affine
slice through that vector the tangent weights are the two nontrivial
third-root characters. The O(6) fiber has trivial character under this
cyclic subgroup because a itself is fixed. Invariance of g therefore
forbids a linear term. Consequently g belongs to m^2 at each of these ten
points as well. The six and ten axis orbits are disjoint, giving sixteen
distinct singular points.

Such a sextic g, with no delta factor, is reduced. Otherwise take the
product h of all irreducible components occurring with multiplicity at
least two, each once. Its divisor is G-stable, its degree is at most three,
and its polynomial is invariant up to character. Perfectness makes that
character trivial. The low-degree invariant list leaves only a nonzero
multiple of delta in positive degree at most three. This would put delta
in g, contrary to Section2.

A reduced plane sextic with r irreducible components has

    sum_p delta_p = p_a + r - 1 - sum_i g_i <= 10+6-1=15,

where g_i are the geometric genera of the normalized components and each
singular point contributes delta_p>=1. This standard normalization-genus
formula applies to reducible reduced curves as well. Sixteen distinct
singular points are impossible. Equivalently a generic polar intersects
a reduced sextic in degree30, while these sixteen multiplicity-two points
would contribute at least32. The contradiction excludes the sextic gcd.

Thus the four components have no common divisor. Their base scheme Bs is
finite and contains Z. Their ideal sheaf is I_Bs; consequently im(s)=I_Bs(6)
and J/im(s) is supported at finitely many points.

## 4. Two scalar jet functionals, with full stabilizer twists

At an order-five axis, consider the quadratic leading part of the components
of s. Since they already belong to I_Z, this takes values in the two-space
spanned by u^2,v^2. Use the FULL projective stabilizer H5=D5 of order ten,
not just its cyclic subgroup. The rotation subgroup gives u,v opposite
primitive fifth-root weights, so u^2,v^2 form the frequency-two irreducible
two-dimensional representation. The fiber of O(9) carries the sign of the
normalizer reflection: the reflection takes the axis representative a to -a.
Twisting a two-dimensional dihedral representation by this sign gives an
isomorphic representation. Meanwhile P restricted to H5 is the sum of
the two inequivalent two-dimensional irreducibles, each once. Therefore

    dim Hom_H5(P, O(9)|p tensor span(u^2,v^2)) = 1.

Transport over the six-point orbit makes the quadratic-jet assignment a
linear map nu5 from Vgate to a one-dimensional space. It is intrinsic up
to choice of a nonzero coordinate on that space. In its kernel the component
ideal is contained in m^3 at all six axes. A nonzero value makes the image
the full two-dimensional generator space, so Nakayama's lemma gives exactly
I_Bs,p=I_Z,p there.

At an order-three axis the full stabilizer is H3=S3. Its tangent/cotangent
plane is the standard irreducible rho. The O(9) fiber again has reflection
sign chi, and chi tensor rho is isomorphic to rho. The restriction

    P|H3 = 1 + chi + rho

therefore gives

    dim Hom_H3(P,O(9)|p tensor (m/m^2))=1.

The first jets give a second scalar linear map nu3 on Vgate. Its kernel
has all ten component ideals contained in m^2; a nonzero value spans the
full cotangent plane and gives I_Bs,p=m at every order-three axis.

The full stabilizers are essential. Cyclic weights alone would leave
separate coefficients and would not prove that each jet target is a line.

## 5. Bezout separates the two jet kernels

Suppose a nonzero s lay in ker nu5 intersect ker nu3. Its four nonics
would all vanish to order at least three at the six axes and at least two
at the ten axes. Section3 proves their common base locus is finite. Hence
two general linear combinations of the components can be chosen without
a common curve component: choose the second to avoid the finitely many
components of the first. These are only general members of a universal
linear system in a proof, not evaluated actual-source parameters.

Bezout gives total intersection number 9^2=81. At the six axes local
intersection multiplicity is at least3^2, and at the ten it is at least2^2.
Their sum would be

    6*9 + 10*4 = 94 > 81,

a contradiction. Thus the joint map (nu5,nu3) is injective. Its source and
target both have dimension two, so it is an isomorphism. In particular
both functionals are nonzero and their kernels ell5 and ell3 are distinct
intrinsic lines.

Off the two lines the local ideals equal those of Z at all sixteen axes.
On ell5 minus zero, the six quotient local rings have length at least
length(O/m^3)=6, while the ten other points are reduced, giving length>=46.
On ell3 minus zero, the six lengths are exactly4 and the ten lengths at
least length(O/m^2)=3, giving length>=54. These are LOWER bounds only;
no assertion is made that the higher local ideals equal m^3 or m^2.

The proof leaves possible additional finite basepoints unresolved. It also
leaves the actual element of Vgate completely unselected, including whether
that actual element is zero. The nonzero universal assertions cannot be
used to select a nonzero original obstruction.

## Verification boundary

The checker authenticates the three immutable input proofs, computes the
low-degree invariant and P multiplicities using exact characters, verifies
full dihedral and symmetric stabilizer multiplicities including the sign
twists, and checks the local colon ideal, genus bound, Bezout obstruction,
and length inequalities. The written sheaf and curve arguments are the
proof; symbolic checks do not certify imported geometry or evaluate an
actual HM instance.
