# Twist-two vanishing: a focused stacked continuation

For the normalized complex Horrocks–Mumford bundle F, this slice proves

    H⁰(P⁴, End₀(F)(2))=0,
    h¹(P⁴, End₀(F)(2))=85,
    Hⁱ(P⁴, End₀(F)(2))=0 for i≥2.

Read [PROOF.md](PROOF.md) for the argument and [AUDIT.md](AUDIT.md) for the independent mathematical checks and exact proof hash. [SOURCES.md](SOURCES.md) maps the specialized inputs to public primary sources; [PROVENANCE.md](PROVENANCE.md) preserves source-artifact hashes without claiming that older audits certified later bytes. [manifest.json](manifest.json) records hashes of the final publication files, excluding itself.

## Dependency and review order

This PR is stacked on branch `mr-slop/hm-twist-one-vanishing`, not on an asserted merged result. Its prerequisite is [PR #91](https://github.com/Akilleez-QA/read-em-and-weep/pull/91), specifically [commit ee7c4d4627c2efa07ea167a535cf1582002ef335](https://github.com/Akilleez-QA/read-em-and-weep/commit/ee7c4d4627c2efa07ea167a535cf1582002ef335). Review [the twist-one proof](../twist-one-vanishing/PROOF.md) before accepting this conclusion.

The new slice first bounds the trace-free section space by five and uses its nontrivial Heisenberg central character to obtain dimensions zero or five. The assumed five-dimensional evaluation then leads to a rank-two reflexive kernel. Central symmetry gives semistability, Bogomolov and Ou give a trivial normalized kernel, and the resulting negative codimension-three defect cycle is impossible.

The refined representation labels, determinant-system refinement, and individual spectral-sequence differential calculations are intentionally not dependencies. No selected instance or large computation is used. This proves neither a source-image assertion nor a sharper collision bound, and does not change any experimental gate.
