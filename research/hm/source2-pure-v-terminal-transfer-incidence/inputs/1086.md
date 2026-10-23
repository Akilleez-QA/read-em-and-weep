# Exact odd invariant-quadratic rank and its remaining homotopy interface

## Result

Retain the conditional actual source2 nonzero pure-V Q-compatible radical
hypotheses. Let Q_d denote multiplication by the SAME invariant quadratic
from degree d to degree d+2, with the inherited central parity. Then

    im Q_3 = the full T-isotypical component of M5_-=W'+3T,
    coker Q_3 = W',        rank Q_3=18,
    ker Q_3 = 3W'+3S+3T  as a representation.             (1)

In particular the map on T multiplicity spaces is onto C^3, of exact
rank three, and the W' component is zero. This holds for the ACTUAL
invariant rank-three quadratic under the stated hypotheses, not for a
generic smooth quadratic or an evaluated source instance.

The remaining independent interface is exact: for the odd two-term
complex M3 --Q_3--> M5, the endomorphism (j3,0) is nullhomotopic iff

    j3(ker Q_3)=0,

or equivalently iff the combined T-multiplicity map (Q_3,j3) has rank3
rather than4. If this condition holds there is a UNIQUE equivariant
nullhomotopy with image in the marked I3=im j3. General equivariant
nullhomotopies need not be unique. This proof does not decide the
condition or an alternating-transfer coefficient.

## 1. Immutable inputs and notation

INPUTS.json authenticates four complete public proofs:

- PR795 at 3f811311d76914a555c7e7d0c5b887b41805aa6c,
  research/hm/source2-radical-filtration/PROOF.md, gives the actual
  fixed-variable reconstruction, all-coupling exact quotient bundles,
  and intertwining of j with BOTH original negative arrows.
- PR792 at 2f01f18960ce56b8b2a0c1260c277de3c5f916bf,
  research/hm/source2-radical-rank-profile/PROOF.md, identifies the actual
  pure-V image spaces I2=D, I3=T, I4=P, and their inherited arrows.
- PR1019 at 3fb2475ffb275c5789acbaa8f9f84ed272713785,
  research/hm/source2-pure-v-secondary-homotopy/PROOF.md, records
  ker j4=im Q_2 and im j4=I4. These are actual subspaces.
- PR1052 at 64e4fdd771a14a764c6e119d2eb25b0237d83622,
  research/hm/negative-string-terminal-gate/PROOF.md, proves the actual
  exact negative-coordinate Koszul sequence

      0 -> M3 --delta--> W tensor M4 --mu--> M5 -> 0,     (2)
      M3=3W'+3S+6T, M4=2V+4P+3D, M5=W'+3T.

  Here delta(s)=x tensor ys-y tensor xs in the fixed determinant
  convention; mu is actual multiplication. Character subtraction alone
  is not used as a replacement for its exactness.

Write N2=M2_+ and M3=M3_-, M4=M4_+, M5=M5_-. The invariant quadratic
is central-even and actual multiplication commutes:

    Q_3(l v)=l Q_2(v) for every l in W, v in N2.         (3)

No extension of the degree-shifting homotopy h is assumed. The fixed
radical intertwines M3->M4, which is all the radical commutation needed.

## 2. Actual first multiplication is onto

To avoid confusing the invariant quadratic with a quotient bundle,
write the latter as mathcal Q. PR795 Sections2–3 gives

    mathcal Q=Sym8 W tensor O(2) direct-sum R*,
    0 -> O(18) -> R* -> A tensor O(6) -> 0,
    N2=H0(mathcal Q(-2)), M3=H0(mathcal Q(-1)),           (4)

with literal multiplication for the first arrows. Twist the residual
sequence by -3. Both outside terms O(15) and A O(3) have zero H1;
also H1(Sym8 W tensor O(-1))=0. Hence

    H1(mathcal Q(-3))=0.

Tensoring the binary Euler sequence by mathcal Q(-1) gives

    0 -> mathcal Q(-3) -> W tensor mathcal Q(-2)
                        -> mathcal Q(-1) -> 0.

Taking sections proves the actual multiplication W tensor N2->M3 is
onto. No splitting of the residual extension is required. This is valid
for both residual couplings and every remaining generated-endpoint branch.
Consequently (3) gives the exact image equality

    im Q_3=mu(W tensor im Q_2).                         (5)

## 3. The odd cokernel as a quotient of the radical image pencil

Let Z=im Q_2 inside M4. By (2) and (5),

    coker Q_3 = (W tensor M4)/(delta M3 + W tensor Z)
               = (W tensor (M4/Z))/bar_delta(M3).       (6)

The actual j4 induces an isomorphism M4/Z->I4, because ker j4=Z and
im j4=I4. Under this isomorphism, the projected delta is

    (Id_W tensor j4)delta(s)=delta(j3 s).               (7)

Indeed expanding delta gives j4(ys)=y j3(s) and j4(xs)=x j3(s), the
original negative-arrow intertwining. Thus its image is exactly delta I3,
not an arbitrary T copy inferred from characters. The full delta in (2)
is injective, and its restriction to I3 takes values in W tensor I4.
Therefore (6) is the actual quotient in the exact sequence

    0 -> I3 --delta--> W tensor I4 -> coker Q_3 -> 0.   (8)

Since I3=T, I4=P, and W tensor P=W'+T, the quotient is W'. Equivariance
now forces Q_3's image to be the entire T-isotypical component of M5:
the only W' copy is its cokernel, while all three T copies survive in
its image. Subtracting from M3 gives (1). This derives the rank at the
actual invariant quadratic from exact maps, not semicontinuity or a
smooth-quadric assertion.

## 4. Precise odd nullhomotopy criterion

First Q_3(I3)=0. Indeed I3=W I2 by the actual pure-V image description,
Q_2(I2)=0 by PR1019, and (3) applies. Thus (j3,0) is a chain endomorphism
of the odd complex. An equivariant nullhomotopy k:M5->M3 must satisfy

    k Q_3=j3,       Q_3 k=0.                           (9)

Necessarily j3 vanishes on ker Q_3. Conversely, if it does, j3 factors
through im Q_3 with values in I3. Extend this factor by zero on the
canonical W'-isotypical complement in M5. The resulting k is equivariant,
has image in I3, and satisfies both identities in (9). Because
Hom_G(W',I3)=0, it is the unique such k whose image lies in I3.

For unrestricted equivariant k, differences factor through
Hom_G(coker Q_3,ker Q_3)=Hom_G(W',3W'+3S+3T), of dimension3.
Thus when solutions exist they form an affine three-dimensional space;
no general uniqueness is claimed.

On T multiplicities, Q_3:C^6->C^3 has rank3 by (1), while j3 has one
nonzero target row, since im j3=I3=T. The condition that j3 vanish on
ker Q_3 is exactly that this row lie in the row span of Q_3, equivalently
rank(Q_3,j3)=3 rather than4. The two values are possible in abstract
linear algebra even with I3 contained in ker Q_3 and j3 square-zero.
The checker includes both abstract controls solely to distinguish the
logical conditions. They are NOT examples of actual source2 modules.

Neither (8) nor the invariant quadratic's rank-three equation decides
this row alignment. A proof of independence or alignment must use an
additional actual interface beyond the identities used here. In
particular a generic smooth-quadric rank statement cannot supply it.

## 5. Verification and limits

The current coordination thread and local source2 proof packets were
checked for the odd map before this deduction. The existing exact
Koszul continuation gives M5 and extends fixed-degree endomorphisms;
it does not itself compute multiplication by the degree-shifting Q.
The new quotient (8) computes this latter map's exact cokernel.

Run python verify.py and python -O verify.py. The checker authenticates
four immutable proofs, verifies the Euler vanishing degrees, the exact
character identities, quotient arithmetic, and abstract row-alignment
controls. The actual-map proof of (5)–(8) is essential and is not replaced
by synthetic matrices. No actual HM coefficient, source parameter,
direction, point, jet, matrix or instance rank is evaluated. No source
or remaining endpoint branch is selected or excluded.
