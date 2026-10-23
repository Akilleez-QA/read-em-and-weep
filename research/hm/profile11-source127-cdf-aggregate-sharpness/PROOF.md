# An exact quotient-support criterion and its formal sharpness

## Result and boundary

For a fixed c-d-f negative pencil, the unresolved positive-quadratic-compatible algebra is determined by explicit tests on two quotient rows and two cross-block maps. In particular, nonzero contributions from both source blocks to the intrinsic seven-dimensional quotient force the compatible algebra to be scalar.

There is no deduction of that two-sided support from the aggregate constraints already proved. We construct, for the same fixed negative pencil, formal equivariant aggregate-positive maps satisfying all the specified aggregate conditions and giving respectively the scalar algebra and each of the two possible nonscalar idempotent types. The constructions are uniform in the negative pencil and require no selected source parameter.

These are formal aggregate maps, not asserted positive-linear factorizations, five-variable window representations, or extensions of the actual HM module. The exact criterion applies to the actual positive-quadratic map; the constructions show precisely which weaker interface does not determine its answer. No source exclusion, actual realization, or count change follows.

## 1. Exact inputs and the interface being tested

All paths refer to Akilleez-QA/read-em-and-weep. The four-input manifest records immutable source bytes.

1. PR924 at c6c25eaf0e5a67c27eee7c3ba4f000df55997692, research/hm/profile11-source127-cdf-pencil-algebra/PROOF.md, blob 83f5aee293995257459229e6b323522224ce8f3d: the whole represented negative-pencil algebra, its actual simultaneous covariant identification, and its component actions, including singular endomorphisms.
2. PR926 at 3d9e1f3949241a6b2bbb48781c056b72b7262dd7, research/hm/profile11-source127-cdf-negative-square/PROOF.md, blob bdcb7d5b14f7477bcd616e0e682fa5f45e250a5d: the actual negative-square product, its exact image, kernel and intrinsic cokernel Pi, and surjectivity of the aggregate positive action onto Pi via PR925's actual generation theorem.
3. PR818 at f4a73af666900ad2cb34a756d24b88e19dd6feaa, research/hm/negative-truncation-extension/PROOF.md, blob 2ba0a7eee6ef2eb5413683e85618d7902dca3970, Section 1: the actual coordinate decomposition T_coord=T_+ direct-sum W, with T_+ center-even of dimension three and W center-odd of dimension two; and the actual grading N2=K3^+, N3=K4^-, N4=K5^+.
4. The original actual-equivariant-splitting note at db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md, blob b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3: the binary-icosahedral representation conventions and self-duality. The nine irreducibles have dimensions 1,2,2,3,3,4,4,5,6; the center-even ones are 1,A,V,P,D, of dimensions 1,3,3,4,5. The fixed character check also authenticates this representation bookkeeping.

Write R=Sym2(T_+). Fix a negative pencil N with the exact represented structure of PR924 and the actual negative-square map q_- of PR926. In a proved normal form set

    N2=X_F direct-sum X_B,
    X_F=V+P+2D, X_B=A+V+2P+2D,
    N4=Y_F direct-sum Y_B direct-sum Y_L,
    Y_F=P+D, Y_B=V+2P+2D, Y_L=V+P.             (1)

The negative-square image is I=Y_F direct-sum Y_B, and Pi=N4/I is intrinsic. A normal form identifies Pi with Y_L; that complement is not declared canonical.

The represented algebra C_N has coordinates e=(a,b,d,w), w in a one-dimensional space J, with product

    (a,b,d,w)(a',b',d',w')
           =(aa',bb',dd',a w'+d' w).           (2)

On N2 it acts by a,b on X_F,X_B. On N4 its diagonal actions are a,b,d and its only off-diagonal action is

    eta_w:Pi=V+P -> P subset Y_F,              (3)

which is zero on V and nonzero on P for every nonzero w. The map w->eta_w is injective. In particular the radical acts trivially on Pi and e induces the scalar d there.

We consider the following precise aggregate interface: a G-equivariant linear map

    q:R tensor N2 -> N4                         (4)

such that im q+I=N4. Equivalently its induced quotient map chi:R tensor N2->Pi is onto. This includes the actual q_+ by PR926. It does not include the unproved assertion that an arbitrary (4) arises from three mutually commuting positive-linear operators and all their mixed squares with W. The actual degree-zero cover and Euler relations are not reconstructed from (4).

## 2. The compatible algebra and quotient-support test

For q as in (4), define

    Theta_q(e)=e4 q-q(1 tensor e2),
    D(q)=ker Theta_q inside C_N.                (5)

Every e in C_N already commutes with q_-, because it intertwines both negative arrows. If e2=0 and Theta_q(e)=0, e4 vanishes on im q and im q_-, hence on N4 by the aggregate assumption. The represented actions in (1)-(3) then force a=b=d=0 and w=0. Thus e=0.

The identity

    Theta_q(ef)=e4 Theta_q(f)+Theta_q(e)(1 tensor f2)

shows that D(q) is a unital subalgebra. The map e->(a,b) embeds it as a unital subalgebra of C^2 by the preceding zero-source argument. Its image contains the scalar diagonal. It follows that D(q) is either C identity or isomorphic to C^2. In the nonscalar case there is a unique idempotent p with source scalars (a,b)=(0,1). Formula (2) gives

    p=(0,1,0,0), or p=(0,1,1,w).               (6)

Indeed p^2=p requires d^2=d and dw=w. This argument is valid for singular endomorphisms and does not assume a window lift.

Write chi_F and chi_B for the restrictions of chi to R tensor X_F and R tensor X_B. Passing (5) to the intrinsic quotient gives, for any compatible e,

    (d-a) chi_F=0, (d-b) chi_B=0.              (7)

If both quotient rows are nonzero, (7) gives a=b=d. Subtracting that common scalar from e leaves a compatible element whose N2 action is zero, which must vanish. Therefore

    chi_F nonzero and chi_B nonzero
                imply D(q)=C identity.         (8)

The hypothesis is nonzero on each entire row, not that each row is onto. Aggregate surjectivity alone does not assert either individual row is nonzero.

## 3. Complete decision criterion when one quotient row vanishes

Let Q_FB:R tensor X_B->Y_F and Q_BF:R tensor X_F->Y_B be the two indicated cross-block components of q in (1). Subscripts are target followed by source. The diagonal components impose no extra equation on the idempotents in (6).

For p=(0,1,0,0), direct substitution into (5) gives exactly

    chi_B=0, Q_FB=0, Q_BF=0.                   (9)

For p=(0,1,1,w), the equations are exactly

    chi_F=0, Q_BF=0, Q_FB=eta_w chi_B.         (10)

To verify the second formula without suppressing a radical term, the F-target/F-source equation is eta_w chi_F=0; the F-target/B-source equation is eta_w chi_B-Q_FB=0; the B-target/F-source equation is Q_BF=0; and the L-target/F-source equation is chi_F=0. The other two diagonal equations are identities. Thus the F/F radical term vanishes because the L/F equation already forces chi_F=0, not by an unstated support assumption. The first formula follows from the same component equations with d=w=0.

Since chi is onto, its two restrictions cannot both vanish. If chi_B=0, chi_F is onto, so only (9) can occur. If chi_F=0, chi_B is onto, so only (10) can occur, and any w in (10) is unique: eta_w chi_B=eta_w' chi_B and surjectivity imply eta_w=eta_w', hence w=w'.

Consequently the following is a necessary-and-sufficient decision criterion:

- If both quotient rows are nonzero, D(q) is scalar.
- If chi_B=0, D(q) is C^2 exactly when both Q_FB and Q_BF vanish; otherwise it is scalar.
- If chi_F=0, D(q) is C^2 exactly when Q_BF=0 and Q_FB belongs to the one-dimensional subspace {eta_w chi_B:w in J}; otherwise it is scalar.

Sufficiency uses the displayed compatible idempotent. Necessity uses the unique idempotent (6) in every nonscalar D(q). The equations are stated in a normal form, but the conclusion is the original fixed-pencil compatibility algebra. In particular no arbitrary scalar complement is promoted to a canonical subspace of N4.

## 4. Existence of the invariant positive functional

We need a nonzero invariant functional epsilon:R->C for the formal constructions. This does not require choosing or identifying the actual type of the positive three-space more precisely than the authenticated input allows.

By semisimplicity and the center-even irreducible dimension list, T_+ is either A, V, or a sum of three trivial representations. There is no other decomposition of dimension three using center-even irreducibles. In either irreducible case, self-duality gives a nondegenerate invariant bilinear form. By Schur's lemma its transpose is either itself or its negative. A nondegenerate alternating form cannot exist in odd dimension, so the form is symmetric. It therefore defines a nonzero invariant functional on Sym2(T_+). In the trivial case such a functional is immediate.

Thus an invariant epsilon exists in every allowed case. This is an existence proof in the abstract representation category, not a selected coordinate quadratic, an evaluation of actual coefficients, or an assertion about one actual positive multiplication operator.

## 5. Three formal aggregate constructions for the same negative pencil

Both X_F and X_B contain V and P. Choose abstract equivariant surjections

    r_F:X_F->Pi=V+P, r_B:X_B->Pi=V+P.

Their existence follows from the genuine direct-sum constituents in (1). No canonical choice is needed or claimed. These are formal auxiliary maps, not values of the actual source multiplication. Choose the normal-form section i_L:Pi->N4 for this construction only.

For s in R and x_F in X_F, x_B in X_B, define three aggregate maps:

    q^both(s tensor (x_F,x_B))
          =epsilon(s) i_L(r_F(x_F)+r_B(x_B)),
    q^F(s tensor (x_F,x_B))
          =epsilon(s) i_L r_F(x_F),
    q^B(s tensor (x_F,x_B))
          =epsilon(s) i_L r_B(x_B).            (11)

Each is G-equivariant and linear on Sym2(T_+) tensor N2. For each map, chi is onto Pi because epsilon and the surviving r maps are onto their targets. Hence im q+I=N4, with the original negative pencil, negative-square map, ninety-three-dimensional restricted kernel and seven-dimensional quotient all unchanged.

All F-target and B-target components in (11) are zero, so Q_FB=Q_BF=0. For q^both both quotient rows are nonzero; (8) gives exactly the scalar algebra. For q^F, condition (9) holds and its compatible algebra is exactly C^2 with idempotent (0,1,0,0). For q^B, condition (10) holds with w=0; uniqueness rules out other w, and its compatible algebra is exactly C^2 with idempotent (0,1,1,0).

Each construction also retains the aggregate radical consequence: eta_j chi is onto P for every nonzero radical j, since chi is onto Pi and eta_j is onto P. Thus none evade the known radical obstruction or the full scalar-target surjectivity. All three obey the same precise aggregate hypotheses while realizing every residual algebra alternative and both idempotent types, already with zero shear in the latter constructions.

The construction works for every fixed negative pencil with the stated structure. It does not require choosing a balanced parameter, altering q_-, or evaluating any actual source instance. The auxiliary formal projections vary the additional aggregate map, not the authenticated actual multiplication map.

## 6. What this resolves and what it does not

Equations (8)-(10) replace an unspecified compatibility-algebra alternative by exact quotient-support and cross-component tests. The formal constructions prove that the negative pencil, its full negative-square relation/cokernel data, equivariance of the aggregate positive map, aggregate generation and the forced radical/scalar-target surjections do not by themselves decide those tests. This is a constructive limitation theorem for that explicitly listed interface.

The constructions do not claim compatibility with all facts about the actual HM module. In particular they do not preserve unmodeled actual relation embeddings, provide three positive-linear factors, satisfy every mixed positive-negative window square, construct a degree-zero-generated full module with the actual Euler relation, or supply actual HM membership. Any of those additional structures may distinguish the actual branch. Their omission is the logical point, not an assertion that they can be filled in arbitrarily.

For an actual occurrence, one may now prove scalarness by showing both intrinsic quotient rows nonzero, or settle a one-row branch using (9) or (10). Establishing such support or factorization for the actual q_+ remains a genuine missing dependency. Even a compatible nonscalar idempotent would not imply a full-module lift or a global splitting. No source exclusion or change in the frontier follows here.
