> Publication scope: Conditional effective descent includes noncentral nilpotent layers and the uniform-neighborhood condition for formal towers. It does not identify a physical algebra. Historical statements about unresolved mixed classes refer to the source stage; this packet does not supersede the separately stated conditional mixed-vanishing result in PR145.

# Global strict-equivariant module descent at finite quotients

## Result and scope

A global sufficiency theorem is proved below, not merely a stalk lemma: trivial inertia gives invariant frames over **quotient-open neighborhoods**; these frames glue uniquely to a locally free module over the fixed sheaf algebra; the extension/invariants functors are inverse, including on morphisms; stable-ideal reduction and compatible nilpotent towers commute with this descent.

There are two versions. The orbit-algebra theorem isolates hypotheses usable for a noncentral deformation. A concrete finite coherent central deformation satisfies them without an unproved spreading or pushforward assertion. A separate noncentral theorem replaces orbit-projectivity by quasi-coherent nilpotent layers and affine section lifting. A formal-tower result includes the uniform-neighborhood hypothesis needed to avoid infinitely shrinking opens. None identifies an actual physical ambient or supplies an actual physical module.

The supplied local inputs were read in `../weak-action-strictification/PROOF.md`, `../weak-action-strictification/SCALAR_INERTIA.md`, and the two source audits in `premise:ramified-module-comparison/`. The argument here is an independent algebraic globalization under its explicitly stated hypotheses. The underlying audited source is https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6261960300 . No external operation or physical calculation is involved.

## 1. Geometric and algebraic hypotheses

Let X and Y be schemes of finite type over C, and let a finite group G act on X. Suppose p:X→Y is a finite quotient: Y has trivial G-action, O_Y=(p_*O_X)^G, and the closed points of each nonempty fiber form a single G-orbit. Assume p is surjective. These fiber properties can instead simply be included as hypotheses when using a specific quotient construction. Write B=p_*O_X.

For a closed point y, B_y is a finite commutative algebra over the local ring O_{Y,y}, and is semilocal. Its maximal ideals correspond to the points x of p^{-1}(y); their residue fields are C. Thus

    B_y/J(B_y) = product_{x over y} C.

One elementary justification is that integrality makes every maximal ideal of B_y lie over the maximal ideal of O_{Y,y}; the finite-dimensional C-algebra B_y/m_y B_y has finitely many maximal ideals and residue C; the Chinese remainder theorem then gives the display. It is not asserted that B_y itself is a product of local rings.

### Orbit-algebra hypotheses

Let E be a sheaf of unital C-algebras on Y, possibly noncommutative, equipped with a genuine action of G by sheaf C-algebra automorphisms. Suppose there is a G-equivariant surjection of sheaf algebras

    E → B

with nilpotent kernel K (local nilpotence with a uniform exponent near each point suffices). Put A=E^G. Consider E-modules P with:

1. A genuine semilinear G-action, compatible with the specified strict action on E.
2. P locally finitely presented as a left E-module.
3. For every closed y, P_y is a finitely generated projective left E_y-module.
4. Trivial inertia: for every closed x over y, the stabilizer H_x acts trivially on the x-component of P_y/J(E_y)P_y.

Condition 4 uses the quotient E_y/J(E_y)=product_x C established below. Ranks may vary between different quotient neighborhoods; G-equivariance makes the dimensions on any one orbit equal.

These are substantive assumptions. In particular, local freeness on X is not silently substituted for projectivity of the orbit stalk P_y. Section 4 verifies that implication in a concrete sheaf setting.

## 2. Semilocal orbit-frame lemma

**Lemma.** Put S=E_y, Q=P_y for a closed y. Under the preceding hypotheses there is an S-basis v_1,…,v_r of Q fixed by all of G.

**Proof.** A nilpotent two-sided ideal is contained in the Jacobson radical: if k lies in such an ideal, then 1-sk is invertible for every s, by a finite geometric series. For a nilpotent extension S→B_y, the inverse image of J(B_y) is J(S). To see the converse inclusion as well, invertibility lifts across a nilpotent ideal, and apply the characterization of the radical by invertibility of all 1-st. Consequently

    S/J(S) = product_{x over y} C.

The additive quotient W=Q/J(S)Q is a module over this product. Write W=⊕_x W_x. G permutes these summands transitively; its maps are C-linear. Choose a basis of W_{x0}. Transport it to every W_x using a g with gx0=x. The transported basis is independent of this choice precisely because H_{x0} acts trivially. Joining the i-th transported vectors across all summands gives w_i in W^G. These w_i form a basis of W over product_x C.

Lift each w_i to u_i in Q and put v_i=|G|^{-1}Σ_g g(u_i). The quotient map is equivariant, so v_i still maps to w_i. The map f:S^r→Q taking the standard basis to the v_i is surjective: its finitely generated cokernel has zero reduction modulo J(S), hence is zero by Nakayama. Since Q is projective, the surjection splits, S^r=Q⊕L. The split kernel L is finitely generated. Reduction preserves this direct sum, and the reduction of f is an isomorphism, so L/J(S)L=0; Nakayama gives L=0. Therefore f is an isomorphism. All v_i are invariant. ∎

This proof neither decomposes S into local factors nor assumes S flat over S^G. It works with left modules and does not change the order of noncentral coefficients. Semilocal projectivity, rather than a pre-existing free frame, is sufficient.

## 3. Global orbit-algebra descent theorem

**Theorem 1.** For the orbit-algebra hypotheses, N=P^G is locally free of finite rank over A, and the multiplication map

    E ⊗_A N → P

is an isomorphism of strict equivariant E-modules. The functors

    N ↦ E⊗_A N,       P ↦ P^G

give inverse equivalences between finite locally free left A-modules and the E-modules satisfying conditions 1–4 above. Here E is a right A-module for the tensor product, with G acting on the E factor.

**Spreading proof.** At a closed y use Lemma 2. Each invariant germ v_i is represented by a section on some neighborhood of y. Since G acts on sheaves over Y, all its translates have the same domain. Average that section to make it invariant without changing its germ. Intersect finitely many domains. The resulting map f:E^r→P is an isomorphism at y.

A stalkwise isomorphism of this form spreads near y when P is locally finitely presented. Explicitly, Hom_E(P,E^r) commutes with passage to stalks for locally finitely presented P: take a finite presentation locally, represent the finitely many image generators, and shrink to satisfy its finitely many relations. The inverse of f_y therefore extends to a morphism t near y. The equalities tf=id and ft=id hold after further shrinking, because equality of morphisms with finitely generated source can be checked on finitely many local generators. Thus f is an invariant frame over an open neighborhood U of y.

These neighborhoods cover Y: their union is open and contains every closed point; a nonempty closed complement in a finite-type C-scheme would have a closed point. On U, P=E^r with coefficientwise action, so N=A^r and the displayed multiplication map is an isomorphism. This proves both local freeness and the counit globally.

Conversely, if N is finite locally free over A, E⊗_A N is locally E^r with coefficientwise action. It satisfies 1–4, and the unit N→(E⊗_A N)^G is an isomorphism in such local frames. The two natural isomorphisms give the asserted equivalence. ∎

### Gluing and full faithfulness, explicitly

On an overlap of two invariant frames, each change-of-basis coefficient is G-fixed, because both bases are fixed and coordinates are unique. The change-of-basis map and its inverse are therefore defined over A. Their ordinary cocycle identity holds over A because it already holds over E and A is a subsheaf of E. These transition maps glue A^r to N. There is no additional choice of a coherence 2-cocycle.

Likewise any equivariant E-linear map between two such P has invariant coefficients in invariant frames, hence is uniquely the extension of an A-linear map. This proves the sheaf-of-morphisms comparison and therefore full faithfulness for global morphisms as well. It is not merely equality of endomorphism ranks.

No descent theorem for arbitrary equivariant E-modules is asserted. Nontrivial stabilizer representations lie outside the category, and ramified sign-character examples can fail both freeness and reduction compatibility.

## 4. Concrete theorem for sheaves on X

Here is a sufficient setting in which E=p_*D and P=p_*M satisfy every hypothesis and the result is genuine sheaf descent on X.

Assume D is a sheaf of associative unital **central O_X-algebras**, coherent as an O_X-module, with a G-equivariant O_X-algebra surjection D→O_X and nilpotent kernel K. Central means the specified structural copy of O_X is central in D; this is a real restriction, not a property of arbitrary quantization algebras. G acts strictly on D, semilinearly over its action on O_X.

Let M be finite locally free as a left D-module, with a strict compatible G-action. Assume H_x acts trivially on

    M_x / (K_x + m_x D_x) M_x

for every closed x. Define

    A=(p_*D)^G,       N=(p_*M)^G.

**Theorem 2.** N is finite locally free over A and the counit

    D ⊗_{p^{-1}A} p^{-1}N → M

is an isomorphism. This gives an equivalence between finite locally free A-modules and strict equivariant finite locally free D-modules with trivial closed-point stabilizer fibers. Morphisms descend uniquely.

**Verification of hypotheses.** Because D and M are coherent O_X-modules and p is finite, their pushforwards are coherent O_Y-modules; finite pushforward is exact on these quasi-coherent sheaves. Thus E→B has the asserted nilpotent kernel p_*K. The O_Y-structure is central.

To check the orbit stalk, take an affine neighborhood U=Spec R of y. Its inverse image is affine Spec B_U. Quasi-coherent central D-modules there are described by modules over S_U=Γ(p^{-1}U,D), with restriction given by central localization in B_U. A finite locally free D-module gives a finitely generated projective S_U-module: finite local free presentations make it finitely presented, and local splittings of a presentation can be combined after clearing denominators on a finite principal-open cover, using a partition of unity in the central ring B_U. Equivalently, local projectivity for a finite presentation descends under these central localizations. Localizing over R at y preserves projectivity, so P_y is finitely generated projective over E_y. Finiteness and finite presentation can also be seen from central noetherianity: E is finite over the noetherian O_Y and hence its finite O_Y-modules are finitely presented E-modules.

The maximal-ideal component of P_y/J(E_y)P_y indexed by x is exactly the displayed residue fiber of M_x. Thus the assumed inertia condition is the one in Theorem 1.

Apply Theorem 1. On a resulting quotient-open U, its invariant frame consists of sections of M over p^{-1}U. It induces D^r→M. Its pushforward is the frame E^r→P and is an isomorphism. Finite pushforward is exact and detects zero quasi-coherent sheaves: on affine inverse images this is the elementary fact that a module with zero module of sections is zero. Hence D^r→M is an isomorphism. This proves the counit and the equivalence on X. Conversely the indicated extension of any locally free N is locally D^r, has fixed basis, and has trivial inertia. ∎

**Noncentral use.** Theorem 1 remains valid without any central O_Y-structure. To apply it to a noncentral D on X, one must independently verify: exact nilpotent quotient E→B; local finite presentation of P; orbit-stalk projectivity; and that the invariant orbit frame E^r→p_*M yields an actual frame D^r→M. Exact/conservative pushforward on an appropriate module category is one sufficient condition for the last assertion. These properties are not inferred from the word “deformation.”

## 4B. A filtered noncentral realization without orbit-projectivity assumptions

There is a stronger concrete variant relevant to noncentral deformations. Suppose D is a sheaf of unital C-algebras on X with a strict G-action and a G-stable nilpotent two-sided ideal K, with D/K=O_X equivariantly. Require each left O_X-module

    K^i/K^{i+1}

to be quasi-coherent. This left action is induced from D/K and is well defined; a central structural embedding O_X→D is **not** assumed. We may take a globally finite nilpotence exponent, or work locally on Y with one uniform exponent on each finite inverse image. Let M be finite locally free over D, strictly equivariant, with trivial stabilizer actions on the closed fibers of M/KM.

**Theorem 2B.** With A=(p_*D)^G and N=(p_*M)^G, N is finite locally free and

    D ⊗_{p^{-1}A} p^{-1}N → M

is an isomorphism. Extension and invariants are inverse equivalences for these module categories, with full faithfulness and gluing exactly as in Theorems 1–2.

**Proof.** The sheaf M_0=M/KM is an equivariant vector bundle on X with trivial inertia. Apply the already proved classical case of Theorem 2 (D=O_X). Around each y choose an affine quotient-open U on which its descended vector bundle is free. Thus M_0 on p^{-1}U has a G-invariant O_X-basis.

The associated layers K^iM/K^{i+1}M are quasi-coherent left O_X-modules: locally a D-frame identifies them with a finite direct sum of K^i/K^{i+1}; their transition maps are O_X-linear because they descend from D-linear maps. Quasi-coherence is local on X, so these local descriptions suffice. The finite filtration therefore makes KM acyclic in positive degrees on the affine scheme p^{-1}U, by induction through the short exact sequences of layers. In particular, H^1(p^{-1}U,KM)=0. Consequently every global section of M_0 on this affine inverse image lifts to a global section of M. Lift the whole invariant basis and average over G. This yields invariant sections v_i of M reducing to that basis, all on the same p^{-1}U.

The map D^r→M they define is an isomorphism: near every point take an existing D-frame for M, and its finite coefficient matrix is invertible modulo K; an inverse lifts across the nilpotent matrix ideal. This matrix assertion is valid also in the opposite ring required by left-module conventions. Thus M has invariant D-frames over quotient-open neighborhoods. In these frames N=A^r, the counit is an isomorphism, transition functions lie in A, and equivariant morphisms have coefficients in A. Conversely extension of a locally free A-module has these frames, so it lies in the claimed category. ∎

This is a genuine noncentral sheaf theorem. Unlike the abstract orbit-algebra proof, it does not require proving beforehand that p_*M has projective orbit stalks or is locally finitely presented over p_*D. The finite quasi-coherent-layer assumption supplies a different, explicit route to quotient-open frames. It remains an extra geometric hypothesis to verify for an actual ambient, not a consequence of a bare filtered-ring presentation.

For completeness, the same acyclicity argument for K gives surjectivity Γ(p^{-1}U,D)→Γ(p^{-1}U,O_X) on affine U. It thus also verifies the pushforward nilpotent reduction in this setting. No disjoint Zariski neighborhoods of orbit points, étale/Galois property, or flatness over fixed rings is used.

## 5. Stable ideals and natural reduction compatibility

Let I⊂E be any G-stable two-sided sheaf ideal, and put J=I∩A. There is a canonical sheaf-algebra isomorphism

    A/J ≅ (E/I)^G.

Indeed finite averaging is a projection onto invariants. A fixed quotient germ has an arbitrary lift, whose average is a fixed lift; the kernel is exactly I∩A. This is a sheaf assertion and does not presuppose surjectivity on sections over every open.

For P in Theorem 1, the invariant frames give canonical isomorphisms

    (IP)^G = JN,
    (P/IP)^G ≅ N/JN,
    (E/I) ⊗_{A/J} (N/JN) ≅ P/IP.

The first equality uses the natural inclusions in P: in a frame IP=I^r and N=A^r. Consequently these identifications are independent of frames and commute with morphisms and with successive stable-ideal reductions. There is no claim I=EJ, which may be false, and no use of exactness of tensoring arbitrary modules.

For Theorem 2, any G-stable quasi-coherent two-sided ideal I_X⊂D gives I=p_*I_X, and finite exact pushforward identifies E/I=p_*(D/I_X), and likewise for the module quotient. The displays therefore become the desired reduction comparison on X. The ideal need not be central or contain K. The original strict action must preserve it.

In Theorem 2B, the same stable-ideal statements hold whenever p_*D→p_*(D/I_X) is surjective. A checkable sufficient condition is that I_X have a finite filtration by abelian subsheaves with quasi-coherent O_X-module successive quotients, for example its intersection filtration with K^i when those layers are quasi-coherent. Then I_X is acyclic on affine inverse images, giving that surjectivity. In the existing invariant frame I_X M=I_X^r, so the analogous module surjectivity follows on the same neighborhoods. This explicitly records the extra condition for arbitrary noncentral coefficient ideals; it is automatic for I_X=K^j in Theorem 2B. It must not be assumed for an arbitrary ideal without verification.

## 6. Compatible nilpotent orders and a formal sheaf

An equivalence at each finite order alone does not justify a finite invariant frame on a single neighborhood for an inverse limit: infinitely many arbitrary shrinkings are invalid. The following supplies the missing uniformity.

Let (D_n)_{n≥0} be an inverse system of central coherent O_X-algebras as in Theorem 2, with D_0=O_X, strict compatible G-actions, surjective transition maps, and nilpotent kernels of D_n→D_0. Let M_n be finite locally free D_n-modules with strict compatible actions and equivariant identifications

    D_{n-1} ⊗_{D_n} M_n ≅ M_{n-1}.

Assume the inertia action of M_0 is trivial. All residue actions at higher orders are then trivial too. Define E_n=p_*D_n, A_n=E_n^G, N_n=(p_*M_n)^G.

Theorems 1–2 and Section 5 give, canonically,

    A_{n-1} = A_n / ker(A_n→A_{n-1}),
    N_{n-1} ≅ A_{n-1} ⊗_{A_n} N_n.

All finite-order counits and morphism comparisons commute with these transition maps.

**Uniform-frame argument.** First take a quotient-open affine U on which N_0 is free, as supplied by Theorem 2 at n=0. Since p^{-1}U is affine and the kernels of M_n→M_{n-1} are quasi-coherent O_X-modules, the maps

    Γ(p^{-1}U,M_n) → Γ(p^{-1}U,M_{n-1})

are surjective. Lift each vector of an invariant frame at order n−1 to order n, then average. The lifts remain compatible and invariant. They are a D_n-frame: locally this map between free modules of the same rank reduces to a basis modulo the nilpotent ideal ker(D_n→D_0), and invertibility of a finite matrix lifts across a nilpotent ideal. Thus the induction never changes U.

Set D=lim_n D_n, M=lim_n M_n, A=lim_n A_n and N=lim_n N_n, with limits taken as sheaves. Finite invariants and pushforward commute with these limits, so

    A=(p_*D)^G,       N=(p_*M)^G.

The compatible frames on U identify the systems with D_n^r and A_n^r respectively. Passing to the limit gives actual local sheaf isomorphisms M|_{p^{-1}U}=D^r and N|_U=A^r, as well as

    D ⊗_{p^{-1}A} p^{-1}N ≅ M.

Here ordinary tensor agrees with completed tensor because N is finite locally free and the statement is locally D⊗_A A^r=D^r. This does not rely on inverse-image functors commuting with arbitrary inverse limits. It is proved by the common local frames.

A compatible family of finite-order equivariant morphisms likewise gives a unique limit morphism, by taking the inverse limit of its finitely many coefficients in these common frames. Conversely a morphism of such locally free limit modules reduces to the finite orders. The projections A→A_n and N→N_n are locally surjective: on affine U the algebra transition maps are surjective on sections by the same quasi-coherent-kernel argument and averaging, so compatible lifts can be chosen recursively. Their kernels give the expected finite-order reductions. Thus this is an effective formal descent statement, not just a collection of unrelated orderwise equivalences.

The whole formal-tower assertion also holds with the noncentral hypotheses of Theorem 2B at every order. Require the transition maps D_n→D_{n-1} to be surjective and compatible with D_0=O_X, and each K_n^i/K_n^{i+1}, where K_n=ker(D_n→O_X), to be quasi-coherent. The transition maps send K_n^i onto K_{n-1}^i, since they send K_n onto K_{n-1}. They likewise send K_n^i M_n onto K_{n-1}^i M_{n-1}. Thus the transition kernels, with their induced finite filtrations, have graded pieces equal to kernels of surjective morphisms between quasi-coherent O_X-modules. Those pieces are quasi-coherent. The finite acyclicity argument gives the needed section-surjectivity on every affine inverse image. Apply Theorem 2B at order zero and lift its invariant frame successively on one fixed affine U. All subsequent limit and morphism arguments are unchanged. This gives a noncentral formal realization under explicit finite-layer hypotheses. Completeness of stalk rings alone does not supply these hypotheses.

## 7. What remains for an actual weak-action ambient

This theorem closes a global **strict-action, trivial-inertia module-descent implication** under the stated hypotheses. In particular, no separate Čech construction of a descended module is required once invariant orbit frames have been obtained: fixed transition maps glue it canonically.

It does not close any of the following distinct prerequisites:

- A normalized weak ambient with coherence units in 1+F^1 can be strictified locally by the earlier result, but that does not produce a single globally strict sheaf algebra with compatible overlap comparisons. Local inner comparison units need not satisfy a chosen global cocycle merely because each pair is comparable.
- A scalar character can be removed locally when a genuine classical linearized line and the relevant scalar residual representation are supplied. This does not make its spatial transition functions disappear or prove global compatibility across varying stabilizers.
- The actual ambient must be identified with the E or D used here, including its group and overlap actions, reduction, coefficient ideals, and the comparison maps. A central O_X-algebra model cannot be substituted for a noncentral physical deformation without such an identification.
- For a noncentral actual deformation one must verify either the explicit orbit-stalk projectivity, finite-presentation/spreading, and sheaf frame-detection conditions, or the quasi-coherent nilpotent-layer and lifting hypotheses of Theorem 2B (including the coefficient-ideal conditions when needed).
- A module with an already strict compatible action, appropriate local freeness, and trivial residual inertia must first exist. The descent theorem does not construct such a module from tentative operators, an obstruction class, or an endomorphism bundle.
- A formal actual object needs compatible finite orders and uniform lifting/effectivity, not only isolated finite-order existence or formal local strictifications.

Accordingly, the remaining comparison gap is a presentation-level, reduction-and-ideal-compatible identification of the actual weak/Morita ambient and its module problem with this strict global descent setting. No existence or nonexistence statement about an actual physical mixed module follows here. No operation, matrix, input, detector, or retained physical value has been evaluated or changed.
