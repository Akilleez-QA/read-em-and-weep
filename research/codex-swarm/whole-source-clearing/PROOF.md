# Actual finite whole-source clearing, with the homogeneous comparison exposed

Producer CLR01. Independent review pending. No physical coefficient is evaluated. The only operations on pinned source polynomials are reading matrix shapes, denominator syntax, and monomial exponent bounds. Matrix products and polynomial derivatives remain factored AST nodes. This is not an arithmetic or Laurent-admission certificate.

## Pinned source and order

`10810ee877fdaf291399198ad60d7dd0c316a42d` supplies the unchanged model/source excerpt, null's combined-pole proof/code, and order-comparison note. Their Git/SHA pins appear in the artifact. The contraction receipt is tied to the same model by canonical serialization, without executing its historical checker. The source first-current and whole scalar equations are those of `globalBuild2`/`crossResidual` and null's transition-scalar input. This is the fresh source-first order: carrier5 first, then primary0..4; numeric low-bit mask; standard tag. Nonlinear source formulas are evaluated only in that order and extended alternatingly. Historical comparison remains with null.

## 1. A uniform polynomial numerator for actual primitive matrices

Set v0=1, vk=e_k(x0,x1,x2,x3), a=v1 v3 v4, H5=a, and Hj=vj^5-product(v0..v4) for j=0..4. Let `Num(M)` denote the stored numerator matrix of I or P. The actual stored di/dp denominators, checked by literal monomial metadata, are

- primary0..4: `-Hj`;
- auxiliary5: `-v1*a`.

Consequently, **for every carrier**, `Hj² M` is polynomial: its numerator is `-Hj Num(M)` for a primary, and `-v3 v4 Num(M)` for carrier5. The latter follows from a=v1 v3 v4 and holds in the rational function field without borrowing another owner's factor. The AST's `catalog_cleared_primitive` names exactly these six cases; it does not stand for arbitrary matrices.

The inverse rewrite is source-derived. P_a I_b P_b I_a=P_a(1-gamma H0_b-H1_b delta)I_a=P_a I_a=1, and likewise in reverse, using the authenticated contraction identities. Thus, for K_ab=(P_a I_b)^t, K_ab^-1=K_ba. Every source owner remains distinct.

## 2. The whole actual F, not independent rational summands

Write sigma=diag(1,-1). Keep these different scalar quantities separate:

    Q_v,i = m_v,i*(x_i²+1)/(2*x_i*(x_i²-1))*sigma,
    q_ab,i = (m_b,i-m_a,i)/x_i.

Both Q endpoint terms occur in

    T_ab,i = partial_i K_ab + Q_b,i K_ab - K_ab Q_a,i.

Only q occurs in the ordered gerbe b12=(15/4)q_01,0 q_12,1. Removing the common y0 y1 character gives the actual scalar

    F12 = b12 - (1/4)tr[K20 (T12,0 T01,1 - T12,1 T01,0)].

The coefficient is 1/4: mu12 has 1/2 and the scalar trace correction has another 1/2. This equation is obtained by differentiating the physical transitions D_b K_ab D_a^-1, then cancelling matching endpoint D's in the normalized trace. Q cannot be replaced by q.

For binary mask bits, let ell_vi=1 if m_vi=0 and x_i(x_i²-1) otherwise. The exact identity

    q_ab,i = m_b(1-m_a)(x_i²-1)/ell_bi
             -m_a(1-m_b)(x_i²-1)/ell_ai

uses only owned pair-legal denominators. Q has numerator m(x²+1)/2 over its own ell; when m=0 the numerator is zero.

The rational DAG performs ordinary common-denominator addition, ordered multiplication, and the quotient rule **without expanding polynomial leaves**. A K_ab has H_a² H_b². A tangent has at most H_a³ H_b³ and at most one ell per actual endpoint in that derivative coordinate. Consequently the whole F has carrier ledger `(5,6,5)` on ordered source slots `(0,1,2)` and legal ledger at most one per pair coordinate/owner. Distinct derivatives mean no legal factor is squared in either trace product. Bringing b and the complete trace difference to that same owned denominator constructs an explicit polynomial N_F.

Thus the emitted polynomial

    P_finite = N_F H_0^9 H_1^8 H_2^9
             = C_0 C_1 C_2 F12,
    C_v = H_v^14 ell_v0 ell_v1,

is an actual finite-frame source identity. H subscripts in this display name source **slots**, not carrier IDs. No numerator in this argument is obtained by assuming null's desired source-clearing conclusion.

## 3. Degree proof: why the naive 218 becomes 217

Fix one coordinate x, treating the others as a characteristic-zero rational coefficient field. Let d_v be the homogeneous assigned carrier degree (5 for0..4;4 for5), and h_v its actual finite coordinate degree (4 for0;5 for1..4;3 for5). These exact finite degrees follow from the elementary-generator formulas: for primary1..4 the fifth-power term has degree5 whereas the product term has degree4; for0 the product has degree4; a has degree3. Their leading factors are nonzero elementary polynomials in the other variables; none is evaluated.

Each e_k is multilinear in x. Sparse exponent inspection establishes the stored numerator bound `5+w` for carriers0..4 and `6+w` for5, where w=column index for I, and w=minus row index for P. Normalizing to H² gives primitive rational degree at most w+epsilon_v, with epsilon0=1, epsilon1..4=0, epsilon5=2. This follows from multiplier degrees4,5,2 for0,1..4,5 respectively. The code checks these source exponent inequalities, rather than assigning weights to arbitrary source data.

For K_ab, entry (r,s) therefore has degree at most `r-s+epsilon_a+epsilon_b`. A partial derivative reduces rational degree by at least one. The physical Q_i coefficient has degree-1 in its own coordinate and degree0 in the others. Thus T_ab,i has the corresponding bound reduced by one in i. Ordered matrix multiplication and trace telescope the entry weights. Each source slot contributes one I and one P to every expanded Leibniz term of the trace, so its total excess is at most `2*count(carrier0)+4*count(carrier5)`. This is a degree proof, not a source matrix expansion.

For a pair coordinate let z_i count mask0 among the three source slots. The actual degree of the clearing product is `14 sum h_v + sum deg_finite ell_vi`, while its homogeneous degree is `D_i=14 sum d_v+sum deg_hom ell_vi`. Each exceptional carrier loses one degree, and each mask0 legal factor loses one degree. The resulting bound, compared with target D_i-2, is

    deg_x P_finite - (D_i-2)
       <= 1-12*count(carrier0)-10*count(carrier5)-z_i.

Hence every case is settled except all three carriers in1..4 and all three masks equal1 in that coordinate. For complementary coordinates the analogous bound is already at most the target D_i, with exceptional slack and no pair-legal factors.

In the critical pair case epsilon=0 and q_ab,i=0 on both edges. All endpoint Q_i are the SAME rf_i sigma. For entry weight w=r-s,

    T_ab,i[rs] = partial_x K_ab[rs] - 2w rf_i K_ab[rs],
    rf_i = 1/(2x)+O(x^-3).

If deg K<=w, `partial_x K - w K/x` has degree<=w-2: its possible degree w-1 term cancels identically, regardless of its coefficient. The rf remainder has degree<=w-3. Thus T has one additional degree of decay. Each trace term contains the i-tangent, so F has degree<=-2 in this coordinate, and b=0 there. This settles the only critical case. A generic source coefficient is never computed; the identity is a universal consequence of the actual first-current endpoint coefficients and the source's verified entry-degree bounds.

It follows that P_finite has coordinate degree at most `14 sum d_v+sum deg_hom ell_vi-2` on the pair, and `14 sum d_v` off the pair. The uniform maxima are **217/210**. The artifact retains the **naive218/210** bound visibly, together with the exceptional-slack and critical-cancellation proof. Homogenizing P_finite to these nonnegative multidegrees therefore defines a polynomial candidate P_hom.

## 4. What this does and does not identify geometrically

The finite identity above and the polynomial homogenization are constructive. The remaining independent source/frame obligation is to identify that homogenization with the intended physical F12 homogeneous character representative. Equality on the dense finite chart will then identify rational sections in that same authenticated frame; the producer does not silently equate different frame conventions. Geometric infinity/source admission stays false pending that audit and the exact transport contract. The finite218-to217 proof is not a blanket declaration that every rational source circuit has the right twist.

## 5. Exact seed12/30 combined numerator and derivative bindings

Each seed's four E34 branches share two scalar output edges. The v5 source binding, selector, weights, explicit tracefree request wrapper, and its unresolved comparisons are preserved. The input scalar remains T12 F12, in pair(0,1). For each edge(a,b), the artifact supplies C_a,C_b and standard Z_ab factors with literal full owners. Inserted u has exactly a's standard tag, inserted v exactly b's; their occurrence IDs stay different even when their polynomial factors agree. Both carrier domains are0..5, masks0..15, interpreted inclusively.

Using null's authenticated recipe, the **full sum** is

    N_ab = C_a C_b Z_ab B_ab
          + Z_ab sum_u Qhat_u P_[u,a,b]
          - C_a Z_ab sum_(u,v) Qhat_u Qhat_v P_[u,v,b].

B_ab is the COMPLETE `R(Kcov Pi + A h S Pi)F` cochain. It retains its support[-1668,5248] and its standard monomial predicates; it is not replaced by an arbitrary rational leaf. The second prism's extra C_a padding is mandatory. Source-first signed extension uses null's repeated-source zero predicate, while denominator occurrences never merge. Qhat uses null's exact N14 definitions, including its paired and complementary line factors and one frame pullback.

Only after forming this N is one derivative taken:

    partial_i(N/D) = [Delta partial_i N
       - N sum_f a_f(partial_i f) product_(g != f)g]/(D Delta).

All products are over labelled positive denominator factors. The artifact binds each E34 coordinate to this sequence and preserves two separately owned Z factors even when standard tags coincide. This is an exact specialization of null's universal implication, not a new proof replacing it.

Still absent are an executable complete B/partition coefficient program, instantiated inserted/source coefficient circuits and supports, a geometric homogeneous-frame comparison accepted by an independent reviewer, historical source/order transport, full detector assembly, and arithmetic/live-memory admission. The output leaves every corresponding gate false. The new concrete progress is the actual whole finite-F polynomial circuit and its source-specific degree proof, rather than a hypothetical arbitrary numerator declaration.
