# Independent review: marked residual string and homotopy kernel

## Verdict and reviewed artifacts

**PASS**, with the stated conditional actual-source hypotheses and the explicit zero-N0-projection restriction on the final branch equivalence. The canonical string projects injectively to the degree-eight core, its quartic is transverse to NC4 in both branches, and the marked section splits only the asserted inverse-image submodule. The proof does not split the full residual extension.

Reviewed SHA256:

- `PROOF.md`: `bf2ad7b5e982b7eeb0b44e1be7ef22656b56d0550a8c6f792a58b17c7bda3f17`
- `verify.py`: `16f299a2c0b61a7c67f87e8cf76bfa0ad27293369cc79e6006d1066956d5da36`

## Input authentication

All four originals were freshly retrieved from their exact repository paths at the immutable commits recorded in `INPUTS.json`. Retrieved bytes match the retained files, and independently computed SHA256 and Git blob hashes agree with the manifest:

| Input | Commit | Git blob |
|---|---|---|
| PR795 | `3f811311d76914a555c7e7d0c5b887b41805aa6c` | `9358ec81c552913fac20f3a92d7b9f7c58105656` |
| PR1050 | `ec18a0fd62c4a9495adf6aad9564d379afc42b62` | `8563bb31385dac0174b3d17bcae7bfa9dcfad716` |
| PR1059 | `af2f163e4bcc593b6895ace840c139d2d4668cde` | `2b00a40de04a7084ff2f08c767fdd2f4f13ae5f4` |
| PR1061 | `90f33f808c2962cdd4c41d11ac32a10c30b0d353` | `aae98e9c7bfdd084b342d222bbdb2c8b06c53c20` |

This authenticates the four retained proofs, not every historical dependency recursively.

## Actual quotient and canonical source

PR795 constructs NC→NR→N8 from a genuine diagram of evaluation sequences. The required cohomology vanishings give exactness at all three vertices, and connecting-map naturality identifies the same fixed negative arrows. Thus the quotient used here is an actual pencil quotient, not an abstract character subtraction or an assumed horizontal splitting.

The genuine N0 projector kills the canonical A because N0,2 has no A. Negative stability then places its full A→S→D string in NR. The quotient is injective on this A because NC2 has no A. The Clebsch decomposition of A⊗Sym⁴W has precisely one A constituent, so the projected source is its specific unique A. This deduction uses the actual maps before the universal calculation.

The degree-eight evaluation model identifies N8,4 with the quotient by complete polarization in bidegree (2,6). Under that identification the first A factor is a coefficient factor and negative multiplication acts on the second polynomial factor. This factor convention is maintained throughout the proof and certificate.

## Universal identity and independent certificate

The inclusion `f↦(Xy−Yx)²f(x,y)` is nonzero, equivariant, and of bidegree (2,4). Its image is therefore the unique A just identified. The actual identification differs by an unevaluated nonzero scalar, which cannot affect the descendant image.

The production quotient certificate checks the full polarization image, its left inverse normalization 28, and the rank-12 transvectant quotient. Independently, direct mixed differentiation of the biform `(Xy−Yx)²b(x,y)f(x,y)`, followed by diagonal substitution, gives exactly `(0,84bf)` for arbitrary quadratics b and f with all six coefficients indeterminate. This confirms the sign, scalar, and variable convention without choosing a direction.

A separate independent check bypassed transvectants entirely. Polarization columns were extracted from the expansions `(X+x)^(8-k)(Y+y)^k`, and marked quartic columns from `(Xy−Yx)²x^(4-k)y^k`. In bidegree (2,6), their ranks are respectively nine and five, and the concatenated matrix has rank fourteen. Thus the marked quartic meets the polarization kernel trivially. This independently verifies injectivity of its image in the endpoint quotient.

Because products bf span all quartics, the endpoint descendant image is exactly the unique D8. Actual multiplication compatibility and PR1050 then make the canonical U4 project isomorphically onto D8. The middle projection is nonzero because its descendants include D8; irreducibility of S makes it injective. This proves the three vertex injections without assuming a splitting of NR.

## Restricted splitting and residual homotopy rank

For U8=π(U), the inverse image has kernel NC and an actual section supplied by U. The section commutes with both negative arrows. Its intersection with NC is zero at every vertex, so the restricted inverse image is NC⊕U, with dimensions (20,22,14). This argument concerns only U8, not all of N8, and gives no Q-stable or horizontal decomposition of NR.

The pure-V radical kills NR. Hence NR4 is contained in ker j4=im Q, and h takes NR4 into I2. The marked D_can lies in NR4 and maps isomorphically onto I2 by PR1061, so h(NR4)=I2. Rank-nullity gives the 16-dimensional kernel K_R, and the same marked inverse supplies NR4=K_R⊕D_can. All these assertions concern actual subspaces; their dimensions are consequences, not evidence replacing the embeddings.

## Residual-only branch equivalence

Under zero N0 projection of P_h, the full generated module lies in NR. In the small branch PR1059 gives F4=NC4 and h(NC4)=0. Thus h descends to N8,4. It is nonzero on D8 by the marked lift and vanishes on V8 and P8 by equivariance. Its kernel is exactly V8+P8, giving the stated inverse-image identity and short exact sequence.

In the large residual branch the actual map A⊗P_h→N8,4 is an isomorphism. The generated F4 has dimension 16 and maps onto N8,4 with kernel I4. Since F4 is contained in K_R and both have dimension 16, they are equal. Intersecting with NC4 gives kernel I4 for the restriction of h, so its rank is five and it induces NC4/I4≅I2.

These cases exhaust the zero-N0-projection hypothesis and establish the asserted if-and-only-if there. The proof correctly does not transfer the conclusion to nonzero N0 projection, where containment of F4 in NR4 need not hold. No branch is selected or excluded.

## Executed verification and limits

Both `python verify.py` and `python -O verify.py` passed all 28 checks with byte-identical output. The independent biform differentiation and polarization-intersection calculations also passed. These are universal symbolic certificates; no actual source coefficient, direction, point, or source-instance rank was evaluated.

The actual-map inheritance, exactness, and splitting arguments were reviewed in the text and authenticated inputs. They are not replaced by synthetic matrix examples or presented as proof-assistant certification. The result makes no new original-Bockstein vanishing claim, extends no homotopy to later degrees, and leaves the quartic's degree-five descendants unresolved.
