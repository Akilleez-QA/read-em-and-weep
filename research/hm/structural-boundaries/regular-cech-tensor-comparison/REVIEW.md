# Independent review of the regular Čech/tensor comparison

## Verdict and reviewed files

**Accepted for the stated standard-product-cover comparison and regular primitive construction**, including the full unsymmetrized, repeated-index extension in Appendix A. The review consists of a complete independent mathematical reading, implementation inspection, fresh normal/optimized runs, and the expanded audit described below. Finite checks supplement the universal proofs; they do not replace them.

Reviewed SHA-256 pins:

- `PROOF.md`: `7ec48fb142cb5ee319a39507889aa01ed8588549e6af11239024f9ab1628893f`
- `check_controls.py`: `64437ba72954a12aa02cdf75bc8eb523588d017ec49e685aae69ab24376c6b7c`
- Independent review harness `review_audit.py`: `378f499e16ad8f1c9696f1d4aec728953476cec1c220d912eb6063ae378de321`

One wording clarification requested during review is incorporated in the pinned final proof: section 7 explicitly requires G to be a regular degree-preserving **cochain map**, with dG=Gδ, and η to be a regular degree-minus-one operator. This is the hypothesis needed to commute the differential through G in GJF(c)+η(c). The final sentence was reread and the final proof hash verified; there are no outstanding review findings.

## Mathematical review

1. **Directions, order, and signs.** Sh:Q→S and AW:S→Q have the claimed incidence boundaries. AW is evaluated on increasing simplices and only then extended alternatingly; applying the cut formula directly to an unsorted list would be wrong. The fourfold front/back diagonal followed by the coordinate chain maps proves the actual ordered formula. The shuffle interior faces cancel with opposite permutation signs, and its endpoint signs match the cubical boundary. Only the increasing-active-coordinate staircase survives AW, proving AW Sh=1. Consequently A=AW*:T→C, B=Sh*:C→T, and BA=1 have the stated directions.

2. **Cone homotopy.** The residual Dσ−K∂σ is a cycle by induction, so coning it gives ∂K+K∂=1−Sh AW. The unaugmented degree-zero cone has an augmentation correction, but D₀=K₀=0 eliminates it. Normalization kills repeated vertices in S. The recursive construction is finite in every degree, including the top degree of the full sixteen-vertex simplex.

3. **Actual sheaf domains.** The product-open intersection identity proves Uσ⊆Uτ whenever all vertices of τ lie in Box(σ). AW, Sh, and K have precisely the required support: AW target cells lie in that box, shuffle staircase domains equal their cell domains, and K stays in the box recursively. Their transposes therefore use genuine restrictions of regular sections; they never extend an arbitrary section to a larger open. Functoriality of those restrictions justifies transposing the entire identities, rather than merely applying a constant-coefficient chain calculation formally.

4. **Line-bundle frames and tensor H.** With e₁=x⁻²e₀, the coefficient conversion is f_v=x^(-2(w−v))f_w coordinatewise. Whenever frames differ in a comparison term, the receiving intersection has the corresponding x invertible, so these are units on the actual receiving domain. In the common rational frame, exponent m is regular on chart 0 exactly for m≥0, on chart 1 exactly for m≤−2, and unrestricted on their overlap. Thus the stated h gives regular local coefficients and satisfies dh+hd=1−P in both degrees. The Koszul signs in H make its four terms telescope to 1−P_top. The only retained monomial class in each factor has degree one, so the tensor projector is supported in degree four.

5. **Full cochain identity and primitive.** Transposition gives δK*+K*δ=1−AB without an additional sign. Therefore J=AHB+K* satisfies δJ+Jδ=1−AP_topB. For closed degree-two c the projector and Jδ(c) vanish, giving δJ(c)=c with the required plus sign. The identity also explains why the Jδ term cannot be omitted for nonclosed inputs. AP_topB is a genuine projector because BA=1 and P_top²=P_top.

6. **All tuples and repetitions.** In Appendix A, p normalizes alternatingly, j includes increasing lists, and both are chain maps with pj=1. The all-tuple cone retains repetitions. Its vertex is the minimum ORIGINAL vertex, which guarantees original-vertex support under the recursion for L. The same residual-cycle proof gives ∂L+L∂=1−jp in every finite input degree. Regular dualization is therefore valid, and J_all=p*Jj*+L* satisfies the stated full identity. Nonzero repeated-index components are handled through L*, rather than silently discarded.

## Independently reproduced executable evidence

Fresh runs of `check_controls.py` with `python` and `python -O` both passed **2,222 checks**. Their deterministic outputs are retained as `review-normal.json` and `review-optimized.json`; these files are byte-identical.

The additional `review_audit.py` imports the reviewed operators as subjects under test, but separately implements the simplicial/cubical incidence expectations, normalization, and regular monomial-domain predicates. It does not merely invoke the implementation's existing checks. Both normal and optimized audit runs passed **290,907 checks**, including:

- All **65,535** nonempty increasing simplices of the sixteen cube vertices, in every degree: AW chain identity and box support, plus K's homotopy identity and box support
- All **81** four-dimensional cubical cells: shuffle chain identity and AW Sh=1
- **5,161** distinct ordered tuples: all triples over sixteen vertices, supplemented by all lengths one through six over three mixed vertices; normalization identity, L identity, and original-vertex support
- All **6,561** regular cubical-cell/monomial combinations with each exponent in {−3,−2,−1,0,1}: H's actual output-domain regularity and the full tensor homotopy identity, including the retained top harmonic case

The audit outputs `review-audit.json` and `review-audit-optimized.json` are byte-identical. The checks use explicit exceptions, so optimization does not remove them. From an extracted packet directory, reproduce with `python check_controls.py`, `python -O check_controls.py`, `python review_audit.py`, and `python -O review_audit.py`.

## Scope and exclusions

The accepted comparison applies to the sixteen standard product opens of (P¹)⁴. Its literal tensor identification uses the stated exterior tensor line bundle; intrinsic comparison by cubical section spaces is the more general formulation. The exact degree-two primitive asserted here uses O(−2,−2,−2,−2).

No actual source cochain, model, matrix, polynomial instance, physical data, or external service was evaluated or modified. A different source/owner cover still needs its own regular cochain comparison. A forward map F supplies a primitive of F(c) on this cover; a source primitive additionally requires the stated reverse cochain map and homotopy, or an appropriate common-refinement construction. Scalar inclusion and End-valued transport remain separate compatibility requirements. This review does not establish them, remove denominators outside their allowed domains, or establish a noncentral or higher-order lift.
