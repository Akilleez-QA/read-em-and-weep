# Differentiated owner partitions: exact discrete Stokes identity and its source defect

## Finding and scope

The entire OUTER-weight derivative family in the complete source-adjoint remainder has an exact decomposition into a scalar Čech boundary and one differentiated-partition operator applied to the Čech defects of four explicitly specified endpoint-current cochains. It is not zero merely because the partitions sum to one. The defect cochains are not the complete closed source, and their closure is not supplied by the published raw-source theorem. Therefore this calculation does not establish cancellation of that family, a rational divergence for B_p, or any detector value.

A second, domain-free rational identity expresses that same entire family using differences of complete owner kernels from an anchor. It removes only the owner-independent part, not the differing kernels. This generic algebra becomes source-specific by specifying the exact four cochains and retaining the entire sorted HPL circuit. It is a bounded reduction, not a newly discovered obstruction-annihilating Ward identity.

This is a bounded consequence of the previously supplied source-adjoint, current-curl, HPL and regular-cover identities. Selected prerequisite sections are supplied in dependencies; their provenance is inherited, not newly authenticated remotely. The partition/prism mechanism is prior work, not a new theorem claimed here.

Only invented free symbols and inert source metadata are used. No actual physical/model/source/owner/jet values, matrix-polynomial products, production imports, or external writes are involved.

## 1. Exact four source cochains

Keep the source's original-resolution, finite-frame interpretation and its single transpose. For r=(a,b), complementary q, define the following formal row-matrix cochains on the SAME increasing residual triple (i,j,k):

    Z_a = (s_q,jk L_b - s_q,ij U_b)/2,
    Z_b = (-s_q,jk L_a + s_q,ij U_a)/2.

Use both pairs (r,q)=(P,Q),(Q,P), so there is one Z_d for each d=0,1,2,3. The s are the actual symbolic raw scalar leaves, L and U the correctly transported currents from the source packet. No derivative acts on s in Z_d. Define the degree-four scalar cochain

    c_d = L_selector[-H_-1 δ H_0 δ j(Z_d)].                 (1)

This is the exact same finite, A-linear HPL composition as before. The symbol L_selector distinguishes the selector from the currents L_d. Define (1) first on source-increasing tuples and then by alternating extension; do not reconstruct a nonlinear source on a newly permuted tuple. Original owner weights stay outside the circuit.

Write Π_rho for the five-owner weighted projection in degree four, S for the signed staircase cochain map, and dot_d rho=V_d rho. Let Π_dot_d mean parameter differentiation of only the scalar weights, holding its input cochain, HPL circuit, frames and selector fixed. After taking that parameter derivative, substitute dot_d rho=V_d rho. This is not the total physical derivative V_d(Π_rho c_d). Before mask extraction, the entire outer-weight derivative contribution in B_p is precisely

    W_outer = -p sum_d S Π_dot_d c_d.                      (2)

Indeed each Z_d is the sum of the exact E-branch coefficients with derivative axis d and its undifferentiated scalar endpoint. Expanding (1) over all paths yields precisely minus the weight-derivative contribution -sum_(lambda,e) p (V_d w_lambda) sign_e/2 ell_lambda(current_e) s_e. The sorting and staircase signs, all deleted-prefix HPL owners, and both endpoints remain in (1)–(2). Formula (2) also agrees with the outer-weight portion of the post-Maurer–Cartan kernel derivative in the current-curl reduction. Derivatives of p and of H/E/I/P inside the circuit are NOT part of W_outer and are untouched.

## 2. Infinitesimal partition prism

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

## 3. Exact anchor form without a new prism domain

Fix a staircase sigma, an original slot h, and the other four original owners. Let f_d(o) denote the complete scalar cochain (1) on the whole original tuple o, including whole-tuple sorting parity. Select any symbolic anchor alpha_* in the SAME slot fiber. Then

    sum_alpha dotrho_(e_h,alpha) f_d(o[alpha])
      =sum_alpha dotrho_(e_h,alpha)
                    (f_d(o[alpha])-f_d(o[alpha_*])).      (6)

Consequently the same W_outer equals minus p times the sum of (6), weighted by the four unchanged original weights, over h=0,...,4, all staircases with their signs, and d=0,...,3. The anchor term cancels because sum dotrho=0. Every differing owner kernel, residual triple, transport, sorting permutation, and HPL path stays inside the difference. One MUST NOT replace only the weight's label while holding its old circuit topology fixed.

This is an identity on the full rational overlap. Anchor differences separately need not enjoy the original weighted regular-extension theorem: the non-anchor weight is not the clearing weight of the anchor coefficient. Only their full exact sum is being asserted. A two-letter free control with rho_0=u, rho_1=1-u gives sum dotrho_i f_i=f_0-f_1, which is generally nonzero. This supplies no actual-source nonvanishing conclusion.

## 4. Domain and novelty boundaries

No regular-extension estimate for these endpoint-current inputs or the differentiated prism is proved here. Complete-source J2 bounds cannot be transferred to c_d without a separate same-source pole/frame argument. The repeated target tags and additional sampled owners in Q_dot must be admitted as mathematical cochains with all original owner identities and frame factors retained. Unlike the older prefix-weighted prism, Q_dot weights every sampled vertex, including both duplicated-pivot vertices, with one differentiated weight. This may support a sharper domain theorem, but does not itself establish one. The frozen distinct-tag terminal evaluator is not extended by this argument.

Thus (4)–(6) are unconditional formal rational/cochain identities on valid common overlaps, conditional on the already supplied source denotations. Turning their boundary into a zero Serre pairing needs an appropriate regular Čech domain; turning it into an ordinary rational divergence needs an additional comparison. Neither is silently inferred. The closed complete-source positive control can inherit a zero-pairing conclusion if its differentiated prism domain is independently supplied, but it does not prove the desired endpoint-family vanishing.

The resulting next obligation is concrete: compute symbolically or identify structurally sum_d S Q_dot_d δc_d together with the other remaining kernel and baseline terms. Claiming that it vanishes merely because rho is a partition would erase exactly this defect term.

## 5. Formal regression control

check.py uses invented two-letter fibers with algebraically independent r_e,d_e and weights (r_e,1-r_e), variations (d_e,-d_e). It treats every alternating cochain coefficient as free, expands both sides of (4) coefficientwise in degrees 0–4, and verifies equality. It also confirms the differentiated projection is generally nonzero, rejecting a false-zero mutation. Both python -B and python -BO pass. These finite controls support the displayed universal proof and fix signs; they do not evaluate actual owner fibers or certify physical-source/domain premises.
