# Independent mathematical review

Verdict: PASS, conditional on the pinned geometric inputs.

Reviewed file: PROOF.md.
SHA-256: f64f42bca345efb7a7140e2abefdea2c11d793a930602c1b94d7130a550943ac.

## Checks

1. The divisor calculation is exact: -3(-5H+3E)+4E=15H-5E=5(3H-E). Preservation of the actual exceptional divisor, not just its class, supplies the canonical action on O_M(4E). The canonical action on omega_M is functorial. Since global units upstairs are constants, transporting this action across an ordinary isomorphism D^5 to the canonical expression is independent of that isomorphism.

2. The descent argument addresses the essential conductor issue. It does not infer descent of an arbitrary bundle or action merely from normalization. The downstairs bundle and its invariant class are already supplied. Each individual downstairs lift exists, and its pullback can be aligned with the prescribed upstairs lift using the isomorphism of global unit groups. Cocycle discrepancies downstairs then pull back to 1 and must equal 1. This proves coherence and uniqueness without assuming injectivity of Pic(V) to Pic(M).

3. Necessity of divisibility by five uses precisely the U-obstruction of PR638; sufficiency for the full group is independently provided by the canonical construction. Tensor powers and duals include zero and negative integers. The full obstruction has exact order five because it is killed by five and has a nonzero order-five restriction.

4. The perfectness argument is valid without a split extension. In SL2(F5), conjugation by diag(2,3) multiplies an upper unipotent parameter by 4, so the commutator parameter is 3x and exhausts F5. Upper and lower unipotents generate SL2(F5). For any lift of -I, its commutators with U give -2u and exhaust U. The derived subgroup therefore contains U and surjects onto the perfect quotient, proving Gamma is perfect. Trivial character group gives uniqueness of the action on a fixed bundle, while scalar automorphisms of the linearized object remain.

5. Artin persistence correctly fixes the underlying Gamma-action and uses invariant pair classes only to obtain individual line-bundle lifts. Scalars are R* with trivial group action because the base is fixed. Finite logarithm and averaging annihilate positive-degree cohomology of 1+m_R, so reduction preserves the obstruction. The proof does not assume a deformed normalization exists. Uniqueness on a fixed representative makes compatible base-change identifications equivariant. It retains marked scalar automorphisms and does not claim unique identifications of representatives.

6. The full-Gamma fixed pair-class functor being constant is explicitly retained; the new result resolves its scalar-sensitive equivariant structure, rather than claiming new full-group deformations. The twelve-dimensional U-fixed locus and the original adjoint/source problem are not conflated with this result.

The local PR638 and PR637 proof texts were checked for the claimed obstruction and fixed-class/scalar distinctions. Other geometric facts are treated as the stated pinned dependencies, not re-proved here. This review is an independent mathematical check, not proof-assistant verification. No selected geometric coefficient, point, matrix, derivative, rank evaluation, or large computation was performed.
