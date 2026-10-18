## 1. Imported structures, with the degree-zero projection retained

Use exactly the original-resolution/common-frame contraction and selector supplied in dependencies/hpl.md §§1–5 and dependencies/source-adjoint.md §3. Write d=d_End and Δ=δ_row. The identities needed are

    d H_r + H_(r+1) d = 1 - P_r,
    P_0(F)=j π(F),       P_r=0 for r≠0,
    dj=0,               dδ=δd,        δ²=Δ²=0,
    π_first δj(Z)=ΔZ,   Ld=0.

The projection identity holds for arbitrary input degree n and arbitrary input Z, not just a cocycle: only the first deleted face changes its leading owner. In the actual same-frame identification,

    j_i(R)=A_i R^t B_i,  π_i(F)=(B_i F A_i)^t,
    B_i A_j=g_ij^t,
    π_i j_j(R)=g_ij^-1 R g_ij.

Thus the first face is transported exactly by g_ij^-1(-)g_ij, and all other faces project in the first owner's frame. This uses the supplied quotient transition/frame theorem; local contractions alone are insufficient. No extra conjugation is added to original-resolution δ. The one transpose remains exactly once in j.

For negative internal degrees the projection vanishes by support of E=A B on K1. These are all projection terms in the following calculation. In particular the first projection jΔZ cannot be dropped when Z is not closed. The same scalar line/bundle transports and valid localizations as the imported theorem remain required.

## 2. General-input HPL chain map

For Z of row Čech degree n define

    J0^(n)(Z)=jZ,
    J_s^(n)(Z)=a_s(n) H_(1-s) δ J_(s-1)^(n)(Z),
    a_s(n)=(-1)^(n+s+1),                  s=1,2,3.

Then J_s has bidegree (n+s,-s). The exact nonclosed recurrence is

    d J_s^(n)(Z)
      =a_s(n)[δ J_(s-1)^(n)(Z)-J_(s-1)^(n+1)(ΔZ)].       (1)

For s=1, dδjZ=0 and the homotopy identity gives

    dJ1^(n)=a_1(n)(δjZ-jΔZ).

For s≥2 there is no projection term. Applying dH=1-Hd and induction gives

    dJ_s^(n)
      =a_s(n) δJ_(s-1)^(n)-a_s(n) H δdJ_(s-1)^(n)
      =a_s(n) δJ_(s-1)^(n)
         +a_s(n)a_(s-1)(n) H δJ_(s-2)^(n+1)(ΔZ).

Since a_(s-1)(n+1)=-a_(s-1)(n), the second term is exactly
-a_s(n) J_(s-1)^(n+1)(ΔZ), proving (1). There is no assumption Hδ=δH, and each H belongs to the leading owner before the next face deletion, retaining all deleted-prefix owners.

Equivalently, with D=δ+(-1)^q d on Čech degree q,

    δJ_(s-1)^(n)+(-1)^(n+s)dJ_s^(n)=J_(s-1)^(n+1)Δ.

The bottom relation also holds:

    δJ3^(n)=J3^(n+1)Δ.                                  (2)

Indeed W=δJ3^(n)-J3^(n+1)Δ is d-closed by (1), Δ²=0 and a_3(n+1)=-a_3(n). It has internal degree -3. The imported bottom injectivity, equivalently absence of degree -4 together with the End contraction, gives W=0. Hence D(sum_s J_s^(n))=(sum_s J_s^(n+1))Δ: this is the full chain map, including nonclosed inputs.

This extension is a direct consequence of the existing contraction argument, not a claim of novelty for HPL itself. It does not invoke complete raw residual closure.

## 3. The degree-two endpoint equations and selector

For n=2 the signs are +,-,+. For n=3 they are -,+,-. Explicitly,

    J1^(2)= H0 δj,          J1^(3)=-H0 δj,
    J2^(2)=-H_-1 δH0 δj,    J2^(3)=-H_-1 δH0 δj,
    J3^(2)= H_-2 δJ2^(2),   J3^(3)=-H_-2 δJ2^(3).

Equation (1) specializes to

    dJ1^(2)(Z)= δjZ-jΔZ,
    dJ2^(2)(Z)=-δJ1^(2)(Z)+J1^(3)(ΔZ),
    dJ3^(2)(Z)= δJ2^(2)(Z)-J2^(3)(ΔZ).                   (3)

As L commutes with restrictions in the admitted same scalar frame and Ld=0, c=LJ2^(2)(Z) satisfies

    δc=LJ2^(3)(ΔZ).                                     (4)

There is no additional sign in (4), and no remaining projection term beyond ΔZ. The omitted dJ3 term is killed by the selector, not set equal to zero. Confusing J1^(3) with J1^(2) would produce a wrong intermediate equation even though J2 has the same sign in the two degrees.

## 4. Exact twisted cup form of the endpoint defects

Set θ_v,ij=g_ij^-1 V_v g_ij, and let t_ij(X)=g_ij^-1 X g_ij transport from the j row frame to i. On increasing triples, g_ik=g_jk g_ij and the Leibniz rule imply

    θ_v,ik=θ_v,ij+t_ij θ_v,jk,
    Δθ_v=0.                                            (5)

This is an edge cocycle identity, not the Maurer–Cartan derivative identity. It requires no evaluation of currents. In the notation of the endpoint packet, θ_v,ij=L_v and t_ij θ_v,jk=U_v.

For a row-valued cochain α of degree r and scalar cochain s of degree t, use the ordinary ordered cup product with all factors restricted to the same overlap:

    (α cup s)_(i0...i_(r+t))=α_(i0...ir) s_(ir...i_(r+t)),
    (s cup α)_(i0...i_(t+r))=s_(i0...it) t_(i0,it) α_(it...i_(t+r)).

The scalar coefficient bundles are multiplied using the SAME physical trivializations. These cups satisfy the graded Leibniz identity for Δ and δ. We use them on increasing tuples and then alternating extension; no nonlinear source is reconstructed on a permuted tuple.

For r=(a,b), complementary q, the given source inputs are exactly

    Z_a=(θ_b cup s_q-s_q cup θ_b)/2,
    Z_b=-(θ_a cup s_q-s_q cup θ_a)/2.

Using (5) and the actual raw first-order equation δs_raw,q=F_q gives

    ΔZ_a=-(θ_b cup F_q+F_q cup θ_b)/2,
    ΔZ_b= +(θ_a cup F_q+F_q cup θ_a)/2.                 (6)

The plus between the two cups follows from the degree-one Leibniz sign. Define the explicit degree-three cochain

    C_(v,q),ijkl
      =θ_v,ij F_q,jkl+F_q,ijk g_ik^-1 θ_v,kl g_ik.       (7)

Then ΔZ_a=-C_(b,q)/2 and ΔZ_b=C_(a,q)/2. Both endpoint transports are retained; the final current is transported through g_ik, not merely g_ij. No cyclic trace or commutation of matrix factors was used. Scalars alone commute with matrices.

An independent direct quadruple check fixes the signs: in the i frame put x=θ_ij, y=t_ijθ_jk, z=t_ikθ_kl. The four endpoint expressions give

    2ΔZ = (s_kl y-s_jk z)
            -(s_kl(x+y)-s_ik z)
            +(s_jl x-s_ij(y+z))
            -(s_jk x-s_ij y)
         =-x(s_kl-s_jl+s_jk)-(s_jk-s_ik+s_ij)z.

This is exactly -(θ cup δs+δs cup θ), before substituting the raw F theorem.

The same raw first-order premise is the directly proved theorem in dependencies/raw-first-order.md, especially §§4–6 and equation (6), and its supplied review dependencies/raw-first-order-review.md. It is not inferred from closure of the complete second-order residual. Its physical/primitive/common-frame premises remain explicit; the excerpt retains these premises.

