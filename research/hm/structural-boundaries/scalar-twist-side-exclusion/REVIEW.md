# Independent review: bounded same-pair scalar multiplication-side exclusion

## Verdict

**Accepted at the stated bounded scope.** No blocking sign, order, normalization, quantifier, actual-overlap, or scope issue was found. For the fixed ordered coefficient, ordinary, left-star, right-star, and every displayed constant-lambda interpolation fail. The stronger joint constant family also has the stated necessary condition A=B=0. That necessary condition is not an existence assertion at A=B=0.

Reviewed artifact: `PROOF.md`.

Reviewed SHA256: `bf370e58da16c4458e1635869c0f0480b88a2b46e0c969d30da43b8021b254e7`.

Review date: 2026-10-18.

I derived the scalar-side associator and the abstract mask formulas independently before reading the completed producer draft. I then checked the complete draft against those calculations. The actual source binding is inherited from the accepted structural and same-pair dependency proofs; this review checks their use, without executing or expanding the physical source/model or primitive matrices.

## 1. Direct associator, rather than interpolation

Use the row convention g_jk g_ij=g_ik and work modulo epsilon cubed. Let

    T_jk*T_ij = h_ijk T_ik + lambda epsilon^2 E_ijk
                  + epsilon^2 D^lambda_ijk,
    E_ijk = mu(b_ijk,g_ik),
    h_ijk = 1+epsilon b_ijk+epsilon^2 c_ijk.

The first-lift equation is required and contains the composite-edge term U_ik. It makes the displayed defect a genuine second-order coefficient. The accepted corrected structural dependency supplies this convention.

At order two, the two scalar-placement errors in the actual associative product are exactly

    T_kl*(h_ijk T_ik)-h_ijk(T_kl*T_ik)
        = epsilon^2 mu(g_kl,b_ijk)g_ik,

    (h_jkl T_jl)*T_ij-h_jkl(T_jl*T_ij)
        = epsilon^2 g_jl mu(b_jkl,g_ij).

These are scalar-slot Leibniz identities. They do not assert that a separately defined twisted operation is associative. Substituting the four triple equations into the ambient associator therefore gives

    0 = g_kl D^lambda_ijk-D^lambda_jkl g_ij
          +D^lambda_ikl-D^lambda_ijl
          +K g_il+F_raw-G_raw+lambda B(E),

    K = c_ijk+c_ikl-c_jkl-c_ijl
          +b_ijk b_ikl-b_jkl b_ijl,
    F_raw = mu(g_kl,b_ijk)g_ik,
    G_raw = g_jl mu(b_jkl,g_ij),
    B(E) = g_kl mu(b_ijk,g_ik)-mu(b_jkl,g_jl)g_ij
             +mu(b_ikl-b_ijl,g_il).

The ordered scalar cup is a cocycle, so b_ikl-b_ijl=b_jkl-b_ijk. Expand the final term using both g_il=g_jl g_ij and g_il=g_kl g_ik. All interior terms cancel, leaving

    B(E) = -mu(b_ijk,g_kl)g_ik+g_jl mu(b_jkl,g_ij)
         = F_raw+G_raw.

Here the last equality uses scalar-slot skewness mu(b,G)=-mu(G,b), which holds for the specified bidifferential coefficient. Thus the lambda coefficient has been derived directly; it was not guessed from the values at lambda=0,1,-1.

With left normalization M^lambda_ijk=g_ik^-1 D^lambda_ijk and the stated row Cech differential, the four defect terms equal -g_il delta_row M^lambda. Consequently

    delta_row M^lambda = K Id+(1+lambda)F+(lambda-1)G,
    F=g_il^-1 F_raw,             G=g_il^-1 G_raw.

This independently confirms the producer's sign and normalization side. Equivalently, delta_row(g_ik^-1 E_ijk)=-F-G. For determinant-one transitions F and G are traceless linear combinations of conjugated logarithmic currents. Taking the trace-free part would also suffice without that observation.

## 2. First lifts, second edges, scalar coefficients, and product coefficient

The proof correctly quantifies over every first lift satisfying the first-order equation. No uniqueness or preferred choice of U is needed. In the scalar-placement errors, a derivative of epsilon b together with an epsilon U term first contributes in degree three. Thus no U survives in F or G.

Every scalar c is allowed. Its entire associator contribution is the scalar K Id, including the ordinary product terms in b. A second-order scalar cocycle has not been assumed and cannot be used to hide the obstruction.

For an arbitrary matrix-valued second edge W, write W_ij=g_ij w_ij. Its change in M is delta_row w. Hence its next boundary vanishes. The separate formal control also keeps six independent second edges and checks their inverse-free ordered cancellation directly.

The calculation requires associativity of the common ambient product and its specified first coefficient mu, but not a particular second coefficient nu. Terms involving nu and epsilon b start in degree three. For the additional interpretation as literal h*T or T*h, the proof correctly assumes a normalized/unital star product. Then nu(1,G)=nu(G,1)=0, while mu(1,G)=mu(G,1)=0 already follows from the displayed derivations, and

    h*T=hT+epsilon^2 mu(b,g),
    T*h=hT-epsilon^2 mu(b,g).

Thus the labels lambda=1 and lambda=-1 are justified with exactly the stated normalization caveat.

## 3. Independent mask computation

On the common accepted carrier, the structural identity P_c I_c=Id reduces the actual transition to the cocharacter D(nu_j/nu_i). This is the use of a proved morphism identity, not an entrywise primitive-matrix evaluation.

Let d_ab,s=m_b,s-m_a,s, let R=(V_0r_0)(V_1r_1)diag(1,-1), and set

    beta_ijk=A d_ij,0 d_jk,1+B d_ij,1 d_jk,0.

Scalar differentiation and the formal logarithmic-current identity independently give

    F=(beta_ijk/2)(d_kl,0-d_kl,1) R,
    G=(beta_jkl/2)(d_ij,1-d_ij,0) R.

The second formula uses the exact simplification G=g_ij^-1 mu(b_jkl,g_ij). Extra bits are annihilated by V_0,V_1 and cancel in normalization.

Direct substitution gives all four reviewed rows:

    masks (0,1,3,5): F=(A/2)R,  G=0;
    masks (0,2,3,6): F=-(B/2)R, G=0;
    masks (0,1,2,3): F=(A/2)R,  G=-(B/2)R;
    masks (0,2,5,7): F=-(B/2)R, G=(A/2)R.

For the fixed coefficient A=15/4, B=0, the final two rows isolate F=(15/8)R and G=(15/8)R respectively. Their necessary conditions force lambda=-1 and lambda=1 simultaneously. The sign of the isolated G is positive; the negative ordinary anomaly comes from its coefficient lambda-1.

For the joint family, the first two rows give (1+lambda)A=(1+lambda)B=0. If either coefficient is nonzero, lambda=-1. The other two rows then give B R=0 and -A R=0, forcing both coefficients to vanish. This is a valid contradiction in characteristic zero with constant coefficients.

The bounded same-edge repair is also correctly identified. For e_ij=t q_0,ij q_1,ij, additivity gives delta e=-t(Q01+Q10). The repaired coefficients satisfy A=15/4-t, B=-t, hence A-B=15/4. They cannot both vanish. The regular first-lift change U'=U+e g has precisely the stated effect b'=b+delta e.

## 4. Actual common overlap and nonzero section

All four quadruples use strictly increasing mask values. Their union consists of masks 0,1,2,3,5,6,7 on one existing carrier. Their joint legal locus is

    L=(U_0 intersection U_1)_0
        times (U_0 intersection U_1)_1
        times (U_0 intersection U_1)_2 times U_0,3.

It is a dense nonempty open in the integral product C^4. The accepted carrier Omega_c is nonempty: the nonconstant curve x-map is surjective onto P^1, and the coefficient map from four copies of P^1 is surjective onto P^4 by binary-quartic factorization over C. Therefore Omega_c intersection L is nonempty. Since L lies in U_0 in every factor, a common finite standard tag is available. There is no covert empty-overlap issue or newly invented primitive localization.

The needed r_0,r_1,r_2 and x_0,x_1,x_2 are units on this legal locus. Regularity of the structural transitions is supplied by the accepted source-bound dependency. The quotient rule and curve relation give, as a rational identity,

    V(y/x)=(x^2+1)/(2x).

Because x is nonconstant, x^2+1 is not the zero rational function. Integrality of C^4 then makes R a nonzero rational section; its restriction to any nonempty open remains nonzero. It may vanish on proper divisors, which does not affect the section-level contradiction. No actual point or physical polynomial was evaluated to prove nonemptiness or nonvanishing.

## 5. Independent controls and their limited role

`check_review_controls.py` was independently written for this review. It uses only exact rational arithmetic, invented noncommuting word labels, formal central scalar-jet labels, and abstract binary-mask metadata. It imports only Python's fractions module. It does not import or read source/model data and does not build actual matrices or physical polynomial models.

The normal and optimized executions both pass; transcripts are `review-control-normal.txt` and `review-control-optimized.txt`. Checks include:

- the four-term correction coboundary delta N=-F-G with the ordered products retained;
- the left/right scalar-side specializations 2F and -2G;
- cancellation of all six independent second-edge corrections;
- all four mask coefficient rows and their ordered-cup cocycle identities;
- detection of sign reversal, mixed-sector doubling, endpoint word-order reversal, and an ordered-cup-slot swap.

Failures use explicit exceptions, so optimized Python does not disable the tests. These controls support the universal formal algebra and mask bookkeeping only. The actual geometric binding and nonzero-section argument remain the written proof and its accepted structural inputs, rather than any claimed source computation certificate.

## 6. Scope retained

The accepted result fixes the common ambient star algebra, its first bidifferential coefficient, the zeroth-order transitions, and the displayed constant-lambda modification. The optional stronger conclusion is limited to the displayed constant two-parameter bilinear family. It does not classify arbitrary cochains or scalar coboundaries.

In particular, this is not an exclusion of general star-gerbes with algebra transition automorphisms, arbitrary non-scalar twists, changed zeroth-order data, or other deformation formulations. It does not compute a same-pair degree-two cohomology class: the defect in question fails closure. It says nothing new about mixed-class exactness or algebraicity. No public write, source/model execution, guard change, or quantitative execution claim is part of this review.
