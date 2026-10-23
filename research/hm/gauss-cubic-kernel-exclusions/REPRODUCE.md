# Reproduce the fixed universal checks

Run from this directory with Python 3 and the standard library:

    python3 verify.py
    python3 -O verify.py

Both commands authenticate all eight complete public originals and exactly replay RESULT.json. The scripts use explicit require checks, not assertions that vanish under optimization. To intentionally regenerate the expected result during development, use python3 verify.py --write; ordinary review should not use that flag.

The checker verifies only the fixed D-source and two target shapes, their exact universal character identities, the degree/rank arithmetic in the quartic-image lemma, and the final negative V multiplicity. The local characters.py verifies its tensor-by-W recurrence against exact physical character values on all nine conjugacy classes. The pinned historical character program is not executed. No source-instance coefficient, point, parameter, jet, tensor, matrix, actual rank, scan, or historical quotient enumeration is evaluated.

The fixed historical frontier182.json is read solely to recover the stable IDs, exact ordered quotient pairs and original defects of the two proved shapes. Its geometric necessity is an imported theorem in the pinned full coverage note; it is not inferred from a JSON field or row count. The four labels are not new live-frontier counts.

The actual-map proof requires independent mathematical review of PROOF.md, particularly the coherent image versus saturation distinction, the saturated graph argument, and the strict-top injection into the actual internal derivative target. A successful checker run does not prove those geometric inputs.

The proof independently re-establishes the D-type cubic-kernel alternative. It does not depend on the unpublished local slice5 packet. It imports only the pinned public near-top visibility, actual ambient, strict-top and primary four-type results. It does not claim COV or exclude the remaining profile-(1,1) equality shape.
