# Historical scope-limited review receipt

This review concerns the original source, possibly a larger scope than the excerpt in this unit. It is not a review of normalized publication bytes.

# Independent audit of the coordinate-multiplication proof

## Artifact binding

Audited file: `PROOF.md` in this directory.

- SHA256: `f81d33eec195fa3251acf95d47750a9371188b232974faf9eb125c40de48b107`
- Byte count: **6501**
- Audit date: 2026-10-18 (UTC)

The auditor independently ran `sha256sum` and `wc -c`, read the entire file with those results, and checked the same digest and length again after writing this audit. The proof file was not modified. This verdict applies to those exact bytes; changes require a new binding.

## Verdict

**PASS**, with the explicit dependency and conditional boundaries below. Both actual coordinate-multiplication maps are surjective under the stated established cohomology and normalizer-representation inputs. The parameter-line and retained-span consequences follow as written. There is no hidden spectral-sequence arrow, convergence problem, or extension issue in the argument. The proof does not establish nonvanishing of the canonical cubic parameter itself.

## Independently checked deductions

1. The coordinate evaluation is everywhere surjective on projective four-space. Its full sheaf Koszul complex is exact, and tensoring by the locally free endomorphism bundle preserves exactness. Its bounded hypercohomology spectral sequence therefore abuts to zero. The stated twists, columns, and differential bidegrees are correct.
2. At `(0,2)`, the only potentially relevant higher incoming arrows have sources `(-2,3)` and `(-3,4)`, whose first-page terms vanish by the imported inputs. There are no outgoing arrows. Thus the cokernel of `mu21` is zero.
3. If `mu32` vanished, the alternating Koszul differential into `(-1,2)` would vanish. Surjectivity of its outgoing first differential gives second-page dimension `5*20-10=90`.
4. For this slot there are no higher outgoing arrows. The only higher incoming arrows are from `(-3,3)` on page two and `(-4,4)` on page three. Their ranks are at most `10*5=50` and `5*1=5`. All later incoming sources lie above sheaf-cohomology degree four. Each page is a subquotient of its predecessor, so these bounds remain valid even if the source terms themselves have other differentials. At least 35 dimensions would survive, contradicting the zero abutment.
5. Self-duality and Serre duality give the stated dimensions at twists minus four and minus five. The nonzero image of `mu32` is stable under the stated normalizer action; target irreducibility then proves surjectivity.
6. A nonzero equivariant cubic has full linear image in the irreducible `J3`. Multiplying its values once spans `J2` by surjectivity of `mu32`, and multiplying twice spans `J1` by surjectivity of `mu21`. Scalar-linearity identifies these values with the indicated mixed operations on multiplied inputs. Only linear spans are asserted; no claim that every target vector is one decomposable value is needed.
7. The cited Euler balancing makes the induced mixed operations well-defined on `U0`, including for every abstract cubic in the symmetry-eligible line. The constructions are linear in the cubic. Every nonzero element of that line yields nonzero mixed operations by the previous span argument, so both parameter-line maps are injective and have one-dimensional images. Conversely, a zero cubic gives zero mixed operations because multiplied inputs generate `U0`. This proves the stated equivalence for the actual common cubic parameter.
8. Under the established filtered-transfer statements, nonzero lower mixed operations fill the canonical four-dimensional retained subspace, while nonzero upper mixed operations surject onto its eight-dimensional quotient. A subspace containing the former and surjecting onto the latter is the full twelve-dimensional target. No splitting is needed, and no converse to this sufficient criterion is asserted.

## Dependencies and evidence boundary

In addition to the bound proof, this audit read these static local dependency texts:

- [the cubic massey module reduction manuscript](../../canonical-cubic-extension/cubic-massey-module-reduction/PROOF.md): scalar-linearity, common one-dimensional cubic parameter space, Euler balancing and generation.
- [the full hm image symmetry manuscript](../../../full-hm-image-symmetry/PROOF.md): actual normalizer-equivariant target irreducibility and upper retained-transfer conclusion.
- [the lower weight image symmetry manuscript](../LOWER-TRANSFER.md): lower retained-transfer conclusion and the subspace-plus-quotient argument, particularly Sections 4 and 6.
- [the projective target directions manuscript](../../../hm_primary_source_verification.md): the recorded primary cohomology verification and its scope.

The audit verifies the new deductions against these stated dependencies. It does not constitute a fresh independent verification of every historical source, literal-presentation identification, cohomology calculation, or filtered-transfer theorem in their dependency closure. In particular, the cohomology rows, the actual equivariant identification/irreducibility, and the canonical filtered-transfer hypotheses remain imported established inputs. No new primary-source browsing was performed for this audit.

Only static mathematical proof reading, abstract spectral-sequence/duality/representation reasoning, file hashing, byte counting, and writing this audit were performed. No actual multiplication map, matrix, polynomial instance, point, jet, source/model product, detector, residual, or Massey value was evaluated. No external state was changed.

The unconditional new conclusion relative to the imported inputs is surjectivity of the two multiplication maps. Mixed nonvanishing and the full twelve-dimensional retained span remain conditional on nonvanishing of the actual cubic parameter. No residual or physical-obstruction verdict follows from this audit.
