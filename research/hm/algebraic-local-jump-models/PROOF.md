# Algebraic étale and analytic local models for ordinary HM restriction jumps

## Result and exact scope

Fix a smooth quintic X over C and E=F|X, with F the normalized rank-two Horrocks–Mumford bundle. Import the hypotheses, calculations, and audited exact completed-hull theorem of ../formal-jump-normal-forms/{PROOF,AUDIT}.md. Write d=24. Define finite-type pointed C schemes, pointed at the origin,

M1 = Spec C[t1,...,t24,z]/(z²,t1 z),

M2 = Spec C[t1,...,t24,z1,z2]/(z1²,z1 z2,z2²,t1 z1+t2 z2,t2 z1+t3 z2).

At a rank-one point satisfying the imported transversality condition L_p≠0 use M1. At a vertex satisfying the imported surjectivity condition L_p:sl(V)→Sym²K_p* use M2. Then:

1. There is a finite-type C scheme U, a C point u, and a representable étale morphism from U to the fixed-determinant bundle stack near (E,det E≅O_X(-1)). The completion of O_{U,u} is the corresponding ring R1 or R2 of the imported theorem.
2. The pointed schemes (U,u) and (Mi,0) have a common elementary étale neighborhood. This is an exact étale-local algebraic normal form of the ordinary miniversal deformation germ.
3. Their complex analytic germs, with their nonreduced structure sheaves, are isomorphic. Thus the analytic germ of an algebraic minimal versal deformation base has exactly the displayed polynomial equations. This statement does not separately assert versality over arbitrary analytic bases.
4. For each prescribed finite order N, the common étale neighborhood can induce an isomorphism of completions agreeing to order N with any specified completed-ring isomorphism. The neighborhood can depend on N. No claim is made that one algebraic or convergent map induces the specified formal isomorphism at every order.

These are statements about parameter germs, not identifications of a moduli stack with a scheme. The determinant-rigidified object still has μ2 automorphisms. No coarse moduli space construction or stability theorem is needed for (1)–(4). No original mixed-source algebraicity, convergence of chosen formal straightening coordinates, global normal form, or pointwise removal of the rank hypotheses is asserted.

## 1. An actual algebraic stack and a finite-type chart

Let Bun_2(X) denote the stack of rank-two vector bundles on the fixed X. The stack Coh_{X/C} is algebraic and locally of finite presentation: [Stacks Project, Theorem 99.6.1 and Lemma 108.4.2](https://stacks.math.columbia.edu/tag/0DLX). The bundle locus is open. Here is the local argument: in a finitely presented flat family, fibrewise local freeness at a point is equivalent, by the local flatness criterion and finite presentation, to local freeness of the family near that point of X_T. The non-locally-free locus is closed; its image in T is closed because X_T→T is proper. Remove that image. Rank two is then an open-and-closed rank condition. This construction is compatible with base change. Thus Bun_2(X) is algebraic and locally of finite presentation.

Fix the line bundle L=det E=O_X(-1). Let D_L be the stack of pairs (V,δ), where V is a rank-two bundle on X_T and δ:det V→L_T is an isomorphism. It is important to include δ, not just require the determinant's isomorphism class. For a family V over T, the fibre of D_L→Bun_2(X) is Isom_{X_T/T}(det V,L_T). This is an affine algebraic space of finite presentation over T by [Stacks Project, Section 108.3](https://stacks.math.columbia.edu/tag/0DLW). Consequently D_L is algebraic and locally of finite presentation over C. This argument does not require choosing a Picard scheme or a universal line bundle.

The imported simplicity of E gives Aut(E)=G_m. Those automorphisms preserving δ are the scalars λ satisfying λ²=1. The stabilizer group scheme at (E,δ) is therefore μ2, which is finite étale over C. By [Stacks Project, Lemma 101.22.2](https://stacks.math.columbia.edu/tag/0DSL), this point lies in the open Deligne–Mumford locus of D_L. By [Stacks Project, Theorem 101.21.6](https://stacks.math.columbia.edu/tag/06MC), that locus has an étale surjective scheme atlas. Choose a point of the atlas above (E,δ). Because the residue field is C and the fibre is nonempty étale over C, we can choose a C point u. Shrink its scheme neighborhood to an affine finite-type C scheme U. The atlas map remains representable and étale.

Only a neighborhood of this one point is needed. Neither global boundedness of all bundles nor global finiteness of the full stack is being assumed.

## 2. The completed chart is the minimal parameter hull

Fix an identification between the object at u and (E,δ). The family on U gives a map from the formal completion of U at u to deformations of (E,δ), with an identification of their special fibre. Given a small extension A'→A of local Artinian C algebras, a deformation over A', and a compatible chart lift over A, base change the representable étale morphism U→D_L by that deformation. Formal étaleness gives a unique lift of the specified section over A to A'. Thus the induced map to the deformation groupoid is formally étale; after passing to isomorphism classes it is smooth and has a tangent-space isomorphism. In particular, Ô_{U,u} is a minimal hull.

There is no extra infinitesimal chart direction: an étale atlas, rather than a general smooth atlas, was used. Finite inertia does not add equations or tangent directions. One can also check directly that an automorphism of a fixed-determinant deformation reducing to the identity is trivial: the first nonzero term of such an automorphism would lie in H⁰(End₀E) tensored with a small-extension ideal, and this group vanishes. Induction on the length of the Artinian base proves the claim. The special-fibre marking is relevant here; the nonidentity element of μ2 is not an automorphism reducing to the identity.

On a smooth quintic, H¹(O_X)=H²(O_X)=0. The determinant comparison already proved in the imported normal-form proof identifies the fixed-determinant and ordinary bundle parameter functors: determinant deformations have no parameters, and a determinant identification differing by a unit congruent to one is corrected by its square-root scalar. Therefore the formal chart above and the imported critical hull are hulls of the same ordinary parameter functor. Uniqueness of minimal hulls up to noncanonical isomorphism identifies Ô_{U,u} with R_i. Equivalently, the usual mutually lifting comparison maps between two hulls are tangent isomorphisms and give isomorphisms of the complete local parameter rings. None of this identifies the unrigidified stack with its isomorphism-class functor.

## 3. The precise approximation theorem

Use [Stacks Project, Lemma 37.39.2, tag 0CAV](https://stacks.math.columbia.edu/tag/0CAV): locally finite-type schemes over a locally Noetherian base, whose pointed completions are isomorphic over the base local ring, have common elementary étale neighborhoods if that base local ring is a G-ring. The induced comparison may be required to match the given formal isomorphism modulo any specified positive power of the maximal ideal. The proof uses Artin approximation in its Popescu form; the theorem itself applies to nonreduced schemes.

Apply it with base Spec C, schemes U and Mi, and the isomorphism Ô_{Mi,0}≅Ô_{U,u} supplied by Section 2. The field C is a G-ring; both schemes are finite type; both points have residue field C. Every hypothesis is satisfied. We obtain a pointed finite-type scheme (W,w) and maps

(U,u) ← (W,w) → (Mi,0)

which are both elementary étale neighborhoods. This proves the claimed algebraic local form. In particular the relevant henselian local rings are isomorphic. It does not assert an isomorphism of Zariski open neighborhoods.

The finite-order assertion is existential separately for each N. Taking a limit of these separately chosen algebraic neighborhoods does not produce a single algebraic coordinate map. The conclusion is existence of algebraic local equivalences, not algebraization of the particular formal transformations used in the imported potential proof.

## 4. Analytification and the reduced orbit germ

As also recorded in [Stacks Project, Section 41.19, final paragraph](https://stacks.math.columbia.edu/tag/025L), an étale morphism of finite-type complex schemes analytifies to a local analytic isomorphism, also when the schemes are nonreduced. This follows directly from a standard étale presentation: locally it is given by polynomial equations in extra variables with invertible relative Jacobian, so the holomorphic implicit-function theorem eliminates those variables with coefficients in the analytic base algebra. Applying this to both maps out of W yields an isomorphism of complex analytic germs (U^an,u)≅(Mi^an,0), including nilpotents.

Consequently the analytic local algebra is C{t1,...,t24,z}/(z²,t1z), or C{t1,...,t24,z1,z2}/((z1,z2)²,t1z1+t2z2,t2z1+t3z2), respectively. The polynomial presentations are themselves critical loci of t1z²/2 and (t1z1²+2t2z1z2+t3z2²)/2. This does not claim an analytic right-equivalence of the initially chosen cyclic potential: an isomorphism of critical schemes is a weaker assertion.

The reduction of each model is z=0. The common étale neighborhood preserves reduction intrinsically (étale maps over reduced C schemes have reduced source). Hence these equivalences identify the reduced deformation germ with the model's smooth 24-dimensional reduced germ. Under the imported formal identification that reduced germ is precisely the formal orbit germ. No prescribed algebraic orbit parameterization, group action, selected orbit classifying map, or specified ambient coordinates are claimed to commute with the newly obtained equivalence. That stronger decorated statement would need an additional compatible approximation or analytic-classification argument.

## 5. Boundaries of the upgrade

- The assertion is for the fixed variety X and ordinary commutative bundle deformations.
- The rank-one transverse and vertex-surjective hypotheses are unchanged.
- The construction retains the distinction between a parameter scheme chart and its stack; μ2 inertia has not disappeared.
- There is no assertion here about coarse moduli spaces, global quotients, global universal bundles, or stability as a prerequisite.
- Exact algebraic equations exist étale locally; no selected formal coordinate system is proved convergent or algebraic.
- A chosen group orbit map is not algebraized by assertion. Only the intrinsic reduced germ is matched.
- Source-constrained, ordered, noncommutative, or original mixed-source deformation problems are untouched.

Only static reads of the imported proof files, primary-source browsing, and local proof/audit writes were used. No selected HM/source/cofactor computation, numerical rank evaluation, large computation, external service write, or selected-instance computation was performed.
