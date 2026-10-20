# Historical mathematical audit receipt

This is a preserved review of the source mathematical manuscript, not a fresh review of the publication bytes. Hashes quoted below identify the historical source versions. See [hm-algebraic-jump-models-PUBLICATION-CHECK.md](../hm-algebraic-jump-models-PUBLICATION-CHECK.md) for the final-publication review.

# Independent audit: algebraic and analytic local models

## Verdict and versions

**Pass.** The completed normal forms upgrade to common elementary étale neighborhoods and hence to analytic isomorphisms of the chosen algebraic minimal versal parameter germs, including their nilpotents. The separate stability argument also passes, with its explicitly imported cohomology inputs. No substantive correction is required in these final versions.

Audited SHA-256 hashes:

- PROOF.md: `854f63f3927c199f2f290623604efb785fabfa6523f0cddc9fe9aa84e132e24d`.
- STABILITY.md: `fcc3c72805fad2f1d90af8d5bafcbbc14e1575227fe78a250d66000eadcebdba`.
- Imported formal-jump-normal-forms/PROOF.md: `dff5923dffd3f5657c3be3cd3979ed5ac456aed00d0765243ce379bf181c70a3`, matching its existing audit.

I read the two new arguments, the imported formal proof and audit, and the relevant section of SHARPEST-BOUND.md. The pre-existing HM computations are imported rather than recomputed. I independently checked the primary Stacks statements and SGA 2 Corollary XII.3.7 used below.

## 1. Algebraicity and determinant identification

The fixed smooth projective X satisfies the hypotheses of [Stacks 09DS](https://stacks.math.columbia.edu/tag/09DS), giving an algebraic stack of flat coherent families with proper support. Local finite presentation is supplied separately by [Stacks 0DLZ](https://stacks.math.columbia.edu/tag/0DLZ). There is no boundedness assumption in this local statement.

The bundle-open argument is valid: for a finitely presented family flat over the base on X times that base, local freeness on a fibre extends to a neighborhood in the total space by the local flatness criterion. Properness then removes from the base the image of the closed failure locus. Since the fibres X are geometrically connected, the locally constant rank on a bundle fibre is one number; the rank-two condition gives the specified open substack.

For any family V, the fibre of the forgetful morphism from pairs (V,delta) to bundles is exactly the relative Isom space between det V and L. Both are finitely presented, base-flat sheaves with proper support. [Stacks 0DLW](https://stacks.math.columbia.edu/tag/0DLW) consequently makes this fibre affine and finitely presented. Thus the forgetful morphism is representable and finitely presented and its source is an algebraic stack locally of finite presentation. This avoids any need for a universal bundle on a coarse space or for an unproved Picard-space construction.

Simplicity determines the automorphism group scheme, not only its complex points: global endomorphisms of E commute with scalar extension from C, so Aut(E) is G_m. Requiring preservation of the chosen determinant identification gives mu_2. Characteristic zero is essential to its being étale. [Stacks 0DSN](https://stacks.math.columbia.edu/tag/0DSN) puts the point in the open DM locus, and [Stacks 06N3](https://stacks.math.columbia.edu/tag/06N3) gives an étale scheme atlas. Its fibre over the chosen object has a C point. An affine neighborhood of that point is finite type over C because the atlas and stack are locally of finite presentation. All ingredients for the actual algebraic parameter chart are therefore present.

## 2. Why the chart completion is a minimal hull

An arbitrary smooth atlas would introduce extra formal variables; the proof correctly uses an étale atlas. Base-changing it by an Artinian deformation yields an étale algebraic space over the Artinian base. A specified section over a nilpotent closed subscheme lifts uniquely. The specified section includes the isomorphism with the family, so this is exactly the lifting statement needed for the deformation groupoid, not merely a lifting assertion on coarse points.

After fixing the special-fibre identification, the induced map on isomorphism classes is formally smooth and tangent-bijective. Indeed an isomorphism between two deformations compatible with the markings transports their sections, and uniqueness of étale lifting controls the first-order comparison. Equivalently, infinitesimal automorphisms in the determinant-identified problem lie in H^0(End_0 E), which is zero. The nontrivial element of mu_2 does not reduce to the identity and causes no failure of the marked hull condition.

The determinant comparison is also sufficient. H^1(O_X) and H^2(O_X) vanish; across small extensions these eliminate new line-bundle parameters and obstructions. A discrepancy between determinant identifications reducing to the same one is a unit in 1 plus the Artinian maximal ideal and has a unique square root there. Scalar multiplication corrects it. Thus the ordinary marked bundle parameter functor and its determinant-identified version have the same hull. The imported completed ring and the chart completion are minimal hulls of this same functor, so the usual uniqueness of hulls gives a noncanonical C-algebra isomorphism. No assertion about equality of the two stacks or their inertia is necessary.

## 3. Approximation, analytic structure, and scope

[Stacks 0CAV](https://stacks.math.columbia.edu/tag/0CAV) is precisely the theorem needed. It applies to locally finite-type schemes over a locally Noetherian base with a G-ring at the base point and a base-linear isomorphism of completions. Here the base is Spec C, both schemes are finite type, and the formal normal form is C-linear. No reducedness or isolated-singularity hypothesis occurs. The theorem gives two elementary étale maps from one pointed scheme; one can shrink around its point to make this source finite type. It also allows any prescribed finite-order agreement with the given formal isomorphism.

That last qualification is correctly retained. Separately approximating every finite jet is not convergence or algebraization of the original formal coordinate map, and no compatible sequence is asserted. A common elementary étale neighborhood does imply isomorphic henselian local rings, but need not give isomorphic Zariski neighborhoods.

Analytification of an étale finite-type complex morphism is a local analytic isomorphism, including structure sheaves. This is explicitly recorded in the final paragraph of [Stacks Section 41.19, tag 025L](https://stacks.math.columbia.edu/tag/025L); it also follows from the standard étale presentation and the holomorphic implicit-function theorem. Applying this to both maps supplies the asserted analytic germ isomorphism. The resulting local analytic algebras are the convergent-power-series quotients by the displayed polynomial ideals. Nilpotents are preserved, so this conclusion is stronger than a homeomorphism of reduced spaces.

The final theorem properly calls this the analytic germ of an algebraic minimal versal base. It does not need a separate analytic versality theorem for arbitrary analytic parameter spaces. Nor does an isomorphism of critical schemes assert right-equivalence of a chosen potential.

Reduction is intrinsic under these equivalences. For an étale map of Noetherian C-schemes the base change to the reduced target is reduced, so the source reduction is that base change. Hence the smooth 24-dimensional reduced germ is correctly identified. The imported formal orbit is its completed germ; no specific orbit map, action, or selected classifying map is asserted to be algebraized.

## 4. Independent check of the stability lemma

The imported section-module resolution has no generators below degree three, giving H^0(F(s))=0 for s<3. The same imported file explicitly records H^1(F(s))=0 for s<0. These are exactly the two inputs used; no stronger restriction theorem is assumed.

For a nonnegative integer a, multiplication by the quintic equation gives the exact restriction sequence, and H^0(F(-a)) and H^1(F(-a-5)) both vanish. Thus H^0(E(-a)) vanishes for every such a, with no condition on the quintic other than smoothness for the subsequent geometric argument.

[SGA 2, XII.3.7](https://grothendiecksga.com/read/sga2/en/XII-3.html) states the Picard-group conclusion for projective complete intersections of dimension at least three; a smooth quintic threefold meets this hypothesis. A rank-one torsion-free subsheaf G of E has line-bundle double dual O_X(a), since X is smooth and locally factorial. Its quotient by G is supported in codimension at least two, so its first Chern class and slope agree with those of G. With H^3=5, a destabilizing slope forces 5a at least -5/2, hence a at least zero.

The inclusion of G into E defines a nonzero section of E(-a) outside a codimension-two subset. Local freeness makes E(-a) reflexive, and on normal X its sections extend across that subset. The extended section remains nonzero and contradicts the restriction vanishing. This handles arbitrary rank-one torsion-free subsheaves; the proof does not confuse them with line bundles. Rank two leaves no other positive proper ranks to test. Thus stability for every smooth quintic restriction is established from the stated imported inputs and is independent of the rank conditions needed for the local normal forms.

## Audit boundaries

This audit establishes the stated abstract algebraic and analytic upgrade and the separate stability consequence. It does not reevaluate an HM matrix, source, cofactor, selected quintic, numerical rank, or the original cohomology calculation. No coarse moduli identification, global universal family, decorated orbit equivalence, convergence of a prescribed formal map, or original mixed-source claim follows here. Only local reads, primary-source browsing, hashes, and this local audit write were used.
