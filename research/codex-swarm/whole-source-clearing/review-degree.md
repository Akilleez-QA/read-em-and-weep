# Independent V01 review: finite degree218 to217

**Accepted theorem:** for the stated actual FINITE-frame F12 equation, assuming the separately audited factored clearing identity makes P_finite=(product_v H_v^14 ell_v0 ell_v1)F12 a polynomial, its coordinate degrees are bounded by217 on coordinates0,1 and210 on coordinates2,3. The more precise per-tuple target uses assigned homogeneous carrier degrees5(primary)/4(auxiliary) and legal degrees1(mask0)/3(mask1). This review accepts the coefficient-free degree refinement; it does NOT identify the resulting homogenization with the intended physical homogeneous/infinity-frame source.

Reviewed clearing.py SHA2562cc26945328dba5069d0b79888416b4d9d48b4031336fe266b2ffc103db3abef and PROOF.md SHA2563ea2b68a04168f76ba217b2b43470c41657124b550111c72a3eb10b60dd89361. Source model is read at10810ee877fdaf291399198ad60d7dd0c316a42d, research/hm/null-operator-compiler/hm-pinned-model.json. The separate CLR-R review owns exact circuit/source identification. No producer file was edited. No physical polynomial was multiplied, expanded, differentiated or evaluated here.

## 1. Independent literal primitive metadata check

I independently parsed every I/P entry and stored monomial exponent tuple, without substituting elementary polynomials. Shapes are I15x2 and P2x15 for all six carriers. Carriers0..4 each have28 nonempty I/P entries and56 stored terms; auxiliary5 has21 entries and24 terms. Every stored term has nonnegative four-exponent tuple and sum bounded by5+w(primary) or6+w(auxiliary), where w=column index for I and minus row index for P. No violations; minimum slack is0 in each carrier. Thus these bounds are actually checked against source entries, rather than stipulated for arbitrary matrices.

Literal denominators are di=dp=-H for primary0..4, and -(v1^2 v3 v4)=-v1*a for auxiliary5. In the finite chart v0=1, a=v1 v3 v4. Consequently H^2 times a primitive is -H times its stored numerator for primary carriers, and -v3 v4 times that numerator for auxiliary5. The latter has multiplier coordinate degree2, not degree3 or4.

Fix coordinate x and regard the other three coordinates as an unevaluated rational coefficient field. Each v_k=e_k is affine-linear in x. Exact coordinate degrees of H are4(carrier0),5(carriers1..4),3(auxiliary5): leading factors are nonzero elementary polynomials, never evaluated. The homogeneous assigned degrees are5,5,4 respectively. Therefore primitive rational degree at infinity is bounded by

    I_v[:,r]: r+epsilon_v,
    P_v[s,:]: -s+epsilon_v,
    epsilon_0=1, epsilon_1..4=0, epsilon_5=2.

These follow respectively from cleared numerator bounds9+w,10+w,8+w minus denominator degrees8,10,6. They use the finite auxiliary a, not a homogeneous v0 factor mistakenly counted as x-degree.

## 2. Ordered products and ordinary coarse bound

For K_ab=(P_a I_b)^t the entry(r,s) has rational x-degree<=r-s+epsilon_a+epsilon_b. In particular the transpose reverses which P row/I column supplies its weight. A derivative in x lowers rational degree by at least1; a derivative in another variable preserves this bound. Q_v,x=m_v,x*rf_x*diag(1,-1) has own-coordinate degree-1; Q in a different coordinate has degree0 in x. Thus T_ab,x has the K bound minus1 in x, while T_ab,y has the unchanged bound in x for y!=x.

In each ordered trace word K_ca T_bc,0 T_ab,1 or K_ca T_bc,1 T_ab,0, entry weights telescope to0 around the closed matrix-index cycle. The endpoint excesses sum to2(epsilon_a+epsilon_b+epsilon_c)=2n0+4n5. Differentiation does not introduce a further epsilon. Hence trace degree<=2n0+4n5-1 on a pair coordinate and<=2n0+4n5 off the pair. Constants -1/4 and15/4 do not affect degrees. The gerbe product q_ab,0*q_bc,1 has pair degree<=-1 and complementary degree0, so obeys these same coarse upper bounds.

Let d_v be the assigned homogeneous carrier degree, h_v the actual finite coordinate degree, and z_i the number of mask0 factors among the THREE source occurrences in pair coordinate i. A mask0 legal equation has homogeneous degree1 but finite value1 of coordinate degree0; mask1 has degree3 in both conventions. Therefore

    h_v=d_v-1 for carriers0/5, and h_v=d_v otherwise;
    sum deg_finite ell_vi = sum deg_hom ell_vi-z_i.

Relative to target D_i-2, where D_i=14 sum d_v+sum deg_hom ell_vi, the coarse polynomial bound is

    deg_x P_finite-(D_i-2)<=1-12n0-10n5-z_i.

All three counts are nonnegative integers. Thus the ONLY unresolved coarse case is n0=n5=z_i=0: all carriers1..4 and ALL THREE masks equal1 in coordinate i. No condition on the other pair coordinate is needed. This case partition includes mixed masks and repeated carriers; it never identifies owner occurrences.

## 3. Critical cancellation is universal and has the correct sign

In the critical case epsilon=0 and all endpoint Q_x are exactly the same rf_x sigma. With zero-based r,s, sigma_rr=1-2r, so

    (Q K-K Q)_rs=-2(r-s)rf_x K_rs.

Thus w=r-s in{-1,0,1} gives T_rs=partial_x K_rs-2w rf_x K_rs, NOT the opposite sign. The exact elementary identity is

    2rf_x=1/x+2/[x(x^2-1)].

For ANY rational f of degree<=w, write f=x^w u with u regular at infinity. Then partial f-w f/x=x^w partial u has degree<=w-2: the possible constant Laurent term of u differentiates to zero. The remainder -2w f/[x(x^2-1)] has degree<=w-3. Consequently degree T_rs<=w-2. This proves the additional degree of decay even for w=0 and w=-1, without assuming a nonzero leading coefficient, determinant cancellation, symmetry of source jets or knowledge of any physical coefficient.

Every mixed trace word contains EXACTLY one tangent differentiated in i, so each word gains this extra degree separately; no cancellation between the two trace words is presumed. The other tangent, differentiated in the complementary coordinate, does not raise its x-degree. The gerbe term vanishes: for i=0, q_ab,0=0; for i=1, q_bc,1=0, because all three masks in that coordinate coincide. Thus F12 has degree<=-2 in x in the critical case. Multiplication by the fixed clearing product proves degree P_finite<=D_i-2 there too.

## 4. Result and limits

For pair coordinates the bound is14 sum d_v+sum deg_hom ell_vi-2, at most210+9-2=217. For complementary coordinates it is14 sum d_v, at most210; exceptional carriers give extra slack. The naive uniform218 was a valid coarse bound, but is not the final degree bound. The improvement is an exact generic leading-weight identity, not sampled leading-coefficient evidence or a new support scan.

Once polynomiality of P_finite is established, rational infinity-degree bounds are polynomial coordinate-degree bounds. Therefore ordinary multihomogenization to these nonnegative per-coordinate targets exists. Identifying that candidate with the PHYSICAL homogeneous character representative still requires the original-frame/deck/infinity comparison. The producer appropriately leaves that gate false. This review provides no Laurent/source admission, historical-order equivalence, detector value, or obstruction conclusion.

Evidence used: exact hand degree argument plus complete literal exponent/shape/denominator metadata inspection. Additional artificial polynomial tests are unnecessary for the universal rational identity above; no physical-source algebra was run.
