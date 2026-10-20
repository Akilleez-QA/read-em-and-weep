# Effective invariant affine atlas for the nilpotent root-transported algebroid

## Result

For the stipulated **actual algebraic sheaf** star-algebroid on X=C² with its coherent pair-group action, the global effectivity gap can be closed. Choose affine opens V_i of Y=P² and put U_i=p^{-1}(V_i). Each U_i is an invariant affine scheme. The genuine equivariant classical root N|U_i lifts to a locally rank-one module of the original algebroid on U_i, with its group coherence. Its endomorphism algebra is an actual sheaf chart of the root-transported ambient. The internal comparison bimodules have invariant generators on U_i∩U_j. Invariant pushforward therefore gives a coherent algebra-and-Morita atlas on the V_i.

This is already a Zariski atlas, hence uses an étale covering of P². It does **not** assert that the ramified finite map p:C²→P² is étale. It does not identify the resulting algebroid with the independently prescribed corrected downstairs model. It does not construct a global root module or the desired rank-two carrier, and all thirty retained values remain unknown.

The proof uses finite algebraic nilpotent layers, affine sheaf cohomology, and finite-group averaging. No completion or algebraization theorem is needed. The source's existing premise that its differential expressions and cocycles are genuine algebraic sheaf data remains explicit: a formal jet dictionary alone would not meet this theorem's hypotheses.

## Sources and scope

Historical context: [6267584308](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6267584308), together with preceding [6265444022](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6265444022) and [6266447817](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6266447817). These respectively provide the internal-root residue cancellation, coherent pair action, and actual finite quotient/coefficient geometry.

Mathematical dependencies:
- [research/hm/null-internal-root-descent/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/557009fe1da15f09a3f409a5e66168defe8ef00d/research/hm/null-internal-root-descent/RESULT.md);
- [research/hm/null-strictification-gluing/invariant-gluing-0841/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/dcecef425c41063dc3ddc42f5285ee39c42e431e/research/hm/null-strictification-gluing/invariant-gluing-0841/RESULT.md);
- [research/hm/null-pair-swap-coherence/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/0050df8fa957b9f7f5e1b21137c63bffc646a1eb/research/hm/null-pair-swap-coherence/RESULT.md);
- [research/hm/null-actual-source-factorization/classical-root/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9bb53d934ad86e50d8519a35d663f9a96fa481d/research/hm/null-actual-source-factorization/classical-root/RESULT.md);
- [research/hm/null-strictification-gluing/strictification-0736/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/dcecef425c41063dc3ddc42f5285ee39c42e431e/research/hm/null-strictification-gluing/strictification-0736/RESULT.md);
- [research/hm/null-actual-source-factorization/physical-factorization/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9bb53d934ad86e50d8519a35d663f9a96fa481d/research/hm/null-actual-source-factorization/physical-factorization/RESULT.md).

The underlying classical root is pinned in [the carrier definition](https://github.com/Akilleez-QA/read-em-and-weep/blob/3bdc6cb28ecd75cfefb3cb0d85f42d5bcde8cc7f/research/hm-carrier-and-atlas.md#L11-L15). The mixed product is pinned in [the supplied ambient specification](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-second-order-raw-closure/PROOF.md#L35-L44).

Standard commutative geometry used below: higher cohomology of quasi-coherent sheaves on an affine vanishes ([Stacks, 01X8](https://stacks.math.columbia.edu/tag/01X8)); affine-intersection Čech cohomology computes sheaf cohomology ([Stacks, 01XD](https://stacks.math.columbia.edu/tag/01XD)); a finite morphism is affine ([Stacks, 01WG](https://stacks.math.columbia.edu/tag/01WG)). The noncommutative finite-layer lifting and invariant-atlas deductions are proved below, rather than inferred from a commutative deformation theorem.

Only static reading and mathematics were performed. No physical evaluation, physical matrices, model imports, source execution, experiments. Here C denotes the stipulated smooth elliptic curve, not the affine line.

## 1. Precise sufficient theorem

Let k have characteristic zero, let G be finite, and let p:X→Y be a finite geometric quotient of a separated finite-type k-scheme, with O_Y=(p_*O_X)^G. Assume Y has an affine open cover. Work with an actual sheaf algebroid A on X with coherent G-action, including its restriction, Čech, group, and mixed coherence maps.

Assume the following finite nilpotent deformation conditions.

1. There is a G-stable finite multiplicative filtration J^r, with J^N=0, whose reduction A_0 is the usual O_X algebroid, equivariantly identified with it. In particular its classical group coherence is not an unspecified projective cocycle.
2. Locally A has sheaf-of-algebras presentations D, with D/J=O_X. The layers K_r=J^r/J^{r+1} are actual quasi-coherent O_X-bimodules with coincident left and right O_X-actions. They are compatible under the algebroid transitions, so define G-equivariant quasi-coherent coefficient sheaves. The same statement applies to the successive kernels in Hom sheaves of locally free rank-one modules.
3. The presentations, multiplication, invertible overlap bimodules, and coherence are algebraic sheaf data. Local rank-one modules and invertible morphisms lift locally across each nilpotent step. For sheaf algebra presentations this follows by taking the free rank-one module and lifting transition units; nilpotent unit lifting is a finite algebraic operation.
4. A genuine G-linearized line bundle N on X is specified as an A_0-module. Its fiber inertia need not be trivial.

Then, for every affine V⊂Y, U=p^{-1}(V) admits a G-equivariant locally rank-one A-module P_V lifting N|U. The end algebra

    D_V = End_A(P_V)^op

is an actual sheaf algebra on U with genuine G-action. For any two such choices on invariant affine opens, the usual internal Morita comparison P'_VW has canonical equivariant reduction Hom_O(N,N)=O and admits an invariant generator on the affine intersection. The invariant sheaves

    B_V = (p_*D_V)^G,
    Q_VW = (p_*P'_VW)^G

are therefore algebras and invertible rank-one bimodules on the downstairs opens, with coherent composition. They form an effective algebroid atlas on Y. Choices produce equivalent presentations of the same invariant root-transported algebroid, not a preferred global algebra or preferred splitting.

The ordinary hypothesis that finite affine intersections remain affine holds here because Y=P² is separated. The conclusion may instead use an affine refinement of overlaps whenever necessary.

## 2. Equivariant affine acyclicity with a moving-point group action

Fix U=p^{-1}(V), which is affine since p is finite. A finite group-stable affine cover of U is obtained by taking a finite affine cover and all its translates. Since X is separated, finite intersections of these opens are affine. Use the full ordered Čech nerve, including repeated labels; group elements transport labels as well as sections.

For a G-equivariant quasi-coherent sheaf K on U, consider

    C^a(G, Čech^b(U_cover,K)).

Its total complex computes equivariant Čech cohomology. Taking Čech cohomology first leaves Γ(U,K) in degree zero and nothing above: U and all cover intersections are affine. Taking group cohomology next leaves Γ(U,K)^G in degree zero and nothing above: averaging by |G|^{-1} makes invariants exact. Thus

    H^n(Tot C^•(G,Čech^•(K))) = 0   for n>0.       (1)

This is the elementary calculation often expressed as cohomological affineness of [U/G]. The calculation is made on actual algebraic sections. It neither treats elements moving x as automorphisms of O_X,x nor assumes that an orbit is a disjoint union of Zariski-open points.

## 3. Lifting the root locally on invariant affines

Let A_r denote reduction modulo J^{r+1}. Begin at r=0 with the actual G-linearized line N|U.

Suppose P_{r-1} has been constructed, with its exact group and Čech coherence. Locally choose free rank-one lifts to A_r. Lift the transition isomorphisms and the group transport isomorphisms. Such lifts exist after an affine refinement: their Hom kernels have quasi-coherent finite layers and affine H¹ vanishes. A lift of an isomorphism remains an isomorphism locally because its reduction is invertible and the kernel is nilpotent.

The lifted isomorphisms need not yet obey their identities. There are three kinds of defects:

- a Čech triple-composition defect, of bidegree (0,2);
- a group/Čech compatibility defect, of bidegree (1,1);
- a group-composition defect, of bidegree (2,0).

Each is the identity modulo the new top layer K_r. At this step K_r²=0 and it is annihilated by the lower nilpotent ideal. Thus 1+K_r is its additive group, and conjugation by a classical line transition acts trivially on K_r. The existing actual pentagon and mixed coherence identities imply that the three defects together form a degree-two cocycle in the total complex of Section 2. This assertion uses the identities of the actual units, not only their inner automorphisms.

By (1) that cocycle is a coboundary. Modify the lifted Čech and group isomorphisms by the corresponding degree-one cochain in 1+K_r. Its total differential cancels all three defects at once. Since K_r²=0, this cancellation is exact at this stage. The result is a coherent equivariant P_r with the specified reduction P_{r-1}.

Inducting through the finitely many layers gives P_V. No infinite series, approximation, or choice of unrelated completed stalks occurs. Difference/isomorphism problems with fixed classical identification are governed at each stage by degree one in the same complex; its vanishing also supplies equivariant comparison isomorphisms on invariant affine overlaps.

This argument is valid even when N|U is nontrivial as a line bundle: it starts with its genuine transition cocycle, not a nonexistent global frame. The coefficient sheaf governing endomorphism defects is End(N)⊗K_r=K_r. Equivariantly this identity is canonical: the character of N cancels that of its dual. Nontrivial root inertia therefore does not obstruct this local lifting.

The construction does not claim that P_V descends to a module on the coarse space; it ordinarily does not. It is an auxiliary root Morita module on U with its original root inertia. Nor do the different P_V glue to a single global module on X: that separate gluing may have a nonzero higher-cohomology obstruction on the projective space.

## 4. Actual end-algebra charts and internal comparisons

An equivariant module object over a coherently acting algebroid induces a genuine action on its endomorphism sheaf. Conjugating an endomorphism by the module transport maps gives the action; the coherence of the module and algebroid cancels in the group-composition identity. Thus D_V is a sheaf algebra with strict action over the geometric action on U. Its reduction is End_O(N)^op=O_U, canonically and G-equivariantly.

Writing P_i for the local (A,D_i) root Morita module and Q_i for its inverse, the internal comparison is

    P'_ij = Q_i ⊗_A P_j,                              (2)

with the original algebroid overlaps inserted when using distinct presentations. Equivalently it is the appropriate Hom sheaf between the two local root modules. This is the same internal object Q_i⊗B_ij⊗P_j isolated in the root-descent audit. Its reduction is canonically Hom(N,N)=O, with invariant section id_N. The inter-ambient P_i itself reduces to N, and is not being declared inertia-neutral.

On U_ij=p^{-1}(V_i∩V_j), the sheaf P'_ij is locally rank one and its successive nilpotent layers are quasi-coherent. The reduction map on sections

    Γ(U_ij,P'_ij) → Γ(U_ij,O)

is surjective: the kernel has a finite filtration by quasi-coherent sheaves on an affine, hence H¹(kernel)=0 by successive long exact sequences. Lift 1=id_N to a section e. Average over G:

    e_inv = |G|^{-1} Σ_g g(e).                         (3)

Its reduction is still 1. Locally, after choosing any left generator of P'_ij, the coefficient of e_inv reduces to an invertible function. Its coefficient is therefore a unit in the local sheaf algebra by nilpotent unit lifting. Hence e_inv is a generator everywhere on U_ij. This proves invariant local freeness directly on actual sections, including every ramification stratum, without any assertion that p_*D has local stalks.

The same argument also shows that the reduction map D_i→O has no section-surjectivity problem on these invariant affine opens. Its kernel is a finite extension of acyclic layers. No central embedding O↪D_i is assumed: cohomology is used only on the associated layers and on exact sequences of additive sheaves.

## 5. Invariant pushforward, tensor products, and exact coherence

For W⊂V_i define B_i(W)=D_i(p^{-1}W)^G. This is an actual sheaf: pushforward and equalizers preserve sheaves. Define Q_ij similarly. Restriction is inherited from actual upstairs restriction, and G acts on p^{-1}W for every W. Thus the group acts over the identity on the downstairs pushforward site even though it moves upstairs points.

Choose the invariant generator e_ij of Section 4. On every subopen of V_ij,

    Q_ij = B_i e_ij.

The right action determines an equivariant sheaf algebra isomorphism φ_ij:D_j→D_i by e_ij b=φ_ij(b)e_ij. Restriction to invariants proves that Q_ij is an invertible (B_i,B_j)-bimodule.

For two overlaps, e_ij⊗e_jk is invariant and is a left generator of P'_ij⊗_{D_j}P'_jk. Therefore the canonical map

    Q_ij ⊗_{B_j} Q_jk
        → (p_*(P'_ij ⊗_{D_j} P'_jk))^G               (4)

is an isomorphism, verified on those generators. This is a special tensor statement for the proved invariant-basis class, not a claim that arbitrary invariants commute with tensor products.

Compose (4) with the invariants of the actual upstairs Morita composition. Its associativity follows because both iterated comparisons send an elementary invariant tensor to the same upstairs tensor, and upstairs composition is associative. All triple units, including nilpotent mixed units, are retained. In invariant frames one obtains the ordinary exact algebra-map/triple-unit algebroid presentation.

Stackifying this presentation, or gluing its module stacks by the invertible Q_ij, gives the required effective algebroid. Effectivity here means actual sheaves, functors, and coherence on an open cover; it does not mean the result is globally represented by one sheaf algebra.

The reduction B_i→O_{V_i} is surjective on an affine basis by the preceding finite-layer H¹ vanishing and averaging. Its kernel is nilpotent. Associated filtered layers are obtained from actual invariant pushforward layers. This does not silently identify powers of invariant ideals with invariants of ideal powers; coefficient-product identifications remain a separate calculation when needed.

## 6. Why stabilizer/completed-local shortcuts are unnecessary and potentially wrong

At an individual geometric point x, only its stabilizer G_x acts on its local ring. The full group acts on the entire orbit. Finite pushforward stalks can be semilocal, not local. A strict-henselian base change splits the finite fiber into local components and permits a stabilizer description, but is not required by the construction above.

A semilocal version of the invariant-generator argument is also valid with suitable actual finite-module hypotheses: reduce at all points of an orbit, choose a nonzero vector at one point fixed by its stabilizer, and transport it to the other points. This gives an invariant tuple of residue generators. Lift the tuple to the semilocal module, average, and apply the semilocal Nakayama argument to obtain a generator. Merely averaging a lift supported at one orbit point, without constructing that invariant tuple, is not the correct proof.

We do not need this auxiliary reduction. Our internal comparison has the stronger property that its whole classical sheaf is canonically O, with invariant section 1. Affine H¹ supplies a section lift; averaging and nilpotence prove its generator property on an actual neighborhood. No completed-local solution is being asserted to spread or algebraize.

A pointwise residue condition alone, without actual sheaf data and classical coherence, does not imply this theorem. For example, even for the trivial group an unspecified nonneutral classical gerbe is not neutralized by averaging. The supplied ambient avoids that issue because its reduction is the usual O algebroid with F=id, A=1, and the root is a genuine line cocycle. Likewise arbitrary analytic/formal charts with no algebraic restrictions would fail assumption 3.

## 7. Instantiation for the supplied pair and mixed ambients

For the pair, X=C², G=W₂=(Z/2)²⋊S₂, Y=P², and p is the finite quotient of degree eight. Take the three standard affine opens of P²; their inverse images and all their intersections are invariant affines. The ramification divisor does not affect their affineness.

The stipulated pair ambient has local algebra O_X⊕sO_X with s²=0, differential product m+sπ/2, identity unary overlaps, and actual units 1+s b. Its nilpotent layer is O_X with the indicated parameter character. The antisymmetrized presentation supplies the coherent genuine group action; the ordered presentation is related to it by the exact central overlap gauge already proved in [research/hm/null-pair-swap-coherence](https://github.com/Akilleez-QA/read-em-and-weep/blob/0050df8fa957b9f7f5e1b21137c63bffc646a1eb/research/hm/null-pair-swap-coherence/RESULT.md). These are finite algebraic differential expressions and regular overlap cochains on the stipulated algebraic cover. Thus the layer is quasi-coherent and the reduction is genuinely equivariantly O_X, not projective.

The root N_pair=O_C(O)⊠O_C(O) is a genuine G-linearized line. It meets assumption 4 even though its inertia is nontrivial at some branch points. Sections 2–5 therefore construct the desired effective quotient atlas. Local end-algebra presentations agree, up to the actual Morita/gauge changes, with root transport by lifts of the same N cocycle: both are built from the same local root Morita modules. Changes of lifts or refinements alter only the presentation equivalence.

For X=C⁴ and the two-pair group W₂×W₂, use products of the affine opens on P²×P². The original mixed algebra is the stipulated external product over k[s,t]/(s²,t²). With J=(s,t), J³=0; its graded layers are the two parameter-character copies of O_X in degree one and the product-character copy stO_X in degree two. They are quasi-coherent. The mixed product and full triple unit are the already supplied finite formulas, and the full group/Čech coherence retains their st terms. The same finite lifting proof works through both layers, or one may take tensor products of separately constructed pair root modules on product affine opens. It proves ambient atlas effectivity, not existence of a global mixed carrier module.

For the étale site, specifically in the stipulated algebraic differential setting, the products extend using the unique étale extension of the underlying derivations; line bundles and the algebraic module/gluing data extend accordingly. One may base-change the finite quotient along each downstairs étale map and apply the same finite-layer construction. This extension to arbitrary small-étale opens is not a conclusion of the abstract theorem for an arbitrary sheaf of k-algebras. Its Zariski effectivity conclusion needs no such extension: the Zariski cover already consists of étale maps. The ramified quotient morphism itself is not being called étale.

## 8. Remaining obligations

Within the source's stipulated actual algebraic sheaf interpretation, the effective quotient-atlas premise is now established. There is no additional global root-inertia obstruction to its internal Morita overlaps.

Still open and separate:

1. Compare this actual invariant root-transported algebroid with the prescribed corrected downstairs ambient, including unary overlap maps, full triple units, reductions, and all mixed coefficient products and st terms. Local affine neutralizations are noncanonical and do not supply that comparison automatically.
2. Construct the intended global quantum carrier with its specified equivariance, or determine its remaining mixed obstruction. The affine auxiliary rank-one root lifts used here do not solve this global rank-two problem.
3. All thirty retained physical values remain unknown. No vanishing or evaluation is implied.

If the stated geometric interpretation of the source formulas is withdrawn and only completed-local or symbolic data remain, this result becomes conditional at exactly assumption 3; neither averaging nor formal local calculations can replace actual algebraic sheaf restrictions. No additional numerical/physical execution was used to strengthen that input.

## 9. Factorwise choices and the retained mixed term

Throughout this section, external product means the prescribed **algebraic differential external product**: on affine product charts use tensor coordinate rings with the specified differential multiplication, then use its algebraic restrictions/localizations to arbitrary opens. It does not mean the topological inverse-image tensor of arbitrary sheaves of k-algebras. Zariski rectangles do not form a basis for the algebraic product topology, so checking rectangles and sheafifying alone would not justify the construction. The supplied differential ambient and its localization data are essential here. Modules and morphisms below are glued in local algebraic frames with these same restriction maps.

The invariant-affine construction can be made separately on each pair. On product opens choose

    P_(i,a) = P^P_i ⊠_k P^Q_a,

where the first factor is over k[s]/s² and the second over k[t]/t². This is a locally rank-one module for the specified external-product ambient over k[s,t]/(s²,t²), with the tensor product of the two actual equivariant structures. Its reduction is the specified N_P⊠N_Q. It is therefore an admissible choice in the preceding construction, without making a new independent choice at mixed order.

The transformed end algebra is the external product of the factor transformed end algebras. The canonical map is an isomorphism locally in rank-one frames and hence globally as a sheaf; the opposite convention End(P)^op is used on both factors. The internal comparison bimodules and their evaluation/composition maps likewise factor. If e^P_ij and e^Q_ab are the invariant generators, e^P_ij⊠e^Q_ab is the product invariant generator. Thus the invariant tensor comparisons are compatible with these factorwise choices.

For the product finite group, the two Reynolds projectors commute. On affine product coordinate rings their tensor projector has image the tensor product of their images, by the direct-sum decompositions into projector image and kernel over k. The resulting identification is extended using the prescribed algebraic differential restrictions/localizations, and is checked on arbitrary restricted local rank-one frames; it is not obtained by treating rectangles as a topological basis. This identifies the factorwise invariant construction with the invariant construction of this prescribed algebraic external-product presentation. No scalar s or t is assumed invariant. The stable reduction ideals are always taken downstairs as actual invariant intersections; an additional claim about their multiplication still requires its own comparison.

All external-product composition units are multiplied in full. In particular (1+s a)(1+t b) includes st ab, and the mixed product of factor products includes its st differential term. The construction does not truncate to the direct sum of two first-order algebroids. This proves that one may preserve the specified external-product ambient structure while establishing atlas effectivity. It still supplies no identification with a separately prescribed corrected mixed ambient.
