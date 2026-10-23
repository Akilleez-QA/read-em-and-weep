# Independent review of the represented source126 radical

23 October 2026. PASS for the stated conditional necessary fingerprint.
This review supports the new deduction; it is not a source exclusion or a
new proof of the complete HM repair. No actual HM coefficient, point,
matrix, derivative or instance rank was selected or evaluated.

## Reviewed immutable bytes and sources

- PROOF.md SHA256: 29136be19fb0740b34fd4ffb6f2146b998fcb92f35f3efad8b2afc3e796729d3
- verify.py SHA256: 98914b6a6fe05f26c9f06691aa2ef5b37792a688a3bcdddcc4beb71fdedc1267

I read the complete new proof and program and the relevant exact source
proofs. Independently fetched all four published source files at their pinned
commits, then recomputed the local Git blob hashes. All four matched:

- PR856: 8a5522965ac861b5c4e149724782a489c5afb7cd
- PR858: 54207bb4a1d2ff7cce3ce365f81bb5b146a61c81
- PR862: e18035dcceb1c7e0d0d4356ee578937d3172390b
- PR869: 050610e5144820c5e323e092dcc7c8417fb52828

This authenticates the exact inputs and verifies the new deduction from
them, not their entire geometric ancestry.

## Independent algebra

Multiplicity one gives four scalar channels on Hbar to C, with block
dimensions 3,3,4,5. The nonzero P-to-X and V-to-Y restrictions allow the two
independent equations to be solved for the P and V channels. With free A,D
coordinates x,y, their solutions are -gamma y and -alpha x-beta y. Thus
R1 describes the complete two-plane, not merely some nilpotent subspace.
The represented map on H=C direct-sum Hbar has only this off-diagonal block,
so its rank is the sum of dimensions of precisely its nonzero channels.
This independently establishes R2.

For a generic projective direction x and y are both nonzero. The V channel
is generically present exactly when alpha or beta is nonzero, and the P
channel exactly when gamma is nonzero. This proves R3 and the four generic
ranks 8,11,12,15. At y=0 the rank is 3 or6; at x=0 it is
5+3[beta nonzero]+4[gamma nonzero]. A third distinct direction exists exactly
when alpha and beta are both nonzero. Only the V channel disappears there,
so its drop is exactly3. These exhaust all zeros of all four linear channel
forms. No algebraic relation between nonzero alpha and beta creates another
exceptional direction. Type I forces gamma=0 and Type III forces beta=0
by the constant spans in the pinned input, so the stated type restrictions
are correct. No converse or realizability of every coupling stratum is used.

A generic element has every channel that is ever supported nonzero at once:
a finite union of proper lines cannot cover a two-space over C. Its image
is therefore the sum of all radical images and its kernel is their common
kernel. The latter contains the whole fifteen-space C and precisely the
unsupported summands of Hbar. This proves both dimensions in R4 without
assuming the same property for arbitrary square-zero subspaces.

Square-zero on the thirty-space makes the Jordan blocks have size at most
two. Each size-two block contributes exactly one to rank; hence there are
r such blocks and 30-2r size-one blocks. The four displayed generic partitions
follow. These are ranks on the reconstructed H, not on one of the individual
pencil spaces, and no full-module extension is inferred.

## Tests and limitations

I reran the final program in normal and optimized Python. Both passed all
eight formal zero/nonzero support strata and the separate sparse square-zero
negative control. The control has a two-dimensional independent square-zero
space whose generic rank is1 but common-kernel codimension2, correctly
refuting both overgeneralizations. Nonzero couplings remain formal symbols;
no geometric or actual-HM parameters are substituted. Explicit exceptions,
not Python assert statements, retain the tests in optimized mode.

The program corroborates polynomial support arithmetic and block dimensions.
It does not verify the previous geometric inputs, authenticate an actual
commutant, or establish a real source elimination. The all-zero coupling
stratum, like the other strata, is a necessary overlist entry, not an asserted
balanced or actual-HM realization. PR869's nonempty abstract families are
left intact and source126's four historical pairs remain retained.

No mathematical blocker was found in the reviewed proof or its scoped tests.

## Final source-integrity amendment

The final verifier authenticates all four vendored sources against their SHA256 and Git blob SHA1 identities before the formal tests. All four blob identities were checked against the independently fetched immutable remote sources listed above. The final INPUTS.json correctly separates initial cached-byte mismatches from the corrected current-byte matches. Both normal and Python -O execution pass with identical output. In an isolated temporary copy, appending a newline to separation856.md was rejected with a source SHA256 mismatch in both execution modes. Proof bytes are unchanged. The verifier hash above identifies this final reviewed version.
