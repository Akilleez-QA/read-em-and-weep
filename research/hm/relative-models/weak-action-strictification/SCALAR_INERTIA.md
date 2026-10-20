# Scalar inertia can be untwisted without weakening a strict local action

## Scope and conclusion

This is a complementary **synthetic local criterion**, following the bounded question recorded in `premise:ramified-module-comparison/MORITA_SOURCE_AUDIT.md` for PR1 comment 6261960300. It is proved from the stated algebraic hypotheses below. It does not identify the actual physical mixed ambient, construct a physical mixed module, or establish global strictification.

**Conclusion.** A genuinely linearized classical line over a commutative local quotient can be framed by its scalar residue character. Those group transitions lift to central constants in the deformation algebra. The corresponding Morita untwist preserves the original strict algebra action and identity coherence. If a suitable strict finite free mixed module already exists, scalar inertia is thereby removed, and the invariant-frame descent lemma applies.

## 1. Precise hypotheses

Let D be a unital, possibly noncommutative, local C-algebra with Jacobson radical m and D/m=C, compatibly with its central structure map C→D. Local means that D/m is a division ring and elements outside m are units. Let G be finite and let α:G→Aut_C(D) be a genuine action: α_gα_h=α_gh, with identity coherence units. In particular, G fixes the specified residue C pointwise.

Let I⊆m be a G-stable two-sided ideal, and assume B=D/I is commutative. Then B is a local C-algebra with maximal ideal n=m/I and residue C; it has the induced genuine action. Neither nilpotence of I nor completeness or Noetherianity of D is needed for the scalar-frame argument.

Let L be an invertible B-module with a **genuine semilinear G-linearization** λ_g: L→L:

- λ_g(bv)=α_g(b)λ_g(v);
- λ_gλ_h=λ_gh and λ_1=id.

Invertible means finite projective of rank one. Since B is local, L is free of rank one. The induced representation on L/nL is a one-dimensional complex character χ:G→C×. A weak/projective linearization is insufficient: it need not produce a character and is not covered by this criterion.

## 2. Equivariant scalar frame

Choose a nonzero vector ē in L/nL and any lift u∈L. Define

    e = (1/|G|) Σ_{g∈G} χ(g)^{-1} λ_g(u).

Because G fixes constants and χ is a character, reindexing the sum shows

    λ_h(e)=χ(h)e.

Every summand χ(g)^{-1}λ_g(u) reduces to ē, so e reduces to ē. Hence e is a basis of L: writing e=be₀ in any B-basis e₀, its nonzero residue implies b∈B×. Thus

    L ≅ B⊗_C C_χ

as semilinear G-modules, where g acts on B by α_g and on C_χ by χ(g). The assertion is existence of an equivariant local frame, not a canonical frame. Any two such frames differ by an invariant unit of B.

The same argument is a character-weighted Reynolds projection. The hypotheses doing the work are invertibility of |G|, a fixed scalar field, and an honest character on the residue line.

## 3. Central lifts preserve strictness exactly

Use the group-arrow convention α_gα_h=Ad(A_{g,h})α_gh, initially A_{g,h}=1. For units q_g, the standard local Morita change is

    α'_g = Ad(q_g^{-1}) α_g,
    A'_{g,h} = q_g^{-1} α_g(q_h)^{-1} A_{g,h} q_{gh}.

In the frame from §2, the classical group transition is χ(g). Choose the lift

    q_g = χ(g)·1_D.

These are central units fixed by every α_h. Consequently

    α'_g=α_g,
    A'_{g,h}=χ(g)^{-1}χ(h)^{-1}χ(gh)=1.

Identity normalization and all group coherence equations therefore remain strict, without a limiting argument or an obstruction calculation. There is also a concrete equivariant lift of the line: the underlying identity D–D bimodule D equipped with g(d)=χ(g)α_g(d). Its equivariant inverse uses χ(g)^{-1}; their tensor products are the equivariant identity bimodule. Reduction gives the framed classical line. This constructs the relevant synthetic local equivariant Morita autoequivalence independently of any mixed module.

Centrality alone would only imply α'=α; the equation A'=1 additionally uses the character identity. A general system of central units can introduce a nontrivial central 2-coboundary. If the original ambient has weak coherence A rather than A=1, these scalar character lifts leave A unchanged; they do **not** strictify it.

## 4. Conditional module descent

Assume now that M is an already existing finite free left D-module of rank r with genuine α-semilinear operators T_g, and its residue representation is scalar:

    M/mM ≅ C_χ ⊗_C C^r,

where C^r has trivial G-action. Set S_g=χ(g)^{-1}T_g. Then S_g is α-semilinear, S_gS_h=S_gh, and the residue action of S is trivial. Denote the resulting module by M'.

Lift a residue basis to vectors u_i∈M' and average:

    v_i = (1/|G|) Σ_g S_g(u_i).

The vectors v_i are invariant and reduce to that residue basis. Their coefficient matrix in a free D-basis is invertible modulo m, hence invertible over D, since the radical of a finite matrix ring is the matrix ring of the radical. Thus they form a D-basis. This argument works with left-module coefficient conventions and does not commute noncentral entries.

Put A=D^G. In the invariant frame,

    M' ≅ D^r,
    (M')^G ≅ A^r,
    D ⊗_A (M')^G → M'

is an isomorphism, where the last map is multiplication. No flatness of D over A is needed. A finite projective M may also be used, by the standard freeness theorem for finitely generated projectives over a local ring.

Because I is stable and |G| is invertible, averaging also proves

    (D/I)^G ≅ A/(I∩A).

The invariant frame gives the compatible module comparison

    (M'/IM')^G ≅ (M')^G/(I∩A)(M')^G
                 ≅ (A/(I∩A))^r.

In particular, the quotient and invariant-frame constructions commute in the asserted sense. This is descent for this specified class of modules. It does not assert an equivalence for all equivariant modules or a general unramified/Galois property of D over A.

A common sufficient input is an equivariant reduction identification

    M/IM ≅ L ⊗_B N₀,

where N₀ is finite free over B and its residue representation is trivial. The scalar frame identifies the reduction of M' with N₀ and establishes the displayed residue condition. If N₀ has nontrivial residue action, scalar untwisting leaves precisely that action; the invariant-frame conclusion need not follow.

## 5. Obstruction transport is different from existence

The equivariant bimodule construction in §3 exists without M. It therefore supplies an equivalence between the corresponding synthetic module-lifting problems, wherever those problems and their reductions have been specified. It does not prove either lifting problem has a solution.

For example, for tentative α-semilinear module operators T_g, define the group-law defect

    Δ_{g,h}=T_gT_h−T_{gh}.

Untwisting gives

    Δ'_{g,h}=χ(gh)^{-1}Δ_{g,h}.

Thus vanishing of the defect is equivalent on the two sides. If T_{gh} is invertible, normalization satisfies

    Δ'_{g,h}(S_{gh})^{-1}=Δ_{g,h}(T_{gh})^{-1}.

This expresses equality of normalized defects under the canonical endomorphism identification. Across a square-zero extension it yields equality of the corresponding normalized obstruction representatives, provided the deformation problem, coefficient modules, and fixed reduction identifications are the same ones being compared. More general overlap and higher obstruction claims require their own specified deformation complexes; no universal unobstructedness follows from this calculation.

The invariant-frame argument in §4 can be invoked only after obtaining a genuine action on an actual finite free module. Averaging tentative operators with nonzero group-law defects does not supply that action.

## 6. Local stabilizers, neighborhoods, and global limits

The theorem assumes that the group acts on this one local algebra. Geometrically, at a point x of a G-space this is naturally an action of the stabilizer H=G_x on the stalk or completed local algebra at x. Replace G by H and χ by its character throughout. If G moves x, the full group generally does not act on O_{X,x}; it relates distinct stalks. A local assertion for H must not be silently presented as a single full-G fixed-point chart. One can instead formulate the orbit action groupoid, with the additional gluing data explicitly supplied.

If the algebra and line are sheaves on a genuine H-stable neighborhood of a fixed point, the same construction produces an equivariant frame near that point whenever the local sections and linearization used above extend there. Start on a common H-stable open domain (intersect the finitely many translates), perform the finite average, and restrict to the open locus where the averaged section generates. This locus is H-stable because the section transforms by a nonzero scalar. In the usual algebraic setting an invertible sheaf has such an open generating locus. This proves a local shrinking statement; an invariant affine neighborhood, a global cover with chosen compatible frames, or algebraization of a completed-local construction requires additional hypotheses.

On overlaps of local scalar frames, ordinary spatial transition functions remain and can carry nontrivial global information. Distinct stabilizers and their characters need not be globally compatible in the desired presentation. Therefore scalar group transitions in a local frame do not eliminate the global line bundle or all Čech/Morita coherences.

Finally, this argument preserves a strict action that is already present. It is separate from formal strictification of arbitrary weak actions, and separate from identifying any synthetic algebra or Morita bimodule with the actual physical stack/coarse mixed transport. No physical operation, operation value, or existence of the physical mixed module is inferred.

## Audit checklist

- Genuine C-linear finite-group action on D: required.
- G-stable proper two-sided I and commutative local B=D/I: required here.
- Genuine classical linearization and one-dimensional residue character: required.
- Scalar character lifts central in D and fixed by G: verified by the C-algebra hypothesis.
- Existing strict finite free module with scalar residue: required only for module descent.
- Weak-action strictification, global gluing, physical ambient identification, and module existence: not supplied by this local result.
