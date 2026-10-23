# The double twelve-orbit modification excludes the remaining cf branch

## Statement and inputs

The source is G3.11.ad509d55173f, original source index113, tuple
(0,0,1,0,0,1,0,1), with

    E=(V+P+D) O(-2)+V O(-4)+O(-8)+O(-10),
    A_q=O(-10)+O(2)+O(16),
    B_q=O(-18)+O(-4)+O(8).

The original source, quotient and actual cohomology data are pinned at
https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load
in ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md,
NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md,
one-one-endpoint-necessary-pairs.json, and
rank-three-quotient-frontier-144.json.

PR861, commit7b5b3371a82cb92f46ea60895e45617d0891a5b0, excludes the
basepoint-free branch and proves the exact subsystem/intersection inputs
used here:
https://github.com/Akilleez-QA/read-em-and-weep/blob/7b5b3371a82cb92f46ea60895e45617d0891a5b0/research/hm/profile11-source113-cf-reduction/PROOF.md

Assume its remaining divisor-twelve branch. By its §§6–7, F has constant
span C=Sym8 W,
M=F^+=Sym7 W O(-1), E intersect C O=F, E^+ intersect C O=M,
and

    B=C O/F=W O(7),
    M/F=O(6),
    C O/M=O(8),
    E^+/E=A2=O(-8)+O(4)+O(18).

The map M/F into A2 is multiplication by f12 into its highest line
L=O(18). All displayed intersections concern actual sheaves and the
original constant connection. The original E spans H, dim H=30,
and dim C=9.

Then the image

    Z0=E/F=D O(-2)+V O(-4)+O(-8)+O(-10)

in the constant quotient (H/C) O has saturation defect exactly24,
with multiplicity exactly2 at every point of the reduced orbit D12.
Its saturation Z has rank10 and degree-16 and spans H/C. The saturated
image S of B in Q=(H O)/E has rank2, degree38, and

    0 -> O(18) -> S -> O(20) -> 0.                    (1)

Thus, as equivariant bundles, S is either O(18)+O(20) or W O(19).
No assertion of either branch's actual occurrence is made.

Together with the dual cohomology and strict-top argument in Section6,
these constraints exclude the complete divisor-twelve branch, hence the
entire cf source when combined with the pinned PR861 basepoint-free exclusion. No whole-label exclusion
or frontier decrement is claimed.

## 1. Derivative compatibility forces a first divisor in the quotient

Let Qplus=(H O)/E^+. The exact intersection with E^+ gives an injective
sheaf map

    j:C O/M=O(8)->Qplus.

The derivative of E^+ kills E. Its restriction to the highest line
of A2 is a map

    phi:O(18)->Qplus(-2).

The derivative of M induces the isomorphism
M/F=O(6)->(C O/M)(-2)=O(6), since M is the complete linear evaluation
kernel. Its comparison with the derivative of E^+ therefore gives

    j(-2)=f12 phi,                                    (2)

up to a nonzero constant. In particular j vanishes on D12. Neither
j nor phi is claimed to be saturated at this stage.

## 2. Stabilizer characters prevent the missing lower-row correction

Because L is saturated in Q, form the vector bundle Q/L. The inclusion
B->Q induces

    k:B/(M/F)=O(8)->Q/L.

Its projection to Qplus is j. At every point of D12, j vanishes, so
k's fiber image lies in (A2/L)=O(-8)+O(4).

The stabilizer calculation is uniform over the orbit, not a choice of
an actual parameter. Take an arbitrary stabilizer and its binary lift
with eigenvalue zeta on the tautological line, where zeta has order10.
The fiber character of O(a) is zeta^(-a). The domain O(8) has character
zeta^2, while the two possible target fibers O(-8) and O(4) have
characters zeta^8 and zeta^6. These are distinct. Equivariance thus
forces the whole fiber map k to vanish at every point of D12.

Since D12 is reduced, k factors through multiplication by f12:

    O(8) --f12--> O(20) -> Q/L.                      (3)

This step cannot be replaced by assuming a global splitting of Q:
there need not be a projection Q->O(-8)+O(4). The fiber-character
argument supplies precisely the needed divisibility without one.

## 3. The rank-two determinant has at least the double divisor

Locally split the line subbundle L in Q. Choose a frame of B extending
its saturated line M/F=O(6). The first column of B->Q is f12 times
a generator of L. By(3), the second column modulo L is also divisible
by f12. Therefore every rank-two minor of B->Q is divisible by f12^2.

For an inclusion of equal generic-rank vector bundles on a smooth curve,
the divisor of the maximal minors is exactly the determinant divisor
between its image and saturation. Consequently the saturation defect
divisor is at least2D12. Let its total length be delta; then delta>=24.

Both B->Q and Z0->(H/C) O have the same cokernel H O/(E+C O).
Its torsion subsheaf is their respective saturation quotient. Hence the
two defects, including their scheme-theoretic multiplicities, agree. Thus

    rank Z=10, deg Z=-40+delta.                      (4)

This does not require that E+C O itself was saturated.

## 4. Full span forces the defect to be exactly24

The original E spans H, so Z0, and hence Z, spans H/C of dimension21.
Since Z is saturated in a constant bundle, each of its splitting degrees
is nonpositive. Hence

    h0(Z*)=rank Z-deg Z=50-delta.

Full span means that the constant coefficient restriction
(H/C)*->H0(Z*) is injective. Therefore delta<=29.

The effective invariant divisor obtained by subtracting2D12 from the
defect divisor has degree delta-24 between0 and5. It must be empty,
because every nonempty invariant effective divisor has degree at least12.
Thus delta=24, and the entire defect divisor is exactly2D12. Equation(4)
gives deg Z=-16.

## 5. The saturated rank-two quotient has only two bundle types

The saturation S of B in Q has degree14+24=38. It contains the entire
line L: B contains f12 O(6) with generic span L, and S is saturated in Q.
As L is saturated in Q, it is also saturated in S. Therefore S/L is a
line of degree20, proving(1).

The extension space is H1(O(-2)), a one-dimensional trivial G-module.
The zero class gives O(18)+O(20); every nonzero class gives the twist
by19 of the standard Euler extension, namely W O(19). This is an
abstract equivariant splitting classification only, not a horizontal
splitting or an identification of a particular actual extension class.

## 6. Dual cohomology contradicts strict-top at the original negative endpoint

Let R be the dual of Q/S. Since S is saturated in Q, there is an exact
sequence of vector bundles

    0 -> R -> Q* -> S* -> 0.                          (5)

Thus R has rank11 and degree-16. The pinned original actual-bundle input gives the exact presentation

    0 -> Q* -> M3* O(-1) -> M2* O -> 0,
    M3=3Wp+3S+6T, M2=A+2V+3P+4D.

At twist0 its cohomology gives H1(Q*)=M2 and H0(Q*)=0. At twist3
Euler additivity gives M3 Sym2 W-M2 Sym3 W. The fixed character
products therefore supply

    H1(Q*)=M2=A+2V+3P+4D,
    chi_G(Q*(3))=T-2W-S.                             (6)

Here S on the right of(6) is the four-dimensional irreducible Sym3 W;
the rank-two bundle S in(5) is distinguished by context. Every splitting
degree of Q*, and hence R, is at most-1: Q* has no constant subbundle.
We do not assume H0(Q*(1))=0.

Both possible bundle types in Section5 have the same equivariant
K-class, so

    H1(S*)=Sym16 W+Sym18 W=A+2V+3P+3D,
    chi_G(S*(3))= -Sym13 W-Sym15 W.

The H0 groups of S*, Q*, and R vanish by negativity. The cohomology
sequence of(5) therefore gives

    H1(R)=D,
    chi_G(R(3))=-W+Wp+S+4T.                          (7)

For the latter identity, Sym13 W=W+Wp+S+T and Sym15 W=S+2T.

There are exactly two ways to supply H1(R)=D with degrees at most-1.
For an atom U O(-j), j>=2, the H1 contribution is U Sym(j-2) W and
(j-1)dim U<=5. At j2 only D survives. At j3 none survives: the four
odd irreducibles tensored with W give1+A, P, A+D, V+P+D, respectively.
At j4 only the trivial coefficient fits the dimension bound, but gives
A rather than D. At j5 no odd coefficient fits. At j6 the trivial
coefficient gives D; all later atoms exceed dimension5. Thus precisely

    R=L6 O(-1)+D O(-2),
    or R=L10 O(-1)+O(-6),                            (8)

where L6,L10 are genuine center-odd coefficient representations of the
indicated dimensions.

In the first alternative, (7) and D W=S+T force

    L6 tensor A=-W+Wp+3T,

which is not a genuine character. Therefore the second alternative
holds. Its twist3 Euler character gives

    L10 tensor A=Wp+S+4T.

Using the complete four odd irreducibles and

    W A=W+S,        Wp A=T,
    S A=W+S+T,      T A=Wp+S+2T,

the absence of W forces the W and S multiplicities of L10 to be zero;
the Wp and S multiplicities on the right force exactly one T, and the
remaining T multiplicity forces exactly two Wp. Hence

    R=(2Wp+T) O(-1)+O(-6).                           (9)

Finally the original dual Gauss quotient is

    B_q=O(-18)+O(-4)+O(8).

The universal strict-top theorem applies to the actual Q* since all its
degrees are at most-1. It gives H0((Q*)^-(1))=0, so the quotient map
Q*->B_q induces an injection

    H0(Q*(1)) -> H0(B_q(1))=Sym9 W=S+T.              (10)

But the subbundle R in(9) injects H0(R(1))=2Wp+T into H0(Q*(1)).
The target in(10) has no Wp. This is impossible.

Therefore the divisor-twelve branch is excluded. Together with the
pinned PR861 basepoint-free exclusion, this excludes
the complete cf source tuple (0,0,1,0,0,1,0,1) at original source index113.

## Boundary

This is one source-edge exclusion, not a full-label exclusion or a
realizability statement. The torsion modification was proved and kept,
not silently discarded. The dual argument needs only the pinned H1 and
Euler identities, the exact quotient B_q, and strict-top at degree-1;
it does not import the unavailable stronger vanishing H0(Q*(1))=0.
No selected actual coefficients, parameters, points, derivatives,
matrices, ranks, or source experiments were used.
