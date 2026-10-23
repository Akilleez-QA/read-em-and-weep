# Independent whole-proof review: the twenty-orbit tail exclusion

## Verdict and exact binding

**PASS for the exclusion of both stated full labels, relative to the explicitly pinned input theorems.** The proof closes the last degree-twenty branch and, importantly, its source-exhaustion argument accounts for every entry of both original necessary source overlists. It does not merely prove a conditional obstruction for two sources while leaving other entries untreated.

This review binds exactly:

- `PROOF.md`: SHA256 `f2874bb3a6b90ef7742ac9f8014ddf532667745c63e8c630dfab70301fda4264`.
- `verify.py`: SHA256 `28f9a9a852c665262f579cc342d01045f49b1f4d0426be44d8462517a07ec681`.

Both files were read completely and their hashes were checked. Neither file was edited. The declared tiny universal verifier was inspected and run successfully. This is a mathematical audit with an exact-character check, not proof-assistant certification.

## 1. Original records and complete source exhaustion

The original five files named in Section 1 were retrieved directly from `Akilleez-QA/read-em-and-weep` at commit `db51525015bb7c5e825833d550d08dedf6f6ea96`, under `research/hm/order-four-quadratic-load/`:

- `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`, Git blob `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
- `one-one-endpoint-necessary-pairs.json`, Git blob `fe0afa410d89340d3082dc814277f89fbb582c19`.
- `rank-three-quotient-frontier-144.json`, Git blob `8b5971092f9ef762584912609fd5e9301c4e271d`.
- `POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md`, Git blob `303c6927265296440470b9dd4015fe6e8d55ca4d`.
- `UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md`, Git blob `d34434e3bffe4e9de4a6aaa4d5e469336b12d5d0`.

The stable-label records directly identify `G3.11.dc58cc54f352` with source index 112 and `G3.11.4b6dad66f329` with source index 115, in both cases profile 11 and original defect zero. Their A and B quotient records agree with the theorem. Index 112 has exactly the four tuples

    (0,0,0,0,0,2,0,1), (0,0,0,0,1,1,0,1),
    (0,0,1,0,0,1,0,1), (0,1,0,0,0,1,0,1).

Index 115 has those four and exactly the additional four

    (0,0,0,0,0,1,1,0), (0,0,0,0,1,0,1,0),
    (0,0,1,0,0,0,1,0), (0,1,0,0,0,0,1,0).

Applying the displayed tuple-to-splitting formulas in the actual-splitting input gives precisely E0, U6, E3, E6 and, for the additional four, E10, U13, E12, E13. Thus the overlists are exhaustive as necessary possibilities, without treating them as realized source instances.

Every exclusion dependency below was retrieved and read at its exact immutable commit, rather than inferred from a PR title or a later summary. Paths are under `research/hm/` in the same repository.

- **PR813**, commit `3f99ecf539a3a3da61743df0dff409e54270c865`, `profile11-o26-divisor-reduction/PROOF.md`, Git blob `c5237be81f13d72776ba117548038f4c2c11b6b4`. Section 1 reproduces exactly the checked tuples and splittings. The theorem and Sections 2–7 give divisor alternatives 0, 12, 20; eliminate 12 for every relevant source; and allow 20 only for matching E6/index112 and E13/index115. In particular the twelve-divisor argument keeps, rather than suppresses, the possible saturation defect and the torsion-modified projected backward kernel. Its degree-twenty conclusion is not a full exclusion and is used only in its stated necessary sense.
- **PR817**, commit `a0b7cbd7a53c1603f284cf0e1a29fff106d02cb3`, `profile11-o26-basepoint-free-top/PROOF.md`, Git blob `891b037953e54cac798819afb23d8e64c6e2bb95`. Section 7 excludes basepoint-free E0/index112 and E10/index115 by genuine constant projection followed by an impossible negative horizontal backward line. It also explicitly excludes E0/index115: only its single O(-10) summand can map to W O(-9), so the rank-two negative quotient cannot be surjective. The main theorem alone would not suffice; the proof correctly cites the additional residual corollary in Section 7.
- **PR829**, commit `5e713ff925335b7fb08b5a5768fb558e81fc3575`, `profile11-o26-two-p-polar-exclusion/PROOF.md`, Git blob `d17ed853339be89219c59d565c7cdbbe348e52be`. Its stated conclusion and final channel exhaustion exclude U6 at both indices and U13 at index115. The nonzero-divisor alternatives are ruled out by coefficient multiplicities; the basepoint-free argument excludes both possible internal-image outcomes and every multiplicity-row case. Thus no displayed U entry remains.
- **PR834**, commit `71e3d3671474e2990c55ee67fec6d2c65e288649`, `profile11-o26-vpd-polar-exclusion/PROOF.md`, Git blob `41a0bc9a9a71d7810c8f7df190cf38c92f1ad2ea`. Its conclusion covers E3 at both indices and E12 at index115. After the PR813 divisor reduction, the argument exhausts the zero internal image, the V O(-6) image, and the O(-12) image. The final constant-part/linear-block contradictions cover every surviving channel case.
- **PR840**, commit `a69b5a8b9a7c4cb673a89c6465e152fcf699840a`, `profile11-o26-basepoint-free-pd-exclusion/PROOF.md`, Git blob `1577481b2aa8d837a0a22794db128cf8c4386e4b`. It excludes exactly the matching basepoint-free E6 and E13 cases, preserving the separate degree-twenty problem. Its exceptional internal Hom space and both possible saturation defects are retained and treated. Section 1 explicitly supplies the E6/index115 mismatch: again only one O(-10) summand maps to W O(-9), so no rank-two surjection is possible.

The resulting complete ledger is:

    index112:
      E0   : divisor12/20 removed by PR813; divisor0 by PR817 §7.
      U6   : PR829.
      E3   : PR834.
      E6   : divisor12 by PR813; divisor0 by PR840;
             divisor20 by the reviewed new argument.

    index115:
      E0   : immediate negative-quotient mismatch, recorded in PR817 §7.
      U6   : PR829.
      E3   : PR834.
      E6   : immediate negative-quotient mismatch, PR813 and PR840 §1.
      E10  : divisor12/20 removed by PR813; divisor0 by PR817 §7.
      U13  : PR829.
      E12  : PR834.
      E13  : divisor12 by PR813; divisor0 by PR840;
             divisor20 by the reviewed new argument.

This ledger checks all twelve source entries individually. Nothing is removed by a numerical total, by an unproved realization assertion, or by a claim that the surviving matching branches were the original complete lists.

## 2. Exact geometric prerequisites

Two further prerequisite proofs were retrieved and read:

- **PR825**, commit `ea94799a3b1e1c18a4d83061b92d7e7e2f1c631e`, `profile11-o26-degree10-endpoint/PROOF.md`, Git blob `41acb092b2db47d0070e6e85e8a2c87ea552e478`. This proves the sheaf intersections E ∩ C O = F and E⁺ ∩ C O = F⁺. It explicitly states that the surviving projected image is not being asserted saturated. Its Section 1 also gives the actual image F⁺ → E⁺/E as f20 O(8), with kernel F and no negative component.
- **PR845**, commit `3078ec876065f772aa10ef9d8478505035f71db8`, `profile11-o26-cubic-residual/PROOF.md`, Git blob `3b6842a1d4ba33dd902ab52466e0d78ede175569`. The fetched proof agrees byte-for-byte with SHA256 `c574a1e3ff6624f43094547dc30fad8fe67f48c07a09006e2e9a2722d0ad064f`. It gives the six necessary cubic-residual templates, their full constant spans, and saturation defect 0 or 12. It does not require the separate stabilizer or coupling drafts.

For the new argument, only the following part of the six-template conclusion is used: C1 has dimension 7–9, its representation is A+P, A+D, P+D, or V+P, and the cubic-image saturation defect is 0 or 12. The proof does not need any assertion that all six templates are realizable or that there are only six embedded equivariance orbits. An invariant torsion sheaf of length 12 must be supported on the twelve-point orbit, so the cubic inclusion is fiber-injective at every point of the disjoint twenty-point orbit.

## 3. Ambient character, actual quotient, and full span

The actual-splitting input explicitly says that E spans its full constant ambient H. This essential hypothesis is therefore an actual-bundle input, not an imposed model or an inference from the degree of E.

The actual exact presentations give, in equivariant K-theory or Euler characters,

    H = M3 ⊗ W − M2 − M4 = 2A + 2V + 2P + 2D.

Indeed χ(E)=−M4, while the actual quotient presentation gives χ(Q)=M3⊗W−M2, and E+Q=H O. The quotient by the actual constant C=Sym10 W=A+V+D therefore has

    Hbar = A+V+2P+D,  dim Hbar=19.

E ∩ C O = F implies that R=E/F injects into Hbar O **as a sheaf**. No fiberwise injectivity or saturation of the whole R is necessary. Since E spans H, this projected image spans Hbar.

Saturation does not change the full constant span of the cubic image: a constant functional killing that image also kills its saturation, by torsion-freeness of the constant target. Thus the C1 used in the proof is the appropriate constant quotient to kill the T O(-3) summand. Because finite-dimensional representations are semisimple, every one of the four possible C1 representations removes at most one P from Hbar. Consequently

    dim B = dim(Hbar/C1) ≥ 10,
    B has a nonzero P constituent.

The induced map q:L→B O spans B. This follows from full span of R and the fact that its entire T summand is killed; it does not assume that q is saturated.

## 4. Generic rank of the negative tail

Rank zero contradicts full span and dim B≥10. If the generic rank were one, saturating its image in B O gives a G-equivariant line S=O(-d), with d≥0. Full span forces the coefficient map B*→H0(O(d)) to be injective, hence d+1≥dim B≥10 and d≥9.

For E13, Hom(W O(-9),O(-d)) vanishes for d>9 by degree; at d=9 its equivariant constant coefficient would be a map W→1, which is zero. This excludes all d≥9.

For E6, degree forces d≤10. The saturated line is center-even because it is a subbundle of the even constant representation B. Every equivariant linearization of a fixed line bundle differs by a character; the group has no nontrivial one-dimensional characters. Hence d must be even, and 9≤d≤10 gives d=10. The O(-8) component is zero, while the nonzero O(-10) component is a scalar isomorphism onto S. A full-span inclusion of S would therefore inject B* into Sym10 W=A+V+D. This is impossible because B* has P and Sym10 W does not.

Thus q has generic rank two in both cases. The argument handles arbitrary rank-one image sheaves by passing to saturation; it does not incorrectly assume that the original rank-one image was already a line subbundle.

## 5. Fiber argument on the twenty-point orbit

The original defect-zero hypothesis makes E⁺/E a vector bundle. Therefore tensoring the exact sequence 0→E→E⁺→E⁺/E→0 with the residue field at x remains left exact. The map F⁺→E⁺/E has image f20 O(8) in O(28) and zero component in L(2). At any x in D20 its fiber map is consequently zero, giving the genuine inclusion

    F⁺_x ⊂ E_x.

This does not identify fiberwise and sheaf intersections: the sheaf intersection E∩F⁺ remains F, while its fiber intersection increases at D20. Since F and F⁺ are saturated in the constant bundle, F_x injects into F⁺_x and F⁺_x/F_x has dimension one. It provides a nonzero vector in ker(i_x:R_x→Hbar).

At the same x, the restriction of i_x to the T O(-3) summand is injective. Its saturation G0 is a subbundle of Hbar O, and its only possible discrepancy from the cubic image is supported on D12, which is disjoint from D20. A nonzero vector in ker(i_x) thus has a nonzero L component l. Writing that vector as (t,l) gives i_x(l)=−i_x(t), whose value lies in C1. Projection to B therefore gives q_x(l)=0 with l≠0.

This proves rank(q_x)<2 at every point of D20. It uses arbitrary fibers along the entire invariant orbit, not a selected point, a selected source matrix, a saturation upgrade for R, or a purported identification of the length-twenty backward modification with T O(-3).

## 6. Exterior square and conclusion

For both tails, det L=O(-18); for W O(-9), this also uses det W=1. Generic rank two makes

    ∧²q : O(-18) → (∧²B) O

nonzero. The established rank drop makes this vector-valued section vanish at every point of the reduced divisor D20. Thus its image lies in (∧²B) O(-20). Equivalently all its degree-eighteen coefficient sections are divisible by the degree-twenty equation. The factor map must vanish because H0(O(-2))=0, contradicting its generic nonzero value.

The proof therefore excludes both remaining degree-twenty matching sources. The complete ledger in Section 1 then excludes both full labels `G3.11.dc58cc54f352` and `G3.11.4b6dad66f329`.

## 7. Executable check and scope limits

The sole mathematical program executed for this review was the declared `verify.py`. It completed successfully with its PASS message and accompanying scope statement. It checks the ambient character, Sym10 W, the four possible constant quotients, their P constituents, and the absence of P from degree ten, using exact Q(√5) arithmetic. It does not purport to check geometric saturation or fibers; those were audited above.

No selected actual source coefficient, parameter, point, derivative value, matrix, source-instance rank, model, scan, large computation, or all-twist envelope was used. Reading the two pre-existing formal source records is not a source-instance evaluation. The prerequisite verifiers were not rerun. No publication was made.

The conclusion is exactly the two-label exclusion. It neither excludes `G3.11.8ae96830fd21` nor resolves source2, any other retained label, or the global rank goal. The independent defect12 stabilizer and constant-coupling drafts are not dependencies of this result.
