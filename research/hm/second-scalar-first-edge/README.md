# Second scalar map: one exact oriented edge

For the separate map

    L_minus(X) = X02[0,5] - X13[10,1],

the supplied exact quotient gives the signed contribution **8655/16** for
orientation **(0,1,2,3)** and pairing monomial **m=(2,2,2,0)**.
There are 203 nonzero terms in the full supplied quotient and 24 nonzero
coefficients among its 207 selected rows.

**This is one edge, not a scalar-class value.** This target requires 18 oriented
contributions; the other 17 are not supplied or computed here. They remain
unknown, and cancellation is possible. This package establishes neither
nonvanishing nor vanishing of the scalar class or the full obstruction.

## Run from a clean copy

Python 3.10 or later, standard library only:

```sh
python replay.py
python -m unittest -v test_replay.py
```

No network, installation, neighboring checkout, or original source files are
needed. The main command also works when invoked by absolute path from another
working directory. Explicit validation stays active under `python -O`.

The replay:

1. Verifies the package manifest and all 203 exact quotient terms.
2. Independently constructs all 207 coefficients of
   G(T,z)^(-70) modulo (T^9,z^23), using plain tuple convolution and Fraction
   arithmetic. It checks the inverse-power identity and the supplied kernels.
3. Derives every requested physical exponent, quotient slot, integer weight,
   coefficient and product, and compares all 207 recorded rows.
4. Sums the exact products with the positive orientation sign, obtaining 8655/16.
5. Verifies the unchanged reduced MODEL's byte and canonical pins, ten
   chain-map basis identities, both merged-anchor inclusion/H0 rows, all 30
   entries of the relevant E=IP rows and 300 generic-Z coefficients.
6. Ties the new column-5 right prefactor's embedded matrices and denominators
   directly to that MODEL, and checks both polynomial contractions.

The tests also derive the kernels by an independent generalized-binomial
expansion, test homogeneous-slot isolation and exact rational arithmetic, and
reject malformed or altered data. No numerical source evaluator is included.

## Reproduction boundary

This is a **supplied-quotient/selector replay**. It does not rebuild the fresh
geometric numerator, the normalized source or the compact reversed source, nor
reconstruct a terminal checkpoint. Attribution of the supplied quotient to
that geometric source relies on the separately recorded source and terminal
audits. Their original hashes are preserved in `provenance.json`; unavailable
artifacts and absent publication links are explicit in `SOURCE-DEPENDENCIES.md`.

The new source uses fresh bounds 47/215/454 and the 9×44×23 window, not the
original map's factor-48 or 6×37×22 window. No previous map's structural zeros,
relation certificates, coefficient arrays or scalar result are applied here.

## Files and integrity

- `quotient.json`: all 203 terms of the supplied quotient, with denominator 64.
- `request.json`: all 207 exact selection rows and their recorded coefficients.
- `kernels.json`: exact integer kernel coefficients, serialized as strings.
- `expected.json`: the one-edge result and explicit incomplete-scope flags.
- `model.json` and `right-prefactor.json`: unchanged small model/prefactor inputs.
- `MATHEMATICS.md`: map conventions, source assumptions and selector derivation.
- `SOURCE-DEPENDENCIES.md`: what is and is not publicly reproduced here.
- `provenance.json`: original artifact hashes, distinct from public-file hashes.
- `manifest.json`: SHA-256 and byte length of every distributed file except the
  manifest itself. It is an integrity inventory, not a source-validity proof.

Public JSON exports omit execution paths and operational metadata. Only
`model.json` and `right-prefactor.json` are included byte-identically to their
original artifacts. The sanitized exports have different bytes; original and
public digests must not be substituted for one another.
