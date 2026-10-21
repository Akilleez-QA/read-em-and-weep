# Wedge rank detects the common radical of a net

## Statement

Let A be a five-dimensional vector space over C, and let N be a three-dimensional linear subspace of exterior^2 A*. Define

    w_N : Sym^2 N -> exterior^4 A*,   omega eta |-> omega wedge eta.

Then rank(w_N) is at most one if and only if the common radical

    Rad(N) = {x in A : contraction_x(omega)=0 for every omega in N}

is nonzero. More precisely:

1. If rank(w_N)=1, N contains a rank-four alternating form, Rad(N) has dimension one, and its line corresponds canonically to image(w_N) under exterior^4 A* = A tensor det(A*).
2. If rank(w_N)=0, exactly one of the following forms occurs, after choosing independent covectors a,b,c,d as needed:
   - N = span(a wedge b, a wedge c, a wedge d); Rad(N)=ann(span(a,b,c,d)) has dimension one.
   - N = exterior^2 span(a,b,c); Rad(N)=ann(span(a,b,c)) has dimension two.

These statements are about vector spaces and closed-point supports. There is also a scheme-theoretic statement on the open locus of nets containing a rank-four form, proved below. No scheme-theoretic identification across the rank-zero wedge locus is asserted.

## Necessity

If x is a nonzero common radical, every member of N lies in exterior^2(x^perp), where x^perp is the four-dimensional annihilator of x in A*. Thus all wedge products lie in the line exterior^4(x^perp), which corresponds to Cx tensor det(A*). Consequently rank(w_N)<=1.

## Rank-one sufficiency

Fix a volume form only to suppress the constant determinant factor. For an alternating form omega let P(omega) denote the vector corresponding to omega wedge omega. The identity

    contraction_{P(omega)}(omega)=0

holds identically in the coefficients of omega. It can be verified in an alternating normal form, and hence is a polynomial identity. Moreover P(omega) is nonzero exactly when omega has rank four, in which case it spans its radical.

If w_N is nonzero, some omega_0 has nonzero square: otherwise polarization would make every product zero. Let its Pfaffian line be Cx. Since all wedge products lie in Cx, the vector P(omega_0+t omega) lies in Cx for every omega in N. It is nonzero for general t, so contraction_x(omega_0+t omega)=0 for general t. Comparing coefficients yields contraction_x(omega)=0 for every omega. Since omega_0 already has a one-dimensional radical, Rad(N)=Cx.

## Classification when all products vanish

Every nonzero element of N is decomposable, since its square vanishes. Choose two independent elements. Their two-dimensional covector supports intersect in a line, because their product vanishes; they cannot have equal support, since exterior^2 of a two-space is one-dimensional. Thus they can be written as a wedge b and a wedge c with a,b,c independent.

Choose a third element eta outside their span and write its support as a two-plane P. The vanishing of eta wedge a wedge b and eta wedge a wedge c says that P meets both span(a,b) and span(a,c).

If a belongs to P, write eta=a wedge d. Independence of the three forms forces d outside span(a,b,c), yielding the first normal form.

If a does not belong to P, those two intersections are distinct lines. They span P, and both lie in span(a,b,c). Hence eta belongs to exterior^2 span(a,b,c). As it is independent of the first two forms, the three forms span that whole three-dimensional exterior square, yielding the second normal form.

The common radical of a family is the annihilator of the sum of its covector supports. This gives the dimensions and formulas claimed, and completes sufficiency also when w_N=0. In particular, a zero wedge map does not select an arbitrary prescribed radical line.

## Scheme-theoretic bridge away from all-rank-two nets

Let G=Gr(3,exterior^2 A*) with tautological bundle N, and let D be the determinantal closed subscheme defined by the 2-by-2 minors of w:Sym^2 N -> exterior^4 A*. Let U be the open locus where N contains a rank-four form. Let J be the closed incidence subscheme of G times P(A), defined by contraction_x(N)=0.

Then the projection J restricted over U -> D intersect U is an isomorphism. Its inverse sends a net to its unique Pfaffian line.

Proof works over arbitrary C-algebras, including nonreduced ones. Work locally on U, choose a local section omega_0 of N, and invert a coordinate of P(omega_0). The rank-at-most-one minors force every wedge column to be a unique scalar multiple of P(omega_0). Put x=P(omega_0), regarded as a unimodular vector on this chart. For every local section omega of N, there is a polynomial a(t) with a(0)=1 such that

    P(omega_0+t omega)=a(t)x.

The alternating adjugate identity gives a(t) contraction_x(omega_0+t omega)=0. Its constant coefficient gives contraction_x(omega_0)=0; its coefficient of t then gives contraction_x(omega)=0. Thus the radical incidence equations hold in the determinantal coordinate ring itself, not merely at its closed points.

Conversely, on J choose locally a generator x of the universal radical line. All forms lie in exterior^2(x^perp), a rank-six bundle, and their products lie in exterior^4(x^perp), a line subbundle. Therefore all 2-by-2 minors vanish. Since omega_0 has rank four on this chart, its radical line equals the universal line x, also over the base algebra: the alternating rank-four pivot has invertible symplectic block and a rank-one kernel. The two constructions are inverse and glue. The choice of volume affects no projective line.

## Application boundary

For any injective universal map phi*:V* tensor W* -> exterior^2 A* with dim W=2, and a rank-two tensor k=p tensor epsilon_1+q tensor epsilon_2, its traceless orbit spans a three-dimensional net

    N_k = span(F_1(q), F_2(p), F_1(p)-F_2(q)),
    F_i(r)=phi*(r tensor epsilon_i).

The condition that N_k has a common radical is therefore exactly rank(w_{N_k})<=1 on closed points. On the open sublocus containing a rank-four form, this replacement is scheme-theoretic and recovers the radical uniquely. On the zero-wedge locus the two normal forms above must be retained, with radical projective fibers a point or a projective line.

This is a universal net lemma, not an identification with a modular surface or a proof of normality, transversality, or smoothness of any HM degeneracy scheme. No selected HM/source coefficients, numerical ranks, or large computation are used. The proof is elementary mathematical reasoning, not a proof-assistant certificate.

## Pullback to a traceless-orbit family

Suppose phi* is an isomorphism and let T be the open locus of tensor-rank-two points in P(V* tensor W*). The span of the three displayed forms defines a morphism f:T->G: the traceless-orbit map has rank three at every such point, since p,q are independent. Define the kernel incidence X in T times P(A) by all equations contraction_x(N_k)=0. Equivalently these are the three traceless-action pairing equations, with their full scheme structures.

On T_4=f^{-1}(U), the preceding universal isomorphism pulls back to

    X restricted over T_4 = f^{-1}(D intersect U),

where the right side is the scheme defined by the 2-by-2 minors of the pulled-back wedge map, and the projection to P(A) is its regular Pfaffian-radical map. This uses base change of an isomorphism, so no flatness or reducedness hypothesis is required. Any further exact-rank-nine condition on the evaluation at x is simply an open restriction of this correspondence. The assertion does not exclude f^{-1}(G\U), nor assert that any chosen actual point belongs to T_4.
