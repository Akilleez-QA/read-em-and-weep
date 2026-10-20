# Ten-axis interpolation and Dic3 rank-five coupling

## Result

Under the standing hypotheses of the rank-five finite-support theorem and the representation and pure/mixed models of `../quaternion-rank-five-coupling-constraint/PROOF.md`, a rank-five point on O250 forces the pure-T coefficient alpha to vanish and has parity ranks exactly (even,odd)=(5,4).

More strongly, if alpha is nonzero, the even rank at every order-three axis is eight and the odd rank is at least three, so total rank is at least eleven. Combined with the independently proved full-normalizer nonvanishing of alpha, this gives residual rank Q at least seven throughout O250, and in particular excludes it from Z5. That nonvanishing is a separate dependency, not assumed in the structural implication just stated.

The new ingredient is nonvanishing of a universal transverse harmonic-cubic coupling, proved by a coordinate harmonicity argument and independently by quadratic and quartic angular-momentum trace identities. No actual-operation coefficient or selected rank instance is evaluated.

## 1. No cubic contains the ten order-three axes

In the usual orthogonal icosahedral representation, the order-three axes are the antipodal pairs of dodecahedral vertices. Put phi=(1+sqrt(5))/2, a=1/phi, b=phi. Representatives are the four projective sign choices of (1,1,1) and the six projective sign choices of

    (0,a,b), (b,0,a), (a,b,0).

This is the standard dual-dodecahedron realization. The Galois-conjugate three-dimensional representation has the same image rotation group up to an automorphism, so the same statement applies to either labeled irreducible representation.

Write an arbitrary cubic as

    x(Ax^2+By^2+Cz^2) + y(Dy^2+Ez^2+Fx^2)
      + z(Gz^2+Hx^2+Iy^2) + Jxyz.

Its values on the four sign choices of (1,1,1) imply J=0 and A+B+C=D+E+F=G+H+I=0. The sign choices of the coordinate-zero vertices separate the remaining odd-coordinate terms. For the x terms they give

    A b^2 + C a^2=0,   A a^2 + B b^2=0.

Consequently A(1-a^2/b^2-b^2/a^2)=0. The parenthesis is nonzero (the sum of a positive number and its reciprocal is at least two). Hence A=B=C=0. Cyclically all remaining coefficients vanish. Thus I(O10)_3=0.

## 2. Odd rank at least three

The odd block at a middle argument u in T is a linear map T tensor W -> Jminus. If its rank were at most two at an order-three axis, its three-minors would vanish on all ten axes by K-equivariance. Section 1 would make all those cubic minors identically zero. This contradicts the established odd rank at least five on the canonical conic. Thus odd rank is at least three at every axis.

## 3. The mandatory mixed invariant direction

Recall the universal formulas, with q and the cross product on T:

    F3(v,u,w)=2q(v,w)u-q(u,v)w-q(u,w)v,
    F5(v,u,w)=v sym (u cross w)+w sym (u cross v).

The pure-T operation is alpha F3 plus beta F5, with beta nonzero by repeated-input injectivity on isotropic vectors. The mixed map g:Sym^2 W tensor T -> P5 is a nonzero scalar times the unique K projection. Its corresponding T' copy in Sym^3 T consists of trace-free cubics C_s, satisfying

    q(g(s,u)u,u)=C_s(u)

up to a fixed nonzero scalar. These facts and their proofs are imported from Sections 3–4 of the quaternion constraint.

If the left-hand side vanished for every s at one axis, every C_s would vanish on all ten axes, contradicting Section 1. Thus the mixed image has a nonzero uu entry at each axis. All pure F5 values have zero uu entry. This supplies a new even direction.

At nonisotropic u the pure F5 image has dimension four and consists of the entire uu-entry-zero hyperplane in P5. The pure map has rank four if alpha=0 and five if alpha is nonzero. Thus even rank is exactly five when alpha=0, and at least six otherwise.

## 4. Exact local representation alternatives

Let D=Dic3 stabilize Cu, and let epsilon be its character on Cu, trivial on the order-three subgroup and -1 on the order-four generator. Let rho be the irreducible two-dimensional representation factoring through S3. Then

    T|D = epsilon + rho,
    T'|D = epsilon + rho,
    P5|D = 1 + 2rho.

The equality for T' follows from the order-three spectrum and the order-four trace -1, exactly as for T. These decompositions also follow by forming Sym^2 T and removing its invariant metric.

For alpha nonzero, the pure image has D-types epsilon + 2rho. Its intersection with P5 is one rho: it is the image under F5 of the transverse trace-free quadratics in Sym^2(u-perp). Indeed the pure F3 vanishes exactly on Cu^2 plus those two transverse trace-free directions. In orthonormal coordinates u=e1, their F5 images are the 23 entry and diagonal difference 22-33. Denote this two-space by L_u.

The mixed source at u is epsilon tensor T'=1+rho. Its trivial constituent adds the mandatory new direction of Section 3. Its rho constituent either lies entirely in L_u, or contributes two new directions modulo the pure image, by irreducibility of rho. Consequently for alpha nonzero the even rank is exactly six or eight, never seven.

Equivalently define the transverse mixed coupling

    gamma_u : (T')_rho -> u-perp,
    s |-> projection_(u-perp)(g(s,u)u).

Both its source and target carry rho after accounting for the evaluation twist; its zero/nonzero status is intrinsic. Its kernel is either all or zero, and gamma_u=0 precisely when the mixed rho image is contained in L_u. Therefore even rank is six if gamma_u=0 and eight otherwise. The statement is independent of scaling u, q, or the unique mixed projection. Equivariance makes its status the same at all ten axes.

Combining odd rank at least three with total rank nine gives the provisional alpha-nonzero alternative: even eight is impossible, so even six and odd three, and gamma_u=0. If alpha=0, even rank is five, giving the alpha-zero alternative.

## 5. A further odd-image constraint

Let E denote the unique two-dimensional irreducible D-module with nontrivial order-three action and negative central action, and let eta_plus, eta_minus be the one-dimensional characters with order-four eigenvalues i,-i. The odd source, including the evaluation twist, has types

    2E + eta_plus + eta_minus.

Repeated-input injectivity embeds the E module u tensor W through w -> f(u,u,w), so the odd image contains E. Thus odd rank three in the provisional alpha-nonzero alternative means its image has exactly E plus one of eta_plus or eta_minus. Exactly one of the two character columns must vanish; the E-isotypic source has image of rank two. This is another necessary condition, not a claim that either character column is universally nonzero.

## 6. The transverse coupling is universally nonzero

### 6.1. Short harmonicity proof

Use the coordinates of Section 1 and the order-three axis u=(1,1,1). The rotation group contains the Klein four subgroup acting by even coordinate sign changes. The harmonic-cubic T' subspace restricts to its three nontrivial characters, each once. A nonzero cubic in its x-character line therefore has the form

    C_x=x(Ax^2+By^2+Cz^2).

There are no other monomials of degree three with this character. Harmonicity gives

    3A+B+C=0.

If gamma_u were zero, every cubic in T' would have vanishing transverse derivative at u. Indeed this holds on the nontrivial order-three eigenspaces by the derivative interpretation of gamma; on the invariant line it holds because the tangent plane has no order-three-invariant direction. Full symmetry of the cubic tensor supplies that interpretation:

    dC_s(u)[v] = 3 q(g(s,u)u,v),

up to one fixed nonzero normalization.

Consequently the gradient of C_x at u must be parallel to u. But

    grad C_x(1,1,1)=(3A+B+C,2B,2C)=(0,2B,2C).

A vector of this form can be parallel to (1,1,1) only if B=C=0. Harmonicity then gives A=0, contrary to the chosen nonzero cubic. Thus gamma_u is nonzero. Equivariance proves the same at all ten axes.

This calculation concerns only the universal harmonic-cubic representation, not the actual operation or a rank instance.

### 6.2. Independent angular-momentum trace proof

We now remove the provisional alpha-nonzero alternative of Section 4 without using any actual-operation information. Work in the real orthogonal icosahedral realization and complexify when convenient. The seven-dimensional space H3 of harmonic homogeneous cubics is the irreducible degree-three SO3 representation. Its A5 decomposition is T' plus P4: indeed Sym^3 T=T plus T' plus P4, and contraction removes the qT summand. Give H3 its rotation-invariant positive inner product, and let P be the orthogonal projector onto its unique T' summand. This projector commutes with A5.

For a real vector v, let L_v be i times the infinitesimal rotation generator about v, acting on H3; the sign convention for i does not affect its even powers. For unit v its eigenvalues are the integers -3,-2,-1,0,1,2,3. The functions

    tr(P L_v^2),  tr(P L_v^4)

are A5-invariant homogeneous polynomials of degrees two and four in v. There are no such invariants beyond multiples of q and q^2, as proved in Section 1 of `../order-four-rank-five-exclusion/PROOF.md`; equivalently Sym^2 T=1 plus P5 and Sym^4 T=1 plus P4 plus 2P5 each have exactly one invariant line. Consequently both functions are constant on the unit sphere. Averaging over SO3, irreducibility of H3 gives the averaged conjugate of L_v^k as (tr(L_v^k)/7) times the identity. Since tr(P)=3, the constants are

    tr(P L_v^2) = (3/7) times 2(1+4+9) = 12,
    tr(P L_v^4) = (3/7) times 2(1+16+81) = 84.

Fix a real unit order-three axis u. Relative to rotations about u, write H3 as the direct sum of its weight spaces m=-3,...,3. Its order-three-invariant sector comprises m=0,+3,-3. Its other two order-three eigenspaces comprise respectively m=1,-2 and m=-1,2. Each constituent of T' occurs once under the order-three subgroup: one invariant line and one line in each of these other sectors.

The differential at u, in directions perpendicular to u, of a harmonic cubic kills the m=0,±2,±3 components and is nonzero on each m=±1 component. This follows immediately from the azimuthal factor and order of vanishing at the pole, or from the standard solid harmonics: m=±1 has a nonzero transverse linear term times the square of the axial coordinate, whereas |m|>=2 vanishes to order at least two in transverse coordinates. The m=0 component has zero transverse derivative by axial invariance.

Full symmetry of the cubic tensor gives

    dC_s(u)[v] = 3 q(g(s,u)u,v)

up to the fixed common nonzero normalization. Thus if gamma_u=0, the two non-invariant lines of T' have no m=±1 component. They must be exactly the m=±2 lines. Their contributions to tr(P L_u^2) and tr(P L_u^4) are therefore eight and thirty-two.

The remaining invariant line of T' lies in m=0,±3. Let its contribution to tr(P L_u^2) be r. The trace identity makes r=12-8=4. On the whole m=0,±3 sector one has L_u^4=9 L_u^2, so this line contributes 9r=36 to the fourth-power trace. It follows that

    tr(P L_u^4)=32+36=68,

contradicting its already proved value84. Hence gamma_u is nonzero.

This is a universal representation calculation. It uses neither the normalization nor any coefficient of the actual mixed operation; the nonzero mixed scalar established by repeated-input injectivity cannot change its conclusion.

## 7. Conclusion, dependencies, and remaining scope

If alpha is nonzero, Section 4 and gamma_u nonzero give even rank eight; Section 2 gives odd rank at least three. Hence total rank is at least eleven, in particular not nine. A rank-five point on O250 must therefore have alpha=0, and then Section 3 gives even rank five and total rank nine gives odd rank four.

If the independently established and separately audited full-normalizer theorem in `../../rank-four/full-normalizer-pure-t-nonvanishing/PROOF.md` is imported, alpha is nonzero. Hence throughout O250 the even rank is exactly eight, the odd rank is at least three, and rank Q = rank b - 4 is at least seven. In particular O250 is excluded from Z5. Combined with the corresponding quaternion theorem, this removes O250, O375, and their union from the already bounded support list, leaving only the empty support and the distinguished 600-point orbit M. The status of M is outside this proof.

Audit should check the real harmonic-cubic projector argument, the normalization-independent derivative interpretation, and the absence of quadratic/quartic invariants beyond q and q^2. Section 5 records the local odd-rank-three alternative before Section 6 removes it; it is not a surviving possibility.

Only local proof files were written. No actual-operation coefficients, selected-input rank instances, source tensors, jets, residues, external state, or large computations were used.
