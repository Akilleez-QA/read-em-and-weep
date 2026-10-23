# Independent adversarial verification: polar-integrability P-row theorem

Reviewed 2026-10-23 against final bytes:

- PROOF.md SHA256 `073cdcb7d43ac9f572dac85306f935a654cfb88cbe6e99eddb1a7f6c968648d9`
- verify.py SHA256 `56fd08826371c184f788b5661cf7f86a07f5e2f3b3af8dbc7cf9a62a821754f8`
- INPUTS.json SHA256 `305638cc26a4b735efd87398f840fca5dd32fad49cd242e712575f9597dfc22d`

## Outcome

The injective joint-P-row theorem is valid in both Types I and II relative to the eight pinned normal-form interfaces. No blocking mathematical issue was found. The argument excludes a nonzero radical with zero P row without assuming compatibility with Q. Its stated compatibility consequences follow, with their Type I and Type II distinctions intact. This checks the new argument and the imported interfaces, not an independent reconstruction of the entire preceding geometric proof chain or a proof-assistant certificate.

## Actual geometric and representation interfaces

1. **Zero-row reduction is faithful.** The natural H1/Serre-duality identification respects target summands, so a zero fourth-endpoint P row makes the actual bundle restriction R→F land in 2D O(-2). Type I radicals already kill X. In Type II the same fact follows for this hypothetical element from Hom_G(O(-8),D O(-2))=0, because Sym6 W=V+P. Since Type II X spans P+D, its ambient constant b has zero P and D coefficients. This uses X as an actual subbundle and its constant span, not as a separate reconstructed or constant summand.

2. **A single saturated D copy.** A nonzero radical cannot kill both X and Y, since R spans Hbar and the constant restriction is faithful. The one-dimensional Hom_G(Y,D O(-2)) therefore makes its two D components a nonzero constant multiplicity vector times dr8. The resulting p embeds one constant D O(-2) direct summand of F. It is not an arbitrary degree-two map whose saturation would need to be proved separately.

3. **P projection and integrability.** Because b has zero constant P coefficient, p_P dr8=0, and the pinned quadratic-polar nonannihilation theorem gives p_P=0. The actual Y is the first polar of f10 in both types. The degree-eight polar realizes the same abstract source W O(-9) after the indicated twist; its equivariant source identification differs only by a constant scalar because End_G(W)=C. Thus p dr8=d(b f10) after constant rescaling is a legitimate equality of polynomial one-forms. There is no unproved variable-dependent source change, and differentiating really gives curl zero.

## Curl obstruction

4. **Unique D channel.** The decomposition D tensor A=Sym6 W+Sym4 W+Sym2 W restricts to V+P+D+A, with a single D. Hence any quadratic equivariant p_D is a scalar multiple of the moment operator m=x^2E-xyH-y^2F. This operator is the infinitesimal action of w tensor omega(w,-), so its equivariance and nonvanishing hold in the universal binary-form models.

5. **Contragredient signs checked independently.** Using E=u partial_v, F=v partial_u, H=u partial_u-v partial_v on D and the dual action E_ext=-y partial_x, F_ext=-x partial_y, H_ext=-x partial_x+y partial_y on coordinate polynomials gives

       Omega=2xE partial_y+H(x partial_x-y partial_y)+2yF partial_x.

   Expanding the total Casimir verifies Omega=(C_D+C_ext-C_total)/2. On the highest Cartan vector u^4 y^8, the first and third terms vanish and the middle term is -32u^4 y^8. This independently checks both the nonzero scalar and its displayed sign; using the wrong external highest-weight convention would obscure this check.

6. **Location of the actual covariant.** The tensor decomposition is Sym12+Sym10+Sym8+Sym6+Sym4. The fixed McKay characters show that only Sym12 has a G-invariant vector, of multiplicity one. The nonzero equivariant covariant r8 is a G-invariant element of this tensor space and therefore lies in that Cartan summand. Consequently Omega r8=-32r8. No SL2 symmetry of the actual module is needed: the operator calculation is on universal representations, and G-invariance locates the actual covariant within them.

7. **Consequence for p_D.** The D projection of the actual integrability equation is c Omega r8=0. Since the characteristic is zero and r8 is nonzero, c=0. This proves p_D=0 rather than merely bounding its image. It does not infer joint-row independence from nonzero individual rows.

## Saturation and final consequences

8. The embedded copy D O(-2) is a direct summand of F. The quotient C O/(D O(-2)) is an extension of locally free F/(D O(-2)) by C O/F, so is locally free. As p_P=p_D=0, its image lies in (A+V)O. The quotient there is torsion-free on the smooth curve and hence locally free of rank one and degree ten. Absence of nontrivial one-dimensional G characters fixes its linearization to O(10).

9. The quotient q to O(28) factors on (A+V)O through O(10). It cannot be zero: that would put a nonzero constant space in F, contradicting H0(F)=0. But an equivariant O(10)→O(28) requires a scalar degree-eighteen invariant, and the fixed character recurrence gives none. This is the contradiction excluding every nonzero element of the joint-P-row kernel in both types.

10. Since J has dimension two, the joint map has rank two. For Type I its target is two-dimensional, so its determinant is nonzero. The earlier full-J-compatibility theorem requires that determinant to vanish; hence dim J_Q≤1 in Type I, retaining possible compatible lines. For Type II, intersecting rank two with the four pinned footprint alternatives leaves only (2,0,0): U dimension 27, Z dimension 24, restricted kernel A+D, restricted cokernel D, quotient kernel D and quotient cokernel P. That quotient remains non-acyclic and cannot be removed by the earlier filtered contraction.

## Reproducible evidence

Executed `python verify.py` and `python -O verify.py`. Both produced identical successful output:

    PASS: 400 checks;8 immutable inputs;45 full-space curl tests;13 Cartan vectors.

The checker authenticates all eight input SHA256 and Git blobs, derives the needed symmetric-power invariants through degree eighteen, checks the exact curl and Casimir equality on all 45 monomial basis vectors, checks commutation with the three total sl2 generators there, and checks the -32 eigenvalue on all thirteen generated Cartan vectors. The written argument supplies the actual-polar identification and saturation, which are not replaced by these representation tests. No actual HM coefficient, selected source instance, or evaluated geometric rank enters the computation.

## Scope retained

Type I full-J compatibility is excluded, not Type I occurrence or its source-dual pairing. A compatible radical line remains possible. Type II full-J compatibility is not excluded, but has only its rank-two 27→24 footprint left. Type III and the source-dual frontier counts are unchanged. The original complete proof repair is not claimed.
