# The actual vector shadow has a twelve-point polar normal form

## New conclusions and exact boundary

Retain the actual quadratic maps

    i: V O_L(-2) -> P4 O_L,
    Q: D5 O_L -> V O_L(2),

and invariant nondegenerate symmetric pairings on V, P4, and D5. The following statements are about those actual maps and the pinned vector representative R, not a selected coefficient model.

1. For a nonzero scalar d, with the indicated twists understood,

       Q Q^t = d i^t i.                                      (1)

   Thus the two actual quadratic presentations have the same nonzero quartic Gram map, up to their fixed pairing normalization.

2. Let E be its known reduced twelve-point degeneracy orbit. The actual quintic extension has a canonical orthogonal meromorphic generator on L minus E. Its poles are simple and its Gram scalar primitive v is identically zero. Comparing it with regular generators at E represents the actual class of R by principal parts of order at most two at these twelve points.

3. Write r_x/z for the polar part of the transition p at x in E, in a normalized local coordinate with z(x)=0. Then r_x is nonzero and isotropic, and the ENTIRE second principal part of R is

       R = (k/15) a(x)^2 tau(h,r_x) z^(-2) + O(z^(-1)).       (2)

   Every other possible double pole cancels. In particular the canonical global scalar inverse u, including its extension correction, affects only the simple principal-part layer in this normal form.

The twelve isotropic lines C r_x correspond to twelve distinct squares ell_x^2 in V=Sym^2 Wprime. The local h-map in (2), before its scalar a(x)^2, is onto V and has kernel ell_x^3 Wprime. Thus for nonzero a and h at least nine of the twelve double coefficients are nonzero.

This last assertion is NOT a nonvanishing theorem for [R], [aR], or the third Bockstein. A global meromorphic coboundary may cancel nonzero principal parts, and the simple principal parts still contain the full actual scalar correction. The final A, D5, and second-Bockstein quotients remain in force. The new result is an actual polar normal form and an exact exclusion of all nonderivative contributions from its second principal-part layer.

## 1. The second actual Gram identity

Regard Q^t as the subbundle map V O_L(-2)->D5 O_L. The composite N=Q Q^t is a symmetric quartic map V O_L(-2)->V O_L(2). Its equivariant Hom space is one-dimensional:

    [End(V) tensor H0(O_L(4))]^G = 1,
    End(V)=1 plus V plus D5,   H0(O_L(4))=D5.

It is important to prove N is nonzero rather than infer this from its two factors. In any fiber Q is onto, so Q^t embeds a three-dimensional subspace of the nondegenerate symmetric five-space D5. If Q Q^t were zero there, that subspace would be totally isotropic. Such a subspace has dimension at most two, since S subset S-perp implies 2 dim S <= 5. Thus N is nonzero in every fiber as a matrix, although it can have rank two.

The actual Gram theorem already proves i^t i is a nonzero element of the same one-dimensional Hom space. This proves (1), with d different from zero. If M_kappa=c i^t i is the actual multiplication map, then N=(d/c)M_kappa. All scalars are retained.

Consequently N has the same reduced degeneracy divisor E, rank two on E and rank three elsewhere. It satisfies N^3=(det N) identity with the line twists retained, and its value at every x in E is regular nilpotent. These properties follow from the actual Gram theorem, not from a selected matrix evaluation.

## 2. A canonical meromorphic inverse, and the correction it does not remove

Put Delta=det N, a nonzero section of O_L(12). On L minus E the quotient Q has the orthogonal right inverse

    S = Q^t N^(-1) = Q^t N^2 / Delta,
    Q S = identity.                                        (3)

Here S:V O_L(2)->D5 O_L. It has at most simple poles because Delta has simple zeros. At each point of E, N^2 has rank one and Q^t remains injective, so its polar coefficient is nonzero of rank one. The identity Q Q^t N^2=N^3 shows that this polar coefficient lands in ker Q. Thus (3) has exactly the twelve simple poles, each with a rank-one kernel-valued residue.

This describes the canonical scalar inverse without pretending that its global extension correction vanishes. Let

    F = k a Lie_(D_a)(Qh) in H0(V O_L(4)),
    u = H0(Q(2))^(-1)(F).

The meromorphic section S(2)F of D5 O_L(2) generally has poles. Write j for the actual cubic inclusion in the twisted quotient sequence

    0 -> Wprime O_L(-1) --j--> D5 O_L(2)
      --Q(2)--> V O_L(4) -> 0.

There is a UNIQUE meromorphic section w of Wprime O_L(-1), with at most simple poles on E, whose image j w has the same principal parts as S(2)F. The reason is the exact principal-parts sequence and

    H0(Wprime O_L(-1)) = H1(Wprime O_L(-1)) = 0.

The rank-one residues in Section 2 lie in the actual kernel subbundle, so the prescribed principal parts do have the required kernel values. Then the exact global formula is

    u = S(2)F - j w.                                      (4)

Uniqueness in (4) is the already known canonical residue inverse. Acyclicity makes w unique; it does NOT say w is zero. Formula (4) preserves the global scalar-extension contribution in R.

## 3. The actual orthogonal quintic generator

Write the actual sextic evaluation sequence as

    0 -> V O_L(-2) --i--> P4 O_L --q--> O_L(6) -> 0.

The transpose q^t has values in the orthogonal kernel of i^t. The universal Gram determinant identity gives

    q q^t = epsilon det(i^t i),   epsilon != 0,             (5)

after fixing the determinant-line and pairing normalizations. One way to see (5) is to identify the normal covector q with the Hodge dual of wedge^3 i; both have degree six, span the same annihilator line, and differ by a nonzero constant. The identity is then the universal Cauchy-Binet Gram identity. It applies to this actual everywhere-injective i and does not evaluate it.

In particular q q^t has the same reduced zero divisor E. The unique orthogonal right inverse of q on L minus E is

    t_perp = q^t/(q q^t): O_L(6) -> P4 O_L.                (6)

Twisting by minus six makes t_perp a meromorphic lift of 1 in P4 O_L(-6), precisely the normalized actual quintic-generator extension. It has simple poles, and its residue at every x is nonzero. The actual inclusion of K5 into the quintic polynomials sends it to a meromorphic generator g_perp. This is a generator of the actual extension, not a chosen split replacement.

The Gram theorem identifies the functional extending n_h with the global lift c i Qh. Therefore its value on t_perp is zero:

    v_perp = c <i Qh,t_perp> = 0.                          (7)

This exact vanishing uses i^t t_perp=0. It does not change the normalization of the primitive or make an arbitrary local choice v=0.

Choose a regular local quintic lift g_x near x in E and put

    g_x = g_perp + p_x f,
    p_x = r_x/z + O(1).

Since the residue of t_perp maps to zero under q, it belongs to im i. Since i^t t_perp=0, its preimage r_x satisfies

    (i^t i)(x) r_x = 0.                                   (8)

It is nonzero and independent of the chosen regular g_x. All coefficient line factors are understood in these local formulas.

## 4. Nilpotent Gram geometry cancels the other double poles

The symmetric Gram endomorphism at x is regular nilpotent of rank two. Its one-dimensional kernel is the image of its square. If r_x=M_x^2 v, self-adjointness and M_x^3=0 imply

    <r_x,r_x>=<v,M_x^4 v>=0.

Moreover n_h=M_kappa Qh, so self-adjointness gives

    tau(r_x,r_x)=0,
    tau(r_x,n_h(x))=0.                                   (9)

The invariant V pairing here is the same pairing as tau, up to its fixed harmless nonzero normalization.

In the SOURCE orthogonal generator g_perp, let

    m_perp=(h f_z-n_h g_perp)/f.

The regular target generator gives m_x=(h f_z-n_h g_x)/f, so the exact relation is

    m_perp=m_x+n_h p_x.

In particular m_perp has at most a simple pole and its coefficient of z^(-1) is n_h(x) r_x. The pinned canonical vector formula, in this source frame and with v_perp=0, is

    R = k a^2[-2tau(p_x,m_perp)/15
              +2p_x tau(p_x,n_h)/5+tau(p_x,p_x)n_h/5
              -tau(h,(p_x)_z)/15]
        -tau(p_x,Gamma)/30,
    Gamma=u+2k a a_z h.                                  (10)

The use of g_perp as source and g_x as target is essential. The target-frame subtraction that defines R is unchanged.

Both u and Gamma are regular in the chosen regular base frame at x. Hence the last term of (10) has at most a simple pole. The other terms have at most double poles. Their double coefficient, before multiplying by k a(x)^2, is

    -2tau(r_x,n_h(x)r_x)/15
    +2r_x tau(r_x,n_h(x))/5
    +tau(r_x,r_x)n_h(x)/5
    +tau(h,r_x)/15.                                     (11)

The sign of the last term follows from (p_x)_z=-r_x z^(-2)+O(1). For arbitrary binary quadratics r,n, the exact identity

    tau(r,nr)=r tau(r,n)+3n tau(r,r)

reduces (11) to

    tau(h,r_x)/15
       +4r_x tau(r_x,n_h(x))/15
       -n_h(x)tau(r_x,r_x)/5.

Equation (9) proves (2). This cancels the nonlinear transition and multiplication contributions at second principal-part order without discarding them from R itself.

For the physical shadow R/nu, the leading coefficient in (2) is divided by nu(x). The nonconstant local factor 1/nu also changes simple coefficients and is retained. After the final multiplication by a, the double coefficient is (k/15nu(x))a(x)^3 tau(h,r_x). Neither statement removes the subsequent quotients.

## 5. Exact local channels, and why they do not settle cohomology

A nonzero null binary quadratic is a square. Thus r_x is a nonzero scalar multiple of ell_x^2. The complete-square conic in P(V) is P(Wprime). The assignment x -> C r_x is equivariant from the twelve-point orbit E to this conic. Every nonempty G orbit on that projective line has at least twelve points, so its image has twelve points and the ell_x are distinct.

For any nonzero ell, the map

    Sym^4 Wprime -> Sym^2 Wprime,
    h -> tau(h,ell^2)

is onto and has kernel ell^3 Wprime. This is the universal directional-second-derivative statement: in a volume-compatible basis with ell=X it is h -> 2 partial_Y^2 h. This choice verifies a universal identity, not actual HM coefficients or an actual-instance rank.

A nonzero positive quartic cannot have triple zeros at two distinct points. Hence tau(h,r_x) is zero for at most one x in E. A nonzero negative quadratic a vanishes at at most two of the twelve base points. This proves the at-least-nine assertion for the double coefficients of R. It also proves that the twelve-point second-principal-part map is injective in h for each nonzero a.

Nevertheless the principal-parts exact sequence is

    H0(V O_L(-6)(2E)) ->
    H0(V O_L(-6)(2E)/V O_L(-6)) -> H1(V O_L(-6)) -> 0.

There is a stronger exact reduction, not just a warning. Put F=V O_L(-6). The sequence

    0 -> F(E)=V O_L(6) -> F(2E)=V O_L(18)
      -> F(2E)|E -> 0

has H1(F(E))=0. Hence its section map onto the second principal-part layer is SURJECTIVE. Every prescribed double layer, including (2), can be removed by a global meromorphic coboundary with poles of order at most two. This removes the double poles of a representative, not the class itself.

After any such subtraction, the remaining simple principal parts are defined modulo H0(F(E)). They give the exact finite quotient

    H1(V O_L(-6)) =
      H0(F(E)/F) / image H0(F(E)),
      dimensions 15 = 36 - 21.                            (12)

Two choices eliminating the same double layer differ by a section of F(E), which is exactly the denominator in (12). Thus this simple-layer class is canonical even though the eliminating section is not.

At the upper twist the analogous exact quotient is

    H1(V O_L(-4)) =
      H0(V O_L(-4)(E)/V O_L(-4))
        / image H0(V O_L(8)),
      dimensions 9 = 36 - 27.                             (13)

Multiplication by a maps the principal-parts sequences for (12) and (13) into each other. The actual connecting A below maps into the actual connecting D5 above, as in the canonical vector theorem. Their further quotients have dimensions twelve and four. The actual second-symbol image must still be removed from that four-space.

Therefore the at-least-nine nonzero second coefficients have NO direct nonvanishing consequence: their entire layer can always be eliminated. Their precise formula is useful because it identifies exactly which global elimination changes the remaining simple layer. Equations (4), (10), and (12) retain the scalar inverse and all its pole corrections in that layer. No assertion is made that its class is zero or nonzero.

## 6. An exact residue criterion for the final quotient

This criterion includes the physical normalization, rather than silently testing the raw vector R. In compatible local Serre frames, write the physical principal part at x as

    R/nu = D_x/z^2 + B_x/z,

where z(x)=0. Its pairing with any zeta in H0(V O_L(4)), the Serre dual of H1(V O_L(-6)), is

    sum over x in E of
      [<D_x,zeta'(x)> + <B_x,zeta(x)>].                   (14)

The derivative and coefficients in (14) are taken in the same transported local frame, so that their sum is the coordinate-independent residue. No actual coefficients or point values are being evaluated in this formula.

For the final third-Bockstein quotient, take c in P4-dual annihilating the actual image of beta2_a, and set

    zeta = a i^t c in H0(V O_L(4)).                       (15)

The actual dual sequences show that i^t c annihilates the connecting D5 in H1(V O_L(-4)), while a i^t c annihilates the connecting A in H1(V O_L(-6)). Therefore (14)-(15) test the actual class after BOTH connecting-space quotients and the quotient by the actual second-symbol image. The final class vanishes if and only if these tests vanish for all such c. For a outside the second-symbol degeneracy scheme Sigma, this annihilator has dimension one. In particular this holds for every square direction, since Sigma is disjoint from the discriminant conic. On Sigma the same criterion uses the full, possibly larger annihilator; no rank-three assertion there is made.

If instead D_x and B_x denote the coefficients of RAW R, the physical coefficients to use in (14) are

    D_x/nu(x),
    B_x/nu(x) - D_x nu'(x)/nu(x)^2.                       (16)

Equivalently, pair the raw coefficients with zeta/nu and its derivative. Formula (16) retains the simple-layer contribution of the nonconstant physical normalization. The criterion neither evaluates these sums nor asserts a nonzero third value.

## Dependencies and verification

Actual inputs are ACTUAL-UPPER-QUARTIC-IS-A-GRAM-COMPOSITE.md, ACTUAL-THIRD-SHADOW-AS-A-CANONICAL-VECTOR-COCHAIN.md, ACTUAL-CONE-DIAGONAL-IS-CANONICAL-RESIDUE-INVERSE.md, VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md, and the actual cubic quotient sequence from UNIVERSAL-CUBIC-EVEN-DEFECT-QUOTIENT-IS-TRIVIAL-V.md.

Run verify_twelve_point_polar_vector_shadow.py. It checks universal character multiplicities, the Gram determinant identity with independent indeterminates, the exact transvectant double-pole cancellation, the square directional-derivative kernel, and the line degrees. It uses no selected HM/source coefficients, actual-instance matrix or rank evaluation, parameter scan, local model experiment, or external write. The geometric conclusions about the actual maps are proved above.
