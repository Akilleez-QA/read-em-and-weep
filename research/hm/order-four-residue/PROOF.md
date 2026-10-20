# The three order-four summands and their sextic residue obstruction

Work over C on P^4. Let F be the normalized Horrocks–Mumford bundle, B=End_0(F), E=F(3), V=H^0(E), and D=det V. Let C be the union of the twenty-five disjoint transverse evaluation-degeneracy lines. Its evaluation cokernel is i_*ell, with ell of degree -1 on each line. Write S_d=H^0(O(d)). Let u∈S_2 and v∈S_3 be nonzero and relatively prime. All ideal products below are sheaf products unless graded pieces are explicitly indicated.

## 1. The entire order-four coefficient has three different summands

For the actual collision coefficient in this section, take u=t_2 and v=t_3 as in PR437, retaining its paired character and filtered coefficient conventions. Sections 2–4 apply to arbitrary globally coprime forms of these degrees; they do not identify an arbitrary pair with that fixed upstairs collision ideal. The exact decomposition at order four is

    B(-3)K_3 ⊕ B(-4)K_2 ⊕ B(-5)K_1,
    K_3=(v,u²),   K_2=K_1=(u,v).

The regular sequence (u,v) gives resolutions

    0→B(-10)→B(-6)⊕B(-7)→B(-3)K_3→0,
    0→B(-9) →B(-6)⊕B(-7)→B(-4)K_2→0,
    0→B(-10)→B(-7)⊕B(-8)→B(-5)K_1→0.

The respective syzygies have entries (u²,-v), (v,-u), and (v,-u). Since B is locally free, tensoring introduces no Tor. Serre duality identifies H²B(-6), H²B(-7), H²B(-8) with the duals of H²B(1), H²B(2), H²B(3). These vanish by PR455 and PR167. Hence the H² of each quotient is exactly the kernel of the H³ syzygy map, with no omitted H² generator contribution. Dualizing gives

    H²(Z,I_D^4 E_pair)_chi* = P_5^(2,1) ⊕ Q_4 ⊕ Q_5,       (1)

where

    P_5^(2,1)=H¹B(5)/(u²H¹B(1)+vH¹B(2)),
    Q_4=H¹B(4)/(uH¹B(2)+vH¹B(1)),
    Q_5=H¹B(5)/(uH¹B(3)+vH¹B(2)).

Finite pushforward and exact character projection are the ones of PR437. Signs in the syzygies do not change these images. In particular order-four whole-coefficient vanishing requires all three quotients, not just Q_4. There is a canonical surjection P_5^(2,1)→Q_5, since u²H¹B(1)⊂uH¹B(3), but no equality is asserted.

## 2. New degree-four and degree-one residue models

Use PR457's exact resolution and canonical duality:

    0→D O(-5)→Λ²V O→V⊗E→Sym²E→i_*ell²→0,
    ω_C⊗ell^(-2)=D* O_C.                                    (2)

For t=-1,-3,-4, the primary HM cohomology gives H²E(t)=H³E(t)=0. Indeed E(t)=F(2), F(0), F(-1), respectively. Also H²B(5+t)=0 by PR167 and PR455. Split (2) into its image short exact sequences. Intermediate cohomology of line bundles vanishes; H⁰ell²(t)=0. Thus

    0→V⊗H¹E(t)→H¹B(5+t)→H¹ell²(t)
      →D⊗H⁴O(t-5)→0.                                      (3)

This argument identifies the first map as the natural cup map and proves its injectivity. The last map has transpose equal to ordinary restriction by PR457's resolution-duality argument, not just by dimension agreement.

Let P_j denote the primary cup image in H¹B(j), and A_j=H¹B(j)/P_j. Then

    A_4* = D*⊗[H⁰O_C(1)/res S_1],
    A_2* = D*⊗[H⁰O_C(3)/res S_3],
    A_1* = D*⊗[H⁰O_C(4)/res S_4].                         (4)

All three restriction maps are injective. The dimensions of the primary spaces are respectively 40,20,0, since h¹F(2)=10, h¹F(0)=5, h¹F(-1)=0. Consequently

    h¹B(4)=40+(50-5)=85,
    h¹B(2)=20+(100-35)=85,
    h¹B(1)=125-70=55.                                     (5)

The latter two agree with the earlier structural results. No tensor-cohomology computation is imported.

Put U_4=uH¹B(2)+vH¹B(1), and R_4=H¹B(4)/(P_4+U_4). Naturality gives uP_2⊂P_4, vP_1=0, and the exact sequence

    0→P_4/(P_4∩U_4)→Q_4→R_4→0.                           (6)

Duality identifies R_4* with D*⊗W_1(u,v), where W_1 consists of sections λ∈H⁰O_C(1), modulo restrictions of global linear forms, such that

    f|C=λ u|C,   g|C=λ v|C                               (7)

for some f∈S_3 and g∈S_4. The same section λ occurs in both conditions. Injectivity of the restrictions in degrees three and four makes f,g unique for a chosen λ. This is a residual criterion; it does not discard the primary term in (6).

## 3. A sextic obstruction and the exact common-line kernel

Let k be the number of component lines contained in both V(u) and V(v). Define

    Φ:W_1(u,v)→H⁰I_C(6),   [λ]↦vf-ug.                    (8)

Changing λ by res h for h∈S_1 changes (f,g) by (hu,hv), so (8) is well-defined. Its image J_6(u,v) lies in H⁰I_C(6)∩(u,v)_6.

If vf=ug, unique factorization and gcd(u,v)=1 give f=hu and g=hv for a common h∈S_1. On each line not contained in both forms, (λ-h)u=(λ-h)v=0 in its polynomial domain, whence λ=h there. Thus the kernel is represented exactly by sections supported on the k common-contained lines.

These sections inject modulo res S_1. Indeed if a global h restricts to a section supported on those lines, then hu vanishes on all C. Injectivity of S_3→H⁰O_C(3) forces hu=0, hence h=0. Each supported line contributes h⁰O_l(1)=2. We have therefore proved the exact sequence

    0→⊕_(common lines l) H⁰O_l(1)→W_1(u,v)
      →J_6(u,v)→0,                                      (9)

and in particular dim Q_4≥dim R_4≥2k.

If C∩V(u,v) is empty, (8) is an isomorphism onto the entire sextic intersection. To see surjectivity, write a sextic in that intersection as vf-ug. On each line, the restrictions of u and v are coprime binary forms. The relation v_l f_l=u_l g_l implies f_l=u_l λ_l and g_l=v_l λ_l for a degree-one binary form λ_l. The lines are disjoint, so these give a section λ of O_C(1). Any change of representation is (f,g)↦(f+hu,g+hv) with h∈S_1 by global coprimality, precisely the quotient in W_1. Therefore

    R_4* = D*⊗[H⁰I_C(6)∩(u,v)_6]                       (10)

under this additional avoidance hypothesis. Mere absence of common-contained lines gives injectivity in (8), not (10).

## 4. The sextic target is not just linear multiples of six quintics

PR458 proves h⁰I_C(5)=6 and identifies its basis space with the six evaluation minors. Twist its Eagon–Northcott resolution by one:

    0→D⊗B(-4)→Λ³V⊗F(-1)→Λ²V⊗O(1)→I_C(6)→0.           (11)

Let K be the image of the middle map. H⁰F(-1)=H¹F(-1)=H²F(-1)=0. Moreover H¹B(-4)=H³B(-1)*=0 by PR455. The first short exact sequence gives H⁰K=0 and H¹K=D⊗H²B(-4). The second gives the exact sequence

    0→S_1⊗H⁰I_C(5)→H⁰I_C(6)
      →D⊗H²B(-4)→0.                                    (12)

The first arrow is actual polynomial multiplication and is injective. In particular its image has dimension 30. On the other hand restriction to the twenty-five disjoint lines gives

    h⁰I_C(6) ≥ dim S_6-h⁰O_C(6)=210-25·7=35.

Thus

    dim[H⁰I_C(6)/(S_1 H⁰I_C(5))] = h²B(-4)
      = h²B(-1) ≥5.                                     (13)

These are at least five independent new degree-six classes of the saturated ideal modulo linear multiples of quintics. Since degree-four restriction is injective, there are no lower-degree ideal sections that could account for them. Sheaf generation by the six quintics does not imply generation of the saturated homogeneous ideal by their polynomial multiples. Any replacement of the target in (8) or (10) by that thirty-dimensional span would omit a proven nonzero dependency. No exact dimension of H⁰I_C(6), no selected sextic generator, and no value of its intersection with (u,v)_6 is asserted.

## Dependencies and scope

- Exact paired filtration, PR437, commit 50e82ed233cd7729c38608194f990376eb832418: https://github.com/Akilleez-QA/read-em-and-weep/blob/50e82ed233cd7729c38608194f990376eb832418/research/hm/paired-collision-filtration/PROOF.md
- Transpose-syzygy method, PR439, commit bf6ce91fd73fbc96cb8ede65448dfedbc0328c7b: https://github.com/Akilleez-QA/read-em-and-weep/blob/bf6ce91fd73fbc96cb8ede65448dfedbc0328c7b/research/hm/paired-collision-endpoint/PROOF.md
- Order-five quotient, PR451, commit ed8841c18f103e71b84c0e9376e20a2a4ed2ef9c: https://github.com/Akilleez-QA/read-em-and-weep/blob/ed8841c18f103e71b84c0e9376e20a2a4ed2ef9c/research/hm/order-five-cubic-defect/PROOF.md
- Twist-one and H³B(-1) vanishing, PR455, commit 8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4: https://github.com/Akilleez-QA/read-em-and-weep/blob/8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4/research/hm/twist-one-structural-vanishing/PROOF.md
- Evaluation resolution and boundary duality, PR457, commit 961694c4f3c805f0d58508811a42da4030dce7a6: https://github.com/Akilleez-QA/read-em-and-weep/blob/961694c4f3c805f0d58508811a42da4030dce7a6/research/hm/fixed-cubic-interpolation/PROOF.md
- Eagon–Northcott and quintic saturation, PR458, commit b46c3b48a8b10a7d0656fde247f2c3f258d1fd23: https://github.com/Akilleez-QA/read-em-and-weep/blob/b46c3b48a8b10a7d0656fde247f2c3f258d1fd23/research/hm/pair-interpolation/PROOF.md
- Primary cohomology and H²B(t)=0 for t≥2, PR167, commit 063da90fc4543304e87e701cdefcc08225412f17: https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md

The new contributions are the exact three-summand order-four endpoint, its linear-section residue criterion with two-dimensional common-line contributions, and the necessary sextic saturation classes. PR462's primary order-five classification does not identify the additional P_5^(2,1) or Q_4 terms. Their values, primary intersections, and the fixed sextic intersection remain open. Actual-source membership, pure conditions, higher-order lifting and algebraicity are separate. No selected HM/source-instance evaluation, numerical multiplication rank, generator/checker, parameter search or large computation was performed. This is authored mathematical reasoning, subject to scoped mathematical review, not formal verification.
