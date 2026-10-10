# Exact integer quotient arithmetic

This focused package publishes the arithmetic engine used by the current-L
exact-rational scalar calculation, together with a separate tuple-exponent
oracle and deterministic fixtures. It computes in

    Z[v,w,z] / (v^6, w^37, z^22).

The sparse, packed and dispatched multiplication implementations are compared
against an independent direct convolution. Signed coefficients are stored as
ordinary arbitrary-precision Python integers. No finite-field reduction or
Frobenius shortcut is used. In particular, the coefficient of v in (1+v)^71
is 71, not zero.

## Reproduce

Requires Python 3, standard library only. From this directory:

```sh
python check_integer_arithmetic.py
```

Run without `-O`: the checker and arithmetic guards use assertions. The checker
is read-only and prints its receipt to stdout. It exercises:

- 103 products through sparse, packed and dispatched paths, including mixed
  signs, zero and identity, boundary truncations and up to 777-bit coefficients;
- 3 analytic dense products with all 4,884 slots and up to 423-bit inputs;
- 8 ordinary powers, including 71, 72 and 142;
- 90 shifted additions and 4 rejection guards.

The deterministic random seed is 102571. The bundled historical receipt records
the original run and hashes of the unchanged arithmetic and oracle files; fresh
wall-clock timing will differ. The fixture runner has only been relocated and
changed to print rather than overwrite that receipt.

## Why packing is exact

Encode (r,w,z) as r + 11w + 803z. A product has r-degree at most 10 and
w-degree at most 72, so the strides 11 and 73 prevent exponent carries. Split
each input into positive and negative coefficient arrays and perform four
nonnegative packed products. At any encoded exponent there are at most
min(nnz(A),nnz(B)) summands, and positive and negative subsets are disjoint.
Choose a byte-rounded digit base strictly greater than
min(nnz(A),nnz(B)) max|A| max|B|. Thus coefficients cannot carry between digits.
Decode the positive and negative totals separately, subtract, then discard
slots outside the quotient. The 4,096-bit per-digit guard is an implementation
limit and raises rather than returning an approximation.

## Scope

This checks arithmetic, not the geometric source construction, denominator
clearing metadata, source-DAG evaluation, or the full obstruction. The adjacent
scalar-result package supplies a separate downstream contraction replay; its
source-provenance limitation remains explicit. No claim of full theorem repair
or formal verification is made.
