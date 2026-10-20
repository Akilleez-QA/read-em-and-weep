# Independent audit: uniqueness of the non-reflexive boundary

PASS for PROOF.md SHA256 5ce00bce295e7d5ac4f4ca27a804c2b49022607fa8ba74bc8c638170baad08c2.

The argument was checked independently from the displayed slope and Hom sequences, with PR228's fiber theorem as its explicit input.

1. A rank-s image for 0<s<r would have slope strictly greater than the stable source, by the kernel inequality and degree additivity. Its inclusion in the semistable target gives the opposite weak inequality. Thus every nonzero map has full rank. Torsion-freeness kills the rank-zero kernel, and equal Hilbert polynomials, not stability alone, eliminate the cokernel. The rank-one ideal-sheaf example correctly exposes why the numerical hypothesis is needed.
2. Properness and coherence make global Hom a finite DVR module; target flatness makes it torsion-free. Flat localization of finitely presented Hom and the finite affine gluing kernel identifies its generic fiber. A primitive lattice representative of the generic isomorphism therefore exists.
3. The exact target sequence gives an injection Hom/pi Hom into special-fiber Hom. Surjectivity is neither used nor asserted. The primitive map specializes nontrivially, so the stable-to-semistable lemma applies.
4. Cokernel vanishing follows from special and generic Nakayama checks. Target flatness is then essential in preserving injectivity of the kernel sequence on the special fiber; that yields an integral family isomorphism. A scalar renormalization of the generic marking is expressly permitted and distinguished from extending the original marking unchanged.
5. Finite ramified DVR base change preserves the known flat family and its stable depth-one special fiber. Competing flat families have the same Hilbert polynomial by their common generic fiber. Hence no slope-semistable reflexive replacement can occur on the fixed projective space, even without equivariance.
6. Reflexive hull and the length-one quotient are functorial consequences of the unique special fiber. Equivariant generic comparison remains equivariant after extension because the base action fixes the uniformizer and target flatness detects maps generically. The statement correctly excludes unstable fillings, changed generic fibers, zero/infinity, and an assertion about the actual HM problem.

This is a rigorous family-level exclusion of replacing the boundary by another semistable reflexive sheaf, not a claim of proper moduli representability. No formal checker, source-instance evaluation, or numerical test was used.
