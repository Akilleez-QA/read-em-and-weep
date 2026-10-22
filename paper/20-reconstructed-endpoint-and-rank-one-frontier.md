# 20. Reconstructed endpoint and the rank-one Gauss frontier

The complete quadratic lower endpoint family is now reconstructed from two actual evaluations. Its canonical P4 residue is explicit, and both involution components of the corrected detecting input are nonzero. Separately, the entire rank-two dual-image branch of the extremal (3,1) Gauss profile is excluded. Ten necessary first quotients remain in its rank-one branch.

This chapter records published results through **22 October 2026, 06:38 UTC (02:38 EDT)**. It supersedes Chapter 19's endpoint and Gauss frontiers, not its proofs. The fourth Bockstein, the four-or-five section alternative, and the complete original proof repair remain open.

## 20.1 The canonical residue and its normalization

The lower endpoint target is Cplus/J=P4. It is not the P4 target of a higher Bockstein merely because it has the same representation label. Full restriction to the vertex open is injective; only the subsequent lowest projection removes J=D5.

At a=t², the two actual values from Chapter 19 are zero on X⁴ and c_eta·3k/(Bc)[Y/z] on XY³. Here c_eta is the same nonzero, unevaluated normal scale. The actual cubic sequence

    0 → Wprime O(−3) → D5 O → V O(2) → 0

identifies the latter class with the canonical residue

    −c_eta keA/(Bc) · (XYs²+(c/2)X²t²).

The connecting calculation uses regular lifts p_x=−BY⁴−AcX³Yz+BcXY³z² and p_y^x=AX²Y²/z, with p_y^x−p_x=fY/z and Q(p_x)=Q(p_y^x)=−(eA/2)XY. The canonical apolar projection sends XYs² to (2/3)(XYs²+(c/2)X²t²). Thus its sign and factor are fixed by the actual quotient, not by an arbitrary P4 identification. The socle scalar e remains nonzero and unassigned. [Explicit residue][RES].

## 20.2 Reconstruction of the entire quadratic family

Retain the marked invariant cubic

    f=AX²Y s³+BY³s²t+AcX³st²−BcXY²t³.

Use unnormalized product transvectants in (X,Y) and (s,t), and let H=(f,f)_(1,1). Set

    U(a,h)=pr_P4((h a²,f²)_(4,4)),
    V(a,h)=pr_P4((h a²,H)_(3,3)).

The projection is onto the actual apolar complement of Q(D5). The representation space Hom_G(D5⊗Sym²A,P4) has dimension two, and U,V are independent. Their coefficient rows on X⁴ and XY³ at a=t² have determinant −3715041853440. This is a universal symbolic independence certificate, not a numerical actual-instance rank experiment.

Calibrating against both actual values gives the complete normalized family

    E(a,h)=ke/(ABc) · (U(a,h)/7464960 − V(a,h)/13436928).

The actual family is c_eta E. In particular,

    E(t²,X²Y²)=ke/(3Bc) · s(AX²s+2BY²t) ≠ 0.

This reconstructs the lower endpoint normal-variation family, not the whole original-source endpoint family. All A,B,c,e,k remain unassigned nonzero parameters. The formula retains the source identification I_f from the actual two-input theorem; it does not replace a source quartic by an unmarked negative-coordinate quartic. U,V are a universal tensor basis, not the symmetric and alternating basis. [Full reconstruction][REC].

## 20.3 Both lower involution components survive

For the detecting input a=t², h=X²Y² and b=L_can(a,h)=γa, the canonical decomposition gives

    C/J = H⁰(D,O_D(−2,10)) ⊕ P4,

    [v_h−bζ_a]
      = ( ((r_mid/ν−γr_t)/g²)|D,
          c_eta ke/(3Bc) · s(AX²s+2BY²t) ).

Both entries are nonzero. The first is the absolute reduced-cubic class, whose vanishing would require simultaneously νγ=1/12 and νγ=−1/6. The second is the reconstructed canonical residue. The correction bζ_a lies entirely in Cminus, so it cannot cancel the positive endpoint. γ, ν and c_eta are retained separately. [Two-component theorem][COMP].

The remaining actual operation is still

    q₀v_h=ahζ_a,
    q₀w_h=a(v_h−bζ_a),
    β₄(a,h)=[aw_h] modulo im β₂,a.

Third vanishing ensures that the corrected lower class is killed by a on the cone. It does not construct w_h or determine its final quotient. Simultaneous lower nonvanishing therefore does not imply fourth nonvanishing.

## 20.4 Both parity coefficients are nonzero

After removing the scalar trace from Sym²A, the lower endpoint-family space has one symmetric and one alternating channel under interchange of its parameter D5 and source D5 slots. Both actual coefficients are nonzero. At the pure input, the alternating transvectant vanishes, so the actual nonzero value forces the symmetric coefficient. At the mixed input, the symmetric projection is nonzero but the actual value is zero; hence the alternating contribution must be nonzero and cancel it. The symmetric nonvanishing follows from the invariant Wronskian bound: a degree-eight, dimension-five series containing st⁷ would require at least 36 units of ramification, exceeding its total degree 20. [Parity proof][PAR].

Mr. Slop's **PR665** independently gives the parallel parity-position theorem and intrinsic reconstruction: the actual normal line is the mixed-evaluation kernel graph in the two-dimensional family space, and each of the twelve C5-square secant restrictions has exact rank one with the transported mixed kernel line. This is credited separately from the explicit transvectant calibration above. It does not assert the rank of the full D5-to-P4 map or determine nonsquare secant kernel position. [PR665 proof][SLOP]. No numerical parity-channel ratio or fourth coefficient is claimed.

## 20.5 The absolute normal scale remains unevaluated

The normalized apolar cocycle has diagonal Euler coefficient four, but its action on the Serre section has coefficient one after compatible regular scalar lifts:

    [η_ap σ]=[σ/z],       [η_ap,n]=2[n/z].

For n=σσᵗJ₀, N_C=−n and conic transition I−(ρ_C/z)n, the actual block-Euler field D₀ has

    At_G(D₀)|U=4ρ_C[n/z].

Both residue characters must be retained: normalizing the vertex changes the conic character to μ^(−4). Differentiating only its original μ^(−2) weight would give the wrong factor. [Apolar Euler theorem][EUL]; [actual scale comparison][SCALE].

Define the distinct ambient multiplier κ by

    a At_F(D₀)=q₀κ At_F(D_a),       κ≠0.

Its value is not evaluated at this cutoff. If N=θn and k is boundary-normalized, the two conventions obey

    c_eta_b/k = +2ρ_C/(θκ),
    c_eta_+/k = −2ρ_C/(θκ).

Here η_b is bracket-normalized, whereas η_+ is the positive transition displacement in P_F=P_mid(I+q₀η_+). The boundary is δ_F(N)=−[η_+,N]; thus η_b=−η_+. The actual endpoint contribution uses the positive-transition convention. Treating these scales as equal would lose a sign. No midpoint extension to 3Q or spinor lift to 2Q is inferred.

A related exact transport identity retains the first-normal error E_err:

    Ahat^S=Ahat+(H Ds+Λhat s)Nhat+s E_err+s² E_err Nhat,
    S=I−sNhat,       Nhat²=0.

Cone cancellation does not justify dropping the final two terms at the next normal order. This universal identity does not determine the actual next connection. [Transport proof][TRANS].

## 20.6 The entire rank-two Gauss branch is excluded

The five rank-two dual-image first-quotient shapes were (4,2), (6,2), (8,2), (6,4), and (8,4). Four had already been excluded. The last (8,2) shape had twenty necessary K splittings, reduced to eleven by the doubled-sector argument in Chapter 19. The new single-sector proof excludes all eleven, including the zero-low-scalar branches. Thus the entire rank-two branch is closed. [Complete last-quotient exclusion][G2].

The proof keeps actual image sheaves at every derivative step. In particular the degree-thirteen map W O(−9)→O(4) has an invariant degree-twelve factor: its actual image is O(−8), not O(4), and its kernel is O(−10). It must not be treated as a basepoint-free degree-thirteen series. The remaining kernels reduce to previously excluded kernels or have next derivative rank at most one, contradicting the last established rank-three plateau step. No later derivative is assumed to have rank three.

These five quotient shapes and eleven final K splittings are different counting units. Their exclusion is not a percentage of the full proof search. Rank three for the restricted dual image was already excluded; the rank-one branch remains.

## 20.7 Ten necessary rank-one quotients remain

For rank-one dual cubic image, its saturated line is J=O(e), with e=9 or 11. The actual first quotient has

    A₀=E/E⁻=B ⊕ O(1−e).

Exactly ten necessary shapes survive the new tests:

- e=9: B=O(−4)⊕O(6), O(2)⊕O(4), O(2)⊕O(6), 2O(4), O(4)⊕O(6), W O(3), or W O(5).
- e=11: B=2O(4), O(4)⊕O(6), or W O(5).

This is an overlist, not a realization theorem. B has rank two and embeds in Q(−2), so its ordinary summand degrees are at most six. Section persistence gives the necessary representation inequality

    Wprime+2T6+Sym^(e−6)W
      ≤ χ_G(B(3))+H⁰(B(1))+H⁰(B(−1)).

Exact degree bounds make the representation and target-Hom tests finite. Three equality cases fail the required derivative rank; four further e=11 cases cannot reach the low line O(−e−1). Splitting is justified only after excluding the possible nonsplit equality case. [Ten-quotient reduction][G1].

The whole (3,1) profile is still open. Generic SF≥3, positive-square rank≥27, generic total sections four or five, and finite Smith exponent 4–31 or permanent cokernel are unchanged. Original source recovery, lifting and algebraicity remain separate unresolved objectives.

## 20.8 Reproduction and source boundary

The proof files provide companion scripts for the exact residue, universal tensor reconstruction, both lower components, apolar Euler coefficient, scale signs, parity inequalities, last rank-two exclusion and rank-one overlist. These verify symbolic identities and finite representation consequences. The actual comparison, saturated-image and geometric arguments remain necessary; these are not proof-assistant certificates or selected-instance experiments.

This snapshot includes only the immutable sources below. Later ambient scale calculations, further rank-one exclusions and higher-division developments are not included.

[RES]: https://github.com/Akilleez-QA/read-em-and-weep/blob/32159567cda4d4ec0d5540eb36fe335001436b61/research/hm/order-four-quadratic-load/ACTUAL-NONZERO-ENDPOINT-HAS-AN-EXPLICIT-P4-SERRE-RESIDUE.md
[REC]: https://github.com/Akilleez-QA/read-em-and-weep/blob/32159567cda4d4ec0d5540eb36fe335001436b61/research/hm/order-four-quadratic-load/ACTUAL-FOURTH-INPUT-ENDPOINT-RECONSTRUCTED-BY-TWO-UNIVERSAL-TENSORS.md
[COMP]: https://github.com/Akilleez-QA/read-em-and-weep/blob/32159567cda4d4ec0d5540eb36fe335001436b61/research/hm/order-four-quadratic-load/ACTUAL-CORRECTED-FOURTH-INPUT-HAS-TWO-NONZERO-INVOLUTION-COMPONENTS.md
[PAR]: https://github.com/Akilleez-QA/read-em-and-weep/blob/32159567cda4d4ec0d5540eb36fe335001436b61/research/hm/order-four-quadratic-load/ACTUAL-ENDPOINT-USES-BOTH-PARITY-CHANNELS.md
[EUL]: https://github.com/Akilleez-QA/read-em-and-weep/blob/32159567cda4d4ec0d5540eb36fe335001436b61/research/hm/order-four-quadratic-load/APOLAR-NORMAL-SECTION-HAS-UNIT-EULER-COEFFICIENT.md
[SCALE]: https://github.com/Akilleez-QA/read-em-and-weep/blob/32159567cda4d4ec0d5540eb36fe335001436b61/research/hm/order-four-quadratic-load/ACTUAL-BLOCK-EULER-ATIYAH-CLASS-AND-ENDPOINT-SCALE.md
[TRANS]: https://github.com/Akilleez-QA/read-em-and-weep/blob/32159567cda4d4ec0d5540eb36fe335001436b61/research/hm/order-four-quadratic-load/UNIVERSAL-FIRST-NORMAL-TRANSPORT-RETAINS-THE-ERROR.md
[G2]: https://github.com/Akilleez-QA/read-em-and-weep/blob/140e6d8a7654017188eb2aeaf3cc294ec3b6495c/research/hm/order-four-quadratic-load/EXTREMAL-31-SINGLE-GAUSS-EXCLUSION.md
[G1]: https://github.com/Akilleez-QA/read-em-and-weep/blob/140e6d8a7654017188eb2aeaf3cc294ec3b6495c/research/hm/order-four-quadratic-load/EXTREMAL-31-RANK-ONE-TEN-QUOTIENTS.md
[SLOP]: https://github.com/Akilleez-QA/read-em-and-weep/blob/1cc13d0bf21abc6553c51a48c72896758cbc333a/research/hm/actual-endpoint-parity-consequences/PROOF.md
