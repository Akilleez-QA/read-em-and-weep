# Outer partition lowering: independently reviewed portable packet

Run with Python 3.10 or newer, standard library only:

    python -B check.py
    python -BO check.py
    python -B test_portability.py
    python -BO test_portability.py

The sources directory contains inert .txt files. They are hashed and parsed as text only; never rename, import or execute them. No repository checkout, network, physical objects or polynomial arithmetic is needed. The checker is anchored to the manifest digest and recomputes every SHA256, byte count and Git blob digest. The portability control copies the packet to a temporary directory and requires actual rejection of corrupted source bytes and a jointly rewritten source/manifest, under normal and optimized Python. It runs only the standalone checker.

PROOF.md gives the universal formal argument. REVIEW.md gives the independent verdict and exact limits. Pins identify exact sources and explicitly labeled review excerpts; excerpts have their own hashes and retain original hashes solely as provenance. Historical JC proof bytes and its complete two-paragraph diff to the later proof are included. Historical acceptance is not claimed for later implementation revisions.

This packet provides no physical arithmetic admission, realized detector value, source-order equivalence or obstruction verdict. Controls are source-wiring and formal-index evidence, not a general Python verifier or a proof of actual geometric pole bounds.
