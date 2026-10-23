# Independent whole-proof review

Verdict: PASS for the final bytes identified below. This is an independent mathematical review with bounded structural verification, not formal proof-assistant verification. The three published results are treated as authenticated inputs. Their precise statements and their uses in the new proof were checked against the complete local input copies.

## Reviewed final files

SHA-256:

- PROOF.md: `24ccacc3e8da0c6cb8e9fdc73bc07c92e6f50bdeb36ee7e0cca1af22e8415c2f`
- INPUTS.json: `29e37badfffa8f23da7fae158c46875b67d2fc18250d380408c1674bd278bfda`
- verify.py: `879c0f0f2a1b36c34d24c7033617b5b390fc911d2438c77d207161f941ab510e`
- REPRODUCE.md: `6905aa5c17c2c276819a7c041a00259eccc21c598f59051d0a2bdbcfa0eb5a95`

## Mathematical checks

1. NINTH supplies an actual derived complex in degrees one and two and identifies every derived fiber, without assuming its final rank. EXHAUST supplies dimension three and square exhaustion at every hyperplane, including the twelve exceptional parameters. SQUARE supplies the actual section bundle Y, its parameter twist, the equivariant symmetric-square identification, and the fiberwise injective square restriction. The new proof does not replace any of these actual maps by an abstract character-compatible map.

2. The finite/global section comparison is valid and self-contained. For B_H(3), every even layer after the seventh neighborhood has twist 3-k at most -5 and vanishing H0 and H1. Odd layers have no positive part. Thus positive sections stabilize under the actual restriction maps. For sufficiently large m, both H0(B_H(3-m)) and H1(B_H(3-m)) vanish; the latter is dual to H2(B_H(m-7)) and follows from positive Serre vanishing. This proves actual restriction is an isomorphism already at the ninth neighborhood. No formal algebraization theorem, uniform choice of the sufficiently large m, or negative-twist vanishing specifically at m=9 is needed.

3. The positive section bundle comparison does not incorrectly assume that the full H0 is constant. The finite normal projection onto R times T pushes the bundle to a vector bundle; its positive eigensummand is a vector bundle, with the indicated even-layer filtration. Ordinary cohomology and base change applies to that summand. The restriction of the actual global square bundle is therefore an isomorphism onto the positive ninth-neighborhood section bundle, and its further plane restriction remains precisely s.

4. The projective-bundle convention, Cartier divisor, and all parameter twists agree. They give omega_X/T=p*O(-4) times pi*O(1), O(E)=p*O(1) times pi*O(-1), and omega_D9/T=p*O(5) times pi*O(-8). The relative Cartier surface family is flat and Gorenstein even on its nonreduced fibers. The equivariant trace pairing on B then makes the dual coefficient B(3) times pi*O(-8). The odd canonical normal factor and the odd ninth-divisor factor cancel, so positive cohomology pairs with positive cohomology; there is no omitted inversion-character swap.

5. Duality is correctly applied to the full locally free sheaf on D9 before taking cohomological eigenspaces. Fiberwise Serre duality first establishes constant positive h2 equal to three. The actual derived fiber complex then proves constant rank twelve for Theta and constant kernel dimension eighteen. Only afterward does the proof use bundle-level duality and underived base change to identify the cokernel with Q dual times O(8). Consequently the conclusion excludes torsion and exceptional rank drops, not merely generic rank changes.

6. Naturality gives the claimed actual image, not only its numerical invariants. The top normal-layer inclusion is the map inducing U15 onto the cokernel. Its dual is restriction of the dual section to the reduced plane, with the O(-8) parameter factor. Equivalently, the universal Cartier-thickening residue pairs the top z^8 layer with the constant term. Under the actual square-section identification this is s. Thus the quotient map is s dual times O(8), and the image is the annihilator bundle, equivalently S12 dual times O(8). The local residue explanation is a universal identity, not evaluation of an actual HM jet. Named representation identifications retain the scalar choices explicitly acknowledged in the proof.

7. Degree-one relative duality gives ker Theta equal to the dual of the positive R1 of B(3) on D9, twisted by O(8). Fiber duality and the established constant rank justify local freeness and base change for this middle cohomology. The statement deliberately concerns finite-neighborhood H1 and does not identify it with global hyperplane H1 or the opposite bundle C. All rank and degree totals, including image degree 78 and kernel degree 42, agree with the exact sequences.

## Reproduction and scope checks

Both `python3 verify.py` and `python3 -O verify.py` were independently run successfully. The explicit checks remain enabled in optimized mode. The verifier authenticates the three input Git blobs, checks the displayed dualizing and Serre exponents and inversion parity, and verifies the fixed rank/degree arithmetic. Its limited role is accurately distinguished from the geometric argument in REPRODUCE.md. The reconstruction instructions preserve immutable input bytes and require only the Python standard library in addition to retrieval of the named source files.

No actual HM coefficients, points, jets, derivatives, matrices, instance ranks, or scans were evaluated. No external state was changed. This review authored only REVIEW.md. It makes no additional conclusion about the top polar map, vertex scalar, opposite-bundle splitting, or source/frontier ledger.
