# Generic twist-three adjoint vanishing from a rank-four cone

## Statement

Let F be the normalized Horrocks–Mumford bundle on P4 over C and B=End_0(F). For a general smooth quadric threefold Q,

    H0(Q,B|Q(3))=0.

Consequently a general smooth quadric admits no nonzero twist-three trace-free map F|Q -> F|Q(3). Combined with the previously checked exclusions of lower primitive twists, the remaining generic full-adjoint obstruction is confined to primitive twist four. This does NOT prove H0(B|Q(4))=0 or the full repair.

## Checked inputs

1. Boralevi, *The Horrocks–Mumford bundle restricted to planes*, https://arxiv.org/pdf/math/0602002, Main Theorem, printed pp.2–3, and Corollary 2.2, printed p.5: outside a closed subset of dimension at most four in Gr(3,5), every plane P has one of

       0 -> 3O_P(-3) -> 5O_P(-2) -> F_P -> 0,
       0 -> O_P(-4) -> O_P(-1)+2O_P(-2) -> F_P -> 0.

   The Grassmannian has dimension six. The first type is open; the second is the divisor stratum. No chosen monad entries are used.
2. The actual primary module satisfies H0(F)=H0(F(2))=0. The published proof packet GENERIC-PRODUCT-PRIMARY-INJECTION.md supplies a nonzero rank-two quadratic q for which q:H1(F)->H1(F(2)) is injective. This input is also used and scoped in the checked product-adjoint note at 04ae00f0134c15d63dc39f84ce9a07b8ed81515d.

## 1. A cone whose every ruling plane has one of the two resolutions

Choose one ruling of planes on a rank-four quadric cone. It is a projective curve in Gr(3,5). PGL5 acts transitively on Gr(3,5). If Z is the closed dimension-at-most-four union of the lower strata, the incidence of pairs (g,t) with g(P_t) in Z has dimension at most dim(PGL5)-1. Since the ruling curve is proper, its projection to PGL5 is closed and proper. Thus a general translate has no plane in Z.

This establishes a nonempty open condition on cones with chosen ruling. It uses no assertion about the exact number of divisor-stratum planes or about their local crossing multiplicities.

## 2. The two planewise symmetric-product maps are isomorphisms

Write E_P=F_P(2). For the generic plane type, E_P has resolution

    0 -> 3O(-1) -> 5O -> E_P -> 0.

It is globally generated, with h0(E_P)=5 and higher cohomology zero. The symmetric-square resolution is

    0 -> 3O(-2) -> 15O(-1) -> 15O -> Sym^2(E_P) -> 0.

All cohomology of O(-1) and O(-2) on P2 vanishes, so the natural map

    Sym^2 H0(E_P) -> H0(Sym^2 E_P)

is an isomorphism of dimension fifteen, and the target bundle has no higher cohomology.

For the divisor-stratum type, use

    0 -> O(-2) -> D=O(1)+2O -> E_P -> 0.

Again E_P is globally generated, h0(E_P)=5 and higher cohomology zero. Since the kernel is a line bundle, its symmetric-square sequence is

    0 -> O(-1)+2O(-2) -> Sym^2 D -> Sym^2 E_P -> 0.

The left term is acyclic. The natural map Sym^2 H0(D)->H0(Sym^2 D) is an isomorphism: its summands are ordinary quadratic products of the three independent linear forms, their products with two constants, and products of those constants. Their dimensions are respectively six, six, and three. This proves the same dimension-fifteen symmetric-product isomorphism and higher-cohomology vanishing for the divisor-stratum plane.

These are exact consequences of the resolutions, not inferred generic ranks.

## 3. Ruling pushforward and negativity

A chosen ruling gives the small resolution

    pi:Y=P_{P1}(O+O(1)+O(1)) -> Q,
    p:Y->P1, H=O_Y(1)=pi^*O_Q(1).

Every fiber of p maps isomorphically to its ruling plane, including at the vertex. Let E=pi^*(F_Q(2)) and J=p_*E. Section 2 and cohomology/base change give a rank-five bundle J, with fiber H0(E_P). The actual relative product map gives an isomorphism

    Sym^2 J -> p_*Sym^2 E,

because it is an isomorphism on every fiber. Since det(F) is O(-1), the characteristic-zero rank-two identity End_0(F)=Sym^2(F)(1) identifies Sym^2 E with pi^*(B_Q(3)).

The rank-at-most-four quadratic variety is irreducible and has the rank-four locus dense. Primary rank-deficiency is a closed locus there. Input 2 supplies a primary-good rank-two point, so a nonempty open subset of this variety is primary-good and meets the rank-four locus. Pull this nonempty primary-good rank-four open back to PGL5 acting on one fixed cone with chosen ruling. The orbit map is onto the rank-four cones, so its pullback is nonempty open. Intersecting with the ruling open of Section 1 inside the irreducible group PGL5 supplies a cone satisfying both conditions. Goodness at a rank-two point is not asserted to extend to every cone.

For such a cone, the hypersurface restriction sequence and the two ambient H0 vanishings identify

    H0(F_Q(2)) = ker[q:H1(F)->H1(F(2))] = 0.

The cone is normal. Proper birationality from the smooth small resolution gives pi_*O_Y=O_Q. Projection formula therefore identifies H0(Y,E)=H0(Q,F_Q(2)); no higher-direct-image vanishing is needed for this H0 argument. Thus H0(P1,J)=0. By splitting on P1, every summand of J has strictly negative degree. Every summand of Sym^2 J is then strictly negative, so

    H0(Q,B_Q(3))
      = H0(Y,pi^*(B_Q(3)))
      = H0(P1,Sym^2 J)
      = 0.

This proves an actual cone vanishing witness without choosing its coefficients or computing a matrix rank.

## 4. Passing to general smooth quadrics

The universal family of nonzero quadrics over P(H0(O_P4(2))) is a flat projective family of Cartier hypersurfaces. Restricting the ambient locally free B(3) gives a sheaf flat over this parameter space. Upper semicontinuity makes the locus where h0(B_Q(3))=0 open. Section 3 proves it is nonempty. The parameter space is irreducible, and its smooth-quadric locus is dense open; their intersection is therefore nonempty open. This proves the stated vanishing for general smooth Q.

No invertibility of the twist-four multiplication, balancedness of a twist-four ruling pushforward, or transversality of the conductor value subspaces follows from this result. Those gates remain separate.
