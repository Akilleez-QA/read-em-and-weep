# Reproduce the bounded four-row closure

Run in this directory with standard-library Python 3:

    python verify.py
    python -O verify.py

Both runs authenticate ten complete pinned originals and reproduce RESULT.json exactly. The fixed inputs are read as documents/data; no imported program or historical source/quotient enumeration is executed.

The only rank partitions considered are the six universal pairs (h1,h2) with h1>=h2>=0 and h1+h2=10. Their applicability is proved from the actual dual endpoint rank, derivative injections and eventual descent in PROOF.md. The program checks their four capacity bounds, equality positions, exact original quotient/defect identities, the degree-ten character and minimum-degree Hom obstruction. It also records the disjoint union of the three proved cuts of the original thirteen-row profile21 list. A partition of JSON records alone would not establish coverage: the original written necessary-list theorem and two direct geometric reductions are explicitly imported.

The equality-to-osculation and actual-annihilator arguments require whole-proof review. They are not inferred from character arithmetic, degree equality alone, or a chosen horizontal complement. characters.py checks its tensor-W recurrence against exact character values on nine conjugacy classes; the independent reviewer recomputes needed multiplicities by direct class averaging.

The resulting theorem excludes actual maximal profile (2,1), not profile (1,1), COV or generic rank three globally. No actual coefficient, point, parameter, jet, tensor, matrix, instance rank, scan or historical enumeration is evaluated.
