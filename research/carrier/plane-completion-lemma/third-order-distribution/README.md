# Byte-preserving third-order distribution

The two frozen third-order packages use exactly the same 23,833,465-byte THIRD_MIDDLE_COCHAINS.json. It is distributed once as THIRD_MIDDLE_COCHAINS.json.gz here. Restore it into both sibling directories before running their unchanged checks. This changes distribution only; it does not change the cochain bytes, mathematical scope, earlier packages, frozen manifests or verification programs.

From the repository root, run:

```sh
python3 research/carrier/plane-completion-lemma/third-order-distribution/unpack_cochains.py
```

The unpacker requires only the Python standard library. It verifies the compressed and reconstructed SHA-256 digests and exact sizes before writing. It accepts no output path, refuses symlink targets/directories and different existing files, and treats already-correct files as verified. New files are installed using a same-directory atomic hard link without overwriting an existing destination. A filesystem supporting hard links is required; a failed run must be resolved explicitly rather than bypassing checks.

Then verify both original SHA256SUMS files and run the original programs:

```sh
cd research/carrier/plane-completion-lemma/third-middle-construction
sha256sum -c SHA256SUMS
python3 construct_third_middle.py
python3 verify_third_middle.py
cd ../third-normal-comparison
sha256sum -c SHA256SUMS
python3 construct_third_section.py
python3 verify_third_section_equations.py
```

The middle constructor requires SymPy. The separate middle verifier and the section programs use standard-library Fraction arithmetic. The programs write generated receipts in their own package directory. Python's -O mode is supported and was verified separately; mathematical checks use exceptions, not removable assertions.

## Integrity and reconstruction

- Raw SHA-256: 011ba80d06f7b47a077845f377e9b22a5a9e51d808804e88e2ba4bf66c2306cd
- Raw bytes: 23,833,465
- Compressed SHA-256: 5033872e143d1e93d650698659a13853af0d7332c405b5454aacab96cfa7196c
- Compressed bytes: 875,342

The gzip was generated with Python 3.12.14 using gzip.GzipFile, compression level 9, an empty embedded filename and mtime=0. Those choices remove filename and clock variation. Recompression under a different zlib version need not produce identical compressed bytes; reconstruction must always reproduce the exact pinned raw bytes. The included compressed file is the publication artifact.

Each original SHA256SUMS remains unchanged and covers the restored raw file. It is expected to report that file missing before unpacking. The additive manifest.json identifies all distributed files, each frozen original manifest, and the two reconstructed targets. Its own identity is anchored by the immutable Git commit.

## Mathematical boundary

These packages give the checked five-parameter structured lift modulo h^4 in the stated gauge. The middle package alone does not supply the section; the second package adds the third-order section and direct equation check. No fourth-order or all-order lift, ancestor identification, algebraic carrier, reflexive-hull base change or defect conclusion is asserted.
