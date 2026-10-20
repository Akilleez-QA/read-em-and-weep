# Twist Three Kernel

Read [PROOF.md](PROOF.md), [PROVENANCE.md](PROVENANCE.md), the [historical mathematical audit](HISTORICAL-AUDIT.md), and [final publication check](PUBLICATION-CHECK.md). The manifest binds every shipped source, proof, and review file.

This slice depends on the twist-three reduction. It does not decide cubic vanishing.

## Universal arithmetic checks

Run `python3 hn_arithmetic.py` and `python3 audit_arithmetic.py` (Python standard library only). Both were rerun successfully during publication preparation. They enumerate rank/determinant congruences and Bogomolov-rounded bounds before all geometric exclusions; a printed positive-defect candidate is not a surviving geometric possibility. PROOF.md §§2–4 supplies the additional exclusions and the exact five final profiles. These scripts do not evaluate an HM map.
