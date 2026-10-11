# Comparison receipt for orders 4, 5 and 6

The bases and connecting matrices were frozen before this comparison.
Shipped labels and sparse maps were not inputs to the enumeration.

- Frozen certificate: `research/hsd-label-audit-61/hsd_label_audit/frozen/higher_certificate.json`
- Content SHA-256: `203311373309eded58fa5e30ee8a9ba1aeb8ff5050f3556abe0a2370685bf7cc`
- Freeze commit: `d154dabe2d6e00dfd0932ecfdc3e980fe9346886`

The change of basis on each ordered source list, and on each raw target list, is the identity.
Its determinant over Q is 1. No integrality claim is made beyond that explicit matrix.
That identity is an identity of raw coordinates. Kernel coordinates are a different presentation.
At orders 5 and 6 the shipped row order is the kernel-free subsequence of the raw list.
A kernel basis vector restores the dependent pivot coordinates.
Surviving rows label those free coordinates. They are not pure raw cohomology classes.

Generated maximum character: U 2, W 2.
Weight-only vanishing from k ≥ 7 uses this generated maximum: True.
That recorded flag compares orders 7 through 12 with the maximum attained at orders 4, 5 and 6.
It is a finite check. The uniform vanishing for every k ≥ 7 is the character bound in the completeness argument.
Surjectivity of the inner connecting map is not extrapolated beyond k = 6.

## D4

- Frozen dimensions: source 520, target 701.
- Shipped shape: 701 target rows by 520 source columns.
- Source change of basis: identity of size 520, determinant 1.
- Raw target change of basis: identity of size 701, determinant 1.
- Kernel-free rows: 701, the ordered complement of the pivots: True.
- Nonzero entries: rebuilt 1962, shipped 1962.
- Map equal over Q: True.
- Raw image meets a C-pivot coordinate: 0 times.
- Alpha columns outside the C kernel: 0.
- Required character 0 block matches the frozen alpha matrix: True.
- Required block determinant over Q: 1.

## D5

- Frozen dimensions: source 627, target 888.
- Shipped shape: 888 target rows by 627 source columns.
- Source change of basis: identity of size 627, determinant 1.
- Raw target change of basis: identity of size 891, determinant 1.
- Kernel-free rows: 888, the ordered complement of the pivots: True.
- Nonzero entries: rebuilt 2484, shipped 2484.
- Map equal over Q: True.
- Raw image meets a C-pivot coordinate: 30 times.
- Alpha columns outside the C kernel: 0.
- Required character 1 block matches the frozen alpha matrix: True.
- Required block determinant over Q: 1.

- E0E1 columns of C5 equal the frozen inner connecting map after the row change
  `[['-1', '0', '0'], ['0', '-1', '0'], ['0', '0', '-1']]`, determinant -1.
- That identification matches entrywise: True.

## D6

- Frozen dimensions: source 744, target 1095.
- Shipped shape: 1095 target rows by 744 source columns.
- Source change of basis: identity of size 744, determinant 1.
- Raw target change of basis: identity of size 1104, determinant 1.
- Kernel-free rows: 1095, the ordered complement of the pivots: True.
- Nonzero entries: rebuilt 3046, shipped 3046.
- Map equal over Q: True.
- Raw image meets a C-pivot coordinate: 90 times.
- Alpha columns outside the C kernel: 0.
- Required character 2 block matches the frozen alpha matrix: True.
- Required block determinant over Q: 1.

- E0E1 columns of C6 equal the frozen inner connecting map after the row change
  `[['-1', '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '-1', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '-1', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '-1', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '-1', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '-1', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '-1', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '-1', '0'], ['0', '0', '0', '0', '0', '0', '0', '0', '-1']]`, determinant -1.
- That identification matches entrywise: True.

No mismatch. Ordered raw labels agree, both full maps agree over Q as coordinate presentations, and the connecting-map change of basis is invertible.
