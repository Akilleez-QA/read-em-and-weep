# Exact quartic-current remainder in the algebraic part of Rsharp

## Result

The quartic first-current sector of M0^0+F_12 K^G_34+F_34 K^G_12 does not vanish universally when H/J and E(TF) are held opaque. All 14 mixed L/U assignment sectors are supported; only the all-L and all-U sectors vanish. There is a compact exact decomposition by 2+2 versus 3+1 current type, below. This concerns independent formal traceless currents with H/J kept opaque, not the actual HM obstruction or the realization of these jets by the pinned source.

The following calculation preserves the full gerbe convention. In Rsharp, adding F_12 K^G_34+F_34 K^G_12 to the full-gerbe M0 cancels the b terms because F=b-c. The remaining scalar corrections are -c_12 K^G_34-c_34 K^G_12. The separate E(TF) terms and all H/J terms remain outside the quartic component analyzed here. This result does NOT exclude cancellation against E(TF) after its scalar-solver dependence is expanded, or against source-specific H/J relations. It is not a nonvanishing assertion about the complete Rsharp representative or its obstruction class.

## Definitions

For p=(a,b), let r=(i,j) be the complementary pair. Set

    BL_p=[L_a,L_b],       BU_p=[U_a,U_b],
    M_p=[L_a,U_b]+[U_a,L_b],
    Delta_p=tr(U_a L_b)-tr(U_b L_a).

Then c_p=Delta_p/4 and K^G_p=(BL_p+BU_p+M_p)/4. Write d(V,W)=tr(VW). Let Q4 denote the quartic first-current component of the algebraic term M0^0+F_12 K^G_34+F_34 K^G_12, with E(TF) held opaque, after the preferred Q simplification in `m0-current-selected-kernels.md`.

## Exact decomposition

Write Q4=R22+R31, where

    R22 = ( [BU_12,BL_34]+[BU_34,BL_12] )/32
          -(Delta_12 M_34+Delta_34 M_12)/16,              (1)

and

    R31 = (1/32) sum over (p,r)=(12,34),(34,12) {
          [U_b,[L_a,BU_r]]-[U_a,[L_b,BU_r]]
          +[L_a,[U_b,BL_r]]-[L_b,[U_a,BL_r]]
        }.                                               (2)

R22 has two U and two L inputs. R31 consists of the three-U/one-L and one-U/three-L parts.

For a direct derivation, the contribution of Q_p's four trace terms, multiplied by 16, is

    d(U_a,BU_r)L_b-d(U_b,BU_r)L_a
       +d(L_b,BL_r)U_a-d(L_a,BL_r)U_b.

Combine it with -Delta_p(BL_r+BU_r), from the corresponding c correction. The identity

    [V,[W,Z]]=2(d(V,W)Z-d(V,Z)W)

turns this sum into half of the braces in (2). The remaining -Delta_p M_r term and the original quadratic K/X brackets give (1). This proves the decomposition without source arithmetic.

## Assignment sectors

An assignment specifies for each coordinate 1,2,3,4 whether only L_i or only U_i is kept. Every term is multilinear in these four coordinate groups.

- LLLL and UUUU: zero.
- UULL: [BU_12,BL_34]/32.
- LLUU: [BU_34,BL_12]/32.
- The other four two-U/two-L assignments have one U in each pair. For each pair p, write V_p=[U_i,L_j], t_p=d(U_i,L_j), and epsilon_p=+1 if U occupies the first coordinate of that pair and -1 if it occupies the second. Their exact formula is

      -epsilon_12 epsilon_34 (t_12 V_34+t_34 V_12)/16.

- For three U and one L, let the pair containing the L be p=(a,b), and let the complementary pair r be all U. If the L is in position a, the sector is [U_b,[L_a,BU_r]]/32. If it is in position b, it is -[U_a,[L_b,BU_r]]/32.
- For one U and three L, let the pair containing the U be p=(a,b), and let r be all L. If the U is in position a, the sector is -[L_b,[U_a,BL_r]]/32. If it is in position b, it is [L_a,[U_b,BL_r]]/32.

None of the 14 displayed mixed-sector formulas is the zero multilinear map on sl2. Thus c-term cancellation does not prune the mixed assignment sectors completely; it reorganizes their kernels.

## Formal survivor and exhaustive multilinear control

With abstract standard sl2 basis h,e,f satisfying [h,e]=2e, [h,f]=-2f, [e,f]=h, take

    L_1=h, L_2=e, U_3=h, U_4=f,
    U_1=U_2=L_3=L_4=0.

Both c scalars and all preferred-Q quartic trace terms vanish. The surviving Q4 is

    [[U_3,U_4],[L_1,L_2]]/32 = h/8.

This is a formal Lie-algebra control, not an evaluated HM transition or source coefficient.

`test_rsharp_quartic_remainder.py` compares 32 times the original quartic expression to 32(R22+R31) on all 16 assignments and all 3^4 choices of formal sl2 basis vectors: 1296 cases. It also checks that R31 vanishes in the two-U sectors and R22 vanishes outside them, plus the explicit survivor. All three test methods pass. The assignment-support test confirms each mixed assignment has nonzero instances; the two pure assignments do not.

No HM data are imported. No physical polynomial, source jet, residue, detector, partition, or coefficient has been evaluated. No physical-cost improvement follows from this decomposition alone.

## Dependency scope

Companion references are identified by basename. A referenced file not supplied with this collection is an external prerequisite, not an embedded proof or a verified relative link. The reading order and unresolved conditions are listed in `proof-notes-index.md`. Reported test results describe the source audit; this proof copy does not by itself constitute a new test run.
