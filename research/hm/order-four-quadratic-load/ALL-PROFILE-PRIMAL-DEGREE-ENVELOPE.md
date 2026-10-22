# The primal finite degree envelope excludes46 further quotient labels

## Result

The published finite Gauss-flag degree envelope excludes46 labels from the baseline144:40 in profile(1,1),6 in profile(1,2), and none in profile(2,1). Input-relative,144 becomes98. Combining the independently published exclusion of G3.21.bf8462f3a0d7 gives **143→97**, with profile counts **82/4/11**. All original182 stable IDs are preserved; no profile is closed and no realization or SF conclusion is asserted.

The general theorem is [PR715 at8ddbcedc7e01f33ae9aacff56df8da0a33503b57](https://github.com/Akilleez-QA/read-em-and-weep/blob/8ddbcedc7e01f33ae9aacff56df8da0a33503b57/research/hm/order-four-quadratic-load/NEGATIVE-GAUSS-FLAGS-HAVE-A-FINITE-DEGREE-ENVELOPE.md). The prior case exclusion is recorded separately at commit f0aaf0dcc7e4503fb6199ddab4bcc8e08a679c66, not counted among the46 new exclusions.

## Universal primal orientation

For every surviving maximal rank-three profile, take the actual saturated subbundle E of the constant thirty-space and its actual Gauss kernel K=E^-. The derivative of E has generic rank3, so rank K=17-3=14. By definition A=E/K is locally free, of rank3. Since deg E=-54,

    deg K=-54-deg A.

The quotient A injects into the ambient quotient (H tensor O)/K through E/K. A local section of K has derivative lying in E, since K kills E's second fundamental form. Consequently K's second fundamental form factors through A(-2), and the injection just described ensures this factorization has exactly the actual Gauss kernel.

K is saturated in the same constant ambient bundle: E/K and the ambient quotient by E are locally free. The published strict-slope result gives top K<=-3; strict negativity would already suffice. Thus all hypotheses of the finite degree-envelope theorem apply with F=K and J=A, irrespective of whether K is an interior stage or an endpoint. In particular this argument uses neither k>=2 nor an assertion about the next derivative rank. It applies to profiles(1,1),(1,2),(2,1) with the same orientation.

## Finite calculation

Expand each rank-three A into ordinary degrees lambda1>=lambda2>=lambda3, repeating a degree by its irreducible dimension. The theorem gives the necessary inequality

    -54-(lambda1+lambda2+lambda3)
      <= max sum_i [h_i lambda_i-h_i(h_i+1)],

where h1>=h2>=h3>=0 and h1+h2+h3=14. These heights are exactly the conjugates of all allowed positive derivative-rank partitions. No later derivative rank or maximal-profile refinement is imposed.

The checker exhausts this explicitly finite height set for every active baseline label. A label is excluded precisely when its actual degree exceeds the maximum. The certificate lists every new stable ID, expanded degrees, actual degree, capacity, positive gap, and maximizing heights. It also partitions all182 original IDs into baseline historical exclusions, the prior689 exclusion, the46 new exclusions, and97 surviving labels. The prior689 ID is not among the46.

## Reproduction and scope

Run `python3 verify_all_profile_primal_degree_envelope.py` to generate `all-profile-primal-degree-envelope.json`. The checker uses only standard Python and the two hash-pinned published inputs present at base715: baseline144 and the general theorem. It does not import a local audit report, another verifier, unpublished witness tables, or the output being checked. The independently produced audit agrees with the46 stable IDs exactly.

All computations are bounded abstract integers and splitting degrees. No actual coefficients, points, source matrices, actual-instance ranks, scans, spikes or consumed experiments are used. This is an unrestricted primal necessary-condition application only: dual and maximal-profile refinements are separate claims.
