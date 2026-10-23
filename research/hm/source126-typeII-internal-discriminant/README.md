# Hidden Type II symbol: exact discriminant rank strata

Conditional on either P-surplus footprint of PR961, the complete internal
first symbol is lambda times binary-quadratic multiplication on A plus
mu times the first transvectant on D. The prior theorem forces lambda≠0;
mu remains unselected.

- mu=0: rank three for every nonzero quadratic.
- mu≠0: rank four on the discriminant conic, rank five off it.

This classifies the full hidden symbol, not the original first Bockstein
(which still vanishes) and not the original maximal-rank problem.

PROOF.md proves the universal result. INPUTS.json pins PR944 and PR961.
Run python verify.py and python -O verify.py for 127 exact checks.
The symbolic minors 384 mu^4 and 64 lambda mu^4 certify the two nonzero-mu
normal forms. Bounded examples are universal binary forms, not HM instances.
