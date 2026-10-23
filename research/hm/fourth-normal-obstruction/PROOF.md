# The invariant plane section fails at normal order four

Work over C with the actual normalized HM bundle F, B=End0(F), positive fixed plane R, and I=I_R. The notation mR means the ordinary ideal-power thickening O/I^m. Retain the binary-icosahedral representations W,A,V,P,D of the immutable inputs: A=Sym²W and V are the distinct three-spaces, P has dimension four, and D=Sym⁴W has dimension five. All even representations used here are self-dual and have invariant nondegenerate symmetric forms.

## 1. Result and immutable inputs

The unique invariant section of B(4) on 3R extends uniquely to 4R, but its boundary at 5R is nonzero. Thus

    H0(3R,B(4))^G = H0(4R,B(4))^G = C,
    H0(mR,B(4))^G = 0 for every m≥5.

In the notation of PR952 the lower transgression α:C→C is an isomorphism and β has zero target. This decides the order-four versus order-six alternative of PR955. It does not determine the rank of the top 2→2 map σ, the actual opposite-bundle splitting row, or the vertex extension scalar.

The proof uses no selected actual HM coefficients, points, jets, derivatives, matrices, ranks, or scans. Its contradiction is between a constant subbundle and the degree of an authenticated first-cup kernel bundle.

All repository inputs are from Akilleez-QA/read-em-and-weep. INPUTS.json gives exact commit, path, and Git-blob identities. The relevant inputs are:

- FINITE: PR955 at bd92a1ad858323966b0596f7b92474ca1766f1a2, research/hm/finite-plane-neighborhood/PROOF.md. This identifies the unique 3R candidate, its first boundary α*, its one-dimensional target, and injectivity of every later invariant restriction.
- STEINER: research/hm/order-four-quadratic-load/HYPERPLANE-SQUARE-SURVIVORS.md at db51525015bb7c5e825833d550d08dedf6f6ea96. The actual stable plane bundle has the fiberwise exact presentation

      0→A O_R(-3)→D O_R(-2)→F_R→0,

  and H0(B_R(3))=Sym²D. The cohomology identity H0(B_R(2))=Λ²A≅A is derived from that presentation in POLAR.
- FIRST and SECOND: ODD-FIRST-SCALING-OBSTRUCTION.md and ODD-SECOND-SCALING-OBSTRUCTION.md in the same immutable directory and commit. The actual invariant second-normal class ζ is nonzero; its coefficient image is an A-summand of H1(B_R(-2)). The actual commutator cup is surjective in each negative direction. Over T=P(W*) this gives

      0→K→H0(B_R(3)) O_T→H1(B_R(1)) O_T(2)→0,
      rank K=9, deg K=-12.                         (1)

  FIRST Sections3,6,7 authenticate the commutator and its surjectivity; SECOND Sections5,6 authenticate the bundle family and degree. This proof uses the actual maps, not arbitrary maps with the same characters.
- POLAR: PR952 at13d0e53e0a64ec6935a2ca83af776942e201c4e9 supplies H0(B_R(2))=Λ²A≅A, H1(B_R)=V⊕P⊕D, and the α,β notation.

The one external theorem used is Grauert–Mülich: a stable normalized rank-two bundle E on complex projective space restricts to O⊕O(-1) on a general line when c1(E)=-1. Original: H. Grauert and G. Mülich, Manuscripta mathematica16(1975),75–100, DOI https://doi.org/10.1007/BF01169064. A publicly readable precise statement is M. Schneider, “Holomorphic vector bundles on Pn,” Séminaire Bourbaki530, Theorem5.1, printed p97 (PDF page19), https://www.numdam.org/article/SB_1978-1979__21__80_0.pdf. We apply it only to the stable rank-two F_R with c1=-1. No special-line splitting is assumed.

## 2. An injectivity lemma for multiplication of plane sections

Put S=H0(B_R(2))≅A and U=H0(O_R(1))≅V. The multiplication map is

    m:S⊗U→H0(B_R(3)).                              (2)

We prove it is injective. This is a universal consequence of the displayed equivariant Steiner presentation, its fiber injectivity, and stability of F_R.

The character identity A⊗V=P⊕D is multiplicity-free. Thus a nonzero kernel of (2) contains P or D. Let ev:S O_R→B_R(2) be section evaluation. Any subspace J⊂ker m gives a sheaf map

    J O_R(-1)→S O_R --ev--> B_R(2)

whose composite is zero. If the first map is generically onto S O_R, all the sections in S vanish on a dense open set and hence globally, an impossibility.

First exclude J=D. Dualizing and twisting the Steiner sequence gives a surjection

    D* O_R(-1)→A* O_R.                              (3)

Its coefficient tensor is a nonzero equivariant embedding D*→A*⊗U. After choosing any equivariant isomorphism S≅A*, multiplicity one of D in S⊗U identifies this tensor with the D-subspace of S⊗U, up to a nonzero scalar. Consequently its evaluation map is (3), everywhere surjective. This contradicts the preceding paragraph. Thus D is not in ker m.

Now suppose P⊂ker m. For a general point x∈R=P(U*), the contraction

    P⊂S⊗U → S

with x cannot have rank three. Choose a nonzero a∈S* annihilating its image. Then

    a⊗x ∈ P^⊥⊂S*⊗U*,                             (4)

and P^⊥ is exactly the unique D-summand. Fix equivariant isomorphisms S*≅A* and U*≅U, the latter provided by the invariant nondegenerate symmetric form on V. They send (4) to a nonzero decomposable tensor a'⊗ℓ in the unique D-subspace of A*⊗U. By multiplicity one this subspace is the image of the dual Steiner coefficient embedding in (3). Hence there is nonzero d∈D* with

    t*(d)=a'⊗ℓ.                                    (5)

Here t* is the coefficient embedding of the dual of A O(-1)→D O→F_R(2). On the line L=(ℓ=0), equation(5) says that the constant functional d:D O_L→O_L annihilates A O_L(-1). It therefore descends to a surjection

    F_R(2)|L→O_L.                                  (6)

Surjectivity is literal: d is a fixed nonzero linear functional and hence D O_L→O_L is onto. Because U*≅U is a linear isomorphism, general x produces a general line L; no selected point or line is evaluated.

Grauert–Mülich gives F_R(2)|L≅O_L(2)⊕O_L(1) on a general line. There is no nonzero homomorphism from either positive line bundle to O_L. This contradicts (6), excluding P. Both possible irreducible kernel summands have now been excluded, so (2) is injective and its image is a nine-dimensional constant subspace of H0(B_R(3)).

## 3. The first invariant obstruction detects the entire plane cup

Write Z≅A for the coefficient subspace of H1(B_R(-2)) determined by the actual nonzero ζ. Define the actual plane commutator pairing

    μ:Z⊗S→H1(B_R),   z⊗s↦[z,s].                   (7)

It is equivariant. Since A⊗A=1⊕A⊕D while H1(B_R)=V⊕P⊕D, (7) has only one possible channel, the multiplicity-one D-channel.

The invariant leading section e on 3R is the nonzero tensor in Sym²W⊗S, and ζ is the nonzero tensor in Sym²W⊗Z. Both identify the dual of N=Sym²W with their respective A-spaces. The boundary at normal degree four is obtained by applying (7) to their coefficients and multiplying the two degree-two normal polynomials:

    α*(e) = mult_N [ζ,e]
      ∈ (Sym⁴W⊗H1(B_R))^G.                         (8)

Indeed choose projective frames relative to the unique first-normal comparison. The quadratic change of transition functions acts on an adjoint section by commutator. Since e starts at normal degree two, its first gluing defect has degree four and is exactly [ζ,e]. Terms of transition degree four or higher contribute only at section degree six or higher. Odd layers have no invariant contribution. This is the same Čech derivation as FIRST Section3, with the section degree shifted from zero to two. It preserves the actual bundle rather than replacing its formal neighborhood by a split one.

There is no hidden zero recoupling in (8). Normal multiplication N⊗N→Sym⁴W=D is the nonzero projection onto the unique D in A⊗A. Under the two invariant tensors e and ζ, contraction in (8) pairs this projection with the D-channel of μ by the nondegenerate invariant duality on that irreducible summand. Equivalently it is the composition of the D-inclusion dual to normal multiplication with μ, up to nonzero scalar identifications. By Schur's lemma it is nonzero exactly when μ is nonzero. Thus

    α=0  if and only if  μ=0.                       (9)

This argument uses the actual nonzero ζ and the actual nonzero candidate e; representation multiplicity alone would not justify (9).

## 4. A negative-degree kernel excludes vanishing of μ

Assume μ=0. The commutator cup is O_R-linear in the section coefficient. Therefore for every plane linear form ℓ∈U, section s∈S, and coefficient z∈Z,

    [z,ℓs]=ℓ[z,s]=0 in H1(B_R(1)).                 (10)

In particular the nine-dimensional image M=im(m) of Section2 lies in the kernel of the actual first cup for every negative direction λ∈T. Formula(1) then gives an inclusion

    M O_T → K

whose composition with K→H0(B_R(3)) O_T is the fixed constant inclusion. It is injective on every fiber. Both bundles have rank nine, so this is an isomorphism, and deg K=0. But the authenticated exact sequence(1) gives deg K=-12. This contradiction proves μ≠0.

By (9), α and its dual α* are nonzero maps between one-dimensional spaces, hence isomorphisms. The exact sequence in FINITE identifies ker α* with H0(5R,B(4))^G, so that space is zero. Its unique 3R candidate reaches 4R because the intervening layer is odd, and fails precisely at order four. All subsequent invariant restriction maps are injective by FINITE, proving H0(mR,B(4))^G=0 for every m≥5.

## 5. Contribution and remaining boundary

This selects one branch of the formerly unresolved actual order-four/order-six alternative by a structural contradiction, not a scalar calculation. It also identifies its root cause as the nonzero plane Lie-cup μ. In the polar filtration α is an isomorphism, H2(K6)^G=0, H1(K6)^G=0, and β has target zero. Hence the later canonical two-space H1(K10)^G is canonically identified with H1(G8)^G via the actual short exact sequences and the intervening invariant-acyclic layers. No splitting of the filtration or formal bundle is asserted.

The top σ and vertex Gysin scalar remain undetermined. Nothing here changes the source/frontier ledger or evaluates an actual HM instance.
