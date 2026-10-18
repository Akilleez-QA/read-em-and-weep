# Paired-current reduction of the source-adjoint remainder

A bounded exact Maurer–Cartan reduction with the transported mixed terms and full nonconstant dual-kernel derivatives retained. The complete ten-term baseline and both original Fk branches remain. This is not a vanishing proof or a divergence certificate.

Read PROOF.md and independent/REVIEW.md. Python 3.9+ standard library only; no third-party packages.

Offline replay from this directory:

    sha256sum -c SHA256SUMS
    python -B check.py
    python -BO check.py
    python -B independent/check_structure.py
    python -BO independent/check_structure.py
    python -B independent/tamper_controls.py

Frozen inputs are inert text and must never be imported or executed. Checkers use generic free words and static AST/hash inspection only. Results are recorded under results. The tamper checker modifies disposable temporary copies and tests both interpreter modes.

Immediate prerequisite proof/review texts are included; their transitive references remain external prerequisites. No self-contained geometric proof or remote provenance authentication is claimed. No publication was performed.
