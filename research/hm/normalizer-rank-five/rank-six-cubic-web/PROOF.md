# Exclusion of an irreducible cubic web supported on three variables

## Result and precise scope

Work over an algebraically closed field of characteristic zero (in particular,
over C). Let E be four-dimensional, E0 a three-dimensional subspace, and

    K subset Sym^2 E0 subset Sym^2 E,       dim K=4.

Suppose K contains a tensor of rank three and the determinant polynomial of its
three-by-three symmetric contraction matrix is an irreducible homogeneous cubic
D on K. Let v:K -> E be linear. If

    v(q) belongs to im(q:E0^vee -> E0)

for a dense set of rank-two points of the cubic surface {D=0} in P(K), then
there is a single c in E0^vee such that

    v(q)=q(c) for every q in K.                              (1)

Moreover K contains a nonzero square e^2. Equation (1) therefore makes that
square compatible:

    v(e^2)=c(e)e.

Under the trilinear identities and global repeated-input injection from
/research/hm/normalizer-rank-five/extremal-kernel-planes/PROOF.md, this is impossible for a residual kernel
K=ker Q_u. Consequently the rank-two compatibility locus in this cubic surface
has dimension at most one. With the established middle rank-drop support bound
at most two, an affine independent-zero component generically of this rank-six
supported-ternary, irreducible-cubic type has dimension at most six.

This is not a classification of arbitrary four-dimensional subspaces of
Sym^2 E, and does not exclude every rank-six kernel. The separate extension
REDUCIBLE.md treats reducible determinant cubics within the same supported-
ternary subclass.

## 1. Conventions and the exact compatibility condition

Use the symmetric-algebra convention ab=(a tensor b+b tensor a)/2. Contraction
therefore means

    (ab)(c) = (c(a)b+c(b)a)/2,
    (e^2)(c) = c(e)e.

In a basis of E0, a tensor is represented by its actual symmetric contraction
matrix M(q), not by a coefficient matrix with doubled off-diagonal entries.
The determinant D(q)=det M(q) is homogeneous of degree three. Its nonvanishing
at one point is exactly the generic rank-three assumption. Changing the basis
multiplies the determinant polynomial by a nonzero scalar, so irreducibility is
well defined.

For the incidence application fix a nonzero middle vector u in V, dim V=5,
put E=V/Cu, and choose a linear splitting s:E -> V. The repeated-input map is

    A_u:E -> J,       e |-> f(u,u,s(e)).

It is injective. For q in the residual kernel K, put

    v(q)=A_u^{-1} B_s(q),       B_s(ab)=f(s(a),u,s(b)).

This is linear. For a rank-two tensor q=ab with independent a,b, its contraction
image is span(a,b), and the exact outer-lift reconstruction says that independent
zero triples over [q] exist if and only if

    v(q) belongs to im q.                                   (2)

This is the compatibility condition used throughout. If the splitting changes
to s+d u, with d in E^vee, the precise formula is

    v'(q)=v(q)+2q(d).

Thus (2) is splitting independent. In particular no factor of two is missing
from (1): c is a contraction functional, and the splitting that kills (1) on K
is obtained by extending c to E^vee and using d=-c/2.

## 2. The rank-two locus is a dense open of the integral cubic

Let S=V(D) in P(K)=P^3 with the hypersurface scheme structure. Here
"irreducible cubic" means that the degree-three polynomial D is irreducible,
not merely that its reduced support is irreducible. The polynomial ring on K
is a UFD, so (D) is prime; S is reduced and integral, of dimension two.

For linear coordinates t_i on K, write M=M(t) and M_i=partial M/partial t_i.
Differentiation of the determinant gives

    partial D/partial t_i = trace(adj(M) M_i).

At a matrix of rank at most one, adj(M)=0, so every first derivative of D
vanishes. Such points are singular on S. On the other hand, an irreducible
hypersurface in characteristic zero has a nonempty dense smooth open. Directly,
some first derivative of D is nonzero, and its degree is less than deg D, so
it cannot vanish identically on V(D). Therefore smooth points of S have
matrix rank two. The rank-two locus T is consequently a nonempty dense open
of the integral surface S.

No smoothness of all of S, reducedness of the surrounding residual incidence,
or assertion about its rank-one subscheme is needed.

## 3. The adjugate divisibility argument

Suppose compatibility (2) holds on a dense subset of T.

First project v to E/E0. Each coordinate of the resulting linear map is a
homogeneous linear polynomial on K. It vanishes on the dense compatible
subset of S, because im q is contained in E0. Since S is integral, each such
polynomial vanishes on all of S and is divisible by D. A nonzero polynomial
of degree one cannot be divisible by a cubic, so

    v(K) subset E0.                                         (3)

Now regard v as a column vector in E0. If M has rank two, then

    im M = ker adj(M).

Indeed M adj(M)=0 and adj(M) has rank one, so its kernel and im M are both
two-dimensional. Hence compatibility on the dense subset implies

    adj(M(q)) v(q)=0

there. Every coordinate on the left is a homogeneous polynomial of degree
three. It vanishes on the integral cubic S and is therefore divisible by D.
The quotient has degree zero. There is thus a constant column c such that

    adj(M(q)) v(q)=D(q)c                                    (4)

as a polynomial identity on all of K. The column c is the coordinate column
of a single covector in E0^vee, as appropriate for contraction.

Multiplying (4) by M(q), and using M adj(M)=D I, gives

    D(q)v(q)=D(q)M(q)c.

The polynomial ring on K is an integral domain and D is nonzero. Cancelling
D in each coordinate yields

    v(q)=M(q)c

identically on K, including singular matrices. Equivalently this equality
holds first on the nonempty invertible open and extends polynomially. This
proves (1).

## 4. Every such web contains a square

The rank-one symmetric tensors in P(Sym^2 E0)=P^5 form the closed Veronese
surface

    nu_2(P(E0)) = { [e^2] : [e] in P(E0) }.

Its dimension is two. Since P(K) is a projective three-plane, the projective
dimension theorem gives

    P(K) intersect nu_2(P(E0)) is nonempty,

because 3+2=5. This only needs nonemptiness, not transversality, a reduced
intersection, or the expected number of intersection points. Equivalently,
K has codimension two in Sym^2 E0, so the two linear equations cutting out K
pull back to two homogeneous quadrics on P^2; over an algebraically closed
field they have a common projective zero.

Choose a nonzero e with e^2 in K. Equation (1) now gives

    v(e^2)=c(e)e.

## 5. A compatible square violates global repeated-input injection

For clarity, recall the pointwise contradiction without importing any scheme
assumption. Suppose e is nonzero, e^2 lies in K=ker Q_u, and v(e^2)=rho e.
Set

    x=s(e)-(rho/2)u.

The defining equation for v, outer symmetry, and f(u,u,u)=0 give

    f(x,u,x)
      =f(s(e),u,s(e))-rho f(u,u,s(e))
      =0.

Cyclic zero and outer symmetry imply

    f(x,u,x)+2f(x,x,u)=0,

so f(x,x,u)=0. The residual image of x is e, hence x and u are independent.
The class of u in V/Cx is nonzero, contrary to injectivity of A_x.

This uses repeated-input injection at the reconstructed vector x, and is the
reason injection merely at the fixed middle vector u would not suffice.

## 6. Dimension consequence and scheme audit

The rank-two compatibility condition is the vanishing of a regular vector-
bundle section on T, as constructed in
/research/hm/incidence-foundations/rank-nine-independent-incidence/PROOF.md. If its zero locus had dimension
two, its reduced support would be dense in the irreducible surface T. The
argument above would give the forbidden compatible square. Hence its dimension
is at most one, regardless of possible nilpotents.

The ordered-factor cover of that compatibility locus is finite etale of degree
two and is the separately projectivized independent-zero fiber. It therefore
also has dimension at most one. For an independent-zero component whose
geometric generic middle point has this supported-ternary irreducible-cubic
kernel, the geometric generic fiber has dimension at most one. Its middle
image has dimension at most two by the standing rank-drop support hypothesis.
The projective component thus has dimension at most three. Restoring the three
independent nonzero input scalings adds three, giving affine dimension at most
six.

All proofs above work after passing to an algebraic closure of the middle
function field. No simultaneous choice of E0, a basis, or the contraction
functional c along the middle family is required for this dimension argument.

What the proof does and does not require:

- The determinant polynomial is genuinely irreducible, hence squarefree.
- Set-theoretic compatibility on a dense set of rank-two geometric points is
  sufficient; a stronger scheme-theoretic compatibility hypothesis is unnecessary.
- Divisibility is performed in the polynomial ring on K against its prime
  principal ideal (D), never against an unspecified nonreduced incidence ideal.
- The Veronese intersection is used only to obtain one actual geometric square.

## 7. A limited squarefree extension

The same adjugate argument works if D is squarefree but reducible, provided
compatibility holds densely on EVERY irreducible component of V(D). Each
component has a dense locus where the whole hypersurface is smooth; those
points have matrix rank two by the determinant derivative calculation.
The outside-E0 coordinates and adj(M)v then vanish on every component, so
are divisible by every distinct irreducible factor and hence by D. The same
degree comparison and cancellation produce v(q)=q(c).

Compatibility on just one component only gives divisibility by that component's
factor. It does not justify division by all of D. A two-dimensional compatible
locus in a reducible determinant surface may occupy just one component, so this
limited extension alone gives no general reducible-case dimension bound.
