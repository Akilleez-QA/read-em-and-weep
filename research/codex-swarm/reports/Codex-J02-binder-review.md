> Worker proposal/review record. Acceptance and supersession are tracked in `../STATUS.md`.

**Codex-J02 → Codex-V03 and orchestrator: scoped mathematical acceptance; schema rejection needs correction.**

Reviewed the proposed binder against source pin `08b73637d4136f91606aad332c46cafd064417f8`, `research/hm/current-scalar-geometric-dependencies/data/{source-formulas.js,model.json}`, and PR79 certificate `research/hm/null-support-certificates/source-second-jet-degeneracy-certificate.md` at `5df68750f766b18a746e50bff662b09829225ab1`.

**Accepted, as a lazy formal contract:** characteristic zero; three ordered finite owners; literal model-chart indices; binary masks; localization at the stated primitive denominators, legal-line denominators and transition determinants.

- Rational partial leaves explicitly differentiate the entire numerator/denominator quotient, including `dp` and `di`.
- The elementary-symmetric pullback includes the Hessian term:
  \[
  \partial_b\partial_aF(e)=
  \sum_{r,s}F_{rs}e_{r-1}(\widehat a)e_{s-1}(\widehat b)
  +\sum_{r=2}^4F_r e_{r-2}(\widehat{a,b}),\quad a\ne b.
  \]
- With \(L_aZ=Q_{v,a}Z-ZQ_{u,a}\), its second jet is correctly
  \[
  V_{ab}=K_{ab}+L_aK_b+L_bK_a+L_bL_aK
  +(\partial_bQ_{v,a})K-K(\partial_bQ_{u,a}).
  \]
  Here \(K_{ab}\) denotes the mixed derivative. Endpoint \(Q\), its derivative nodes, transpose order and physical-frame convention agree with PR79 and public comment **6205660472**.
- Products preserve the required order:
  \(\bar H=K^{-1}V_{01}\),
  \(\bar J=K^{-1}B^{-1}V_{12}K\).
  Traceless components use the stated \(h,e,f\) basis.
- Slots `(13,14,23,24)` and pairing signs `(+,-,-,+)` correctly produce the three demands
  \(C_{ef}-C_{fe},C_{he}-C_{eh},C_{fh}-C_{hf}\), for \(C=J^tSH\).

**Concrete schema defect:** adding a top-level `carrier_map` to an otherwise valid request is silently accepted and discarded. This fails the requested explicit rejection of external carrier mappings, although literal `model_chart` lookup remains unchanged. Require an exact top-level key set. Owner-level external fields and infinity owners already reject.

Additional validation weaknesses: `standard=[0.0]*4` and `[false]*4` are accepted through Python equality; a null owner raises incidental `TypeError`. A missing owner field correctly raises `ValueError`.

**Executed evidence:** authorized metadata self-tests passed normally and under `-O`, each reporting 866 nodes. In-memory malformed-request checks reproduced the outcomes above. No files were written; no physical polynomial, arithmetic oracle or source identity was evaluated.

**Unresolved semantic dependency:** hash authentication and node-presence controls do not verify an AST evaluator, quotient-rule lowering, or equality with independently differentiated physical transitions. Those remain untested. No actual-source cross-Gram symmetry, detector annihilation, boundary completeness or corrected full-sign \(R^\sharp\) conclusion follows.

**Next step:** Codex-V03 should tighten schema rejection; subsequent review should compare independent formal physical differentiation with the emitted recurrence. This review supplies new binder/schema evidence; the mathematical criterion itself is the published PR79 result.