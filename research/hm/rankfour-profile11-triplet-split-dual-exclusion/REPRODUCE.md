# Reproduce the bounded checks

Use Python 3 with only its standard library:

    python verify.py
    python -O verify.py

Both runs must report identical PASS output, including 34 explicit checks, 6373 proof bytes and proof SHA256 57a435c44d7de7f2ef0e97b168530acc32aa37dc25258adfff48ba06f848cc82.

The exact isolated replay set contains six files:

* PROOF.md
* INPUTS.json
* REPRODUCE.md
* verify.py
* inputs/dual-extension.md
* inputs/mixed-jet-pairing.md

Copy only those files, retaining their relative paths, into a newly empty directory. Run both commands there and compare their output bytes. Confirm that all six selected files remain byte-identical after both runs. Exclude LOCAL-SOURCE-FETCHES.json, all other LOCAL* files, scratch audits, reviewer material, prior outputs and caches. No characters.py or other helper is needed.

The two inputs were freshly fetched in full at their immutable repository commits. INPUTS.json records their exact paths, URLs, complete UTF8 lengths, SHA256 hashes and Git blob SHA1 hashes. The verifier independently hard-codes both complete pins and the current complete proof length/hash; changing the manifest cannot replace these pins.

The bounded checks use only fixed diagonal twists, ranks, degrees and line-bundle Hom arithmetic. They do not evaluate any selected actual coefficient, scalar, parameter, point, jet, tensor, matrix, instance rank or normalization. There is no new character calculation, broad scan, large computation or quotient connection. Every check uses an explicit require call and remains active under -O.

The actual auxiliary full span and fourth-jet containment, exact constant dual pairing, principal-parts construction, restriction to the incomplete system, and distinction between the excluded O(-4) subline and retained O(-4) quotient require independent entire-proof review. This executable authenticates its sources and checks arithmetic; it is not a substitute for that geometric proof. The conclusion is conditional non-splitting, not exclusion or realization of the residual branch, and uses no K1/K3 assumption.
