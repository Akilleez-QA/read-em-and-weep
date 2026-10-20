# Twist Four Blocks

Read [PROOF.md](PROOF.md), [PROVENANCE.md](PROVENANCE.md), the [historical mathematical audit](HISTORICAL-AUDIT.md), and [final publication check](PUBLICATION-CHECK.md). The manifest binds every shipped source, proof, and review file.

This slice depends on the twist-three reduction, independently of the kernel-semistability slice. It does not decide any quartic block value.

## Universal character check

Run `python3 characters.py` with SymPy installed. A publication-preparation rerun reproduced all source, target, coefficient and trace-free-source decompositions displayed in PROOF.md. The script uses only the nine-column finite character table and exact symbolic arithmetic. It does not compute any of the five obstruction restrictions.
