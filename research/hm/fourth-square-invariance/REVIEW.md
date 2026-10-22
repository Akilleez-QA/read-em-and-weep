# Independent mathematical review

Verdict: PASS, conditional on the three pinned input theorems listed in PROOF.md.

Reviewed PROOF.md SHA-256:
`2d9eca985d88cfe26fa107cd5a202c2d774fc68de394ce47d8864b56ac9e3233`.
Reviewed verify.py SHA-256:
`adfe2b8d8be5a0fd655dfc0579a5558fc81793f8a4a84759930f3ce6e32572b1`.

The review independently checked:

1. Multiplication by q^2 uses the actual two-neighborhood module, not an unjustified ambient extension of U_a. Restriction of the other factor to 2Q makes the square-invariance argument valid, including on the singular locus.
2. Cayley-Hamilton and the last scalar layer produce a unique even section sigma of twist14. The local trace-free lift argument proves regular divisibility by a^2 and gives the global twist10 quotient tau without inverting a along its divisor.
3. The exact local trace image is the square of the full Serre ideal. The local scalar criterion and positive global vanishing imply the stated local/global equivalence, but do not establish the remaining local containment.
4. The invariant-line argument uses only q-regularity and reducedness of Q for its two cancellations. Its converse gives an intrinsic kernel line on the regular nilpotent locus. It correctly avoids claiming uniqueness of all invariant lines over a nonreduced base.
5. Integrality, nonzero source restrictions, and torsion-freeness justify the sharp nilpotency index2-or4 conclusion. Sigma is not identified with beta4 or with an obstruction to arbitrary adjoint extension.

The opening hypothesis explicitly requires nonzero restrictions of a and h to Q; this is necessary for the cancellation, nonempty-open, and sharp-index conclusions.

The bounded standard-library verifier was read and independently rerun successfully. It checks universal polynomial identities, twists, and elementary q-orders only. It does not verify the imported geometric theorems, evaluate any selected source instance or sigma, or constitute proof-assistant certification.

The unresolved mathematical question remains whether sigma vanishes, equivalently whether the stated local square-ideal containment holds everywhere. No actual-value claim is approved by this review.
