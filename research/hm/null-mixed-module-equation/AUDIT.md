# Independent review of the explicit mixed module cocycle

## Verdict

PASS, conditional on the geometric/sheaf premises and imported pure-lift existence and cohomology results explicitly retained in RESULT.md. No material correction is required to formulas (3)–(10), the row-normalized cocycle argument, or the compact tracefree normalization. In particular, the overlap-composition term, both overlap–pure interactions, both overlap–derivative interactions, the mixed product operator, and the product of the scalar triple coefficients have all been retained with the correct signs.

This review independently expands the formal coefficient operations. It neither evaluates physical transition matrices or jets nor proves the mixed obstruction vanishes. 

## Sources and conventions checked

Compared the full mixed-module RESULT.md with:

- null-actual-pair-comparison/RESULT.md and its independent AUDIT.md, especially the final downstairs pair presentation and the external-product scope;
- null-module-boundary-audits/module-lifting/RESULT.md, including row normalization, the exact four-index identity, and the sign of the correction equation;
- null-pure-lift-uniqueness/pure-lift-uniqueness/RESULT.md, for the conditional compact rigidity and scalar cohomology inputs;
- null-simple-fiber-moduli/family-lift-torsor-0523/RESULT.md, for double-Čech signs and scalar/trace conventions;
- null-actual-source-factorization/RESULT.md, for the formal factor-support interpretation and the distinction between ambient comparison and module existence.

The row order is g_jk g_ij = g_ik. An endomorphism represented in the j frame transports to the i frame by τ_ij(x)=g_ij⁻¹ x g_ij. All coefficient-line identifications are implicit in these restriction formulas. No commutation of matrix entries is used.

## 1. External-product ambient

Root-HKR's pair presentation is exactly

    μ(f,g)=df∧dg/2,
    v_ij(f)=df∧β_ij/2,
    b_ijk=−2(β²)_ijk,
    (β²)_ijk=−β_ij∧β_jk.

Taking its external product gives three separate types of mixed data:

1. Multiplication: the ordinary degree partitions (0,0)+(1,1), (1,1)+(0,0), (1,0)+(0,1), and (0,1)+(1,0); the two μ_z terms with one K_h input; the two μ_h terms with one K_z input; and M=μ_z⊗μ_h on two degree-zero inputs.
2. Overlap maps: v_z on the K_h input, v_h on the K_z input, and w=v_z v_h on the degree-zero input.
3. Triple units: the coefficient-line product bc on the same triple intersection.

These are precisely (3)–(4). The factor 1/4 in M follows from the two factors 1/2, with no further factor of two. The two degree directions are ordinary nilpotent coefficient directions, not odd variables introducing an extra Koszul sign. The total Čech–forms sign is already included in the stipulated β² representatives.

The support qualifications matter: b comes from z, so its h derivative vanishes; c comes from h, so its z derivative vanishes. Thus A is central in this truncated external product and the mixed part of A⋆G is

    b v_ik + c u_ik + bc g_ik

when G has zero mixed coefficient. Without factor support, the extra μ_h(b,g_ik) and μ_z(c,g_ik) terms would indeed be needed. RESULT.md states this limitation correctly.

## 2. Direct mixed source check

For F_ij(G_jk), write its four coefficients as

    f = g_jk,
    U = u_jk + v^z_ij(g_jk),
    V = v_jk + v^h_ij(g_jk),
    T = v^z_ij(v_jk) + v^h_ij(u_jk) + w_ij(g_jk).

Multiplying by G_ij=(g_ij,u_ij,v_ij,0) gives the mixed coefficient

    T g_ij + U v_ij + V u_ij
    + μ_z(g_jk,v_ij) + μ_z(V,g_ij)
    + μ_h(g_jk,u_ij) + μ_h(U,g_ij)
    + M(g_jk,g_ij).

Subtracting the mixed part of A⋆G_ik from Section 1 gives exactly (6). This partition exhausts the allowed bidegrees, so no further mixed contribution can occur. In particular, expanding U and V retains both μ_z(v^h_ij(g_jk),g_ij) and μ_h(v^z_ij(g_jk),g_ij), rather than dropping them as if the overlap maps were identity.

Substitution u→u+p and v→v+q changes U→U+p and V→V+q. Expanding these two products independently gives the two quadratic terms p_jk q_ij and q_jk p_ij and all linear terms displayed in (7). The finite variation formula is correct; it is not merely the linearized top-order ambient characteristic map.

## 3. Row normalization, closure, and correction sign

The remaining defect is J-valued because the two pure equations hold. The exact module-lifting four-index identity therefore reduces to

    R_ikl + g_kl R_ijk − R_ijl − R_jkl g_ij = 0.

Left multiplication by g_il⁻¹ gives

    C_ikl + C_ijk − C_ijl − τ_ij(C_jkl) = 0.

This is minus the standard degree-two Čech differential and hence is precisely its vanishing. There is no reversal of the zero condition or of the subsequent correction convention.

Adding a mixed coefficient Y_ij=g_ij x_ij changes the raw defect by

    g_jk Y_ij + Y_jk g_ij − Y_ik.

Its normalization is x_ij+τ_ij(x_jk)−x_ik=δx. Consequently the equation to solve is δx=−C, exactly as stated. On the specified affine acyclic refinement, this yields the claimed H² obstruction and does not leave a separate local action obstruction for locally free modules.

## 4. Independent pure-gauge computation

Set H_i=1+a_i+d_i. Since positive bidegrees truncate separately, its inverse is

    H_i⁻¹ = 1−a_i−d_i+a_i d_i+d_i a_i.

There are no derivative terms: every eligible derivative with a degree-zero identity entry is zero, and derivatives between two positive-degree entries exceed a permitted bidegree.

Let B_ij=F_ij(H_j)⋆G_ij. Its pure coefficients are

    B_z=u_ij+a_j g_ij,
    B_h=v_ij+d_j g_ij,

and its mixed coefficient is

    B_J=[v^z_ij(d_j)+v^h_ij(a_j)]g_ij
        +a_j v_ij+d_j u_ij
        +μ_z(d_j,g_ij)+μ_h(a_j,g_ij).

Multiplication by H_i⁻¹ gives

    Q_ij=B_J+g_ij(a_i d_i+d_i a_i)
         −B_z d_i−B_h a_i
         −μ_z(g_ij,d_i)−μ_h(g_ij,a_i),

which is exactly (9). The displayed order of every noncommuting matrix factor is preserved.

For the full transformed transitions, cancellation of H_j⁻¹⋆H_j and the actual inner-gluing identity give

    D'_ijk=F_ij F_jk(H_k)⋆D_ijk⋆H_i⁻¹.

Because D is J-valued and H reduces to identity, this equals D literally. The new classical transitions are still g. Thus C(u',v') plus the mixed correction δ(g⁻¹Q) equals C(u,v). Resetting that correction to zero gives

    C(u',v')−C(u,v)=−δ(g⁻¹Q).

The minus sign in (10) is therefore essential and correct. Adding a mixed frame coefficient e_i changes g⁻¹Q by τ_ij(e_j)−e_i=δe, so it leaves this equation unchanged.

## 5. Compact tracefree claim and its exact scope

Künneth gives H²(P²×P²,ω_P²⊠ω_P²)=0: ω_P² has cohomology only in degree two, so its external product has cohomology only in degree four. Since trace commutes with conjugation and the Čech differential, tr C is a closed scalar J-valued 2-cochain and has a scalar 1-cochain primitive k on the acyclic cover.

For rank two,

    C₀=C−(1/2)(δk) Id_E

has zero trace as a cochain and differs from C by the coboundary δ((k/2)Id_E). Thus the statement is stronger than merely saying the class has zero trace, and its factor 1/2 is correct. This does not assert that the original source (6) is pointwise traceless, nor does it modify the ambient scalar gerbe. The report makes both distinctions correctly.

The compact pure-representative independence follows from the imported H¹ pure vanishings plus (10), conditional on nonempty pure lifting groupoids. The H⁰ vanishings supply uniqueness of the comparison isomorphisms, rather than the existence of the gauge itself. The final mixed H¹ and H⁰ vanishings imply uniqueness only if the mixed obstruction vanishes. None of these vanishings supplies its missing primitive.

Finally, the relative construction uses D=δ_h+(−1)^pδ_z. Removing C₀^(0,2) by δ_z x^(0,1)=−C₀^(0,2) changes the (1,1) component by +δ_h x^(0,1), matching the cited torsor formula. It requires passing to the appropriate double resolution; it does not identify ordinary single-cover cochain components without that passage. The stated restriction warning remains necessary.

## Final assessment

The result establishes an explicit, choice-independent compact obstruction class for the fixed external-product ambient and compatible pure boundary. It does not evaluate that class, identify arbitrary additional mixed ambient deformations with this one, or align a separately frozen physical module two-jet. Those limits are correctly maintained throughout.
