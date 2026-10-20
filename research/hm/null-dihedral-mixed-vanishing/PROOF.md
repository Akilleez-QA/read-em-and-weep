# Retained obstruction: a genuine dihedral route

Formal proof independently audited, 19 October 2026. The cohomology dimensions below are admitted pinned inputs, not recomputed. Both retained components vanish under the stated premises.

## Result and hypotheses

In the actual unscaled binary-coefficient coordinates of the pinned HM carrier, the binary-form action contains a genuine order-ten dihedral subgroup preserving the HM monad. For its canonical linearizations,

\[
H^2(\operatorname{End}_0 H(-4))^{D_5}=0,
\qquad H^2(\operatorname{End}_0 H(-3))^{D_5}=0.
\]

These are statements about the actual coefficient actions, not characters inferred from the base or dimensions. The first follows from equivariant Euler characteristic plus the Heisenberg representation on the five-dimensional H1; the second follows directly from equivariant Euler characteristic and concentration.

The corrected pair presentation is natural for the diagonal binary-form action when its canonical-form coefficient and equivariant O(1) frames are retained. Pure-boundary uniqueness then makes the canonical mixed obstruction invariant. The canonical coefficient lines W and W² are trivial for this action. Consequently both canonical retained projections vanish. Together with the already established constant-component vanishing, this gives zero compact mixed obstruction, and hence existence of regular Čech primitives. It does not give evaluated physical coefficients, an explicit primitive formula, or a frozen-jet identification.

Separate independent audits accepted the character calculation and ambient equivariance; see [CHARACTER-AUDIT.md](CHARACTER-AUDIT.md) and [AMBIENT-AUDIT.md](AMBIENT-AUDIT.md). The conclusion is that all thirty retained classes vanish for the canonical corrected mixed model, under the geometric-source, algebraic-sheaf, cohomology-rank and pure-boundary premises. It proves original mixed-quotient lifting, not pure-square vanishing for the full total-degree-two ambient or an all-order deformation theorem. Only the explicit D5 subgroup is needed, not the optional full-normalizer intersection result in Section 1.

The trust boundary is explicit: the dimensions and cohomological concentration at twists -1 and -2 are imported from the exact small-complex certificates pinned below. Their ordinary bundle interpretation retains the same HM-monad/local-freeness premises as the discussion. Neither those ranks nor the actual mixed-source values are newly computed here. The new input is an analytic equivariant-character proof using those tables and the displayed genuine monad action.

## 1. Coordinates and actual subgroup

Use the carrier's basis e_0,...,e_4 and projective coordinates v_i=e_i(x_1,...,x_4). These are ordinary coefficients of the product of four binary linear forms, not binomially rescaled coefficients. The HM monad uses

\[
w_a^+=e_{a+2}\wedge e_{a+3},\quad
w_a^-=e_{a+1}\wedge e_{a+4}
\]

with indices modulo five. Let ζ be a primitive fifth root, and define

\[
T e_i=\zeta^{i-2}e_i,\qquad R e_i=e_{4-i}.
\]

Both have determinant one, T^5=R²=1, and RTR=T^{-1}. They are induced on quartics by the binary SL2 matrices diag(ζ²,ζ^{-2}) and [[0,i],[i,0]], respectively. The latter squares to minus the identity in SL2, which acts trivially on binary quadratics and quartics. Thus this is a genuine D5 action on both projective spaces and on their O(1) bundles, not merely a projective action requiring an unresolved cocycle.

The HM Heisenberg group has cyclic shift and diagonal clock generators. T is a central multiple of its clock; R is a cyclic shift composed with the index-negation normalizer. Hence these are known HM symmetries. More directly, the monad check below supplies the action without needing a full automorphism-group theorem.

There is also an exact bounded intersection statement. Let N be the known projective Heisenberg normalizer, P its normal projective Heisenberg subgroup (Z/5)^2, and K=N intersect the binary PGL2 image. Then P intersect K is C5: it contains T; any exponent-five abelian subgroup of PGL2 containing T lies in its torus centralizer and has order at most five. Thus C5 is normal in K, forcing K into the torus normalizer in PGL2. On quartic coefficients a torus element is projectively diag(1,t,t²,t³,t⁴). Conjugating the cyclic shift gives four equal adjacent ratios and one wrap-around ratio; membership in the projective Heisenberg group forces t⁵=1. The reflection R is present, so K=D5. This is an intersection with the known normalizer only; no unproved assertion that this is the full HM stabilizer is needed.

## 2. Equivariant K-class, including the reflection sign

Write Q=V/O(-1), with V the five-dimensional coordinate representation. The normalized monad is

\[
U O(-1)\longrightarrow 2\Lambda^2Q\otimes O(-1)
\longrightarrow U^*O,
\]

where U has dimension five. Under R, BOTH wedge formulas satisfy

\[
R w_a^\pm=-w_{4-a}^\pm.
\]

Therefore U_R=-R, while the two-dimensional multiplicity factor in the middle term is trivial. The alternating pairing on the middle term takes values in O(-1), with no extra determinant character because det(V)=1. It gives exactly the displayed U* action on the final term. This sign must not be replaced by the permutation action on U.

The tautological sequence gives

\[
[H]=2O(-3)-2V O(-2)+(2\Lambda^2V-U)O(-1)-U^*O.
\]

At R, tr(V)=1, tr(Λ²V)=(1²-5)/2=-2, tr(U)=tr(U*)=-1. The coefficient traces at twists (-3,-2,-1,0) are consequently

\[
(c_{-3},c_{-2},c_{-1},c_0)=(2,-2,-3,1).
\]

For End(H), the autocorrelation coefficients at differences 0,±1,±2,±3 are

\[
a_0=18,\quad a_1=-1,\quad a_2=-8,\quad a_3=2.
\]

These come from the alternating K-class, so negative coefficients are intended. R has eigenvalues (+1,+1,+1,-1,-1) on V; hence χ_R O(0)=1, χ_R O(1)=1, χ_R O(2)=3. Also χ_R O(-5)=1 by equivariant Serre duality, and O(-1),...,O(-4) are acyclic. Therefore

\[
\chi_R\operatorname{End}(H)(-2)=2-8+2=-4,
\]
\[
\chi_R\operatorname{End}(H)(-1)=-1-8+6=-3.
\]

At any nonidentity T^k, tr(V)=tr(U)=tr(U*)=tr(Λ²V)=0. The K-class coefficient traces reduce to (2,0,0,0), so the End K-class trace is 4O(0); after twist -1 or -2 its Euler trace is zero. All five reflections are conjugate in D5.

Scalar O(-1) and O(-2) are acyclic, so these calculations apply unchanged to End0.

## 3. The twenty-dimensional summand

The admitted cohomology table says End0(H)(-2) has only H2, of dimension twenty. Its character is therefore

\[
(20,0,-4)
\]

on identity, nontrivial rotations, reflections. Averaging gives

\[
\dim H^2(\operatorname{End}_0H(-2))^{D_5}
=\frac{20+4\cdot0+5(-4)}{10}=0.
\]

Since det(V)=1, ω_P4=O(-5) equivariantly. End0(H) is equivariantly self-dual under matrix trace. Thus its degree-two twist -3 representation is dual to twist -2, and also has no invariants.

## 4. The ten-dimensional summand: no guessed representation

The admitted cohomology table for End0(H)(-1) has H1 of dimension five and H2 of dimension ten, with no other cohomology. Therefore its invariant Euler characteristic is

\[
\chi^{D_5}=\frac{(10-5)+4\cdot0+5(-3)}{10}=-1.
\]

To separate H1 and H2, use the actual Heisenberg action. Its central scalar acts trivially by conjugation on End(H), and nontrivially on O(-1). Thus this five-dimensional H1 has a nontrivial Heisenberg central character. Every irreducible representation with this central character has dimension five; consequently H1 is one such irreducible representation. Restriction to the clock C5 has every character exactly once. In particular dim(H1^D5)≤dim(H1^C5)=1.

Exactness of finite-group invariants in characteristic zero now gives

\[
\dim H2^{D_5}-\dim H1^{D_5}=-1.
\]

Nonnegativity and the upper bound force dim H1^D5=1 and dim H2^D5=0. This proves the ten-dimensional assertion without identifying H2 with a guessed exterior-power representation. Equivariant Serre duality transfers it to twist -4.

## 5. Ambient action, coefficient lines, and canonical class

On P2 the corrected square-zero presentation is

\[
(f,\eta)\star(g,\theta)=(fg,f\theta+g\eta+df\wedge dg/2),
\]
\[
F_{ij}(f,\eta)=(f,\eta+df\wedge\beta_{ij}/2),
\quad A_{ijk}=(1,-2(\beta^2)_{ijk}),
\]

where β=dlog(t_ij) for O(1), with the stated total cup/wedge convention. Take a D5-stable affine cover indexed by translates, and choose each translated O(1) frame by transport under the genuine linearization. Pullback respects multiplication, exterior differentiation, wedge, the ordered nerve, and dlog of the transported transition functions. Hence all three displayed pieces, not just the product symbol, transform compatibly and satisfy group composition exactly. If the original cover uses other frames, the usual frame-change equivalence transports this action; a literal invariant original coordinate formula is not required.

On quadratics the binary reflection lift is minus coefficient reversal, not bare reversal. Its determinant is +1. Thus the canonical ω_P2 coefficient is precisely O(-3) with the induced SL2 linearization. There is no hidden reflection sign arising from replacing ω by an unrelated linearization. Tensor the two identical pair actions diagonally: the full external-product mixed product, unary maps, and triple units are preserved, with all mixed terms. The two factors are NOT exchanged in this D5 argument.

The canonical mixed class is independent of the pure representatives by the established H1 vanishings and gauge-boundary formula. Transport of the pure boundary therefore yields an isomorphic boundary and the same obstruction class. This gives genuine D5 invariance in H2(End0 E tensor ω_X).

The canonical W generator is σ=vV-2(uW+wU), the discriminant polarization of two binary quadratics. This polynomial is SL2-invariant. The quartic invariant I=c²-3bd+12ae is also invariant; hence τ=σ²-2I is invariant. The lines W and W² in the canonical splitting are therefore trivial under D5. Finite-duality projections are natural, and ω_P4=O(-5) has already been checked equivariantly. Both C10 and C20 are thus invariant in exactly the zero-invariant target representations above.

It follows that their cohomology classes vanish. On an affine Čech cover, choose regular p1,p2 with δp1=c_A(σ), δp2=c_A(τ); the earlier constant vanishing supplies p0. The already proved regular dual-basis reconstruction then gives a primitive. Any original-source comparison boundaries still have to be retained, with final transition correction x=-h-H_model. Vanishing does not justify dropping those representative corrections.

## Sources and relation to previous exclusions

- Pinned coordinate basis and monad: https://github.com/Akilleez-QA/read-em-and-weep/blob/3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f/research/hm-carrier-and-atlas.md
- Admitted small cohomology table: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6130699166 ; underlying certificate https://github.com/Akilleez-QA/read-em-and-weep/blob/f968b53943ba2312f09fbc3e8f9d462e86bcaa34/research/hm/d8-small-certificates/p4/Perfect-Complex-D8-F3.md
- Primary Heisenberg representation and HM construction, Sections 1–2: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf . Only its finite Heisenberg representation theorem and known normalizer action are imported; the dihedral character calculation above is derived explicitly.
- Full corrected ambient: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6270678828
- Complete mixed equation and pure-gauge independence: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6271101716
- Constant-component vanishing: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6274541018
- Canonical two-component splitting: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6277692474
- Regular primitive reconstruction and source corrections: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6279132359
- Earlier self-duality exclusion: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6272324961 . This argument does not reuse the invalid C=-C shortcut, exchange the two factors, assume arbitrary SL2 equivariance of HM, or infer cohomology characters from the base alone.
- Earlier weighted-primitive failure: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6276688181 . The present route proves classes zero by an additional actual finite symmetry; it does not claim that weighting the old primitive works.
