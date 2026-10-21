# Independent mathematical review

Verdict: **PASS**, conditional on the stated pinned dependencies.

Reviewed artifact: `PROOF.md`.

Reviewed SHA-256: `f3638dace39595d9e5f2aea7b006bc0640637997314d589b33b11fa7c9f32209`.

Review date: 2026-10-21 (UTC).

## Evidence and scope

I read the entire proposed proof and the local proof artifacts for PR627 (pinned commit `7c3f76f2e55c5cc0c3356972b5d7d676544c943a`) and PR628 (pinned commit `f08ff9c2760e4aef074cfe716b923d29d5e7ebe8`). The present review checks the new deduction from their stated results; it does not independently reprove the earlier HM geometry or certify remote repository commit identity from these local copies. The statements of [Stacks 07QZ](https://stacks.math.columbia.edu/tag/07QZ), [07QY](https://stacks.math.columbia.edu/tag/07QY), and [00IP](https://stacks.math.columbia.edu/tag/00IP) were checked directly against the cited pages.

## Independent verification

### 1. High-power embedding and finite-dimensional parameter space

PR628 supplies an effective projective flat finitely presented family with an ample invertible sheaf over the Noetherian affine base C[[t]]. Taking a sufficiently large power gives one closed projective-space embedding of the whole family, so its Hilbert-scheme parameter space has fixed finite dimension of ambient projective space. This does not require extending the original degree-one sections. The classifying map lands in the Hilbert scheme with the special fiber's Hilbert polynomial, by flatness. An affine open containing its closed-point image contains the entire image: an open subset of the spectrum of a local ring containing its closed point is the whole spectrum.

### 2. Approximation is of exactly the required kind

The affine chart has a finite polynomial presentation over C. The ring C[t]_(t) satisfies the Noetherian G-ring hypothesis of 07QZ. That theorem yields an étale algebra and a chosen point with unchanged residue field, together with a polynomial solution agreeing to the requested order. Étaleness and the unchanged residue field identify the completed local ring at this point with C[[t]] as an algebra over C[t]_(t). Consequently the agreement is modulo the same t^N, not modulo a reparametrized variable. The alternate henselian explanation is also valid, since finitely many elements and equations descend through a filtered colimit.

Spreading out the finite presentation, the solution, its equations, and étaleness requires only finitely many denominators not vanishing at zero. Thus an affine finite-type scheme étale over an open subset of A1 exists, retaining the selected C-point and the prescribed local solution. Its component containing that point is open and closed. A smooth connected Noetherian curve over C is integral because regular local rings are domains, so its finitely many irreducible components cannot intersect. Restricting to this component preserves every required property.

At the selected point, t is a uniformizer and C[t]/(t^N) maps isomorphically onto the local quotient. Equality of the two Hilbert morphisms over that quotient gives equality of the universal embedded-family pullbacks up to the canonical identifications. Transporting the original special-fiber marking through these identifications supplies exactly the asserted marked abstract jet. No descent of the original invertible sheaf itself is required.

### 3. Rigidity at every positive Artin order

Since N is at least two, the newly constructed family has the original first-order class v. Any fixed-base automorphism at any positive order restricts to an automorphism of V fixing v. Its special-fiber restriction is therefore identity by the defining free-stabilizer condition. For each successive small extension, the kernel of restriction consists of derivations into the square-zero ideal. Flatness identifies that ideal with a copy of O_V tensored with the one-dimensional base ideal; derivations factor through the special fiber because the maximal ideal annihilates it. The kernel is therefore H0(Theta_V) tensored with that ideal and vanishes. Induction applies to arbitrary higher jets of this new family, including orders beyond the finite matching range. No assertion of surjectivity of automorphism restriction is used.

### 4. Local algebraic and global relative automorphisms

Over the local DVR D, the equalizer of an automorphism with the identity is closed by separatedness and has coherent ideal by Noetherianity. Triviality on all Artin reductions puts its ideal stalks inside every power of t at points of the closed fiber. Krull intersection applies there because t belongs to the maximal ideal. Thus the coherent ideal's closed support misses the closed fiber. Properness of the family makes its image in Spec D closed, and any nonempty closed subset of Spec D contains the closed point. This forces the support to be empty. This argument does not require D to be complete.

A global B-automorphism is then identity on the generic fiber, by restriction to D. Flatness over an integral B makes each affine coordinate algebra torsion-free over the corresponding affine base domain. Its map to its generic localization is injective. The equalizer ideal vanishes after generic localization and hence vanishes already. Thus the global automorphism is identity, with no unjustified analytic continuation or extension-of-generic-automorphisms step.

## Boundaries and result

All four theorem assertions follow. The construction may depend on N; it realizes finite jets and does not algebraize the entire original formal arc. The proof establishes fixed-base automorphism triviality of Artin reductions, the local family, and the whole chosen curve family. It does not establish triviality of generic or geometric generic automorphism groups. It requires no descent of the original line bundle or original P9 embedding, and makes no selected HM source evaluation or original Weil-class/full-adjoint algebraicity claim.

The final clarification that the Hilbert construction retains the high-power polarization on the matched jet but does not descend the original line bundle L was also checked and is correct. No correction is required for the reviewed version. This is an independent mathematical review, not proof-assistant certification.
