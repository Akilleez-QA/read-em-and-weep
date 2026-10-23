# A nested constant-annihilator obstruction excludes the source127 g-b edge

## Result and scope

The exact original source

    G3.11.cce6e3ba4eeb, source_index127,
    (0,1,0,0,0,0,1,0),
    E=(P+D) O(-2)+T O(-3)+W O(-9),
    A_q=O(-8)+O(2)+O(16),
    B_q=O(-18)+O(-4)+O(6)

cannot occur with its original maximal profile-(1,1). This is a whole-source exclusion, not an exclusion of every source at index127 or of its stable label.

The new step retains arbitrary couplings between the remaining blocks. It proves that two successive dual osculations have rank at least nineteen, whereas the original profile permits at most eighteen. Independence follows from two fixed constant projections and rank-nullity, not from adding ranks through a nonconstant extension. The exact twist-one character is compatible in the final branch; it is the maximal plateau condition that gives the contradiction.

No selected actual HM/source coefficients, parameters, points, derivative values, matrices, instance ranks, models, scans or large computation are used. All character checks are fixed universal identities.

## 1. Immutable inputs and actual conventions

The original actual presentation, strict-top theorem and both source catalogs are at commit db51525015bb7c5e825833d550d08dedf6f6ea96 of Akilleez-QA/read-em-and-weep, under

https://github.com/Akilleez-QA/read-em-and-weep/tree/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load

The manifest pins their exact bytes. They give a saturated full-span inclusion E in H O, where

    H=2A+2V+2P+2D, dim H=30,
    rank E=17, degree E=-54,
    Q=H O/E, rank Q=13, degree Q=54,
    H0(E^-(2))=0, H0(Q*)=0.

The original zero defect gives the actual saturated quotient

    A2=E^+/E=O(-6)+O(4)+O(18) subset Q.          (1)

The maximal plateau convention is the original actual-presentation note, Sections4-5. In particular profile-(1,1) says that Q* has first forward rank gain three and its next gain is at most two. Thus

    rank (Q*)^(++) <= 13+3+2=18.                (2)

The further immutable inputs are:

- PR859, commit 6129e92a26572779003f3295227f688b77ed881c, research/hm/profile11-o16-high-p-divisor/PROOF.md. Its theorem explicitly includes the g-b tuple and proves its high-P map basepoint-free.
- PR867, commit b2a12c98bc162062a938b7a7a6a90ab45786e340, research/hm/profile11-o16-cdf-kernels/PROOF.md, Section2. Its complete rank-three kernel classification uses only the fixed kernel characters, not the c-d-f internal target.
- PR885, commit 53939364de5459822be1a32be08f2b12dbbb4280, research/hm/profile11-source127-hbf-kernel-reduction/PROOF.md. We use its stated actual internal/external image principle, quadratic first-polar calculations, and the degree-38 obstruction in Section8. We do not transfer its scalar-tail theorem: every changed internal or endpoint channel is checked below.

Work over C with the binary icosahedral group G and its defining two-space W. Write A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and Wp,V,P for the other irreducibles of dimensions2,3,4. All irreducibles are self-dual. G has no nontrivial line characters. Every nonempty invariant effective divisor has degree at least twelve.

Superscripts + and ++ mean actual saturated forward transforms. When discussing generic osculating ranks, we may work over K=C(P1); saturation does not change these ranks. All projections used below are induced by constant subspaces, so commute with the ambient trivial connection.

## 2. All high-P kernels and the changed internal target

Put F=P O(-2). Its derivative maps only to O(16), since the negative row vanishes by degree and P is absent from Sym4 W. PR859 makes this map onto. Its kernel K0 has

    rank K0=3, degree K0=-24,
    H0(K0(2))=0,
    H1(K0(2))=A+V+P+D,
    chi_G(K0(3))=-(W+S+T).

The exhaustive classification in PR867 Section2 therefore gives exactly

    I. A O(-8);
    II. W O(-7)+O(-10);
    III. W O(-9)+O(-6);
    IV. Wp O(-3)+O(-18);
    V. O(-6)+O(-8)+O(-10).                       (3)

The actual internal target is now

    (E/F)(-2)=D O(-4)+T O(-5)+W O(-11).          (4)

Every component into the last term is zero. All source terms except O(-18) are too high by degree, and that last possible map would require W in Sym7 W=Wp+T. The complete remaining channels, all of multiplicity one, are:

    I: A(-8) to D(-4) or T(-5);
    II: W(-7) to D(-4), O(-10) to T(-5);
    III: W(-9) to D(-4) or T(-5);
    IV: O(-18) to D(-4) or T(-5);
    V: O(-8) to D(-4), O(-10) to T(-5).

The nonzero T maps in I and III are multiplication by the formal tautological l^3 and l^4 and are injective everywhere. The D map in I factors through the Euler quotient W(-7), followed by multiplication by l^3. In III it factors through the Euler quotient O(-8), followed by l^4. In II the W map is injective multiplication by l^3. The scalar O(-10) map to T(-5) is the complete quintic and is saturated. In IV the degree-fourteen D and degree-thirteen T covariants are saturated: a possible degree-twelve divisor would leave D in Sym2 W or T in Sym1 W, both absent. A nonzero pair is saturated as well. Images in distinct rows have their evident saturated direct sums.

Consequently the complete list of saturated internal images J is

    I: 0, W(-7), A(-8);
    II: 0, W(-7), O(-10), W(-7)+O(-10);
    III: 0, O(-8), W(-9);
    IV: 0, O(-18);
    V: 0, O(-8), O(-10), O(-8)+O(-10).           (5)

The saturated external line and internal image give actual exact sequences

    0 -> J -> I_F -> O(16) ->0,
    0 -> F -> M=F^+ -> I_F(2) ->0.               (6)

Quadratic first polars generate M(1), so its degrees are zero or minus one. A zero image, a sole O(-8), or a sole O(-10) gives positive degree M and is impossible. For J=W(-9) or O(-8)+O(-10), the constant coefficient of M is A, while its putative linear coefficient is Wp+T-S, not a genuine representation. Thus III and V disappear. The only surviving possibilities are

    J=W(-7): M=(V+P) O;
    J=A(-8) or W(-7)+O(-10): M=(Wp+T) O(-1);
    J=O(-18): M=T O(-1).                         (7)

These polar identities are exactly the fixed computations in PR885 Section2, with (4)-(5) separately justified here.

## 3. The nonconstant first spans are impossible

We recall the endpoint-specific obstruction used here. If an actual constant c-space C has X=E intersect C of rank c-2 and degree -38, and C/X is an extension of O(20) by the saturated O(18) in (1), then this is impossible for source127. Indeed the projected E/X has rank19-c, degree-16 and full span H/C. The shared-cokernel saturation defect delta satisfies

    30-c <= h0((E/X)^*_sat)=35-c-delta,

so delta<=5 and invariance forces delta=0. PR885 Section8 then computes the dual quotient R to have H1(R)=D and chi_G(R(3))=-W+Wp+S+4T. The complete single-D budget forces R=(2Wp+T)O(-1)+O(-6). Its top two Wp copies contradict the original strict-top injection

    H0(Q*(1)) -> H0(B_q(1))=Sym7 W=Wp+T.        (8)

This argument depends on the original Q presentation and B endpoint, which are identical here, not on the lower source-tail splitting.

For either rank-eight case in (7), first polars give M=P W O(-1). Its full constant span is C=P+D of dimension nine or C=V+P+D of dimension twelve. The actual N=E intersect M has

    N/F=A O(-6),               in case I;
    N/F=W O(-5)+O(-8),         in case II,
    rank N=7, degree N=-26.                       (9)

If dim C=9, then C/M=O(8), M^-=(V+P)O(-2). Were N contained in M^-, equal rank and saturation inside M would give equality, forcing an absent V(-2) coefficient in E. Otherwise differentiating N supplies C/M and saturation puts C inside E^+. Its lower rows vanish: on M they factor through M/F=P O, and on C/M=O(8) they vanish by degree. Thus E intersect C has rank8 and degree-18. Its degrees are at most-2, forcing a degree-minus-two coefficient of dimension6 or7. Neither is a subrepresentation of the multiplicity-free top P+D. This excludes dim C=9.

For dim C=12, the complete quadratic Euler sequences give

    M/F=P O, C/M=P O(2), M^-=F,
    beta_M: M/F -> (C/M)(-2) is an isomorphism.

Taking the first span of (9) gives a saturated Y=N^+ with

    Y/M=A O(-4),               in case I;
    Y/M=W O(-3)+O(-6),         in case II;
    rank Y=11, degree Y=-20, C/Y=O(20).           (10)

C cannot lie in E^+. Its lower rows would then factor through P O(2) and vanish, leaving a rank11 degree-18 kernel inside E, impossible when all degrees of E are at most-2. Therefore E^+ intersect C=Y. In case I both lower rows of Y vanish: A is absent from Sym8 W, and the negative target is too low. Thus X=E intersect C has rank10 and degree-38, contradicting the recalled obstruction.

In case II the O(4) row vanishes because W is absent from Sym7 W and Sym10 W has no invariant. The possible negative row from the scalar O(-6) in (10) is also zero here, unlike the scalar-tail source of PR885. To see this on the actual connection, its preceding scalar O(-8) in N/F=J(2) maps into E/F only through T O(-3). It has no map to D O(-2), since D is absent from Sym6 W, and no map to W O(-9) by degree. The original negative O(-8) derivative row of T O(-3) is zero by degree. The negative row of Y/M is precisely this induced derivative of N/F, so it vanishes. Again X has rank10 and degree-38, impossible. This checks the missing endpoint interface rather than merely suppressing an allowed scalar O(-6) map.

Finally consider M=T O(-1) in case IV. Its full constant span is C=V+D, of dimension eight. The complete cubic Euler sequences tensored with Wp give M^-=F, M/F=Wp O(1), C/M=Wp O(3), and beta_M is an isomorphism between those quotients after twisting by -2. Here N/F=O(-16), and Y=N^+ satisfies

    Y/M=O(-14), rank Y=7, degree Y=-20, C/Y=O(20).

If C lay in E^+, its lower rows would vanish. Then (E intersect C)/F would have rank3 and degree-10 inside D(-2)+T(-3)+W(-9). It has no degree-minus-two coefficient, since no representation of dimension at most3 maps to D. Its possible degree-minus-three coefficients W,Wp map neither to T at equal degree nor to D(-2), since D W=S+T. Its degrees would all be at most-4, contrary to degree-10. Thus E^+ intersect C=Y. The lower rows of Y factor through O(-14) and would require invariant scalar degrees18 and8, both absent. This is the rank6 degree-38 contradiction. Every nonconstant M in (7) has now been excluded.

## 4. The remaining constant first span yields an actual constant ten-space

Suppose M=(V+P)O, of dimension seven. Its image in Q is exactly L=O(18). For N=E intersect M, equation (6) gives N/F=W O(-5). This quotient maps into E/F only through D O(-2): the T component would require W in T Sym2 W=Wp+S+2T, and the W(-9) component vanishes by degree. Its unique D map is multiplication by l^3, with quotient A O.

Because M/N=L is saturated in Q, projection by the constant M gives a saturated full-span inclusion

    E/N=A O+T O(-3)+W O(-9) subset (H/M) O.

The A O summand is an actual constant subspace, because its sections in a trivial bundle are constant. Its inverse image defines a constant ten-space

    C0=A+V+P subset H,
    F0=E intersect C0=(P+D) O(-2),
    C0 O/F0=L=O(18) saturated in Q.               (11)

These equalities follow from the actual projections: the A quotient is exactly D(-2)/W(-5), so its inverse image in E is the full top F0. No horizontal splitting of E has been presumed.

Let Hbar=H/C0. Projecting again gives

    Z=T O(-3)+W O(-9) subset Hbar O,
    Hbar=A+V+P+2D, dim Hbar=20.                  (12)

Z is saturated and has full constant span. Its raw derivative image is O(2)+O(-8): (11) removes exactly the saturated high quotient L, and constant projection commutes with the connection. Write R=T O(-3) and N0=W O(-9) for its original direct summands.

## 5. The T block and its actual constant span

The R->O(2) row is nonzero. Otherwise R has no external derivative by degree, and its internal derivative toward N0(-2)=W(-11) is also zero, making a negative bundle horizontal in a constant bundle. The nonzero row is the complete quintic T system, onto with kernel D(-4). Its internal derivative toward N0(-2) is zero by degree. Repeating this complete-kernel argument gives the actual saturated chain

    O(-8), W(-7), A(-6), S(-5), D(-4), T(-3),

each the first span of the preceding term. At every step a zero derivative would make the preceding negative bundle horizontal; the only nonzero complete symmetric-power map gives exactly the stated kernel. The constant span of the initial line is a quotient of Sym8 W=P+D and contains the rank-six last term. Every proper subrepresentation of P+D has dimension at most five. Thus the constant span is the full

    C=Sym8 W=P+D subset Hbar,
    R=U5^8 subset C O,
    C O/R=A O(6).                               (13)

Here U_k^n is the universal subbundle l^(n-k) Sym^k W in Sym^n W O. Its exact formulas are

    U_k^n=Sym^k W O(k-n),
    (U_k^n)^+=U_(k+1)^n,
    (Sym^n W O)/U_k^n=Sym^(n-k-1) W O(k+1).      (14)

They follow directly from the Euler filtration and differentiation of the formal power l^(n-k); the coefficient n-k is nonzero in characteristic zero. The annihilator of U_k^n is U_(n-k-1)^n in the dual constant space, using the invariant self-duality of Sym^n W.

## 6. The projected Euler plane is exactly the standard saturated plane

Let pi:Hbar O -> D0 O be constant projection by C, with

    D0=Hbar/C=A+V+D, dim D0=11.

First pi on N0 has generic rank two. Rank zero contradicts the full span of Z. If its generic rank were one, its coherent image would be an equivariant line O(e) with e<=0, and the onto map W O(-9)->O(e) would require W in Sym^(e+9) W. Center parity and the odd symmetric powers up to degree nine leave only e=-8: Sym1=W, Sym3=S, Sym5=T, Sym7=Wp+T, Sym9=S+T. Thus its kernel would be O(-10), mapped into C by the original N0. Its map into C/R=A O(6) vanishes because A is absent from Sym16 W. It would therefore lie in R, contrary to the direct-sum injection R+N0=Z. Generic rank one is impossible.

Consequently pi:N0->D0 O is an injection of sheaves with coherent image N isomorphic to W O(-9). This does not yet assert saturation. The negative external row of Z is supplied only by N0; it is a nonzero complete Euler map

    W O(-9) -> O(-8), with kernel K0=O(-10).

Write K for the projected K0 inside N. It is a nonzero line map into D0 O and has no zero divisor, since an invariant divisor would have degree at most ten. It is not a constant projective line: D0=A+V+D has no trivial constituent, so the nonzero constant coefficient span of K has dimension at least three.

The derivative of K lands in N as a coherent image, not just generically. Indeed the negative external derivative of K0 is zero by definition, and the entire positive derivative quotient O(4) is supplied inside C by R^+/R. The actual inverse image of that quotient is Z+R^+. Thus differentiating K0 lands in Z+C, whose constant projection has exactly coherent image N.

Modulo K the derivative is a map

    K=O(-10) -> (N/K)(-2)=O(-10).

It is nonzero, since otherwise K would define a constant projective line. Hence it is an isomorphism. The raw first-polar sheaf of K is exactly N: it contains K and surjects onto N/K everywhere. This is equality of coherent lattices, with no saturation inference from generic rank.

The constant span of N is all D0, because Z has full span and pi(R)=0. The constant span of a line and its first polar coincide, so K also spans D0. Its degree-ten coefficient map Sym10 W->D0 is therefore onto, and both dimensions are eleven. It is an equivariant constant isomorphism. Thus K is the complete degree-ten line and N is its universal first polar:

    K=U0^10, N=U1^10 subset D0 O.                (15)

In particular N is now proved saturated, by the explicit standard Euler sequence. Equations (13)-(15) give actual exact sequences of bundles

    0 -> C O/R -> Qbar=Hbar O/Z -> D0 O/N ->0,
    C O/R=A O(6), D0 O/N=(P+D) O(2).             (16)

To justify the first kernel, pi on N0 is injective, so Z intersect C=R. The saturation of N makes the right quotient locally free; equivalently C/R is saturated in Qbar.

## 7. Constant projection, not split-model rank additivity

We state the elementary connection lemma used to control arbitrary extensions. Work over K=C(P1), choose any local derivation d/dz, and for a K-subspace B of a constant vector space set

    Osc_j(B)=span_K { derivatives of order at most j of local sections of B }.

This is independent of the chosen local frame. It is the generic fiber of the j-fold forward transform. If A is a subspace of B, then Osc_j(A) is contained in Osc_j(B). If pi is a constant linear projection, then

    pi(Osc_j(B))=Osc_j(pi(B)).                   (17)

One inclusion follows by commuting pi with differentiation. For the other, every rational section of pi(B) has a rational lift in B; differentiating the lift proves the reverse inclusion. If A is also contained in the constant kernel of pi, then all its derivatives stay in that kernel. Rank-nullity therefore gives

    dim Osc_j(B) >= dim Osc_j(A)+dim Osc_j(pi(B)). (18)

No extension splitting is involved. The counted subspaces are independent because the first lies in a fixed constant kernel while the second is measured in its quotient.

Dualizing (16), with actual constant restriction to C*, gives

    0 -> R1=(D0 O/N)* -> R0=Qbar*
      -> (C O/R)* ->0,
    R1=U8^10 subset D0* O=ker(Hbar* O -> C* O),
    image(R0 -> C* O)=U2^8=A O(-6).             (19)

Both displayed inclusions and the image are the actual ones, not just splitting types: the right-hand image is the annihilator of R=U5^8, while R1 is the annihilator of N=U1^10. The induced second fundamental forms are restrictions/projections of the trivial connections, and hence are the standard forms from (14). Applying (18) at j=2 yields

    rank R0^(++) >= rank U10^10+rank U4^8
                  =11+5=16.                    (20)

Thus the two residual second directions cannot cancel through any coupling: the full eleven-space on the left is in the fixed kernel of restriction, and the five-space on the right is its projected image.

The saturated line L in (11) similarly gives

    0 -> R0=Qbar* -> Q* -> L*=O(-18) ->0,       (21)

where R0 lies in the fixed constant annihilator (H/C0)* O and the image in C0* O is precisely the quotient-curve line L*. That curve has full coefficient span C0*: dualizing 0->F0->C0 O->O(18)->0, the coefficient map C0->H0(O(18)) is injective because H0(F0)=0. Its ten-dimensional coefficient system has a generic second osculating space of dimension three. Indeed, in characteristic zero, three linearly independent rational coordinate functions have a nonzero Wronskian; if all value/first/second minors vanished, the entire coefficient system would have dimension at most two. This is a universal generic argument, not evaluation at a chosen point.

Apply (18) again to (21) and the constant restriction to C0*. Equations (20)-(21) give

    rank (Q*)^(++) >=16+3=19,                   (22)

contrary to (2). This proves the whole g-b exclusion with all couplings retained.

## 8. Twist-one compatibility and the precise obstruction boundary

The final branch is not already ruled out by the fixed twist-one character. As ordinary equivariant bundles, (19) splits because H1(A(P+D)O(4))=0, and (21) then splits because H1(R0(18))=0. Therefore it would have

    Q*=(P+D)O(-2)+A O(-6)+O(-18).

This statement is only about bundles, not about the ambient connection. It gives exactly the original characters

    H1(Q*)=A+2V+3P+4D,
    chi_G(Q*(1))=-W-2S-3T.

Thus the early character test leaves this branch intact. The obstruction is instead (22), forced by the actual nested constant annihilator flag and the original maximal-profile endpoint. A constant direct-sum construction with these three blocks indeed has second dual gain three rather than two; it is not a realization of the exact source127 profile. No claim about the separate c-d-f abstract family follows.

The finite verifier checks all changed channel vanishings, kernel/polar characters, the fixed source identity, the positive/negative endpoint characters and both numerical rank bounds. The actual coherent-image, saturation, connection and independence arguments are the proof above.
