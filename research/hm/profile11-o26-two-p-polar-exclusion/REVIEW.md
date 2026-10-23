# Independent exact-version review: two-P O(26) polar exclusion

## Verdict and scope

**PASS.** The reviewed proof is sound for its stated source-entry exclusion. It excludes U6 at source index 112 and U6/U13 at source index 115, for the two displayed zero-original-defect profile-(1,1) labels. It does not exclude either entire label, any additional source entry, source2, or the global rank problem.

This review binds the following exact files:

- `PROOF.md`: SHA256 `cd0631e411d81ded4bcff090231871a25b7c5f9780b20d8714cf0ebffe56dc15`.
- `verify.py`: SHA256 `6dc13822ac9f11d4278c012e17821538790923167ade316e311b94978866885d`.

Both files were read in full. The verifier was run successfully. The completeness argument, derivative-image sequence, actual saturation, contraction surjectivity, and all multiplicity-row cases were independently checked as mathematical arguments, not inferred from the verifier's output. Neither reviewed file was edited.

The decisive distinction is maintained throughout: an abstract equivariant splitting identifies available bundle maps, but the connection and the constant quotient are those of the actual embedding. No horizontal splitting is assigned to an arbitrary complement.

## 1. Input and source verification

The original inputs are pinned to commit `db51525015bb7c5e825833d550d08dedf6f6ea96` of [Akilleez-QA/read-em-and-weep](https://github.com/Akilleez-QA/read-em-and-weep), under `research/hm/order-four-quadratic-load/`. I read the actual-splitting, strict-top, and endpoint-quotient arguments and directly inspected the relevant JSON records in the available immutable-input snapshots. Their Git blob identities are:

- `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`: `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
- `NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md`: `d7506dae49b4be43230450c4132bd5db91f137ef`.
- `ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md`: `dcacf0bcdef8377c1ed7654e5b82659ea409456e`.
- `one-one-endpoint-necessary-pairs.json`: `fe0afa410d89340d3082dc814277f89fbb582c19`.
- `rank-three-quotient-frontier-144.json`: `8b5971092f9ef762584912609fd5e9301c4e271d`.

Index 112 has A_q=O(-10)+O(-8)+O(26), B_q=O(-28)+O(6)+O(8), defect zero, and includes the tuple (0,0,0,0,1,1,0,1). Index 115 has A_q=W O(-9)+O(26), B_q=O(-28)+W O(7), defect zero, and includes that tuple and (0,0,0,0,1,0,1,0). The frontier records identify these as G3.11.dc58cc54f352 and G3.11.4b6dad66f329, respectively.

Substitution in the catalog formula

    R_2=(c+g+h-1)V+(d+e+g+h)P+(f+g)D

gives R_2=2P+D for both tuples. The remaining rows give precisely Wp O(-5)+O(-8)+O(-10) and Wp O(-5)+W O(-9). Thus the local names U6 and U13 have the claimed meaning; they are not mistaken for the different catalog entries elsewhere named E6 and E13.

The structural dependency snapshots read in this audit are:

- [PR813 divisor reduction](https://github.com/Akilleez-QA/read-em-and-weep/blob/3f99ecf539a3a3da61743df0dff409e54270c865/research/hm/profile11-o26-divisor-reduction/PROOF.md), SHA256 `16d4c27256932b57b3395edd39ec7118e37e7b00757a4d969a7e17b0b2c84bad`.
- [PR799 first-polar obstruction](https://github.com/Akilleez-QA/read-em-and-weep/blob/2172e4a7abbbe232f9f448bea6fa01dee7927460/research/hm/profile11-quadratic-polar-obstruction/PROOF.md), SHA256 `3a55f2c37548c7b05bf0f39f775ab37807c9f852d3601f77271fc0dd052022ed`.
- [PR796 derivative-image lemma](https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md), SHA256 `622763aac375db7e17bc7cab472f1afda0477b0f769371a3b3ef845cd5c9e3b1`.

Only the profile-free image and first-polar statements are required from PR796/PR799. In particular, no interior-stage vanishing H0(E^+)=0 is imported. The positive O(26) image is saturated because the original defect is zero and A_q is the dual of an actual locally free quotient, with the prescribed twist.

## 2. Top map and complete small kernel support

The canonical top F=(2P+D) O(-2) is a direct bundle summand of E, hence saturated in the constant ambient bundle. Its map to the negative summands of A_q is zero by degree. Strict-top vanishing makes the section map 2P+D -> Sym28 W injective.

The common divisor is invariant. Its degree is at most 16 already from the thirteen independent sections; the coarser PR813 list {0,12,20} is therefore valid as well. Degree 12 would require two copies of P in Sym16 W=V+P+2D, and degree 20 would require an injection into Sym8 W=P+D. Neither is possible. Thus p:F->O(26) is onto as a sheaf and on every fiber.

The exact sequence then gives rank K0=12, deg K0=-52, H0(K0(2))=0, H1(K0(2))=A+V+2D and chi_G(K0(3))=Wp-W-S. The vanishing excludes all degrees above -3. For a lower atom U O(-j), the H1(K0(2)) contribution is U tensor Sym^(j-4) W. It is genuine, so dimension and central parity bound the eligible atoms without cancellations.

The verifier checks all 29 dimension/parity-eligible atoms, their exact characters, and the rejection of all but the nine displayed atoms. I independently checked the support-completeness argument using both cohomology budgets:

1. The -W in chi_G(K0(3)) must be supplied by an H1 tail, so one of 1_6 or W_7 occurs. These are the only eligible tails containing W. Each consumes the sole A, so exactly one occurs, and A_4, S_5 and 1_14 cannot occur alongside it.
2. With W_7, its budget A+D and tail W+S leave V+D. The only assemblies are V_4+D_4, V_4+1_8, and Wp_7.
3. With 1_6, its budget A and tail W leave V+2D. An S tail is still required. Among the remaining atoms only 1_8 supplies S, so at least one 1_8 occurs. The residual V+D has the same three assemblies.

The degree-three coefficient is then uniquely the honest representation obtained by adding the tail to Wp-W-S. This yields exactly the six listed splittings, with no unlisted free degree-three summand. All six have rank 12 and degree -52, as the verifier checks. This is a complete two-budget proof, not merely six successful examples.

## 3. Internal image, raw first span and real saturation

The only internal target factor reachable from these six kernels is Wp O(-7). The last source degree is -8; all tail targets have degrees at most -10. For the remaining factor, W_7 has no scalar map to Wp_7 and 1_8 has no linear map because Hom_G(1,Wp tensor W)=0. All smaller source degrees are excluded by ordinary degree. Thus only the scalar Wp_7 endomorphism survives, and J is either zero or the full direct target summand Wp O(-7).

The exact image sequence is valid for the original connection: projecting the full derivative image I of F to Q(-2) has image O(26), and its kernel is precisely the image of the derivative of K0 in (E/F)(-2). Therefore

    0 -> J -> I -> O(26) -> 0,
    0 -> F -> B -> I(2) -> 0.

If J=0, B has rank 14 and degree 2. Any locally free sheaf injecting into a trivial bundle has no positive splitting summand and hence nonpositive degree. Saturation of B is not needed for this contradiction.

For nonzero J, J is a genuine saturated direct summand of (E/F)(-2), while O(26) is saturated in Q(-2). The quotient of (H O/F)(-2) by I is an extension of the respective locally free quotients. Consequently I, and therefore B, is saturated. This proves B=F^+; it does not mistake a generic image for a saturated one. The independent degree check is also correct: B has rank 16 and degree -8, whereas any nonzero invariant saturation defect has length at least 12 and would force positive degree after saturation.

The universal quadratic first-polar map surjects onto B. Hence B(1) is globally generated, and its inclusion in H O puts all degrees in {-1,0}. The exact Euler characters force

    B=(A+D) O+(Wp+T) O(-1).

Here C=H0(B)=A+D is an actual constant eight-dimensional subspace of H. Both C O and B are saturated in H O, so B/C O is an actual saturated subbundle of the genuine constant quotient (H/C) O. It is pure degree -1 and has no global sections.

## 4. Why a full linear block is forbidden

Let bar F be the image of F in (H/C) O. Every local section of bar F has a local lift in F, so its derivative belongs to the projected first span B/C O. This assertion is about the original connection and is unaffected by a noncanonical choice of equivariant splitting.

If bar F contains a nonzero full direct linear block L=U O(-1) of B/C O, then the values and first derivatives of the actual linear columns of L span their nonzero constant coefficient space. Thus this constant span lies generically in B/C O; saturation of B/C O extends the containment as sheaves. It gives a nonzero global section of B/C O, impossible. Equivalently, one can use the local value-plus-first-polar identity directly. This step needs full sheaf containment of L, not merely a generic rank estimate; the surjectivity statements below supply exactly that.

## 5. Three-channel contraction

The two tensor products P tensor W=Wp+T and D tensor W=S+T give exactly the three one-dimensional linear Hom channels P->Wp, P->T and D->T. D->Wp is zero.

For an arbitrary nonzero line ell in W, contraction by its symplectic annihilator maps Sym8 W onto Sym7 W in characteristic zero. Its kernel is the line ell^8. As a bundle map with the stated twists this gives

    Sym8 W O(-2) -> Sym7 W O(-1), kernel O(-10).

This is an everywhere-onto universal map, with no selected point or source evaluation. All three irreducible channels are nonzero: reaching Wp requires P->Wp; omitting D->T would put a rank-five bundle in a rank-one kernel; omitting P->T would put the rank-at-least-two kernel of P->Wp there.

The nonzero-channel graph has edges P--Wp, P--T and D--T. It is a tree. Constant nonzero rescalings of the two source and two target factors therefore realize every choice of three nonzero channel scalars. Every all-three-nonzero map is consequently onto. Projection to T is onto too, and arbitrary pairs of nonzero P->T and D->T coefficients are obtained by source rescalings.

For the isolated channel P->Wp, the additional exact identity W tensor Wp=P identifies the channel with the Euler surjection tensored by Wp. I separately checked this character identity. Hence this channel is also everywhere onto, not merely generically nonzero.

## 6. Exhaustion of multiplicity rows and rank obstructions

Write lambda,mu in the dual two-dimensional P multiplicity space for the Wp and T rows, and nu for D->T. These are all channels.

- If lambda=mu=0, the actual 2P O(-2) subbundle lies in C O. It is saturated in H O: it is a direct summand of F, F is a direct summand of E, and E is saturated. Thus C O/(2P O(-2)) is both torsion-free and rank zero, so it is zero. This contradicts degrees 0 and -16. Equal generic rank alone would not justify this case; the required saturation is present.
- If lambda=0 and nu=0 with mu nonzero, ker(mu) tensor P plus D is an injective rank-nine bundle inside the rank-eight C O. This is impossible without needing any further saturation assertion.
- If lambda=0 and both mu,nu are nonzero, restriction to a constant P multiplicity line on which mu is nonzero, together with D, surjects onto the full T O(-1). Section 4 excludes it.
- If lambda is nonzero and lambda,mu are independent, ker(mu) is a constant P multiplicity line on which lambda is nonzero. It surjects onto the full Wp O(-1) and has no T component. Section 4 excludes it. The same argument applies when mu=0.
- In the remaining case mu is a nonzero multiple of lambda. If nu=0, the common P-row kernel together with D has rank nine inside C O, impossible. If nu is nonzero, any P multiplicity line not killed by lambda, together with D, has all three channels nonzero and surjects onto the entire (Wp+T) O(-1), again impossible.

These cases are exhaustive. The choices of multiplicity lines are formal linear-algebra choices under the hypothetical branch, not evaluations of an actual source model.

## 7. Verification boundary

The standalone verifier successfully checks the 29 bounded atoms, all six displayed supports and their ranks/degrees, all 36 distinct atomic internal Hom channels, both six-entry internal-Hom lists, the first-polar characters, and the three contraction-channel multiplicities. It does not certify geometry; the mathematical audit above supplies the geometric and completeness checks separately.

No selected actual HM/source coefficients, parameters, points, derivative values, instance matrices, source-instance ranks, model experiments, scans, old all-twist envelope, or large computations were used. No external write or publication was performed. The only computations beyond reading and hashing were the stated bounded universal character verification and its single extra Euler-channel identity.

This is an independent written exact-version review, not proof-assistant certification. Subject to the explicit actual-bundle inputs, the source-entry exclusion follows. Both full O(26) labels and the broader open goal remain untouched by this verdict.
