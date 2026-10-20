Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

Supporting dependency only: this complete source text is not a fresh result of this packet.

# Structural proof of primitive A on all six pinned carriers

## Theorem and scope

For the exact rational matrices decoded from the pinned model, on each of its six denominator localizations,

    gamma H0 + I P + H1 delta = Id15.

This proof does not assume A or the historical 1350-entry computation receipt. It composes source-specific sparse elimination and incidence lemmas, each established independently of A. It also proves the full elementary contraction identities below. The separate determinant-volume argument can consequently use A as a theorem rather than an imported historical premise.

The model has SHA256 635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926 and Git blob fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761. Immutable source: https://github.com/Akilleez-QA/read-em-and-weep/blob/31f5b074f7c212f9bb6498ed2920e0c93cc781a9/research/hm/null-operator-compiler/hm-pinned-model.json. The decoder divides H0,H1 by dh, I by di and P by dp. These denominator records coincide on each carrier.

All statements are algebraic for these decoded matrices over the stated commutative localizations, with v0=1. This does not establish the external physical-frame identification, all-chart geometric pole bounds, a detector value, obstruction vanishing, or algebraicity. No historical execution is reattested.

## 1. Independently established ingredients

The constituent proofs and their source-binding controls establish:

1. **Retraction.** H0 gamma=Id5 and H0=gamma_F^{-1} E_F^t. Five sparse four-cycle solves and one triangular solve identify all six stored H0 arrays. No delta, I, P, or A identity is used to prove this inverse.
2. **Projection.** P=J^{-1}E_D^t(Id15-gamma H0), where J=I[D,:] is invertible. Every stored P coefficient is identified by the sparse inverse formulas. Hence P gamma=0.
3. **Common complex.** delta gamma=0. The two-edge incidence paths pair with opposite signs and reversed scalar labels; the proof is polynomial and needs no localization or primitive map.
4. **Cycle inclusions.** delta I=0. The literal I arrays are two solutions of a universal sparse kernel recurrence on the primary carriers, and of a triangular kernel solve on the auxiliary carrier. This proof assumes none of H0, P, H1, A, or exactness.
5. **Complementary inverse.** With S the eight-coordinate complement of F union D, M=L delta E_S and T=E_S^t H1 W, the sparse inverse recurrence identifies all stored H1 coefficients and proves TM=MT=Id8. Neither I nor A is used in this solve.

The literal zero and normalization records additionally give

    I[F,:]=0, H1[F union D,:]=0, P[:,S]=0,
    I[D,:]=J, P[:,D]=J^{-1},
    H0 I=0, H0 H1=0, PI=Id2, PH1=0.

The primary J is diag(1,v_c); auxiliary J is diag(1,-v4/v1^2). Its factors are units on the respective recorded denominator localization. All these support claims are checked from inert records; they are not inferred from A.

## 2. Evaluation and pivot identities without A

Write the ten coordinates as two blocks of five and let

    ev(Y,Z)=(sum_i v_i Y_i, sum_i v_i Z_i).

The pinned delta formula from the incidence proof is

    Y_i=v_(i-1) A_(i+2)-v_(i+1) A_(i-2)
         +v_(i+2) C_(i+1)-v_(i-2) C_(i-1),
    Z_i=v_(i+2) B_(i+1)-v_(i-2) B_(i-1)
         +v_(i-1) C_(i+2)-v_(i+1) C_(i-2),

with indices modulo five. Reindexing each weighted sum gives zero. For example the two coefficients of A_k in sum_i v_iY_i are v_(k-2)v_(k+2) and its negative; the C_k coefficients are v_(k-1)v_(k+1) and its negative. The B_k and C_k coefficients in sum_i v_iZ_i cancel in the same two ways. Thus ev delta=0 directly, before localization.

For pivot p, eta has columns e_p/v_p and e_(5+p)/v_p. W has columns e_(5h+r)-(v_r/v_p)e_(5h+p) in the cyclic nonpivot order, and L selects those nonpivot coordinates. Coordinate substitution proves

    LW=Id8, ev W=0, L eta=0, ev eta=Id2,
    WL+eta ev=Id10.

All pivot factors are units on the corresponding carrier localization. Because the two pivot columns of H1 are literal zero, H1 eta=0 and H1=H1WL. Because ev delta=0, delta=WL delta. These identities are independent of A.

Since H1 has rows only in S, its definition of T now gives

    H1=E_S T L.

No actual matrix product needs evaluation for this identification: H1W is the nonpivot submatrix of H1 because its pivot columns vanish.

## 3. Direct proof of A

Let z be an arbitrary vector of length 15 over the carrier localization. Set

    r=z-gamma H0 z-I Pz.

First, r_F=0: E_F^t gamma H0=E_F^t and I_F=0. Second, the proved projection formula gives

    J Pz=E_D^t(z-gamma H0 z),

so r_D=0. Therefore r=E_S r_S for a unique eight-coordinate vector r_S. No exactness assertion has been assumed.

The independently proved equations delta gamma=0 and delta I=0 give delta r=delta z. Hence

    H1 delta z
      =E_S T L delta r
      =E_S T (L delta E_S) r_S
      =E_S TM r_S
      =E_S r_S=r.

Substituting the definition of r proves gamma H0+IP+H1 delta=Id15. This proof uses no A-dependent determinant, contraction, or cohomology comparison. The coordinate complement and its inverse are established by the sparse solves themselves.

Equivalently, the independently invertible basis N=[gamma,I,E_S] conjugates the A defect to three lower blocks T Ldelta gamma, T Ldelta I, and TM-Id8, plus the previously removed Pgamma block. Every one of those blocks is now established zero by an A-independent ingredient. The direct vector proof above avoids relying on that normal-form theorem as a black box.

## 4. Full contraction as a consequence

The pivot decomposition and the complementary inverse give

    delta H1 = delta E_S T L
               =W (L delta E_S)T L
               =W MT L=WL=Id10-eta ev.

Together with the ingredients, the full list is

    H0 gamma=Id5, gamma H0+IP+H1 delta=Id15,
    delta H1+eta ev=Id10, ev eta=Id2,
    PI=Id2, delta gamma=0, delta I=0, ev delta=0,
    Pgamma=0, PH1=0, H0I=0, H0H1=0, H1eta=0.

Thus the four-term complex has the displayed explicit contraction onto the rank-two middle module on each carrier. The elementary split-basis identities follow as well:

    [gamma,I,H1W]^{-1}=[H0;P;Ldelta],
    [W,eta]^{-1}=[L;ev].

For the first identity, multiply the factors abstractly using the displayed relations. Its lower-right block is Ldelta H1W=LWLW=Id8; the other off-diagonal blocks vanish. This is an algebraic consequence of the proved relations, not a new physical source calculation.

## 5. Determinant consequence and revised dependency frontier

The separately proved determinant-line calculation has lambda_c=det[gamma,I,H1W]/det[W,eta]=1 on all six specific carriers. Its actual sparse-minor equalities were independent of A; its change-of-basis implication used the contraction. Section 3 now discharges that premise without a historical receipt. Therefore

    det(P_i I_j)=1

on every common carrier localization. Under the already specified reciprocal root-line/frame identification, the physical row transitions also have determinant one. Their rank-two adjugates are genuine inverses, and their logarithmic currents are traceless for the specified derivations.

Neither the historical primitive-A computation nor the separate historical determinant computation is required for these algebraic conclusions. Source authentication and decoder semantics remain explicit; arithmetic implementation, ambient geometric interpretation, full all-chart regularity, actual terminal values, and global obstruction or algebraicity questions are distinct. This completes a structural replacement of those two imported finite-model identity premises, not the entire research goal.

## Evidence classification

The proofs derive formulas by sparse elimination and pair cancellation in universal commuting symbols. Their metadata checkers bind those handwritten formulas to the complete relevant pinned arrays; they do not evaluate physical matrices, jets, or detectors. Separate invented controls exercise signs and logical dependencies. Independent reviews accompany the ingredient proofs and this composition. Reproducibility manifests identify exactly the bytes reviewed; hashes establish identity, not mathematical truth by themselves.
