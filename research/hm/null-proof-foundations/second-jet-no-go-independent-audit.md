# Independent audit of the second-jet survivor

The formula and scope in `m0-second-jet-survivor.md` are correct. The normalized mixed block is (1/4) sum epsilon J_ij H_kl. Differentiating determinant one gives tr(H_ij)=tr(L_i L_j) and tr(J_ij)=tr(U_i U_j). The exact2x2 identity tf(XY)=[X,Y]/2+tr(X)tf(Y)/2+tr(Y)tf(X)/2 yields the displayed coefficient1/8 and retains all scalar-trace correction terms.

On A=B=I with first jets zero, k and its first derivatives vanish. Thus quadratic and mu terms vanish; full gerbe contributes only a central term, which disappears under exact tracefree projection. No assumption b=0 is necessary. The remaining four-commutator expression is antisymmetric when the A/B second-jet arrays are exchanged. Nilpotent determinant-one shears with B_13=E12,A_24=E21 give diag(1,-1)/8, checking the factor and sign. The note's exchanged example gives the correspondingly exchanged commutator sign.

The strengthened labeled-edge argument is also valid: a correction depending on each edge's transition2jet alone restricts to f_bc(b)-f_ac(a+b)+f_ab(a). Its mixed finite difference cancels both single-edge rules and is symmetric in(a,b), even if the three fixed-edge rules differ and are not polynomial. It therefore cannot cancel the nonzero antisymmetric mixed interaction in characteristic zero. A value/first-jet-only target has zero such mixed interaction.

This excludes only universal transition-local corrections with no independent vertex data and jet order at most2. It does not establish a nonzero actual HM obstruction, survival under the detector, a resource lower bound, or an impossibility for higher-jet/source-specific/vertex-dependent corrections. No physical source values were computed.

## Dependency scope

Companion references are identified by basename. A referenced file not supplied with this collection is an external prerequisite, not an embedded proof or a verified relative link. The reading order and unresolved conditions are listed in `proof-notes-index.md`. Reported test results describe the source audit; this proof copy does not by itself constitute a new test run.
