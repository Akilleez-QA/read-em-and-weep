# Second mathematical review

Reviewed proof SHA-256: ed36858dc2b7d5bf24df12a167739867d5333febb821d2fa590ae59cfd797e6c.

Verdict: PASS relative to the pinned transport, invariant-pair, and cohomological inputs. This is mathematical review, not formal verification.

For the frame lemma, evaluations at all closed points span the dual of the finite-dimensional section space. The open set of tuples giving independent evaluations intersects the frame-open set in the irreducible product of projective spaces. A projectivity matching the fixed source frame then forces restriction injectivity. Independence of these moving evaluations is algebraic and open; there is no assertion that arbitrary six points separate the sections.

The pure-power rational normal quartic is in the invariant zero locus by torus weights and positive homogeneity, and any five of six distinct points are independent by degree-four interpolation. This supplies the precise six-point frame needed. Nondegeneracy of I gives irreducibility; hypothetical division of J by I would give an invariant linear form, impossible for Sym4. Thus the transported pair is coprime throughout.

The smooth quadratic orbit surjects onto all smooth quadrics. Its primary-good and no-contained-line preimages are nonempty opens. Intersecting these with the independently established separation-open in irreducible PGL5 is legitimate. PR458 only needs injectivity of the tuple-to-quintic map here, so full avoidance of the common zero scheme and the 25 lines is not assumed. Primary coverage removes the remaining primary quotient. The geometric cohomology interpretation is used through the explicitly pinned transport and endpoint inputs.

For the curve, det(Id+t(G-Id)) is nonzero at both endpoints, so the principal open is nonempty and contains 0 and 1. The preimage of the good open contains 1; its complement is a proper closed subset of this open affine line and hence finite. No good-special-fiber inference or torsion-length bound follows. The bundle remains fixed while coefficient/root geometry moves; simultaneous transport of the bundle would be a different assertion.

The proof genuinely establishes genericity on the constrained coordinate orbit, not merely the ambient independent coefficient space. It still leaves the original positioning, retained source values, six pure conditions, module lifting and quantization algebraicity unresolved.
