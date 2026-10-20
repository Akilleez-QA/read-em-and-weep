> Historical mathematical review retained with the source. This is not a new independent review or a formal verification certificate.

# Independent audit: higher maximal-line obstructions on a fixed conic

## Verdict

The proof passes independent review under its stated hypotheses. No substantive correction to its obstruction groups, determinant-correct constructions, splitting thresholds, or scope is required.

The decisive distinction is correctly maintained throughout: lifting the intrinsic maximal line is controlled by a negative-degree group, while splitting a bundle after that line exists is controlled by a different, positive-degree extension group. At a new layer the latter obstruction generally belongs to a quotient, not to the entire positive-degree group. The proof includes that quotient and proves sharpness using references for which its denominator vanishes.

The constructed third-neighborhood family is a valid family on the actual scheme 3C in P². Its reduction on 2C is the fixed split reference, and its nonzero parameters obstruct lifting the unique maximal line. The argument establishes neither actual HM realization nor global algebraizability or nonalgebraizability. Its compatible formal extension statement concerns the bundle alone and is correct.

Read directly: this directory's PROOF.md; ../ribbon-catalecticant-classification/PROOF.md and AUDIT.md; and ../ribbon-duality-constraints/PROOF.md. The audit uses only the stated geometry, square-zero descent, line-bundle cohomology, and exact sequences. No selected HM instance, actual source, retained class, or rank is evaluated.

## 1. The square-zero layer really depends on its order

For I=O_{P²}(−2 plane), the immersion X_m=mC into X_{m+1}=(m+1)C has ideal

    J_m=I^m/I^{m+1}=O_C(−2m plane)=O_C(−4m).

The conversion to P¹ degree contributes the second factor of two. Multiplication by I kills this ideal, so a tensor with J_m depends only on the reduction of the other factor to C. Its square vanishes because 2m≥m+1 for m≥1. Thus all uses of square-zero descent in the proof apply to these actual plane thickenings; none requires a retraction to C or a split structure sheaf.

In particular, the second new layer is O_C(−8), not another copy of O_C(−4). The obstruction at that stage is consequently not another occurrence of the first-order negative-root parameter.

## 2. The line obstruction, its completeness, and embedded uniqueness

Fix a subbundle A_m⊂F_m whose reduction is A_1. Locally, choose a generator of A_m and lift it to F_{m+1}. A coordinate of the generator that is a unit remains a unit after lifting across the nilpotent ideal. The resulting line is a direct summand locally, with locally free quotient. Therefore there is no local obstruction of a different kind hidden by the cohomology calculation.

Two such local lifts differ, modulo changes within the line, by a graph in

    J_m⊗Hom(A_1,F_1/A_1).

Here deg(F_1/A_1)−deg(A_1)=b−a=−d. The sheaf of graph differences is therefore O_C(−d−4m). Its overlap differences are a Čech cocycle; changing local graph lifts changes that cocycle by a coboundary. This gives the complete obstruction

    ob_m(F_{m+1},A_m)∈H¹(O_C(−d−4m)).

Its vanishing is both necessary and sufficient. When it vanishes, the set of global embedded lifts is a torsor under H⁰ of the same sheaf. That group is zero. This proves uniqueness of the embedded lift and, inductively, uniqueness at every level if a lift exists.

The numerical and duality statements follow directly from cohomology on P¹:

    h¹(O_C(−d−4m))=d+4m−1,
    H¹(O_C(−d−4m))=H⁰(O_C(d+4m−2))*.

At m=2 these become dimension d+7 and dual degree d+6. The asserted equality with a deformation parameter uses one consistent Čech sign convention, which can be fixed when choosing the cocycle representatives.

Every decomposition of F_n into two line bundles reduces to a decomposition of F_1 with degrees a and b. The degree-a summand is the intrinsic A_1, since a>b and Hom(O_C(a),O_C(b)) has no global sections. Thus every such decomposition would supply the unique maximal-line lift. This validates the later deductions that a nonzero negative obstruction prevents any decomposition, rather than merely the chosen reference decomposition.

This uniqueness does not concern a complement, an abstract line-bundle lift, or a chosen isomorphism to a reference line. Those distinctions are properly stated in the proof.

### Variation as the next bundle changes

The added variation subsection is also correct. Fix F_m with its determinant identification and, for the line-obstruction statement, the existing A_m under discussion. Isomorphism classes of determinant-fixed lifts framed on X_m form a torsor under

    H¹(J_m⊗End₀(F_1)).

The kernel automorphisms of a lift are exactly 1+u with u in J_m⊗End₀(F_1), and their multiplication and gauge changes are additive. Their descent obstruction is in H² of this sheaf and vanishes. Framing is essential here: automorphisms of the preceding bundle are not additionally quotiented out.

Changing the bundle cocycle by u changes the graph-lifting cocycle by its image under the intrinsic map

    End₀(F_1)→Hom(A_1,F_1/A_1),

again with the common sign convention. After choosing a complement of A_1 in F_1, this map is the lower-root projection from O_C(d)⊕O_C⊕O_C(−d). Tensoring by J_m and taking H¹ shows directly that the variation map is surjective. The affine obstruction map therefore has a nonempty zero fiber, a torsor for the kernel of this projection on H¹. In the chosen splitting those directions are H¹(O_C(d−4m)) and H¹(O_C(−4m)). The existence of a zero fiber does not designate an origin or eliminate either direction.

This argument applies to nonreference F_m as well. The premise that A_m already exists is necessary for ob_m(F_{m+1},A_m) to be defined. The revised subsection explicitly fixes the pair (F_m,A_m), making this premise unambiguous. No claim is made that every F_m carries such a line.

## 3. Picard ambiguity and compatible determinant-correct references

The exact sequence of structure sheaves at each stage has kernel J_m with no global sections. Inductively H⁰(O_{X_n}) embeds into H⁰(O_C)=C, while constants already supply all of C. Hence H⁰(O_{X_n})=C and every global unit lifts across every layer.

The units sequence 1→1+J_m→O*_{X_{m+1}}→O*_{X_m}→1, together with 1+J_m≅J_m additively, therefore gives precisely

    0→H¹(O_C(−4m))→Pic(X_{m+1})→Pic(X_m)→0.

There is no further quotient caused by nonlifting global units, and surjectivity follows from H²(C,J_m)=0. The kernel has dimension 4m−1, with multiplication by two invertible over C.

For L_n=O_{X_n}(d/2 plane) and D_n=O_{X_n}(−2 plane), the restriction degree of L_nD_n is d−4. The proposed initial root has degree (d−4)/2. At each subsequent layer, lift the preceding root, compare its square to L_{m+1}D_{m+1}, and correct by half the discrepancy in the Picard kernel. This proves existence of compatible roots A_n^0 on the specified thickenings. The root identifications can be made compatible as well: any scalar discrepancy of their restrictions lifts as a scalar and can be corrected.

With Q_n^0=D_n(A_n^0)^{-1}, both identities required later hold:

    det(A_n^0⊕Q_n^0)=D_n,
    Hom(Q_n^0,A_n^0)=(A_n^0)²D_n^{-1}=L_n.

The construction remains valid when the restriction degrees of A_n^0 and Q_n^0 are odd. No nonexistent plane half-twist is introduced. General line lifts still carry Picard ambiguity; choosing this special square-root reference does not erase that ambiguity for arbitrary split bundles. The first-order criterion for d≥8 does not identify their factors with these references.

## 4. The universal family on 3C

After fixing the split reference on X_3, the sheaf of lower-root kernel automorphisms is

    J_2⊗Hom(A_1^0,Q_1^0)=O_C(−d−8).

Choose cocycle representatives of a basis of its H¹ and multiply them by the coordinates of the affine parameter space V. This gives the tautological cocycle after base change. The additive cocycle equation is the correct equation in this twisted sheaf, with its gluing inherited from the reference bundle; it does not assume that the reference transitions are globally constant.

Multiplying the reference transitions by 1+u_ij is legitimate because all products of two J_2-valued terms vanish. In rank two,

    det(1+u_ij)=1+tr(u_ij)=1,

since the quadratic determinant term is zero and the lower-root term is tracefree. Thus the family has the specified determinant. Every modification is zero on X_2, so it also has the stated fixed identification there.

The maximal line on this X_2 reduction is the unique A_2^0. Its graph-lifting obstruction is exactly the tautological class, up to the fixed sign convention. Every nonzero geometric parameter therefore prevents a line lift and hence prevents any splitting on X_3. At zero the reference splits. The first-order connecting map is zero throughout because the X_2 bundle is fixed and split, in the range d≥8 where the audited first-order theorem applies.

The identical construction with J_m works at every order, leaving the entire previous neighborhood fixed and split. Accordingly, vanishing of any finite sequence of earlier line obstructions does not force the next one to vanish within this local package. These are symbolic families; no selected value or actual HM rank is needed.

## 5. Extending the bundle formally does not extend the line

The compatible formal extension assertion is correct. Starting with a determinant-identified F_m, choose local free lifts and local determinant identifications compatible with D_{m+1}. Lift the transition matrices and correct their determinants locally. The defect of their cocycle equation then has values in

    J_m⊗End₀(F_1).

The obstruction to removing this defect lies in H² of this coherent sheaf on C, and that group is zero. Corrections give a determinant-fixed F_{m+1} with a specified reduction isomorphism. Iterating produces a compatible system, which is the asserted meaning of a bundle on the formal completion.

This lifting problem has no requirement to preserve the maximal line. Its unobstructedness is therefore fully consistent with a nonzero H¹ obstruction to lifting that line already from X_2 to X_3. Any extension of the bundle to later neighborhoods retains the same restriction to X_3 and cannot repair that failed line lift.

The proof does not replace this formal compatible-system argument by a global algebraization claim. Whether a chosen system or finite neighborhood bundle is realized by an algebraic bundle on W, with particular Chern classes or HM origin, is left open exactly as it should be.

## 6. Once the line exists, the extension obstruction is different

If A_n⊂F_n exists, the quotient Q_n is invertible, so

    Ext¹(Q_n,A_n)=H¹(X_n,A_nQ_n^{-1})=H¹(X_n,R_n).

The resulting class ξ_n vanishes exactly when the exact sequence splits. Its splitting complements form a torsor under H⁰(X_n,R_n), which can be nonzero. This is compatible with uniqueness of the embedded maximal line.

For compatible lines at successive levels, R_{m+1} restricts to R_m and has reduction O_C(d). Tensoring the square-zero structure sequence by R_{m+1} gives

    0→O_C(d−4m)→R_{m+1}→R_m→0.

There are no omitted Tor terms because R_{m+1} is invertible. The cohomology sequence in the proof is correct and ends in zero because H²(C,O_C(d−4m))=0. In particular,

    ker[H¹(R_{m+1})→H¹(R_m)]
      ≅H¹(O_C(d−4m))/im δ_m.

Restriction sends ξ_{m+1} to ξ_m. When the preceding sequence is split, ξ_{m+1} is thus an element of this quotient. Different choices of splitting below account for the image of δ_m. Treating a chosen representative in H¹(O_C(d−4m)) as an absolute obstruction would incorrectly disregard this ambiguity; the proof avoids that mistake.

## 7. Vanishing ranges and their sharpness

On P¹,

    h¹(O_C(d−4m))=max(4m−d−1,0).

It vanishes exactly for d≥4m−1, or d≥4m in the stated even-degree range. If F_m is split and the maximal line lifts, this vanishing forces ξ_{m+1}=0. If ξ_m is nonzero instead, restriction already prevents ξ_{m+1} from vanishing; the proof correctly keeps this inherited obstruction separate.

Starting at R_1=O_C(d), whose H¹ is zero, the same exact sequences show that H¹(R_n)=0 for all possible compatible Picard choices whenever

    d≥4(n−1)−1,

equivalently d≥4n−4 for even d. Thus the last uniformly guaranteed level is floor(d/4)+1. In particular, for all even d≥8 a line lift to X_3 forces splitting there, although first-order vanishing alone does not force that line lift.

Sharpness requires more than just the nonvanishing of a potential obstruction group. The proof supplies the needed construction. For the chosen reference ratio R_n=L_n, every section of L_m lifts from the plane, using the displayed conic-power exact sequence and H¹(P²,O(k))=0. Consequently restriction H⁰(L_{m+1})→H⁰(L_m) is surjective and δ_m=0.

Whenever 4m−d−1>0, a nonzero upper-root cocycle in H¹(O_C(d−4m)) therefore maps injectively to a nonzero extension class. The square-zero modification preserves A_{m+1}^0, Q_{m+1}^0, and the determinant, while reducing to the split reference below. It yields a nonsplit bundle despite the maximal-line lift. Equivalently one can use the tautological class over the punctured parameter space to keep the construction universal. No alternative decomposition can evade the nonzero class, because any decomposition must use the unique maximal line.

Taking m=n−1 proves sharpness of the uniform n-level threshold. These thresholds are sharp universal guarantees, not necessary conditions for an individual bundle to split.

## 8. Scope and final assessment

The proof consistently separates three data:

1. Negative-root classes obstructing successive maximal-line lifts.
2. Picard choices for the underlying line bundles, including the diagonal freedom already invisible to ε for d≥8.
3. Positive extension classes obstructing splitting once a maximal line exists.

The third-neighborhood construction disproves a deduction from ε=0 to higher splitting based solely on the specified local package. It does not compute the actual higher class of an HM restriction, identify a retained source, or prove failure of global algebraizability. A global nonsplit bundle can have an obstructed maximal conic line; conversely, the local formal lifting argument alone does not establish global realization. Those qualifications are explicit and mathematically appropriate.

All requested checks are complete. No theorem-level or formula correction is required.
