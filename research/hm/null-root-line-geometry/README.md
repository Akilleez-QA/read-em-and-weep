# Root-line geometry certificate

Read PROOF.md for the geometric proof and REVIEW.md for scope and audit findings. The inputs directory contains inert, pinned source documentation and a line-numbered raw-engine excerpt. pins.json records provenance; SHA256SUMS covers bundle files.

Requires Python 3 and SymPy. From this directory:

    python verify_one_curve.py
    python -O verify_one_curve.py

Both commands must pass. Negative probes:

    python verify_one_curve.py --inject-wrong-sign
    python -O verify_one_curve.py --inject-wrong-sign

Both negative probes must exit nonzero. Ordinary negative controls run automatically even without the flag. The checker imports only SymPy and the Python standard-library argparse module. It performs exact one-curve rational algebra, without numerical sampling or physical/source object evaluation. Rational algebra supplements the divisor/local-ring proof; it cannot by itself establish regularity of line-bundle sections.

The package is portable and has no network or private-filesystem dependency. Nothing is published by running it. No claim is made about source claims outside the root-line/old-connection scalar arrow.
