# Canonical cubic splitting and regular reconstruction

This directory records the October 19, 2026 results behind the [canonical cubic splitting](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6277692474) and [regular dual reconstruction](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6279132359).

The splitting supplies two canonical weighted components. The reconstruction is regular even on branch fibers, but supplies a primitive only if the component primitives and representative-comparison boundaries are supplied. **The cubic result itself proves no obstruction vanishing.** At that historical stage all thirty retained conditions were unknown. Later symmetry reductions are not part of this package.

## Read in order

1. The earlier [filtration-only statement](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6276362114) and [weighted remainder](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6276688181).
2. [PROOF.md](PROOF.md), Part I: the actual algebra structure corrects the stronger no-canonical-complement claim. The bare vector-bundle statement remains valid.
3. [PROOF.md](PROOF.md), Part II: coefficient-extraction pairing, globalization, and conditional primitive reconstruction with signs and all comparison boundaries.
4. [AUDIT.md](AUDIT.md): the two corresponding mathematical audits.

The source foundations remain in [PR79](https://github.com/Akilleez-QA/read-em-and-weep/pull/79), including the [pinned complete raw source](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-second-order-raw-closure/PROOF.md). Additional dependencies are the [complete canonical mixed source and correction equation](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6271101716) and [source-to-canonical comparison](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6274541018). Existing source files are referenced, not copied.

## Exact universal checks

The two Python scripts are the existing exact scalar verification artifacts. They require Python 3 and SymPy; the packaged checks were verified with Python 3.12.14 and SymPy 1.14.0. Install the pinned dependency in an appropriate Python environment:

```sh
python -m pip install -r requirements.txt
python check_splitting.py
python -O check_splitting.py
python check_reconstruction.py
python -O check_reconstruction.py
```

All checks use explicit exceptions, not assertions, and remain active under `-O`.

- `check_splitting.py`: the six-variable factorization cubic, root-weight sum, squared Vandermonde, quartic discriminant identity, nonzero universal coefficient, and multiplication table.
- `check_reconstruction.py`: coefficient-extraction Gram matrix and unit determinant, dual basis, functional reconstruction, trace normalization, frame covariance, and formal boundary substitution.

These verify polynomial identities in independent formal variables. They do not calculate an actual obstruction value, supply the missing weighted primitives, or verify the imported HM cohomology dimensions. The global determinant-line and sheaf/Čech arguments are justified in the proof and audit, not by scalar tests alone.


## Published predecessor pins

- [research/hm/null-actual-pair-comparison](https://github.com/Akilleez-QA/read-em-and-weep/tree/1c5ccbd7e2e5e1532fdcdd13ba4734ab65247252/research/hm/null-actual-pair-comparison)
- [research/hm/null-mixed-module-equation](https://github.com/Akilleez-QA/read-em-and-weep/tree/a4697a27a8077cdc16e917aebca468dfa6277738/research/hm/null-mixed-module-equation)
- [research/hm/null-canonical-alternating-transfer](https://github.com/Akilleez-QA/read-em-and-weep/tree/ff241cdfd7c7606f5dcb17cb1fd1282e61c73994/research/hm/null-canonical-alternating-transfer)
- [research/hm/null-retained-weighted-remainder](https://github.com/Akilleez-QA/read-em-and-weep/tree/4edb97ceeb159778fa20ffd33c0e540af1292e06/research/hm/null-retained-weighted-remainder)


## Historical source frontier

Statements in this packet that leave thirty obstruction coordinates or values unresolved describe the historical stage of these preserved notes, not the latest project verdict. For subsequent developments and the current project status, see [project status, issue #92](https://github.com/Akilleez-QA/read-em-and-weep/issues/92). Original arguments and historical review scopes are preserved; publication performs no new source evaluation.
