# Independent mathematical review: differentiated stage-two transfer

## Verdict

PASS, conditional on the explicitly retained coefficient-family contraction, common-frame transport, support and selector premises. No missing sign, input-degree correction, projection term or row-differential derivative was found.

Reviewed author artifact: `PROOF.md`, SHA-256 `c0bbb976e98cc7c4e137079a0ddd9ad191607fc8f7608e97088539b185ff17e2` (portable copy; only prerequisite links changed from the reviewed author version).

This review independently derived the operator identities before reading the author's completed derivation, then checked the stable eight-section version. It read the supplied endpoint-defect-transfer, HPL-lowering and scalar/frame-bridge public proofs. It made no fresh remote-source, latest-head, actual primitive-denotation or physical-model claim. No production imports, actual owner/source/model/jet evaluation, physical matrix-polynomial products or external writes were used. This is a mathematical review, not a claim of an independently executable proof checker.

## Independent derivation

Use the author's a,t,S,U,W notation and unsigned J1=Hδj. All identities are family identities, with derivative preserving internal degree. From dj=0 and the contraction decomposition,

    j′ = ja + dt − Hd′j.

Multiplying the differentiated contraction equation on the left by H gives

    H′ = dS − Sd − Hd′H − tπ + jπH′.

This agrees with author equation (4), since H′j=−t and πH′=−π′H. For input internal degree zero the last term vanishes by support. For input degree −1 both projection terms vanish. This is exactly where normalization and the fixed degree-zero cohomology support matter.

Apply the degree-zero formula to δj, and use πδj=Δ and dδj=0. Expanding Hδj′ then yields

    J1′ = dU + δt − tΔ + J1a − Hd′J1 − HδHd′j.

Differentiate J2=−HδJ1. The first differentiated factor gives

    −H′δJ1 = −dSδJ1 − SδjΔ − Hd′J2,

because dJ1=δj−jΔ. The second differentiated factor gives

    −HδJ1′ = dHδU − δU + HδtΔ + J2a
                    + HδHd′J1 + HδHδHd′j.

Here Hδδt=0; the identity HdδU=δU−dHδU has no projection term because δU has internal degree −2. Addition gives exactly

    J2′ = dW − δU − UΔ + J2a
              − Hd′J2 + HδHd′J1 + HδHδHd′j.

Thus all three d′ insertions and both nonclosed-input signs are necessary in the derived expression. Applying a restriction-compatible L with Ld=0 gives the author's selected formula; constancy L′=0 is required only to identify it with the entire derivative of LJ2. A varying input contributes LJ2(Z′).

## Degree and arity check

For input Čech degree n and internal degree zero, t has output bidegree (n,−1), U has (n+1,−2), W has (n+2,−3), and each summand in J2′ has (n+2,−2). The term UΔ means U_(n+1)Δ_n. Stage-two output therefore has five owners for n=2 and six for n=3. The unsigned auxiliary J1 is the negative of the actual HPL stage-one operator for n=3; actual stage two is the same minus word in both cases. No wrong-arity production invocation follows.

## Varying row differential and other corrections

Independently differentiate Δ=πδj, use δj=dJ1+jΔ, π′d=−πd′, π′j=−a, and the displayed j′ decomposition. This gives

    Δ′ = Δa − aΔ − πd′J1 − πδHd′j.

Consequently Δ need not be constant when δ is constant. There is no missing Δ′ in the direct derivative of the literal stage-two word. The author's alternate derivation through π′=−aπ−πd′H−πH′d is also valid.

If δ varies, the literal product derivative adds exactly

    −Hδ′Hδj − HδHδ′j,

and the row compatibility identity acquires πδ′j. If L varies, add L′J2. These corrections do not require moving H through δ. The scalar selector must commute with the admitted restrictions to turn LδU into δ(LU).

## Actual normalization and controls

For H_r(F)=hF+(−1)^r EFh with E=AB, the supplied h²=hA=Bh=0 implies hE=Eh=0. The four-term expansion of H_(r−1)H_r vanishes term by term, and Hj=πH=0 follows from the same side conditions. The author therefore uses the supplied normalized End homotopy rather than silently replacing it. This remains conditional on the original primitive/contraction premises.

For the author's formal acyclic control d=t and H=t^−1, H′=−t^−2=−Hd′H, so dropping d′ would indeed fail. In the independent row-variation control, g=diag(t,1) gives transport(e12)=t^−1e12 and θ=t^−1e11, hence transport′(e12)=−t^−2e12=[transport(e12),θ]. This is a valid nonzero Δ′ example with H=0. It does not test a nonzero J2; the author explicitly preserves that limitation.

## Remaining boundary

The result is an exact conditional reduction of the inner derivative family. It does not prove disappearance of the a, d′ or nonclosed-input defects, cancellation of the complete remainder, an admissible global domain for the new boundary, any detector/trace value, or the global obstruction. Nonconstant outer weights and varying inputs require their own Leibniz and domain accounting. The supplied proof maintains these boundaries correctly.
