# Comparison receipt

The bases were frozen before this comparison. Shipped labels and sparse
maps were not inputs to the enumeration.

- Frozen certificate: `research/hsd-label-audit-61/hsd_label_audit/frozen/basis_certificate.json`
- Content SHA-256: `8044d1e26a3b0419570cec48a388afabec58a7e0b89d5d3ca20318854b6836a6`
- Freeze commit: `a628b449f9c48bb08a227d55cc65c729fb890d7b`

The bijection is the identity on ordered labels.
A frozen U record `(slot, e, dual)` is the shipped source label `[slot, e, dual]`.
A frozen W record `(slot, e, actual)` is the shipped target label `[slot, e, actual]`.
The change-of-basis matrix is the identity, so the rebuilt alpha matrix is
compared in that common order.

Alpha multiplication uses the frozen finite representative of each U basis
vector, the finite relation `(-a0, W^6, -g, XY)`, the all-negative projection,
and removal of forced lower terms with the same cutoff as the basis.

## D2

- Frozen dimensions: source 336, target 390.
- Shipped shape: 390 target rows by 336 source columns.
- Label sets equal: source True, target True.
- Ordered identity: source True, target True.
- Nonzero entries: rebuilt 1068, shipped 1068.
- Full matrix equal over Q: True.
- Character -2 slice: 16 rows by 15 columns.
- Slice equal over Q: True.
- Slice rank over Q: 15.
- Slice determinant over Q: the slice is not square.

## D3

- Frozen dimensions: source 423, target 534.
- Shipped shape: 534 target rows by 423 source columns.
- Label sets equal: source True, target True.
- Ordered identity: source True, target True.
- Nonzero entries: rebuilt 1480, shipped 1480.
- Full matrix equal over Q: True.
- Character -1 slice: 9 rows by 9 columns.
- Slice equal over Q: True.
- Slice rank over Q: 9.
- Slice determinant over Q: 1.

No mismatch. The ordered labels and both full matrices agree exactly over Q.
