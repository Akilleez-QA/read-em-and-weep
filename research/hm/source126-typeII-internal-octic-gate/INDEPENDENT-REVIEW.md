# Independent review: internal fourth-through-seventh vanishing and the octic line

## Verdict and scope

No mathematical blocker found. Under the retained full-J Type II hypotheses, the actual internal symbols4,5,6,7 vanish globally. The internal eighth is well-defined and belongs to one canonical line of rank-at-most-one maps satisfying quotient-kernel naturality. That line has a nonzero universal generator, but the actual scalar is not selected. The all-orders original generic vanishing is an imported result, not the new conclusion here.

## Recursive construction and choice independence

The parameter variety is P(A), a plane. All coefficients in the nth correction have homogeneous degree n in its three coordinates. A zero residual in E factors uniquely through the first multiplication subbundle A O(-1) into D O. Its inverse on that image gives a global homogeneous A-valued correction, not a rational division. Subtracting a kernel correction leaves the previous Q-lifting equation unchanged; the next correction then exists through the fixed equivariant Q right inverse.

Choice independence was checked independently. For the earliest difference between two normalized correction strings, Q-closedness places it in A+D. If another lifting stage follows, normalization forces its A part to vanish by first-symbol injectivity. Subtracting a shifted normalized lift string of its D part removes that difference; its final residual is a lower internal symbol and vanishes. Repeating leaves only a final kernel correction, whose first image disappears in E. This proves that the global maps are the actual higher internal differentials on the unchanged D/E page.

## Rank-one classification and degree bounds

A rank-one equivariant image saturated in E is reflexive by the depth lemma, hence O(k). Its inherited linearization has no character ambiguity. H0(E(-1))=0 on the plane gives k<=0; source and invariant inclusion require D in Sym^(n+k)A and an invariant section of E(-k). Exact A5 character calculations independently confirm all candidate lists:

- Degree4: no compatible saturated line.
- Degree5: no compatible saturated line.
- Degree6: only k=-4, both factor spaces one-dimensional.
- Degree7: only k=-5, again the quadratic source factor and a one-dimensional target section space.
- Degree8: only k=-6 or k=-4.

The inherited rank(S)<=23 means the surviving D-to-E formal map has rank at most one. Any nonzero fourth or fifth symbol would instead have rank two by this classification, proving both vanish. This then legitimately constructs the sixth and subsequent symbols recursively.

## Higher naturality and sixth/seventh vanishing

On the dense open where quotient first multiplication is onto, its kernel vectors lift through every finite order. An actual radical chain map with nonzero D cohomology scalar carries such strings to S strings. Hence every first potentially nonzero internal higher symbol kills the correctly shifted kappa. Equality extends globally as a vector-bundle morphism and does not assume specialization of kernels at exceptional directions.

The unique quadratic source covector is the apolar pairing c_a(h)=<a^2,h>. At a general nonflex square a=l^2, the pinned sextic-series argument gives kappa represented by h=v/l^2 not divisible by l. In universal coordinates l=x, the pairing is h4, which is nonzero. Thus c kappa is a nonzero degree-six scalar polynomial on P(A). Multiplication by either nonzero invariant target section cannot annihilate it on the integral plane. The unique rank-one sixth and seventh lines therefore fail naturality unless their scalar is zero. This proves both additional vanishings without an actual selected parameter evaluation.

## Exact eighth-order boundary

The k=-6 factor in degree8 again uses c and is excluded by the same nonzero restriction. For k=-4, quartic covectors form a two-dimensional space. Delta c has nonzero kappa restriction. Conversely the unique nonzero cubic P-covariant cP defines psi4=cP* b_T, which kills kappa and is nonzero because b_T is generically onto. These two independent facts show that the quartic restriction kernel is exactly one-dimensional.

Composing psi4 with the unique nonzero invariant section sigma:O(-4) to E gives a nonzero rank-one map satisfying naturality. Every rank-one map satisfying naturality must have precisely this factorization up to scalar. Consequently the eighth gate is exactly a canonical line, not merely a dimension upper bound. The argument selects no actual scalar and establishes no all-orders internal vanishing or original repair.

## Final-byte verification

Independently read the full final-scope proof and checker and ran normal and optimized Python. Both passed185 checks with identical output. The checker authenticates four immutable inputs, computes plane characters through degree8, checks possible saturated factors and Hom dimensions, verifies the invariant apolar pairing and transverse coefficient, and checks noncommuting recursive normalization identities. Geometric nonflex and chain-map comparisons remain written mathematical arguments; no actual HM instance is evaluated.

Reviewed hashes:

- PROOF.md: `8f75112f5dcc7bb57efb24d9abc0bf7b33fbbcc6b128569eea8576bcf90699cd`
- verify.py: `d31a2e851e7436f3d52aee6af493b035a5f67bda5bc604158b5c72ccc7f6125c`
- INPUTS.json: `4d483772bfd6afd70bcf16545d7206ff368c8442ba1e817d7213d618db8200d2`
- RESULT.json: `03267aede0b16771c2d16bbf04a676980fcde6d5897ff803e32a30a8669df576`

This is a conditional mathematical review supported by finite exact checks, not proof-assistant certification or a completed source exclusion.
