# Reproduce the five-kernel and first-two-image theorem

Requires Python3 standard library only. Run from this directory:

    python verify.py
    python -O verify.py
    python verify-independent.py
    python -O verify-independent.py

Author55 checks and independent1,291 checks each pass normally and optimized, with byte-identical outputs within each pair. The independent checker is portable, uses an explicit full class-character table and no author character code, and pins the complete proof and both retained inputs by SHA256.

PROOF.md gives five necessary kernels and full coherent image A_std(2) only for K1/K2. REVIEW-INDEPENDENT.md reviews the whole proof, including the actual saturation/derivative geometry, conditional on its explicit imported hypotheses. INPUTS.json identifies two exact immutable complete source proofs. No new claim about K3/K4/K5 is included. No original-zero-defect or later principal-parts lemma is a dependency.
