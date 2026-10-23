# Source126 dual specialization

The three actual residual templates of PR858 allow only two of the four retained source126 quotient profiles. Types I/II force index129; Type III forces157. Indices231 and249 are removed, but stable label G3.11.8ae96830fd21 remains open.

Read PROOF.md for the actual quotient/Ext argument and the universal first-polar no-linear-annihilator lemma. The Type III full splitting uses the pinned exhaustive retained catalogue; rank/degree alone is not asserted sufficient. PR869 supplies nonempty abstract residual templates, which this theorem does not rule out or identify with the fixed HM tensors. No abstract-family catalogue completeness is asserted.

Reproduce with Python3:

    python verify.py
    python -O verify.py

Both execute 288 checks and write RESULT.json. Checks cover immutable proof/catalogue hashes, exact profiles, ranks/degrees, the 4=2+2 filter, and coefficientwise universal differentiated Euler identities in degrees1–14 and coefficient dimensions1–6. These are symbolic identities with independent formal coefficients, not actual-HM evaluations.

No external experiment, model run, actual coefficient, parameter, point, matrix, derivative value or source-instance rank is used. This is a new quotient specialization of existing actual geometry, not a complete proof repair.
