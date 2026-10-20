# Finite exceptional support as a punctual modification

## The structural result

Retain the setup and hypotheses of [the relative Chern constraints](https://github.com/Akilleez-QA/read-em-and-weep/blob/01c96a7e1b24685eacd5d1dc52ed0ea026490146/research/hm/relative-models/relative-chern-constraints/PROOF.md) and, only for the numerical consequences in Section 4, [the rigidity corollary](https://github.com/Akilleez-QA/read-em-and-weep/blob/01c96a7e1b24685eacd5d1dc52ed0ea026490146/research/hm/relative-models/relative-chern-constraints/RIGIDITY_COROLLARY.md). Write B=P² over C, ω=ω_B=O_B(−3), X=P²×B, s:X→B, A=m*End₀(HM), and K=A⊗ω_X. Here m:P²×P²→P⁴ multiplies binary quadratics, and HM is the normalized Horrocks–Mumford bundle. Set

- D=R¹s_*A, with local projective dimension at most one;
- V=D∨, a locally free rank-twelve sheaf;
- E=V⊗ω and T=ℰxt¹_B(D,O_B)⊗ω.

Here ℰxt and derived sheaf Hom denote sheaf-valued functors; ordinary Ext denotes global Ext. The predecessor proves Rs_*A≅D[−1], local projective dimension at most one, rank(V)=12, and the relative-duality description used below. Assume, additionally and conditionally, that T has finite support. The empty-support case is included.

Then D is torsion-free, F=D∨∨=V∨ is locally free, and there is a canonical exact sequence

    0 → D → F → Q_exc → 0,

where Q_exc is a finite-length sheaf. It is a quotient of a vector bundle, not the quadratic obstruction operation denoted Q elsewhere. There is a canonical isomorphism

    T ≅ ℰxt²_B(Q_exc,ω).

Consequently H⁰(T)≅H⁰(Q_exc)∨ and length(T)=length(Q_exc). Under the canonical dualities

    H⁰(T) ≅ H⁰(Q_exc)∨,
    H²(E) ≅ H⁰(F)∨,

the Leray differential

    d₂ : H⁰(T) → H²(E)

is the dual of the finite-quotient evaluation map

    ev = H⁰(F→Q_exc) : H⁰(F) → H⁰(Q_exc),

up to the harmless common sign determined by the chosen convention for spectral-sequence differentials. Its kernel is therefore canonically the annihilator of im(ev), equivalently

    ker(d₂) ≅ coker(ev)∨.

In particular the exceptional contribution to H²(X,K) is dual to the failure of global sections of the reflexive hull to surject onto this punctual quotient. No value or rank of ev is evaluated here.

## 1. Why finite support forces torsion-freeness

At a codimension-one point of B the local ring R is a DVR, and ℰxt¹(D,O)_R=0 because T has finite support and ω is invertible. A finite R-module is the direct sum of a free module and cyclic torsion modules R/(π^a). Each nonzero torsion summand has nonzero Ext¹_R(−,R). Thus D_R is free.

The torsion subsheaf of D consequently has support of codimension at least two, hence finite support. At every closed point x, pd(D_x)≤1 over the regular local ring O_{B,x} of dimension two. Auslander–Buchsbaum gives depth(D_x)≥1 (the zero stalk causes no issue). A module of positive depth has no nonzero finite-length submodule: a nonzero finite-length submodule has a nonzero socle and would force depth zero. Hence the torsion subsheaf vanishes.

A torsion-free coherent sheaf on this smooth surface injects into its double dual. The double dual F is reflexive and therefore locally free. The map D→F is an isomorphism in codimension one, so its cokernel Q_exc has finite support. These statements also show that D and F have the same rank twelve.

## 2. Canonical finite-length duality

For a finite-length sheaf Q on a smooth surface,

    ℋom(Q,ω)=0,    ℰxt¹(Q,ω)=0,
    RHom_B(Q,ω) ≅ ℰxt²(Q,ω)[−2],

where RHom_B here is the derived sheaf Hom. The vanishings are the grade-two property of finite-length modules over regular local rings of dimension two. Applying derived sheaf Hom into ω to 0→D→F→Q_exc→0, with F locally free, gives

    ℋom(F,ω) ≅ ℋom(D,ω)=E,
    ℰxt¹(D,ω) ≅ ℰxt²(Q_exc,ω).

The second group is T because ω is invertible. This establishes the claimed canonical isomorphism; it does not require choices of presentations or local coordinates.

The functor Q↦ℰxt²(Q,ω) is finite-length duality on B. Locally it preserves length (this follows by a composition series and its exactness on finite-length modules); its double dual is canonically Q. Thus Q_exc and T have the same support and length. Since Q_exc is finite, the local-to-global Ext spectral sequence gives

    Ext²_B(Q_exc,ω) ≅ H⁰(ℰxt²_B(Q_exc,ω)) ≅ H⁰(T).

Serre duality on the proper smooth surface supplies the canonical trace pairing

    Ext²_B(Q_exc,ω) × H⁰(Q_exc) → C.

It is perfect, giving H⁰(T)≅H⁰(Q_exc)∨. Similarly, since E=F∨⊗ω, the ordinary vector-bundle Serre pairing gives H²(E)≅H⁰(F)∨.

## 3. Identifying the derived extension, not merely its dimensions

Use cohomological shifts, so a sheaf M[−j] has its sole cohomology in degree j. The already audited relative duality identifies

    C := Rs_*K ≅ RHom_B(D,ω)[−1].

Indeed Rs_*A=D[−1], relative duality contributes the shift [−2], and the base canonical twist is ω. The cohomology sheaves of C are E in degree one and T in degree two.

Dualizing the triangle D→F→Q_exc→D[1] into ω gives

    RHom_B(Q_exc,ω) → E → RHom_B(D,ω)
       → RHom_B(Q_exc,ω)[1].

Using RHom_B(Q_exc,ω)=T[−2], rotating and shifting gives

    E[−1] → C → T[−2] → E.

This is the canonical cohomological truncation triangle for C: its first map induces the canonical isomorphism on degree-one cohomology and its second map the canonical isomorphism on degree-two cohomology. Thus its connecting morphism T[−2]→E is exactly the derived extension governing Leray. It is also, up to the usual rotation sign, the derived dual of the quotient morphism F→Q_exc.

On global hypercohomology, the connecting map H⁰(T)→H²(E) of this triangle is the Leray d₂. Equivalently, apply global Ext_B(−,ω) to the original short exact sequence. The relevant exact sequence is

    Ext¹_B(F,ω) → Ext¹_B(D,ω) → Ext²_B(Q_exc,ω)
       → Ext²_B(F,ω) → Ext²_B(D,ω) → 0.

The final zero uses Ext³_B(Q_exc,ω)=0. Under the identifications above and C=RHom_B(D,ω)[−1], this is precisely

    H¹(E) → H²(X,K) → H⁰(T) → H²(E) → H³(X,K) → 0.

The central arrow is q*:Ext²_B(Q_exc,ω)→Ext²_B(F,ω), induced contravariantly by q:F→Q_exc. Naturality of Serre duality says that q* is the dual of H⁰(q). Explicitly, for t∈H⁰(T) and f∈H⁰(F),

    ⟨d₂(t),f⟩ = ± ⟨t,ev(f)⟩.

The single sign depends only on triangle/Leray conventions; it affects neither the map's rank nor its kernel, image, or annihilator description. This proves the identification of the actual structural map, rather than only matching dimensions of its source and target.

For an additional exactness check, dualizing the cohomology sequence of the modification gives

    0 → H¹(F)∨ → H¹(D)∨ → H⁰(Q_exc)∨
       → H⁰(F)∨ → H⁰(D)∨ → 0,

because H¹(Q_exc)=0. It matches the displayed Leray sequence via global Serre duality. In particular, the leftmost injection is also recovered.

## 4. Numerical consequences under the imported rigidity input

The pinned rigidity corollary imports the pure-boundary weight-two vanishing and total h²(X,K)=62 and proves h⁰(D)=44 and h⁰(V)=0. Retaining those inputs, set

    ℓ=length(T)=length(Q_exc),   r=rank(ev)=rank(d₂).

Left exactness gives ker(ev)=H⁰(D). Therefore

    r=h⁰(F)−44,
    h²(E)=h⁰(F)=44+r,
    dim coker(ev)=ℓ−r,
    dim ker(d₂)=ℓ−r,
    h¹(E)=62−ℓ+r.

The dimension inequalities 0≤r≤ℓ and ℓ−r≤62 follow immediately; no numerical value of r or ℓ follows. Equivalently, if one writes defect=dim coker(ev), then h¹(E)=62−defect and the exceptional quotient of H²(X,K) has dimension defect.

If T=0, then Q_exc=0, D=F is locally free, ev has zero target, r=0, h⁰(F)=44, and the exceptional contribution vanishes. If T is nonzero with finite support, ev need not be surjective or zero: neither alternative is asserted. Nothing here proves that the exceptional support is finite or nonempty. Exceptional curves invalidate the finite-length argument and require the divisorial framework of the prior proof.

## Scope and next mathematical datum

The new reduction is from an abstract Leray transgression to an explicitly characterized, but still unevaluated, finite-quotient map: determine the canonical modification D⊂F and its global-section map to Q_exc. The quotient sheaf and the embedding matter; the support set and its three-dimensional residue fibers do not determine this map. This is a structural identification, not a computation of its entries or rank.

All groups above concern the full recipient. Block exchange interchanges the two projections, so these fixed-projection groups are not independently identified with the retained thirty-dimensional sector. No entry or rank of the evaluation map, and no specified obstruction value, is determined by this structural theorem.
