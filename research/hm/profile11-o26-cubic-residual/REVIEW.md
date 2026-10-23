# Independent review: six necessary cubic-residual forms

## Verdict

**PASS for the stated necessary classification, relative to its explicitly pinned structural inputs.** The proof correctly distinguishes the actual length-twenty elementary modification from the saturation of the original cubic image. It proves the six necessary structural templates without asserting realization, six isolated equivariance orbits, constant separation, or an exclusion of the degree-twenty stratum.

This review binds the exact files:

- `PROOF.md`: SHA256 `c574a1e3ff6624f43094547dc30fad8fe67f48c07a09006e2e9a2722d0ad064f`.
- `verify.py`: SHA256 `d198011a2c199799d586e86d25ad287acbf820e6ffe2dd8934cd131248f9fbc8`.

Both hashes were recomputed before and after executing the verifier. Neither reviewed file was changed. This is an independent mathematical review with a bounded exact-character check, not proof-assistant certification.

## Immutable inputs checked

The original files were retrieved at commit `db51525015bb7c5e825833d550d08dedf6f6ea96` in `Akilleez-QA/read-em-and-weep`, under `research/hm/order-four-quadratic-load/`:

- `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`, Git blob `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
- `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md`, Git blob `d7506dae49b4be43230450c4132bd5db91f137ef`.
- `ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md`, Git blob `dcacf0bcdef8377c1ed7654e5b82659ea409456e`.
- `one-one-endpoint-necessary-pairs.json`, Git blob `fe0afa410d89340d3082dc814277f89fbb582c19`.
- `rank-three-quotient-frontier-144.json`, Git blob `8b5971092f9ef762584912609fd5e9301c4e271d`.

The two selected formal records, not any source-instance evaluation, were checked directly. Source indices 112 and 115 have original defect zero and the displayed O(26) quotients, and their stable labels are respectively `G3.11.dc58cc54f352` and `G3.11.4b6dad66f329`. Their compatible source lists contain the stated E6 and E13 tuples. The original plateau convention gives generic Gauss rank below three at the maximal backward-index-one endpoint.

The following exact dependency files were independently retrieved and read:

- PR840, commit `a69b5a8b9a7c4cb673a89c6465e152fcf699840a`, `research/hm/profile11-o26-basepoint-free-pd-exclusion/PROOF.md`, Git blob `1577481b2aa8d837a0a22794db128cf8c4386e4b`. Its stated basepoint-free exclusion applies exactly to the matching E6/E13 cases. Together with PR813’s divisor alternatives {0,12,20} and exclusion of twelve, it forces degree twenty. This is an imported prerequisite, not a new exclusion proved by the cubic-residual argument.
- PR813, commit `3f99ecf539a3a3da61743df0dff409e54270c865`, `research/hm/profile11-o26-divisor-reduction/PROOF.md`, Git blob `c5237be81f13d72776ba117548038f4c2c11b6b4`. Its degree-twenty argument supplies the actual complete degree-ten constant osculating block and the matching E6/E13 reduction.
- PR825, commit `ea94799a3b1e1c18a4d83061b92d7e7e2f1c631e`, `research/hm/profile11-o26-degree10-endpoint/PROOF.md`, Git blob `41acb092b2db47d0070e6e85e8a2c87ea552e478`. It supplies the exact endpoint intersections E∩C=F and E⁺∩C=F⁺ without assuming saturation of the surviving projection.
- PR798, commit `2bbf244bafc380cf5b0ce1114f86fcd8053e4e55`, `research/hm/profile12-backward-plateau-exclusion/PROOF.md`, Git blob `835404ada200cea294aa0cf0b13d962bd604cdc0`. Its generic internal/projected derivative-rank argument agrees with the use here.
- PR796, commit `d2b43060c83328dd5118aee6b9288fcfa0c873ac`, `research/hm/profile12-quadratic-block-exclusion/PROOF.md`, Git blob `46a0de762000f21182f6d3168f3ecfd63adaf75f`, Section 8. The new proof also supplies its needed quadratic-gap special case directly.

## Sections 1–3: actual quotient, modification, and rank

The quotient diagram is valid as a sheaf diagram. Dividing the onto map E→O(26)⊕L by F→f20 O(6) gives an onto map T O(-3)⊕L→T20⊕L. Its L component vanishes on T O(-3) by degrees and is an automorphism on L. Therefore the kernel has zero L coordinate, and T O(-3)→T20 is onto. The snake-lemma sequence has kernel U⁽¹⁰⁾₇ and quotient M′ of rank six and degree -38. Possible maps from L into T20 do not affect this conclusion.

The exact intersection E∩C=F makes E/F→(H/C)O injective as a sheaf; it does not make that image saturated. The proof preserves this distinction throughout. The image of K has the same generic plane as the cubic T O(-3) image because M′ differs from it only by a torsion modification.

At the generic point, projection of the derivative of K is the derivative of its projected plane. The derivative of K∩C=U⁽¹⁰⁾₇ has a nonzero rank-one image in U⁽¹⁰⁾₈/U⁽¹⁰⁾₇, is nonzero modulo K, and lies in the kernel of the projected target map. Hence the two contributions are independent and

    1 + rank β(G0) ≤ rank β(K) ≤ 2.

The saturation defect is the length of an invariant torsion sheaf. Its bound 0≤δ≤18 and the orbit sizes leave only 0 or 12. In either case G0 has negative degree, so it cannot be a horizontal saturated bundle. Thus its Gauss rank is exactly one. The cubic-column argument gives 7≤dim C1≤9, and minimality of the constant span makes its globally generated quotient strictly positive.

## Sections 4–5: defect-zero classification

The cohomology formulas and rank-one character subtraction are correct.

For quotient-dual ranks two and three, the successive backward kernels cannot be horizontal, since they lie in a negative bundle. Their forward osculations therefore recover the original quotient dual, and the backward line has the same full constant span. This justifies using nondegenerate line-system Wronskians rather than presuming a line-curve decomposition.

In rank two, degree gives r0=2d−20; the eight-section Wronskian gives 7r0≤8(d−7), hence 10≤d≤14 and r0≤8. Equivariance then forces r0=0, because a nonempty invariant divisor has degree at least twelve. The unramified first-jet image is the dual principal-parts bundle W O(-9), not a split O(-10)⊕O(-8). Its cohomology forces C1=A+D, and multiplicity one identifies the actual projected degree-ten system up to constant equivariance.

In rank three, the degrees of the first three osculating graded lines give 3d=24+2r0+r1. The nine-section Wronskian inequality yields 2r0+4r1≤0. Thus d=8 and both ramification divisors vanish. Full span identifies the complete degree-eight Veronese, and apolar annihilator duality gives U⁸₅.

The first table row correctly retains the multiplicity-two P choice in Sym¹⁸W and stipulates the required T O(-3) splitting. No false uniqueness claim is made for that family.

## Sections 6–7: defect-twelve classification

The bounds on splitting degrees follow from generic surjectivity of T O(-3) and the embedding in a constant bundle. The cubic coefficient character excludes trivial constant constituents. Constant ranks four and five are correctly eliminated by actual quotient maps and degree bounds, not merely by dimension counting.

Constant rank zero forces six degree-minus-one summands. Linear generation and Gauss rank one force seven constants, and the complete O(6) quotient identifies U⁶₅.

For constant rank three, if n1,n2,n3 are the multiplicity dimensions at degrees -1,-2,-3, then n1+n2+n3=3 and n1+2n2+3n3=6 imply n1=n3. A nonzero odd multiplicity dimension is at least two, so both must vanish. The remaining degree-minus-two coefficient is V, since T occurs in V⊗W but not in A⊗W or 1⊗W. The constant summand is genuinely horizontal; taking a constant complement makes the stated direct-sum embedding legitimate.

For the quadratic V O(-2) factor, the span has dimension four or five. In dimension five, the second span is already constant. The derivative of the first span factors through its line quotient O(b), giving a nonzero O(b)→O(4−b) and therefore b≤2. The nonzero original Gauss map would simultaneously require V in SymᵇW, which is impossible: its first occurrence is degree six. The span is therefore four-dimensional. Since its coefficient is a quotient of V⊗A=P+D, it is P. The degree-six quotient and multiplicity-one P constituent identify precisely the stated P-system kernel.

## Executable check and scope

The entire `verify.py` was inspected before execution. It uses exact Q(√5) arithmetic and checks only the declared bounded universal character identities and multiplicities. It completed successfully with all three PASS messages. No broad enumeration or selected actual coefficient, point, matrix, derivative, source-instance rank, or model evaluation was performed.

The result is a valid new necessary classification of the saturated generic cubic residual. The elementary modification, its realization and compatibility, residual constant coupling, the source2 branch, and the global rank goal remain unresolved exactly as stated in the proof.
