# Invariant Morita bimodules give a conditional global algebroid

## Result and scope

**Yes, with precise local and sheaf hypotheses.** Let the local rings carry genuine finite-group actions fixing their residue fields pointwise, let the group order be invertible, and let the overlap bimodules be genuinely equivariant, Morita-invertible, and locally free of rank one on the left. If their residue inertia acts trivially, then each overlap has an invariant local generator. Consequently:

1. Its invariants form an invertible bimodule between the invariant rings.
2. The canonical comparison from the tensor product of the invariant overlap bimodules to the invariants of their tensor product is an isomorphism.
3. Given equivariant composition isomorphisms and their actual associativity, these descend to coherent composition isomorphisms. The invariant rings and bimodules therefore define an algebroid on the specified downstairs site.
4. Independent strictifications of the local weak actions are compatible with this construction: transport the overlap action by the left gauge and the inverse right gauge. The local gauges need not be equal on overlaps.

These conclusions do **not** follow merely from a root line, a cohomological half-class, or an endomorphism-algebra calculation. They require the actual coherent equivariant Morita data. They identify the resulting algebroid with its own invariant presentation, not with an independently prescribed physical or corrected ambient algebra. No mixed obstruction is evaluated, and no global module is manufactured.

The theorem is stated for genuine geometric local charts, with the acting group fixing the residue field. A full decomposition group with nontrivial residue-field action needs a separate semilinear residue-descent argument; elements moving a point cannot act on that point's single local ring.

All arguments are universal algebra and static reading. No physical source or jet values are evaluated in this argument.

## 1. Precise local hypotheses

Let D_i be associative unital local rings, with two-sided Jacobson radicals m_i and residue **fields** k_i. Let a finite group G act genuinely on every D_i by automorphisms α_i(g). Require n = |G| to be invertible in D_i; equivalently here it is invertible in k_i. Its inverse is central and G-fixed. Require G to fix every k_i pointwise.

Let P_ij be a Morita-invertible (D_i,D_j)-bimodule, free of rank one as a left D_i-module. Here Morita-invertible means that tensoring with P_ij is an equivalence with an inverse bimodule and compatible evaluation isomorphisms. In particular the canonical right-action map

    D_j^op → End_{D_i}(P_ij)

is an isomorphism. Assuming rank one on both sides is harmless but redundant in this formulation.

Suppose additive bijections σ_ij(g) satisfy the **exact** identities

    σ_ij(g)(a p b) = α_i(g)(a) σ_ij(g)(p) α_j(g)(b),
    σ_ij(g) σ_ij(h) = σ_ij(gh).

Require G to act trivially on P_ij / m_i P_ij. In this geometric local setting G is the residue inertia group, so this is the stated trivial-residue-inertia condition. A general projective action on that fiber is not enough.

The two sides are compatible: every left basis identifies the right action with a ring isomorphism D_j → D_i, so m_i P_ij = P_ij m_j. Consequently the one-sided residue condition is the same condition on the common residue bimodule.

For a family of overlaps, additionally supply genuine equivariant bimodule isomorphisms

    μ_ijk : P_ij ⊗_{D_j} P_jk → P_ik,

normalized unit data P_ii = D_i, and the actual associativity equation

    μ_ikl (μ_ijk ⊗ 1) = μ_ijl (1 ⊗ μ_jkl).                 (1)

The standard associator of tensor products is understood in (1). All data are restricted to the common overlap when necessary. Merely knowing equality of the induced inner automorphisms does not supply (1).

## 2. Trivial residue inertia gives invariant bases and full faithfulness

**Lemma.** Let D be local with residue field k, G finite acting trivially on k, and |G| invertible. Let M be a finite free left D-module with a genuine semilinear G-action. Then M has a G-invariant D-basis if and only if G acts trivially on M/mM.

### Lifting the basis

Choose a basis of M/mM, all of whose vectors are invariant by hypothesis. Lift it arbitrarily to M and average its lifts using

    R(m) = |G|^{-1} Σ_{g∈G} g(m).

The resulting invariant vectors still reduce to the chosen basis. They form a D-basis by the noncommutative Nakayama argument from the earlier report: the corresponding map D^r → M is surjective; it splits because M is free; its finitely generated direct-summand kernel has zero reduction and hence is zero. Conversely, an invariant D-basis makes the residue action coefficientwise; since G fixes k, its action on the entire fiber is trivial. This proves the lemma.

Write A = D^G. The ring A is local with radical A ∩ m and residue field k. Indeed an invariant element outside m has invariant inverse, and averaging lifts proves A → k is surjective. An invariant basis immediately gives the canonical isomorphism

    D ⊗_A M^G → M,       d ⊗ v ↦ dv.                     (2)

It also proves the equivalence

    finite free A-modules
       ≃ finite free equivariant D-modules with trivial residue inertia.

The inverse functors are extension of scalars with the canonical action and invariants. Their unit and counit are isomorphisms on actual invariant bases. In particular equivariant D-linear maps between these objects are fully and faithfully recovered from their A-linear restrictions. No flatness of D over A is needed.

## 3. Invariants of a rank-one Morita bimodule are invertible

For one overlap write D = D_i, E = D_j, P = P_ij, A = D^G, and B = E^G. By Section 2 choose an invariant left generator e of P.

There is a unique ring homomorphism φ : E → D such that

    e b = φ(b) e.                                         (3)

It is an isomorphism: the canonical map E^op → End_D(P) is an isomorphism by Morita invertibility, and the left basis identifies End_D(P) with D^op. In particular e is also a right generator, and φ carries the radical of E onto the radical of D.

Because e is invariant, applying g to (3) gives

    α_i(g)(φ(b)) = φ(α_j(g)(b)).                           (4)

Thus φ is G-equivariant and restricts to an isomorphism φ^G : B → A. Uniqueness of left coefficients gives

    Q := P^G = A e,
    e b = φ^G(b)e       for b ∈ B.

Therefore Q is the rank-one invertible (A,B)-bimodule defined by φ^G. Its inverse is the rank-one (B,A)-bimodule defined by (φ^G)^{-1}. Equivalently one may take the equivariant inverse of P: its dual basis is invariant, and its invariant evaluation maps give these inverse identifications.

The canonical map in (2) is also right B-linear in this situation:

    D ⊗_A Q ≅ P          as (D,B)-bimodules.               (5)

It is not being asserted that two-sided extension by both D and E is an isomorphism; see Section 9.

## 4. Tensor comparison is proved on invariant bases

Let P be as above and let R be an equivariant rank-one invertible (E,F)-bimodule satisfying the same hypotheses. Let f be an invariant left E-generator of R, and let ψ : F → E be its right-action isomorphism. Put C = F^G and S = R^G.

The tensor P ⊗_E R is free of rank one on the left with generator e ⊗ f: explicitly

    (a e) ⊗ (b f) = a φ(b) (e ⊗ f).                     (6)

The coefficient map in (6), and a ↦ a(e ⊗ f), are mutually inverse. Its right action is given by φψ. Its diagonal group action is genuine, e ⊗ f is invariant, and its residue inertia is trivial.

Likewise Q ⊗_B S is free of rank one over A with generator e ⊗ f, using φ^G. Consequently the canonical map

    t_{P,R} : P^G ⊗_{E^G} R^G → (P ⊗_E R)^G,
              p ⊗ r ↦ p ⊗ r                            (7)

is an isomorphism: both sides are precisely A(e ⊗ f). This is an actual proof of (7), not an assertion that arbitrary invariants commute with tensor products.

The comparison is natural in equivariant bimodule maps, compatible with units, and associative. All iterated comparisons send an elementary invariant tensor to that same tensor in the full iterated tensor product; hence their associativity diagrams agree. Alternatively, on invariant generators both parenthesizations are the same coefficient identification.

The same argument works when R is a finite free equivariant **left E-module** with trivial residue inertia: an invariant basis f_1,...,f_r gives invariant basis e ⊗ f_1,...,e ⊗ f_r. Thus

    P^G ⊗_{E^G} M^G ≅ (P ⊗_E M)^G                    (8)

for exactly that class of modules. No analogous assertion is made for unrestricted equivariant modules.

## 5. Composition and all triple coherence descend

Put A_i = D_i^G and Q_ij = P_ij^G. Define

    μ̄_ijk = μ_ijk^G ∘ t_{P_ij,P_jk} :
               Q_ij ⊗_{A_j} Q_jk → Q_ik.                (9)

Both factors are isomorphisms. The restrictions of the unit maps give the unit maps downstairs. Naturality and associativity of (7), followed by the original equality (1), show that the μ̄ satisfy (1) literally over the A_i.

Here one can use the full faithfulness from Section 2 at each fixed left ring D_i: the tensor products in question have invariant bases and trivial inertia, so their equivariant D_i-linear maps and equalities are faithfully detected by restriction to invariants. There is no averaging of associators and no hidden central defect being discarded. More simply, the given two equal upstairs composites restrict to the same map on elementary invariant tensors, which generate the downstairs source.

There is an explicit algebroid presentation. Choose invariant local generators e_ij, and write

    e_ij b = φ_ij(b)e_ij,
    μ_ijk(e_ij ⊗ e_jk) = u_ijk e_ik.

Each u_ijk is a **G-invariant unit**, since μ is an equivariant isomorphism. Bimodule linearity and associativity give, in the written order,

    φ_ij φ_jk = Ad(u_ijk) φ_ik,
    u_ijk u_ikl = φ_ij(u_jkl) u_ijl.                     (10)

Restrict φ_ij to A_j → A_i. Equation (10) is then the required algebra-map and triple-unit presentation of the invariant algebroid.

Replacing e_ij by v_ij e_ij, with v_ij ∈ A_i^×, changes the presentation by the ordinary exact gauge

    φ'_ij = Ad(v_ij) φ_ij,
    u'_ijk = v_ij φ_ij(v_jk) u_ijk v_ik^{-1}.

The invariant algebroid therefore does not depend on a choice of invariant generators, up to the specified presentation equivalence.

## 6. Exact global sheaf criterion

The local statement alone is not a theorem that arbitrary completed local data algebraize or glue. A precise sufficient global framework is the following.

Work on a specified site with an open cover {V_i}, and assume there are enough points for the stated local checks. Suppose:

- D_i are sheaves of algebras on V_i, with genuine G-actions over the identity of the site, so the action commutes with restrictions.
- P_ij are actual locally left-free rank-one invertible sheaf bimodules on V_i ∩ V_j, with actual semilinear G-actions and μ_ijk as in Section 1.
- Locally on overlaps, the P_ij admit invariant left generators.

The last condition is the exact condition used in Sections 3–5. A sufficient way to establish it is that the stalk rings D_i,x are local with residue fields fixed pointwise by G, the group order is invertible, and G acts trivially on every P_ij,x / m_i,x P_ij,x. Section 2 supplies an invariant generator at the stalk. It extends to a local section; averaging a representative makes it invariant while retaining that germ, and after shrinking it is a generator. Finite G-invariants commute with the relevant stalks, and the action being over the identity means this shrinking and averaging take place on the same open set.

Define sheaves A_i = D_i^G and Q_ij = P_ij^G. Sections 3–5 apply locally and produce invertible Q_ij with coherent μ̄. They give a global algebroid by descent, or equivalently by stackifying the local algebra presentations (10). One may glue the stacks of left A_i-modules using the equivalences Q_ij ⊗_{A_j} − and the natural composition isomorphisms μ̄. This does not assert that the algebroid is represented by one global sheaf of algebras.

On the subcategories of locally finite free modules, this also yields an equivalence between:

1. downstairs descent data for the A_i and Q_ij; and
2. upstairs descent data for the D_i and P_ij whose local module actions are genuine and have trivial residue inertia.

Indeed local extension/invariants are mutually inverse by Section 2, and (8) intertwines every gluing functor. Unit, counit, gluing morphisms, and their cocycle equalities match by full faithfulness of the **left-module** equivalences. This is a conditional equivalence of existing module problems, not an existence theorem for an object in either descent category.

If charts have different groups or the global finite group permutes them, one must instead supply an appropriate equivariant groupoid/atlas and its restriction and transport maps. The preceding theorem applies on compatible fixed-group pieces, but it does not construct that atlas. Similarly, the pushforward of a sheaf from a finite cover can have semilocal orbit stalks; calling those stalks local would be incorrect. One must provide the orbit/stabilizer reduction or establish invariant local generators directly. Individual formal completions do not by themselves supply sheaves on the chosen downstairs site.

## 7. Local strictification transports the overlap group coherence exactly

Now begin with coherent weak algebra actions on D_i:

    F_i(g) F_i(h) = Ad(A_i(g,h)) F_i(gh),
    A_i(g,h) A_i(gh,t) = F_i(g)(A_i(h,t)) A_i(g,ht).

Here A_i(g,h) denotes a weak-action unit, not the invariant ring of earlier sections. Assume normalized units and operators for simplicity. A weak equivariant overlap bimodule must be supplied with the **exact** compatibility

    σ_ij(g)(a p b) = F_i(g)(a) σ_ij(g)(p) F_j(g)(b),
    σ_ij(g)σ_ij(h)(p)
       = A_i(g,h) σ_ij(gh)(p) A_j(g,h)^{-1}.             (11)

Assume also that μ_ijk is equivariant for these σ and that its associativity is exact. The equation for automorphisms alone cannot replace (11).

Choose any local gauges c_i(g), and define

    F'_i(g) = Ad(c_i(g)) F_i(g),
    A'_i(g,h) = c_i(g) F_i(g)(c_i(h))
                   A_i(g,h) c_i(gh)^{-1},
    σ'_ij(g)(p) = c_i(g) σ_ij(g)(p) c_j(g)^{-1}.         (12)

The new operator is (F'_i(g),F'_j(g))-semilinear. A direct substitution, with no rearranging noncommuting factors, gives

    σ'_ij(g)σ'_ij(h)(p)
      = c_i(g) F_i(g)(c_i(h)) A_i(g,h) σ_ij(gh)(p)
          A_j(g,h)^{-1} F_j(g)(c_j(h))^{-1} c_j(g)^{-1}
      = A'_i(g,h) σ'_ij(gh)(p) A'_j(g,h)^{-1}.           (13)

Thus if each A'_i = 1, every σ'_ij is a genuine group action. No equality c_i = c_j is required.

Moreover the same original composition maps μ remain equivariant, because balanced tensoring cancels the adjacent middle gauge:

    μ_ijk(σ'_ij(g)(p) ⊗ σ'_jk(g)(q))
      = μ_ijk(c_i(g)σ_ij(g)(p)c_j(g)^{-1}
                    ⊗ c_j(g)σ_jk(g)(q)c_k(g)^{-1})
      = c_i(g) μ_ijk(σ_ij(g)(p) ⊗ σ_jk(g)(q)) c_k(g)^{-1}
      = σ'_ik(g)(μ_ijk(p ⊗ q)).                         (14)

The maps μ and their associativity equality have not changed. Unit bimodules transport to the new algebra actions as well. Consequently **independent chart strictifications are sufficient once the actual weak bimodule coherence (11) and composition coherence are supplied**. Requiring equal chart gauges would be unnecessarily strong.

The preceding strictification report supplies c_i(g) ∈ 1 + J_i when the weak coherence units lie in 1 + J_i and the relevant filtered algebra is nilpotent or complete and separated, with |G| invertible. If J_i ⊆ m_i, the new overlap action has the same residue action as the old one: both left and right gauge factors are 1 on the residue bimodule, using m_iP_ij = P_ijm_j. Thus trivial residue inertia is preserved.

For a global construction the gauges must be actual chart sections, or otherwise compatible sheaf automorphisms, not merely unrelated choices on all completed stalks. When the weak-action units and ideals are actual sheaf data and the sheaf algebras are complete as needed, the explicit finite-average recursion in the earlier report is restriction-compatible and constructs such chart gauges. Across different charts, equations (12)–(14) handle their mismatch. There is no averaging over Čech directions, and nontrivial algebroid gluing may remain.

A nontrivial classical projective cocycle is not removed by a gauge congruent to 1. The weak-action units must genuinely satisfy the hypotheses of strictification, including their central coherence, and the original overlap actions must satisfy (11). These conditions cannot be inferred from an action on endomorphisms.

## 8. Coefficient ideals, reductions, and complete tensors

Suppose I_i are stable two-sided ideals and are genuinely compatible with the bimodules:

    I_i P_ij = P_ij I_j.

In an invariant basis this says φ_ij(I_j) = I_i. Set B_i = I_i ∩ D_i^G. Then

    B_i Q_ij = Q_ij B_j,
    D_i^G / B_i ≅ (D_i/I_i)^G,
    Q_ij / B_i Q_ij ≅ (P_ij/I_iP_ij)^G.                (15)

The ring equality in (15) follows by averaging lifts. The module equality follows coefficientwise in the invariant generator. The maps μ, their tensor comparisons, and their coherence commute with these actual quotient maps. Gauges preserve stable two-sided ideals, and (12) preserves the indicated bimodule ideal submodules.

No identity between invariants of products of ideals and products of invariant ideals is asserted. In particular B_i is the actual intersection, not an ideal guessed from a trace map or a characteristic class. Any desired identification of mixed coefficient multiplication with another model must still be proved.

For separated complete filtered sheaves, require continuous actions, maps, and compatible induced finite-free module topologies. Then the same proofs hold for completed tensor products: the displayed finite-free invariant bases turn the tensors into finite direct sums with the induced filtration. This does not prove an unspecified formal object effective or identify induced and intrinsic adic topologies.

## 9. What full faithfulness does and does not say

The full faithfulness used here concerns equivariant **left D_i-linear maps** for a fixed left algebra and its inertia-trivial free modules. It does not assert full faithfulness of invariants on arbitrary bimodule maps with different right actions.

For example, let D = k[[u]], G of order two act by u ↦ −u, and char(k) ≠ 2. Two (D,D)-bimodules can have the same regular left module and coefficientwise G-action but right actions given respectively by id_D and by the sign automorphism. Both have invariant left generator 1 and trivial residue inertia. Their invariant bimodules are the same regular bimodule over k[[u²]], because the two right automorphisms restrict identically there. The identity map between these invariant bimodules does not lift to a D-bimodule map between the two different right actions. It does lift uniquely as a left-module map, exactly as the stated full faithfulness promises.

Likewise even for the regular bimodule, multiplication

    D ⊗_{D^G} D → D

need not be an isomorphism. The proof never uses such a two-sided base-change claim. It uses (5), the already supplied right action, and the special tensor comparison (7).

These distinctions do not weaken the invariant-algebroid construction: the given equivariant bimodule maps descend, their isomorphisms remain isomorphisms, and their actual coherence descends. They limit what one could reconstruct from the downstairs bimodules alone without retaining the original upstairs data.

## 10. Conclusion for the open comparison problem

The following implication is now proved:

    actual coherent weak equivariant rank-one Morita atlas
    + local nilpotent/pronilpotent strictification hypotheses
    + trivial residual inertia
    + an effective compatible sheaf/atlas setting
        ⇒ a coherent invariant Morita atlas and global algebroid,
           with the stated equivalence of locally free module problems.

There is no extra requirement that the independently chosen local strictifying gauges agree: transport of overlap operators by (12) supplies the correct compatibility.

What still must be supplied in any application is the actual ambient algebras, actual overlap bimodules and all of their group/Čech coherence, the specified group or stabilizer atlas, the local/inertia and effectivity hypotheses, and any desired identification with a prescribed downstairs physical or corrected algebroid. Such an identification must include coefficient products and mixed terms. The construction does not create a module or decide its remaining mixed obstruction.

## Static inputs

Read:

- ../../null-root-morita-inertia/root-morita-0719/RESULT.md
- ../../null-root-morita-inertia/trivial-inertia-0719/RESULT.md
- ../strictification-0736/RESULT.md

The invariant bimodule/tensor proof, explicit algebroid identities, and weak-bimodule transport formulas above are derived directly from the stipulated universal algebraic data.
