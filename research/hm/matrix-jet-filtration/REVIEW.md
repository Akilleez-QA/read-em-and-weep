# Independent audit of the physical matrix-jet filtration

## Verdict and exact artifact

**PASS within the stated scope.** No substantive mathematical defect was found in the filtration, parity, or saturation argument. This is an independent deductive audit, not proof-assistant certification or an evaluation of an actual HM matrix.

Reviewed artifact: `PROOF.md`.

SHA-256: `1f0b292e2aae41e406f9e6a26301afce793a2648ba8e9eb8df9c1c09aac7ecd5`.

The three cited input files were read directly at immutable commit `8d8b5be4ce62c3055bb53be9e16d29cc63072f04` of `Akilleez-QA/read-em-and-weep`, under `research/hm/order-four-quadratic-load/`:

- `NEGATIVE-VERTEX-EVALUATION-SCALAR.md`, Git blob `4d2737b94c19b84816382984db9ecb91af66ef0e`.
- `NO-PRESERVING-POSITIVE-CONE-EXCESS.md`, Git blob `2f90c2c3d816220c0ab3142c2eeb5c2d3c49b74c`.
- `VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md`, Git blob `0800677ef4177a96226f490e28d9a2ea948b7678`.

The same-commit `ACTUAL-CORRECTED-THIRD-NEIGHBORHOOD-LIFT-IS-SQUARE-ZERO.md` and `POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md` were also read to check the existing weighted convention and the distinction between physical and residual-stack parity. Their further norm or harmonic computations are not established by this review.

## 1. Exact physical center signs: checked

The pinned negative-vertex source states and proves

    F|L = O_L(3)_- direct-sum O_L(-4)_+,
    F|L(2) = O_L(5)_- direct-sum O_L(-2)_+.

Its section 1 derives the splitting from the actual reduced evaluation/minor scheme. For F(3), the image line is O(6) with positive character, because the actual four-dimensional evaluation space is positive. The determinant character on the negative line forces the quotient O(-1) to be negative. The negative character of O(-3)|L then yields the displayed signs for F; twisting by two retains them for E. Thus the proof uses the correct physical linearization, not the local stack stabilizer or extra Serre involution.

Since physical inversion fixes L pointwise, the two character eigensubbundles on L are intrinsic.

## 2. Averaged eigenframes and the Koszul ordering: checked

Locally trivialize the two eigenlines, lift their generators to the actual ambient bundle, and apply the character projectors (1 + epsilon iota)/2. Their restrictions remain the original nonzero generators. Their determinant is a unit modulo the ideal of L, so they form a local frame after shrinking, and a frame on the formal completion. The same argument works modulo every power of q. It needs only local lifting and an invariant neighborhood; it gives no global formal splitting and uses none.

The apparent swap between the quotient generators and the kernel section is necessary and correctly handled. The cubic relation is O(-2), whereas the independent quintic quotient is O(5). More explicitly, the uniform initial relation construction supplies a surjection E|L -> K3=O(-2). Its restriction from O(5) is zero, since Hom(O(5),O(-2))=0, and its O(-2) restriction is an isomorphism. Therefore the kernel is the intrinsic O(5) line. In the quotient-generator order (f,g), with orders (3,5), the Koszul kernel has coordinates (-g,f). Ordering the O(5) bundle line first swaps the coordinates and makes the section cubic-first, then quintic. Only the leading flag is identified.

This remains true for arbitrary such averaged eigenframes. A change preserving the O(5) line has lower-left entry in the transverse ideal, so it cannot introduce a cubic leading term into the second section component. Nothing here selects a global quintic lift; the pinned quintic relation extension is genuinely nonsplit.

## 3. Transition, inverse, and multiplication inequalities: checked

Ordinary scalar functions on the binary cover have even cover degree. Physical inversion acts on cover degree 2j by (-1)^j. With eigenframe characters (-,+), transition diagonals are physical-even and off-diagonals physical-odd. Thus their cover degrees are respectively 0 modulo 4 and 2 modulo 4.

For an entry in position ij write its weight as its cover degree plus c_i-c_j, where c_1=2 and c_2=0. This gives the stated shifts 0,+2,-2. The least possible weights of diagonal, upper, and lower transition entries are therefore 0,4,0. The inverse is regular and intertwines the same character actions, so it has precisely the same bounds. This does not rely on a termwise formal inverse with unjustified convergence.

For a product through index k, the shifts add as

    (c_i-c_k) + (c_k-c_j) = c_i-c_j.

Hence matrix multiplication adds lower weight bounds. Multiplication on either side by a nonnegative-weight transition preserves each filtered submodule; applying the inverse proves equality, not merely inclusion. Conjugation therefore glues the filtration.

For a regular frame preserving only the ordered cubic-first line, the lower-left coefficient vanishes on L and has cover degree at least two. Its lower weight is at least zero. The upper entry may be constant but then has weight two; diagonal entries have nonnegative weight. The inverse has the same triangular restriction on L. Thus these more general adapted frames preserve the same filtration as the physical eigenframes.

## 4. Physical-even weights and fourth corrections: checked

In an ordered physical eigenframe, an invariant endomorphism has the same diagonal/off-diagonal character pattern as a transition. After applying the shifts, every allowed weight belongs to 4Z, and the minimum is zero. In particular the otherwise possible regular lower-entry weight minus two is absent in this sector.

The homogeneous ambient quadric q has cover weight four and is physical-even. Consequently q^4 times any regular physical-even correction has weighted order at least sixteen. The statement applies to endomorphisms, and to the even twists relevant here with their standard physical local trivializations; no statement about arbitrary odd line-bundle twists is being inferred.

## 5. Saturation along the entire line: checked

The coefficient-freeness assertion can be made explicit. On a negative affine chart with base ring A, the ordinary transverse coordinates x_1,x_2,x_3 have cover weight two. The rank-three quadric equation q is a fixed homogeneous quadratic in those coordinates, independent of the base coordinate after this trivialization. The transverse associated graded scalar ring on nQ is

    A[x_1,x_2,x_3]/(q^n).

Its homogeneous pieces are A tensored with finite-dimensional complex vector spaces, hence are A-free. The case n=1 is equivalently the even binary-coordinate cone algebra. The proof does not need a nonexistent binary parametrization of a nonreduced nQ: on nQ, binary degree is only the rescaled homogeneous weight of the ordinary transverse algebra. The ambient formal case uses the unquotiented polynomial associated graded ring.

The matrix shifts merely reindex these free scalar pieces. For a fixed lower bound, only finitely many forbidden weights occur because regular matrix weights are bounded below by minus two. The quotient by the corresponding filtered submodule therefore has a finite filtration with locally free, in particular base-torsion-free, graded pieces. It is itself base-torsion-free. Thus a nonzero base function cannot annihilate a nonzero forbidden coefficient class.

A regular matrix that belongs to the weighted submodule over C(L) consequently belongs locally to it everywhere on L. This is the valid saturation argument, including every zero of any source used in a generic calculation. It does not divide by that source at its zeros.

The generic comparison has an essential hypothesis, already retained by the proof: its generic frame must be a genuine regular, invertible frame over the completed transverse algebra over C(L), and must preserve the intrinsic cubic-first line. An arbitrary frame on a transverse punctured neighborhood, or a meromorphic gauge with transverse poles, is not covered. No conclusion is inferred solely from a basis of a generic fraction field. These are scope conditions, not defects in the stated argument.

## Limits and audit discipline

The audited result establishes frame independence and saturated descent of already-proved adapted weighted bounds. It does not establish a particular actual harmonic coefficient bound, a full fifth-norm cross-term formula, or removal of the scalar norm-lift subtraction. It does not claim globally split formal jets or a global quintic generator.

No selected actual coefficient, point, matrix, rank, derivative, or source was evaluated. No large computation or external write was performed. Only this local review file was authored. No access denial or pending authorization blocked the audit.
