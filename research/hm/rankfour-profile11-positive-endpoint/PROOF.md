# The short-profile endpoint derivative is onto its full positive rank-three image

## 1. Exact conditional result

Work in the actual rank-four maximal ordered profile (1,1), on the original physical binary-icosahedral parameter line P(W*) over C, and assume max ordinary degree of the primal quotient is three. Retain the actual geometric and source hypotheses of PR1188 at 518b3f2686269f83e4f788fe4ed30d0e36dac37b. That theorem gives the actual quotient and source

    0 -> K -> E -> A_q -> 0,
    E=D O(-2)+(W'+T6)O(-3)+V O(-4)+O(-8),
    A_q=W O(3)+O(2)+O(-8),

and exactly three necessary kernel shapes

    K_T=S4 O(-3)+V O(-4)+T6 O(-5),
    K_W=S4 O(-3)+(V+P)O(-4)+W' O(-7),
    K_1=S4 O(-3)+(V+D)O(-4)+O(-10).

K is saturated in the original constant thirty-space, has rank13 and degree-54, and its actual derivative beta_K has generic rank at most three. It factors through

    beta_K:K -> (E/K)(-2)=W O(1)+O+O(-10).             (1)

We prove the stronger actual image statement

    im beta_K = W O(1)+O,                              (T1)

where this is the full positive subbundle displayed in (1), with equality as coherent sheaves at every parameter. In particular the O(-10) component vanishes; the derivative has rank exactly three everywhere, not just generically; and

    0 -> K^- -> K -> W O(1)+O -> 0,
    rank K^-=10, deg K^-=-56.                          (T2)

The actual forward transform is also identified:

    K^+=E0=D O(-2)+(W'+T6)O(-3)+V O(-4),
    rank E0=16, deg E0=-46, E0^-=K.                    (T3)

The adjacent actual rank-three quotients K/K^- and E0/K are W O(1)+O and W O(3)+O(2), and the derivative between them after the cotangent twist is an isomorphism. This is an unramified step in the actual Gauss filtration, not a horizontal splitting.

No K type is selected or excluded by this theorem. Neither the top-three boundary nor the full rank-four profile is closed. There is no new global rank bound, square-surjectivity or original-repair conclusion.

All eleven full immutable inputs are retained in INPUTS.json with the same authenticated identities as the preceding packets. The top-three theorem above and the invariant-orbit original at db51525015bb7c5e825833d550d08dedf6f6ea96 are the additional inputs needed here. This proof does not need the separate matched-graph theorem as a premise: it rederives the V-row information directly from the published top-three theorem and uses capacity only on actual kernels inside the constant ambient.

Our notation is A_std=Sym2 W, S4=Sym3 W, D=Sym4 W, T6=Sym5 W, with V the other three-space, P the even four-space, and W' the other doublet. All ordinary splittings used below are equivariant bundle splittings, never assumed compatible with the constant connection.

## 2. An invariant-base-divisor observation

For an equivariant nonzero map R O(-d)->O, its coefficient sections have common zero divisor invariant under the projective A5 action. This divisor has degree at most d: it is bounded by the zero divisor of any nonzero coefficient section. Every nonzero effective invariant divisor on the physical line has degree at least twelve, because the projective orbit sizes are12,20,30,60. Thus if d<12, any such nonzero row is everywhere onto O.

The same argument applies to the maximal minors of an equivariant map R O(a)->S O(b). If the map has the desired generic rank, some minor is nonzero; their common zero divisor is invariant. When every minor is a section of a line bundle of degree below twelve, their common divisor is zero. On the smooth curve this means the minors generate the unit ideal, so the map has full rank everywhere. This is a universal argument about a map's base divisor, not a choice or evaluation of an actual minor.

## 3. The actual V-row is everywhere onto W O(1)

Each possible K has a V O(-4) block. The near-top coefficient lemma from the preceding theorem makes its ACTUAL derivative nonzero. For completeness, if a nonzero coefficient line O(-4) inside that block were killed by beta_K, its derivative would land in (K/O(-4))(-2), whose top degree is at most-5. The internal Hom is zero, making this saturated negative line horizontal in the constant ambient, a contradiction. Thus no nonzero coefficient vector in the degree-minus-four block is killed.

The V-row has no scalar O component because

    Hom_G(V O(-4),O)=Hom_G(V,Sym4 W)=Hom_G(V,D)=0.

Its O(-10) component vanishes by ordinary degree. Therefore it is a nonzero map

    f:V O(-4) -> W O(1).                              (2)

If its coherent image had rank one, it would be an equivariant line bundle O(e). As a quotient of V O(-4), it has e>=-4; as a subsheaf of W O(1), it has e<=1. But every relevant Hom is zero:

    Hom_G(V O(-4),O(e))=Hom_G(V,Sym^(e+4) W)=0,
    -4<=e<=1.

Indeed the symmetric powers through degree five are 1,W,A_std,S4,D,T6, none equal to V. There is no additional line character because G is perfect. Hence f has generic rank two.

Its two-by-two minors have degree ten: their source is wedge2 V O(-8) and their target is det(W O(1))=O(2). At least one minor is nonzero. Their common zero divisor is invariant and has degree at most ten, hence is empty by Section 2. Consequently

    f is everywhere onto W O(1).                       (3)

In particular the actual coherent image of beta_K already contains this entire subbundle, including at ramified parameters. We have not replaced an actual image by its saturation.

## 4. The two scalar projections are controlled globally

Let p0 and p_-10 be the projections of beta_K to O and O(-10).

Every potentially nonzero irreducible source row of p0 is one of

    S4 O(-3), T6 O(-5), W' O(-7), D O(-4).

The V and P degree-minus-four rows have zero Hom to O because Sym4 W=D. The O(-10) row also has zero Hom to O, since

    Sym10 W=A_std+D+V

has no invariant. A nonzero p0 therefore has a nonzero row of degree3,4,5 or7. Each such row is everywhere onto by Section 2. It follows that p0, if nonzero as a morphism, is globally onto O.

The projection p_-10 vanishes automatically for K_T and K_W. For K_1 it can come only from the single O(-10) summand, through a constant scalar. Hence p_-10, if nonzero, is everywhere onto O(-10).

Both scalar projections cannot be nonzero. The V block already spans W O(1). The p0 row is supported on the complement of the O(-10) tail, whereas p_-10 vanishes on that complement and is nonzero on the tail. At the generic point these supply two independent further directions, so beta_K would have rank at least four. This contradicts its endpoint bound of three.

Thus there are precisely three structural alternatives before the next capacity test:

    p0=0, p_-10=0:             im beta_K=W O(1);
    p0=0, p_-10 nonzero:       im beta_K=W O(1)+O(-10);
    p0 nonzero, p_-10=0:       im beta_K=W O(1)+O.       (4)

The equalities are coherent-sheaf equalities everywhere, not just generic images. They follow by (3) and the corresponding onto scalar projection: lift the scalar component locally, then correct its W component using the surjective V row.

## 5. A rank-two image violates the actual kernel capacity

Assume the first alternative in (4). Let F0=K, F1=K^-, and continue actual derivative kernels inside the original constant ambient. Then

    C=F0/F1=W O(1), rank F1=11, deg F1=-56.

Outward derivative ranks are at most two. The negative kernel chain terminates, and its coherent successive quotients inject into C(-2j), exactly as in the previously proved endpoint capacity argument. Writing the two column heights h1>=h2>=0 with h1+h2=11 gives

    deg F1 <= 11-h1(h1+1)-h2(h2+1) <= -61,

because the minimum quadratic cost is72 at (h1,h2)=(6,5). But deg F1=-56. This contradiction excludes the rank-two image.

This capacity is applied to the actual K^- subbundle of the original constant ambient. It is not applied to K/U or an induced quotient map lacking a flat connection.

## 6. The negative scalar image also violates actual kernel capacity

Assume the second alternative in (4). Then

    C=K/K^-=W O(1)+O(-10),
    rank K^-=10, deg K^-=-46.

Now the actual subsequent derivative ranks are at most three, so all three columns must be retained. For heights h1>=h2>=h3>=0 with total ten, write z=h3. The capacity expression is

    h1+h2-10z-sum hi(hi+1)
      = -11z-h1^2-h2^2-z^2
      <= -11z-(10-z)^2/2-z^2
       = -50-z-(3/2)z^2 <= -50.

This contradicts deg K^-=-46. No third-height possibility has been discarded; the bound holds for every z>=0. It excludes the entire negative-only alternative, not merely the two-column subcase.

Only the third alternative in (4) remains. Since its scalar projection is onto everywhere, this proves (T1) and the exact sequence (T2). In particular generic rank three has been promoted to everywhere rank three by explicit image arguments, not inferred merely from a rank count.

## 7. Identify the actual forward transform and adjacent graded step

The positive image in (T1) is saturated in A_q(-2). By the definition of the saturated forward Gauss transform, K^+/K is exactly its twist by two, the positive subbundle W O(3)+O(2) of A_q. Its preimage in E is the kernel of the actual O(-8) quotient coordinate.

That coordinate can only come from the single source O(-8), with nonzero scalar coefficient. Thus its kernel is precisely the source subbundle

    E0=D O(-2)+(W'+T6)O(-3)+V O(-4),

and K^+=E0. This subbundle is saturated in E and in the original constant ambient. Its rank is16 and degree-46.

The derivative of E0 kills K because derivatives of K lie in K^+=E0. Conversely the projection of beta_E0 to Q(-2) is the restriction of beta_E to E0. The latter has kernel K, since beta_E has kernel K and K is contained in E0. Therefore the actual derivative kernel of E0 is exactly K, proving E0^-=K and its generic rank three.

The two actual rank-three quotients are

    K/K^-=W O(1)+O,
    E0/K=W O(3)+O(2).

The induced derivative from the first into the second twisted by -2 is the image isomorphism already proved in (T1). Its determinant defect is zero. These statements identify an actual unramified rank-three step inside the original rank-four configuration. They do not invoke a horizontal Birkhoff decomposition or apply any separate rank-three theorem whose central source had different rank and degree.

## 8. Contribution and limits

The three necessary K forms all obey the same stronger actual image theorem: neither derivative rank two nor the possible negative tail can occur, and the full positive target is attained everywhere. The next actual kernel and forward transform now have exact ranks, degrees and quotient identifications, ready for subsequent structural work.

The separate matched-graph and defect results are compatible but are not used to assume a descended connection on K/U. The only iterated capacities here concern genuine saturated derivative kernels in the original constant ambient.

All three original K forms remain necessary possibilities until separately excluded; no original determinant value is selected here. The top-three boundary and the full rank-four (1,1) profile remain open. No coarse rank label, global rank bound, square-surjectivity, full-adjoint, smoothing, algebraicity or original-repair conclusion changes.

No selected actual coefficients, points, parameters, jets, tensors, instance matrices/ranks, historical enumeration or broad search is used. The calculations check only fixed representation identities, minors' degrees and universal height inequalities. Original actual/source premises remain imported, not certified merely by hashes or arithmetic.
