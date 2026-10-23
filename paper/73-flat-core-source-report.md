# A flat core counterfamily and the missing selection input

**Craig Ward · 23 October 2026 · Source report on PR1029**

This is a report of mr. slop's [full immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/88d079cafbe6b051ed703412e2ee356fcb2f999f/research/hm/core-flat-rank-jump/PROOF.md), not an independent reproof or an actual HM family.

## 1. A saturated universal family

Choose nonzero generators of the universal channels u:W′O(-3)→SO(1), v:W′O(-3)→AO(2), and c:O(-8)→SO(1). The proof shows v and c are subbundles with quotients O(12) and VO(4), respectively. For an auxiliary affine parameter t set

    F_t(x,z)=(t u(x)+c(z), v(x)).

Because v and c inject fiberwise, F is a rank-three subbundle on the entire parameter product. Its quotient Q_univ is a vector bundle, hence flat, with rank 4 and degree 24 in every fiber. This is a universal parameter, not a selected actual HM coefficient.

## 2. Both cohomological alternatives persist

The quotient sequence is

    0→VO(4)→Q_t→O(12)→0.

Its extension class is t times a nonzero class in a one-dimensional equivariant Ext space. Nonvanishing follows from the connecting homomorphism and the absence of an equivariant AO(2)→VO(4) lift. The known sextic evaluation sequence then identifies

    Q_t=PO(6) for t≠0,
    Q_0=VO(4)⊕O(12).

All splitting degrees are at least four. Thus the precise universal core channels, saturation, positivity and flatness coexist with the jump.

## 3. The complete-evaluation interface also survives

Adding O(2) gives ample globally generated C_t of rank 5 and degree 26, with the unique invariant quotient to O(2). Cohomology and base change, together with the relative diagonal resolution, produce the actual complete-evaluation sequence for this auxiliary family:

    0→E₂₆O(-1)→H₃₁O→C_univ→0,
    E₂₆=2W+W′+2S+2T₆,
    H₃₁=1+3A+V+2P+2D.

Equivariant multiplicity trivializations need not be canonical; the evaluation construction itself is not an arbitrary chosen matrix. Both fibers retain the same evaluation characters and fiberwise injectivity. Nevertheless dim H⁰(C_t(-12))^G is zero for t≠0 and one at zero, the cohomological alternatives associated to the actual top-obstruction criterion. No actual incidence map σ_t is assigned to this auxiliary family.

## 4. Precisely what the counterfamily rules out

The reduced exact core, complete-evaluation character interface, positivity, saturation and flatness alone cannot select whether the W′→S block vanishes. Additional actual-map information or another geometric condition is necessary.

The explicit core and evaluation pencil lie over the same auxiliary C_univ, but the proof **does not establish** that the explicit core is obtained through the historical HM complement choices and reduction maps. Such compatibility is excluded from the no-go scope and could provide an additional selection condition. The counterfamily does not show that both types occur among actual HM objects, or that every actual-geometric selection argument is impossible.

No actual C row, top obstruction, vertex scalar or source is selected. Seven opposite-bundle types remain separate from the four-pair source-dual frontier. The source reports authenticated inputs, independent whole-proof review and ordinary/optimized checks; this chapter preserves their attribution without claiming another independent proof.
