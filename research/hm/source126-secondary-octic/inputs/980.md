# Canonical secondary homotopy of the Type II radical kernel line

## Result and boundary

Assume the actual source126 Type II occurrence and full two-dimensional radical J compatibility with Q, retaining every hypothesis of PR973. Let S and T be its actual common-annihilator and quotient complexes. There is a canonical one-dimensional subspace

    J0=ker[J→Hom_G(H0(T),H0(S))].

For each j∈J0 there is a UNIQUE G-equivariant degree-minus-one homotopy h_j:T1→S0 with

    j0=h_j Q_T,    j1=Q_S h_j.                         (1)

Here j0,j1 denote the two descended endpoint maps T→S, not their induced cohomology maps. For every negative quadratic a, put

    K_j,a^0=h_j L_T,a,   K_j,a^1=L_S,a h_j.             (2)

These are a genuine chain map T→S for Q+tL_a. On Q-cohomology the induced maps satisfy

    k_j,a^1:P→D =0,
    k_j,a^0:D→A+D = (0,ν(j){a,-}_1),                   (3)

where ν:J0→C is linear after fixed equivariant identifications, and {a,-}_1 is the first binary transvectant on Sym²W×Sym⁴W. In particular the secondary A component and the entire secondary cokernel component vanish identically. This is stronger than naturality alone as an unprocessed relation: it removes two of the three a-linear equivariant channels.

The value of ν is NOT selected. If ν(j)≠0, then k_j,a^0 has rank four for every nonzero a, kernel C·a², and the universal D-channel has exact kernel O(-3) and cokernel O(2):

    0→O(-3)→D O(-1)→D O→O(2)→0.                      (4)

If ν(j)=0, both secondary induced maps vanish. A nonzero h_j or a faithful P endpoint row does not by itself decide this scalar. Neither branch is excluded here. This theorem does not prove full-J existence or nonexistence, select a source, or solve the original repair. It uses no actual coefficient, selected point, matrix or rank evaluation.

## 1. Exact interfaces and chain conventions

INPUTS.json authenticates PR973 at f48c517d776b7f82ee1f96787da722223431a565, research/hm/source126-typeII-radical-naturality/PROOF.md, and PR970 at b4267159972c8999ea3cfff53fbb631008d1e482, research/hm/source126-polar-integrability/PROOF.md.

PR973 establishes the actual two-term families S=[S0→S1], T=[T0→T1], with sources in cochain degree zero, and

    H0(S)=A+D, H1(S)=D, H0(T)=D, H1(T)=P.

Their first symbols are

    b_S,a(k,h)=λ a k, λ≠0,
    b_T,a(h)=c[a h] in Sym⁶W/V6=P, c≠0.               (5)

In particular b_T,a is surjective for every nonzero square a; this is a proved uniform rank theorem, not an instance evaluation. Each j∈J descends to a G-equivariant chain map T→S for every Q+tL_a. Its induced degree-one cohomology map is zero, and its induced degree-zero map lands in D⊂A+D. At least one j gives a nonzero scalar on this D. Since dim J=2, its scalar map has a one-dimensional kernel J0.

PR970 ensures nonzero elements of J have nonzero P endpoint row. We do not use this to infer a nonzero secondary scalar: that inference requires additional information. It only emphasizes that the nonzero j considered here is a genuine, nonzero endpoint chain map, even though it is zero on Q-cohomology.

## 2. Existence and uniqueness of the equivariant homotopy

A cohomologically zero map between finite-dimensional complexes over C is null-homotopic: split each complex into its cohomology with zero differential and its contractible image blocks, and solve the equations on the blocks. Since G is finite in characteristic zero, averaging these splittings or the resulting homotopy makes the homotopy G-equivariant. Thus (1) has an equivariant solution for each j∈J0.

If h and h' are two solutions, e=h-h' satisfies

    Q_S e=0,    e Q_T=0.

Consequently e factors canonically through

    H1(T)=coker Q_T → ker Q_S=H0(S).

But Hom_G(P,A+D)=0. Hence e=0. This proves uniqueness. It also proves linearity in j. Changing auxiliary splittings cannot change h_j. The construction is canonical on the actual complexes, not only up to a quotient of choices.

## 3. Secondary chain map, sign and first-symbol naturality

Fix j and a, and abbreviate h=h_j. For a degree-minus-one map the Hom-complex differential is

    d_Q h=(h Q_T,Q_S h).

For a degree-zero pair f=(f0,f1), its degree-one differential is

    d_Q f=Q_S f0-f1 Q_T.

There is therefore no minus sign in (2). Direct substitution gives

    Q_S K0-K1 Q_T
      =Q_S h L_T-L_S h Q_T
      =j1 L_T-L_S j0=0,

by the exact negative-family chain-map identity for j. Also

    L_S K0-K1 L_T=L_S h L_T-L_S h L_T=0.

Thus K_j,a is a chain map for the entire one-parameter family Q+tL_a. It depends linearly and equivariantly on a, and linearly on j. No common-chain-map assertion for unrelated directions a and b is needed: the identity is for the same a on both sides.

The first-symbol naturality identity on Q-cohomology is exactly

    b_S,a k_j,a^0 = k_j,a^1 b_T,a.                     (6)

For completeness, if x∈ker Q_T represents a cohomology class, K0 x is a Q_S-cycle. The left side is the class of L_S K0x, the right side is the class of K1 L_Tx, and these representatives agree by the second displayed identity. Thus (6) includes the correct signs and does not assume a higher-obstruction comparison.

## 4. Rank and invariant duality force two channels to vanish

The actual irreducibles A=Sym²W, D=Sym⁴W and P are self-dual. Fix G-invariant perfect pairings on D and P. Taking the adjoint of b_T,a defines an equivariant linear family

    b_T,a^*:P→D.

It is nonzero. Moreover this family spans Hom_G(A⊗P,D): duality identifies that Hom space with Hom_G(A⊗D,P), which is one-dimensional by

    A⊗D=Sym⁶W+Sym⁴W+Sym²W=V+P+D+A.

Therefore k_j,a^1=ρ(j)b_T,a^* for a scalar ρ(j), independent of a. No positivity, Hermitian metric or identification of a complex transpose with a conjugate transpose is used; these are complex bilinear invariant pairings.

For any nonzero square a, the proved map b_T,a:D→P is surjective. Its adjoint b_T,a^*:P→D is injective. Thus if ρ(j)≠0, the right side of (6) has rank four: it is a surjection onto P followed by an injection out of P. By (5) the left side factors through the A component of k_j,a^0, a space of dimension three, so its rank is at most three. Contradiction. Hence ρ(j)=0 and k_j,a^1=0 for all a.

Equation (6) now gives b_S,a k_j,a^0=0. Multiplication by every nonzero binary quadratic a is injective on Sym²W. Since λ≠0, the A component of k_j,a^0 must be zero for every nonzero a, and hence identically. Finally Hom_G(A⊗D,D) is one-dimensional by the same decomposition. Its nonzero generator is the ordinary first transvectant, equivalently the sl2 action on binary quartics. This proves (3).

This argument uses only the already proved uniform rank of b_T. It does not infer nonzero secondary coefficients from endpoint faithfulness or dimensions.

## 5. The remaining D channel, conditional on ν≠0

Write the first transvectant as

    {a,h}_1 = a_x h_y-a_y h_x.

It is a nonzero SL2-equivariant generator of the unique D channel. It kills a² by the product rule. Every nonzero binary quadratic is, under an SL2 change and a nonzero scalar, either x² or xy. For a=x², the operator is2x∂y on Sym⁴W, rank four with kernel C·x⁴. For a=xy, it is y∂y-x∂x, with weights -4,-2,0,2,4 on the binary quartic monomials and kernel C·x²y². Thus its rank is four and its kernel is C·a² for all nonzero a.

This is a universal SL2 computation on the representation model, not an evaluation of any actual obstruction coefficient. On P(A), the polynomial vector a² defines a nowhere-zero bundle inclusion O(-3)→D O(-1), and the preceding fiber calculation identifies it with the kernel. Constant rank makes the cokernel a line bundle. The determinant equation gives

    c1(coker)=0-(-5H)+(-3H)=2H,

so it is O(2), proving (4).

## 6. Remaining mathematical question

The construction proves a canonical linear functional ν on the radical kernel line J0. A nonzero j has a nonzero homotopy h_j, since d_Qh_j=j. Yet taking d_Lh_j and then Q-cohomology can annihilate a nonzero homotopy. No implication ν≠0 follows formally from j≠0 or its faithful P endpoint row. Establishing nonvanishing or vanishing of ν from the actual balanced source, or deriving an incompatible next naturality relation, is a separate gate.

The verifier authenticates both original proofs and checks finite synthetic Hom-complex identities, null-homotopy ambiguity in split complexes, the unique representation channels, rank of a surjection followed by its bilinear transpose, and both universal quartic Jordan types. Synthetic matrices are diagnostic linear algebra, not actual HM realizations. The written proof supplies actual source and chain-map identifications; the verifier is not proof-assistant certification.
