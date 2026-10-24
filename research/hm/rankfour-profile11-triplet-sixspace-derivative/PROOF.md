# The actual six-space derivative forces a W'(-1) image and an O(14) quotient

## Statement and retained boundary

Retain the complete actual-geometric hypotheses and conclusions of PR1207, in the original rank-four maximal ordered profile (1,1), its source and section gates, and precisely the full-positive coherent-image branch

    A_q=A(4)+O(-8),  A=Sym2 W,  im beta_K=A(2).

In the genuine constant ambient C, let V18 subset C* be the actual fifteen-dimensional coefficient span of the degree-eighteen scalar curve, let N=ann(V18) of dimension six, and let

    G0=E0 intersect N O=V(-4),
    S=ann_(N)(G0) subset N* O,
    u=O(-10) subset N* O

be respectively the actual kernel of restriction E0->F18, its local dual annihilator, and the projected degree-ten scalar curve. Then:

1. G0 spans N=A+V. Its actual derivative has rank two, and

       S^-=u,
       S/u=W'(-1),
       im beta_G0=W'(-1) everywhere,
       H:=G0^-=O(-10).

2. The actual derivative image of G0 is saturated in E0/K=A(4), giving

       0 -> W'(-1) -> A(4) -> O(14) -> 0.

3. The original actual kernel satisfies K intersect G0=H, and restriction gives

       0 -> K/H -> F18 -> O(14) -> 0,
       rank(K/H)=12,  deg(K/H)=-48.

4. The local dual annihilator has abstract equivariant splitting S=V(-4). This does not identify its actual inclusion in N* with G0's inclusion in N, or identify the primal line H with the dual projected line u.

These are necessary actual-map conditions, not realization claims. Neither of the two PR1207 alternatives for F18 is excluded. No whole K splitting, triplet quotient, maximal profile, or full-positive branch is excluded or realized. The original defect t=0 is unchanged; the other coherent endpoint images of PR1199 remain separate. No actual coefficient, parameter, point, jet, tensor, matrix, or relative normalization is selected or evaluated.

## 1. Immutable inputs and retained actual subbundles

INPUTS.json records the complete immutable source files and their exact commits, paths, Git blobs, byte lengths, and SHA256 hashes. The principal input is PR1207 at commit af136934955f1bcc700ee768e2debb983e75451d, path research/hm/rankfour-profile11-triplet-shared-d-gluing/PROOF.md, whose complete proof has SHA256 7043302b3fb672f02777d44aac67e4579ac3421bc9cad66af3655a503d2b6bb7. The retained actual derivative data come from PR1205 at commit 97dad5c307a04f61d850e8a4211559e97ed4c2fd, path research/hm/rankfour-profile11-triplet-positive-span/PROOF.md. The physical representation and equivariant splitting conventions are those of ACTUAL at commit db51525015bb7c5e825833d550d08dedf6f6ea96, path research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md. Their transitive actual-geometric hypotheses remain assumptions. No rank-seventeen theorem is transferred to E0 or G0.

Work on the physical binary-icosahedral line P(W*) over C, with G=SL2(F5) and the fixed determinant convention. PR1207 gives the actual restriction sequence

    0 -> G0 -> E0 -> F18 -> 0,
    G0=V(-4),
    E0=D(-2)+(W'+T6)(-3)+V(-4).                       (1)

Here F18 is the first-jet annihilator in V18* O, and its inclusion there is saturated. Set

    N=ann(V18) subset C,
    dim N=6,  N=A+V.

The map E0->F18 in (1) is restriction to V18. Thus G0 is the actual, fiberwise intersection

    G0=E0 intersect N O.                              (2)

It is also the actual degree-minus-four subbundle in the projected degree-ten first-jet annihilator R in N O. The reviewed gluing theorem gives

    R/G0=O(-6).

Let

    S=ann_(N)(G0) subset N* O,
    u=O(-10) subset N* O,
    m=P^1(O(10))*=W(-9) subset N* O,

where u and m are the actual projected degree-ten line and its first jets in N*=V10/D. They are saturated, and u has full constant coefficient span N*. Duality gives

    u subset m subset S,
    S/m=O(6).                                       (3)

The original actual derivative quotient remains

    K=E0^-,
    E0/K=A(4),  A=Sym2 W.                            (4)

The intrinsic derivative conclusion is

    rank beta_G0=2,
    S^-=u,
    S/u=W'(-1),
    im beta_G0=W'(-1) everywhere,
    H:=G0^-=O(-10).                                 (5)

The target in the fourth statement is the actual subbundle (S/u)*(-2) in (N/G0)(-2), not an abstract replacement of a coherent image by its saturation.

Moreover restriction to E0 gives exact sequences

    0 -> W'(-1) -> A(4) -> O(14) -> 0,              (6)
    K intersect G0=H,
    0 -> K/H -> F18 -> O(14) -> 0,
    rank(K/H)=12,  deg(K/H)=-48.                     (7)

The line H subset N O in (5)-(7) and the line u subset N* O in (3) are different actual subbundles in different constant ambients. Both are abstractly O(-10), but this proof neither identifies them nor chooses a self-duality of N.

## 2. The constant-intersection bridge is fiberwise and saturated

The restriction C O->V18* O has constant kernel N O. Its restriction to E0 has image exactly the saturated F18, and is everywhere onto that bundle by (1). Consequently its fiberwise kernel is exactly G0 in every fiber, proving the fiberwise assertion (2), not merely a generic sheaf intersection.

Equivalently E0+N O is the inverse image of F18 under C O->V18* O. Since F18 is saturated, E0+N O is saturated. There is an exact sequence of bundles

    0 -> N O/G0 -> C O/E0 -> V18* O/F18 -> 0.       (8)

In particular j:N O/G0->C O/E0 is everywhere a subbundle inclusion.

Because N is a genuine constant subspace, differentiation of G0 inside N and inside C is compatible with the quotient map. Therefore

    beta_E0 restricted to G0 = j(-2) beta_G0.         (9)

This is the only compatibility of differentiation with a quotient needed here. No connection is put on E0/G0 or on F18, and no ordinary Birkhoff splitting is declared horizontal.

## 3. Span, cohomology, and the rank bound

The actual G0 is saturated in N O by (2) and (8). Its minimal constant coefficient span is G-invariant. Because N=A+V is multiplicity-free, a proper nonzero such span would be A or V, of dimension three. In either case G0 would be a saturated rank-three subbundle of a trivial rank-three bundle and hence equal to that trivial bundle, contradicting deg G0=-12. Thus G0 spans N.

It follows that H0(S)=0. From

    0 -> S -> N* O -> G0* -> 0

we obtain

    rank S=3,  deg S=-12,
    H1(S)=P+D,                                      (10)

using the physical identity

    V tensor Sym4 W=V tensor D=A+V+P+D.

Indeed N*=A+V injects into H0(G0*) because G0 spans N, and all the remaining constituents are P+D. In particular S and all its subbundles have ordinary top degree at most -1.

Since the actual first derivatives of u lie in m subset S, we have

    u subset S^-.

The annihilator transpose identity gives equal generic ranks for beta_G0 and beta_S. Hence rank beta_G0<=2. Rank zero is impossible: a horizontal subbundle of a constant bundle on the complex projective line is constant and has degree zero, whereas G0 has degree -12. It remains to exclude rank one.

## 4. Rank one violates a two-step coherent-kernel capacity bound

Assume rank beta_G0=1. Write the actual rank-one derivative quotient as

    G0/G0^-=O(a).

The group has no nontrivial scalar characters. Since G0 is center-even, a is even. The nonzero quotient map V(-4)->O(a) gives

    Hom_G(V,Sym^(a+4) W) nonzero.

The first occurrence of V in even physical symmetric powers is in Sym6 W=V+P; Sym0 W=1, Sym2 W=A, and Sym4 W=D do not contain V. Therefore

    a>=2.                                            (11)

Set L=S^-, and write S/L=B1=O(b). The actual annihilator transpose is a nonzero coherent injection

    O(b) -> O(-a-2).

No saturation is presumed for this map. Ordinary degree alone gives

    b<=-a-2<=-4,
    rank L=2,
    deg L=-12-b.                                    (12)

We now prove the needed two-step derivative bound directly inside the genuine constant ambient N* O. Since L=S^-, the derivatives of local sections of L lie in S. Consequently its actual second fundamental form factors through

    beta_L:L -> (S/L)(-2)=B1(-2).

This map is not zero. If it were zero, L would be horizontal in N* O. A horizontal saturated subbundle of a constant bundle on the complex projective line is constant: its Grassmannian classifying map has zero differential, hence is constant in characteristic zero. Such a bundle has degree zero. But L is a subbundle of the negative-top S, so all its ordinary degrees are strictly negative.

Thus beta_L has generic rank one. Its saturated kernel L1=L^- has rank one, and the actual coherent quotient injects into the indicated line:

    L/L1 -> B1(-2),
    deg(L/L1)<=b-2.                                 (13)

Next, the derivatives of L1 lie in L by the definition L1=L^-. Its second fundamental form therefore factors through (L/L1)(-2). Again this map cannot vanish: the negative line L1 cannot be horizontal in the constant ambient. It is a nonzero line map, so composing it with (13) twisted by -2 yields the coherent injection

    L1 -> (L/L1)(-2) -> B1(-4),
    deg L1<=b-4.                                    (14)

The word coherent is essential: zeros or torsion cokernels in either map are permitted, and only their degree inequalities are used. Neither image is replaced by its saturation. Adding (13)-(14) gives

    -12-b=deg L<=2b-6,
    b>=-2.                                          (15)

This contradicts b<=-4 from (12). Therefore rank one is impossible. Together with Section 3, rank beta_G0=2.

## 5. The only possible dual derivative quotient is W'(-1)

Now S^- has rank one and contains the saturated u of the same rank. Saturation implies

    S^-=u.

Let B=S/u. Then B has rank two, degree -2, and is center-even. Since H0(S)=H0(u)=0, the cohomology sequence and (10) give

    0 -> H0(B) -> P+D -> P+D -> H1(B) -> 0.         (16)

Therefore H0(B) and H1(B) are subquotients of P+D.

For a rank-two equivariant bundle, an irreducible doublet splitting is forced by the degree to be W(-1) or W'(-1). Otherwise it is a sum of scalar even-degree lines. Order them as

    B=O(c)+O(-2-c),  c>=-1.

Then c is even, so c>=0, and

    H0(B)=Sym^c W,  H1(B)=Sym^c W.

Since these must fit in P+D, c+1<=9. The only even values to check are 0,2,4,6,8. Their symmetric powers are respectively 1,A,D,V+P,P+D. Thus only c=4 or c=8 is allowed. This leaves exactly

    W(-1), W'(-1), O(4)+O(-6), O(8)+O(-10).         (17)

The actual derivative beta_G0 factors through B*(-2) and has generic rank two. For B=O(4)+O(-6), that target is O(-6)+O(4); the O(-6) row receives no map from V(-4), even non-equivariantly. For B=O(8)+O(-10), the target is O(-10)+O(8), and the O(-10) row likewise receives no map. Each scalar alternative would give rank at most one, so is impossible.

For B=W(-1), the target is W(-1), but

    Hom_G(V(-4),W(-1))
       = Hom_G(V,W tensor Sym3 W)
       = Hom_G(V,A+D)
       = 0.                                             (18)

Thus B=W'(-1). The physical tensor identity for the permitted map is

    W' tensor Sym3 W=V+D,
    Hom_G(V(-4),W'(-1))=C.                              (19)

No actual scalar in this one-dimensional Hom space is selected.

## 6. The intrinsic derivative is everywhere onto and has kernel O(-10)

The actual induced derivative map is

    V(-4) -> B*(-2)=W'(-1),                              (20)

with generic rank two. Its entries have degree three, and its two-by-two maximal minors have degree six. At least one such minor is nonzero. Their common divisor is the rank-drop divisor, is G-invariant, and has degree at most six. The invariant-divisor minimum twelve makes it empty.

Consequently (20) is everywhere onto. Since B*(-2) is itself a subbundle of S*(-2)=(N/G0)(-2), this proves the statement about the actual coherent derivative image, not just its saturation. Its actual kernel H=G0^- is a line of degree

    deg G0 - deg W'(-1) = -12-(-2)=-10.

The absence of nontrivial characters gives

    0 -> H=O(-10) -> G0=V(-4) -> W'(-1) -> 0.      (21)

## 7. The derivative embeds as a saturated W'(-1) in A(4)

The image W'(-1) in (20) is a subbundle of (N/G0)(-2). By (8)-(9), it remains a subbundle in the larger derivative target (C/E0)(-2).

The restriction of the actual E0 derivative factors through its actual quotient E0/K=A(4). As (9) identifies its restriction on G0 with an injective inclusion of the intrinsic derivative image, the induced map

    i:W'(-1) -> A(4)                                    (22)

is well-defined and injective. Its composition with the actual inclusion of the E0 derivative image into (C/E0)(-2) is the subbundle inclusion already obtained. Consequently i has rank two on every fiber. Its cokernel in A(4) is a line bundle, with degree

    deg A(4)-deg W'(-1)=12-(-2)=14.

Thus

    0 -> W'(-1) -> A(4) -> O(14) -> 0.                  (23)

For an independent elementary check of saturation, the entries of (22) have degree five, so its maximal two-by-two minors have degree ten. A generic rank-two equivariant map of these types can have no rank-drop divisor, by the same invariant-divisor minimum. This additional check is not needed once the actual constant-intersection bridge (8) is used.

There is no confusion here between beta_K's retained full coherent image A(2) and the derivative quotient/image A(4) of E0: equation (22) uses precisely the latter, with domain E0 and kernel K as in (4).

## 8. The induced quotient of F18 and its actual kernel

Equation (9) and injectivity of j identify the kernel on G0 with the intrinsic derivative kernel H. Hence

    K intersect G0=H.                                  (24)

Compare the actual quotient rows

    0 -> K -> E0 -> A(4) -> 0,
    0 -> G0 -> E0 -> F18 -> 0.

The image of G0 in A(4) is exactly the saturated W'(-1) of (23). Passing to quotients therefore gives the exact sequence of bundles

    0 -> K/H -> F18 -> A(4)/W'(-1) -> 0,
    0 -> K/H -> F18 -> O(14) -> 0.                      (25)

The surjectivity in (25) is actual and everywhere: E0->A(4) is onto its actual derivative quotient and (23) is a quotient by a subbundle. No differential structure on F18 is asserted or used.

Finally

    rank K=16-3=13,
    deg K=-46-12=-58,
    rank(K/H)=12,
    deg(K/H)=-58-(-10)=-48.                             (26)

This agrees with deg F18=-34 and the quotient degree 14 in (25).

## 9. The dual annihilator also has splitting V(-4)

The result B=W'(-1) gives

    0 -> u=O(-10) -> S -> W'(-1) -> 0.                  (27)

Its equivariant extension space is one-dimensional:

    Ext1_G(W'(-1),O(-10))
       = (W' tensor H1(O(-9)))^G
       = (W' tensor Sym7 W)^G
       = C,
    Sym7 W=W'+T6.                                      (28)

This extension cannot split, because a W'(-1) summand of S would give a nonzero map to N* O=(A+V)O, whereas

    Hom_G(W'(-1),(A+V)O)
       = Hom_G(W',(A+V) tensor W)
       = Hom_G(W',W+S4+T6)
       = 0.                                             (29)

The sequence (21) is a nonzero extension in the same one-dimensional space: it cannot split because Hom(W'(-1),V(-4))=0 by ordinary degree. Therefore (21) and (27) have the same abstract equivariant middle-bundle type, and

    S is equivariantly isomorphic to V(-4).              (30)

This is an abstract splitting consequence only. It does not identify the actual G0 in N with its actual annihilator S in N*, or identify H with u.

## 10. Contribution and exact boundary

The new claims are the intrinsic rank-two derivative, its everywhere W'(-1) coherent image, the saturated inclusion in the actual A(4) derivative quotient of E0, and the resulting actual F18 quotient O(14) with kernel K/H of rank twelve and degree -48. Section 9 additionally identifies the abstract splitting of the dual annihilator S.

No first-jet partial system is treated as complete, no quotient bundle is given an unjustified connection, no coherent image is silently saturated, and no selected actual coefficient or matrix is tested. The rank-one exclusion uses only a two-step coherent derivative flag, proved directly above. Both gluing alternatives for F18 remain unexcluded here. Realization, further compatibility, and any whole-branch exclusion remain outside this conclusion.
