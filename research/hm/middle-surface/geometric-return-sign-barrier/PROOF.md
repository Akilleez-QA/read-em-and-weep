# Geometric base changes cannot supply a negative mixed coefficient character

## New statement and assumptions

Let X=P²_C × P²_C. Put L_z=p_z*Ω²_P²=O(-3,0), L_h=O(0,-3), and J=L_z⊗L_h=ω_X. Assume the pure square-zero restrictions of the specified ambient have intrinsic commutators β_z(f,g)=d_z f∧d_z g and β_h(f,g)=d_h f∧d_h g. Keep the multiplication identification L_z⊗L_h→J, with commuting coefficient products as in the specified external product. If I is the full nilpotent ideal, retain I·J=J·I=0. A geometric return means an algebra isomorphism from the full opposite ambient to the original covering a biregular automorphism φ of X, preserving the pure ideal filtration, with the induced permutation of the two pure lines agreeing with φ. The same conclusion holds locally for an invertible bimodule locally right-free of rank one whose classical action is the graph of φ, with these marked coefficient actions.

Then each pure coefficient map is MINUS its canonical differential pullback, and its mixed coefficient map is PLUS the canonical pullback on ω_X. This includes arbitrary product projective automorphisms and factor exchange, not just identity-reduction returns. For a geometric automorphism of the original ambient, both pure signs are plus and the mixed sign is again plus. No additional scalar freedom on J is available.

This is a necessary condition. It neither constructs a return nor asserts that pullback on obstruction cohomology is the identity. In particular a geometric automorphism may still have negative eigenspaces on the retained detector or obstruction space.

## 1. Every biregular base automorphism preserves or exchanges the factors

Pic(X)=Z H_z ⊕ Z H_h. Its nef cone is the positive quadrant: restriction to a line in either fiber tests the two coefficients, and nonnegative combinations are globally generated. An automorphism and its inverse preserve nef classes, so they permute the two primitive extremal generators. If φ*H_z=H_z and φ*H_h=H_h, the complete linear systems |H_z| and |H_h| show that φ is a product of projective linear automorphisms. If the generators are exchanged, compose with factor exchange first. Thus Aut(X)=(PGL₃×PGL₃)⋊C₂. This is an elementary Picard/linear-system argument, independent of source values.

In particular the canonical differential pullback permutes L_z,L_h in the same fashion. Their tensor product is ω_X; exchange introduces (-1)^(2·2)=+1 on top forms.

## 2. Bracket naturality fixes the coefficient maps

Work with φ* of the opposite sheaf, so the map now covers identity. On an open chart the canonical differential identification j_i:φ*L_i→L_{σ(i)} satisfies

    j_i(φ*β_i(f,g)) = β_{σ(i)}(φ*f,φ*g).

This is the chain rule for exterior differential forms along the corresponding factor, including exchange. Any coefficient identification λ_i:φ*L_i→L_{σ(i)} differs from j_i by a unit c_i. Globally these units are constants since X is connected and projective, but constancy is not needed below.

For any square-zero extension of a commutative algebra by a symmetric module, the commutator is intrinsic and any algebra map carries source commutators to target commutators. The opposite commutator is -β_i. Consequently an opposite return satisfies

    β_{σ(i)}(φ*f,φ*g) = -λ_i(φ*β_i(f,g)).

The wedges of local differentials generate the coefficient line. Comparison with the chain-rule identity gives c_i=-1 on every chart, hence λ_i=-j_i globally. This argument allows arbitrary initially chosen unit multipliers, not only signs. For an automorphism of the original ambient the same argument gives c_i=+1.

## 3. Mixed consequence and higher-order rigidity of this sign

Multiplicativity and the retained identification J=L_z⊗L_h force λ_J=λ_z⊗λ_h, followed by the ordinary exchange of the coefficient factors if needed. Thus λ_J=j_z⊗j_h. Since the degrees of the two differential factors are both two, this is exactly canonical pullback on ω_X, with positive relative scalar.

Terms of mixed order added to pure images do not change their product. Locally the parameter relations are s²=t²=0 with st nonzero; replacing the pure images by -s+a st and -t+b st still gives st. The same holds with the factors permuted. Therefore a higher-order correction cannot repair a proposed negative mixed coefficient identification once the pure restrictions and product marking are fixed.

For the asserted line-bimodule version, a local right generator identifies the left algebra with the endomorphism algebra of a free rank-one right module. Use the induced map from the left algebra to the right algebra; if the chosen graph convention yields φ⁻¹ instead of φ, invert the local algebra identification. The induced classical map is then φ by the graph-action hypothesis. The same local commutator argument applies; changing generators only conjugates the map and leaves its induced pure commutator test unchanged. No general derived or arbitrary Morita equivalence is included.

## 4. Effect on the open goal

The earlier identity-reduction barrier left nontrivial geometric base changes and factor exchange unclassified. This proves that neither supplies an extra negative scalar on the mixed coefficient line, even when pure coefficient maps were initially allowed arbitrary units. In this class, a proposed vanishing argument must instead establish a genuinely negative action on the relevant obstruction class through the base/module/band action. A coefficient-sign assertion alone is insufficient.

The next consequence is a clean separation of necessary data: for a proposed φ-return, the coefficient action is fixed canonically; remaining work is the existence of the full return, return of the prescribed pure boundary, and its actual induced action on retained cohomology. This proof does not evaluate that action or any of the thirty retained pairings. It does not exclude anti-Poisson behavior relative to a different scalar-valued Poisson marking, partial opposites, nongeometric equivalences, or unmarked changes of coefficient products.

Sources and dependencies: corrected pure product and external-product identification at https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6270678828 ; self-duality/sign issue at https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6272324961 ; intrinsic square-zero and local line-bimodule lemma in /research/hm/middle-surface/mixed-serre-duality-update/PROOF.md.
