# Historical source review

The following audit concerns the larger original residue manuscript, not these extracted bytes.

# Independent audit of the Serre-dual residue certificates

## Verdict and scope

PASS, conditional on the explicitly imported ordered pair vanishings, zero Massey indeterminacy, Kodaira–Spencer identification, and representation-theoretic statements. No mathematical correction is required. The completed PROOF.md was independently read in full, together with the algebraic TW proof and audit, scalar Čech proof, and both parameter-space proofs. This audit verifies the new residue construction and its interface with those imports; it does not independently reconstruct the entire earlier dependency chain.

## 1. Residue and orientation

On the intersection indexed by 01234, scalar sections of O(−5) are finite homogeneous Laurent sums. A Čech boundary term from the face missing j has nonnegative x_j exponent, so its all-minus-one coefficient vanishes. Conversely, every weight −5 monomial other than the all-minus-one monomial has a nonnegative exponent and is the boundary of its corresponding missing-face component, with the alternating sign adjusted. The coefficient functional therefore induces an isomorphism H⁴(O(−5))→C with the displayed generator mapped to 1.

The homogeneous volume Ω restricts on x_0=1 to the ordered form dz_1∧dz_2∧dz_3∧dz_4. Thus the declared coefficient functional agrees with the stated normalized ordered residue convention. The simplex orientation dt_1∧dt_2∧dt_3∧dt_4 agrees with increasing vertices. Its barycentric monomial integral is exactly the factorial quotient in (4). The top Whitney form has coefficient 4! in these coordinates, while the constant simplex integral is 1/4!, so IW=id introduces no additional factor into (1). The ordinary matrix trace, rather than half-trace, is the correct evaluation pairing. Coordinate and volume choices must be transported as specified.

## 2. Duality and TW product

The trace form identifies End(H) with its vector-bundle dual. Consequently E_(−r)^∨⊗K is E_(r−5), and smooth proper four-dimensional projective space gives a perfect degree-two pairing with the stated twists. The cup/evaluation description and the required finite-dimensional perfectness were checked in [Stacks, §48.27](https://stacks.math.columbia.edu/tag/0FVU), especially Remarks 48.27.2 and 48.27.6. The Laurent description agrees with [Stacks, §30.8](https://stacks.math.columbia.edu/tag/01XS).

The imported algebraic reduction supplies a closed C of degree two and twist −r. For closed η of degree two and twist r−5, tr(Cη) is therefore a closed scalar degree-four cochain of twist −5. The imported multiplicative DGA comparisons identify this product with the cohomological cup/evaluation product. Integration is used only afterward as a chain map and cohomology comparison. No false cochain-level multiplicativity assertion about I or W is needed. The degrees two and two introduce no trace-cyclic minus sign.

## 3. Independence and finite exactness

Both displayed boundary identities in §3 have the correct Leibniz signs. Integration takes them to Čech boundaries and the residue annihilates them. Together with the imported singleton Massey theorem, this proves independence from input representatives, normalized local lifts, and permitted scalar-primitive choices. Vanishing of H²(O(−4)) and H²(O(−3)) permits a trace-free dual representative, but the construction neither needs one nor imports an unproved scalar contraction at those twists. Whitney extension of an ordinary dual cocycle is legitimate in every twist.

All regular scalar coefficients on the full intersection are finite Laurent sums, and the imported operators preserve finite simplex expressions. Formula (4) is therefore an exact finite operator prescription for supplied representatives. Its proof does not evaluate an actual input polynomial. Perfectness proves the nonzero-witness equivalences, but does not supply witnesses or justify an arbitrary finite cutoff.

## 4. Four upper and eight lower coordinates

For finite-dimensional S_r and T_r, the canonical identification Hom(S_r,T_r)^∨=S_r⊗T_r^∨ and surjectivity of restriction to the dual of its equivariant subspace justify every lift L_j in (7). Serre duality identifies the second tensor factor with D_r. Finite expansion into decomposable source tensors, followed by arbitrary representative choices, gives (8). Different lifts agree on equivariant operations, and representative independence was proved above.

Accordingly simultaneous vanishing of all four upper or all eight lower coordinate sums is equivalent to vanishing of the corresponding operation. This is an existential finite-sum realization of chosen parameter functionals; it does not compute the lifts or their cocycles. The proof correctly distinguishes parameter counts, downstairs target dimensions, and retained target dimensions, and avoids the invalid naive flip of the twice-iterated lower multiplicity factors. The conditional full-image statements follow from the imported irreducibility only after nonvanishing is established.

## Evidence boundary and exact binding

Only static local proof reads, read-only primary-reference checks, universal mathematical reasoning, this audit-file write, and a proof-file integrity hash were used. No actual input classes, source/model matrices, instance products, ranks, polynomial instances, points, jets, residuals, or Massey values were evaluated. No external writes, local Codex task, or large computation occurred. The audit establishes no instance vanishing, nonvanishing, retained span, or physical-source verdict.

Reviewed PROOF.md SHA256:

    d85613e1d0ed6340511c69ca316455f114821bfedfbade89980bfd7e633fb993

The hash was unchanged after writing and rereading this audit.
