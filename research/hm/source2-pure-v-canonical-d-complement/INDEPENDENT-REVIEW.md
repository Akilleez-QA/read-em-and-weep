# Independent review: canonical quartic homotopy complement

## Verdict and artifacts

**PASS**, under the retained actual-source and compatible nonzero pure-V radical hypotheses. The marked quartic is an actual complement to ker h inside im Q. The entire generated endpoint lies in the other summand. No conclusion about degree-five descendants or a splitting of the full multiplication module is implied.

Reviewed SHA256:

- `PROOF.md`: `57737d45d69c0873444243b5dacc5cea46c4372f8b0d605f97078a7807c0e18b`
- `verify.py`: `2e8894f5d562ba6d0699846b6d82282ea7bd45ac569a5cc5f30f639e618cd7a4`

## Authentication

All four retained proofs were freshly retrieved at their exact immutable commit and repository path in `INPUTS.json`. Retrieved bytes equal the retained bytes, and independently computed SHA256 and Git blob hashes match the manifest:

| Input | Commit | Git blob |
|---|---|---|
| PR1019 | `3fb2475ffb275c5789acbaa8f9f84ed272713785` | `bf63c14f76933d59fa7e3ac61aecb3366ac1b442` |
| PR1048 | `9eaed2dfadf9c4877327d21db5974b6c94d3863d` | `0710577541a79a5d8d56e5aa693a8fc01c559112` |
| PR1054 | `8732cb65fe0e72da59e785f3f85ad197a7092e6c` | `64e6bf9f1bf46440700ebab7c90a18f9d8155fd8` |
| PR1050 | `ec18a0fd62c4a9495adf6aad9564d379afc42b62` | `8563bb31385dac0174b3d17bcae7bfa9dcfad716` |

This authenticates these four originals, not every dependency recursively.

## Actual A identification and scalar normalization

PR1050 constructs coherent embeddings into the actual cohomology multiplication module. Its U2 is the unique A subspace of N2. Since the source2 character has exactly one A constituent and PR1019 identifies ker Q as A+D, the two occurrences of A in these constructions are the same embedded subspace. The proof does not replace U2 by an arbitrarily chosen copy of its character.

Coherence of the canonical string and commutativity of the negative-coordinate ring action give `T_a f2(x)=f4(ax)` for every pair of quadratics. PR1019, Sections 3–4, proves that the actual operator hT_a sends this A to I2 by the unique multiplication channel with a nonzero scalar. Its section 3 places the image in I2 before character analysis; section 4 forces the scalar nonzero using original-second nonvanishing. In particular the asserted equality is literal in N2: the degree-zero cohomology of the two-term Q complex is ker Q, with no incoming boundaries.

Changing the nonzero identifications of A or I2 changes only the scalar. Changing the initial normalization of the canonical string changes f2 and f4 coherently. Thus the identity `h f4=mu i_D` follows from the surjectivity of quadratic-by-quadratic multiplication and cannot depend on a chosen expression of a quartic as a sum of products. Explicitly the products x²·x², x²·xy, x²·y², xy·y², and y²·y² span all quartics. This proves that h restricted to this marked D_can is an isomorphism onto I2, not just that some D summand has such a restriction.

## Literal subspaces and the splitting

Original first-symbol vanishing puts every T_a U2 in im Q. Their span is D_can, so D_can is contained in im Q. Separately, `Qh=j4` implies that ker h lies in ker j4, which the retained actual identities identify with im Q. Finally `h(im Q)=im(hQ)=im j2=I2`.

These facts give the actual short exact sequence with kernel ker h and target I2. The inverse of h on the marked quartic supplies its specific section. For any y in im Q, the decomposition is explicitly

`y = (y-rh(y)) + rh(y)`.

The first term lies in ker h and the second in D_can. If a vector belongs to both subspaces, injectivity of h on D_can makes it zero. This proves existence and uniqueness of the direct-sum decomposition independently of dimension subtraction. The character and dimension equalities then check the result: ker h has dimension 28 and character `2V+3P+2D`, while D_can has dimension five.

The projector `rh` is well-typed only on im Q, where h takes values in I2. The proof explicitly restricts it to that domain. Its image, kernel, idempotence, and invariance under a nonzero rescaling of the radical follow from `hr=Id`. Nothing defines this formula on all N4, declares a horizontal splitting, or treats h as a graded module map.

## Generated endpoint and boundary

The sandwich identity annihilates each generator `T_a h(y)` under h. It therefore annihilates their full span F4, not just the image for a single direction. The direct-sum decomposition gives `F4∩D_can=0` and vanishing of the marked projector on F4. A possible D constituent inside F4 consequently occupies the remaining D-isotypical space, not the marked quartic.

This uses no unproved cross-direction commutation. It makes no inference about multiplication out of degree four and does not settle the marked quartic's incidence with any later joint kernel. The conclusion is an actual endpoint embedding comparison, not a source-branch selection.

## Reproduction and verification scope

Both `python verify.py` and `python -O verify.py` passed all 27 checks with byte-identical output. The checks cover complete universal quadratic multiplication, symbolic exact-sequence/projector identities, normalization invariance, and character/dimension bookkeeping. The abstract block matrices are used only after the written splitting argument; they are not evidence for the actual embedding premises and are not source-instance evaluations.

The independent review above verifies the actual-map inference from the authenticated proofs, including the absence of degree-zero boundaries and the precise projector domain. This is mathematical review, not proof-assistant certification. No actual source coefficient, point, direction, or instance rank was evaluated.
