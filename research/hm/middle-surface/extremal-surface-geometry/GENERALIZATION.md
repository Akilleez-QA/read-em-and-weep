# Rectangular annihilation finiteness and the rank-six cross-block case

## Results and hypotheses

Let V have dimension n>=4 over C, let J be finite dimensional, and let
f:V x V x V -> J be trilinear, outer symmetric, and cyclic-zero. Assume
for every nonzero a that

    A_a:V/Ca -> J,       [b] |-> f(a,a,b)

is injective. Fix positive integers p,q with p+q=n-1.

The closed incidence scheme

    C_{p,q} = { ([u],X,Z) in P(V) x Gr(p,V) x Gr(q,V)
                : f(X,u,Z)=0 }

is finite over C, possibly empty or nonreduced. In particular every
geometric point automatically satisfies

    V = Cu direct-sum X direct-sum Z.                         (1)

For n=5, p=q=2, this excludes a positive-dimensional middle family with
residual kernel A B, where E_u=V/Cu=A direct-sum B and dim A=dim B=2,
if compatibility vanishes on the entire rank-two Segre surface of that
kernel. Under the established middle rank-drop support bound at most
two, an affine independent-zero component generically of this rank-six
cross-block type has dimension at most six.

This does not classify general four-dimensional residual kernels or
exclude every rank-six independent component. It is a separate
extension of PROOF.md and leaves that frozen proof unchanged.

## 1. Two repeated-input values on an independent plane

For independent a,b, the vectors A_a(b) and A_b(a) are linearly
independent. This is the identity already proved in PROOF.md, Section 1,
but its short verification is included here.

Cyclic-zero and outer symmetry give

    f(b,a,b) = -2 A_b(a),
    f(a,b,b) = A_b(a),
    f(b,b,b) = 0.

Consequently

    A_{a+t b}(b) = A_a(b) - t A_b(a).

Both original values are nonzero by injection. If they were dependent,
one could choose t to make this expression zero. The vectors a+t b and
b remain independent, contradicting injection at a+t b. In particular,

    A_a(b) + A_b(a) != 0                                   (2)

whenever a,b are independent.

## 2. The direct decomposition is forced by annihilation

Fix a point ([u],X,Z) of C_{p,q}, with u nonzero. No directness condition
has been imposed in the definition of the incidence. We prove it.

### 2.1 The middle line belongs to neither outer subspace

Suppose u belongs to X. Then for every z in Z,

    0 = f(u,u,z) = A_u(z).

Injection implies Z is contained in Cu. Since q is positive, this forces
q=1 and Z=Cu. Now for every x in X, outer symmetry gives

    0 = f(x,u,u) = A_u(x).

Injection implies X is contained in Cu, so p=1 and X=Cu. We would have
p+q=2=n-1, hence n=3, contrary to n>=4. Therefore u is not in X.
The same argument with X and Z exchanged proves u is not in Z.

This handles p=1 or q=1 as well as the larger cases. No hidden assumption
that both outer dimensions exceed one is used.

### 2.2 The outer subspaces are disjoint

If 0!=a belongs to X intersect Z, annihilation and the cyclic identity give

    0 = f(a,u,a) = -2 A_a(u).

Injection at a implies u belongs to Ca, hence u belongs to X. This
contradicts Section 2.1. Thus X intersect Z=0.

### 2.3 Their sum does not contain the middle line

Suppose u belongs to X+Z, and write u=a+b with a in X and b in Z.
Neither a nor b can be zero by Section 2.1. They are independent by
Section 2.2. But annihilation gives

    0 = f(a,u,b)
      = f(a,a,b) + f(a,b,b)
      = A_a(b) + A_b(a),

contradicting (2). Hence u is not in X+Z. As the dimensions sum to
1+p+q=n, this proves (1).

The dimension threshold is genuine for this argument: in dimension
three with p=q=1, the incidence contains every triple
([u],Cu,Cu), since f(u,u,u)=0. It is therefore not finite in that case.

## 3. Projective projector rigidity proves finiteness

Let

    P = P(V) x Gr(p,V) x Gr(q,V),

with tautological bundles U, X, Z of ranks 1,p,q. The trilinear map
induces the bundle map

    X tensor U tensor Z -> J tensor O_P.

Its zero scheme is C_{p,q}. Thus C_{p,q} is a closed subscheme of the
projective variety P, and is projective of finite type.

Let T be a reduced irreducible component of C_{p,q}. The natural map

    U direct-sum X direct-sum Z -> V tensor O_T

is an isomorphism on all geometric fibers by Section 2. It is therefore
an isomorphism of vector bundles. The three projections onto these
summands are global endomorphisms of the trivial bundle V tensor O_T.
Their matrix entries are elements of H^0(T,O_T)=C, since T is integral
and projective. All three projectors are constant matrices.

Their images give a fixed line U and fixed subspaces X,Z. Therefore all
three coordinate maps from T to P(V), Gr(p,V), Gr(q,V) are constant.
Since T is a subvariety of their product, T is one point.

There are finitely many irreducible components, so C_{p,q} is a
zero-dimensional projective scheme. Hence it is finite over C.
Nilpotent structure at its finite support is not ruled out.

This proof uses the entire closed incidence; no family can evade it by
approaching an intersecting or noncomplementary boundary configuration,
because Section 2 rules out every such boundary point by injection.

## 4. The rank-six cross-block residual kernel

Now specialize to n=5 and a nonzero middle vector u. Put E=V/Cu and
assume the residual map Q_u has rank six, with

    E = A direct-sum B,       dim A=dim B=2,
    K = ker Q_u = A B subset Sym^2 E.                       (3)

Here A B is the image of symmetric multiplication A tensor B -> Sym^2 E.
That map is injective, and its image has dimension four.

### 4.1 Its rank-two locus is exactly a smooth Segre surface

After choosing bases of A and B, an element of A B has a symmetric
matrix, up to the harmless fixed nonzero normalization factor, of form

    [ 0  M  ]
    [ M^t 0 ],

where M is a 2-by-2 matrix. Its rank is twice rank M: its kernel is the
direct sum of ker M^t in A and ker M in B. Consequently every nonzero
element of A B has symmetric rank two or four, and rank two holds
exactly when rank M=1.

Thus the entire projective rank-two locus is

    Sigma = { [a b] : [a] in P(A), [b] in P(B) }
          = P(A) x P(B) subset P(K)=P^3.

It is the smooth irreducible Segre quadric surface. There are no
rank-one points. The two factors of a rank-two element lie one in A and
one in B, uniquely up to their individual scalar choices.

### 4.2 Compatibility is a linear-map condition on the Segre surface

Choose any linear splitting s:E->V. For k in K define the linear map

    v:K -> E,       v(k)=A_u^(-1) B_{s,u}(k),

where B_{s,u}(a b)=f(s(a),u,s(b)). This is well defined because K is the
residual kernel. Identical compatibility on Sigma means exactly

    v(a b) belongs to span(a,b) for all a in A and b in B.    (4)

It suffices initially to impose (4) for nonzero a,b. Zero inputs give
zero by linearity, and identical vanishing on a dense subset of Sigma
extends to the whole surface because the compatibility section is
regular and Sigma is reduced and irreducible.

Let pi_A,pi_B be the projections of E=A direct-sum B. For a fixed
nonzero b, the endomorphism

    A -> A,       a |-> pi_A v(a b)

preserves every line Ca by (4). A linear endomorphism preserving every
line is scalar: evaluate it on two independent vectors and their sum.
Thus pi_A v(a b)=lambda(b)a. The scalar lambda(b) depends linearly on b.
For example fix a nonzero a_0 and a functional eta with eta(a_0)=1;
then lambda(b)=eta(pi_A v(a_0 b)), a linear expression. Similarly
pi_B v(a b)=mu(a)b for a linear functional mu on A. Therefore

    v(a b) = lambda(b)a + mu(a)b,
    lambda in B^vee,       mu in A^vee.                     (5)

Conversely (5) implies (4). This establishes the exact compatibility
normal form; there is no extra assumed independence of compatibility
equations.

### 4.3 The normal form lifts to an annihilating rectangle

Define two-dimensional subspaces of V by

    X = { s(a) - mu(a)u : a in A },
    Z = { s(b) - lambda(b)u : b in B }.

Their images in E are A and B, respectively, so

    V = Cu direct-sum X direct-sum Z.

The lift expansion gives, for all a in A and b in B,

    f(s(a)-mu(a)u, u, s(b)-lambda(b)u)
      = A_u(v(a b)-lambda(b)a-mu(a)b)
      = 0.

Thus ([u],X,Z) is a point of C_{2,2}.

These lifted spaces do not depend on s. Replacing s by s+d u changes
v(a b) by d(b)a+d(a)b, so lambda changes by d|B and mu by d|A;
the corrections cancel in the displayed definitions of X and Z.

For this exact cross-block kernel, identical compatibility produces
precisely the two ordered independent-zero sheets

    P(X) x {[u]} x P(Z),
    P(Z) x {[u]} x P(X).

The two sheets are disjoint because X intersect Z=0. They exhaust the
fiber by the exact rank-two factor classification above and uniqueness
of the corrected lifts. This is the analogous reconstruction to the
rank-seven common-factor case.

## 5. Finiteness and the component dimension consequence

By Section 3, C_{2,2} is finite. Therefore the middle lines [u] for which
(3) holds and compatibility is identical on Sigma form a finite set:
each such middle line is the first projection of a point of C_{2,2}.
No global choice of A,B along a family is required; choosing them at an
individual point already places that point in the projection of a
single fixed finite incidence scheme.

At any remaining rank-six cross-block point, compatibility is a nonzero
section on the irreducible Segre surface. Its zero locus is a proper
closed subset, hence has dimension at most one. The ordered-factor
cover is finite, and reconstruction has no additional projective
parameters, so its projective independent-zero fiber has dimension at
most one. At the finitely many identical-compatibility points it has
dimension two, as described above.

Now assume the previously established residual-rank-drop support in
P(V) has dimension at most two. Let Y be an irreducible affine
independent-zero component whose generic middle point has rank six and
cross-block kernel (3). Its separately projectivized counterpart has
three fewer dimensions. If its middle image has positive dimension,
the generic fiber has dimension at most one, because the only
cross-block points with two-dimensional fiber lie in a finite set.
The projective component therefore has dimension at most 2+1=3.
If its middle image is a point, its projective fiber dimension is at
most two. In either case

    dim Y <= 6.

Here "generic cross-block kernel" may equivalently be read as the
condition at the geometric generic point of the reduced middle-image
closure; it holds on a nonempty constructible open after shrinking.
Only generic fibers are used for the dimension calculation. No claim
is made that the cross-block form extends over all boundary points.

Hence any remaining affine independent-zero component of dimension at
least seven with generic middle rank six must have a different generic
four-dimensional residual-kernel geometry. This conclusion narrows the
rank-six problem; it does not solve that classification or exclude
components over smaller residual ranks.

## 6. Scope checks

- Both p=1 and q=1 cases are explicitly covered for n>=4.
- The proof is global in the repeated-input injection hypothesis and
  controls all projective boundary points of the rectangular incidence.
- The residual-kernel normal form uses symbolic tensor identities only.
- No normalizer symmetry, target-dimension assumption, or rank instance
  is needed for rectangular finiteness.
- The middle-support dimension bound is used only for the final affine
  component bound.
