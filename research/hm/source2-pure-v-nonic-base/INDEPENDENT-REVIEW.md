# Independent mathematical review

Verdict: PASS, with no mathematical blocker. This is a mathematical review and
reproducible diagnostic replay, not a proof-assistant verification.

## Scope and conclusions checked

Read the complete proof, verifier, all three retained immutable inputs, and
result. No selected actual HM coefficient, source, direction, or instance was
used. The claims are universal for every nonzero element of the conditional
two-dimensional gate; the zero/nonzero status of the actual gate remains open.

- The invariant gcd line is genuinely invariant because A5 has no characters.
  Exact invariant dimensions through degree nine, together with the conic
  exclusion from H0(J(1))=D, leave only a non-conic sextic gcd.
- The unique residual cubic P-covariant has the required six reduced basepoints
  by the pinned PR1005 proof. Its ideals equal m there and are unit elsewhere.
- The colon ideal ((u²,v²):m)=m² is correct. At the ten other axes, the rotation
  fixes the axis vector and hence the sextic fiber, while both tangent weights
  are nontrivial; a vanishing invariant sextic therefore has no linear term.
- If a sextic had repeated components, their reduced product would have degree
  at most three and invariant divisor, hence an invariant polynomial. The only
  possible positive degree here is the discriminant quadratic. Its exclusion
  proves reducedness. The normalization-genus bound of fifteen singular points
  is valid also for reducible reduced sextics. Sixteen is impossible.
- The full projective stabilizers, rather than cyclic subgroups alone, force
  the two jet Hom spaces to be one-dimensional. The odd O(9) reflection sign
  is retained, and twisting the relevant two-dimensional irreducible by sign
  preserves its isomorphism class. The restrictions of P are correct.
- At a C5 axis, I_Z=(u²,v²) has I_Z∩m³=mI_Z. Thus the quadratic generator
  space is exactly I_Z/mI_Z, and a nonzero equivariant jet spans it. Nakayama
  gives equality of the whole local ideals, not just their quadratic images.
  At a C3 axis the same argument uses m/m².
- Absence of a fixed component permits two general members of the component
  system without a common curve. Their local intersection lower bounds give
  6·3²+10·2²=94>81. Thus the joint jet map is injective, forcing both scalar
  functionals to be nonzero and their kernel lines to be distinct.
- On each exceptional line the other functional is nonzero. Therefore the
  exact local behavior at the other orbit is retained, and the lower bounds
  46 and54 follow. No equality with m³/m², exact total length, or absence of
  additional finite basepoints is inferred.

## Authentication and reproducibility

Fresh independent GitHub fetches at the stated commits returned these exact
blob SHAs, which agree with the retained files and INPUTS manifest:

- PR1025: d036adcf5bc2bfc53e07cd752ff180c5993251f7.
- PR1005: ba88e70e50342eef9c92db9053789cb238802dee.
- PR1000: 0ca1301de04a630cb184c4429f5b59e09698c6c9.

Both python verify.py and python -O verify.py pass, with outputs byte-identical
to one another and to RESULT.json. Hashes of the reviewed files:

- PROOF.md: 6c6f88789501483d4ae738894f68afbf9b3d95a6d850d1cee51ea7ebd256a1bb.
- verify.py: 218735f32738e1c043cf8f74301c7b5b5093d11721d0649f4ff8dbef7dfe79be.
- INPUTS.json: 24e07e81ec1349f64c7ba170a61bff83dede1e99cc0609f385b8c9ef496074c0.
- RESULT.json: b38bee3e42364f089523d0d840bdb51ef41b4de319891a04a4f96c8b3e413299.

