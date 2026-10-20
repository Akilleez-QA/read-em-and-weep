# Independent audit: mixed-obstruction duality and retained Serre detector

## Verdict

The proposed conclusion is correct with qualifications: rank-two alternating self-duality does not force the tracefree mixed obstruction to vanish. The relevant transformation of the normalized multiplicative gluing defect is **minus adjoint**, and the alternating adjoint on tracefree rank-two endomorphisms is **minus identity**. Their composite is identity. This is a statement about obstruction naturality for dualization, not a claim that all contravariant actions on Ext² have an intrinsic minus sign.

A stronger assertion that the actual fixed-ambient mixed problem possesses a self-duality symmetry requires extra data. Classical E ≅ E*⊗det(E) alone does not furnish such a symmetry of its noncommutative deformation problem.

This audit uses only formal transition identities and the previously established geometric cohomology decompositions. 

## 1. Defect sign, including opposite coefficients

Use the row convention of null-mixed-module-equation/RESULT.md. In the mixed small extension, write the module equation defect in multiplicative normalized form as

    F_ij(G_jk) ⋆ G_ij = A_ijk ⋆ G_ik ⋆ (1+C_ijk).

Here C is End(E)⊗J-valued, J=ω_X, J²=0, and positive-order ambient coefficients annihilate J. This is precisely the additive normalized defect C=g_ik^−1 R_ijk to the order under consideration. Moving C to the other side changes its frame by classical conjugation and does not change the intrinsic endomorphism-valued class.

Transpose must be interpreted as an anti-map Mat_r(B)→Mat_r(B^op), not as an anti-map of Mat_r(B) with unchanged noncommutative coefficients. Inverse transpose is therefore a group homomorphism between the corresponding invertible matrix groups. Applying it to the displayed equation takes the infinitesimal defect to

    (1+C)^−t = 1−C^t.

The classical transition factors transport this into the appropriate dual frame. The induced obstruction class for the dual module over the opposite ambient is thus minus the ordinary sheaf transpose of the original class. This calculation pins the sign to the gluing equation, rather than guessing it from a generic slogan about dualizing an Ext² element.

The categorical dual reverses arrows and exchanges right and left modules. Translating back into the chosen row-module convention is part of the calculation. Ignoring the opposite ambient or this reversal is not justified.

## 2. Alternating adjoint and determinant line

For any rank-two bundle, wedge product supplies the nondegenerate alternating pairing

    E⊗E → L,    L=det E,

and hence E ≅ E*⊗L. Locally let J represent this pairing. The induced adjoint is

    T^† = J^−1 T^t J = tr(T)·Id − T.

Consequently T^†=−T on End₀(E), while Id^†=Id. The line-frame scaling of J cancels in J^−1 T^t J, so this adjoint is globally well defined even when L is nontrivial. No trivialization of det E is needed for this classical identity.

Combining this with the actual multiplicative-defect sign gives

    C ↦ −C^† = C     on End₀(E)⊗J.

Thus even a compatible self-duality of the deformation problem would give the tautology o=o on its tracefree mixed obstruction, not o=−o. In characteristic zero this cannot imply vanishing.

The scalar part has opposite behavior under minus adjoint, but H²(X,ω_X)=0 already removes scalar obstruction classes in this problem. That scalar fact cannot be extended to End₀.

The determinant caveat is substantive: the classical line L does not automatically lift as an invertible bimodule implementing an equivalence of the deformed algebroids. Nor can one blindly take the ordinary determinant or exterior power of a module over a noncommutative algebra. A comparison of the dual deformation with the original requires a compatible deformed pairing/twist or other specified Morita-type equivalence, as well as compatibility with the chosen pure boundary. The formal matrix identity does not construct these data.

## 3. Why the opposite ambient cannot silently be identified

For the central-unit presentation in null-mixed-module-equation, passage to the opposite ambient replaces the local product by its opposite and replaces the central triple unit A by A^−1. The overlap algebra maps F remain the same underlying maps, interpreted between opposite algebras. In particular, if

    A=(1+b)(1+c),

then

    A^−1=(1−b)(1−c)=1−b−c+bc.

For the external-product multiplication, the pure alternating biderivations change signs and the tensor-product mixed bidifferential is unchanged. This resembles simultaneous reversal of the two infinitesimal directions. However, such a reversal also changes the signs of the pure overlap corrections v^z,v^h, whereas taking the opposite leaves the underlying F maps unchanged. Therefore a literal equality of the opposite presentation with the original presentation after parameter reversal has not been established by inspecting products alone.

Any identification may require additional overlap gauge data and determinant-line twisting. Its existence and compatibility must be proved rather than assumed. If a genuine self-comparison acts nontrivially on the coefficient line J or by a base automorphism, that action must also be included; the plus conclusion above refers to the identity coefficient comparison. The simultaneous two-direction sign reversal itself acts as +1 on J=K_z⊗K_h.

These limitations only weaken a proposed vanishing argument. They do not weaken the conclusion that ordinary rank-two self-duality alone supplies no tracefree mixed vanishing theorem.

## 4. Exact Serre detector for the retained thirty dimensions

Let A₀=End₀(E), B₀=End₀(HM), F=m_*O_X. The trace pairing identifies A₀* with A₀. On the fourfold X, Serre duality supplies a perfect pairing

    H²(X,A₀⊗ω_X) × H²(X,A₀) → C,
    (o,a) ↦ ∫_X tr(o∪a).

The degree-two/degree-two cup product has sign (−1)^(2·2)=+1. There is no degree-induced antisymmetry here that would force the pairing to vanish.

Use the canonical trace splitting and block involution from pair quotient report:

    F=O·1 ⊕ F₀,    F₀=ker(tr:F→O),
    F₀=F₀⁺ ⊕ F₀⁻.

Finite duality identifies the obstruction space with H²(P⁴,B₀⊗F*⊗ω_P⁴), while its Serre dual is H²(P⁴,B₀⊗F). Thus the canonical even retained space and its dual are

    V_ret = H²(P⁴,B₀⊗(F₀⁺)*⊗ω_P⁴),
    W_ret = H²(P⁴,B₀⊗F₀⁺).

They are perfectly paired and each has dimension thirty under the imported twist ranks. Equivalently, W_ret is the canonical quotient

    H²(X,A₀)⁺ / W_const,

where W_const is the two-dimensional constant-summand subspace H²(P⁴,B₀), embedded using O→F. As a quotient of the full 62-dimensional Serre-dual space, one must also remove the entire odd summand. The trace splitting gives a preferred complementary summand, so quotient and summand formulations agree canonically here.

Hence the retained projection of o vanishes if and only if

    ∫_X tr(o∪a)=0   for every a in W_ret,

where a is represented by the canonical summand inclusion. If o itself is already known to lie in V_ret, it annihilates W_const and the odd subspace, so pairing with equivalence classes in the stated quotient is independent of the chosen representative. Without that hypothesis, pairing the unprojected o with an arbitrary quotient representative is not well defined; use the canonical splitting or first project o.

The other 30-dimensional space, the block-odd obstruction sector, is different. Its equal dimension is irrelevant and does not make it the detector for V_ret. The geometric canonical action on ω_X is essential for the equivariant Serre pairing; swapping two surface factors contributes +1, as checked in pair quotient report.

This is a complete dual criterion, not an evaluation. It neither constructs thirty test cochains nor proves any of their values zero. It also concerns the fixed external-product ambient obstruction; comparison to a frozen physical two-jet remains an additional requirement.

## Inputs checked

- null-mixed-module-equation/RESULT.md, including the normalized defect and pure-gauge invariance.
- null-pair-quotient-bracket/pair-quotient-0512/RESULT.md, including finite duality, the canonical trace splitting, the 32/30 parity dimensions, and the retained 2+30 decomposition.
- null-pure-lift-uniqueness/pure-lift-uniqueness/RESULT.md, including fixed-ambient pure-boundary uniqueness and its limits.
- null-module-boundary-audits/module-parity/RESULT.md, for the distinction between an allowed obstruction space and an actual vanishing theorem.

The companion DUALITY-RESULT.md was not yet present when the independent argument above was written. Its final wording will be checked separately when available.

## Final companion-result check

Read null-mixed-duality-reversal/DUALITY-RESULT.md after it appeared. Its conclusions and essential qualifications pass this audit. In particular:

- Block-evenness follows from the actual exchange-linearized external-product ambient and the uniquely compared pure boundary, rather than from a dimension count. The mixed tensor ideal has the correct plus exchange sign.
- The Čech detector formula transports the second factor into the first-index frame and has total degree four, with no sign from exchanging degree-two factors.
- The constants projector λ↦[f↦λ(1)Tr(f)/6] is the correct transpose of unit·Tr/6. Its complement and the quotient caveat are stated correctly.
- The inverse-transpose sign, determinant twist, opposite-algebroid warning, and coefficient action ε are all included.

For precision, the product identity (ab)^−t=a^−t b^−t in that result is understood with the product on the right taken in the opposite-coefficient matrix algebra. Its subsequent opposite-algebroid paragraph provides this context. A hypothetical one-factor reversal forces vanishing only under the specified full self-comparison yielding exactly ε(−†); an arbitrary base automorphism that reverses one parameter can additionally act on cohomology and needs its own invariant-space calculation.

No correction to the substantive result is required. All obstruction values remain unevaluated.
