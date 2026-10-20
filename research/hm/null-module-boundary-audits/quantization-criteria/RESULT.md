# Bundle-quantization criteria: primary-source result and remaining gap

## Bottom line

There is a genuinely applicable whole-support bundle obstruction theorem, and a stronger characteristic-class necessary test worth isolating. Neither currently proves existence or nonexistence for the supplied twisted, equivariant HM module. The missing bridge is not ambient associativity: it is passage from the specified algebroid/module descent to the hypotheses and characteristic classes of a theorem for a fixed global algebra sheaf. The full-sign thirty-coordinate obstruction has not been evaluated.

Inputs read: [RESULT.md](../module-lifting/RESULT.md) and [LEMMA.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/9e3d8dc8525a7d11ae919dfac2126794c9bdc366/research/hm/null-literal-ambient-extension/descent/LEMMA.md). This research used primary mathematical texts only and performed no source, jet, physical-model, matrix-product, or repository computation.

## 1. Exact whole-support theorem, not a Lagrangian analogy

Baranovsky–Huey, *Obstructions to Deformation Quantization of Bundles*, arXiv:2607.12910v1 (14 July 2026), Theorem 1 and Corollary 11:

https://arxiv.org/html/2607.12910v1#S2
https://arxiv.org/html/2607.12910v1#S6

For a smooth characteristic-zero algebraic symplectic variety or holomorphic symplectic manifold, fix a complete deformation-quantization **sheaf of algebras** O_h. Given a locally free order-k module E_k, for k+1≤ℓ≤2k+1 its extension obstruction belongs to H²(M,End(E)_(k,ℓ]); vanishing is necessary and sufficient. Here the coefficient sheaf is h^(k+1)End_(O_h)(E_(ℓ-k-1)), with the h-power recording its filtration position. Extensions form an H¹ torsor. In particular, the one-step coefficient sheaf is End(E). Vanishing H²(End(E)) implies all-order extension. For larger jumps, Theorem 2 supplies a necessary obstruction in an extension of the filtered endomorphism sheaf by O_M; it does not claim sufficiency.

**Application/gap (our comparison):** This rigorously validates the type of obstruction in the local module-lifting lemma. It does not kill it. For an abelian fourfold, scalar inclusion and trace/rank split O_X off End(E); consequently H²(O_X) is a direct summand of H²(End(E)). Thus the simple vanishing hypothesis cannot hold for the full group. Restricting to a symmetry component still needs its actual obstruction to vanish. The paper's fixed-global-algebra setup does not, without proof, identify its torsor with modules over the supplied non-neutral descent presentation. The local lemma already provides the needed small-extension statement directly for that presentation, so merely citing this theorem adds no missing vanishing.

## 2. More promising: a characteristic-class obstruction on the whole symplectic variety

Baranovsky, *Chern classes of quantizable coisotropic bundles*, J. Noncommut. Geom. 18 (2024), 37–59, Theorem 1.1 and §2.2:

https://ems.press/content/serial-article-files/42628
https://doi.org/10.4171/JNCG/491

Assume a fixed flat, complete quantization algebra sheaf O_h, and a flat complete coherent module whose reduction is j_*E for a smooth coisotropic j:Y→M. Writing dim M=2(p+q), codim Y=q, the trace-density class A-hat(TM) exp(−c(O_h)) ch(j_*E) vanishes outside degrees 2q through dim M. There is also a lift to the null-foliation-filtered de Rham cohomology. This includes **Y=M**; it is not restricted to Lagrangians. For a symplectic fourfold with full support, components in de Rham degrees 6 and 8 must vanish. The period is c(O_h)=[ω]/h+ω_0+hω_1+⋯. The theorem is necessary, not sufficient, and is stated for a global algebra sheaf, in algebraic or holomorphic topology.

**Universal symbolic specialization (our calculation, not a model evaluation):** On an abelian fourfold A-hat(TX)=1. For any rank-two E with c1(E)=0, writing d=c2(E), its Chern character is 2−d+d²/12. If this E quantizes over an algebra sheaf with period c, the theorem therefore requires

    c d − c³/3 = 0 in H⁶_dR(X)((h)),
    d²/12 − c² d/2 + c⁴/12 = 0 in H⁸_dR(X)((h)).

These are formal cup-product identities, not numerical evaluations of the supplied HM data. They offer a sharper target than a generic connection argument. To use them against the present module, one must first establish a twisted-algebroid version with the correct characteristic class and sign, or a justified neutralization/Morita comparison preserving the specified classical E and finite jet. One cannot simply insert the gerbe's b as a period coefficient: the conversion and normalization must be proved. Neutralizing by a module whose existence is the question would be circular. Even a successfully verified trace-density identity can miss trace-free Ext² obstructions, unless a separate detection/injectivity theorem is established.

The two-parameter ambient construction does not remove this gap. One may restrict a genuine two-parameter module to a one-parameter formal curve and then apply a theorem whose hypotheses have been verified, but the inherited period and twist remain part of those hypotheses. Ambient HH² corrections unavailable in the retained full-sign channel cannot be substituted for a module-class calculation.

## 3. Why smooth Fedosov is not the missing existence theorem

Bursztyn–Waldmann, *Deformation Quantization of Hermitian Vector Bundles*:
https://arxiv.org/abs/math/0009170

For a fixed Hermitian star product on a smooth manifold, Hermitian vector bundles admit deformation as projective modules, uniquely up to the stated equivalence. Waldmann's Fedosov construction starts with symplectic and bundle connections:
https://arxiv.org/abs/math/0201181

**Gap:** Smooth connections and smooth resolutions are available without the holomorphic/algebraic vanishing required to descend regular coefficients. Solving the smooth problem does not prove that its resulting holomorphic integrability/descent equations are solvable. Conversely, nonzero Chern classes obstructing an ordinary holomorphic connection on E do not by themselves obstruct a one-sided locally free quantum module: its definition is not the definition of a flat Poisson module or a bimodule with prescribed semiclassical connection.

## 4. Torus duality is genuine but does not automatically cover the mixed twist

Ben-Bassat–Block–Pantev, *Non-commutative tori and Fourier–Mukai duality*, especially §5.3 and Appendix B:
https://arxiv.org/pdf/math/0509161

Their formal holomorphic noncommutative torus is Fourier–Mukai equivalent to a formal gerbe on the dual torus. Appendix B treats bundle-lifting obstructions; §5.3 derives support restrictions for transformed objects, including an obstruction to quantizing ample line bundles. This is a theorem in the correct holomorphic world, not the smooth noncommutative-real-torus theory.

**Gap:** Their specific pure-Poisson/dual-gerbe equivalence is not automatically an equivalence for the simultaneous Poisson-plus-gerbe deformation here. Applying it requires constructing the corresponding mixed deformation equivalence and tracking the given E, its finite lift, flatness, and support. A derived equivalence alone does not prove that the transform of this particular E extends. Thus this route may re-express the obstruction geometrically but is not presently an existence theorem for HM.

## Recommendation

The most useful new research target is a **twisted trace-density/period comparison preserving the fixed two-jet**, followed by testing whether its characteristic-class map detects the retained full-sign Ext² component. The exact lifting theorem is already matched by the local lemma; smooth Fedosov and Lagrangian projective-flatness criteria do not repair the actual proof. No all-order module existence, nonexistence, or retained-coordinate vanishing is claimed.

## Addendum: an endomorphism-algebra route that does not assume neutral gerbe

A closer reading of the same 2024 proof gives a more precise route. Section 3.3, equation (6), uses the matrix Weyl algebra 𝔈=gl_e(D_p), its derivation algebra, and a central extension. Lemma 3.5 proves degree-above-2p vanishing of a universal characteristic class. Section 4.2 constructs the endomorphism-algebra Harish–Chandra torsor P_𝔈; Lemma 4.3 descends the relevant class to Der(𝔈). The published theorem nevertheless starts with a global O_h-module, and states no arbitrary-gerbe theorem.

**Proposed bridge, not established here:**

1. Assume a locally free twisted module exists. Its endomorphisms should glue to an honest global algebra B_h, locally a matrix algebra over the local quantization or its opposite. Prove this using the precise row convention; do not confuse B_h with a commutative deformation of O_X.
2. Verify that B_h has the formal matrix-Weyl local normal form and the transitive Harish–Chandra torsor required for the universal class. This would let the vanishing mechanism be used without first neutralizing the original algebroid.
3. Identify the resulting Gelfand–Fuks class in global de Rham cohomology. This is the crucial missing step: compare the central extension characteristic class with the original algebroid's (μ,F,A), its gerbe term b, and E's characteristic classes. Trace normalization, tensoring E by a line bundle, and opposite-algebra/sign conventions must agree. The formula A-hat exp(−c)ch(E) from the neutral case cannot simply be copied.
4. If that comparison is proved, extract the degree-six/eight conditions and ask whether they detect the retained obstruction. They remain necessary tests; a vanishing characteristic image alone is not module existence.

The construction of B_h in step 1 is conditional on the sought module, but that is legitimate in a necessary-condition argument. It would be circular only if used to assert the module already exists or to neutralize the ambient algebroid in an existence proof. This is a narrower and more plausible continuation than demanding a blanket theorem for all twisted modules.
