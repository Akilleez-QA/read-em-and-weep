# Verdict on the one recorded edge

Reviewed head: `b29c6aec939e4ee270da1bdadd8b3e2469b6e5cc` (#43).

Evidence class: **supplied-quotient replay**. This is not source regeneration.
The value below is one partial term. It is not a scalar-class value.

## Reproduced

The supplied quotient, under the displayed selector for roles `(0,1,2,3)` and
`m=(2,2,2,0)`, equals **8655/16**.

Derived selector parameters, checked against the stated pins:

| pin | derived |
| --- | --- |
| `S` | 6 |
| `d = 6 + m_1` | 8 |
| `L = 22 - m_3` | 22 |
| `w = 35 + S` | 41 |
| orientation sign | `+1` (identity, zero inversions) |
| selected rows | 207 |
| nonzero selected coefficients | 24 |
| signed sum | `8655/16` |

`G(T,z)^{-70}` modulo `(T^9, z^{23})` was expanded twice, by Newton
reciprocal and by the generalized binomial series. The two kernels agree,
every coefficient is an integer, and both equal the rows in `kernels.json`.
All 207 recorded request rows match the derived slot, physical exponents,
integer weight, reduced coefficient, and weighted contribution.

Denominators:

- The quotient's stated common denominator is 64, and the coefficient-array
  pin matches the 203-term list.
- Each of the 24 nonzero selected coefficients reduces with denominator in
  `{1,2,4,8,16,32,64}`.
- `gcd(8655,16) = 1`, so the signed sum is in lowest terms with denominator 16.

Signs:

- The orientation sign used in the sum is `+1`.
- Every one of the 24 nonzero selected coefficients is negative.
- Worked term `(v,w,z) = (5,41,22)`: stored numerator `-266128860` over 64
  reduces to `-66532215/16`, kernel weight `K_3[0] = -59640`, and the
  product is `+495997662825/2`.
- Worked term `(8,41,22)`: stored numerator `-16452272515660` over 64
  reduces to `-4113068128915/16`, weight `K_0[0] = 1`.

Pins at this head:

- `quotient.json` SHA-256 `1be369e0cbbc5379a29d104a459e1f442194a2375b1bf602dcaf809d76460dfa` (manifest match)
- coefficient-array SHA-256 `dfc8ee5bbabef051a9c18708f0b93b758ed34943ace9ee7ee448a0b33640da71`
- `expected.json` pins `8655/16` and `complete_scalar_pairing_computed: false`

## Defect

None in this finite arithmetic edge.

## Missing hypothesis

These are outside the reproduced arithmetic. They are not defects in the
partial term above.

- The quotient is an input. Nothing here regenerates it from the geometric
  source, the fresh numerator, the reversed circuit, or a terminal checkpoint.
- All-entry pole bounds, legal-line comparison, the support enclosures
  47/215/454, safe reversal, and integer clearing stay external. Provenance
  hashes of artifacts that are not in the package were not recomputed.
- The boundary-residue argument that produces this selector is used as the
  displayed selector. It is not re-proved here.
- For `m=(2,2,2,0)` there are 18 orientations. Only `(0,1,2,3)` is present.
  The other 17 are unknown, and cancellation remains possible.
- `8655/16` is not a scalar pairing, a scalar class, an obstruction
  nonvanishing result, or a complete second-scalar coordinate.

Model chain-map identities and prefactor contractions were not rerun. They
are outside this single-edge check.
