# Exact synthesis of outer and inner derivative families

This is a conditional algebraic corollary of the differentiated-contraction-transfer-public sibling proof and the bounded endpoint/partition excerpts supplied here. It is not a cancellation theorem for the remaining defects.

Fix a direction d and write T_n=LJ2_n on row cochains of Čech degree n. The endpoint transfer identity gives δT_n=T_(n+1)Δ_n; the dJ3 term is killed by L, rather than assumed zero. Write Π for the full ordinary partition cochain map and Qdot_d for its differentiated prism, with Π′=δQdot_d+Qdot_dδ. Here Π′ differentiates weights only, holding the input fixed. These precise identities are supplied in dependencies/endpoint-transfer.md and dependencies/partition-identity.md.

With fixed ambient restrictions and selector (δ′=L′=0), define

    M_n=Π_(n+2) T_n,
    K_(d,n)=Qdot_(d,n+2) T_n - Π_(n+1) L U_(d,n).

The operator T_n raises Čech degree by two, U_n by one, and Qdot lowers it by one; thus K_n raises it by one. The differentiated-contraction identity states

    T_n′=-δ(LU_n)-(LU_(n+1))Δ_n+T_n a_n+L E_n.

Product differentiation, with Πδ=δΠ, gives exactly

    M_n′=δK_(d,n)+K_(d,n+1)Δ_n+M_n a_(d,n)+Π_(n+2)L E_(d,n).

Indeed Π′T contributes δQdot T+Qdot TΔ, while ΠT′ contributes -δΠLU-ΠLUΔ+Ma+ΠLE. No T or H is commuted through a Čech differential, and no source closure is imposed. This is the derivative of the kernel M with its input held fixed; a varying input would add M_n Z′.

For each of the four endpoint inputs Z_d of degree two, apply the staircase map S and full-sign extraction to the complete equality. Their combined outer-weight and inner-kernel derivative family is therefore

    -p sum_d S M_2′ Z_d
      = -δ_tensor[p sum_d S K_(d,2) Z_d]
        -p sum_d S [K_(d,3)ΔZ_d+M_2 a_(d,2)Z_d+Π_4 L E_(d,2)Z_d].

The full-sign extraction is understood on both sides after this assembled equality. The test p is interpreted as its authenticated dual section, so multiplication commutes with restrictions.

Both pieces of K_(d,2)Z_d have regular full-sign domains: the supplied differentiated-partition domain theorem treats Qdot_d T_2Z_d, and PROOF.md of this packet treats Π_3LU_(d,2)Z_d. Their difference is therefore a genuine degree-three F-valued cochain after comparison; multiplication by p makes its boundary canonical-bundle-valued. That boundary has zero Serre pairing. This does not assert an independent pole certificate for arbitrary separately expanded F-current, a, or E summands.

There is also a conservative direct domain for the nonclosed-input term before scalar-free substitution. The row first face is g^-1 Z g; it is not a pole-neutral scalar restriction. With the actual g and g^-1 bounds4/2 retained as premises (dependencies/raw-premises.md and dependencies/raw-poles.md), this gives

    ΔZ_d: 19/7+4/2+4/2=27/11,
    LU_(d,3)ΔZ_d: 17/9+27/11=44/20.

Other row faces fit this bound. Every transport endpoint and every homotopy-prefix owner remains attached; new occurrences receive harmless padding rather than borrowed charges. The degree-four result has five occurrences, all carrying their own ordinary54/29 weight, leaving10/9 slack. The same full-sign frame and finite-flat projection argument therefore gives a regular Π_4LU_(d,3)ΔZ_d. This uses no transport cancellation. The other piece Qdot_(d,5)T_3ΔZ_d inherits the already supplied differentiated-prism domain through T_3ΔZ_d=δ(T_2Z_d). Hence K_(d,3)ΔZ_d is regular before replacing ΔZ_d by its current–F identity. No unchanged19/7 bound for the row differential is asserted.

The already supplied scalar-free endpoint identities are

    ΔZ_a=-(θ_b cup F_q+F_q cup θ_b)/2,
    ΔZ_b= +(θ_a cup F_q+F_q cup θ_a)/2,

for each complementary pair r=(a,b),q. They may be substituted in K_(d,3)ΔZ_d by the same linear operator extension and within the exact combined identity. The scalar-free label concerns this nonclosed-input subfamily; the a and E terms can still contain raw scalar leaves. No term is thereby shown to vanish, and there is no new executable degree-three/repeated-key admission or separate direct pole estimate for the expanded F-current expression.

Derivatives of p and of the current/source input, the full baseline, and other remainder families remain separate. If ambient restrictions or L vary, the original E_restr and L′J2 corrections must be added before applying Π. A local split gauge does not authorize omitting them. This synthesis supplies no numerical source value, detector verdict, or complete obstruction cancellation.
