# Independent review of compatible single-radical-line footprints

## Verdict and distinction from predecessors

No mathematical blocker found. The proof applies to one nonzero Q-compatible radical element and does not import full-J annihilators or collective-image equalities. The six endpoint footprints are necessary possibilities, not actual realizations. Two footprints force generic rank36 and all later original generic symbols to vanish; the remaining four pass the sharp abstract square-zero-module surjection criterion.

The relevant predecessor comparison was checked locally. The earlier source126 radical-rank packet classifies ranks on the thirty-dimensional reconstructed H and explicitly does not identify N2/N4 endpoint ranks. The nilpotent-generation packet excludes the pure Type III X arrow and leaves a compatible graph line unresolved. The Type I/II polar-row theorem does not cover Type III. The full-J image/top result concerns sums over all radical elements. Thus the present Type III row extension and single-element endpoint classification are distinct applications. The general annihilator-surjectivity and dual-number module arguments are not claimed as new general mathematical principles.

## Mathematical checks

1. **Type III P row.** A zero fourth P row, via the actual natural H1 isomorphism, puts the bundle map into2D O(-2). Its X restriction is zero because Sym6 W has no D. Since X spans P+D, the constant coefficients b_P and b_D vanish. The remaining nonzero Y map factors through one D multiplicity line using the abstract unique map Y to D O(-2). The polynomial nonannihilation lemma forces both P and D projections of its embedding into C O to vanish. This uses no actual first-polar formula for the Type III Y inclusion. Saturation then gives a line quotient O(10) in(A+V)O, and the nonzero top map would require an invariant section of O(18), impossible.
2. **Single-element images.** Source and target characters give im(j2)=uP+vD and im(j4)=P+delta D with u,delta in{0,1}. On D, actual Q surjectivity gives Q im(j2_D)=im(j4_D). Since the intersection with the irreducible D kernel has multiplicity k in{0,1}, v=delta+k. Type I separately has v at most1 because its isolated X vertex is killed.
3. **Eliminated alternative.** The nilpotent action on the multiplicity-free ker Q=A+D is zero. Thus the restricted kernel on U=ker(j2) is the whole original kernel. Character subtraction gives coker(Q:U to Z)=uP+kD. If u=k=0, this restriction is onto. Its preserved negative subpencil provides first corrections within U and forces the same actual second A symbol to vanish, contradicting the retained theorem. In particular the otherwise conceivable rank pair(5,9) is properly excluded, rather than silently omitted.
4. **Enumeration and quotient.** The remaining triples give exactly the six displayed pairs, with four allowed in Type I. Quotient Q has kernel kD and cokernel(1-u)P: P injectivity and D surjectivity are verified on entire actual isotypical subspaces, not chosen copies.
5. **Top obstruction.** A j-commuting surjection would induce a surjection of image quotients. Exactly the u=k=1 rows have quotient target dimension exceeding source by one. Their rank bound36 combines with rank33 at Q and generic second rank3 to give exact generic rank36. Cancelling the three order-two pivots leaves a zero1-by-5 formal residual, so every original later generic differential vanishes in these rows. No exceptional-direction extra kernel is computed.
6. **Sharpness for abstract modules.** For modules R^r plus S^(n-2r) over the dual numbers, a surjection requires r at least s and n-r at least m-s. The explicit free-block and simple-top construction proves sufficiency. All four other listed rows satisfy both conditions. These examples do not claim G-equivariance, actual multiplication, or an actual HM occurrence.

## Exact tests and frozen bytes

Read the checker and independently ran both normal and optimized Python. Both passed105 exact checks with identical stdout. Eight input files are authenticated by SHA256 and Git blob identities. The synthetic diagrams verify Q rank33, square-zero actions, Q compatibility, image ranks, restricted and quotient kernels/cokernels for all six rows. Explicit Jordan-block constructions verify surjections for all four permitted abstract rows. No actual HM instance or parameter is evaluated.

- PROOF.md: `07cbd30f47cacfbae27b7885cfa3fe728fb1296946d4577911b7882a34488b86`
- verify.py: `52767c6838842f09a8cf689ce76457bfe7870fa1cdfca74d776eb2127e233de2`
- INPUTS.json: `804c7d8af4f4b4208198b9076dc217197d3e9d1528a186fe04e2641af2517d96`

This review is conditional on the pinned geometric inputs. The finite computations support the proof and its sharp limitations; they do not constitute proof-assistant verification or a complete original repair.

## Final Type III refinement

The final additional Type III restriction was independently checked against PR862 Section3 and PR946. A compatible nonzero radical has a nonzero Y-arrow component. The tail restriction has a nonzero V coefficient, so a nonzero element of its kernel must have nonzero constant A coefficient. The X arrow is supported on P+D and cannot cancel that A coefficient. If the fourth D row vanished, natural H1 identification would put the bundle image in P O(-2). The coefficient span of its inclusion in C O is contained in P tensor A=V+P+D and cannot contain A, contradicting the actual nonzero A coefficient and the spanning property of R. Thus delta=1 for every compatible nonzero Type III element. Its list is reduced to exactly(9,9),(10,9),(14,9). This does not assume full-J compatibility. Both execution modes were rerun on the final105-check bytes listed above.
