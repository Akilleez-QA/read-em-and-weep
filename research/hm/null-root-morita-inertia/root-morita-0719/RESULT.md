# Exact line untwisting by Morita transport of a differential algebroid

## Result and boundaries

A genuine classical line L can always be untwisted from the reduction of a locally free module by changing a genuine ambient algebroid, provided its transition functions admit local invertible lifts. This does not require a quantization of L as a module over the original ambient algebroid. It constructs a Morita equivalence whose reduction is tensoring by L^{-1}; it does not assert that a global module exists on either side.

The construction is upstairs, or on a specified stack/action groupoid. It does not identify the transported algebroid with a prescribed downstairs or physical model. A rational class such as H/2 cannot replace the genuine line. Equivariance and descent to a ramified coarse quotient require the additional qualifications in Section 7.

All formulas below are universal formal algebra. No physical source or jet values are evaluated in this argument.

## 1. Setup and row convention

Let A_i be associative unital local differential deformation algebras, with products denoted by juxtaposition, reducing to O on a common space. Their overlap maps and triple units satisfy

    F_ij F_jk = Ad(A_ijk) F_ik,
    A_ijk A_ikl = F_ij(A_jkl) A_ijl.

Every displayed noncommutative product has the written order. Maps act entrywise on matrices. Classical row transitions for E satisfy g_jk g_ij=g_ik. A left module represented by rows has overlap maps

    φ_ij(v)=F_ij(v)G_ij,
    F_ij(G_jk)G_ij=A_ijk G_ik.

Let ℓ_ij be classical transitions of a genuine line L, so ℓ_jk ℓ_ij=ℓ_ik. Choose any local units q_ij in A_i lifting ℓ_ij. No twisted cocycle equation is imposed on q. Unit lifting holds across nilpotent extensions whenever sections can be lifted; in a complete formal setting use compatible adic lifts and inverses. Refinement or a coefficientwise local presentation can supply this local lifting hypothesis. Set q_ii=1 in normalized data.

## 2. Exact ambient formulas and pentagon

Define A^L locally to have the SAME algebras and products A_i, and put

    F^L_ij = Ad(q_ij^{-1}) F_ij,
    A^L_ijk = q_ij^{-1} F_ij(q_jk)^{-1} A_ijk q_ik.       (1)

The inverse in F_ij(q_jk)^{-1} is the algebra inverse, equivalently F_ij(q_jk^{-1}). These reduce to identity gluing and unit triple coherence. Inner conjugation is a differential operator order by order when the original product and overlap maps are differential. Thus the differential nature is preserved.

For the first coherence equation,

    F^L_ij F^L_jk
      = Ad(q_ij^{-1} F_ij(q_jk)^{-1} A_ijk) F_ik
      = Ad(A^L_ijk) F^L_ik.

For the pentagon, the left side is

    A^L_ijk A^L_ikl
      = q_ij^{-1} F_ij(q_jk^{-1}) A_ijk
          F_ik(q_kl^{-1}) A_ikl q_il
      = q_ij^{-1} F_ij(q_jk^{-1} F_jk(q_kl^{-1}))
          A_ijk A_ikl q_il
      = q_ij^{-1} F_ij(q_jk^{-1} F_jk(q_kl^{-1}) A_jkl)
          A_ijl q_il.

Here the second equality uses A_ijk F_ik(x)=F_ij F_jk(x) A_ijk. The right side F^L_ij(A^L_jkl) A^L_ijl expands to exactly the last line: the adjacent q_ij q_ij^{-1} and F_ij(q_jl) F_ij(q_jl)^{-1} cancel. No triple unit or lifted line unit was commuted through another factor.

Equivalently, for arbitrary units c_ij the gauge formula is

    F^c_ij=Ad(c_ij)F_ij,
    A^c_ijk=c_ij F_ij(c_jk) A_ijk c_ik^{-1}.

Formula (1) uses c=q^{-1}. Using c reducing to ℓ rather than ℓ^{-1} would tensor the module reduction by L, not untwist it.

## 3. Local Morita bimodules and their coherence

Let P_i be the regular (A_i,A^L_i)-bimodule, with overlap map

    p_ij(p)=F_ij(p)q_ij.

Its left and right semilinearity is

    p_ij(a p b)=F_ij(a) p_ij(p) F^L_ij(b).

Its precise triple coherence is

    p_ij p_jk(p)=A_ijk p_ik(p)(A^L_ijk)^{-1}.           (2)

Indeed the left side equals A_ijk F_ik(p) A_ijk^{-1} F_ij(q_jk)q_ij, which is the right side by (1). Thus P is a coherent invertible bimodule between the algebroid presentations, reducing to L.

The inverse Q_i is the regular (A^L_i,A_i)-bimodule with

    qmap_ij(x)=q_ij^{-1}F_ij(x),
    qmap_ij qmap_jk(x)=A^L_ijk qmap_ik(x) A_ijk^{-1}.

Local multiplication identifies P_i⊗_{A^L_i}Q_i with A_i and Q_i⊗_{A_i}P_i with A^L_i. These identifications respect descent: for example

    (F_ij(p)q_ij)(q_ij^{-1}F_ij(x))=F_ij(px),

and in the reverse order the analogous product is F^L_ij(xp). Hence these are genuinely inverse Morita functors, not merely identifications of endomorphism sheaves.

## 4. Transporting module transitions, defects, and chain complexes

Suppose M is an A-module reducing to E⊗L. Then N=Q⊗_A M is an A^L-module reducing to E. In row notation its transitions are

    H_ij=q_ij^{-1}G_ij.                                (3)

This is LEFT multiplication of every matrix entry by q_ij^{-1}, not right multiplication. Directly,

    F^L_ij(H_jk)H_ij
      =q_ij^{-1}F_ij(q_jk)^{-1}F_ij(G_jk)G_ij
      =A^L_ijk q_ik^{-1}G_ik=A^L_ijk H_ik.

Conversely G_ij=q_ij H_ij reconstructs M from N. For arbitrary candidate transitions, not necessarily satisfying descent, the defects obey the exact identity

    D^L_ijk=q_ij^{-1}F_ij(q_jk)^{-1}D_ijk,              (4)

where D=F_ij(G_jk)G_ij−A_ijk G_ik. Thus solving descent on one side is exactly equivalent to solving it on the other.

Across a small extension with kernel I, suppose the classical G transitions are ℓ_ij g_ij. The multiplier on I in (4) reduces to ℓ_ik^{-1}. Therefore the normalized End(E)-valued obstruction cocycles agree literally:

    g_ik^{-1}D^L_ijk=(ℓ_ik g_ik)^{-1}D_ijk.

This equality is understood on the I-valued defect, where products reduce to classical ones. It preserves fixed-reduction deformation groupoids and their obstruction classes under End(E⊗L)=End(E). It supplies a chain-level comparison stronger than equality of the characteristic evaluation alone.

For a local left-module morphism represented by v↦vT_i, the transported morphism has the SAME matrix T_i. Indeed its descent equation G_ij T_i=F_ij(T_j)G'_ij becomes H_ij T_i=F^L_ij(T_j)H'_ij after left multiplication by q_ij^{-1}. Consequently the construction applies degreewise to complexes, preserves differentials and compositions, and yields an exact equivalence; the local bimodules are free on both sides. Derived or dg module categories inherit the corresponding equivalence where defined. No new higher coherence is hidden in the phrase “chain-level”: (1)–(4) are actual cochain/descent identities.

Different choices of q give equivalent presentations, not generally literal equality. For q and q̃, applying the c-gauge with c_ij=q̃_ij^{-1}q_ij to A^L(q) yields A^L(q̃). This comparison reduces to the identity. No canonical lifted transition representative is selected.

## 5. Literal square-zero check and characteristic sign

Take a central even square-zero parameter ε. Write

    f⋆g=fg+ε μ_i(f,g),  F_ij=Id+ε v_ij,
    A_ijk=1+ε a_ijk,    q_ij=ℓ_ij+ε r_ij.

For normalized μ, direct expansion of (1) gives

    μ^L_i=μ_i,
    v^L_ij(f)=v_ij(f)+ℓ_ij^{-1}(μ_i(f,ℓ_ij)−μ_i(ℓ_ij,f)),
    a^L_ijk=a_ijk+r_ik/ℓ_ik−r_ij/ℓ_ij−r_jk/ℓ_jk
                    −v_ij(ℓ_jk)/ℓ_jk−μ_i(ℓ_jk,ℓ_ij)/ℓ_ik. (5)

One quick way to verify the last line is to put K=F_ij(q_jk)⋆q_ij, observe A^L=K^{-1}⋆A_ijk⋆q_ik, and subtract the first-order coefficients of K and A_ijk⋆q_ik. The r terms form minus the Čech coboundary of r/ℓ. If μ=(1/2)π, then the extra unary term is π(df,d log ℓ_ij). It is not in general zero.

The supplied characteristic convention is

    κ_E(π,v,b)=(1/2)ι_π At(E)^2+v⌟At(E)−b Id.

Writing λ=c1(L), its tensor-line identity is

    κ_{E⊗L}(π,v,b)
      =κ_E(π,v+D_πλ,b−v⌟λ−(1/2)ι_πλ²).               (6)

Our direction is from E⊗L to E, so (6), with exactly the displayed signs, is the compatibility required of the induced ordinary HKR transport. Formula (5) gives the actual cochain transformation without relying on an HKR comparison or inferring an ambient class from its potentially nonfaithful characteristic evaluation. The usual identification of the induced HKR action with the triple in (6) also requires the specified ordinary HKR/Čech sign convention; no Todd-modified convention is introduced here. This report does not infer equality of full ambient classes merely from equality of their κ-images.

For a genuine upstairs root with λ=(1/2)p*H, this explains why untwisting changes unary overlap data as well as triple-unit data. It creates no fractional line downstairs and establishes no compatibility with finite pushdown on its own.

## 6. Exact factorization for an external product ambient

Let the space be Z×H, L=L_z⊠L_h, and assume the ORIGINAL ambient is an actual external tensor algebroid A_z⊠A_h, not merely one with matching pure characteristic classes. Use product opens with indices (i,α). Assume even central parameters with

    s²=t²=0,  but st≠0.

Take factor lifts q^z_ij, q^h_αβ, and choose

    q_(iα)(jβ)=q^z_ij⊗q^h_αβ.

Cross-factor elements commute in this ordinary external tensor algebra. The inverse, overlap maps, and units then factor exactly:

    q^{-1}=(q^z)^{-1}⊗(q^h)^{-1},
    F^L_(iα)(jβ)=(F_z^{L_z})_ij⊗(F_h^{L_h})_αβ,
    A^L_(iα)(jβ)(kγ)=(A_z^{L_z})_ijk⊗(A_h^{L_h})_αβγ,
    P=P_z⊠P_h,   Q=Q_z⊠Q_h.

Thus (A_z⊠A_h)^{L_z⊠L_h} is precisely A_z^{L_z}⊠A_h^{L_h} in these chosen presentations. Sequential factor untwisting agrees with simultaneous untwisting here.

The mixed coefficients are part of the construction. For example, if transformed factor units are 1+s a_z and 1+t a_h, their product unit is

    1+s a_z+t a_h+st(a_z⊗a_h).

If the transformed factor overlaps are Id+s f_z and Id+t f_h, their external tensor includes st(f_z⊗f_h). Likewise the local product of decomposable inputs is

    (a⊗b)⋆(a'⊗b')
      =aa'⊗bb' +s μ_z(a,a')⊗bb' +t aa'⊗μ_h(b,b')
                  +st μ_z(a,a')⊗μ_h(b,b').

And q=(ℓ_z+s r_z)⊗(ℓ_h+t r_h) includes st(r_z⊗r_h). Inverting, transporting, or multiplying after incorrectly imposing st=0 would lose the specified mixed extension.

The same statement works with sheaf-valued square-zero coefficient lines: the mixed ideal is their tensor product. For canonical coefficient lines on two planes this is K_z⊗K_h=ω_{Z×H}.

If only L factors while the ambient is arbitrary, (1) still works but no external factorization follows. General successive gauges c followed by d compose in the order dc. Cross-factor commutation and absence of additional mixed terms must be proved from an external ambient identification, not assumed from the classical product geometry. Most importantly, E need not be an external tensor bundle or an external tensor module: even for this factorized ambient the existence of a global mixed lift of E is a separate obstruction problem.

## 7. Equivariance, root inertia, and coarse descent

Nonequivariant line data prove only the nonequivariant construction. For an equivariant statement one needs a specified genuine linearization of L (or a specified twisting gerbe for projective linearization), the ambient group action including all coherence, and compatible module equivariance when a module is being transported.

There is a safe fully coherent formulation: present the quotient stack by its action/Čech groupoid, place the algebra maps F and coherence units A on that full groupoid, and choose lifts q of the classical line cocycle on ALL its arrows, including stabilizer arrows. Formula (1) on these arrows and composable pairs gives a coherent Morita transport by the same proofs. Its reduction sends an inertia representation W⊗χ_L to W. This retains, rather than discards, the root character.

However, even if the original group action was strict, the transported action need not remain strict: the new coherence units for group multiplication can be nontrivial. It is generally a weak action up to specified inner automorphisms. One must not apply an invariant-basis lemma requiring a genuine strict group action to this weak presentation without constructing a compatible strictification or proving the equivalent descent assertion in the stack formalism. Averaging arbitrary q does not prove the needed nonlinear coherence identities. Under special compatible choices strictness may hold, but it is an additional result.

An order-two root identity for the underlying line does not itself specify its linearization; scalar inertia can be nontrivial and is invisible in End. The local sign-ramification counterexample from ramified-descent-0644 remains valid for naive invariant formation. The present Morita construction avoids pretending that invariants untwist the original module: it first changes the ambient presentation and transfers the character into the bimodule. Whether its resulting stack data admit the desired coarse algebra/module description still needs proof.

For a strictly equivariant transported module with trivial residual stabilizer representation, an appropriate local invariant-basis argument can sometimes establish locally free invariant modules. That assertion requires its actual hypotheses (a genuine action, suitable local algebra and residue, exact invariants/characteristic zero, and compatible reductions). It does not identify the invariant algebra with any proposed canonical-coefficient or external-product algebroid. In particular normalized trace identifies certain coefficient sheaves linearly; it does not invert the ramification multiplication factors or supply this algebra identification.

## 8. What this resolves and what remains

Resolved: a universal exact Morita construction untwists any genuine lifted line transitions, with explicit overlap maps, triple units, inverse bimodules, row-module formulas, defect comparison, pentagon verification, and exact external-product factorization under the stated ambient hypothesis. A prior demand for a line module over the unchanged ambient is unnecessary for this change-of-ambient construction.

Still required for any physical-to-corrected comparison:

1. A genuine root line and its full linearization or gerbe data on the relevant space/stack, plus local unit lifts.
2. The actual full ambient algebroid and equivariance coherences to which (1) is applied.
3. A chain-level identification of the resulting ambient with the proposed corrected model, including the mixed st coefficients and any frozen jet identifications. Matching ordinary HKR classes or pure restrictions is insufficient.
4. A strictification/coarse-descent argument, where required, checking local inertia, coefficient multiplication, and reduction compatibility.
5. Existence of the relevant module/boundary and vanishing of its remaining mixed obstruction for that specified ambient. Morita equivalence preserves this question; it does not solve it.

The pure-lift uniqueness report concerns a fixed corrected ambient and can compare transported pure modules only AFTER the necessary ambient identification and reduction compatibility have been supplied. Neither its pure contractibility nor the external-product construction evaluates the mixed obstruction. No retained physical obstruction value is evaluated here.

## Static inputs

Read in full or relevant complete sections:

- ../../null-module-boundary-audits/module-lifting/RESULT.md
- ../../null-root-characteristic/root-characteristic-0527/RESULT.md
- ../../null-ramification-guard/ramified-descent-0644/RESULT.md
- ../../null-pure-lift-uniqueness/pure-lift-uniqueness/RESULT.md

All new identities are obtained directly from the stipulated algebroid and row-module equations.
