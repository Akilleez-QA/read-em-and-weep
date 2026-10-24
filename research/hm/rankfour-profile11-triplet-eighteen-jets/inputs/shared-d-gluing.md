# Exact shared-D gluing forces two degree-eighteen jet-kernel alternatives

## Statement and retained boundary

Work over C on the physical binary-icosahedral line P(W*), with G=SL2(F5) and the fixed determinant convention. Retain all actual-geometric hypotheses of PR1206, in particular the original rank-four maximal ordered profile (1,1), its source and section gates, and precisely the full-positive coherent-image branch

    A_q=A(4)+O(-8),  A=Sym2 W,  im beta_K=A(2).

Use PR1206's actual twenty-one-dimensional constant ambient C*, its degree-ten and degree-eighteen scalar curves, and their forced common constant D coefficient block. Their individual first-jet subbundles are M10 and M18. Let

    F=ann(M10+M18) in C O,
    F10=ann_(V10)(M10) in V10* O,
    F18=ann_(V18)(M18) in V18* O,

where V10 and V18 are the two actual coefficient spans. Let R be the first-jet kernel of the degree-ten curve projected to V10/D, the incomplete coefficient system of representation A+V. Then:

1. The actual first-jet annihilators satisfy an everywhere-surjective gluing sequence

       0 -> F -> F10 direct-sum F18 -> D* O -> 0,
       F10=(P+D)(-2).

2. The projected degree-ten system is everywhere first-jet-spanned, and

       R=V(-4)+O(-6),
       0 -> R -> F10 -> D* O -> 0,
       0 -> R -> F -> F18 -> 0.

3. Exactly the following two equivariant splitting types are permitted for the actual degree-eighteen first-jet annihilator:

       F18=D(-2)+(W'+T6)(-3),

   or

       F18=(D+V)(-2)+W'(-3)+V(-4).

4. Restriction from the actual E0 induces

       0 -> V(-4) -> E0 -> F18 -> 0.

   It splits equivariantly in the first case. In the second case its unique nontrivial extension block is the universal physical Euler sequence

       0 -> V(-4) -> T6(-3) -> V(-2) -> 0.

As a separate final corollary, if V(-4) denotes the actual common kernel just obtained, then Q=F10/V(-4) is equivariantly T6(-1), and restriction induces an actual map F18->Q. No rank, image, saturation, or further exclusion is asserted for that map.

These are necessary actual-bundle compatibility statements, not realization claims. Neither degree-eighteen alternative is excluded. No full-positive branch, whole K splitting, triplet quotient, or maximal profile is newly excluded or realized. The original defect t=0 is unchanged. The other coherent endpoint images of PR1199 remain separate. No actual coefficient, point, parameter, jet, tensor, matrix, or relative normalization is selected or evaluated. Only the degree-ten system is complete, as already proved in PR1206; the degree-eighteen and projected degree-ten systems remain incomplete.

## 1. Immutable inputs and retained actual objects

INPUTS.json records the complete immutable source files, their exact commits, paths, Git blobs, byte lengths, and SHA256 hashes. They are PR1206 at commit 252b967ebbfbea6fc0c6451a835ab2daff92d73b (the forced shared-D theorem); PR1205 at commit 97dad5c307a04f61d850e8a4211559e97ed4c2fd (the actual small ambient, scalar curves, first jets, and coefficient-span alternatives); PR1199 at commit 95af2c0fa1e3cce92496a44ef9023708735e1ec7 (universal principal parts and the invariant-divisor minimum); and ACTUAL at commit db51525015bb7c5e825833d550d08dedf6f6ea96 (physical representations and equivariant splitting conventions). Their transitive actual-geometric hypotheses remain assumptions. No rank-seventeen theorem is transferred to E0.

Work on the physical binary line P(W*) over C, for G=SL2(F5). Write V10 and V18 for the actual constant coefficient spans in the PR1206's C*. Retain

    dim C*=21,
    V10=A+V+D,                dim V10=11,
    V18=A+V+P+D,              dim V18=15,
    V10+V18=C*,               V10 intersect V18=D.

The degree-ten coefficient map Sym10 W -> V10 is an actual isomorphism. The degree-eighteen map Sym18 W -> V18 has exactly one P kernel; no particular P subspace in its two-copy isotypic component is selected.

The actual scalar lines and their actual first jets satisfy

    U=O(-10), T=O(-18), L=U+T,
    M10=P^1(O(10))*=W(-9),
    M18=P^1(O(18))*=W(-17),
    M=M10 direct-sum M18 subset C* O,
    E0=D(-2)+(W'+T6)(-3)+V(-4),
    F=ann(M),
    0 -> E0 -> F --q--> O(-6) -> 0,
    F=D(-2)+(W'+T6)(-3)+V(-4)+O(-6).           (1)

Here the quotient q and E0=ker(q) are actual maps/subbundles. The last abstract equivariant splitting follows from H1(E0(6))=0; it does not declare an arbitrary splitting horizontal.

Define

    Fi=ann_(Vi)(Mi) subset Vi* O,   i=10,18.

All appearances of D* below refer to the actual dual of the constant intersection V10 intersect V18. Its representation is isomorphic to D; an identification is not chosen.

## 2. Universal identities used in the proof

For the fixed determinant convention, the complete first-jet evaluation sequence is

    0 -> Sym^(d-2) W(-2)
      -> Sym^d W O
      -> P^1(O(d)) -> 0,                       d>=2.       (2)

This is a universal identity for the complete polynomial system, not a completeness assertion about an actual partial system. At a variable point the kernel consists of forms divisible by the square of its vanishing linear form. Multiplication identifies this kernel with Sym^(d-2) W times the tautological square O(-2). The quotient is the universal first-principal-parts bundle. The fixed determinant pairing identifies the needed dual binary representations.

The complete evaluation dual for degree four also gives

    0 -> O(-6) -> D(-2) -> S4(-1) -> 0.                    (3)

The small physical representation identities used below are

    Sym2 W=A,       Sym3 W=S4,       Sym4 W=D,
    Sym8 W=P+D,
    Sym10 W=A+V+D,
    Sym16 W=V+P+2D,
    Sym18 W=A+V+2P+D,
    A tensor D=A+V+P+D,
    A tensor P=V+P+D,
    W tensor D=S4+T6,
    W tensor V=T6,
    W tensor P=W'+T6,
    W tensor W'=P,
    W tensor W=1+A,
    P tensor S4=S4+2T6.                                   (4)

All irreducibles here are self-dual. In particular (4) gives

    Sym16 W tensor W - P tensor S4 = W'+S4+2T6.            (5)

The physical W is never replaced by W'. The group has no nontrivial one-dimensional characters. Its nonzero invariant effective divisors on P(W*) have degree at least twelve. These are the fixed representation/orbit facts already retained in the sources.

For an equivariant center-even summand R(-j), j>=4, equivariant Serre duality gives

    H1(R(-j)(2)) = R tensor Sym^(j-4) W.                   (6)

The coefficient representation R has center parity (-1)^j. Every contribution in (6) is genuine; forbidden constituents cannot cancel.

## 3. The shared-D gluing sequence is onto everywhere

The actual constant-span sum and intersection give

    0 -> C -> V10* direct-sum V18* -> D* -> 0,             (7)

where the final map is the difference of restrictions to the actual common D.

Set J10=P^1(O(10)), J18=P^1(O(18)), J=J10 direct-sum J18. The actual subbundle M in C* O dualizes to a surjective evaluation map

    C O -> J.

For each i this map followed by J->Ji factors through the restriction C->Vi*. Consequently Vi* O->Ji is everywhere onto as well. Its kernel is precisely Fi. In particular, no separate completeness assertion about the degree-eighteen curve is needed for its jet evaluation.

Compare (7), tensored with O, with the exact row

    0 -> J --identity--> J -> 0 -> 0.

The first two vertical arrows are the evaluations just described. The snake lemma gives an exact sequence of bundles

    0 -> F -> F10 direct-sum F18 -> D* O -> 0.             (8)

Thus the final gluing map is surjective, not merely a generic map with an unspecified coherent image or torsion defect. Since the degree-ten system is complete, (2) gives

    F10=Sym8 W(-2)=(P+D)(-2).                              (9)

Also rank(F18)=13 and deg(F18)=-34, from the exact evaluation onto J18.

## 4. Projecting degree ten away from D remains first-jet-spanned

Consider the actual quotient V10/D, of representation A+V, and the projected degree-ten scalar system in this six-dimensional constant quotient. Equivalently its coefficient sections form the annihilator of D in the complete degree-ten section space.

This partial system is basepoint-free. If its sections had a common zero, their common zero divisor would be G-invariant and have degree at most ten. The invariant-divisor minimum twelve rules this out. The curve is nonconstant: its coefficient sections are six linearly independent sections, so its constant span is the full quotient A+V. In characteristic zero, its first-jet evaluation therefore has generic rank two.

Project the complete first-jet kernel (9) to the removed coefficient quotient D*. This gives a map

    phi:(P+D)(-2) -> D* O.                                 (10)

Generic first-jet surjectivity of the projected curve, via the evaluation diagram, says that phi has generic rank five. Its matrix entries are quadratic sections. Every 5-by-5 maximal minor is a section of O(10), and at least one is nonzero. The common divisor of these maximal minors is the zero-dimensional rank-drop divisor, with the minimum local vanishing multiplicities. It is G-invariant and has degree at most ten, bounded by any nonzero minor. Hence it is empty. Therefore phi is everywhere onto.

Writing R=ker(phi), the same diagram identifies R with the actual first-jet evaluation kernel of the projected A+V degree-ten system. We have proved the exact sequence

    0 -> R -> (P+D)(-2) --phi--> D* O -> 0,
    rank R=4,  deg R=-18.                                 (11)

This argument does not evaluate a maximal minor or choose a point: it uses only its universal degree and equivariance. The projected degree-ten system is incomplete; it has not been replaced with a complete one.

## 5. The projected degree-ten kernel is V(-4)+O(-6)

Twisting (11) by two, H0(R(2)) is the kernel of an equivariant constant map

    P+D -> D tensor A=A+V+P+D.

Since P and D occur once in the source, any nonzero kernel contains one of them. A D kernel would inject D(-2), of rank five, into the rank-four R. A P kernel would inject P(-2) into R with equal rank four. Its determinant would be a nonzero map O(-8)->O(-18), which is impossible since H0(O(-10))=0. Thus

    H0(R(2))=0,
    H1(R(2))=A+V.                                         (12)

The first equality makes the top ordinary degree of R at most -3. For completeness, the small atom argument behind the second equality's splitting consequence is as follows. A summand Rj(-j), j>=4, contributes Rj tensor Sym^(j-4)W to the genuine six-dimensional budget A+V. Center parity and this dimension bound leave the following possibilities to check:

* Scalar even degrees j=4,6,8 contribute 1,A,D respectively; only j=6 is allowed.
* Odd doublets can contribute only at j=5; W tensor W=1+A and W' tensor W=P are both forbidden. Higher odd degrees exceed the budget.
* Even triplets contribute at j=4, giving A or V. Their next even degree already contributes dimension nine.
* An even four-space at j=4 contributes the forbidden P; a dimension-five or dimension-six coefficient is either too large, has a forbidden irreducible, or exceeds rank R. Odd degree-three atoms contribute no H1 and do not supply either required triplet.

Thus the only positive-H1 atoms are A(-4), V(-4), and O(-6). The required V constituent forces V(-4), using three of the four ranks. The remaining A constituent and remaining rank force O(-6). Therefore

    R=V(-4)+O(-6).                                        (13)

In particular, by (8) and the surjectivity of its F10 component (10), projection to the second factor gives an exact sequence

    0 -> R -> F -> F18 -> 0.                               (14)

## 6. Exactly two possible degree-eighteen first-jet kernels

Let K18 be the actual P kernel of Sym18 W -> V18. Dualizing gives the complete section space modulo V18* as K18*, of representation P. Comparing complete and partial first-jet evaluations yields

    0 -> F18 -> Sym16 W(-2) -> P O -> 0.                   (15)

Here surjectivity follows from the already established everywhere-surjective actual evaluation V18* O->J18. Thus F18 has top degree at most -2, independently of any splitting classification.

Twist (8) by two. Formula (1) gives

    H1(F(2))=V+A,
    H1(F10(2))=0,
    H1(D*(2))=0.

Hence H1(F18(2)) is a quotient of A+V. On the other hand, (15) twisted by two makes it a quotient of

    P tensor A=V+P+D.

Semisimplicity and multiplicity one show

    H1(F18(2)) is either 0 or V.                            (16)

From (15) and (4),

    chi_G(F18(2))
       = Sym16 W - P tensor A
       = (V+P+2D)-(V+P+D)
       = D.

Consequently

    H0(F18(2)) is respectively D or D+V.                    (17)

If H1 is zero, all ordinary degrees of F18 are -2 or -3, since its top is at most -2. Its degree-minus-two coefficient block is D by (17). Twisting (15) by three gives

    chi_G(F18(3))=W'+S4+2T6

by (5). The block D(-2) contributes D tensor W=S4+T6. Thus the degree-minus-three block is W'+T6, giving

    F18=D(-2)+(W'+T6)(-3).                                 (18a)

If H1 is V, formula (6) has the genuine budget consisting of one triplet V. The only possible atom with nonzero H1 is V(-4): scalar degree four contributes 1, scalar degree six contributes A, any higher scalar has dimension at least five, odd doublet degree five has dimension four, and all other possibilities have a forbidden constituent or exceed dimension three. Thus there is exactly one V(-4). Equation (17) supplies the degree-minus-two block D+V. The remaining rank is two, its degree is -6, and the same twist-three Euler characteristic gives W'. Hence

    F18=(D+V)(-2)+W'(-3)+V(-4).                            (18b)

This also identifies a necessary condition on the complete-jet map in (15) on global quadratic sections: its P source constituent maps nontrivially to the target P, and its two-copy D source maps onto the target D. Its only possible global-section failure is the scalar map from its V constituent to the target V. No actual value of that scalar is chosen.

## 7. The scalar line cancels against the actual quotient F/E0

Fix any equivariant splitting (13), and let a:O(-6)->R->F denote its scalar summand. We claim that q a:O(-6)->O(-6), for the actual quotient q in (1), is nonzero.

Suppose q a=0. Then a factors through the actual E0. Its possible equivariant components are controlled by the following explicit small Hom identities:

    Hom_G(O(-6),D(-2)) = (D tensor Sym4 W)^G = C,
    Hom_G(O(-6),W'(-3)) = (W' tensor S4)^G = 0,
    Hom_G(O(-6),T6(-3)) = (T6 tensor S4)^G = 0,
    Hom_G(O(-6),V(-4)) = (V tensor A)^G = 0.                (19)

Thus the nonzero inclusion a must lie solely in D(-2), and is a nonzero scalar multiple of the universal quartic inclusion (3). In particular the quotient of that D(-2) is S4(-1). Since a is a subbundle of R and R is a subbundle of F, the quotient F/a(O(-6)) is locally free. Using (1) and (3), its abstract splitting contains S4(-1) as a rank-four direct summand.

Quotienting (14) by this scalar line gives

    0 -> V(-4) -> F/a(O(-6)) -> F18 -> 0.                  (20)

But (15) implies Hom(S4(-1),F18)=0: after composing with F18->Sym16 W(-2), all entries would be sections of O(-1). Hence the entire rank-four S4(-1) summand of F/a(O(-6)) lies in the rank-three kernel V(-4) in (20), impossible.

Therefore q a is nonzero and hence an isomorphism. On the other summand of R,

    Hom(V(-4),O(-6))=V* tensor H0(O(-2))=0.                 (21)

It follows that R intersect E0 is precisely its actual V(-4) kernel under q, and that E0 maps onto F18 in (14): subtracting the unique scalar element of R cancels q for any lift. We obtain the actual exact restriction sequence

    0 -> V(-4) -> E0 -> F18 -> 0.                          (22)

This is not an arbitrary splitting or an assumption that coefficient-span decompositions split E0. It is derived from the actual quotient q, the shared-D gluing, and the quartic universal inclusion.

## 8. Extension types in the two branches

For (18a), every equivariant extension block in Ext1_G(F18,V(-4)) vanishes:

    Ext1_G(D(-2),V(-4))
       = (D* tensor V tensor H1(O(-2)))^G
       = Hom_G(D,V)=0,
    Ext1_G(W'(-3),V(-4))=0,
    Ext1_G(T6(-3),V(-4))=0,                                (23)

the latter two because H1(O(-1))=0. Hence (22) splits equivariantly in branch (18a).

For (18b), the same vanishings apply to D(-2) and W'(-3); the V(-4) quotient block also has zero extension group because H1(O)=0. The sole nonzero group is

    Ext1_G(V(-2),V(-4))
       = (V* tensor V tensor H1(O(-2)))^G
       = End_G(V)=C.                                      (24)

If this class were zero, the middle bundle in (22) would contain V(-2), contrary to the prescribed E0 splitting in (1). Therefore the extension is nonzero. The universal Euler sequence, tensored with V(-2), represents its nonzero class:

    0 -> V(-4) -> (W tensor V)(-3) -> V(-2) -> 0,
    W tensor V=T6.                                        (25)

Its middle bundle is T6(-3), exactly the prescribed degree-minus-three block. Since (24) is one-dimensional, all nonzero classes have this equivariant middle-bundle type, up to automorphisms of the end terms. No actual extension scalar or coefficient normalization is fixed.

## 9. Contribution and remaining work

The theorem establishes, under the retained PR1206 hypotheses:

* An everywhere-surjective shared-D first-jet gluing sequence, with no omitted torsion defect.
* An independently derived, incomplete projected degree-ten first-jet system with kernel V(-4)+O(-6).
* Exactly two possible degree-eighteen first-jet-annihilator splittings.
* An actual restriction sequence 0->V(-4)->E0->F18->0 and its split/Euler extension alternatives.

All arguments use fixed universal bundle identities, small physical representation identities, exact diagrams, and the invariant-divisor minimum. They neither select nor test an actual coefficient system. The incomplete degree-eighteen system remains incomplete throughout. Neither overlapping alternative is excluded or asserted realized at the level proved here. Realization, higher-jet compatibility, and any further exclusion remain outside this theorem.


## 10. Separate corollary: the universal T6(-1) quotient and an induced actual map

Use the actual subbundle V(-4)=R intersect E0 identified in Section 7, viewed also as a subbundle of F10 through R subset F10. Define

    Q=F10/V(-4).

Quotienting (11) by V(-4), and using (13) and (21), gives an exact sequence of actual bundles

    0 -> O(-6) -> Q -> D* O -> 0.                         (26)

Here R/V(-4)=O(-6); this statement uses the actual kernel of q on R, not an arbitrary degree-four subbundle. Since D is self-dual and Sym4 W=D,

    Ext1_G(D* O,O(-6))
       = (D tensor H1(O(-6)))^G
       = (D tensor Sym4 W)^G
       = C.                                              (27)

The extension (26) cannot split. A splitting would give a surjection Q->O(-6), whose composition with the quotient F10->Q would be nonzero. But

    Hom(F10,O(-6))
       = (P+D)* tensor H0(O(-4))
       = 0.                                              (28)

The universal dual evaluation sequence in degree five, twisted by -1, is

    0 -> O(-6) -> Sym5 W(-1) -> Sym4 W O -> 0,
    Sym5 W=T6,  Sym4 W=D.                                 (29)

It represents a nonzero class in the one-dimensional group (27): its middle bundle has only ordinary degree -1, so is not the split O(-6)+D O. Thus every nonzero equivariant extension in (27) has that middle-bundle type, up to automorphisms of the end terms. Equations (26)-(29) prove

    Q is equivariantly isomorphic to T6(-1).               (30)

Finally, the actual projection F->F10 from (8), restricted to E0, gives E0->F10. Its composition with F10->Q vanishes on the actual kernel V(-4) in (22), because that kernel is the same subbundle coming from R. Therefore it factors uniquely through the actual quotient E0->F18, giving a commutative restriction diagram and an induced actual map

    F18 -> Q,     Q isomorphic to T6(-1).                 (31)

No identification in (30) selects a coefficient normalization, and this corollary makes no claim about the map's rank, coherent image, saturation, or whether either alternative (18a)-(18b) can satisfy further compatibility. Those are separate questions.
