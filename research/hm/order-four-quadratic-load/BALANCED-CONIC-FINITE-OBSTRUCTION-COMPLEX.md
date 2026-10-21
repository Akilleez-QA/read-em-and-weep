# Balanced-conic finite obstruction complex and staged excess gates

## Main deductions

Let Q vary in the nonempty open of smooth inversion-even quadrics for which the positive fixed conic C has balanced restriction F_C=O_P1(-1)^2. Put B=End_0(F), G=B_Q(4), I=I_(C/Q), and J_5=G/I^5G. The balanced-conic theorem and the uniform ideal-power theorem give

    H0(I^5G)=0,
    H1(J_5)=0,
    h0(J_5)_+=87,             h0(J_5)_-=78.

The new actual obstruction spaces are

    K_Q=H1(Q,I^5G),
    dim(K_Q)_+=83,            dim(K_Q)_-=82.

All other cohomology of I^5G vanishes. The canonical restriction boundary therefore gives the actual two-term presentations

    H0(J_5)_+ -> (K_Q)_+       [87 -> 83],
    H0(J_5)_- -> (K_Q)_-       [78 -> 82],

whose kernels are H0(G)_+ and H0(G)_-, and whose cokernels are H1(G)_+ and H1(G)_-. In families this is a two-term vector-bundle complex representing the actual derived pushforward, not merely an equality of numerical indices.

There are sharper staged interfaces:

* Positive: the actual 15-dimensional fourth-jet boundary, then a 45-dimensional second-jet boundary into its cokernel, then the 27-dimensional conic restriction boundary.
* Odd: the actual 36-dimensional third-jet boundary, then a 42-dimensional first-jet boundary into its cokernel.
* On the lower-good open, the previous positive 64-to-87 presentation is replaced by an actual 60-to-83 presentation with canonically identical cohomology. The reduction uses the actual second-through-fourth jet space, not a chosen four-dimensional matrix cancellation.

No maximal rank, higher-neighborhood splitting, lifting of arbitrary jets to Q, or exact full corank four is asserted.

## 1. The actual finite jet data

Write E_m for the section space of the m-th normal graded piece. Balance gives

    I^mG/I^(m+1)G = O_P1(8-2m)^(3(m+1)).

For m=0,1,2,3,4 these graded pieces have H1=0, dimensions

    dim E_0=27, dim E_1=42, dim E_2=45,
    dim E_3=36, dim E_4=15,

and characters (-1)^m. Exactness of eigenspace projection preserves these canonical filtrations. In particular the following are exact sequences of actual section spaces:

    0 -> E_4 -> H0(I^2G/I^5G)_+ -> E_2 -> 0,
    0 -> H0(I^2G/I^5G)_+ -> H0(J_5)_+ -> E_0 -> 0,

    0 -> E_3 -> H0(J_5)_- -> E_1 -> 0.

Their dimensions are 15,60,45; 60,87,27; and 36,78,42, respectively. There is no choice of splitting in these statements. The identifications of the odd quotients with E_1 are induced by the canonical doubled-conic splitting and the absence of odd character in the second graded piece.

The balanced-conic theorem proves H0(I^5G)=0 by descending from the proved uniform H0(I^7G)=0 through the two section-free fifth and sixth graded pieces. Thus no infinite-order separation argument is being used here.

## 2. Exact obstruction dimensions, without lower-twist assumptions

For every smooth even Q the actual adjoint calculation gives

    H2(G)=H3(G)=0,
    chi(G)_+=4,                  chi(G)_-=-4.

The exact sequence

    0 -> I^5G -> G -> J_5 -> 0

and H1(J_5)=0 imply H2(I^5G)=H3(I^5G)=0. Together with H0(I^5G)=0, this proves that I^5G has cohomology only in degree one. Taking equivariant Euler characteristics gives

    h1(I^5G)_+=87-4=83,
    h1(I^5G)_-=78-(-4)=82.

Hence, in each parity, the restriction sequence is exactly

    0 -> H0(G) -> H0(J_5) --Delta_Q--> H1(I^5G)
      -> H1(G) -> 0.

This deduction holds throughout the balanced smooth-even open, even where lower-twist sections occur. The lower-good hypothesis is needed only for comparison with the fixed-dimensional 64-to-87 Koszul presentation below.

## 3. Relative derived presentation and equality of failure schemes

Let S be this balanced smooth-even open, let pi:Q_S->S be the universal smooth quadric, let C_S be the relative fixed conic, and use G and I for the corresponding relative sheaves. The conic is a relative regular immersion. Its powers and finite neighborhoods are flat over S: this follows inductively from the locally free normal graded pieces and the exact power sequences.

The fiberwise vanishings and constant dimensions in Sections 1 and 2 imply cohomology and base change and give vector bundles

    J=pi_*(G/I^5G),             ranks (+,-)=(87,78),
    K=R^1 pi_*(I^5G),           ranks (+,-)=(83,82).

All other derived direct images of these two sheaves vanish. The actual restriction triangle therefore identifies

    R pi_* G = [ J --Delta--> K ],

with J in degree zero and K in degree one. More precisely this is the two-term complex supplied by the connecting morphism in that restriction triangle; no unspecified extension class or arbitrary isomorphism of vector spaces is inserted.

The same actual derived pushforward is represented by the ambient full-adjoint pencil, with source H1(B(2)) tensor O_S(-1) and target H1(B(4)). Its even ranks are 41-to-37 and odd ranks 44-to-48. The two presentations are thus functorially presentations of the same derived object, not only complexes with equal Euler characteristics. No preferred acyclic direct-summand decomposition is claimed.

Consequently the positive failure ideal is exactly

    Fitt_0(R^1 pi_*G)_+,

computed either by the 83-by-83 minors of Delta_+ or by the 37-by-37 minors of the actual even ambient block. The odd failure ideal is exactly

    Fitt_4(R^1 pi_*G)_-,

computed either by the 78-by-78 minors of Delta_- or by the 44-by-44 minors of the actual odd ambient block. Parentheses here mean take the indicated eigensheaf before forming its Fitting ideal. This is equality of actual determinantal ideal sheaves, not just equality of supports. It does not assert that either ideal is nonzero.

At a fiber, positive excess vanishes precisely when Delta_+ is onto, and odd sections vanish precisely when Delta_- is injective. If

    e=dim coker Delta_+,       o=dim ker Delta_-,

then the actual full-adjoint kernel has dimension 4+e+o. Exact corank four is therefore equivalent to these two actual conditions together.

## 4. Positive fourth-, second-, and zeroth-order gates

Restrict Delta_+ to the canonical subspace E_4:

    d_4:E_4 -> K_+,             dimensions 15 -> 83.

The exact sequence 0->I^5G->I^4G->gr^4G->0 identifies

    ker d_4 = H0(I^4G)_+,
    R_4:=coker d_4 = H1(I^4G)_+.

Write k_4=dim ker d_4. Then dim R_4=68+k_4. The next exact power sequence, projected to positive parity, gives the actual boundary

    d_2:E_2 -> R_4,             dimensions 45 -> 68+k_4.

This map is equivalently induced by Delta_+ modulo the image of d_4. It is well-defined independently of any lift through the nonsplit extension in Section 1. Put

    k_2=dim H0(I^2G)_+.

Its exact sequence is

    0 -> ker d_4 -> H0(I^2G)_+ -> ker d_2 -> 0,
    R_2:=coker d_2 = H1(I^2G)_+,
    k_2=k_4+dim ker d_2,       dim R_2=23+k_2.

Finally the conic restriction gives the actual boundary

    d_0:E_0 -> R_2,             dimensions 27 -> 23+k_2,

and

    0 -> H0(I^2G)_+ -> H0(G)_+ -> ker d_0 -> 0,
    H1(G)_+=coker d_0.

These are successive compatible gates, not independent maps. In particular positive excess vanishes exactly when d_0 is onto, using the actual cokernels from the preceding stages. It then necessarily has k_2<=4. If k_2>=5, positive excess is forced, with

    h1(G)_+ >= k_2-4.

A single nonzero fourth-order section is not enough to force excess: the unavoidable four positive sections may already account for it. Injectivity of d_4 and d_2 is not necessary for exact corank four. If both are injective, the remaining positive gate is precisely an actual 27-to-23 surjectivity question.

The preceding two stages can also be combined without choosing any splitting. Define

    S_2=H0(I^2G/I^5G)_+,       dim S_2=60,
    beta_2:S_2 -> K_+,          dimensions 60 -> 83.

Then

    ker beta_2=H0(I^2G)_+,     coker beta_2=H1(I^2G)_+.

On the independently proved lower-good even open, the actual power-Koszul resolution gives the earlier presentation

    alpha:H1(B_Q(1))_- tensor W -> H1(B_Q(2))_+ tensor Sym^2 W,
    dimensions 64 -> 87,

where W is the actual two-dimensional odd normal-generator space; determinant characters can equivalently be retained as W tensor det W on the left. Both [S_2->K_+] and the Koszul complex represent R Gamma(I^2G)_+ with its actual restriction maps. Their kernel and cokernel identifications are canonical through that sheaf. The four-dimensional difference of presentation ranks is not a proof of any additional rank or a choice of a cancellable subspace of the original matrix.

## 5. Odd third- and first-order gates

The canonical third-order subspace gives

    d_3:E_3 -> K_-,             dimensions 36 -> 82.

The actual power sequence identifies

    ker d_3=H0(I^3G)_-,
    R_3:=coker d_3=H1(I^3G)_-.

Write k_3=dim ker d_3, so dim R_3=46+k_3. The first-normal-jet quotient then gives the induced actual boundary

    d_1:E_1 -> R_3,             dimensions 42 -> 46+k_3.

Its precise compatibility is expressed by

    0 -> ker d_3 -> H0(G)_- -> ker d_1 -> 0,
    H1(G)_-=coker d_1.

Thus odd vanishing is equivalent to BOTH d_3 being injective and d_1 being injective. Under the first condition the latter is an actual 42-to-46 injectivity question. Any kernel of d_3 already gives a genuine global odd adjoint section with leading normal order three; it is not merely a formal jet. The new finite interface separates this possibility from an odd section detected at first order.

This does not replace the smaller 34-to-38 odd Koszul presentation as a numerical rank problem. It supplies a geometric filtration of that same actual obstruction, with the higher-order lifting compatibility kept in the cokernel R_3. In particular arbitrary choices of first- and third-order coefficients do not define global sections.

## Dependencies and boundary

The required actual inputs are proved in FIXED-PLANE-CONIC-BALANCE-AND-FOURTH-JETS.md, FIXED-CONIC-PARITY-JETS-AND-POSITIVE-GATE.md, FULL-ADJOINT-PENCIL-INVOLUTION-BLOCKS.md, and LOWER-TWIST-EVEN-QUADRIC-PARITY.md. The nonempty balanced open and nonempty lower-good open lie in the same irreducible smooth-even family, so their intersection is nonempty. No claim is made about the rank of any newly displayed actual boundary on that intersection.

All maps in this note arise from the fixed actual HM bundle, its actual conic ideal, and exact restriction or power sequences. No selected coefficients, actual rank scans, surrogate multiplication matrices, or external writes are used.
