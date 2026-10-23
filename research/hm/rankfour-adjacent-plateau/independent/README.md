# Portable independent review: rank-four adjacent plateau (2,3)

Verdict: PASS conditional on the actual geometric source inputs. Only this ordered maximal rank-four plateau is excluded.

Run `python3 check_package.py` from any directory. No third-party Python packages or network access are needed. The command authenticates every listed file, replays the independent checker and the author's frozen checker in ordinary and optimized Python, and reruns six fail-closed negative controls.

- `REVIEW.md`: independent complete proof audit, including endpoint saturation, physical parity, both exact sequences, every cohomology correction, and scope limitations.
- `verify.py`: independent exact-class arithmetic checker, with no author-code import or quotient-shape enumeration.
- `RESULT.json`: independent deterministic result, 222 checks.
- `test_controls.py`, `CONTROLS.json`: six genuine rejected mutations plus both successful baselines.
- `author/`: exact reviewed proof, verifier, result, and sole original source input.
- `MANIFEST.json`: SHA-256 and byte counts for this exact portable review.

The source note and proof are fully included; the package has no coordination transcript or abandoned quotient-enumeration scratch. The checker authenticates and tests universal consequences, not the truth of all imported geometry. No actual-instance coefficients, parameters, jets, matrices, or ranks are computed.
