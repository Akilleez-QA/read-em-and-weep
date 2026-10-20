# Full formal normal forms at transverse HM restriction jumps

## Theorem and scope

Over C, fix a smooth quintic X=X_p and the restricted normalized HM bundle E=F|X. All deformations below are ordinary bundle deformations on this fixed X, equivalently their fixed-determinant parameter functor. Import the audited results of

- ../generic-restriction-deformations/{PROOF,JUMP-STRATA,AUDIT}.md;
- ../jump-obstruction-pairing/{PROOF,AUDIT}.md;
- ../heisenberg-vertex-obstructions/{PROOF,AUDIT}.md.

Put A=H¹(End₀F), of dimension 24, and K_p=ker Φ(p). The orbit family embeds a smooth 24-dimensional formal germ in a minimal hull, with tangent A. Write L_p(v)(u,w)=Φ(v·p)(u,w) on K_p.

1. At every rank-one point with L_p nonzero (equivalently orbit transverse to the determinant quadric), the complete minimal hull is isomorphic to

   C[[t₁,…,t₂₄,z]]/(z²,t₁z).

2. At every vertex point where L_p:sl(V)→Sym²K_p* is surjective, the complete minimal hull is isomorphic to

   C[[t₁,…,t₂₄,z₁,z₂]]/((z₁,z₂)²,t₁z₁+t₂z₂,t₂z₁+t₃z₂).

These are exact complete local rings, not just their quadratic initial approximations. The isomorphisms identify the orbit germ with z=0. They are noncanonical, and assert formal equivalence only. The imported genericity results make both conclusions valid on nonempty open dense subsets of their respective smooth-quintic strata. They do not settle the exceptional rank-one nontransverse points or nonsurjective vertices.

## 1. The precise cyclic input

The primary source used is Okke van Garderen, *Cyclic A-infinity Algebras and Calabi–Yau Structures in the Analytic Setting*, arXiv:2306.00771v2 (18 July 2024), [Theorem 5.10](https://arxiv.org/html/2306.00771v2), together with Theorem 5.2 and Corollary 4.24. Theorem 5.10 constructs a cyclic minimal A∞ model on Ext for a perfect complex on a smooth projective variety equipped with a volume germ along its support. In the projective CY case its pairing is Serre duality (Theorem 5.2 and Remark 5.12). Corollary 4.24 gives a potential when H⁰=C. These hypotheses apply to the simple vector bundle E on the smooth projective CY threefold X. No stability hypothesis occurs in this minimal-model theorem. We use only its formal consequence, not its stronger analytic estimates or a semistable-moduli quotient assertion.

Here are the deformation-theoretic and normalization details needed to apply that consequence. Let D=A^{0,*}(X,End E). Its Maurer–Cartan equation is ∂̄α+α∧α=0 and its gauge equivalence is change of bundle trivialization. Thus its commutator DGLA controls bundle deformations. A minimal A∞ model of D, after antisymmetrization, is a minimal L∞ model of this DGLA; its Maurer–Cartan equation on H=Ext¹(E,E) is

   κ(x)=Σ_{n≥2} m_n(x,…,x)=0 ∈ Ext²(E,E).

We use unsuspended conventions in which m₂ on degree-one inputs is the Yoneda product. The standard minimal-model/Kuranishi construction gives a hull by the components of κ: one solves the acyclic summand recursively, and the remaining cohomology component is the obstruction map. Equivalently this is the usual homotopy transfer construction underlying the imported Kuranishi proof. For precision, the map from the minimal MC solution functor to its gauge-quotient deformation functor is smooth: over a small extension, take a solution representing the given lifted deformation; its reduction is gauge-equivalent to the prescribed solution. Lift that gauge transformation to the extension and apply it, so the reduction is exactly the prescribed solution. Gauge parameters, or a finite composition of them, lift along a surjection of Artinian coefficient ideals. Minimality makes the first-order gauge action zero, so the tangent map is an isomorphism. This is precisely the hull property. The first-order map is the identity on H. This assertion needs no absence of scalar automorphisms and does not identify an unrigidified moduli stack with a scheme. For general Maurer–Cartan deformation and minimal-model conventions see [Manetti, Deformation theory via differential graded Lie algebras](https://arxiv.org/abs/math/0507284).

Cyclicity supplies a formal scalar function

   f(x)=Σ_{n≥2} (1/(n+1)) ⟨m_n(x,…,x),x⟩,

where the signs are fixed by the above MC convention and the CY trace. Each summand has degree n+1. Differentiating it gives n+1 equal terms by cyclicity; hence

   df_x(h)=⟨κ(x),h⟩.

The perfect Serre pairing Ext²×Ext¹→C therefore identifies the ideal of κ with the gradient ideal J(f). Consequently

   R≅C[[H*]]/J(f),     f∈m³.

Its cubic term is ⟨x∪x,x⟩/3=⟨β(x,x),x⟩/6, exactly the primary cubic of the imported obstruction proof. If conventions multiply f by a common nonzero scalar, J(f) and the following coordinate argument are unchanged. Higher operations need not vanish.

## 2. Determinant and trace-free compatibility

For a smooth quintic, H¹(O_X)=H²(O_X)=0. The decomposition End E=O_X·id⊕End₀E therefore identifies H¹ and H² of the full endomorphism complex with their trace-free versions. The trace pairing makes these summands orthogonal: tr(id·b)=0 for trace-free b. Its restriction to End₀E is nondegenerate, so Serre duality gives the same perfect H²–H¹ pairing used in the imported primary calculation.

We deliberately apply the associative cyclic theorem to End E, not End₀E: the latter is a DGLA under commutators but is not in general an associative subalgebra. There is no unjustified assertion of a trace-free associative A∞ subalgebra. On commutative Artinian bases, the full and fixed-determinant deformation parameter functors agree here by the imported determinant argument: determinant deformations are trivial, and a change of determinant identification by a unit congruent to one is corrected by its square-root scalar automorphism. Thus the same minimal hull applies. Fixed determinant removes infinitesimal scalar stabilizers; finite μ₂ inertia and unrestricted scalar inertia are not additional parameters or equations in this hull.

## 3. Straightening the orbit preserves the critical presentation

Use the particular critical hull R=S/J(f), S=C[[x₁,…,x_N]], N=24+dim K_p. The actual orbit family has a compatible classifying map R→B=C[[u₁,…,u₂₄]], constructed successively over powers of the maximal ideal using the hull lifting property. Its tangent map is the imported injection A→H. Thus S→B is surjective on cotangent spaces.

Choose 24 source coordinates whose images have independent linear parts. Their images are formal coordinates on B by the formal inverse-function theorem. Complete them to coordinates (t,z) on S, and subtract from each z its image expressed as a power series in the t. This gives an invertible formal coordinate change with

   S→B : t_i↦u_i, z_j↦0,
   J(f)⊂(z).

The chain rule under a formal coordinate automorphism multiplies the gradient by its invertible Jacobian matrix. Therefore the transformed hull is still exactly J(the transformed f), not merely a set-theoretic critical locus. The tangent subspace z=0 is precisely A.

All derivatives of f vanish on z=0. Expand uniquely

   f(t,z)=a(t)+Σ_j b_j(t)z_j + terms in (z)².

Normal derivatives give b_j=0; tangential derivatives give ∂a/∂t_i=0 for all i. In characteristic zero a is constant. Subtracting that constant, which changes no gradient, yields f∈(z)². Moreover f remains in m³, because the coordinate change fixes the closed point and has invertible linear part.

The straightening may change the chosen complement to A, but cannot change the intrinsic A⊗Sym²(H/A)* part of the cubic. Consequently its orbit-linear normal-quadratic coefficient map is exactly L_p, up to the chosen tangent and volume normalizations. Pure normal cubics may change; they cause no difficulty below.

## 4. Formal coefficient-absorption lemma

Let S=C[[t₁,…,t_d,z₁,…,z_r]] and f∈m³∩(z)². Suppose the coefficient map of the cubic's t-linear, z-quadratic part has rank s=r(r+1)/2 as a map from the t-space to Sym²(C^r)*. Assume d≥s. Then f is formally right-equivalent, by coordinates keeping the ideal (z) fixed, to the universal quadratic form in z with s independent t coefficients.

Proof. Choose the usual basis q_α(z) of quadratic monomials, using the convention q=z²/2 for r=1 and (z₁²/2,z₁z₂,z₂²/2) for r=2. Write

   f=Σ_{α=1}^s a_α(t,z)q_α(z),   a_α∈m.

Existence follows by assigning each monomial of z-degree ≥2 to one quadratic monomial dividing it. There are finitely many q_α, so this groups a formal series into finitely many well-defined formal series. Membership in m³ ensures the coefficients can be chosen in m. Although the decomposition is not unique, the t-linear part of each a_α is uniquely determined by the t-linear z-quadratic part of f. Thus the differentials of a_α restricted to z=0 have independent t-linear terms.

Choose linear orbit coordinates t so that these terms are t₁,…,t_s. Replace t_α by a_α(t,z) for α≤s; keep t_{s+1},…,t_d and all z unchanged. Its linear matrix has block form with an invertible t-block and identity z-block; possible linear z terms in a_α are harmless. By the formal inverse-function theorem this is an automorphism. In these coordinates f=Σ t_α q_α(z) exactly. Since z is unchanged, the orbit ideal is unchanged; the map restricted to z=0 is itself an invertible formal orbit reparametrization. Finally the chain rule identifies the whole gradient ideals under this automorphism. ∎

Surjectivity is essential. Merely knowing that the image quadratics have no common projective zero does not justify this lemma; that weaker vertex criterion is not enough for the present conclusion.

## 5. Application and exact rings

For rank-one Φ(p), r=1. Nonzero L_p makes the coefficient map rank one. Sections 3–4 put the potential in the exact form f=t₁z²/2. Its nonzero partial derivatives are z²/2 and t₁z. This proves the first ring in the theorem, including all orders.

At a vertex r=2. Surjective L_p has rank three. Sections 3–4 put the potential in the exact form

   f=(t₁z₁²+2t₂z₁z₂+t₃z₂²)/2.

Its derivatives in t₁,t₂,t₃ span z₁²,z₁z₂,z₂², and its derivatives in z₁,z₂ are t₁z₁+t₂z₂ and t₂z₁+t₃z₂. The remaining 21 orbit derivatives vanish. These generate the full ideal, proving the second ring.

This is stronger than a statement that all higher initial equations vanish: an actual formal change of variables removes every higher term of the potential. It does not prove formality of the controlling DGLA or A∞ algebra, nor determine ordered/noncommutative or source-constrained obstructions.

## 6. Immediate ring-theoretic consequences and limitations

In either ring the nilradical N is generated by the z variables, N²=0, and R/N=C[[t₁,…,t₂₄]]. Indeed the displayed ideal contains (z)² and is contained in (z); its radical is exactly (z). Thus the orbit is the entire reduced formal germ and the unique minimal prime is (z). The rings are nonreduced: all defining equations have order at least two, so each z has nonzero class in the cotangent space and cannot vanish in R. Their dimensions are 24 and their embedding dimensions are respectively 25 and 26.

More precisely, with B=C[[t₁,…,t₂₄]], the rank-one ring is the square-zero B-algebra B⊕(B/(t₁))z. The vertex ring is B⊕N where N is the cokernel of the symmetric map B²→B² with matrix [[t₁,t₂],[t₂,t₃]], and multiplication on N is zero. Its module support is t₁t₃−t₂²=0; the rank-one support is t₁=0. These are statements in the resulting noncanonical formal coordinates, not a new selected-quintic rank calculation or an identification of physical source matrices.

No claim of convergent or algebraic coordinate equivalence is made: the orbit-classifying map used in Section 3 is only constructed formally. An analytic potential alone does not upgrade that map or the straightening automatically. Nor do we claim a global moduli description, a universal quotient by automorphisms, or that each point of either jump stratum satisfies the rank hypothesis.

Only static reads of the named proofs, primary-source browsing, abstract formal algebra, and local proof/audit writes were used. No selected HM map, source, cofactor, polynomial, or numerical rank instance was evaluated; no external service was modified.
