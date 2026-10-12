# A complete selected Cartier component over F3

This package contains one complete supplied polynomial: the residue-41 section
C_(2,1,1,1)(s23615), for assignment01234. It has 95,082 nonzero coefficients in F3.
The 28 immutable two-bit frames encode 659,344 trits, including every zero.
Their quotient shape is (28,28,29,29). A quotient exponent q represents the
original exponent e=3q+(2,1,1,1); treating q as e is incorrect.

The canonical nonzero logical-row SHA256 is:
ab8a327f73a88c781f377925b54ad6496cc20825ef9b83808f50bc0af916b426

## Two distinct verification claims

1. The supplied-value checker validates these published bytes: exact file set
   and checksums, canonical metadata, full frame headers and transaction chain,
   all trits and zero padding, quotient and original-coordinate support,
   nonzero counts, and the complete logical row digest. This is a portable
   representation check; it performs no source-polynomial multiplication.
2. The historical component receipt attests that separate primary and reverse
   computations compared the complete actual value, including carry values.
   Each lane used 728 source products. The historical saved-state receipt
   subsequently accepted the held6173 representation after independent readback.
   The public JSON files are scoped projections of those receipts; their
   immutable source-receipt hashes are included. The historical source graphs,
   computation implementations and execution archive are not distributed here,
   so this package alone is not an end-to-end source-arithmetic reproduction.

The component is internal to the first rational Cartier stage. Its nonzero
value does not establish a first-stage value, assignment contribution, complete
J2 simplex, full blind-functional pairing, full detector, or full obstruction.
See ATTRIBUTION.md for the remaining dependency ladder.

## Files and read-only verification

Use POSIX Python 3 (for example, Linux) with O_NOFOLLOW, O_DIRECTORY and
directory-descriptor support. From this directory:

    python3 -I -S -B verify_component.py .
    python3 -I -S -B test_verify_component.py -f

The scripts require only the standard library. They do not modify this package,
load a saved evaluator state, access a network, or regenerate source coefficients.
Tests use bounded tiny synthetic objects for malformed-input boundaries.

value-files.json lists the exact sizes and SHA256 values of all 28 frames,
HEAD.json, spec.json and the two public receipts. Frame filenames are their
content hashes. spec.json and HEAD.json use canonical JSON without a trailing
newline; the other JSON files have one newline. SHA256SUMS covers all 37 other
public files and deliberately excludes itself. A trusted copy of SHA256SUMS
or a release digest is needed to authenticate a downloaded package as a whole.

The held-state projection records an empty resident cache, 95,082 parked terms,
and a conservative 291-row literal baseline. It records no restart or reload
permission. The old saved states remain immutable provenance, not additional
coefficient inputs supplied by this package. Workspace paths, private runtime
commands and execution-control records are intentionally absent.
