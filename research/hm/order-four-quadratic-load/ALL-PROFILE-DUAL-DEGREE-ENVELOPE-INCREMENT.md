# The dual finite degree envelope removes58 more labels after the primal application

## Result and non-double-counting

On the current143 quotient labels, the dual degree envelope excludes86. Exactly28 were already excluded by the primal46-label application. Thus this second application removes **58 new labels**, taking **97→39**, with profile counts **30/4/5**. The58 consist of52 profile(1,1) and6 profile(2,1) labels. No profile is closed.

The general theorem is [PR715 at8ddbcedc7e01f33ae9aacff56df8da0a33503b57](https://github.com/Akilleez-QA/read-em-and-weep/blob/8ddbcedc7e01f33ae9aacff56df8da0a33503b57/research/hm/order-four-quadratic-load/NEGATIVE-GAUSS-FLAGS-HAVE-A-FINITE-DEGREE-ENVELOPE.md). The first application is `ALL-PROFILE-PRIMAL-DEGREE-ENVELOPE.md`. The prior exclusion of G3.21.bf8462f3a0d7 at f0aaf0dcc7e4503fb6199ddab4bcc8e08a679c66 is retained separately throughout; it is not included in the143,86 or58 counts.

## Dual orientation valid for every profile

The actual bundle Q* is a saturated rank13, degree -54 subbundle of the dual constant ambient bundle. Its Gauss derivative is the negative transpose of E's and has the same generic rank3. Therefore its actual kernel L=(Q*)^- has rank10. Put B=Q*/L, a locally free rank-three bundle. Then

    deg L=-54-deg B.

The actual presentation in `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md` includes Q* in M3* O(-1), so Q*, and hence L, has strictly negative splitting degrees. This does not require H0(Q*(1))=0, a hypothesis unavailable in some profiles. The published source statement also gives no constant subbundle for Q*.

L is saturated in the dual constant ambient bundle because Q*/L and the ambient quotient by Q* are locally free. The natural injection B=Q*/L into that ambient quotient by L identifies the target of the factored second fundamental form. Indeed a section of L has derivative in Q*, since it kills the second fundamental form of Q*. Thus the actual derivative of L factors through B(-2), with exactly the actual Gauss kernel. These are precisely the finite degree-envelope theorem's hypotheses for F=L and J=B.

This argument applies to endpoints as well as interior stages; it uses no l>=2 assumption, no equality of primal and dual degrees, no prescribed rank of later derivatives, and no maximal-profile refinement.

## Independent finite calculation and bookkeeping

Expand each B into ordinary degrees mu1>=mu2>=mu3. The necessary dual inequality is

    -54-(mu1+mu2+mu3)
      <= max sum_i [h_i mu_i-h_i(h_i+1)],

over all h1>=h2>=h3>=0 with sum h_i=10. The checker independently computes this maximum for all143 labels, and recomputes the rank14 primal maxima to identify the28 overlaps. It does not import the primal output. All derivative partitions permitted by the unrestricted theorem remain in both maxima.

The compact certificate lists every one of the58 new stable IDs with its ordinary B degrees, actual L degree, capacity, positive gap and maximizing heights. It also lists the28 overlapping IDs, the full46 primal IDs, baseline historical exclusions, the prior689 ID and the39 remaining IDs. The disjoint historical/prior/primal/new-dual/remaining partition contains exactly the original182 stable IDs.

## Reproduction and scope

Run `python3 verify_all_profile_dual_degree_envelope_increment.py` to generate `all-profile-dual-degree-envelope-increment.json`. It uses standard Python and only the hash-pinned baseline144 and published715 theorem. It is independently reproducible from base715 without unpublished audit files, another checker, missing local witness data or an existing output certificate. A separately produced scope/arithmetic audit agrees with both the58 new and28 overlapping stable-ID sets exactly.

These are bounded integer-degree necessary conditions, not evaluations of actual source coefficients, points, matrices or actual-instance ranks. There are no scans, spikes or consumed experiments. This claim is only the unrestricted dual increment after the primal application; the maximal-profile refinement, positive-defect analyses, realization questions and any SF conclusion remain separate.
