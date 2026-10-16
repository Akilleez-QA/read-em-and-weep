# Exact nonzero Omega at the fixed source specialization

The single bounded source attempt completed on 2026-10-16. It used the selection fixed before evaluation at PR90 commit 4f6fceab9ddddd2c680ad2d9e2193d1e0848c291:

- Vertices (carrier,mask): (0,0), (1,5), (2,10).
- Rational base point: (2,13/6,7/3,5/2), original all-finite frame.
- Source model SHA-256: 635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926.
- Executed launcher SHA-256: 0f68a68aaeb2461dcc197ffb167ecf8fd956e0b195840c506bfb6053a552c453, published before execution at PR79 1931a5c527d63921684521966797186fc63a29b9.

The output is `one-attempt-result.json`, SHA-256 a6290391e3cfdf7f211bec87dcbc3fd516471377642e4f839f0bc9efd85babe2. It contains all exact rational H/J arrays, cross-Gram matrix, three skews, stripped Omega matrix, denominator checks, normalization, source/code hashes and counters. The child exited successfully. Both independent derivative routes agreed, including the full elementary mixed Hessian and direct moving-frame differentiation; PI, determinant and row-cocycle germ checks passed.

The stripped Omega is nonzero. A compact exact witness is its (0,0) entry: its denominator is a unit modulo101 and its residue is7. This is a certificate about the already computed exact rational number, not a probabilistic source computation. The full numerator and denominator are in the result. Since the physical Omega is this matrix times y0*y1*y2*y3, and each y_i is nonzero at the chosen elliptic lift, physical Omega is nonzero too. The first mask is zero, so no additional constant first-frame conjugation occurs.

Thus the proposed actual-source pointwise identity Omega=0, equivalently J-transpose-S-H symmetry, is false. This result does not imply that the complete raw remainder, any assembled detector, or the global obstruction class is nonzero. Those remain unresolved. In particular, other terms may still cancel or form a boundary.

The successful attempt used560048 rational operations/constructions,5232964 integer primitives and maximum1041 intermediate integer bits, all below its unchanged refusal caps. Combined captured child output was12372bytes. The final parent result, including supervision fields, is12430bytes. No alternate point, adaptive retry, or cap increase occurred. The one-attempt allowance is consumed; there are zero remaining invocations under this decision. The historical residue replay is unchanged and unreleased.

`verify_recorded_result.py` independently uses Python Fraction arithmetic to reconstruct Omega and the full cross-Gram matrix from the saved H/J arrays, check all skews, exact tracefreeness, nonzero denominator records and the modulo101 witness. It reads only the saved certificate and does not evaluate the source. It passes in normal and optimized Python. The derivative agreement itself was checked inside the one supervised source attempt, not by rerunning that attempt.

The prior independent mathematical preparation review remains applicable to the unchanged kernel. Root reviewed the additive launcher and its one-line release change; peer review of that wrapper was requested but had not been received before the single attempt. This is recorded explicitly rather than claiming external acceptance. The full reproducible evidence is supplied for independent review.
