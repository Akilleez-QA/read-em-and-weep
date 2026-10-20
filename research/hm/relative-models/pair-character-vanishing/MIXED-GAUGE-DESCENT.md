> Publication scope: Explicit two-factor pushforward splitting gives H0/H1 vanishing; mixed gauge comparison still imports actual source identities. Source-stage audit/checker references describe historical evidence, not fresh execution or bundled executable artifacts. Named source identities are hypotheses unless separately proved below.

# Mixed curvature, gauge matching, and finite-quotient descent

## Conclusion and hypotheses

The structural pair-character vanishing in PROOF.md supplies the missing uniqueness-up-to-gauge step. Under the imported actual-source premise S (the first-lift/mixed identities and their arbitrary-tuple extension in the source-family notes), it implies covariance of the actual mixed class under deck-equivariant ordinary bundle isomorphisms wherever the two relevant pair-character H¹ groups vanish.

Consequently a finite coefficient-space group acting by such ordinary bundle isomorphisms preserves the actual mixed-class zero scheme on a group-stable open neighborhood where these vanishings and the relative obstruction bundle hold. On its free-action locus this closed scheme descends to the finite quotient. The audited monomial-symmetry theorem supplies an established group of degree 500, its ordinary full-chain isomorphisms and free coefficient-locus quotient, as bound explicitly in §5 below. This note does not extend the pair-character vanishings to the entire generating locus.

No claim is made that the zero scheme contains any point, is nonempty, or equals the whole parameter space.

## 1. The exact mixed algebra and the weighted gerbe

Let p=(0,1), q=(2,3), using the source's zero-based indexing. On any permitted coefficient base A use the fixed associative algebra

𝒜=O_(X_A)[t,u]/(t²,u²),
F⋆G=FG+t μ_p(F,G)+u μ_q(F,G)+tu μ_pq(F,G).

This is precisely the commuting-field exponential product in FIRST-LIFT-STRUCTURAL §7, including its displayed coefficient μ_pq. The physical derivations commute, act on separate elliptic factors, and kill A. Thus the product is valid under all coefficient base changes, including nonreduced ones.

The prescribed scalar cocycle is

c_ijk=(1+t b_p,ijk)(1+u b_q,ijk).

Source §8 proves the exact complementary derivative vanishings

V₂b_p=V₃b_p=0,    V₀b_q=V₁b_q=0.

These imply c⋆F=cF=F⋆c for EVERY local matrix F over 𝒜. Indeed the only potentially surviving star correction from t b_p is tu μ_q(b_p,F₀), which is zero, and the only one from u b_q is tu μ_p(b_q,F₀), also zero; all other corrections have t² or u² as a factor. The same argument applies on the other side. The tu b_p b_q term has no surviving derivative corrections. This is a claim about the parameter-weighted c, not a false claim that b_p or b_q alone is central in the whole product.

Each b_r is an ordinary additive Čech cocycle. Since c=exp(t b_p+u b_q), its ordinary multiplicative Čech cocycle law follows. Its star products are the same ordinary products by the preceding calculation. Hence c is an actual fixed central gerbe for this truncated mixed algebra, with the exact source convention.

## 2. The actual curvature class

Set T⁰_ij=g_ij+t U_p,ij+u U_q,ij. The actual first-lift equations imply

T⁰_jk⋆T⁰_ij−c_ijk⋆T⁰_ik=tu D_ijk.

This is the ten-term D of source §7; centrality above explains why its ordinary c multiplication is also star multiplication. Normalize M_ijk=g_ik^−1D_ijk. Associativity and the fixed central cocycle give δM=0, consistently with the independently proved source closure.

Adding a mixed transition term tu K_ij changes M by the ordinary End(E)-valued Čech coboundary of g_ij^−1K_ij, with the row convention in those sources. Therefore [M] is the lifting-obstruction class for this specific mixed algebra and gerbe.

The exact source identity is R=tf(M)+δW. Thus the actual source class satisfies

[R]=tf([M]).

Ordinary trace-free projection commutes with Čech differential and ordinary conjugation. This equality, rather than an assumed equality of raw representatives, binds the gauge argument to the actual residual. No assertion that the scalar part of [M] vanishes is needed.

## 3. Ordinary transport is followed by first-order gauge matching

Let h:E→E′ be a deck-equivariant ordinary bundle isomorphism over the SAME X and coefficient base, represented by H_i. Choose the same physical fields and the same legal root labels, and refine the two carrier covers to a common cover. Then c is literally the same scalar cochain on both sides.

Lift H_i to star-invertible matrices and transport transitions by

T_ij↦H_j⋆T_ij⋆H_i^(⋆−1).

Centrality of c proves covariance of the full mixed curvature. Its tu coefficient transforms by ordinary conjugation, because multiplication of tu by t or u is zero. Hence normalized [M], and therefore tf([M]), transport by the intrinsic End isomorphism.

At first order on branch r the transported coefficient is exactly

U′_r,ij=[H_j U_r,ij+μ_r(H_j,g_ij)−μ_r(g′_ij,H_i)]H_i^−1.

This is the established formula in invariant-first-star-lifting §3. The μ terms cannot be discarded. A deck-equivariant h, with the source's scalar root-frame deck signs, makes this raw first coefficient have endpoint character η′_iη′_jχ_r; its normalization (g′_ij)^−1U′_r,ij has pure End character χ_r, since μ_r contributes χ_r. Both this transported lift and the target's raw chosen lift solve the SAME first equation with the SAME b_r.

Their normalized difference is therefore an End(E′)-valued χ_r Čech 1-cocycle. If H¹(End E′)_χr=0, it is δa_r for a χ_r degree-zero cochain. The gauge 1+t a_p+u a_q on the axes ring A[t,u]/(t²,u²,tu) matches both first lifts simultaneously. Lift this gauge arbitrarily to the mixed ring; it remains invertible. Its transported transitions now agree with the target's raw transitions through both first orders, and differ only by some tu K_ij. Section 2 shows their mixed classes differ by a coboundary. Thus the ACTUAL class [R] is covariant, although the raw first lifts and raw residual cochains need not be covariant as formulas.

The H⁰ pair-character vanishing proves uniqueness of each matching gauge in the ordinary nonnegative Čech model. This is useful for coherence but is not necessary merely to prove equality of the obstruction classes. In another dg model one retains the higher-homotopy qualification in PROOF.md.

## 4. Relative scope and arbitrary base change

The central pair-character H⁰ and H¹ vanishings proved in PROOF.md extend by upper semicontinuity to an open neighborhood of the central tuple. For a finite group orbit consisting of ordinarily isomorphic deck-linearized bundles, they hold at every orbit point. Intersect the relevant open loci and their finitely many translates to obtain a group-stable neighborhood of that orbit.

This neighborhood can also be intersected with the constant-dimension locus used for the rank-352 obstruction bundle, and with the free-action locus when required. The result is a group-stable OPEN locus, not necessarily one affine chart; use affine charts and common refinements for the cochain argument. If the free locus misses some orbit point, no neighborhood containing that point inside the free locus is asserted.

These pair-character vanishings persist under arbitrary base change in the requisite relative sense. Locally a perfect pushforward complex can, by splitting contractible summands, be represented with no terms in degrees below 2 when all its fibers have no cohomology below 2. Tensoring this representative with any base ring still has no such terms. Thus the relative degree-zero and degree-one groups vanish even on nonreduced base changes. On affine parameter patches, Leray then gives the corresponding absolute degree-zero/one vanishings needed to solve the family Čech matching equations. Equivalently the gauge match exists locally on the parameter base and is unique where H⁰ vanishes.

This step is important: checking only complex points would not by itself prove equality of ideal sheaves or scheme-theoretic descent.

## 5. Finite quotient

Take Γ=μ₅²⋊AGL(1,5), the projective monomial group of degree 500 established in ../../cubic-loci/foundation-p02/MONOMIAL.md, §§5–8, with its independent audit in that directory. Its full-chain blocks are constant on X. The pulled-back complex has terms N^(2j+1) with the fixed natural deck linearization, and all coefficient sections descend to Y. Therefore these constant blocks commute with the deck action on every term and induce deck-equivariant ordinary bundle isomorphisms between the coefficient tuples. Their compositions satisfy the group law up to scalar by the canonical projective-coherence theorem there. Changes of normalized projective coefficient charts can introduce scalar coefficient-base units, but physical derivatives kill such units. No linearization of H itself is claimed or needed. Scalar ambiguity acts trivially on End, so it supplies an honest Γ-linearization of the relative End complex and of V=(R²π_*End 𝓔)_χ wherever V is locally free. Scalars pulled back from the coefficient base are killed by the physical derivations, so they do not introduce a star-transport defect either.

The preceding transport-and-gauge argument proves Γ-equivariance of the actual relative section r=[R] of V. The full-sign purity theorem identifies this with the entire source mixed class, rather than just one projected component. Therefore its image ideal

I=im(V∨→O_B),  λ↦λ(r),

is Γ-stable. On a free finite-group locus in characteristic zero, B→B/Γ is finite étale and faithfully flat. Equivariant quasi-coherent descent gives a descended vector bundle, section, ideal, and closed zero scheme. The pulled-back descended zero scheme is exactly the original actual mixed-class zero scheme, including its nonreduced scheme structure.

For this established free degree-500 quotient, this proves descent of the actual total mixed-class zero scheme on the stated invariant open under the named actual-source premise S. It does not require individual raw source formulas to be group-covariant. It does require the actual source identification, the fixed disjoint-pair product and gerbe, the ordinary bundle symmetries, and the neighborhood restrictions above.

## Inputs read and audit boundary

Static inputs:
- imported-premise:invariant-first-star-lifting/PROOF.md (not bundled), especially §3;
- ../relative-obstruction-locus/PROOF.md;
- ../relative-mixed-character-purity/PROOF.md;
- ../relative-mixed-character-purity/dependencies/FIRST-LIFT-STRUCTURAL.md, §§7–8;
- PROOF.md in this directory;
- ../../cubic-loci/foundation-p02/MONOMIAL.md and its independent AUDIT.md (audited proof SHA-256: 1b96861d7404cf6e4e2c3de3ca8c13496b5f01a70b73e0d8f6f1291e86ba8042).

The actual-source premise S remains imported; this note does not reauthenticate all primitive identities or source identifications appearing in those dependency snapshots. Over a nonclosed characteristic-zero field, Γ denotes the full finite étale group scheme of degree 500. It does not mean only the subgroup of rational points. The argument can be checked after a separable extension and descends by the canonical projective coherence.

Only formal algebra, cohomology, and static source reading were used. No source/model/rank/polynomial-instance/point/jet/residual execution or evaluation was performed.
