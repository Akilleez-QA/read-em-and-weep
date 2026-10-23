# Exact certificate schema, version1

The executable schema is `check_certificate.py`. A UTF-8 JSON object has
exactly these top-level fields:

```text
schema: "source2-finite-correction-v1"
binding:
  theorem_commit: "5b52eedce3420ccc3e407e97201bcdd056501bbf"
  theorem_sha256: "d1f96ad68df6781474e0aa247625b08de8cfc06e2af854418cbd32ce52469140"
  data_sha256: lowercase hexadecimal SHA256 of canonical data JSON
data:
  variables: ["a0", "a1", "a2"]
  dimensions: {"N": positive integer, "M": positive integer, "P": positive integer}
  maps: {"Q": matrix, "T": matrix, "s": matrix, "i_P": matrix}
  corrections: [matrix x0, matrix x1, ..., matrix x23]
  generators: [generator, ...]
```

No additional keys are accepted at these levels or inside matrices or
generators. Duplicate JSON keys, floating-point numbers, nonfinite numbers
and booleans in integer positions are rejected. A zero polynomial matrix
is represented by an empty term list, never by explicit zero terms.

## Matrices and coefficient field

A matrix is exactly

```json
{"rows": 2, "cols": 3, "terms": [[0, 1, [2, 0, 1], [-7, 3]]]}
```

This example has entry `-(7/3)*a0^2*a2` in zero-based row0, column1,
with all other entries zero. Each term is exactly
`[row, column, [e0,e1,e2], [numerator,denominator]]`.

- Row/column indices are in bounds. Exponents are nonnegative integers.
- Numerators are nonzero integers; denominators are positive integers;
  numerator and denominator are coprime. Fractions are exact rationals.
- A matrix cannot repeat a `(row,column,exponent-vector)` key. Term order
  has no algebraic meaning, but **does** affect the data's content digest.
- Each nonzero term must have the required total homogeneous degree.
  Empty matrices satisfy any specified homogeneous degree.
- `Q` has shape `M by N` and degree0; `T` shape `M by N` and degree1.
- `s` has shape `N by P` and degree0; `i_P` shape `M by P` and degree0.
- `x_i` has shape `N by P` and degree `i`, for each `i=0,...,23`.

The use of letter `P` for a dimension here does not itself identify the
actual representation P. Exact data over an unsupported algebraic field
must not be encoded as decimal or rational approximations.

## Optional supplied generator actions

A generator has exactly `name`, `A`, `N`, `M`, `P`. Its name is unique,
nonempty and at most80 characters. The four action values are constant
square matrices of dimensions3, N, M, P respectively and must be
nonsingular. No relations, orders, faithfulness, or generating property
are assumed or proved by the checker.

Coordinates are columns. For an action `A_g` and a polynomial matrix
`f(a):source -> target`, the tested equation is

\[
 f(A_g a)\,R_{source}(g)=R_{target}(g)\,f(a).
\]

It is checked coefficient-by-coefficient for `Q,T,s,i_P` and every `x_i`.
The coordinate substitution is exact expansion of the three linear forms,
not evaluation at sample directions. To turn these identities into group
equivariance, a separate audit must identify these actions as valid,
generating actions of the intended group on the actual spaces.

An empty generator list is allowed only for the weaker polynomial check;
the result says equivariance was not checked. A nonempty list says only
that the equations for the supplied generators were checked.

## Digests and provenance

The canonical serialization of `data` is the ASCII byte sequence produced
by Python's

```python
json.dumps(data, sort_keys=True, separators=(",", ":"),
           ensure_ascii=True, allow_nan=False).encode("ascii")
```

`binding.data_sha256` is its SHA256, rather than a hash of the entire
certificate, so there is no circular hash field. All matrices, corrections,
actions, dimensions and variable names are within the hashed payload.
The optional CLI `--expected-data-sha256` demands equality to a digest
provided separately by the caller. Neither digest route proves actual-map
provenance. JSON has no field that can set actual-map authentication to true.

The theorem text itself is byte-pinned with SHA256 and Git's blob SHA1;
its commit identifier is also checked against the fixed public source.
Only content identity is checked locally, not a digital signature or a
live remote commit/tree membership proof.

## Mathematical and resource outcomes

`ALGEBRAIC_IDENTITIES_VERIFIED` means the supplied equations passed.
It never means that an actual HM instance has been certified. Missing
external hypotheses are always explicit in the result.

`CERTIFICATE_REJECTED` means invalid encoding or a failed supplied
equation. It does not refute existence of other corrections.

`RESOURCE_LIMIT_INCONCLUSIVE` means a documented resource bound was hit.
The input was not fully verified and no mathematical failure is inferred.
