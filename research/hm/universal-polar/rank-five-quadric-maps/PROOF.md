# Five independent quadratic coordinates on a smooth quadric threefold

Work over C. Let V have dimension four and let W ⊂ Sym²V be a five-dimensional space of quadratic polynomials on V*. Suppose a basis q₀,…,q₄ has generic Jacobian rank four and satisfies a quadratic relation qᵀCq=0 with C nonsingular.

## Result

There is a nonzero linear form e∈V and a quadratic form h such that

    W=eV+Ch.

After linear changes of variables and of the basis of W, the coordinates are

    (x₀², x₀x₁, x₀x₂, x₀x₃, H(x₁,x₂,x₃)),

where H is a nondegenerate ternary quadratic form. The gcd of the maximal Jacobian minors is exactly x₀² up to scalar. In particular, it cannot be an irreducible quadratic polynomial.

The proof uses the previously established pure symmetric-tensor incidence lemmas, not a claimed exhaustive standard-parametrization theorem.

## 1. Elementary ternary lemma: no rank-five relation for the Veronese surface

For a three-dimensional vector space U, the kernel of

    Sym²(Sym²U) → Sym⁴U

contains no quadratic form of rank five. Its possible nonzero ranks are precisely 3, 4, and 6.

To see this, let S be a formal symmetric 3×3 matrix with six independent entries sᵢⱼ. Substituting S=uuᵀ makes every entry of adj(S) zero. Its six independent entries are linearly independent quadratic polynomials in the sᵢⱼ. They span the kernel: multiplication is surjective, and its source and target have dimensions 21 and 15. Consequently every relation is

    F_A(S)=tr(A adj(S))

for a unique symmetric 3×3 coefficient matrix A. Under S↦PSPᵀ, the formula

    adj(PSPᵀ)=det(P)² P⁻ᵀ adj(S) P⁻¹

shows that the coefficient matrix changes by congruence, up to a nonzero scalar. Over C, a symmetric A is congruent to diag(I_r,0), where r is its rank. For r=1,2,3 the corresponding relations, after a possible relabeling, are respectively

    s₂₂s₃₃−s₂₃²,
    (s₁₁+s₂₂)s₃₃−s₁₃²−s₂₃²,
    s₁₁s₂₂+s₁₁s₃₃+s₂₂s₃₃−s₁₂²−s₁₃²−s₂₃².

Their ranks are 3,4,6. This proves the lemma directly, with no external classification.

## 2. Every linear form has a product partner in W

For any nonzero e∈V, restrict quadrics to the plane e=0. If W→Sym²(V/Ce) were injective, its five-dimensional image would carry the same nonsingular rank-five relation C. Extending this relation by zero on a complementary sixth coordinate would give a rank-five element of the ternary Veronese relation space, contradicting Section 1. Thus

    W∩eV ≠ 0 for every e∈V.

Also W has full support: if W⊂Sym²U for some proper U⊂V, its polynomials depend on at most three independent variables, contrary to generic Jacobian rank four.

## 3. Application of the previously proved pure incidence lemmas

Here are the exact inputs already proved in the sibling folders:

* nonlinear-curve-factor-exclusion/PROOF.md: a full-support five-space cannot have a nonlinear curve of first factors each with a projective line of second partners;
* one-planar-factor-exclusion/PROOF.md: a two-dimensional ordered product family in a five-space cannot have one factor image a plane and the other a nonplanar surface.

Both inputs are independent of any additional compatibility map or square-avoidance condition.

For a∈V put N_a={b∈V:ab∈W}. The matrix of these equations is the symmetric annihilator evaluation matrix of W; Section 2 says its generic rank is at most three. Generic rank at most two contradicts the nonlinear-curve lemma, by choosing a nonlinear curve through the generic open and a rank-two subbundle of its partner kernels. Hence the generic kernel is a line and defines f:P(V)⇢P(V).

Let D be its image. Symmetry gives that the inverse fiber over b is contained in P(N_b), so generically dim N_b≥4−dim D.

If dim D=2, a nonlinear curve in D contradicts the nonlinear-curve lemma. If dim D=1, the same lemma forces D to be a line P(L). For distinct general b,c∈P(L), dim N_b=dim N_c=3: dimension four would force a constant generic partner. The three-spaces bN_b and cN_c in W intersect exactly in Cbc, since their sum has dimension at most five and the intersection of bV and cV is Cbc. Consequently L⊂N_b, Sym²L⊂W⊂LV, and W/Sym²L is a two-dimensional subspace of L⊗(V/L) containing rank-one tensors with all general first factors in L. Its determinant vanishes identically. Such a pencil has a fixed second factor (a fixed first factor is excluded); therefore W is supported on a three-space, contradiction.

If dim D=3, symmetry gives f²=id generically. The plane/nonplanar lemma implies that a general plane is mapped to a plane. The degree-one argument in nonplanar-factor-degree-bounds/PROOF.md, Section 3, then shows f is induced by an invertible linear map T. Therefore W contains the span of aT(a) for all a∈V. This span has dimension at least six: triangularizing T with nonzero eigenvalues λ₁,…,λ₄, the induced operator on Sym²V has diagonal entries λᵢ+λⱼ. The four diagonal-pair entries are nonzero and at most four of the six off-diagonal-pair entries vanish. This contradicts dim W=5.

Thus D is a point [e]. Closure gives eV⊂W, and the dimension gives W=eV+Ch.

This is precisely the ambient-rank-three analysis of nonplanar-factor-degree-bounds/PROOF.md, Sections 1–3, with its surviving constant-partner case retained. No hypothesis about a particular surface family is needed for this classification.

## 4. Normal form and minor gcd

Choose e=x₀. Subtracting an element of x₀V from h leaves h=H(x₁,x₂,x₃), nonzero because dim W=5. In the indicated basis the image satisfies

    q₀q₄−H(q₁,q₂,q₃)=0.

This polynomial is irreducible: as a polynomial linear in q₄ its two coefficients q₀ and −H are coprime. Generic Jacobian rank four implies that the image is dense in this hypersurface, so every quadratic relation is a scalar multiple of it. Its rank is 2+rank(H). Therefore the assumed rank five forces rank(H)=3.

The Jacobian rows are

    (2x₀,0,0,0),
    (xᵢ,x₀δᵢ₁,x₀δᵢ₂,x₀δᵢ₃), i=1,2,3,
    (0,H₁,H₂,H₃).

Its maximal minors, with irrelevant signs suppressed, are

    2x₀²H, 2x₀³H₁, 2x₀³H₂, 2x₀³H₃, 2x₀⁴.

They have gcd x₀² because H is nonzero and independent of x₀. Invertible row operations and invertible linear changes of variables preserve the gcd up to scalar and change of variables. Thus the original gcd is a square of a linear form.

## Scope

Only abstract algebra and previously established pure incidence lemmas were used. The ternary classification was proved explicitly above; no niche external theorem or unverified exhaustive parametrization classification is used. The calculation of minors is symbolic and elementary.
