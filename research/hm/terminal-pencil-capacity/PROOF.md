# Kernel restriction and the terminal capacity of a split linear pencil

Work over C and the same projective parameter line P1 throughout. A coefficient linear pencil is a map S1 tensor O(-1) -> S2 tensor O, with S1,S2 finite-dimensional constant coefficient spaces. A morphism of pencils consists of constant maps f1:S1->T1 and f2:S2->T2 commuting with both linear coefficients. No independent change of the source and target parameter is allowed.

This packet develops a reusable exact obstruction test motivated by PR1122 at commit 65c13bb9a3748a19eb8466f748bd29a5a849ecb5. That proof established a particular actual-primary versus long-terminal-pencil contradiction. Here no actual HM pencil is decomposed, no catalogue entry is tested, and no actual source or coefficient is selected. The contribution is the general kernel-restriction proof, its sharp short-block capacity consequence, and a new full-coefficient rational solver with exact basis output. No claim of novelty in the general theory of matrix pencils is made. In particular this packet does not claim the collaborator's subsequent actual slope-containment or catalogue exclusions as its contribution; its new deliverable is the universal extension lemma and reusable exact coefficient certificate machinery.

## 1. Full faithfulness of kernel restriction

Let two pencils be everywhere surjective, so there are exact bundle sequences

    0 -> K_S -> S1 O(-1) -> S2 O -> 0,
    0 -> K_T -> T1 O(-1) -> T2 O -> 0.

Restriction to the kernels gives a canonical vector-space isomorphism

    Hom_pencils(S,T) -> Hom_bundles(K_S,K_T).                 (1)

Proof. Start with a kernel map u:K_S->K_T and compose it with K_T->T1 O(-1). Applying Hom(-,T1 O(-1)) to the first exact sequence gives an exact segment whose outside terms are

    Hom(S2 O,T1 O(-1)) = Hom(S2,T1) tensor H0(O(-1)) = 0,
    Ext1(S2 O,T1 O(-1)) = Hom(S2,T1) tensor H1(O(-1)) = 0.

Consequently the composite extends uniquely to f1:S1 O(-1)->T1 O(-1). Such a map is constant on coefficient spaces since H0(O)=C. Its composite with T1 O(-1)->T2 O kills K_S and therefore descends uniquely to f2:S2 O->T2 O, also a constant coefficient map. The square commutes and its restriction is u. Conversely any square with zero kernel restriction has f1=0 by the same uniqueness, and then f2=0 because the source pencil is surjective. These constructions are inverse and respect composition. This proves (1).

The assertion requires everywhere-surjective bundle sequences on the same P1. A rank drop, torsion cokernel, parameter-dependent coefficient map, or different parameter identification is outside its hypotheses. For equivariant pencils, the same unique extension is equivariant whenever u is; hence (1) restricts to equivariant morphisms. It does not turn a character match into a compatible actual map.

## 2. Explicit standard pencils

For m>=1 let E_m be the (m-1)-by-m pencil B_m(x,y) whose row i has x in column i and y in column i+1 (indices start at zero). For m=1 this means the zero map C->0. For a nonzero pair (x,y), the rows have rank m-1: use the first m-1 columns when x!=0, or the last m-1 columns when y!=0. The kernel bundle is the line O(-m); a generating polynomial column is

    (y^(m-1), -x y^(m-2), ..., (-x)^(m-1)).

Its entries have no common projective zero and degree m-1 inside O(-1)^m. Thus

    0 -> O(-m) -> O(-1)^m -> O^(m-1) -> 0.

Formula (1) now yields the complete result

    Hom_pencils(E_n,E_m) = H0(O(n-m)),
    dim Hom_pencils(E_n,E_m) = max(n-m+1,0).                (2)

For E2^r -> E_m this dimension is r max(3-m,0). There is also an elementary full-coefficient description. Write F as an m-by-2r matrix, G as an (m-1)-by-r matrix, and order each source copy's columns x,y. The x coefficient equations are

    F[i,2j]=G[i,j],   F[i,2j+1]=0,

and the y coefficient equations are

    F[i+1,2j]=0,     F[i+1,2j+1]=G[i,j].

If m=1 there are no equations: F is arbitrary and G has zero rows, giving 2r parameters and no terminal image. If m=2, F has diagonal-copy blocks G, so G is any one-by-r row and there are r parameters. If m>=3, the overlapping rows force every G entry to zero, then every F entry to zero. Thus (2) includes the sharp boundary m=2, not just the long-block vanishing m>2.

## 3. A sharp terminal image-capacity bound

Suppose an everywhere-surjective target pencil is supplied with an actual coefficient-pencil direct sum

    T = direct_sum over m>=1 of E_m tensor B_m,

where B_m are multiplicity coefficient spaces. This is a hypothesis about the two actual arrows, not a conclusion inferred from kernel degree or degreewise character. Let a coefficient morphism E2 tensor A -> T be given, with r=dim A. Then:

* All components to m>=3 vanish.
* The m=1 components may be nonzero on source coefficients, but have zero terminal target.
* The terminal coefficient map is exactly a map A->B_2 into the terminal target of the E2 summands.

Consequently its rank is at most min(r,dim B_2). This is sharp: every map A->B_2 gives such a pencil morphism, and a terminal injection exists if and only if dim B_2>=r (without additional equivariance constraints). In an equivariant supplied decomposition, an equivariant terminal injection requires an injection of the actual terminal coefficient representation A into B_2 with its induced marking; a numerical capacity bound alone is not sufficient.

This capacity statement is independent of the chosen coordinates inside the given coefficient decomposition. The displayed target summand can change when the decomposition changes; the theorem does not assign an unproved canonical decomposition to an HM pencil.

More generally, suppose the actual ambient target has a coefficient-pencil decomposition T plus a complementary residual pencil R. If the terminal coefficient dimension of R is d, then the terminal image of E2 tensor A has rank at most dim B_2+d. Therefore an actual terminal injection of rank r requires

    r <= dim B_2 + d.                                      (3)

This is only a necessary condition unless the residual maps are also controlled. In PR1122's conditional configuration, T has only m=8 blocks, hence dim B_2=0, while d=6 and r=8; (3) recovers its contradiction. The new general test quantifies exactly how much short-block terminal capacity a different supplied decomposition would need. It does not assert which blocks an actual other candidate possesses and does not extend the source2 exclusion to an unverified larger hypothesis class.

## 4. Reproducible evidence and limits

The stdlib-only verify.py builds both coefficient equations over Q and computes the full rational nullspace by RREF. It emits exact bases, not selected-direction ranks. It compares the E2^r bases to the explicit formulas above for m=1,...,10 and r=1,2,3. It additionally tests all E_n->E_m with n=1,...,6 and m=1,...,10 against (2), checks every returned basis against every coefficient equation, and tests sharp terminal capacities at source multiplicities 1,2,3,8. Fifteen further rectangular direct-sum tests solve the full mixed system, verify all returned basis vectors, prove zero terminal components in every long block, and compare the dimension of the terminal-map space with r times the number of E2 blocks. A control satisfying the x equations but failing y is explicitly rejected; this prevents a one-direction test from masquerading as a pencil morphism. Two independent small rank controls check the elimination helper. All checks use explicit exceptions, not Python assert statements.

Normal and optimized runs give identical RESULT.json with 327 checks. The written sheaf argument proves the general statement; the finite rational tests independently exercise the full-coefficient implementation and the sharp boundaries. They are not proof-assistant verification, actual HM data, or catalogue classification. INPUTS.json pins the motivating PR1122 original; its written proof is retained unchanged for context and its SHA256 and Git blob identity are checked. No transitive mathematical authentication is claimed by that byte check.
