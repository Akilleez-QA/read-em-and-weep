# Independent audit of the owned-denominator finite scalar domain

## Verdict and scope

The positive-twist owned-denominator complex is a valid finite scalar cochain model. Its degree-one cohomology vanishes, its actual denominator sections define the common cover, and the established scalar solutions belong to its degree-one space. The bounded total-primitive construction below admits its scalar gauge primitives to the authenticated detector comparison. Consequently the scalar adjoint annihilates the finite degree-one kernel.

This is a source-independent mathematical certificate using the previously authenticated geometric and local-contraction identities. No source polynomial, residual, coefficient, partition expansion, jet, or obstruction value was evaluated. No practical quotient pivots, explicit eta coefficients, transpose-solve residual artifact, product ledger, or peak-byte schedule were computed. 

## Sources

The geometric definitions and local contractions are pinned to commit `08b73637d4136f91606aad332c46cafd064417f8`:

- [Cover equations and local contractions](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/source-identity.md), sections 1–3.
- [Physical frames and owned poles](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-geometric-dependencies/frames-and-poles.md).
- [Closed End lift and totalization conventions](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/closure-and-characters.md), section 3.
- [Pinned linear resolution and tensor contraction](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-proof/finite-model/full-sign-boundary-oracle.js).

The present audit read the previously authenticated regular-cover transport note, which states the exact global legal sections and End degrees −3 through 3, together with `refined-tracefree-pole-domain.md`, `scalar-cover-and-domain-audit.md`, `authenticated-refined-detector-composition.md`, and `direct-dual-scalar-fill-contract.md`. The pinned links identify the underlying sources; this audit does not claim a fresh full replay of their contraction matrices.

## 1. Actual homogeneous denominators and coverage

Let X=(P1)^4 and F=O(0,0,−2,−2), with the analogous permutation for the other pair. For an actual common-cover vertex v=(e,b,m), put

    d_v = H_b^14 product_i ell_(m_i,i) product_i Z_(e,i)^5250.

Here Z_(e,i)=Y_i for e_i=0 and X_i for e_i=1. The legal sections are

    ell_(0,i)=Y_i,
    ell_(1,i)=X_i (X_i^2−Y_i^2).

The carriers are H_*=a and H_j=h_j, where

    product_i(Y_i+X_i z)=sum_(j=0)^4 v_j z^j,
    a=v0 v1 v3 v4,
    h_j=v_j^5−v0 v1 v2 v3 v4.

These are genuine homogeneous sections. Their nonvanishing loci give exactly B_v=U_e intersect V_(b,m). The legal pair covers each P1 because Y_i=0 implies ell_(1,i)=X_i^3 is nonzero. The standard charts cover. Finally all carriers cannot vanish: h_j+v2 a=v_j^5 would force every v_j to vanish, whereas a product of four nonzero linear homogeneous-coordinate factors is a nonzero polynomial. Thus the family d_v has no common zero.

Distinct COMMON vertices remain distinct indices even when their standard tags, carrier labels, legal labels, or divisor factors agree. Repeated divisor factors then acquire the correct additive multiplicity. Only an identical repeated common vertex is killed by alternating normalization.

## 2. The positive-twist Koszul resolution

Write L_v=O(div d_v) and define

    C^q = direct_sum_(|I|=q+1) F tensor product_(v in I) L_v.

The index I ranges over increasing subsets of distinct common vertices. The differential inserts a missing vertex with the usual alternating sign and multiplies the numerator by its d_v. The augmentation is F→C^0, f↦(d_v f)_v.

This is the wedge-by-d Koszul cochain complex for the section d of direct_sum_v L_v. At every point some d_v is invertible in a local trivialization. Contraction against that coordinate divided by d_v supplies a local contracting homotopy. Hence the augmented sheaf complex is exact. Positive twists, rather than their negatives, are essential for this differential convention.

Let V^q=H0(X,C^q). In every coordinate a nonempty summand has degree at least 5250−2=5248. All such line bundles are acyclic by the standard cohomology of P1 and the product formula. Therefore C^bullet is an acyclic resolution of F, and

    H^q(V^bullet)=H^q(X,F).

For F=O(0,0,−2,−2), the product formula gives H1(X,F)=0: a degree-one contribution would require H0 of one of the two O(−2) factors. Thus ker D1=im D0 for the actual finite maps D0 and D1.

This proof uses the entire finite Koszul resolution to establish the equality at degree one; it does not infer exactness from an arbitrary truncation of Laurent support.

## 3. Faithful cochain representation and scalar inclusion

A numerator in the summand indexed by I represents the rational F-section obtained by dividing by product_(v in I)d_v. It is regular on the actual intersection B_I. This realization is injective, and its differential is exactly the scalar Cech differential: multiplying by the missing denominator merely aligns fractions. No projection or truncation occurs.

The existing scalar solutions have owned orders at most carrier14, legal1, and standard-boundary5250 per actual edge vertex. Multiplying by the two actual d_v clears all their divisorial poles, including coordinate boundaries. On the smooth, hence normal, variety X the resulting rational line-bundle section extends globally. Therefore every demanded scalar solution lies in V1, and its actual Cech image lies in V2. The homogeneous numerator spaces provide finite monomial bases without unidentified relations.

## 4. Gauge-domain admission by a bounded total primitive

Let f∈V0 and A=A_p(f) be the degree-one End-valued primitive from the exact identity

    E_p(delta f)=−delta A_p(f).

The already authenticated physical derivative/current ledger applies to arbitrary f in this denominator space: derivative orders are at most15/2/5251 and current orders at most9/5, giving A and delta A the conservative owned bounds24/7/5251. High numerator degree does not add a new divisor pole.

Put R=delta A and take its authenticated closed total lift J(R)=J0+J1+J2+J3. For D=delta+(-1)^q d_End, construct a total degree-one primitive as follows:

    K0=jA,
    K_(s+1)=(-1)^s H_(-s)(J_s(R)−delta K_s),  s=0,1,2.

K_s has Cech degree1+s and internal degree−s. For s=0, the defect has zero augmentation because R=delta A and the augmentation respects restrictions. The pinned local contraction therefore applies. At each subsequent stage, DJ=0 and the preceding identity make the next defect d_End-closed; negative internal cohomology vanishes. Consequently

    delta K_s+(-1)^s d_End K_(s+1)=J_s(R),  s=0,1,2.

The End complex has no internal degree below−3 and is exact at negative degree. The final defect J3−delta K3 is closed in degree−3 and hence zero. Thus

    DK=J(R).

The signs above are determined by the Cech degree2+s of K_(s+1): its vertical contribution has sign(-1)^(2+s)=(-1)^s.

Inclusion adds carrier4/legal2, and every End homotopy adds carrier6/legal3. Both summands of each defect have the same inherited bounds. Hence

    K_s: carrier≤28+6s, legal≤9+3s, standard-boundary≤5251.

At s=3 the maxima are46/18/5251. The full J(R) has the same stage bounds. Every owner remains an actual tuple vertex, and no absent apex is introduced. These bounds fit inside the fixed carrier54/legal29 comparison domain with the same standard-tag projection r. The actual standard factors are units on the corresponding target intersections, just as in the authenticated refined comparison.

The enlarged numerator domain also fits the existing GLOBAL homogeneous envelope; it need not fit the smaller scalar solver Laurent box. Each E(V1) output has the full-sign End character and the established owned poles. For a lift component of internal degree−s on m=s+3 vertices, clearing with the fixed outer54/29/5251 denominators gives coordinate numerator degree at most 5608m−s−2. With m≤6, the same quotient-degree and frame-reversal calculation therefore gives the conservative transported envelope [−45684,73705]^4 for every such input. This argument depends on poles and line-bundle twists, not source-specific numerator sparsity. The K_s components have one fewer vertex and fit as well.

Applying its chain map S Pi_out gives a total boundary. The full authenticated dual cocycle annihilates that boundary. The three-row formula for Phi agrees with that full cocycle on J(R), since J(R) has no internal-degree-positive components. It follows that Phi(delta A)=0 and hence

    D0^t e=0, where e=E_p^*Phi.

Together with ker D1=im D0, this establishes that e annihilates ker D1 on this finite model.

## 5. What remains computationally open

The finite direct-fill theorem now applies to this domain: an eta with D1^t eta=e exists, and the pivot-minor formula in the direct-dual contract is mathematically valid. That does not compute a useful pivot structure, an inverse, or eta's explicit coefficient rows. A practical implementation must still provide its exact instantiated maps, pivot/rank and residual certificates, exact regularized adjoint rows, and a complete product/byte schedule. Existence and finite-dimensionality do not establish efficiency.

## Dependency scope

Companion references are identified by basename. A referenced file not supplied with this collection is an external prerequisite, not an embedded proof or a verified relative link. The reading order and unresolved conditions are listed in `proof-notes-index.md`. Reported test results describe the source audit; this proof copy does not by itself constitute a new test run.
