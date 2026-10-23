# Independent exact-version review: V+P+D exclusion in the O(26) branches

## Verdict and exact scope

**Sound for the stated source-branch exclusion.** I found no mathematical defect in the reviewed version. The complete top-kernel support, the actual internal-image classification, the saturation arguments, the first-polar characters, and the channel-by-channel contradiction all check out.

This review binds the following exact files:

- `PROOF.md`, SHA256 `2f6486e50d74724025c8c397aba7015a2eeb86b002a508d93944fb46ff6e8d85`.
- `verify.py`, SHA256 `3e2f7951237cdb113a2fd2090f049fbd303a7ab6af06435f26fc0c42d3e3a67a`.

Neither file was edited during this audit. The included bounded verifier was inspected and run successfully. The geometric argument was checked separately; the verifier is not being treated as a certificate of the geometric statements.

The conclusion removes exactly the E3 source entries for `G3.11.dc58cc54f352` and `G3.11.4b6dad66f329`, and the E12 source entry for `G3.11.4b6dad66f329`, under the retained zero-original-defect profile-(1,1) hypotheses. It does not exclude either entire label, any unrelated source type, source2, or the global rank-three possibility.

## 1. Immutable dependencies and source identifications

I independently retrieved the following files from their stated immutable commits in [Akilleez-QA/read-em-and-weep](https://github.com/Akilleez-QA/read-em-and-weep). The locally read copies have Git blob hashes equal to those returned for the immutable public files.

At commit `db51525015bb7c5e825833d550d08dedf6f6ea96`, under `research/hm/order-four-quadratic-load/`:

- `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`: blob `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
- `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md`: blob `d7506dae49b4be43230450c4132bd5db91f137ef`.
- `ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md`: blob `dcacf0bcdef8377c1ed7654e5b82659ea409456e`.
- `one-one-endpoint-necessary-pairs.json`: blob `fe0afa410d89340d3082dc814277f89fbb582c19`.
- `rank-three-quotient-frontier-144.json`: blob `8b5971092f9ef762584912609fd5e9301c4e271d`.

The structural dependencies are:

- [PR813 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/3f99ecf539a3a3da61743df0dff409e54270c865/research/hm/profile11-o26-divisor-reduction/PROOF.md), commit `3f99ecf539a3a3da61743df0dff409e54270c865`, blob `c5237be81f13d72776ba117548038f4c2c11b6b4`.
- [PR796 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md), commit `d2b43060c83328dd5118aee6b9288fcfa0c873ac`, blob `46a0de762000f21182f6d3168f3ecfd63adaf75f`.
- [PR799 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/2172e4a7abbbe232f9f448bea6fa01dee7927460/research/hm/profile11-quadratic-polar-obstruction/PROOF.md), commit `2172e4a7abbbe232f9f448bea6fa01dee7927460`, blob `a62a56f6b8f97e02b3eab6fe3a47ec3bedb6c6b1`.

Direct inspection of the JSON confirms the two labels, their source indices 112 and 115, both zero original defects, and the displayed A_q and B_q splittings. The E3 tuple occurs in both source lists; the E12 tuple occurs in index 115. Substitution into the original source parametrization gives precisely the two E splittings displayed in the proof.

Only the needed parts of the structural dependencies enter this audit. In particular, PR813's common-divisor argument restricts the top system to divisor degrees 0, 12, or 20. For E3/E12 its degree-12 case has zero internal image, raw first-span rank 13 and degree -8, and hence no possible invariant saturation defect. The resulting quotient O(16) contradicts the quadratic Gauss gap at top rank 12. At degree 20 the top coefficient would have to inject into Sym8 W=P+D, which cannot contain V+P+D. Thus the present top map really is everywhere onto O(26). No more difficult E6/E13 intersection argument from PR813 is needed for this reduction.

PR796 is used only for its actual saturated derivative-image lemma, not its profile-(1,2) interior-stage vanishing. PR799 supplies first-polar generation and the actual constant-quotient principle, both of which were also checked directly below.

## 2. Exact top-kernel support is complete

Let R=V+P+D. The onto map R O(-2) to O(26), and the injectivity of R into Sym28 W, give rank K0=11, degree K0=-50, H0(K0(2))=0, and

    H1(K0(2))=A+P+2D,
    chi_G(K0(3))=-W-S.

The H1 budget has dimension 17. Every irreducible atom U O(-j), j>=4, therefore satisfies `(j-3) dim U <= 17`, the center-parity condition, and componentwise containment of U tensor Sym^(j-4) W in A+P+2D. There are exactly the 30 parity-compatible atoms within the dimension bound declared in the verifier; checking their character decompositions leaves exactly the 11 admissible atoms listed in the proof. No degree outside this bound can occur. Degree-3 atoms contribute only to H0 at twist 3 and are subsequently forced by the second Euler identity.

The two-case support argument is complete, not just a check of twelve examples:

1. Writing the next-twist H1 tail as T_tail, the degree-3 coefficient is T_tail-W-S. Its genuineness requires a W and an S in the tail.
2. Among admissible atoms, only 1_6 and W_7 supply W. Each consumes the sole A in the H1 budget, so exactly one occurs, and every other A-consuming atom is excluded.
3. If W_7 occurs, the remaining budget is P+D. It has exactly six fillings: either V_6 or 1_12; or one P-consuming atom from P_4,Wp_5 and one D-consuming atom from D_4,1_8.
4. If 1_6 occurs, S must come from 1_8, since every other possible S supplier consumes the already exhausted A. After including one 1_8, the same remaining P+D budget has exactly the same six fillings. This includes the case with two copies of 1_8 and does not omit it.

The resulting degree-3 coefficients are precisely the ones displayed in the proof. All twelve supports have the required rank, degree and both cohomological identities. This verifies necessity and completeness of the support overlist; no realization of every support is needed or claimed.

## 3. Internal images and saturation

For each atom in those supports, the equivariant Hom to each displayed target summand is computed from U occurring in the target coefficient tensor Sym^(j-k) W. The complete nonzero list is exactly:

- V_6 to V_6;
- 1_12 to V_6;
- 1_12 to 1_12 in E3;
- 1_12 to W_11 in E12.

All these spaces have dimension one; there are no maps to O(-10). None of the twelve supports contains both V_6 and 1_12. Thus no mixed rank-four internal image has been silently omitted.

A nonzero V_6-to-V_6 map is a scalar isomorphism onto that entire target summand. For a nonzero map from 1_12, any nonzero component is represented by forms of degree 6, 0, or 1. Its common-zero divisor is G-invariant, but its degree is at most the degree of a nonzero component. Every nonempty projective icosahedral orbit has at least 12 points. Consequently each such nonzero component is nowhere zero, and the line image, including any diagonal image, is a saturated copy of O(-12). This proves the three alternatives J=0, V O(-6), or O(-12) as actual image sheaves.

The raw derivative-image sequences are legitimate in the same original constant ambient bundle. For J=0 they give rank B=13 and degree B=4, which is already impossible for a locally free sheaf injecting into a trivial bundle. For nonzero J, both J and the external O(26) image are saturated. The quotient of the full derivative target by I is an extension of locally free quotients; hence I and B are saturated. There is no unaccounted saturation divisor.

## 4. First-polar characters and the actual constant quotient

The first-polar map R tensor W tensor O(-1) has image B. Thus B(1) is generated by global sections. Its inclusion in a trivial bundle bounds degrees above by zero, so all splitting degrees are 0 or -1.

The two nonzero J alternatives give the following independent numerical checks:

- J=V O(-6): rank B=16 and degree B=-8.
- J=O(-12): rank B=14 and degree B=-6.

In both cases chi_G(B)=A+D. Indeed the contribution of J(2) is -(P+D) in both cases. At the next twist,

    chi_G(B(1))=Sym29 W-T             for J=V O(-6),
    chi_G(B(1))=Sym29 W-(Wp+T)        for J=O(-12).

Subtracting `(A+D) tensor W = W+2S+T` leaves Wp+T and T respectively. This verifies both exact first-polar splittings in the proof.

Since H1(B)=0, C=H0(B)=A+D is not merely an abstract degree-zero coefficient: its evaluation is a genuine constant eight-dimensional subspace of H. Quotienting by C therefore commutes with the original connection. The embedded quotient B/C O is saturated in (H/C) O and is pure degree -1, so it has no global sections.

If the projected image of F contains a whole nonzero direct linear block M, every local section of M lifts locally to F. Its derivative lies in the projected B. The value and first derivative of a linear column span its constant coefficients. Therefore the first span of M is a nonzero constant subspace contained in B/C O, contradicting its zero H0. Saturation justifies passing from generic containment to the saturated first span if needed. This argument never assigns a horizontal connection to an arbitrary abstract complement.

## 5. Universal channels and the geometric exclusion

### The quadratic obstructions

For any equivariant quadratic map D O(-2) to (A+D) O, the tautological line O(-6) inside D O(-2) is killed. Its fiber is represented by the highest product ell^4 tensor ell^2; this lies in the Sym6 W component of D tensor Sym2 W. Since Sym6 W=V+P has no map to A+D, the composite vanishes. The tautological line is nowhere zero, so such a quadratic map cannot be an inclusion.

Neither V nor P has a quadratic channel to A: the identities V tensor A=P+D and P tensor A=V+P+D exclude A in both coefficient maps. Consequently an inclusion of (V+P) O(-2) into the constant A+D would land in D alone, impossible for a rank-seven domain and rank-five target.

### D plus either extra T channel

The unique nonzero D-to-T linear channel is multiplication Sym4 W tensor ell to Sym5 W. It is fiberwise injective and has the locally free line quotient O(4). If a nonzero V-to-T or P-to-T channel had generic image inside this D image, its composite to the line quotient would vanish generically, hence identically. It would factor globally through D O(-2). Equal twists reduce this factorization to Hom_G(V,D) or Hom_G(P,D), both zero. Thus adding either nonzero channel makes the map generically onto T O(-1).

Every maximal minor has degree 6. A nonzero minor exists by generic surjectivity. Any common-zero divisor of all minors is invariant and has degree at most 6, whereas a nonempty invariant divisor has degree at least 12. Therefore generic surjectivity upgrades to everywhere surjectivity. This supplies the full T linear block needed for the constant-span contradiction, not merely a generically full image.

### The Wp channel and three-channel contraction

Only P maps linearly to Wp. Since P=Wp tensor W, its unique nonzero channel is the Wp-tensor Euler surjection, with rank-two kernel, and is onto everywhere.

The standard contraction

    Sym8 W O(-2) -> Sym7 W O(-1)

is onto everywhere with kernel O(-10). Under Sym8 W=P+D and Sym7 W=Wp+T, it has exactly the three channels P-to-Wp, P-to-T and D-to-T. All three must be nonzero: otherwise Wp is missed, or the rank-five D source is in the kernel, or the rank-two kernel of P-to-Wp is in the rank-one contraction kernel. The nonzero three-channel diagram has no cycle; independent nonzero source and target scalings normalize any three nonzero channel coefficients to those of the standard contraction. Thus every map with all three channels nonzero is onto.

These are statements about the entire universal Hom spaces, with no selected actual coefficient or point.

### Exhaustion of both projected targets

For target T O(-1), D must project nontrivially by the quadratic obstruction. Any nonzero V or P projection then forces the full forbidden T block. If both vanish, V+P would inject into the constant D, which is impossible.

For target (Wp+T) O(-1), D again has a nonzero T channel. If P-to-Wp is nonzero and P-to-T is zero, P supplies the full forbidden Wp block. If both are nonzero, the three-channel contraction supplies the whole forbidden target. Thus P-to-Wp must vanish. Any remaining V-to-T or P-to-T channel combines with D to supply the full forbidden T block; if neither exists, the same rank-seven-to-rank-five constant obstruction applies.

Every possible zero/nonzero channel pattern is covered. Together with J=0, this excludes all possible internal images and proves the stated source exclusions.

## 6. Verification record and limits

Running `python verify.py` exits successfully and reports:

    PASS: exact source cohomology identities; all 30 declared bounded atoms;
    11 admissible atoms; 12 declared supports with rank 11 and degree -50;
    complete atomic Hom lists and all 24 support/target Hom dimensions.
    Support completeness is proved by the two-case argument, not enumerated.
    PASS: both first-polar splittings and all universal quadratic/linear channels.

The verifier uses exact arithmetic in Q(sqrt(5)), checks irreducible character orthonormality, checks the declared bounded atom boundary, and checks the finite list of identities and Hom spaces. It does not establish the geometric saturation and constant-connection arguments; those are the separate written checks above. No predecessor envelope or other verifier was run, and no source-instance evaluation, numerical experiment, or selected-model calculation was used.

No revision is required for the stated conclusion. The new contribution is an actual first-polar obstruction for the remaining basepoint-free V+P+D quadratic top block, not a full-label exclusion or a resolution of the global goal.
