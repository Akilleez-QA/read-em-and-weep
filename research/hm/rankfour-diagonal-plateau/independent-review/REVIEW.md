# Independent review of the ordered rank-four (2,2) plateau

## Current verdict

PASS. The corrected mathematical derivation and the complete frozen public mathematical
packet pass independent review. Accepted author manifest SHA256:
d9c70b32bcb4819f07d9b556313b266cf248a35a544ba894542d8200162da378.
Accepted proof SHA256:
0fcfaf0258427ae436572b386587ea1652718ed2ce7d0ffb23482af0f83eae25.
Accepted verifier SHA256:
6ca8f891d05a9a18074bfdb2645df6e95253fb309cb0783b6fcd7eb211d124b1.
This review excludes only the ordered maximal rank-four plateau (2,2),
conditional on the retained actual geometric inputs. It does not establish
generic SF rank at least five, surjectivity, full-adjoint invertibility, or
the original repair.

The filter H1(D0(1)) >= H1(Q*(1)) is invalid because it assumes an
unjustified surjection on H1. The corrected derivation below does not use it
and retains both positive-defect cases through the complete search and final geometry.

## Independent methods and source authentication

`independent.py` imports no author implementation. It uses exact conjugacy
class characters in Q(sqrt(5)), and enumerates ordinary line-degree
partitions before decomposing each equal-degree coefficient representation.
This is independent of the author's McKay recurrence and irreducible-block
enumeration. Normal and optimized Python runs agree byte for byte.

All five original input files were freshly retrieved through the GitHub
connector at commit db51525015bb7c5e825833d550d08dedf6f6ea96 and compared
byte for byte with the author's inputs, including SHA256, Git blob SHA1,
and byte count. The full original rank-one flag theorem is directly included:

- Path: research/hm/order-four-quadratic-load/RANK-ONE-GAUSS-FLAG-DEGREE-EXCLUSION.md
- Git blob: 4843b6e506495ccc8649d28f11eb18568cb65154
- SHA256: efc9ca4ea3348429be704d27096ba8ceec00de522ee5159bcfdf33972ecd7d22

The source files are under `remote-inputs/`. No actual-instance coefficient,
parameter, jet, matrix, or rank evaluation is used. The calculations concern
universal representations, hypothetical splitting data, and degree identities.

All 14 public mathematical manifest entries authenticate. Coordination material is omitted; all mathematical source bytes are unchanged. Author normal and optimized
outputs replay byte-exactly against RESULT.json. The independently computed
359 cohomology tuples and 172 residual tuples agree with the author's complete
sets, not merely their counts. The independent checker also passes 22 genuine
subprocess mutation rejections, including defect omission, parity deletion,
torsion sign/length, duality and derivative twists, and final rank-one errors.
The author's 28 subprocess mutation controls were separately replayed and
matched CONTROLS.json byte for byte.

## Degree and torsion completeness

For the saturated four-block chain F0 < F1 < F2=E < F3 < F4, the
endpoint ranks are 9 and 5. The reversed flag is Di=F(4-i)^perp.
Each proper interior stage has no constant subbundle. Universal section
persistence at the endpoints gives every endpoint line degree at most -4,
so a<=-36 and b<=-20. Center-even determinant parity makes a,b,ci even.

With c(i+1)=ci+8+delta_i, direct elimination of c1 gives

    a+b = -76 + delta1 + 2 delta2 + delta3.

Thus, writing a=-36-2u and b=-20-2v,

    2(u+v)+delta1+2delta2+delta3=20.

The invariant-divisor semigroup leaves only defects 0,12,20 below this
budget. Delta2 must vanish. A defect20 forces a=-36,b=-20 and makes c1
odd, hence is excluded by determinant parity rather than silently dropped.
The resulting nine cases are exactly:

- No defects: (-54,-22), (-50,-26), (-46,-30), (-42,-34), (-38,-38).
- Delta1=12: (-42,-22), (-38,-26).
- Delta3=12: (-42,-22), (-38,-26).

Put B=L2. Since delta2=0, L3=B(2). The genuine torsion sequences give

    [E]-[F0]=[B(-2)]+[B]-[T1],
    [Q]-[D0*]=[B(2)]+[B(4)]+[T3(2)],
    [F0]-[D0*(-4)]=[E]-[Q(-4)]+[T1]+[T3(-2)].

A length12 torsion cokernel is supported with length1 at each point of the
unique orbit of size12. Its stabilizer is cyclic of order10. Trivial central
action leaves exactly the five characters represented by O_D(r),
r=0,2,4,6,8 modulo10. Their Euler character is chi O(r+t)-chi O(r+t-12).
For the upper defect the parameter r denotes T3(-2), not T3 itself. This
absorbs the twist without losing any stabilizer character.

The endpoints are completely enumerated from rank, total degree, parity,
and their forced line-degree window [degree+4(rank-1),-4]. For B, the
quotient E -> B gives H1(B(1)) <= W'+3T6. Dimension first bounds any
negative splitting degree below by -22; the exact character comparison
excludes every degree below -10. Therefore B's complete forced line window
is [-10,degree(B)+30]. No historical source-type list is required.

## Valid sequence inequalities

The following comparisons hold in the representation cone:

1. H1(B(1)) <= H1(E(1)) = W'+3T6, from E -> B.
2. chi B(2)-chi E(2) >= H1(B), from 0 -> F1 -> E -> B -> 0,
   H0(F1(2))=0, and the successive surjections
   H1(F1(2)) -> H1(L1(2)) -> H1(B).
3. -chi B(-2)-chi Q*(2) >= H0(B), from 0 -> D1 -> Q* ->
   B*(-2) -> 0, H0(D1(2))=0, and the successive surjections
   H1(D1(2)) -> H1(L4*(2)) -> H1(B*(-2)).
   The last surjection follows from L4*(2) -> B*(-2) with torsion cokernel.
4. H0(B(-1)) <= -chi Q*(1), from the quotient Q*(1) -> B*(-1)
   on H1 and Serre duality. H0(Q*(1))=0 follows from persistence.

All torsion quotients have H1=0. No erroneous surjection H1(D0)->H1(Q*)
is used. The parent replacement lemma with additional H0(B(1)), H0(B(-1)),
and H0(T3(-1)) terms is correct but is not needed by this checker.

## Independent finite results

The nine cases give the following counts, with both endpoint Euler
identities checked at twists0,1 and all four valid inequalities applied:

| a,b,delta1,delta3 | Endpoint domains | B raw domain | Cohomology rows | After horizontal tests |
|---|---:|---:|---:|---:|
| -54,-22,0,0 | 1355 x 10 | 308 | 216 | 132 |
| -50,-26,0,0 | 680 x 24 | 268 | 17 | 0 |
| -46,-30,0,0 | 303 x 46 | 253 | 24 | 0 |
| -42,-34,0,0 | 130 x 83 | 218 | 8 | 0 |
| -42,-22,0,12 | 130 x 10 | 218 | 12 | 0 |
| -42,-22,12,0 | 130 x 10 | 308 | 70 | 40 |
| -38,-38,0,0 | 33 x 130 | 208 | 6 | 0 |
| -38,-26,0,12 | 33 x 24 | 208 | 6 | 0 |
| -38,-26,12,0 | 33 x 24 | 268 | 0 | 0 |

There are 359 cohomology rows and 172 horizontal-test survivors. All complete rows and explicit horizontal
witnesses are recorded in `INDEPENDENT-RESULT.json`.

## Why the horizontal tests are legitimate

For a saturated direct-sum subbundle S of an endpoint A, if

    Hom_G(S,outer target)=0,
    Hom_G(S,(A/S)(-2))=0,

then its ambient derivative has zero image both outside A and modulo S
inside A. Thus S is derivative invariant. Saturation makes it a constant
subbundle, impossible since all its splitting degrees are negative.

The torsion-safe outer targets are B(-4) for F0 and B*(-6) for D0:
the actual targets inject into these bundles, even with delta1 or delta3
positive. The script chooses the union of all coefficient blocks with no
path to the outer target in the graph of possible equivariant derivative
Homs. This union has no outgoing internal or external Hom, and the script
verifies both vanishing conditions directly for every recorded witness.
It does not declare the chosen Birkhoff splitting horizontal.

## The final 172 rows

Every remaining row has delta3=0 and

    D0 = W'O(-5) + V O(-4),
    B = O(-8) + C,

where C is one of O(2)+O(4)+O(6), O(2)+W O(5), W O(3)+O(6), A O(4).
The true reversed derivative target is B*(-6), which is O(2) plus
summands of ordinary degrees at most -8. There are no ordinary bundle Homs
from D0 to those latter summands. Therefore beta_D0 has generic rank at
most1. It cannot vanish, because a saturated derivative-invariant D0
would be constant, contradicting degree -22. Its rank is exactly1.

Let U be D0's smallest constant span, of dimension N. It is G-invariant.
D0 is saturated in U O, has no constant section, and spans U. Successive
backward Gauss increments are at most1 and cannot vanish at a positive
rank, because the stages lie in D0. Successive forward increments likewise
remain1 until U: a proper constant stop would contradict minimality of U.
This proves the complete saturated unit-step flag, not merely its numerical
degree identity.

The first j forward transforms of D0 lie in the reversed plateau stage Dj.
If N-5<=3, the constant bundle U O would occur inside a proper interior Dj,
which has no constant subbundle. Hence N>=9. The complete rank-one degree
bound 22>=5(N-5) gives N<=9, and therefore N=9.

For r=5, N=9, the exact full-flag identity requires

    9(22-5*4)=18
      =4 sum_(j<5) j delta_j +5 sum_(j>=5)(9-j) delta_j.

All these divisors are G-invariant. A positive delta_j is at least12,
and the smallest weight is4. Thus the right side is either0 or at least48,
never18. All172 residual rows are excluded, including the40 positive
lower-defect rows. No horizontal decomposition of the complete flag is used.

## Audit boundary

The arithmetic checker does not establish the actual kernel presentations,
local freeness, geometric identification with the original multiplication
problem, or general Gauss saturation lemmas from scratch. These retained
inputs are identified above and in the original source packet. Within
that boundary, the corrected derivation is complete. This is not a
proof-assistant certificate or an unconditional repair of the original theorem.

## Public packaging

This portable review uses the relative accepted-author-packet/ snapshot. Its
manifest contains fourteen mathematical files, omitting coordination material.
The accepted proof, verifier, results, controls and five original source files
are byte-identical to the accepted mathematical packet. The sole
change to the independent arithmetic checker is its relative source path and
public manifest digest; one fewer manifest-member authentication reduces the
check count by one without altering any mathematical computation.
