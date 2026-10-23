# Independent review: both source127 cf-family edges

## Verdict and exact version

PASS for the two entire source edges stated in `PROOF.md`, under its pinned actual-bundle inputs. No mathematical correction is required for this version.

This review is bound to the following SHA256 digests:

- `PROOF.md`: `0075805e34bdf0746a1a20cb95110144655080b6c5dfa294e23f81c6b0627895`.
- `verify.py`: `16480184a87c523959f8f1311532b47ac2d797be7054e6753659fe96b648af3f`.
- `REPRODUCE.md`: `405c37cba8b50a264705be621eb2f275f3666b7b82f9c857f9c35118c83bdea4`.
- `audit-inputs/manifest.json`: `51ffdf45d3aa2373306323c35f0c0d73639be47b39af2d4462fe7013281c5f73`.

The reviewed claim excludes exactly the two tuples

    (0,0,1,0,0,1,0,1), (0,0,1,0,0,0,1,0)

for original source127, stable label `G3.11.cce6e3ba4eeb`, with

    A_q=O(-8)+O(2)+O(16), B_q=O(-18)+O(-4)+O(6).

It is not a whole-label exclusion, a compatible-pair recount, a frontier decrement, or a global rank theorem. It is a written mathematical proof, not proof-assistant certification.

## Public inputs and source decoding

All eight local input files passed the verifier's exact Git-blob integrity checks. Independently fetching each path at its manifest commit through GitHub returned the same eight Git blob hashes. The actual presentations, strict-top lemma, source127 catalog row, stable label, and relevant parts of PR796, PR802, and PR861 were read rather than inferred from their titles.

The original catalog decoder gives, respectively,

    E=(V+P+D) O(-2)+V O(-4)+O(-8)+O(-10),
    E=(V+P+D) O(-2)+V O(-4)+W O(-9).

Both have rank17 and degree-54. The original determinant defect is zero, so the proof legitimately uses the saturated actual inclusion

    A2=A_q(2)=O(-6)+O(4)+O(18) subset Q.

The endpoint interpretation was also checked against the public note `ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md` at the same original commit `db51525015bb7c5e825833d550d08dedf6f6ea96`. In particular B_q is the actual quotient of Q* by its derivative kernel, not an unrelated formal bundle. That source explicitly permits degree-minus-one summands in Q*; the present proof does not silently strengthen this to H0(Q*(1))=0.

Current [PR1](https://github.com/Akilleez-QA/read-em-and-weep/pull/1), including its source113/source127 distinctions, was checked at head `2531056eae05fdf31e8fb4ca3affc5907073ad73`. The source113 completion in PR868 is not needed as a theorem premise: the present Sections4-6 prove the modification and dual obstruction for source127 itself. PR861 is used only for interfaces explicitly restated and rechecked here.

## High-line reduction and all changed interfaces

If the D-to-O(2) row vanished, the twelve independent top sections would form a basepoint-free degree-eighteen system: a nonempty invariant divisor would leave at most seven independent sections. The two exact full-top kernels have rank11 and degree-40. Their internal maps to V O(-6) and either N(-2) vanish, including the scalar-to-V degree-equality exception. The quadratic Gauss gap at rank12 then excludes the quotient O(18).

For F=(V+P) O(-2), the only common-divisor possibilities are degree0 and degree12. The independent seven-section system and the minimum invariant orbit length justify this dichotomy. In the degree0 case, the four kernels in equation(2) are exhaustive, not selected examples.

I recomputed their complete supports independently using the integer McKay graph for tensoring by W and the recurrence

    U Sym(n+1) W = W (U Sym(n) W) - U Sym(n-1) W.

The graph has edges

    1-W-A-S-D-T, T-V, T-P-Wp.

The H1(K(2))=A+P+D budget gives precisely the eleven supported negative atoms listed in PR861. Matching chi(K(3))=-W-S, rank6, and degree-30 leaves exactly the four displayed kernels. Applying the same calculation to the A+P budget gives exactly the two full-top kernels. No further kernel alternative is lost in the transfer.

For both tails, the complete surviving internal channels in the four-kernel case are exactly

    W O(-7) -> D O(-4),
    O(-8) -> D O(-4),

each with multiplicity one. All tail channels and all remaining V channels vanish. The two universal multiplication maps are everywhere injective, so the actual-image lemma applies without a hidden saturation correction. First-polar generation gives the three cases stated in the proof; the scalar internal image has nongenuine linear character T-S, leaving only

    M=P O+T O(-1).

The constant-P projection argument is valid for the actual connection. A zero P channel would yield a forbidden invariant determinant of degree8; both channels nonzero would make the complete Euler quotient horizontal. The linear coefficient-kernel argument then forces Kc=P, constant span P+V+D of dimension12, and the two rank-two quotients Wp O(3), Wp O(1).

The map from (E intersect M)/F=W O(-5) to Wp O(1) cannot have generic rank one: the only eligible invariant saturated line is O(-4), and its map to Wp O(1) vanishes. Its generic rank two therefore forces the actual constant twelve-space into E^+. The two lower quotient components vanish after factoring through Wp O(3). This remains true for the changed O(-6) component. The resulting rank-eleven subbundle of E has degree at least-18, contradicting its upper bound-22. This excludes the entire basepoint-free branch for both tails.

## Exact intersections and the double divisor

For the degree12 branch, the kernel T O(-3) has zero internal derivative for either tail. The raw first span has rank8 and degree-8. Its saturation defect is an invariant effective divisor of degree at most8, so is zero. This justifies the actual saturated bundle M=Sym7 W O(-1), rather than assuming it.

The linear-span argument identifies C=Sym8 W=P+D, with

    C O/M=O(8), M/F=O(6), C O/F=W O(7), M^-=F.

If C O were contained in E^+, the induced high component W O(7)->O(18) would be nonzero and onto. Its two degree-eleven sections cannot have a nonempty invariant common divisor. Its kernel O(-4) has zero Hom to every summand of E/F for both tails, a contradiction. Saturation and the derivative kernel then give exactly

    E intersect C O=F, E^+ intersect C O=M.

These identities do not make the projected image E/F saturated. The proof correctly keeps its torsion defect.

The derivative comparison j(-2)=f12 phi is a comparison of maps between actual subquotients in the same constant ambient bundle. It implies vanishing of j along D12 without any assertion that j or phi is saturated. In Q/L, the quotient map k from O(8) has fiber image in A2/L at those points. The stabilizer characters are respectively ζ² and ζ⁶, ζ⁶, for ζ of order10. Thus k vanishes along the entire reduced orbit. This argument is uniform; it is not an evaluation at a selected actual source point.

Locally, the O(6) subline of B=W O(7) maps as f12 times a generator of L. The second column modulo L is also divisible by f12. Every maximal minor is therefore divisible by f12 squared. The argument does not require a chosen global projection of Q onto the two lower summands and does not assume any particular negative-endpoint component nonzero.

The two inclusions B->Q and E/F->(H/C) O have the same cokernel, so their full saturation defects agree, including multiplicities. Full span gives

    24<=delta<=29.

After subtracting 2D12, the remaining invariant effective divisor has degree at most5 and must be empty. Hence the defect is exactly 2D12, not merely a lower bound or a reduced twelve-orbit defect.

The saturation Sigma contains all of the saturated L=O(18). Its quotient has degree20, so its equivariant extension is either O(18)+O(20) or W O(19). The one-dimensional invariant Ext1 space justifies this complete alternative. No horizontal splitting is introduced.

## Dual cohomology and terminal contradiction

For R=(Q/Sigma)*, the exact dual sequence has rank R=11 and degree R=-16. Both possibilities for Sigma have the same equivariant cohomology and K-class. Negativity at twist0 makes the cohomology sequence exact in the form used, yielding

    H1(R)=D,
    chi_G(R(3))=-W+Wp+S+4T.

The independent McKay recurrence also reproduced these identities from the pinned M2 and M3, as well as all symmetric powers used in the calculation.

Because every R degree is at most-1, any atom contributing to H1(R) has the parity and dimension bound (j-1) dim U<=5. The complete surviving support is just D O(-2) or O(-6). The first alternative would require a nongenuine coefficient character. In the second, the genuine degree-minus-one coefficient is uniquely 2Wp+T. Thus

    R=(2Wp+T) O(-1)+O(-6).

The actual strict-top lemma for Q* gives an injection

    H0(Q*(1)) -> H0(B_q(1))=Sym7 W=Wp+T.

The subbundle R supplies 2Wp+T inside its source. Two Wp copies cannot inject into one. This is the claimed contradiction, and it uses no unjustified H0(Q*(1)) vanishing.

## Executed checks and remaining boundary

`python3 verify.py` passed against all eight exact input files. Python compilation also passed. In addition to running and reading that verifier, the independent integer McKay calculation reproduced the complete two-kernel and four-kernel classifications, the changed Hom interfaces for both tails, the exhaustive H1(R)=D support, and the unique coefficient 2Wp+T.

The reproduction instructions correctly separate the five focused publication files from the already-public input blobs. Their download recipe verifies each blob before use. No private notes, personal information, credentials, selected actual HM/source values, source-instance computations, or large calculations are needed by this package.

The two complete source-edge exclusions pass. Every other source tuple and every whole-label or global conclusion remain outside this review's verdict.
