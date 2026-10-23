# The fifth alternating criterion and all-orders stabilization in the residual-large branch

## Theorem and scope

Retain the actual source2 nonzero pure-V compatible-radical hypotheses,
and assume the residual-large endpoint-sixteen branch. Write R for the
unique quadratic lift of the original fourth. Conditional on R=0, there
is an actual equivariant isomorphism

    Xi:A tensor P -> (Hom(A,I2))_(V+P+D).                    (1)

In the fixed universal channel conventions below it has three NONZERO
Schur coordinates lambda_D, lambda_P, lambda_V. The original fifth
vanishes if and only if

    lambda_D=-lambda_V,     lambda_P=lambda_V.              (2)

Equivalently, Xi lies in the unique alternating bracket line. This is
compatible with every Schur coordinate being nonzero; mixed nonzero
transfer does not by itself force fifth nonvanishing.

More strongly, if (2) holds, a fixed linear normalization constructs
polynomial corrected lifts to ALL orders. Every higher original positive
obstruction then vanishes. Thus for the ORIGINAL 37-by41 block in this
residual-large branch the last Smith exponent is exactly one of

    4 if R is nonzero;
    5 if R=0 and the fifth class is nonzero;
    absent if R=0 and the fifth class is zero.              (3)

The first two cases have generic Laurent rank37; the last has rank36.
No finite exponent6 through24 remains in this branch. No actual value,
branch occurrence, source exclusion, opposite-pencil conclusion or
full-adjoint conclusion is asserted. In particular this is not a proof
that the surviving actual isomorphism does or does not lie on (2).

## 1. Immutable inputs and actual maps

INPUTS.json retains exact bytes and hashes for PR1069 (canonical mixed
transfer), PR1089 (actual alternating vanishing), PR1031 and its universal
model (normalizations), PR1058 (separated P multiplication), PR1104
(fifth page and cubic gauge), PR1113 (full common homotopy kernel), and
PR1107 (global corrected strings and finite stopping). Their exact public
commits and repository paths are in that manifest; no historical actual
source executable is run.

Use q=Q:N2->M4, the genuine negative quadratic multiplication T_a,
h:M4->N2, and j2=hq, j4=qh. We retain

    j4T_a=T_a j2, ker j4=im q, im h=F2=I2+P_h,
    qs=i_P, hT_a h=0, ker q=A_can+I2.                     (4)

Here s:P=I4->P_h is the canonical inverse. Let e0 be the actual
projection to the separated N0 summand, not a residual splitting. Put
J2=ker j2. PR1113 proves, in the present residual-large branch,

    Gamma:J2->H=Hom(A,I2), Gamma(v)(a)=hT_a v,
    H=A+V+P+D, Gamma onto, dim ker Gamma=21,
    J2=NR2+(N0,2)_P.                                    (5)

Under R=0, PR1089 gives B(a,b)=hT_a G T_b s=0, and PR1113 gives

    K=ker Gamma=F2 direct-sum k(A tensor P),
    k(b,p)=G T_b s(p), QK=F4 subset NR4.                  (6)

G is any fixed equivariant right inverse of q on im q. The P component
of e0k is nonzero, is independent of G, and lands in the unique separated
P8=(N0,2)_P. The V and D components of e0k vanish. These are actual
embedded statements, not identifications obtained from characters.

Let a_A:A->A_can be the canonical inclusion. PR1107 retains the exact
normalization

    q a_A=0, e0 a_A=0, Gamma a_A=mu m, mu nonzero,
    m(z)(c)=c z in Sym4 W=I2.                            (7)

Thus Gamma(A_can) is precisely the unique A summand H_A of H. Write
H'=H_(V+P+D); both summands are canonical isotypic subspaces.

## 2. The actual separated-image isomorphism

Since qK lies in NR4, e0q on J2 factors uniquely through Gamma. Let
xi:H->N0,4 be this factor. It kills H_A by (7). Choose a coherent nonzero
equivariant identification E8:P->P8. Multiplicity one gives

    e0 k(b,p)=eta E8 rho_P(b)p, eta nonzero.               (8)

This is a reference normalization, not a selected actual coefficient.
Define M8(a,p)=T_a^0 E8p, where T^0 is actual separated multiplication.
PR1058 proves M8 is injective with12-dimensional image A P8=V+P+D.

For every a,b,p put w=G T_a k(b,p). It is defined because j2k=0 and
j4T=Tj2. Moreover j2w=hT_a k(b,p)=B(a,b)p=0, so w belongs to J2.
Consequently

    xi Gamma(w)=e0qw=eta M8(a,rho_P(b)p).                 (9)

The nonzero map rho_P:A tensor P->P is onto. Hence the right sides of
(9) span all of A P8. The factor xi has domain H/H_A of dimension12;
therefore its image is exactly A P8 and

    xi|H':H' -> A P8 is an isomorphism,
    Xi=(xi|H')^(-1) M8.                                 (10)

No assertion that q preserves NR is used. Changing E8 scales Xi and
eta reciprocally, so its projective alignment criterion is intrinsic.

## 3. Universal channels and the exact fifth class

Use the pinned PR1031 apolar embedding E:P->Sym6 W and projection Pi
with Pi E=Id. Transvectants are unnormalized:

    (f,g)_r=sum_j (-1)^j binom(r,j)
                 (partial_x^(r-j) partial_y^j f)
                 (partial_x^j partial_y^(r-j) g).

Set rho_n(a)f=(a,f)_1 and rho_P(a)=Pi rho_6(a)E. The three channel
maps, written with output evaluated on the independent quadratic b, are

    J_D(a,p)(b)=(b,(a,Ep)_2)_1,
    J_P(a,p)(b)=(b,E rho_P(a)p)_2,
    J_V(a,p)(b)=(b,(1-E Pi)rho_6(a)Ep)_2.                 (11)

They factor respectively the D, P and V constituents of A tensor P.
Their exact coefficient matrices have ranks5,4,3 and their sum has
rank12. Thus they are nonzero intertwiners onto the corresponding
constituents of H'. It follows from (10) that

    Xi=lambda_D J_D+lambda_P J_P+lambda_V J_V,            (12)

with all three lambda values nonzero, but unselected.

In PR1104 notation L_a*=(a,Ep)_2/60, R1=rho_D L*,
R2=L* rho_P, and C1=rho_D R1, C2=rho_D R2, C4=R2 rho_P.
The three cubics C1,C2,C4 are independent. The sole cubic m gauge is

    C4-C1/4=-m_a (a^2,Ep)_4/720.                         (13)

In particular [C1],[C2] form a basis of the actual fifth target, and
span(C2,C4) has zero intersection with the gauge line.

The first corrections can be taken as x1=-k(a), x2=G T_a k(a),
x3=-G T_a x2. Under R=0, x2 belongs to J2. Equations (8)-(10) give

    pr_H' Gamma(x2(a,p))=eta Xi(a,rho_P(a)p).             (14)

The H_A component evaluates on a as m_a times an A-valued quadratic
family; it is exactly an allowed cubic gauge, not a claim of raw zero.
The raw fifth lift is C=j2x3=-hT_a x2. Whole-polynomial identities give

    J_D(a,rho_P(a)p)(a)=60 C2,
    J_P(a,rho_P(a)p)(a)=60 C4,
    J_V(a,rho_P(a)p)(a)=60(C2-C4).                        (15)

The last identity also follows from transvectant covariance:
(a,rho_6(a)f)_2=rho_4(a)(a,f)_2, since (a,a)_1=0.
Combining (13)-(15), the actual fifth class is

    [C]=-15 eta(lambda_P-lambda_V)[C1]
        -60 eta(lambda_D+lambda_V)[C2].                  (16)

PR1104's actual quotient-fourth/original-fifth comparison is injective
on this target. Since eta is nonzero, (16) proves (2), with the original
sign retained. These classes are sequential actual obstructions, not
freely realizable coefficients.

The exact bilinear identity

    J_P+J_V-J_D=-3((a,b)_1,Ep)_2                         (17)

identifies the line (2) as alternating in the two A variables. It has
rank12, not zero as a mixed map. Since wedge^2 A=A and A tensor P
contains D once, the alternating equivariant space here is one-dimensional.
Equations (15)-(17) exhibit literal diagonal cancellation on this
all-nonzero Schur line; no nonvanishing conclusion can be drawn merely
from mixed rank12.

## 4. A fixed normalization and all-orders polynomial continuation

Assume now the fifth vanishes, hence Xi is alternating. Let
r:H_A->A be the inverse of the embedding m in (7). Define the FIXED
linear equivariant operator on J2

    N(v)=v-a_A r(pr_H_A Gamma(v))/mu.                    (18)

It uses only the already nonzero constant mu. Directly from (7),

    qN=q, e0N=e0, j2N=0,
    Gamma N=pr_H' Gamma=(xi|H')^(-1)e0q.                 (19)

In particular the normalization removes the entire A component of
Gamma, not just its value in one direction, and leaves the q equation
unchanged.

We construct homogeneous equivariant polynomial maps x_i(a):P->N2
satisfying

    x0=s, qx0=i_P,
    qx_(i+1)=-T_a x_i,
    x_i in J2, hT_a x_i=0.                              (20)

The base case follows from (4): s is in im h, so Gamma s=0, and
j2s=hqs=hI4=0. Suppose x_i satisfies (20). Since j2x_i=0,
T_a x_i lies in im q. Define y=-G T_a x_i. Then

    qy=-T_a x_i, j2y=hqy=-hT_a x_i=0.                  (21)

Thus y is in J2 and x_(i+1)=N(y) is defined. Since J2 has only P8 in
its separated projection, write e0x_i=E8 v_i for a P-valued polynomial
v_i(a). Equations (19), (21) and actual split preservation by T give

    Gamma x_(i+1)=-(xi|H')^(-1)T_a^0 E8 v_i
                 =-Xi(a,v_i).                         (22)

Evaluating (22) on the SAME quadratic a is zero by alternation, for
EVERY P-valued polynomial v_i, not just rho_P(a)p. This proves the
induction. All operators G,N and isotypic projections are fixed linear
maps; hence the x_i are global homogeneous polynomial families of
degree i. No direction-dependent inverse, gate denominator, or removal
of a kappa term is needed. This special normalization bypasses the
higher kappa gauge rather than assuming it absent.

These actual strings give corrections at every quotient order and,
by the original comparison retained in PR1107, at every higher
original order. Alternatively truncating at x23 already supplies that
proof's finite certificate: all original orders4 through24 vanish, so
each37-minor has order at least31 but degree at most30. Thus all maximal
minors vanish identically and generic rank is36. The three known
second-order pivots retain the lower bound36. This proves the absent
case in (3). Because the maximal minors are polynomials in the pencil
variable and the three direction coordinates, generic identical vanishing
also gives original rank at most36 at EVERY point of this Q+tT_a slice;
special ranks may fall. This does not concern other quadratic directions.
Nonzero fourth and fifth give their respective first
remaining pivot, proving the other two cases. The all-orders conclusion
is specific to the residual-large R=0 factorization and does not extend
this argument to the separated endpoint-sixteen branch.

## Verification boundary

verify.py authenticates the retained immutable inputs and checks the
full formal coefficient identities (11)-(17), with no evaluation of an
actual direction or source. It also checks the symbolic linear identities
for (18)-(22), including preservation of q and e0, removal of the A
component, and diagonal vanishing for an arbitrary P-valued argument.
These are certificates for the algebraic mechanism; their application
to the actual maps uses the pinned geometric statements in Sections1-2.
Normal and optimized Python runs reproduce RESULT.json. All actual
Schur scalars and the branch itself remain unselected.
