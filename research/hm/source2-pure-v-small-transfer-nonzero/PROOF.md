# Actual Q-image transversality in every branch and nonzero small transfer

## Result and scope

Under the conditional actual source2 nonzero pure-V compatible-radical
hypotheses, let U_Q=Q(NC2), and let D_C be the unique actual D summand
of NC4=I4 plus D_C. In EVERY remaining branch,

    D_C is not contained in U_Q,
    U_Q intersect NC4 = I4 if dim F4=9,
    U_Q intersect NC4 = 0  if dim F4=16.                 (0)

Thus full NC4 transversality holds in ALL endpoint-sixteen branches,
including the nonzero N0-projection branch not covered by PR1065's
previous residual-large result. In endpoint nine, PR1074 then forces
the canonical coefficient gamma in R=gamma R1 to be NONZERO.

This decides the zero/nonzero alternative in endpoint nine without
selecting a numerical coefficient. It does not prove that any branch
or source exists, and it excludes neither endpoint nor a source pair.
The new argument combines polynomial prolongation with actual
multiplication by Q into degree five. No actual instance is evaluated.

## 1. Exact premises

INPUTS.json authenticates the immutable proofs below.

- PR794 and PR795: the embedded polynomial first spaces NC2=Sym16 W
  and NC3=Sym17 W, with ordinary negative multiplication, and

      I2=f12 Sym4 W, I3=f12 Sym5 W,
      NC2=V+P+2D, NC3=W'+S+2T.

  These hold for every compatible pure-V branch, not just endpoint nine.
  Indeed PR794 Section1 identifies the pure-V quotient map as f12 q_V
  and proves q_V onto H0(O(4)) and H0(O(5)) after the two twists.
  The inclusions into the residual reconstruction are genuine and
  injective. PR795 retains those actual fixed-variable maps. Thus the
  two images are literally the displayed polynomial multiples, with
  f12 a nonzero invariant form, D=Sym4 W and T=Sym5 W.
- PR1068: the FULL actual joint-negative kernel in degree four is

      NC4=ker[M4 -> W tensor M5]=P+D.                   (1)

  This is equality of embedded spaces, not just W NC4=0.
- PR1065: ker(Q|NC2)=I2, and Q(NC2) has character V+P+D.
- PR1069: in endpoint nine the full transfer factors with its single
  unselected scalar gamma and diagonal R=gamma R1.
- PR1074, the transfer-incidence theorem: in endpoint nine,

      gamma=0 iff NC4 is contained in Q(NC2),
      gamma nonzero iff Q(NC2) intersect NC4=I4.         (2)

  Its immutable commit is 7b7d6aad86dbd99ab476a1aa1fb7f43ec62afec3,
  research/hm/source2-pure-v-transfer-incidence/PROOF.md.

All actual-source hypotheses of these inputs remain in force. Q is the
actual invariant quadratic acting on the cohomology module M. Write
Q_2:M2->M4 and Q_3:M3->M5 when the degree matters. Since these are
multiplications by the SAME polynomial, for each negative linear form l,

    Q_3(l v)=l Q_2(v).                                  (3)

This uses the ordinary module action of the actual quadratic, not an
extension of h or of the fixed-pencil radical. We never assume Q preserves
NC, NR, or a chosen residual splitting.

## 2. An injective polynomial prolongation lemma

For any complex linear map j:Sym4 W->Sym16 W, define

    P(j)=mu (Id_W tensor j) Delta : Sym5 W->Sym17 W,

where mu is ordinary multiplication and
Delta(f)=(x tensor f_x+y tensor f_y)/5 is the canonical polarization.
Thus multiplication after Delta is the identity on Sym5 W. The map
j -> P(j) is injective, even without equivariance.

Indeed put f_i=j(x^(4-i)y^i), for 0<=i<=4. The six outputs are

    P(j)(x^(5-i)y^i)
       = ((5-i)x f_i+i y f_(i-1))/5,  0<=i<=5,          (4)

with nonexistent terms omitted. If these outputs vanish, the i=0
identity gives x f_0=0, hence f_0=0 in the polynomial domain. Successively
using i=1,2,3,4 gives every f_i=0. This proves injectivity.

If j is G-equivariant, P(j) is G-equivariant. Suppose j is nonzero and
the image of P(j) is contained in I3=f12 Sym5 W. Since T=Sym5 W is
irreducible, Schur's lemma gives

    P(j)=c (multiplication by f12) on Sym5 W.

But P(multiplication by c f12 on Sym4 W) is exactly that map, by Euler's
identity. Injectivity therefore gives j=c f12 on Sym4 W. In particular,
its image is I2. This conclusion requires only finite-group equivariance;
it does not assume j is SL2-equivariant.

Consequently, for EVERY equivariant D subspace J in NC2 complementary
to I2 in the D-isotypical part, the T image P(j)(Sym5 W) is nonzero and
DIFFERENT from I3. The two irreducible T subspaces have zero intersection
and span the full two-copy T-isotypical component of NC3. Choices of
source identifications merely rescale j and do not affect this assertion.

## 3. No D incidence in any branch

Suppose D_C is contained in U_Q=Q(NC2). No endpoint-nine hypothesis
is imposed in this section. The D summand of U_Q has multiplicity
one, hence it is exactly D_C. Complete reducibility and ker(Q|NC2)=I2
provide an equivariant D complement J to I2 in the D-isotypical part of
NC2, with

    Q_2:J -> D_C an isomorphism.                       (5)

No arbitrary equal-character D spaces are identified here: (5) follows
from actual image containment and the actual restriction kernel.

Equation (1) kills W D_C. Therefore (3) and (5) give Q_3(W J)=0.
Also Q_2(I2)=0 gives Q_3(W I2)=0, and W I2=I3. Section2 then shows
that Q_3 kills the ENTIRE T-isotypical component of NC3.

Let V_C be the unique V summand of NC2. The finite-group tensor identity
W tensor V=T puts W V_C in that T-isotypical component; this is an
actual image statement from equivariance, regardless of its dimension.
Consequently Q_3(W V_C)=0. Applying (3) again gives

    W Q_2(V_C)=0.

By the FULL joint-kernel equality (1), Q_2(V_C) is contained in NC4.
But Q_2 is injective on V_C since its restriction kernel is I2=D.
Its image is therefore a nonzero V representation, while NC4=P+D has
no V constituent. This is impossible, proving D_C is not contained in U_Q in every branch.

The equivariant intersection U_Q intersect NC4 therefore has no D
constituent: an intersection with the irreducible D_C is either zero or
all of D_C. Since NC4=I4 plus D_C is multiplicity-free, every invariant
subspace is a sum of these inequivalent constituents, with no hidden
P/D graph. Consequently U_Q intersect NC4=U_Q intersect I4. PR1065
identifies the latter as I4 in endpoint nine and zero in endpoint sixteen,
proving (0) including the formerly untreated nonzero-N0 branch.

Finally, in endpoint nine only, (2) implies gamma is nonzero. The
incidence theorem is used for this scalar corollary, not for the
all-branch no-D-incidence argument.

## 4. Verification and boundaries

The checker verifies the prolongation coefficient matrix has rank85
on all 85 coefficients of a completely arbitrary linear map
Sym4 W->Sym16 W. This is a universal linear-algebra certificate, not an
actual HM matrix. It also verifies the recurrence symbolically, Euler
normalization with a fully formal degree-twelve form, and exact binary
icosahedral character identities including W tensor V=T and the two
T copies in Sym17 W. Normal and optimized executions agree.

The proof uses neither a selected invariant f12 polynomial nor selected
actual coefficients, parameters, directions, points, jets or source ranks.
It does not construct Q_3 numerically. Its actual commutation comes from
the polynomial module action, and the ambient kernel equality is precisely
the pinned geometric theorem, not an extrapolation from a truncated pencil.
