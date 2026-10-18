# Independent complete-residual lowering review

## Disposition

Accept the narrow literal lowering theorem for the pinned source, conditional on the explicitly imported physical leaf, derivative, determinant-one, and exact-field premises. No missing baseline term, coefficient, sign, endpoint, normalization-side, trace-placement or noncommutative transport-order discrepancy was found. This is not an independent proof of those imported premises or an obstruction verdict.

The original proof, checker, manifest and both historical receipts were inspected. The original checker was then run independently with `python -B` and `python -BO`; both runs passed and rejected all thirteen semantic mutations. No production import or physical model, source, owner, jet, matrix or polynomial evaluation was performed. Formal symbols are invented, not actual-source payloads.

## Source comparison

All seven source files in pins.json were read. The manifest now supplies complete public provenance for the compiler, raw engine and BI proof as well as the four already fully identified inputs. SHA256 and Git blob identities were checked directly from bundled bytes. Public provenance uses the previously recorded immutable source references; this review did not refetch GitHub or establish a signature/trust chain for the repository.

- RS PROOF at ce8b3ee, section 3 equation (E), gives the two U-product terms, four mu terms and four-monomial mixed mu2 term. It gives the three negative gerbe terms before normalization and projection. All match Source.residual literally.
- RS section 4, BI section 2 equation (3), and direct scalar-free reduction at 10810ee sections 1–4 agree on the full baseline, F definitions and five-term representative. The baseline is the full globalCross specialization, not a pre-gerbe crossResidual.
- mu has coefficient 1/2; k has coefficient -1/4 in derivative-inverse wedge form. Mixed mu2 has coefficient 1/4 and signs +,-,-,+; the two disjoint pair orders justify that coefficient.
- b has ordered AW coefficient 15/4. All three gerbe terms have coefficient -1. G inverse multiplies their complete sum and all seven kinetic terms on the left. tf is applied only after this step.
- Both actual tf return expressions implement X-tr(X)I2/2. Both positive Fk terms use complementary pairs and the ik edge. F=b-tr(G inverse mu)/2, including b.
- Each E term retains four terms with signs +,-,+,- and coefficient 1/2. jk derivatives multiply A inverse D(A); ij derivatives multiply A inverse B inverse D(B) A. The complementary pair is passed to T; the current pair selects derivatives. No matrix factors are commuted.
- RawSource has the single base SC.Source and precisely one method, T, whose only statement returns the 1x1-wrapped model.s_raw(tuple(p),a,b). Its signature and full body were inspected. source_and_lift instantiates RawSource and passes its bound residual to the lift. No alternative residual is reconstructed.
- Mat.mul's index contraction preserves factor order. Mat.D applies each entry's V derivative. Its inverse is the adjugate and therefore needs the determinant-one premise. Scalar coefficients are exact Fraction rationals; the actual matrix entries belong to the imported exact field, not all to Fraction itself. This refines the loose phrase “All factors are exact Fractions” in the original proof.

BI equation (7) supplies the raw scalar and equation (8) its first-order equation. This review checks the scalar's dispatch, not the separate denotation proof for all its moving-frame blocks. BI and its independent acceptance concern global class equality under their premises; no pointwise raw/N14 equality is inferred.

## Formal checker versus semantic proof

The interpreter evaluates selected Source ASTs in a free differential algebra with central scalar/trace symbols and ordered matrix words. Both source and expected expressions share these primitive algebra operations. Consequently the executable comparison is a composition/formula check relative to that algebra, not an independent verification of its implementation or of production operations. Manual source inspection and the stated mathematical premises supply the interpretation bridge.

The formal model deliberately treats inverse jets as independent and does not impose inverse cancellation, determinant identities, cyclic trace, transition cocycles, or actual physical field relations. Commuting formal derivatives are valid only under the accepted commuting physical derivation premise. Since equality holds in this more weakly constrained algebra, specializing symbols to the stated physical denotations preserves the checked expression equality. The derivations' physical correctness is not established by that observation.

Only one generic invented triple with distinct endpoint labels is interpreted. Inspection of the fixed source shows no owner-dependent branch in this construction beyond memoization; the triple therefore supplies symbolic variables, not a numerical sample of owners. Owner admission, ordering/alternating extension and actual transition denotation remain outside this checker.

The original tf controls inspect return expressions rather than proving all preceding method statements or rejecting arbitrary hostile source. Raw subclass checks are similarly tailored to pinned source. This is sufficient in conjunction with immutable bytes and source inspection; neither checker is a security sandbox or a universal validator of mutated Python. Semantic controls are meaningful perturbations, not exhaustive proof against all bugs. The whole-sum equality is accompanied by separate ten-term and five-component comparisons, so cancellation cannot conceal an omitted baseline term in this audit.

The small formal word counts are properties of the invented algebra only. No physical coefficient counts, resource estimates, admission changes or detector/ID0 values follow. No HPL, selector or outer transport theorem is added.

## Portable replay and controls

The portable adaptation changes only paths and source authentication/negative-pin checks; the formula interpreter and expected expression are retained. The seven original public inputs are copied byte-for-byte. Production Python is stored as .py.txt and never imported. The pin manifest itself is SHA256-bound in the checker, and each input is checked by byte count, SHA256 and Git-blob digest. All guards use explicit exceptions and remain active under -O.

The portable normal and optimized runs each pass, rejecting thirteen semantic mutations plus 35 input-pin mutations (five per input) and one manifest-drift control. The pin controls use invented changed byte strings or records in memory, leaving originals untouched. The manifest-drift control demonstrates the digest inequality used by its mandatory guard; it does not mutate a real manifest. SHA256SUMS authenticates all other bundle files for transfer. Digests establish identity, not mathematical truth or an adversarially secured trust root.

The bundle is offline and replay-self-contained for the literal lowering check. Its imported theorem premises retain their original dependency scopes. No claim that every transitive mathematical dependency is embedded is made. No external publication occurred.
