# Clean-extraction replay

The final ZIP was extracted into a fresh temporary directory and replayed from its extracted package root, with no reference to the producer's working directory and no network use.

Commands:

    python replay_portable.py
    python -O replay_portable.py

Both exited successfully and produced identical output, also identical to the package's `normal.txt` and `optimized.txt`. Every manifest-listed file matched its expected SHA256, and the independently reviewed proof hash matched exactly.

The invoked proof control checked eight universal formal identities, including all four first-lift routes and the full ε² associator with arbitrary scalar h₂ and all six second edges. Its six deliberate convention mutations were rejected.

In a separate isolated extraction, appending one line to `PROOF.md` caused a checksum failure before the formal checker ran. That deliberate mutation affected only the disposable extraction. The packaged proof and all inherited dependency snapshots remained unchanged.

The replay ran only the supplied invented-word checker after checking hashes. No physical source, model, matrix, polynomial, point, jet, residual or detector was executed or evaluated. The geometric carrier/nonvanishing argument remains a written proof rather than an execution result.

`SHA256SUMS` binds the final package contents other than itself. The archive's external SHA256 is supplied with delivery and is not embedded in the archive, avoiding a self-referential checksum.
