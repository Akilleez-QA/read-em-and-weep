# Independent Lean proof-boundary audit

Audit date: 2026-10-18 UTC. Status: all four mathematical source files below independently pass compilation and dependency audit, including the integrated numerical and genuine Mathlib linear-algebra extensions. This is not certification of the full geometric argument.

## Checked artifacts and execution

- KoszulDimension.lean: 7,353 bytes, SHA-256 d62835482cd202ff62fe5b0232b4d8070dafef8ee6c46478741b98da19672e3d.
- KoszulSlots.lean: 5,718 bytes, SHA-256 4af4e2e0af38e8c841635e3e0b039b89219c6f29724540c34ec74d4dea373752.
- Audit.lean: a separate auditor-owned axiom probe and synthetic consistency witness, compiled against freshly built artifacts.
- AUDIT-COMPILE.txt: direct output of the auditor's compiler invocation, not a worker's success assertion.

The auditor directly ran the workspace-local official Lean 4.19.0 release, commit 6caaee842e94, rebuilt both .olean files from the listed sources, and then compiled Audit.lean. The shell used pipefail; all commands exited zero. The installation source and archive receipt are documented in ENVIRONMENT.md. Its archive hash is a local integrity receipt, not a separately publisher-authenticated hash. No independently verified binary-reproducibility claim is made. The trust base includes the official compiler/kernel and bundled imported libraries.

## Kernel-checked content

KoszulDimension proves the balance law for explicit kernel/image dimension equations; nonincrease under a page step; nonincrease along a finite PageEvolution; a telescoping DropBudget inequality; the 90 minus 50 minus 5 lower bound of 35; page-two dimension 90 under a zero-map supposition; and inequality of mu32 and a distinguished zeroMap under the explicit Inputs record.

KoszulSlots proves exact higher incoming source classifications at (0,2) and (-1,2), exclusion of outgoing arrows, exclusion of incoming arrows from page four on, and numerical rank bounds under PageRankData. All integer/Nat coercions and endpoint inequalities are checked.

The two source-classification iff theorems use only the standard axioms propext, Classical.choice, and Quot.sound. The remaining checked base-layer theorems use propext and Quot.sound. No sorryAx, declared custom axioms, native_decide, unsafe proof oracle, or admitted theorem occurs in the checked proofs. Audit.lean constructs a witness of Inputs true false using Bool as the abstract map type; premises_inhabited uses no axioms. Thus Inputs is not universally inconsistent. This synthetic witness is a bookkeeping consistency example, not an evaluated HM multiplication map.

## Exact dependency boundary

1. Imported geometry: coordinate evaluation and its exact sheaf Koszul complex; local freeness; the hypercohomology spectral sequence and its zero abutment; the cohomology dimensions and vanishing; identification of d1 with coordinate multiplication; rank-nullity and quotient interpretation for actual finite-dimensional cohomology groups.
2. Imported numerical interfaces: PageStep assumes the two correct dimension identities; PageRankData assumes the rectangular support, first-page domination and image bounds. Inputs assumes the relevant first-page sizes, outgoing rank 10, zero-multiplication implication for the alternating incoming rank, source bounds, no higher outgoing ranks, and page-four vanishing.
3. Proved numerical consequences: finite source monotonicity, support classifications, budget inequalities, and contradiction of a zero mu32 under Inputs.
4. External final geometric step: actual target irreducibility and equivariance identify the nonzero image as the whole target. These are absent from the base-layer theorem.
5. External conditional Massey consequence: scalar-linearity, cubic parameter nonvanishing, generation/balancing, and filtered transfer. In particular no theorem here establishes nonvanishing of the actual cubic parameter or a residual/physical-obstruction verdict.

The base-layer Inputs theorem does not assume mu32 is nonzero or surjective. Its premises describe independent page facts from which nonzeroness follows. The zero-map supposition correctly forces an inconsistent dimension budget; that is the intended reductio, not a vacuous overall record. However, mu32 is only an element of an arbitrary Type in that theorem, so naming it mu32 does not formalize a linear map. Likewise PageStep and PageRankData are records of numbers, not constructed homology groups or a spectral sequence. A claim that these files alone prove actual HM surjectivity would exceed the formalization.

## Improvement path

A genuine Mathlib linear-algebra layer can replace numerical page equations with derivations from finite-dimensional linear maps, image contained in kernel, quotient finrank, and rank-nullity. Nonzero equivariant maps into irreducible representations can then supply abstract surjectivity and image-propagation statements. Even that extension leaves sheaf geometry, cohomological calculations, representation identification, and realization of these abstract hypotheses by the HM object as separate obligations. Such an extension must not hide the final conclusion in an assumed image-surjectivity premise.

## Scope

Only abstract theorem checking, static source inspection, and artifact hashing were performed. No actual HM model/source map, rank calculation, polynomial instance, point, jet, residual, or Massey value was evaluated. The geometric prose proof and historical source dependencies were read as context, not re-certified by these Lean runs.

## Integrated numerical layer: independently PASS

KoszulCombined.lean: 6,390 bytes, SHA-256 feac384c5b6c0fb93ba9fb64a92851a0651a2663ab4aec3ba7376eaaea924a33.
AuditCombined.lean: 1,818 bytes, SHA-256 da46d1a031442defd94dd22fd96b2325887eb0763a98f6d42856e6d4a4c00026.

The auditor independently rebuilt KoszulCombined.olean and compiled AuditCombined.lean. Both exited zero; direct output is AUDIT-COMBINED.txt. The exported stabilization, rank-ten, and integrated nonzero theorems have only propext and Quot.sound dependencies. The combined consistency witness has only propext, Classical.choice, and Quot.sound.

The integrated layer closes the separate-interface gap: QuotientIdentities assumes the finite-page balance law for the two selected slots, rather than directly assuming rank ten or page-four zero. Absence of arrows implies right-slot stabilization at page two and left-slot stabilization at page four. Zero dimensions at some finite N≥4 then give those earlier zero dimensions. The right-slot first-page dimension ten and balance yield the d1 rank ten; the slot rank bounds and zero-map implication instantiate every field of the dimension theorem. Thus the final theorem derives both numerical rank ten and abstract mu32≠zeroMap.

A concrete, kernel-checked synthetic PageRankData witness satisfies all integrated premises simultaneously: first-page dimensions 90,100,10 in columns -2,-1,0 at row two; first-page outgoing ranks 90,10,0 respectively; all later pages zero; abstract mu32=true and zeroMap=false. This is a consistency witness for the interface only. It is not asserted to be the actual geometric spectral sequence. No arbitrary rank evaluations of actual objects occur.

Still imported: realization of the numerical fields by geometry, correctness of quotient identities for that realization, first-page bounds and cohomology values, eventual zero abutment, and the Koszul zero-map implication. PageRankData first-page domination is assumed globally; the separate PageEvolution theorem proves how to obtain it from an actual finite succession of PageStep data, but that succession is not constructed for the geometric source slots here. The integrated theorem therefore strengthens numerical coverage without changing the geometric trust boundary.

## Genuine Mathlib linear-algebra layer: independently PASS

Propagation.lean: 8,932 bytes, SHA-256 d6bd62d188051667f31ff254facee3f3be8184ae3ae0f542dc8ce4c2e1c7d394.

The auditor independently compiled the frozen source to Propagation.olean, then compiled AuditPropagation.lean against that freshly built artifact. Both exited zero. AUDIT-PROPAGATION.txt contains all eight theorem axiom reports: equivariant_nonzero_surjective uses propext and Quot.sound; the other seven use propext, Classical.choice, and Quot.sound. No sorryAx or custom axiom appears. Earlier development errors were repaired before this passing run; those earlier failed compilations are not used as evidence.

Environment: official Mathlib v4.19.0, commit c44e0c8ee63ca166450922a373c7409c5d26b00b (independently read from the checkout), with manifest-pinned dependencies and official cached compiled imports described by ENVIRONMENT.md. The auditor compiled the new proofs, not all of Mathlib from source. The trusted imported library/cache boundary therefore remains explicit; a cache-download success alone was not treated as proof compilation.

This layer uses actual Mathlib LinearMap and Submodule objects. It proves that a nonzero equivariant linear map has invariant nonzero range and hence is surjective when every invariant target submodule is bottom or top. It proves images of spanning generators span under a surjection, aggregate coordinate multiplication transports spanning families, and iteration fills both mixed channels. Its assembly theorem derives aggregate coordinate spanning from a surjective assembled map and elementary generators spanning the assembled domain; it does not erroneously require every coordinate map to be surjective. Finally a subspace containing L and surjecting onto T/L is all of T, without choosing a splitting; quotient finrank plus the imported 4 and 8 dimensions gives 12.

The final conditional chain does not assert its conclusion as a hypothesis. It uses explicitly named geometric transfer implications to supply containment and quotient surjectivity after establishing upper/lower spanning. These implications are substantial external hypotheses, not newly verified filtered-transfer theorems. Nonvanishing of f is a hypothesis; no actual cubic is constructed or shown nonzero. Irreducibility is an explicit property of an operator family, not a construction/identification of the classical normalizer representation. Aggregate coordinate surjectivity remains a premise in this Mathlib layer; its realization by the numerical Koszul layer and the actual geometric maps is not formalized. The numerical PageStep equations have still not been derived from constructed spectral-sequence vector spaces, although the final propagation and quotient arguments themselves are genuine abstract linear algebra.

## Final audited outcome

PASS for the exact four mathematical Lean source files bound above, plus their auditor-owned probes and consistency witnesses, at the explicitly stated abstract/conditional scope. The integrated numerical proof and genuine linear-algebra propagation proof are kernel-checked relative to the official Lean/Mathlib trust base. No claim of a complete Lean formalization of the HM geometry, an unconditional nonzero cubic, or an evaluated residual is warranted.
