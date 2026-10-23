# The unique invariant third-neighborhood section cannot reach the seventh

Work over C. Let F be the actual normalized HM bundle, B=End0 F, R its positive fixed plane, I=I_R, p:X=Bl_R(P4)→P4, and E the exceptional divisor. Write mR for the ordinary scheme defined by I^m, not a symbolic thickening or a split normal bundle.

This is a corollary of PR952 at commit13d0e53e0a64ec6935a2ca83af776942e201c4e9 in Akilleez-QA/read-em-and-weep, research/hm/exceptional-polar-obstruction/PROOF.md, independently reviewed and byte-authenticated with SHA25603f7909a73ebe2cd2ff7c8639f3bea3384741058297156f51f38b2b6094354e6. INPUTS.json records its exact immutable Git-blob identity. Its exact geometric inputs and binary representation conventions are retained unchanged. No selected actual HM coefficient, point, parameter, derivative, matrix or instance rank is evaluated.

## 1. Statement

There is exactly one invariant section on 3R, up to scalar:

    H0(3R,B(4)|3R)^G = C.

It is supported in the last ideal layer I²/I³ and comes from

    (Sym²W ⊗ H0(B_R(2)))^G=(A⊗A)^G=C.

But

    H0(7R,B(4)|7R)^G=0.                         (1)

The restriction maps H0((m+1)R,B(4))^G→H0(mR,B(4))^G are injective for every m≥3. The unique nonzero section on3R therefore fails to extend either from4R to5R or, if it extends to5R, from6R to7R. These are actual ordinary normal orders4 and6. No earlier odd-order obstruction can occur in the invariant sector.

More precisely, if α:C→C and β:C²→coker α are the actual polar connecting maps of the prior theorem, the first obstruction is α*, and if α=0 the second is β*. The first target has dimension one; the second target has dimension two. The proved rank relation rankα+rankβ=1 forces this finite nonextension. We do not decide which order occurs.

## 2. Exact duality between polar sheaves and ordinary thickenings

For j≥2 set

    L_j=R1p_*O_X(jE),    K_j=B(-9)⊗L_j.

The exceptional-polar theorem proves H2(K4)^G=C and H2(K8)^G=0. We identify the duals of these actual cohomology spaces with ordinary-thickening sections, rather than replacing the polar filtration by its associated graded.

The morphism p is proper between smooth fourfolds and ω_X=p*ω_P4⊗O(E). Its dualizing functor therefore satisfies p!O_P4=O_X(E). Standard blowup direct images give

    p_*O_X(jE)=O_P4,
    Rq p_*O_X(jE)=0 for q≥2,
    Rp_*O_X(-(j-1)E)=I^(j-1)  in degree zero.    (2)

The last assertion includes higher-direct-image vanishing for nonnegative ideal powers; it follows on the standard affine blowup charts, or from relative Proj and fiber cohomology for the blowup of the regular codimension-two ideal.

The natural unit inclusion O_X→O_X(jE) yields the actual triangle

    O_P4 → Rp_*O_X(jE) → L_j[-1] → O_P4[1].     (3)

Grothendieck duality applied to the middle term gives

    RHom(Rp_*O_X(jE),O_P4)
       =Rp_*O_X((1-j)E)=I^(j-1).

Under this identification the dual of the first arrow in(3) is the natural ideal inclusion I^(j-1)→O_P4: it is dual to multiplication by the canonical exceptional section to the jth power, with the relative dualizing O(E) retained. Thus dualizing(3) gives

    RHom(L_j,O_P4)[2] ≅ O_P4/I^(j-1),
    RHom(K_j,ω_P4) ≅ B(4)|((j-1)R)[-2].        (4)

Here B*=B and ω_P4=O(-5); hence the twist is9−5=4, and the ordinary thickening index is j−1, not j or j−2. All identifications are equivariant; determinants of W and of the ambient representation are trivial.

Applying global Serre duality to(4) gives canonical isomorphisms

    H2(P4,K_j)^{G,*} ≅ H0((j-1)R,B(4))^G.      (5)

There is no contribution from other sheaf Ext degrees: (4) is an actual derived identification concentrated in sheaf Ext degree two. This also verifies the Cohen–Macaulay duality involved without assuming a split formal neighborhood.

For j4 and j8, (5) proves both dimensions in Section1 directly from the prior theorem.

## 3. Identifying the unique candidate and the obstruction orders

The actual ordinary-thickening sequences have graded layers

    I^k/I^(k+1) ⊗ B(4)
      =Sym^kW ⊗ B_R(4-k).                       (6)

The center acts on layer k by(-1)^k. Odd layers therefore have no invariant cohomology. The plane cohomology from the Steiner resolution gives:

- k0: H0(B_R(4))^G=0;
- k2: invariant H0=(A⊗A)^G=C, and H1=0;
- k4: H0=0, invariant H1=(D⊗(V+P+D))^G=C;
- k6: H0=0, invariant H1=((V+P)⊗(A+V+P+D))^G=C².

The first invariant candidate thus lies in the subsheaf I²B(4)/I³B(4) of B(4)|3R. Since lower layers have no invariant sections, this supplies the whole one-dimensional H0(3R)^G. There are no new invariant H0 layers for k≥3 because B_R(4-k) has no sections for k≥3, using the established H0(B_R(1))=0 and stability in twists≤0. This proves injectivity of subsequent restriction maps.

Passage from3R to4R and from5R to6R is an isomorphism on invariant H0 because the new layer is odd. Passage from4R to5R has its actual boundary to the one-dimensional k4 H1 group. If this boundary vanishes on the candidate, its unique extension reaches5R and6R. Passage from6R to7R then has actual boundary to the two-dimensional k6 H1 group. Equation(1) forces that boundary to be nonzero on the surviving line.

For map orientations, dualizing the actual polar short exact sequence by sheaf Ext²(-,ω_P4) gives the actual ordinary-thickening sequence

    0→i_*(Sym^(j-2)W*⊗B_R(6-j))
      →B(4)|((j-1)R)→B(4)|((j-2)R)→0.

This follows from (4) and Ext²(i_*G_j,ω_P4)=i_*(G_j*⊗ω_R); all other sheaf Ext degrees vanish. Thus j6 and j8 give exactly normal layers4 and6, with compatible boundary signs. In particular naturality of(4) sends L_(j-1)→L_j to the restriction O/I^(j-1)→O/I^(j-2). Thus the polar H2 maps dualize to the ordinary restriction maps. The polar exact segment at j6 is

    H1(G6)^G=C --α--> H2(K4)^G=C → H2(K6)^G→0,

where odd steps have been identified only on invariant cohomology. Its dual is

    0→H0(5R,B4)^G→H0(3R,B4)^G --α*--> C.

At j8 the dual of β is the second obstruction

    H0(5R,B4)^G=(coker α)* --β*--> C².

If α=0, the prior theorem makes β a rank-one surjection, so β* is injective and the candidate cannot reach7R. This verifies the directions and identifies the two obstruction orders without assigning their actual scalars.

## 4. Contribution and boundary

The prior polar theorem forced one lower transgression to be nonzero. This corollary identifies exactly what that nonvanishing excludes: the actual unique invariant section of B(4) on the third ordinary neighborhood cannot extend to the seventh. Its failure is necessarily at normal order four or six, with target dimensions one or two respectively. This is a finite-neighborhood exclusion, not merely a restatement that global H0(B(4)) vanishes or a claim about infinite formal algebraization.

No claim identifies the first failing order, determines the opposite-pencil bundle row or vertex scalar, or changes the source/frontier ledger. The order here is explicitly an ordinary power of I_R, unlike the prior parameter-line twist -12.
