# Independent audit: transfer of the alternating zero

## Preliminary verdict

The proposed weight filtration argument is valid for the specified external-product ambient, provided the comparison uses actual equivariant ambient/module transport and first removes exact high-weight boundary differences by ordinary pure gauges. It is not a consequence of the Ext¹ dimensions at cochain level without that gauge step. The source primitive is already a complementary mixed-source theorem, so no diagonal-polarization uniqueness assumption is necessary.

This audit is static/formal only.  The initial review preceded the companion result; the final cross-check below resolves that historical pending status.

## 1. Exact source normalization and polarization

The pinned raw-closure proof uses parameters with s²=t²=0 and explicitly prescribes the mixed product coefficient D_P D_Q/4 and actual triple unit (1+s b_P)(1+t b_Q). Its normalized obstruction is M=g_ik^(-1)D, and its section 3 proves

    R_raw = tf(M) + δ_row W.

There is no extra scalar multiple between these cohomology classes. Scalar trace removal is valid for the full-sign class because its scalar H² vanishes. The corrected alternating primitive proof states directly

    Alt(E_12(s_raw,34)+E_34(s_raw,12))

and combines this with the Q4, Q2, and Omega terms of that same mixed remainder. Its Alt is 1/24 times signed geometric permutation; four-form evaluation carries no additional factorial. Its primitive coefficient is -1/72. Therefore the needed zero belongs to the matching polarized mixed source, not merely a one-parameter diagonal source. It would be incorrect to substitute s=t=h after imposing s²=t²=0.

The common-ambient-frame correction must remain part of the imported theorem: the induced connection difference is -dG G^(-1)=-L^t, with G the genuine determinant-normalized physical cohomology transition. The earlier array-only comparison is not a valid replacement.

## 2. Boundary differences and the weight bound

Write the deck character of a subset S as χ_S; multiplication of characters is symmetric difference. The pair directions have P={1,2}, Q={3,4}. The imported Ext¹ table is per character, (79,2,0,0,0), so H¹(End(F)) has support only in subset sizes 0 and 1.

Choose a homogeneous reference pure boundary in the original fixed ambient: its P coefficient has character χ_P, its Q coefficient χ_Q. The ambient first-order operations and gerbe terms have these same characters. For any other pure boundary, the normalized differences are ordinary closed End(F)-valued one-cochains. Project them by finite deck idempotents. Every component of weight at least two is exact by the imported H¹ vanishing, and can be removed by a reduction-identity pure frame gauge. This is an existence argument for ordinary cochains, not a finite-cutoff construction.

Such gauges must be interpreted through the full mixed order. They can create a mixed transition coefficient Q_ij. Naturality, or null-mixed-module-equation equations (9)–(10), shows that setting this new mixed coefficient back to zero changes the normalized mixed source by an ordinary Čech boundary. Thus the obstruction class may indeed be compared after the low-weight normalization.

Every term of the finite mixed-source variation is either a reference/ambient pair-character term times one low-weight change, or a product of two low-weight changes. The former has subset size at most 2+1=3; the latter at most 1+1=2. Derivative operations are included as pair-character operations, not assumed weight-preserving individually. No term has full deck character {1,2,3,4}. Consequently the full-weight cohomology projection is unchanged. Applying geometric S4 alternation afterward preserves this equality because the full-deck character is permutation-stable.

The argument does not prove equality of whole obstruction classes outside full deck weight, or equality of arbitrary frozen pure representatives.

## 3. Ramification and actual ambient comparison

The root-HKR proof supplies equivariant cochain gauges and an invariant downstairs normal form, not an isomorphism of naive pulled-back downstairs coefficient lines with upstairs trivial coefficient lines at the branch divisor. Its coefficient map is

    ρ(η)=s f,  f Ω=p*η.

This map has the ramification Jacobian upstairs. It becomes the specified isomorphism only after invariant finite pushdown. To obtain an upstairs module from a corrected module, use extension of scalars along the actual local algebra maps into the normalized upstairs presentation, then inverse gauges and inverse root Morita transport. Locally free modules stay free under extension of scalars. The factor external product retains all st terms in products, overlaps, and units.

Normalized Morita defects agree literally after the canonical cancellation End(N⊗f*HM)=End(f*HM), as root Morita report section 4 proves. The correction gauges induce identity on reduction and the coefficient ideal. These facts justify obstruction transport; matching ordinary HKR characteristic images alone would not.

Homogeneity of the comparison boundary must be justified in an equivariant presentation (or after a coherent finite-group strictification/averaging), not inferred merely from an underlying root-line square. The full action-groupoid construction of root-HKR and its genuine parameter characters are the relevant input.

## 4. Projector and finite trace normalization

For Y=(P¹)^4, the full elliptic-deck-sign line M has ordinary product linearization, while ω_Y=M⊗sign(S4). Thus full S4 alternation in M is invariance in ω_Y. After the two inner swaps, the canonical line is ω_(P²×P²); swapping surface factors has sign +1.

With m:P²×P²→P⁴ of degree six and F=m_*O, the constants projector is unit·Tr/6. Under finite duality the corresponding projector on λ∈Hom(F,ω_P⁴) is

    λ ↦ (f ↦ λ(1)Tr(f)/6).

This is exactly the full alternating two-dimensional projector, not an arbitrary rank-two summand. The pair deck normalization 1/8 and the multiplication-map normalization 1/6 perform different descents and must not be confused. A zero class is unaffected by an overall nonzero normalization, but a literal projector identification still requires the displayed factor 1/6.

## 5. Bound on the conclusion

Subject to the imported physical geometric premises and the genuine ambient/boundary transport above, the argument transfers the known fully alternating zero to the canonical corrected mixed obstruction. It neither annihilates the remaining thirty-dimensional even trace-zero summand nor evaluates any retained detector. The block-odd thirty-dimensional space is a separate sector. No executable primitive, physical value, or execution admission follows.

## Final companion-result review

Read RESULT.md in full after completion. The report discharges the preliminary qualifications and passes this audit at its explicitly imported algebraic-source scope.

The stronger equivariant-boundary route is also justified by the inspected source text. closure-and-characters.md section 2 explicitly asserts the actual pure corrections have their respective pair characters after common-frame transport, explaining the scalar root-frame signs, even split-column powers, invariant old connection, and pair contraction. Its displayed mixed formula has coefficient 1/4 and exactly the ten terms used by PR79. null-pair-swap-coherence explicitly gives v_d1=v_d2=1, so restricting the ordered ambient to the deck subgroup introduces no hidden overlap gauge for that action.

The induced corrected boundary has genuine deck-equivariance through the full groupoid maps. Equivariant pure-lift differences are controlled by H¹(End(F)) in the relevant pair character; finite-group positive cohomology vanishes. Each of these groups is zero. Thus an equivariant reduction-preserving comparison exists, even without H⁰ vanishing. Combining the two pure comparisons gives a boundary comparison, and ordinary mixed defect covariance identifies their obstruction classes. This avoids needing a literal frozen-jet match. The report correctly keeps the weaker low-weight argument as an independent alternative.

In particular RESULT.md does not assert the dangerous ramified upstairs coefficient-line isomorphism: it uses invariant-algebra inclusion and free-module scalar extension, then identifies the coefficient map only on finite invariant pushdown. It also does not require an S4-equivariant isomorphism of the paired deformed ambients. Equality of the transported classes in the canonical underlying End cohomology is enough to apply that cohomology's geometric S4 projector.

The conclusion pr_const(C)=0 is therefore supported. The canonical C is block-even by the separate prior theorem, so it belongs to the canonical thirty-dimensional retained summand. No retained pairing, mixed-module existence, or numerical physical value follows.
