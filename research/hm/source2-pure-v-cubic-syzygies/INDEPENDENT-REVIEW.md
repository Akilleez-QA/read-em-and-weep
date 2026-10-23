# Independent cubic-syzygy and Hilbert-Burch review

Result: PASS. No mathematical blocker found.

Read the final proof, complete S.json matrix, checker, fixed model and
immutable dependencies. Independently ran normal and optimized verification:
all 32 checks pass, outputs are byte-identical, and both match RESULT.json.
All final hashes match the author's freeze.

## Exactness, minimality and saturation

The certificate concerns the actual normalized universal row N L (R1-2R2).
Every cubic matrix entry is retained in S.json. The independently replayed
checks establish the whole syzygy identity and all four signed maximal-minor
identities with the SAME nonzero factor 9sqrt(5)/2050. Thus the maximal-minor
ideal equals the component ideal algebraically, not only after taking a
radical or sheafifying.

The previously proved nonempty finite projective base scheme gives height
two: there is no common curve divisor, while its affine cone has dimension
one. Hilbert-Burch therefore applies and proves exactness over the graded
polynomial ring. All cubic matrix entries have positive degree; hence the
resolution is minimal. An explicit sentence to this effect was added
during review, without changing the calculation.

The resulting quotient has depth one at the homogeneous maximal ideal,
so its irrelevant-torsion submodule vanishes. This proves saturation.
It is not an assumption that every homogeneous finite base ideal is
saturated. Sheafification and twist by nine then give K_F=O(-3)^3.
The Hilbert numerator and length 54 agree with the independent old scheme
length, but are not used to infer splitting from Chern classes.

## Representation identification

The 91-by-40 coefficient system is exact over Q(sqrt(5)); its rank is 37,
and the three coefficient columns of S are independent and exhaust the
cubic syzygy space. Equivariance of the underlying universal row makes this
space stable under the full group. Its central action is trivial, so it
is an A5 representation. By characteristic-zero semisimplicity and the
irreducible dimensions 1,3,3,4,5, the ONLY dimension-three possibilities
are A, V, or three trivial representations. There is no omitted reducible
one-plus-two case.

The specified element is a pinned binary group generator, not an arbitrary
SL2 matrix with a convenient trace. Its determinant, fifth power and Pi
intertwiner are checked in the retained basis. The verifier transforms all
forty coefficient coordinates of each syzygy, solves the change of basis,
and verifies the complete coefficient action identity. Its trace agrees
with A and differs from V and the three-trivial possibility. This suffices
to identify the FULL stable representation as A; it is not a trace-only
assumption of irreducibility or a pointwise evaluation. The evaluation
isomorphism U tensor O(-3)->K_F is therefore equivariant.

## Original-fourth consequence and boundaries

Substitution into the authenticated kernel bridge gives the modification
of A O(-2) by the length-ten C_L, with the inherited R^2 plus m local type
and nonsplit Koszul extension. The Chern substitutions for b=54 give
27,22,46 for K_F,E,K_H respectively. They do not show K_H splits.
The theorem is conditional on a nonzero gate on ell3 and selects no actual
gate coefficient or source occurrence. It does not address specialized
additional A-kernel classes.

## Provenance

Fresh direct GitHub reads in this task authenticated:

- PR1049, commit 6210a276622e15c6977b8070bc1fd12744fe2f07,
  blob 88e8f27f6a783bbb6d77a07bb4db88b820e80149.
- Group/intertwiner source, commit 6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0,
  blob 0ff4a2fd717842d8df9cf3ce3e3d29fd189bcd6e.

The PR1036 proof/model and PR1037 proof were freshly authenticated earlier
in this same review session; their blobs are respectively
718f987511b5bf6144a85fc14e8ef343612a4491,
a7ca4755e50c85fe7fc20a757125127a05de4056, and
7fdcab9202a78e9f371c32903840969e0453c7b5.
All retained bytes match the manifest. Exact paths and URLs are in
INPUTS.json. The historical group-source executable was not run.

## Frozen hashes

SHA256:

- PROOF.md: 144ebd2b790202093b5a9d4989199e545afb3da8433a9b5bddae9e58c4f19258
- verify.py: cfa6fcdd03d4509e152893cf4a4979e3b456fa5f5fb6d27afef4988635bcfea6
- S.json: 4e136d308702a65ee9a35f5c0b44aa5eb4f8fc9786f19467181df7aa19024ea8
- INPUTS.json: ce9b160b6d9156fdee191ce1208a91a19663a0dadee98eeffbd043cedae96d4e
- RESULT.json: b5e710a6c283a4a9a289475166c3eed452dd4d50ba276a9dc15163e623461549

No actual HM coefficient, selected direction, orbit root or source-instance
rank was evaluated. No public files were changed.
