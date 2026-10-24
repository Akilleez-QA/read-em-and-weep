# Actual resolved F18 gluing surjectivity

## Result and retained scope

Under the full-positive triplet branch, original t=0 and local delta=12,
residual simultaneous rank-seven k=2 geometry, remaining original kernel K1,
and every complete transitive actual-geometric hypothesis of the four
immutable direct originals, this packet proves that the actual maps

    F18=D(-2)+(W'+T6)(-3) -> Q=T6(-1),
    E0 -> F10=(P+D)(-2)

are everywhere onto. The canonical D(-2) top row of the first map is
saturated with quotient O(4). Their actual kernels are canonically identified
with the kernel of the induced quotient row, giving

    0 -> G7 -> (W'+T6)(-3) -> O(4) -> 0,
    rank G7=7, deg G7=-28.

These are identifications by actual quotient maps, not literal equality of
embedded subbundles in different ambients. No splitting type of G7, branch
closure, individual-row exclusion beyond this theorem, or realization is
asserted. Original t and delta are unchanged. There is no higher-order
matching or algebraicity claim.

## Structural proof

1. If the actual canonical D top were killed by degree-ten restriction, its
   constant inclusion would factor through A+V+P. Universal quartic scalar
   and first-jet lifting would then produce a nonzero O(-6) map into the
   actual backward kernel K, contradicting two fixed Hom vanishings.
2. The surviving D row has a one-dimensional universal Hom space and is the
   saturated complete-evaluation kernel D(-2) in T6(-1).
3. Vanishing of the remaining quotient row would produce an actual rank-three
   annihilator A3 containing O(-4). Its inclusion in the actual S0 contradicts
   the retained exact sequence for S0. A nonzero degree-seven row has no
   invariant base divisor because the minimum invariant divisor degree is 12.
4. The exact actual gluing diagram propagates surjectivity and canonically
   identifies the three kernels.

## Files and verification status

- PROOF.md is the full proof, including actual coefficient directions.
- INPUTS.json and INPUTS.md authenticate and locate all four complete originals.
- PROVENANCE.md separates direct imports, new arguments, and review obligations.
- inputs/ contains the four unchanged complete original proofs.
- verify.py checks exact frozen hashes and only fixed small character and
  rank/degree identities. It does not prove any actual-map claim.
- FROZEN.json fixes the ten selected core files. Its own SHA256 is an external
  freeze anchor, not a self-referential entry.
- evidence/ and AUTHOR-VERIFICATION.md contain author-side source/replay
  evidence. They are outside the core and are not replay dependencies.

Run python verify.py and python -O verify.py from a clean copy containing
only the ten core files listed by FROZEN.json plus FROZEN.json itself.
There are no third-party Python dependencies, network access, source-instance
evaluations, broad scans, or historical enumerator in the checker.

This is an unpublished frozen core prepared for a NEW independent entire-proof
review. Preparatory checks and author replay do not supply that review. The
review must cover the full proof and all four complete direct originals,
especially the quartic jet-image argument and actual annihilator directions.
No prior frozen packet was changed; no local Codex, GitHub write, external
submission, or merge was used to prepare this packet.
