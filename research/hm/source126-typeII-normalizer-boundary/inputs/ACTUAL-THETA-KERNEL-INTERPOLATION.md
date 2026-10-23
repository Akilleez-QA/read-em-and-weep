# The actual 25 points are a theta-kernel orbit

## Statement

For a smooth general beta surface X_B, let pi:X_B -> A be the contraction of its25 HM lines, let Sigma be the25 contraction points, and let P be the descended polarization with pi*P=H+C. Then, after choosing one point of Sigma as origin,

    Sigma = K(P)[5] = K(Theta),
    P = Theta^2,

where Theta is a polarization of type(1,5), and K(L) denotes the translation kernel {a : t_a*L is isomorphic to L}. Thus the interpolation in GENERIC-BETA-ABELIAN-INTERPOLATION.md is at the actual theta-kernel configuration, not at25 freely chosen general points.

Moreover, with W=H0(A,P tensor I_Sigma), the actual quadric subsystem is exactly

    Sym^2 W -> H0(A,P^2 tensor I_Sigma^2),

and this multiplication map is an isomorphism between15-dimensional spaces. In particular the quadratic section used by the55 -> 70 interpolation map is constrained by this complete quadratic system; it is not a freely chosen section of P^2.

## 1. The cohomology action forces translations

ADHPR, Syzygies of Abelian and Bielliptic Surfaces in P4, Section1 and Section3, fixes the actual action of the Heisenberg group H5 and its normalizer N5 on the normalized HM bundle F. The quotient N5/H5 is SL2(F5). The nontrivial one-dimensional characters of H5 are the24 nonzero characters of H5/[H5,H5], and SL2(F5) acts transitively on them. Every irreducible representation with nontrivial central character has dimension5.

Proposition3.2 gives dim H1(F(3))=2. Because this is an actual N5-module, its H5 restriction cannot contain a5-dimensional irreducible. It also cannot contain a nontrivial one-dimensional character: normalizer equivariance would force all24 characters in that orbit to occur with the same positive multiplicity. Therefore H5 acts trivially on H1(F(3)). The same argument applies to the actual four-dimensional N5-module H0(F(3))=U, so H5 acts trivially on U and on det B for every fixed hyperplane B.

The actual Hilbert–Burch resolution and Serre duality identify

    H1(O_X_B) = det B tensor H1(F(3))*

H5-equivariantly, up to the fixed canonical volume line (trivial on H5). Thus H5 acts trivially on H1(O_X_B). Blowup invariance identifies this with H1(O_A). By Hodge theory it also acts trivially on H0(Omega_A^1).

The projective quotient G=H5/center, of order25, acts on X_B and permutes its25 exceptional curves simply transitively. The contraction is equivariant, so G acts on A and simply transitively on Sigma. Any automorphism of a complex abelian variety is a translation followed by a group automorphism. Its action on one-forms determines the differential of the group part; identity on all one-forms forces that group automorphism to be the identity. Hence every element of G acts by a translation.

This is an actual representation argument. The mere fact that q(A)=2 would not, without normalizer equivariance, rule out nontrivial characters or linear automorphisms.

## 2. Identification with the polarization kernel

Both H and C are G-invariant as line bundles, so pi*P=H+C is invariant. Injectivity of pi*:Pic(A)->Pic(X_B) gives t_g*P isomorphic to P for every g in the translation group G. Therefore G is a subgroup of K(P)[5].

The linked-family source proves that P has type(2,10). Its polarization kernel is

    K(P) isomorphic to (Z/2)^2 times (Z/10)^2,

whose5-primary subgroup has exactly25 elements and is isomorphic to (Z/5)^2. Since G already has25 elements, G=K(P)[5]. Choosing any point of Sigma as the origin converts its free orbit into that subgroup itself.

The Riemann form of a type(2,10) polarization is divisible by2 as an integral alternating form. Its half is a positive integral (1,1) form of type(1,5), hence is the Chern class of an ample line bundle Theta0. The line P tensor Theta0^(-2) is in Pic0(A); multiplication by2 on Pic0(A) is surjective. After modifying Theta0 by a flat line, choose Theta with Theta^2=P. Its kernel has order25 and lies in K(P)[5], so K(Theta)=K(P)[5]. No uniqueness of the square root is asserted or needed.

## 3. The actual complete quadratic subsystem

The blowup identities give

    W=H0(A,P tensor I_Sigma)=H0(X_B,H),
    H0(A,P^2 tensor I_Sigma^2)=H0(X_B,2H).

The Hilbert–Burch resolution shows that restriction from P4 is an isomorphism in degrees1 and2. For degree2, H0(I_X(2))=0 follows from H1(F(-5))=0, and H1(I_X(2))=H2(F(-5))=H2(F(1))*=0. The normalized HM monad gives the latter vanishing. Consequently

    H0(X_B,H)=H0(P4,O(1)),
    H0(X_B,2H)=H0(P4,O(2)).

The multiplication map is therefore the actual ambient isomorphism Sym^2 H0(O_P4(1)) -> H0(O_P4(2)), transferred through these restriction maps. In particular dim W=5 and the quadric subsystem has dimension15.

In theta notation the interpolation map of the preceding note is precisely multiplication by

    q in Sym^2 H0(Theta^2 tensor I_K(Theta))
      = H0(Theta^4 tensor I_K(Theta)^2)

on

    H1(Theta^2 tensor I_K(Theta)^2)
        -> H1(Theta^6 tensor I_K(Theta)^4),

of dimensions55 -> 70. The ideals here are ordinary powers at the25 distinct smooth points, not25 independent arbitrary jets with independently chosen coordinates.

## Boundary

This identifies the specific abelian surface configuration and the allowed multiplier subsystem. It proves neither maximal rank of the55 -> 70 multiplication nor invertibility of its universal20 -> 20 boundary. Generic-position point counts and arbitrary theta-polynomial coefficients cannot replace this actual theta-kernel interpolation map.

Sources: https://arxiv.org/pdf/alg-geom/9606013v2 , Sections1,3,7 and Proposition8.4(ii); the actual beta-family/linkage and universal quotient identifications are proved in GENERIC-BETA-ABELIAN-INTERPOLATION.md. No selected HM coefficients or rank computation is used.
