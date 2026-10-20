# Parameter rigidity under equivariant formal coordinate changes

This slice extends [PR300](https://github.com/Akilleez-QA/read-em-and-weep/pull/300) beyond fixed-ring module isomorphisms. Over a local Artin C-algebra A, the displayed parameter remains recoverable from the completed family even after a continuous A-linear formal coordinate automorphism commuting with the fixed H action.

The proof treats nilpotent constants, completed Ext base change, semilinear contravariance, and the initial relation module explicitly. It includes a nonlinear automorphism illustrating the enlarged equivalence relation. Consequently the tangent direction remains nonzero modulo this coordinate-change group, and all finite-order parameter jets remain separated.

- PROOF.md: theorem, exact assumptions, derivation, and scope exclusions.
- DEPENDENCIES.md: exact parent commits and independent inputs.
- INDEPENDENT-AUDIT.md: independent proof review bound to the final proof hash.

This does not cover the normalizer of H, arbitrary coordinate changes, coefficient-algebra automorphisms, versality, or actual HM/source realization. No selected-source evaluation or large computation is involved. The six pure diagonal source conditions remain separate.
