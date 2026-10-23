# A finite global corrected-lift criterion through original order twenty-four

## Theorem

Retain the actual source2 nonzero pure-V compatible-radical hypotheses.
The quotient and original positive pencils admit a GLOBAL polynomial
obstruction recursion. Conditional on all preceding classes being zero,
the quotient order-n obstruction is a canonical equivariant sheaf map

    s_n:P O_X(-n) -> J=I_Z(6),       X=P(A), n>=3.          (1)

It compares with the original order-(n+1) obstruction by

    iota beta_(n+1)|D = -s_n L.                           (2)

This statement uses the actual pages. It is not a claim that arbitrary
maps in a Hom space are actual obstructions.

Every zero s_n admits an exact global correction update. Its raw lift
C_n of degree n-1 decomposes uniquely as

    C_n=m g_n+kappa c_n,
    deg g_n=n-2,       deg c_n=n-5.                       (3)

An earlier A-valued correction removes m g_n. The kappa term is retained;
L kappa=0 makes the next equation soluble without removing it. Thus
there is no new globalization obstruction at the first kappa degree.
All correction operators are polynomial in the three plane coordinates.

The ORIGINAL 37-by41 positive component has generic Laurent rank37
if and only if the sequential process finds a nonzero class among

    s3,s4,...,s23   (original orders4,...,24).             (4)

If the first nonzero class is s_n, its last Smith exponent is n+1.
If all these classes vanish, every maximal37-minor is identically zero,
and the generic Laurent rank is36, with kernel dimension5. The latter
conclusion follows from an order31 versus degree30 contradiction, not
from an assumption that higher obstructions automatically vanish.

In particular, after R=s3=0 and the fifth class s4=0, the original sixth
has the genuine global target Hom_G(P,H0(J(5))) of dimension3, with
five quartic lifts modulo two m gauges and no equivariant kappa gauge.
The first possible equivariant kappa gauge occurs at quotient order8,
original order9. None of these actual classes is evaluated here.

This is a finite conditional algorithm using the ACTUAL maps, not a
source occurrence test already run, not a full-adjoint conclusion, and
not a reintroduction of the excluded endpoint-nine branch.

## 1. Exact inputs and fixed actual maps

INPUTS.json retains four immutable proofs:

- PR1019 at3fb2475ffb275c5789acbaa8f9f84ed272713785: the canonical h,
  original second map, and exact nonzero hT channel on the canonical A.
- PR1025 at09f1377f83b027ca27eea0b3a9f40a1b92c6c466: the actual quotient,
  its endpoint maps, quadratic third lift, J resolution and comparison.
- PR1104 at287a94911cdfec629529490e5c1642ddbe610b31: the actual next
  corrected page, cubic gauge and original-fifth comparison.
- PR1103 at0c2da01cfa9440d25b38360a5742ee8b32f20d0f: every original
  maximal37-minor has degree at most30 in the pencil variable.

Write q=Q:N2->M4, T=T_a, I2=D, I4=P, and identify the coherent actual
image map T|I2 with L_a. The canonical A is the A summand of ker q.
Denote its inclusion by a_A:A->N2. The canonical s:P->P_h subset N2
satisfies qs=i_P, where i_P:I4->M4 is the actual inclusion. The fixed
identifications suppress i_P when convenient. The actual identities are

    hq=j2, qh=j4, j4T=Tj2, ker j4=im q,
    j2 a_A=0,       hT a_A=mu m, mu nonzero.              (5)

Here m_a(x)=a x:A->D. The scalar mu is never evaluated.
First-symbol vanishing puts T a_A in im q. Choose a fixed equivariant
linear inverse G on im q and set

    u_A(a)=-G T_a a_A.

Then the TWO simultaneous actual identities are

    q u_A=-T a_A,       j2 u_A=-mu m.                     (6)

The second follows by applying h to the first. This is the exact gauge
action needed below, rather than a dimension-based assertion that some
A correction ought to remove a lift.

The target has the exact global resolution

    0 -> A O(-2) plus O(-5) --(m,kappa)--> D O(-1)
      --[L]--> J -> 0,                                  (7)

where the first map is injective, L kappa=0, and J is torsion-free.
The second page B=-mu Lm is SHEAF-injective on A, and the original
first and third symbols vanish. Quotient source after the second page
is P; original source after it is D. The target remains coker B while
all successive higher classes vanish. These are sheaf statements, not
claims about extra specialized A kernels at rank-drop points.

## 2. Actual correction strings and canonical obstructions

The base construction of PR1025 supplies equivariant polynomial maps
x_i:P->N2, homogeneous of degree i in a, for i=0,1,2, such that

    x0=s,      qx0=i_P,
    qx_i=-T x_(i-1)   for i>=1.                          (8)

Their quotient classes in U=M/im j are the quotient correction string.
Suppose inductively that (8) has been constructed through x_(n-1),
with every previous s_r, 3<=r<n, zero. Define

    C_n=j2 x_(n-1):P->I2,
    s_n=[L C_n] in J.                                   (9)

C_n has degree n-1. The endpoint identity gives

    j4 T x_(n-1)=L C_n.                                 (10)

It identifies (9) with the actual quotient order-n obstruction, not
with an arbitrary chosen representative. The factorization through J
is global at the representative level. Standard lift-string subtraction
shows correction-choice independence: differences in P contribute earlier
quotient symbols, all zero; differences in A contribute the image B.
Hence s_n is the canonical page class in coker B, and thus in its
subsheaf J. The source is still P because B is sheaf-injective on A.

For the original comparison, substitute p=L_a d in the string and use
T_a d=i_P L_a d. The successive original source corrections are

    d,-x0(Ld),-x1(Ld),...,-x_(n-1)(Ld).

The q equations cancel all terms through degree n. The next obstruction
is represented by -T x_(n-1)(Ld). Applying j4, the endpoint identification
and (10) gives exactly (2), modulo the surviving target image im B.
This proves the sign and index shift at every stage. Since L is
generically onto and J torsion-free, (2) is identically zero if and only
if s_n=0. Nonzero s_n is therefore also nonzero at the generic direction.

## 3. Global gauge cancellation and continuation

Assume s_n=0. By (7), the global polynomial C_n is in the kernel of [L].
Twisting (7) by n and taking sections gives the unique decomposition
(3). There are no local denominators: the kernel is the actual image
of the injective map (m,kappa), so its inverse on that image is a sheaf
isomorphism, and global sections glue uniquely. Equivariance follows
from uniqueness. For negative degree the corresponding c_n is zero.

Update TWO consecutive corrections, not x_(n-1) in isolation:

    x'_(n-2)=x_(n-2)+(1/mu) a_A g_n,
    x'_(n-1)=x_(n-1)+(1/mu) u_A g_n.                     (11)

All earlier corrections remain unchanged. Degrees match. Since q a_A=0,
the earlier q equation is unchanged. The first identity in (6) makes
the next q equation precisely qx'_(n-1)=-T x'_(n-2). Thus (11) preserves
the full already-constructed string. The second identity in (6) gives

    j2 x'_(n-1)=C_n-m g_n=kappa c_n.                     (12)

The previous j2 image is unchanged because j2 a_A=0. Importantly, (12)
is NOT asserted zero at degrees permitting a kappa family. Instead,

    j4 T x'_(n-1)=L kappa c_n=0.

By ker j4=im q, the next polynomial equation is soluble. Define

    x_n=-G T x'_(n-1).                                  (13)

A fixed linear inverse suffices, so the degree-n map is global and
polynomial in a. Equations (11)-(13) prove the induction at every order.
They keep all retained kappa remainders inside the actual strings; no
higher-stage scalar or syzygy is silently set to zero.

For n=4 this is the specific next step after PR1104: change x2 by the
quadratic A gauge and x3 by its first correction, then construct x4.
This globalizes s5 and the original sixth. The initial n=3 case has
no equivariant m or kappa ambiguity, recovering the earlier raw-zero
quadratic argument as a special case, not as an all-orders assumption.

## 4. Sequential target dimensions and first kappa appearance

Twist (7) by n>=3. On P2, H1(O(k))=0 for every integer k. Hence there
is an exact sequence of equivariant Hom spaces

    0 -> Hom_G(P,A tensor Sym^(n-2) A)
          plus Hom_G(P,Sym^(n-5) A)
      -> Hom_G(P,D tensor Sym^(n-1) A)
      -> Hom_G(P,H0(J(n))) -> 0.                         (14)

A negative symmetric exponent means zero. These are symmetric powers
of the THREE-dimensional plane-coordinate A, not binary powers of W.

For reproducibility, the class character of Sym^k A is generated by

    sum_k chi(Sym^k A)(g) z^k
       =1/(1-chi_A(g)z+chi_A(g)z^2-z^3).

This uses Lambda2 A=A and determinant A=1. Pairing (14) with the exact
binary-icosahedral class table gives the lift, m, kappa and target counts
for n=3,...,23 in GATE-TABLE.json and RESULT.json. The verifier separately
reconstructs the same characters by Newton power sums on every class.
This is an exact character/Hilbert-series computation, not interpolation
from selected directions.

In particular the first rows (n; lift,m,kappa,target) are

    3: 2,0,0,2
    4: 3,1,0,2
    5: 5,2,0,3
    6: 7,3,0,4
    7: 9,4,0,5
    8: 12,5,1,6.

Since Sym0 A=1, Sym1 A=A, Sym2 A=1+D have no P and Sym3 A contains
P once, the first equivariant kappa gauge occurs at n=8, original
order9. These spaces are CONDITIONAL SEQUENTIAL TARGETS. They are not
independent actual coefficients, not a list of realizable gate choices,
not a parameter count for HM sources, and not completion percentages.

## 5. The finite certificate and stopping rule

At the generic direction, original elimination has33 units and three
t^2 pivots. Original first and third are zero. If s_n is the first nonzero
class in the sequence n=3,...,23, comparison (2) makes the remaining
pivot t^(n+1), so the original generic Laurent rank is37.

If every class through s23 vanishes, original orders4,...,24 all vanish.
The last pivot, if finite, would have exponent at least25. Every nonzero
maximal37-minor would then have order at least6+25=31. But PR1103 proves
that every such original minor has polynomial degree at most30, without
requiring Q to preserve the negative-module splitting. Therefore every
maximal minor is identically zero. The known33 units and three t^2 pivots
still give rank36. There is no unseen later finite pivot.

Conversely generic Laurent rank36 implies that every sequential original
obstruction vanishes generically. By (2) and torsion-freeness each s_n is
zero globally, and Sections2-3 construct the global strings. Thus the
finite criterion is an equivalence, not merely a sufficient truncation.

One can package its zero outcome as a finite exact linear coefficient
certificate: equivariant homogeneous maps x0,...,x23 with x0=s and all
actual equations (8). For d in D the polynomial truncated source

    d-sum_(i=0)^23 t^(i+1) x_i(a)(L_a d)

has image under q+tT_a equal to

    -t^25 T_a x23(a)(L_a d).

Thus its coefficients through original order24 cancel identically.
All equations are finite polynomial coefficient equations, linear in the
unknown corrections once the ACTUAL q,T,s are supplied. No such actual
coefficient data is supplied or evaluated here. Gauge updates (11) prove
that zero sequential classes admit this certificate globally; they are
not a substitute source instance.

The field-generic criterion uses the whole plane and the degree30 bound.
We do not claim that restricting a nonzero plane gate to the square
conic supplies an independent global recursion there. PR1103's sharper
square bound is separate; no unproved base-change lifting is used.

## Verification and scope

Run python verify.py and python -O verify.py to reproduce RESULT.json.
The verifier authenticates four pins; computes all twenty-one target
rows twice by exact characters; checks the simultaneous two-stage gauge
update, retained kappa remainder, complete formal cancellation through
order24, and the order31/degree30 stopping arithmetic. Written actual-map
and sheaf arguments establish transport; abstract arithmetic alone does
not identify actual coefficients. No source occurrence, mechanism,
higher symbol value, or full-adjoint invertibility is selected. No
actual HM coefficients, points, jets, or instance ranks are evaluated.
