> Publication scope: Nonempty marked lifting problems have equivariant objects; individual objects require fixed isomorphism classes. No underlying lift is manufactured. Historical statements about unresolved mixed classes refer to the source stage; this packet does not supersede the separately stated conditional mixed-vanishing result in PR145.

# Equivariance is effective for a nonempty square-zero module-lifting problem

## Result and precise boundary

Let a finite group G act on a square-zero extension of sheaf algebras, or on a coherently specified square-zero extension of algebroids, over a field of characteristic zero. Fix a finite locally free boundary module **together with its genuine G-action**. Then:

1. If the marked ordinary lifting problem is nonempty, the marked G-equivariant lifting problem is nonempty.
2. A particular marked ordinary lift admits a compatible G-action **if and only if its marked isomorphism class is G-fixed**. Nonemptiness alone does not make every previously selected lift equivariant.
3. Equivariant marked lift classes are precisely the G-fixed ordinary marked lift classes. If nonempty, they form a torsor under the invariant part of the ordinary relative Ext¹. Relative equivariant automorphisms are the invariant part of relative Ext⁰.
4. On a fixed G-invariant marked lift class, compatible actions are unique up to an automorphism inducing the identity on the boundary. That conjugating automorphism need not be unique.
5. For the actual bounded upstairs action constructed in `premise:quantum-swap-gauge/PROOF.md`, this applies to the mixed kernel (st), while retaining an already fixed G-equivariant pure-axis boundary and all its markings.

Thus, for that fixed boundary, quantum equivariance is not an additional **existence** obstruction after underlying mixed-lift existence. This does not construct a lift from an empty lifting problem, repair an arbitrary non-equivariant prescribed boundary, or identify the coarse ambient with an independently proposed corrected model. No retained physical value is evaluated here. At the original source stage the thirty values were unevaluated; this is not a current frontier claim.

## 1. Exact hypotheses and coefficient object

Work on a space X with its sheaf topology, over a field k with |G| invertible. Characteristic zero is sufficient. First take a surjection of sheaves of associative unital k-algebras

    0 → I → A → B → 0,             I² = 0.

No commutativity, central structural O_X-embedding, splitting of A→B, or flatness of A over an auxiliary parameter algebra is assumed. The two-sided ideal I is a B-bimodule: changing a lift of an element of B changes either product by I²=0.

The group acts on X and strictly on this extension. Use a left action on the module category, denoted g*, with g* h*=(gh)*; this is achieved by inverse geometric pullback as in the supplied upstairs construction. The action is k-linear; it may act nontrivially on the deformation parameters.

Fix a finite locally free **left** B-module M̄ and specified isomorphisms

    ρ_g : g*M̄ → M̄,       ρ_g ∘ g*ρ_h = ρ_gh,       ρ_e = id.

A marked lift is a finite locally free left A-module M with an isomorphism θ:M/IM→M̄. Morphisms of marked lifts are A-linear isomorphisms inducing the identity of M̄ via the markings. Write L for this groupoid and T=π₀L for its set of classes. Its group action transports the marking using ρ_g; the boundary action is part of the definition, not something to be chosen afterward.

Set

    N = I ⊗_B M̄,
    F = Hom_B(M̄,N)                   (internal sheaf Hom),
    E^q = Ext^q_B(M̄,N)              (global sheaf-module Ext).

Because M̄ is locally finite free, internal Hom_B(M̄,−) is exact locally, and the local-to-global derived Hom calculation gives

    E^q = H^q(X,F).

These are global Ext groups, not Ext over the ring of global sections. The formula F=End(M̄)⊗I requires additional hypotheses, such as B=O_X and a symmetric O_X-bimodule I; the displayed internal Hom is the general noncommutative formula. For a coefficient that is annihilated by a lower nilpotent ideal, Section 8 gives the corresponding classical simplification.

There are two precise ways to use the cohomology statements below:

- On an arbitrary suitable sheaf site, use the standard classification of gerbes banded by the abelian sheaf F and derived sheaf cohomology.
- For an elementary Čech proof, require a cover trivializing the local module problem, with local comparison lifts on pair intersections, and with Čech cohomology computing H^q(X,F) in the needed degrees. A sufficient algebraic-geometric condition is that X is separated and quasi-compact, F is quasi-coherent over O_X, and one uses a finite affine cover with affine intersections. Local comparisons then exist on the intersections because their F-torsors have H¹=0. A finite G-stable refinement is obtained by adjoining all G-translates. Use the full ordered nerve, transporting labels without sorting.

Only the torsor and automorphism conclusions in Section 2, and their compatibility with G, are needed for the main existence proof. They can equally be supplied by a deformation complex in a more general module problem; they must not be assumed for arbitrary non-flat or non-locally-free module lifts.

## 2. The marked lifting groupoid is linear at square-zero order

For a finite locally free lift M, multiplication identifies

    IM ≅ I⊗_B M̄ = N.

This follows in an A-frame and is therefore canonical and global. An A-linear endomorphism u of M inducing zero on M̄ has image in IM and kills IM: locally u(im)=i u(m), which lies in I²M=0. Consequently it factors uniquely as

    M → M̄ → N → M.

Conversely each B-linear M̄→N defines such an endomorphism. If u and v are two of them, uv=vu=0. Therefore

    (1+u)(1+v)=1+(u+v),             (1+u)⁻¹=1−u,
    Aut_θ(M) = H⁰(X,F) = E⁰        as an additive group.

This argument uses the bimodule structure of I and the order of left-module compositions correctly; it never commutes general algebra elements.

Local marked lifts exist: trivialize M̄ and lift it by A^r. Any two local lifts are locally marked-isomorphic. Indeed a matrix representing the prescribed reduced comparison lifts locally across A→B and is invertible because a matrix invertible modulo a square-zero ideal is invertible. For left modules this statement may be read in the appropriate opposite matrix ring; nilpotent inversion works there too.

The local marked-isomorphism sheaves are F-torsors. Conjugation by a marked isomorphism induces the canonical identity on this band: changing that isomorphism by 1+u acts trivially on 1+F because all products of two relative endomorphisms vanish. The lift stack is therefore a gerbe with the **abelian** band F.

In a suitable Čech cover choose local lifts and comparison isomorphisms reducing to the prescribed boundary comparisons. Their triple failure is 1+c_ijk, with c a two-cochain in F. Associativity, including the ambient algebroid associator if present, gives δc=0. Changing comparisons by 1+b changes c by δb with the chosen orientation. Hence there is an obstruction

    o(M̄,A) ∈ H²(X,F)=E².

It vanishes exactly when the comparisons can be corrected and glued to a global marked lift. Effectiveness here is ordinary sheaf/module descent, not an assertion that a cohomology class alone is a physical module. The general-site version is the same statement about the class of this abelian gerbe.

If L is nonempty, fix M as reference. Its F-valued one-cocycle twists glue local copies of M with the correction units 1+b_ij. Coboundaries give marked-isomorphic results, and every other lift is obtained this way. Thus

    T is a torsor under V:=H¹(X,F)=E¹,
    Aut_θ(M)=W:=H⁰(X,F)=E⁰.

The construction is natural in the extension and the marked boundary. Thus G acts linearly on V,W and affinely on T:

    g(x+v)=g(x)+g(v).

The standard commutative Ext obstruction/classification is also recorded in [Stacks Project, Section 91.4](https://stacks.math.columbia.edu/tag/08L3). The direct band calculation above explains why the locally free assertion used here survives noncommutativity and algebroid twists.

## 3. A nonempty affine lift torsor has a fixed class

Choose x∈T and let b_g=g(x)−x∈V. Then

    b_gh=b_g+g(b_h).

Put

    v = |G|⁻¹ Σ_h b_h.

Since left multiplication permutes the elements h of G,

    g(v)=v−b_g,
    g(x+v)=x+b_g+g(v)=x+v.

Therefore x_*:=x+v is a G-fixed marked isomorphism class. The torsor action in Section 2 realizes x_* by an actual finite locally free sheaf module M_* with the same boundary marking.

This is the explicit vanishing H¹(G,V)=0. It averages differences in an affine space of **marked isomorphism classes**, and realizes the resulting class by square-zero cocycle twisting. It does not average finished transition matrices, tensor together translates and change rank, or assume invariant local frames.

It can change the underlying marked isomorphism class: that distinction is essential.

## 4. A fixed class admits an actual group action

Let (M,θ) represent a G-fixed point of T. By the definition of equality in T, there are global marked comparison isomorphisms

    λ_g : g*M → M,

reducing exactly to ρ_g. Choose λ_e=id. They need not initially satisfy the group law. Define c(g,h)∈W by

    λ_g ∘ g*λ_h ∘ λ_gh⁻¹ = 1+c(g,h).

The defect reduces to the identity because the **specified boundary action** satisfies its group law. Hence it lies in the additive relative automorphism group W, not in an arbitrary multiplicative scalar group.

Conjugation by λ_g on relative automorphisms agrees with the action on W induced from I and ρ_g. It is independent of the choices λ_g, since 1+W is abelian. The resulting W-action is genuine: the discrepancy between two composite conjugations is inner conjugation by 1+c(g,h), which acts trivially on W.

Associativity of three comparisons gives the exact additive cocycle equation

    c(g,h)+c(gh,k)=g c(h,k)+c(g,hk).

Set

    a_g=|G|⁻¹ Σ_k c(g,k).

Average the displayed equation over k. It gives

    c(g,h)=a_g+g a_h−a_gh.

Now define genuine comparison maps

    λ'_g=(1−a_g)λ_g.

Their new defect is

    c'(g,h)=c(g,h)−a_g−g a_h+a_gh=0.

Thus λ'_g ∘ g*λ'_h=λ'_(gh) exactly, and λ'_e=id. The maps are sheaf-module maps, commute with restrictions and all ambient module descent, and still reduce to ρ_g. This supplies the actual compatible semilinear G-action.

Conversely any compatible action supplies marked isomorphisms g*M≅M, so its class is G-fixed. Hence the fixed-class criterion is both necessary and sufficient.

This is H²(G,W)=0, with an explicit finite primitive. There is no further associativity obstruction for this ordinary groupoid of modules: the displayed equality of maps implies all longer group relations. No additional H³ obstruction is silently discarded. Finite-group cohomology vanishing over characteristic zero is consistent with [Stacks Project, Lemma 59.57.6](https://stacks.math.columbia.edu/tag/0A2H); the degree-one and degree-two arguments needed here were proved explicitly.

## 5. Classes, fibers, automorphisms, and uniqueness

Fix one compatible action λ on M. Any other compatible action has the form

    μ_g=(1+d_g)λ_g,
    d_gh=d_g+g d_h.

Conjugating λ by a marked automorphism 1+w gives a new action with difference w−g w. For a one-cocycle d, the average w=|G|⁻¹Σ_h d_h satisfies d_g=w−g w. Therefore all compatible actions on this fixed marked lift are conjugate by a marked automorphism. The ambiguity in that conjugating automorphism is W^G.

More generally, let L^G denote marked lifts with compatible actions and equivariant marked isomorphisms. The forgetful map gives a bijection

    π₀(L^G)  ≅  T^G.

Surjectivity is Section 4. For injectivity transport one action along an ordinary marked isomorphism and use the preceding conjugacy calculation. Its statement about classes does not say that the forgetful functor is fully faithful: ordinary isomorphisms need not be equivariant.

If nonempty, T^G is a torsor under V^G, since the difference of two fixed points is invariant and adding an invariant vector preserves fixedness. For each equivariant marked lift,

    Aut_{θ,G}(M)=W^G.

For a fixed lift class in arbitrary characteristic the action obstruction would be in H²(G,W), with action structures modulo marked conjugacy a torsor under H¹(G,W). Here both groups vanish. This is the exact fiber description.

Useful uniqueness distinctions:

- If E¹=0, every ordinary lift lies in the same G-fixed class and each admits a compatible action.
- If only (E¹)^G=0, there is exactly one equivariant marked lift class when nonempty, but there may be many non-equivariant ordinary lift classes.
- Uniqueness of an equivariant class means uniqueness up to equivariant marked isomorphism. The isomorphism itself is unique only when (E⁰)^G=0.
- No preferred transition representative or preferred literal action follows from these statements.

## 6. Equivalent obstruction comparison through invariants

Define equivariant sheaf cohomology by the group/sheaf total complex

    H_G^n(X,F)=H^n(RΓ(G,RΓ(X,F))).

For a strict G-compatible resolution, or a suitable G-stable Čech model, there is the spectral sequence

    H^p(G,H^q(X,F)) ⇒ H_G^(p+q)(X,F).

The Reynolds projection makes invariants exact over k. Indeed an invariant element of a quotient has an arbitrary lift whose finite average is invariant. Hence H^p(G,−)=0 for p>0, and

    H_G^n(X,F) ≅ H^n(X,F)^G.

The G-equivariant lift gerbe has an obstruction o_G∈H_G²(X,F). Its forgetful image is the ordinary obstruction o∈H²(X,F), which is G-invariant by functoriality. Under the displayed isomorphism these are the same invariant class. In particular,

    o_G=0  ⇔  o=0.

The corresponding equivariant deformation and automorphism groups are (E¹)^G and (E⁰)^G. This agrees with the constructive proof and does not evaluate o. If working with a more general deformation complex C rather than the locally free band F, the same conclusion requires that C genuinely control this marked lifting groupoid and be supplied with the coherent G-action. Then H^n(C^G)=H^n(C)^G; an unrelated endomorphism cohomology calculation is not by itself such a model.

## 7. Algebroid twists and strict versus weak group data

The proof applies to a square-zero quotient of k-linear algebroids when the quotient and ideal are given compatibly with all local rings, overlap equivalences/bimodules, and associators. Require that the locally finite free module categories form effective stacks and that reduction is locally the square-zero ring quotient of Section 1. Fix the boundary module with its actual compatible group linearization.

On a local neutralization the coefficient is

    F_i=Hom_{B_i}(M̄_i,I_i⊗_{B_i}M̄_i).

The boundary module comparisons and ambient equivalences transport these sheaves. On triples their conjugation action obeys the honest cocycle because it acts on a genuine boundary module and its coefficient module; the ambient associator is already included. Thus F is a global sheaf. The local relative automorphism calculation and the lifting gerbe proof are unchanged. Noncentral triple units must be included in those comparison diagrams, not declared central for convenience.

If the ambient action is strict, Section 4 produces a strict module action relative to it. If it is a coherently specified weak action with structural maps α_(g,h):g*h*⇒(gh)* and the pentagon, replace the group-law expression by

    λ_g ∘ g*λ_h = λ_gh ∘ α_(g,h),

and use the matching boundary equation. The pentagon gives the same additive defect cocycle. The result is an honest equivariant object for that weak action, meaning all those coherence equations hold. It does not claim to turn unspecified weak ambient data into a strict action.

Merely knowing group elements act on isomorphism classes, or having a projective classical boundary action, is insufficient. A defect already nontrivial at the boundary may live in k^× or a nonabelian automorphism group; the square-zero additive averaging argument cannot remove it. The actual supplied upstairs construction avoids this problem by giving strict bounded ambient data and exact root-sign comparisons.

## 8. Application to the bounded mixed extension with fixed pure axes

Use the root-transported upstairs algebroid from `premise:quantum-swap-gauge/PROOF.md`, especially Sections 6–8. Its group is

    G=G₁₂×G₃₄,       G_ab=(Z/2)²⋊S₂,

acting on X=C⁴ and on R=k[s,t]/(s²,t²). It has order 64, and s,t carry the respective pair determinant characters. The antisymmetric and root-transported presentations have a strict action; the original source presentation has the explicitly coherent action transported by the units W_g. All uses here respect that distinction.

Let A_mix denote that fixed algebroid and let

    I=st A_mix,       B=A_mix/I.

Locally I=st O_X; I²=0 and sI=tI=0 on both sides. The ideal is G-stable, with the product character on its formal symbol st. The quotient is the **pure-axis boundary**, not the full mixed algebra. Fix a finite locally free B-module M_∂, with its full G-action and marking data on both pure axes and their common classical reduction M₀.

If the boundary is specified by pure modules M_s,M_t and an identification of their reductions with the same M₀, it is their fiber-product module over the corresponding fiber-product ring/algebroid. Local freeness follows locally by choosing pure frames compatible with the common reduced frame: lift the necessary reduced change of basis across each nilpotent quotient. These then give B^r. Specified compatible pure actions glue to the boundary action. This uses actual compatible pure module data; it does not produce them from a candidate class.

Because I is annihilated by s,t,

    I⊗_B M_∂ ≅ I⊗_{O_X}M₀,
    Hom_B(M_∂,I⊗_B M_∂)
      ≅ Hom_{O_X}(M₀,I⊗_{O_X}M₀)
      ≅ End_{O_X}(M₀)⊗_{O_X}I.

The last equality uses the actual symmetric classical O_X-bimodule I in this mixed kernel. Thus

    E^q_mix = H^q(X,End(M₀)⊗I).

These coefficients are quasi-coherent and admit the finite affine-intersection Čech model already present upstairs. All modifications used in Sections 2–5 are identity modulo st. They therefore preserve both pure-axis modules, their markings, and their specified actions. No pure coefficient is changed and the st term is retained.

Consequently, for this **fixed G-equivariant boundary**, an ordinary mixed module lift exists if and only if a genuine G-equivariant mixed module lift exists. A supplied particular mixed lift can receive that action exactly when its marked class is fixed. If (E¹_mix)^G=0 the equivariant lift class is unique when it exists; if E¹_mix=0 every supplied marked lift has the property. These different hypotheses must not be interchanged.

The coarse comparison of `premise:coarse-quantum-atlas/PROOF.md`, Sections 7–8, now applies to such an equivariantized lift when its classical inertia is trivial after root transport. Root transport supplies the known classical cancellation; this theorem supplies no invariant frame for a module with nontrivial classical inertia. A perfectly genuine group-linearized module with nontrivial stabilizer representation need not be a coarse locally free module.

Thus the actual coarse module existence comparison has one fewer independent hypothesis: after fixing the genuine equivariant boundary, quantum equivariance of **some** mixed lift follows from underlying mixed-lift existence. Identification with the separately proposed corrected coarse ambient, ordinary mixed-lift existence, and all physical evaluations remain separate.

## 9. Why an arbitrary selected lift need not work

Here is a counterexample entirely within finite locally free sheaf modules. Let X=P¹_k, A=O_X[ε]/ε², B=O_X, and let G=Z/2 act trivially on X,A and ε. Give

    M̄=O_X ⊕ O_X(2)

the boundary involution diag(1,−1). The trivial extension of this bundle is an equivariant marked lift. Its ordinary marked lift classes form the vector space

    H¹(P¹,End(M̄))ε = H¹(P¹,O(−2))ε ≅ k.

The off-diagonal summand Hom(O(2),O)=O(−2) is acted on by −1 under conjugation by the boundary involution. The elementary two-affine Čech calculation gives H¹(O(−2)) as a one-dimensional Laurent quotient; the other End summands O,O,O(2) have zero H¹. Hence every nonzero class x satisfies g(x)=−x≠x and admits no action reducing to the fixed boundary action. The zero class does.

All these classes are realized by genuine finite locally free rank-two modules using the square-zero one-cocycle twists of Section 2. This disproves the stronger assertion that averaging can linearize every existing marked lift without changing its class.

## 10. A subgroup-rigidity criterion for keeping a supplied pure lift

Let H⊂G be any subgroup. Suppose the fixed boundary has a full G-action, the ambient has the action specified above, an H-equivariant marked lift M_H is supplied, and

    (E¹)^H=0.

Then the **same underlying marked module M_H**, with its specified H-action, admits an extending full G-action.

Proof: ordinary nonemptiness gives some G-equivariant lift M_G by Sections 3–4. The H-equivariant lift classes form a nonempty torsor under (E¹)^H, so there is an H-equivariant marked isomorphism M_G|_H≅M_H. Transport the full G-action along that isomorphism. Its restriction to H is exactly the supplied H-action, and its reduction is the fixed full G-boundary action. No normality of H is needed for this argument. If (E⁰)^H=0 the marked H-equivariant comparison is unique, but uniqueness is not needed for existence.

For the normal deck subgroup H=(Z/2)^4 of the signed-pair group, a pure parameter has character {1,2} or {3,4}. If the imported physical Ext¹ table has zero in every weight-two character, then (E¹_pure)^H=0. The table does not say that all upstairs E¹ vanish. Likewise a mixed parameter has character {1,2,3,4}, so a weight-four zero gives only the corresponding invariant rigidity.

The source [PR 1 comment 6260553958](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6260553958), explicitly states that the dimensions (79,2,0,0,0) are **per deck character** by weight, totals 87, and imports the weight-two and weight-four zeros for its corrected model. It does not supply a verification that any particular physical raw pure representative is H-equivariant. The subgroup criterion is therefore conditional on that representative's genuine deck action, its marked boundary compatibility, and the applicability of the imported coefficient identification. None of those are inferred from this numerical table alone.

## 11. Audit boundary

This proof uses only static structural algebra, finite averages, and sheaf descent. No source operations, physical operation matrices, input evaluations, detector computations, source writes, or large computation were performed.

It removes an additional equivariance-existence obstruction in the specified square-zero lifting problem. It preserves the distinctions between a nonempty lift groupoid, a fixed marked lift class, a prescribed pure boundary, a strict versus coherent weak ambient action, and trivial inertia for coarse descent. It does not identify the actual mixed ambient with a proposed corrected model, prove existence of the designated carrier deformation, or determine any of the thirty retained physical values.
