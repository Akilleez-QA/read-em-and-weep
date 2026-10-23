# A finite correction-certificate checker

This package checks **supplied polynomial identities**, not an HM source
realization. No actual certificate is included. All executed coefficient
tests are newly constructed universal or synthetic examples.

## Mathematical interface

The finite theorem in [PR1107](https://github.com/Akilleez-QA/read-em-and-weep/pull/1107),
at commit `5b52eedce3420ccc3e407e97201bcdd056501bbf`, reduces the rank36
outcome for the original positive 37-by41 component to a finite certificate:

\[
 x_0=s,\qquad Qx_0=i_P,\qquad Qx_i=-T(a)x_{i-1}\quad(1\leq i\leq23),
\]

where every `x_i:P -> N2` is equivariant and homogeneous of degree `i`
in the three coordinates of `a`. The equivalence is conditional on the
retained actual-source, actual-map, sheaf and minor-degree hypotheses.
The exact theorem text is retained as `inputs/PR1107-PROOF.md`.

The checker verifies the following over `Q[a0,a1,a2]`:

1. Consistent dimensions; homogeneous degrees of all supplied maps.
2. All24 equations above, including `x0=s` as a separate condition.
3. If supplied, equivariance for each named, nonsingular constant action
   on the coordinate, domain, target and P spaces.
4. Canonical-JSON SHA256 of the supplied data, optionally against a
   separately supplied expected digest, and both hashes of the theorem text.

It performs no search for corrections, no numerical substitution, no
evaluation of source-instance ranks, and no maximal-minor computation.
The group-action nonsingularity test concerns only supplied constant
generator matrices, not the pencil. No group relations or generating
property are inferred from these checks.

## A directly checked universal consequence

Put `X(t)=sum(i=0..23) t^i x_i`. Coefficient collection gives

\[
 (Q+tT)X(t)=i_P+t^{24}Tx_{23}.
\]

If the retained actual identities `Qd=0` and `Td=i_P Ld` hold, then

\[
 (Q+tT)(d-tX(t)Ld)=-t^{25}Tx_{23}Ld.
\]

Thus all original coefficients through order24 cancel. The term
`Tx23` need **not** vanish. The positive synthetic example has a
nonzero terminal term and passes; a checker requiring it to vanish
would reject certificates allowed by the finite theorem.

Under that theorem's retained lower pivots (33 units and three order-two
pivots), a remaining finite pivot would force a maximal minor of order
at least `3*2+25=31`. The separately proved degree bound30 rules it out.
This final argument is a conditional use of the theorem, not something
established by checks on arbitrary supplied matrices.

## Exact boundary of any conclusion

To apply the rank36 conclusion, an external mathematical audit must establish:

- The supplied `Q,T,s,i_P` are the exact original positive actual maps of
  the **same** source2 nonzero pure-V compatible-radical object, in coherent
  bases and coordinates, with dimensions `N2=41`, `M4=37`, `P=4`.
- The retained hypotheses of PR1107 hold for that object: the actual
  radical/endpoint identities, sheaf-injective second page, actual initial
  symbol statements, torsion-free target and exact `(m,kappa)` resolution,
  original/quotient transport, known lower pivots, and degree30 minor bound.
- The supplied generator actions are the correct group representations
  on these exact spaces, obey the group relations, and generate the group.
  Checking intertwining for arbitrary named invertible maps is not enough.
- The coefficients really belong to the supported rational field in
  the declared bases. Algebraic coefficient fields require an exact-field
  extension of this checker; rounding them to rationals is not supported.

Matching hashes bind bytes, not geometry. Even a separately trusted digest
does not prove these hypotheses. A self-consistent digest is not source
authentication. The checker always returns `NOT_ESTABLISHED` for actual-map
authentication and retained geometric hypotheses, and `NOT_DETERMINED` for
the actual rank. Original dimensions are reported only as a shape check.

No actual maps or correction coefficients were supplied, so this package
does not determine the actual rank, evaluate a sequential obstruction,
prove source occurrence or establish full-adjoint invertibility. Rejecting
one proposed certificate also does not prove nonexistence of another one,
nor does it prove rank37. An empty generator list verifies the polynomial
identities only and explicitly reports equivariance as `NOT_CHECKED`.

## Reproduction

Python3.8 or later and the standard library suffice. No installation,
network access or external computer is needed. From this directory:

```sh
python verify.py
python -O verify.py
python check_certificate.py synthetic-example.json
python check_certificate.py synthetic-example.json --expected-data-sha256 \
  "$(python -c 'import json; print(json.load(open("synthetic-example.json"))["binding"]["data_sha256"])')"
```

The last command demonstrates the interface only: reading the expected
digest from the same certificate is **not independent authentication**.
In an audited workflow the expected digest must come from the separate
source-binding review, whose geometric obligations still remain external.

`verify.py` independently regenerates the fixture, runs the tests, checks
the complete CLI result, and prints deterministic JSON. It does not write
or mutate inputs. Its output is retained as `RESULT.json`.

The fixture has two scaled image coordinates and a free third domain
coordinate, rational binomial corrections in all three variables, a
nontrivial coordinate-swap action, and free homogeneous kernel corrections.
It is an abstract test, not an invented realization of an HM source.
The zero-data shape test makes the authentication boundary explicit.

Bounds are enforced: input8MB, dimension64, at most8 generators,
100000 total input terms/intermediate terms, 512-bit input coefficients,
4096-bit intermediate coefficients and5000000 arithmetic steps. Hitting
a bound returns `RESOURCE_LIMIT_INCONCLUSIVE`, not a mathematical rejection.
These are fixed testing bounds, not a capacity guarantee for a dense
original-size41-by37 problem or all its corrections. A mathematically
valid certificate can exceed them. No limits are raised automatically.
The CLI exit codes are0 for verified supplied identities,1 for rejected
input or false identities, and2 for an inconclusive resource stop.

See [SCHEMA.md](SCHEMA.md) for the exact serialization and conventions.

## Public source

- [Finite theorem, immutable text](https://github.com/Akilleez-QA/read-em-and-weep/blob/5b52eedce3420ccc3e407e97201bcdd056501bbf/research/hm/source2-pure-v-finite-obstruction/PROOF.md).
- [PR1 finite-theorem coordination](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6372051513).

The retained theorem SHA256 is
`d1f96ad68df6781474e0aa247625b08de8cfc06e2af854418cbd32ce52469140`;
its Git blob SHA1 is `a8f57401d93c296d23a5ed55cd09d8893222e7c1`.
The public immutable source was fetched and its bytes matched both pins.
This authenticates this immediate written source, not its hypotheses for
any particular object or every ancestor theorem recursively.
