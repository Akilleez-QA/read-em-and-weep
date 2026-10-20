# Faithful parameter recovery through the non-reflexive boundary

## Assumptions and new conclusion

Use the centered family N over S=B[x1,x2,x3,x4], B=C[lambda,lambda^{-1}], of PR274 at commit714e2643752d9aabf52d25686501f9d0ae552b61, with the fixed H action and fixed coordinate ring. Its Ext1 module is the explicit P=coker L and Ext2_S(N,S) is B-free of rank16. These are premises established there, not inferred from fiber dimensions.

For every commutative C-algebra A and every unit a in A, let N_a be base change along lambda→a. For any two units a,b, an H-equivariant A[x]-module isomorphism N_a≅N_b forces a=b. In particular over local Artin C-algebras the parameter is recoverable to every infinitesimal order, including at a fourth root. The family has nonzero Kodaira–Spencer direction in the fixed-ring H-equivariant module deformation problem at every complex parameter c≠0.

This is an injectivity assertion for the displayed one-parameter family, not versality, unobstructedness of all deformations, a moduli-space representability theorem, or actual HM/source liftability.

## 1. Ext1 survives arbitrary parameter base change

Take a finite projective S-resolution F of N. Since N is B-flat and the terms of F are B-flat, F⊗_B A remains a resolution of N_a. Its dual Hom complex C=Hom_S(F,S) satisfies

    C⊗_B A = Hom_{A[x]}(F⊗_B A,A[x]).

The PID B has global dimension one. The universal-coefficient spectral sequence for this bounded B-flat complex therefore gives

    0 → Ext1_S(N,S)⊗_B A → Ext1_{A[x]}(N_a,A[x])
      → Tor1_B(Ext2_S(N,S),A) → 0.

The last term vanishes because total Ext2 is B-free. Thus Ext1 of the base-changed family is exactly P_a, naturally and H-equivariantly. This conclusion includes nonflat and nonreduced base changes; it does not assert base change in every Ext degree. In particular the distinct torsion corrections identified in PR274 do not invalidate this degree-one isomorphism.

## 2. Recover the coefficient from the initial linear relation module

Write m=(x1,x2,x3,x4). The module P_a has the same linear presentation as PR228 with lambda replaced by a, and top

    P_a/mP_a = T⊗_C A,

where T has basis t_j and is the fixed irreducible H representation: the normal abelian subgroup has four distinct weights and the order-four generator permutes them transitively. Consequently

    End_{A,H}(T⊗A)=A.

This also follows directly by the weight decomposition: commuting with the abelian subgroup forces a diagonal matrix and commuting with the cyclic permutation makes all four diagonal entries equal. Thus it is valid over arbitrary A, including rings with nilpotents, without a field-only application of Schur's lemma.

An H-equivariant A[x]-isomorphism P_a→P_b induces multiplication by a unit u∈A on the top. The multiplication map from (m/m²)⊗(P_a/mP_a) to mP_a/m²P_a is functorial. Therefore the induced map on its source is multiplication by the same u, and carries its kernel R_a onto R_b. Since u is a unit, R_a=R_b.

The initial relation module is exactly the A-span of the ten displayed linear columns of L_a. There are no additional degree-one relations after base change: this is the degree-one piece of the defining homogeneous cokernel presentation. In the two-monomial coordinate block spanned by

    x_i t_i,  x_{−i}t_{3i},

the only defining relation is

    x_i t_i − a x_{−i}t_{3i}.

The supports of the other l columns, monomial m columns and clock columns are disjoint from this block. Equality of relation modules therefore gives equality of the two rank-one direct summands A(1,−a) and A(1,−b) in A². Comparing first coordinates of a generator expression makes its coefficient one; comparing second coordinates yields a=b. This argument is valid even if A has zero divisors.

An isomorphism of N_a and N_b induces an isomorphism of their Ext1 modules by contravariant functoriality. Section1 identifies these with P_a and P_b; Section2 now recovers the parameter. The direction reversal of the Ext isomorphism does not affect its existence.

## 3. Infinitesimal nontriviality at every point

Fix c∈C* and set A=C[epsilon]/(epsilon²). For v∈C, compare a=c+v epsilon with the constant b=c. An equivalence to the constant deformation in the fixed-ring H-equivariant category would in particular give an unmarked H-equivariant A[x]-isomorphism N_a≅N_b. Parameter recovery forces v=0.

Hence the tangent map from the one-dimensional parameter space to equivariant module deformations has zero kernel at every c, including c^4=1. No marking convention can make a nonzero v trivial, since the proof excluded even unmarked isomorphisms. The same argument over C[epsilon]/(epsilon^n) recovers every coefficient, but does not claim that arbitrary deformations are obtained in this way.

The boundary jump is therefore not caused by the parameter becoming infinitesimally invisible or by an equivariant change of module generators with the coordinate ring fixed. Allowing coordinate changes or dropping equivariance is a different question and is not covered here.

## Verification status

Authored structural proof using the exact total Ext theorem and the explicit ten-column presentation. No selected source instance or computation is executed. Independent review is required before publication.
