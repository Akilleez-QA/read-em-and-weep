# The cf source at index113 must have the twelve-point high-line divisor

## Result and scope

For G3.11.ad509d55173f, original source index113 and tuple
(0,0,1,0,0,1,0,1), put

    E=(V+P+D) O(-2)+V O(-4)+O(-8)+O(-10),
    A_q=O(-10)+O(2)+O(16).

The D O(-2) component to O(2) is necessarily nonzero. For
F=(V+P) O(-2), the induced map to O(16) necessarily has the reduced
invariant divisor D12 of degree twelve. In particular its basepoint-free
branch is impossible.

In the remaining branch there is an actual constant nine-space
C=Sym8 W=P+D, and exact actual subsystems

    F=(Sym6 W) O(-2),
    M=F^+=(Sym7 W) O(-1),
    M^+=C O,
    C O/M=O(8),
    C O/F=W O(7).

They satisfy

    E intersect C O=F,
    E^+ intersect C O=M.

No saturation of the projected residual E/F in (H/C) O is asserted.
Its possible modification remains a separate dependency.

This is a complete exclusion of the basepoint-free branch and a rigorous
restriction on the remaining branch, not a whole-source or whole-label
exclusion. No source-instance coefficients, parameters, points, derivative
values, matrices, ranks, selected models, scans, or large computation are
used. All arguments are universal representation and bundle arguments.

## 1. Inputs

Original source and quotient data are pinned at
https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load
in ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md,
NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md,
one-one-endpoint-necessary-pairs.json, and
rank-three-quotient-frontier-144.json. The complete original index113
source overlist has ten tuples; only the displayed cf tuple is treated.

The actual E is saturated in a constant thirty-space H O, all its degrees
are at most-2, and H0(E^-(2))=0. Original determinant defect zero makes

    E^+/E=A_q(2)=O(-8)+O(4)+O(18)                    (1)

an actual saturated subbundle of Q=(H O)/E.

Use the binary icosahedral irreducibles W,Wp,A,V,P,S,D,T, with
A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W. There are no nontrivial
one-dimensional characters. Every nonempty invariant effective divisor
has degree at least12; the divisor of degree12 is the reduced exceptional
orbit D12.

We use the actual derivative-image and rank-one quadratic-gap arguments
of PR796, commit d2b43060c83328dd5118aee6b9288fcfa0c873ac, and the
complete (V+P+D) kernel support and first-polar argument of PR802, commit
e484640a6565c278321bf6557860262c1ac1b7df. All applications are restated.
The corresponding proof paths are research/hm/profile12-quadratic-block-exclusion/PROOF.md
and research/hm/profile11-o16-constant-span-exclusion/PROOF.md.

## 2. The low D row cannot vanish

If the full top R O(-2), R=V+P+D, mapped only to O(16), strict-top
would inject its twelve sections into Sym18 W. A common divisor would
leave at most seven sections, so this map is onto. Its kernel has
H1 at twist2 equal to A+P and Euler character at twist3 equal to T-W.
The exhaustive PR802 support argument gives exactly

    T O(-3)+P O(-4)+O(-6),
    (Wp+T) O(-3)+Wp O(-5)+O(-6).                     (2)

Their internal derivative target is V O(-6)+O(-10)+O(-12). Every
component is zero, including the only degree exception O(-6)->V O(-6).
Thus the full raw derivative image is the saturated O(16), and the first
span has quotient O(18) by the rank12 quadratic bundle.

For a rank r saturated quadratic bundle with a saturated rank-one raw
image and first-span quotient O(b), the quadratic Gauss gap is
b=2r or b<=r-1. Indeed its second span is constant; its rank is r+1
or r+2, and in the latter case the nonzero derivative between the two
line quotients gives b<=r-1. At r12,b18 neither possibility holds.
Hence the D row to O(2) is nonzero. Its equivariant channel is the
complete quartic evaluation and is onto.

Neither V nor P maps to O(2), since Sym4 W=D. Therefore F=(V+P) O(-2)
maps only to O(16). Its seven sections are independent by strict-top.
Their common invariant divisor has degree0 or12. In the latter case
the residual system is the complete Sym6 W=V+P.

## 3. Complete kernels in the basepoint-free branch

Suppose F->O(16) is onto, and write K for its kernel. Then

    H0(K(2))=0,
    H1(K(2))=A+P+D,
    chi_G(K(3))=-W-S.                               (3)

For an atom U O(-j), j>=4, its contribution to the H1 budget in(3)
is U Sym(j-4) W. Parity and (j-3)dim U<=12 give the complete allowed
atoms below. The two right-hand entries are its H1 at twists2 and3.

    A O(-4): A,0;       P O(-4): P,0;
    D O(-4): D,0;       Wp O(-5): P,Wp;
    S O(-5): A+D,S;     O(-6): A,W;
    V O(-6): P+D,T;     W O(-7): A+D,W+S;
    O(-8): D,S;         Wp O(-9): A+P+D,S+T;
    O(-12): P+D,Wp+T.                                (4)

For clarity this is an exhaustive support list. At j4 it is immediate;
at j5 the other odd representations contribute a forbidden trivial or
V constituent. At j6 the only survivors are1 andV. At j7 only W survives,
since Wp Sym3 W=V+D. At j8 only1 fits. At j9 only Wp survives, since
W Sym5 W=V+P+D. At j10,12,14 the only dimension-eligible even coefficient
is1; their contributions are V+P, P+D, A+V+D, respectively, so only12
survives. Later atoms exceed dimension12. Odd j>=11 also exceed it.

The negative W in(3) forces either O(-6) or W O(-7), which consumes
the unique A. If W O(-7) is used, the remaining P is supplied by
P O(-4) or Wp O(-5). If O(-6) is used, the required S can only be
supplied by O(-8), and the same two P choices remain. Degree-minus-three
coefficients are then forced. Thus exactly

    K=P O(-4)+W O(-7),
    K=Wp O(-3)+Wp O(-5)+W O(-7),
    K=P O(-4)+O(-6)+O(-8),
    K=Wp O(-3)+Wp O(-5)+O(-6)+O(-8).                 (5)

The internal target is D O(-4)+V O(-6)+O(-10)+O(-12).
All components vanish except the unique channels

    W O(-7)->D O(-4),
    O(-8)->D O(-4).                                  (6)

They are respectively the universal multiplication W tensor l^3 into
Sym4 W and the tautological l^4 line, at an arbitrary tautological line
l. Each is an everywhere injective subbundle map. Hence the internal
image J is0, W O(-7), or O(-8), always saturated.

The positive O(16) is saturated in Q(-2), so the actual raw image I
and actual first span M satisfy

    0->J->I->O(16)->0,
    0->F->M->I(2)->0,                                (7)

with no saturation correction. First-polar generation makes every
splitting degree of M either0 or-1.

J=0 gives deg M=4, impossible. J=O(-8) gives the constant character
A+P and the purported linear character T-S, which is not genuine.
The only remaining case is

    J=W O(-7),
    M=P O+T O(-1).                                   (8)

Indeed chi_G(M)=P and chi_G(M(1))=Wp+2T, and P W=Wp+T.

## 4. The projected linear span is forced

Let C0=P be the actual constant space H0(M). Constant projection makes
L=M/C0=T O(-1) an actual saturated subbundle of (H/C0) O. The projected
map from F has precisely the two multiplicity-one channels from V andP.

The P channel cannot vanish: otherwise P O(-2) would inject into the
constant P of equal rank, giving a nonzero invariant determinant of
degree8. Such a determinant does not exist.

If both channels were nonzero, rescaling the two irreducible source
factors identifies their map with the complete Euler contraction

    Sym6 W O(-2)->Sym5 W O(-1).

This is everywhere onto. Derivatives of the projected F land in L;
an everywhere onto image equal to L would therefore make L horizontal.
That contradicts its degree-6. Thus the V channel is zero.

For completeness, the following general linear-bundle fact identifies
the remaining span and also proves the needed saturation. If an actual
saturated L=R O(-1) has coefficient span C1 and constant coefficient map
R tensor W onto C1, with kernel K1, the Euler sequence gives

    L^-=K1 O(-2).                                    (9)

Fiberwise injectivity of L ensures that this is a bundle identity: the
kernel K1 has zero intersection with each R tensor l, and the Euler
projection embeds K1 O(-2) in R O(-1). Its image is exactly the kernel
of the induced derivative. This is the actual constant connection.

The nonzero projected P O(-2) is killed by beta_L, so(9) gives an
injection P->K1. But T W=V+P+D is multiplicity-free. Since L is negative,
its constant span has dimension at least7, so dim K1<=5. Consequently
K1=P and C1=V+D. In particular

    L^-=P O(-2),
    C1 O/L=Wp O(3),
    L/L^-=Wp O(1),                                  (10)

and the induced derivative between the last two bundles, after twist-2,
is an isomorphism. The splitting in(10) follows also by tensoring the
complete cubic Euler sequence with Wp: Wp Sym3 W=V+D and
Wp Sym2 W=T.

Let Ctot be the actual constant span of M. Then

    Ctot=P+V+D, dim Ctot=12,
    Ctot O/M=Wp O(3),
    M/M^-=Wp O(1), rank M^-=8.                       (11)

No abstract complement has been endowed with a connection.

## 5. A rank-two channel forces an impossible constant space in E^+

Let N=E intersect M. Equation(7) identifies

    N/F=J(2)=W O(-5), rank N=9.                     (12)

Since F is killed by beta_M, projection to M/M^- induces

    W O(-5)->Wp O(1).                                (13)

It is nonzero, because otherwise N would lie in the rank8 bundle M^-.
Every nonzero equivariant map in(13) has generic rank2. Here is a
basis-free proof excluding generic rank1. Saturate a putative rank-one
image inside Wp O(1), obtaining an invariant line O(d), with d<=1.
A nonzero map W O(-5)->O(d) requires d>=-5 and W in Sym(d+5) W.
For degrees0 through6 the only such occurrence is Sym1 W, forcing d=-4.
But O(-4)->Wp O(1) is zero because Sym5 W=T contains no Wp.
Thus a rank-one image is impossible.

The actual derivative of M identifies its quotient in(13) with
(Ctot O/M)(-2). Since N lies in E, its derivatives lie in E^+.
The generic rank-two conclusion therefore forces Ctot O inside E^+;
saturation of E^+ upgrades the generic containment to sheaf containment.

Its map to the two lower summands O(4)+O(-8) in(1) vanishes. It is zero
on M, whose external image was only O(18); hence it factors through
Ctot O/M=Wp O(3). Both remaining Hom spaces are zero, the O(4) channel
because Wp is not W, and the negative channel by degree.

Thus Ctot O has image a nonzero subsheaf of O(18) in E^+/E. Its kernel
is a rank11 subbundle of E of degree at least-18. On the other hand
every splitting degree of a subbundle of E is at most-2, so this degree
must be at most-22. Contradiction. This excludes the complete basepoint-free
branch.

## 6. The surviving divisor branch has a genuine degree-eight subsystem

Now the high-line map of F has divisor D12 and residual complete degree6
system, so K=T O(-3). Its internal target has largest degree-4, and its
internal derivative is zero. The raw first span has rank8 and degree-8,
with quotient O(6) by F. Its invariant saturation defect is at most8
because its saturation is a subbundle of a constant bundle. A nonzero
such defect would have length at least12. Hence the raw span is already
saturated and

    M=(Wp+T) O(-1)=Sym7 W O(-1).

The derivative of M kills F and therefore has rank at most1. It is not
zero, since a negative saturated bundle cannot be horizontal. A linear
bundle reaches its coefficient span after one derivative. Its constant
span C has rank9 and quotient O(8) by M. Taking global sections makes
this the complete evaluation sequence for degree8, so C=Sym8 W=P+D.
Its derivative kernel is precisely F=Sym6 W O(-2), and the two-jet
Euler quotient is

    C O/F=W O(7).                                    (14)

## 7. Exact intersections, without assuming a saturated projection

First C is not contained in E^+. If it were, its quotient in(14) would
map to(1), with the lower two components zero by degree. A nonzero map
W O(7)->O(18) is onto: its two degree11 sections have an invariant
common divisor, and degree11 is below the minimum12. Its kernel is
O(-4). Thus (E intersect C O)/F=O(-4), which would inject into

    E/F=D O(-2)+V O(-4)+O(-8)+O(-10).

Every equivariant Hom from O(-4) into this bundle is zero: Sym2 W=A
has no D, V has no invariant vector, and the last degrees are too small.
This is impossible.

Since M lies in E^+, the intersection C O intersect E^+ therefore has
rank8. It equals M because M is saturated. If N0=E intersect C O,
then derivatives of N0 lie both in C O and in E^+, hence in M.
Since N0 lies in M, it lies in M^-=F. The reverse containment is known,
so N0=F. This proves both exact intersection identities.

## Remaining boundary

The divisor-twelve branch is not excluded. Any later use of the projected
residual must establish its saturation or keep its torsion modification.
The proof establishes no source-edge, whole-label, or global decrement.
