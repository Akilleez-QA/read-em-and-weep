# Independent final-byte audit

Verdict: **PASS for the stated bounded theorem. No mathematical correction is required.**

- Reviewed artifact: `PROOF.md`
- SHA-256: `701619c9d83333cf3f7c03d9441afedb3e5b6e0f40578b1bbffc2291b3dd9cd3`
- Review date: 2026-10-18 UTC

## Premises and derivation

I read the complete final proof, the included product-root proof sections 3, 4 and 7, the same-carrier proof's identity and propagation sections, and both included dependency reviews. The regular homogeneous contraction and its authenticated source identity remain accepted dependencies, not new results of this audit.

The final proof correctly obtains the downstairs vector bundle directly from the homogeneous complex and its regular split contractions on a covering family. This gives locally free rank-two cohomology in degree zero and no other cohomology. It does not infer descent from an arbitrary bundle on X. Pullback preserves the explicit split identities without requiring a separate flatness argument. The coefficient morphism identifies rho*O(1) with O(1,1,1,1).

The cohomological signs are (-,+,-,+). They give rank 2, c1=-H and ch2=-7H²/2, hence c2=4H². On Y, the square of the sum of the four axis classes has coefficient 2 on every distinct-axis product; the c2 coefficient is therefore 8, not 4. Pic(Y)=Z⁴ includes every algebraic line bundle, and the proof's induction using fiber degree, base change and evaluation is valid for these connected projective products.

For hypothetical summand degrees a_i and -1-a_i, the coefficient equation is -a_i-a_j-2a_i a_j=8. Rewriting it gives (2a_i+1)(2a_j+1)=-15. Three axes force two nonzero factors equal and then require their square to be -15. This is impossible for integers. The direct P4 argument and the alternative pullback argument are both valid.

The X consistency calculation is also correct: f*H=2n gives c1(f*E tensor N)=0 and c2(f*E tensor N)=15n². The displayed physical complex character has ch1=0 and ch2=-15n². These computations are not promoted to an arbitrary-X nonsplitting result.

## Exact scope

Ordered diagonal invertible transition matrices glue their two coordinate lines separately. Consequently every globally covering regular algebraic atlas of the stated kind, including any open refinement or regular algebraic regauging, would provide the forbidden direct-sum decomposition. The transition-atlas conclusion follows without assuming a particular set of carrier frames.

The same-carrier identity is appropriately retained as a restricted identity. The proof explicitly avoids asserting that every all-carrier simplification implies the forbidden atlas. It distinguishes diagonal local connection forms from diagonal overlap transitions, excludes no arbitrary X gauges, and makes no claim about unordered/Weyl-monomial atlases, other base changes, rational or meromorphic gauges, or source-specific cancellation. No detector or obstruction conclusion follows. These limitations resolve the scope concern raised during the preliminary audit.

## Evidence boundary

This review certifies the mathematical implication from the stated accepted dependencies and the final proof's exact bounded scope. It does not independently certify the historical searches or source-read log in section 5, literature novelty, or the external six-carrier connection calculation; the latter is contextual and unnecessary to the nonsplitting proof. No new external source authentication was performed.

Only inert local file reads, SHA-256 hashing, symbolic mathematical reasoning and this review-file write were used. No source/model/matrix/polynomial/point/jet evaluation, source computation or external write occurred. The proof file was not modified.
