# Horrocks–Mumford and carrier gate ladder

The audit, fault tree, and FMEA are in [gate-ladder.md](gate-ladder.md).

## Fixed chosen carrier

The central defect of the fixed chosen carrier has independently certified length \(\operatorname{length}_B(Q)=12\).

- PR #1, comment [6104798062](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6104798062).
- PR #1, comment [6104803214](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6104803214), an independent SymPy Groebner-basis reproduction of the same five-relation module.

As of the earlier checkpoint, before 6104798062, that length was uncomputed.

- G2, the global vector-bundle extension, is **EXCLUDED** for this carrier only.
- G1, the formal continuation of this carrier, stays open.
- Other formal-lift and carrier choices stay **OPEN**.

A parameter-family continuation by upper semicontinuity needs a finite or proper relative-support certificate for \(Q\) over the base. The module \(\mathbf{Q}[t,x]/(tx-1)\) has fibre length \(1\) for \(t\neq 0\) and length \(0\) at \(t=0\). The target is a non-empty zero-defect locus. A smaller positive length remains a defect.

This result does not settle the original theorem, the central conditions for other carriers, or the Horrocks–Mumford second-order obstruction computation.
