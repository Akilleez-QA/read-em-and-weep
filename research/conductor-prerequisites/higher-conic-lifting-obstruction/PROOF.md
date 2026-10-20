# Higher maximal-line obstructions on a fixed plane conic

## Statement and scope

Work over C. Fix a smooth conic C in W=P², write X_n=nC, and let all degrees on C be P¹ degrees. A plane twist is explicitly marked. Fix even d≥8, a=(d−4)/2, b=(−d−4)/2, and D_n=O_{X_n}(−2 plane). Let F_n have rank two, determinant D_n and reduction O_C(a)⊕O_C(b). The intrinsic maximal line in F_1 is A_1=O_C(a).

The audited first-order theorem says ε=0 precisely when F_2 splits, equivalently when A_1 lifts to X_2. It does not identify the split factors with fixed reference factors.

For every m≥1 and every line subbundle A_m⊂F_m lifting A_1, the obstruction to extending A_m inside a prescribed extension F_{m+1} is

    ob_m(F_{m+1},A_m) ∈ H¹(C,O_C(−d−4m)).                 (1)

It vanishes exactly when such a line subbundle exists; if it exists, it is unique as an embedded subbundle. This obstruction group has dimension d+4m−1, and is dual to H⁰(O_C(d+4m−2)). In particular, the next obstruction after ε=0 is in H¹(O_C(−d−8)), of dimension d+7. It is additional data, not the first-order catalecticant parameter.

We construct a universal determinant-correct family on the actual X_3 whose X_2 reduction is the fixed split reference (so ε=0), with (1) equal to its freely varying nonzero parameter at m=2. Consequently first-order vanishing cannot imply splitting on X_3 or on all higher neighborhoods. These models are not asserted to be actual HM restrictions. We assert neither that they are globally algebraizable nor that they are nonalgebraizable; global realization is a separate question not settled by this local construction.

## 1. The actual square-zero layers

Let I=I_C=O_W(−2 plane). The immersion X_m⊂X_{m+1} has ideal

    J_m=I^m/I^{m+1}=O_C(−2m plane)=O_C(−4m).

Its square is zero because 2m≥m+1, and I annihilates J_m. Thus any tensor with J_m uses only reduction to C. No retraction X_n→C is used. Confusing J_m with O_C(−4) at every stage loses the essential order dependence.

Local lifts of a line subbundle exist: lift its primitive local generator in a local trivialization of F_{m+1}; a component that is a unit remains a unit across a nilpotent ideal. The quotient is locally free. Differences between two local graph lifts take values in

    J_m⊗Hom(A_1,F_1/A_1)=O_C(−d−4m).

On overlaps these differences form a Čech 1-cocycle; changing graphs adds a coboundary. This proves (1), its necessity and sufficiency. When its class is zero, global lifts form a torsor under H⁰(O_C(−d−4m)), which vanishes. This proves uniqueness. It is uniqueness of the embedded line in the prescribed bundle, not uniqueness of a complement, of abstract Picard lifts, or of an identification of the line with a reference.

Inductively there is at most one line subbundle of F_n reducing to A_1. Every direct-sum decomposition of F_n into lines would contain that line: its reduction must have summand degrees a,b by uniqueness of the splitting type on P¹, and the degree-a summand equals A_1.

### Variation with the prescribed next bundle

For fixed (F_m,A_m) as above, with its determinant identification, determinant-fixed extensions to X_{m+1}, framed by an identification on X_m, form a torsor under

    H¹(J_m⊗End₀(F_1))
      = H¹(O_C(d−4m)) ⊕ H¹(O_C(−4m)) ⊕ H¹(O_C(−d−4m)).

They exist since their local descent obstruction is in H²(J_m⊗End₀(F_1))=0. Relative to any chosen extension, changing its class by u changes ob_m by the image of u under the canonical projection

    End₀(F_1) → Hom(A_1,F_1/A_1),

up to the common Čech sign. After choosing the displayed splitting of F_1, this is exactly the negative-root coordinate. In particular this affine obstruction map is surjective. Its zero fiber is an affine torsor with positive-root and diagonal directions; it does not canonically set either direction to zero. This remains true for nonreference F_m and makes precise the new information required about an actual prescribed F_{m+1}. The obstruction itself is canonical, while coordinates on the bundle-extension torsor require a reference and framing.

## 2. Picard lifts and determinant-correct references

For every n, H⁰(O_{X_n})=C. Indeed use the successive exact sequences with kernels O_C(−4m), whose H⁰ vanishes. Global units therefore lift, and the units sequence gives

    0 → H¹(O_C(−4m)) → Pic(X_{m+1}) → Pic(X_m) → 0.       (2)

Surjectivity follows from H²(C,O_C(−4m))=0. The kernel has dimension 4m−1. In particular abstract line lifts exist but are not canonically specified by reduction. The kernel is an additive complex vector group and multiplication by two is invertible on it.

Put L_n=O_{X_n}(d/2 plane). Choose compatible A_n^0 with

    (A_n^0)² ≅ L_n D_n,
    Q_n^0=D_n(A_n^0)⁻¹,   F_n^0=A_n^0⊕Q_n^0.             (3)

Start with A_1^0=O_C(a). Given a root at level m, lift it using (2) and correct the square discrepancy by half its kernel class. This constructs (3) inductively, with compatible root identifications if desired. The resulting references exist on the actual nonsplit plane thickenings, including when a or b is odd and cannot be a plane line-bundle degree. Their ratio Hom(Q_n^0,A_n^0) is L_n and their determinant is D_n.

The X_2 reference has ε=0 by the audited theorem (or by lifting its positive-root sections from P²). General split factors on X_2 need not equal these factors: diagonal Picard parameters remain invisible to ε when d≥8.

## 3. A universal third-neighborhood countermodel

Fix the reference (3) on X_3 and let

    V=H¹(C,O_C(−d−8)),   S=Spec Sym(V*).

Choose a basis of V and Čech cocycle representatives on a fixed affine cover, and let e_univ be their linear combination with the universal coordinate functions of S. It represents the tautological section of V⊗O_S. Modify the transitions of F_3^0 over X_3×S by the automorphisms

    1+u_ij,   u_ij=e_univ,ij E_−,
    u_ij ∈ J_2⊗Hom(A_1^0,Q_1^0).

The coefficient twisting is exactly −8−d. Products of any two kernel coefficients vanish in J_2², so the additive Čech cocycle condition is precisely the transition cocycle condition. Also tr u=0 and det(1+u)=1. These transitions define a locally free rank-two family F_3 with determinant D_3 and a specified identification

    F_3|_{X_2×S} ≅ F_2^0×S.

Its first-order connecting map is therefore zero identically. The obstruction to lifting the unique embedded A_2^0 is e_univ, by the graph computation. On S\{0}, every geometric fiber has nonzero obstruction. Hence no such fiber splits into two line bundles on X_3. At the zero parameter the reference splits. No parameter value or selected HM rank instance has been evaluated.

More generally, at every m one can perform the same pure lower-root deformation of F_{m+1}^0 by a universal parameter in H¹(O_C(−d−4m)), leaving F_m^0 unchanged. Thus no finite collection of vanishing earlier line obstructions forces the next one to vanish using this local package alone.

These are algebraic bundles on the finite scheme X_3, constructed with formal symbolic parameters. If “formal bundle” means a compatible system on the entire formal completion, any individual fiber also admits compatible determinant-fixed bundle extensions: local lifts across each square-zero layer have their gluing obstruction in H²(J_m⊗End₀(F_1)), which is zero on C. One corrects local cocycles and iterates. This extension of the bundle does not extend its obstructed maximal line. This existence statement supplies no global algebraic bundle on W and no HM realization.

## 4. Once the line exists: the separate extension obstruction

Suppose A_n⊂F_n exists, and put Q_n=F_n/A_n and R_n=Hom(Q_n,A_n)=A_n²D_n⁻¹. The exact sequence

    0 → A_n → F_n → Q_n → 0

has class ξ_n∈Ext¹(Q_n,A_n)=H¹(X_n,R_n). It splits precisely when ξ_n=0. A splitting complement, when it exists, is a torsor under H⁰(X_n,R_n); it is not generally unique. Here R_n|C=O_C(d).

For a compatible line A_{m+1}, restriction gives the exact sheaf sequence

    0 → O_C(d−4m) → R_{m+1} → R_m → 0.                  (4)

The resulting exact cohomology sequence ends as

    0 → H⁰(O_C(d−4m)) → H⁰(R_{m+1}) → H⁰(R_m)
      →[δ_m] H¹(O_C(d−4m)) → H¹(R_{m+1})
      → H¹(R_m) → 0.                                  (5)

Moreover ξ_{m+1} maps to ξ_m. If F_m is split, the class ξ_{m+1} therefore belongs to the kernel

    ker[H¹(R_{m+1})→H¹(R_m)]
      ≅ H¹(O_C(d−4m))/im δ_m.                           (6)

Thus the positive new-layer group controls the splitting obstruction, but in general the obstruction is in its quotient (6). Choices of a splitting below alter a representative through δ_m. Omitting this quotient incorrectly erases lower-level ambiguity.

The exact group dimension and vanishing threshold are

    h¹(O_C(d−4m))=max(4m−d−1,0),
    H¹(O_C(d−4m))=0 iff d≥4m−1.                         (7)

For the even d under consideration, the threshold is d≥4m. Under this condition, IF F_m is split and the maximal line lifts to X_{m+1}, then F_{m+1} splits. If F_m is not split, vanishing of the new-layer group cannot remove its inherited nonzero extension class.

Starting with the automatic splitting on C, a maximal-line lift all the way to X_n forces splitting for every bundle in this package whenever

    d≥4(n−1)−1, equivalently for even d, d≥4n−4.          (8)

Indeed every positive-layer H¹ through n vanishes, and (5) inductively gives H¹(R_n)=0, regardless of the Picard choices. For even d the last guaranteed level is n=floor(d/4)+1. In particular d≥8 suffices at X_3: there a successful maximal-line lift forces splitting, although its existence is not forced by ε=0.

Conditions (7) and (8) are sharp as universal guarantees, not necessary conditions for an individual bundle to split. To verify sharpness, use the reference ratio R_{m+1}=L_{m+1}. Every section of L_m lifts from P², by

    0 → O_{P²}(d/2−2m) → O_{P²}(d/2) → L_m → 0

and H¹(P²,O(k))=0 for all k. Thus δ_m=0 for this reference ratio. If 4m−d−1>0, a universal nonzero class in H¹(O_C(d−4m)) gives a pure upper-root square-zero deformation of F_{m+1}^0. It preserves the line A_{m+1}^0 and the determinant, restricts to the split F_m^0, and has nonzero extension class by (5). The resulting F_{m+1} cannot split by some different decomposition either: any decomposition would split the sequence for its unique maximal line. This proves that, beyond the threshold, line lifting alone does not universally imply splitting. The same construction with m=n−1 proves sharpness of (8).

## 5. What the first-order criterion does and does not establish

For a prescribed compatible system F_n, ε=0 establishes a unique A_2 and splitting of F_2. The next dependency is to determine ob_2(F_3,A_2). Its vanishing determines whether there is A_3; for d≥8 it also forces splitting on X_3. Subsequently each ob_m is defined only after the previous embedded line has actually lifted. Once the uniform positive vanishing range ends, one must in addition track ξ_m through (5), or determine the precise quotient (6). The negative-root ob_m, the diagonal Picard choices (2), and the positive extension ξ_m are distinct pieces of data.

The family in §3 disproves any implication from first-order ε=0 to splitting on every higher neighborhood, including in the fixed nonsplit ambient plane geometry with the correct determinant. It also disproves identifying first-order zero with vanishing of the next negative-root class. A nonzero ob_2 prevents a global splitting whose restriction would lift A_1; restriction of any such splitting would contradict (1).

This is not a counterexample to global algebraizability of the underlying nonsplit bundle. A global nonsplit vector bundle may have an obstructed maximal conic line. Conversely, a compatible formal bundle does not come with a demonstrated algebraization merely because each finite lifting obstruction for the bundle vanishes. We make no assertion about a general formal algebraization theorem here. Any claim of realization on W with specified Chern classes, or as an actual HM restriction, needs additional global input establishing precisely that claim. In particular the universal local countermodels cannot be substituted for the actual HM F_3, and no conclusion about its actual ob_2 or any retained source follows.

## Dependencies and restrictions

Read ../ribbon-catalecticant-classification/PROOF.md and AUDIT.md, and ../ribbon-duality-constraints/PROOF.md. The derivation uses only square-zero descent, line-bundle cohomology, extension classes, and exact sequences on the fixed conic thickenings. No actual HM source or selected rank is evaluated.
