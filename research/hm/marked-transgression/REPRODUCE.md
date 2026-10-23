# Reproduction

The nine exact input paths and commits are listed in INPUTS.json. Fetch each from Akilleez-QA/read-em-and-weep at its immutable commit and write the original UTF-8 bytes to audit-inputs/LABEL.md. The verifier authenticates their Git blob SHA-1 values, including exact final newline bytes. Audit copies need not be committed.

Run `python3 verify.py` and `python3 -O verify.py`. Both return 22 passing input/authentication and bounded representation/index checks. The script uses only the Python standard library, performs no network requests, and evaluates no actual HM/source data. It checks the dimensions of the transgression input and target, the necessary spectral-sequence differential positions, and rank/degree bookkeeping.

The actual-map naturality, Koszul regularity, base-change and transgression arguments require mathematical review of PROOF.md. The checker does not certify them formally, nor does it select any value of the detector.
