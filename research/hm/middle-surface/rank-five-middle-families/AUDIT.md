# Independent audit: canonical rank-five complement and boundary

## Verdict

PASS, with the scope stated in PROOF.md. The construction yields a canonical complement on the nondegenerate supported-ternary surface-fiber stratum and a positive top-Chern obstruction to extending it transversely over a complete middle surface. It does not exclude an open two-dimensional good family or a seven-dimensional affine component with boundary. The necessary boundary is more precisely a residual-rank-at-most-four point or a rank-five point with degenerate ternary form.

Reviewed PROOF.md in full, together with the pointwise construction in /research/hm/universal-polar/rank-five-surface-countermodel/PROOF.md and both the irreducible and complete reducible supported-ternary theorems in /research/hm/normalizer-rank-five/rank-six-cubic-web/.

## 1. Correction and canonical lift

The outside-support argument correctly uses the theorem for arbitrary four-dimensional ternary tensor spaces, not an unjustified application only to genuine residual kernels. If the quotient correction is nonzero, its kernel has dimension four and contains every compatible rank-two point. The no-compatible-square property survives restriction. REDUCIBLE.md supplies the required bound even for reducible or nonreduced determinant cubics.

With ab=(a tensor b+b tensor a)/2, changing s to s+u d gives v' = v+2(q -> q(d)). The factor two is essential and is retained correctly.

Independently, extend v from K to Sym²(E0) using the trace-free projection

    P_h(q)=q-h(q)h^{-1}/3.

Contract the output of v composed with P_h against one covariant input. For i(c):q -> q(c), this contraction is (5/3)c. In h-orthonormal coordinates its tensor coefficients are

    i(c)_{a,bc}=(delta_ab c_c+delta_ac c_b)/2-delta_bc c_a/3,

and summing i(c)_{a,ab} over a gives (5/3)c_b. This independently verifies tau_h(i(c))=(5/3)c and tau_h(2i(d))=(10/3)d. It agrees with the invariant trace-pairing derivation in the proof.

Consequently the corrected lift s-(3/10)u tau_h(v) has exactly the right sign and scale. Its image is a complement because projection back to E0 is the identity. A further shear preserves the normalization only if its restricted covector vanishes. Middle-vector scaling cancels between u and v. Rescaling h leaves P_h unchanged, independently confirming conformal invariance. No choice of Hermitian structure or complex conjugation enters.

Formation of kernels and support spaces is regular on the relevant constant-rank strata. The invariant contraction is regular where h is nondegenerate. Thus the construction gives a genuine algebraic Grassmannian map, not merely a pointwise choice.

## 2. Complete-surface obstruction

On a smooth projective surface resolving the graph, the limiting rank-three tautological C remains a subbundle of the trivial V-bundle. Hence R=V/C is a globally generated rank-two vector bundle. The middle line U gives a global section of R tensor U*, vanishing precisely where U is contained in C.

The formula

    c2(R tensor U*)=c2(R)+h c1(R)+h²

has the correct positive signs, with h=c1(U*). Global generation gives nonnegative c2(R) degree and nef c1(R); h is nef and big. A general section of R has either an empty or zero-dimensional zero scheme, which justifies the c2 assertion without an assumption on the particular middle-induced section. On the birational graph resolution, h²=degree(B)>0. On a generically finite parameter surface, this becomes the generic degree times the degree of its image.

A nowhere-zero section would make the top Chern class vanish, contrary to these inequalities. When the actual zero scheme is zero-dimensional, smoothness of the surface and codimension two make the section regular, so its scheme length is the displayed Chern number. When there is a divisorial zero component, no naive zero-count interpretation is justified or claimed.

## 3. Localization of the boundary

The rank-at-most-five locus is closed. On its rank-five part, support of dimension at most three is a closed condition by the proper incidence with the relative Grassmannian. A five-dimensional symmetric tensor space cannot have support dimension at most two. Thus support remains exactly three at every rank-five specialization on B, and full four-dimensional support is indeed excluded as an alternative boundary.

The proof's dependent-triple claim follows from the global repeated-input hypothesis. In particular, if x,z are independent then A_x(z), A_z(x) are nonzero and independent: proportionality would give a t with

    A_(x+t z)(z)=A_x(z)-t A_z(x)=0,

contradicting injectivity at x+t z. The cyclic identity yields the displayed formula. Consequently a dependent zero triple has all three projective lines equal. Its locus in each middle fiber is a single point.

Proper upper semicontinuity for the full zero incidence therefore ensures that the independent fiber retains dimension at least two at every specialization in B. At rank five with nondegenerate h all good-point hypotheses hold, so the canonical map is regular there. The graph cannot acquire a different limiting value over such a point. Its section zeros consequently lie over rank at most four or degenerate h, exactly as claimed.

## 4. Fiber dimension and curve check

Section 8's restriction argument is valid. The trace-free ternary rank-two locus is the dense open of an irreducible cubic threefold in P(K). If compatibility were dense there, closedness on the rank-two open would give compatibility everywhere on that open. A general projective three-plane section has a two-dimensional determinant locus with a dense rank-two part: the ambient rank-one locus is only a curve. Its four-dimensional vector space K' would therefore violate the complete ternary-web theorem. Hence compatible dimension is at most two, and a good fiber has dimension exactly two.

Minor wording precision communicated to the author and now corrected: the rank-two locus is the dense open of the cubic threefold, rather than the entire projective cubic threefold. This does not affect the argument.

For a complete good curve, H=U direct-sum C gives deg(V/H)=deg(U*)+deg(det C*). The bundle C* is globally generated as a quotient of V*, so its determinant has nonnegative degree. The curve inequality and the exclusion of a constant support hyperplane for a nonconstant middle curve follow. This does not exclude varying-hyperplane complete curves.

The subsequently added Section 9 also passes. The conformal form gives C isomorphic to C* tensor M, and therefore -2a=3deg(M). This correctly proves that a is divisible by three. If a=0, the ample Plücker bundle forces the Grassmannian map to be constant. The nondegenerate form classes on that constant C lie in the affine principal open defined by the determinant in projective space. A map from a complete integral curve into that affine variety is constant, so K is fixed as well. The correction transforms as v_(t u)=t^{-1}v_u; thus v_u tensor u is a global section of the constant Hom(K,C) tensored with the negative-degree line U. It must vanish. The resulting v=0 is forbidden because the nondegenerate ternary form has isotropic vectors over C, hence K contains squares. This proves a>=3 and the sharpened inequality deg(H-map)>=deg(middle-map)+3. It does not exclude all nonconstant complete good curves.

## Operational and logical scope

  

The final frontier remains unchanged: this is a forced-boundary theorem and a numerical defect class, not a global affine dimension-six theorem or an existence theorem for positive-dimensional middle families.
