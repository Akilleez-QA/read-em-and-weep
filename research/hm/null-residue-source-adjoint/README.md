# Complete-source adjoint remainder

An exact source-bound reduction of the complete extracted scalar to rational divergence plus an explicit remainder. No actual retained value or vanishing conclusion is established.

Read PROOF.md and independent/REVIEW.md first. Frozen source inputs are inert .txt files: never import or execute them. The checkers use only static AST/hash inspection and invented free differential symbols. Dependencies contain supplied prerequisite proof texts; references not included there remain external prerequisites. Their old reported tests are not new runs by this packet.

## Offline replay

Use Python 3 and SymPy 1.14.0 (requirements.txt). From this directory:

    sha256sum -c SHA256SUMS
    python -B check.py
    python -BO check.py
    python -B independent/check_kernel.py
    python -BO independent/check_kernel.py
    python -B independent/tamper_controls.py

The tamper script tests both normal and optimized modes and writes only temporary disposable copies. The dependency residue-route packet has its own documented checks, which can be run separately; they are not required by the new checker. Output records are under results. Formal control counts support the written arguments; they do not prove geometric premises or authorize production evaluation.

The public proof adds an explicit tau^-4/finite-tau=1 clarification. It does not append a new frame multiplier. The new public checker strengthens integrity and pair-field validation. Original input bytes and the branch/contract records are unchanged. No builder with machine-specific paths or execution-history files is distributed.
