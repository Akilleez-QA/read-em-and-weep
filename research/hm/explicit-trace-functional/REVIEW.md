# Independent mathematical review

Reviewed PROOF.md SHA-256: 17621b0e0171b22658624d1d664f62a27d07ee08f1cf87b2f4dc910ff01c9622.

Verdict: the stated universal identities and their conditional consequences are correct under the regular-pair, characteristic-zero, and polynomial harmonic-coefficient assumptions.

Checks performed:

- Read the dependency proofs for trace-target reduction, canonical first-normal lift, modular elimination, scalar-slope factorization, and source-family homogeneity. The trace-kernel descent and the unique degree-two residue representative are applied with the stated normalization.
- Independently expanded the diagonal and lower contributions to Psi modulo the unspecified cubic F. The diagonal coefficients are 9/22, -2/11, -2/11; the lower coefficient is 1/11. Differentiating the exact trace identity, rather than differentiating an arbitrary quotient congruence, cancels the terms involving G derivatives. The remaining expression is tau2(f,r)/352. The scalar u cancels exactly.
- Checked the upper-only trace representative y=t/u. Its contribution is Hess(g)t/144 + tau2(g²,t)/198, proving the full one-division formula with correct homogeneous degree eight.
- Checked Hess(f)(1,t)=6FF''-4(F')² and the second-ideal coefficient 1/44. This proves annihilation of f³S3, the nine-dimensional source quotient, and the induced Hessian multiplication map.
- Checked the multiplicity argument over an algebraic closure. The gcd degrees for the three cubic multiplicity partitions are 0, 2, 3, so the last-layer ranks are respectively 3, 1, 0. Field extension does not change rank. No actual multiplicity type is determined.
- Checked the exact lift-transport correction: changing T by ell A0 changes Psi(D) by ell(fx+gy), giving [ell e/(ug)]. It vanishes on fS9. Section 4 now correctly distinguishes canonical and actual fixed-frame lifts and uses all primed data consistently.
- Checked the final degree exclusion: V_h' has diagonal degree zero, upper degree minus two, and lower degree two. Its polynomial upper entry therefore vanishes, and tr(nV_h') is divisible by f. The conclusion requires the stated polynomial harmonic-coefficient interpretation.
- Inspected and executed verify.py, which passed its bounded free-jet symbolic identities and rational denominator checks. These are symbolic computer-algebra checks, not proof-assistant formal verification.

No actual selected form, source, point, matrix rank, or model was evaluated. Surjectivity of the descended functional, when f is square-free, does not imply surjectivity or nonvanishing of the source map K. The note correctly leaves actual source values, the separate fourth-Bockstein quotient, and algebraicity unresolved.
