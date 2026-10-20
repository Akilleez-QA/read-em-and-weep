# Preserved conditional module-application audit

The endpoint and pairing inputs are hypotheses listed in unit09 INPUTS.md, not supplied by the geometric conductor theorem.

## Pairing blocks, spatial contractions, and their exact count

Let U=M₋₅, T=M₋₄, with dimensions 2 and 10. Define μ:S₁⊗U→T by multiplication and α:T→M₀⁵ by the five j-coefficients. Under the perfect pairing M₀=U*, the output-r/input-s block of αμ is

    C_rs(h,h′)=⟨s h,j_r h′⟩=⟨h,(s j_r)h′⟩.

Indeed the output j_r s h paired with h′ gives the same expression by multiplication compatibility and symmetry. Interchanging h and h′ preserves this expression, so each block belongs to Sym² U*. There is no resulting symmetry between its two spatial indices r and s. In particular it is not justified to regard the entire 10-by-10 matrix as symmetric.

For a vector-field column Av, its syzygy gives

    Σ_{r,s} A_rs C_rs=tr(AᵗC)=0.

Thus the four identities displayed in PROOF.md have the correct indices and coefficients. The Euler condition is the spatial partial trace; the other three are the infinitesimal Lie contractions. The four coefficient tensors are independent. Consequently their tensor product with the three-dimensional space Sym² U* gives exactly twelve independent linear equations on the unrestricted 75-dimensional space of twenty-five symmetric 2-by-2 blocks. The resulting ambient linear space has dimension 63.

Equivalently the block tensor is the pullback of a linear map

    K₅→Sym² U*,

or an element of K₅*⊗Sym² U*. This factors out precisely the four polynomial degree-five syzygies. The actual graded module can impose further equations; neither 63 nor 21 is a dimension or rank claim about the actual HM pairing family.

These constraints apply to αμ. Transporting them to a matrix of α by an inverse of μ requires a separate proof that μ is an isomorphism. Even under that extra assumption, the displayed contractions alone do not establish a singular matrix.

## 6. Endpoint complexes and the newly proved vanishing

Applying the polynomial syzygies to an arbitrary graded S-module gives the complexes

    M₋₆⁴ --L_M→ M₋₅⁵ --α*→ M₋₁,
    M₋₄ --α→ M₀⁵ --L_M*→ M₁⁴.

The second is dual to the first using M_t*=M₋₅₋t; L_M* is the displayed transpose matrix acting by multiplication. Thus im L_M⊂ker α*, and formally

    rank α≤10−dim im L_M.

For a general module this inequality contains an unevaluated module map. Tensoring the free resolution with M need not preserve exactness, so equality of im L_M and ker α* is not available.

The listed six Hilbert-function entries alone do not justify setting M₋₆ to zero. However, prerequisite hm-low-degree-dependency, document PROOF.md (see the unit INPUTS.md) now supplies an independent geometric proof of M₁=M₋₆=0 for the actual HM module. Its essential chase is sound:

- A regular section of F(3) has smooth abelian zero surface A, giving 0→O(−3)→F→I_A(2)→0.
- Tensoring by F∨(t)=F(t+1) gives 0→F(t−2)→End(F)(t)→I_A⊗F(t+3)→0.
- The regular-section normal identification is N_(A/P⁴)=F(3)|A, so the restriction sequence ends in N(t).
- For t≥1, Kodaira vanishing, the restricted Euler sequence, and the trivial tangent bundle of A give H¹N(t)=0.
- The verified H²F support at twist −2 gives H²F(t−2)=H²F(t+3)=0 for every t≥1. The two exact cohomology segments therefore give H²End(F)(t)=0, and hence H²B(t)=0.
- Trace/Serre duality gives the corresponding vanishing for every t≤−6.

There is no endpoint exception at t=1: its two F twists are −1 and 4, neither equal to −2. No incoming-map rank or surjectivity is needed.

Accordingly the first term of the first complex and the last term of the dual complex are zero for the actual module. These complexes supply no nonzero element of ker α* and no nontrivial equation after α in that degree. The general Euler implication α invertible ⇒ S₁M₀=0 is automatically satisfied because M₁=0 and contributes no obstruction here. The degree-zero block identities of §5 remain nontrivial constraints; endpoint vanishing neither proves μ invertible nor makes the tensor complex exact.

## 7. Lowest generation and the cofactor defect

The explicit B basis identifies

    Σ B_r M₋₅=S₁M₋₅=im μ.

The dual of μ is the map M₋₁→S₁*⊗M₀ given by all five coordinate products. Hence

    (im μ)⊥=Soc(M)₋₁,
    μ is an isomorphism ⇔ Soc(M)₋₁=0,

where the last equivalence also uses that both source and target of μ have dimension ten. Equal dimensions alone do not imply either condition.

With Q=I:T→M₋₂, R=J:T→T*, K_primary=ker Q, and W_low=im μ, consider the image RK_primary⊂T*. Restriction from T* to W_low* has kernel W_low⊥. Therefore the loss of rank upon restricting the cubic pairing to W_low is exactly

    c−e=dim(RK_primary∩W_low⊥)
       =dim(JK_primary∩Soc(M)₋₁).

This verifies the stated defect formula directly. Neither the universal B coefficients nor the Hilbert–Burch syzygies prove that this intersection is zero. The separate quadratic-image defect, actual primary map, and secondary map remain undetermined.

## Final assessment

The proof successfully removes the ambiguity in the universal conductor quartics and supplies all their polynomial syzygies. It gives genuine necessary constraints on the actual multiplication maps while preserving the distinction between polynomial identities, module relations, and unevaluated cohomological data. No retained obstruction or actual rank is settled by these structural results.
