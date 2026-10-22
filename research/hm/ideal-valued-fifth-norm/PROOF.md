# The ideal-valued norm shadow of the actual fifth-neighborhood boundary

## Statement and pinned inputs

Work over C with the actual locally free rank-two bundle F on X=P4,
B=End_0(F), the integral quadric Q=(q=0), and rQ=(q^r=0).
Retain the fixed marking and physical-center-even sector. Fix nonzero
sources a in A and h in D5. Each has twist two. Let N have twist two,
and let pi: X_stack=P_stack(1,1,2,2) -> Q be the weighted-stack coarse
map. Let I_Z denote the ideal of the regular Serre zero scheme ON THE
SMOOTH STACK. Define the coarse trace-image sheaf

      Qsq=pi_*(I_Z^2(6)) subset O_Q(6).

The square here is the ordinary ideal square on the stack. Qsq must NOT
be replaced by the square of the coarse Ext-annihilator ideal I_e.
All cohomology and images below may be taken in the even sector.

The inputs are:

- [The actual fifth-boundary ladder, at 8d8b5be4ce62c3055bb53be9e16d29cc63072f04](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-BOCKSTEIN-AS-A-FIFTH-NEIGHBORHOOD-ADJOINT-BOUNDARY.md): J4 is an actual global section of B_(4Q)(10), J4|Q=a^3 h N, and for K=aJ4,

      0 -> B_Q(4) --q^4--> B_(5Q)(12)
          -> B_(4Q)(12) -> 0,                         (1)
      beta4_a(h)=[delta_5 K] modulo im(beta2_a).

  Its boundary convention is the positive coboundary divided by q^4.
- [The weighted-stack square-shadow theorem, at 8d8b5be4ce62c3055bb53be9e16d29cc63072f04](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/WEIGHTED-STACK-SQUARE-SHADOW-AND-PRIMARY-SCALAR.md), sections 1-2: the exact coarse trace-image sheaf is Qsq as defined above. Coarse pushforward is exact in characteristic zero, but does not commute with taking the square of the coarse annihilator ideal.
- [PR687, 2874402c884a6b426cfd521a674c962a738f84a6, section 3](https://github.com/Akilleez-QA/read-em-and-weep/blob/2874402c884a6b426cfd521a674c962a738f84a6/research/hm/fourth-square-invariance/PROOF.md): the exact trace image is

      tau=tr(N-): B_Q(4) -> Qsq,                 (2)

  and this map is surjective as a sheaf map, with its square-image notation
  interpreted by the pinned weighted-stack theorem above. That distinction
  is essential at the singular vertex.
- [PR685, 449a8df60662bd7a1d93e318ea4f7e6dab28e5ad](https://github.com/Akilleez-QA/read-em-and-weep/blob/449a8df60662bd7a1d93e318ea4f7e6dab28e5ad/research/hm/third-lift-uniqueness/PROOF.md): classified completion changes alter the raw fifth boundary by a second-symbol value. Thus its class modulo im(beta2_a), rather than its raw representative, is intrinsic for the stated source data.

Put f=a^4 h, a nonzero section of O_Q(10), so K|Q=fN.
We construct a norm coset whose connecting class is exactly tau_*(delta_5 K).
Its class modulo tau_*(im beta2_a) is a necessary shadow of beta4.
No nonvanishing of this shadow or of beta4 is asserted.

## 1. Scalar lifts exist, without adjoint lifts

For a trace-free rank-two endomorphism over any C-algebra,

      L^2=n(L) Id,       n(L)=tr(L^2)/2,
      n(L+D)-n(L)=tr(LD)+n(D).                       (3)

Consequently n(K) is a global section of O_(4Q)(24). The scalar restriction
sequence is

      0 -> O_Q(16) --q^4--> O_(5Q)(24)
          -> O_(4Q)(24) -> 0.                        (4)

Here H^1(O_Q(16))=0. Indeed the hypersurface sequence on P4 is
0 -> O_P4(14) -> O_P4(16) -> O_Q(16) -> 0,
and the relevant intermediate cohomology groups of line bundles on P4
vanish. This argument does not require smoothness of Q.
Thus there is a GLOBAL scalar lift P of n(K) to O_(5Q)(24).
This does not supply a global adjoint lift of K in (1).

## 2. The norm coset and its exact connecting class

Choose an affine cover and local trace-free lifts K_i of K to B_(5Q)(12).
They exist by the sheaf surjectivity in (1). On overlaps write

      K_j-K_i=q^4 c_ij,       c_ij in B_Q(4).

The cocycle c_ij represents delta_5 K with the convention in (1).
Since q^8=0 on 5Q, (3) gives

      n(K_j)-n(K_i)=q^4 tr((K|Q)c_ij)
                        =q^4 f tau(c_ij).           (5)

The degree check is 10+6=16 for the coefficient of q^4, and 16+8=24
for the norm. Define local sections w_i of O_Q(16) uniquely by

      n(K_i)-P=q^4 w_i.

By (5), w_j-w_i=f tau(c_ij). Let

      J_f=f Qsq subset O_Q(16),
      C_f=O_Q(16)/J_f.

The images of w_i therefore glue to a global section chi_P of C_f.
Changing K_i to K_i+q^4 D_i changes w_i by f tau(D_i), so chi_P is
independent of the local adjoint lifts. Changing P to another global
scalar lift replaces P by P+q^4 r for a global r in H^0(O_Q(16)); hence
chi_P changes by the negative of the image of r. We obtain a canonical
norm coset

      nu(K) in H^0(C_f)/im H^0(O_Q(16)).              (6)

Integrality of Q and f!=0 make multiplication by f an isomorphism
Qsq -> J_f onto its image. Applying the connecting map to
0 -> J_f -> O_Q(16) -> C_f -> 0 and using H^1(O_Q(16))=0 yields a
canonical isomorphism

      H^0(C_f)/im H^0(O_Q(16))  ~=  H^1(J_f)
                                  ~=  H^1(Qsq). (7)

Under (7), formula (5) proves the exact identity

      nu(K)  <->  tau_*(delta_5 K).                  (8)

All cancellations by f above are sheaf identifications onto the image.
There is no inversion of f on its zero divisor and no assumption that f
is a unit. The construction therefore includes source divisors and the
singular locus of Q.

## 3. The second-symbol quotient is retained

Write V_a=im(beta2_a) subset H^1(B_Q(4)) for the actual fixed-direction
second-symbol image. Functoriality gives a well-defined linear map

      bar_tau_a: H^1(B_Q(4))/V_a
                    -> H^1(Qsq)/tau_*(V_a).     (9)

The image of beta4_a(h) under (9) is precisely the class of the norm
coset (6), interpreted by (7), modulo tau_*(V_a). PR685 ensures that
classified completion changes affect this class only by that image.
This assertion does NOT require, and does NOT assert, tau_*(V_a)=0.
It applies on rank-drop directions as well: no inverse or constant rank
for beta2_a is used.

A nonzero class in the right side of (9) would prove beta4_a(h)!=0.
The trace-image theorem alone does not justify inferring beta4_a(h)=0
from a zero shadow. More explicitly, put
C_N=ker(tau). Exactness of

      0 -> C_N -> B_Q(4) -> Qsq -> 0

gives ker(tau_*:H^1(B_Q(4))->H^1(Qsq)) equal to the image of
H^1(C_N). If the shadow vanishes, one can subtract a member of V_a
from delta_5 K so that the remainder lies in this image. Therefore
faithfulness of the shadow modulo V_a requires controlling that image;
it is not provided by the trace-image theorem alone. The additional
pinned weighted-stack kernel cohomology, beyond this general logic, is
addressed in a separate follow-up; no faithfulness theorem is asserted here.

## 4. What ordinary scalar cohomology forgets

If one replaces J_f by the ambient scalar sheaf O_Q(16), the cocycle
in (5) has zero cohomology class, because H^1(O_Q(16))=0. Thus the
ordinary scalar trace of the fifth-boundary cocycle loses exactly the
possibility of a nontrivial class supported by the square-ideal quotient
C_f. Formula (7) shows where that information can still reside; it does
not say the actual class there is nonzero.

Similarly, for two twist-twelve sections and their local fifth lifts,
polarized trace differences have coefficients in O_Q(16), and their
ordinary scalar H^1 classes vanish for the same reason. This statement
concerns these ordinary linear trace and polarized-trace H^1 targets,
not every conceivable scalar invariant or every ideal-valued construction.

In particular, knowledge of the q^3 coefficient of n(K), including its
nonvanishing, supplies no value for the q^4 norm coset constructed here.
Nonzero fourth-square scalar or exact nilpotency index four is not being
identified with a nonzero fifth-neighborhood adjoint boundary.

## Contribution and verification status

The construction gives an explicit, source-divisor-compatible scalar
representative of the image of the actual beta4 obstruction under the
Serre-ideal trace map, with its full second-symbol indeterminacy.
Determining this norm coset modulo tau_*(V_a) remains a mathematical
dependency. The general argument also identifies the trace-kernel
cohomology needed for a sufficient criterion; its additional pinned
weighted-stack input is addressed in a separate follow-up, not here.

This is an authored deductive reduction. Its checks are the exact
rank-two polarization identity, q-adic orders, twists, and the connecting
cocycle calculation. It is not a proof-assistant certification and makes
no selected actual coefficient, point, derivative, matrix, rank, or
source evaluation. It gives no algebraicity conclusion.
