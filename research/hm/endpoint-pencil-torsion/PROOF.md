# A length-two primary pencil and bounded order-six specialization

## Statement, inputs, and boundary

Work over C. Fix Y=P^4, its normalized Horrocks–Mumford bundle F,
B=End_0(F), and M=H^1_*(F). Fix the original binary-quartic invariants
u_0=t_2 and v_0=t_3. Write

    Q_0 = H^1(B(6)) /
          [u_0 H^1(B(4)) + v_0 H^1(B(3))].

PR441 proves the existence of a quadratic q_1 with
q_1 M_1=M_3; here dim M_3=2. Choose such a q_1 existentially,
without constructing or evaluating its multiplication map. Put

    A=C[t],                 u(t)=u_0+t q_1,
    R=coker[u(t): M_1 tensor A -> M_3 tensor A],
    Q_A=coker[(u(t),v_0):
          (H^1(B(4)) + H^1(B(3))) tensor A
             -> H^1(B(6)) tensor A].

The symbol + in a source denotes direct sum. All cohomology groups
in these definitions are on the fixed Y, and the maps are extended
A-linearly. In particular these are explicit module cokernels, not
definitions by relative higher direct images.

The following hold.

1. There is a monic quadratic f(t) and a surjection from a module
   of C-dimension two onto R. Consequently

       length_A(R)=dim_C(R) <= 2,     f(t) R=0.

2. The natural section-resolution comparison gives

       R^(direct sum 15) ->> Q_A.

   Thus Q_A has total A-length at most 30 and is killed by the
   same quadratic f(t). The number of distinct parameters a in C
   with Q(u_0+a q_1,v_0) nonzero is at most two. No exceptional
   parameter is located or asserted to exist.

3. Cokernel base change gives canonical identifications

       Q_A/(t-a)Q_A = Q(u_0+a q_1,v_0),
       Q_A/t Q_A = Q_0.

   If e_a is the multiplicity of a as a root of f, then

       length_(A_(t-a))((Q_A)_(t-a)) <= 15 e_a,
       (t-a)^(e_a) (Q_A)_(t-a) = 0.

   A nonroot means zero localization. In particular a nonzero
   original Q_0 can occur only at a root of f; its deformation
   module at zero is killed by t^2, or by t if that root is simple.
   This is an upper bound on torsion exponent, not a claim that
   exponent two is attained.

An optional formal realization in Section 5 replaces the fixed
cubic v_0 by a transformed cubic with the same constant term.
It gives an actual translated-root family through the original
geometry, with generic order-six whole-coefficient vanishing,
and the same local length and exponent bounds for its explicitly
defined quotient module. No identification of that torsion module
with a relative R^2, or with its ordinary dual, is asserted.

This is a quantitative specialization refinement of PR440–441:
the original fixed quotient is the exact special fiber of a
finite-length module whose total length, support size, and local
nilpotence order are uniformly bounded. It does not determine Q_0.
No selected HM/source-instance evaluation, multiplication-matrix
construction, random sample, checker, or large computation is used.

## 1. The two-column pencil lemma

Let V and W be finite-dimensional complex vector spaces with
dim W=2, let T_0,T_1:V->W be linear maps, and suppose T_1 is
surjective. For A=C[t] define

    T(t)=T_0+tT_1:V tensor A -> W tensor A.

Choose a two-dimensional subspace L of V on which T_1 is an
isomorphism. This exists by lifting a basis of W through T_1;
no evaluation is needed. Identify L with W using that isomorphism.
Then the restriction of T(t) to L tensor A is

    P(t)=t I+C,

where C is the constant endomorphism T_0|_L under the identification.
Let

    E=coker P(t),             f(t)=det(t I+C).

The determinant f is monic of degree two. The adjugate identity

    P(t) adj(P(t)) = f(t) I

shows fE=0. Inclusion of the restricted domain in the full domain
gives a surjection

    E ->> coker T(t).                                  (1)

We verify the sharper length statement rather than deducing an
incorrect bound of four from two generators and a quadratic
annihilator. Every polynomial vector in W tensor A is congruent
modulo im P to a constant vector: successively replace t w by
-Cw. If a nonzero polynomial vector p(t) has degree d, then
(t I+C)p(t) has degree d+1, because its leading coefficient is
the nonzero leading coefficient of p. Thus a nonzero constant
cannot lie in im P. The map W->E induced by constants is therefore
a C-linear isomorphism. Under it, multiplication by t on E is -C.

It follows that

    dim_C E=length_A E=2,      length_A coker T(t)<=2.   (2)

The equality of C-dimension and A-length holds because all simple
finite-length C[t]-modules are C[t]/(t-a), of C-dimension one.
This proof uses neither Smith normal form nor any evaluated entry
of T_0 or T_1.

For the local refinement, decompose the two-dimensional endomorphism
-C into generalized eigenspaces. Since f(t) is its characteristic
polynomial, the generalized a-eigenspace has dimension e_a, the
multiplicity of a in f, and is killed by (t-a)^(e_a). The localization
E_(t-a) is precisely this primary summand. Therefore every quotient
R' of E satisfies

    length R'_(t-a)<=e_a,      (t-a)^(e_a)R'_(t-a)=0.  (3)

This is the elementary primary-decomposition statement for a
two-dimensional endomorphism. It also follows by factoring f
and applying the coprime-factor decomposition. A simple root
contributes a one-dimensional eigenspace; at a double root the
whole space has dimension two and its shifted operator squares
to zero.

## 2. Apply the lemma to the primary cohomology module

The exact public PR167 primary resolution, used in PR441, supplies
the degree-zero generation of M and the Hilbert function

    Hilb(M,z)=5+10z+10z^2+2z^3.

PR441's structural multiplication theorem then supplies q_1 with
q_1 M_1=M_3. We use that theorem as a pinned input; the present
proof does not select a numerical q_1 or calculate any HM rank.

Apply Section 1 with

    V=M_1,  W=M_3,  T_0=mu_(u_0),  T_1=mu_(q_1).

It gives E->>R, a monic quadratic f, and all the assertions
length(R)<=2, fR=0, and the local bounds (3). The polynomial f
depends on the good direction and the chosen two-dimensional
subspace; neither uniqueness nor an intrinsic minimal annihilator
is asserted.

The same construction shows that u(a):M_1->M_3 is surjective
whenever f(a) is nonzero. Indeed the restricted map P(a) is
then already an isomorphism. Conversely, a root of f need not
be bad for the full primary map: the unselected domain may
restore surjectivity. Thus f gives a containing exceptional
divisor, not necessarily the exact failure locus.

## 3. Naturality transfers the bound to the endpoint quotient

PR440 constructs natural surjections

    p_4:15 M_1 + 4 M_2 -> H^1(B(4)),
    p_6:15 M_3         -> H^1(B(6)),

arising from a single graded section resolution. They commute
with multiplication by every homogeneous polynomial. Moreover
M_4=0. After tensoring with A, multiplication by u(t) in the
upper row is therefore u(t) on each of the fifteen M_1 copies
and zero from the four M_2 copies. The resulting square commutes
coefficientwise in t.

Pass first to cokernels for multiplication by u(t) alone.
The upper cokernel is exactly R^(direct sum 15), and the
surjective map p_6 induces

    R^(direct sum 15) ->>
    coker[u(t):H^1(B(4)) tensor A -> H^1(B(6)) tensor A].

Quotienting further by v_0 H^1(B(3)) tensor A gives

    R^(direct sum 15) ->> Q_A.                        (4)

Every step is an A-linear quotient. In particular (4) retains
all additional section-resolution relations implicitly; it
does not identify Q_A with fifteen copies of R or delete the
incoming resolution map from PR440's exact presentation.

Combining (1) and (4), Q_A is a quotient of E^(direct sum 15).
Therefore

    length_A Q_A <=30,             f Q_A=0.           (5)

Localization is exact. Section 1 gives

    length (Q_A)_(t-a) <=15 e_a,
    (t-a)^(e_a)(Q_A)_(t-a)=0.                         (6)

The argument in this section also works with any polynomial
cubic v(t) in S_3 tensor A, not only with the constant v_0.
If v(0)=v_0, all conclusions about the original special fiber
remain unchanged. No regular-sequence premise on (u(t),v(t))
is needed for the module argument. Its geometry is addressed
separately below.

## 4. Exact fibers and the limit of the specialization argument

Tensor the defining cokernel sequence for Q_A with A/(t-a).
Right exactness, without any flatness hypothesis on Q_A, gives

    Q_A tensor_A A/(t-a)
      = coker[(u_0+a q_1,v_0):
             H^1(B(4))+H^1(B(3)) -> H^1(B(6))]
      = Q(u_0+a q_1,v_0).                             (7)

At a=0 this is precisely the original Q_0, with its fixed
multiplication maps, not merely a vector space of the same
dimension. It follows that Q_0 is a special fiber of the
explicit module constructed here.

Because Q_A is finite over A, Nakayama's lemma identifies
nonvanishing of its fiber at a with nonvanishing of its
localization at (t-a). Thus (5) implies at most two distinct
nonzero endpoint fibers. More quantitatively,

    sum_(a in C) dim_C Q(u_0+a q_1,v_0)
       <= sum_(a in C) length (Q_A)_(t-a)
       = length_A Q_A <=30.                           (8)

Only finitely many terms can be nonzero. If f has two distinct
roots, each corresponding localization is killed by t-a and
equals its own fiber as a C-vector space; in that case the
first inequality in (8) is an equality. At a simple root
the endpoint fiber has dimension at most 15.

If Q_0 is nonzero, f(0)=0. Put e_0=ord_(t=0) f, necessarily
1 or 2. Formula (6) says

    t^(e_0)(Q_A)_(t)=0,       length (Q_A)_(t)<=15e_0.  (9)

In particular the local parameter has nilpotence order at most
two. The same statements hold after completion at t=0, since
this finite-length localization is already killed by a power
of t.

These facts do not prove Q_0=0. For example, even the elementary
module A/(t) has zero generic fiber and nonzero fiber at zero.
Generic vanishing cannot be specialized to vanishing at a
specified parameter without an additional premise such as
flatness at that parameter. Here a finite flat module over a
neighborhood of zero with zero generic fiber would indeed be
zero there, but no such flatness is established.

Nor does f(0)=0 prove Q_0 is nonzero. The selected two-column
map may fail while other primary columns, the cubic image, or
the retained section-resolution relations kill the quotient.
The specific fixed endpoint remains unresolved in both directions.

There is a useful conditional dichotomy, without evaluating any
primary fiber. Put d_a=dim_C(R/(t-a)R). If d_a=2, its local
length is at least two, exhausting the total bound on R. Thus
R is supported only at a and is isomorphic to
(A/(t-a))^(direct sum 2); in particular (t-a)R=0. If d_a=1,
Nakayama's lemma makes R_(t-a) cyclic, hence isomorphic to
A_(t-a)/(t-a)^m for some 1<=m<=2. In this latter case (4)
shows that the endpoint fiber has dimension at most 15, even
when a is a double root of the chosen f. These alternatives
are conditional descriptions, not calculations of d_a.

## 5. Optional formal translated-root realization through the origin

The polynomial family with fixed v_0 is an algebraic quotient
family. We do not assert that every pair (u(t),v_0) is obtained
by transporting the original root cover. A formal change of
the cubic makes such a transport explicit.

PR441 proves that the original quadratic u_0 is nondegenerate.
Represent u_0 and the chosen q_1 by symmetric coefficient matrices
U_0 and U_1 on the five-dimensional coefficient space, so

    u_0(x)=x^T U_0 x,       q_1(x)=x^T U_1 x,

with U_0 invertible. These are notation for quadratic forms,
not evaluated primary HM multiplication matrices. In
Ahat=C[[t]] put

    D=U_0^(-1)U_1,
    H(t)=(I+tD)^(1/2)
        =sum_(n>=0) binom(1/2,n)t^n D^n.

This t-adic series is well-defined, has constant term I, and
satisfies H(t)^2=I+tD. Symmetry of U_0,U_1 gives
D^T U_0=U_0 D, hence H(t)^T U_0=U_0 H(t). Consequently

    H(t)^T U_0 H(t)=U_0+tU_1.

Let g(t)=H(t)^(-1), viewed as a projective automorphism over Ahat.
Using this specified GL_5 lift, we have the literal identity

    (g(t)^(-1))^*u_0=u_0+tq_1.

Define the transformed cubic

    vhat(t)=(g(t)^(-1))^*v_0=v_0(H(t)x).

Then vhat(0)=v_0 and g(0)=identity. Define an explicit quotient
module, again from the fixed complex cohomology groups:

    Qhat=coker[(u_0+tq_1,vhat(t)):
             (H^1(B(4))+H^1(B(3))) tensor Ahat
                  -> H^1(B(6)) tensor Ahat].           (10)

The same natural square and quotient argument gives

    (R tensor_A Ahat)^(direct sum 15) ->> Qhat,
    Qhat/t Qhat=Q_0.                                  (11)

If e_0=ord_0 f, with e_0=0 when f(0) is nonzero, then
f is t^(e_0) times a unit in Ahat. The primary-decomposition
calculation of Section 1 gives

    length_Ahat Qhat<=15 e_0<=30,
    t^(e_0)Qhat=0.                                    (12)

For e_0=0 these statements mean Qhat=0. The quotient Qhat
need not equal Q_A tensor_A Ahat, since the cubic was changed;
the same controlling primary module maps onto both.

In every case t^2 Qhat=0, so the canonical map
Qhat -> Qhat/t^2 Qhat is an isomorphism. Right-exact cokernel
base change therefore reconstructs the entire module (10)
from its presentation over J=C[epsilon]/(epsilon^2).
Specifically, H(t)=I+(t/2)D modulo t^2, so put

    w_1(x)=(1/2) sum_i (Dx)_i (partial v_0/partial x_i).

Then, with t acting as epsilon on the right, there is a canonical
identification

    Qhat =
      coker[(u_0+epsilon q_1, v_0+epsilon w_1):
         (H^1(B(4))+H^1(B(3))) tensor J
                    -> H^1(B(6)) tensor J].             (12a)

Here "canonical" refers to the reduction map for the specified
q_1 and formal transport. It does not make their existential
choices canonical. No higher coefficient of H(t) or vhat(t)
is needed for this quotient-module reconstruction. This is a
first jet in the auxiliary translation parameter, not a source
jet, a collision-ideal order, or a star-product deformation
order; its actual multiplication maps remain unevaluated.

There is also an actual formal translated-root family. With
the fixed ordered-root map q_0:Z=(P^1)^4->Y, set over Ahat

    q_g=g(t) o q_0,
    E_g=q_g^*B tensor (q_g^*O_Y(1))^(-2),
    I=I_D on the constant root space Z.

The special fiber has g(0)=identity, so it is exactly the
original coefficient geometry. On the generic fiber over
K=C((t)), f is invertible; hence u(t):M_1 tensor K -> M_3 tensor K
is surjective. The fixed cohomology groups of F and B commute
with this field extension, so PR440's naturality gives the
surjectivity of u(t) on H^1(B(4)) tensor K -> H^1(B(6)) tensor K.
The transformed pair is a transported regular sequence because
g(t) is an automorphism.

PR437/439's transported full-character filtration and endpoint
calculation, as applied in PR441 Section 5, therefore give

    H^2(Z_K,I^6(E_g)_K)_chi=0,
    H^2(Z_C,I^6(E_g)_0)_chi^vee=Q_0 + Q_0.             (13)

These are statements on the generic and special fibers
separately. In particular (12) is proved for the explicitly
defined positive-cohomology cokernel Qhat, not for a claimed
relative R^2. Fiberwise Serre duality does not justify an
ordinary module-duality identification across this torsion
specialization, and no cohomology-and-base-change assertion
of that kind is used or made.

The bundle F on the target is held fixed; its pullback by the
varying root map changes. No equivariance or invariance of
F under g(t) is assumed. The formal transport retains all
collision strata, including quadruple collisions.

## 6. Contribution, exact dependencies, and exclusions

PR441 gives an open good-quadratic locus but does not bound
the multiplicity of an exceptional specialization. The new
step is a pencil through the exact original endpoint, governed
by a length-two primary module and a common quadratic
annihilator. It yields a total endpoint length bound of 30,
at most two exceptional parameters, a local exponent bound of
two, and exact special-fiber identification. Section 5 shows
how to realize the quadratic pencil in an actual formal
translated-root family while keeping the special geometry,
and reconstructs its explicit quotient module from the first
jet in the auxiliary translation parameter.

The exact imported inputs are:

- PR441, commit
  `6d81d9500f42ae31bef6d3150cf3ba513c28502b`, proof blob
  `5d040d083e0d413c4de7249ed632cfb58fa55572`:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/6d81d9500f42ae31bef6d3150cf3ba513c28502b/research/hm/generic-quadratic-surjectivity/PROOF.md
  Sections 1–3 provide the good quadratic and primary-module
  hypotheses; Sections 4–5 give nondegeneracy and the precise
  translated-root convention used in the optional construction.
- PR440, commit
  `829e03411d04511f6cf04860bf18db4a70b12448`, proof blob
  `998dd6d488636565c6b32e8879383cce167f010f`:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/829e03411d04511f6cf04860bf18db4a70b12448/research/hm/degree-six-structural-reduction/PROOF.md
  Its Sections 3–4 supply the natural surjections and their
  polynomial-multiplication compatibility. Its distinct
  surface-transgression model is not invoked here.
- The endpoint used in the optional fiberwise interpretation
  is PR439, commit
  `bf6ce91fd73fbc96cb8ede65448dfedbc0328c7b`, and the filtration
  is PR437, commit
  `50e82ed233cd7729c38608194f990376eb832418`, through their
  explicitly transported application in PR441 Section 5:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/bf6ce91fd73fbc96cb8ede65448dfedbc0328c7b/research/hm/paired-collision-endpoint/PROOF.md
  https://github.com/Akilleez-QA/read-em-and-weep/blob/50e82ed233cd7729c38608194f990376eb832418/research/hm/paired-collision-filtration/PROOF.md

The bounded prior-work comparison is with current PR1 and the
exact PR440/441 proofs above. No exhaustive literature or
repository novelty search is claimed.

The value of Q_0, the ranks of its fixed multiplication maps,
the actual high-order source representative, the six pure
conditions, module lifting, and algebraicity remain unresolved.
A nonzero endpoint quotient would not itself prove nonzero
image in unrestricted cohomology or nonzero actual source class.
The total length estimate is a deformation-module estimate,
not a claim dim Q_0<=2, nor an automatic improvement on PR440's
fixed-fiber bound of 30. All derivations are structural; none
evaluates a selected actual HM/source instance.
