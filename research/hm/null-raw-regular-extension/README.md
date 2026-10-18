# Conditional raw regular-extension packet

This offline packet independently reviews direct raw scalar pole estimates and their conditional J3/suffix-clearing consequence. It does not publish anything or authorize physical execution.

Run from any working directory with standard-library Python 3:

    python /path/to/packet/check.py
    python -O /path/to/packet/check.py
    python /path/to/packet/test_portability.py
    python -O /path/to/packet/test_portability.py

All geometric and production sources are inert `.txt` inputs. The checker only reads bytes, parses AST/JSON and performs integer ledger/index checks. A fixed digest enforces the input manifest; each input SHA-256 is enforced. `test_portability.py` copies the entire packet to a temporary directory and runs positive, corrupted-source, and jointly corrupted source/manifest controls under normal and optimized Python. Temporary copies are removed automatically.

Read PROOF.md and REVIEW.md for the theorem and its genuine hypotheses. In particular source hashes, declared degrees, and pole-budget arithmetic do not establish actual homogeneous primitive semantics, all-chart physical frames, determinant-one transitions, complete F bounds, raw closure, or HPL identities. The local controls do not import production modules, evaluate the physical model, form actual model polynomial products, or generate any detector value. The trust root is the reviewed checker; this is not resistance against an attacker replacing that checker too.
