# Terminal-pencil kernel restriction and capacity

A focused universal linear-algebra and bundle lemma supporting the HM proof-repair program. The original problem remains open. No actual source is selected or evaluated here.

- `PROOF.md`: kernel restriction is fully faithful for everywhere-surjective linear coefficient pencils on the same P1; sharp Hom and terminal image-capacity consequences.
- `verify.py`: Python standard-library rational coefficient solver.
- `RESULT.json`: exact nullspace bases and 327 successful checks.
- `INPUTS.json`, `inputs/PR1122.md`: immutable motivating source and byte authentication.

Reproduce from this directory:

    python3 verify.py > result-normal.json
    python3 -O verify.py > result-optimized.json
    cmp result-normal.json result-optimized.json
    cmp RESULT.json result-normal.json

The only inputs to the solver are universal standard pencil sizes. It does not load any HM coefficient matrix or evaluate any selected geometric point. Its capacity theorem assumes a supplied actual coefficient-pencil decomposition and does not establish one. PR1122 already contains the specific source2 contradiction; this packet supplies the general kernel-map extension proof and a reusable sharp-boundary test artifact rather than claiming that earlier result as new.
