# An isolated rank-five middle point with a two-dimensional independent-zero fiber

## Result and precise scope

Work over C. There exist a five-dimensional vector space V, a
20-dimensional vector space J, and a trilinear operation

    f: V × V × V → J

with the following properties:

1. f is symmetric in its outer variables and its cyclic sum is zero.
2. For every nonzero a, the repeated-input map
   A_a: V/Ca → J, [b] ↦ f(a,a,b), is injective.
3. For one specified middle line [u], the residual map Q_u has rank 5.
   At every other middle line [a], Q_a has rank 10.
4. The separately projectivized independent-zero fiber over [u] is
   nonempty and has dimension exactly 2.

Thus the residual-rank-drop support consists of a single point. In
particular it satisfies the hypothesis that this support has dimension
at most two. These hypotheses do not imply a pointwise bound of one for
independent-zero fibers at residual rank five.

This is an abstract synthetic quotient construction. It is not a model
claimed to be equivariant for the intended normalizer, nor an evaluation
or counterexample for the actual source operation. The total separately
projectivized independent-zero locus in this construction has dimension
2, and its all-inputs-nonzero affine version has dimension 5. In
particular this construction does NOT give a seven-dimensional affine
component or a two-dimensional middle family. It only rules out the
proposed pointwise fiber bound under the stated coarse hypotheses.

## 1. A five-dimensional ternary symmetric kernel

Write

    V = Cu ⊕ E,       dim E = 4,

and choose a three-dimensional subspace E0 of E. Let

    ell: Sym² E0 → C

be the functional corresponding to a nondegenerate symmetric bilinear
form on E0, and put

    K_res = ker ell,       dim K_res = 5.

Throughout, the symmetric-algebra convention is

    ab = (a ⊗ b + b ⊗ a)/2.

For q ∈ Sym² E0, its contraction map is q: E0^vee → E0. Its actual
symmetric contraction matrix will be denoted M(q). In particular,
M(e²)=e e^T, without a doubled diagonal or off-diagonal convention.

The rank-one points of P(K_res) are precisely

    C = { [e²] : [e] ∈ P(E0), ell(e²)=0 }.

The quadratic equation ell(e²)=0 defines a smooth plane conic because
ell is nondegenerate. Its Veronese image C is a closed smooth curve of
dimension 1 in P(K_res)=P⁴. Strictly speaking C itself is the Veronese
image of that plane conic (a degree-four curve in P⁴), not a plane conic
in its ambient P⁴. Only its smoothness, projectivity, and dimension are
used below.

### 1.1 The rank-two locus is smooth, irreducible, and three-dimensional

Let

    T = { [q] ∈ P(K_res) : rank q = 2 }.

Here is a convenient description that establishes all three assertions
without assuming irreducibility of a determinant polynomial. On
P(E0^vee), let S be the rank-two bundle with fiber ker(lambda) over
[lambda]. Restriction of ell gives a bundle map

    Sym² S → O.

It is surjective at every point. Otherwise the two-plane ker(lambda)
would be totally isotropic for a nondegenerate symmetric form on a
three-dimensional space, which is impossible: if a two-plane P were
totally isotropic then P ⊂ P^perp, but dim P^perp=1.

Consequently

    R = ker(Sym² S → O)

is a rank-two vector bundle. Its projective bundle P(R) is smooth and
irreducible of dimension 2+1=3. In each fiber P(R_lambda), the rank-two
condition is nonempty and open. Indeed this fiber is a projective line
inside P(Sym² ker(lambda))=P², whereas the rank-one binary symmetric
forms constitute a smooth conic, which contains no projective line.

Let P(R)^{(2)} be this nonempty rank-two open. Forgetting lambda gives
an isomorphism

    P(R)^{(2)} → T.

A rank-two q has unique annihilator line [lambda] for im q, and the
kernel/annihilator line varies algebraically on the constant-rank
locus. Thus T is smooth, irreducible, and of dimension 3. Equivalently,
it is the rank-two open of the determinant cubic threefold in P(K_res).
The latter description is not needed for the argument.

## 2. A linear correction with no compatible squares and a compatible surface

Let

    A = Hom(K_res,E0),       dim A = 15.

We show that v can be chosen in A with both of the following properties:

    v(e²) ∉ Ce whenever 0 ≠ e² ∈ K_res;                  (1)

    C_v = { [q] ∈ T : v(q) ∈ im q }
    is nonempty and has dimension exactly 2.             (2)

### 2.1 Avoiding every square is a nonempty open condition

For each square line [e²] in C, the condition

    v(e²) ∈ Ce

has codimension 2 in A. Evaluation at a nonzero e² is onto E0, and
membership in Ce imposes the two independent quotient coordinates in
E0/Ce. The corresponding incidence in C × A is a rank-13 vector bundle
over C, and therefore has dimension 1+13=14.

It is closed in C × A. Since C is projective, its projection to A is
closed, of dimension at most 14. Its complement U_square is therefore a
nonempty Zariski-open subset of the 15-dimensional affine space A, and
every v in U_square satisfies (1).

### 2.2 The universal rank-two compatibility incidence dominates A

On T, the images im q form a rank-two subbundle of E0 ⊗ O_T. The
quotient line bundle will be denoted Q. Compatibility is the vanishing
of the section of

    Hom(O_T(−1),Q) = O_T(1) ⊗ Q

induced by v. For each fixed [q]∈T, this is one nonzero linear condition
on A: evaluation at q followed by E0 → E0/im q is surjective. Thus the
universal incidence

    I = { ([q],v) ∈ T × A : v(q) ∈ im q }

is the total space of a rank-14 vector bundle over T. In particular I
is smooth and irreducible, and

    dim I = 3+14 = 17.                                    (3)

We must justify that I→A is dominant; dimension counting alone does
not prove this. Fix [q0]∈T and a nonzero projective tangent vector
xi∈T_[q0]T. Represent xi by a vector delta_q in K_res modulo Cq0, so
q0 and delta_q are linearly independent. Let lambda0 be a nonzero
annihilator of im q0. Choose a linear v0:K_res→E0 such that

    v0(q0)=0,
    lambda0(v0(delta_q)) ≠ 0.                             (4)

These two assignments are possible because q0 and delta_q are
independent. Extend arbitrarily to a linear map on K_res.

Locally near [q0], choose regular representatives q and lambda(q) of
the tensor line and its annihilator line. The incidence has local
scalar equation

    F(q,v) = lambda(q)(v(q)) = 0.

At (q0,v0), its derivative in the xi direction is

    d_q F(xi) = lambda0(v0(delta_q)) ≠ 0.                  (5)

The derivative of lambda contributes zero because v0(q0)=0. Equation
(5) implies that the differential of I→A is surjective at (q0,v0):
any change of v in its target can be offset by a tangent change of q.
Since I and A are smooth, the projection is smooth at this point, and
its image contains a nonempty open subset of A. In particular it is
dominant.

By the generic-fiber dimension theorem for a dominant morphism of
irreducible varieties, there is a nonempty open U_surface⊂A on which
the fibers are nonempty and have dimension

    dim I − dim A = 17−15 = 2.                            (6)

For nonemptiness, one may first restrict to a nonempty open contained
in the constructible dense image of I→A. The dimension theorem then
allows a further open restriction. No properness of T or I→A is being
assumed.

The irreducibility of A ensures U_square∩U_surface is nonempty. Fix v
in this intersection. Then (1) and (2) hold simultaneously. Notice
that (4) was only a witness to dominance. It was not asserted to
satisfy (1); intersecting the two nonempty opens is what establishes
simultaneous existence.

## 3. The universal trilinear operation

Put

    W = ker(V ⊗ Λ²V → Λ³V),       dim W = 40,

where the arrow is exterior multiplication, and define

    f0(a,b,c) = a ⊗ (b∧c) + c ⊗ (b∧a).

The exterior products of the two summands cancel. The operation takes
values in W, is outer symmetric, and has cyclic sum zero. Its
repeated-input map is

    A0_a(b) = f0(a,a,b) = a ⊗ (a∧b).

For every nonzero a, let

    F_a = im(Sym²V → W, bc ↦ f0(b,a,c)).

A splitting V=Ca⊕U gives

    Sym²V = Ca² ⊕ aU ⊕ Sym²U.

The first summand maps to zero. The second maps isomorphically to
A0_a(V)=a⊗(a∧U), of dimension 4. The third maps injectively into
U⊗(a∧U) by bc↦b⊗(a∧c)+c⊗(a∧b). Its dimension is 10, and its
first-factor summand differs from that of A0_a(V). Hence

    dim F_a = 14,
    F_a/A0_a(V) ≅ Sym²(V/Ca).                             (7)

Also

    F_a ⊂ V ⊗ (a∧V).                                     (8)

Let X be the projective rank-one tensor locus in P(W), for tensor rank
in V⊗Λ²V. It is precisely

    X = { [a⊗(a∧b)] : a∧b ≠ 0 }.

Indeed a⊗beta∈W means a∧beta=0. In a splitting V=Ca⊕U, exterior
multiplication by a is injective on Λ²U, so beta=a∧b. Thus X is the
closed image of the projective flag variety of a line in a two-plane:

    (Ca ⊂ span(a,b)) ↦ [a⊗(a∧b)].

Both subspaces can be recovered from the tensor factors. Consequently
X is closed and has dimension 4+3=7. A quotient of W preserves every
repeated-input injection if its projective kernel avoids X.

## 4. Prescribing the five-dimensional kernel graph

Use E0⊂E⊂V as the fixed splitting representatives. Define

    B0_u: Sym²E0 → F_u,
    B0_u(ab)=f0(a,u,b),

and set

    L = { B0_u(q) − A0_u(v(q)) : q∈K_res } ⊂ F_u.          (9)

This is a five-dimensional subspace. Projection onto
E0⊗(u∧E0) recovers B0_u(q), which is injective in q.

### 4.1 Exact matrix normalization and tensor support

Identify u∧E0 with E0. In first-factor rows Cu⊕E0 and second-factor
columns u∧E0, the tensor in (9) has block matrix

    [ −v(q)^T ]
    [  2M(q)  ].                                          (10)

The factor two is essential: our symmetric-algebra convention gives
B0_u(e²)=2e⊗(u∧e). Since M(q) is symmetric, the row space of (10),
identified with a subspace of E0, is exactly

    im q + Cv(q).

Thus the second-factor support of the tensor (9) is

    u∧(im q + Cv(q)),                                     (11)

and its tensor rank is dim(im q+Cv(q)).

For rank q≥2 this rank is at least 2. For rank q=1, write q=e² after
rescaling e; then condition (1) makes im q+Cv(q)=Ce+Cv(q) two-
dimensional. Therefore every nonzero tensor in L has tensor rank at
least 2, and

    P(L) ∩ X = ∅.                                         (12)

This argument does not confuse symmetric rank of q with tensor rank
of its graph lift. The correction row in (10) is exactly what prevents
rank-one q from producing rank-one lifted tensors.

### 4.2 No other middle image meets L

We claim

    L ∩ F_a = 0 whenever [a]≠[u].                         (13)

Suppose a nonzero tensor from L also belonged to F_a. By (8) and (11),
its second-factor support would be contained in a∧V. That support
contains u∧w1 and u∧w2 for independent w1,w2 in E0, because it has
dimension at least 2. The first containment implies

    a∧u∧w1=0, hence a∈span(u,w1),

and the second implies a∈span(u,w2). Since u,w1,w2 are independent,
the intersection of those two planes is Cu. This forces [a]=[u] and
proves (13).

## 5. Extending L to a global quotient kernel

Let

    W_bar = W/L,       dim W_bar = 35,
    G = Gr(15,W_bar),       dim G = 15·20 = 300.

A point M of G specifies a 20-dimensional subspace K_tot⊂W containing
L by inverse image under W→W_bar. We impose the following three
conditions and show that each holds on a nonempty open of G.

### 5.1 Avoid the whole repeated-input variety

Because of (12), projection with center P(L) restricts to a morphism
X→P(W_bar). Its image Y is closed, since X is projective, and dim Y≤7.
For a fixed point [h] of P(W_bar), the 15-planes containing Ch form
Gr(14,34), of dimension 14·20=280. Therefore

    { (y,M)∈Y×G : y∈P(M) }

has dimension at most 7+280=287<300. Its projection to G is closed
and proper, so there is a nonempty open on which

    P(K_tot) ∩ X = ∅.                                     (14)

### 5.2 Retain exactly L in F_u

The space H_u=F_u/L⊂W_bar has dimension 14−5=9. The condition

    M ∩ H_u = 0

is nonempty open: 15+9≤35, and one can choose M in a complement to
H_u. Equivalently,

    K_tot ∩ F_u = L.                                      (15)

### 5.3 Avoid every other middle image simultaneously

Let B=P(V)\{[u]}, of dimension 4. The spaces F_a form a rank-14
subbundle of W⊗O over P(V): the map defining them is algebraic and
has constant rank 14 by (7). Equation (13) shows that on B their
images H_a in W_bar form a rank-14 subbundle H⊂W_bar⊗O_B.

The relative incidence

    T_bad = { (a,[h],M) : a∈B, [h]∈P(H_a), [h]∈P(M) }

has dimension

    dim B + 13 + dim Gr(14,34)
      = 4+13+280 = 297 < 300.                             (16)

More explicitly, it is the relative Grassmannian of 15-planes
containing a specified line over the 17-dimensional space P_B(H).
Its image in G is constructible and consists exactly of the M meeting
at least one H_a. Since the source has dimension 297, the closure of
this image has dimension at most 297. Removing that closure gives a
nonempty open on which

    K_tot ∩ F_a = 0 for every [a]≠[u].                    (17)

Taking the closure is important: the base B is not proper, so its
incidence image need not itself be closed.

Since G is irreducible, the three nonempty open conditions intersect.
Choose K_tot in their intersection. In fact (14) also follows from
(12), (15), and (17), because each repeated-input tensor belongs to
some F_a; the separate incidence proof of (14) is harmless and makes
global injection explicit.

## 6. The quotient and its exact residual ranks

Set

    J = W/K_tot,       dim J=20,
    f = p∘f0,

where p is the quotient map. Outer symmetry and cyclic zero descend.
By (14), every map

    A_a: V/Ca → J, [b] ↦ p(A0_a(b))

is injective. Define the residual map by

    Q_a: Sym²(V/Ca) → J/A_a(V/Ca),
    [b][c] ↦ f(b,a,c) modulo A_a(V/Ca).

Changes of lifts add only A_a-values, so this map is well defined.
By (7) and injectivity of A_a,

    rank Q_a = dim p(F_a) − 4
             = 10 − dim(K_tot∩F_a).                      (18)

Equations (15) and (17) now give

    rank Q_u = 5,
    rank Q_a = 10 whenever [a]≠[u].                       (19)

Under the fixed identification V/Cu=E,

    ker Q_u = K_res ⊂ Sym²E0 ⊂ Sym²E.                    (20)

To check this directly, the general kernel is
((K_tot∩F_u)+A0_u(V))/A0_u(V). By (15) it is the image of L, and
projection of (9) to F_u/A0_u(V) is exactly q∈K_res.

Moreover (9) vanishes after applying p, so on K_res

    B_u(q) = A_u(v(q)),
    B_u(ab) = f(a,u,b).                                   (21)

Thus the linear correction v used in Section 2 is precisely the
correction entering the full zero equation, with no sign or factor-two
change.

## 7. Exact independent-zero fiber dimension

An independent triple with middle line [u] has two independent
residual outer vectors a,b∈E. Their product q=ab is a nonzero rank-two
symmetric tensor. By (20), a zero triple must have [q]∈T. Conversely,
every rank-two tensor over C factors as a product ab of independent
vectors, uniquely up to rescaling the factors and interchanging their
lines.

Write the outer lifts as

    x = a+alpha u,       z = b+beta u.

Using (21), outer symmetry, and f(u,u,u)=0 gives

    f(x,u,z) = A_u(v(q)+beta a+alpha b).                   (22)

Since A_u is injective, a zero exists precisely when

    v(q) ∈ span(a,b) = im q.

If v(q)=nu a+mu b, the unique outer directions for this ordered
factorization are

    [x]=[a−mu u],       [z]=[b−nu u].                     (23)

They are independent together with u, because their residual vectors
a,b are independent. Changing representatives of the factor lines
rescales these reconstructed vectors, and interchanging the factor
lines interchanges the two outer directions.

Algebraically, the two ordered factorizations form a finite étale
cover of degree two over the rank-two locus T: a nondegenerate binary
quadratic has two distinct factor lines. Restricting it to C_v and
using (23) identifies that cover with the separately projectivized
independent-zero fiber over [u]. This is also the established
ordered-factor reconstruction from
../rank-nine-independent-incidence/PROOF.md.

The cover is finite and surjective, so by (2)

    dim(projective independent-zero fiber over [u]) = 2. (24)

At every other middle line, Q_a is injective by (19), so there are no
independent zero triples. Hence the whole separately projectivized
independent-zero locus has dimension 2. Restoring the three independent
nonzero input scales is a (G_m)^3-torsor and gives affine dimension 5.
Fixing an actual middle vector instead leaves two scales and gives
dimension 4 for that affine fiber.

## 8. What the construction rules out, and what remains open

The model satisfies outer symmetry, cyclic zero, global repeated-input
injection, generic residual rank 10, and a residual-rank-drop support
of dimension zero. Nevertheless its exceptional rank-five middle fiber
has projective dimension 2. Thus those assumptions alone cannot
establish the pointwise fiber bound

    projective independent-zero fiber dimension ≤ 1

at every residual-rank-five middle point.

The model does not obstruct a global affine bound six: its own affine
independent-zero locus has dimension only five. It provides no
positive-dimensional middle family, no seven-dimensional independent-
zero component, and no occurrence result for a specified equivariant
source operation.

If a proposed symmetry group on V has an element moving [u], this
particular quotient cannot be equivariant for any compatible action
on J. Equivariance preserves residual ranks, whereas (19) singles out
[u]. This observation underscores the separation of hypotheses; it
does not establish that equivariance by itself excludes rank five or
two-dimensional fibers.

## Audit and operational scope

The proof uses abstract tensor spaces, bundle ranks, incidence
dimensions, and generic existence. It does not evaluate the actual
source operation, choose actual source inputs, compute a source matrix
rank, mutate any source files, or perform numerical/large computation.
Only local mathematical proof and review artifacts are written.
Dimensions concern reduced supports; no reducedness of the residual
rank-drop scheme is claimed.
