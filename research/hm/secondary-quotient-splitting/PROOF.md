# Canonical splitting of the rank-six secondary quotient and a forced nonzero extension

Work over C with G=SL2(F5), the actual normalized HM bundle F, B=End0 F, and the negative direction line T=P(W*). Every O(d) below is on T with its standard equivariant linearization. Set A=Sym2 W, D=Sym4 W, V=Sym2 W', and let P be the genuine even four-dimensional representation.

No selected actual coefficient, point, direction, matrix, derivative, or instance rank is evaluated. The argument uses exact actual bundle sequences and fixed abstract character arithmetic.

## 1. Immutable inputs

Both inputs are in Akilleez-QA/read-em-and-weep at commit db51525015bb7c5e825833d550d08dedf6f6ea96, under research/hm/order-four-quadratic-load/:

- HYPERPLANE-SQUARE-SURVIVORS.md, equations (6), (7), (8), (9), denoted SQUARE. It proves the actual everywhere-surjective quadratic map

      y: D O -> A O(2),       ker y = W O(-3),

  the actual square subbundle A O(-6) in the rank-nine first-cup kernel K, and the identification

      Q6 := K/(A O(-6))
         = ker[f:(Lambda2 A tensor V) O(2) -> (Lambda2 A) O(4)],   (1)

  where f is everywhere onto. It also factors the actual secondary boundary through Q6.
- ODD-SECOND-SCALING-OBSTRUCTION.md, theorem (2) and Section 6, denoted SECOND. It gives the exact actual first-cup sequence

      0 -> K -> H0(B_R(3)) O -> H1(B_R(1)) O(2) -> 0,            (2)

  with dimensions 9,15,6, respectively. In particular K is a subbundle of a trivial bundle.

INPUTS.json records exact original bytes, SHA256 and Git-blob identities. These statements retain their actual maps; no equal-dimensional substitute is introduced.

## 2. The actual quotient splits

The fixed character identities are

    Lambda2 A = A,      A tensor V = P + D,
    A tensor A = 1 + A + D.

In particular, with H0(O(2))=Sym2 W=A, the space of equivariant arrows in (1) is

    Hom_G(P+D, A tensor H0(O(2)))
      = Hom_G(P+D, 1+A+D) = C.                               (3)

The P coefficient block must vanish. The D coefficient block is a scalar multiple of y tensor O(2): the map y is a nonzero member of the same one-dimensional Hom space on D. This scalar is nonzero, since f is onto by the input. Any choices in identifying Lambda2 A with A or its multiplicity-one D constituent merely rescale these identifications and do not change the kernel.

Taking the kernel of the actual arrow therefore gives the equivariant decomposition

    Q6 = P O(2) directsum ker[y tensor O(2)]
       = P O(2) directsum W O(-1).                            (4)

The rank and degree are 4+2=6 and 4(2)+2(-1)=6, consistent with (1). This is an identification of the actual quotient, not only an abstract bundle of the same character or degree. The center acts positively on both summands: its negative character on W is canceled by that of O(-1).

## 3. Intrinsic positive part and uniqueness of the equivariant complement

The maximal-slope term of the Harder–Narasimhan filtration of (4) is precisely P O(2). Thus this rank-four subbundle is intrinsic to Q6, independently of the coefficient decomposition used to prove (4). Its quotient is W O(-1).

The difference between two splittings of this sequence is a homomorphism from W O(-1) to P O(2). Equivariantly this space is

    Hom_G(W, P tensor Sym3 W)=0,                              (5)

because W tensor Sym3 W=A+D has no P constituent (equivalently W tensor P=W'+T6 has no Sym3 W constituent). Hence the intrinsic Harder–Narasimhan sequence has a unique G-equivariant splitting, or equivalently a unique equivariant complementary subbundle.

This does NOT assert a unique isomorphism with a named direct sum: scalar automorphisms of its two irreducible factors remain. Nor is the ordinary nonequivariant complement unique; the ordinary Hom space in (5) before taking invariants has dimension 2 times 4 times 4=32.

## 4. The original K extension is necessarily nontrivial on the positive summand

Retain the actual sequence

    0 -> A O(-6) -> K -> Q6 -> 0.                             (6)

Pull it back along the canonical inclusion P O(2) -> Q6, and call its middle bundle K_P. If this pulled-back extension split, even nonequivariantly, it would supply an injection P O(2) -> K_P -> K. Composing with the injection (2) would give a nonzero map

    P O(2) -> H0(B_R(3)) O.

Every such map is zero, because H0(O(-2))=0. This contradiction proves that the actual extension over P O(2) is NONSPLIT. In particular the whole sequence (6) cannot split.

The equivariant extension spaces are determined exactly by fixed characters and ordinary Serre duality on T:

    Ext1_G(P O(2), A O(-6))
      = (P* tensor A tensor H1(O(-8)))^G
      = Hom_G(P tensor A, Sym6 W),       dimension 2;

    Ext1_G(W O(-1), A O(-6))
      = (W* tensor A tensor H1(O(-5)))^G
      = Hom_G(W tensor A, Sym3 W),       dimension 1.           (7)

Here determinants are trivial and all named representations are self-dual. The identities are

    P tensor A=V+P+D,      Sym6 W=V+P,
    W tensor A=W+Sym3 W.

Thus (6) has a nonzero actual component in the canonical two-dimensional P-extension space. Its component in the one-dimensional W-extension space is not determined. The proof selects no coordinate, scalar, or projective direction in either extension space. Nonvanishing is forced by the actual injection into the trivial bundle, not by an instance calculation.

## 5. Contribution and remaining boundary

The prior square-survivor theorem determined Q6's rank and degree and its actual kernel presentation (1). The new step identifies its complete equivariant splitting and its unique equivariant Harder–Narasimhan complement, then forces the P component of the original K extension to be nonzero.

The actual secondary map still has source Q6 as in (4), but neither its rank nor its kernel has been computed here. Splitting Q6 does not split K. The exact nonzero extension in Section 4 must remain in any reconstruction of the first-cup kernel. No global odd-quadric section, selected first failing normal order, opposite-pencil C splitting, vertex scalar, or source/frontier exclusion follows.
