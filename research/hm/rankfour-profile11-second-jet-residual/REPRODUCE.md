# Reproduce the second-jet and residual-quotient checks

Run from this directory:

    python verify.py > RESULT.replay.json
    python -O verify.py > RESULT.optimized.replay.json
    cmp RESULT.json RESULT.replay.json
    cmp RESULT.replay.json RESULT.optimized.replay.json
    python review_verify.py > REVIEW-RESULT.replay.json
    python -O review_verify.py > REVIEW-RESULT.optimized.replay.json
    cmp REVIEW-RESULT.json REVIEW-RESULT.replay.json
    cmp REVIEW-RESULT.replay.json REVIEW-RESULT.optimized.replay.json

The author checker uses physical McKay recurrence in characters.py. The independent checker uses closed conjugacy-class characters over Q(sqrt(5)), with no author implementation import. Both check only fixed products, the seven residual rank-two forms already forced analytically by rank/parity/negativity/degree, tiny Hom and Ext dimensions, and rank-degree identities. Hom dimension arrays are dimensions of fixed universal representation spaces, not matrices of an actual bundle map. No actual coefficients, parameters, points, jets, tensors, matrices or instance ranks are evaluated. No global candidate search or historical enumeration is run.

INPUTS.json retains complete immutable sources. The principal-parts source is used only for its universal identity and actual differential-evaluation construction; its triplet-specific hypotheses and flag are not applied to this branch. REVIEW-AUTHENTICITY.json records independent fresh full-byte authentication. Both checkers bind the exact proof hash. REVIEW-INDEPENDENT.md reviews the entire actual second-jet identification, quotient exactness, character exhaustion, structural rank obstructions and equivariant extensions. These mathematical checks are not proof-assistant certification of imported actual geometry.

The exact necessary conclusion is M=A_std(-8) as the actual second osculating subbundle, followed by the target-dependent residual alternatives and four S0 splittings stated in the proof. These bundle splittings are not horizontal splittings. Neither primal positive form is excluded or realized; original defect twelve and torsion fiber characters are retained. The selected publication files contain all dependencies needed for these commands; no unshipped scratch or earlier-stage file is required.
