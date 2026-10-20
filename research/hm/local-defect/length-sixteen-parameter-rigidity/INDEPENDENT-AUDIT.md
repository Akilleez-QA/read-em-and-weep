# Independent audit: faithful parameter recovery

## Result and exact text

Scoped PASS. No blocking mathematical flaw was found in PROOF.md with SHA256

    d531cefc3367319d1c83a97b0893e1d5f65ab839bd14a80c81acdee0c3377305

This is an independent human-readable algebraic review, not machine-formal verification. The conclusion is conditional on the total-family theorem of PR274 at commit 714e2643752d9aabf52d25686501f9d0ae552b61 and its fixed equivariant conventions. The exact PR274 proof and exact PR228 presentation were inspected through their published changed-file contents. PR228 is at commit 06c7e2f13e902d819bb6945c033fd455a5f28eac; its proof blob is 9b02d130cf41b60f1b2906668dbd8f10087f4554.

## 1. Arbitrary base change

The premise needed is flatness of the total Ext2 module over B, not constancy of fiber dimensions. PR274 explicitly identifies total Ext2 with Hom_B(P,B), free of rank sixteen. Its torsion correction occurs in total Ext3, so it does not enter the degree-one universal-coefficient exact sequence.

S is regular of finite global dimension, so the finite projective resolution exists. Each resolution term and each term of its S-dual is B-flat because S is B-free and finite projective S-modules are direct summands of finite free S-modules. Since N is B-flat, its projective resolution stays exact after tensoring with any B-module A. Equivalently, all its B-syzygies are flat by induction. Finite projectivity also justifies the termwise Hom base-change identification without flatness or noetherianity of A.

For a bounded flat cochain complex over the hereditary ring B, the universal-coefficient sequence in degree i has Tor1 of cohomology in degree i+1 as its right-hand term. Thus the displayed index Ext2 for i=1 is correct. Vanishing of that Tor term establishes the natural Ext1 base-change isomorphism for every commutative C-algebra A. The argument does not require A to be reduced, Artinian or flat over B. Naturality preserves the fixed H action, with trivial action on the coefficient algebra A.

## 2. Scalar commutant and initial relations

Distinct weights of the normal abelian subgroup force every commuting A-linear matrix on the top to be diagonal: an off-diagonal coefficient is annihilated by a nonzero complex scalar, which remains a unit in any C-algebra. The cyclic permutation forces all four diagonal entries to agree. Hence the full commutant is A, including over nonreduced A, and automorphisms are unit scalars. This is not an unjustified extension of fieldwise Schur's lemma.

Any A[x]-linear isomorphism preserves the m-adic filtration even if it is not graded. Its map on the source of the canonical multiplication map is identity on m/m² tensored with its scalar top map. Consequently it carries the relation kernel to the other relation kernel by the same scalar; a unit scalar leaves an A-submodule unchanged. The use of associated graded modules therefore does not impose a hidden grading restriction on the isomorphism.

The relation kernel in question is exactly the degree-one image of L. This follows from the homogeneous cokernel presentation: the generating relations have degree one, and only their constant coefficients contribute in that degree. No flatness inference from specialization is needed.

For a fixed nonzero residue i modulo five, consider coordinates x_i t_i and x_{−i}t_{3i}. The PR228 monomial columns are x_j t_{3j}; neither selected coordinate has that variable-to-row pattern. The other two-term columns x_j t_j−a x_{−j}t_{3j} cannot overlap this pair unless j=i. The two clock columns have row index equal to minus the variable index, while the selected coordinates have ratios 1 and 2 respectively. Thus the chosen block is disjoint from every other column support. Projection of the relation module onto it is precisely A(1,−a).

The equality A(1,−a)=A(1,−b) forces (1,−a)=r(1,−b) for some r in A; first coordinates give r=1, then a=b. This is valid with zero divisors and nilpotents. Contravariance of Ext reverses the isomorphism direction but does not alter this argument.

## 3. Infinitesimal scope

N is B-flat, hence every parameter pullback is A-flat. The dual-number pullbacks therefore are genuine deformations of the fixed fiber. A trivialization in the fixed-ring equivariant deformation category would in particular be an unmarked equivariant A[x]-module isomorphism. The recovered parameter excludes such an isomorphism for every nonzero tangent coefficient v, including at fourth roots of unity. This proves injectivity of the one-dimensional parameter tangent map and the stated higher-jet distinguishability.

The proof makes no assertion that all deformations arise from this family, that its full deformation functor is unobstructed, that a moduli scheme exists, or that a map to a coarse moduli scheme is unramified. Nor does it allow coordinate changes, nontrivial H action on A, removal of equivariance, or actual HM/source realization. These restrictions are essential to the reviewed argument.

## 4. Further consequence

The same parameter recovery persists after faithfully flat descent: if A→A' is faithfully flat and N_a and N_b become isomorphic in the fixed category over A'[x], then the proved theorem gives a−b=0 in A', and faithful flatness gives a−b=0 in A. Thus even an isomorphism available only after a faithfully flat cover cannot identify two different parameter values. This is a direct consequence of the theorem and faithful flatness, not a claim of representability or full faithfulness on automorphism groups.

## Verification limits

Only structural algebra and the published dependency statements were used. No selected actual HM/source instance was evaluated, no repository code was executed, no large computation was performed, and no external publication was made during the mathematical review. The hash above pins the exact authored proof audited.
