# Residual Koszul lifts force global alternating-transfer vanishing

**23 October 2026 · PR1089, read in full**

[Immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/f8dfebc8c12cbefd3b17422fa1220629e90af78e/research/hm/source2-pure-v-alternating-vanishing/PROOF.md), blob `7459702e0b6c28aa6605ca34e2cbd98a9d366417`.

## Global conclusion under the actual pure-V hypotheses

For the same actual invariant quadratic Q, the radical j and canonical endpoint homotopy h,

    j3(ker Q3)=I3,
    rank_T(Q3,j3)=4,
    κ=0.

The rank is on T multiplicity spaces; Q3 itself has actual vector-space rank eighteen by [PR1086](111-actual-odd-quadratic-rank.md). The odd endomorphism (j3,0) is **not nullhomotopic**. This does not contradict the even endpoint homotopy and does not extend h to both complexes.

The transfer B is symmetric and determined by its diagonal R:

    B(a,b) = [R(a+b)−R(a)−R(b)]/2.

Zero R, equivalently zero B, remains unexcluded. Symmetry is not ambient mixed-operator commutation, and no surviving positive-component rank follows.

## Actual residual Koszul lift

Set Z=im Q2 and choose an equivariant right inverse G:Z→M2. Since NR4⊂Z, the actual Koszul map δ on NR3 can be lifted:

    v_G=X(Id_W⊗G)δ|NR3.

Actual multiplication gives Q3v_G=0. The radical image is

    j3v_G=X(Id_W⊗h|NR4)δ|NR3=:θ.

θ is independent of G, although v_G need not be. Differences of lifts land in K3=ker Q3∩ker j3. This is an actual kernel construction, not a section on all of M4 or a horizontal splitting of NR.

If h|NC4 is nonzero, it induces NC4/I4≅I2; the actual isomorphism δ:NC3→W⊗NC4 makes θ(NC3)=I3. If h|NC4=0, h descends through the genuine quotient N8,4. It remains nonzero on its D channel because h is an isomorphism on the marked D_can. With the coherent inclusions i2(f)=f12 f and i3(g)=f12 g, its quotient formula is

    θ̄(a⊗g)=λ i3[x(a,yg)₂−y(a,xg)₂]
           =2λ i3((a,g)₁),   λ≠0.

This full polynomial identity has universal rank six, hence θ is onto I3 in this case also. The same λ occurs in both terms by the actual inherited arrows. No lift of N8 to NR or endpoint-nine assumption enters the descent.

## Exact common kernel and odd cohomology

The surjectivity j3(ker Q3)=I3 adds one to the T-multiplicity rank three of Q3, giving combined rank four. The [mixed-syzygy obstruction](110-mixed-syzygy-transfer.md) then forces κ=0.

There is an exact sequence

    0 → K3 → ker Q3 --j3→ I3 → 0,
    K3 ≅ 3W′+3S+2T,
    K3/F3 ≅ 2W′+3S.

These are representation identifications, not canonical splittings. The quotient has dimension sixteen and no T. Consequently the T restriction of H̄ vanishes; its W′ restriction is **not determined here**.

On odd cohomology ker Q3, j3 is nonzero and square-zero. On its three-dimensional T multiplicity space it has rank one and Jordan blocks (2,1). The T-isotypical part of K3 equals that of the actual F3, not merely an abstract equal-character replacement.

## Current limits

Endpoint sixteen remains necessary with two unselected projection mechanisms and negative module lengths 51 or 45. The diagonal's two symmetric channels remain unselected, including their simultaneous vanishing. The universal five-stratum component-scheme theorem is unchanged; no actual source, coefficient, positive/full-adjoint rank or source-pair cut is supplied. Four necessary pairs remain.

The written proof uses seven authenticated inputs, exact determinant signs, actual quotient maps and coherent inclusions. Formal coefficient checks and the universal rank-six certificate support these arguments, not an evaluated HM-instance matrix.
