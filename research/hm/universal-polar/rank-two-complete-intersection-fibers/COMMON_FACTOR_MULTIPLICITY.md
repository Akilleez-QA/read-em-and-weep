# Common-factor pencils force boundary multiplicity at least six

Retain PROOF.md and its even formal presentation

    R=C[[t_1,t_2,t_3,t_4]]/(g_1,g_2),
    g_i(-t)=g_i(t),
    in_2(g_i)=q_i.

If the annihilator pencil has a common factor, then the Hilbert--Samuel multiplicity of R at its maximal ideal is an even integer at least six. This strengthens the multiplicity-four coprime case. No reducedness of the surface R is assumed.

Write the two independent initial quadrics as z*l_1 and z*l_2. By replacing the pencil basis, choose both l_i nonproportional to z. Their mutual independence is automatic. Thus the three linear forms z,l_1,l_2 are pairwise nonproportional, including the case z belongs to span(l_1,l_2).

Take a general two-dimensional linear subspace L in the four-dimensional tangent-coordinate space. Two simultaneous open conditions can be imposed:

1. Its two defining linear forms give a minimal reduction of the maximal ideal of the two-dimensional Cohen--Macaulay ring R. The resulting Artinian quotient has length e(R).
2. The restrictions of z,l_1,l_2 to L are nonzero and pairwise nonproportional.

For (1), over the infinite residue field C, two general linear combinations of generators of the maximal ideal form a minimal reduction. Since R is Cohen--Macaulay, the length of the parameter quotient equals its multiplicity. For (2), each failure is a proper determinantal closed subset of the Grassmannian, and all finitely many such failures can be avoided. These open conditions intersect.

The plane restrictions h_i=g_i|L are even formal power series with initial forms z*l_i. Each is an ordinary node: the two distinct tangent lines lift to two unique smooth formal branches. This follows directly by blowing up the origin and applying the formal implicit-function theorem at the two simple roots of the tangent polynomial. Each branch is invariant under central inversion, because inversion preserves its tangent line and that branch is unique.

For each i denote by C_i the branch tangent to z=0 and by D_i the branch tangent to l_i=0. In linear coordinates (r,s) on L with z=s, the branches C_i have equations s=phi_i(r). Their inversion invariance implies phi_i(-r)=-phi_i(r). Their tangent is s=0, so phi_i has order at least three (or is zero). As the plane quotient is Artinian, C_1 and C_2 cannot be the same branch. Consequently

    I(C_1,C_2)=ord_r(phi_1-phi_2) >= 3.

The other three cross pairs (C_1,D_2), (D_1,C_2), and (D_1,D_2) have distinct tangent lines, hence each has intersection multiplicity one. Additivity of plane intersection multiplicity under factorization gives

    e(R)=length C[[r,s]]/(h_1,h_2)
        =I(C_1,C_2)+I(C_1,D_2)+I(D_1,C_2)+I(D_1,D_2)
        >=3+1+1+1=6.

Moreover phi_1-phi_2 is an odd nonzero series, so its order is odd. Thus the displayed sum is even. This proves both parity and the bound for squared-factor and unsquared-factor pencils. The argument uses the even presentation essentially: without it the common-tangent branches could have quadratic contact and would only give the weaker bound five. No exact multiplicity or analytic classification in the common-factor case is claimed.
