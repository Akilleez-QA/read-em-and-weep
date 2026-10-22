# Physical eigenframes preserve the vertex matrix filtration

## Established inputs and scope

All source files below are pinned at commit 8d8b5be4ce62c3055bb53be9e16d29cc63072f04 in research/hm/order-four-quadratic-load/ of Akilleez-QA/read-em-and-weep.

NEGATIVE-VERTEX-EVALUATION-SCALAR.md, Checked conclusions (1) and section 1, proves for physical inversion iota that

    E|L = O_L(5)_- direct-sum O_L(-2)_+,
    E=F_Q(2).

These are intrinsic eigenlines since inversion fixes L pointwise. Its proof uses the actual positive four-space H0(F(3)), the reduced jumping-line evaluation scheme, and the determinant character. This is not inferred from a stack stabilizer or from the extra Serre involution.

NO-PRESERVING-POSITIVE-CONE-EXCESS.md section 2 and VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md sections 1-2 prove that locally over every point of L the actual odd quotient generators have a regular initial cubic/quintic pair. The cubic relation line is O_L(-2), and the independent quintic relation quotient is O_L(5). No global quintic generator is supplied or needed.

We prove a missing frame-independence dependency. This note alone makes no assertion about the actual fifth-boundary value or its matrix formula.

## 1. Regular physical eigenframes exist locally along the entire vertex

Take a negative affine chart and a sufficiently small affine open in L trivializing the two eigenline bundles. The base parameter is fixed by physical inversion, and the positive ordinary transverse coordinates change sign. Lift the two eigenline generators to local sections of the actual bundle on an invariant neighborhood (or to its formal completion). Replace a lift v of character epsilon by (v+epsilon*iota(v))/2. This retains its restriction to L and gives an eigenvector section. The resulting two sections form a frame near L by invertibility of their determinant modulo the vertex ideal. The same argument works on every finite ambient thickening of Q.

Order the frame with the O(5) eigenline first. Its compatibility with the usual cubic-first section convention follows from the rank-two Koszul description: the cubic generator of the quotient comes from the O(-2) summand, and the kernel section has coordinates (-g,f) in the quotient-generator frame. After ordering O(5) first, the section's first component starts in cubic degree and its second in quintic degree. This identification concerns the leading line only, not a splitting of formal jets.

The binary cover is used only to record degrees. Physical inversion on even functions of cover degree 2j is (-1)^j. The residual stack mu2 says only that the bundle-frame transition functions have even cover degree; the additional physical eigenframe condition determines their degrees modulo four.

## 2. Transitions and inverses preserve the weighted filtration

Write a transition matrix between two such ordered eigenframes as T. Its diagonal entries are physical-even scalar functions; its off-diagonal entries are physical-odd scalar functions because the two frame characters are opposite. Therefore their possible cover degrees are

    diagonal: 0,4,8,...;
    off-diagonal: 2,6,10,... .

Define the weight of an entry of cover degree r to be r on the diagonal, r+2 in the upper position, and r-2 in the lower position. Equivalently a homogeneous matrix of total weight d has entry degrees d,d-2,d+2. The minimum transition weights are respectively 0,4,0. Every transition consequently has nonnegative weighted order. Its inverse has the identical character pattern and regular entries, so also has nonnegative weighted order.

Matrix multiplication adds these weights: the off-diagonal shifts cancel in products contributing to diagonal entries and add correctly in the other entries. Thus conjugation by T and T inverse preserves every weighted-order submodule, in both directions. This defines a sheaf filtration on the formal endomorphism bundle along all of L. The filtration does not require a global splitting of E on a thickening, or a global homogeneous quintic generator.

In the physical-even endomorphism sector all weights are multiples of four. In particular every regular physical-even endomorphism has weight at least zero, not merely the weight-minus-two bound for an arbitrary regular endomorphism. With q assigned cover weight four, q^4 times any regular physical-even correction has total weight at least sixteen.

## 3. Intrinsic leading line and saturation

The filtration can also be recognized before imposing physical eigenframes. Any regular frame restricting to the same ordered cubic-first line on L has transition lower-left entry vanishing in the transverse ideal. On the even binary cover that entry has degree at least two; the upper entry can have degree zero. Hence its weighted order and that of its inverse are nonnegative. Such adapted frames define the same filtration. This permits comparison with regular-pair frames without asserting that those frames were initially physical eigenframes.

In every local eigenframe the associated weighted graded pieces have locally free coefficient modules on L: they are the appropriate homogeneous polynomial pieces of the transverse coordinate algebra, with the matrix shifts above. The statement is valid on Q and on each finite q-thickening, with its homogeneous relation. Therefore membership in a weighted-order submodule is saturated with respect to a nonzero base function on the integral L. A regular matrix whose forbidden low-weight coefficients vanish over C(L) has those coefficients zero everywhere. No selected source is inverted at its zeros.

This is the precise mechanism by which a generic weighted bound can be promoted, provided its generic frame is adapted to the intrinsic cubic-first line. It is not a license to transfer bounds from an arbitrary meromorphic frame.

## Limits and verification

The proof independently checks the transition and inverse inequalities and their compatibility with multiplication. It separates physical inversion from stack mu2 and from extra Serre parity. It uses no selected actual coefficient, point, derivative, matrix, rank, or large computation. It is an authored structural proof, not proof-assistant verification.

A complete fifth-norm matrix formula would additionally have to identify the relevant ambient harmonic coefficient convention, transfer its specific leading bounds through adapted regular frames, and keep the scalar norm-lift subtraction. The invariant finite scalar-jet theorem does not depend on making that further identification.
