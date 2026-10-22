# Actual quartic and quintic interpolation: normalization overlap criteria

Work over C. Retain the exact configuration transport, X,H,C,Y,Z and elliptic fibration from PRIMARY-NORMALIZATION-QUADRIC-INTERPOLATION.md and ELLIPTIC-PUSHFORWARD-SPLITTING.md. This note does not assume projective normality, maximal rank, or general position of the ambient subspace in normalized sections.

## 1. Normalized and ambient section defects

There are no ambient equations for S in degrees at most four, since S contains C and I_C(4)=0. There is no equation in degree five either: I_S(5) is a subspace of the six-dimensional I_C(5), and PR572 at a20545dcc4c0e26dc1bb8af17852db63696ec7b1 proves independence of the six residual sections on S. These arguments are needed; BHM Proposition11's statement that sextics generate the ideal sheaf alone would not justify absence of lower-degree saturated equations.

Let S_m denote the ambient degree-m polynomial space and put P_m=H0(X,mH)/S_m. The two possible E_2 splittings in the companion note give h0(2H)=20 and H1(2H)=0. For m>=3, mH-K_X=mI+(2m-3)F is nef and big: at m=3 it is 3(I+F), and at larger m it is ample by the displayed intersection tests. Kawamata-Viehweg and Riemann-Roch therefore give h0(mH)=5+(15m²-15m)/2 and higher cohomology zero. In particular

 m               2    3    4     5
 h0(X,mH)       20   50   95   155
 dim S_m        15   35   70   126
 dim P_m         5   15   25    29.

For m=4,5 let V_m=H0(Q,O_Q(m))=S_m/qS_(m-2) and W_m=H0(Y,O_Y(mH)). Then dim(V_4,V_5)=(55,91) and dim(W_4,W_5)=(75,105). Applying the snake lemma to multiplication by q gives the exact sequence

 0 -> ker(q:P_(m-2)->P_m) -> V_m -> W_m
   -> coker(q:P_(m-2)->P_m) -> 0.                 (1)

Thus define D_m=coker(q:P_(m-2)->P_m); it is the exact defect W_m/im(V_m), not an assumed complement. If k_m is the kernel dimension in (1), then dim D_4=20+k_4 and dim D_5=14+k_5.

## 2. Residual quartic sections and their possible intrinsic obstruction

Put L_4=O_Y(4H-Z), of degree70 and Euler characteristic25. On X, A_4=4H-C=-I+8F and A_4-Y=-3I+4F have no H0 or H2. The former has H1 dimension30 and the latter H1 dimension55, by Riemann-Roch or relative duality. Explicitly, using E_1=O(-2)^5,

 R1 pi_*O_X(-I+8F)=O(5)^5.

For E_3=pi_*O_X(3I), the same argument as the companion splitting note gives rank15, degree-55 and splitting multiplicities divisible by five. Vanishing of h0(3I+qF) for q<3 forces

 E_3=O(-3)^10 direct_sum O(-5)^5,
 or E_3=O(-3)^5 direct_sum O(-4)^10.

Hence R1 pi_*O_X(-3I+4F)=E_3^* tensor O(-1) has H0 dimension55 and H1 zero in either case. Restriction gives

 0 -> H0(Y,L_4) -> C55 --q--> C30 -> H1(Y,L_4) -> 0. (2)

Consequently h0(L_4)=25+h1(L_4), and vanishing of h1(L_4) has not been proved here. This is a separate possible intrinsic obstruction to quartic evaluation, before asking about ambient sections.

## 3. Residual quintic sections

Put L_5=O_Y(5H-Z)=O_Y(10F). Its degree is100>2g(Y)-2=90, so H1(L_5)=0 and h0(L_5)=55. On X, O_X(10F) has h0=11 and h1=6: pi_*O_X=O and R1 pi_*O_X=O(-5), the latter also following from relative duality with omega_(X/P1)=O(5F). The restriction kernel is O_X(3H-C), whose H1 is50 and other cohomology zero. Therefore

 0 -> C11 -> H0(Y,L_5) -> C50 --q--> C6 -> 0.       (3)

The eleven-dimensional subspace comes from the elliptic base; it must not be confused with the six ambient residual quintics. Formula (3) shows that forty-four additional residual sections occur on Y.

## 4. Exact ambient evaluation cokernels

Let T_m=H0(Z,O_Z(mH)), of dimension50, and J_m=coker[V_m->T_m]. The actual maps are all induced by restriction. Since H1(Y,mH)=0 for m=4,5, quotienting the evaluation exact sequence by im(V_m) yields

 0 -> coker[H0(Y,L_m)->D_m] -> J_m -> H1(Y,L_m) -> 0. (4)

For quintics this specializes to the exact identification

 J_5 = coker[H0(Y,L_5) -> coker(q:P_3->P_5)],        (5)

where the outer source has dimension55 and the inner map is the actual 15-to-29 multiplication. No arbitrary overlap or general-position assumption enters (5).

For quartics, J_4=0 if and only if BOTH the actual 55-to-30 map (2) is surjective and H0(Y,L_4)->coker(q:P_2->P_4) is surjective. The latter target is controlled by the actual 5-to-25 multiplication. In particular, proving only the normalized quartic evaluation map surjective would not establish ambient quartic interpolation.

Finally the ideal sequence for C intersect Q gives the intrinsic interpretations

 J_4 = coker[q:H1(I_C(2))->H1(I_C(4))],
 J_5 = coker[q:H1(I_C(3))->H1(I_C(5))].

Thus (4)-(5) supply exact normalization criteria for the lower-twist cokernels without treating the ambient sections as a general subspace. Surjectivity of these maps, and nonvanishing of the remaining full-adjoint determinant, are not concluded.

## Source boundary

BHM Proposition11 was read directly: it proves ideal-sheaf generation by the ten sextics locally, not an unstated homogeneous saturation or section-surjectivity statement. PR572 independence is the additional degree-five input used here. The surface and configuration dictionaries are pinned in the preceding notes. All new dimensions and exact sequences above are proved symbolically; no selected actual coefficients, numerical ranks, or experiments were used.
