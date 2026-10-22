# Exact actual-extension Q4 compression

## Scope and source

This is a dependency-free Python 3 library using only `fractions` and `dataclasses`. All arithmetic is exact over Q. No floating-point approximation, rank tolerance, symbolic specialization, HM coefficient fixture, network access, coefficient-fetch facility, selected-source evaluation, or parameter search is present.

Read before implementation: PR543 `PROOF.md` and `PRIMARY-INJECTION-AND-FAILURE.md`, at current inspected head `f4e61e37e8be9ad32936baa7c69a3433efdc8c2a`, directory `research/hm/order-four-quadratic-load/`. The implementation instantiates their intrinsic quotient criterion, not a proof that a selected or generic HM pair satisfies it.

Given column-action matrices

- `u`: K3 → K5, shape m × n;
- `v`: K2 → K5, shape m × k;
- `inclusion`: L3 → K3, shape n × ell, required injective;

the routine constructs

    D = K5 / (vK2 + uL3),    N = K3/L3,
    W: N → D,               coker(W) ≅ K5/(uK3+vK2).

No primary rank, residual rank, independence, or split-extension assumption is made. Complements used for coordinates do not discard off-diagonal entries of the supplied maps. The routine proves a statement about its supplied abstract matrices only. Input rational strings such as `"2/3"` and `Fraction(2,3)` are accepted. Floats and booleans are rejected. Matrix dimensions are retained even for zero-row or zero-column spaces.

## Minimal use

```python
from q4_compression import Matrix as M, compress
u = M.of([[0, 0], [0, 1]])
v = M.of([[1], [1]])
l = M.of([[1], [0]])
result = compress(u, v, l)
assert result.verify()
print(result.dimensions)
```

This is the two-dimensional synthetic lift-cancellation example, NOT HM data. Here u kills the primary source. Its residual column and the cubic column differ by a nonzero primary target vector, so the full paired cokernel vanishes. Replacing v by its diagonal residual column `(0,1)` leaves a one-dimensional cokernel, despite unchanged residual coverage.

## Returned certificates and exact identities

For every `Quotient` object with generator matrix G:

- `basis_indices` and `relation_basis` B select independent ORIGINAL columns, so B=G[:,indices].
- `coordinates` Z certifies G=BZ. Thus no relation generator is discarded without a reconstruction certificate.
- `section` S and `relation_coordinates` H, together with `projection` P, satisfy

      [B S] [H; P] = I,    [H; P] [B S] = I,
      PG=0,                PS=I.

  Consequently ker(P)=im(B)=im(G), not merely an inclusion or a rank agreement.

For `Compression`:

- `residual_source.projection` is q_N and `residual_source.section` is J, with q_N J=I.
- `target.projection` is P, with kernel im[v,uL].
- `induced` is W=P u J. The verifier checks the descent identity P u=W q_N.
- `row_transform` R=[H;P] is invertible by the quotient certificates.
- `full_augmented` is [v,uL,uJ]; `reduced_full_block` certifies

      R [v,uL,uJ] = [ Z  H uJ ]
                      [ 0    W  ].

  This preserves all original columns and supplies their exact reconstruction Z.
- `pivot_augmented` is [B,uJ], selecting the independent relation columns. The verifier also checks

      R [B,uJ] = [ I  H uJ ],
                  [ 0    W  ]

  and `pivot_column_transform` is the invertible matrix

      [ I  -H uJ ],
      [ 0     I  ]

  reducing this block to `diagonal_pivot_block` = diag(I,W). Redundant original relation columns are justified by G=BZ, not an unjustified invertible deletion.

Let F be `full_cokernel.projection`, C be `compressed_cokernel.projection`. The returned `forward` A and `backward` B0 satisfy

    A F = C P,    B0 C P = F,    A B0 = I,    B0 A = I.

They are explicit inverse coordinate maps between the full and compressed cokernels, compatible with the canonical map out of K5. These identities certify the actual cokernel isomorphism, not only equality of dimensions. `compress` checks the certificates before returning; verification uses explicit conditionals rather than removable Python `assert` statements.

## Why the construction works

Set G=[v,uL]. Exact row reduction chooses a basis B for im(G), and extends B by standard ambient vectors to a basis [B,S_D]. Its inverse gives P and H. Similarly a complement J to the injective L gives q_N. For every x in K3, x−Jq_Nx lies in L, so Pux=PuJq_Nx. Thus W descends intrinsically. Quotienting D by im(W) removes precisely the remaining uK3 directions, hence gives the full paired cokernel. The explicit inverse maps above implement this canonical identification in the chosen coordinates.

If J changes to J+LB, then Pu(J+LB)=PuJ because PuL=0. Under invertible changes a,b,e,f on K5,K3,K2,L3, input matrices change to

    u'=a u b^-1, v'=a v e^-1, L'=b L f^-1.

The tests build the induced isomorphisms on N and D from quotient projections and sections, and verify their commuting square with W exactly. They also check the nonzero full cokernel isomorphism, not just ranks.

## Tests and reproducibility

Run from this directory:

    python -m unittest -v

Six synthetic test groups cover rational rank drops; genuine off-diagonal lift cancellation; changes of residual representatives; invertible changes of all four input bases with explicit commuting isomorphisms; zero and extreme dimensions; and rejection of invalid inputs plus certificate tampering. The base-change example has a one-dimensional paired cokernel, so its cokernel compatibility check is nonvacuous.

`TEST-RESULTS.txt` records the run; `SHA256SUMS` binds the implementation, tests, README, and that record. This is ordinary reproducible code testing, not a formal proof-assistant certification or a selected HM computation. Dense rational elimination may incur large integer growth; no practical claim is made for large inputs, and there are no project-specific numerical defaults.
