# The represented radical rank pencil forced by source126

2026-10-23. Conditional written deduction for the surviving E10 source of
G3.11.8ae96830fd21. No actual HM tensor, coefficient, parameter, point,
derivative, matrix or instance rank is selected or evaluated. This is not a
source exclusion, a formal proof, or a lifting theorem for the full module.

## 1. Inputs and new information

The exact inputs are public in Akilleez-QA/read-em-and-weep:

- PR856, cee45480686c39a321feaa77d4b669682cc71efe,
  research/hm/profile11-degree28-constant-separation/PROOF.md.
- PR858, d3b3134e23d0aa4c4b58fd1457f040856d2d0655,
  research/hm/profile11-degree28-residual-templates/PROOF.md.
- PR862, e103e25456897a1123f9636eb20080e8641ce66a,
  research/hm/profile11-degree28-pencil-algebra/PROOF.md.

They supply the actual constant decomposition H=C+Hbar with
C=Hbar=A+V+P+D, dimensions 3,3,4,5, and the entire two-dimensional
square-zero Jacobson radical J of the fixed-variable equivariant negative
pencil commutant. Its elements act on H by

    N_b(c,r)=(b(r),0),  b in ker Theta,
    Theta(b)=q b|_(X+Y),
    X=O(-8), Y=W O(-9), q:C O -> O(28).

The two target components of Theta are one-dimensional. Its P restriction
on X and V restriction on Y are nonzero. A and V have zero X restriction;
P has zero Y restriction. The D restriction can occur in either component.
PR862 determines the abstract algebra but does not record the following
rank stratification of its represented radical on the thirty-space H.
That stratification gives a necessary additional certificate for a future
actual-pencil comparison; abstract algebra isomorphism alone does not encode
its action on H.

## 2. A two-parameter normal form with all coupling zeros retained

A constant equivariant b:Hbar->C has four scalar channels b_A,b_V,b_P,b_D,
by multiplicity one. Choose nonzero identifications on the four irreducibles
and on the two target Hom lines. Because the P-to-X and V-to-Y restrictions
are nonzero, their coefficients can be normalized to one. Thus there are
scalars alpha,beta,gamma, not evaluated here, such that the two equations are

    b_P+gamma b_D=0,
    alpha b_A+b_V+beta b_D=0.

Consequently EVERY radical element has the unique expression

    b(x,y)=diag(x I_A, -(alpha x+beta y) I_V,
                -gamma y I_P, y I_D).                 (R1)

Here (x,y) are coordinates on the abstract radical, not coordinates on the
geometric parameter line P(W). They may both vary freely. In Type I of
PR858/862, gamma=0 because X spans P. In Type III, beta=0 because Y spans
A+V. Type II has neither of those forced zero conditions. No converse is
claimed: additional zeros may occur, and not every triple is asserted to
arise from a balanced degree28 system or actual HM tensors.

The change of constant complement used in PR856 conjugates the represented
endomorphisms, so their ranks, common kernel and total image dimensions are
invariants of the original inclusion. The chosen coordinates only express
these invariants. No basis change in the negative variables is made.

## 3. Complete projective rank formula

Since the four output representations are independent and each nonzero
scalar channel is an isomorphism of its irreducible, the rank on H is

    rk N_(x,y) = 3 [x!=0] + 3 [alpha x+beta y!=0]
                 +4 [gamma y!=0] +5 [y!=0].          (R2)

This proves the formula for every radical element, including all degeneracies.
It does not infer rank from the abstract algebra alone. For [x:y] in P(J),
there are at most THREE exceptional points: x=0, y=0, and
alpha x+beta y=0 if this last equation supplies a distinct point.
In particular:

- At [1:0], rank = 3+3[alpha!=0].
- At [0:1], rank = 5+3[beta!=0]+4[gamma!=0].
- If x y !=0 and alpha x+beta y=0, rank =8+4[gamma!=0].
- Away from these points, the generic rank is

      r_gen=8+3[(alpha,beta)!=(0,0)]+4[gamma!=0].    (R3)

The generic rank therefore belongs to {8,11,12,15}. For Type I it belongs
to {8,11}; for Type III the possible ranks are still read from (R2) with
beta=0, so there is no third distinct exceptional point. These are necessary
overlists, not assertions that all listed strata are realized.

Over C the complement of finitely many points in P(J) is nonempty. Thus J
contains an element of rank at least EIGHT, while the line y=0 contains a
nonzero element of rank at most SIX. It is impossible for the represented
radical to have constant rank on P(J), or for all its elements to have rank
at most seven. A third distinct rank-drop point, if present, drops rank by
exactly three and is impossible for Type III. The point y=0 always drops
rank by at least five, hence the rank pencil is intrinsically nonconstant.

## 4. Common kernel, total image, and Jordan types

Let Im(J) mean the sum of images of all its elements, not the image of one
chosen element. The A and D channels in (R1) are always present in Im(J).
The V channel is present precisely when (alpha,beta)!=(0,0), and the P
channel precisely when gamma!=0. Therefore

    dim Im(J)=r_gen,
    dim intersection_(N in J) ker N=30-r_gen.       (R4)

For the second identity, all of C is killed and each supported irreducible
of Hbar has no nonzero vector killed by every scalar channel. Hence generic
N has image Im(J) and kernel equal to the common kernel. This stronger
simultaneous saturation property follows from the multiplicity-one block
action, not from square-zero algebra relations by themselves.

Every N satisfies N^2=0. Its Jordan form on H is therefore

    rank(N) blocks of size two,
    30-2 rank(N) blocks of size one.                 (R5)

Thus the possible generic Jordan partitions are respectively
2^8 1^14, 2^11 1^8, 2^12 1^6, and 2^15. This is another expression of
(R3), not an assertion that a generic actual HM commutant has been found.

## 5. Fixed-pencil use and precise limitation

PR862's full-faithfulness identifies H naturally as

    ker(B_u,B_v) / im(A_v,-A_u),

for independent formal variable symbols u,v with the fixed sign convention.
Thus a future authenticated fixed-pencil commutant certificate can compute
its induced J-action on this quotient and test (R2)-(R5). These are ranks on
H, not ranks on any one of M2,M3,M4. No equality of those ranks is asserted.
Failure of these necessary represented-radical conditions would rule out
source126, provided the actual pencil, full commutant, radical and induced
quotient action had separately been authenticated. None is evaluated here.

PR869 (e7ac74f7e92c3c59d4a3c13fa0388fcff8722f47,
research/hm/profile11-degree28-open-family/PROOF.md) proves nonempty abstract families.
The rank fingerprint does not contradict them. It refines the required
represented algebra, rather than treating its nontrivial radical as an
endomorphism of the full HM module. Full-module extension is still a
separate question. All four historical pairs of source126 remain retained.

## Verification

The supplied script verifies the symbolic two-equation kernel and rank
strata using exact integral polynomials and formal block sizes. All eight
zero/nonzero coupling support patterns are checked without assigning any
value to a nonzero coupling. A separate synthetic sparse square-zero
two-plane checks that the abstract radical identities do not imply this
represented fingerprint or simultaneous-kernel saturation. It performs no
actual HM evaluation, scan, or consumed experiment.
