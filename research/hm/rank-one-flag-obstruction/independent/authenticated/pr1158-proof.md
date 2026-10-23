# The two remaining forced P targets have a rank-one scalar endpoint

## Statement and exact scope

Work over C on the physical binary-icosahedral line with G=SL2(F5), standard doublet W and the other doublet W'. Let E be the ACTUAL saturated primary bundle in the constant thirty-dimensional ambient bundle, let K=E^- and A=E/K, and assume

    E=P O(-2)+(W'+T)O(-3)+V O(-4)+W' O(-5),
    A=W' O(-r)+O(16),    r in {3,5}.

Assume the actual maximal rank-three plateau has k=1 (in particular the maximal profile (1,1) satisfies this). The theorem is source-conditioned: it does not select P as the actual source in any unconditioned case.

Then the actual derivative beta_K has rank ONE, and its coherent image in A(-2) is exactly the displayed saturated scalar line O(14). In particular, for L=K^- there is an actual exact sequence

    0 -> L -> K -> O(14) -> 0,
    rank L=13,  deg L=-84+2r,  maxdeg L<=-4.

The evaluated cubic top C=W'O(-3) maps surjectively onto O(14), with line kernel O(-20). Thus O(-20) is saturated in L and L/O(-20) is isomorphic as an equivariant ordinary bundle to N=K/C, a rank-twelve bundle of degree -64+2r with maxdeg N<=-4. The next actual derivative of L lands in O(12), so has rank at most one. It is nonzero because a nonzero negative saturated bundle in a constant bundle cannot be horizontal.

These are new actual-map restrictions. Neither target is excluded by this theorem. This is not a complete original proof repair, a live frontier count, a claim of realization, or a new experiment.

## 1. Pinned inputs and forced cubic top

INPUTS.json records immutable public originals, including PR1153 at4b97c71dace666dd5bf39e0128abbe7b01a2f056, PR1155 at076d2fb4e6abec42bd365bb32318b89d8ece400f, and the original actual plateau and strict-top sources atdb51525015bb7c5e825833d550d08dedf6f6ea96. Full bytes are retained. The actual plateau source Section5 gives rank beta_K in {1,2} at k=1. This is not the assumption that its rank remains three.

PR1153 proves cubic vanishing implies genuineness of

    H0(A(2))+chi_G(A(4))-(3V+3P+2D).

For either target in the statement, this virtual character has V coefficient -1. Therefore cubic vanishing is impossible. The P cubic alternative is exactly W', and strict-top gives maxdeg K<=-3. Equivariant ordinary splitting then gives

    K=C+N,  C=W'O(-3),  rank N=12, maxdeg N<=-4.

Here C is the canonical highest-degree evaluated subbundle; a complement is noncanonical and is NOT horizontal. Since deg A=16-2r and deg E=-54,

    deg K=-70+2r,   deg N=-64+2r.

For each of the twelve ordinary degrees n_i of N, the other eleven are at most -4. Therefore

    n_i >= deg N+44=-20+2r.

All ordinary degrees of K are consequently at least -20+2r: at least -14 when r=3, and at least -10 when r=5. This elementary lower bound uses exactly the forced cubic multiplicity, not an unsupported lower slope bound for a general subbundle.

## 2. The cubic top fills the scalar line with no base divisor

The actual derivative of K lands in A(-2)=W'O(-r-2)+O(14), because the derivative of E kills K. Its restriction to C has zero doublet component: the degree difference is 1-r<0. Strict-top implies this restriction is nonzero, since it is injective on the nonzero coefficient representation H0(K(3))=W'. Hence C maps nontrivially to O(14).

Write its coherent image as O(14)(-D), where D is an invariant effective divisor of degree b. G is perfect, so there is no additional character on this line. A nonzero equivariant morphism W'O(-3)->O(14-b) requires W' in Sym^(17-b) W. The first W' occurrence is degree7, so 0<=b<=10. Every nonempty projective A5 orbit has at least12 points. Thus D is empty and this map is surjective as a sheaf, not just generically nonzero. Its kernel has degree -6-14=-20 and is O(-20).

Let I be the coherent image of beta_K. It contains the entire displayed O(14) as a subsheaf. Since the target splits, its projection to the doublet B0=W'O(-r-2) has image J and, sheaf-theoretically, I=O(14) direct-sum J inside O(14) direct-sum B0: locally any lift of a section of J can have its scalar component subtracted using the contained scalar summand. No choice of a horizontal splitting is involved.

If rank I=1, then J=0 and I=O(14) exactly. If rank I=2, then J is a coherent line O(e) injecting into B0, not initially assumed saturated. The induced map K->J is a sheaf surjection. At least one splitting block of K maps nontrivially to O(e), so e>=min degree K>=-20+2r. Equivariance of J->B0 requires W' in Sym^(-r-2-e)W, giving e<=-r-9. The central involution also makes e even. These inequalities apply to the COHERENT image, without discarding any torsion in B0/J.

## 3. The rank-two alternative is impossible

For r=5 the inequalities give simultaneously e>=-10 and e<=-14. This is impossible.

For r=3, they give -14<=e<=-12 with e even. The candidate e=-14 would require W' in Sym9 W=S+T, which does not occur. Thus only e=-12 remains. Its map to W'O(-5) is a degree-seven W' covariant. It is in fact saturated (a common divisor would have degree at most7, below the minimum invariant orbit12), but the following argument needs no saturation assertion.

Suppose r=3 and I=O(14)+O(-12). Put L=ker beta_K. It is saturated in K and in the constant ambient, and strict-top gives maxdeg L<=-4. The actual derivative of L lands in (K/L)(-2)=I(-2). Applying strict-top to L gives H0(L^-(4))=0, hence an injective coefficient map

    H0(L(4)) -> H0(I(2)).

From 0->L->K->I->0 and 0->K->E->A->0, the character

    Q=H0(I(2))+chi_G(A(4))+chi_G(I(4))-chi_G(E(4))

must be genuine: it equals coker[H0(L(4))->H0(I(2))]+H1(L(4)). All Euler terms are signed and include H1. At r=3,e=-12 these terms are

    H0(I(2))=Sym16 W,
    chi(A(4))=P+Sym20 W,
    chi(I(4))=Sym18 W-Sym6 W,
    chi(E(4))=3V+3P+2D.

Their difference is

    Q=1+2 A_std+3D+P-V.

Its V multiplicity -1 is impossible. Therefore rank I cannot be two in either target; it is exactly one and equals O(14).

## 4. Consequences and remaining boundary

Degree and rank additivity now give rank L=13 and deg L=-84+2r, namely -78 for r=3 and -74 for r=5. The cubic kernel O(-20)=ker[C->O(14)] lies in L. Since C->O(14) is surjective, the snake lemma for C subset K gives

    0 -> O(-20) -> L -> K/C=N -> 0.

Thus its inclusion in L is saturated. This extension is not asserted to split: Ext1(N,O(-20)) can be nonzero. In particular one must not infer a top degree -20 for L or a displayed splitting compatible with the connection. The next derivative of L lands in (K/L)(-2)=O(12). Its rank is at most one, and cannot be zero: zero derivative would make L horizontal and hence constant, contrary to maxdeg L<=-4. Its coherent image could be O(12)(-D') for an invariant divisor D'; this theorem does not remove D' or determine the next kernel.

For comparison, the same necessary quartic envelope for the now forced rank-one image is genuine: it is 1+2A_std+3D+2P when r=3, and 1+2A_std+3D+P when r=5. Thus the rank-two contradiction does not silently exclude the rank-one branch. Further actual-map analysis of that branch remains necessary.

## Reproducibility

The accompanying verifier authenticates complete immutable inputs, checks the character ring controls, first occurrence and degree/parity bounds, the only rank-two candidate and its exact signed negative witness, and rank-one degree and character consequences. Run python3 verify.py and python3 -O verify.py; both outputs must equal RESULT.json. The elementary computations support the written geometric proof but do not replace the actual-map and saturation arguments. No actual HM coefficient, point, parameter, jet, instance matrix, rank test, source scan, historical enumeration or stopped experiment is used.
