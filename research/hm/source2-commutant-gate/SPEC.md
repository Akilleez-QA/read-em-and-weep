# Contract for a future fixed-HM source2 commutant test

## Present status

Preparation only. This slice contains a proof and this contract. It
contains no actual HM tensor fixture, no instantiated commutant matrix,
no selected source evaluation, and no source2 exclusion.

The object to authenticate is the original pair of negative
multiplication tensors from PR790 at
af0e03d26da5e47d18ae732291aca46f4d448dc5,
research/hm/source2-first-constant-block/PROOF.md, Section 6. The pinned
normal-form and algebra hypotheses and their dependencies remain those
listed in PROOF.md. An implementation must report missing authenticated
source data rather than manufacture a tensor with the right dimensions.

## Required source package

A future evaluation must freeze all of the following before constructing
either gate:

1. The repository commit, exact source paths, byte hashes, and a derivation
   identifying the supplied maps with multiplication on the fixed actual
   HM cohomology spaces M2,M3,M4. Record the original cohomology quotient
   representatives and the induced maps, or an equivalent independently
   checkable exact construction. Matching representation characters does
   not authenticate the tensors.
2. An exact characteristic-zero coefficient field K embedded in C, its
   representation, and all denominators. If using multiplicity coordinates,
   K must support the stated split irreducibles and exact isotypic bases;
   otherwise extend K. An alternative raw-matrix implementation must
   separately authenticate a complete basis of each End_G(Mi) by exact
   G-commutation equations; it cannot assume the displayed multiplicity
   matrix coordinates over an unsplit field. A rational field of definition
   is not presumed.
3. Exact G actions on W and M2,M3,M4; exact isotypic identifications with
   the characters in PROOF.md; and exact bases of the two equivariant Hom
   spaces. Record all changes of basis. Each irreducible multiplicity
   space must retain its full matrix of endomorphism unknowns.
4. The two actual tensors alpha:W tensor M2 -> M3 and
   beta:W tensor M3 -> M4, with the same fixed W and exact equivariance
   identities. Both basis variables must be represented in both arrows.
   A simultaneous coordinate change is only a recorded presentation
   change; variable-changing endomorphisms must not be added to the kernel.
5. The common-pencil identity B_u A_v=B_v A_u and the original cohomology
   origin of the pair. This identity is an input consistency check; by
   PR788 it does not by itself distinguish the actual tensors from abstract
   feasible ones. Do not claim that a finite sample proves the required
   all-parameter geometric hypotheses.

Any failure of these prerequisites leaves the actual test incomplete.
The abstract pencil construction of PR788 is suitable as a separately
labelled synthetic check only. Its output cannot certify any actual HM
result. The trace and dimension identities of PROOF.md need no fixture.

## Exact construction and independent replay

Build Delta from its intrinsic formula in PROOF.md (4). It has 113
scalar unknowns and 153 scalar equations in exact multiplicity bases.
Append the three dimension-weighted ordinary trace rows (13) to obtain
Delta_tr of shape 156 by 113. Store the exact row/column ordering and
the complete basis/provenance manifest with the matrices.

For independent replay, the reviewer should form the full fixed-basis
equations X3 A_u-A_u X2, X3 A_v-A_v X2,
X4 B_u-B_u X3, X4 B_v-B_v X3 using the same 113 equivariant unknowns.
Before equivariant row compression these have

    2*(54*41+37*54)=8424 scalar entries.

Their kernel must agree with the compressed Delta kernel under the
recorded isotypic maps. This is a comparison of exactly the same tensors
and variables, not an independent selected source model. It can detect
an omitted Hom channel or an incorrect compression basis.

The simultaneous identity triple must lie in ker Delta. In characteristic
zero its trace vector is (41,54,37), so it must not lie in ker Delta_tr.
Every delivered kernel basis must be checked directly against all four
uncompressed intertwining equations and, for Delta_tr, all three ordinary
trace equations. Independence requires an exact certificate.

## What constitutes a rank certificate

For a claimed exact rank r, provide both a nonzero r-by-r minor or an
equivalent exact pivot certificate and a complete exact kernel of
dimension 113-r. Check every kernel vector and its independence. A rank
obtained only by floating-point tolerance is not a certificate.

One-sided rejection can stop earlier:

| Gate | Contradicting lower bound | Contradicting kernel witness |
| --- | --- | --- |
| Delta | rank at least 110 | six independent commuting triples |
| Delta_tr | rank at least 112 | three independent trace-zero commuting triples |

A modular nonzero minor may certify a characteristic-zero lower bound
only after the entire authenticated characteristic-zero matrix and its
coordinate spaces have been fixed. Record an integral localization/order,
a residue homomorphism, and proof that every used denominator maps to a
unit. A nonzero reduced determinant then implies its original determinant
is nonzero. Do not rebuild the commutant using a possibly different
modular representation decomposition or use modular nullity as a
characteristic-zero upper bound. A vanishing reduced minor, a rank drop,
or several unsuccessful primes proves no upper bound.

Actual computation limits are to be frozen with the authorized evaluation
plan before running; this preparation does not select a machine budget,
prime, endpoint, tensor coefficient, or parameter. A limit or failed check
produces an inconclusive result, not an inferred rank or zero tensor.

## Result classification and acceptance

- **Preparation only / missing source:** the actual tensor package is
  absent or its simultaneous identification is unverified. No actual rank
  or source exclusion is reported.
- **Inconclusive:** provenance is incomplete, an exact identity fails,
  the replay disagrees, or the available rank bounds do not decide the
  relevant necessary condition. Preserve the failed check and artifacts.
- **Certified incompatible with source2:** an authenticated actual package
  and exact certificate violate rank Delta in {108,109} or
  rank Delta_tr=111. State the precise violated condition and the pinned
  actual-source hypotheses on which the implication depends. This alone
  addresses source2, not other labels or the original algebraicity goal.
- **Necessary linear tests passed:** exact ranks satisfy both conditions.
  No actual realization follows. Even with these ranks, the trace-zero
  kernel of an arbitrary pencil cannot be called its radical without
  further algebraic proof. Later checks may test its ideal and square-zero
  properties, full algebra type, and PR792-795 image/core constraints.

Acceptance of a future actual result requires exact source pins, the
simultaneous tensor identification, reproducible gate construction,
independent checking of the claimed certificate, and a conclusion limited
to what that certificate proves. The present slice meets none of those
actual-evaluation prerequisites. No authenticated actual tensor package
has yet been supplied in this slice.
