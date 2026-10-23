# Marked opposite incidence as an actual positive Koszul transgression

Work over C, with G=SL2(F5), negative doublet W, positive coordinate space V, A=Sym2 W, S=Sym3 W, T6=Sym5 W, and T=P(W*). Put X=Bl_R(P4), where R is the positive fixed plane, with p:X→P4 and π:X→T. Write B=End0(F) for the actual normalized HM bundle. All maps below are actual multiplication maps; equivariant model identifications may be rescaled but images and zero assertions are intrinsic.

## Immutable inputs

- PR1038, e567a431830f6dd37fe5fd2a65e24fc1210eedb3, research/hm/global-ninth-bridge/PROOF.md: π_*p*B(2)=0, Jg=(R1π_*p*B(2))_+, and its complete evaluation presentation.
- PR1045, 47d2832dd306f26eabcfa2a57450cea982c5a153, research/hm/global-steiner-reduction/PROOF.md: the canonical L=O(2)⊂Jg is represented by the actual subcomplex W O(-1)→A O, with quotient L. The W and A coefficient spaces each occur once.
- PR1060, 13acb1a85a38e9d236069f41b21dd4cef70ab056, research/hm/positive-joint-embedding/PROOF.md: positive V multiplication embeds the original marked T6=V W in H1(B(2))_-, and its actual negative pencil is T6 O(-1)→(P+D)O with quotient V O(2). It is the V-multiple of the preceding W/A subcomplex, by mixed commutativity.
- PR1062, 2a7565f5828447907ad860c861891ec2fdb4f7cb, research/hm/double-mixed-block/PROOF.md, and PR1067, 0201d67280fbfe0f87c84e7e726c3dc6c12bbecb, research/hm/weighted-incidence-line/PROOF.md: the original marked multiplicity line k_mark lies in the two-dimensional K; the actual η:K⊗V O(2)→C has nonzero multiplicity functional and kernel line K0. Here C=(R1π_*p*B(3))_+.
- db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md: (π_*p*B(3))_+=A O(-6).
- The same commit, research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: the actual source kernel E has exact presentation 0→E→M3 O(-1)→M4 O→0, with M3=3W'+3S+6T6 and M4=2V+4P+3D.
- eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c, research/hm/order-four-quadratic-load/POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md: H0(B(4))=0. It also implies H0(B(3))=0 by multiplication with a nonzero linear form.

- PR945, 089003175d9e31a7cf6288ab7a9e3ac4d66a3e63, research/hm/exceptional-adjoint-exhaustion/PROOF.md: all hyperplanes have exactly three positive B_H(3) sections, and the actual A O(-6) base-change map is an isomorphism everywhere, including the exceptional orbit.

## 1. The actual marked bridge

Positive-coordinate multiplication on X induces a natural map V⊗Jg→C. Its adjoint is j:Jg→V*⊗C. The standard incidence resolutions for B(2) and B(3) commute with multiplication by positive coordinates, since polynomial multiplication commutes before applying cohomology. Thus on complete presentations they give the same square as global mixed multiplication.

Restrict this square to W O(-1)→A O from PR1045. PR1060 identifies its V-multiple with the original marked T6 O(-1)→(P+D)O, not merely an abstract block of the same type. Passing to cokernels therefore identifies V⊗L→C with η restricted to k_mark⊗V O(2). Consequently

    k_mark=K0  if and only if  j|L=0.                 (1)

This uses the original marked embedding, not any later T6 copy selected during opposite-pencil reduction.

## 2. The source E is the degree-four direct image

The universal hyperplane sequence for B(4) has first term B(3)⊗O_T(-1). Since H0(B(3))=H0(B(4))=0, its direct-image sequence identifies

    (π_*p*B(4))_+ = ker[M3 O(-1)→M4 O] = E.         (2)

The central parity of O(-1) changes the negative H1(B(3)) coefficient space M3 to the positive direct-image part. This is an identification of actual maps with the source presentation, not a rank-degree comparison.

## 3. Relative Koszul transgression

The three positive coordinates cut a section Z≅T in X: each negative hyperplane meets the negative vertex line in one point, and this line is disjoint from the blowup center R. Locally the three coordinates form a regular sequence, also at Z. Their Koszul complex, tensored with p*B(2), is

    p*B(2) → Λ2V⊗p*B(3) → V⊗p*B(4) → p*B(5),     (3)

in degrees -3,-2,-1,0, after identifying Λ3V with the trivial line. It resolves p*B(5)|Z in degree zero. Hence its derived π-image has no negative cohomology. This remains true after taking central positive eigenspaces. No parity assumption on the point-supported term is needed.

The positive q=0 row of the hypercohomology spectral sequence begins

    0 → V*⊗A O(-6) --a--> V⊗E --b--> D,
    D=(π_*p*B(5))_+.                              (4)

Here Λ2V≅V*≅V. The first map a is the actual Koszul differential, not plain multiplication without its exterior signs. It is injective on every fiber: the Koszul complex is exact before its last term, and H0(B_H(2))=0; thus the first nonzero H0 differential is injective. The A O(-6) base-change isomorphism at every fiber is supplied by PR945, not inferred merely from local freeness. For E, the universal restriction sequence and the everywhere surjective actual M3 O(-1)→M4 O presentation identify its fibers with the degree-four section kernels: the kernel sequence remains exact after tensoring with every residue field. Thus E also has the required H0 base-change identification. Therefore a is a subbundle embedding. Define H=coker(a), and let bbar:H→D be induced by b.

In the q=1 row, the first differential is exactly j:Jg→V*⊗C. Write J=ker(j) and H2=ker(bbar). The spectral-sequence differential

    d2:J→H2                                             (5)

is a natural isomorphism. Indeed its source has position (-3,1), its target (-1,0). There is no incoming differential to the source, and its only possible higher outgoing differential is this d2. The target has no higher outgoing differential and no other possible incoming differential. Both total degrees, -2 and -1, are negative, so their limiting terms vanish. This proves both injectivity and surjectivity. It does not require H0(B_H(4))=0 or any additional vanishing of higher direct images.

## 4. A one-dimensional input detector on the original source

First,

    Hom_G(O(2),D)=0.                                  (6)

To see this without calculating D, the universal hyperplane sequence for B(5) gives an exact sequence with left term H0(B(5))_+ O and right term a subsheaf of H1(B(4))_- O(-1). More precisely D is an extension of that kernel subsheaf by the quotient of H0(B(5))_+ O by the image of H0(B(4))_- O(-1); the latter image is zero because H0(B(4))=0. Neither a constant bundle nor a subsheaf of a sum of O(-1)'s admits a map from O(2). This proves (6). Consequently Hom_G(O(2),H2)=Hom_G(O(2),H).

Also Hom(O(2),V⊗E)=0, since E embeds into M3 O(-1). Applying equivariant Hom(O(2),−) to the short exact sequence defining H gives

    Hom_G(O(2),H)=ker Δ,
    Δ:Ext1_G(O(2),V*⊗A O(-6))→Ext1_G(O(2),V⊗E),     (7)

where Δ is induced by the actual Koszul differential a. The domain is canonically a one-dimensional vector space:

    Ext1_G(O(2),V*⊗A O(-6))
       =Hom_G(V,A⊗Sym6 W)=C,                         (8)

because Sym6 W=V+P and A(V+P)=V+2P+2D.

The complete global presentation further gives Hom_G(O(2),Jg)=C, generated by L→Jg. In fact twisting its presentation by O(-2) identifies these invariants with the invariant part of H1((W+2S+3T6)O(-3)), which is one-dimensional; the next term H1((A+2V+3P+4D)O(-2)) has no invariants. Since L supplies a nonzero element, it generates that space.

Combining (1), (5), (6), and (7) therefore proves the actual map-level equivalence

    k_mark=K0  ⇔  j|L=0  ⇔  Δ=0.                    (9)

If Δ is nonzero, its one-dimensional domain makes it injective, and the original marked V O(2) has nonzero image in C. If Δ=0, d2 identifies the unique marked O(2) direction with the unique equivariant O(2) direction in H2. This is a natural lifting/transgression statement; it does not choose a splitting of E or identify repeated representation labels.

For size only, the target of Δ has dimension4. Twisting the exact E presentation by O(-2) gives

    0→H1(E(-2))→M3⊗W→M4→0.

Here M3 W=3A+6V+9P+9D, so H1(E(-2))=3A+4V+5P+6D has V multiplicity4. Hence Ext1_G(O(2),V⊗E)≅C4 abstractly. The detector is one-dimensional-input, not a scalar endomorphism of a specified line; no basis or actual value is selected.

## 5. A quotient-free dual detector

Equivariant Serre duality on T, with omega_T=O(-2), identifies the dual of (7) with the restriction/contraction map

    Δ*:Hom_G(E,V* O)→Hom_G(V*⊗A O(-6),O).          (10)

For an equivariant f:E→V* O, its image is the composite of a with id_V⊗f and the evaluation pairing V⊗V*→C. The domain of (10) has dimension4 and its target dimension1, by the already proved dimensions and duality. Using the self-duality of V identifies the first space with Hom_G(E,V O), without choosing four numerical maps or a basis. Naturality of Serre duality makes (10) exactly the transpose of Δ, not a separately embedded representation channel.

Thus k_mark=K0 if and only if this entire restriction/contraction functional vanishes. This version uses only the original source E, its actual positive Koszul differential a and the invariant pairing; constructing H, H2 or a splitting of E is unnecessary. It selects no value of the functional.

## 6. Contribution and limit

This resolves the missing bridge from the original positive descendant to opposite weighted incidence, and transfers that incidence to a specific natural map on the original degree-four source E. It also isolates the exact obstruction to the tempting joint-injectivity argument on hyperplanes: the nonzero degree-four section bundle E supplies a possible d2 transgression. Global H0(B(4))=0 cannot eliminate that relative bundle.

No value of Δ, source type, opposite row, actual coefficient, point, parameter, matrix, jet, derivative, or instance rank has been evaluated. No nonvanishing or incidence selection is claimed. All seven opposite necessary types and the surviving source-pair ledger remain unchanged. The proof is mathematical, not proof-assistant certification.
