# Ordered rank-four (1,2): one necessary source/endpoint tuple

This is a conditional mathematical reduction, not a profile exclusion or a repair of the original theorem.

The actual ordered (1,2) profile must have source D, endpoint degrees (−58,−22), zero determinant defects, quotient B=O(−8)+W′O(−1)+O(14), and upper dual endpoint Z0=W′O(−5)+VO(−4). The proof retains all positive torsion until it is intrinsically excluded.

Read PROOF.md for the complete geometric argument and evidence boundary. INPUTS.json pins eight complete original documents by immutable URL, Git object identity and SHA256.

Reproduce with:

    python3 verify.py
    python3 -O verify.py
    python3 test_controls.py

The first two outputs agree exactly with RESULT.json from any working directory. The checker performs3477 explicit checks. Ten executed mutations are rejected normally and optimized; the unmutated one-tuple control survives. Finite domain enumeration is independently cross-checked, as are physical representation arithmetic and endpoint capacity.

Files base.py, verify.py, test_controls.py, INPUTS.json, inputs/, PROOF.md, RESULT.json and CONTROLS.json form the portable author packet. No actual coefficients, points, jets, matrices or instance ranks are evaluated. The invalid exploratory H0(Q*(1)) vanishing is not assumed. Historical one-shot classifications are not rerun or used as exhaustive sources.
