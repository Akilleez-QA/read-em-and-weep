# Historical mathematical audit receipt

This is a preserved review of the source mathematical manuscript, not a fresh review of the publication bytes. Hashes quoted below identify the historical source versions. See [hm-jump-obstructions-PUBLICATION-CHECK.md](../hm-jump-obstructions-PUBLICATION-CHECK.md) for the final-publication review.

# Independent audit: quadratic obstructions at restriction jumps

## Verdict and audited version

**Pass, with the stated audited HM inputs.** The proof establishes the exact mixed Yoneda bracket with its declared cone/action conventions, the primary cubic reduction, generic nonzero mixed obstructions on the smooth rank-one stratum, and local hull dimension exactly 24 there. The additional vertex criterion and rank-one zero-derivative criterion are also valid as conditional statements. No mathematical correction is required.

Audited [PROOF.md](PROOF.md) SHA-256:

`cf9fd13f7d68485652a490d011b05684e6715144e03f34ef3f6ce9c54a46e4c3`.

This is an independent audit of the new argument. I read the imported restriction and orbit proofs and their audits; I did not repeat the original HM cohomology or scalar-propagation calculations. The current imported proof hashes match their recorded audits:

- Generic restriction deformation proof: `261c57bde9ce8bad8b04e511a08dc3eae40d4746c34592e4195979f4d64ef21f`.
- Its JUMP-STRATA complement: `dd698b95c1cdec3d1b01824785ce06beaac93c90667a2a03f34c852a3003cdca`.
- Restriction jump-locus proof: `5009e39fe76a0971e96ef1473946187525283e0c5cbb1312b2c52b0f1b08f39a`.
- Nonzero-scalar corollary: `038c429400ac00da021177fc123150e3e4ae6dc6056daa7475b2dd6162c35a2a`.
- Scalar-propagation proof underlying that corollary: `35a93234687c5d79533f8fc55a7589b3cae6546e683dd3e4c192adbbc3d89c4c`.

## 1. The cone Bockstein and exact mixed bracket

The differential D_p(b,c)=(db+pc,−dc) squares to zero. A degree-one cocycle has c in C²(B(−5)), with dc=0 and db=−pc. In the dual-number family p+s q, its differential is precisely s(qc,0), so dividing by s gives the Bockstein class [(qc,0)]. Its image in H²(L_p) is j([m_q[c]]), where the brackets on the inner expression mean reduction modulo im m_p.

The map is independent of representative: D_pD'+D'D_p=0, and changing a cocycle by a D_p-boundary changes its image by a D_p-boundary. Its projection to H³B(−5) is zero because the second summand is zero. Thus this calculation proves the class formula in the full H², not only its image in some quotient.

The projection to the shifted second summand is the declared connecting-map convention. With some usual short-exact-sequence conventions it is the negative of the connecting map computed by differentiating an arbitrary lift. This is harmless here because the proof explicitly fixes its cone, δ, and Bockstein simultaneously; one must not silently change δ while retaining the displayed sign.

The geometric comparison has the correct action direction. For q=v·p and g_s=exp(sv), the equation action p↦p∘g_s⁻¹ makes g_s an isomorphism X_p→X_{g_s·p}. Pulling the restricted bundle back along this isomorphism gives (g_s*F)|X_p. Therefore the moving-equation cohomology family is the endomorphism cohomology family of the stated orbit deformation on the fixed X, with the identity identification at s=0. A first-order equivalence inducing the identity on the central fiber preserves the Bockstein; a change of trivialization only changes the derivative by a chain homotopy.

For a Dolbeault deformation ∂̄+sα, the induced endomorphism differential is d+s[α,−]. On degree-one forms its derivative is αx+xα, so its Bockstein is the symmetric Yoneda bracket β(a_v,x). This proves (1), including the positive sign for the declared conventions. No unknown scalar beyond the already defined actual multiplication map Φ occurs in (1).

## 2. Serre duality, symmetry, and the cubic

The restriction triangle and trace pairing make restriction and its connecting morphism adjoint up to the scalar trace convention on X. The proof fixes that convention by (4), using the isomorphism H³O_X→H⁴O(−5). Hence (2) follows from (1). The scalar trace must remain compatible with this adjunction normalization: changing it independently introduces the corresponding factor into the pairing formula. The proof expressly avoids asserting a normalization-free numerical sign.

The image j(coker M) annihilates A because δA=0. It has dimension dim ker M, equal to dim(H/A), so the perfect Serre pairing identifies it exactly with A^⊥ and identifies its pairing with K_p as perfect. This validates both the vanishing criterion and the use of dual orbit components below.

For degree-one factors, cyclically moving one past the other two has sign +1. Trace cyclicity together with the built-in symmetry of β therefore makes C(x,y,z)=⟨β(x,y),z⟩ fully symmetric. Formula (1) gives β(A,A)=0. Consequently, after a splitting, the only possible cubic summands are A⊗Sym²K_p* and Sym³K_p*, the former fixed by L and the latter denoted G. The coefficients 1/2 and 1/6 in (5) follow from expanding the symmetric trilinear form and ensure that the derivative of W₃ is q₂=β(x,x)/2.

Thus there are one and four undetermined normal-cubic coefficients when dim K_p is one and two, respectively. These are unknown coefficients after a chosen splitting; the proof does not claim they are intrinsic moduli or invariant under changing that splitting. Most importantly, cyclicity forces q₂(z), paired with a_v, to equal L(v)(z,z)/2. The normal-normal quadratic companion cannot be discarded.

## 3. Rank-one transversality and the exact quadratic initial space

For a rank-one symmetric form, an adapted basis gives M=diag(μ,0), μ≠0, and d(det)_M(N)=μN₂₂. The kernel vector u is the second basis vector. This proves that λ_p(v)=Φ(v·p)(u,u) detects exactly the derivative of the determinant along the orbit. Rescaling u or adding a multiple of p to a projective tangent representative does not affect vanishing. Since the coker/kernel pairing is perfect and both are one-dimensional, λ_p=0 is equivalent to vanishing of all mixed brackets.

If λ_p≠0, the cubic is t₁z²/2+γz³/6. Its gradient components span exactly z² and t₁z. This conclusion includes the component dual to t₁, rather than incorrectly keeping only mixed terms.

The added contraction/gauge-slice paragraph correctly explains why this is the entire degree-two initial space of the minimal hull ideal. A strong contraction may be chosen in the Dolbeault complex. The formal solution η=i(x)−h[η,η]/2 begins with i(x), and the usual Kuranishi map k=P[η,η]/2 begins with q₂. The gauge-slice Maurer–Cartan condition is equivalent to k=0; this follows also by the Bianchi identity and formal-order induction. Trace-free H⁰ vanishes, so this supplies the ordinary fixed-determinant hull, which has the same deformation parameters as the unrestricted problem here.

Every generator of its ideal starts at order at least two. Consequently a degree-two initial term of any ideal element is a constant linear combination of those quadratic components. Higher-order coefficients or cancellations cannot add a new degree-two term. Transport to another minimal hull only changes the tangent variables linearly at this order. This justifies the word “exactly” while leaving the higher-degree initial ideal undetermined.

## 4. The dimension-24 conclusion

The associated graded hull is a quotient of C[t₁,…,t₂₄,z]/(z²,t₁z). The latter has radical (z), hence Krull dimension 24. A complete Noetherian local ring has the same dimension as its maximal-ideal associated graded ring, so the hull has dimension at most 24.

The imported orbit complement provides a closed embedded formal 24-dimensional smooth germ, not merely 24 independent tangent vectors. Its construction gives a surjective map from the hull to C[[u₁,…,u₂₄]], so it supplies the needed dimension lower bound. Combining these bounds yields exactly 24. Embedding dimension 25 then proves nonregularity and failure of formal smoothness. The argument does not determine reducedness, all components, or the full higher Kuranishi ideal, as the proof correctly notes.

## 5. Generic transversality

The smooth-quintic rank-one stratum is a nonempty open subset of the irreducible determinant quadric. If every infinitesimal orbit direction were tangent throughout this open set, every corresponding homogeneous quadratic derivative of Q would vanish on a dense subset of the quadric. Irreducibility and equality of degrees force each derivative to be a scalar multiple of Q. Whether one uses the vector-field derivative or the contragredient action on polynomial functions changes only a common sign, with no effect on this invariant-line argument.

The resulting one-dimensional Lie representation has zero character because sl₅ is perfect; connectedness then gives SL₅-invariance of Q. A nonzero invariant quadratic on Sym⁵V* would polarize to a nonzero equivariant linear map Sym⁵V*→Sym⁵V. These irreducible representations have distinct highest weights 5ω₄ and 5ω₁, so no such map exists. This is the required contradiction.

The simultaneous vanishing of derivatives for a fixed basis of sl₅ is a closed condition. Its complement in the irreducible smooth rank-one stratum is therefore nonempty, open, and dense. This establishes generic actual obstruction and dimension 24 without establishing transversality at every point. No selected polynomial or rank instance is needed.

## 6. Vertex and zero-derivative criteria

At a vertex point, the orbit-dual components of q₂ are exactly the quadratics in im L, up to the harmless factor 1/2, and are independent of G. If these binary quadratics have no common projective zero, their affine common zero set is the origin. The Nullstellensatz gives radical (z₁,z₂); adjoining the 24 t variables yields a quotient of dimension 24. The same associated-graded upper bound and embedded-orbit lower bound therefore prove hull dimension 24, while embedding dimension 26 proves singularity. Surjectivity onto all binary quadratics is a sufficient condition. The proof makes no claim that this condition has been verified at a particular vertex or generically on the vertex.

At rank one with λ_p=0, W₃=γz³/6. If γ≠0, its gradient supplies z² and the identical dimension argument applies. If γ=0, all primary quadratic obstructions vanish, but higher obstructions are not decided. Both statements have the appropriate conditional scope.

## Scope of the audit

Only static local proof/audit reads, abstract cochain/deformation/representation arguments, hashes, and this local audit-file write were performed. No selected quintic, HM multiplication map, source, cofactor, numerical rank, coefficient instance, or large computation was evaluated. No external application or previously audited proof was modified.
