Editorial scope: This is a mathematical source edition. Historical review and check statements describe the original artifact, not a fresh run. Supporting snapshots are dependencies, not additional new results. Later PR145 mixed-class vanishing supersedes historical unknown mixed-class status; it does not resolve the six pure diagonal conditions.

# Independent review: the retained-test / selector-connection pair

## Verdict and exact scope

**ACCEPTED, under the explicitly listed geometric and source-denotation premises. No mathematical correction is required.**

The exact plus-signed family

    p[-L G_ref,d J2(Z_d)] + (V_d p)[L J2(Z_d)]

has a tensorial full-character scalar interpretation, and hence a canonical-line coefficient on Y. Its full ordinary comparison is regular with either sufficient five-occurrence certificate

    carrier (26,17,14,14,5), legal (6,7,7,7,3),
    carrier (22,22,18,15,6), legal (6,8,8,8,4).

These give the stated uniform 26/7 and 22/8 bounds. The actual constant scalar row is regular on the entire degree-minus-two End term, rather than merely on one of its blocks. The assertion is about the grouped family, with the same original-reference derivative convention in both terms. It is not a separate regularity theorem for the source-reference selector-connection term.

The reviewed `PROOF.md` has SHA-256

    44a00dec309cf7516c6e8f4c696e50d56b2335368106248bfd566ab7ee121a12.

The reviewed `source-pins.json` has SHA-256

    aa603f160f8c9151803cba81f0cee925ccecfd60ecd897f20c7c25846f688f9e.

I read the complete producer proof and checker, the pinned common-split source, the complete frozen compiler as inert text/AST, the endpoint and HPL material, the retained-test premise, and the relevant accepted overlap, raw-block, homogeneous-frame and ownerwise dependencies/reviews. The checker authenticates all 20 listed input/dependency snapshots. Hashes establish the reviewed bytes; they do not establish the mathematical premises.

No physical source or model was imported, read as data, or executed. No actual matrix, polynomial, primitive, source, owner-value, jet or detector was constructed or evaluated. The only executable checks are inert-byte/AST authentication and small integer, formal-label and abstract-occurrence calculations. 

## 1. The frozen selector is a global regular morphism

The complete frozen `scalar_terms` function returns exactly

    L_(i,b)(M) = M_(3,1)[i,b]
                 - sum_(a,k) g_iak M_(2,0)[a,5b+k].

Here g is the fixed coefficient tensor of the homogeneous linear gamma map. The source does not insert coordinate-dependent gamma entries into this row: it inserts their fixed coefficients. Zero-coefficient omissions do not change the morphism. The conclusion does not require evaluating those coefficients.

The key (u,v) means K^(u-1) -> K^(v-1). Therefore:

- (3,1) is K^2 -> K^0 and has N-power 1-5=-4.
- (2,0) is K^1 -> K^-1 and has N-power -1-3=-4.

These are precisely the two blocks of End degree -2 in this four-term complex. Their fixed multiplicity spaces are tensored with the same line N^-4=q^*O_Y(-2,-2,-2,-2). Consequently any stated constant coefficient row on their direct sum is a global regular morphism to that line. It commutes with the common ambient restrictions, preserves deck character, adds no denominator and has constant coefficients in the common standard multiplicity frames. In particular L_A=L_ref and V_d L_A=0 are justified in the frames actually used.

The optional bottom chain-row identity also has the correct sign. For W of degree -3,

    d_End W = dW + Wd,

so the two relevant blocks are gamma W and W ev. The selected coefficient g_iak W_ab v_k occurs once positively and once negatively. This proves L d_End=0 on that degree without evaluating a gamma matrix, ev matrix or W. It supplies no implication L G=0, no cyclic-trace simplification, and no rank, basis or Serre-duality identification for the retained rows. The domain proof does not need such an implication.

## 2. Both transported anomalies have the claimed signs

Put a_A=V_d(log tau_A), and write F_A=LJ2,A(Z_d). The actual even-Hom coefficient law is F_A=tau_A^r F_ref with r=-2. Because the connection is V_d+G, its coefficient transport is forced to be

    G_A(M_A) = tau_A^r G_ref(M_ref) - r a_A M_A.

It follows that, with A_src=-tau_A^-2 L G_ref J2,ref and A_loc=-L G_A J2,A,

    A_loc = A_src - 2 a_A F_A,
    A_src = A_loc + 2 a_A F_A.

The test is a section of the dual line, with p_A=tau_A^2 p_ref. Thus its transported source derivative is

    D_src p_A = tau_A^2 V_d(p_ref)
              = V_d p_A - 2 a_A p_A.

Combining these equations gives the exact identity

    p_A A_src + (D_src p_A) F_A
       = p_A A_loc + (V_d p_A) F_A.

At infinity a_A=-u_d/t_d. Therefore the source selector term has the relative correction -2(u_d/t_d)F_A, while the transported test derivative has the relative correction +2(u_d/t_d)p_A. The signs are opposite. A minus sign between the two source summands would double, rather than cancel, these corrections.

Every factor of tau_A must be included in p_A. Other-coordinate factors have zero V_d logarithmic derivative, but their line exponents are still necessary for overlap gluing. The proof handles this correctly; it does not replace the full source test by an unrelated local function.

For a general overlap lambda=tau_B/tau_A,

    F_B=lambda^-2 F_A,
    p_B=lambda^2 p_A,
    A_loc,B=lambda^-2 A_loc,A+V_d(lambda^-2)F_A.

The two cross terms in the local expression are proportional to

    lambda^2 V_d(lambda^-2)+lambda^-2 V_d(lambda^2)=0.

Thus the pair glues as an unstripped scalar on X. This is the essential tensorial statement. Its two local summands are not individually being asserted to glue as scalars.

## 3. The local connection has an owned all-chart bound

The source common-split connection is

    G_ref = ad_B + r(-m_d y_d/x_d),

where r is the Hom degree, not the difference of the resolution N-powers. The latter difference is 2r, which has already been included through 2r beta with beta=-m_d y_d/(2x_d).

After the necessary connection transport, the scalar one-odd-factor coefficient of G_A is

    -r m_d/x_d on a finite chart,
     r(1-m_d)/t_d on an infinity chart.

For r=-2 the coefficients are 2m_d/x_d and -2(1-m_d)/t_d. On the finite chart only bit 1 can give a pole, and its own legal section x_d(x_d^2-1) clears it. At infinity only bit 0 can give a pole, and its own legal section t_d clears it. The other two scalar cases vanish. No different occurrence supplies this factor.

The accepted raw-block theorem clears each b in B=z_d b by carrier 5/legal 1 at that same leading occurrence. The left and right B actions and the scalar contribution are added, not multiplied, so the same 5/1 is a common padded allowance for their sum. It is not 10/2. Earlier H or j charges at that occurrence remain and must add to this 5/1.

This is a bound for the correctly represented local connection action. It does not turn G into a tensorial zero-order operator, or give the transported reference action the same isolated domain. The missing-d input makes coefficient extraction especially simple. More generally, when d is already present, multiplying by z_d adds the regular branch polynomial z_d^2, rather than requiring division by z_d.

## 4. The canonical line and product rule are valid on every chart

The coefficient of a degree-r, character-S ambient section is in O_Y(r*1-2*1_S). For F=LJ2(Z_d), r=-2 and S omits d. Its coefficient line therefore has degree -2 in d and -4 in each other direction. Multiplication by the actual global test p gives coefficient degree 0 in d and -2 in every other direction.

Since d is absent from the character, V_d differentiates only that base coefficient in direction d. In a finite chart it contributes y_d partial_(x_d); at infinity it contributes -u_d partial_(t_d). The full invariant vector field also has a non-base-coordinate derivative, but that part does not act on this missing-d coefficient. This observation applies both to pF and to the fixed-physical-row endpoint Z_d. No assumption V_d Z_d=0 is made.

The derivative adds the missing odd bit and the missing -2 coefficient-line degree. The result is full character with coefficient in O_Y(-2,-2,-2,-2)=K_Y. Projection to that character is a regular direct-summand map in the finite-flat quadratic algebra after invariant clearing. It is not division by a vanishing odd monomial at a branch point.

An independent local derivation checks the displayed stripped formulas. On the switched factor f_B=t^-2 f_ref(1/t) and p_B=t^2 p_ref(1/t). Transporting the original-reference derivatives gives

    f: -partial_t f_B - 2 f_B/t,
    p: -partial_t p_B + 2 p_B/t.

Their plus-signed product is -partial_t(p_B f_B). These expressions confirm both the infinity derivative sign and the dual test correction.

The operator identity with fixed common ambient restrictions is

    J2'=-G_ref J2+H C J1+H delta H C j.

Applying it to a varying Z_d adds J2(V_d Z_d). Using L'=0 therefore proves exactly

    Q_d=V_d[pLJ2(Z_d)]
        -pL(H C J1+H delta H C j)(Z_d)
        -pLJ2(V_d Z_d).

Both overlap terms and the entire input derivative are indispensable. The independent ordered-word checker verifies this identity without commuting H through delta. If ambient restrictions really move, their derivative terms must be restored; the proof explicitly uses the fixed common ambient convention rather than suppressing a genuine restriction derivative.

## 5. Independent occurrence enumeration confirms both bounds

I independently enumerated all 20 deleted-face branches of H delta H delta j on an abstract five-position tuple. Every occurrence selected before a later face deletion retained its charges. The implementation does not reuse the producer's vector-max recursion.

Starting with Z carrier/legal (9,14,5)/(4,7,3), the resulting J2 envelope is

    (21,17,14,14,5)/(5,7,7,7,3).

Adding the local G allowance at the actual first output occurrence gives

    (26,17,14,14,5)/(6,7,7,7,3).

Regular multiplication by p_A adds no pole. The local derivative V_d p_A has regular one-odd-factor coefficient on the whole standard chart, so its product with F has the smaller J2 envelope. This proves the direct bound after the independently established grouping law.

For the product-rule proof, differentiating a fully cleared local fraction raises each named carrier exponent by at most one and each direction-d legal exponent by at most one. Padding the legal increment to every direction is safe. Numerator derivatives and all denominator derivatives are retained. Hence the scalar-product derivative has envelope

    (22,18,15,15,6)/(6,8,8,8,4).

Differentiating the endpoint gives (10,15,6)/(5,8,4). Applying the original j/H/delta occurrence rules independently gives the same final envelope for J2(V_d Z_d). This uses the endpoint's fixed physical frame and missing-d character; a general untransported derivative of an arbitrary nonzero-degree coefficient would not justify the estimate.

Independent enumeration of the two first-face C insertions yields

    H C J1:       (9,22,14,14,5)/(1,6,7,7,3),
    H delta H Cj: (13,18,18,14,5)/(1,6,7,7,3).

The coordinatewise maximum of these four independently regular families is precisely

    (22,22,18,15,6)/(6,8,8,8,4).

Neither certificate is an exact attained pole-order claim. The two uniform bounds trade carrier against legal allowance and neither dominates the other. They must not be combined by taking the smaller entry of each without another proof.

## 6. The failure mode is real, but no actual endpoint failure is asserted

Take an infinity direction for which all available direction-d legal bits are 1. Their sections are 1-t_d^2, so none owns the equation t_d. On a locus where the permitted carrier factors are units, the isolated source-reference term has residual stripped coefficient -2f_A/t_d after subtracting its regular local part.

More generally, let C be the fixed clearing product for the regular local contributions. The exact condition for separate regularity is

    t_d divides C f_A.

For the mismatched pair using A_src with only V_d p_A, the exact condition is instead

    t_d divides C p_A f_A.

These conditions are neither replaced by an assumption that C is a unit nor automatically imposed on the actual input. A retained p can vanish on the divisor. A carrier can already contain the divisor. A particular f can satisfy the required divisibility. The reviewed proof correctly refrains from deciding any of these actual-source questions.

A tiny actual-frame example explains why a generic claim cannot ignore the correction: set the local infinity coefficient f_B=1 and local test p_B=1 in one direction. Their reference coefficient labels are f_ref=x^-2 and p_ref=x^2. The transported reference derivative contributions are -2u/t and +2u/t, while the local scalar product is constant in that direction. Pairing the first transported contribution with the local test derivative 0 leaves -2u/t. On the actual curve u^2=t(1-t^2), ord(t)=2 and ord(u)=1, so this is genuinely nonregular. This is an invented rational-section/frame control, not a realization or evaluation of the actual endpoint, retained test list or J2 output.

## 7. Full ordinary weights suffice; no boundary or value follows

Each actual source occurrence retains its original carrier, legal mask and target tag. The unchanged weights 54/29 dominate the direct certificate with carrier slack (28,37,40,40,49) and legal slack (23,22,22,22,26). They dominate the product-rule certificate with slack (32,32,36,39,48)/(23,21,21,21,25).

If C'_o is either certified occurrencewise clearing factor, the regular compared summand is

    [(product_o C'_o)b_d] product_o(rho_o/C'_o).

The quotient for each occurrence is regular on its own chart. The inherited standard-factor exponent 5251 only introduces denominators that are units on the full tagged target intersection; it is not used to conceal the infinity connection anomaly. Distinct occurrences remain distinct even if their labels, divisors or target tags coincide. A partial prefix comparison with an unweighted suffix does not acquire this full-comparison conclusion.

For Omega equal to the product of all five weights, the weighted product rule retains

    V_d[p Omega F]
      =Omega[Q_d+pL O_d(Z_d)+pLJ2(V_d Z_d)]
        +(V_d Omega)pF.

The independent checker expands all five separate weight-derivative slots. Regularity of the grouped coefficient alone proves no exactness, total divergence, Serre-trace zero, full remainder cancellation or retained-test value. In particular it does not remove baseline terms, either Fk branch, the current/input derivative, or the outer derivatives.

The supplied latest public `null-overlap-homotopy` snapshots at commit fdbf6651861df586f9c29aec2e1dd3fec6363ae8 were compared byte-for-byte with the supplied shared snapshots and authenticated against their Git blobs. Their exact overlap reduction and separate conditional boundary domain explicitly leave the selector connection and other source families untouched. The present theorem addresses a different grouped domain and is compatible with that frontier. No fresh remote-state or current-HEAD attestation is claimed.

## 8. Independent controls and remaining premises

`check_independent_pair.py` performs 5,118 explicit checks. It covers 1,024 chart-overlap/direction cases, 1,024 chart/legal-mask/direction cases, all 20 J2 face branches, both overlap ledgers, all 30 admissible constant selector rows through universal coefficient labels, the actual-curve infinity valuation, and exact ordered-word product rules. Fourteen active negative controls reject the specified frame, sign, selector-degree, dropped-overlap, dropped-input, frozen-weight and merged-owner errors.

`independent-normal.json` and `independent-optimized.json` are byte-identical. I also reviewed and ran the producer checker in both modes; `reviewer-producer-normal.json` and `reviewer-producer-optimized.json` are byte-identical. The checks use explicit exceptions, so optimization does not disable them. They authenticate syntax and discriminate finite formal errors; the line, regularity and divisibility arguments above supply the mathematics.

The actual root/even-Hom identification, all-chart homogeneous primitive and raw-block theorems, normalized contraction, physical endpoint denotation, fixed common ambient restriction convention, authenticated global retained-test interpretation and full ordinary comparison remain named mathematical premises. This review does not reverify source arithmetic or source values. The new conclusion is exactly the regular canonical-line domain of the plus-signed selector/test pair, with unchanged weights and no higher-order conclusion.
