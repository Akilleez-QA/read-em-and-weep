# Independent entire-proof frozen review

## Verdict and exact binding

**ACCEPT.** This is a new independent review of the entire frozen proof, all
three complete direct originals, the entire checker, source documentation,
provenance, and freeze. No mathematical gap or required correction was found.
Acceptance is conditional on exactly the hypotheses retained by the proof; it
does not turn inherited actual-geometric assumptions into new existence
claims. This review does not authorize publication by the reviewer. The
parent's review/publication decision remains separate.

Reviewed packet:
`/workspace/shared/rankfour-profile11-triplet-original-second-kernel-derivative`.

The acceptance binds exactly:

- `PROOF.md`: 11,709 UTF-8 bytes; SHA256
  `a11b3386584390375a6a3249898170a2240d614d4f067e824ddf12aa0c3d6e6f`.
- `verify.py`: 10,710 UTF-8 bytes; SHA256
  `da356825cf67bc0828c76327e5abd2373970e5239ac8325bf3ecc210a6d5dcf7`.
- Nine-file core SHA256:
  `7fb3a09266e24f6335e724e7fc439d863f23dea8c985316735ef0ec37d069d33`.
- `FROZEN.json` SHA256:
  `ef42cb4768e49e6fcf184f6804d949b7f693335f555d341037619e3c7f0945a4`.

The aggregate is SHA256 of the concatenation in sorted relative-path order
of `<file SHA256>  <relative path>\n`. The freeze itself is not in that
aggregate. All nine entries, their lengths, their hashes, the aggregate,
and the standalone freeze hash were recomputed independently before replay.
The original selected core and freeze were unchanged afterward. This is
not acceptance of an unfrozen draft or a subsequently edited proof.

## 1. Scope, independence, and complete reading

The exact retained branch is full-positive triplet, original t=0, original
local delta=12, residual simultaneous rank-seven k=2, original K=K1, and
all complete transitive actual-geometric assumptions of the three direct
originals. In particular, the original local delta and the newly determined
second-kernel derivative defect are not silently identified as the same
geometric construction merely because both have value twelve.

I read the complete final `PROOF.md`, complete `verify.py`, `README.md`,
`INPUTS.json`, `INPUTS.md`, `PROVENANCE.md`, and `FROZEN.json`, then read
each of the three complete retained originals. I also read the complete
unselected draft, self-check, author verification, and author map audit.
Those author-side records are not substitutes for the independent map
review below. The fresh source responses in this review were obtained by
this reviewer, rather than copied from the author's evidence.

Exactly the three requested direct originals were authenticated afresh.
Their transitive sources were not recursively refetched, and their
retained actual-geometric premises remain premises. Each direct original
was reviewed as a whole, including its sections not needed for the new
lemma. The bounded checker is not treated as a theorem prover.

No source packet file was edited, no GitHub write was made, no local Codex
work was used, and no publication, merge, or upstream submission occurred.

## 2. Fresh independent complete source authentication

For each source, I made a complete exact-commit
`mcp__codex_apps__github_fetch_file` request with `encoding: base64` and no
line bounds, and a separate `mcp__codex_apps__github_fetch_blob` request
for that path response's Git blob identity. Both responses are retained
in full with request arguments and independent UTC intervals under
`source-responses/`. The path base64 was decoded without newline or text
normalization. The complete blob text was encoded as strict UTF-8.
These complete byte strings were compared to one another and to the
complete retained original. SHA256 and SHA1 of the exact Git blob header
plus unchanged bytes were independently recomputed.

All three complete byte comparisons, all three expected lengths and
SHA256 values, and all three recomputed Git blob identities passed:

### PR1228

- Repository: `Akilleez-QA/read-em-and-weep`.
- Commit: `d3c9e9ff8d06977e6c3d3be6cd1c9ed71007a593`.
- Path: `research/hm/rankfour-profile11-triplet-first-kernel-structure/PROOF.md`.
- Complete bytes: 12,921.
- SHA256: `4869bca9584bfa6876533516b61a6a14d6ca0fde97e80649828588b28e8f617e`.
- Git blob: `41ab2148d3ea13d07dcdfe2bf353a18c664bb848`.
- Path read UTC: 2026-10-24T13:45:25.417Z to 13:45:25.750Z.
- Blob read UTC: 2026-10-24T13:45:31.978Z to 13:45:32.355Z.
- [Immutable complete original](https://github.com/Akilleez-QA/read-em-and-weep/blob/d3c9e9ff8d06977e6c3d3be6cd1c9ed71007a593/research/hm/rankfour-profile11-triplet-first-kernel-structure/PROOF.md).

### PR1234

- Commit: `3d55622ece9a4bb9e20197dec560b298f1d03fb1`.
- Path: `research/hm/rankfour-profile11-triplet-simultaneous-kernel-three-exclusion/PROOF.md`.
- Complete bytes: 16,183.
- SHA256: `9a164b510ccb9c529d2380c7e9e4880067bde0e86656b82e2c4649e09e5443c2`.
- Git blob: `c57074c1fbfaa61ef452a6d5e3a77dd0ff4ea70b`.
- Path read UTC: 2026-10-24T13:45:25.750Z to 13:45:26.033Z.
- Blob read UTC: 2026-10-24T13:45:32.355Z to 13:45:32.675Z.
- [Immutable complete original](https://github.com/Akilleez-QA/read-em-and-weep/blob/3d55622ece9a4bb9e20197dec560b298f1d03fb1/research/hm/rankfour-profile11-triplet-simultaneous-kernel-three-exclusion/PROOF.md).

### PR1236

- Commit: `092fc5f31dfaa5553ee5ea687f175ecba1878a2a`.
- Path: `research/hm/rankfour-profile11-triplet-first-kernel-forward-closure/PROOF.md`.
- Complete bytes: 18,052.
- SHA256: `90081703a5e2a988a29e4d5bb918a93df4d4a954221a9bcba4cd858b0fa28137`.
- Git blob: `f77cfb52743be86e46e0c40570ec036e69aebaf3`.
- Path read UTC: 2026-10-24T13:45:26.033Z to 13:45:26.360Z.
- Blob read UTC: 2026-10-24T13:45:32.676Z to 13:45:33.137Z.
- [Immutable complete original](https://github.com/Akilleez-QA/read-em-and-weep/blob/092fc5f31dfaa5553ee5ea687f175ecba1878a2a/research/hm/rankfour-profile11-triplet-first-kernel-forward-closure/PROOF.md).

`REVIEWER-SOURCE-AUTHENTICATION.json` records all exact requests, intervals,
URLs, checks, lengths, content hashes, path-returned blob hashes, recomputed
blob hashes, and hashes of the six complete raw response envelopes. The
blob API response exposes complete text, not a second independent SHA
field; the review therefore correctly computes the Git object identity
from those returned bytes rather than claiming an absent response field.

## 3. Section-by-section review of the new frozen proof

### Statement and conditional scope: accepted

The object differentiated is the actual original `Fhat=K^-` in the
constant twenty-one-space C. Its algebraic type may be transported from
the projected F by the retained actual constant restriction. Its normal
derivative may not be transported that way, and the proof explicitly does
not do so. The target rank-three original image is not confused with the
rank-two small projected image `O(10)+O(-10)`.

The asserted conclusions are mutually compatible: rank Fhat=10 and rank
Chat=7 produce generic image rank three; their degree difference is -12;
the image type `W(-1)+O(-10)` has that rank and degree; its degree-zero
saturation therefore permits a length-twelve torsion quotient. This
arithmetic is only a consistency check, not the proof of the maps.

### Section 1, complete originals and actual data: accepted

The cited data really occur in the complete sources under the same branch.
PR1228 provides the exact small bundle type and physical W-adjacency.
PR1234 Sections 1-4 supply the original actual lift, exact original kernel
`Bhat^-=Chat`, coherent saturated original derivative image W(-1), and
actual `R11=Bhat^+` inside K. Crucially, PR1234 Section 4 proves the
nonzero actual row `R11/Bhat -> K/Fhat`, identifies it with the saturated
Euler inclusion, and proves `R11 intersect Fhat=Bhat`. It is not merely an
abstract occurrence of a W(1) summand.

The beta_K isomorphism `K/Fhat=A(2)` is an algebraic identification of an
actual quotient. No derivative of that identification is needed. PR1236
Section 1 explicitly retains `K^+=E0` and `span_C(E0)=C`. A constant span
contains the derivatives and their saturation, so these facts legitimately
give `span_C(K)=C`.

The universal invariant facts also appear in PR1236 Section 1: a nonzero
degree-twelve invariant, its one-dimensional invariant line, and the
minimum orbit size imply a reduced orbit divisor. Absence of nontrivial
scalar characters prevents an unrecorded character twist of the scalar
line. No G7/H5 lemma is required or introduced.

### Section 2, actual Euler plane in the coherent image: accepted

For a local section s of Fhat, the equality Fhat=ker beta_K implies
`ds in K tensor Omega`. Therefore beta_Fhat is a regular O-linear map
to `(K/Fhat)(-2)`, and that subbundle of its full normal target is
saturated because the quotient `(C O/K)(-2)` is locally free.

On Bhat, the relevant derivative is obtained by the natural projection
of the original beta_Bhat. Its full coherent image before projection is
`(R11/Bhat)(-2)`. The actual intersection and saturated Euler inclusion
from PR1234 ensure that this projection is fiberwise injective with
locally free cokernel. Thus no hidden divisor appears when W(-1) is
projected into the normal bundle of Fhat. In particular the kernel on
Bhat remains Chat, not a potentially larger sheaf inferred from types.

The preimage of the Euler plane under beta_K is R11+Fhat, and the actual
quotient K/(R11+Fhat)=O(4). Twisting by Omega gives the exact actual
normal sequence `0 -> E=W(-1) -> A O -> O(2) -> 0`. Because the entire
E is in the coherent image, the quotient row is genuinely induced from
`Fhat/Bhat=O(-10)`. The argument differentiates no quotient and equips
no quotient with a connection.

### Section 3, nonzero scalar row: accepted

Suppose the actual quotient row phi vanished. The original derivative
would then take all of Fhat into the actual E. The ordinary extension
group for `0 -> Bhat -> Fhat -> O(-10) -> 0` is
`(D+P) tensor H1(O(4))=0`. Averaging a regular algebraic splitting over
the finite group preserves the splitting identity and produces an
equivariant splitting. Its line L_F is an actual embedded direct summand
of Fhat. It is neither selected by actual coefficient evaluation nor
identified with the auxiliary Zhat0 in the D-top.

The first Hom obstruction has target-source twist nine:
`Hom_G(O(-10),W(-1))=(W tensor H9)^G=0` because H9=S4+T6.
It forces beta_Fhat to kill this actual L_F. Consequently derivatives
of local sections of L_F lie in Fhat, so their own normal derivative in
C/L_F factors regularly through `(Fhat/L_F)(-2)=(D+P)(-8)`.
The second obstruction has twist two and is
`((D+P) tensor H2)^G=0`, since H2=A. It forces the actual normal
derivative of L_F itself to vanish.

This is a two-stage use of natural normal quotients. Vanishing of the
first map alone would not make L_F horizontal, and the proof correctly
includes the second stage. L_F is saturated in Fhat, Fhat is saturated
in K, and K is saturated in the original constant bundle. Its resulting
horizontal Grassmannian map is constant in characteristic zero, which
forces degree zero and contradicts degree -10. The splitting was never
assumed horizontal; horizontality was derived only under the contradictory
assumption phi=0.

Thus phi is nonzero and adds a third generic direction beyond E. As an
equivariant `O(-10)->O(2)` map, it is an invariant degree-twelve section.
The invariant space is one-dimensional. Its divisor has degree twelve,
and each nonempty invariant orbit has at least twelve points, so it is a
single reduced orbit. No actual scalar, orbit representative, coefficient,
or value is selected.

### Section 4, image, kernel, local defect, and span: accepted

Let I be the coherent image. Because E is already its entire subbundle,
the kernel of `I -> O(2)` is exactly E and the image is im phi. A nonzero
map between line bundles on the integral curve is injective as a sheaf,
even though its fiber map vanishes along its divisor. Thus im phi is
abstractly O(-10), not O(2). This distinction is essential and is made
correctly. The exact sequence for I splits ordinarily because
`Ext1(O(-10),W(-1))=W tensor H1(O(9))=0`; finite-group averaging gives
an equivariant splitting used only for the isomorphism type. Accordingly
`I=W(-1)+O(-10)` as claimed.

I has full generic rank in the actual saturated A O. Its saturation
there, and therefore in the full normal bundle, is all A O. The exact
quotient is `O(2)/phi(O(-10))`, not merely an arbitrary torsion sheaf of
degree twelve. Locally it has one generator and one equation with a
simple zero at each point of D12. Therefore it is locally cyclic and
reduced, with length one at every one of the twelve points. The proof
does not try to extract this local statement from degree arithmetic alone.

For the backward kernel, a local section killed by beta_Fhat has a class
in Fhat/Bhat killed by the sheaf-injective phi, hence lies in Bhat. The
already established exact kernel on Bhat is Chat. This proves the actual
embedded equality `Fhat^-=Chat=Bhat^-`, not only equality of types or
generic fibers. A torsion cokernel at D12 does not invalidate this
sheaf-kernel argument.

The full saturated image `(K/Fhat)(-2)` makes the saturated forward
span exactly K. Constant spans are unchanged under an actual forward
transform: a constant space containing Fhat contains its derivatives,
their generic span, and its saturation. The reverse containment follows
from Fhat being contained in its forward span. Combining with the actual
`K^+=E0` and `span_C(E0)=C` gives the claimed twenty-one-dimensional
span of Fhat without transferring the span of projected F or Bhat.

All stated numerical identities are correct: ranks 10-7=3;
degrees -64-(-52)=-12; degree K/Fhat=-58+64=6; twisting a rank-three
quotient by O(-2) gives degree zero; and defect length is twelve.

### Section 5, contribution and restrictions: accepted

The new information is the actual original derivative of the second
kernel, its coherent versus saturated image, exact backward kernel,
full forward span, and reduced cyclic defect. The proof does not exclude
K1, prove that K1 occurs, close another branch, match higher jets, or
prove algebraicity. Its statement remains a necessary differential
compatibility within the explicitly retained branch. Its restrictions
agree with the mathematics and with the performed review work.

### Section 6, bounded character derivation: accepted

The listed nine-irreducible W-adjacency agrees with the direct original.
The recurrence H(n+1)=W tensor Hn-H(n-1), starting from H0=1,H1=W,
is the determinant-one symmetric-power recurrence. Through degree twelve
it gives H2=A, H9=S4+T6, and H12=1+A+D+P. These imply precisely the
two Hom vanishings and the invariant line used in Section 3. The Ext
computations use only H1(O(4)) and H1(O(9)), both zero on P1. No
universal calculation is mistaken for an actual-map saturation check.

## 4. Complete direct-original mathematical review

The following records the whole-source reading, not just a check of
extracted assertions. Acceptance of a source's use is conditional on its
explicit retained transitive actual-geometric premises.

### PR1228: all sections reviewed

- Scope and statement correctly distinguish the original K^- from
  projected F and its small-ambient backward kernel. Its conditional
  branch matches this packet. The imported coherent image of beta_F is
  explicitly a retained premise, not a new consequence of its splitting.
- Section 1: the obstruction to extending the actual fifth-jet inclusion
  is the indicated D-to-R Hom, which vanishes. The difference of two
  ambient extensions factors through positive O(2), so is zero in the
  constant bundle. This proves the actual complement, rather than
  assuming one is horizontal. The nonzero quadratic line has its stated
  saturated Euler quotients, and surjectivity produces the exact sequence
  for the actual kernel and N.
- Section 2: the proposed rank-two W' kernel cannot have rank one by the
  low-degree W' Hom vanishings. Its degree-six minors cannot have a
  nonempty invariant divisor. The induced endpoint maps and Euler
  sequences give the stated B_V and B_P. The extension of B_P by B_V
  has just the displayed one-dimensional component; the O(-10)
  components vanish. This gives the two necessary types of N without
  evaluating an actual extension scalar.
- Section 3: all degree differences used to split the extension by
  D(-6) are at least -1. In the unwanted type, the canonical W'(-5)
  is killed by both coherent derivative rows. Its own derivative then
  factors into a strictly lower-degree quotient, forcing an actual
  negative horizontal subbundle. This validly excludes that type. The
  actual jet D-block identification follows from the inequivalent
  same-degree blocks and the absence of maps to the lower line.
- Section 4: surjectivity onto the coherent image makes the lower
  scalar row an isomorphism and makes the upper B row onto. The actual
  f12-divisible D row and P row are kept distinct. A common divisor of
  the P row would allow division by f12 and violate the degree-four P
  Hom, so that row is onto. The Q sequence is therefore exact. The
  section arguments at twists six, seven, and eight are sound: the
  distinct irreducible rows at six inject; at seven an entire T6 kernel
  is too large for a rank-four bundle with top at most -7; at eight
  the forced V_alt is the only possible kernel module within the
  rank-four bound. Degree then gives the remaining O(-12) line.
  Ext vanishing lifts this type to the stated small F^-.
- Section 5 correctly rejects an unwarranted internal projection of
  derivatives onto F/B and preserves the open K1 compatibility question.
- The universal audit agrees with the fixed adjacency and the displayed
  symmetric-power recurrence. None of the source's projected derivative
  conclusions is imported as an original-ambient derivative in the new
  proof.

### PR1234: all sections reviewed

- Scope and Section 1 retain exactly the stated residual branch, actual
  constant projection, saturated K and E0, everywhere-onto beta_K, and
  actual small top/derivative data. They do not assert K1 realization.
- Section 2 lifts B and Csmall by an algebraic inverse only. The actual
  preimage in K is Bhat direct-sum H. The residual derivative map to
  H(-2) is O-linear and zero by degree. Constant projection proves the
  converse kernel inclusion, giving the exact Bhat^-=Chat needed here.
- Section 3 compares coherent images through the constant projection,
  using the already established exact kernels. The quotient by the
  lifted image is an extension of locally free sheaves, establishing
  saturation in the full normal bundle. The actual R and its projected
  isomorphism follow from exact sequences, not type matching.
- Section 4 proves the actual Euler row is nonzero by ranks eleven
  and ten. Its one-dimensional Hom has a saturated Euler generator.
  Therefore its nonzero member is saturated, its kernel on R is Bhat,
  and R intersect K^-=Bhat. The two O(4) quotient maps are explicitly
  not assumed to have the same kernel. This is the decisive valid
  original-map input for the new proof's Section 2.
- Section 5: unequal splitting degrees in the rank-two quotient are
  constrained by parity and low-degree scalar-invariant vanishings.
  The only unequal type is O(-10)+O(4); the equal type is W'(-3),
  identified by its section injection into H7. No extension class is
  selected.
- Section 6: the actual derivative of N produces a regular section of
  its normal extension through an algebraic inverse that is never
  differentiated. It would give the forbidden quotient E0->O(-10).
  Ordinary degree rules it out. This is a valid actual extension
  obstruction, not an assumed splitting of a quotient connection.
- Section 7: the canonical D(-4) of K3 cannot map to W'(-3), so lies
  in R. Its possible row to W(1) is the universal quartic-evaluation
  row. If zero, all D(-4) lies in Bhat; if nonzero, S4(-5) lies there.
  Both conflict with the degree-minus-six top of Bhat. This excludes
  only the stated K3 case and does not exclude K1.
- Section 8 accurately states the bounded universal identities,
  limitations, and remaining K1 case. The complete source does not
  supply an unauthorized later G7/H5 premise.

### PR1236: all sections reviewed

- Statement and Section 1 distinguish the original twenty-one-space
  from the actual eighteen-dimensional S and retain all needed actual
  annihilator and dual-curve hypotheses. The degree-twelve divisor is
  justified from the fixed action and invariant line, without evaluating
  an actual point. K^+=E0 and span_C(E0)=C are explicit retained data.
- Section 2 uses actual annihilator transposition to identify E19 and
  obtain its everywhere-onto normal derivative. The rank-seventeen
  backward kernel and inclusion of E0 follow.
- Section 3 constructs each next forward image as an actual saturated
  graph over a nonzero Euler inclusion. Locally free cokernels justify
  saturation and the stated intersections with K and E0. This is not
  a transfer of a projected normal derivative.
- Section 4: the quotient Q is embedded by actual constant projection
  into V_alt. A rank-one image is excluded by its low-degree W' Hom;
  degree-six minors exclude a common invariant divisor. Its nonzero
  actual derivative is onto by degree-seven common-divisor bounds. Local
  lifts of sections of Q show that E0 projects onto the full constant
  triple. Rank, degree, and saturation give the actual intersection
  with S. The O(8)+V_alt normal type is obtained from a legitimate
  ordinary Ext vanishing, not a horizontal splitting.
- Section 5: the O(8) row vanishes by the Hom calculation. The O(16)
  row must be nonzero by the rank of the intersection with the actual
  E19 backward kernel. Its one-dimensional Hom is generated by the
  degree-twelve invariant gradient, whose entries have no common zero
  because the invariant divisor is reduced. The exact O(-6) kernel
  has the correct degree.
- Section 6 isolates the possible internal scalar row on that kernel;
  the V_alt component vanishes. It correctly leaves the f12 row
  potentially zero until the following actual-map argument.
- Section 7: under the zero-row assumption, the saturated graph gives
  N of rank sixteen and degree -18. The projected original degree-ten
  curve remains nonzero, basepoint-free, and nonconstant using its
  retained A coefficient component and minimum orbit size. First jets
  lie in ann(N); their equal rank and degree give a genuine saturated
  isomorphism, not assumed projected unramifiedness. Actual transposition
  then confines beta_N to O(6), while its quotient source is O(18).
  The resulting negative-horizontal contradiction is valid.
- Section 8: retaining the nonzero internal row gives generic rank two
  with coherent image W(5). Saturation has the stated extension by
  O(6), split equivariantly by the degree-eight invariant vanishing.
  The everywhere-onto projected row makes one local invariant factor
  a unit, while the determinant f12 gives the other simple factor.
  The reduced cyclic local defect is therefore proved, not merely
  inferred from the length.
- Section 9 identifies the rank-seventeen forward span with the actual
  projected degree-ten annihilator by saturation, rank, and degree.
  Its remaining scalar derivative row must be nonzero, so its next
  forward span is the actual constant S.
- Section 10 accurately limits the source's conclusion to its forward
  flag and preserves K1, other branches, and algebraicity questions.
  The new proof requires only its Section 1 span/invariant data, not
  its later forward-flag construction as a hidden dependency.

## 5. Documentation, freeze, and checker audit

README, INPUTS, and PROVENANCE consistently name exactly three direct
originals and the exact final core. README correctly distinguishes the
projected and original derivatives, L_F and Zhat0, coherent image and
saturation, and conditional theorem versus branch exclusion. INPUTS.md
matches the actual use and does not substitute excerpts for originals.
The retained draft and author records are expressly unselected. Their
presence outside the core does not affect the selected-only replay.

The checker was read in its entirety. Its local reads are bounded by
the fixed ten-file inventory, a per-file 64 KiB bound, an aggregate
byte bound, and a five-second alarm. It checks exact selected bytes,
source metadata, expected source bytes and recomputed Git blob identities,
the core digest, fixed physical W-adjacency, the recurrence only through
degree twelve, Hom/Ext twists, and the displayed rank/degree arithmetic.
Its tests are explicit `need` calls rather than Python assert statements,
so optimization does not erase them. It uses only standard-library local
operations and no network or third-party package.

It correctly states that replay of retained sources is not fresh remote
authentication. The independent six-response authentication in this
review supplies that separate requirement. Likewise, the checker's
minimum-orbit arithmetic does not prove the geometric action or map
compatibility; those are handled by the complete proof review and the
retained hypotheses. The hard binding to the exact externally supplied
freeze/core/proof/checker hashes is independently checked in this review,
not assumed merely because a self-consistent manifest passes.

No selected actual HM/source-instance coefficient, parameter, point,
jet, tensor, matrix, eigenline, scalar normalization, or instance rank
was evaluated. There was no broad scan, historical enumeration, large
computation, quotient connection, moving inverse derivative, or assumed
horizontal Birkhoff splitting.

## 6. Four new clean selected-only replays

After independently binding the freeze, the reviewer created two new
empty directories with independent temporary suffixes. Each received
exactly the nine frozen core files and FROZEN.json, preserving relative
paths. The verified pre-copy inventories were empty. The only directory
inside each replay is `inputs/`, containing exactly the three originals.
No raw source responses, author records, draft, review, audit script,
output log, or unselected dependency was copied into a replay.

### New replay directory A

`selected-only-a-xffmxte4`, under this review directory.

- `python3 -B verify.py`: 2026-10-24T13:47:32.000592+00:00 to
  13:47:32.034577+00:00; exit 0; 367 explicit checks; optimization=0.
- `python3 -B -O verify.py`: 2026-10-24T13:47:32.036230+00:00 to
  13:47:32.123231+00:00; exit 0; 367 explicit checks; optimization=1.

### New replay directory B

`selected-only-b-l74xbpgw`, under this review directory.

- `python3 -B verify.py`: 2026-10-24T13:47:32.126565+00:00 to
  13:47:32.152392+00:00; exit 0; 367 explicit checks; optimization=0.
- `python3 -B -O verify.py`: 2026-10-24T13:47:32.153940+00:00 to
  13:47:32.240102+00:00; exit 0; 367 explicit checks; optimization=1.

Every stderr was empty. Both replay inventories, every selected-file
length/hash, and the original core/freeze were identical before and
after all runs. `REVIEWER-REPLAYS.json` contains full commands, absolute
working directories, creation and run intervals, elapsed times, complete
stdout/stderr, and full per-run before/after inventories. Separate
stdout/stderr artifacts are also retained outside the replay directories.
The reviewer audit script records the authentication and replay method;
it is not part of the mathematical core or a substitute for this review.

## 7. Final acceptance boundary

The accepted structural conclusion is exactly that the original Fhat
has generic derivative rank three, coherent image W(-1)+O(-10), actual
saturated normal image `(K/Fhat)(-2)=A O`, reduced cyclic defect on D12,
actual backward kernel Chat=Bhat^-, actual forward span K, and constant
span C of dimension twenty-one.

There are no requested revisions or unresolved mathematical gaps in this
exact frozen packet. No new G7/H5 dependency has been added. All retained
conditional hypotheses remain in force. This review does not claim K1
exclusion, realization, new higher-order matching, or algebraicity.

The companion `ARTIFACT-MANIFEST.json` binds the reviewed frozen packet
and inventories this separate review's evidence artifacts. The reviewer
has made no publication or upstream state change.
