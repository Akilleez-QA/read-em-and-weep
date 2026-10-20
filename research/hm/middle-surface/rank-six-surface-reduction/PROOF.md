# Rank-six residual kernels: exhaustive non-ternary surface reduction

## Status and scope

Everything is over C. This note concerns an abstract four-dimensional linear
space K contained in Sym^2 E, where dim E=4. Its rank-at-most-two locus is

    R_2(K) = { [k] in P(K) : symmetric rank(k) <= 2 }.

The support of K is the smallest E_0 contained in E such that
K is contained in Sym^2 E_0. Thus K has full support precisely when its
symmetric matrices have no constant common kernel in E^vee.

The main classification proved here is:

1. If K contains an invertible tensor, every irreducible surface component
   of R_2(K) is a plane, unless K=A B for a decomposition
   E=A direct-sum B with dim A=dim B=2. In that exceptional case R_2(K)
   is the smooth Segre quadric. An irreducible quadric cone cannot occur.
2. If K has generic rank three and full support, every irreducible surface
   component of R_2(K) is a plane. A degree-two or degree-three surface
   component forces K to be supported on a three-dimensional subspace.
3. If every member of K has rank at most two, K=ell E for a fixed line
   C ell. In particular there is no omitted generic-rank-one case.
4. Every plane in R_2(K) is P(Sym^2 A), dim A=2, or P(ell U), dim U=3.

The matrix-factorization argument and the linear-space classification are
proved elementarily below. No classification theorem is being assumed.

For the trilinear situation of the companion proofs, all the non-ternary
possibilities can then be controlled by the already-proved finite
rectangular-annihilation incidences. More precisely: any middle line
with full-support rank-six residual kernel and a two-dimensional
compatible rank-two locus belongs to a fixed finite set, independent of
which kernel type occurs. Sections 6--9 establish this precise assertion.

The only remaining surface geometry after this note is the supported
ternary case K contained in Sym^2 E_0 with dim E_0=3. That case is the
subject of the separate cubic-web analysis. No conclusion about residual
rank at most five is made here.

## 1. Linear spaces consisting of symmetric tensors of rank at most two

**Lemma.** If L is a linear subspace of Sym^2 E and every tensor of L has
rank at most two, then either

    L contained in Sym^2 W for some dim W=2,

or

    L contained in ell E for some nonzero ell in E.

The assertion holds in any dimension for E, over C.

**Proof.** If all members have rank at most one, L has dimension at most
one: independent rank-one symmetric tensors are scalar multiples of a^2
and b^2 for independent a,b, and their sum has rank two. Such a space
satisfies the conclusion. Otherwise choose a rank-two tensor in L. Over C
it factors as x y with x,y independent. Put W=span(x,y), choose a
complement F, and scale the symmetric matrix of xy on W to

    A_0 = [ 0  1 ]
          [ 1  0 ].

For an arbitrary q in L write its block matrix as

    q = [ A  B   ]
        [ B^t C ].

The pencil xy+tq has rank at most two for every t. Its upper-left block
A_0+tA is invertible over C(t), so its Schur complement is zero:

    t C - t^2 B^t (A_0+tA)^(-1) B = 0.

Expanding at t=0 gives

    C=0,
    B^t A_0 B=0,
    B^t A_0 A A_0 B=0.                                  (1.1)

Let b_1,b_2 be the two rows of B. The middle identity says
b_1^t b_2+b_2^t b_1=0. Equivalently the product of the two linear forms
b_1,b_2 is zero, so one row vanishes. If B=0, q belongs to Sym^2 W.
If b_1 is nonzero and b_2=0, the last identity in (1.1) forces A_22=0.
Together with C=0 this says exactly that q is divisible by x. The other
case says that q is divisible by y.

Consequently every q in L lies in

    Sym^2 W union x E union y E.

A vector space over C is irreducible as an affine variety and cannot be
a finite union of proper linear subspaces. Hence L lies in one of these
three spaces, proving the lemma. The use of the expansion is purely a
polynomial identity over C(t), not an analytic assumption. QED.

**Consequences for dim E=4.** A three-dimensional L is Sym^2 W or ell U
for a three-dimensional U. A four-dimensional L is necessarily ell E.
In particular these statements include all possible planes of rank at
most two, whether or not they contain rank-one points.

## 2. The determinant limits surface degrees in the invertible case

Choose coordinates on K, and let M(x) be the corresponding symmetric
4-by-4 matrix of linear forms on K. The map x -> M(x) is injective.
Suppose det M is not identically zero. An irreducible surface
S contained in R_2(K) has one irreducible homogeneous equation g, because
P(K)=P^3. Every entry of adj M vanishes on S, hence is divisible by g.

Let D=det M. Jacobi's formula gives

    partial D / partial x_i = trace(adj M * partial M / partial x_i).

Thus g divides every partial derivative of D. Euler's identity gives
g|D. If its multiplicity in D were one, write D=g h with g not dividing
h. Modulo g the derivative identities would give

    h * partial g / partial x_i = 0

for every i. Since g is irreducible, it would divide all its nonzero
partial derivatives, which is impossible in characteristic zero by
degree. Therefore g^2 divides D. Since deg D=4,

    deg g <= 2.                                           (2.1)

A degree-one surface is a plane and is classified by Section 1. If
deg g=2, g is irreducible and

    det M = c g^2,       adj M = g L,
    M L = c g I_4,                                       (2.2)

where c is a nonzero scalar and L is a symmetric matrix of linear forms.
An irreducible quadratic form over C has rank three or four. Both are
analyzed next.

## 3. Normalizing the symmetric linear matrix factorization

Write q=g and N=L/c, so M N=q I_4. Choose e with q(e) nonzero and rescale
q, and hence N, so q(e)=1. Equation (2.2) makes M(e) invertible.
A constant congruence puts M(e)=I_4. Under M -> P^t M P, transform
N -> P^(-1) N P^(-t). Both remain symmetric, and M N=qI is preserved.
Afterward N(e)=I_4 as well.

Let b be the polar bilinear form of q, normalized by b(e,e)=1. Split the
parameter space K as

    K = C e direct-sum H,       H=e^perp under b.

This works even when q is degenerate, since e is nonisotropic. For y in
H write

    M(t e+y)=t I+A(y),       N(t e+y)=t I+B(y).

Comparing the coefficient of t in M N=(t^2+q(y))I yields B(y)=-A(y).
The remaining equality is

    A(y)^2 = -q(y) I.                                     (3.1)

Polarization gives the corresponding anticommutation relations.
After rescaling the nondegenerate coordinate directions by constants,
the nonradical generators may be denoted Gamma_i, with

    Gamma_i^t=Gamma_i,
    Gamma_i^2=I,
    Gamma_i Gamma_j + Gamma_j Gamma_i=0  (i != j).          (3.2)

A radical generator R is symmetric, satisfies R^2=0, and anticommutes
with each Gamma_i. None of these normalizations changes injectivity of
the original four-parameter map x -> M(x).

## 4. A smooth quadric forces the cross-block form; a cone is impossible

### 4.1 Smooth quadric

If rank q=4, there are three generators Gamma_1,Gamma_2,Gamma_3. Set

    P = Gamma_1 Gamma_2 Gamma_3.

Using (3.2) gives

    P^t=-P,       P^2=-I,       P Gamma_i=Gamma_i P.

Thus P has eigenspaces V_+,V_- for the distinct eigenvalues i,-i. For
vectors v,w in either one of these eigenspaces, skew-adjointness gives

    lambda <v,w> = <P v,w> = -<v,P w> = -lambda <v,w>,

so that eigenspace is totally isotropic for the standard nondegenerate
symmetric bilinear form. Each has dimension at most two. Together they
span a four-dimensional space, so each has dimension exactly two.

Every M(x) commutes with P. It therefore preserves V_+ and V_-. Its
associated symmetric bilinear form vanishes on each V_+ x V_+ and
V_- x V_-, because those eigenspaces are isotropic. Taking a basis of
these two eigenspaces puts all M(x), by constant congruence, in the form

    [ 0   C(x) ]
    [ C(x)^t 0 ].

The space of such symmetric matrices has dimension four. Since K also
has dimension four and its matrix map is injective, K is exactly this
space. In tensor notation it is A B for complementary two-dimensional
subspaces A,B of E.

Its rank-two locus is det C=0, the smooth Segre quadric, because the
rank of the displayed matrix is twice rank C. This also shows directly
that there are no additional plane surface components in this case.

### 4.2 Irreducible quadric cone

If rank q=3, there are two generators Gamma_1,Gamma_2 and one radical
generator R. The +1 and -1 eigenspaces of the symmetric involution
Gamma_1 are orthogonal and nondegenerate. Anticommutation makes
Gamma_2 exchange them isomorphically; hence both have dimension two.
Because Gamma_2 is itself a symmetric involution, it preserves the
standard bilinear form. Choosing an orthonormal basis of the first
eigenspace and its image under Gamma_2 in the second gives

    Gamma_1 = [ I_2   0  ],       Gamma_2 = [ 0   I_2 ],
              [  0  -I_2 ]                  [ I_2  0  ]

in that basis. Symmetry and anticommutation with Gamma_1 force

    R = [ 0   B ],
        [ B^t 0 ].

Anticommutation with Gamma_2 then forces B^t=-B. Every 2-by-2
skew-symmetric matrix is B=s J, where

    J = [ 0  1 ]
        [-1  0 ].

But R^2=0 gives B B^t=0, and B B^t=s^2 I_2. Thus s=0 and R=0.
The coefficient of the nonzero radical parameter direction in M is
zero, contradicting the injectivity of x -> M(x). Therefore an
irreducible quadric cone is impossible.

## 5. Generic-rank-three kernels

Suppose M has generic rank three. Then adj M is a nonzero symmetric
matrix of cubic forms and has rank one over the fraction field. Let an
irreducible equation g of degree at least two define a surface contained
in R_2(K). Divisibility of all adjugate entries gives

    adj M = g L,       degree L <= 1.                      (5.1)

If g has degree three, L is a constant symmetric rank-one matrix, so it
has the form c a a^t. If g has degree two, L is linear and all its
2-by-2 minors vanish identically. Its coefficient space is a linear
space consisting of symmetric rank-at-most-one matrices. Such a space
has dimension at most one: two rank-one tensors with different support
lines have a rank-two sum. Hence again

    L = ell(x) a a^t

for a fixed nonzero vector a and a nonzero scalar linear form ell.
From M adj M=0 we obtain M(x)a=0 identically. Thus M has a constant
common kernel. Equivalently K is supported on the three-dimensional
annihilator E_0 of a in E.

It follows that a generic-rank-three kernel of full support has only
plane surface components. In the non-full-support case, dimension four
for K rules out support dimension at most two; consequently the support
has dimension exactly three. This is precisely the ternary case left
to the separate analysis.

Finally, if the generic rank is at most two, all members have rank at
most two by closedness and Section 1 gives K=ell E. This completes the
pure kernel-geometric classification in the initial summary.

## 6. Trilinear compatibility and the forbidden compatible square

For the applications, assume the setup of
/research/hm/middle-surface/extremal-surface-geometry/PROOF.md and GENERALIZATION.md:

- dim V=5;
- f:V x V x V -> J is trilinear, outer symmetric and cyclic-zero;
- for every nonzero a, A_a:V/Ca -> J, [b] -> f(a,a,b), is injective.

Fix a middle line [u], let E=V/Cu, choose a linear splitting s:E->V,
and let K=ker Q_u have dimension four. On K the residual-zero condition
allows the linear map

    v:K->E,       A_u(v(ab))=f(s(a),u,s(b)).

A rank-two tensor ab, with a,b independent, is compatible precisely when

    v(ab) belongs to span(a,b).                            (6.1)

This is the usual lift-reconstruction condition. Rank-two tensors over
C have just the two ordered factor choices, so the ordered-factor cover
is finite and introduces no extra dimension.

We shall use the following consequence of the global injection: for
independent a,b in V, A_a(b) and A_b(a) are linearly independent. Its
proof is in the companion PROOF.md, Section 1; it follows by expanding
A_{a+t b}(b)=A_a(b)-t A_b(a) and using injection.

In particular there is no nonzero a in E such that

    a^2 belongs to K and v(a^2) belongs to C a.             (6.2)

Indeed (6.2), after lifting a by s, would make

    -2 A_{s(a)}(u)=f(s(a),u,s(a))=A_u(v(a^2))

proportional to A_u(s(a)), contradicting the independence just stated.
We call (6.2) a compatible square only as a convenient shorthand inside
this proof. No claim that compatibility automatically extends to a
rank-one boundary point is being made.

## 7. Identical compatibility on a plane

Let H be a three-dimensional subspace of K consisting of tensors of
rank at most two. Assume (6.1) holds on a dense set of rank-two members
of P(H). Its polynomial identities then hold for every rank-two member
where the displayed support condition is defined.

### 7.1 Binary plane

If H=Sym^2 A for dim A=2, a generic rank-two member has support A, so
v(H) is contained in A. On A the expression

    a wedge v(a^2) in exterior^2 A

is a scalar homogeneous cubic in a. Every homogeneous cubic on a
complex two-dimensional vector space has a nonzero zero, including the
case when it is identically zero. At such a zero, v(a^2) belongs to Ca,
contradicting (6.2). Therefore a binary plane cannot be identically
compatible.

### 7.2 Common-factor plane containing its factor

Write H=ell U, dim U=3. Modulo C ell, condition (6.1) says

    vbar(ell a) belongs to C abar  for a in U outside C ell.

If ell belongs to U, fix a outside C ell and replace it by a+t ell.
Linearity implies that vbar(ell^2) belongs to C abar. Since U/C ell has
dimension two and a can represent different lines, this forces
vbar(ell^2)=0. That is a compatible square, again impossible.

### 7.3 Transverse common-factor plane

The remaining case is E=C ell direct-sum U. The quotient map U->E/C ell
is an isomorphism. Condition (6.1) says that the induced endomorphism
of U preserves every line, hence is scalar. Therefore

    v(ell a)=lambda a+mu(a)ell,
    lambda in C,       mu in U^vee.                        (7.1)

Define

    X=C(s(ell)-lambda u),
    Z={s(a)-mu(a)u : a in U}.

Then dim X=1, dim Z=3, and the lift expansion using (7.1) gives

    f(X,u,Z)=0.                                           (7.2)

Consequently every identically compatible rank-two plane supplies a
point of the fixed finite incidence C_{1,3} proved finite in
/research/hm/middle-surface/extremal-surface-geometry/GENERALIZATION.md. This is a global finite
incidence, independent of K; it therefore bounds all such middle lines
simultaneously, rather than separately for each kernel.

## 8. Entirely rank-two kernels K=ell E

Here R_2(K)=P^3, so a two-dimensional compatible locus need not initially
be a surface component of R_2(K). It still produces the plane from
Section 7.3, as follows.

Choose E=C ell direct-sum U, dim U=3. Write a=t ell+w and take the U-part
of v(ell a). Because v is linear, it has the form

    t b+T w,       b in U,       T in End(U).

The forbidden-square statement (6.2) gives b nonzero. For w nonzero,
compatibility is equivalent to

    (T-lambda I)w+t b=0                                   (8.1)

for one uniquely determined scalar lambda. The scalar depends regularly
on a compatible point in each chart with a chosen nonzero coordinate of
w, so these charts define the same map to the affine lambda-line.

If lambda is not an eigenvalue of T, then T-lambda I is invertible and
(8.1) has a one-dimensional vector solution space. Its projectivization
is a single point. Thus a compatible family that dominates the
lambda-line has dimension at most one. Every compatible irreducible
surface must lie over one of the finitely many eigenvalues lambda_0.

Its ambient vector solution space is

    U_0=ker[(t,w) -> (T-lambda_0 I)w+t b] contained in E.

Since b is nonzero, dim U_0<=3, and ell is not in U_0. A projective
surface contained in P(U_0) forces dim U_0=3. All nonzero members of U_0
have w nonzero, and all satisfy compatibility. Therefore the entire
plane P(ell U_0) is identically compatible and is transverse to its
factor ell. Section 7.3 applies and again gives (7.2).

This argument also proves directly that the compatible rank-two locus
of K=ell E has dimension at most two; there is no omitted compatible
threefold case.

## 9. Exhaustive non-ternary consequence

Suppose a rank-six residual kernel K has full support and its compatible
rank-two locus has dimension at least two. Consider its generic rank.

- Generic rank four: a compatible surface is dense in a surface
  component of R_2(K), because R_2(K) is then a proper closed subset of
  P^3. By Sections 2--4 this component is a plane, or K=A B with
  complementary two-dimensional A,B. A plane gives a point of C_{1,3}
  by Section 7. The cross-block case gives a point of C_{2,2} by
  /research/hm/middle-surface/extremal-surface-geometry/GENERALIZATION.md, Section 4.
- Generic rank three: full support and Section 5 force every surface
  component to be a plane. Section 7 gives C_{1,3} again.
- Generic rank at most two: Section 1 gives K=ell E, and Section 8
  produces a transverse compatible plane, hence C_{1,3}.

Both C_{1,3} and C_{2,2} are fixed finite projective schemes under the
stated trilinear hypotheses. Therefore all full-support rank-six middle
lines having a compatible surface belong to the finite set

    image(C_{1,3}->P(V)) union image(C_{2,2}->P(V)).          (9.1)

No constancy of kernel type in a family, no global choice of block
factors, and no extension across a residual-rank boundary is needed.

If the established middle rank-drop support has dimension at most two,
an affine independent-zero component whose generic middle point has
rank six and full-support residual kernel has dimension at most six:
a positive-dimensional middle image has generic projective fiber of
dimension at most one by (9.1), and hence total projective dimension at
most three. A point middle image has projective fiber dimension at most
two by Sections 2, 5 and 8. Restoring the three separate nonzero scalings
adds three dimensions.

This last conclusion covers the full-support rank-six cases only. A
universal rank-six conclusion additionally requires the independent
supported-ternary proof. Lower residual ranks are outside this note.

## 10. Audit and limits

- Only abstract symbolic linear algebra and algebraic geometry are used.
- The quadric-cone exclusion uses dim K=dim E=4; larger symmetric
  factorizations can have nonzero radical generators and are not covered.
- The linear-space lemma uses factorization of complex binary quadrics;
  real classification without scalar extension would require care.
- No passage from rank-two compatibility to a rank-one boundary is
  assumed. Each use of a forbidden square is independently deduced
  from an explicit linear identity or from a binary cubic zero.
- The finite-incidence assertions are inherited from the cited local
  companion proof, whose hypotheses are listed explicitly in Section 6.
