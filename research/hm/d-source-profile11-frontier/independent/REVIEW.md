# Independent review: D-source maximal-profile (1,1) necessary frontier

Verdict: PASS for the explicitly conditional necessary-frontier theorem. No realization, other-source closure, global rank-three exclusion, or original proof repair is certified.

## Frozen artifact identity

- PROOF.md SHA256: 7a21b3efdd1326266623093f3b1d2c6f95c13027c73c8d3ccb005134b9ed443e
- verify.py SHA256: df0bb3d5634091f748908d25861621c75a58a97609a06169b34a89fa4ba25c89
- INPUTS.json SHA256: bd63cacc47c963d5202b2dac4ad390a845a7536b516108c6c9979fb3163c420f
- RESULT.json SHA256: bd593940ff604883e2293f2609b04654050a70b0d7a26c36048ccbd93d6420f3

These identities bind this review to the packet, not later changes.

## Independent evidence

All nine originals were freshly fetched at the author's full immutable commits through the connected GitHub reader. Their Git blobs, SHA256 digests, byte counts, and packet bytes agree. FETCH.json records those immutable origins. In particular the original 159-pair written necessity theorem was read, not replaced by an inference from its JSON output.

The independent checker uses nine conjugacy classes, exact arithmetic in Q(sqrt(5)), closed binomial symmetric-power traces, and character inner products. It does not use the author's McKay recurrence to compute the result. It verifies orthonormality of all irreducible characters and cross-checks all 369 products R tensor Sym^n W for n=0,...,40 against the separate production character implementation.

All 159 historical records were read, not regenerated. Both source-cohomology inequalities were independently recomputed at all 21 prescribed twists. Every signed failing witness, the complete cubic character, and every one of six capacities for every record matches the author's output. The capacity was independently summed over the six possible nonincreasing rank sequences before comparison with the height formula. All record degrees and determinant defects agree.

The independent checker passes 6,676 explicit controls under normal Python and Python -O, with identical JSON. The author's checker passes 1,204 controls plus 81 character-module controls in both modes, and both replay outputs are byte-identical to frozen RESULT.json.

## Geometric transfer and scope

The original written necessity theorem supplies a necessary overlist under its imported actual hypotheses, including its explicitly external lower-degree theorem. This packet correctly imports that theorem and prerequisites instead of claiming this review reproves the whole dependency chain. The finite twist interval remains only a necessary filter. The exact D tuple is (1,1,1,0,0,1,0,0), directly consistent with PR1123's coefficient formulas.

PR1140's cubic injection is into global sections, not a rank-14 fiber subbundle. The source-conditioned character inequality used here follows precisely from that statement. Signed virtual character subtraction is retained.

The dual capacity argument applies to the actual negative dual endpoint of profile (1,1): rank L=10 and derivative rank at most two. Saturated successive kernels remain negative, a nonzero horizontal kernel cannot occur in the constant connection over C, and the rank decreases until zero. Actual quotient derivatives give sheaf injections into B(-2j); no saturated image is needed. Their determinant degrees give the six capacity bounds. No profile-(2,1) top(S)<=-2 hypothesis is imported.

The scopes of the full pinned exclusion proofs were checked:

- PR1135 excludes O(-8)+O(4)+O(6) and O(-8)+W O(5) for the D-source with no next-derivative-rank or defect restriction. Its actual graph argument retains the V(-4) rows.
- PR1142 excludes O(-8)+O(4)+O(8) and O(-8)+O(4)+O(10), using the forced O(2) coherent image and signed fourth-twist envelope. It is not applied to residual shapes containing O(2).
- PR1145 excludes O(-8)+O(2)+O(16) in profile (1,1). Its positive-defect row is already cut by capacity; its zero-defect row requires the complete published height-seven and height-eight proof. The certificate imports that full theorem, not a false inference from equality alone. Its partial coefficient quotient is made full by the sextic-net span before its final dimension contradiction.

## Exact verified partition and residual obligation

The disjoint ordered partition is:

159 = 57 D-incompatible + 32 cubic + 62 capacity + 2 PR1135 + 2 PR1142 + 1 PR1145 + 3 remaining.

The 102 D-compatible records leave exactly indices 32,50,52, with two A shapes and three ordered pairs:

- 32: A=O(-8)+O(2)+O(4), B=O(-18)+O(-4)+O(6), defect 12.
- 50: A=O(-8)+O(2)+O(4), B=O(-6)+O(-4)+O(6), defect 0.
- 52: A=W O(3)+O(-8), B=W O(-5)+O(6), defect 0.

Record 32 has degree L=-38 equal to maximum capacity -38, attained at height pairs (7,3) and (8,2). It is not excluded. Records 50 and 52 also survive these necessary tests. Neither existence nor freedom from other obstructions is certified. P/V/Z closures are entirely separate and were not used. No new live-case count follows by adding historical category counts.

No blocking mathematical gap was found in this conditional reduction. This is independent exact arithmetic plus written-proof scope verification, not proof-assistant verification or a new theorem beyond the reviewed artifact.

## Reproduction

From this review directory, with the frozen author packet in the parent directory:

    python3 independent_check.py > replay.json
    python3 -O independent_check.py > replay-optimized.json
    cmp RESULT.json replay.json
    cmp replay.json replay-optimized.json

The checker reads the frozen historical data and universal characters only. No actual source coefficient, selected parameter, point, jet, matrix, instance-rank test, historical enumeration regeneration, spike restart, or external write was performed.
