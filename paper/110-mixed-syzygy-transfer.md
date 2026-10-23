# A canonical mixed syzygy detects alternating transfer

**PR1089 update, 23 October 2026:** [Actual residual Koszul lifts](112-global-alternating-vanishing.md) now prove combined T-rank four and κ=0 in all remaining mechanisms. The odd radical is not nullhomotopic; K3/F3 has character 2W′+3S. The unselected rank-three/rank-four interface below records the earlier checkpoint, not the current frontier. Zero R and hence zero full bilinear transfer remain unexcluded.


**23 October 2026 · PR1085, read in full**

[Immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/7d1c49ea66c54039f6adbbc27cac54222961784e/research/hm/source2-pure-v-mixed-syzygy/PROOF.md), blob `2988fbbb5ed316124769c7157c0592e4c87aaa0f`.

## Canonical quotient and exact identity

Retain actual source2 nonzero pure-V compatible-radical hypotheses and only the fixed negative two-space W. Put K3=ker Q3∩ker j3. Actual Q commutation, W I4=0 and radical intertwining imply F3=W im h⊂K3, with character W′+2T.

For s:I4→P_h inverse to Q2 and an equivariant right inverse G_Q of Q2, set k_b=G_Q T_b s. The relation

    H(l,m;r)=X_l k_(mr)−X_m k_(lr)

lies in K3 and is alternating in l,m. Factoring through the fixed determinant tensor gives H_r. Changing G_Q changes H_r only by an I3-valued term, so its class defines a canonical map

    H̄: W⊗I4 → K3/F3.

The pairing Ψ(n,[v])=hY_n v is well-defined with target I2: radical intertwining gives the target, and hT_a h=0 kills F3. The literal comparison, without exchanging directions across any homotopy, is

    hY_n H(l,m;r)=B(nl,mr)−B(nm,lr).

With Alt B=(B−Bᵒᵖ)/2=κL_[a,b]* and the unscaled Hamiltonian bracket, the exact identity becomes

    Ψ(n,H̄(r,p))=4κ L_(nr)*p.

Both symmetric transfer channels cancel. The reason is the exact trivial kernel of Sym²(Sym²W)→Sym⁴W together with Hom_G(P,D)=0, not a general assertion that every symmetric bilinear map factors through multiplication. The coefficient four follows from [nl,mr]−[nm,lr]=4ε(l,m)nr. No actual coefficient is numerically normalized.

## Conditional rank obstruction and limit at this checkpoint

W⊗I4=W′+T, and its W′ constituent pairs trivially with I2. If κ≠0, the identity forces the T constituent to inject into K3/F3. K3 then contains at least three T copies, including the two in F3.

Consequently the actual T-multiplicity map of (Q3,j3), with domain dimension six and target dimensions three plus one, has rank at most three. Equivalently its fourth exterior power vanishes. This is a conditional structural rank restriction, not an evaluated source-instance matrix.

If an additional theorem established combined rank four, it would force κ=0; if also R=B(a,a)=0, it would force B=0. **PR1085 does not establish that rank, select κ, or exclude the zero full-transfer case.** It neither extends h to a graded module map nor supplies cross-direction commutation. Endpoint nine is already excluded by PR1082; endpoint sixteen remains necessary with two unresolved projection mechanisms. There is no new source-pair cut or positive-component solution.
