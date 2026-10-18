
For any alternating scalar degree-q cochain c, put

    (Q_dot c)_(e0,...,e_(q-1))
      = sum_(k=0)^(q-1) (-1)^k
        sum_(a0,...,a_(q-1),b)
        [product_(j=0)^(q-1) rho_(ej,aj)] dotrho_(ek,b)
        c_(a0,...,ak,b,a_(k+1),...,a_(q-1)).               (3)

Here each a_j is a symbolic vertex in the fiber over e_j and b lies over e_k; all restrictions and original owner identities remain attached. Q_dot=0 on degree zero. Repeated target tags are intentional; only identical alternating source vertices vanish. Equation (3) is a mathematical cochain expression, not permission to invoke the frozen terminal program on tuples outside its certified distinct-staircase-tag domain.

If sum_a rho_(e,a)=1 and sum_a dotrho_(e,a)=0, then

    Π_dot c = δ Q_dot c + Q_dot δc.                       (4)

One proof uses the usual two-projection prism, weighting its prefix by rho and suffix by rho+t dotrho. Its coboundary is Π_(rho+t dotrho)-Π_rho. Differentiate at t=0. Any differentiated suffix weight other than the duplicated pivot leaves that pivot weighted by rho_a rho_b; its alternating sum is zero by exchange of a,b. Only the derivative on the duplicated pivot survives, giving (3). This proves (4) without differentiating c or any frame. Alternatively, direct expansion pairs all interior faces; endpoint faces use exactly the unit and zero-sum identities. In degree zero, Q_dot δc=sum_(a,b)rho_a dotrho_b(c_b-c_a)=sum_b dotrho_b c_b, fixing the sign.

Applying (4) to (2), using Sδ=δ_tensor S and the fact that the same rational test p commutes with Čech restrictions on the common rational trivialization, gives

    W_outer = -δ_tensor[p sum_d S Q_dot_d c_d]
              -p sum_d S Q_dot_d δc_d.                   (5)

Here p need not be globally regular on the projective variety. Multiplication by p is used in the restriction-compatible rational module; no regular-domain conclusion follows from this alone. Mask15 extraction may be applied after this complete equality. This is discrete Stokes: the sum of all outer derivative terms is replaced by a boundary plus four specified source defects. It is not an ordinary rational coordinate-divergence certificate.

For the COMPLETE closed scalar c=L_selector J2, the source's J3 equation and L_selector d_End=0 give δc=0; hence Π_dot c=δQ_dot c. This is a valid positive structural control. It does not apply to (1): the input Z_d is an endpoint-current coefficient, not the complete raw residual. Neither δs=F nor closure of the complete residual proves δc_d=0. A cancellation of the last term in (5) would require a new identity for these actual four defects, potentially combined with the baseline and other kernel derivatives. No such identity has been established here.

