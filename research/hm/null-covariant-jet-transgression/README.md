# Covariant-jet transgression: portable formal packet

Read RESULT.md for the full derivation, REVIEW.md for the independent audit and full trace-dual adjoint. Frozen dependencies contain the complete starting S2, retained Q4, physical derivative conventions and the full remaining-target normal form. Their original external prerequisites remain conditional; this packet is not a recursive geometric proof.

Run with Python 3 and its standard library:

    python check.py
    python audit_check.py
    python verify_bundle.py

All scripts locate bundled files relative to their own location. The logs record exact normal, optimized (-O), and alternate-working-directory results for both checkers. They execute universal scalar-coordinate polynomial identities only. No physical matrix-polynomial products or actual source/model/owner/jet values are evaluated. The audit checker shares the scalar algebra engine but independently specifies its adjoint and transport checks.

The exact result is S2 = covariant divergence + C4 + M2. Neither M2 nor the full dual-kernel derivative is discarded. No residue value, cancellation, new pole bound, detector reduction, performance claim or authorization to execute physical sources follows.

The bounded QUARTIC_ADDENDUM.md collects Q4+C4; its author and independent checks are check_quartic.py and audit_quartic.py. All four checkers are recorded in each regression log. REVIEW.md includes their independent review.
