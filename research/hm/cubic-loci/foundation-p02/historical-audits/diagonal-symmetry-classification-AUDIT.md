# Historical scope-limited review receipt

This review concerns the original source, possibly a larger scope than the excerpt in this unit. It is not a review of normalized publication bytes.

# Independent audit of diagonal symmetries

Audited proof: [PROOF.md](../DIAGONAL.md). Its final SHA-256, independently verified with sha256sum, is `4654f99b6698f24ab963da2a7551021a88052144cd72bf9218e2da2d8be68c7b`.

Literal-table and structural references: first-differential proof (see dependency map: cm rank free, PROOF.md), and [independent presentation proof, Section 3](../../../hm-presentation-independent/PROOF.md). The full extension and coefficient-parameter conclusions were audited against the final proof above. The final proof uses the precise quotient-morphism wording noted below.

This audit uses the literal homogeneous coefficient tables for gamma, delta, and ev, together with the previously established exact-presentation and strict-lifting premises. All identities below are formal coefficient identities; no polynomial instance, matrix-product evaluation, rank, point, jet, residual, or detector computation is used.

## 1. First differential

Indices lie in Z/5. Let S=diag(s_0,...,s_4), with all s_j nonzero. The disjoint support argument for the literal gamma table forces both constant blocks in

    M gamma(v) = gamma(Sv) N

to be diagonal. Writing their entries m_r and n_j gives

    m_(U_i)=s_(i+1)n_(i+2)=s_(i+4)n_(i+3),
    m_(V_i)=s_(i+3)n_(i+1)=s_(i+2)n_(i+4),
    m_(Z_i)=s_i n_i.

The U relations propagate n_j from n_0 by

    n_(j+1)=(s_(j-1)/s_(j+2))n_j.

The cyclic product of these ratios is one. Thus either every n_j is zero, or every n_j is nonzero. Substitution into the V relations gives precisely

    s_j s_(j+1)^2 = s_(j+2)^2 s_(j+3)    for all j.

Consequently the intertwiner space is zero off this locus and one-dimensional on it.

Normalize s_0=1 and write a=s_1, b=s_2. The first two equations give

    s_3=a^2/b^2,    s_4=b^6/a^3.

The other three give

    a^10=b^15,    b^10=a^5,    b^5=a^5.

The latter two imply a^5=b^5=1, and these suffice for all the equations. This is reversible elimination in Laurent coordinate rings, so proves the scheme-theoretic statement, not merely a classification of geometric points.

Equivalently the full locus is

    s_j=c alpha^j beta^(j^2),    alpha^5=beta^5=1,

with inverse c=s_0, a=s_1/s_0, b=s_2/s_0,

    alpha=a^2/b^3,    beta=b^3/a.

Hence the full group scheme is G_m times mu_5 squared, and its quotient by scalar matrices is mu_5 squared. In characteristic zero this quotient is finite etale of degree 25. It need not be constant over the ground field; its rational points are mu_5(k) squared.

## 2. Explicit extension through the complete presentation

Put u_i=alpha^i beta^(i^2), so s_i=c u_i. For any scalar t, the first two blocks are

    N_ii=t u_i^2,
    M_(U_i)=ct beta^4 u_i^3,
    M_(V_i)=ct beta u_i^3,
    M_(Z_i)=ct u_i^3.

These formulas satisfy every gamma coefficient: the two U exponents reduce to alpha^(3i) beta^(3i^2+4), the two V exponents to alpha^(3i) beta^(3i^2+1), and the Z exponent to alpha^(3i) beta^(3i^2).

In the plus/minus ordering of the ten rows of delta, define diagonal blocks

    A_(+,l)=c^2 t beta^2/u_l,
    A_(-,l)=c^2 t beta^3/u_l,
    B=c^3 t diag(beta^2,beta^3).

The literal next differential is

    delta(U_i)=(D_(i+2,i+3),0),
    delta(V_i)=(0,D_(i+1,i+4)),
    delta(Z_i)=(D_(i+1,i+4),D_(i+2,i+3)),
    D_(a,b)=v_a e_b^* - v_b e_a^*.

The needed identities are

    u_i^3 u_(i+2) u_(i+3)=beta^3,
    u_i^3 u_(i+1) u_(i+4)=beta^2.

Indeed their alpha exponents are 5i+5, and their beta exponents respectively 5i^2+10i+13 and 5i^2+10i+17. Reducing modulo five proves both identities, independently of the representatives chosen for cyclic indices.

For a D_(a,b) in the plus or minus copy, with associated scalar weight q=beta^2 or beta^3, the coefficient at row b in A delta is c^2 t q v_a/u_b, while that in delta(Sv)M is c u_a v_a m. The row-a coefficients give the same scalar equality with their common minus sign. Thus the condition is simply

    q = u_a u_b (m/(ct)).

For U, this is beta^2=beta^4 beta^3. For V it is beta^3=beta beta^2. For the plus and minus portions of Z, respectively, it is beta^2=beta^2 and beta^3=beta^3. These verify every coefficient of

    A delta(v) = delta(Sv) M.

Finally ev is evaluation (v_0,...,v_4) separately in the two blocks. In either block, its coefficient in ev(Sv)A is

    (c u_l v_l)(c^2 t q/u_l)=c^3 t q v_l,

which is exactly the coefficient in B ev(v). Hence

    B ev(v)=ev(Sv) A.

For t nonzero, N, M, A, and B are all invertible. They therefore give an isomorphism of the complete complexes, inducing an isomorphism of their sole cohomology bundles.

## 3. Bundle conclusion and its premises

The first-differential calculation alone would give only a necessary condition for bundle symmetry. Section 2 supplies the missing sufficiency by constructing the complete chain isomorphism.

Assuming the established exact presentation with sole cohomology H, and its degree-gap identification of bundle maps with strict constant-block chain maps, the conclusions are

    Hom(H,S*H) is one-dimensional on the diagonal locus,
    Hom(H,S*H)=0 off the locus.

For the dimension upper bound, every strict map has first two blocks proportional to the displayed pair. Subtract the same multiple of the constructed full chain map. Its degree-zero block M is then zero, so its induced map on degree-zero cohomology is zero. The constructed isomorphism gives the dimension lower bound. Thus the diagonal projective stabilizer of this bundle is exactly mu_5 squared, with every nonzero Hom on the locus an isomorphism.

The proof does not separately establish the exactness or identity of the presentation with the intended HM bundle; it uses those previously established structural premises. It establishes no scalar-detector response or other covariance beyond these bundle and chain-map statements.

## 4. Audit of the coefficient-parameter consequence

On an invariant independent-generating open U in P(W^5), the mu_5 squared action is free. At a geometric point, if (s_i f_i) is a common scalar multiple lambda(f_i), then every f_i is nonzero, so s_i=lambda for all i. The projective diagonal element is therefore the identity. Since the acting group scheme is finite etale in characteristic zero, absence of nontrivial geometric stabilizers also rules out infinitesimal stabilizers, giving scheme-theoretic freeness.

The quotient of this quasi-projective open by the finite group scheme exists, and the quotient morphism U to U/(mu_5 squared) is a torsor under that finite etale group scheme. In particular the morphism is finite etale of degree 25. Over an algebraically closed field every orbit has 25 distinct points.

Scaling the tuple changes its associated morphism f:T to P^4 to S composed with f. The constructed isomorphism S*H isomorphic to H pulls back along f, so every orbit gives isomorphic pullback bundles. This establishes only this finite family of identifications, not that all isomorphic pullbacks lie in one such orbit.

For dim W=16 the ambient projective parameter space has dimension 5 times 16 minus 1, namely 79. The assertion applies to an invariant open where independence and generation hold. For entirely arbitrary T, openness of the generating locus is an additional issue; it is safe to retain that conditional formulation (and standard properness hypotheses supply openness). Also, it is the quotient morphism that is finite etale, not the quotient scheme by itself over k.
