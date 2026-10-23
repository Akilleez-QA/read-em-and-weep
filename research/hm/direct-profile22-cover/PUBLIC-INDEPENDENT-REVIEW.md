# Independent review: direct maximal-profile (2,2) quotient cover

**Verdict: ACCEPT as the stated conditional necessary-coverage lemma.**

Reviewed on 2026-10-23. I found no mathematical blocker in `PROOF.md` or its
standalone finite verifier. Acceptance is conditional on the explicitly pinned
actual HM presentations, the actual four-source theorem, the original maximal
saturated plateau, strict top-slope decrease, and the invariant-divisor gap.
It does not assert realization of any survivor, independently reprove those
upstream actual-input theorems, or by itself prove a global SF bound.

## Mathematical audit

1. The pinned primary-terminal theorem supplies exactly the four source bundles
   encoded in the verifier, with the physically marked W and W' distinct. All
   have rank 17, degree -54, and minimum splitting degree at least -8. The
   intrinsic quotient argument therefore makes A(8) globally generated. With
   rank A=3 and degree a<=4, every ordinary degree lies in [-8,20]. No finite
   historical source-pair frontier is needed for this bound.

2. On the actual maximal (2,2) plateau, K and L are interior rank-three stages;
   their kernels have ranks 11 and 7. Negativity and strict decrease give top
   degrees at most -4 on those kernels. The resulting inequalities
   -10-a<=deg J<=a-6 and -26-b<=deg J'<=b-6 imply a>=-2 and b>=-10. Thus the
   original determinant length t=-6-a-b satisfies 0<=t<=6 and must be zero.
   Consequently B=A*(-2), b=-6-a, and a is one of -2,0,2,4.

3. The separate second-interior defects obey s<=2a+4 and s'<=8-2a. The proof
   and code correctly retain the possible positive length-12 branch for s'
   at a=-2 and for s at a=4. The primal endpoint equality is used only for
   a<=2; the dual endpoint equality is used only for a>=0. No endpoint
   derivative rank is improperly assumed to be three.

4. Every filter is necessary. The Hom test is only a necessary component test
   for a quotient. The twist-two H0 injection and H1 surjection are applied to
   one common candidate source. The twist-two Euler inequalities follow from
   H0(K(2))=H0(L(2))=0. The second-interior twist-three Euler inequalities retain
   torsion as a genuine H0 term and use H0(M(3))=H0(N(3))=0. Their cotangent
   target has twist 1, not 2. The endpoint envelopes follow from strict
   top-slope decrease and the already justified zero defect on that side.

5. The finite domain is exhaustive: three even trivial lines; an odd W or W'
   block plus an even trivial line; or one even A3 or V block. Repeated lines
   are allowed. Self-duality justifies determining B by degree reversal and
   the same irreducible label. The only survivors are precisely:

   - A=O(-8)+O(2)+O(6), B=O(-8)+O(-4)+O(6).
   - A=O(-8)+O(4)+O(6), B=O(-8)+O(-6)+O(6).
   - A=O(-8)+W O(5), B=W O(-7)+O(6).

   Their a values are 0,2,2; both second-defect upper bounds are then below 12.
   Hence the original and both second-interior determinant defects vanish.
   These are the quotient and endpoint hypotheses required by the separately
   pinned terminal three-pair exclusion. The new cover does not depend on that
   exclusion to obtain its own finite output.

## Independent computation and provenance checks

- Ran `verify_direct22_cover.py` with ordinary Python and with `python3 -O`.
  Both passed 837 checked conditions and all seven stated counterfactual
  controls; the printed output was byte-identical.
- Wrote and ran `independent_mckay_replay.py`. It does not import the author
  verifier or any historical proof/record helper. It uses integer affine-E8
  McKay adjacency with the fixed standard W, rather than the Q(sqrt(5)) class
  table, and enumerates all bundles by a recursive rank budget rather than
  prespecifying the three shapes. Ordinary Python and `-O` again agree.
- The independent domain contains 1,130 shapes. Stage sizes are
  134 -> 25 -> 23 -> 10 -> 3 -> 3 (degree range, common-source conditions,
  twist-two Euler, second-interior Euler, primal endpoint, dual endpoint).
  I compared the complete domain and every stage set with the author verifier,
  not merely these counts, and they match exactly.
- All 279 products R tensor Sym^d W for the nine irreducibles and 0<=d<=30
  match between the independent integer recurrence and the author character
  table. The independent recurrence also passes positivity and dimension
  checks throughout that range.
- No historical source-pair record file was generated or used. No actual
  coefficient, point, HM map, instance matrix, or rank experiment was used.

## Reviewed artifact hashes

- PROOF.md: b8a8795dcc08e4f34cedd82ef27013bf9f76c6c263d0c6d15b2974ef39e07a28
- verify_direct22_cover.py: 42799b7364cea236e2dd90020d471628bfad48b987fff4e53b4bc9f091405ace
- RESULT.json: 3fd9a374b2844857ec1b080b8bc19f8cf2697e0629ca117d8462b3c363106466
- independent_mckay_replay.py: 511b276d18ac83d8d1fd929fa8a501d77493bbdf483e888be01e5980159a8a08
- INDEPENDENT-RESULT.json: a0c2160c5291449b008f91f30b31bf96f0c95919d8d5a63474044d37e1b53947

## Portable publication and source authentication

This rendering preserves the independent mathematical audit and computation
findings. Source-provenance details are replaced here by publicly resolvable
immutable references. The frozen independent review has SHA-256
7f0496264dc8b4b21060c544c111c3403fca04779a4ae6e744fca22f01ec59c1.
The proof and both verifier files are byte-for-byte unchanged.

A separate publication check authenticated all six entries of SOURCE-PINS.json
against their immutable repository paths, checking both Git blob IDs and SHA-256
hashes. The four-source proof is at commit
504b7eb800407dfc7e6340c98c72cdd553939f54, with SHA-256
d5feb4b4478b5ec8178a049124179d25473b2e2526b20823a40f6dc60095e28e.

The included test_compare_replays.py reproduces the full-domain, all-stage,
279-product, ordered-survivor, seven-control, and wider-window comparisons.
It uses explicit runtime checks that remain active with Python -O.
