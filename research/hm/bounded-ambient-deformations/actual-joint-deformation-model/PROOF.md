# An explicit bounded joint Čech model and its exact gerbe comparison

## Result

There is a direct, bounded, coefficient-action-marked joint algebra–module equation model for the actual coarse and corrected algebroids in the accepted inputs. It uses multiplication cochains, overlap cochains, triple units, and free-module transition cochains. It includes the associators, not just local associative algebras. Its normalized mixed module curvature represents **exactly** the complete prescribed-boundary gerbe defect class, with row-left sign and the specified coefficient normalization.

More explicitly, the model supplies an equation

    δx + Λ(c) + B(x_z,x_h) = 0.                         (R)

Here c is the actual mixed ambient correction; x_z,x_h denote the complete joint pure data, including module transitions and coefficient-input operations; Λ is written explicitly below; B is an explicit finite convolution of the two pure data sets. All quantities are cochains, not cohomology classes. For the actual ambient and fixed pure boundary,

    [Λ(c)+B(x_z,x_h)] = o(A,M_boundary)
       in H²(End(E)⊗J).                               (C)

The coefficient of δx is +1. Thus the obstruction is the class of the positive curvature, and the correction solves δx equal to its negative. No factor 1/2 occurs in mixed coefficient extraction.

This resolves the model-comparison dependency by the direct bounded model option. It does **not** assert that the naive Čech–Hochschild totalization is a strict DGLA, identify an unspecified strict DGLA bracket with B, or construct a global bilinear operation on arbitrary characteristic kernels. The conditional strict-DGLA theorem in the earlier proof remains a theorem about such a model when one is chosen. Equation (R) is its now-established concrete bounded replacement for this prescribed problem.

## 1. Inputs and the precise category

Mathematical antecedents:

- ../corrected-mixed-secondary-class/PROOF.md and AUDIT.md;
- antecedent mixed-obstruction-transport / PROOF.md and AUDIT.md;
- antecedent mixed-ambient-rigidity / PROOF.md, especially §§3–4;
- antecedent coarse-quantum-atlas / PROOF.md;
- antecedent external-morita-descent / PROOF.md;
- antecedent retained-obstruction-comparison / PROOF.md.

The previously established source-bound existence, effectiveness, marked transport, and pure-boundary identifications are imported. They are not re-certified here.

Let U be a finite affine refinement on Y that trivializes E, both coefficient lines, and the supplied local algebroid/overlap presentations. Intersections are affine. The corrected base is Y=P²×P², with coefficient layers L=O(-3,0), M=O(0,-3), J=L⊗M. The same construction works in the actual presentation before marked transport.

Write weights 0,z,h,m for (0,0),(1,0),(0,1),(1,1). Weight addition outside this square is zero. Locally the additive presentation is

    V_i = O_i ⊕ L_i ⊕ M_i ⊕ J_i.

Local splittings and coefficient trivializations are auxiliary choices. Their overlap transport is retained in the cochains; a global additive splitting is not asserted. Set N=L⊕M⊕J in these presentations. The intrinsic assertions are N³=0, NJ=JN=0, J²=0, and L·M→J the specified cross pairing. The algebra action on J factors through the ordinary O-action.

Fix the complete pure-boundary algebroid and its finite locally free marked module. In the relative mixed category also fix every multiplication with a positive-coefficient input and every overlap restriction to N, exactly as in mixed-ambient-rigidity §3.2. These fixed operations include their mixed-output portions and must satisfy their own compatibility identities. Only products on two classical inputs, overlaps on classical inputs, and triple units may receive new J-valued ambient corrections. Morphisms fix the indicated markings.

The actual external products supply these data. Merely naming L,M,J would not do so. No free change of the actions on lifted pure ideals is permitted below.

## 2. The complete bounded cochain presentation

In each chart let μ_i:V_i⊗V_i→V_i be a normalized unital multiplication. Let F_ij:V_j→V_i be an invertible normalized overlap map, including coefficient-line transport. Let A_ijk be an invertible element of V_i on triple intersections, with classical reduction 1. Write a⋆b=μ_i(a,b) in chart i.

Impose all four ambient equations, on arbitrary homogeneous inputs, with restriction maps understood:

    (a⋆b)⋆c = a⋆(b⋆c),
    F_ij(a⋆_j b) = F_ij(a)⋆_i F_ij(b),
    F_ij F_jk(a) ⋆ A_ijk = A_ijk ⋆ F_ik(a),
    F_ij(A_jkl) ⋆ A_ijl = A_ijk ⋆ A_ikl.          (A)

The third equation is inverse-free notation for F_ij F_jk=Ad(A_ijk)F_ik. The fourth is the pentagon. Unit and identity-index normalizations are included; one may use ordered indices and recover inverse comparisons.

Use free **left** modules, with vectors written as rows. A semilinear transition is

    v ↦ F_ij(v) ⋆ G_ij,

where F acts componentwise and G_ij is an invertible transition array. Its entries are universal coordinate variables, not any evaluated physical transition matrix. The module equation is precisely

    F_ij(G_jk) ⋆ G_ij = A_ijk ⋆ G_ik.             (M)

The action of A_ijk on the right side is scalar left multiplication on every entry. Keeping its order matters before passage to J. Equation (M) implies the specified coherent module descent, and conversely coherent free-module descent gives (M).

This is a colored cochain model: μ has algebra input/output colors and Čech degree zero; F has overlap degree one; A has overlap degree two; G has module color and overlap degree one. Algebra arities up to three and Čech degrees up to three suffice to state the equations. All weight expansions stop at m. It is an equation model, not a claim that these four lists alone constitute a strict Lie algebra.

### Completeness, including local module operations

For a genuine ambient satisfying (A), the local module is V_i^r with its regular left action. Any finite locally free marked lift is locally isomorphic to this module: lift a boundary frame and use nilpotent invertibility. Thus the free-frame choice loses no local module-action deformation. It replaces local action coordinates by a choice of free frame.

An overlap map between these free modules is exactly a map of the displayed semilinear form. Invertibility is equivalent to invertibility of its classical reduction. The associator condition is exactly (M). Effective descent, supplied by the input atlas, then produces the desired module. Conversely, local frames on any such module produce these coordinates.

For example, changing the local row coordinate by v↦v⋆H_i changes transitions by

    G'_ij = F_ij(H_j)^{-1} ⋆ G_ij ⋆ H_i.          (G)

This follows by substituting v'_i=v_i⋆H_i in the semilinear transition formula. Together with actual algebra-coordinate and overlap-generator changes, these give the coordinate isomorphisms of the model. For a fixed actual ambient with its coherent presentation, the groupoid of these coordinates with frame-change arrows (equivalently, framed objects modulo changes of frame) maps fully faithfully to actual descent objects, since every local module map is determined by images of a free frame, and essentially surjectively by the preceding paragraph. Relative frame changes must induce the identity on the entire boundary. No equivalence with an unspecified simultaneous deformation 2-groupoid is asserted. This verifies equivalence of the presented descent groupoid with the marked lifting groupoid; it is stronger than an equivalence of zero loci.

## 3. Explicit finite convolution, including positive-input terms

Split every variable into its weight-raising components. For homogeneous inputs of weights u,v, μ_i^q means its component with output weight u+v+q. F_ij^q similarly raises input weight by q. Write G_ij^w and A_ijk^a for their weight components. Terms outside the square are zero. The degree-zero coefficient transports are always included in F^0 and μ^0; they are not silently trivialized on intersections.

The component of the module residual in weight d is the following finite expression:

    D^d_ijk =
       Σ_(q+u+v+w=d) μ_i^q(F_ij^u(G_jk^v), G_ij^w)
       − Σ_(q+a+b=d) μ_i^q(A_ijk^a, G_ik^b).    (1)

This formula defines the model's curvature in every retained weight. In particular it specifies all pure cross terms, even when pure coefficients are not central in the full ambient. A correction F^z acting on G^h, or μ^h acting on a z-valued input, is present. Deleting such terms would change this model and would not compute the prescribed problem.

To isolate the mixed forcing, retain exactly those summands of (1) with total weight m and with **no individual index equal to m**. Denote their signed sum by D_cross. This is an explicit finite-index formula, requiring no choice of a bracket, a resolution comparison, or an HKR splitting. It is bilinear in the two lists of pure-weight operations, when those lists range in a compatible fixed linear presentation. For a single fixed external product it is simply a specified cochain. The marking already fixes the positive-input entries of these lists.

Every remaining mixed summand has one index m and all other indices zero. There cannot be three positive indices, since their weight would leave the square. Therefore the displayed separation is exact. It does not discard a higher-order remainder.

Put g_ij=G_ij^0. With the row convention,

    g_jk g_ij = g_ik.

After using classical coefficient transport to place terms in chart i, the part linear in the freely adjustable mixed ambient data c=(μ^m,F^m,A^m) is

    D_ambient(c)_ijk =
       μ_i^m(g_jk,g_ij) + F_ij^m(g_jk) g_ij
       − A_ijk^m g_ik.                         (2)

Normalization removes μ^m(1,g_ik); normalized overlap maps also fix 1. Formula (2) uses the local chart expression of g_jk under F^0, as in (1). In a nontrivial classical chart presentation, insert F^0 in every such occurrence; the intrinsic expression is (1).

The remaining terms are exactly

    D_module(G^m)_ijk =
       g_jk G_ij^m + F_ij^0(G_jk^m) g_ij − G_ik^m. (3)

Here F^0 on the J-coefficient includes the marked transition of J. Equations (1)–(3) explicitly yield

    D^m = D_module + D_ambient + D_cross.         (4)

The actual ambient solves (A), and the given pure data solve (M) in weights z,h. Thus (4) is the only remaining module equation. In particular the word “mixed” here means the full remaining equation, not one selected cross summand.

## 4. The relative cochain complex and the sign

Let F=End(E)⊗J. Define the honest cochain complex

    k^p = Čech^p(U,F),       differential δ.

The coefficient system is the actual classical row-frame system with the specified J transitions. Write G_ij^m=g_ij x_ij, where x is a section of F in the source row convention. Dividing (3) on the left by g_ik gives exactly

    (δx)_ijk = x_ij + g_ij^{-1} x_jk g_ij − x_ik,   (5)

with coefficient transports implicit in the middle term. This is ordinary Čech differential in these frames, not an ungraded commutator convention.

Define the normalized linear and bilinear terms

    Λ(c)_ijk = g_ik^{-1} D_ambient(c)_ijk,
    B(x_z,x_h)_ijk = g_ik^{-1} D_cross,ijk.         (6)

Equations (4)–(6) prove (R) literally. The sign of the triple-unit contribution in Λ is −A^m Id. This matches the imported pure convention in which the source triple-unit coordinate contributes −b Id. Notice that the multiplication and overlap contributions have positive signs in the module residual. Arbitrarily replacing the ambient totalization's triple coordinate by its negative would require changing its identification with A^m as well.

For comparison of module solutions at fixed ambient, (G) with H_i=1+h_i, h_i in F, gives

    x'_ij = x_ij + h_i − g_ij^{-1}h_j g_ij.

With the ordinary Čech convention δh=g_ij^{-1}h_j g_ij−h_i, this is x'=x−δh. The harmless sign on gauge parameters does not change (5) or the obstruction sign. Relative automorphisms are H⁰(k), and, if solutions exist, their isomorphism classes form an H¹(k)-torsor. Obstructions belong to H²(k).

Because E is locally free and the cover is affine-acyclic,

    H^p(k)=H^p(Y,End(E)⊗J)=Ext^p(E,E⊗J).

This computes the actual relative kernel cohomology; no assertion about Ext over global sections is used.

## 4A. Explicit joint linear differential and its gauge identity

Here is a linear complex through equation degree, rather than only the module part of its derivative. Use a classical chart presentation with F⁰=id and A⁰=1, retaining all E and coefficient transitions as above. For any one coefficient weight Q, joint variables have the space

    V¹_Q = (Čech⁰ C²(O,Q) ⊕ Čech¹ C¹(O,Q)
             ⊕ Čech² Q) ⊕ Čech¹(End(E)⊗Q).

The first three entries are (μ,f,a), and the last is x. Positive-arity cochains are normalized; the allowed differential-cochain condition is inherited from the ambient. The equation space is

    V²_Q = (Čech⁰ C³ ⊕ Čech¹ C² ⊕ Čech² C¹
             ⊕ Čech³ C⁰) ⊕ Čech²(End(E)⊗Q).

Writing b for the ordinary Hochschild differential and δ for Čech differential with its specified coefficients, the derivative is

    d¹(μ,f,a;x) =
       (bμ, δμ−bf, δf+ba, δa ; δx+Λ_Q(μ,f,a)).    (8)

Here Λ_Q is exactly (2),(6) with weight Q instead of m. Choose the associativity residual as right-associated minus left-associated to obtain bμ; the other ambient residual signs are those in (A). This choice affects no module-residual sign. Formula (8) follows by expanding each displayed equation once. It does not require local Hochschild module-action coordinates, since those have been removed by free framing, as proved in §2.

Joint degree-zero gauge parameters are

    V⁰_Q = Čech⁰ C¹(O,Q) ⊕ Čech¹ Q
             ⊕ Čech⁰(End(E)⊗Q),

written (e,b_edge,h). To avoid confusion, b_edge denotes the edge unit coordinate, whereas b above is Hochschild differential. Their differential is

    d⁰(e,b_edge,h) =
       (b e, δe, δb_edge ; ξ−δh),
    ξ_ij = g_ij⁻¹(b_edge,ij g_ij − e_i(g_ij)).       (9)

An algebra cochain e acts entrywise on g. The coefficient Q is a symmetric classical bimodule, so b:C⁰(O,Q)→C¹(O,Q) is zero; this is why the edge unit has no extra inner-derivation term in δe in (9). These formulas are the derivatives of actual changes of coordinates. In full nonlinear notation, with chart maps E_i, edge units B_ij, and initially no module frame change, they are

    μ'_i(a,b)=E_i⁻¹(μ_i(E_i a,E_i b)),
    F'_ij=E_i⁻¹ Ad(B_ij) F_ij E_j,
    A'_ijk=E_i⁻¹(B_ij⋆F_ij(B_jk)⋆A_ijk⋆B_ik⁻¹),
    G'_ij=E_i⁻¹(B_ij⋆G_ij).                       (10)

Apply (G) afterwards for module frames H_i. Direct substitution in (A),(M) shows that (10) and (G) preserve every solution. Since the classical point is a solution, differentiation proves d¹d⁰=0, including the nontrivial identity

    δξ + Λ_Q(b e,δe,δb_edge)=0.                   (11)

Alternatively (11) follows entrywise from the product rule defining b e and g_jk g_ij=g_ik. Thus (8)–(9) are an actual joint cochain complex through the needed variable/equation degrees. It is not claimed to be a full Hochschild quasi-isomorphic resolution in all degrees. The relative module portion continues with its ordinary Čech differential in every degree; the quadruple calculation below supplies the required closure identity for its mixed curvature when ambient equations vanish.

Finally, the polarized second differential of these same polynomial equations is obtained by selecting precisely two nonzero pure weights in their substitution expansion. For the module equation it is exactly D_cross of (1), followed by normalization by g_ik. For the ambient equations it is obtained by the identical finite weight-selection rule applied to the four explicitly displayed expressions (A). Therefore the mixed equation vector is the linear differential (8) of the mixed correction plus this polarized second differential of the pure data. This is an explicit algorithm on finite index sets of weights and arities, rather than an assumed bracket. Terms involving three positive weights vanish, and even parameters give the mixed coefficient once, with no factorial. Its module component is (R).

## 5. Proof that the curvature is the complete gerbe class

Choose the proposed full transitions with G^m=0 in the selected additive coordinates. This is allowed: it is just a lift of the fixed boundary transitions. Their classical parts are invertible, so they are invertible in the nilpotent ambient. The local modules are the genuine free modules over the **actual** ambient. They exist independently of any solution to the mixed descent equation.

Set

    L_ijk=F_ij(G_jk)⋆G_ij,
    W_ijk=A_ijk⋆G_ik,
    D_ijk=L_ijk−W_ijk.

The boundary equation implies D lies in J. The row-coordinate automorphism comparing the composite and the required transition is exactly

    W_ijk^{-1}⋆L_ijk
       =1+W_ijk^{-1}⋆D_ijk
       =1+g_ik^{-1}D_ijk.                       (7)

The last equality is exact: every positive coefficient annihilates J. By (4)–(6), the additive coefficient in (7), for the chosen G^m=0, is

    R=Λ(c)+B(x_z,x_h).

The ratio in (7) is the relative triple automorphism defining the banded lifting gerbe in mixed-obstruction-transport §2, in precisely its row-left convention. Thus this is equality of representatives under the supplied band identification, before passing to cohomology.

For completeness, cocycle closure does not require assuming module descent. On a quadruple intersection, compare the composite of three proposed semilinear transitions in its two parenthesizations. Using overlap multiplicativity, the third equation of (A) moves the intermediate associator through the transported transition. The two remaining scalar factors are respectively

    F_ij(A_jkl)⋆A_ijl    and    A_ijk⋆A_ikl.

They agree by the fourth equation of (A). The only remaining factors are the four transported triple failures. Each is 1 plus a J-valued relative endomorphism; any product of two corrections is zero. The resulting identity is the alternating Čech sum δR=0. The transport of these endomorphisms is the classical transport of End(E)⊗J because NJ=0. This also proves that omitting the associator or its pentagon is not a valid replacement model.

Changing G^m by g x changes R by δx, by the explicit calculation (5). Hence a solution exists exactly when [R]=0. Changing frames, preliminary lifts, or an acyclic refinement changes its representative by a band-compatible coboundary, equivalently by the fully faithful descent identification of §2. Consequently (C) follows as equality of cohomology classes, not merely equivalence of vanishing.

## 5A. Exact specialization to the complete ten-term source

For this paragraph only, import the accepted bounded source presentation in antecedent mixed-obstruction-ks-centralizer / dependencies/FIRST-LIFT-STRUCTURAL.md §7, the complementary-support premise proved under the stated source denotations in antecedent pure-deck-structure / inputs/raw-second-order-closure.md §5, and the same-class bridge in antecedent retained-obstruction-comparison / INTEGRATION-COROLLARY.md. This is a static symbolic specialization; no physical operation is evaluated.

In that presentation the bounded transition equation has F=id, multiplication μ⁰+sμ_p+tμ_q+stμ_pq, triple unit

    A=1+s b_p+t b_q+st b_p b_q,

and proposed transitions G=g+s U_p+t U_q. The imported complementary-factor support gives

    μ_p(b_q,f)=μ_q(b_p,f)=0

for every input f, and the analogous identities when the scalar occupies the second slot. Therefore A⋆G=A G in this bounded quotient: a same-axis correction is killed by s² or t², and a cross-axis correction differentiates an unrelated coefficient. This is a bounded weighted statement; it does not assert that the unweighted scalars are central for the unrestricted star product.

Substitution in the universal convolution (1) gives exactly

    D^m = U_p,jk U_q,ij + U_q,jk U_p,ij
       + μ_p(U_q,jk,g_ij) + μ_q(U_p,jk,g_ij)
       + μ_p(g_jk,U_q,ij) + μ_q(g_jk,U_p,ij)
       + μ_pq(g_jk,g_ij)
       − b_p U_q,ik − b_q U_p,ik − b_p b_q g_ik.   (12)

These are all ten terms of the structural source's (7.2), in the same order and with the same signs. In particular the mixed ambient contribution includes μ_pq and −b_p b_q g; it is not only the product of the two module corrections. Left multiplication by g_ik⁻¹ is exactly its normalized full M. Equation (7) therefore identifies this complete source representative with the model curvature, subject to the explicitly imported same-source premises.

Without the support premise, the generic convolution also contains the potentially nonzero terms −μ_p(b_q,g_ik)−μ_q(b_p,g_ik); without the displayed F=id presentation, it also contains overlap corrections. Neither can be suppressed merely because b_p,b_q are ordinary scalar Čech cocycles. The universal model deliberately retains them.

The already established scalar-elimination identity R_raw=tf(M)+δW and vanishing of the descended scalar recipient identify its class with the complete End-valued class, as detailed in the cited integration corollary. No source detector or isolated ten-term summand is being substituted for the complete curvature here.

## 6. Boundary restriction, ambient dependence, and transport

Every mixed variable in §§3–5 lies in J. It vanishes in A/J, so the entire specified pure module, including both axis markings and their identified classical reduction, remains fixed. No replacement by a different module with the same classical E is hidden in (R).

At fixed coefficient actions, changing the mixed ambient correction from c to c+e changes R by the explicit cochain Λ(e), if both ambients satisfy (A) and the same preliminary boundary coordinates are used. It follows from §5 that Λ(e) is closed in this situation. This is the bounded characteristic variation, with its actual triple-unit sign. An arbitrary ambient cochain not satisfying the linearized ambient equations is not asserted to have closed image. In particular this argument does not falsely declare Λ to be a chain map from only its degree-two formula.

It is important that c itself generally solves an **inhomogeneous** ambient equation. Applying the same finite weight expansion to (A) gives

    d_ambient c + P_ambient(x_z,x_h)=0.

Only the difference e between two genuine mixed ambient extensions is a cocycle. The vanishing HH²(Y,J)=0 concerns these closed differences and does not imply that the actual c may be set to zero in the chosen coordinates. Doing so need not preserve (A). Correspondingly, only δ(Λ(c)+B)=0 has been proved; B alone need not be a cocycle, and Λ(c) cannot be discarded. Changing ambient coordinates can redistribute terms between Λ(c) and B, but the full curvature and its marked class transform together. This is a concrete obstruction to using mixed ambient rigidity as a mixed module vanishing argument.

More generally, transporting all variables by an actual marked coherent algebra/Morita equivalence transports the local free modules and every comparison used in (7). Its map on relative automorphisms is the classical End marking tensored with the coefficient marking. Therefore the class produced by this explicit model is carried to the class produced by the target model by exactly that band map.

For the accepted actual-to-corrected transport, this is the map Ψ of mixed-obstruction-transport: cancel the root in End, then descend with normalized coefficient trace

    st f ↦ (1/64) Tr_p(f Ω₁₂∧Ω₃₄).

It acts entrywise on coefficients, not by taking an endomorphism trace. Thus the present curvature is the same full actual class under Ψ, including the normalization and sign already established there. Rescaling the pure coefficient markings by a,b rescales the mixed coordinate class by ab. Ordinary even coefficient weights and the product marking introduce no mixed factorial or exchange sign.

## 7. What has been resolved, and what remains

The earlier conditional secondary formula lacked an actual joint-model comparison. The present finite convolution model resolves that specific dependency for the bounded prescribed-boundary problem:

1. The algebra and module variables and every ambient coherence equation are specified.
2. Coefficient-input markings and their mixed contributions are retained.
3. Free-frame descent gives equivalence with the actual locally free module lifting groupoid.
4. The complete mixed forcing is a concrete cochain Λ(c)+B, with relative correction differential exactly δ.
5. Its ratio is literally the gerbe cocycle, so its class, normalization, and sign are proven.

This is not merely naming a general deformation theory or reusing equality of zero loci. Formula (1) is an explicit finite construction of the nonlinear cross term from the complete presentation, and (2)–(7) supply the comparison.

It does not compute this cochain on the physical carrier, decide whether its class vanishes, supply a primitive, certify any detector, or identify the cross term with an ordinary Yoneda product. Pure rigidity only removes permissible pure-lift ambiguity; it does not remove B. A strict-DGLA realization with all the cohomology identifications of the earlier conditional theorem would require an additional rectification/comparison and is not claimed. No such assertion is needed for (R) or (C).
