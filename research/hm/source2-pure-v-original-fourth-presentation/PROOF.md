# Mixed-degree presentation and unique equivariant kernel extension on ell3

## Theorem and boundary

Assume a nonzero universal gate on ell3. The cubic Hilbert-Burch theorem identifies K_F=A O(-3), with its actual inclusion S. Twist it by one, so S:A O(-2)->P O(1). Retain the exact normalized kernel bridge, with C_L=coker(D O->P O(1)), E=ker(A O(-2)->C_L), and line kernel O(-4).

## 1. Immutable inputs and actual maps

INPUTS.json pins PR1053 at 9658196f793afda6767565307ebc818ddfe341a5,
including its proof, complete S.json cubic syzygy matrix and unchanged
model.py, and PR1049 at 6210a276622e15c6977b8070bc1fd12744fe2f07.
All four files are retained unchanged and authenticated by Git blob hash
and SHA-256. The model supplies the exact matrix L; the cubic matrix S
is the actual equivariant Hilbert-Burch inclusion, not a rank-three matrix
inferred from matching Chern classes. Its source is the abstract syzygy
space A in the basis recorded by S.json; the source action is correspondingly
the action identified in PR1053, not an unverified coordinate identification
with the standard monomial basis of Sym2 W.

These are the determinant-target kernel bundles of the surviving
original-fourth D summand. No claim concerns specialized additional
A-kernel classes, an actual coefficient choice or actual obstruction value.

## 2. The surjective mixed-degree bundle presentation

The map [L,-S]:D O plus A O(-2)->P O(1) is surjective as a sheaf, hence fiberwise onto because its target is locally free. Indeed its cokernel is the cokernel of A O(-2)->C_L, which is zero by the kernel bridge. Its kernel identifies canonically with K_H: projection sends (d,a) with Ld=Sa to d, necessarily in K_H. Conversely every d in K_H has a unique a because S identifies A O(-2) with ker F(1). Therefore

0 -> K_H -> D O plus A O(-2) -> P O(1) -> 0.

This is a genuine bundle presentation, not a Chern identity or a generic presentation requiring saturation.

The entries in the L block are linear; those in the S block are cubic.
These degrees agree with D O plus A O(-2) mapping to P O(1).
One does not infer surjectivity from a nonzero maximal minor or from
having matching Chern data. Surjectivity at the rank-drop orbit follows
from the actual induced quotient map in PR1049.

For an explicit local verification, in the compatible normal form of
PR1049 write S=(S0,0;0,1), where S0 is a three-by-two matrix of local
syzygies. Then [L,-S] has its first three source columns equal to the
first three coordinate vectors of R^4, and its last source column equal
to minus the fourth coordinate vector. These four columns give a right
inverse over the entire local ring, including the closed point. This
checks fiberwise surjectivity without any point evaluation of the actual
universal matrices.

## 3. Global Ext reduction

The same data determine the equivariant extension class. Apply global Ext(-,O(-4)) to 0->E->A O(-2)->C_L->0. The outer groups Ext1(A O(-2),O(-4)) and Ext2(A O(-2),O(-4)) vanish, because H1(O(-2))=H2(O(-2))=0. Hence Ext1(E,O(-4)) is canonically Ext2(C_L,O(-4)), equivariantly.

For a finite group in characteristic zero, taking invariants is exact.
Thus the invariant part of this global Ext is the Ext group in the
category of equivariant coherent sheaves. All representations here factor
through the projective group A5; the binary center acts trivially.

## 4. Full stabilizer characters and local duality

At an order-three axis its full projective stabilizer is S3. The axis line has the sign character: its cyclic order-three subgroup fixes the vector, while a half-turn reversing the axis acts by minus one. Thus O(-1) has sign, O(-2) and O(-4) are trivial there. The rotation module A restricts as sign plus standard. The one-dimensional fiber of C_L is a quotient of A O(-2), by the actual surjection from the bridge. This module has no trivial summand, so that quotient must be sign. This derives the cokernel character from the actual map, not a guessed linearization.

The tangent representation of the plane is Hom(axis,A/axis)=standard tensor sign, which has determinant sign. Local Koszul duality therefore gives Ext2_R(k_sign,O(-4)) with character sign-dual times trivial times determinant(tangent)=trivial. The local-to-global Ext spectral sequence has only the Ext2 skyscraper term for C_L. Thus Ext2(C_L,O(-4)) is the representation induced from the trivial stabilizer character on the transitive orbit of ten axes. Its invariant subspace has dimension one by Frobenius reciprocity.

## 5. Uniqueness and original-fourth consequences

Consequently Ext1_G(E,O(-4)) has dimension one. The actual kernel bridge is nonzero, since it is locally the nonsplit Koszul extension at every axis. Thus it is, up to nonzero scalar and rescaling the line injection, the unique nonzero equivariant extension with these endpoints. This does not claim that all nonequivariant extensions are the same: their space has dimension ten.

The rank-four middle bundle is not inferred to split. Its mixed-degree presentation has c1=-10 and c2=46, consistent with the prior kernel theorem. These statements remain conditional on the unknown nonzero gate lying on ell3. No actual source coefficient is identified.


## Reproduction and novelty

Run `python verify.py` and `python -O verify.py`; both reproduce RESULT.json
identically. The verifier authenticates all four public files, reads the
actual mixed-degree blocks, checks a formal local right inverse and kernel
comparison, checks the full S3 relations and line/tangent characters, and
checks local Ext/Frobenius multiplicities and Chern data. The local group
matrices are abstract stabilizer normal forms, not a selected actual
quadratic direction or source evaluation.

The new claims are the surjective mixed-degree presentation of the actual
original-fourth kernel and the one-dimensional equivariant extension space
with its unique nonzero class up to scalar. The preceding Hilbert-Burch
splitting, component schemes and kernel Chern values are inputs or
consistency checks, not new classifications.
