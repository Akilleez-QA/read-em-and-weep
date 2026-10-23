# Reproduce the source-113 bb audit

PROOF.md is the mathematical result. The verifier cross-checks fixed abstract arithmetic and catalog identity; it does not replace the actual saturation, connection, or span proofs, and is not Lean certification.

Run using Python 3 and its standard library:

    python verify.py

The companion characters.py performs exact Q(sqrt(5)) arithmetic for the nine binary-icosahedral irreducible characters. The verifier checks the thirteen declared abstract kernel candidates, five surviving kernel characters, their full internal Hom support, the three nontrivial polar characters, every changed final-span Hom, the HN and defect budgets, and the original dual strict-top character obstruction. It does not select or evaluate actual coefficients, parameters, points, derivatives, matrices, instance ranks, or models; it performs no scan or frontier enumeration.

Input files are read from audit-inputs. Their exact Git blob hashes are enforced in verify.py. Retrieve the four originals from immutable commit db51525015bb7c5e825833d550d08dedf6f6ea96 under:

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

- ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md
- NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md
- one-one-endpoint-necessary-pairs.json
- rank-three-quotient-frontier-144.json

PROOF.md pins PR859, PR867 and PR868 and restates their needed arguments, verifying the different source-dependent hypotheses. The expected output begins:

    PASS: four pinned original hashes; exact bb source; thirteen kernel candidates;

Scope is the whole original index-113 source tuple (0,2,0,0,0,0,0,1) only. The proof alone asserts no full-label or global frontier decrement.
