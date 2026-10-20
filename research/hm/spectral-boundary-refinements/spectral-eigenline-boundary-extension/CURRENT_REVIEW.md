# Current mathematical review

Reviewed 2026-10-20. The proof and retained refinements pass independent mathematical text review under the premises in DEPENDENCIES.md. This is not formal proof checking or an actual source-instance evaluation. Historical audits remain historical.

The finite locally free quadratic algebra embeds in its separable generic algebra over integral Y, hence is reduced. Lambda is a nonzerodivisor because lambda squared is a nonzero regular section on Y. Constant geometric rank on the reduced cover supplies the line subbundles; the local cyclic vector proof then gives the actual matrix equivalence diag(1,lambda,lambda squared), without a PID assumption. The determinant has Cartier divisor exactly 3D, and the sign convention gives the eigenline-dual sum 3r−2H. Global generation and finite-surjective descent prove nefness; the nilpotent components use r=h+2t and H=3t. Neither smoothness nor reducedness of D is used.

External premises: PR269 at 264b18521dd174e3e4ae185b8be51f9f6c303d87 supplies the reduced projective incidence, universal twisted traceless rank-two endomorphism, characteristic polynomial and regularity/rank-one exclusion. Nilpotent flag formulas are those of the referenced structural package; they were also directly checked in PR271.
