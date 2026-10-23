# Independent verification: nonzero Type I radical P row

Reviewed 2026-10-23 against frozen artifacts:

- PROOF.md SHA256 `8ebf466131d0ceb3f57d1cf28578978ec875d3487985549d793a3ba76882a060`
- verify.py SHA256 `888ec6a8e92c5bd066caef671722a90e7098100db03187fa62661c0f01d37b0b`

## Outcome

The new nonzero-row theorem is valid relative to the five pinned normal-form interfaces. Its intersection with the previously reviewed joint-annihilator theorem validly removes the rank-zero conditional footprint. No mathematical blocking issue was found. Publication still requires replacing the explicitly marked local dependency with its immutable published pin; that provenance requirement is separate from the checked theorem.

## Adversarial checks

1. The coefficient map is an injective G-map D*→Sym8 W*. Identifying D* with Sym4 W* is permitted by the stated irreducibility and self-duality. This does not assert that the degree-eight embedding is SL2-equivariant. The proof only uses the usual SL2 decomposition of its domain W* tensor Sym4 W*, which restricts to the distinct G-irreducibles S and T.

2. Both channels of multiplication are genuinely nonzero. The formal pure tensor x tensor x^4 belongs to T and has nonzero image x r_0 in the polynomial integral domain. If the S channel vanished, all four kernel-of-quartic-multiplication tensors y tensor f_i minus x tensor f_(i+1) would vanish. Their recurrence implies x^4 divides r_0 and r_i=h x^(4-i)y^i, not merely an unproved dimension coincidence. Equivariance of multiplication by h forces h invariant. The absent degree-four invariant gives the contradiction. This proves the claimed isomorphism and absence of arbitrary linear syzygies, not just equivariant ones.

3. The derivative is a nonzero equivariant first-polar bundle map W O(-7)→D O. Its Hom multiplicity is one because D tensor W=S+T and Sym7 W=Wp+T. Twisting both sides by -2 gives the exact domain Y=W O(-9) and target D O(-2). The polar identification therefore uses the correct degree and coefficient dual conventions.

4. For arbitrary quadratic p, annihilating the first polar gives p r=0 by Euler's identity. The product rule then makes each row of each derivative of p a linear syzygy. Since the preceding argument excludes every such syzygy, p is constant and homogeneous of degree two, hence zero. No actual point, derivative value, or HM coefficient is evaluated in this universal polynomial argument.

5. Under the hypothetical zero P row, the injective restriction of the two-dimensional J lies in the two-dimensional Hom_G(Y,2D O(-2)); it is therefore the entire Hom space. The injectivity premise comes from Y spanning the actual constant support A+V+D. Thus the constant P projection annihilates the generator into each D copy separately, which is exactly what is required to apply the polar lemma. This is not an inference from one chosen radical map.

6. Saturation is valid: C O/F_D is an extension of the vector bundle C O/F by F/F_D, hence locally free. The induced quotient H0 O/F_D is a subbundle quotient of rank one (it embeds in C O/F_D), hence torsion-free and locally free on the smooth curve. Its degree is 20. Any difference between its G-linearization and the standard one is a one-dimensional character, and the binary icosahedral group has no nontrivial such character. The same applies to the degree-28 line. The restricted quotient map is nonzero because otherwise a nonzero constant subspace would give nonzero global sections of F=(P+2D)O(-2). Consequently it would be a nonzero invariant section of O(8), contradicting the pinned symmetric-power decomposition.

7. The preceding argument proves r≥1 independently of Q compatibility. Intersecting with the prior conditional bound r≤1 gives exactly r=1 only under full-J compatibility. The remaining filtered 32→28 reduction is inherited from the separately checked prior theorem. The argument does not prove r=2, exclude full-J compatibility, or remove Type I or a catalogue pair.

## Executed checks and limits

Both `python verify.py` and `python -O verify.py` returned:

    PASS: 136 checks; five immutable sources and one explicit prior candidate.

The exact local dependency hash matches the independently reviewed joint-annihilator proof. The tests authenticate inputs and check representation recurrences and universal polynomial identities; they are not a proof-assistant certificate or actual-HM computation. This review verifies the new deduction relative to the pinned interfaces, not the entirety of their upstream geometric proof chains.

## Final publication-provenance amendment

The previously noted local-dependency prerequisite is now resolved. PR954 is pinned in INPUTS.json at commit `1dfd8f6b2b7d39d41de2619737b6cf4cfb951e75`, path `research/hm/source126-typeI-joint-annihilator/PROOF.md`, Git blob `e5ac339ac33ab6b7f9d467fcada545bceac1d852`. Its retained bytes have SHA256 `0957ba7fb53f03b99c98fe8d16fd00bdc000d264055d70018bfdac54345b96b9`, exactly the previously reviewed dependency. No mathematical premise changed.

The final proof provenance paragraph and verification-scope wording now identify six immutable sources. The checker replaces the standalone local SHA check with both SHA256 and Git-blob authentication through the manifest. The final artifact hashes are:

- PROOF.md: `2bd9e58004ab319366a2e1e16244de440a5f2740a64c2c9e523ce61e403f2028`
- verify.py: `10734afc5db0564231e85ed77f937151d2ea046cfd2d646de57c1290f9e43bca`
- INPUTS.json: `433e1de5f13e9be1de9b00a61798e796f22ad4d48196d232f1eb43e578ff8deb`

Both normal and optimized final checker executions passed 137 checks and six immutable sources. The preceding mathematical assessment applies to these final bytes without any remaining local-dependency caveat.
