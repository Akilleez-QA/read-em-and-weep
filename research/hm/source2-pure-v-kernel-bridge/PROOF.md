# The kernel-bundle bridge and its ten elementary-modification points

## Theorem and scope

Fix any nonzero member of the universal conditional pure-V gate. Let B be
its finite component base scheme, b=length(B), and use the normalized maps

    F:P O -> I_B(9),       H:D O -> I_B(10),
    L:D O -> P O(1),       H=F(1)L.

The maps to their indicated image ideals are surjective. Put K_F=ker F
and K_H=ker H. They are vector bundles of ranks three and four. There is
an exact sequence of actual kernel sheaves

    0 -> O(-4) -> K_H -> K_F(1) -> C_L -> 0,                (1)

where C_L=coker L has length ten, one at each order-three axis. The map
K_F(1)->C_L is surjective at every one of these points, for every nonzero
coefficient direction, including ell3.

Writing E=ker(K_F(1)->C_L), one has

    0 -> O(-4) -> K_H -> E -> 0,
    0 -> E -> K_F(1) -> C_L -> 0.                          (2)

E is torsion-free of rank three, but is NOT locally free at any of the
ten axes. Its double dual is K_F(1); its double-dual defect has length ten.
Locally at every such axis the first sequence in (2) is a direct sum of
a free rank-two identity and the nontrivial Koszul extension

    0 -> R -> R^2 -> m -> 0.

The exact Chern data, with h the plane hyperplane class, are

    rank(K_F)=3,  c1(K_F)=-9h,   c2(K_F)=(81-b)h^2;
    rank(K_H)=4,  c1(K_H)=-10h,  c2(K_H)=(100-b)h^2;
    rank(E)=3,    c1(E)=-6h,     c2(E)=(76-b)h^2.

In particular the length-ten modification cannot be omitted from the
kernel comparison. No actual gate coefficient or source occurrence is
selected. This concerns the surviving original-fourth D summand through
its determinant target, not specialized additional A-kernel classes.

## 1. Immutable inputs and twists

INPUTS.json pins two public proofs by commit, path, Git blob and SHA-256:

- PR1046 at 56c1ee605ba1886d7e837d6a686b3e8a00af1dc9 proves equality of the
  projective component ideals of the nonic row F and the degree-ten row
  H=FL, including all ten rank-drop axes. At each such axis their common
  ideal is m off ell3 and m^2 on ell3.
- PR1025 at 09f1377f83b027ca27eea0b3a9f40a1b92c6c466 supplies the actual
  original-fourth comparison and the universal sequence for L. Twisting
  its sequence by one gives

      0 -> O(-4) -> D O --L--> P O(1) -> C_L -> 0.

  Here C_L denotes the twisted finite cokernel; its length and reduced
  support remain ten. We do not silently identify different equivariant
  twists of that finite sheaf.

The nonic determinant row is a map P O->O(9), with image I_B(9).
Its twist F(1) maps P O(1) onto I_B(10). PR1046 proves that H has that
same image ideal, so the right vertical map in the diagram below is the
identity on I_B(10). This is stronger than generic equality of images.

PR1025 identifies the original fourth on surviving D, after its endpoint
identification, with minus the quotient-third composed with L. The
injective determinant map to the target line bundle then gives -H.
An overall sign does not change the kernels. No fiberwise injectivity of
a singular ideal-sheaf target is presumed.

## 2. Both kernel sheaves are vector bundles

At a point of the smooth plane, the local ring R is regular of dimension
at most two. Off B the ideal I_B is free. At a point of B, R/I_B has finite
length and I_B has projective dimension one: this follows from depth one
for I_B and the Auslander-Buchsbaum formula, or from its length-two ideal
resolution on a regular surface.

For a surjection from a finite free module to I_B, its kernel is therefore
projective and hence free over the local ring. Applying this to F and H
proves that K_F and K_H are locally free everywhere. Their ranks are
four minus one and five minus one. This argument does not assume that
B is reduced or locally a complete intersection; it covers m^2 and m^3
as well as the other established base schemes.

## 3. The exact snake sequence

Use the commutative diagram of short exact sequences

    0 -> K_H    -> D O    -> I_B(10) -> 0
         |          L          identity
    0 -> K_F(1) -> P O(1) -> I_B(10) -> 0.

The snake lemma gives precisely (1), since ker L=O(-4) and coker L=C_L.
In particular it proves surjectivity K_F(1)->C_L, not just an equality
of ranks or K-theory classes. This is an actual map induced by the
inclusion K_F(1) into P O(1) and the quotient to C_L.

Its kernel E is a subsheaf of the bundle K_F(1), so is torsion-free.
Away from the ten axes it equals that bundle. The local analysis below
identifies its singularities, rather than presuming it is a bundle.

## 4. Compatible local normal forms

Work at one order-three axis and trivialize all line bundles. This is a
local algebra argument at every point of the orbit, not an evaluation of
an actual source or a chosen quadratic direction. Let R be its regular
local ring with parameters u,v and maximal ideal m=(u,v). The reduced
rank-drop scheme of L gives, by invertible row and column operations,

    L = diag(I3,(u,v)) : R^5 -> R^4.

Write F=(g1,g2,g3,f4) and J=(g1,g2,g3). Then

    (F)=J+(f4),       (FL)=J+m(f4).

PR1046 says these ideals are equal. The cyclic finitely generated module
(J+(f4))/J consequently equals m times itself. Nakayama gives f4 in J.
Choose regular a1,a2,a3 with f4=a1g1+a2g2+a3g3.

Replace the fourth target basis vector by e4-sum ai ei. In that basis
F=(g1,g2,g3,0), while L acquires top entries u ai and v ai in its last
two columns. Subtract those multiples of its first three source columns
to restore the displayed normal form of L. These are invertible local
basis changes compatible with both maps. They yield simultaneously

    F=(g1,g2,g3,0),        H=(g1,g2,g3,0,0),
    L=diag(I3,(u,v)).                                     (3)

Let S=ker(R^3 --g--> I_B). The same projective-dimension argument proves
that S is free of rank two. Thus (3) identifies the kernel comparison as

    K_H = S + R^2  ->  K_F(1) = S + R,
    (s,a,b)       |-> (s,ua+vb).

The induced map to C_L=k is (s,c)|->c modulo m. It is visibly surjective,
with kernel E=S+m, locally isomorphic to R^2 plus m. Since m needs two
generators but has rank one, it is not free. Thus E is singular at every
axis, and nowhere else. The first sequence in (2) becomes

    1 |-> (0,-v,u),       (s,a,b) |-> (s,ua+vb).

Exactness is the regular-sequence Koszul calculation. The extension of m
by R is nontrivial: a split extension would make m a direct summand of
R^2 and hence free, a contradiction. Equivalently it represents a nonzero
class in Ext1_R(m,R)=k. This conclusion is independent of the coefficient
line; there is no extra splitting direction at a C3 axis.

The inclusion O(-4)->K_H is therefore a line-sheaf injection, NOT a
subbundle inclusion at those points. Viewed as a section of K_H(4), its
component ideal is (u,v), so its zero scheme is exactly the ten reduced
axes. This is intrinsic to the kernel bridge, not a rank assertion for R.

## 5. What changes on ell3

The abstract local elementary-modification type R^2+m is uniform. The
embedding of its kernel bundles in the original free source modules does
remember the coefficient line. Let mu be the minimal number of generators
of I_B at an axis. PR1046 gives

    mu=2 off ell3,       mu=3 on ell3.

For a surjection R^n->I_B, tensoring with k shows that the image of its
kernel in k^n has dimension n-mu. Thus the fiber image of K_F in P O is
of dimension two off ell3 and one on ell3; the corresponding image of
K_H in D O is of dimension three off ell3 and two on ell3.

In (3), the last F generator is redundant and gives the direct R summand
of K_F(1)=S+R. Its map to C_L is the residue isomorphism on that summand.
The image of S in the first three source coordinates has dimension
3-mu. Consequently the map to C_L kills this (3-mu)-dimensional redundant
subspace and is surjective on the remaining one-dimensional redundant
direction. On ell3 it detects the ONLY redundant F direction; off ell3
one additional redundant direction survives in its kernel. Minimal
syzygies, whose source fiber image is zero, map to zero in C_L.

These statements concern the fibers of the indicated inclusions, not a
failure of the bundles themselves to have constant rank. They distinguish
the two cases without choosing any actual coefficient pair.

## 6. Chern data and the length-ten correction

For a finite scheme of length b,

    ch(I_B(d))=1+d h+(d^2/2-b)h^2.

The two defining exact sequences therefore give the stated Chern classes
of K_F and K_H. For the rank-three twist K_F(1),

    c1=-6h,        c2=(66-b)h^2.

From 0->E->K_F(1)->C_L->0 and ch(C_L)=10h^2, one obtains

    c1(E)=-6h,     c2(E)=(76-b)h^2.

Chern classes for E here are defined by its K-class, valid for this
coherent sheaf on the smooth surface. Finally (2) gives

    c2(K_H)=c2(E)+(-4h)(-6h)=(100-b)h^2,

agreeing with its defining presentation. Omitting C_L would give an
incorrect answer smaller by ten.

Since E and K_F(1) agree off a finite set and K_F(1) is reflexive,
E**=K_F(1) canonically. Hence E**/E is exactly C_L, with length ten.
The local nontrivial extensions in (2) explain how a bundle K_H maps onto
this singular elementary modification without making E locally free.

## Verification and novelty

verify.py authenticates both public inputs, checks the compatible normal
form changes symbolically, the Koszul maps, the twist and Chern identities,
and the minimal-generator/fiber-image bookkeeping in both cases. Local
freeness, exactness and double-dual claims are proved above; the checker
does not replace them with numerical ranks or specialized examples.

The new result is the exact kernel-bundle bridge and its uniform singular
quotient, nontrivial local extension and ell3-dependent redundant-source
structure. Component-ideal equality and nonic base lengths are inputs,
not new classification claims. No actual coefficients or instances are
computed and no choice of actual gate is made.
