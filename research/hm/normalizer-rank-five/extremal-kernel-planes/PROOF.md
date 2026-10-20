# Extremal rank-seven kernel planes and the common-factor alternative

## Result and scope

Work over C under the symbolic hypotheses and conventions of
`rank-nine-independent-incidence/PROOF.md`. In particular, dim V=5,
f is trilinear, symmetric in its outer variables, and satisfies the
cyclic-zero identity; for every nonzero a the map

    A_a: V/Ca -> J,       [b] |-> f(a,a,b)

is injective. The projective residual-rank-drop locus in P(V) has dimension
at most two. No actual source operation, chosen input, or rank instance is
evaluated here.

The conclusions are:

1. A seven-dimensional irreducible component of the all-inputs-nonzero
   affine independent-zero locus whose generic middle residual rank is
   seven has a two-dimensional projective middle image. Over the reduced
   closure B of that image inside the rank-seven stratum, the whole kernel
   plane P(K_b) consists of tensors of rank at most two. Compatibility
   vanishes identically on its rank-two locus.
2. Every three-dimensional linear subspace K of Sym²E, dim E=4, all of
   whose tensors have rank at most two has exactly one of the two forms

       K = Sym²W,           dim W=2,
       K = ell U,           dim ell=1, dim U=3.

   The second notation means the image of ell tensor U under symmetric
   multiplication. There is no additional exceptional type.
3. Under the global repeated-input injection, identical compatibility
   excludes the first type and excludes the second type when ell is
   contained in U. Therefore the necessary type on the extremal middle
   image is

       K_b = ell_b U_b,     E_b = ell_b direct-sum U_b.

4. For this remaining type the ordered-factor cover splits canonically
   into two copies of P(U_b). Reconstruction fixes one outer direction
   [x_b], while the other ranges over a projective plane P(Z_b) in P(V).
   The two ordered fibers are

       ([x_b], [b], P(Z_b))   and   (P(Z_b), [b], [x_b]).

   Here V=Cb direct-sum Cx_b direct-sum Z_b. Equivalently the polar map
   z |-> f(x_b,b,z) has its minimal possible rank, namely two, and kernel
   Z_b.

These are necessary structural conclusions, not a proof that an actual
rank-seven middle point, extremal component, or rank-two polar map occurs.
No nonexistence conclusion is made for the surviving transverse
common-factor type. The exclusions in item 3 use the global injection at
new nonzero vectors, not merely injection at the original middle vector.

## 1. Dimension saturation over the middle-image closure

Use the notation from the incidence proof. On the rank-seven middle
stratum S_7 the residual kernel bundle K has rank three, and

    H = P_{S_7}(K)

is a projective-plane bundle. Write R inside H for the closed
rank-at-most-two determinantal locus, T for its rank-exactly-two open, C
for the compatibility zero scheme in T, and D_C -> C for the finite etale
ordered-factor cover of degree two. The earlier proof gives the exact
identification of D_C with the separately projectivized independent-zero
scheme over S_7.

Let Y be a seven-dimensional irreducible component of the reduced affine
independent-zero locus with generic middle rank seven. Separate
projectivization is a Zariski-locally trivial (G_m)^3-torsor. Its
irreducible components correspond to those of its base, because locally
the torsor is a product with an irreducible torus. Thus the projective
image X of Y has dimension four. The rank-seven part X_7 is a nonempty
open subset of X and still has dimension four.

Let B be the reduced closure of the middle image of X_7 in S_7. It is
integral, has dimension d at most two, and X_7 dominates B. After base
change, H_B=P_B(K) is integral of dimension d+2. Under the incidence
identification, the finite map D_C -> C sends X_7 to a constructible
subset D of H_B of dimension four. Therefore

    4 = dim D <= dim H_B = d+2 <= 4.

Every inequality is an equality. In particular d=2, and D is dense in
H_B: a proper closed subset of an integral four-dimensional variety has
smaller dimension.

The closed determinantal locus R_B contains D. It therefore contains all
of H_B. More precisely, H_B is reduced and its rank-at-most-two minors
vanish on the dense subset D, so those minors vanish identically. Hence

    R_B = H_B

scheme-theoretically. The rank-two locus T_B is consequently an open
subset of the reduced integral variety H_B. The compatibility section
psi of the rank-two bundle on T_B vanishes on D. A section of a vector
bundle on a reduced integral variety that vanishes on a dense subset is
zero, so

    psi = 0 on T_B,         C_B = T_B

scheme-theoretically. In particular these statements hold on every
geometric fiber over B, not only at its generic point. This strengthens
the generic saturation assertion without making a claim about any
nonreduced structure on the original middle-image scheme.

For the avoidance of doubt, a three-dimensional vector space of symmetric
tensors over C cannot consist only of rank-at-most-one tensors: two
linearly independent rank-one tensors are squares of independent vectors,
and their sum has rank two. Thus the rank-two open in every saturated
kernel plane is nonempty.

### The precise root cause of the dimension bound

If on the generic middle point of an integral B contained in S_7 the
kernel plane is not contained in the rank-at-most-two determinantal
variety, its rank-two part has dimension at most one. Every independent
zero component dominating B then has projective dimension at most

    dim B + 1 <= 3,

and affine dimension at most six. If the kernel plane is contained but
compatibility is not identically zero on its rank-two open, the same
bound holds: a proper closed zero locus in that irreducible open surface
has dimension at most one. No assertion that the two compatibility
equations are independent is needed.

Consequently an affine seven-dimensional rank-seven component requires
both entire-plane rank-at-most-two containment and identical
compatibility. Exceptional lower-dimensional middle subsets cannot
repair either failure for a component that dominates B.

## 2. Classification of three-dimensional rank-at-most-two spaces

Here is a self-contained linear-algebra proof. It uses only algebraic
identities for pencils and no classification theorem or computation on
an actual residual matrix.

Let K be a three-dimensional subspace of Sym²E such that every element
has rank at most two. As observed above, K contains an element q of rank
two. Over C choose a basis e_1,e_2,e_3,e_4 so that the matrix of q is

    [ J  0 ],       J = [0 1].
    [ 0  0 ]           [1 0]

Thus q=2e_1e_2 under the symmetric-algebra convention, and its support is
W=span(e_1,e_2). Write an arbitrary A in K in symmetric blocks

    A = [ B  C  ],
        [ C^t D ],

where B and D are symmetric 2-by-2 blocks. For every t, q+tA has rank at
most two. Its upper-left block P(t)=J+tB is invertible over C(t).
The Schur-complement identity therefore gives

    tD - t² C^t P(t)^(-1) C = 0.

Expansion at t=0 first gives D=0, and then gives

    C^t J C = 0.

The column space of C is totally isotropic for J. In the two-dimensional
hyperbolic plane its only possible nonzero totally isotropic subspaces
are Ce_1 and Ce_2. Thus for each A, either the first row of C is zero or
the second row is zero.

The map A |-> C is linear. Its image is a linear space contained in the
union of the two linear spaces just described. A linear space over an
infinite field contained in the union of two linear spaces is contained
in one of them. Hence either C=0 for every A, or, after exchanging e_1
and e_2, every C has the form

    C = [r],
        [0]

and at least one such row r is nonzero.

If all C are zero, the already-proved D=0 gives

    K contained in Sym²W.

Both sides have dimension three, so K=Sym²W.

In the other case write B=(b_ij). The (1,1)-entry of P(t)^(-1) is

    t b_22 / det P(t).

The Schur-complement identity, now with D=0, implies

    t b_22 r^t r = 0.

For r nonzero the outer-product matrix r^t r is nonzero, so b_22=0.
Choose one A_0 with nonzero r. If A has r=0, apply the same argument to
A+A_0 and subtract the equality b_22(A_0)=0. It follows that b_22=0
for every A in K. All tensors in K therefore have matrices of the form

    [ * * * * ]
    [ * 0 0 0 ]
    [ * 0 0 0 ]
    [ * 0 0 0 ],

which is exactly the subspace e_1 E of quadrics divisible by e_1.
Multiplication by the nonzero vector e_1 is injective on E, so its inverse
image U of K is a three-dimensional subspace. Thus

    K = ell U,       ell=Ce_1,       dim U=3.

This exhausts all cases. Conversely every tensor in either displayed
type has rank at most two, so the classification is exact.

The types are distinct: the tensors in Sym²W have no nonzero common
linear factor, whereas the tensors in ell U have the common factor ell.
In the second type ell is unique. Indeed, a second common factor m
different from ell would force every nonzero tensor in K to be a scalar
multiple of ell m, contradicting dim K=3. Once ell is fixed, U is unique.

## 3. Ordered factors for the two geometric types

This section concerns linear spaces of quadrics alone, before imposing
the injection or compatibility hypotheses.

### 3.1 Binary type

If K=Sym²W, its rank-one locus is the Veronese conic

    { [w²] : [w] in P(W) } inside P(Sym²W)=P².

Every point outside the conic has two distinct factors in W. The ordered
factor cover is

    (P(W) x P(W)) minus the diagonal
       -> P(Sym²W) minus the Veronese conic,
    ([p],[q]) |-> [pq].

It is finite etale of degree two, with involution interchanging the two
factors. Its source is irreducible, so this cover does not split into
two disjoint sections.

### 3.2 Common-factor type

If K=ell U and e is a nonzero generator of ell, multiplication identifies
P(K) with P(U). The tensor ea has rank two exactly when a is not in ell.
Therefore its rank-two locus is

    T = P(U)                         if ell is not contained in U,
    T = P(U) minus {[ell]}           if ell is contained in U.

The ordered factors are (ell,Ca) and (Ca,ell). Hence the ordered-factor
cover is canonically the disjoint union

    T disjoint-union T -> T.

There is a single rank-one point [e²] when ell is contained in U, and no
rank-one point when ell is not contained in U.

## 4. A compatible square contradicts global repeated-input injection

Fix a nonzero middle vector u, put E=V/Cu, and choose a linear splitting
s:E -> V. For any residual kernel tensor k define

    v(k) = A_u^(-1) B_{s,u}(k),

as in the incidence proof. This is a linear map K -> E. In particular,
for a square e² in K,

    f(s(e),u,s(e)) = A_u(v(e²)).

Suppose e is nonzero and v(e²)=rho e. Set

    x = s(e) - (rho/2)u.

Outer symmetry and f(u,u,u)=0 give

    f(x,u,x)
       = f(s(e),u,s(e)) - rho f(u,u,s(e))
       = 0.

The cyclic-zero identity and outer symmetry then give

    f(x,u,x) + 2 f(x,x,u) = 0,

so f(x,x,u)=0. But x and u are independent, because x has nonzero
residual image e. This contradicts injectivity of A_x on V/Cx.

Consequently

    e² in K and v(e²) in Ce are impossible for every nonzero e.

This criterion is independent of the chosen splitting: changing the
splitting changes v(e²) by a multiple of e. It does not assert that K
contains no squares; it prohibits squares with the specified
one-dimensional compatibility.

## 5. Saturation excludes binary kernel planes

Suppose K=Sym²W and compatibility vanishes identically on the rank-two
open of P(K). Every rank-two tensor in K has support W, so compatibility
says v(k) belongs to W on this dense open. Linearity then implies

    v(Sym²W) contained in W.

For e in W consider

    h(e) = e wedge v(e²) in exterior²W.

After choosing a generator of exterior²W this is a homogeneous cubic on
the two-dimensional space W. If it is zero identically, every nonzero
e is a zero. If it is not zero, its degree-three zero divisor on P(W)
is nonempty over C. In either case some nonzero e satisfies h(e)=0,
which means v(e²) is a multiple of e.

Section 4 rules this out. Thus a saturated binary kernel plane is
impossible under the global repeated-input injection.

This exclusion uses identical compatibility, not just the existence of
some independent zero over a binary kernel plane.

## 6. The linear compatibility map for a common-factor plane

Suppose K=eU, with e nonzero, dim U=3, and compatibility vanishes
identically. Define the linear map

    F: U -> E,       F(a)=v(ea).

For every a not in Ce its rank-two support is span(e,a), so

    F(a) belongs to span(e,a).

Let pi:E -> E/Ce be the quotient. The restriction pi|U has rank at least
two, and the displayed condition says

    pi(F(a)) is a multiple of pi(a)

whenever pi(a) is nonzero. If e belongs to U, replacing a by a+t e shows
that pi(F(e)) belongs to Cpi(a) for every a; using two independent
projected vectors gives pi(F(e))=0. Thus pi F factors through pi(U)
in both cases. The induced linear endomorphism of pi(U) preserves every
line, so it is a scalar: applying it to independent vectors a,b and to
a+b shows their eigenvalues agree. Therefore there is a scalar lambda
and a linear functional mu on U such that

    v(ea) = lambda a + mu(a)e       for every a in U.              (1)

Conversely (1) implies identical rank-two compatibility. The scalar
lambda and functional mu are unique for the fixed generator e, because
pi|U has rank at least two.

If e belongs to U, equation (1) at a=e yields

    v(e²) = (lambda+mu(e)) e,

contradicting Section 4. Hence the only compatible common-factor type
allowed by the global injection satisfies

    E = Ce direct-sum U.                                         (2)

This gives the claimed elimination of the common-factor type with a
rank-one point.

### Reconstruction and the split ordered fiber

Assume (2). For a in U define

    x = s(e) - lambda u,
    z(a) = s(a) - mu(a)u,
    Z = { z(a) : a in U }.

Equation (1) and the exact reconstruction formula give

    f(x,u,z(a)) = 0       for every a in U.

The map a |-> z(a) is linear and injective, so dim Z=3. Its residual
image is U, whereas x has residual image e. Consequently

    V = Cu direct-sum Cx direct-sum Z.

Every nonzero a gives an independent triple. The full separately
projectivized independent-zero fiber at [u] is precisely

    {([x],[u],[z]) : [z] in P(Z)}
       disjoint-union
    {([z],[u],[x]) : [z] in P(Z)}.

There are no other kernel lines or ordered factorizations, and uniqueness
of reconstruction excludes any other outer lifts. The two copies of P²
are disjoint because x is not in Z. This is an exact reduced fiber
description; using the incidence scheme structure it is also the exact
fiber scheme, since the rank-two locus here is all of P(K), and the
compatibility section vanishes identically.

### Change of splitting

If s changes to s+d u for d in E^vee, then

    v(ea) changes by d(a)e + d(e)a,
    lambda changes by d(e),
    mu changes by d|U.

Thus the reconstructed x and Z do not change. Since E=Ce direct-sum U,
one can also choose d(e)=-lambda and d|U=-mu, obtaining a splitting in
which v vanishes on all of K. This is a choice of lifts, not an extra
vanishing assertion about the original trilinear map.

## 7. The remaining case is exactly a minimal-rank polar map

For independent u,x define

    L_{x,u}: V -> J,       z |-> f(x,u,z).

First, the vectors A_u(x)=f(u,u,x) and A_x(u)=f(x,x,u) are linearly
independent. Both are nonzero by the repeated-input injection. If they
were proportional, choose t with

    A_u(x) - t A_x(u) = 0.

Trilinearity, cyclic-zero, outer symmetry, and f(x,x,x)=0 give

    A_{u+t x}(x)
       = f(u+t x,u+t x,x)
       = A_u(x) - t A_x(u)
       = 0.

The vectors u+t x and x are independent, contradicting the injection at
u+t x. This proves the claim.

On span(u,x), the polar map has values

    L_{x,u}(u) = A_u(x),
    L_{x,u}(x) = -2 A_x(u),

so L_{x,u} has rank at least two and is injective on that plane.

For the transverse common-factor reconstruction in Section 6, the map
L_{x,u} vanishes on the three-plane Z and V=span(u,x) direct-sum Z.
Therefore

    rank L_{x,u} = 2,       ker L_{x,u} = Z.

Conversely suppose u,x are independent and rank L_{x,u}=2. Then its
kernel Z has dimension three and is complementary to span(u,x).
In E=V/Cu put e=[x] and U=image(Z). These satisfy E=Ce direct-sum U.
The zero equations f(x,u,Z)=0 imply

    eU contained in ker Q_u.

Thus rank Q_u is at most seven. If rank Q_u is exactly seven, the two
spaces have the same dimension three, so ker Q_u=eU. Choosing the
splitting E -> V with image Cx direct-sum Z gives v=0 on eU. Hence
compatibility is identical, and the fiber has exactly the two P² sheets
described in Section 6.

In particular, at a fixed middle line of residual rank seven, the
following are equivalent:

- the projective independent-zero fiber has dimension two;
- its kernel plane is the transverse common-factor type and compatibility
  is identical;
- some independent outer direction x has rank L_{x,u}=2.

For the first implication, a dimension-two compatibility image is dense
in P(K_u)=P²; the fiberwise version of Section 1 gives saturation, and
Sections 5 and 6 give the remaining type. The other implications have
already been proved. None of these equivalent conditions is claimed to
occur for the actual stipulated map.

## 8. Variation along the extremal middle surface

Return to the integral surface B in Section 1. The preceding arguments
apply at every geometric point of B. Its kernel planes therefore have
the transverse common-factor type throughout B.

For a safe relative statement, shrink to a nonempty open subset B^o.
The common factor ell is unique, and U is uniquely recovered from ell
and K. Over the function field of B their geometric subspaces are
therefore Galois-invariant and descend to that field. Extend their
generic bases and relations after shrinking. This gives subbundles

    E|B^o = ell direct-sum U,       K|B^o = ell U.

The unique scalar/function expressions of Section 6 and reconstruction
then vary algebraically. The distinguished reconstructed outer line
X and the three-plane Z are subbundles of V tensor O_{B^o}, and

    V tensor O_{B^o} = U_middle direct-sum X direct-sum Z.

The full projective independent-zero locus over B^o is the disjoint
union of two copies of P_{B^o}(Z), embedded with X in the first or the
third outer slot. Thus the factor cover has no ordering monodromy in
this remaining case: its splitting is intrinsic to the unique common
factor.

This relative conclusion only describes the locus over B^o. It makes
no claim about its boundary at lower middle rank, intersections with
other middle components, or the full nonreduced ambient zero scheme.

## 9. What remains open

The classification and saturation reduce a potential seven-dimensional
rank-seven independent-zero component to a middle surface carrying a
distinguished outer line with a rank-two polar map. Excluding or
constructing that configuration needs additional information about the
actual map f. The identities and arguments here do not decide it.

This proof uses only symbolic tensor identities, dimension theory, and
linear algebra. The sole write is this local proof artifact; there is
no external write, source evaluation, large computation, or numerical
rank test.
