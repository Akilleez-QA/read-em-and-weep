# Independent final-version review of the source113 cf exclusion

## Verdict and exact scope

**PASS. No mathematical gap found in Sections 1–6 of the final frozen proof.**

This is an independent review of the new divisor-twelve exclusion, not merely an execution of its character verifier. Under the pinned actual-bundle inputs and the already independently reviewed PR861 subsystem/intersection conclusions, the proof excludes the remaining divisor-twelve branch. Together with PR861's basepoint-free exclusion, it excludes exactly the cf tuple `(0,0,1,0,0,1,0,1)` at original source index113 for `G3.11.ad509d55173f`.

The verdict does not exclude the whole label, assert a frontier decrement, prove realizability of any hypothetical bundle, or reconstruct the frozen underlying HM geometry.

## Hash binding and dependencies

The reviewed final bytes are:

- `NEXT-DEFECT-BOUND.md`: SHA256 `2c9faa4394d96c158530f90bbccd586d0685b47da63c34ad4c66b7fb65ad5553`.
- `verify_next.py`: SHA256 `09ed51399de3872e63cb3dcc9beb7aa0d38107a894ca010544d6d281c35a11eb`.
- Adjacent unchanged PR861 helper `verify.py`: SHA256 `3f3e1d0807ba25f19df75407604c1f8f028bb05681bef5becc0f69bd513c394a`.
- `NEXT-REPRODUCE.md`: SHA256 `5d31986f23e587c2f61770b6761a39d5ea985dd0f7d824e960e4f92c04687756`.

For publication, renaming the new proof, review, and reproduction document to `PROOF.md`, `REVIEW.md`, and `REPRODUCE.md` does not change the reviewed bytes. Both scripts must retain their stated names and be adjacent.

The preceding reduction documents, read during this audit and distinct from the new package's renamed proof and review, are:

- `PROOF.md`: SHA256 `8157ffa4a39882a8bc4a0b2f1c5200d01e1fc8d9d336904fce63464e672d2204`.
- Its separate independent `REVIEW.md`: SHA256 `c6fad502bd196d96e24b2c26171afcade61428d09d8301a588f289f7079b4229`.

The reduction's immutable provenance supplied for the final proof is PR861, commit `7b5b3371a82cb92f46ea60895e45617d0891a5b0`, at:

https://github.com/Akilleez-QA/read-em-and-weep/blob/7b5b3371a82cb92f46ea60895e45617d0891a5b0/research/hm/profile11-source113-cf-reduction/PROOF.md

The original inputs are supplied at commit `db51525015bb7c5e825833d550d08dedf6f6ea96`, under `research/hm/order-four-quadratic-load`. I read the local pinned copies, with these verified hashes:

- `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`: `a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256`.
- `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md`: `53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08`.
- `one-one-endpoint-necessary-pairs.json`: `6002ad138a41d98c351130a29703722979f31b8da90d7c75a120f28bf89480eb`.
- `rank-three-quotient-frontier-144.json`: `a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad`.

I inspected original catalog record113 directly. It has defect zero, the stated A_q, the stated B_q, and ten compatible tuples including cf. Applying the original splitting formula gives the stated E, rank17 and degree−54. In particular the dual quotient used at the end is the original actual quotient, not a proposed quotient inferred from the new construction.

## 1. Connection compatibility and the first divisor

The inputs concern actual subsheaves of the original constant bundle. The reduction's Sections6–7 correctly give M=F^+, its actual constant span C, and both exact intersections. I checked the relevant connections again: the complete evaluation sequence for O(8) makes M the complete linear kernel; its derivative has kernel F and gives the nonzero isomorphism `M/F=O(6) → (C O/M)(−2)=O(6)`.

Since E^+ contains the derivatives of E, its second fundamental form vanishes on E and descends to A2. Restriction to its saturated highest line L defines phi. Compatibility of differentiation with the actual inclusions M⊂E^+ and C O⊂H O gives equation(2), up to the allowed nonzero scalar. Thus j vanishes at every point of the reduced twelve-orbit. This uses neither a new connection on an abstract splitting nor a saturation claim for j.

For completeness, the exact-intersection input is consistent independently: C⊂E^+ would give a nonzero map W O(7)→O(18), with both lower rows zero. Its degree-eleven two-section system has no nonempty invariant common divisor, hence is onto. Its kernel O(−4) has no equivariant map to E/F. This rules out C⊂E^+; saturation gives C O∩E^+=M. Differentiating E∩C O then lands in M, so its containment in M forces E∩C O⊂M^−=F, proving equality.

## 2. The missing lower-row correction is genuinely excluded

L is saturated in A2 and A2 is saturated in Q, so Q/L is a vector bundle and the sequence

    0 → A2/L → Q/L → Qplus → 0

is exact on fibers. The map from M/F to Q lies in L, hence B→Q/L descends to the asserted map k from B/(M/F)=O(8). Its composite to Qplus is j.

At an arbitrary point of the twelve-orbit, the stabilizer in the binary group is cyclic of order10. A generator acts on the tautological line by a primitive tenth root zeta; the natural O(a) fiber character is zeta^(−a). No unmentioned line character can change these weights because the binary icosahedral group has no nontrivial characters.

At that point j is zero. Consequently k's fiber map lands in A2/L, whose two characters are zeta^8 and zeta^6. Its source has character zeta^2. All three characters are distinct. Stabilizer equivariance therefore makes the entire fiber map zero. The conclusion is uniform over the orbit and does not evaluate a selected actual source point.

Vanishing on a reduced divisor gives a sheaf factorization through O(8)(D12)=O(20), exactly equation(3). This is valid even though Q has no chosen global splitting. In particular the argument supplies the lower-row divisibility that could not follow merely by projecting j.

## 3. Determinant valuation and the common torsion quotient

Locally split the saturated line L⊂Q, and extend the line M/F⊂B to a local frame. The first column is a uniformizer times a unit multiple of the L-frame at each point of D12. The second column modulo L is divisible by that same uniformizer, by the preceding step. Therefore every two-by-two minor is divisible by its square.

For a rank-two bundle inclusion into a bundle over a smooth curve, local Smith normal form identifies the minimum valuation of maximal minors with the length of the quotient by the image inside its saturation. Thus the saturation defect is at least2D12. This is a determinant-divisor assertion, not an unsupported inference from generic rank.

The exact intersection E∩C O=F gives both injections

    C O/F → H O/E,
    E/F → H O/C O.

Their cokernel is literally the same sheaf `H O/(E+C O)`. For either injection, the saturation quotient is its cokernel's torsion subsheaf. Hence their defect divisors agree point by point, with their full scheme-theoretic multiplicities. No saturation of E+C O has been presumed.

The projected residual has rank10 and degree−40 before saturation, so its saturation Z has degree−40+delta.

## 4. Full span determines the entire defect

The full-span input for E implies that its image in H/C spans the full21-dimensional quotient; passing to the saturation Z preserves that span. Since Z is a subbundle of a constant bundle, all its splitting degrees are nonpositive. Its dual therefore has no H1, and

    h0(Z*) = rank Z − deg Z = 50 − delta.

A constant functional on H/C that restricts to zero on Z vanishes on its coefficient span. Thus full span makes `(H/C)* → H0(Z*)` injective and gives delta≤29.

The defect divisor is invariant. Subtracting the established effective sub-divisor2D12 leaves an invariant effective divisor of degree at most5. There is no nonempty invariant effective divisor of that degree, since every projective orbit has at least12 points. Therefore the defect is exactly2D12, not merely a length24 divisor. This proves rank Z=10 and degree Z=−16.

## 5. The saturated rank-two bundle and dual exactness

B=W O(7) has degree14, so its saturation S in Q has degree38. It contains L because it contains the generic span of the nonzero image f12·(M/F); the map L→Q/S is generically zero and its target is locally free, hence it is zero. Since L is already saturated in Q, S/L is a line bundle, of degree20.

The equivariant extension space is `H1(O(−2))^G`, one-dimensional and trivial. The zero extension gives O(18)+O(20). A nonzero extension is the twist by19 of the Euler extension and gives W O(19). Finite-group averaging and the absence of line characters justify this in the equivariant category. Only its K-class is needed below.

Because Q/S is a vector bundle, dualization gives the actual short exact bundle sequence

    0 → (Q/S)* → Q* → S* → 0.

There is no unaccounted Ext sheaf or torsion term. Thus R=(Q/S)* has rank11 and degree−16. Its inclusion in Q* gives strictly negative splitting degrees. S* is also strictly negative in either extension case.

## 6. Original cohomology and exhaustive residual support

The original exact presentation is

    0 → Q* → M3* O(−1) → M2* O → 0.

Since O(−1) has no cohomology, twist zero gives H0(Q*)=0 and H1(Q*)=M2. Twist three gives, by Euler additivity, `M3 Sym2 W − M2 Sym3 W`. Using the supplied original M2 and M3, this is exactly T−2W−S. The newly added provenance derivation is correct and is checked in the final verifier. No assumption about H0(Q*(1)) enters it.

The extension for S gives

    H1(S*) = Sym16 W + Sym18 W = A+2V+3P+3D,
    chi_G(S*(3)) = −Sym13 W−Sym15 W.

All three H0 groups in the untwisted dual exact sequence vanish. Its long exact sequence consequently gives an exact sequence of H1 representations and H1(R)=D. Euler additivity at twist three gives `chi_G(R(3))=−W+Wp+S+4T`.

I checked the support exhaustion independently, not just the listed alternatives. An irreducible atom U O(−j), j≥2, contributes the genuine representation U Sym^(j−2) W to the five-dimensional H1 budget D. Thus `(j−1)dim U≤5`. At j2 only U=D can fit inside that irreducible budget. At j3 the dimension-eligible odd coefficients are W and Wp, producing 1+A and P, respectively, so neither works. At j4 only U=1 is dimension-eligible, and it produces A rather than D. At j5 the odd minimum dimension2 already exceeds the budget. At j6 only U=1 is eligible, and it produces D. All j≥7 exceed the budget even before any parity restriction.

Therefore exactly one of D O(−2) and O(−6) occurs, and every remaining summand has degree−1. Rank11 gives precisely the two forms in(8). The first would require the character `L6 A=−W+Wp+3T`, impossible for genuine L6. In the second, the four odd irreducible products displayed in the proof force L10=2Wp+T with no alternative: absence of W eliminates W and S in L10; the Wp coefficient forces one T; the remaining T coefficient forces two Wp. Hence(9) is established exhaustively.

## 7. Strict-top contradiction and conclusion

Q* is the actual saturated annihilator bundle in the dual constant ambient space. Its degrees are at most−1, which also follows directly from H0(Q*)=0. The original universal strict-top lemma applies with d=1, regardless of any endpoint derivative rank. It gives `H0((Q*)^−(1))=0`.

The original B_q is exactly `Q*/(Q*)^−`. Its twist-one global sections are Sym9 W=S+T, so the quotient induces the claimed injection H0(Q*(1))→S+T. On the other hand R⊂Q* gives an injection of H0(R(1))=2Wp+T. These maps are equivariant, while S+T has no Wp. Their composition is impossible. The proof uses only the strict-top vanishing for the Gauss kernel, not the unavailable stronger vanishing for Q*(1) itself.

This closes the divisor-twelve branch and, with PR861, precisely the cf source edge stated in the verdict.

## Execution and restrictions

I inspected both verifier files and executed the final `verify_next.py`, which also executes `verify.py`; both passed. The fixed computations check universal representation identities, bounded atom support, stabilizer congruences, source-record membership, and degree arithmetic. The connection, saturation, common-cokernel, full-span, equivariant-extension, and dual-exactness arguments were checked separately above.

No actual selected source coefficients, parameters, points, derivatives, instance matrices, instance ranks, models, scans, or large computations were used. This is an independent mathematical review, not proof-assistant certification. No publication was performed.

## Final package and reproduction check

The reproduction document's recipe is correct: run `python3 verify_next.py` with the unchanged adjacent `verify.py` and the two original catalog files under adjacent `audit-inputs/`. Both scripts use only Python's standard library. The next verifier resolves its helper relative to its own path, and the helper resolves the catalog directory relative to its own path. Neither script imports a predecessor checkout or writes or regenerates a catalog. The large catalogs need not be copied into the published proof package.

I independently requested the original catalog paths at the exact original commit through the GitHub connector. The returned canonical URLs match the two URLs in the reproduction document, and the returned blob identities are:

- `one-one-endpoint-necessary-pairs.json`: `fe0afa410d89340d3082dc814277f89fbb582c19`.
- `rank-three-quotient-frontier-144.json`: `8b5971092f9ef762584912609fd5e9301c4e271d`.

Local `git hash-object` independently gives those same identities for the supplied input bytes. I also requested the helper at the stated PR861 path and commit; its returned blob identity is `ed6d0a5cf6c32c16d717fb3e77c4701f242dad03`, matching the adjacent local helper. Thus the supplied immutable URLs and blob checks correctly identify the needed inputs. The successful verifier run used exactly this file layout.

The final proof includes only the declared publication-clarity edits: removing the opening status sentence and replacing the two ambiguous predecessor-document references with the pinned PR861 exclusion. Reversing exactly these edits recovers the previously reviewed proof SHA256 `fdedd7160e79771c3a4916908918d6e2a03728bdea717004d46e9a0e59ad09ce`; the final hash bound above is `2c9faa4394d96c158530f90bbccd586d0685b47da63c34ad4c66b7fb65ad5553`. Thus no mathematical text changed. Both script hashes and the mathematical verdict remain unchanged. This package check adds no new mathematical assumption and performs no publication.
