# Complete diagonal symmetry locus for the literal HM bundle

## Result and exact scope

Let k be a characteristic-zero field, and use the homogeneous cyclic differential γ from the exact-presentation foundation and the explicit table below. For s_i in k^×, let S(v_i)=s_i v_i. There exist constant matrices M (15 by 15), N (5 by 5), not both zero, satisfying

    M γ(v) = γ(Sv) N

if and only if, cyclically modulo five,

    s_j s_(j+1)^2 = s_(j+2)^2 s_(j+3).                 (1)

Modulo the common scalar s_0, the complete solution locus is μ_5 × μ_5. Explicitly, with a=s_1/s_0 and b=s_2/s_0, it is

    (s_0,...,s_4) = c (1,a,b,a²b³,a²b),
    c in k^×, a⁵=b⁵=1.                              (2)

Equivalently it is

    s_i = c α^i β^(i²),   α⁵=β⁵=1.                  (3)

For each such S, the vector space of pairs (M,N) satisfying the first equation is exactly one-dimensional. Every nonzero pair consists of invertible matrices. Outside this locus it is zero.

The first-differential condition alone is only necessary for bundle symmetry. Section 6 independently extends every such pair through the other two literal differentials. Consequently this same μ_5² is exactly the diagonal projective symmetry locus of the HM bundle, and Hom(H,S*H) is one-dimensional on this locus and zero outside it.

## 1. Support forces both matrices diagonal

The nonzero entries of γ are, with cyclic indices,

    γ_(U_i,i+2)=v_(i+1),  γ_(U_i,i+3)=v_(i+4),
    γ_(V_i,i+1)=−v_(i+3), γ_(V_i,i+4)=−v_(i+2),
    γ_(Z_i,i)=v_i.

Here U_i=i, V_i=5+i, Z_i=10+i. Every ordered pair (column, variable label) belongs to exactly one row. Every two-entry row has distinct columns and labels, and if one column equals i, the label in its other column differs from i.

The right side in row Z_i has only variable v_i. Every two-entry row t of γ has an entry whose column and variable label both differ from i: if neither column is i, use distinct labels; if a column is i, use the other entry. Its coefficient forces M_(Z_i,t)=0. The pairs (j,j), j≠i, force M_(Z_i,Z_j)=0. Thus row Z_i of Mγ has only column i. Comparing its other columns with s_i v_i N_ij and using s_i≠0 gives N_ij=0 for j≠i.

Now N is diagonal and the right side in row r is supported inside the support of row r of γ. All other rows have disjoint supports in (column,label) pairs. Comparing such a pair forces M_rt=0 whenever t≠r. Hence M is diagonal as well.

Put n_j=N_jj. The remaining equations are precisely

    m_(U_i)=s_(i+1)n_(i+2)=s_(i+4)n_(i+3),
    m_(V_i)=s_(i+3)n_(i+1)=s_(i+2)n_(i+4),
    m_(Z_i)=s_i n_i.                                (4)

## 2. Eliminate N without a rank calculation

The U equations give

    n_(j+1) = [s_(j−1)/s_(j+2)] n_j.                 (5)

All factors are nonzero, so either all n_j vanish or none do. The product of the five factors is one; consequently (5), alone, has a one-dimensional solution space for every invertible S. A nonzero pair cannot have N=0, by (4).

Multiplying three consecutive instances of (5), and cancelling s_(j−1)=s_(j+4), gives

    n_(j+3)/n_j = s_j s_(j+1)/(s_(j+2)s_(j+3)).

The V equation with i=j−1 requires this same ratio to equal s_(j+2)/s_(j+1). Equating the ratios gives exactly (1). Conversely (1) makes every V equation follow from (5). This proves necessity and sufficiency, and proves the intertwiner space is one-dimensional whenever nonzero.

Every n_j is then nonzero; equation (4) makes every diagonal entry of M nonzero too. Thus both matrices are invertible. This conclusion required no invertibility assumption on M or N.

## 3. Solve the entire multiplicative locus

Normalize s_0=1, and write a=s_1, b=s_2, d=s_3, e=s_4. The five equations (1) become

    a²=b²d,
    ab²=d²e,
    bd²=e²,
    de²=a,
    e=a²b.                                         (6)

The last and fourth give e=a²b and d=a^(−3)b^(−2). The first then gives a⁵=1. The third gives a¹⁰b⁵=1, hence b⁵=1. Conversely, these two fifth-root relations and d=a²b³, e=a²b satisfy all five equations, including the second, whose reduced form is a⁵b⁵=1.

All these steps are identities in Laurent coordinate rings, so they establish the scheme-theoretic locus, not just a list of geometric points. The projective diagonal locus is isomorphic as a group scheme to μ_5²; before quotienting common scalars it is G_m × μ_5². Characteristic zero makes it reduced. Over an algebraically closed field it has exactly 25 projective points. Over a general field only its k-rational roots of unity contribute rational transformations; over Q, for example, only the identity survives projectively.

To pass between (2) and (3), set a=αβ and b=α²β⁴. Then b/a²=β², so the inverse formulas are

    β=(b/a²)³,   α=a/β.

The exponent 3 is the inverse of 2 modulo five. This proves the two parameterizations agree over k, without choosing a primitive fifth root.

## 4. Explicit full first-equation intertwiner

For (3), all solutions are scalar multiples, with scalar t in k, of

    n_i = t α^(2i) β^(2i²),
    m_(U_i) = ct α^(3i) β^(3i²+4),
    m_(V_i) = ct α^(3i) β^(3i²+1),
    m_(Z_i) = ct α^(3i) β^(3i²).

All exponents may be reduced modulo five. These formulas follow directly from (4) and (5). Since α⁵=β⁵=1, they are independent of the chosen integer representative of a cyclic index. They are formal formulas, not evaluated polynomial or matrix instances.

## 5. Comparison with diagonal Heisenberg transformations

Over a field containing a primitive fifth root ζ, define D=diag(ζ^i) and Q=diag(ζ^(i²)), for i=0,...,4. The locus is exactly the projective subgroup generated by D and Q. The usual cyclic Heisenberg diagonal subgroup generated by D is the five-point sublocus β=1. It is therefore a proper subgroup of the first-equation locus.

This comparison can be checked directly in the abstract coordinate representation. Let P e_i=e_(i+1). Then DP=ζ PD. The group generated by P, D and scalar ζ is the standard order-125 Heisenberg representation. Its diagonal elements are scalar multiples of powers of D. Moreover,

    Q D Q^(−1)=D,
    Q P Q^(−1)=ζ P D².

Thus Q normalizes that Heisenberg representation, explaining why the larger locus is compatible with a Heisenberg-normalizer interpretation. These group identities alone would not prove extension through the bundle presentation. That extension is established directly in Section 6. No assertion about the full, possibly nondiagonal, classical HM symmetry group is needed here.

## 6. Independently verify the full-chain extension

The exact presentation in [exact-presentation proof](../../hm-presentation-independent/PROOF.md), §3, supplies the remaining literal tables. Set D_ab=v_a e_b*−v_b e_a*. Then

    δ(U_i)=(D_(i+2,i+3),0),
    δ(V_i)=(0,D_(i+1,i+4)),
    δ(Z_i)=(D_(i+1,i+4),D_(i+2,i+3)).

The final map ev consists of the two evaluation rows (v_0,...,v_4), one on each block. This presentation has sole cohomology H in degree zero.

Write u_i=α^i β^(i²), so s_i=c u_i, and take the N,M of Section 4. Define the degree-one block A and degree-two block B by

    A_(+,l)=c²t β²/u_l,    A_(−,l)=c²t β³/u_l,
    B= c³t diag(β²,β³),

where A is diagonal in the two ordered five-dimensional blocks. We claim these satisfy

    Aδ(v)=δ(Sv)M,       B ev(v)=ev(Sv)A.              (7)

This is a separate coefficient proof, rather than an inference from the first equation. The only exponent identities needed are

    u_i³ u_(i+2) u_(i+3)=β³,
    u_i³ u_(i+1) u_(i+4)=β².                        (8)

For the first identity the α exponent is 5i+5 and the β exponent is 5i²+10i+13. For the second these exponents are 5i+5 and 5i²+10i+17. Reduction modulo five proves (8), including wrapped indices.

For a column whose relevant δ block is D_ab and whose M entry is ct λ u_i³, comparison of its e_b* coefficient in the first equation of (7) requires

    κ/u_b = λ u_i³ u_a,

where κ is β² in the plus block and β³ in the minus block. The e_a* coefficient requires the same identity with a,b reversed, with matching minus sign. Thus both coefficients are equivalent to

    κ = λ u_i³ u_a u_b.

For U, (λ,κ)=(β⁴,β²), and the first identity of (8) gives β⁴β³=β². For V, (λ,κ)=(β,β³), and the second identity gives ββ²=β³. For Z, λ=1: its plus component uses the second identity, and its minus component the first. This exhausts every δ coefficient.

Finally, on block ± and label l, ev(Sv)A has coefficient

    c u_l · c²t κ/u_l = c³t κ,

exactly the corresponding coefficient of B ev(v). This proves the second equation of (7). For t≠0 all four blocks N,M,A,B are invertible, so this is an isomorphism of complexes and induces H ≅ S*H.

## 7. Necessity and the complete bundle statement

On P⁴ the Hom complex between the two four-term presentations has terms that are sums of O(r), −3≤r≤3. All its higher cohomology vanishes, and its negative-degree terms have no global sections. The degree-gap argument therefore identifies Hom(H,S*H) with global strict degree-zero chain maps, whose blocks are constant.

Hence every bundle morphism supplies an initial pair classified in Sections 1–4. The map from bundle morphisms to initial pairs is injective: a chain map with M=0 induces the zero morphism on degree-zero cohomology. Consequently the dimension is at most one, and outside μ_5² it is zero. Section 6 supplies a nonzero invertible map at every point inside μ_5². Therefore

    Hom(H,S*H) = 0                       outside μ_5²,
    dim_k Hom(H,S*H) = 1                 on μ_5²,

and on the locus every nonzero bundle map is an isomorphism, being a nonzero scalar multiple of the constructed one. In particular μ_5² is exactly the diagonal projective stabilizer of the isomorphism class of H. This does not claim to classify nondiagonal symmetries.

The distinction between the stages matters: Sections 1–4 classify only a necessary initial chain equation; the independent coefficient identities of Section 6 are what make that condition sufficient for this particular full bundle.

No lift of an arbitrary S to the elliptic carrier X has been assumed. No statement is made about selector/HPL covariance, detector values, or final scalar responses.

## 8. Finite ambiguity after substitution into a generating five-tuple

Let W be a fixed k-vector space of sections on a scheme T, and consider ordered linearly independent five-tuples (f_0,...,f_4) in W that generate a line bundle, modulo common scalar. They determine morphisms f:T→P⁴. The projective μ_5² action scales the five sections by the corresponding s_i. It acts freely: if the scaled tuple is a common scalar multiple of the original tuple, every nonzero f_i forces its s_i to equal that common scalar, giving the identity in the projective diagonal group.

All tuples in such an orbit give isomorphic pullback bundles, because the transformed morphism is S∘f and Section 6 gives S*H≅H. Over an algebraically closed characteristic-zero field, each orbit therefore contains 25 distinct projective coefficient presentations with isomorphic pullback bundles. On any invariant open subscheme of the projective coefficient parameter space where these hypotheses hold, the quotient morphism for this free finite étale group action is finite étale of degree 25. This applies in particular when dim W=16, so that the full ordered coefficient space is P(W^5)=P^79, restricted to its independent generating locus.

This gives a finite source of global nonuniqueness. It neither contradicts local versality statements nor asserts these are all identifications between coefficient presentations.

