> Historical mathematical record, 16 October 2026. Statements of PASS and check counts below refer to the original recorded verification, not a new execution. See PUBLICATION-SCOPE.md at the common series root for current scope, imported premises, and source/public hash bindings.

# Explicit epsilon generator and detector-dual bridge

## Result

Over Q, the authenticated 32-dimensional full-deck-sign, D8-epsilon H2 space has the following **specified, global, inversion-equivariant complex splitting**:

    C_epsilon = B(-3) direct_sum B(-4) direct_sum B(-5),
    (G0,G1,G2) |-> a G0 + a U G1 + a U^2 G2,

where B=End(L), L is the pinned perfect complex in genuine degrees -1,0,1,2, and pullbacks/full-sign line factors in this formula are understood as below. Its H2 dimensions are 20,10,2. The three generators have degrees1,2,3 and are each fixed by homogeneous simultaneous inversion. This supplies the previously missing equivariant generator comparison, rather than selecting a basis from a dimension count.

Each of the actual four detector functionals has an explicit dual-cycle triple. Put

    beta0=1, beta1=v2, beta2=v2^2-v1 v3+2v0 v4.

If E_d is the degree+2 supertrace-dual matrix to the authenticated row L_d, then the triple is

    (4 E_d, 4 v2 E_d, 4 beta2 E_d)

in the existing small models B(-2), B(-1), B(0), dual respectively to the three displayed primal summands. Section4 gives the actual component signs. `detector-dual-cycles.json` supplies exact sparse coordinates for all four triples and their inversion transports in the archived ambient basis. These are closed-cycle representatives; no quotient coordinates or original-only inversion relation are asserted.

The saved small-twist package contains exact rank data and executable matrix generators, but no saved quotient basis or reduction/comparison matrices. We authenticate and inspect it without running its rank computation. The precise remaining linear-algebra input is given in Section7.

## 1. Specified global epsilon generators

Let Y=(P1)^4, sigma:Y->P4 be the binary-product map, and T=Q[v0,...,v4]. Every vi has Segre degree1, v0=product Yi. Set

    U=X1 X2 Y3 Y4+Y1 Y2 X3 X4,
    a=(X1 Y2-X2 Y1)(X3 Y4-X4 Y3).

Let H=< (12),(34),(13)(24)> and epsilon=sign restricted to H. This group permutes the four coordinate pairs, fixes every vi, and does not permute the carrier vertices on a cover pulled back from P4. If R is the equal-multidegree Segre section ring, the existing global cubic-resolvent and Klein-character proofs establish

    R^H=T direct_sum TU direct_sum TU^2,
    R^epsilon=a R^H
             =aT direct_sum aUT direct_sum aU^2T.

For completeness, oddness on each pair forces division by the two coprime irreducible pair brackets in the polynomial Cox ring. The resulting quotient is H invariant. The invariant triple is globally independent by the generic degree-three minimal polynomial of U, and globally spanning by equality of each graded dimension. No localization at v0 or any discriminant enters. Thus sheafification gives the actual isomorphism

    (sigma_* O_Y)^epsilon
       = O(-1) a direct_sum O(-2) aU direct_sum O(-3) aU^2.

It is not a noncanonical averaged lift or a choice of a generic-field basis. The exact polynomial generators are fixed in the displayed conventions. Localizing on any symmetric owned carrier denominator preserves this same free basis and adds no poles.

## 2. Global complex comparison and linearization

The full-sign summand of the four elliptic double covers is sigma^*O(-2), with its product linearization. Its local generator y1 y2 y3 y4 is invariant under permutations, unlike the wedge of four one-forms. Inversion acts on that generator by (product xi)^(-2), because i^4=1. This is exactly the standard homogeneous O(-2) linearization, with no additional sign.

Projection formula and the preceding specified free-module isomorphism therefore give, at the level of complexes of locally free sheaves on P4,

    (sigma_*(sigma^*B tensor sigma^*O(-2)))^epsilon
        = B(-3) direct_sum B(-4) direct_sum B(-5).       (1)

The map is entrywise multiplication by a,aU,aU^2. The End differential is T-linear, so it commutes with this map. Finite pushforward is exact; the carrier opens and their intersections are affine. Hence (1) gives an isomorphism of the complete total Cech complexes on that cover and consequently their hypercohomology. In particular it retains the incoming internal-degree -3 components; no truncated Laurent space is used.

For the authenticated complex L, the genuine degrees and ranks are

    degree: -1, 0, 1, 2; ranks: 5,15,10,2; twists: -1,0,1,2.

Homogeneous reversal rho sends vi to v_(4-i), and the specified chain matrices are

    T_-1=-J5, T_0=-diag(J5,J5,J5),
    T_1=diag(J5,J5), T_2=I2.

They act by the usual source/target conjugation on End. Exchanging X and Y negates each bracket defining a, hence fixes their product; it exchanges the two summands of U. Therefore all three generators in (1) are fixed. The involution on (1) is the direct sum of the ordinary semilinear rho/T actions on B(-3), B(-4), B(-5), with no generator permutation or minus sign.

The dimensions20,10,2 follow from the archived small-twist certificates and perfect-complex Serre self-duality. They are not evidence of a quotient basis. Nothing in (1) requires a nonlinear obstruction coefficient or a particular source expression to have been acquired.

## 3. The detector map on each summand

At internal degree -2 write F20:K2->K0 and F31:K3->K1, where K0,...,K3 denote L in the order above. The original rows, with zero-based matrix indices, are

    Lh=F31[0,1]-F20[2,6]-F20[3,9],
    Lj=F31[1,1]-F20[3,7]-F20[4,5],
    Lp=F31[5,0]+F20[1,3]+F20[4,2],
    Lr=F31[6,0]+F20[0,3]+F20[2,4].

They vanish on all other internal degrees. The independent homogeneous source-row authentication proves that every row kills the incoming degree -3 differential. Together with the common frame degree, this is a global map of complexes to the scalar line sheaf placed in internal degree -2. Thus it respects the full total differential and changes of representatives.

Put q=X3^2 X4^2 Y1^2 Y2^2 and Delta=product_(i<j)(XiYj-XjYi), with unnormalized alternation over all24 permutations. The exact global finite-trace identity is

    Alt(q a (A+UB+U^2C))/Delta
            =4(A+v2 B+beta2 C).                       (2)

This is the existing cubic-resolvent trace identity, freshly controlled here as an exact polynomial identity. It extends globally across infinity and ramification, and uses the canonical finite trace, not its average divided by24.

For a class represented in (1) by (G0,G1,G2), its detector is therefore exactly

    D_d(G)=Tr_P4(4 L_d(G0)+4 v2 L_d(G1)+4 beta2 L_d(G2)).   (3)

Here the selected internal -2 components of Gj have scalar line degrees -5-j. Multiplication by betaj, of degreej, puts all three in O(-5), whose Serre trace is normalized positively on the ordered coordinate cover. The actual finite-chart harmonic target (-1,-1,-3,-3) is the one corresponding to q. Equation(3) is the complete detector comparison and preserves that normalization. There is no extra 1/8 factor: the input is already in the epsilon summand. Projection of a general input into that summand would separately use its character projector.

## 4. Actual supertrace signs and sparse dual cycles

Use the genuine complex degrees -1,0,1,2, not a tacit degree shift to0,1,2,3. For E of internal degree+2, its only blocks are E02:K0->K2 and E13:K1->K3. Then

    Str(F E)=-tr(F20 E02)+tr(F31 E13).                (4)

Thus a coefficient c on F20[i,j] gives -c at E02[j,i]; a coefficient c on F31[i,j] gives +c at E13[j,i]. This transpose is solely the dual-pairing identification and is distinct from the physical source-current transpose or chain conjugation. The explicit E_d are

    Eh: E02[6,2]=1, E02[9,3]=1, E13[1,0]=1;
    Ej: E02[7,3]=1, E02[5,4]=1, E13[1,1]=1;
    Ep: E02[3,1]=-1, E02[2,4]=-1, E13[0,5]=1;
    Er: E02[3,0]=-1, E02[4,2]=-1, E13[0,6]=1.

All other entries vanish. The checker independently verifies [d,E_d]=0 from the homogeneous gamma/delta/ev literals. It also verifies this for the transported cycles.

The perfect-complex pairing and Serre duality identify

    H2(B(-3-j))^* = H2(B(j-2)).

In this identification equation(3) is represented by the global Cech-degree-zero cycle 4 betaj E_d. The total multiplication sign is positive: the only nonzero product pairing has internal/Cech degrees(+2,0) and(-2,4), so the cross sign is (-1)^(2*4)=+1. The scalar trace is the same positively normalized H4(O(-5)) trace used above. Hence neither a hidden block sign nor a Cech sign is left unresolved.

The archived basis has keys (u,v,a,b,m0,...,m4), with u,v in0,...,3, v-u=2, target rowa, source columnb, and a homogeneous degreej monomialm. Its ordering loops u, rowa, columnb, then monomials lexicographically with the first exponent increasing. The dimensions are80,400,1200 for j=0,1,2. `detector-dual-cycles.json` gives all24 sparse cycle records (four detectors, three twists, original/transported), including exact integer coefficients, basis keys and zero-based ambient indices. There are at most9 nonzero entries per record. Those are fully specified ambient-cycle coordinates, not coordinates in the32-dimensional quotient.

## 5. Inversion on these particular detector cycles

Each betaj is fixed by rho. Reversal on the five homogeneous coordinates is an even permutation, so its determinant is+1 and the P4 canonical Serre trace is invariant. Equivalently, each P1 inversion reverses one Cech edge and one canonical one-form; the four-factor conventions agree with the existing positive total trace. There is no new sign in (3) or(4).

The transformed matrix is E'_d=T E_d T^(-1), with the appropriate source/target blocks. Consequently the dual transform of the detector on the epsilon summand is represented by

    (4 E'_d, 4 v2 E'_d, 4 beta2 E'_d).              (5)

This also accounts for the inversion of the original harmonic target: rho(q) is the pair-exchanged q, and that pair exchange belongs to H with epsilon+1. Thus q and rho(q) have the same functional on the epsilon summand. More directly, (2) is fixed on its polynomial multipliers under reversal. There is no unproved raw-branch invariance in this argument.

Applying (4) to E'_d gives exactly the four transported rows of the independent inversion-detector theorem. At raw cycle level their entries differ from the original ones. Determining any equality modulo dual boundaries still requires the small-model reduction in Section7. In particular (5) does not imply a closed4-by4 action on the original detector span.

## 6. What was already saved in the small-twist package

The freshly retrieved package is pinned at commit f968b53943ba2312f09fbc3e8f9d462e86bcaa34, repository Akilleez-QA/read-em-and-weep, directory research/hm/d8-small-certificates/p4. Exact local copies and Git blob hashes are:

- pinned/Perfect-Complex-D8-F3.md: 3a8c3633e83466b29ea2e5739c6b486f856b91b2;
- pinned/certificate.json: 304d031083bb2a19fb9bc012cfd338bbe0129980;
- pinned/check_hm_p4_all_twists.js: 7adc1d6a733636204b1dd613870c168717be6277.

The saved certificate gives ranks and a 10-by10 unit minor, but no quotient basis or exact reduction maps. The source gives the full ordinary polynomial-matrix generator and the small d5 construction. We inspect these definitions but do not execute its 0/-1 rank routines or any large model.

A separate tiny observation, communicated for the independent involution audit, is that the five derivative cycles partial_k d form a basis of H1(B(-1)): d^2=0 proves they are cycles; their ev coefficient pivots prove independence; there is no incoming global-section term; and the archived dimension is5. Positive chain covariance sends partial_k d to partial_(4-k)d. The checker authenticates these identities from the fixed linear maps. This observation is independent of the detector bridge and is not used as a substitute for its quotient reduction.

## 7. Exact remaining finite input and stopping boundary

The global epsilon generator map and the images of these particular detectors are now supplied explicitly. What remains for exact32-quotient coordinates or a closed detector involution is **linear**, with the following specified finite inputs:

1. In twist-2, reduce the eight degree+2 cycles E_d,E'_d in the kernel of the archived50-by80 map modulo the image of its80-by10 d5 map. The d5 correction cannot be omitted.
2. In twist-1, reduce the eight cycles v2 E_d,v2 E'_d modulo the image of the400-by245 ordinary map, inside the kernel of the150-by400 next map.
3. In twist0, reduce the eight cycles beta2 E_d,beta2 E'_d modulo the image of the1200-by1225 ordinary map, inside the kernel of the350-by1200 next map.

All matrices are defined by the authenticated existing script, but its saved output is insufficient to perform these reductions without further exact linear work. A direct sparse boundary certificate for a candidate linear relation would be an equally valid substitute. Such a certificate must respect the genuine supertrace signs above and the d5 image in the first summand. No quotient basis is invented from the dimension32.

No nonlinear source, obstruction value, primitive table, clipped Laurent model, new carrier denominator, rank rerun  is used. The current deliverable stops at this explicit global comparison and exact sparse dual-cycle interface. Whether the actual obstruction is inversion invariant remains governed by its separate geometric first-lift comparison, not by this detector construction.

## Checks and provenance

`check.py` uses bounded exact integer polynomial arithmetic, homogeneous linear differential literals and saved metadata only. It checks generator characters/degrees/reversal, all three trace identities as polynomial alternants, beta reversal, original and transported dual closedness, actual supertrace signs, ambient basis indices, derivative-cycle pivots/covariance and the three downloaded Git blob hashes. No physical coefficient is evaluated.

Dependencies, all in sibling folders:

- hm-cubic-resolvent-trace-20261015/THEOREM.md and hm-cubic-resolvent-independent-audit-20261015/AUDIT.md;
- hm-klein-character-algebra-20261015/THEOREM.md;
- hm-four-detector-carrier-transfer-20261015/THEOREM.md;
- hm-terminal-demand-independent-20261015/SOURCE-ROW-AUTHENTICATION.md;
- hm-finite-duality-independent-20261015/THEOREM.md;
- hm-coordinate-reversal-chain-lift-20261016/THEOREM.md;
- hm-inversion-detector-action-independent-20261016/THEOREM.md and COMBINED-SYMMETRY.md;
- hm-symmetric-pushforward-status-20261015/AUDIT.md.

The exact homogeneous model input is hm-factored-coefficient-action-20261014/pinned-model-input.json, source blob fcd48a9a22d40d55ce7a08b8aefcb4eaa2fdf761, SHA256635bb12d9986e0dcada161d4173c773c4f134b9225354a3bc74267840ca19926. The source arrays are read only for their gamma/delta/ev linear differential entries.
