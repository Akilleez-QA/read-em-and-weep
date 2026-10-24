# Reproduce the deep-image and principal-parts rigidity theorem

Requires Python3 standard library only. From this directory run:

    python verify.py
    python -O verify.py
    python independent_review_check.py
    python -O independent_review_check.py

The author verifier has40 checks; its normal/optimized outputs are byte-identical. The independent verifier has177 checks in both modes, using explicit require() failures; its outputs differ only in the optimized flag. It uses direct exact class-character inner products rather than importing author characters.py. Both checkers pin the proof and retained source files.

The whole-proof review covers the universal principal-parts identity, the actual differential-evaluation map from a possibly incomplete coefficient system, saturated factorization and equal-degree rigidity, the cubic A_std(-4) obstruction, and every image alternative. The arithmetic checkers do not replace that geometric review or certify the imported actual hypotheses by a proof assistant.

INPUTS.json pins the complete immutable PR1198, PR1194 and PR1185 proofs. The PR1198 copy was freshly fetched at its immutable commit and compared byte-for-byte after publication. The previous accepted proof and original source statements, not their historical searches, are the dependencies.

Conclusion: all five necessary triplet kernels have derivative rank3. K3 allows full positive A_std(2) or W(1)+O(-10); K4/K5 allow full positive A_std(2) or the specific length12 positive image preimage of f12 O(-8). The negative-image branch forces a five-stage unramified rank2 flag and is incompatible with K5's actual A_std(-4) subbundle. No whole kernel, quotient, profile or coarse bin is removed or realized. No actual coefficients, points, jet values, instance matrices/ranks or height scans are evaluated.
