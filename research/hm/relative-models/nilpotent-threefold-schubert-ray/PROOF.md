> Publication scope: Exact pushforward ray and degree divisibility with degree bounds; necessary constraints only. Historical statements about unresolved mixed classes refer to the source stage; this packet does not supersede the separately stated conditional mixed-vanishing result in PR145.

# A forced Schubert ray and degree divisibility for nilpotent threefold images

## Result

Under the hypotheses and conclusions of `../nilpotent-extremal-picard-obstruction/PROOF.md`, let Z be an integral projective threefold in the reduced nilpotent incidence N, and let g:Z -> G=Gr(3,5) be the recovered-three-plane map. Use the standard Schubert convention with partitions inside the 3-by-2 rectangle, so sigma_1=c1(Q) for the tautological rank-two quotient Q.

If dim g(Z)=3, put B=g(Z) with reduced structure, delta=[C(Z):C(B)], and c=degree(t^3[Z]). Then c is a positive integer, and

    g_*[Z] = 3c (sigma_111 + 4 sigma_21) in CH^3(G),
    [B] = n (sigma_111 + 4 sigma_21),
    delta n = 3c,
    degree_Plucker(B) = 9n,

where n is a positive integer. Moreover delta<=6. If the generic kernel dimension over B is one, delta=1 and 3 divides n. If it is two, delta<=3; when the restricted trace-square is not identically zero at the generic point, delta<=2. In particular if 3 does not divide delta, then 3 divides n and the Plucker degree of B is divisible by 27.

These are necessary cycle and degree constraints; they neither construct an extremal component nor exclude all threefolds. If dim g(Z)=2, g_*[Z]=0 as a three-cycle and no positive n is asserted.

No actual operation, source-model value, matrix, rank instance, selected input, jet, or residue is evaluated. This is a universal intersection-theoretic deduction, with only local proof-file writes.

## 1. Imported bundles and degrees

On N the recovered rank-three bundle W is filtered with line quotients L, M, and M^2 tensor L^(-1). Put h=c1(L*) and t=c1(M*). These are integral Cartier classes, are nef, and 2h+t is ample. Moreover

    g* sigma_1 = 3t,
    c2(g*Q) = h^2 - 2ht + 7t^2,
    t(h^2 - 2ht + 3t^2) = 0.

These identities hold operationally on the possibly singular reduced N and may be restricted to Z. Write

    a=degree(h^2 t[Z]), b=degree(ht^2[Z]), c=degree(t^3[Z]).

Then a-2b+3c=0. If dim B=3, the pullback of the ample Plucker bundle is nef and big on Z. The projection formula gives

    27c = degree((g*sigma_1)^3[Z]) = delta degree_Plucker(B) > 0.

Thus c is a strictly positive integer.

## 2. The two middle-dimensional Schubert pairings

The rank-two quotient Q has c3(Q)=0. The Giambelli identities give

    sigma_21 = c1(Q)c2(Q),
    sigma_111 = c1(Q)^3 - 2c1(Q)c2(Q).

In particular sigma_1^3=2sigma_21+sigma_111. Pulling back and taking degrees yields

    degree(g*sigma_21 [Z])
      = 3(a-2b+7c) = 12c,

    degree(g*sigma_111 [Z])
      = 27c - 2(12c) = 3c.

Equivalently the second equality also follows from sigma_111=c3(S*) and c3(W*)=ht(2t-h).

The group CH^3(Gr(3,5)) is free on sigma_111 and sigma_21. Both partitions are self-complementary in the 3-by-2 rectangle. The Schubert intersection pairing therefore satisfies

    degree(sigma_111^2)=degree(sigma_21^2)=1,
    degree(sigma_111 sigma_21)=0.

By the projection formula the two preceding pairings determine the complete integral Chow class:

    g_*[Z] = 3c sigma_111 + 12c sigma_21.

The map Z -> B is proper and generically finite, so g_*[Z]=delta[B]. Expressing [B] in the integral Schubert basis proves that n=3c/delta is an integer and

    [B]=n(sigma_111+4sigma_21).

Pairing with sigma_1^3 gives degree_Plucker(B)=n+8n=9n. If 3 does not divide delta, the equality delta n=3c implies 3 divides n.

## 3. A universal bound on the generic degree

The imported global results give dim N<=3 and dim G_4<=2, where G_k denotes the kernel-dimension-k stratum. Since B has dimension three, the generic kernel dimension k on B is at most three and at least one. Also the full nilpotent incidence over the generic point of B has dimension zero. Indeed, if a component of N over the generic point of B had positive dimension, its closure in N would have dimension at least four, contrary to dim N<=3. The following point bounds can be checked after an algebraic closure of C(B).

For k=1, the projective kernel is a point. Thus delta=1.

For k=2, the projective kernel is P^1 and its nilpotent locus is cut out by a quadratic q and a cubic d. At least one is nonzero because the fiber is zero-dimensional. If q is nonzero, the reduced common-zero set has at most two points. If q is identically zero, the cubic d must be nonzero and there are at most three points. Thus delta<=3, improved to delta<=2 when q is nonzero.

For k=3, the projective kernel is P^2. Both q and d must be nonzero: the zero set of one nonzero positive-degree homogeneous polynomial in P^2 is a curve. They cannot share a common homogeneous factor, since that would give a curve of common zeros. Hence they form a plane complete intersection of degrees two and three and length six. Their reduced common-zero support has at most six points.

Finally the extension C(Z)/C(B) is separable because the characteristic is zero. Its generic geometric fiber has delta distinct points and embeds as a subset of the full reduced nilpotent fiber. The preceding bounds therefore give delta<=6, with the stated refinements. This argument counts geometric points rather than claiming that the original incidence equations are reduced or transverse.

## 4. Consequence for the boundary of a four-dimensional spectral component

Let Y be an integral four-dimensional component of the projective spectral incidence X. The nonzero trace-square section q is a section of M_spectral^2, where

    c1(M_spectral)=r-H,
    r=c1(O_P(E)(1)), H=p*c1(O_G(1)).

Its nonempty effective Cartier divisor D has cycle sum_i m_i[Z_i], where the Z_i are integral nilpotent threefolds and m_i are positive integers. For each Z_i put c_i=degree(t^3[Z_i]); this is nonnegative and is zero precisely when dim g(Z_i)<3. Thus the proper pushforward to G satisfies

    p_*(2(r-H) cap [Y])
      = 3C (sigma_111+4sigma_21),
    C=sum_i m_i c_i >= 0.

In particular its Plucker degree is 27C. This includes the case C=0, when all boundary components have image dimension at most two. No effectiveness of r-H away from its given effective multiple, no normality of Y, and no smoothness of the boundary are assumed.
