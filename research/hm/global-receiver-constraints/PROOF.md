# Canonical receiving subbundles force actual global cohomology subbundles

Work over C with G=SL2(F5), T=P(W*), A=Sym2 W, S=Sym3 W, D=Sym4 W, V the other three-space and P the even four-space. All twists are equivariant. No actual coefficient or branch is selected.

## 1. Exact inputs and actual map

BRIDGE is PR1038 at e567a431830f6dd37fe5fd2a65e24fc1210eedb3, research/hm/global-ninth-bridge/PROOF.md. It proves the actual exact sequence

    0 -> Jg -> ker Theta -> C* O(8) -> 0,

where Jg is the global positive R1 of B(2), rank13 degree28, and C is the actual opposite bundle, rank5 degree26. The actual finite geometry selects the split subbundle

    S5=A O(4) plus W O(5) -> ker Theta.

TYPES is PR996 at54dc2b2b301f8a7e453b3101d5813c643beed71a, research/hm/opposite-second-degree-bound/PROOF.md. Its seven remaining equivariant C types, with its row labels, are

     9: O(2) plus O(12) plus V O(4)
    10: O(2) plus O(18) plus A O(2)
    14: O(2) plus W' O(5) plus W' O(7)
    15: O(2) plus P O(6)
    17: O(14) plus W O(1) plus W' O(5)
    18: O(18) plus W O(1) plus W O(3)
    20: W O(1) plus V O(8).

INPUTS.json records exact original bytes and identities. Write Z=C* O(8), and let f:S5->Z be the ACTUAL composite from BRIDGE. The new argument constrains this composite without asserting that it is an arbitrary member of its Hom space or selecting its coefficients.

## 2. Intrinsic receiver and joint kernel

For any of the seven possible Z define two canonical sheaves:

    E_S = image[Hom_G(S5,Z) tensor S5 -> Z],
    K_S = intersection of the kernels of all maps in Hom_G(S5,Z).

The first evaluation uses all equivariant channels, not a sampled map. The second is equivalently the kernel of the joint evaluation S5->Hom_G(S5,Z)* tensor Z. We prove that E_S and K_S are subbundles and determine them:

    rows9,14,15,17,20:
        E_S ≅ O(6),       K_S = W O(3) plus O(4);
    rows10,18:
        E_S ≅ O(6) plus W O(5),       K_S = O(2).

The displayed K_S inclusions are intrinsic in the selected A O(4) plus W O(5): W O(3) is the quadratic-evaluation kernel in A O(4); O(4) is the Euler kernel in W O(5); O(2) is the quadratic-tautological line in A O(4). The direct-sum notation for E_S asserts its equivariant bundle type, not a unique choice of complement.

Consequently f factors through a rank1 receiver in five rows and a rank3 receiver in the other two. The actual sheaf intersection S5 intersect Jg has rank at least4 in the five rows and rank at least2 unconditionally. Moreover

    O(2) -> Jg

is an unconditional actual subbundle selected by the finite geometry. In the five rank1-receiver rows the larger selected W O(3) plus O(4) is an actual subbundle of Jg. These are stronger assertions than the negative determinant bound, and do not choose a surviving row.

## 3. Universal evaluation sequences

The equivariant Euler and quadratic evaluation sequences, with the determinant form on W used to identify duals, give

    0 -> O(4) -> W O(5) -> O(6) -> 0,
    0 -> W O(3) -> A O(4) -> O(6) -> 0,             (1)
    0 -> O(2) -> A O(4) -> W O(5) -> 0.             (2)

For (2), dualize the untwisted quadratic evaluation and twist appropriately. Its first map is the quadratic-tautological inclusion. These are everywhere-exact universal bundle sequences, not selected parameter evaluations. The map A O(4)->O(6) vanishes on the O(2) subbundle, because Hom_G(O(2),O(6))=(Sym4 W)^G=0. Thus O(2) lies inside the W O(3) kernel in (1).

We also use

    0 -> W O(5) -> A O(6) -> O(8) -> 0,
    0 -> O(6) -> W O(7) -> O(8) -> 0.              (3)

Every map from S5 to O(8) is zero:

    Hom_G(A O(4),O(8))=Hom_G(A,Sym4 W)=0,
    Hom_G(W O(5),O(8))=Hom_G(W,Sym3 W)=0.          (4)

It follows that every S5->A O(6) map factors through the W O(5) in the first sequence (3), and every S5->W O(7) map factors through the O(6) in the second. This proves the necessary common-image assertions for ALL channels. It does not infer a common image merely from dimension or one-dimensional multiplicity.

The channels from A O(4) and W O(5) to O(6) each have dimension1 and are the onto maps in (1). The channels to W O(5) are the onto map in (2) from A O(4), and the identity from W O(5). Their spaces also have dimension1. These identities follow from W tensor W=1+A and A tensor A=1+A+D.

## 4. The five line-receiver rows

The dual targets Z for rows9,14,15 are respectively

    O(6) plus O(-4) plus V O(4),
    O(6) plus W' O(3) plus W' O(1),
    O(6) plus P O(2).

Degree and irreducible-character considerations kill every source map except those into O(6). For row9, the only extra nonnegative possibility is A O(4)->V O(4), and Hom_G(A,V)=0. The two maps in (1) are independent channels because they have different source summands. They generate the full O(6) receiver, and their joint kernel is exactly W O(3) plus O(4).

For rows17 and20 the targets are

    O(-6) plus W O(7) plus W' O(3),
    W O(7) plus V O.

All maps land in W O(7), and (3)–(4) force them into its canonical O(6) subbundle. Conversely both maps in (1), composed with that line inclusion, are allowed channels and generate the line. Their joint kernel is again W O(3) plus O(4). Thus E_S is intrinsically the channel-image line, independent of a splitting used to write Z. In fact it is the O(6) injection dual to TYPES' canonical quotient C->O(2), twisted by8.

## 5. The two rank-three receivers

For row10,

    Z=O(6) plus O(-10) plus A O(6).

The negative summand receives no map. Equations (3)–(4) constrain the A O(6) component to its W O(5) subbundle. Both pieces O(6) and W O(5) are generated by maps from S5, so their sum is exactly E_S. It is a subbundle of Z. On S5, the existence of a map equal to the identity from the W O(5) source to the W O(5) receiver forces every joint-kernel vector to have zero W component. The remaining A component lies in the kernel (2), namely O(2); (1) also kills this line. Therefore K_S is precisely that O(2).

For row18,

    Z=O(-10) plus W O(7) plus W O(5).

Again ignore the negative summand for maps from S5. Every map into W O(7) factors through its Euler O(6) subbundle, and the W O(5) target receives the maps described after (4). Thus, under any equivariant splitting of the positive-degree part, E_S is O(6) plus W O(5), and the same joint-kernel argument gives O(2).

There is no hidden canonical-complement assumption in this case. W O(7) is the maximal-slope subbundle of the positive-degree part. Two equivariant lifts of the W O(5) quotient differ by W O(5)->W O(7). By (4), such a difference factors through O(6); hence it does not change the sum of that line with the lifted W O(5). Equivalently E_S was intrinsically defined as the image of all channels. The receiver's ordinary extension of W O(5) by O(6) splits because H1(O(1))=0, but its equivariant complement need not be unique. No uniqueness is claimed.

## 6. Actual global consequences and subbundle precision

The actual f is equivariant, so it is one of the channels used to define E_S and K_S. It therefore factors through E_S and kills K_S. This proves the asserted rank bounds and inclusions into Jg via BRIDGE's actual kernel sequence.

Each claimed named subbundle remains a subbundle of Jg, not merely a locally free subsheaf. For example the quadratic-tautological O(2) is a subbundle of S5 and hence of ker Theta, since S5 is a split subbundle. It is contained in Jg, and the exact sequence

    0 -> Jg/O(2) -> (ker Theta)/O(2) -> Z -> 0

shows Jg/O(2) is locally free. The same argument applies to W O(3) plus O(4) in the five line-receiver rows. In the two rank-three rows K_S is O(2); in the other five it contains the same O(2) by Section3. Thus the O(2) inclusion is unconditional and independent of the actual row.

As a separate character check of this unconditional conclusion, the seven types all satisfy Hom_G(C,O(6))=0. Therefore Hom_G(O(2),C*O(8))=0, so the selected O(2) must be killed by f. This agrees with, but is not a substitute for, the explicit subbundle and channel-image constructions.

The sheaf intersection S5 intersect Jg is saturated in S5, because its quotient is the torsion-free image sheaf of f on a smooth curve. Its rank is at least5-rank(E_S), giving the stated bounds. This does not assert that its fiber is every pointwise kernel at a jumping point, nor that the actual map has the maximal possible receiver rank.

In the five line-receiver rows there is a sharper degree statement without choosing a coefficient. Every nonzero channel from either source summand to O(6) is onto by (1). Therefore a nonzero f is onto E_S on every fiber: the two source summands are independent, so a nonzero component suffices. Its kernel intersection has rank4 and degree22-6=16. If f is zero the intersection is all S5, of rank5 degree22. The intersection is also a subbundle of Jg, since Jg modulo it is the image sheaf of Jg in (ker Theta)/S5 and hence torsion-free. These statements do not impose maximal rank in the two rank-three receiver rows.

## 7. Contribution and limits

The theorem provides a canonical rank1-or-rank3 target reduction for the actual finite/global comparison and forces a named positive line subbundle in actual global cohomology without selecting any coefficient. Five possible rows force a still larger named global subbundle. It upgrades a determinant obstruction to common-image and joint-kernel constraints using universal evaluation geometry.

No surviving opposite type is newly selected or excluded; no individual coefficient is declared nonzero, and no rank equality for the actual map is assumed. The global Jg remains distinct from the rank13 residual bundle in ker Theta. No source/catalogue occurrence, top obstruction, vertex scalar or secondary torsion alternative is determined. No selected actual HM/source parameter, point, coefficient, derivative, jet, matrix, instance rank or large scan is used.
