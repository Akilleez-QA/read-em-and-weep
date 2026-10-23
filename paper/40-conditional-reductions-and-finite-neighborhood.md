# Conditional reductions and finite-neighborhood obstruction

**Craig Ward · 23 October 2026 · Update through PR961**

The necessary catalogue frontier remains **four pairs across three stable labels**, distributed **2 + 1 + 1**. This chapter records tighter conditional structures, not new pair exclusions, actual realization, or completion of the original proof repair. Historical figures and counts are unchanged.

## 1. Type I source126: the zero-row alternative is now impossible

[PR959](https://github.com/Akilleez-QA/read-em-and-weep/blob/06919d6651dc9e747128a4c09c515bb3b0f41e09/research/hm/source126-typeI-polar-row/PROOF.md) proves that the joint radical P-row map R_P is nonzero for every Type I constant inclusion in its pinned balanced normal form. This statement does **not** require Q compatibility. The proof establishes that the degree-eight D covariant has no linear syzygies, and hence no nonzero quadratic covector can annihilate its first polar. A hypothetical zero P row would force the two-dimensional radical's restrictions to exhaust the two D-copy polar maps. Their P projection would vanish. Saturation would then give an equivariant nonzero O(20)→O(28), contradicted by the absence of degree-eight scalar invariants.

PR954 separately proved rank R_P≤1 under compatibility of the entire radical with Q. Together the results give **rank R_P=1 under that hypothesis**, and retain only the common-annihilator spaces

- U=A+2V+2P+3D, dimension 32;
- Z=2V+3P+2D, dimension 28.

The quotient Q is invertible on P+D. The prior filtered contraction retains U→Z, kernel A+D and cokernel P, preserving the specified Bockstein problem. The historical **rank-zero 36→32 alternative in chapter39 is superseded**, not silently deleted from the record.

This is not a proof of rank two, full-radical incompatibility, Type I exclusion, or a claim about Types II/III. Rank-one compatibility remains unresolved.

## 2. Every non-V compatible source2 line: two smaller active complexes

Assume a nonzero Q-compatible radical line exists and is not pure V. [PR960](https://github.com/Akilleez-QA/read-em-and-weep/blob/ac41f18da1e7870c30c6fe8bd2867667629c780d/research/hm/source2-quadratic-annihilator-reduction/PROOF.md) now includes the exceptional mixed direction, extending the earlier regular-only theorem PR957. The embedded subpencil NC/im(j) has initial space Z=V+D and final space zero. Every ordered composite of its first and second negative arrows therefore kills Z, so every negative quadratic kills Z. This requires neither first-arrow vanishing nor the exceptional splitting theorem.

The entire deformed pencil restricts to the constant map Q|Z. Equivariance and the actual kernel A+D force exactly two possibilities:

| Restriction rank | Active pencil | Invariant active kernel | Cokernel | Invariant active rank | What must be retained |
|---:|---|---|---|---:|---|
| 8 | 24→20 | A+D | P | 16 | Active complex alone is equivalent |
| 3 | 24→25 | A | P | 21 | Additional permanent D in degree zero |

The rank-three case retains a five-dimensional kernel for all negative perturbations. A multivariable formal argument and polynomial maximal minors prove that the **original 41→37 map has rank at most 36 at every point of Q+Sym²W**. Surjectivity somewhere in that affine family would therefore force rank eight; it is neither proved nor assumed.

These are actual two-term filtered homotopy statements, not a Q-stable splitting of the three-vertex pencil. Arbitrary off-diagonal Q blocks are retained and removed only by explicit invertible chain operations. The rank-three active complex alone is not equivalent: its permanent D summand cannot be discarded.

The hypothesis is essential. This theorem does not select a compatible line, decide its restriction rank, cover all quadrics, or exclude source2. Pure V remains outside it: its endpoint quotient has final space D rather than zero. The earlier PR957 theorem used an intrinsic common first-arrow kernel in the regular case; PR960 uses only the genuinely embedded quadratic-annihilated space, which need not be a first-arrow kernel or the maximal common quadratic kernel.

## 3. Exceptional source2: contraction instead of an isolated first vertex

[PR958](https://github.com/Akilleez-QA/read-em-and-weep/blob/97857b1bcda30135507f160812823eb5e74bbf85/research/hm/source2-exceptional-quotient-structure/PROOF.md) gives the exceptional mixed quotient, uniformly over balanced endpoints and both residual coupling classes:

N/im(j) ≅ N0 ⊕ N8 ⊕ L,

where L=(W'⊗H¹(O(-5)), W'⊗H¹(O(-4)), 0), with dimensions (8,6,0) and characters (V+D,T,0). The full quotient has dimensions **(32,42,28)**. Its first arrows are multiplication by the original linear forms on H¹, not zero maps. Each nonzero first arrow on L is onto with two-dimensional kernel, while their common kernel is zero. The full quotient's first arrows have rank 30 and common kernel zero.

The proof identifies the exceptional kernel bundle as T O(1) ⊕ W'O(-3), then splits the residual two-arrow extension by an explicit universal recursion and equivariant averaging. This is an arrow-level theorem, not character subtraction alone. It needs no Q compatibility; when compatibility is assumed, Q still need not preserve the displayed summands.

Because L's last vertex is zero, every negative quadratic kills L's initial space despite its zero common **linear**-arrow kernel. These two statements must not be conflated. PR960 uses this weaker quadratic-annihilation condition to extend the two-term conclusions to the exceptional direction. It does not turn the contraction arrows into zero arrows or claim a Q-stable decomposition.

## 4. Type II source126: four conditional annihilator footprints

[PR961](https://github.com/Akilleez-QA/read-em-and-weep/blob/cc3215b97a5c92a9253a9774d0f25ade0648b6e5/research/hm/source126-typeII-joint-annihilator/PROOF.md) proves that Type II's joint P row is nonzero even before Q compatibility is assumed. This uses the actual X=O(-8) subbundle with constant span P+D, not a fictitious constant decomposition of the shared-D residual pencil. If the P row vanished, every radical map would land in 2D O(-2); its restriction to X would vanish since Sym⁶W has no D. That would force all constant D coefficients to vanish, contradicting the pinned restriction equations.

Under the further hypothesis that the entire two-dimensional radical is Q-compatible, only the following necessary common-annihilator footprints remain. Here r is the joint P-row rank, epsilon the residual P common-kernel multiplicity, and d the residual D common-kernel multiplicity.

| (r, epsilon, d) | Restricted map U→Z | Restricted cokernel | Quotient kernel | Quotient cokernel |
|---|---|---|---|---|
| (1,0,0) | 27→28 | P+D | D | 0 |
| (1,0,1) | 32→28 | P | 0 | 0 |
| (1,1,0) | 31→28 | D | D | P |
| (2,0,0) | 27→24 | D | D | P |

All restricted kernels are the actual A+D. Only the (1,0,1) quotient is invertible and can be removed by a filtered formal contraction. The other three have a D kernel and cannot be discarded as acyclic.

In the two P-surplus rows (1,1,0) and (2,0,0), the internal first symbol A⊗A→D is nonzero and is a scalar multiple of binary-quadratic multiplication. Thus it has rank three on the A kernel for every nonzero negative quadratic. The original first Bockstein remains zero: inclusion kills this internal D cokernel in the original P cokernel. This locates the required first correction in the non-acyclic quotient rather than furnishing a contradiction by itself.

No row is selected or claimed realizable. Neither full-radical compatibility nor Type II is excluded. The four footprints are not four additional source-dual pairs and do not change the four-pair, three-label ledger.

## 5. Collaborator source report: a finite ordinary-neighborhood obstruction

The full pinned text of mr. slop's [PR955](https://github.com/Akilleez-QA/read-em-and-weep/blob/bd92a1ad858323966b0596f7b92474ca1766f1a2/research/hm/finite-plane-neighborhood/PROOF.md) was read for this update. The following is a report of that source and its stated dependencies, **not an independent reproof of its geometric chain**.

For the actual positive fixed plane R, B=End₀F and the ordinary thickening mR defined by I_R^m, the source proves

H⁰(3R,B(4)|3R)^G=C, while H⁰(7R,B(4)|7R)^G=0.

The unique candidate lies in I²/I³. It cannot extend to the seventh neighborhood; failure occurs either from 4R to 5R or, if it survives that stage, from 6R to 7R. These are **ordinary normal orders four or six**, with obstruction targets of dimensions one or two. Odd layers have no invariant cohomology. The restriction maps are injective from level m+1 to m for m≥3.

The argument translates the actual polar sheaves into ordinary ideal powers by blowup duality, preserving map orientations and the full filtration. It is not a replacement by a split normal bundle or associated-graded dimension calculation. Its first and second obstructions are dual to the preceding polar maps α and β. Their rank relation forces nonextension but does not identify which order first fails.

This does not select the opposite bundle row, vertex scalar, source pair, or a complete algebraicity result. It is separate from the four-pair accounting and from the earlier parameter-line twist −12.

## 6. Evidence and unresolved scope

The new proof packets have independent written reviews and reproducible checks: PR957 has **244**, PR958 **737**, and PR959 **137**, PR960 **168**, and PR961 **129** checks, each reported passing in ordinary and optimized Python modes on the frozen publication inputs. Their universal claims rest on written arguments; finite symbolic or synthetic tests are supporting evidence, not actual-instance evaluations or proof-assistant verification of the entire dependency chain.

The live issues include whether a source2 compatible nilpotent line exists, its direction and restriction rank, and whether Type I full-radical compatibility can survive its now necessarily rank-one row, and which Type II footprint, if any, can occur. No unpublished generalization or pending result is incorporated. The original repair remains open, and the unchanged necessary relation supplies no total proof-completion estimate.
