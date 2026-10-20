Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

Supporting dependency only: this complete source text is not a fresh result of this packet.

# A collected rank-two reduction of the complete baseline jet family

## Result and evidence boundary

The complete algebraic baseline admits the exact decomposition R_alg = Q4 + S2 below. Q4 is the EXISTING quartic remainder R22+R31. The new bounded step is to collect every normalized-second-jet term from both preferred Q kernels and the entire mixed Moyal block into S2, eliminating all nested jet/current brackets and all eight YH/ZH intermediate matrices. This is a formal algebraic rearrangement, not a universal cancellation or a physical-cost improvement.

Read before deriving: latest PR1 through comment 6250367808; the corrected full-sign alternating primitive; m0-current-selected-kernels.md including preferred equation (3'); rsharp-quartic-current-remainder.md; the baseline and current-kernel independent audits; and the complete-remainder normal form. The exterior/Fierz cancellation already used by the full-sign primitive is not claimed again. No actual source/model/owner/jet values, matrix-polynomial products, experiments or publication were performed.

## 1. Exact input contract

Use the old current-kernel index convention 1,2,3,4 (subtract one to match the new complete-remainder note). A=g_ij, B=g_jk, G=BA. At the first row endpoint set

    L_a=A^-1 V_a A,
    U_a=A^-1 B^-1(V_a B) A,
    T_a=L_a+U_a,
    H_ab=tf(A^-1 V_a V_b A),
    J_ab=tf(A^-1 B^-1(V_a V_b B) A).

H here is a normalized second jet, NOT the HPL homotopy. All these symbols are traceless 2-by-2 matrices over a commutative Q-algebra. H_ab=H_ba and J_ab=J_ba refer to the existing commuting physical derivative convention. Write d(X,Y)=tr(XY).

Use precisely the four signed complementary entries

    (ab,cd,e)=(13,24,+1),(14,23,-1),(23,14,-1),(24,13,+1).

Define scalar current contractions

    a_ab=d(T_a,T_b)-d(L_a,L_b)
        =d(U_a,U_b)+d(U_a,L_b)+d(U_b,L_a),
    b_cd=d(T_c,T_d)-d(U_c,U_d)
        =d(L_c,L_d)+d(U_c,L_d)+d(U_d,L_c).

Then the ENTIRE second-jet family is

    S2 = (1/8) sum e {
          [J_ab,H_cd] + a_ab H_cd + b_cd J_ab
          - d(U_a,H_cd)L_b - d(U_b,H_cd)L_a
          - d(J_ab,L_c)U_d - d(J_ab,L_d)U_c
        }.                                                   (A)

There is no newly discarded term in R_alg=Q4+S2. In particular Q4 includes the old -c_P k_Q,ik-c_Q k_P,ik contribution, obtained from the full-gerbe baseline plus both Fk terms using F=b-c. The central gerbe term vanishes only after the existing exact tracefree projection. Neither F nor the raw scalar solution is replaced by an endpoint value.

## 2. Universal proof

Cayley-Hamilton and polarization give XY+YX=d(X,Y)I for traceless 2-by-2 matrices. Expanding commutators with that identity gives

    [X,[Y,Z]]=2(d(X,Y)Z-d(X,Z)Y),
    [[X,Y],Z]=2(d(Y,Z)X-d(X,Z)Y).                  (B)

These are the Pauli/Fierz contraction identities; no generic-basis assumption, division by a Gram determinant, or chosen eigenbasis is needed.

Expand ONLY the YH/ZH terms in the preferred equation (3') of m0-current-selected-kernels.md, retaining the outside 1/4 and their inside 1/4. Collecting each jet produces the following complete coefficient inventory:

    J_13: +([[J_13,U_4],L_2]+[[J_13,U_2],L_4])/16
    J_14: -([[J_14,U_3],L_2]+[[J_14,U_2],L_3])/16
    J_23: -([[J_23,U_4],L_1]+[[J_23,U_1],L_4])/16
    J_24: +([[J_24,U_3],L_1]+[[J_24,U_1],L_3])/16

    H_24: +([U_1,[L_3,H_24]]+[U_3,[L_1,H_24]])/16
    H_23: -([U_1,[L_4,H_23]]+[U_4,[L_1,H_23]])/16
    H_14: -([U_2,[L_3,H_14]]+[U_3,[L_2,H_14]])/16
    H_13: +([U_2,[L_4,H_13]]+[U_4,[L_2,H_13]])/16.

Equivalently the complete nested contribution is

    (1/16) sum e {
       [[J_ab,U_d],L_c]+[[J_ab,U_c],L_d]
       +[U_a,[L_b,H_cd]]+[U_b,[L_a,H_cd]]
    }.

Apply (B). For each signed complement the result is 1/8 times

    (d(U_d,L_c)+d(U_c,L_d)) J_ab
      -d(J_ab,L_c)U_d-d(J_ab,L_d)U_c
    +(d(U_a,L_b)+d(U_b,L_a)) H_cd
      -d(U_a,H_cd)L_b-d(U_b,H_cd)L_a.

The existing full mixed Moyal block is

    (1/8) sum e { [J_ab,H_cd]
                  +d(U_a,U_b)H_cd+d(L_c,L_d)J_ab }.

Adding it gives (A) with the stated a,b. Every other term of the complete preferred baseline is first-current quartic or a noncentral gerbe correction; those are exactly the pre-existing Q4 after adding both Fk branches. This proves the complete decomposition.

## 3. Direct contraction with a local dual matrix

For any formal traceless dual matrix V in the SAME first-endpoint frame, define

    W_H,ab(V)=[V,J_ab]+a_ab V
                  -d(V,L_b)U_a-d(V,L_a)U_b,
    W_J,cd(V)=b_cd V-d(V,U_d)L_c-d(V,U_c)L_d.

Cyclicity of the single-frame trace yields the exact identity

    d(V,S2)=(1/8) sum e {
                   d(H_cd,W_H,ab(V))+d(J_ab,W_J,cd(V)) }.

The [V,J_ab] term retains all H/J-bilinear dependence; this is not separate linearity in both jets at once. The formula supplies a jet-adjoint contraction for any already-authenticated local dual input. It does not authenticate or shrink the global detector family.

## 4. Transport and stopping point

All B-edge jets/currents retain the exact A^-1(...)A transport before any pairing. Products in (A) never mix untransported owners. The derivation makes no derivative of a moving conjugation and hence introduces no frozen-frame shortcut. Once the normalized symbols are formed, the identity is equivariant under simultaneous conjugation: traces are invariant and every vector/bracket conjugates. This is not a claim that physical derivatives transform tensorially under an arbitrary new coordinate-dependent trivialization; such a change must first transform the normalized physical jets correctly.

The formula can be substituted only for R_alg inside the complete normal form. Actual Ccur terms, test/selector coupling, overlap/homotopy insertions and the scalar-free K Delta Z family all remain. No boundary or rational divergence has been exhibited here. The previously known formal second-jet and mixed quartic survivors are consistent with (A); rank two does not force S2 or Q4 to vanish. Local three-dimensional traceless fibers do not reduce the thirty global residual tests. No new pole-domain, execution, resource or retained-value claim follows.

## Primary context

C. C. Nishi, Simple derivation of general Fierz-type identities, Am. J. Phys. 73 (2005), 1160-1163, section II: https://arxiv.org/html/hep-ph/0412245v4. The paper supplies the matrix-completeness viewpoint, including Pauli/SU(2); (B) and its precise normalization are proved directly above rather than imported from a spinor-sign convention.

Repository context: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6250367808. The complete-baseline and preferred-Q source formulas are the existing local proof-foundation records; (A) is a newly derived bounded collection of their full jet family; see REVIEW.md for the independent audit and its precise scope.
