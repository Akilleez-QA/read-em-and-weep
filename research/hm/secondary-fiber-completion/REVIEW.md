# Independent review of the conditional exceptional-fiber completion

## Verdict and exact reviewed artifacts

APPROVED as a new conditional theorem, retaining the hypothesis that both actual D-row channel coefficients are nonzero. No actual channel coefficient or branch has been selected.

This review binds the following SHA256 identities:

- PROOF.md: `2ec9f71862bad628ee1663fa91c6bb511db9232355143a3a51e067362ebca575`
- verify.py: `7860b4e3204cb4b50079b176f0d091473a99cee6caad5d1fecd79fdf14625083`
- INPUTS.json: `fca42853a73594aca164cc7264e2fc076229647e366d2c24a0d218bbe73d06b3`
- Exact retained DROW proof: `59756d7dac77cfe0f91c323e9d9bf88ef1b4947923beac0f5af5c50ed360099b`

I read the complete new proof and the retained D-row and target-exclusion arguments, checked the local source identity against the DROW audit copy, and independently replayed both `python3 verify.py` and `python3 -O verify.py`. Both passed. The executable checks concern fixed abstract characters, character weights, elementary inequalities and input identities; they are not substitutes for the bundle and local-algebra arguments reviewed below.

## Mathematical checks

1. **P-to-V channel.** The degree-six P system is basepoint-free because a nonempty invariant base divisor would be too small. Its linear syzygy space injects into the irreducible six-space Sym5 W, while projection to one P coordinate bounds its dimension by four. This proves the required vanishing, not merely an expected dimension. Rank three, degree minus six and that vanishing force the evaluation kernel to be V O(-2). Dualizing and twisting gives exactly O(-4) as the kernel of the everywhere-surjective P(2)-to-V(4) channel. The twist and dual signs are correct.

2. **P-to-P channel.** Tensoring the Euler quotient W(2)-to-O(3) and Euler inclusion O(3)-to-W(4) with W' produces a nonzero rank-two channel. Its kernel is W' O(1) and image W' O(3), with the displayed twists correct. The one-dimensional equivariant Hom space identifies it with the desired universal channel up to scalar.

3. **W-channel injectivity.** A putative saturated rank-one image O(d) satisfies minus one at most d at most four. Perfectness removes a possible character twist, and central parity leaves d=0,2,4. The fixed character exclusions eliminate d=2,4, while d=0 would require the forbidden O-to-J(4) map. Generic rank is therefore two. Its exterior-square section has degree ten; the common-zero divisor is invariant and cannot contain a projective orbit. This establishes everywhere injectivity, not only sheaf injectivity.

4. **Stabilizer signs and nonvanishing.** With O(1) character lambda, the Euler kernel O(-2) has zeta character 4; the P-to-V kernel O(-4) has character 3; and W' O(1) has characters 2 and 4. The displayed source and target character lists are correct. In particular the D quotient O(12) has character 1, so the D-row exceptional kernel has precisely characters 0 and 4. The other P channels are nonzero on their character-0 sources, and the W channels are nonzero on both source characters. No inference from permitted characters alone is being used to assert nonvanishing.

5. **Comparison normalization.** The character-0 lines and the Euler right inverse are well-defined equivariantly over the entire reduced homogeneous orbit. The two maps being compared for each target are nonzero maps into the same line. Their ratio is an invariant invertible function on a transitive finite reduced scheme, hence a single scalar. Thus the compatible universal normalization exists without evaluating a chosen actual point. In that normalization the residual character-0 map is exactly proportional to a_D b_J minus b_D a_J. This expression should not be transported unchanged to arbitrary independently chosen channel generators; the proof expressly retains the compatible normalization.

6. **Full fiber ranks.** The D-kernel's character-4 line contributes exactly e, and its character-0 line contributes exactly r. Distinct characters make these contributions independent. This proves rank 4+e+r on the orbit. Off it the D-kernel is the Euler line, giving rank 5+e. All four indicator possibilities are covered without choosing an actual one.

7. **Scheme order and torsion.** In the e=1, r=0 case, the four P columns can be cleared using the D injection. A further row is a unit on the Euler column, and the remaining D entry is a unit times the reduced orbit equation. Their six-by-six minor has valuation exactly one. Every six-by-six minor vanishes on the orbit by the established fiber rank, proving equality of ideals rather than just equality of supports. Rank five on the orbit leaves exactly one positive Smith exponent, which must be one. The e=0, r=0 case reduces exactly to the retained D row. Constant rank for r=1 gives locally free cokernel. Adding a zero A row and the locally split square-survivor source kernel preserves the asserted minors and torsion for the original boundary.

## Contribution and scope

The new result resolves the exceptional-fiber rank and exact torsion multiplicity within the already conditional two-D-channel branch. The original kernel-sheaf classification is correctly attributed to DROW rather than counted as new. The result does not establish that this branch occurs for the actual HM boundary, determine any of its six coefficients, or imply a global quadric, top-sigma, vertex-delta or catalogue conclusion.

No selected actual HM/source coefficient, point, parameter, jet, derivative, matrix or instance rank was evaluated during this review. No mathematical blocker remains for the precisely stated conditional theorem.
