# Reproduce the actual coefficient-span exclusions

Run from this directory:

    python verify.py > RESULT.replay.json
    python -O verify.py > RESULT.optimized.replay.json
    cmp RESULT.json RESULT.replay.json
    cmp RESULT.replay.json RESULT.optimized.replay.json
    python review_verify.py > REVIEW-RESULT.replay.json
    python -O review_verify.py > REVIEW-RESULT.optimized.replay.json
    cmp REVIEW-RESULT.json REVIEW-RESULT.replay.json
    cmp REVIEW-RESULT.replay.json REVIEW-RESULT.optimized.replay.json

The author checker uses physical McKay recurrence in characters.py. The independent checker does not import the author implementation. Both check only fixed character products, the exact H and C characters from the actual presentation, coefficient multiplicities, the one stated five-stage flag's ranks/degrees, and the few universal evaluation Hom spaces. The four dimensions 0,3,4,7 are the possible quotients of the single representation V+P, not a bundle candidate search. No actual coefficient, parameter, point, jet, tensor, matrix or instance rank is selected or evaluated.

INPUTS.json pins four complete immutable originals. The principal-parts input is used only for its universal identity and actual differential-evaluation construction, not its triplet-specific flags. REVIEW-AUTHENTICITY.json independently authenticates all four texts. Both checkers bind the exact reviewed proof hash, and all counted guards stay active under Python optimization.

REVIEW-INDEPENDENT.md audits the entire actual argument: span(M)=span(U), full span of S0, exact C character, the actual top-D derivative flag and its genuine seven-space, transport of the full universal annihilator, the O-linear apolar factorization, the zero-projection case and the unchanged annihilator under nonzero invariant multiplication. These are mathematical reviews, not computational proof of actual instance behavior or proof-assistant certification of imported geometry.

The selected files contain all dependencies required by the commands above. The conclusion excludes the scalar-positive primal form O(2)+2O(4)+O(-8) and leaves only W(3)+O(4)+O(-8) within the two decomposable branches, with S0=A_std(-8)+W'(-11). It does not claim existence of the remaining form or close the separate triplet branch, top-degree-four locus or full profile. The original defect remains twelve, and ordinary splittings have not been declared horizontal.
