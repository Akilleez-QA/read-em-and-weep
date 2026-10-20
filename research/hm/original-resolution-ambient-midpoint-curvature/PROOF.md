Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

# Ambient midpoint curvature and the retained C4 replacement

## Scope and assumptions

This packages the structural result already delivered on 2026-10-18. It is not a new source evaluation. Work is over characteristic zero. The physical derivations V_a commute. All ambient objects are restricted to the same common original-resolution frame before addition and composition. Internal d has degree +1 and commutes with the ordinary ambient Cech differential delta. Totalization signs are kept separately.

Use the established contraction dH+Hd=1-j pi, with cohomology concentrated in internal degree zero. H has degree -1. The inclusion j_i is linear, sends every admitted row endomorphism to an internally closed degree-zero ambient endomorphism, and obeys j_i[X,Y]=-[j_iX,j_iY]. This minus sign is the single prescribed row transpose. Lambda is the admitted regular selector, with Lambda d=0 and Lambda delta=delta Lambda. These are retained geometric/selector premises, not implementation semantics proved here.

Each Gamma_i is the flat, normalized common split connection from the pinned source, on the SAME contraction. Thus V_a d=-[Gamma_i,a,d] and V_a j_i(X)=j_i(V_a X)-[Gamma_i,a,j_iX]. Its edge A_a=Gamma_j,a-Gamma_i,a is tensorial, internally closed, and decomposes as

    A_a=-j_iL_a+d Xi_a,       Xi_a=H_i A_a.

The edge overlap theorem supplies the owned all-chart 5/1 bound for A, the 4/0 bound for H, and 4/1 for j. These bounds are applied occurrencewise, never by merging coincident labels. Actual transported L and U are those in the pinned transgression source, including the trailing transition in U. Frame changes transport the full connection, not a reset reference connection.

## 1. The average connection and its lift homotopy

Set GammaBar=(Gamma_i+Gamma_j)/2, and let nablaBar_a=V_a+ad(GammaBar_a). Both endpoint connections preserve d, so their average does too. For every admitted row X, without assuming Cech closure,

    nablaBar_a j_iX
      =j_i(V_a X)+(1/2)[A_a,j_iX]
      =j_i(V_a X+[L_a/2,X])+(1/2)d[Xi_a,j_iX].

Only INTERNAL closure of j_iX is used. No arbitrary row Cech-closure assertion is made. The two flat endpoints give

    Fbar_ac=-(1/4)[A_a,A_c].

Indeed expand the curvature of Gamma_i+tA. Its constant term is zero; flatness at t=1 makes the linear term minus the quadratic term, leaving t(t-1)[A_a,A_c]. At t=1/2 this is the formula above. The average is generally curved.

## 2. Explicit curvature homotopy

Write B_a=j_iL_a and D_a=dXi_a. Define

    R_ac=-[B_a,Xi_c]-[Xi_a,B_c]
          +(1/2)([Xi_a,D_c]-[Xi_c,D_a]).

All brackets are internally graded: Xi has degree -1, while B,D,A have degree zero. R has degree -1 and R_ca=-R_ac. An equivalent edge-based expression is

    R_ac=[A_a,Xi_c]+[Xi_a,A_c]
          -(1/2)([Xi_a,dXi_c]-[Xi_c,dXi_a]).

Using dB=dD=0 and the graded derivation rule gives

    dR_ac=-[B_a,D_c]-[D_a,B_c]+[D_a,D_c],
    [A_a,A_c]=[B_a,B_c]+dR_ac
             =-j_i[L_a,L_c]+dR_ac.

For Fmid_ac=-[L_a,L_c]/4 this proves

    Fbar_ac=-j_iFmid_ac-(1/4)dR_ac.

Consequently, for admitted row X,

    [Fbar_ac,j_iX]=j_i[Fmid_ac,X]-(1/4)d[R_ac,j_iX].

The same leading owner i is used throughout. Nothing replaces a different owner's Xi or H by owner i. The theorem is a homotopy comparison, not equality of connection coefficients or an inference of flatness.

## 3. The actual C4 slot, with all four signs

Every sum below means precisely

    (a,b,c,d,epsilon)=(1,3,2,4,+1),(1,4,2,3,-1),
                      (2,3,1,4,-1),(2,4,1,3,+1).

There is no full S4 alternation. The pinned source defines

    C4=-(1/16) sum epsilon [U_b,[Fmid_ac,L_d]].

Two anti-homomorphism applications give a PLUS sign for the nested bracket. Substitute the curvature homotopy and define

    E_C=sum epsilon [j_iU_b,[Fbar_ac,j_iL_d]],
    N_C=sum epsilon [j_iU_b,[R_ac,j_iL_d]].

Internal closure of j_iU and j_iL then proves the exact ambient identity

    j_i C4=(1/16)E_C+(1/64)dN_C.                 (C)

E_C has internal degree zero and N_C has internal degree -1. Both are Cech degree two, with the triple's actual leading owner i retained.

## 4. Exact-input stage two, and the retained trace replacement

Define the ambient-input stage-two word Jtilde2=-H delta H delta; its composition with j is the established stage-two lift. For any ambient N of internal degree -1, projection to internal cohomology vanishes both on delta N and delta H delta N. Therefore

    Jtilde2(dN)
      =-H delta H d delta N
      =H delta d H delta N
      =delta H delta N-dH delta H delta N.

The omitted intermediate term is -H delta delta N=0. Applying Lambda yields the positive-sign exact-input identity

    Lambda Jtilde2(dN)=delta Lambda H delta N.

No Cech closure of N or of its row precursor is used. Thus, writing T_row=Lambda Jtilde2 j,

    T_row(C4)=(1/16)Lambda Jtilde2(E_C)
                 +(1/64)delta Lambda H delta N_C.       (T)

Let Pi be the established full ordinary regular comparison, commuting with delta, and p the established global test. The regularity proof below makes Pi_3 Lambda H delta N_C a legitimate degree-three coefficient cochain. Consequently its p-weighted boundary has zero Serre trace. The precise retained scalar replacement is

    SerreTr(p Pi_4 T_row(C4))
       =(1/16)SerreTr(p Pi_4 Lambda Jtilde2(E_C)).        (S)

This uses the actual unchanged comparison and test; it is not a generic assertion that internal exactness has zero trace before HPL. If a partial-prefix comparison is used, the unchanged suffix clearing factors must remain. No replacement of the full kernel by a constant functional is made.

## 5. Covariant domain before the pole ledger

A is the difference of connections in a common original-resolution frame, hence a tensor. Xi=H_i A and dXi=A+j_iL are genuine ambient tensors with the corresponding internal degrees. All brackets above are bundle compositions in this fixed common frame. Thus R and N_C are rational cochains of the correct ambient Hom bundles. No differentiation of a frame is performed in R, E_C or N_C. The covariant identity in section 1 uses the complete connection and its transformation law, so its derivative terms do not introduce a reset-frame anomaly.

The physical current in direction a, A_a and Xi_a all carry character {a}; H and j preserve character. Every displayed complement tuple has four distinct directions. Therefore E_C and N_C have full deck character. N_C has internal degree -1; after H it has degree -2. E_C has degree zero; after its two H factors it also has degree -2. In the standard root-line convention the degree-r character-S coefficient line is O_Y(r*1-2*1_S). Both selected outputs consequently lie in multiplicity copies of O_Y(-4,-4,-4,-4). Cech restriction preserves this covariance. Character extraction is projection in the free cover algebra, including at branch points, never division by an odd generator.

These are genuine sheaf-membership statements prior to clearing. The selector remains subject to its admitted regular degree-compatible hypothesis. No separate bound or tensoriality for an isolated connection coefficient Gamma is invoked.

## 6. Conservative occurrencewise bounds

Use carrier/legal vectors on the exact ordered occurrence tuple. The literal current bounds are L=(5,5)/(3,3), U=(4,9,5)/(2,5,3). Inclusion at the leading owner gives jL=(9,5)/(4,3) and jU=(8,9,5)/(3,5,3). A=(5,5)/(1,1), and Xi=H_iA=(9,5)/(1,1).

For dXi use the exact identity A+jL, giving (9,5)/(4,3). This avoids any new premise about pole orders of the coefficients of d. The R formula then gives

    R on (i,j):          (18,10)/(5,4),
    N_C on (i,j,k):      (35,24,5)/(12,12,3).

Products ADD allowances at the same occurrence. Signed sums take coordinatewise maxima after embedding into the same occurrence list. Let D(x) be the coordinatewise maximum of all one-slot-omission embeddings of x; this is the delta bound. H adds carrier four at its current leading occurrence and no legal allowance. Hence

    delta N_C:           (35,35,24,5)/(12,12,12,3),
    Lambda H delta N_C:  (39,35,24,5)/(12,12,12,3).

The boundary primitive has uniform bound 39/12.

Separately Fbar=[A,A] times -1/4 has (10,10)/(2,2). Thus

    E_C:                 (27,24,5)/(9,10,3),
    delta E_C:           (27,27,24,5)/(9,10,10,3),
    H delta E_C:         (31,27,24,5)/(9,10,10,3),
    delta H delta E_C:   (31,31,27,24,5)/(9,10,10,10,3),
    Lambda Jtilde2 E_C:  (35,31,27,24,5)/(9,10,10,10,3).

The surviving curvature slot has uniform bound 35/10. Signs and rational constants do not change the bounds. Both are below the existing full ordinary 54/29 weights at every occurrence. Full comparison retains each sampled source occurrence and its original target tag. The inherited standard-tag factors are units on that full target intersection; no new standard divisor is introduced. For a degree-three primitive the full comparison has four sampled occurrences, and its boundary has five; none are merged even when labels coincide.

The existing global homogeneous clearing sections and regular partition coefficients therefore give regular compared O(-4)^4 cochains. Multiplication by the established global test p makes the boundary in (T) an admissible Serre-trace boundary, proving (S). Mere numerical pole inequalities would not suffice without section 5's covariance.

## 7. What remains

Only the actual C4 slot is replaced by (S). The full old Q4, M2, full-kernel covariant-adjoint derivative, overlap/current-F families and all previously retained corrections remain. No cancellation against them, rational-divergence certificate, detector value, zero obstruction or source-specific nonzero specialization is asserted. No physical source, model, matrix, polynomial, point, jet or residual evaluation is performed.
