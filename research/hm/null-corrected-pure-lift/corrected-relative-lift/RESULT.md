# Global vanishing for the corrected relative canonical direction

## Conclusion

Yes. Let X=P²_z×U, s:X→U, E=m*HM, K=ω_s, and use the ordinary characteristic-HKR convention

    κ_E(P,v,b) = (1/2)ι_P At_s(E)² + v⌟At_s(E) − b Id_E.

For the specified corrected direction

    η_z = (P, D_P(H_z/2), −2H_z²),

its characteristic class vanishes in the GLOBAL group:

    κ_E(η_z)=0 ∈ H²(X,End(E)⊗K).

Here H_z denotes the relative Atiyah class of O_z(1), and H_z² is identified with its canonical-valued class through P:Λ²Ω¹_s→K. The proof includes every base-cohomology component of At_s(E); it is not a deduction from fiberwise vanishing.

Consequently, for a genuine first-order square-zero algebra/algebroid representing this full HKR class, in the locally free module-lifting framework of the supplied reports, E has a global first-order lift. On the stable-plane open U its relative V-torsor is therefore trivial. A chosen lift gives a trivialization; neither a preferred lift nor a canonical origin is produced.

This constructs an abstract existence argument directly for the corrected relative ambient problem. It neither needs nor proves a chain-level Morita transport of the physical problem. The naive bracket-only problem, and any ambient class with additional unlisted first-order components, are different problems.

## 1. Relative means projection of forms, not restriction to fibers

Use the compact product

    Xbar=P²_z×P²_h,    sbar:Xbar→P²_h,    Ebar=m*HM.

The family E is its restriction to X. Write q for the projection from absolute differentials to relative differentials:

    Ω¹_Xbar → Ω¹_Xbar/P²_h = pr_z*Ω¹_P²_z.

It extends multiplicatively to exterior powers and their cohomology. Naturality of principal parts gives

    A=At_sbar(Ebar)=q(At_Xbar(Ebar))
       ∈ H¹(Xbar,End(Ebar)⊗Ω¹_sbar).

This class can have components involving base Čech degree or base antiholomorphic differential degree. They are retained by q. In a Dolbeault representative, q removes holomorphic dh factors, not antiholomorphic d-hbar factors. In particular, a curvature component dz∧d-hbar is retained. This is the distinction needed to address the possible H¹(U,V) obstruction.

The assertion below is a global identity for A on Xbar before restricting to U. No replacement of A by its individual fiber restrictions is made.

## 2. Global relative Chern identities

Let h=c1 O_P⁴(1). The normalized rank-two HM bundle in the supplied setup has

    c1(HM)=−h,    c2(HM)=4h²,    ch2(HM)=−(7/2)h².

These are also determined by its supplied plane Chern data, since the restriction maps in these degrees from P⁴ to a linear P² identify the respective hyperplane generators. The multiplication morphism satisfies

    m*O_P⁴(1)=O_z(1)⊠O_h(1).

Thus, in absolute Hodge cohomology on Xbar,

    tr At(Ebar)=−(H_z^abs+H_h^abs),
    (1/2)tr At(Ebar)²=−(7/2)(H_z^abs+H_h^abs)².

Under q, H_h^abs maps to zero: the Atiyah class of the base-pulled-back line has its holomorphic cotangent factor entirely in sbar*Ω¹_P²_h. Define H_z=q(H_z^abs). Multiplicativity of q gives GLOBAL relative identities

    tr A=−H_z,
    (1/2)tr A²=−(7/2)H_z².                         (1)

The vanishing of q(H_h^abs) does not discard possible base components of the tracefree A. It computes only the trace and trace-square classes. Controlling the tracefree square requires the next argument.

## 3. Rank-two identity with all base components retained

Put

    B=A−(1/2)(tr A)Id = A+(H_z/2)Id.

There is a global relative cohomology identity

    B²=(1/2)tr(B²)Id.                              (2)

For a rigorous representative proof, choose a Hermitian metric on Ebar and represent its absolute Atiyah class by normalized Chern curvature R. Project its holomorphic cotangent factor to the z factor, obtaining R_z. It represents A and is Dolbeault closed. Its entries have one holomorphic z degree and one arbitrary antiholomorphic degree, hence total differential degree two. In particular these scalar form entries commute, including entries whose antiholomorphic degree lies in the base direction.

The traceless matrix

    R_z,0=R_z−(1/2)tr(R_z)Id

is a rank-two matrix over this commutative even-form algebra. Cayley–Hamilton gives

    R_z,0²=(1/2)tr(R_z,0²)Id.

The statement is invariant under changes of local frame, so it is global. Passing to relative Dolbeault cohomology proves (2). Compact GAGA identifies this with the algebraic coherent-cohomology identity on Xbar; restriction yields the same algebraic identity on X. This route avoids any need to identify analytic and algebraic cohomology on the nonproper open X directly.

At the cohomology level tr A=−H_z, so B is exactly the tracefree class even if a selected curvature representative for H_z is not pointwise equal to −tr R_z. All changes of representatives affect only coboundaries. The argument therefore controls the base-cohomology terms of B², not merely its fiber values.

Using (1) and rank two,

    tr B²
      = tr A² + H_z tr A + (H_z²/4) tr Id
      = −7H_z² − H_z² + H_z²/2
      = −(15/2)H_z².

Hence

    B²=−(15/4)H_z² Id.                             (3)

This is the crucial global scalar identity.

## 4. Evaluate the full corrected direction

The middle-component convention is fixed intrinsically by

    (D_P ℓ)⌟A=ι_P(ℓ A),    ℓ=H_z/2.

Since the Atiyah factors have even total degree and ℓ is scalar,

    (1/2)ι_P A² +(D_Pℓ)⌟A
      = (1/2)ι_P(A+ℓ Id)² − (1/2)ι_Pℓ² Id.

Consequently the corrected characteristic class is

    κ_E(η_z)
      = (1/2)ι_P B² − H_z²/8 Id + 2H_z² Id
      = (−15/8 −1/8 +2)H_z² Id
      = 0.                                         (4)

In these equalities P is the identity Λ²Ω¹_s=K→K, so writing ι_P H_z² as H_z² simply uses this canonical identification. The first term of (4) already has zero tracefree part globally, by (3). Its scalar part then cancels exactly. Thus there is no hidden H¹(U,V) remainder.

The proof actually establishes the corresponding relative characteristic vanishing on the whole compact product Xbar. The explicit ambient construction below likewise exists there, so the same first-order obstruction criterion gives a global module lift on Xbar, not just on X. Stability is unnecessary for this identity or existence assertion; it enters only the vector-bundle torsor description over U. Outside U the supplied constant cohomology dimensions are unavailable, so the lift object must be described by the full relative derived endomorphism complex and deformation groupoid, not an asserted extension of the rank-12 V-torsor. This first-order extension assertion does not settle extension of any mixed lift or of a prescribed particular lift on U.

## 5. Exact consequence for the relative V-torsor

A full square-zero first-order ambient class has multiplication, unary gluing, and scalar triple-unit components. The triple η_z includes all three; in particular its nonzero middle component cannot be silently omitted. There is an explicit genuine algebroid realization, as follows. This construction works on Xbar and can then be restricted to X.

Choose an affine acyclic cover {Q_i} of Xbar, with affine intersections. Choose relative derivation-valued Čech cocycle v_ij representing D_P(H_z/2), and a K-valued Čech 2-cocycle b_ijk representing −2H_z². Coherent cohomology on this cover represents both classes. On every Q_i take the algebra

    B_i=O_(Q_i)⊕K_(Q_i),
    (f,u)(g,w)=(fg,fw+gu+(1/2)P(d_s f∧d_s g)).

The relative biderivation is a Hochschild 2-cocycle, so this product is associative. Its ideal K is central, square-zero, and carries its usual symmetric O-bimodule action. Define overlap algebra isomorphisms

    Φ_ij(f,u)=(f,u+v_ij(f)).

The derivation rule proves multiplicativity directly; Φ_ij is identity on K and on the quotient O. Its inverse subtracts v_ij. Since δv=0, these overlap maps satisfy Φ_ij Φ_jk=Φ_ik. Supply the additional triple coherence units

    a_ijk=1+b_ijk ∈ B_i^×.

They are central, so Ad(a_ijk)=id, as required by the triple-overlap algebra identity. Their pentagon identity reduces exactly to δb=0: products of two K-valued terms vanish and every Φ fixes K. Thus (B_i,Φ_ij,a_ijk) are actual coherent algebroid descent data, not just a putative cohomology class. The quotient is the ordinary structure sheaf, and the square-zero coefficient ideal is K. All maps are relative over the base since d_s and v_ij annihilate base functions.

In the total relative Hochschild–Čech complex these data have degrees (Čech,Hochschild) equal to (0,2), (1,1), and (2,0), respectively. Each displayed cocycle condition holds exactly. With the characteristic convention fixed at the start, orient the overlap indices and coherence equation so that the middle class pairs as +v⌟At_s and the triple unit contributes −b Id. These are precisely the conventions of the supplied module-lifting report. Accordingly the ambient class is η_z, including its nonzero middle coordinate and specified gerbe coordinate. No higher integrability equation is needed for this first-order square-zero construction. Different representative choices give coherently equivalent first-order presentations, rather than literal equality of presentations.

For that fixed representative, the global module obstruction is (4). Local free lifts exist, and its zero cohomology class means a global correction of the gluing data exists. Thus a global module lift L_z exists without importing any physical module.

On U the supplied canonical splitting is

    H²(X,End(E)⊗K)=H¹(U,V) ⊕ H⁰(U,O_U),
    V=R¹s_*(End_0(E)⊗K),

with H⁰(X,End(E)⊗K)=0 and

    H¹(X,End(E)⊗K)=H⁰(U,V).

Equation (4) kills both summands. Therefore the sheaf T_z of lifts with fixed reduction E is a trivial V-torsor. Choosing L_z gives the isomorphism

    V → T_z,    a ↦ L_z+a.

Changing L_z translates this isomorphism. The result is existence and noncanonical triviality, not a canonical cochain primitive or a distinguished section.

There is no claim that a preselected physical lift is this L_z, that physical descent data have been transported, or that the corrected abstract algebroid is physically equivalent to another prescribed ambient algebra. Those claims need a separate comparison. This proof bypasses that comparison only for the independent corrected relative existence statement.

## 6. What remains at mixed order

Fix a genuine two-direction extension B_zh with mixed ideal

    J=K⊗s*ω_U,

annihilated by the two pure first-order ideals. Also fix its full boundary module L_boundary over B_zh/J, including the z lift, the h lift, and their compatibility along E. Neither B_zh nor L_boundary is determined by the vanishing in (4).

The remaining mixed obstruction is

    c_zh(B_zh,L_boundary) ∈ H²(X,End(E)⊗J)
       = H¹(U,V⊗ω_U) ⊕ H⁰(U,ω_U).

If a mixed scalar gerbe modification is permitted, its unique compensating cohomology class kills the second component. It does not change the first component

    θ_zh(B_zh,L_boundary) ∈ H¹(U,V⊗ω_U).

The mixed relative lift torsor is trivial exactly when this remaining class vanishes. If scalar modifications are fixed or forbidden, the scalar component must also vanish without such a change.

More explicitly, for the normalized mixed defect in an acyclic double Čech resolution,

    C=C^(0,2)+C^(1,1)+C^(2,0),
    D=δ_h+(−1)^p δ_z,    DC=0,

first remove its permitted scalar part and choose local vertical primitives

    δ_z x^(0,1)=−C^(0,2).

Then the remaining class is precisely

    θ_zh = [ [C^(1,1)+δ_h x^(0,1)]_vertical ]
           ∈ H¹(U,V⊗ω_U).

The C^(2,0) term supplies coherence ensuring this is a base cocycle. It is not legitimate to omit it in an arbitrary presentation. Gauge changes and changes of local vertical primitives do not alter the resulting class.

The new first-order result supplies a global z-direction boundary lift for the corrected problem. It does not specify an h-direction boundary lift for a separately prescribed problem, a mixed ambient extension, or its normalized mixed defect. Even when both pure corrected lifts are available, their existence does not annihilate mixed cross terms. Changing the chosen pure lift can change the mixed problem; its freedom cannot be used silently when the boundary is fixed. Rank-two scalarity of the square of a normalized Atiyah class does not identify or evaluate this higher small-extension obstruction.

If the goal is a physical mixed obstruction, an identification of the physical ambient extension and boundary with this corrected relative problem remains necessary. Exceptional-parameter extension and global restriction-kernel issues likewise remain for mixed order. No mixed obstruction value, physical two-jet compatibility, or vanishing of H¹(U,V⊗ω_U) is proved here.

## Sources and scope

Primary inputs: ../../null-root-characteristic/root-characteristic-0527/RESULT.md; ../../null-simple-fiber-moduli/family-lift-torsor-0523/RESULT.md. Family geometry and cohomology: ../../null-factor-surfaces/relative-surface-0502/COTANGENT_TARGET.md. Canonical coefficient and first-order ambient interpretation: ../../null-pair-quotient-bracket/canonical-bracket-0517/RESULT.md.

Only static reading and universal relative Atiyah, Chern, curvature, and square-zero descent algebra were used. No physical source/model/jet evaluations or physical matrix products are used.
