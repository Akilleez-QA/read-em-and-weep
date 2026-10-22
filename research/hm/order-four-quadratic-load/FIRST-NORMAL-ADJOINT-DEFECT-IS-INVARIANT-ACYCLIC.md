# Invariant acyclicity of the first-normal adjoint defect

## New conclusion

Let M=omega_(2Z)(1) be the tangent-modulo-conjugation sheaf on the smooth weighted cone stack. Its first-normal twist satisfies

    H0(M(-2))^G = H1(M(-2))^G = 0.                    (1)

Equivalently, proper duality on the ordinary square thickening gives

    H0(O_(2Z)(1))^G = H1(O_(2Z)(1))^G = 0.           (2)

Here 2Z is the square of the regular Serre ideal, not the ambient double quadric. This proves that invariant global nongauge ambiguity is absent in this twist. It does not identify an arbitrary local Hessian formula with the actual midpoint lift, nor evaluate the higher secondary operation.

## 1. The necessary negative cohomology input

The precise cone groups are

    H1(B_Q(-2))^G=C,     H2(B_Q(-2))^G=0.             (3)

The second group is ZERO. It must not be confused with the one-dimensional obstruction group at twist minus four. For completeness, the negative-monad theorem gives H2(B(-2))^G=0, while ambient Serre duality gives

    H3(B(-4))^G=H1(B(-1))^{G,*}=0,

because H1(B(-1))=V+W. The ambient restriction sequence therefore proves the second equality of (3). The first follows from the same pinned negative-monad calculation. These inputs are also recorded in NORMAL-QUADRATIC-BRACKET-COMPONENT-SHADOW-GATE.md, Section 1.

## 2. The twisted Serre bundle

The actual Serre presentation, twisted by minus two, is

    0 -> O_X(-2) -> G(-2) -> I_Z -> 0.

The line O_X(-2) is acyclic. The actual zero scheme has H0(O_Z)=2·1+V and H1(O_Z)=0, as proved through the primary spinor presentation in the Serre-residue double-cover theorem. Since H1(O_X)=H2(O_X)=0, the ideal sequence gives

    H0(G(-2))=0,
    H1(G(-2))=1+V,
    H2(G(-2))=0.                                    (4)

In particular the invariant H1 is a line.

## 3. The actual map between the invariant lines is nonzero

Use the complete commutator presentation and set J=im(B_Q -> G). After twisting by minus two it gives

    0 -> O_X(-4) -> B_Q(-2) -> J(-2) -> 0,
    0 -> J(-2) -> G(-2) -> M(-2) -> 0.              (5)

The notation B_Q means its pullback to the stack where necessary. Tame pushforward is exact and preserves the cohomology used here.

The intermediate cohomology H1/H2 of O_X(-4) vanishes. Also

    H3(O_X(-4))^G=H0(O_X(1))^{G,*}=0,

since H0(O_X(1))=V+W has no invariant. It follows from (3) that

    H1(J(-2))^G=C,     H2(J(-2))^G=0.             (6)

The map H1(J(-2))^G -> H1(G(-2))^G is an isomorphism, not merely an allowed channel. Indeed, its composite with the tangent inclusion G(-2)->B_Q is the actual bracket [eta,N], up to the fixed nonzero tangent-normalization factor. The midpoint theorem proves that bracket nonzero: the boundary of N vanishes at the midpoint and is opposite and nonzero at the two ambient endpoints. Thus the map between the two lines in (4),(6) is nonzero and hence invertible.

Now the second long exact sequence in (5) contains

    0 -> H0(M(-2))^G -> C --isomorphism--> C
      -> H1(M(-2))^G -> 0.

This proves (1). No positivity or reduced-support vanishing assumption on the nonreduced curve has been used.

## 4. Duality and limits

Because M(-2)=omega_(2Z)(-1), Cohen--Macaulay duality on the proper one-dimensional tame stack gives the two dualities

    H0(M(-2)) = H1(O_(2Z)(1))*,
    H1(M(-2)) = H0(O_(2Z)(1))*.

Taking invariants is exact in characteristic zero and commutes with duality, so (2) follows.

For an invariant Cech gluing problem whose discrepancy is genuinely a cocycle in this sheaf, (1) gives existence of a correcting cochain and uniqueness modulo the usual changes of local representatives. This applies only after checking that the full frame, determinant, and coordinate changes produce that specified cocycle. It does not bypass those comparisons or determine the actual twist-four operator residue in M(4).

## Pinned sources and reproduction

- [Global defect and twist](https://github.com/Akilleez-QA/read-em-and-weep/blob/6118f6711df979073aa55b2811b801cd69bd0c14/research/hm/order-four-quadratic-load/GLOBAL-NORMAL-ADJOINT-DEFECT-DUALIZING-TWIST.md).
- [Actual Serre zero-scheme cohomology](https://github.com/Akilleez-QA/read-em-and-weep/blob/a0ccfe44a4d2b528622d591888b8cc1cddb47792/research/hm/order-four-quadratic-load/NORMAL-QUADRATIC-NONZERO-BY-SERRE-RESIDUE-DOUBLE-COVER.md).
- [Midpoint and nonzero bracket](https://github.com/Akilleez-QA/read-em-and-weep/blob/b7010f3a25097aa6c9489ff802b44f5b149f9a66/research/hm/order-four-quadratic-load/MIDPOINT-NORMAL-EXTENSION-HAS-UNIQUE-SQUARE-ZERO-ADJOINT.md).
- [Complete commutator comparison](https://github.com/Akilleez-QA/read-em-and-weep/blob/d6a23bf47a3d08a67fc809a4a7d57bb9d4bd780a/research/hm/order-four-quadratic-load/ACTUAL-THIRD-VALUE-AS-MIDPOINT-DUALIZING-OPERATOR-DEFECT.md).

The companion verifier checks the invariant characters and the formal exact-sequence dimensions after the geometric nonzero-bracket input. No actual coefficients, matrices, ranks, or parameter scans are evaluated.
