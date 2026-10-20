Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

Supporting dependency only: this complete source text is not a fresh result of this packet.

# Exact graded overlap insertion reduction

## Result

Under precisely the common-complex/contraction/frame premises of dependencies/common-connection.md, the overlap terms admit an exact selected reduction. Put d=d_End, G=Gamma_End, J1=H delta j (unsigned), J2=-H delta J1. All ambient maps are restricted to the same original-resolution frame before addition/composition. Define on edges

    Aij=Gamma_j-Gamma_i,
    aij=j_i(-theta_ij),    theta_ij=g_ij^-1 V(g_ij),
    Xi_ij=H_i,0(Aij),      zeta_ijk=Xi_jk-Xi_ik+Xi_ij.

The first occurrence Xi_jk is restricted as an ambient degree-minus-one map, not conjugated as a row matrix. Then A=a+dXi. Define first-face insertion operators, for X of internal degree r,

    (C0 X)_(i0...ip+1)=[a_i0i1,X_(i1...ip+1)],
    (R X)_(i0...ip+1)=Xi_i0i1 X_(i1...ip+1)-(-1)^r X_(i1...ip+1) Xi_i0i1,
    (W X)_(i0...ip+2)=zeta_i0i1i2 X_(i2...ip+2)-(-1)^r X_(i2...ip+2) zeta_i0i1i2.

No first-face sign is suppressed. C0 has bidegree (1,0), R has (1,-1), and W has (2,-1). Exact identities are

    C=C0+dR+Rd,
    delta R+R delta=W,
    d zeta=-delta a.

For any row input Z of degree n (not assumed closed), let Delta=delta_row. The actual two overlap insertions satisfy

    L H C J1 Z+L H delta H C j Z
      = L H C0 J1 Z+L H delta H C0 j Z
        +L R J1 Z+L H W j Z
        -delta(L H R j Z)-L H R j(Delta Z).                 (Reduction)

This is not an assertion that the homotopy part vanishes. It replaces both actual overlap insertions by their cohomology-current insertions, two explicit homotopy corrections, a boundary, and a nonclosed-input correction. This author theorem itself proves no separate regular boundary domain. The independently reviewed conditional domain theorem is supplied separately in DOMAIN.md; without its additional premises the new boundary cannot be discarded under Serre trace. The selector term -L G J2, the complete ten-term baseline, both Fk branches, moving selector/restriction/input terms, and outer weights remain exactly as in the preceding packet.

## Cohomology sign and transpose

The SAME common frames have cohomology columns A_i=I_i diag(nu_i,nu_i^-1), projection B_i and transition Gij=B_i A_j=gij^t. Compatibility with the differential gives d(Aij)=0. The induced column connection difference is -V(Gij)Gij^-1=-(gij^-1 V(gij))^t=-theta_ij^t. Since pi_i(F)=(B_i F A_i)^t, pi_i(Aij)=-theta_ij, not its transpose and not +theta. This uses common frames, not the prescribed local arrays. The degree-zero contraction gives Aij=j_i pi_i(Aij)+d H_i Aij because d Aij=0. Thus the stated Xi is canonical for this chosen leading-owner contraction.

## Independent row-transport sign check

For a closed degree-zero X, the transpose makes pi_i([j_i(-theta),X])=theta pi_i(X)-pi_i(X) theta. The dXi part projects to zero on such X. In particular pi_i(CjR)=[theta_ij,t_ij R] on the first face, where t_ij R=g_ij^-1 R g_ij. Therefore the preceding connection theorem gives Delta'R=-pi CjR=-[theta_ij,t_ij R]. This is exactly the direct derivative V(g_ij^-1 R g_ij) for coefficient-constant R. It independently fixes the minus and the single transpose without treating j as a multiplicative row-algebra homomorphism.

## Graded insertion calculation

The differential is a graded derivation of composition. With |Xi|=-1 and |X|=r,

    d[Xi,X]_gr=[dXi,X]-[Xi,dX]_gr.

This proves C=C0+dR+Rd on every face. In particular R is an anticommutator on internal degree -1 and an ordinary commutator on internal degree 0 or -2. The signs are internal-degree signs; Cech degrees do not enter this formula because the packets use d delta=delta d and insert totalization signs separately.

For delta R+R delta, all faces after the first two cancel with their ordinary alternating signs. The three surviving terms are [Xi_12-Xi_02+Xi_01,X_2...]_gr, proving W. This is the actual first-face owner formula. It is not permissible to replace Xi_jk by H_i(A_jk): Xi_jk was formed with H_j. Finally delta A=0 by telescoping common connection differences, hence d delta Xi=delta(A-a)=-delta a. Although Delta theta=0, delta a need not vanish: a is the first-owner lifted cochain, and j changes owner.

## Derivation under the actual HPL homotopies

For all n, the unsigned J1 obeys dJ1=delta j-jDelta. (The signed stage-one inclusion is (-1)^n J1; stage two is J2 for every n.) Since RJ1 has internal degree -2, the projection in Hd=1-P-dH is zero there. Thus

    H C J1=H C0 J1+RJ1-dH RJ1+H R delta j-H R jDelta.

For the second insertion, dj=0 and Rj has internal degree -1, again with zero projection:

    H C j=H C0 j+Rj-dH Rj,
    H delta H C j=H delta H C0 j+H delta Rj-delta H Rj+dH delta H Rj.

Here d commutes with ambient delta; H was never commuted through delta. Applying Ld=0, and the admitted L delta=delta L, adding the equations and using delta R+R delta=W yields (Reduction). This retains every nonclosed-input projection term and all deleted-prefix owners.

For the actual degree-two endpoint Z_a=(theta_b cup s_q-s_q cup theta_b)/2, the last correction can use the already proved Delta Z_a=-(theta_b cup F_q+F_q cup theta_b)/2; Z_b has the opposite sign. The correction therefore becomes +LHRj(theta_b cup F_q+F_q cup theta_b)/2 for Z_a. This substitution removes s_raw ONLY from this named correction. The other terms in (Reduction) still depend on the original endpoint input.

## Further literal cohomology-insertion simplification

Write h=h_i and e=A_i B_i. Since h a=a h=0 and e a=a e=a for a=j_i(-theta), the actual End homotopy gives, on an arbitrary degree-r ambient X,

    H_i[a,X]=(-1)^r a X h-h X a.

For the first family X=(J1 Z)_(i1...), r=-1, so

    (H C0 J1 Z)_(i0...)=j_i(theta_i0i1) X h_i+h_i X j_i(theta_i0i1).

For the second family's innermost X=j_i1(Z_tail), r=0,

    (H C0 jZ)_(i0...)=-j_i(theta_i0i1) X h_i+h_i X j_i(theta_i0i1).

The shifted-owner X is not replaced by j_i of its row transport. Its exact-vector difference matters before H. These identities remove the outer End H from each C0 insertion; no actual matrix-polynomial product has been evaluated.

## Precise negative controls and limits

Dropping homotopy exactness inside H loses LRJ1+LHWj-delta LHRj-LHRjDelta, not merely an Ld boundary. Dropping zeta is unjustified: Delta theta=0 does not give delta j_i(theta)=0, and d zeta=-delta a is its exact defect. Treating a degree-minus-one R insertion as an ordinary commutator changes its X Xi sign. Treating Z as closed loses the last term of (Reduction). Transposing theta a second time changes the cohomology identification. Suppressing -LGJ2 leaves the selector connection missing, as before.

Equation (Reduction) is purely formal/static. No actual source/model/owner/jet values, physical matrix products, physical experiments were used. No cancellation with baseline, retained-test value, global regularity for separated terms, or complete divergence/obstruction conclusion follows. Immutable common-connection source: commit 4ae1ba6081db6563389d5ff78597cf2e98ecc04f of Akilleez-QA/read-em-and-weep, research/hm/null-common-split-connection/PROOF.md. Bundled premises: dependencies/common-connection.md, hpl.md, raw-first-order.md (especially sections 3, 5 and 8), and endpoint.md. Frozen bytes and supplied-source hashes are recorded in pins.json.
