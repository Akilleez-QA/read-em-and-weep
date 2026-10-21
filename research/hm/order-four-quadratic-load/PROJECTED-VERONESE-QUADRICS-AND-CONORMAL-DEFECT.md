# The exact quadratic net and its reducible complete-intersection threefold

## Theorem

Let T be the actual degree-nine embedded plane in P6 supplied by DEGREE-NINE-PROJECTED-VERONESE-SURFACE.md. Its linear system on R=P(V) is

    L=q0 V* directsum G,     G=H0(I_Z6(3))=4,

where q0 is the invariant conic, Z6 is the six-point axis orbit, and A is the other irreducible A5 three-space. Then:

1. The quadratic equations of T form exactly the irreducible three-space A, and H1(I_T(2)) is exactly V.
2. These three quadrics are bilinear between the V and G coordinate blocks. Their matrix is the full Hilbert-Burch matrix of the six-point ideal. They have no linear syzygies as equations in P6 and form a regular sequence.
3. Their common zero scheme X is reduced of degree eight, with precisely two irreducible components: the coordinate P3 on which the V-block vanishes, and a residual irreducible degree-seven threefold Y. The plane T lies in Y.
4. The conormal differential of the quadratic net has rank-drop support exactly

       (q0=0) union Z6 subset R.

   Equivalently, this is the support of the singular scheme of X restricted to T. In particular the degeneracy is positive-dimensional. The Chern number 24 computed below is not the length of an actual finite scheme.

No generic-rank assumption or selected HM coefficient evaluation is used.

## 1. The forced quadratic net

The representation decompositions are

    Sym^2 L = 2(1) directsum A directsum 2(4) directsum 3(5),
    H0(R,O(6)) = 2(1) directsum V directsum 2(4) directsum 3(5).

For the classes of orders 1,2,3,5,5 their characters are respectively

    (28,4,1,phi',phi),     (28,4,1,phi,phi'),

where phi=(1+sqrt(5))/2 and phi'=1-phi. Thus the actual multiplication map has the entire unique A in its kernel and the entire V in its cokernel. At this stage matching-channel defects are not excluded; Section 4 will exclude them geometrically.

Moreover A occurs only in the mixed term V tensor G: neither Sym^2 V nor Sym^2 G contains A. Choose bases only for notation, writing ambient coordinates as (x,y) in the two blocks. The forced net consequently has the form

    Q(x,y)=M(x)y=N(y)x,

where M is a 3-by-4 matrix of linear forms in x and N a 3-by-3 matrix of linear forms in y. These express intrinsic bilinear maps; no actual coefficients are selected or evaluated.

The parametrization of T is

    p |-> [q0(p)p : g(p)],

where g is the vector of four cubic generators of I_Z6. The identity Q(q0(p)p,g(p))=0, and cancellation of the nonzero polynomial q0, give

    M(p)g(p)=0.                                      (1)

## 2. Identification with the full six-point Hilbert-Burch matrix

The established six-point theorem gives I_Z6(2)=0, 3-regularity, and four degree-three generators. A saturated finite-point ideal in the polynomial ring of P2 is Cohen-Macaulay of codimension two. Its minimal resolution therefore has length one. There are three minimal syzygies, and regularity forces their degrees to be four:

    0 -> O_R(-4)^3 -> O_R(-3)^4 -> I_Z6 -> 0.        (2)

The three independent quadrics in the A-net give three independent linear syzygies in (1): the map from a bilinear equation to its coefficient row is injective. They therefore exhaust the three-dimensional linear-syzygy space in (2). Hence M is the full Hilbert-Burch matrix, up to invertible changes of the source and generator bases.

Its maximal minors generate I_Z6. Thus M(p) has rank three outside Z6. At a point of Z6 it has rank exactly two: locally the reduced point ideal has two generators, so the four-generator presentation (2) has two cancellable unit summands and a one-relation minimal presentation. In particular there is no locus of rank at most one.

These are deductions from the actual ideal presentation, not evaluated matrix ranks.

## 3. The cubic surface associated to the four-generator system

For completeness, the required cubic-surface geometry follows from the same presentation. The incidence

    B={(p,[y]) in P2 x P3 : M(p)y=0}

is the blowup of R at Z6. Indeed its equations present the symmetric algebra of I_Z6(3); this ideal is locally a complete intersection and hence of linear type, so the symmetric and Rees algebras agree. The map to P3 is the four-cubic system, with divisor class

    H_S=3H-sum E_i=-K_B.

The incidence has dimension two: its fibers over R are points away from Z6 and projective lines at Z6. Therefore det N(y) is not identically zero. Otherwise every [y] in P3 would admit a nonzero kernel vector p, making B dominate P3.

This determinant is a nonzero A5-invariant cubic on the irreducible four-space. The unique such cubic is smooth, as proved universally in ACTUAL-GAMMA-CLEBSCH-CUBIC.md, Section 2. Thus it cuts a smooth Clebsch cubic S. At every point of S, N has rank two: rank at most one would annihilate all first derivatives of its determinant. The kernel line consequently varies regularly and supplies an inverse S->B to the second projection. Hence

    B isomorphic to S,     O_S(1)=-K_B,

and this anticanonical divisor is ample. This identifies the four-generator cubic model without asserting an identification of its conic image with any previously named HM curve.

## 4. The quadratic equation count is exactly three

The products involving at least one q0 V* factor span all of q0 H0(O_R(4)). Indeed multiplication V* tensor G -> I_Z6(4) is onto because the ideal is generated in degree three. The latter space has dimension nine. Furthermore

    q0 Sym^2 V* intersection I_Z6(4) = 0:

if q0 h vanishes on Z6, then h does, because q0 is nonzero at each of these six points; but I_Z6(2)=0. The spaces q0 Sym^2 V* and I_Z6(4) have dimensions six and nine, so their sum is all H0(O_R(4)). Thus these products contribute exactly fifteen dimensions.

The products Sym^2 G contribute ten independent dimensions: the four-generator image is the cubic surface S, which has no quadratic equation. These ten dimensions have zero intersection with q0 H0(O_R(4)). Otherwise a nonzero quadric on P3 would contain the image of C0=(q0=0). Since C0 avoids Z6, its strict-transform class on B is 2H. Such a quadric would give an effective divisor of class

    2H_S-2H=4H-2 sum E_i.

This class is nonzero and has intersection zero with the ample H_S, which is impossible for a nonzero effective divisor.

The actual quadratic multiplication map therefore has rank 15+10=25. Its source and target both have dimension 28. The forced three-dimensional kernel and cokernel from Section 1 exhaust the defects:

    H0(I_T(2))=A,     H1(I_T(2))=V.                  (3)

No unverified matching-channel rank remains in (3).

## 5. The complete intersection and its two components

Consider X=V(Q) in P6. On the open set x!=0, projection to [x] in P2 has affine fiber ker M(x): dimension one away from Z6, and dimension two at Z6. Thus this open part has dimension three, with one irreducible three-dimensional component, the closure Y of the affine-line bundle over R minus Z6. The exceptional fibers have dimension two and cannot supply further three-dimensional components.

The complement x=0 is the coordinate P3. Therefore X has dimension three, so the three quadrics have height three and are a regular sequence in the polynomial ring. In particular X is a degree-eight complete intersection and is unmixed.

At a general point [0:y] of the coordinate P3 outside S, the x-Jacobian N(y) is invertible. This component is therefore generically reduced, of multiplicity one. The main component is generically smooth on the affine-line-bundle open, so it too has multiplicity one. There are no further components; unmixedness and generic reducedness make X reduced. Consequently

    X=P3 union Y,     deg(Y)=8-1=7.

The parametrization of T lies on Y on the dense open R minus (C0 union Z6), hence all of T lies on Y. The regular-sequence conclusion comes from the actual incidence dimension, not from a comparison between degrees eight and nine in different dimensions.

## 6. The canonical conormal section

Let N_T=N_(T/P6), pulled back to R. The tangent sequence gives

    c(N_T)=(1+3H)^7/(1+H)^3=1+18H+132H^2.

The quadratic differential is

    theta:A tensor O_R(-6) -> N_T*.

Its maximal minors form an invariant section of

    Hom(det(A O(-6)), Lambda^3 N_T*) = N_T,

because det A is trivial and det N_T=O_R(18). The finite group has no nontrivial characters, so the equivariant identifications introduce no hidden character twist.

The invariant section space H0(N_T)^A5 has dimension one. The Euler sequence gives

    h0(T_P6|R)^A5 = dim Hom_A5(L,H0(O_R(3)))-1 = 2-1=1.

The tangent bundle of R has H1(T_R)=0 and H0(T_R)^A5=0, the latter because V is irreducible. The normal sequence therefore preserves this one-dimensional invariant space.

A generator is the normal component nu of the ambient vector field scaling the V-block relative to the four-block. Its zero support is exactly C0 union Z6. On C0 the V-block is zero, so the ambient field itself vanishes. Away from C0, projection to the V-block identifies T with its original plane point p. The scaling vector field projects to zero on P(V); if it were tangent to T, the corresponding tangent vector on R would thus be zero. The ambient vector field must then vanish, which occurs exactly when g(p)=0, namely at Z6. It is nonzero at every other point.

The actual minors are nonzero. At p outside C0 union Z6, the y-Jacobian is M(q0(p)p), which has rank three by Section 2. Therefore theta has rank three there. Its invariant minors are consequently a nonzero scalar multiple of nu. This proves the exact rank-drop support asserted in the theorem.

## 7. Why the number 24 is not a finite degeneracy length

The source O_R(-6)^3 has c1=-18H and c2=108H^2. Thus

    c1(N_T* - O_R(-6)^3)=0,
    c2(N_T* - O_R(-6)^3)=24H^2.

For a rank-three to rank-four map, expected codimension of rank at most two is two. If that hypothesis held, Porteous would give length 24. But Section 6 proves that the actual rank-drop locus contains the entire invariant conic. The expected-codimension hypothesis fails. Neither a length-24 finite scheme nor a finite orbit-cycle classification describes this actual degeneracy.

Because the net is a regular sequence, its Jacobian singular scheme restricted to T is precisely the determinantal scheme of theta. Only its support has been identified here; no scheme multiplicities along C0 or Z6 are asserted.

## Dependencies and boundaries

The determinant-family and embedded-surface theorems supply the actual system L, the reduced six-point base scheme, and the closed immersion. QUADRATIC-CHANNELS-CHECK.md independently verifies the character mismatch and the absence of ambient linear syzygies; alternatively the latter now follows immediately from the regular sequence. The universal smooth invariant-cubic proof is used in Section 3. The companion verify_projected_veronese_quadrics.py checks only the character and Chern arithmetic; its conditional finite-orbit arithmetic is not an assertion about this positive-dimensional degeneracy.

No selected HM/source coefficients, evaluated actual matrices or ranks, scans, or experiments are used. The theorem does not identify the two unrelated degree-six curves automatically, prove smoothness of individual determinant cubics, or settle remaining adjoint multiplication gates.
