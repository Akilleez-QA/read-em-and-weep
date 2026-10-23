# A finite-jet bound for the actual dual Gauss-kernel chain

## 1. Theorem and conventions

Work over C on P1. Let E be a saturated vector subbundle of the constant bundle H tensor O, with H finite-dimensional. Let R be its constant span: the smallest vector subspace of H such that E is contained in R tensor O. Put S=E-perp=(H O/E)*, as an actual subbundle of H* O. Define S_0=S and

    S_(j+1)=ker(beta_(S_j)),

where beta is the second fundamental form for the constant connection on H* O. There is no choice of a connection on a splitting summand.

Suppose m is a nonnegative integer and E(m) is globally generated. Equivalently, every ordinary Birkhoff splitting degree of E is at least -m. Then

    S_m = R-perp tensor O.                           (1)

In particular, if E spans H, equivalently H0(S)=0, then

    S_m=0.                                          (2)

The number m is optimal in general. No equivariance, plateau rank, completeness of a polynomial coefficient system, or nonramification assumption is required.

The kernels in this statement are the actual sheaf kernels, which are already saturated. Indeed beta_F is O-linear into the locally free bundle (H* O/F) tensor Omega1. Its image is torsion-free, so F/ker(beta_F) is locally free on the smooth curve. An extension of this quotient by H* O/F shows that H* O/ker(beta_F) is locally free. Induction therefore makes every S_j saturated in the same constant ambient bundle.

## 2. Polynomial generators and their constant span

An inclusion O(b)->H O can be nonzero only for b<=0. Thus choose a Birkhoff splitting

    E = direct sum_i O(-a_i),   0<=a_i<=m.

This is a splitting of bundles only, not a horizontal splitting. On the standard affine chart with coordinate t, the image of the usual frame of the i-th summand is an H-valued polynomial

    p_i(t)=sum_(k=0)^a_i v_(i,k) t^k.

These p_i are a frame of the actual embedded E on that chart. The constant span R is exactly the span of all v_(i,k). One inclusion follows from the displayed formula. For the other, if a constant linear functional vanishes on E, its pairing with each polynomial is identically zero, so it vanishes on every coefficient. Equivalently the map E->(H/R)O vanishes on the dense affine chart and hence globally, including the omitted point. This argument does not require the coefficient vectors of any individual generator to be independent.

Every global section of S is a constant vector of H*: global sections of a trivial bundle on P1 are constant. Such a vector annihilates E precisely when it annihilates R. Hence H0(S)=R-perp, which proves the stated equivalence.

## 3. Exact jet-annihilator identity and the pairing sign

On any open subset of the affine chart, use D=d/dt on the ambient constant bundles. We claim, as an equality of sheaves there, that

    S_j = {s : <s,D^a p_i>=0 for every i and 0<=a<=j}. (3)

For j=0 this is the definition of S. Suppose (3) holds at j-1. A local section s belongs to S_j exactly when s belongs to S_(j-1) and Ds belongs to S_(j-1); this is precisely the local expression of beta_(S_(j-1))(s)=0. The connection respects the ordinary evaluation pairing, so

    D<s,D^a p_i> = <Ds,D^a p_i> + <s,D^(a+1) p_i>.  (4)

There is a plus sign in the product rule; after imposing the zero pairing it becomes <s,D^(a+1)p_i>=-<Ds,D^a p_i>. If s and Ds lie in S_(j-1), (4), for a=0,...,j-1, proves all the extra vanishings required at j. Conversely, if s annihilates derivatives through j, it belongs to S_(j-1), and (4) makes Ds annihilate derivatives through j-1. This proves (3) in both directions.

The sheaf statement permits arbitrary regular local coefficients in s, not merely constant vectors. It does not assume an osculating image has constant rank. Nor does it equate a coherent image with its saturation. Under a change of local frame of E or a change of coordinate, derivatives up to a fixed order change by an invertible triangular transformation of the full jet-generated sheaf; alternatively (3) is already identified with the intrinsic S_j, so its use is coordinate independent.

## 4. Taylor inversion and the global conclusion

For any vector polynomial p(t)=sum_(k=0)^d v_k t^k, characteristic zero gives the polynomial identities

    v_k = sum_(a=k)^d binom(a,k) (-t)^(a-k) D^a p(t)/a!,
                                                        0<=k<=d. (5)

They follow by comparing coefficients of an independent variable z in the exact Taylor formula p(z)=sum_a D^a p(t)(z-t)^a/a!. Thus derivatives through d generate, over the affine coordinate ring, exactly the constant coefficient-span bundle. This is a polynomial identity, not evaluation at any selected parameter.

Because a_i<=m, the joint derivatives through m of the p_i generate R O everywhere on the affine chart. Equation (3) implies S_m=R-perp O there. The constant subbundle R-perp O lies in S and in every S_j, because derivatives of its sections remain in that same constant subbundle. Finally S_m/(R-perp O) is a subsheaf of the vector bundle (H*/R-perp)O; it vanishes on the dense affine chart, so it is torsion and torsion-free, hence zero. This proves (1) globally. For m=0 the same argument simply says E is the constant bundle R O and S=S_0=R-perp O.

This also explains why spanning is essential: without it, the exact stable remainder is R-perp O, not zero. Over positive characteristic the theorem as stated is not asserted; ordinary derivatives of p-th powers can vanish and the factorial inversion can fail.

## 5. Sharpness as a universal formal model

For m>=1 take the rational-normal line O(-m) in C^(m+1) O given on the affine chart by p(t)=(1,t,...,t^m). Its homogeneous coordinates are all degree-m monomials, so it is saturated and spans the entire constant space. Define the nonzero dual polynomial vector

    s_k(t)=binom(m,k)(-t)^(m-k),  0<=k<=m.

The identity sum_k s_k(t) z^k=(z-t)^m implies <s,D^a p>=0 for 0<=a<m, while <s,D^m p>=m!. Equation (3) gives a nonzero local section of S_(m-1), whereas S_m=0 by the theorem. Thus m cannot uniformly be replaced by m-1. This is an abstract universal sharpness model, not an actual HM coefficient or parameter choice.

## 6. Relation to the partial-apolar argument

PR1145 Section6 correctly allows a partial coefficient quotient q:Sym^n W->R for an embedded line O(-n). Its dual injection R*->(Sym^n W)* transports the actual annihilation condition into the full universal polynomial space; it does not assume q injective. The present proof is a direct generalization of that mechanism, avoiding any need to select a line or prove completeness.

For comparison, a nonzero line inside S_m has its first m derivatives in S, by the recursive kernel definition. The partial-apolar argument then makes the projection of E to R*, followed by the dual coefficient injection, factor through Sym^(n-m-1)W O(-m-1) if m<n; the annihilator is zero if m>=n. Since every degree of E is at least -m, the first target admits no nonzero map from E. The resulting constant R in S contradicts H0(S)=0. This is an alternative explanation; the proof of the theorem is already complete in Sections2-4 and does not import apolarity or coefficient-system completeness.

## 7. Application and exact limits

The original actual inclusion and its spanning property are pinned in inputs/actual-splitting.md. The four-source theorem in inputs/four-sources.md gives, for the D source,

    E=D O(-2)+(W'+T6)O(-3)+V O(-4)+O(-8).

Thus E(8) is globally generated, and the actual dual chain satisfies S_8=0. With the indexing F_0=S, F_1=L=S^- used in PR1145, every last nonzero F_h has h<=7. Equivalently there cannot be a nonzero eighth successive kernel. This statement is independent of a rank-three plateau or endpoint equality assumption.

This is a reusable necessary bound for residual D-source geometry. It does not exclude any of the current original-index records32,50,52, does not revise any frozen frontier count, and does not prove complete profile coverage. It is not a full-adjoint, smoothing, algebraicity, generic rank-four, or original proof-repair theorem. The four-source and actual-spanning inputs are imported written mathematical results; no proof-assistant verification is claimed.

## 8. Sources and reproducibility

INPUTS.json records complete immutable public URLs, commits, byte lengths, SHA256 values and Git blob IDs for the full original sources read before this proof. These include the actual splitting/spanning note, four-source theorem, strict-top/saturation conventions, and PR1145's partial-apolar proof. All four source bytes were freshly fetched and their Git blob identities checked.

The standard-library verifier authenticates these retained sources, checks exact formal Taylor inversion, the Leibniz signs, and the sharp rational-normal jet identities for every degree0 through16 (degree0 handled separately). It also verifies the D source's ranks, degree and bound. These are bounded regression tests of universal identities, not an experimental proof of arbitrary degree or a test of any actual HM instance. The all-degree argument is Sections2-4.
