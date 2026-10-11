# Horrocks–Mumford and carrier gate ladder

The audit, fault tree, and FMEA are in [gate-ladder.md](gate-ladder.md).

## Fixed chosen carrier

The independent checks establish the displayed finite module of the fixed chosen carrier and the conditional Ext-to-central-defect bridge, with \(\operatorname{length}_B(Q)=12\) for that displayed module.

- PR #1, comment [6104798062](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6104798062).
- PR #1, comment [6104803214](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6104803214), a SymPy Groebner-basis reproduction of the same five-relation module.

The two checks share a source identification, so the geometric attribution is not independently certified twice. The total-resolution and source-identification artifacts are still requested. As of the earlier checkpoint, before 6104798062, that length was uncomputed.

- G2, the global vector-bundle extension: the geometric exclusion for this carrier is conditional on the total-resolution and source-identification artifacts.
- G1, the formal continuation of this carrier, has status formal construction reported; immutable artifact review pending.
- Other formal-lift and carrier choices stay **OPEN**.

A correctly identified fibre with \(Q_t=0\) is a valid pointwise test. It is not a false pass, and that test stays available. The failure mode is inferring generic or neighbourhood vanishing from that one fibre without the family hypotheses, flatness and base change. A parameter-family continuation by upper semicontinuity still needs a finite or proper relative-support certificate for \(Q\) over the base. The module \(\mathbf{Q}[t,x]/(tx-1)\) has fibre length \(1\) for \(t\neq 0\) and length \(0\) at \(t=0\). The target is a non-empty zero-defect locus. A smaller positive length remains a defect.

A Horrocks–Mumford Frobenius or Cartier fixture test runs in characteristic \(3\), or in an extension of \(\mathbf{F}_3\) in which the coefficient Frobenius is handled. A large prime of another characteristic cannot validate those identities. A large prime remains available for characteristic-free linear algebra, such as the ranks of matrices defined over \(\mathbf{Q}\). The current fixtures are formal over \(\mathbf{F}_3\), and no carry defect is reported.

This result does not settle the original theorem, the central conditions for other carriers, or the Horrocks–Mumford second-order obstruction computation.

## Citation correction

The accessed source of arXiv:2502.03415 has no Lemma 8.3.4 and no Remark 8.3.5. The first-order criteria are Lemma 8.2.4 and Remark 8.2.5. Equations (8.3.4) and (8.3.5) are a secant Orlov transform and a subspace of \(HT^2\). [PR #67](https://github.com/Akilleez-QA/read-em-and-weep/pull/67) records that the only surviving strategy is Pridham, arXiv:1208.3111, Remark 1.21 together with Corollary 1.20, as an unverified comparison. The audit is in [gate-ladder.md](gate-ladder.md).
