# Constant restriction forces the actual second and third jets of the degree-eighteen curve

## Statement and retained boundary

Retain the complete actual-geometric hypotheses and conclusions of PR1208, hence the original rank-four maximal ordered profile (1,1), its source and section gates, and precisely the full-positive coherent-image branch

    A_q=A(4)+O(-8),  A=Sym2 W,  im beta_K=A(2).

Let p:C->V18* be restriction to the actual fifteen-dimensional coefficient span V18 of the degree-eighteen scalar curve. Write F18=ann_(V18)(M18) for its actual first-jet annihilator, where M18=W(-17). Let G0=ker(p|E0)=V(-4), and let H=G0^-=K intersect G0 be the actual primal line O(-10) of PR1208. Then:

1. The derivative of F18 has everywhere coherent image O(14), as a saturated line in (V18* O/F18)(-2)=W(15), and

       J:=F18^-=p(K),
       0 -> H -> K -> J -> 0,
       rank J=12,  deg J=-48.

2. The actual second-jet map of the degree-eighteen scalar curve identifies

       P^2(O(18))*=A(-16)

   with the actual saturated subbundle ann(J) in V18 O.

3. The derivative of J has everywhere coherent image O(12), as a subbundle of its actual normal target. Consequently

       0 -> J^- -> J -> O(12) -> 0,
       rank J^-=11,  deg J^-=-60,

   and the actual third-jet map identifies

       P^3(O(18))*=S4(-15)

   with the actual saturated subbundle ann(J^-) in V18 O.

4. The constant restriction p is everywhere injective on K^-, and its actual image satisfies

       0 -> p(K^-) -> J^- -> O(4) -> 0,
       p(K^-) isomorphic to K^-,
       rank p(K^-)=10,  deg p(K^-)=-64.

5. The actual image p(K^-) has full constant span V18*, of dimension fifteen. Thus p realizes K^- in this genuine smaller constant ambient, without asserting that its original inclusion in C has the same constant span.

These are necessary actual-map and intrinsic-jet conditions, not realization claims. The degree-eighteen coefficient system remains incomplete, with a single P kernel in Sym18 W. No fourth or higher jet, differential structure on a quotient bundle, algebraicity assertion, or new whole-branch exclusion is claimed. Neither PR1207 splitting alternative for F18 is excluded here. No whole K splitting, triplet quotient, or maximal profile is excluded or realized; the original defect t=0 remains unchanged. No actual coefficient, parameter, point, jet, tensor, matrix, or relative normalization is selected or evaluated.

## 1. Immutable inputs and exact actual objects

INPUTS.json records the complete immutable source files, their exact commits, paths, Git blobs, byte lengths, and SHA256 hashes. The principal input is PR1208 at commit 2a8105d5a3a263b7518eb98bdf81689c3d4b3dfa, path research/hm/rankfour-profile11-triplet-sixspace-derivative/PROOF.md, whose complete proof has SHA256 16823fcb3c9012c02a23406dcf4656e27441fcb05734551e7d2d4b1756085c67. The retained gluing input is PR1207 at commit af136934955f1bcc700ee768e2debb983e75451d, path research/hm/rankfour-profile11-triplet-shared-d-gluing/PROOF.md. The universal physical principal-parts identity is PR1199 Section 4, at commit 95af2c0fa1e3cce92496a44ef9023708735e1ec7, path research/hm/rankfour-profile11-triplet-deep-images/PROOF.md. These are the three complete direct sources. In particular the full coherent image of beta_K and the actual small ambient are explicitly retained in PR1208 Section 1; their older source hypotheses remain imported transitively. The physical representation and determinant conventions are those retained in these three sources. No rank-seventeen theorem is transferred to any smaller bundle.

Work on the physical binary-icosahedral line P(W*) over C, with G=SL2(F5) and the fixed determinant convention. All annihilators below use the actual constant pairing between V18 and V18*. We retain

    dim C=21,  dim V18=15,
    p:C -> V18* constant and surjective,
    p(E0)=F18,
    0 -> G0 -> E0 --p--> F18 -> 0,
    G0=V(-4),
    E0=D(-2)+(W'+T6)(-3)+V(-4),
    K=E0^-,
    E0/K=A(4),
    beta_K:K -> (E0/K)(-2)=A(2) is everywhere onto.       (1)

The last statement is precisely the retained equality of actual coherent images, not merely a generic-rank or saturation statement. In particular

    rank K=13,  deg K=-58,
    0 -> K^- -> K -> A(2) -> 0,
    rank K^-=10,  deg K^-=-64.                          (2)

The actual first jets and their annihilator satisfy

    M18=P^1(O(18))*=W(-17) subset V18 O,
    F18=ann(M18) subset V18* O,
    rank F18=13,  deg F18=-34,
    V18* O/F18=M18*=W(17).                              (3)

PR1207 also gives F18 subset Sym16 W(-2), so F18 has strictly negative top degree. PR1208 supplies the exact actual maps

    H=G0^-=K intersect G0=O(-10),
    0 -> H -> G0 -> W'(-1) -> 0,
    0 -> W'(-1) -> A(4) --pi--> O(14) -> 0,
    0 -> K/H -> F18 --rho--> O(14) -> 0.                (4)

The map W'(-1)->A(4) in (4) is the actual derivative image of G0 inside the actual quotient E0/K. The last row is induced from the preceding rows by constant restriction, not chosen independently. In particular, if q:E0->A(4) is the actual derivative quotient, then

    rho p|E0 = pi q.                                  (5)

H is a line in the primal constant space C. It is not identified with the projected degree-ten scalar line in the distinct dual constant space N*. The original degree-eighteen scalar line in V18 O will be denoted T=O(-18).

## 2. First constant derivative square and the O(14) image

For the first square, p induces the actual quotient map

    pbar:C O/E0 -> V18* O/F18.

Differentiation of local sections commutes with the constant linear map p. Therefore the actual second fundamental forms satisfy

    beta_F18 p|E0 = pbar(-2) beta_E0.                   (6)

Every map in (6) is between an actual subbundle and its actual normal quotient in a constant ambient. No connection on E0/G0 or on F18 as a quotient is being asserted.

The actual E0 derivative factors as q:E0->A(4), followed by the injective actual image map to (C O/E0)(-2). Composing that image map with pbar(-2), and using (3), gives a regular equivariant bundle map

    theta:A(4) -> (V18* O/F18)(-2)=W(15).               (7)

Its restriction to the W'(-1) in (4) is zero. Indeed beta_E0 restricted to G0 is everywhere onto that image, whereas p(G0)=0 makes the left side of (6) vanish on G0. Thus theta factors through the actual quotient pi:

    theta=epsilon pi,
    epsilon:O(14) -> W(15).                            (8)

The map epsilon is nonzero. Otherwise (6) would make beta_F18 vanish, since p|E0 is onto F18. A horizontal saturated subbundle of a constant bundle on the complex projective line is constant: its Grassmannian classifying map has zero differential and is constant in characteristic zero. It has degree zero. This contradicts deg F18=-34, so beta_F18 is nonzero.

For the physical W,

    Hom_G(O(14),W(15))=(W tensor Sym1 W)^G=C,
    W tensor W=1+A.                                    (9)

Every nonzero map in (9) is a nonzero scalar multiple of the universal Euler inclusion

    0 -> O(14) -> W(15) -> O(16) -> 0.                 (10)

Thus epsilon is an everywhere saturated line inclusion. No scalar or relative normalization is selected.

Using (5), (6), and (8), we have

    beta_F18 p|E0=epsilon pi q=epsilon rho p|E0.

Since p|E0 is surjective, this proves the actual factorization

    beta_F18=epsilon rho.                              (11)

Consequently its coherent image is exactly the saturated epsilon(O(14)), and its actual kernel is

    J:=F18^-=ker rho=p(K).

The equality p(K)=ker rho can also be seen directly: a lift e in E0 of a section of ker rho has q(e) in the image of G0, so subtracting a local section of G0 gives a lift in K. Since K intersect G0=H, we obtain

    0 -> H -> K --p--> J -> 0,
    0 -> J -> F18 --rho--> O(14) -> 0,
    rank J=12,  deg J=-48.                             (12)

All sequences in (12) are actual bundle sequences. They do not merely identify generic vector spaces.

## 3. Intrinsic second jets identify ann(J) with A(-16)

Set T2=ann(J) in V18 O. It is saturated, and (12) gives

    rank T2=3,  deg T2=-48.                            (13)

The actual forward transform of M18=ann(F18) is T2. To see the derivative containment directly, take a local section j of J=F18^- and a local section m of M18. Since j annihilates m and its derivative lies in F18,

    0=d<j,m>=<dj,m>+<j,dm>,
    <dj,m>=0,
    <j,dm>=0.

Thus J annihilates M18 and all its first derivatives. The annihilator-transpose identity gives equal generic ranks for the derivatives of F18 and M18, namely one by (11). Therefore the generic forward span of M18 has rank three. Its saturation is exactly T2: the annihilator of that generic span is the saturated backward kernel J.

The intrinsic second-jet map of the actual scalar inclusion T=O(-18) in V18 O is

    eta2:P^2(O(18))* -> V18 O.

It is the dual of evaluating the actual constant coefficient sections on order-two principal parts. Its generic image is the span of T, its first derivatives, and its second derivatives, hence the same rank-three forward span just described. Since T2 is saturated, eta2 factors regularly through T2. Equivalently its composite with V18 O/T2 vanishes generically and therefore vanishes identically.

The universal physical principal-parts identity gives

    P^2(O(18))*=Sym2 W(-16)=A(-16),
    rank P^2(O(18))*=3,
    deg P^2(O(18))*=-48.                              (14)

The factorization eta2:A(-16)->T2 is generically full rank between bundles of equal rank and degree. Its determinant is a nonzero section of O, so it is an everywhere isomorphism. Thus

    T2=ann(J) is the actual saturated second-jet subbundle,
    T2 is identified by eta2 with A(-16).               (15)

The universal identity in (14) does not assume completeness of the actual fifteen-dimensional coefficient system. Its role is to identify the intrinsic source; injectivity and saturation of the actual map are proved by the actual derivative rank and degree in (13).

## 4. Second constant derivative square and the O(12) image

Now apply the same constant restriction p to K and its actual image J. Since K=E0^-, derivatives of K lie in E0, so its intrinsic second fundamental form factors through (E0/K)(-2)=A(2), as in (1). Since J=F18^-, derivatives of J lie in F18, so its intrinsic second fundamental form factors through

    (F18/J)(-2)=O(12).

The actual map on these quotient bundles is pi from (4), twisted by -2:

    0 -> W'(-3) -> A(2) --pi(-2)--> O(12) -> 0.         (16)

Differentiation commutes with the same constant p, giving the second actual derivative square

    beta_J p|K = pi(-2) beta_K,                         (17)

where beta_J is written with its factored target O(12). In full normal quotients, both sides of (17) are followed by the same subbundle inclusion

    (F18/J)(-2) -> (V18* O/J)(-2).

This inclusion is a subbundle because J is a saturated subbundle of F18 and F18 is saturated in V18* O.

Both beta_K:K->A(2) and pi(-2):A(2)->O(12) are everywhere onto. Thus their composition is onto. Since p|K is onto J by (12), equation (17) proves that beta_J is everywhere onto its indicated O(12) target. Its actual coherent image is this subbundle, not a saturation substituted afterward. Therefore

    0 -> J^- -> J --beta_J--> O(12) -> 0,
    rank J^-=11,
    deg J^-=-48-12=-60.                               (18)

Again (17) uses the constant linear map between the original ambients. It does not differentiate the quotient map E0/G0 or assert a connection on either quotient in (16).

## 5. Intrinsic third jets identify ann(J^-) with S4(-15)

Set T3=ann(J^-) in V18 O. From (18),

    rank T3=4,  deg T3=-60.                             (19)

By the same constant-pairing differentiation argument as in Section 3, J^- annihilates T2=ann(J) and all its first derivatives. The actual derivative of J has rank one by (18), so the transpose identity makes the generic forward span of T2 have rank four. Its saturated forward transform is T3.

Since T2 is already the actual second-jet subbundle by (15), this generic forward span is precisely the span of the first four scalar-curve jets, through order three. The intrinsic third-jet map

    eta3:P^3(O(18))* -> V18 O

therefore has generic image T3 and factors regularly through T3 by saturation. The universal principal-parts identity gives

    P^3(O(18))*=Sym3 W(-15)=S4(-15),
    rank P^3(O(18))*=4,
    deg P^3(O(18))*=-60.                              (20)

As in Section 3, eta3 is generically full rank between equal-rank, equal-degree bundles. Its determinant is a nonzero constant, so it is an everywhere isomorphism onto T3. Hence

    T3=ann(J^-) is the actual saturated third-jet subbundle,
    T3 is identified by eta3 with S4(-15).              (21)

This is an intrinsic statement for the actual partial degree-eighteen coefficient system. It is not a calculation of a selected actual jet, nor an assumption that the curve has a complete coefficient system.

## 6. The derivative of H is an everywhere saturated line in W'(-3)

We next establish the final quotient in the theorem independently of any fourth-jet assertion. Restrict the square (17) to H=ker(p|K). Its left side vanishes. Therefore beta_K|H lands in the kernel W'(-3) of (16):

    beta_K|H:H=O(-10) -> W'(-3).                       (22)

This map is nonzero. Indeed H=G0^- implies that the derivatives of local sections of H lie in G0. If (22) vanished, H subset K^- would also make these derivatives lie in K. The actual fiberwise intersection K intersect G0 is H. Thus H would be horizontal in the constant ambient C, impossible for the negative line O(-10).

The entries of the nonzero line-to-doublet map (22) have degree seven. Their common zero divisor is invariant and has degree at most seven, bounded by any nonzero entry. The smallest nonzero invariant effective divisor has degree twelve, so the common divisor is empty. Consequently (22) is everywhere a saturated line inclusion. Degree and absence of nontrivial characters give

    0 -> H=O(-10) -> W'(-3) -> O(4) -> 0.              (23)

This argument selects neither a degree-seven covariant nor a point at which it is evaluated; it uses only the actual nonzero map, its universal degree, and the invariant-divisor minimum.

## 7. The exact quotient of J^- by p(K^-)

Compare the actual exact rows

    0 -> K^- -> K --beta_K--> A(2) -> 0,
    0 -> J^- -> J --beta_J--> O(12) -> 0.

Their vertical maps are restriction p on the first two terms and pi(-2) on the final terms, and the square commutes by (17). The kernel of p:K->J is H, while the kernel of pi(-2) is W'(-3). The induced map between these kernels is exactly (22).

The snake lemma gives

    0 -> ker(p|K^-) -> H -> W'(-3)
      -> coker(p|K^-) -> 0.                            (24)

By (23), the map H->W'(-3) is everywhere injective with line-bundle cokernel O(4). Therefore

    0 -> K^- --p--> J^- -> O(4) -> 0.                  (25)

In particular p|K^- has no fiberwise kernel, and its image is saturated in J^-. With the actual image denoted p(K^-),

    0 -> p(K^-) -> J^- -> O(4) -> 0,
    p(K^-) isomorphic to K^-.

Equation (2) gives rank p(K^-)=10 and degree p(K^-)=-64. This agrees with deg J^-=-60 and the quotient degree four in (25).

There is also a full constant-span consequence. The constant span of J^- is all V18*: otherwise a nonzero constant vector in V18 would annihilate every fiber of J^- and give a nonzero global section of ann(J^-)=S4(-15), which has none.

Let C' subset V18* be the actual constant span of p(K^-). The projection

    J^- -> (V18*/C') O

vanishes on p(K^-), hence factors through the O(4) quotient in (25). But Hom(O(4),O)=0, so that projection is zero. Therefore J^- lies in C' O. Since J^- spans all V18*, this proves

    constant span of p(K^-) = V18*,  dimension fifteen.   (26)

Thus the constant restriction p supplies an actual everywhere injection of K^- into a genuine fifteen-dimensional constant ambient, with full span there. It does not assert that the original inclusion K^- subset C O has constant span fifteen, nor declare an arbitrary source splitting horizontal.

The assertion is about the actual constant restriction of K^-. It does not identify p(K^-) with (J^-)^- and makes no assertion about the rank or image of the derivative of J^-.

## 8. Contribution and exact stopping point

The two constant restriction squares transfer the retained full coherent image of beta_K into the actual derivatives of the degree-eighteen first-jet annihilator and its backward kernel. They force everywhere images O(14) and O(12), respectively. Duality and the equal-rank, equal-degree intrinsic principal-parts maps then give the actual saturated second and third jets A(-16) and S4(-15).

The last argument additionally identifies the actual saturated image p(K^-) in J^- with quotient O(4), using the nonzero derivative of the separate primal line H and a degree-seven invariant-divisor bound. That image has full constant span V18*, giving an actual fifteen-dimensional constant realization of K^-. No quotient is given an unjustified connection, and no coherent image is silently replaced by its saturation.

The proof stops at the third jet and the stated restriction quotient. It does not claim fourth-jet separation, any longer osculating flag, algebraicity, realization, or a new whole-branch exclusion. Both retained F18 splitting alternatives remain unexcluded here, and the original defect remains t=0.
