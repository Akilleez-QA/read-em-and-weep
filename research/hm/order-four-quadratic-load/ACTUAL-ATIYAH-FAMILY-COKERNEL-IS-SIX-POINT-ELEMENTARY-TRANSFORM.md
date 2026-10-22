# The actual Atiyah-family cokernel is a six-point elementary transform

## Statement and input boundary

Let S=P(A), and let D be its six reduced C5-axis points. Use the actual residue comparison to identify the positive nine-space with V tensor A. The actual family map is

    K:D5 O_S(-1) -> (V tensor A) O_S.

Its cokernel E is a rank-four torsion-free sheaf, not a vector bundle at D. There are exact sequences

    0 -> I_D(2) -> E -> V O_S(1) -> 0,             (1)
    0 -> E -> O_S(2) + V O_S(1) -> O_D(2) -> 0.  (2)

Sequence (1) is the unique nonzero equivariant extension up to scalar automorphisms of its end terms. Its middle term has c1=5 and c2=15. The double dual in (2) has its unique equivariant splitting compatible with those end terms.

These are deductions about the actual lower Atiyah factor. They do not compute the absolute secondary operation, the third Bockstein, or the original proof-repair obstruction.

The inputs are the [actual residue comparison](https://github.com/Akilleez-QA/read-em-and-weep/blob/b2500656b997a0a846477fdd527fc821fa681f7f/research/hm/order-four-quadratic-load/ACTUAL-POSITIVE-ATIYAH-MULTIPLICATION-SURJECTS-ONTO-NINE-SPACE.md) and the [six-axis scheme theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/b30db22c6f4e5a972e43aca4262937753f3c4ba9/research/hm/order-four-quadratic-load/POSITIVE-ATIYAH-SIX-AXIS-LOCUS-AND-UNIFORM-SQUARE-INJECTIVITY.md). In particular K is not replaced here by an arbitrary equivariant map of the same dimensions.

## 1. The inner rank-one cokernel

The image of ad_a on A=sl2 is the Killing-orthogonal plane to a. On S these planes form the Euler kernel Omega_S^1(1), so K factors as

    D5 O(-1) -> V tensor Omega_S^1(1) -> (V tensor A) O.

The second arrow is a subbundle inclusion with quotient V O(1). Let F be the first cokernel. Its presentation is injective as a map of sheaves because it is generically injective, and its source is locally free. It is locally free of rank one off the six points. At those points a length-one locally free resolution gives depth at least one over the regular local surface ring. Consequently F has no zero-dimensional torsion. It cannot have divisorial torsion either, since its nonfree support is finite. Thus F is rank-one torsion-free.

Write H=c1(O(1)). The Euler sequence and the presentation give

    ch(F)=3(3-exp(H))-5 exp(-H)=1+2H-4H^2.

Hence F**=O(2), and F=I_T(2) for a zero-dimensional scheme T of length six. At each point of D the inner matrix has rank four, rather than five. F cannot be free there: if it were free of rank one, the local presentation would split and the first map would have full rank on the fiber. Thus T contains all six distinct points of D in its support. Their total length is already six, so T=D scheme-theoretically and is reduced. This proves F=I_D(2), including the scheme structure rather than merely support.

Taking the outer quotient now gives (1).

## 2. The extension class is genuinely nonzero

The six-axis Hilbert--Burch resolution is

    0 -> V O(-4) -> P4 O(-3) -> I_D -> 0.

After twisting by one, the cohomology of O(-3) and O(-2) on P2 yields

    H0(I_D(1))=0,    H1(I_D(1))=V.

The identification H2(O(-3))=C has no omitted finite G-character because G is perfect. Since V is self-dual and irreducible,

    Ext^1_G(V O(1),I_D(2))
      = (V* tensor H1(I_D(1)))^G = C.

It remains essential to distinguish zero from nonzero in this allowed channel. The actual presentation, twisted by minus one, is

    0 -> D5 O(-2) -> (V tensor A) O(-1) -> E(-1) -> 0.

All H0 terms on the left and H1(O(-2)) vanish, so H0(E(-1))=0. A split version of (1) would instead contain the nonzero section space V from its V O summand after the same twist. Therefore the actual extension class is nonzero. All nonzero elements of this one-dimensional equivariant Ext space are related by scalar automorphisms of the end terms. This proves the claimed uniqueness at the isomorphism-class level, not a claimed numerical normalization of an Ext class.

## 3. Double dual and elementary transform

Locally (1) splits because its quotient is locally free. Double dualizing therefore gives an exact sequence

    0 -> O(2) -> E** -> V O(1) -> 0,

and the comparison quotient is E**/E=O_D(2). The double-dual extension splits since

    Ext^1(V O(1),O(2))=V* tensor H1(O(1))=0.

An equivariant splitting exists by averaging over the finite group. It is unique because

    Hom_G(V O(1),O(2))=(V* tensor A*)^G=0

for the two distinct irreducible three-spaces V and A. This proves (2). In particular it would be incorrect to replace E itself by this split vector bundle: the length-six elementary modification and the nonsplit sequence (1) are actual data.

Finally ch(E)=9-5 exp(-H)=4+5H-(5/2)H^2, whence c1(E)=5H and c2(E)=15H^2. Restriction away from D is a vector bundle, but no consequence for the separate higher-obstruction map is asserted.

## Verification

Run verify_atiyah_family_elementary_transform.py. It checks the representation multiplicities, formal Chern characters, Hilbert polynomial length, and extension dimensions used above. The torsion-free, nonzero-extension, and double-dual arguments are the geometric proof. No actual coefficients, matrices, rank evaluations, or parameter scans are used.
