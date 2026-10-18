# Portable curve-derivation bridge

This directory is a self-contained static/formal review bundle. It is prepared locally and has not been published or deployed.

Read REVIEW.md for the independently checked conclusion, premises and remaining obligations, and PROOF.md for the full source-bound mathematical argument.

Run with Python 3.9 or newer:

    python check.py
    python -O check.py
    python test_negative_pins.py
    python -O test_negative_pins.py

The first two commands each report 918 checks. Each negative-pin run reports six specific pin rejections. The checker uses only Python's standard library. Its source inputs are deliberately suffixed `.txt` and are parsed as inert text only. It never imports or executes them.

All dependencies are inside this directory. Input hashes are fixed in check.py and repeated in pins.json. SHA256SUMS binds the distributed bundle; it is an integrity inventory, not a signature or independent authenticity guarantee. Stored result files are receipts only; rerun the commands to reproduce them.

The `inputs/field.py.txt` input is the frozen original field source. `inputs/candidate-field.py.txt` is the inert proposed candidate. The 53-method equality statement does not validate added certificate functionality or authorize execution or deployment of either input.
