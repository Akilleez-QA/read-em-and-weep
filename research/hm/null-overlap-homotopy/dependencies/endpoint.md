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

## 5. Four exact terminal defects and the Ward family

For P=(0,1), Q=(2,3), let T=LJ2^(3). Equations (4)–(7) yield

    δc_0=-T(C_(1,Q))/2,
    δc_1=+T(C_(0,Q))/2,
    δc_2=-T(C_(3,P))/2,
    δc_3=+T(C_(2,P))/2.                                (8)

Here T retains the entire original-resolution stage-two circuit with quadruple residual occurrences and the same selector. All sorting, path and prefix-owner signs remain in T. No production compiler call of degree-three arity is asserted.

Consequently the supplied partition-Ward identity becomes

    W_outer = -δ_tensor[p sum_d S Q_dot_d c_d]
      +(p/2) S[ Q_dot_0 T(C_(1,Q))-Q_dot_1 T(C_(0,Q))
                  +Q_dot_2 T(C_(3,P))-Q_dot_3 T(C_(2,P)) ].       (9)

This is the exact scalar-free defect family sought. The boundary term still contains c_d, hence s_raw. The derivative of p, inner H/E/I/P kernel derivatives, full baseline and current-curl terms remain outside this reduction. No one of the C_(v,q) is asserted zero. Although ΔC=0 follows from Δθ=δF=0, closure is not vanishing, and applying HPL to this closed degree-three input does not annihilate its selected scalar value.

The rational/cochain identity (9) is not a rational-coordinate divergence certificate for B_p. The supplied differentiated-partition domain theorem (dependencies/domain.md) already gives regularity for Q_dot c_d and Q_dot delta c_d, conditional on its homogeneous all-chart primitive/frame/current premises. It uses the 35/15 per-occurrence endpoint certificate, the differentiated own-weight certificate 53/28, the missing-axis eigensheaf, and every sampled owner's clearing weight, including repeated target tags. With the retained test interpreted as its authenticated global dual section, the boundary in (9) therefore has zero Serre trace. This imports that theorem; it does not reprove its premises or admit repeated-tag production execution.

Equation (4) identifies T(Delta Z_d) with the SAME delta c_d on each admitted overlap. Therefore the summed scalar-free expression in (9) inherits that cochain's established domain through equality. No new pole estimate is claimed for individually expanded F-current branches or a new direct six-owner implementation. In particular the inherited domain does not follow merely by transferring closed degree-two source bounds to degree-three inputs.
