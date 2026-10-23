# The actual negative-coordinate symmetric string and a weighted kernel presentation

Work over C with G=SL2(F5). Write H=V⊕W for the coordinate representation, with W the negative two-space, A=Sym2 W, S=Sym3 W, D=Sym4 W and T6=Sym5 W. All cohomology and multiplication maps below are the actual HM ones. No selected actual coefficient, point, parameter, jet, derivative, matrix or instance rank is evaluated.

## 1. Immutable inputs and result

INPUTS.json authenticates four exact originals in Akilleez-QA/read-em-and-weep:

- STEINER, PR1045 at 47d2832dd306f26eabcfa2a57450cea982c5a153, research/hm/global-steiner-reduction/PROOF.md: the unique W subspace U1⊂H1(B(1))_- maps under all negative coordinates onto the unique A subspace U2⊂H1(B(2))_+. This is the nonzero symmetric projection W⊗W→A, with its determinant relation zero. The same proof pins the current normalized monad and its K-class used below.
- SYMMETRIC, PR456 at 07c11a096970a58f5f275b1438d4df3a27a1c6dd, research/hm/symmetric-evaluation/PROOF.md: h0(F(3))=4, and actual natural multiplication Sym2 H0(F(3))→H0(B(5)) is an isomorphism.
- ACTUAL, commit db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, Section1: actual negative multiplication has the exact sequence of bundles on T=P(W*)

      0→E→M3 O(-1)→M4 O→0,
      M3=H1(B(3))_-=3W'+3S+6T6,
      M4=H1(B(4))_+=2V+4P+3D.                         (1)

  In particular the last map is onto on every fiber, and E has rank17 and degree−54. This is not a generic-rank hypothesis.
- QUADRIC, commit eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c, research/hm/order-four-quadratic-load/POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md: H0(B(4))=0. Its further invariant-quadratic assertions are not needed to prove the new string.

We prove canonical actual subspaces

    U1≅W, U2≅A, U3≅S, U4≅D in H1(B(1)),...,H1(B(4)),

such that negative-coordinate multiplication is, after one coherent scalar normalization, the usual symmetric multiplication at each step. In particular U3 and U4 select definite multiplicity lines in the three S and three D copies of (1).

A consequence is a new actual presentation of the same kernel E:

    0→E→D O(-2)⊕(3W'+2S+5T6) O(-1)
          →(2V+4P+2D) O→0.                            (2)

The displayed splittings use explicit complement choices; the maps are inherited from (1). No remaining source-pair or quotient type is selected or excluded.

## 2. Actual degree-five sections have no negative part

We first prove, rather than assume, the joint-kernel vanishing needed below. Use the current monad labels from STEINER. Put Nmon=A⊕W', L2=Λ2 H, and

    c_-1=-Nmon, c_0=W'⊗L2-Nmon,
    c_1=-W'⊗H, c_2=W'.

The normalized bundle has K-class Σ c_i O(i). Thus the fixed equivariant Euler character at twist3 is

    χ_G(F(3))=Σ_(i=-1)^2 c_i Sym^(i+3) H=P-W.           (3)

The bounded exact nine-class checker verifies this identity in the current labels. It is not a computation of a monad differential. The twist-three monad terms Nmon O(2), W'⊗Ω2(5), Nmon O(3) have no positive cohomology by the standard exterior Euler/Bott computation. Consequently Hq(F(3))=0 for q≥2, and (3) is [H0]-[H1]. Its positive P multiplicity forces P into H0. Since SYMMETRIC gives h0=4=dim P, this exhausts H0:

    H0(F(3))=P,  H1(F(3))=W.

The natural isomorphism from SYMMETRIC is equivariant. The identity B(5)=Sym2(F(3)) has no missing constant character: det F=O(-1), and G has no nontrivial characters. Therefore

    H0(B(5))=Sym2 P=1⊕P⊕D,
    H0(B(5))_-=0.                                    (4)

This uses actual symmetric-square exhaustion, not Euler characteristic alone. In particular χ(B(5)) is not being mistaken for its space of sections.

## 3. Two joint-negative multiplication kernels vanish

Let R=P(V)⊂P(H) be the common zero plane of the two negative coordinates. The coordinate Koszul sequence, tensored by the locally free B(k+2), is

    0→Λ2W⊗B(k)→W⊗B(k+1)→I_R B(k+2)→0.                (5)

Identify Λ2W with C using the determinant pairing. The left cohomology map is, up to interchange/sign of the two components, simultaneous multiplication by both negative coordinates. Its kernel is the image of H0(I_R B(k+2)).

For k=2, this section space is zero because it embeds in H0(B(4))=0. Hence

    H1(B(2))→W⊗H1(B(3)) is injective.                 (6)

For k=3, H0(I_R B(5))_- embeds in H0(B(5))_-=0 by (4). Exactness of finite-group invariants/eigenspaces then gives

    H1(B(3))_-→W⊗H1(B(4))_+ is injective.             (7)

No assertion is made that the full, parity-unrestricted degree3 joint kernel vanishes. No chosen negative linear form is used: (6) and (7) concern the complete two-coordinate map.

## 4. Ring commutativity gives a canonical symmetric string

Choose any G-isomorphism W→U1. STEINER proves its degree-two determinant relation is zero and its symmetric part is nonzero onto U2. Since cohomological multiplication is an action of the commutative polynomial ring, all multiples of that determinant relation remain zero.

The universal binary Koszul identity

    Sym^(d-2)W⊗Λ2W→Sym^(d-1)W⊗W→Sym^dW→0

therefore gives well-defined compatible maps

    f_d:Sym^dW→H1(B(d)),    d=1,2,3,4,                (8)

whose images are the degree-d negative-coordinate descendants of U1. Their compatibility is precisely multiplication Sym^dW⊗W→Sym^(d+1)W. Here f1 and f2 are nonzero by STEINER.

If f3 were zero, every element of U2 would be annihilated by both negative coordinates, contradicting (6). Thus f3 is nonzero. Since Sym3W=S is irreducible, it is injective and defines the canonical actual U3=f3(S)⊂M3.

If f4 were zero, every element of U3 would be annihilated by both negative coordinates, contradicting (7). Thus f4 is nonzero and, since Sym4W=D is irreducible, injective. Define U4=f4(D)⊂M4. Changing the initial isomorphism W→U1 rescales every f_d by the same nonzero scalar, so neither image nor its multiplication structure changes. This proves the canonical string.

The earlier suggested invariant-quadratic argument Q(U1)=0 is not counted as new: M3 contains no W, so it already follows from equivariance alone. The new information is nonvanishing of the subsequent complete negative-coordinate maps and the actual selected S/D multiplicity lines.

## 5. Remove the selected S-to-D subcomplex

Restrict (1) to the canonical source U3 O(-1). Its image lies in U4 O, and (8) identifies the map with multiplication of a binary cubic by the parameter linear form. The universal evaluation sequence is

    0→S O(-1)→D O→O(4)→0.                           (9)

It injects on every fiber. Hence U3 O(-1) meets E trivially, and quotienting the actual subcomplex in (1) gives an exact sequence

    0→E→(M3/U3) O(-1)→Z→0,
    Z=(M4 O)/(U3 O(-1)).                            (10)

The canonical selected D gives 0→O(4)→Z→(M4/U4) O→0. Choose an equivariant constant complement to U4 in M4. This identifies, noncanonically,

    Z≅O(4)⊕(2V+4P+2D) O,
    M3/U3=3W'+2S+6T6.                              (11)

These are actual quotient maps and a chosen target splitting, not replacements based solely on characters. The map in (10) is onto everywhere because (1) is.

For every such target complement, projection of (10) onto O(4) is onto. Its Hom space from a constant representation R twisted by−1 is Hom_G(R,Sym5W). Thus only the six T6 copies contribute, through a nonzero multiplicity functional and the complete quintic evaluation

    T6 O(-1)→O(4).

Its kernel is D O(-2), by the binary evaluation sequence. Choosing a complementary T6 multiplicity direction displays the full source kernel as

    D O(-2)⊕(3W'+2S+5T6) O(-1).                     (12)

Such a complement is not canonical. Equivalently the extension of D O(-2) by the unused constant-twisted source splits because H1(O(1))=0. Taking the kernel of the target projection in (10) proves (2). Its final map is still onto on every fiber, with kernel the original E.

The weighted source has rank49 and degree−54: the D block contributes rank5 and degree−10, and the remaining block has rank44 and degree−44. Its constant target has rank32, so the kernel retains rank17 and degree−54. Nothing in this construction evaluates the nonzero functional on the six T6 copies or discards the remaining actual off-diagonal maps.

## 6. Scope and contribution

The theorem applies to the actual multiplication module before any of the remaining source-pair alternatives is selected. Thus every such alternative must carry this canonical W→A→S→D string and the inherited weighted presentation (2); no separate source-instance test is used. It does not change the four-pair ledger, prove any source realization, decide the opposite bundle, or determine a smoothing or vertex scalar.

The substantive new data are the actual selected S and D subspaces, the universal multiplication structure between them, and the forced quintic functional leading to the weighted source. Joint-negative injectivity was justified by actual section exhaustion and Koszul geometry, not presumed from a character match. The bounded verifier checks representation identities and degree bookkeeping only; the exact sequences and actual-map inheritance require mathematical proof and independent review.
