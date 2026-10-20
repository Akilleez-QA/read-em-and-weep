# Completion of the supported-ternary rank-six case

## Result and scope

Work over an algebraically closed field of characteristic zero. Let E0 be a
three-dimensional subspace of a four-dimensional space E, and let

    K subset Sym^2 E0,       dim K=4.

Let v:K -> E be linear and suppose no nonzero square in K is compatible:

    e^2 in K, e!=0   implies   v(e^2) not in Ce.             (NS)

For residual kernels of the trilinear operation in the standing hypotheses,
(NS) follows from global repeated-input injection, by PROOF.md, Section 5.

Then the locus of rank-two [q] in P(K) for which

    v(q) belongs to im(q:E^vee -> E)

has dimension at most one. This includes all reducible, nonreduced, and
irreducible determinant cubics. In particular, K automatically contains a
rank-three tensor; no additional generic-rank-three hypothesis is needed.

With the established middle-image dimension bound at most two, every affine
independent-zero component whose geometric generic rank-six kernel is supported
on a three-dimensional subspace has dimension at most six.

This classifies only the determinant alternatives inside a four-dimensional
TERNARY web. It is not a classification of general four-dimensional kernels
in Sym^2 E with four-dimensional total support.

## 1. Two compatible plane types already violate (NS)

We use the audited theorem from ../extremal-kernel-planes/PROOF.md, Section 2:
a three-dimensional vector space H of symmetric tensors, all of rank at most
two, has one of the forms

    H=Sym^2 W, dim W=2;             or             H=eU, dim U=3.

If H is contained in Sym^2 E0, then W is contained in E0 in the first case,
and in the second case e belongs to E0 and U=E0. To see the latter, a product
e a with a independent of e has image span(e,a), necessarily contained in E0.
Doing this for the elements of U gives e,U subset E0, and dimensions give U=E0.

Suppose compatibility is dense in the rank-two part of P(H). The compatibility
condition is closed on the rank-two open, so it holds everywhere on that open.

### 1.1 Binary plane

For H=Sym^2 W, every rank-two tensor has image W. Density and linearity imply
v(H) subset W. The expression

    e wedge v(e^2),       e in W,

is a homogeneous cubic taking values in the one-dimensional space wedge^2 W.
A homogeneous binary cubic over an algebraically closed field either vanishes
identically or has a projective zero. Thus some nonzero e has v(e^2) in Ce,
contradicting (NS).

### 1.2 Common-factor plane

For H=eE0, choose f,g so that e,f,g are a basis of E0. For every nonzero t,

    e(e+t f),       e(e+t g)

have rank two and images span(e,f) and span(e,g), respectively. Compatibility
and linearity, or simply taking the algebraic limit t=0 in these fixed closed
subspaces, imply

    v(e^2) in span(e,f) intersect span(e,g)=Ce.

Again this contradicts (NS).

These arguments allow v to take values in the larger space E; they do not
assume at the outset that v(K) is contained in E0.

## 2. Normal forms for a web containing a rank-at-most-two hyperplane

Suppose H subset K is a three-dimensional subspace consisting of rank-at-most-
two tensors. Write K=H+Cq0 with q0 outside H. All displayed matrices are actual
symmetric contraction matrices for ab=(a tensor b+b tensor a)/2.

### 2.1 H=Sym^2 W

Choose E0=W direct-sum Ce3. Subtracting an element of H from q0 removes its
upper-left two-by-two block. Every element of K then has the matrix

    M(A,t) = [ A      t h ],
             [ t h^T  t d ]

where A is an arbitrary symmetric two-by-two matrix, h in W and d a scalar
are fixed, and (h,d)!=(0,0) because q0 is outside H. Direct expansion gives

    det M = t (d det A - t h^T adj(A) h).                    (1)

If d!=0, complete the square in the extra tensor:

    2 e3 h + d e3^2
      = d(e3+h/d)^2 - h^2/d.

The last term is in H. With e3'=e3+h/d this gives the normal form

    K=Sym^2 W direct-sum C(e3')^2,
    M = [ a b 0 ],       D=t(ac-b^2).                       (B)
        [ b c 0 ]
        [ 0 0 t ]

The cubic is the product of one plane and an irreducible rank-three quadric
cone.

If d=0, then h!=0. Choose the basis of W so that h has coordinates (1,0),
absorbing a nonzero scalar into t. This gives

    M = [ a b t ],       D=-c t^2.                          (N)
        [ b c 0 ]
        [ t 0 0 ]

The reduced determinant support is the union of two distinct planes. The
plane t=0 is binary, and the plane c=0 is the common-factor plane e1 E0.
In both alternatives D is nonzero.

### 2.2 H=eE0

Choose a basis e,f,g. Subtracting a member of H from q0 removes its first row
and column, leaving a nonzero symmetric two-by-two block B. Every element is

    M = [ a    x^T ],
        [ x    t B ],

with a,t arbitrary and x a two-component arbitrary column. Its determinant is

    D=t(a t det B - x^T adj(B)x).                           (2)

If B has rank two, over the algebraically closed field it can be brought by
congruence to the hyperbolic matrix with off-diagonal entries one. Thus

    K=span(e^2,ef,eg,fg),
    M = [ a b c ],       D=t(2bc-at).                       (C)
        [ b 0 t ]
        [ c t 0 ]

The second factor is a nondegenerate rank-four quadratic polynomial, hence
its projective surface is a smooth irreducible quadric. Intrinsically

    K = span(e,f) span(e,g),

and the quadric is the Segre image of P(span(e,f)) times P(span(e,g)) under
multiplication. The products e^2,ef,eg,fg are a basis, so this multiplication
map is the Segre embedding into P(K), with no projection or identification.

If B has rank one, choose B=diag(1,0). Then

    M = [ a b c ],       D=-t c^2.
        [ b t 0 ]
        [ c 0 0 ]

This is the same web type as (N), with the names of the independent coordinates
changed. Again the determinant support consists of two planes. There is no
rank-zero alternative because B!=0. Thus D is nonzero in every case.

These computations establish all possibilities for a four-dimensional ternary
web containing a rank-at-most-two hyperplane: (B), (C), or (N).

## 3. A four-dimensional ternary web cannot have identically zero determinant

Suppose, to the contrary, that every element of K has rank at most two. Choose
any three-dimensional hyperplane H subset K. The audited classification puts
H into one of the two forms of Section 1. Choose q0 outside H. Section 2 then
computes its determinant and shows that it is nonzero in every possible case,
a contradiction.

Therefore det|K is a nonzero homogeneous cubic for EVERY four-dimensional
K subset Sym^2 E0. In particular rank three occurs on a nonempty open subset.

This deduction uses only the already-proved three-dimensional bounded-rank
classification, not a new general classification of four-dimensional bounded-
rank spaces.

## 4. Reducible cubics have exactly the alternatives above

If D is reducible, it has a nonzero linear factor L, since its degree is three.
The vector hyperplane H=ker L in K consists entirely of singular matrices and
has dimension three. Section 2 applies. Consequently the only reducible
possibilities, up to a change of basis and linear coordinates, are:

- (B): a binary plane and an irreducible quadric cone;
- (C): a common-factor plane and a smooth irreducible quadric;
- (N): two distinct plane components, one with multiplicity two.

In particular the computations also rule out three distinct plane factors,
a triple plane, or any additional nonreduced cubic type in this subclass.
No reducedness hypothesis was used to obtain these alternatives.

## 5. Compatibility on either quadric forces its distinguished square

Assume compatibility is dense in a rank-two open subset of one irreducible
quadric component. Its zero condition is a regular bundle section on the
ambient rank-two locus, so it vanishes on the entire reduced rank-two open
of that component. This includes rank-two points where the quadric meets the
other determinant component. No extension of the image bundle through a
rank-one point is assumed.

### 5.1 The binary-plus-square web (B)

Write E0=W direct-sum Ce3. The quadric component is det A=0, and its points
are represented by

    q=w^2+t e3^2,

allowing rescaling and the vertex e3^2. Fix any nonzero w in W. The line

    q_s=e3^2+s w^2

lies on that quadric, and for every s!=0 its tensor has rank two with the
fixed image span(e3,w). Compatibility therefore implies, on taking s=0 in
the linear map v,

    v(e3^2) in span(e3,w).

Choose two independent w in W. The two planes intersect in Ce3, so
v(e3^2) belongs to Ce3. This violates (NS).

### 5.2 The common-factor-plus-product web (C)

Here K=span(e^2,ef,eg,fg), and the quadric is the product surface described
in Section 2.2. Its two ruling lines through the square [e^2] contain

    q_s=e(e+s f),       r_s=e(e+s g).

For s!=0 their images are span(e,f) and span(e,g), respectively. These
rank-two points belong to the quadric even though they also belong to the
plane component t=0. The extension on the rank-two open already proved at
the start of this section applies to them. Passing to s=0 in each fixed
image plane gives

    v(e^2) in span(e,f) intersect span(e,g)=Ce,

again violating (NS).

These fixed-plane arguments use ordinary linear continuity (equivalently,
polynomial specialization in s). They do not incorrectly assert that image
spaces automatically extend with the same rank at a rank-one limit.

## 6. Exhaustion of possible compatible surfaces

Since D is nonzero, the rank-at-most-two locus in P(K)=P^3 has two-dimensional
hypersurface support. The rank-two locus is an open subset of it.

If D is irreducible, PROOF.md gives dimension at most one for the compatibility
locus. If D is reducible, Section 4 lists all irreducible surface components.
A two-dimensional compatibility locus must be dense in the rank-two open of
at least one such component. Every plane component is excluded by Section 1;
every quadric component is excluded by Section 5. This rules out dimension two.

For clarity, in (B), (C), and (N), the indicated plane and quadric components
all have nonempty dense rank-two opens, as follows either from the displayed
matrices or the product descriptions. Multiplicities of determinant components
in (N) cannot change the dimension of the compatibility locus. The argument
uses reduced component supports only and makes no assertion that the ambient
zero scheme is reduced.

Thus every four-dimensional ternary web satisfying (NS) has compatibility
locus of dimension at most one.

## 7. Residual-kernel consequence and limitations

For a rank-six residual kernel, dim K=10-6=4. If its total tensor support is
contained in a three-dimensional E0, the compatible-square exclusion follows
from the global repeated-input injection, and the preceding theorem applies.
The ordered-factor cover and unique outer-lift reconstruction identify the
projectivized independent-zero fiber with a finite etale degree-two cover of
the compatibility locus. Its dimension is therefore at most one.

Over a middle image of dimension at most two, any independent-zero component
generically of this type has separately projectivized dimension at most three
and affine dimension at most six. The proof works over an algebraic closure
of the middle function field, so no global choice of E0 or simultaneous normal
form is required.

The hypothesis "supported on three dimensions" is essential to this scope.
A general four-dimensional subspace of Sym^2 E may have four-dimensional
support, whose rank-two locus is not covered by the ternary determinant
classification. No statement here resolves those other rank-six cases.

All arguments concern symbolic tensor spaces. No actual source operation,
source matrix, selected source input or value, numerical rank computation,
external communication, or source write has been performed. The only writes
are these local proof and review artifacts.
