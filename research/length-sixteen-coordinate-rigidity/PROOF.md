# Parameter rigidity modulo equivariant formal coordinate changes

## Statement, dependencies, and added scope

Use the centered family N over S=B[x1,x2,x3,x4], B=C[lambda,lambda^{-1}], from [PR274](https://github.com/Akilleez-QA/read-em-and-weep/pull/274) at commit 714e2643752d9aabf52d25686501f9d0ae552b61. Retain its specified H action and its parameter-base-change theorem in [PR300](https://github.com/Akilleez-QA/read-em-and-weep/pull/300) at commit 95fa9ebd8f7b382f02e2abfaeac2e9fa2bf24c14. In particular N is B-flat, Ext1_S(N,S)=P=coker L, and Ext2_S(N,S) is B-free. These are exact premises, not conclusions inferred from fiber lengths.

Let A be a local Artin C-algebra, with trivial H action, and let a,b be units of A. Set R=A[[x1,x2,x3,x4]], m=(x1,x2,x3,x4), and let Nhat_a be the m-adic completion of the parameter base change N_a. Suppose phi is a continuous A-algebra automorphism of R commuting with every element of the fixed H action. Suppose there is an H-equivariant additive bijection

    F:Nhat_a -> Nhat_b,   F(rn)=phi(r)F(n).

Then a=b.

Unlike PR300, this permits nonlinear formal coordinate changes as well as module-generator changes. It does not require that phi preserve the augmentation as a separate hypothesis: that follows from the H weights, even over a nonreduced Artin base. The assertion concerns the centralizer of the fixed H action, not its normalizer, arbitrary coordinate changes, automorphisms of A, or character-twisted equivariance. No versality, representability, algebraicity of arbitrary formal deformations, or actual HM/source realization is asserted.

## 1. Equivariance fixes the origin and makes the cotangent action scalar

Write U for the normal abelian subgroup C5 squared. In the conventions of the family, the cotangent representation W has basis x_i for i=1,2,3,4 (indices modulo five), with U weights

    wt(x_i)=(i,3i^2),

and the order-four generator g sends x_i to x_(2i). The four weights are pairwise distinct and nontrivial. The top representation T has basis t_j with weights (j,0), and g sends t_j to t_(2j). Thus both representations have distinct weight lines on which g acts transitively.

The augmentation e:R->A, x_i->0, is H-equivariant. For any i, e(phi(x_i)) has weight wt(x_i), since phi and e commute with H. But A has trivial H action. Choosing an element of U whose character on x_i differs from one gives

    (chi_i(h)-1)e(phi(x_i))=0.

The coefficient is a nonzero complex number, hence a unit in A. Consequently e(phi(x_i))=0. This excludes nilpotent constants as well as nonzero residue-field constants. Applying the same argument to phi^{-1} gives phi(m)=m.

The induced automorphism of m/m^2=W tensor A is H-equivariant. To compute its commutant over A, commuting with U forces every off-diagonal entry to vanish: for two distinct weights choose h separating them and divide by the nonzero complex difference of their characters. Commuting with g makes all diagonal entries equal. Hence

    End_{A,H}(W tensor A)=A,
    End_{A,H}(T tensor A)=A.

This is a calculation over A, not an invocation of Schur's lemma over a field. In particular phi acts on m/m^2 by v times the identity, for a unit v in A. All higher-order terms of phi are allowed; they disappear in m/m^2.

The enlarged class includes explicit genuinely nonlinear automorphisms. Put q=(x1 x2 x3 x4)^5 and define phi(x_i)=x_i(1+q). Each U character has order dividing five, so q has trivial U weight. The cyclic generator permutes the four factors, and the central mu5 character also becomes trivial after taking the fifth power. Thus q is H-invariant and this substitution commutes with H. It has identity linear term. The formal inverse is obtained recursively in total degree, since its linear coefficient matrix is the identity over A; completeness gives the inverse continuous A-algebra substitution. Thus this is an automorphism over every A in the statement, including nonreduced A, and is not the identity ring map. The proof below permits these terms without needing their explicit inverse.

## 2. Completed Ext1 and its semilinear functoriality

PR300 establishes, naturally and H-equivariantly, that

    Ext1_{A[x]}(N_a,A[x])=P_a.

For clarity, the reason arbitrary nonflat parameter base change is allowed is that a finite projective S-resolution of N stays exact after tensoring with A, by B-flatness of N. The dual complex has the degree-one universal-coefficient sequence over the PID B; its correction is Tor1_B(Ext2_S(N,S),A)=0. One must not substitute a blanket assertion of base change in every Ext degree.

The ring A[x] is Noetherian. Its m-adic completion is R and is flat over A[x]. The finite projective resolution just described, after base change to A[x], therefore remains a finite projective resolution after tensoring with R. Finite projectivity identifies its dual with the completed dual complex; flatness commutes with cohomology. Consequently

    Ext1_R(Nhat_a,R)=P_a tensor_{A[x]} R=:Phat_a.

The identification is natural and H-equivariant. The finite-support presentation of P implies m^4 P_a=0, so Phat_a can also be identified with P_a. Neither this observation nor the proof requires P_a to be A-flat; at a fourth root it is precisely the nonflat defect module that must be retained.

A phi-semilinear F induces a phi^{-1}-semilinear isomorphism in the opposite direction on Ext1:

    G:Phat_b -> Phat_a.

Here is a convention-independent check of the direction. On dual maps a semilinear comparison F sends ell to phi^{-1} composed with ell composed with F; this is R-linear as a functional, and phi^{-1}-semilinear as a function of ell. Apply the same construction to resolutions (equivalently, use the exact category equivalence given by twisting scalars through phi). It induces the displayed map on Ext, independent of comparison choices. Since F and phi commute with H, so does G. Its inverse is phi-semilinear. Thus no unstated determinant or character twist occurs: this is functoriality of Ext with target the ring, not a choice of a local-duality orientation.

## 3. Initial relation recovery survives the coordinate change

For every a, Phat_a/m Phat_a=T tensor A. Because phi fixes A and preserves m, G induces an A-linear H-equivariant isomorphism on this top, hence multiplication by a unit u in A.

Consider the canonical multiplication map

    (m/m^2) tensor_A (Phat_a/m Phat_a) -> m Phat_a/m^2 Phat_a.

Let R_a denote its kernel. Semilinearity makes the corresponding diagrams for a and b commute, with map phi^{-1} on the cotangent factor and the top map of G on the other factor. The source map is multiplication by the single unit v^{-1}u. It carries R_b onto R_a. Multiplication by a unit preserves every A-submodule, so R_a=R_b inside the common free module W tensor T tensor A.

The presentation defining Phat_a has ten linear columns:

    m_i = x_i t_(3i),
    l_i = x_i t_i - a x_(-i)t_(3i),  i=1,2,3,4,
    c1 = x1 t4 - x4 t1,
    c2 = x2 t3 - x3 t2.

Its initial relation module R_a is exactly their A-span. Indeed the degree-one part of any formal combination of linear columns depends only on the constant coefficients of that combination. Conversely every constant combination is a degree-one relation. This argument still holds with nilpotent coefficients and without assuming any flatness of P_a.

In the two-coordinate direct summand of W tensor T spanned by x_i t_i and x_(-i)t_(3i), the displayed l_i is the only column with support. The remaining l columns, four monomial columns, and two clock columns have disjoint support from this summand. Projection of R_a=R_b onto this summand gives

    A(1,-a)=A(1,-b) inside A^2.

Write (1,-a)=q(1,-b). Comparing first coordinates gives q=1, and second coordinates give a=b. There is no cancellation by a possibly nonunit element and no passage to the residue field. This proves recovery of the entire Artin parameter.

## 4. Infinitesimal consequence and boundaries of the result

Take A=C[epsilon]/(epsilon^2), a=c+w epsilon and b=c, for any c in C* including c^4=1. An equivalence to the constant deformation, even after an H-equivariant continuous A-linear coordinate change, forces w=0. Thus the known tangent direction remains nonzero after quotienting by this coordinate-change gauge group, not merely in PR300's fixed-ring category. Taking arbitrary local Artin A proves the analogous separation of all finite-order parameter jets.

No hypothesis that the coordinate automorphism reduce to the identity was imposed. The argument therefore also excludes an unmarked equivalence, which is stronger than excluding only equivalences inducing the identity on the special fiber.

The centralizer restriction is essential to what is proved: an automorphism conjugating H through a nontrivial automorphism could permute weight labels, and the scalar-commutant argument would no longer apply. Likewise an automorphism of the coefficient algebra A is not allowed, and a character-twisted isomorphism of the H modules is not the specified equivariant map. No conclusion about those larger equivalence relations is drawn. The theorem does not classify other deformation directions or say every coordinate change can be reconstructed from an isomorphism of the defect modules.

## Verification status

Authored structural proof. Checked directly: augmentation preservation including nilpotent constants; scalar commutants over A; flat-completion Ext comparison; semilinear contravariance; and the disjoint two-monomial block. No selected HM/source instance, search, or large computation was executed. Independent review is required before publication.
