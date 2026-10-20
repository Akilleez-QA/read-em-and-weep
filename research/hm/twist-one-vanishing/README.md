# First twisted trace-free endomorphism vanishing

## One result

For the normalized Horrocks–Mumford bundle F on complex P⁴,

    H⁰(P⁴, End₀(F)(1)) = 0.

This small proof capsule excludes all six ranks of the quadratic determinant of a hypothetical section. Its sole HM-specific section input is provided directly from Decker's published graded resolution.

## Reading order

1. SOURCES.md fixes the normalization and supplies the complete section-vanishing input.
2. PROOF.md gives the structural spectral-cover argument.
3. AUDIT.md checks each determinant-rank branch, including the rank-three cone-depth step.
4. manifest.json binds these exact public text files by SHA-256 and Git blob IDs.

## Review focus

- The spectral sheaf is constructed after restriction and is maximal Cohen–Macaulay because its finite pushforward is locally free.
- On a smooth quadric surface the Euler polynomial permits O(2,−2) and O(−2,2); this is not itself a contradiction. The rank-three case needs the subsequent vertex-depth obstruction.
- The quadric surface cone uses rank-one reflexive sheaves, not a false assertion that every such sheaf is a line bundle.

## Scope and next step

This is a written proof with a mathematical audit, not a Lean certificate or a claim of novelty. It neither evaluates a selected HM matrix nor changes any experimental release gate. It makes no claim about H⁰End₀(F)(2), h¹End₀(F)(1), higher twists, or an ambient obstruction. A subsequent focused note can address twist two after this dependency has received review.
