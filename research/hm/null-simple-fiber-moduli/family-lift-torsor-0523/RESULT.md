# Relative lift torsors and the conditional mixed gluing class

## Outcome

For the universal family on the stable-plane open, a specified canonical-valued first-order algebra/algebroid lifting problem, with a fixed global scalar compensation, determines a torsor under the rank-12 bundle V. Its obstruction to a global section is an element of H¹(U,V). An existing global first-order module lift supplies a section and therefore trivializes this torsor; it does not canonically choose a trivialization before that lift is chosen.

A specified mixed small-extension problem similarly determines, after its scalar obstruction is cancelled, a V⊗ω_h-torsor with class in H¹(U,V⊗ω_h). This class is canonical relative to the full mixed ambient extension and the fixed module on its first-order boundary, up to equivalence. A canonical bracket, the universal family, and a pure fiber-direction lift do not by themselves determine those data or a mixed class. No actual mixed class or obstruction value is computed here.

## 1. Setup and the exact splitting

Work over C. Put Z=P²_z, X=Z×U, with s:X→U, where U⊂P²_h is the stable-plane open from the supplied reports. Let E=m*HM, A=End(E), A₀=End₀(E), and r=rank(E). Use the intrinsic relative canonical bundle K=ω_s=pr_z*ω_Z. Set

    V=R¹s_*(A⊗K)=R¹s_*(A₀⊗K).

The supplied fiber calculations give

    R⁰s_*(A⊗K)=0,
    R¹s_*(A⊗K)=V, of rank 12,
    R²s_*(A⊗K)=O_U,

where the last identification is Serre trace. Trace splitting and the product projection give stronger, canonical derived statements:

    A=O_X·id_E ⊕ A₀,
    Rs_*K ≅ O_U[-2],
    Rs_*(A₀⊗K) ≅ V[-1].

For the scalar summand the projection A→O_X is tr/r; the Serre-trace coordinate on R²s_*(A⊗K) is r times the scalar-inclusion coordinate. Consequently

    H²(X,A⊗K) ≅ H¹(U,V) ⊕ H⁰(U,O_U),                 (1)
    H¹(X,A⊗K) ≅ H⁰(U,V),
    H⁰(X,A⊗K)=0.

The second coordinate in (1) is the scalar-inclusion coordinate. These are not merely associated graded groups: the trace splitting eliminates a potential Leray ambiguity or differential. For any line bundle M on U, projection formula gives

    H²(X,A⊗K⊗s*M) ≅ H¹(U,V⊗M) ⊕ H⁰(U,M),           (2)
    H¹(X,A⊗K⊗s*M) ≅ H⁰(U,V⊗M),
    H⁰(X,A⊗K⊗s*M)=0.

In particular M=ω_U=ω_h|_U gives the mixed target. These statements use neither affineness of U nor an assumed global moduli space. The derived identifications are canonical because the tracefree relative complex has exactly one nonzero cohomology sheaf. Constant volume/determinant factors are retained if the canonical-line normalizations in the bracket report have not been fixed.

## 2. Which deformation problem is being classified

Fix a genuine first-order algebra or algebroid thickening B_z of O_X with square-zero coefficient K, together with its algebra descent data. For example, the relative canonical wedge bracket supplies a particular split first-order algebra, but it does not supply the other choices below automatically. Fix the reduction to E and require every comparison isomorphism to induce the identity on E. Consider locally free module lifts with this fixed reduction. The argument applies in the locally free gluing framework of the module-lifting report: local free modules exist, their obstruction is in H²(A⊗K), corrections are additive End(E)⊗K cochains, and the ambient descent equations hold.

Let c_z∈H²(X,A⊗K) be the module obstruction for this fixed ambient problem. A scalar square-zero algebroid modification is described by γ∈H²(X,K). Adopt the module-lifting report's sign convention: adding the scalar triple-unit cochain a changes the module defect by −a·id_E. Thus scalar compensation changes

    c_z ↦ c_z − i(γ),    i(γ)=γ·id_E.                   (3)

Equivalently one may define a gerbe action with the opposite sign; then the compensating γ changes sign. No conclusion here depends on that convention.

Write c_z=(θ_z,σ_z) under (1). Then H²(X,K)=H⁰(U,O_U), and the unique scalar compensation class that kills its fiberwise scalar obstruction is γ=σ_z. In trace coordinates it is γ=tr(c_z)/r. Equation (3) leaves the tracefree component θ_z unchanged.

Important distinction: the fact that every fiber obstruction is scalar does not imply that c_z is globally scalar. Its remaining component is precisely θ_z∈H¹(U,V).

## 3. Can the fiber compensations be made global?

For this product family, with unrestricted additive square-zero scalar gerbes, yes at the level of cohomology classes. The relative obstruction section σ_z is regular, not an arbitrary assignment of complex numbers to fibers. The map

    H²(X,K) → H⁰(U,R²s_*K)=H⁰(U,O_U)

is an isomorphism. Hence σ_z has a unique global scalar gerbe class, with no further base-gluing obstruction. Moreover H¹(X,K)=H⁰(X,K)=0, and the same statements hold over every base open. Thus gerbes of this band with the same class are equivalent, the equivalence is unique up to isomorphism, and its residual band-valued automorphisms vanish. Cochain representatives and cochain equivalences can still differ; one must transport module lifts through the chosen equivalence rather than equate presentations literally.

This conclusion assumes that arbitrary additive K-gerbe modifications are allowed and that the ambient lifting problem already exists globally. If scalar modifications are frozen, restricted by a fixed physical two-jet, required equivariance, a normalization, or an extension across excluded parameters, σ_z must lie in the image of the actually permitted scalar modifications. Failure of that image condition is a genuine obstruction to allowed compensation. A merely pointwise chosen scalar family need not be regular and need not define any global gerbe. Those are different issues from H¹(U,V).

For M-valued coefficients the same argument uses H²(X,K⊗s*M)=H⁰(U,M), with H¹ and H⁰ equal to zero. In particular there is likewise no extra scalar-cohomology gluing obstruction for the mixed band K⊗s*ω_U once its obstruction section and permitted compensation are specified.

## 4. The relative first-order torsor

Fix a global compensated ambient algebroid, including its chosen representative or a coherent equivalence class. Define T_z(W), for W⊂U, as isomorphism classes of locally free module lifts over Z×W, with the fixed identification of their reduction with E|_(Z×W).

After compensation, the obstruction on a sufficiently small affine W is zero: by (1) it belongs to H¹(W,V)=0. Thus T_z is locally nonempty on the base. Whenever a lift exists over W, the difference between two lifts, modulo identity-on-reduction frame changes, lies in

    H¹(Z×W,A⊗K)=Γ(W,V).

The action is simply transitive. Infinitesimal automorphisms of any such lift are H⁰(Z×W,A⊗K)=0. Hence there is no residual groupoid obstruction to descent of isomorphism classes: the relative lift stack is equivalent to a sheaf T_z, and T_z is a torsor under the additive vector bundle V. This assertion concerns the stack pushed to the base; local frame automorphisms on subsets of X still occur in its Čech presentation.

Choose affine base opens W_α and lifts L_α. On W_αβ let v_αβ∈Γ(W_αβ,V) be determined by

    L_β = L_α + v_αβ.

Then v_αβ+v_βγ=v_αγ, and

    [T_z]=[v_αβ]∈H¹(U,V).                                (4)

Changing local choices L_α to L_α+a_α changes v_αβ by a_β−a_α. Equation (4) vanishes exactly when a global lift exists. Under matching sign conventions for the obstruction and torsor cocycles, it is the θ_z component of c_z; reversing the convention for the torsor difference reverses that equality, without changing the vanishing criterion.

If L_z is an already chosen global lift, the map v↦L_z+v is an isomorphism of V-torsors V≅T_z. Global lifts form an affine space under H⁰(U,V), not a canonically pointed vector space. Replacing L_z by L_z+a translates the trivialization by a. Any stipulated existing first-order lift can be used here only after it is identified with a lift for this same compensated ambient problem; a lift of a different algebra or gerbe does not automatically provide a section.

If reduction identifications are forgotten, ordinary automorphisms of E, including scalar units from the base, must also be quotiented or retained in a groupoid. They are not the infinitesimal automorphisms above. The clean torsor statement uses fixed reduction and identity-on-reduction comparisons.

## 5. What must be fixed at mixed order

Let B_zh be a genuine two-direction algebra/algebroid extension with ideals in the fiber and base directions, and mixed ideal

    J=K⊗s*ω_U.

Assume the two first-order ideals kill J, J²=0, and the quotient B_∂=B_zh/J is the first-order boundary. For example the tensor product of the normalized first-order canonical algebras supplies one candidate mixed ambient algebra. It is not thereby identified with any separately stipulated deformation.

A mixed module lifting problem requires a specified locally free B_∂-module L_∂ reducing to E. This includes both pure first-order module lifts and their compatible identification along E. A pure fiber lift L_z alone is insufficient: the base-direction lift may not have been specified or may not exist, and ambient mixed descent data may differ. Fixing the full boundary is what makes this a small-extension lifting problem with coefficient A⊗J.

Its obstruction is

    c_zh(B_zh,L_∂)∈H²(X,A⊗J)
       ≅ H¹(U,V⊗ω_U) ⊕ H⁰(U,ω_U).                       (5)

After an allowed fixed mixed scalar compensation, the relative mixed-lift sheaf is a torsor T_zh under V⊗ω_U. Its class is the first component of (5), with the same torsor-sign convention as above. Fiberwise solvability after scalar compensation is consistent with a nonzero class in H¹(U,V⊗ω_U). A global pure first-order lift trivializing T_z does not trivialize T_zh.

The word canonical is therefore conditional: the class is invariant under choices of covers, arbitrary top-order transition lifts, and coherent presentation equivalences of the specified mixed problem. It is not canonically determined by E, V, or the fiber bracket alone.

## 6. Exact double-Čech construction

Choose an affine base cover {W_α}, a sufficiently refined fiber/local trivialization cover, and an acyclic double Čech resolution for F=A⊗K⊗s*M, with M=O_U for pure first order or M=ω_U for mixed order. Let p denote base Čech degree and q the fiber Čech degree. Put

    D=δ_h+(-1)^p δ_z.

The normalized linearized module descent defect is a total degree-two cocycle

    C=C^{0,2}+C^{1,1}+C^{2,0},    DC=0.                  (6)

Here “normalized defect” has exactly the meaning in the module-lifting report: lift the fixed lower-order module transitions arbitrarily, subtract the required algebroid descent equation, and identify the residual square-zero term with F using the classical transitions. The exact ambient associativity and pentagon imply DC=0. A top-order module correction x of total degree one changes C to C+Dx. No actual transition entries or matrix products are evaluated by this construction.

First remove the scalar obstruction by a global permitted scalar modification. Its cohomology class is the H⁰(U,M) component of (2). The resulting C^{0,2} is vertically exact on each W_α. Choose local correction cochains

    x^{0,1} with δ_z x^{0,1} = −C^{0,2}.

Extend x by zero in bidegree (1,0). The corrected defect has

    C'^{0,2}=0,
    C'^{1,1}=C^{1,1}+δ_h x^{0,1},
    C'^{2,0}=C^{2,0}.                                    (7)

The (1,2) and (2,1) components of DC'=0 give

    δ_z C'^{1,1}=0,
    δ_h C'^{1,1}=−δ_z C'^{2,0}.                          (8)

Taking vertical H¹ therefore gives an honest base Čech 1-cocycle

    b_αβ=[C^{1,1}_αβ+(δ_h x^{0,1})_αβ]_vertical
          ∈ Γ(W_αβ,V⊗M),
    θ(C)=[b]∈H¹(U,V⊗M).                                 (9)

This is the promised exact formula. It uses the linearized module equations and their coherence, rather than a heuristic differentiation of the torsor T_z. If local vertical solutions are changed by vertical closed cochains a_α, formula (9) changes b by δ_h[a]. Vertical exact changes and bidegree-(1,0) gauge corrections have zero vertical H¹ class. A general change C→C+Dy likewise leaves θ(C) unchanged after adapting x. Thus (9) is intrinsic to the specified extension problem.

The C^{2,0} term is the double-overlap/triple-base coherence datum: it ensures the second relation in (8). It cannot simply be omitted in an arbitrary presentation. Nevertheless R⁰s_*F=0, so it supplies no additional base H² obstruction or residual automorphism after the H¹ torsor obstruction vanishes. Trace splitting makes (9) the actual tracefree component of (2), with no unaccounted spectral-sequence differential.

Equivalently, solve the mixed module equations separately over each Z×W_α. The affine difference between these local solutions on W_αβ is b_αβ, up to the explicitly chosen torsor orientation. This gives the relative torsor construction of Section 4 directly from the double complex.

## 7. Dependence on ambient, scalar, and lower-order choices

- Top-order module lifts or frame gauges: change C by a total coboundary, hence leave (9) unchanged. Coherent equivalences of ambient presentations transport both the boundary module and the obstruction.
- Different genuine mixed ambient extensions with the same reduction: if their difference is an allowed closed ambient cochain η, the module-lifting report gives c_new=c_old+κ_E([η]). The change in θ is the tracefree component of κ_E([η]) under (2). Therefore the mixed class need not be independent of the mixed ambient extension.
- Pure mixed scalar change: κ_E of a scalar triple-unit change is −γ·id_E. It changes only the H⁰(U,ω_U) component of (5). Thus the tracefree mixed class is independent of such an isolated top-order scalar modification, after the other data have been identified.
- Representatives of the same compensating scalar class: transport through coherent gerbe equivalences; their cochain differences are gauge, not new obstruction values. The scalar class required to compensate a fixed obstruction is unique here.
- Changes of a pure first-order gerbe, or of a pure first-order module lift: these change the lower-order boundary itself. They may alter mixed cross terms and hence θ_zh. The small-extension κ formula for changing only the top-order ambient extension does not prove invariance under these changes. A lower-order comparison, including its mixed compatibility, is required.
- If both pure boundary lifts are fixed, no arbitrary freedom to vary them may be used when testing the fixed mixed obstruction. If their variation is allowed, existence becomes a problem over the allowed family of boundary choices; (9) must be recomputed or compared for that family.

## 8. Exact datum still needed

To evaluate the mixed gluing class one needs:

1. A specified globally coherent mixed ambient algebra/algebroid, including its mixed multiplication, gluing maps, triple units, and coefficient normalization, or equivalent intrinsic extension data.
2. A specified compatible first-order boundary module, including the base-direction lift as well as the chosen fiber-direction lift and scalar-gerbe identifications.
3. The resulting normalized mixed defect C in (6), or equivalent local mixed solutions and overlap differences.
4. An allowed global scalar compensation for its scalar component, followed by the vertical primitives x^{0,1} needed in (9).

Items 3–4 may be calculated in any acyclic presentation; the resulting class does not depend on that computational presentation. The first two items are mathematical inputs, not disposable gauges. No combination of rank(V)=12, fiberwise scalarity, or existence of a pure first-order lift supplies them. If a separate global second-order source obstruction is already given, one additionally needs a proved identification with this mixed small-extension problem before applying (9) to it.

## 8a. Essential physical comparison: an End-identification is insufficient

An additional comparison warning is essential: the physical bundle is F_phys=N⊗p*E, with determinant cancelled by the root line N (on a plane, det(E)=O(-1) and N²=p*O(1)). The canonical isomorphism End(F_phys)≅p*End(E) identifies coefficient groups, but tensoring by N does not automatically identify module lifting problems for the same unmodified ambient quantization. Quantizing that line, or transporting through a specified Morita/algebroid equivalence, can change the ambient characteristic class and the module obstruction map.

Consequently an existing physical first-order lift cannot be used to trivialize the naive canonical-bracket torsor T_z of E solely because these End sheaves agree. One first needs the root-line/Morita comparison, its induced ambient algebroid, its scalar compensation, and its coherent action on module descent. Section 4's requirement that the existing lift belong to the same ambient problem is substantive even before mixed order.

At the level of classical Atiyah classes the conditional normalization is precise. If N²≅p*(det E)^(-1), Atiyah additivity gives, after the natural pullback map on differentials,

    At(F_phys)=p*At(E)+id_E⊗At(N)
              =p*(At(E)−(1/2)id_E⊗tr At(E)).

Thus for rank two the relevant normalized class is the tracefree Atiyah class, rather than At(E) without correction. In a curvature representative with even-degree two-form entries, the rank-two Cayley–Hamilton identity says that the square of a traceless representative is scalar. More generally, for a rank-two such representative A,

    (A²)_0=(tr A)A_0.

This explains why a determinant-normalized first-order characteristic expression can have vanishing tracefree part while the unnormalized expression need not. It does not identify the actual quantization characteristic map, prove equality of the two torsors, or evaluate a mixed obstruction. The required comparison must establish how the root line modifies that map and the descent data. Any use of this normalization at quantized module level is conditional on that comparison, not a consequence of the End-cohomology identification alone.

Accordingly the first item in Section 8 must include the correctly transported/root-line-corrected ambient problem when the goal is comparison to the physical lift; the second must include the corresponding transported boundary module. Until those identifications are proved, the torsors in this report are rigorous formal recipients for specified universal-family problems, not an assertion that the physical lift has trivialized the naive torsor of E.

## 9. Exceptional parameters and the limitation of restriction

Everything above is on U. On P²_h\U the stability and cohomology dimensions used to identify Rs_*(A₀⊗K) with V[-1] are not established. Relative cohomology can jump, higher or lower direct-image sheaves can appear, and the relative lift object need not remain a vector-bundle torsor. The appropriate object there is the full relative derived endomorphism complex and its deformation groupoid, not an unproved extension of V.

Even θ_zh=0 on U would not imply global mixed lifting over all parameters. Classes may be supported on the exceptional locus, restriction can have a kernel, scalar compensation may fail an imposed extension requirement, and extending a chosen lift is an additional problem. Block exchange also compares the two fibrations and their good loci; it is not automatically an endomorphism of this one torsor presentation.

## Sources and scope

This formal derivation uses the universal-family cohomology and duality in ../../null-factor-surfaces/relative-surface-0502/COTANGENT_TARGET.md, the intrinsic canonical bracket and conditional scalar-gerbe discussion in ../../null-pair-quotient-bracket/canonical-bracket-0517/RESULT.md, and the fixed-ambient module obstruction, linearization, gauge, and κ formulas in ../../null-module-boundary-audits/module-lifting/RESULT.md. No physical source or jet values are evaluated in this argument. No actual mixed class, global obstruction value, or vanishing of H¹(U,V⊗ω_U) is asserted.
