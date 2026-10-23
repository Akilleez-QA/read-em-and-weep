# Type II source126: four joint-annihilator footprints and a forced internal first symbol

## Result and scope

Assume an actual source126 Type II occurrence with the exact negative-pencil
interfaces of PR856/858/862. Let J be its two-dimensional square-zero radical,
and Q:N2→N4 the canonical invariant positive-coordinate product. Suppose the
WHOLE J is Q-compatible. Let U=Ann_J N2 and Z=Ann_J N4. Define r as the rank
of the joint P-row map J→Hom_G(3P,P). Then r≥1 even without Q
compatibility. Under full-J compatibility,

    U=A+2V+(2+epsilon)P+(2+d)D,
    Z=2V+(4-r)P+2D,                                           (1)

where the only possible triples are

    (r,epsilon,d)=(1,0,0),(1,0,1),(1,1,0),(2,0,0).                           (2)

The restricted Q has kernel A+D and cokernel

    (2-r-epsilon)P+(1-d)D.                                   (3)

The actual induced quotient Q:N2/U→N4/Z has

    kernel (1-d)D,    cokernel (r+epsilon-1)P.                 (4)

For d=1 the quotient is invertible and can be removed by a filtered
formal chain contraction, retaining the actual Bocksteins on U→Z.
For d=0 it has a D kernel and cannot be discarded as acyclic.

In the two P-surplus triples (1,1,0),(2,0,0), the internal first symbol
on the unique actual A kernel,

    b:A⊗A→coker(Q|U)=D,  b(a,k)=[T_a k],                      (5)

is NONZERO. After equivariant identifications it is a nonzero scalar
multiple of ordinary binary-quadratic multiplication Sym²W⊗Sym²W→Sym⁴W.
Thus b(a,-) has rank three for every nonzero negative quadratic a.
The original first Bockstein is nevertheless zero: this entire internal
cokernel maps to zero in the original cokernel P.

No existence of any row or full-J compatibility is claimed. This is not
an exclusion of Type II, a source label or a source-dual pair. It neither
identifies an actual parameter nor evaluates an actual coefficient or
matrix. No full-module endomorphism extension is used.

## 1. Immutable interfaces and distinct Type II geometry

INPUTS.json pins nine exact public inputs in Akilleez-QA/read-em-and-weep:
PR856 cee45480686c39a321feaa77d4b669682cc71efe, PR858
d3b3134e23d0aa4c4b58fd1457f040856d2d0655, PR862
e103e25456897a1123f9636eb20080e8641ce66a, PR944
84d7c9b3ee57c0a12c9e99816ec690cd8ea7ffbc, and PR946
893e14c2aee0391cdc881679c5015a8aac48ac24; the invariant rank33 and
first-vanishing originals at eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c;
the actual second-nonvanishing original at
6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0; and PR935
a7707ba3e25592023eb69cc15686aa4ee1fdcb7c for the surjective-block comparison.
Full paths, Git blobs and SHA256 hashes are in the manifest. All their
published hypotheses remain in force.

Write G for the binary icosahedral group, A=Sym²W, D=Sym⁴W, and V,P for
the other irreducibles of dimensions three and four. The genuine constant
splitting is E=F⊕R in H=C⊕Hbar with

    F=(P+2D)O(-2), C=Hbar=A+V+P+D,
    R=X⊕Y, X=O(-8), Y=W O(-9).

In TYPE II the constant spans are span X=P+D and span Y=A+V+D.
Their common D prevents a further constant separation of R. We never
split the reconstructed residual pencil into X and Y. The actual endpoint
characters from PR944 are

    N2_F=A+2V+2P+2D,  N4_F=P+2D,
    N2_R=P+2D,       N4_R=2V+3P+D.                         (6)

Each j∈J kills F and maps R into F. It comes from an equivariant constant
map b:Hbar→C satisfying q b|R=0. On the four scalar channels A,V,P,D,
this is a two-dimensional space of two restrictions: the P channel is
nonzero on X and zero on Y; the V channel is zero on X and nonzero on Y.
In particular prescribing an A coefficient and D coefficient allows a
unique solution for P,V. There is therefore j with nonzero A coefficient.
This uses the actual restriction statements of PR856/862, not just the
dimension of J or character multiplicity.

The pinned actual invariant theorem gives

    ker Q=A+D,  im Q=2V+3P+3D,  coker Q=P.                    (7)

Hence Q is injective on the entire P-isotypical source and surjective
on the entire D-isotypical target. The fixed-pencil reconstruction is
simultaneously the actual negative linear multiplication in both arrows.
Every radical element therefore intertwines each actual negative quadratic
T_a:N2→N4, a∈Sym²W. No assertion about additional degrees is needed.

## 2. Both joint D and joint P actions are nonzero

PR946 proves the natural cohomology map

    Hom_G(R,(P+2D)O(-2))→Hom_G(H1(R),P+2D)

is an isomorphism, using Serre duality and the trivial determinant
linearization. It respects the P and 2D target factors. If the D component
of every j4 were zero, every bundle map b|R would factor through the
intrinsic P O(-2) factor of F.

The constant coefficient span of an equivariant inclusion P O(-2)→C O
is contained in an image of P⊗A. The fixed McKay identities give

    P⊗A=V+P+D,

which has no A. Indeed W⊗P=Wp+T, W⊗Wp=P, W⊗T=V+P+D and W⊗W=1+A
prove this identity by associativity. But choose b with nonzero A
coefficient as above. Since R spans Hbar, the coefficient span of b(R)
contains A. This contradiction proves nonzero joint D action.

N4_R has only ONE D copy. Consequently the common kernel of all j4 on
that D is zero. The two V copies are killed automatically, and the joint
P rows from 3P to the single P in N4_F have common-kernel multiplicity
3-r. As every j kills F, this proves the Z formula in (1). The joint row
matrix is 2×3, NOT the Type I 2×2 matrix. Its rank is basis-independent;
no numerical value is selected.

In fact r cannot be zero, independently of Q compatibility. If all joint
P rows vanish, the same natural H1 isomorphism implies that every bundle
map j:R→F factors through 2D O(-2). On the actual intrinsic subbundle
X=O(-8) of R, this restriction belongs to

    Hom_G(O(-8),2D O(-2))=(2D⊗Sym⁶W)^G=0,

since Sym⁶W=V+P has no D. Thus every constant b defining j kills X.
The ACTUAL Type II constant span of X is P+D, so all such b would have
zero D coefficient. But the independent P and V restriction channels
in Section 1 allow the D coefficient to be prescribed nonzero and solved
for P,V. This contradiction proves r≥1. This uses X as an intrinsic
bundle subobject only; it does not split a reconstructed X pencil out
of the Type II residual. The shared D support is essential to this
argument: the Type I span X=P would not give the same contradiction.

## 3. Exact enumeration of common-annihilator footprints

Since every j kills F, U contains N2_F. In its genuine residual complement
N2_R=P+2D, its common kernel is epsilon P+dD, with epsilon∈{0,1} and
initially d∈{0,1,2}. A subrepresentation of the two D copies is not a
chosen distinguished copy; d records only multiplicity. This establishes
the first formula in (1) without a false isolated-X argument.

Assume full-J compatibility. Each j preserves ker Q, and its restriction
to the multiplicity-free A+D is equivariant and square-zero, hence zero.
Thus ker Q⊂U, Q(U)⊂Z, and the exact restricted image character is

    Q(U)=2V+(2+epsilon)P+(1+d)D.                             (8)

Comparing (8) with Z gives d≤1 and epsilon≤2-r. If r=0, every j4 kills
the entire P target. Compatibility gives Q j2=0 on the P source; its
P-injectivity forces every j2 there to vanish. Hence epsilon=1.

The annihilator is a genuine negative subpencil: j4T_a x=T_a j2x=0 for
x∈U, so T_a(U)⊂Z. If (8) equals Z, Q|U is onto. A right inverse s yields,
for any vector k in the unique actual A kernel summand, a correction u=-sT_a k in U
with Qu=-T_a k and [T_a u]=0 in the original cokernel.
The canonical correction in the pinned first-vanishing theorem is
u0=-h zeta_a for k=h xi and a xi=q0 zeta_a. Since u-u0∈ker Q and the
ORIGINAL first Bockstein vanishes globally, [T_a(u-u0)]=0. Thus this
would kill the SAME original second A-to-P family, contradicting its
pinned geometric nonvanishing theorem.

Surjectivity occurs precisely when d=1 and epsilon=2-r. The allowed
r=0,epsilon=1 is not surjective. Removing (1,1,1) and (2,0,1) leaves
six elementary triples: (0,1,0),(0,1,1) and the four in (2). Section 2
independently excludes both r=0 triples. The four remaining triples
are exactly (2). Subtracting (8) from Z gives (3).
This is a necessary finite footprint list, not four claimed realizations.

## 4. The actual quotient map, not only quotient characters

The quotient endpoint characters are

    N2/U=(1-epsilon)P+(2-d)D,  N4/Z=rP+D.                   (9)

If a P-source vector x satisfies Qx∈Z, then Q j2x=j4Qx=0 for every j.
By P-injectivity of Q, j2x=0 for every j, so x∈U. Therefore the quotient
P map is injective, with rank multiplicity 1-epsilon and cokernel
multiplicity r+epsilon-1. Surjectivity of the full D map in (7) implies
surjectivity onto the quotient's single D, so its kernel multiplicity
is (2-d)-1=1-d. Equivariance gives no cross terms. This proves (4)
for the ACTUAL quotient map, not a merely possible character map.

When d=1, the only row is (1,0,1); both quotient kernel and
cokernel vanish. For each a, the quotient of Q+tT_a is invertible over
C[[t]] because its constant term is invertible. Choose constant
complements and write the differential as M=[[A,C],[0,B]]. Its inclusion
of U→Z has retraction

    p0(x,y)=x, p1(z,w)=z-C B^(-1)w,

and degree-minus-one homotopy h(z,w)=(0,B^(-1)w). Direct calculation gives
p1M=A p0, pi=1, hM=1-i0p0 and Mh=1-i1p1. These maps preserve all t-adic
filtrations, since B^(-1) has no negative powers. This is a filtered chain
homotopy equivalence retaining the actual Bocksteins, not generic
surjectivity of the original pencil.

When d=0, quotient kernel D is nonzero. The preceding contraction has
no invertible B(0) and is NOT asserted. The six-term exact sequence of
the subcomplex, full complex and quotient makes the distinction precise:

    0→D→coker(Q|U)→P→(r+epsilon-1)P→0,                    (10)

because the restricted and full kernels are the same A+D, with identity
inclusion. The initial D is the quotient kernel; its connecting map is
injective. In the sole d=0 row with r+epsilon=1, (10) reads
0→D→D+P→P→0. In the two rows with r+epsilon=2, it reads
0→D→D→P→P→0: the D→D is an isomorphism, the D→P is zero, and P→P is
an isomorphism. These are exact subquotient statements, not a preferred
splitting or a replacement of the obstruction problem.

## 5. A forced nonzero internal first symbol in the P-surplus rows

Now take (r,epsilon,d)=(1,1,0) or (2,0,0). The internal cokernel is D,
and its natural map to the original cokernel P is zero by (10).
For k in the unique actual A⊂ker Q⊂U define b(a,k)=[T_a k] internally.
This is bilinear and G-equivariant, as the annihilator subpencil and Q
are equivariant.

Suppose b were zero identically. For every a and k in A we could solve
Qu=-T_a k with u in U. Then T_a u∈Z. Its class in the original cokernel
is zero, because Z/Q(U)=D maps to zero there. Comparing u with the
canonical u0=-h zeta_a using global original first vanishing, exactly as
in Section 3, would make the original second symbol zero on all A for
all a. That contradicts the actual nonzero second-Bockstein theorem.
Thus b is nonzero.

The standard binary-form decomposition restricts to

    A⊗A=1+A+D

with three pairwise nonisomorphic irreducibles. Consequently
Hom_G(A⊗A,D) is one-dimensional. Ordinary multiplication of binary
quadratics is a nonzero member. After any equivariant identification
of the unique actual A kernel with A and the internal cokernel with D,
b is a nonzero scalar multiple of that multiplication. For every
nonzero a, multiplication k↦ak is injective in the polynomial domain
C[x,y]. Its rank is exactly dim A=3, uniformly, without evaluating a
selected quadratic or any actual coefficient.

There is no contradiction with original first vanishing: inclusion kills
this internal D cokernel. Instead (10) locates the required first
correction outside U, in the non-acyclic quotient kernel D. This is why
one must not transfer the d=1 acyclic reduction into these branches.
The internal symbol on the D part of the kernel is not computed here.

## 6. Evidence and precise remaining questions

verify.py exhausts the elementary triples, checks the six preliminary and four surviving footprints,
constructs synthetic constituentwise quotient diagrams with the stated
kernel/cokernel maps, and verifies the universal binary-quadratic
multiplication rank certificate. Inputs are authenticated by exact hashes.
These bounded diagnostics do not establish the imported geometry or
construct an actual Type II occurrence.

Still open are which, if any, of the four footprints can occur, whether
full-J compatibility is possible at all in Type II, and whether the
internal symbol or quotient D kernel supplies a further obstruction.
No original source-dual frontier count changes. No actual coefficient,
selected parameter, or instance matrix is evaluated.
