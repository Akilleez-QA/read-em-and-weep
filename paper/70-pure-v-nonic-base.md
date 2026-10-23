# No divisorial defect and two intrinsic jet lines

**Craig Ward · 23 October 2026 · PR1030**

[Immutable full proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/418a7d9ebedaae9b5d00db9f69e449b5d8767108/research/hm/source2-pure-v-nonic-base/PROOF.md).

## 1. The nonzero universal system

For any nonzero s in the established two-dimensional pure-V gate, composition with J=I_Z(6)⊂O(6) gives four linearly independent degree-nine polynomials spanning P. PR1030 proves they have no common divisor. Their base scheme B_s is finite, contains Z, and

    im(s)=I_B_s(6),   J/im(s) has finite support.

This is not a claim that the actual s is nonzero. The old length-34 scheme Z and cubic P-covariant's six reduced basepoints are imported inputs, not new calculations.

## 2. Why no common curve survives

Any homogeneous greatest common divisor is invariant, since A₅ has no nontrivial characters. The low-degree invariant dimensions leave only the discriminant conic or a non-conic sextic as possible factors. The conic is excluded by H⁰(I_Z(7))=D and Hom_G(P,D)=0. A remaining sextic factor would multiply the unique cubic P-covariant.

At each of the six order-five axes, the cubic's ideal is m and Z's ideal is (u²,v²). The colon ideal ((u²,v²):m)=m² forces the sextic singular there. At each of the ten order-three axes, the cubic has a unit component and invariance excludes a linear term of the sextic. Thus the sextic would have sixteen distinct singular points.

It must be reduced: a repeated-component divisor would yield an invariant of degree at most three, hence a forbidden conic factor. For a reduced plane sextic with r components, the total singularity δ invariant is at most 10+r−1≤15. Sixteen singular points contradict that bound. Hence no common divisor exists.

## 3. Full stabilizers produce two scalar jets

At the order-five axes, the quadratic leading terms define a scalar functional ν₅ on Vgate. Its one-dimensional target follows from the **full** dihedral stabilizer, including the O(9) reflection-sign twist. At the order-three axes, first jets similarly give a scalar ν₃ using the full S₃ stabilizer. Cyclic weights alone would not justify the one-dimensional targets.

If both jets vanished for a nonzero s, two general component combinations, with no common curve, would meet with multiplicity at least

    6·3²+10·2²=94>9²=81.

Bézout rules this out. Therefore (ν₅,ν₃) is an isomorphism between two-dimensional spaces, and ℓ₅=ker ν₅ and ℓ₃=ker ν₃ are distinct intrinsic lines.

## 4. Exact conclusions and unresolved geometry

- Outside ℓ₅∪ℓ₃, the local base ideals at all sixteen axes equal the old Z ideals: six (u²,v²) and ten reduced maximal ideals.
- On ℓ₅ minus zero, the six ideals are contained in m³ and the ten other points remain reduced. Total length(B_s) is at least 46.
- On ℓ₃ minus zero, the six ideals remain those of Z and the ten ideals are contained in m². Total length(B_s) is at least 54.

These are lower bounds, **not** equalities or exact exceptional local ideals. Agreement with Z at its support does not exclude additional finite basepoints elsewhere. Placement of these intrinsic lines in a chosen quadratic-lift basis is not supplied here. This theorem alone supplies no additional conic-basepoint or support classification; the later [PR1033 refinement](74-pure-v-conic-base.md) settles the conic intersection only.

This nonic base scheme is not the older source126 octic generator's scheme; the shared number 46 in a lower bound does not identify those objects. The actual gate, its nonzero status and any compatible source remain unselected. The source reports independent review and 47 ordinary/optimized checks; no actual-instance coefficient or obstruction value is evaluated. Four necessary pairs across three labels remain.
