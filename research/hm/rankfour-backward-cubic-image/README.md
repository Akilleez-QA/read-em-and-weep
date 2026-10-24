# Rank-four backward cubic image bound

Conditional theorem for the actual ordered maximal profile (3,1): every restricted dual cubic image from a T6 copy has rank 1, 2 or 3, never 4. Rank 1 forces O(9) and necessary source D. This does not close the profile.

The independently derived 31-row endpoint/defect ledger retains 24 positive-defect rows. General unramifiedness is not assumed.

Reproduce with the Python standard library:

    python3 verify.py
    python3 -O verify.py

Outputs must equal RESULT.json. The program is independent of working directory. PROOF.md supplies the geometric proof and precise imported assumptions; INPUTS.json pins the five complete original sources. LEDGER.json and ENDPOINTS.json are readable projections of the full certificate. No actual instance or historical source enumeration is evaluated. Source hashes verify bytes, not geometric truth.
