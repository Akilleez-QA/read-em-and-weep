# Prior mathematical audit

This audit concerns the source manuscript. It is not a formal verification or a review of later normalized publication bytes.

# Independent audit of the rank-five compactification

## Verdict and scope

The proposed compactification is correct over **C**. For a nonempty Zariski-open set of maps `v: K → U` satisfying the stated square-avoidance condition, it produces a smooth, connected, projective K3 surface. Its complement of one smooth rational curve of self-intersection −2 is exactly the ordered-factor cover of the rank-two compatible quadrics.

This is a symbolic audit of the synthetic construction. It uses no actual source inputs or evaluations. No arithmetic or descent assertion is implied.

## 1. Bundle conventions and intersection signs

Use projective bundles of **lines**, so `O_X(−1) ⊂ π*F` and `ξ = c₁(O_X(1))`.

The tautological sequence on `B = P(U*)` gives

`c(S) = 1 − H + H²`.

The trace map `Sym²S → O_B` is everywhere surjective: a two-dimensional subspace of a nondegenerate three-dimensional quadratic space cannot be totally isotropic. Thus `F` is locally free of rank two. The splitting principle gives

`c₁(F) = −3H`,  `c₂(F) = 6H²`.

Consequently

`ξ² − 3Hξ + 6H² = 0`,

`K_X = −2ξ + π*(K_B − c₁(F)) = −2ξ`.

The useful Chow pushforwards are `π_*(ξ) = 1`, `π_*(ξ²) = 3H`, and `π_*(ξ³) = 3H²`.

## 2. The surface T and simultaneous genericity

The map `v` induces a section `s_v` of `G = F* ⊗ O_B(1)`, by restricting `v` to `F_[k]` and then projecting to `U/S_[k]`. The equation of `T` in `X` is the corresponding tautological evaluation, hence

`[T] = ξ + H`.

The parameter space `Hom(K,U)` globally generates `G`: at a fixed `[k]`, any map `F_[k] → U/S_[k]` extends to a linear map `K → U`. A generic `s_v` therefore has regular, reduced zero locus of length

`c₂(G) = 6 + 3 + 1 = 10`.

Locally `T` is the incidence equation `f x + g y = 0` in a trivial `P¹` bundle. At a regular zero of `(f,g)` this is the blowup model, after a linear change of the homogeneous coordinates. Therefore `T ≅ Bl_Z(P²)` for ten distinct points `Z`, and `T` is smooth, projective, rational, and connected. These ten points need not be general points of the plane.

Square-avoidance is also a nonempty open condition. For each isotropic line `[e]`, the condition `v(e²) ∈ Ce` imposes two independent linear conditions on the 15-dimensional space `Hom(K,U)`. Its incidence over the one-dimensional smooth conic has dimension at most 14. Since the conic is projective, its image is closed and proper. This open set intersects the nonempty open set of regular sections of `G`.

Adjunction gives

`K_T = (−ξ + H)|_T`,  so `L = O_T(ξ − H) = −K_T`.

As a check, on `T` one has `H² = 1`, `ξH = 4`, `ξ² = 6`, and therefore `K_T² = −1`.

## 3. The discriminant and its intersection with T

The determinant of the universal binary tensor is a section of

`O_X(2) ⊗ (det S)² = O_X(2ξ − 2H)`.

Its zero scheme is the rank-one divisor `E`, whose points are exactly

`([e],[k])` with `h(e,e)=0` and `k(e)=0`.

This incidence description identifies `E` scheme-theoretically with a smooth `P¹` bundle over the isotropic conic. In particular, the determinant divisor is reduced, even though its intersection with certain individual projective-bundle fibers can be a double point.

On `E`, the equation of `T` is `k(v(e²))=0`. Square-avoidance makes `e` and `v(e²)` linearly independent. Thus there is exactly one admissible `[k]`, namely the annihilator of their span. The intersection

`D = E ∩ T`

is the graph of the regular map `[e] ↦ Ann⟨e,v(e²)⟩`. Moreover, the defining equation on every ruling fiber of `E` is a nonzero linear form. Hence `D` is smooth and reduced, and `T` and `E` meet transversely along it. It follows that

`D ≅ P¹`,  `[D] = 2L = −2K_T`,  `D² = −4`.

There is no hidden rank-one component or nonreduced branch contribution.

## 4. The global cover algebra and K3 properties

The binary discriminant is a section `d ∈ H⁰(T,L²)`. Using the usual discriminant rather than the determinant changes only a nonzero scalar; over C this does not change the isomorphism class of the double cover. Its algebra is

`A = O_T ⊕ L⁻¹`,

with multiplication `L⁻² → O_T` induced by `d`. This is the correct global twist. Locally the cover has equation `w² = d`.

The ordered-factor map `P(S) ×_B P(S) → P(Sym²S)` is the finite flat double cover given by this discriminant: interchange of the factors negates the alternating product of the two factors, and that alternating product transforms as `O(1) ⊗ det S`. Restricting to `T` identifies its anti-invariant summand with precisely `L⁻¹`. Thus the stated algebra gives the ordered-factor cover, not merely some double cover with the same branch support.

For `p: Y = Spec_T(A) → T`:

- `Y` is finite flat over projective `T`, hence projective.
- Smoothness follows from the local equation `w²=d` and smoothness of the reduced branch divisor.
- The canonical bundle formula gives `K_Y = p*(K_T + L) = O_Y`.
- Since `L⁻¹ = K_T` and `T` is rational, `H¹(O_Y) = H¹(O_T) ⊕ H¹(K_T) = 0` by Serre duality.
- Also `H⁰(O_Y) = H⁰(O_T) ⊕ H⁰(K_T) = C`, so `Y` is connected.

Therefore `Y` is a smooth connected projective K3 surface. The ramification curve `R` maps isomorphically to `D`, and `p*D = 2R` gives `R² = D²/2 = −2`.

Away from `E`, every tensor has rank two and its unique supporting plane is its image in `U`. Its two distinct projective factors therefore give exactly the independent ordered-factor locus. Removing `R` from `Y` gives exactly that locus, with no additional boundary components.

## 5. Independent complete-intersection cross-check

There is also a direct model in `P(U) × P(U)`:

`h(p,r) = 0`,

`det(p,r,v(p r)) = 0`.

To write the second equation on the full ambient product, extend `v` linearly to `Sym²U`. Different extensions change the second equation by a multiple of the first, so the common zero scheme is intrinsic. The equations have bidegrees `(1,1)` and `(2,2)`. On their common zero scheme, the span of `p`, `r`, and `v(p r)` has dimension exactly two: this is immediate for independent factors, while on the diagonal it follows from square-avoidance. The image plane consequently varies regularly and recovers the point of `B`. This identifies the entire complete-intersection surface with `Y`, including the boundary. Its diagonal locus is exactly the isotropic conic and corresponds to `R`.

Adjunction in `P² × P²` independently gives the trivial canonical bundle, since `(−3,−3)+(1,1)+(2,2)=(0,0)`. The Koszul resolution also yields `h¹(O_Y)=0`. This cross-check confirms the global factor-cover identification and excludes an extraneous diagonal component.

## 6. Audit of the corrected outer map and full reduced fiber

I also inspected Sections 7–8 of `COMPACTIFICATION.md` after their completion. Their scheme-level complete-intersection identification and corrected outer morphism are valid.

With ordered factor frames `a,b`, the formulas

`X = (a∧b)a − (a∧v(ab))u`,

`Z = (a∧b)b − (v(ab)∧b)u`

have respective frame weights `(2,1)` and `(1,2)`, with common value line `det S`. They therefore define global projective maps once their nonvanishing is checked. Away from the diagonal their residual components are nonzero. On the diagonal their scalar coefficients are nonzero multiples of `e∧v(e²)`, which is nonzero by square-avoidance. These maps consequently extend everywhere on `Y`, recover the independent-zero isomorphism off `R`, and send precisely `R` to `([u],[u])`.

The dependent-zero lemma used there is also correct. For independent vectors `x,z`, outer symmetry and the cyclic-zero identity give

`A_(αx+βz)(γx+δz) = (αδ−βγ)(α A_x(z) − β A_z(x))`.

Any dependence between `A_x(z)` and `A_z(x)` would violate repeated-input injectivity after choosing a complementary pair `(γ,δ)`. Thus those two vectors are independent. If `u` lies in the span of independent `x,z`, a zero of `f(x,u,z)` is impossible; if the outer vectors are proportional, cyclic zero gives `f(x,u,x)=−2A_x(u)`, so a zero forces all three input lines to coincide.

It follows that the corrected map is a proper birational resolution of the entire **reduced** synthetic projective fiber over `[u]`, with exactly the exceptional curve `R`. This does not establish normality of that image, reducedness of the unreduced equation scheme, or an analytic singularity type. None of those stronger assertions is needed for the result, and none is made in the inspected proof.
