# A joint-row determinant gate for the Type I source126 radical

## Result and boundary

Assume an actual source126 occurrence of Type I, with the fixed negative-pencil radical J of dimension two. Let Q:N2→N4 be the canonical invariant positive quadratic. If EVERY j in J satisfies j4 Q=Q j2, then the joint P-row map

    R_P:J → Hom_G(2P,P)

has rank r=0 or1, never2. Equivalently its determinant vanishes. The exact common-annihilator subpencil U=Ann_J N2, Z=Ann_J N4 then has one of only two footprints:

| r | U | Z | dimensions U,Z | quotient endpoints |
|---|---|---|---|---|
| 1 | A+2V+2P+3D | 2V+3P+2D | 32,28 | P+D, P+D |
| 0 | A+2V+3P+3D | 2V+4P+2D | 36,32 | D, D |

In both cases Q|U has kernel A+D and cokernel P. The induced quotient Q is an isomorphism, so the two-term pencil Q+tT_a reduces formally to U→Z for every negative quadratic a. This is conditional on full-J compatibility; it does not assert that either row occurs, that the determinant is nonzero on the balanced locus, or that J_Q has dimension at most one. Types II/III are not covered. No source-dual pair is removed and the original proof remains open.

## 1. Pinned interfaces

INPUTS.json retains nine immutable originals: PR856 separation, PR858 templates, PR862 whole algebra, PR944 endpoint reconstruction, PR946 natural Serre-duality faithfulness, the original invariant-product theorem, original first-Bockstein vanishing, original nonzero second-Bockstein theorem, and PR935's explicit correction-comparison lemma. Their exact commits, paths, Git blobs and SHA256 hashes are recorded there.

The Type I genuine constant decomposition is E=F⊕X⊕Y in H=C⊕P⊕(A+V+D), where F=(P+2D)O(-2), X=O(-8), Y=W O(-9). Every j∈J kills F and X and maps Y into F. The constant coefficient of j on P is zero; its A,V,D coefficients satisfy one linear equation whose V coefficient is nonzero. In particular there exists j whose A coefficient is nonzero. Y spans A+V+D as an actual constant inclusion.

The reconstructed endpoints are

    N2_F=A+2V+2P+2D, N2_X=D, N2_Y=P+D;
    N4_F=P+2D, N4_X=V+P, N4_Y=V+2P+D.

The actual invariant theorem gives ker Q=A+D, im Q=2V+3P+3D, coker Q=P. Thus Q is injective on P and surjective on D. These are imported exact facts, not evaluated matrices.

## 2. The joint D action cannot vanish

The natural Serre-duality isomorphism

    Hom_G(Y,F0 O(-2)) ≅ Hom_G(H1(Y),F0), F0=P+2D,

identifies the actual bundle map with its fourth-endpoint action. It respects the target decomposition into P and 2D. If every j4 had zero D component, every j:Y→F would factor through the intrinsic P O(-2) summand of F.

Any equivariant inclusion P O(-2)→C O has constant coefficient span contained in an equivariant image of P⊗Sym²W. The fixed McKay identities give

    P⊗Sym²W=P⊗A=V+P+D,

which contains no A. (Indeed W⊗P=Wp+T, W⊗Wp=P, W⊗T=V+P+D, and W⊗W=1+A.) Choose j with nonzero A constant coefficient, possible by the nonzero V restriction in Section1. Since Y spans A+V+D, the coefficient span of j(Y) contains A. This contradicts its factoring through P O(-2). Therefore the joint D action is nonzero.

This proves only that the maps from the SINGLE D source copy in N4_Y to 2D in N4_F are not all zero. That is exactly enough: their common kernel on that source D is zero. No individual-rank-to-common-rank inference is being used.

## 3. Exact common-annihilator characters

Choose any basis j,j' of J and any multiplicity basis of the two P copies in N4_Y. Their P components are two row vectors. Let R be the resulting 2×2 matrix and r=rank R. Changes of either basis multiply R by invertible matrices, so r and the vanishing of det R are intrinsic. This is the map R_P in the statement, not a chosen actual coefficient evaluation.

All radicals kill N4_F and N4_X. On N4_Y they kill V, act on its two P copies by these joint rows, and have zero common kernel on its D copy by Section2. Consequently

    Z=Ann_J N4=2V+(4−r)P+2D.

At the first endpoint U contains N2_F⊕N2_X=A+2V+2P+3D. Its remaining part is a G-subrepresentation of N2_Y=P+D, so for ε,δ∈{0,1},

    U=A+2V+(2+ε)P+(3+δ)D.

Now assume J⊂D_Q. Every j preserves ker Q and is square-zero there. As ker Q=A+D is multiplicity-free, Schur's lemma forces j to act zero on it. Hence ker Q⊂U, while compatibility gives Q(U)⊂Z. Subtracting the exact kernel character yields

    im(Q|U)=2V+(2+ε)P+(2+δ)D.

Comparison with Z forces δ=0 and ε≤2−r. If r=0, j4 vanishes on the whole P-isotypical target; compatibility and Q's P-injectivity force j2 to vanish on the whole P source. Thus ε=1 in that case.

## 4. The second Bockstein excludes every surjective row

The annihilators form an actual negative subpencil: for every negative quadratic a and x∈U, j4T_a x=T_a j2x=0, so T_a(U)⊂Z. U contains the unique actual A source, which lies in ker Q.

If Q(U)=Z, a right inverse s:Z→U gives, for k in this A, a first correction u=−sT_a k with Qu=−T_a k. Then T_a u∈Z⊂im Q, so the second obstruction vanishes. To compare with the original canonical correction u0=−hζ_a, note Qu=Qu0, so u−u0∈ker Q. The imported global first-Bockstein vanishing gives πT_a(u−u0)=0. Thus this is exactly the original second class, not an unrelated lifting obstruction. The pinned theorem says its A-to-P quadratic family is nonzero, contradiction.

For r=2, the character inequalities force ε=δ=0, and Q(U)=Z. This case is impossible, proving det R=0. For r=1, ε=1 would likewise give Q(U)=Z and is impossible; therefore ε=0. For r=0 the previous section already gives ε=1. These are precisely the two rows of the table. In each the difference Z/im(Q|U) is exactly P.

## 5. The complementary two-term complex is actually invertible

Equal quotient characters alone would NOT prove invertibility. Here the actual constituent behavior supplies the missing argument.

On P, if Qx∈Z, then Q(j2x)=j4Qx=0 for every j. Since Q is injective on the P-isotypical source, every j2x=0, so x∈U. Therefore the induced P quotient map is injective. Its source and target have equal multiplicity r, so it is an isomorphism (including the empty r=0 case).

On D, Q:N2_D→N4_D is surjective. It therefore induces a surjection to N4_D/Z_D, and factors through N2_D/U_D. Both quotient spaces are one copy of D, so this is an isomorphism as well. There are no other quotient constituents.

Thus the quotient Q is invertible. Because T_a preserves U→Z, the quotient Q+tT_a is invertible over C[[t]] by a formal geometric-series inverse. The inclusion of complexes [U[[t]]→Z[[t]]]→[N2[[t]]→N4[[t]]] is consequently a quasi-isomorphism. This is a formal reduction of the exact two-term pencil, not a claim of generic full rank. It retains the actual kernel A+D, cokernel P and nonzero second symbol in the reduced complex.

For the filtration statement explicitly, choose constant complements to U and Z and write the full differential over C[[t]] as

    M=[[A,C],[0,B]],

where A=(Q+tT_a)|U and B has invertible constant term. The inclusion i of the restricted complex is the standard first-block inclusion. Define a retraction and degree-minus-one homotopy by

    p0(x,y)=x,
    p1(z,w)=z−C B^(-1)w,
    h(z,w)=(0,B^(-1)w).

Direct multiplication gives p1 M=A p0, p i=1, h M=1−i0 p0, and M h=1−i1 p1. Thus i and p are chain-homotopy inverses. Every displayed map is C[[t]]-linear and carries t^m into t^m for every m; no negative powers of t occur because B(0) is invertible. This proves a filtered chain-homotopy equivalence, and therefore identifies the actual successive t-adic Bocksteins, not merely the unfiltered cohomology. The coefficient a remains arbitrary throughout. These formulas cancel the acyclic QUOTIENT, retaining the annihilator subcomplex; they do not cancel that subcomplex.

## 6. Remaining precise gate and test scope

To exclude full-J compatibility in Type I, it now suffices to establish det R≠0 for the relevant actual balanced top, or otherwise rule out the two reduced rows by a new argument. The balanced-top hypotheses alone have NOT been proved here to force that determinant. The D nonvanishing argument does not establish P-row independence. Type II has shared D support and cannot inherit the Type I isolated-X annihilator bound.

The bounded verifier authenticates nine inputs, derives P⊗A from McKay rules, exhausts the 12 elementary (r,ε,δ) alternatives, and checks exact synthetic joint-row matrices and the formal first-correction identity. A negative control exhibits two rank-one rows with a nonzero common kernel; it prevents inferring joint rank two from their individual ranks. Synthetic matrices are tests of linear-algebra implications, not HM instances or balanced-top realizations. No actual HM coefficient, point, chosen parameter, derivative or rank was evaluated.
