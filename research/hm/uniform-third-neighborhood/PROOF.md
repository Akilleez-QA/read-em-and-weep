# Uniform third-neighborhood vanishing and an explicit next cohomology gate

Work over C with the actual normalized HM bundle F, B=End0(F), positive fixed plane R, and negative direction line T=P(W*). For λ∈T put H_λ=P(V⊕λ), and write mR_λ for the ordinary mth thickening of R inside H_λ. Thus its ideal is the mth power of the hyperplane ideal in H_λ, not I_R^m in P4. These schemes vary in the actual universal hyperplane family over T.

No selected actual HM coefficient, point, jet, derivative, matrix, rank, or scan is evaluated. The proof propagates the already proved nonzero actual Lie-cup to every direction by a unique representation channel and an authenticated bundle duality.

## 1. Result and exact inputs

For every λ and every m≥3,

    H0(mR_λ,B|H_λ(2))=0.                              (1)

All three sections on R are already obstructed at ordinary normal order TWO: the passage from 2R_λ to 3R_λ. This differs from PR967's normal-order-four obstruction for the invariant B(4) candidate, whose leading section itself has normal degree two.

Let E_m be the pushforward of B|H_λ(2) on the actual mR_λ family to R×T by the normal projection, and let q:R×T→T. Inversion has two eigensheaves E_m,+ and E_m,-. The complete third-neighborhood derived cohomology is

    q_*E_3=R2q_*E_3=0,
    R1q_*E_3,+ ≅ V O(2) ⊕ P O(2) ⊕ W O(5),
    R1q_*E_3,- ≅ (A⊕V) O(1).                         (2)

The positive part has rank nine and degree24, and its indicated splitting is intrinsically determined up to scalar identifications of the irreducible factors. The full R1 has rank15 and degree30.

There is also an actual next even-cohomology gate

    Θ: T30 → (Sym²D) O(8),                            (3)
    T30 ≅ V O(2) ⊕ P O(2) ⊕ W O(5)
             ⊕ (A⊕V⊕P⊕D) O(4) ⊕ (A⊕V) O(6).

The source has rank30 and degree120; the target rank15 and degree120. Its source splitting is not claimed canonical. The derived pushforward of E_9,+ is represented by (3) in cohomological degrees one and two. Thus its actual H1 and H2 are the kernel and cokernel of this actual boundary, and the same two-term complex computes every fiber. No rank of Θ is selected.

All repository inputs are from Akilleez-QA/read-em-and-weep; exact commits, paths and Git-blob identities are recorded in INPUTS.json:

- FOURTH: PR967, commit39c5f4fbc012f4ec57ffc56d5de18cedb3571d60, research/hm/fourth-normal-obstruction/PROOF.md. Its Sections3–4 prove that the actual plane commutator

      μ: A⊗H0(B_R(2)) → H1(B_R)

  is nonzero, with only its multiplicity-one D-channel possible.
- SQUARE: commitdb51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/HYPERPLANE-SQUARE-SURVIVORS.md. It proves the actual everywhere-surjective coefficient family

      0→W O(-3)→D O→A O(2)→0.                       (4)

- FIRST: ODD-FIRST-SCALING-OBSTRUCTION.md in that same commit and directory. Sections3,6,7 authenticate the actual commutator boundary and the nonzero coefficient class ζ, identify its A-channel with y_a:D→A, and prove y_a surjective for every a≠0.
- POLAR: PR952, commit13d0e53e0a64ec6935a2ca83af776942e201c4e9, research/hm/exceptional-polar-obstruction/PROOF.md. The actual stable plane Steiner resolution gives

      H0(B_R(2))=A,       H1(B_R(2))=0,
      H0(B_R(t))=0 for t≤1,
      H1(B_R(1))=A⊕V,    H1(B_R)=V⊕P⊕D,
      H1(B_R(-2))=A⊕V⊕P⊕D,
      H1(B_R(-4))=A⊕V,  H1(B_R(t))=0 for t≤-5,
      H0(B_R(3))=Sym²D.

  Self-duality gives H2(B_R(t))=H0(B_R(-t-3))*.

All O(d) in the bundle statements are on T with their standard equivariant linearizations. A=Sym²W, D=Sym⁴W, V is the other three-space, and P is the even four-space. The named irreducibles are self-dual.

## 2. The actual first cup is the twisted dual of y

The nonzero invariant ζ identifies the coefficient A-space with a summand of H1(B_R(-2)). Write S=H0(B_R(2))≅A. Since

    A⊗S = 1⊕A⊕D,       H1(B_R)=V⊕P⊕D,

FOURTH proves that the actual μ has a nonzero D-channel and no other channel. In the family of negative directions its evaluation is therefore the nonzero equivariant bundle map

    c: A O → (V⊕P⊕D) O(2),                         (5)

with image in D O(2). The space of such maps to that D summand is one-dimensional, since

    Hom_G(A,D⊗Sym²W)=C.

Dualize (4) and twist by O(2). Using self-duality yields the actual exact sequence

    0→A O --y^∨(2)--> D O(2)→W O(5)→0.           (6)

Its first arrow is nonzero in exactly the same one-dimensional Hom space. Thus the D block of (5) equals a nonzero scalar multiple of y^∨(2), after equivariant identifications. Consequently c is injective on every fiber and

    coker c ≅ V O(2)⊕P O(2)⊕W O(5).               (7)

The conclusion is about the actual cup, not an abstract map with its character: its nonzero scalar is supplied by FOURTH, and the comparison map is the authenticated y of SQUARE. No value of that scalar is chosen.

More generally, identifying both A-spaces by their invariant forms, μ_a:S→D is the transpose of y_a, up to one nonzero scalar. FIRST proves y_a onto for every nonzero coefficient a, hence every such μ_a is injective. The negative-direction conic provides the actual family used in (5).

## 3. Actual third-neighborhood cohomology

The complement of the negative fixed line has its normal projection onto R. Restricted to the mR_λ family it is finite over R×T. Its normal degree-k layer is

    B_R(2-k) ⊠ O_T(k).                              (8)

The degree-k layer has inversion sign (-1)^k. The projection identifies the ambient normal scheme, not the bundle F: none of the bundle extensions is assumed split.

The unique first-normal comparison and the actual quadratic transition class give the exact positive sequence on R×T

    0→B_R ⊠O(2)→E_3,+→B_R(2)⊠O→0.               (9)

The boundary on q-cohomology is exactly (5). This follows directly from the actual transition comparison: a section of B_R(2) changes in normal degree two by its commutator with ζ. Higher transition terms cannot contribute at this truncation. This is FIRST's actual Čech cup argument at the indicated twist.

Both ends of (9) have H2 zero, the left has H0 zero, and the right has H1 zero. Its q-cohomology sequence is therefore

    0→q_*E_3,+→A O --c--> (V⊕P⊕D)O(2)
      →R1q_*E_3,+→0,       R2q_*E_3,+=0.            (10)

Fiberwise injectivity of c and (7) prove the positive statements in (2). All resulting cohomology sheaves are locally free and commute with base change.

The negative eigensheaf has just its degree-one layer:

    E_3,- = B_R(1) ⊠O(1).

Its H0 and H2 vanish, while H1 is (A⊕V)O(1), proving the rest of (2). Hence the entire H0 on each actual third neighborhood vanishes.

For every further step, the new layer B_R(2-k) has H0 zero for k≥3. The exact ordinary-thickening sequence therefore makes H0((k+1)R_λ)→H0(kR_λ) injective. Induction proves (1), without requiring higher lifting obstructions to vanish. The plane sections do reach 2R_λ: the even part there is B_R(2), while its odd layer has H0 zero. They all fail at the quadratic step by the injective cup.

## 4. Intrinsic splitting at the third neighborhood

In (7), W O(5) is the maximal-slope Harder–Narasimhan subbundle, and the quotient is (V⊕P)O(2). Existence of an equivariant complement follows from (7). Its ambiguity would be

    Hom_G((V⊕P)O(2),W O(5))
      = Hom_G(V⊕P,W⊗Sym³W)=0,

because W⊗Sym³W=A⊕D. Thus the Harder–Narasimhan sequence has a unique equivariant splitting. The two quotient constituents V and P are distinct irreducibles, so their isotypic subbundles are also intrinsic. Scalar choices in identifying the named irreducibles remain; no unique scalar-normalized isomorphism is asserted.

## 5. The next nontrivial even H1 obstruction has an explicit source

For the positive eigensheaves, passage from 3R to 5R adds B_R(-2)⊠O(4); passage from 5R to 7R adds B_R(-4)⊠O(6). Odd intermediate layers have no positive part. Both added layers have H0 and H2 zero. Therefore their actual q-cohomology sequences are short exact sequences

    0→(A⊕V⊕P⊕D)O(4)→R1q_*E_5,+→R1q_*E_3,+→0,
    0→(A⊕V)O(6)→R1q_*E_7,+→R1q_*E_5,+→0.        (11)

Their H0 and H2 pushforwards vanish. These are actual extensions; nevertheless their underlying extension classes vanish on T. In the first sequence, the relevant line differences are 4-2=2 and 4-5=-1; in the second, they are 6-2=4, 6-4=2, and 6-5=1. All have H1(O(d))=0. Hence both sequences split as ordinary bundles, and averaging provides equivariant splittings. No uniqueness is asserted. This proves that R1q_*E_7,+ is the displayed T30 of (3).

Passage from 7R to 9R adds B_R(-6)⊠O(8). Its H0 and H1 vanish, and its H2 is

    H2(B_R(-6))O(8)=H0(B_R(3))*O(8)
                       ≅(Sym²D)O(8).

The actual cohomology boundary therefore gives precisely (3), with exact sequence

    0→R1q_*E_9,+→T30 --Θ--> (Sym²D)O(8)
      →R2q_*E_9,+→0.                                (12)

More precisely, the triangle from this actual short exact sequence identifies Rq_*E_9,+ with the two-term complex (3) in degrees one and two. Since the family and its layers are flat over T, its derived fiber at any λ is the cohomology of the actual 9R_λ. Thus fiber kernels and cokernels compute H1 and H2 without presuming constant rank or underived base change for (12).

The degree totals are 24+15·4+6·6=120 for T30 and15·8=120 for the target. This explicit source and target preserve the actual next boundary and its unknown rank; replacing its source by a trivial thirty-space is not allowed.

## 6. Contribution and boundary

The new exclusion is uniform and stronger than the earlier invariant scalar test: every actual direction kills every B_R(2) section at the first quadratic normal step. It determines the full third-neighborhood derived cohomology bundle and, using vanishing of ordinary Ext groups, supplies a concrete thirty-to-fifteen next H1 gate through the ninth neighborhood.

No rank of Θ, top polar σ, or secondary β is determined; no opposite-pencil row or vertex-extension scalar is selected. None of the actual sheaf extensions (9) or higher formal bundle transitions is declared split merely because some cohomology bundles split. The source/frontier ledger is unchanged.
