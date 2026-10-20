# Finiteness of minimal-rank polar pairs and exclusion of the extremal middle surface

## Result and scope

Work over C. Let V be a five-dimensional vector space, J any finite-dimensional
vector space, and f: V x V x V -> J a trilinear map satisfying:

1. Outer symmetry: f(a,b,c)=f(c,b,a).
2. Cyclic zero: f(a,b,c)+f(b,c,a)+f(c,a,b)=0.
3. Global repeated-input injection: for every nonzero a, the map

       A_a: V/Ca -> J,       [b] |-> f(a,a,b)

   is injective.

Define the polar map L_{x,u}:V->J by L_{x,u}(z)=f(x,u,z). The closed
projective determinantal locus

    D = { ([x],[u]) in P(V) x P(V) : rank L_{x,u} <= 2 }

has finite support. It may be empty, and this argument makes no
reducedness assertion about its determinantal scheme.

Consequently there is no positive-dimensional algebraic family of
minimal-rank polar pairs. In particular the two-dimensional middle
surface required for a seven-dimensional affine independent-zero
component with generic residual rank seven cannot exist.

This is a global finiteness assertion, not pointwise nonexistence. It is
consistent with the isolated rank-two polar in
/research/hm/universal-polar/rank-two-structural-countermodel/PROOF.md. No normalizer equivariance,
generic residual rank, target dimension, or residual-rank boundary
assumption is required for the finiteness theorem.

The proof uses projectivity of the entire polar determinantal locus and
a canonical decomposition of the trivial bundle on it. Considering only
the original open middle surface would miss the crucial completeness.

## 1. The two polar values are always independent off the diagonal

The identities imply f(a,a,a)=0, so A_a is well defined on V/Ca.

Fix independent u,x. By global repeated-input injection, both

    A_u(x)=f(u,u,x),       A_x(u)=f(x,x,u)

are nonzero. If they were dependent, write A_u(x)=t A_x(u) for some
scalar t. Trilinearity gives

    f(u+t x,u+t x,x)
      = A_u(x) + t f(x,u,x) + t f(u,x,x).

Here the quadratic term is zero. Outer symmetry gives
f(u,x,x)=A_x(u), and cyclic zero gives f(x,u,x)=-2 A_x(u).
Thus

    A_{u+t x}(x) = A_u(x) - t A_x(u) = 0.

The vectors u+t x and x remain independent, contradicting injection at
the nonzero vector u+t x. Therefore

    A_u(x), A_x(u) are linearly independent.                 (1)

The values of the polar map on the two-plane H=span(u,x) are

    L_{x,u}(u) = A_u(x),
    L_{x,u}(x) = -2 A_x(u).

It follows that L_{x,u}|H is injective and rank L_{x,u} >= 2 for
every off-diagonal pair. If rank L_{x,u}=2, then

    V = Cu direct-sum Cx direct-sum ker L_{x,u}.             (2)

Indeed the kernel has dimension three and has zero intersection with H.

On the diagonal, L_{u,u}=A_u on V, with kernel Cu and rank four. In
particular no diagonal point belongs to D.

## 2. The entire minimal-rank locus is projective and has no bad boundary

Put P=P(V) x P(V), with the first factor recording [x] and the second
recording [u]. The bilinear dependence on x,u gives the bundle map

    Phi: V tensor O_P -> J tensor O_P(1,1),

whose fiber map, up to the irrelevant scalar choices of representatives,
is L_{x,u}. The vanishing of its 3-by-3 minors defines D as a closed
subscheme of the projective variety P.

Section 1 proves at every closed point of D that:

- the two input lines are different;
- the polar rank is exactly two;
- the kernel is complementary to their sum.

These assertions hold at every point of the closed determinantal locus,
including all limits of an initially given family. A limiting middle
point may have a lower residual rank, but that does not affect any of
these conclusions. This is why compactifying the polar pairs does not
introduce an uncontrolled boundary.

## 3. Canonical projector rigidity on a projective component

Let C be any irreducible component of D with its reduced induced
structure. It is an integral projective variety over C. Pull all bundles
and maps back to C. Write X and U for the two tautological line
subbundles of V tensor O_C, and put

    Z = ker(Phi|C).

The bundle map Phi|C has rank exactly two at every point, so Z is a
rank-three vector subbundle. One can see this locally without any
smoothness assumption: invert a nonzero 2-by-2 minor and use elementary
row and column operations. All remaining Schur-complement entries
vanish because the map has rank two everywhere on the reduced base.
Equivalently the 3-by-3 minors already vanish after pullback from D.
Thus both kernel and image are locally free of the indicated ranks.

The inclusion map

    X direct-sum U direct-sum Z -> V tensor O_C               (3)

is an isomorphism on every fiber by (2), hence is an isomorphism of
vector bundles. This defines canonical global endomorphisms

    p_X, p_U, p_Z in End(V tensor O_C)

by projecting onto each summand along the other two. In a fixed basis
of V, every entry of these endomorphisms is a global regular function
on C. An integral projective variety over C has only constant global
regular functions. Therefore all three projector matrices are constant.

In particular the image of p_X is one fixed line in V, and the image
of p_U is another fixed line. Both maps

    C -> P(V),       c |-> X_c and c |-> U_c

are constant. But C is a closed subvariety of P(V) x P(V) and these are
its coordinate maps. Consequently C is a single point.

Every irreducible component of D_red is therefore a point. The
Noetherian scheme D has finitely many irreducible components, so its
support is finite. Since D is projective and zero-dimensional, it is
also a finite scheme over C. This last statement does not imply it is
reduced; the proof controls its support, not possible infinitesimal
thickenings at the points.

## 4. The extremal middle surface is excluded

Use the residual-map notation and the audited classification from
/research/hm/normalizer-rank-five/extremal-kernel-planes/PROOF.md. At a rank-seven middle line [u], a
two-dimensional projective independent-zero fiber is equivalent to the
existence of an independent line [x] such that

    rank L_{x,u} = 2.

The classification further gives the unique distinguished line [x] and
three-plane Z, with

    ker Q_u = x-bar U_bar,
    V = Cu direct-sum Cx direct-sum Z,
    f(x,u,Z)=0.

Here the overbars refer to the quotient V/Cu, and U_bar is the image of Z.

If a seven-dimensional affine independent-zero component has generic
middle residual rank seven, the earlier saturation argument supplies an
integral two-dimensional projective middle-image stratum B and a
nonempty open B^o carrying these distinguished lines and kernels
algebraically. Its graph

    B^o -> P(V) x P(V),       [u] |-> ([x(u)],[u])

lies in D. The second projection is the inclusion of B^o, so this graph
has dimension two. This contradicts the finiteness of D.

No extension of x(u) or Z(u) to the closure of B is assumed. Their graph
already lies in the finite closed locus D; equivalently its closure
would be a positive-dimensional projective subvariety of D, to which
Section 3 applies. In particular a rank change of Q at the boundary
cannot evade the argument.

Under the preceding dimension-at-most-two hypothesis for the middle
residual-rank-drop support, every affine independent-zero component
whose generic middle residual rank is seven therefore has dimension at
most six.

For completeness, the dimension conclusion can also be read fiberwise.
The rank-seven projective fibers have dimension at most two; the fibers
of dimension two occur only over the finite image of D. Away from that
finite set they have dimension at most one. A projective component with
positive-dimensional middle image of dimension at most two consequently
has dimension at most three. A component over a single middle point
has dimension at most two. Restoring the three independent nonzero
input scalings adds three dimensions, giving the bound six in all cases.

Combining this with ../rank-nine-independent-incidence/PROOF.md gives
one further precise reduction. Rank ten supports no independent zeros;
the affine rank-nine and rank-eight parts have dimensions at most five
and six, respectively. The new rank-seven bound is also six. Therefore
any affine independent-zero component of dimension at least seven has
generic middle residual rank at most six. In fact the entire component
lies over rank at most six: if its largest occurring rank were seven,
eight, or nine, that constant-rank part would be nonempty open and have
the full component dimension, contradicting the respective bound.

The rank-seven restriction belongs to the new incidence application,
not to the finiteness theorem itself. Nothing here bounds the dimension
of independent components with smaller generic middle residual rank;
in particular no universal affine independent-dimension bound six is
claimed.

## 5. Universal tensor-span obstruction

This reformulation answers the linear-span version of the surface
question without choosing a particular quotient operation.

Let

    W = ker(V tensor exterior^2 V -> exterior^3 V),
    f0(a,b,c) = a tensor (b wedge c) + c tensor (b wedge a).

The repeated-input projective variety is

    R = { [a tensor (a wedge b)] : a wedge b != 0 } in P(W).

It is the closed line-in-plane flag variety, as proved in
/research/hm/universal-polar/rank-two-structural-countermodel/PROOF.md. A quotient W -> W/S
preserves every repeated-input injection exactly when P(S) avoids R.

Let Omega parametrize ordered decompositions

    V = U direct-sum X direct-sum Z,
    dim U=dim X=1,       dim Z=3.

This is the open subset of P(V) x P(V) x Gr(3,V) on which the displayed
sum is direct. To a decomposition t associate the three-plane

    L_t = span{ f0(x,u,z) : z in Z },

where u and x are any nonzero representatives of U and X. It is
independent of their scalings and has dimension three.

Claim: If T is any positive-dimensional algebraic subvariety of Omega,
then the vector-space span

    S_T = sum over t in T of L_t

contains a nonzero repeated-input tensor. Equivalently,

    P(S_T) intersects R.                                    (4)

Proof. Suppose otherwise, and set f equal to f0 followed by W -> W/S_T.
This quotient satisfies the two trilinear identities and global
repeated-input injection. For every t in T, f(x,u,Z)=0, so the associated
polar map has rank at most two. The theorem puts all its pairs ([x],[u])
in a finite set D. For each such pair the polar kernel has dimension
three and necessarily equals Z. Hence the entire decomposition t is
determined by its pair and T has finite support, contradicting positive
dimension. This proves (4).

Thus annihilating the universal three-planes of any genuinely varying
transverse-common-factor family necessarily destroys repeated-input
injection somewhere. A single three-plane, and potentially a finite
collection, is not excluded. This is the exact distinction between the
isolated synthetic model and the forbidden surface family.

## 6. Assumption audit and limitations

- All arguments are over C. The projector step uses properness and
  H^0(C,O_C)=C on each reduced integral component.
- Global repeated-input injection is essential twice: to exclude the
  diagonal from D and to prove the two off-diagonal polar values are
  independent. Injection only on a chosen open set would not control
  boundary points.
- Outer symmetry and cyclic zero are used only in the explicit polar
  identities in Section 1 and in the universal construction.
- The finiteness theorem works without a generic residual-rank or
  normalizer-equivariance hypothesis.
- The same proof works in every dimension dim V >= 4: the diagonal
  rank is dim V-1 > 2 and the kernel rank is dim V-2. Dimension three
  does not satisfy that diagonal inequality and is not covered.
- No pointwise exclusion of rank-two polars, no reducedness claim for D,
  and no existence claim for the actual operation is made.
