# Publication scope

This is a preserved theorem manuscript, with the exact hypotheses and held identifications listed in unit 10 INPUTS.md. Abstract geometry and formal conditional implications are distinct from identification with the actual HM module or retained source. Historical words such as “new,” “remaining,” or “previously verified” describe the source manuscript, not a claim about the current research frontier.

# The positive middle boundary is supported on the limiting metric discriminant

Work over C. This is universal algebraic geometry and bundle algebra only. No source operation instance, rank experiment, or computational evaluation is used.

## 1. Statement and imported hypotheses

Let B be the integral projective good-general middle surface of `prerequisite rank-five-middle-families, document PROOF.md (see the unit INPUTS.md)`, with its global repeated-input injectivity hypothesis, and put X=B^ν. Import the support-finiteness conclusion and its descent argument in the conditional integration of `prerequisite double-plane-boundary-support, document PROOF.md (see the unit INPUTS.md)`. Thus the support hyperplane map extends to X, giving subbundles

    U ⊂ H ⊂ V⊗O_X,    rank(U,H,V)=(1,4,5),
    E=H/U,    N=(V⊗O_X)/H.

Write a=c1(U*), n=c1(N), and L_X=U*⊗N. Both a and n are nef; a is ample, since X→B is finite. The letter a avoids confusing the middle hyperplane class with the metric h.

On the dense good open, the five-dimensional residual kernel is a hyperplane in Sym²E, hence determines a rational projective metric. Its limiting discriminant defines an effective Weil divisor Δ_X on X, intrinsically described below. There is also the actual middle-boundary Weil divisor A_X, obtained by pushing down the middle-section zero divisor on any smooth full-flag model. We prove

    0 ≤ A_X ≤ Δ_X,
    Δ_X·c1(L_X) ≥ A_X·c1(L_X) ≥ degree(B)>0.       (1)

Consequently a nonzero effective curve in the actual positive middle boundary has degenerate limiting ternary metric at its generic point. A residual-rank drop with nondegenerate limiting metric contributes zero to A_X. Residual rank is allowed to drop arbitrarily; no constant-rank hypothesis on the residual kernel is imposed.

On a simultaneous resolved metric and complement model, the stronger identity is

    A=Δ−F,    0≤F≤Δ,                              (2)

where F is the divisor of the entire coefficient base ideal of an explicitly constructed regular covector. At a codimension-one point where the limiting metric has rank two, F has coefficient zero, so A and Δ have identical coefficients, including arbitrary determinant multiplicity.

These conclusions concern the effective boundary selected by the middle section. They do not assert that every bad curve contributes positively, or that every metric-degenerate curve contributes to A_X. They do not establish existence or nonexistence of the original family.

## 2. Projective metric, its graph, and codimension-one meaning

Use the quotient convention

    P_X(Sym²E)=Proj_X Sym(Sym²E).

Its points parameterize one-dimensional quotients of Sym²E, equivalently lines of quadratic forms in Sym²E*. Its tautological quotient is Sym²E→O(1). The good-locus hyperplane kernel therefore defines a rational section of this projective bundle over X.

Let G_h be its reduced graph closure, and take a projective smooth resolution Z→G_h. Pull all bundles to Z. Put M=O(1)|Z. The tautological form

    h:Sym²E→M

is everywhere surjective. In particular it is nowhere zero as a quadratic form, though its associated symmetric map E→E*⊗M may have rank one or two. Define

    D=(det E*)²⊗M³,    δ=det(h)∈H⁰(Z,D).

The generic metric is nondegenerate, so δ is not identically zero. Its zero divisor Δ is effective Cartier and D is canonically O_Z(Δ) by its section δ.

For every prime divisor P⊂X, the normal local ring O_{X,η_P} is a DVR. Properness of the relative projective bundle extends the generic metric section uniquely over this DVR. The extension spreads to an open neighborhood of η_P. Thus the rational metric is regular away from a finite subset of X. At η_P it is represented, after local trivialization, by a symmetric matrix with coefficients in the DVR and at least one unit coefficient. Changing such a primitive representative multiplies it by a unit. The order

    d_P=ord_P det(h)≥0

is therefore intrinsic. Define Δ_X=Σ_P d_P P. This is a finite effective Weil divisor. Its coefficients do not require choosing a global line bundle M on X. On every resolved metric model, pushforward of Δ is Δ_X. Exceptional determinant components are simply contracted by that pushforward.

## 3. The correction is regular on the five-plane bundle even when residual rank drops

Here is the regularity argument needed to avoid a hidden constant-rank assumption. Put T=(V⊗O)/U. The repeated-input maps assemble into a bundle monomorphism

    A:T⊗U²→J⊗O.

It has rank four everywhere by the global repeated-input hypothesis. Consequently its image is a subbundle, its quotient is locally free, and A admits local left inverses onto its source. This assertion remains true after arbitrary pullback to the metric model.

A local splitting of H→E gives the middle-linear numerator map

    B_s:Sym²E⊗U→J⊗O.

Modulo im(A), this is the restriction of the residual map Q. The subbundle K_h=ker(h) has rank five everywhere because h is surjective. On the dense good locus Q annihilates K_h. The resulting regular bundle map from K_h⊗U to (J⊗O)/im(A) vanishes on a dense open of the integral model, hence vanishes identically. Thus K_h lies inside the actual residual kernel at every point, even when that actual kernel is larger.

Applying a local left inverse of A to B_s|K_h gives a regular correction

    v_s:K_h→T⊗U.

The factorization through A makes this correction unique, so choices of left inverse do not matter. The composite to (T/E)⊗U vanishes on the dense good locus by the supported-correction theorem, and hence vanishes identically. Therefore

    v_s:K_h→E⊗U

is regular everywhere. Changing the splitting by d:E→U changes v_s by q↦2q(d), with the convention in the cited canonical-complement proof.

The repeated-input square-avoidance lemma applies to K_h at every geometric point: for a nonzero r with h(r,r)=0, one has v_s(r²)∉Cr⊗U. Indeed K_h is contained in the actual kernel just proved. None of these steps asserts that the actual kernel is itself locally free.

## 4. A regular global covector with determinant as its middle coefficient

Locally split H=U⊕E. Let α:H→U be the resulting projection and let p:H→E be the quotient. Since h is a surjection onto a line bundle, extend v_s locally to

    W:Sym²E→E⊗U.

On the nondegenerate locus the intrinsic contraction is

    τ_h(v_s)=tr(W)−(1/3)h(W(h^{-1}),−),

and the canonical complement is the graph of −(3/10)τ_h(v_s). Thus its annihilator, normalized to be the identity on U, is α+(3/10)τ_h(v_s)∘p.

Multiplying by δ gives a regular map β:H→U⊗D. In the chosen splitting its coefficients are

    β|U=δ·id_U,
    β|E=(3/10)δ tr(W)−(1/10)h(W(adj(h)),−).          (3)

The adjugate is intrinsically a section of Sym²E⊗(det E*)²⊗M². Hence the second term has exactly the value bundle E*⊗U⊗D, as required. Formula (3) is polynomial in h and W; it is regular at every metric degeneration.

Changing W by h⊗w changes δ tr(W) by δ h(w,−), and changes h(W(adj(h)),−) by 3δ h(w,−), so (3) is unchanged. Changes of splitting, frames, or metric representative also glue: on the dense nondegenerate open the formula is the intrinsic normalized annihilator multiplied by the intrinsic section δ, and two regular bundle maps agreeing there agree everywhere on the integral model. Therefore β is a globally defined regular covector with

    β∘(U→H)=δ·id_U.                                 (4)

The undivided coefficients (3) need not be primitive at higher-corank points. Their possible common factors are precisely the base ideal treated next.

## 5. Principalization gives the actual complement graph and exact divisor subtraction

Let T_β=U⊗D. Define the coefficient ideal intrinsically by

    I_β=im(H⊗T_β^{-1}→O_Z).

It is a coherent nonzero ideal. Equation (4) gives an inclusion of ideals

    O_Z(−Δ)⊂I_β.                                    (5)

Blow up I_β, then take a smooth projective resolution Y of that blowup. Write p:Y→Z and

    I_β O_Y=O_Y(−F)

with F effective Cartier. Divide the pulled-back covector by its entire coefficient ideal. The result is an everywhere-surjective bundle map

    β_prim:p*H→p*T_β⊗O_Y(−F).

Its kernel C is a rank-three subbundle of H. On the good open it is exactly the canonical complement. Thus its Grassmannian map factors through the reduced canonical complement graph. Together with the already extended H, this gives a morphism to the full-flag graph. Conversely, the blowup is the graph of the rational line of the coefficients of β: locally its Rees algebra is the graph closure of [β_1:…:β_4]. Hence this construction resolves the canonical flag, rather than an unrelated incidence component. A further common resolution can be used with any previously chosen full-flag model.

The quotient line is

    H/C≅U⊗D⊗O_Y(−F)≅U(Δ−F),                       (6)

where bundles and Δ have now been pulled to Y. The map U→H/C corresponds to δ divided by the local equation of F. By (5) that quotient is regular. Its exact zero divisor is

    A=Δ−F≥0.                                        (7)

This is the actual middle-section divisor: the inclusion H/C→V/C is a line subbundle, with locally free quotient N=V/H, so passage to V/C leaves its zero ideal unchanged. In particular (7) concerns full scheme multiplicities, not just supports; no residual isolated zero ideal remains on Y.

The base divisor F may include divisors already present on Z as well as exceptional divisors. Calling it merely exceptional would be incorrect. Formula (7) says exactly what cancellation occurs at higher-corank metric degenerations.

## 6. Codimension-one coefficients and corank-one equality

At any divisorial valuation on a smooth metric model, trivialize all bundles over its DVR and put

    d=ord(δ),    b=min_i ord(β_i).

Equation (4) implies 0≤b≤d. The primitive covector has middle coefficient of order

    ord(A)=d−b.                                      (8)

If the limiting metric is nondegenerate, d=0, hence b=0 and ord(A)=0, irrespective of the residual rank. In fact the canonical complement extends transversely throughout the entire open where δ is a unit.

Suppose instead that the reduced metric has rank two. Its adjugate is a nonzero scalar multiple of r² for a generator r of its radical. That square is in K_h. Square avoidance gives v_s(r²) outside the radical, so

    h(v_s(adj(h)),−)≠0

in the residue field (or after a geometric residue-field extension). Reducing (3) modulo the maximal ideal therefore gives a nonzero E-coefficient of β. Thus b=0, and ord(A)=d. This applies to every determinant order d≥1, including nonreduced discriminants and arbitrary ramification. No diagonal normal form or generic-transversality assumption is needed.

At rank-one limiting metrics the common factor b can be positive; (8), rather than an asserted equality A=Δ, is the general statement.

## 7. Descent, intersection, and the new boundary localization

Let f:Y→X be the composite. The good-locus complement and support determine the same rational flag on every model. On a common resolution the middle-section Cartier divisor is the pullback of the corresponding divisor from either smooth full-flag model. Consequently its pushed divisor cycle

    A_X=f_*A

is independent of that model. Equivalently, it is determined by the unique extended flag over each codimension-one DVR of the normal surface X and the vanishing order of its middle-line map there. Normalization separates branches; each prime divisor receives its own DVR order. No reduced-support convention is used.

Pushing forward (7) gives

    Δ_X−A_X=f_*F≥0.                                  (9)

Here f_*Δ is precisely the primitive-metric divisor of Section 2. The support and middle hyperplane classes are both pulled back from X. The full-flag identity and positivity theorem therefore give

    A_X·c1(L_X)=A·f*c1(L_X)
               =∫_Y c2((V/C)⊗U*)
               ≥degree(B)>0.                         (10)

Weil-divisor intersection with the Cartier class c1(L_X) is well defined on the normal projective surface. Because L_X is nef, intersecting (9) with it preserves the inequality and proves (1). Equivalently, every effective curve has nonnegative intersection with L_X; indeed a is ample here, so every nonzero effective curve has strictly positive intersection.

Thus A_X is a nonzero curve cycle, and every prime curve in its support has d_P>0. In particular the previously forced positive boundary cannot be explained solely by residual-rank degeneration with nondegenerate limiting ternary form. It necessarily includes a curve of degenerate limiting metrics, even if the actual residual rank drops along that same curve. At every rank-two generic metric degeneration, its boundary multiplicity equals its determinant multiplicity.

The essential new construction is the global determinant-cleared annihilator and its coefficient-ideal principalization. The discriminant is defined independently from the rational metric before the complement divisor is considered; thus A≤Δ is a genuine localization and multiplicity bound, not a renaming of A.
