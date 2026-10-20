# Full supported first jets need not be tangent to the support hyperplane

## Conclusion and exact scope

For an abstract fixed operation satisfying cyclic zero, outer symmetry, and global repeated-input injectivity, the complete first-order supported-family equations do not imply that middle velocities lie in the support hyperplane H. These equations include preservation of the ternary support, its metric kernel, and the actual supported correction of that fixed operation. This remains true when the metric has rank one, so they do not imply containment in the lifted radical three-plane P either.

More precisely, there exists a single fixed quotient of the universal cyclic, outer-symmetric operation on a five-dimensional V, with twenty-dimensional target J and repeated-input injectivity at every complex middle point, having a supported-ternary family over Spec C[t]/(t²) with middle velocity transverse to H. Its residual map has rank exactly five over the dual numbers. The metric can be chosen nondegenerate or of rank one. In either case its central compatible rank-two locus can be chosen to have dimension exactly two.

This is an abstract fixed-operation construction. It is not asserted to satisfy every additional equivariance or source-specific hypothesis of the original operation, and no source equivariance is proved. It therefore excludes deriving tangent containment from the listed structural hypotheses and complete first-order supported identities alone. This is a full supported infinitesimal family, stronger than a determinantal tangent countermodel. It is NOT a reduced middle surface, not an integrated curve, and not a counterexample to a possible theorem about tangent directions of a genuine surface. Such a theorem must use integrability beyond these first-order equations, or additional global hypotheses. In fact the prescribed constant-data continuation in this construction is obstructed already at order two.

## 1. Central data

Let V=Cu direct-sum E direct-sum Cz with dim E=3. Let h be a nonzero symmetric form on E, either nondegenerate or rank one, and K=ker(h:Sym²E→C). Choose v:K→E satisfying

    v(e²) not in Ce for every nonzero e with h(e,e)=0.       (1)

Such v exist for either metric rank: the projective square locus in P(K) has dimension one, and for each square the forbidden condition has codimension two in Hom(K,E). The closed bad incidence therefore has dimension at most fourteen in the fifteen-dimensional parameter space. Properness of the projective square locus makes its image closed.

One may additionally require that the compatible rank-two locus has dimension exactly two. Here is a justification that covers the rank-one case as well. The rank-two locus T in P(K) is a hypersurface of dimension three: the determinant does not vanish identically on K, and its rank-one locus has dimension one. For rank-one h, write h=l² and choose coordinates with l=e3*. The determinant on K is

    -a e² + 2b d e - c d²

for the symmetric matrix with rows (a,b,d), (b,c,e), (d,e,0). This polynomial is irreducible: over C[d,e], its coefficients as a linear polynomial in a,b,c have gcd one, and over C(d,e) it is an irreducible linear polynomial. Thus T is irreducible and has a nonempty smooth open of dimension three. For nondegenerate h, use the kernel-line incidence: over P(E*) let S_lambda=ker(lambda). The restriction h:Sym²S_lambda→C is never zero, since a nondegenerate ternary form has no totally isotropic two-plane. Its kernel is a rank-two bundle, whose projectivization is an irreducible smooth threefold. Its nonempty rank-two open maps isomorphically to the rank-two locus in P(K), since each such tensor has a unique kernel line. This proves the required irreducibility and smoothness. See AUDIT.md for the complete independent derivation.

On a smooth open of T, compatibility is one scalar equation lambda(q)(v(q))=0, where lambda annihilates im(q). Its universal incidence over Hom(K,E) has dimension seventeen. It dominates the parameter space: choose a nonzero projective tangent delta_q at q0, prescribe v(q0)=0 and lambda(q0)(v(delta_q)) nonzero, and differentiate the compatibility equation. Consequently a nonempty open of v has a nonempty two-dimensional compatible locus. Generic fiber dimension applied to the full irreducible rank-two locus gives dimension exactly two. This open intersects the square-avoidance open. No numerical tensor values are needed.

## 2. Universal tensors and the complete first derivative

Let

    W=ker(V tensor Λ²V → Λ³V),  dim W=40,
    f0(a,b,c)=a tensor (b wedge c)+c tensor (b wedge a),
    B_a(q)=f0(q,a),   A_a(b)=a tensor (a wedge b).

Use symmetric contraction matrices with B_u(e²)=2e tensor (u wedge e). Define

    L(q)=B_u(q)-A_u(v(q)).

Let g:V→V send u to z and annihilate E and z, and let D(q) be the derivative of the induced tensor action on L(q). Explicitly,

    D(q)=B_z(q)-z tensor (u wedge v(q))-u tensor (z wedge v(q)).

Set

    N={L(q0)+D(q1):q0,q1 in K}.

The E-first-factor components are

    2q0 in E tensor (u wedge E),
    2q1 in E tensor (z wedge E).

Thus dim N=10. Also N intersect F_u=L(K), where F_u=im B_u on Sym²V: every element of F_u has second factor in u wedge V, so its E tensor (z wedge E) component is zero, forcing q1=0.

## 3. N avoids every repeated-input tensor

In fact N contains no nonzero tensor of rank one in V tensor Λ²V. Suppose L(q0)+D(q1)=x tensor beta is nonzero and rank one. Its E-first-factor component cannot vanish, by the preceding displayed components. Write e for a nonzero representative of the E-component of x. Each symmetric q_i has image in Ce, hence

    q0=c0 e²,  q1=c1 e²,

with (c0,c1) nonzero. Since q_i belong to K, e is h-isotropic. Put w=v(e²); by (1), e,w are independent. Put s=c0u+c1z, which is nonzero. The E-first-factor component determines beta, up to nonzero scale, to be s wedge e. But the u-first-factor row of our tensor is exactly

    -s wedge w.

It cannot be proportional to s wedge e because s is outside E and e,w are independent. This contradicts tensor rank one.

In particular P(N) is disjoint from the closed repeated-input variety

    X={ [a tensor (a wedge b)] : a wedge b nonzero }, dim X=7.

## 4. A fixed twenty-dimensional target preserving all injections

In W/N, of dimension thirty, choose a ten-dimensional subspace M'. Impose two open conditions:

1. M' avoids the nine-dimensional image of F_u. This is possible since 10+9≤30.
2. P(M') avoids the projection of X. Since P(N) avoids X, this projection is a morphism from the projective X, with closed image of dimension at most seven. For a fixed image point, ten-planes containing it have dimension dim Gr(9,29)=180, whereas dim Gr(10,30)=200. The bad incidence has dimension at most 187 and has closed image, so its complement is nonempty open.

The two opens intersect. Let M be the inverse image of M', so dim M=20, and let f be f0 followed by W→J=W/M. Then every repeated map of f is injective, because P(M) avoids X. Also M intersect F_u=L(K), so the residual kernel at u is exactly K and rank Q_u=5. The actual correction is exactly v. The compatible-fiber conclusion of Section 1 therefore applies to this fixed operation.

## 5. Full dual-number family, rather than a determinantal tangent only

Work over A=C[t]/(t²). Put

    u_t=u+tz,   U_t=A u_t,
    H_t=A u_t direct-sum (E tensor A),
    h_t=h,   K_t=K tensor A,   v_t=v.

The actual universal identity is

    B_(u+tz)(q)-A_(u+tz)(v(q))
      =L(q)+tD(q)-t² A_z(v(q)).                           (2)

Modulo t² its right side belongs to M tensor A. Hence the *fixed* f satisfies

    f(q,u_t)=A_(u_t)(v(q)) for every q in K tensor A.

This is the full supported correction identity in the moving ternary support H_t/U_t, with fixed projective metric. The full middle-linear map has the direct rank-six kernel submodule generated by u_t² and q-u_t v(q), q in K. A nine-by-nine minor is a unit by its central rank, and the exhibited rank-six direct kernel bounds the rank by nine. Thus its rank is exactly nine over A; repeated-image rank is four and residual rank is exactly five. No merely set-theoretic rank assertion is used here.

The middle velocity is z modulo Cu, which is not in H_0/Cu=E. When h has rank one and R=rad h, the lifted radical is P_0=Cu+R, and the same velocity is also outside P_0/Cu.

## 6. Where integration first enters

Equation (2) gives the exact obstruction to continuing these *prescribed* constant E,h,v data with u_t=u+tz to order two. In the fixed quotient its t² coefficient is -A_z(v(q)). Square avoidance ensures v is not identically zero. For q with v(q) nonzero, v(q) belongs to E and is independent of z; global repeated injectivity therefore gives

    A_z(v(q)) nonzero in J.

So this prescribed family does not even extend to C[t]/(t³). Allowing second derivatives of u,H,h,v changes the second-order equations, and the argument does not rule out cancelling that obstruction by such changes. Nor does it prove that every supported first jet is obstructed.

Accordingly, the rigorous negative conclusion is only that a tangent-to-H or tangent-to-P theorem for genuine middle surfaces cannot be obtained from the complete first-order supported-family identities alone. Establishing or refuting such a theorem for integrated surfaces remains open here.

All arguments are abstract finite-dimensional tensor and incidence algebra.
