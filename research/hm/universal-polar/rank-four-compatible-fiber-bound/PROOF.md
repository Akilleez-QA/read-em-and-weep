# Six-dimensional residual kernels have compatible fibers of dimension at most two

## Statement and dependencies

Over C, let dim E=4, K⊂Sym²E have dimension six, and v:K→E be linear. Assume square avoidance: for every nonzero e with e²∈K, v(e²)∉Ce. Then the projective compatible rank-two locus

  T={ [q]∈P(K): rank(q)=2, v(q)∈im(q) }

has dimension at most two.

For an outer-symmetric cyclic-zero operation on a five-dimensional V with all repeated-input maps injective, square avoidance and the finite ordered-factor reconstruction hold by https://github.com/Akilleez-QA/read-em-and-weep/blob/59a2aa5db85baeb0da1ff467c4f72d77a41ae488/research/hm/universal-polar/full-support-rank-five-dimension-bound/PROOF.md, Section 1. Therefore every residual-rank-four independent-zero fiber has separately projectivized dimension at most two. Under the additional middle rank-drop support bound (H) of that proof, independent-zero components generically of residual rank four have affine dimension at most seven.

Dependencies are (i) the compatible-surface classification and fiber bound for every full-support five-dimensional K in https://github.com/Akilleez-QA/read-em-and-weep/blob/3109756417e62b91a092b5a89ee412089322a986/research/hm/incidence-foundations/fullsupport-rank-five-surface-exclusion/PROOF.md and https://github.com/Akilleez-QA/read-em-and-weep/blob/59a2aa5db85baeb0da1ff467c4f72d77a41ae488/research/hm/universal-polar/full-support-rank-five-dimension-bound/PROOF.md, Sections 2–4, and (ii) the supported-ternary four-space theorem https://github.com/Akilleez-QA/read-em-and-weep/blob/c109a2f634916ca7fe9dc4bf3e8f25c2dae6a309/research/hm/normalizer-rank-five/rank-six-cubic-web/REDUCIBLE.md. The former pointwise linear-algebra statements use only square avoidance; no condition that a restricted subspace remain an entire residual kernel is needed. No global finite-middle conclusion is imported for a restricted subspace.

This does not exclude residual rank four itself, lower residual ranks, or dimension-seven moving families.

## 1. Ternary support and the compulsory normal correction

If K has support at most three, its support E0 has dimension exactly three and K=Sym²E0. Write h for v modulo E0, a map K→E/E0. Then h≠0.

Indeed, if v took values in E0, the quadratic map e↦v(e²) would induce a nowhere-zero section of Q(2) on P(E0), where 0→O(-1)→E0⊗O→Q→0. But c1(Q)=H and c2(Q)=H², and thus c2(Q(2))=H²+2H²+4H²=7H²≠0. A nowhere-zero section of a rank-two bundle would have zero top Chern class. Its zero is exactly an eigenline v(e²)∈Ce, prohibited by square avoidance.

Every compatible q lies in K0=ker h, a five-dimensional subspace of Sym²E0. If its compatible locus had dimension at least three, a general hyperplane K1⊂K0 (dimension four) would meet it in dimension at least two. Rank two remains a dense open in at least one such section, and compatibility and square avoidance restrict. This contradicts the supported-ternary four-space theorem. Hence dim T≤2.

This gives a structural restriction in addition to the dimension bound: a ternary six-dimensional kernel has a nonzero, splitting-independent normal correction and its entire compatible locus is confined to its canonical five-dimensional kernel. Splitting changes add contractions q↦2q(d), whose values lie in E0, so h is indeed unchanged.

## 2. Full support: reduction of a hypothetical threefold to a factor curve

Assume now K has full support E. A general hyperplane K'⊂K has full support. In fact there is at most one hyperplane of K supported on three dimensions: two distinct such hyperplanes K1,K2 would intersect in dimension four. If their three-dimensional supports differ, Sym²E1∩Sym²E2=Sym²(E1∩E2) has dimension three, impossible. If the supports agree, K=K1+K2 would itself have ternary support. Support at most two is impossible for a five-dimensional space.

The full-support five-space fiber theorem, applied to v|K', first gives dim T≤3: a larger-dimensional component would meet a general hyperplane in compatible dimension at least three.

Suppose equality holds, and take an integral ordered-factor component Z of dimension three. Multiplication P(E)×P(E)→P(Sym²E) is finite onto its image: a quadratic product has only its two ordered factorizations (one on the diagonal). Therefore the pullback of the hyperplane linear system is ample and basepoint-free. A general hyperplane section S of Z is integral by Bertini, has dimension two, and meets the compatible rank-two open densely.

If both factor images of Z have dimension at least two, both images of S have dimension two. For a two-dimensional factor image, general fibers of Z have dimension one, and an ample divisor meets every projective positive-dimensional fiber, so S dominates that image. For a three-dimensional factor image, the projection is generically finite, and S has two-dimensional image. Thus S contradicts the five-space compatible-surface classification, which forces a point or line factor image. Consequently one factor image of Z has dimension at most one.

A point image is impossible: for a fixed a the square-avoiding compatible locus has dimension at most two. The elementary proof is Section 3 of https://github.com/Akilleez-QA/read-em-and-weep/blob/59a2aa5db85baeb0da1ff467c4f72d77a41ae488/research/hm/universal-polar/full-support-rank-five-dimension-bound/PROOF.md; it does not use dim K=5. Explicitly set M_a={b:ab∈K}; when M_a=E, the pencil b↦v(ab) modulo Ca minus λ(b modulo Ca) has generic rank three, and every exceptional kernel has dimension at most three because a zero map would make a² compatible. The other cases have projective dimension at most two.

Hence the first factor image is an integral curve C. Every two-dimensional irreducible component of a general fiber is, by the same pencil argument, a plane P(U), dim U=3. The general fiber need not be geometrically integral. To handle its possible monodromy, take an irreducible curve Γ in the relative Grassmannian parametrizing these plane components and dominating C generically finitely; equivalently split the finitely many geometric generic plane components after a finite function-field extension and close one of them. Write a_γ for its first factor and U_γ for its plane. Also a_γ∉U_γ: otherwise two paths a_γ(a_γ+tb), a_γ(a_γ+tc), with b,c independent modulo a_γ in U_γ, imply v(a_γ²)∈Ca_γ. In the next section, subscripts a and b denote chosen general points of Γ above their first factors; no descent of the planes to C is assumed.

## 3. NEW: a curve of compatible planes in a six-space must be a line

For general points of Γ with first factors a,b∈C, the spaces aU_a and bU_b have zero intersection. Otherwise, since aE∩bE=C(ab), a nonzero intersection forces b∈U_a. If this held for general pairs in Γ×Γ, then for a fixed general point of Γ above a the dense set of first factors b of general points of Γ would lie in P(U_a). Closedness gives C⊂P(U_a), hence a∈U_a, a contradiction.

Choose a general pair with zero intersection. Since both spaces have dimension three,

  K=aU_a⊕bU_b⊂LE,  L=span(a,b).

For any general c∈C outside P(L), the inclusion cU_c⊂LE implies U_c⊂L: reduce modulo L in Sym²(E/L), where c-bar times z-bar vanishes only when z-bar=0. This contradicts dim U_c=3. Thus the entire integral curve C is the line P(L).

This argument is independent of the five-space surface classification.

## 4. NEW: the line case also forces a forbidden compatible square

The multiplication subspace LE has dimension seven (kernel Λ²L of L⊗E→Sym²E has dimension one). Since K has dimension six and K⊂LE, choose a nonzero functional ℓ on LE with kernel K. Write

  B(a,z)=ℓ(az),  a∈L, z∈E.

For general [a]∈P(L), B(a,−) is nonzero and U_a=ker B(a,−); otherwise K would contain LE. Compatibility holds throughout the rank-two part of aU_a. The quadratic d(a)=B(a,a) is nonzero because a∉U_a generally. It has a projective root [a0] over C.

If B(a0,−)≠0, the kernel planes extend regularly to U0=ker B(a0,−), and d(a0)=0 implies a0∈U0. If B(a0,−)=0, choose a1 independent of a0. Then B(a1,−)≠0 and all generic kernel planes equal U0=ker B(a1,−). Symmetry on L gives B(a1,a0)=B(a0,a1)=0, again a0∈U0.

In either case a0U0⊂K and its entire rank-two open is compatible. For precision, locally extend any z∈U0 to a regular section z(t) of the extending kernel bundle, along a(t)→a0. The rank-two pairs a0,z independent lift to rank-two pairs nearby. The polynomial compatibility equation v(az)∧a∧z=0 then specializes and is equivalent to compatibility at these independent pairs.

Choose b,c∈U0 independent modulo Ca0. Compatibility on the two lines a0(a0+tb) and a0(a0+tc), t≠0, implies on specialization

  v(a0²)∈span(a0,b)∩span(a0,c)=Ca0.

Since a0²∈K, square avoidance is contradicted. The hypothetical threefold is impossible, completing the proof.

## Scope and audit checks

The theorem bounds reduced-support dimension, not tangent spaces or scheme multiplicity. For the actual operation the outer-lift map adds no parameter; restoring all three nonzero input scales adds exactly three dimensions. The bound under (H) is 2 middle parameters + 2 fiber parameters + 3 scales = 7.

All statements use abstract tensor geometry. 
