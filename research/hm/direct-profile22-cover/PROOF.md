# Direct three-pair cover for the maximal Gauss profile (2,2)

## Statement and exact scope

Work over C with the actual normalized HM module, the fixed physical binary
icosahedral marking, and the actual inclusion E in H tensor O on T=P(W*).
Assume the immutable actual-bundle inputs listed below, including the four-source
theorem. Suppose the actual second fundamental form has generic rank three and
its maximal rank-three Gauss plateau has profile (k,l)=(2,2).

Let K=E^-, L=(Q*)^-, A=E/K, and B=Q*/L. Then the ordered pair (A,B) belongs to
exactly the following necessary overlist:

1. A=O(-8)+O(2)+O(6), B=O(-8)+O(-4)+O(6).
2. A=O(-8)+O(4)+O(6), B=O(-8)+O(-6)+O(6).
3. A=O(-8)+W O(5), B=W O(-7)+O(6).

The assertion is containment in an explicit three-element list, not occurrence
or realizability of any listed pair. In each case the original transpose map
and both second-interior quotient maps have zero determinant torsion.

This is a new direct cover. It does not regenerate or consume the historical
2947/1880/1221/723/354-record chain. Its only finite calculation enumerates
abstract rank-three equivariant bundle splittings in an intrinsic finite degree
window and applies proved necessary conditions. It evaluates no actual HM
coefficient, point, map, matrix, generic rank, or parameter instance.

The terminal proof TWO-TWO-ENDPOINT-RANK-DROP-EXCLUDES-LAST-THREE-PAIRS.md
excludes all three pairs under precisely these actual endpoint and quotient
hypotheses. Therefore this cover can replace the old finite-cover chain when
using that terminal theorem, conditional on the four-source input. The cover
alone is not a global SF lower bound or a completion of the original proof.

## 1. Immutable inputs and conventions

All old paths below are in Akilleez-QA/read-em-and-weep, under
research/hm/order-four-quadratic-load/ at commit
db51525015bb7c5e825833d550d08dedf6f6ea96:

- ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, Sections 1–5:
  rank-degree pairs (17,-54) for E and (13,-54) for Q*, the actual Euler
  presentations, finite-group equivariant splitting, center parity, actual
  maximal-plateau saturation, and section persistence.
- NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md:
  if a saturated negative bundle F has highest splitting degree at most -d,
  then its actual Gauss kernel has highest degree at most -d-1. This is a
  statement about the actual constant connection, not a horizontal splitting.
- GAUSS-DETERMINANT-ORBIT-RAMIFICATION.md, Section 1: a positive equivariant
  determinant torsion length belongs to <12,20,30>, and in particular is at
  least 12.
- TWO-TWO-SECOND-INTERIOR-EULER-EXCLUDES-SEVENTEEN-PAIRS.md, Section 1:
  the actual negative-transpose factorization and degree conventions. The
  degree derivation needed here is supplied again in Section 2 below.
- TWO-TWO-ENDPOINT-RANK-DROP-EXCLUDES-LAST-THREE-PAIRS.md: terminal exclusion,
  used only for the stated corollary, not as input to the cover calculation.

The additional four-source theorem is
research/hm/primary-terminal-slope-obstruction/PROOF.md at commit
504b7eb800407dfc7e6340c98c72cdd553939f54, Sections 1–5. Its actual primary
terminal-pencil argument proves W'+T6 embeds in the canonical degree-minus-three
coefficient space R3. Intersecting this with ACTUAL's genuine splitting equations
leaves the four necessary sources

    ED = D5 O(-2)+(W'+T6) O(-3)+V O(-4)+O(-8),
    EP = P4 O(-2)+(W'+T6) O(-3)+V O(-4)+W' O(-5),
    EV = V O(-2)+(W'+T6) O(-3)+2V O(-4),
    EZ = (W'+2T6) O(-3)+V O(-4).

The four-source theorem is used as a theorem about the same actual E, not as a
source-pair ledger or an arbitrary abstract kernel. Its inherited primary-module
and terminal-reconstruction assumptions remain explicit dependencies; this note
does not reprove the original HM presentations from first principles.

Write A3=Sym^2 W, S4=Sym^3 W, D5=Sym^4 W, T6=Sym^5 W. The irreducibles of
dimension at most three are 1,W,W',A3,V. W and W' are distinct physically marked
doublets. All irreducibles used here are self-dual. There is no nontrivial
one-dimensional character. O(e) has central sign (-1)^e. Bundles E,Q*,A,B
are center-even. Every splitting is equivariant as a bundle only.

The actual Euler presentations are

    [E]=[M3 O(-1)]-[M4 O], [Q*]=[M3 O(-1)]-[M2 O],
    M3=3W'+3S4+6T6,
    M4=2V+4P4+3D5,
    M2=A3+2V+3P4+4D5.

In particular all four sources have the same equivariant Euler class.
The verifier obtains every Q* Euler character directly from this presentation;
it does not classify Q* or read the historical 37-type list.

## 2. Intrinsic degree and determinant bounds

Let M=K^- and N=L^-. The (2,2) convention says K and L are interior stages,
so their derivatives have generic rank three, with saturated kernels M and N
of ranks 11 and 7. No derivative rank is assumed for M or N.

E has all degrees at most -2 by the actual global H0(E(1))=0. Dual section
persistence for k=2 gives H0(Q*(1))=0, so Q* also has all degrees at most -2.
The strict-top lemma then gives

    maxdeg K,maxdeg L <= -3, maxdeg M,maxdeg N <= -4.

Put a=deg A and b=deg B. The actual rank-three derivatives induce injections
of equal-rank bundles with possibly torsion cokernel

    J:=K/M -> A(-2), J':=L/N -> B(-2).

Since deg K=-54-a and deg L=-54-b, their degrees satisfy

    -10-a <= deg J <= a-6,
    -26-b <= deg J' <= b-6.

Thus a>=-2 and b>=-10. Negative transposition of the two actual fundamental
forms induces an injection A -> B*(-2). Its determinant length is

    t=-6-a-b, 0<=t<=6.

The invariant-divisor gap forces t=0. Hence A is isomorphic equivariantly to
B*(-2), b=-6-a, and -2<=a<=4. Since A is center-even of rank three, a is even.
Consequently a belongs to {-2,0,2,4}.

Let s and s' be the determinant lengths of J -> A(-2) and J' -> B(-2).
The same degree estimates, without discarding any positive defect, give

    0<=s<=2a+4, 0<=s'<=8-2a.

Therefore s=0 if a<=2, and s'=0 if a>=0. At a=-2 the possible s'=12 branch
is retained; at a=4 the possible s=12 branch is retained. The filters below
never use the endpoint equality on either unproved side.

Every one of ED,EP,EV,EZ has all degrees at least -8, so E(8) is globally
generated. Since A is its locally free quotient, A(8) is globally generated.
Every ordinary splitting degree of A is thus at least -8. Since rank A=3 and
a<=4, any one of its three ordinary degrees is at most 4-2(-8)=20.

This proves the intrinsic finite window [-8,20], with no classification or
degree-minimum assumption on Q*.

## 3. Complete rank-three domain

An equivariant rank-three center-even bundle has exactly one of these forms:

1. Three trivial-coefficient lines O(e1)+O(e2)+O(e3), each ei even.
2. W O(e)+O(f) or W' O(e)+O(f), with e odd and f even.
3. A3 O(e) or V O(e), with e even.

Indeed each coefficient irreducible has dimension at most three; the preceding
list exhausts their possible dimension partitions and central signs. Repeated
line summands are allowed. The verifier exhausts these families in [-8,20],
then retains the allowed total degrees {-2,0,2,4}. For each A, B is determined
exactly as A*(-2), not chosen independently.

## 4. Every finite filter is necessary

An inequality of virtual characters below means nonnegative multiplicity of
every irreducible. H0 and H1 are computed from the equivariant Birkhoff splitting.

### 4.1 Actual source quotient constraints

For at least one of the four necessary E splittings, every direct summand of A
must receive a nonzero equivariant component from E. This is necessary because
E -> A is surjective; it is not sufficient for a quotient and is not used as
such. For a target block S O(e) and source block R O(d), eligibility is

    e>=d and Hom_G(R,S tensor Sym^(e-d) W) nonzero.

The same source E must satisfy both cohomology conditions

    H0(A(2)) >= H0(E(2)), H1(E(2)) >= H1(A(2)).

The first follows from H0(K(2))=0; the second from surjectivity of
H1(E(2)) -> H1(A(2)), since H2(K(2))=0. Testing these against one common source,
not allowing independent choices per condition, preserves necessity.

### 4.2 Twist-two Euler constraints on both towers

The exact quotient sequences and H0(K(2))=H0(L(2))=0 give

    chi(A(2))-chi(E(2))=H1(K(2)) >= 0,
    chi(B(2))-chi(Q*(2))=H1(L(2)) >= 0.

These conditions do not presume any vanishing of H1(E(2)) or H1(Q*(2)).

### 4.3 Second-interior Euler constraints, with torsion retained

Let T be coker[J -> A(-2)]. From the exact sequence
0 -> M -> K -> A(-2) -> T -> 0 and H0(M(3))=0, one obtains

    chi(A(1))-chi(K(3))=H0(T(3))+H1(M(3)) >= 0.

Using chi(K(3))=chi(E(3))-chi(A(3)) yields

    chi(A(1))+chi(A(3))-chi(E(3)) >= 0.

The dual tower gives

    chi(B(1))+chi(B(3))-chi(Q*(3)) >= 0.

These are valid at twist three even when K or L has no degree-minus-three
summand, because the bound on M,N is global. They retain both second determinant
defects. No generic map realizability or saturation of J's image is assumed.

### 4.4 Endpoint envelopes only after proving the corresponding defect zero

If a<=2, then s=0 and K/M=A(-2). The actual derivative of M factors through
A(-4). Since maxdeg M<=-4, the strict-top lemma gives H0(M^-(4))=0 and hence
an injection H0(M(4)) -> H0(A). Also

    chi(M(4))=chi(E(4))-chi(A(4))-chi(A(2)).

Consequently the necessary primal endpoint inequality is

    H0(A)+chi(A(2))+chi(A(4))-chi(E(4)) >= 0.

It is applied only when a<=2. Dually, when a>=0, s'=0 and the valid inequality is

    H0(B)+chi(B(2))+chi(B(4))-chi(Q*(4)) >= 0.

No endpoint derivative rank is assumed in either injection.

## 5. Exact finite certificate and conclusion

verify_direct22_cover.py defines the abstract binary-icosahedral character table
over Q(sqrt(5)), verifies orthonormality of all nine irreducibles, and obtains
symmetric powers by the exact recurrence Sym^(n+1)W=W Sym^nW-Sym^(n-1)W.
It checks each source against both its rank/degree and the actual Euler
presentation. It then implements exactly the complete domain and necessary
filters of Sections 3–4, without importing a previous proof script or data file.

The surviving SET is compared with the three fully specified ordered pairs
in the statement, not with a numerical count. Thus the finite calculation is a
certificate of necessary coverage, not an inference from a historical output
size. RESULT.json records those pairs explicitly.

Their a values are 0,2,2. Accordingly both bounds 2a+4 and 8-2a are strictly
below 12, so both second determinant defects vanish for all three pairs.
All hypotheses of the terminal three-pair exclusion are now supplied directly.

Normal Python and python -O produce byte-identical output. Seven counterfactual
controls detect omission of the H1 quotient constraint, reappearance of the
seven-W and double-octic obstructions without it, omission of endpoint filters,
the wrong cotangent twist, a missing terminal pair, and interchange of W and W'.
An independent wider-window control [-10,26] gives the same final set.

The arithmetic certificate verifies the finite character and degree statements.
The geometric necessity, saturation, fixed-marking transfer and positive-defect
arguments are the proofs above and the explicitly pinned source theorems.
