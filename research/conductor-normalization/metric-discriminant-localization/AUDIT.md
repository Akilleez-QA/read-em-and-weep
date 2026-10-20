# Preserved mathematical audit

This review concerns the source manuscript and its stated assumptions. It is preserved as mathematical history, not a new independent certification of all publication edits or of unpublished input theorems. Source and publication hashes are recorded in SOURCE-HASHES.json. A split manuscript’s module or polar application remains conditional in its destination unit.

# Independent audit: limiting metric discriminant localization

## Verdict

Accepted. The proof establishes the stated localization and multiplicity bound under its explicitly imported support-finiteness and good-general-surface hypotheses. No further constant-rank hypothesis on the actual residual kernel is used. The argument is universal bundle algebra and algebraic geometry; no operation instance or computational experiment was inspected or evaluated.

Reviewed sources: the accompanying `PROOF.md`, the conditional integration in `prerequisite double-plane-boundary-support, document PROOF.md (see the unit INPUTS.md)`, and the canonical-complement, ternary-metric-boundary, and full-flag-resolution proofs cited there.

## 1. Metric graph and bundle orientation

With the stated quotient convention, the relative projective bundle parametrizes surjections Sym²E→M up to line isomorphism. Its tautological map remains surjective on the graph and every subsequent pullback. Thus K_h is genuinely a rank-five subbundle even where h has rank one, and it must not be identified with the entire actual residual kernel there.

The determinant line is D=(det E*)²⊗M³. The adjugate has type Sym²E⊗(det E*)²⊗M², so h(W(adj(h)),−) has type E*⊗U⊗D. This agrees with the determinant-times-trace term. All determinant and adjugate factors in the displayed covector are correct.

## 2. Regular correction across residual-rank jumps

The repeated-input injection A:T⊗U²→J has constant rank four at every point by the imported hypothesis. A unit minor provides a local left inverse, so the asserted regular correction does not rely on a nonexistent kernel bundle across a rank jump. Applied to B_s:Sym²E⊗U→J, its inverse has target T⊗U²; cancelling the input U gives v_s:K_h→T⊗U, with the negative tautological U twist, not U*.

The maps expressing Q(K_h)=0 and v_s(K_h)⊂E⊗U are regular and vanish on the dense good locus. Their extension over the integral metric model is valid. The resulting restriction is canonical because A is injective. Consequently square avoidance on the actual kernel applies to each isotropic square of the limiting metric.

## 3. Determinant-cleared annihilator and gluing

The normalized canonical complement is the graph of −(3/10)τ_h(v_s). Its annihilator with middle coefficient one therefore has E-coefficient +(3/10)τ_h(v_s). The signs and constants in β are correct.

Changing the extension W by h⊗w adds δ h(w,−) to δ tr(W) and 3δ h(w,−) to the adjugate term; the displayed combination is unchanged. Under a splitting change s′=s+d, the contraction changes by (10/3)d. Thus the E-coefficient of β changes by δd while the U-coordinate projection changes by −d∘p. These cancel. This directly verifies the gluing also justified in the proof by agreement on a dense open. Frame and metric-scale changes are already accounted for by the intrinsic determinant line.

No inversion remains in the polynomial formula, so it is regular at all metric ranks allowed by the nowhere-zero form.

## 4. Base ideal, actual graph, and exceptional multiplicities

The coefficient ideal is intrinsically im(H⊗(U⊗D)⁻¹→O). Since β|U=δ, it contains the determinant ideal. Principalizing the entire ideal as O(−F) makes division a surjection H→U⊗D⊗O(−F). The minus sign is essential and is correct. Its kernel is a subbundle, agrees with the canonical complement generically, and its proper image is the actual reduced canonical flag graph. The local Rees-algebra graph description excludes extraneous incidence components.

The quotient is H/C=U(Δ−F), and the middle-line map is the actual section δ divided by the coefficient common factor. Therefore A=Δ−F is an equality of Cartier divisors with full orders of vanishing. Because V/H is locally free, including H/C into V/C introduces no additional zero ideal. There is no residual isolated zero on this model.

F need not be exceptional, and the proof correctly says so. For every divisorial valuation, including exceptional valuations on further resolutions, d=ord δ and b=min ord β_i satisfy 0≤b≤d and ord A=d−b. Thus the bound does not omit exceptional multiplicities or replace them by reduced supports.

## 5. Rank-two equality and nondegenerate boundary

When the residue metric has rank two, its adjugate is a nonzero radical square. Square avoidance puts its correction outside the radical, hence the contracted adjugate term has a nonzero coefficient in the residue field. The determinant term vanishes there. Therefore β has a unit coefficient, b=0, and ord A=ord Δ for any determinant multiplicity. The reasoning also works after extending the residue field and does not require a reduced or transverse discriminant.

If the metric is nondegenerate, β|U is already a unit, so the complement extends transversely and A vanishes, even at a residual-rank drop. At rank one, cancellation is allowed; the proof appropriately retains only d−b rather than asserting discriminant equality.

## 6. Codimension-one descent and positivity

At a prime divisor of the normal surface X, properness and separatedness give a unique extension of the rational projective metric over its DVR. A primitive local matrix differs under trivializations only by units and invertible changes of basis, so its determinant order is intrinsic. The graph is an isomorphism near each such generic point. Thus the pushed determinant cycle is exactly the stated effective Weil divisor Δ_X, independent of resolution. No Cartier assertion about Δ_X is required.

The same DVR argument, or a common resolution of the actual flag graphs, proves independence of A_X. Divisors exceptional over closed points push forward to zero; the remaining generic orders are preserved. Consequently Δ_X−A_X=f_*F is effective as a cycle.

The support and middle line bundles descend to X by the imported finite-support result, and their pullbacks are precisely the classes used by the full-flag Chern identity. Projection formula therefore gives A_X·c1(U*⊗N)≥degree(B). Intersecting the effective difference with this nef Cartier class proves the stated discriminant inequality. In fact U* is ample on X, so its sum with N has positive degree on every nonzero effective curve.

## Scope

This is a genuine new localization: Δ_X is constructed from the rational metric before defining the complement defect, and A_X≤Δ_X is substantive. It forces a nonzero curve of degenerate limiting metrics in the positive middle boundary. It neither says that every bad curve contributes to A_X nor excludes cancellation at higher corank. The imported support-finiteness/application premises remain prerequisites. No existence result, classification, or universal dimension-six bound follows.
