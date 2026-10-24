# Independent bounded (2,1) review

The accepted result is the necessary restriction delta2 in {0,12}. The full
ordered (2,1) profile remains open. Read `REVIEW.md` for the independent
sheaf, torsion-completeness, finite-domain, and complete-flag audit.

Run `python replay.py` from any directory. All paths are relative to the
script. This regenerates `BOUNDED-RESULT.json`, `INDEPENDENT-CONTROLS.json`,
and `COMPARISON.json`, cross-compares all 31 tuples and all five residuals,
and replays both author and independent normal/optimized controls.

Only universal representation characters, abstract splitting lists, and
integer identities are computed. No actual-instance coefficients,
parameters, jets, matrices, or ranks are evaluated.
