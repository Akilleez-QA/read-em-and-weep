# One-factor reversal is excluded by the intrinsic first-order bracket

## Result

For the corrected pair algebroid on Y=P² with coefficient K=ω_Y, an identity-on-base Morita self-comparison cannot reverse K. Its first-order commutator is the nowhere-degenerate, K-valued bracket

    [f,g]=df∧dg.

This bracket is preserved by any invertible Morita bimodule whose classical reduction is a line on the identity graph. It forces coefficient action +Id. A Morita comparison from the opposite pair to the original instead forces coefficient action −Id. Applied to both factors, an opposite-to-original comparison must reverse BOTH pure coefficient lines, so its mixed coefficient action is +Id. A one-factor reversal fails already on one pure restriction, before unary or triple data can help.

This is a proved symbol obstruction, not merely the absence of a supplied comparison. It closes the proposed identity-reduction one-factor-sign shortcut. It does not evaluate the canonical mixed module obstruction or any of its thirty retained detector values.

There is also a positive refinement: the full opposite pair admits an explicit return Morita comparison after coefficient reversal and transport by O(1). It matches unary and triple data exactly. Its external product still acts positively on the mixed ideal; hence it supplies no tracefree vanishing equation.

## Inputs and restrictions

Historical public context, comment 6272324961:
https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6272324961

Read null-actual-pair-comparison/RESULT.md, null-mixed-duality-reversal/DUALITY-RESULT.md and DUALITY-AUDIT.md, and null-root-morita-inertia/root-morita-0719/RESULT.md. Checked the pinned source, including its row convention and total Čech–forms signs:
https://github.com/Akilleez-QA/read-em-and-weep/blob/c8aec970fd65a105f39f4e8aeb8a17f0f0053f89/research/hm/second-order-algebroid.md

All statements concern ordinary algebraic sheaf/Morita comparisons of the stipulated corrected square-zero presentations.  No assertion about arbitrary derived equivalences without the stated classical reduction is needed.

## 1. Intrinsic bracket, center, and coefficient identification

Write A₊=O_Y⊕K with

    (f,η)⋆(g,θ)=(fg,fθ+gη+½df∧dg).

K is central, K²=0, and A₊/K=O_Y. It is intrinsically the nilradical: a nilpotent section has nilpotent reduction in the reduced ring O_Y, hence belongs to K. The commutator of any lifts of f,g∈O_Y is independent of their lifts and equals df∧dg. Thus it defines

    b_A : ∧²Ω¹_Y → K,   df∧dg ↦ df∧dg,

which is the identity of ω_Y. Locally in smooth coordinates, commutators generate K as an O-module. In particular this invariant is nonzero on every smooth chart, not a class whose Čech coboundary could remove it.

For completeness, the center consists locally of pairs (f,η) with df=0, together with arbitrary η. Indeed df∧dg=0 for all g implies df=0 on a smooth surface. Thus K is a central nilpotent ideal, but its bracket with the reduced algebra retains information that the abstract center alone would miss.

If Φ:A₊→A₊ reduces to Id and acts on K by ψ, then

    ψ(df∧dg)=Φ([f,g])=[Φ(f),Φ(g)]=df∧dg.

Therefore ψ=Id. Adding any first-order correction Φ(f)=f+D(f) cannot change this equation, since K is central. Equivalently, a change of splitting adds a Hochschild coboundary, whose antisymmetric part is zero over the commutative reduction.

For A₊^op, the bracket is −df∧dg. The same calculation for Φ:A₊^op→A₊ gives ψ=−Id. These are necessary conditions for ANY local algebra comparison, independently of overlap and gerbe choices.

## 2. Why rank-one Morita transport cannot evade it

Let P be an invertible (A,B)-bimodule inducing a classical equivalence on the identity graph. Its reduction P̄ is an invertible O-module, hence a line. On an open trivializing P̄, the finitely generated projective right B-module P is free of rank one: lift a local generator, use nilpotent Nakayama for surjectivity, and projectivity plus reduction to rank one to kill the kernel. This argument is local and only uses the nilpotent extension.

Choose a right B-generator. The invertible Morita action then identifies

    A ≅ End_B(P) ≅ B

as local algebras, with the chosen classical identity on O. A different generator changes the identification by inner conjugation. Inner conjugation acts trivially on the central ideal K and on the commutative reduction O. Hence the coefficient map and bracket compatibility above are independent of the generator and glue.

Consequently rank-one Morita equivalence preserves this bracket under its induced coefficient map. Tensoring by a genuine classical line can change unary and scalar Čech data, but not the local alternating product. This also follows directly from the exact Morita formulas in root Morita report: μ^L=μ. A line twist cannot turn P into −P while fixing the coefficient marking.

The same local proof applies when the reduction is a line on the graph of a specified geometric automorphism, with the semilinear version of the bracket equation in Section 5.

## 3. Sign-reversed presentations versus self-symmetries

Let A₋ be obtained by reversing the coefficient parameter in all of the corrected pair data. Its local product is −½df∧dg, its unary correction is −df∧β/2, and its triple coefficient is +2β². There is a tautological isomorphism

    S:A₋→A₊,   S(f,η)=(f,−η).

It matches all three pieces. This does NOT give an automorphism of A₊ with negative coefficient action. It compares two differently marked deformations, and its negative coefficient map is exactly what is required to identify their opposite brackets. If one first reverses the parameter and then uses S to return, the two sign changes cancel on the identified coefficient line. Treating S as a self-map while forgetting the changed source would manufacture the false equation C=−C.

Likewise, for a two-parameter presentation, base change s↦−s transports its obstruction to the changed ambient and changed boundary. A comparison with negative map on that changed pure coefficient simply transports it back. It does not furnish a negative automorphism of the fixed obstruction problem.

## 4. Full opposite return exists, but has the harmless mixed sign

Use the corrected pair presentation

    μ(f,g)=½df∧dg,
    v_ij(f)=½df∧β_ij,
    A_ijk=(1,b_ijk),   b_ijk=−2(β²)_ijk,

where β_ij=dlog t_ij for e_j=t_ij e_i in O(1). In the opposite algebroid the product is opposite, unary maps are the same, and central triple units invert. Thus its data are (−μ,v,−b).

Apply coefficient negation S. The resulting presentation B has data

    (μ,−v,b).

Now apply the exact line Morita transport with L=O(1) and q_ij=t_ij. These lifts are star-invertible with inverse t_ij⁻¹. Its unary correction is

    (−v)^L_ij(f)=−½df∧β_ij + df∧β_ij = v_ij(f).

The scalar correction from the exact formula is

    b^L_ijk=b_ijk − (−v_ij)(t_jk)/t_jk
                       − μ(t_jk,t_ij)/t_ik.

The two terms cancel literally, because

    (−v_ij)(t_jk)/t_jk = +½β_ij∧β_jk,
    μ(t_jk,t_ij)/t_ik = −½β_ij∧β_jk.

Thus B^L has exactly (μ,v,b), including the fixed triple cocycle, with no unspecified scalar primitive. The genuine t cocycle supplies all coherence through the exact Morita construction. This gives a full opposite-to-original Morita comparison, whose coefficient map is −Id; the subsequent line transport acts identically on the coefficient ideal.

For the external product, use L=O(1,1) and the external tensor of these comparisons. The exact product Morita formulas preserve all mixed terms. Both pure coefficient maps are negative, so the map on J=K_z⊗K_h is positive. At the level of module reduction, the untwisting functor sends E* to E*⊗O(−1,−1), which is E by the canonical determinant-valued rank-two identification when det E=O(−1,−1). This is consistent with the determinant sign in null-mixed-duality-reversal.

Combining this positive mixed action with the actual contragredient obstruction operator −† gives +Id on End₀(E)⊗J. The resulting self-duality condition is tautological on the tracefree obstruction. This strengthens the previous conditional discussion by providing the ambient return comparison; it still gives no vanishing.

## 5. Geometric automorphisms and determinant bookkeeping

Let φ be a geometric automorphism of a smooth surface. An algebra comparison covering φ has a semilinear coefficient map Ψ. Naturality of commutators forces, for an ordinary-to-ordinary comparison,

    Ψ(df∧dg)=d(φ*f)∧d(φ*g)=φ*(df∧dg).

Since these forms generate K, Ψ is exactly the canonical pullback on top forms. For an opposite-to-original comparison, Ψ is its negative. Hence even allowing a geometric automorphism gives no extra independent negative scalar on the canonical coefficient line. In coordinates the Jacobian determinant appears on BOTH sides of this identity. A coordinate orientation reversal is not an additional parameter reversal once K is canonically marked.

For Y=P(V), dim V=3, the canonical GL(V)-equivariant line is

    K_Y = O_Y(−3) ⊗ det(V*)

with the convention that P(V) parametrizes lines. Omitting det(V*) creates a spurious determinant character. In particular scalar matrices act trivially on the geometric canonical bundle: the scalar weight of O(−3) cancels that of det(V*). The canonical bracket ∧²Ω¹→K is the identity tensor and is preserved by every geometric automorphism with its canonical coefficient action. No choice of determinant −1 representative in GL₃ supplies an antibracket automorphism of this canonically marked pair.

For factor-preserving φ on P²×P², an ordinary self-comparison therefore has the canonical actions on K_z and K_h; an opposite return has their negatives. The product action on J is the canonical action in either case. Factor exchange only permutes these two lines; the exchange of two degree-two forms has sign +1. Accordingly these geometric possibilities do not create an isolated negative scalar on J.

A nonidentity φ may nevertheless act nontrivially on H²(End₀(E)⊗J), and would require an actual lift identifying φ*E with E and the pure boundary. Any relation it yields is invariance under that full cohomological action, not C=−C inferred from a coordinate determinant. This report does not claim that every conceivable geometric action is trivial on the retained space.

## 6. Two-factor pure restrictions make the no-go decisive

Let I_z,I_h be the two pure ideals in the external product and J=I_z I_h. Modulo J, the bracket has independent components

    b_z(df,dg)=d_z f∧d_z g,
    b_h(df,dg)=d_h f∧d_h g.

For functions from the z factor, only b_z survives; for functions from h, only b_h survives. Restricting any identity-reduction Morita comparison to each pure quotient therefore forces its two signs separately. No mixed-order change can repair an already incorrect pure bracket.

An ordinary self-comparison requires (+,+), while an opposite-to-original comparison requires (−,−). A proposed (−,+) or (+,−) action fails one of these independent identities. Multiplication identifies (I_z/J)⊗(I_h/J) with J in the fixed external product, so the permitted scalar action on J is always +1. Even allowing linear mixing of pure ideals does not evade the identity-base statement: the two partial bracket images generate their respective summands, so bracket compatibility fixes them separately.

## Conclusion

The one-factor-reversal vanishing strategy is formally ruled out for identity-reduction algebra/Morita comparisons of this corrected external-product ambient, and geometric canonical-line bookkeeping cannot restore it by a determinant sign. The full opposite return can be constructed and confirms the double reversal, positive mixed coefficient, and tautological tracefree self-duality equation. The exact thirty-detector annihilation problem remains unevaluated.
