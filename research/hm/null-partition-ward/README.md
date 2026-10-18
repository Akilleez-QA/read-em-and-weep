# Differentiated partition reduction

A portable, conditional formal reduction of the complete source-adjoint outer-weight derivative family into a rational Čech boundary plus an explicit source defect. Neither term is silently discarded. Read PROOF.md and independent/REVIEW.md first.

Requires Python 3 and SymPy. From this directory, run each in both modes:

    python -B check_binding.py
    python -B check.py
    python -B independent/check_exterior.py
    python -B independent/tamper_controls.py

Replace -B by -BO to replay optimized mode. The tamper control itself exercises both modes. Saved outputs are in results. SHA256SUMS inventories the distribution; check_binding.py separately embeds fixed pins for proof, branch metadata and selected prerequisite sections.

The selected prerequisite sections are supplied verbatim. Their full-file source hashes and selections are in PROVENANCE.json. These are supplied-byte references, not fresh remote attestations or a self-contained proof of all geometric premises. No production module is included or imported; no actual source/model/owner/jet values or matrix-polynomial products are computed. No new execution admission or publication is implied.
