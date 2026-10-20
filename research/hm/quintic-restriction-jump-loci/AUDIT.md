# Historical mathematical audit receipt

This is a preserved review of the source mathematical manuscript, not a fresh review of the publication bytes. Hashes quoted below identify the historical source versions. See [hm-quintic-restriction-PUBLICATION-CHECK.md](../hm-quintic-restriction-PUBLICATION-CHECK.md) for the final-publication review.

# Independent audit of restriction deformation jump loci

## Verdict and audited version

**Pass**, with the previously established cohomology and representation theorem retained as explicit inputs. No substantive gap was found. The argument proves simplicity and the stated Ext dimensions for every smooth quintic, basepoint-freeness of the auxiliary kernel, smooth members in every affine fiber, and the conditional quadratic jump geometry. It does not determine the scalar c.

Audited [PROOF.md](PROOF.md) SHA-256:

`5009e39fe76a0971e96ef1473946187525283e0c5cbb1312b2c52b0f1b08f39a`.

Supporting files independently read:

- [Pairing theorem](../quintic-pairing-representation/PROOF.md), SHA-256 `6c4036d50840eac5a2f9b4face17894fb6a1cc821a758de29edeb1731f722624`.
- [Pairing audit](../quintic-pairing-representation/AUDIT.md), SHA-256 `99a5be1438674f831bf64170b849d4dd22bff98ed3cbb6af7491cb9520960d4c`.
- [Established End-cohomology audit](../pairing-foundation-inputs/COHOMOLOGY.md), especially items 4–6.

The numerical row and identification of the literal HM bundle are imported established results. This audit does not claim to re-prove the original published cohomology proposition or independently re-identify the monad.

## 1. Restriction exact sequences and simplicity

The trace-free bundle B is locally free, and multiplication by a nonzero hypersurface equation is injective on it. The restriction sequence therefore has no missing Tor term. The supplied row gives H⁰B=H¹B(−5)=0, hence H⁰(B|X)=0. This is enough for simplicity after adjoining the scalar summand; stability of the restriction is unnecessary and is not asserted.

At the two middle degrees, the exact sequence is

    0 → H¹B → H¹(B|X) → H²B(−5) → H²B
      → H²(B|X) → H³B(−5) → 0.

Thus both middle dimensions equal 24+2−rank(m_p). Trace/Serre duality identifies H²B with U*, and the multiplication map m_p has the rank of Φ(p). The final segment also gives H³(B|X)=0, using H³B=H⁴B(−5)=0. The scalar cohomology on a smooth quintic is (1,0,0,1). Consequently

    dim Ext^i_X(E,E) = (1, 26−rank Φ(p), 26−rank Φ(p), 1).

Local freeness of E justifies Ext^i=H^i(End E). The characteristic-zero trace decomposition commutes with restriction. The fixed-determinant statement is correct because both middle scalar cohomology groups vanish. Ext² is an obstruction space, not a computation of the obstruction map or actual local moduli dimension. All these distinctions are preserved in the proof.

## 2. Kernel basepoint-freeness and central conventions

Surjectivity of the nonzero intertwiner Ψ uses the established irreducibility of its three-dimensional target. Its dual embeds the dual target into S₅*. Since H₅ acts trivially on the target and its dual, every vector in K-perpendicular is fixed by H₅. This is a claim about invariant functionals, not an identification of invariant sections with their duals.

With P(V) parametrizing lines and the action on sections given by inverse substitution, direct substitution into the dual action yields h·ev_v=ev_(hv). The central element ζI has weight ζ on V and ζ⁻¹ on V*. Both fifth symmetric powers have trivial central weight. This matches the pairing theorem and introduces no character twist.

A base point [v] of K would put the nonzero evaluation functional ev_v in K-perpendicular. Equivariance and injectivity of the fifth Veronese map then make [v] a common H₅-fixed point. A common projective fixed point is precisely an invariant line in V, excluded by the irreducible five-dimensional Schrödinger representation. There is no use of the false assertion that each group element separately acts without fixed points. Absence of base points is equivalent to surjectivity of K⊗O→O(5), since the target is a line bundle. The reasoning is valid.

## 3. Bertini through incidence and generic regularity

For a basepoint-free subspace L, the kernel of evaluation is a vector bundle. Its projectivization is the universal incidence I_L and is smooth over C. The projection f:I_L→P(L) is projective, of finite presentation, and dominant: every nonzero positive-degree homogeneous equation on P⁴ has a zero. In particular its generic fiber is nonempty.

The regularity claim concerns the *whole generic fiber*, not merely its generic point. On affine charts above an integral affine chart Spec A of the base, passing to the generic fiber replaces a regular coordinate ring R by the localization R⊗_A Frac(A). All of its local rings remain regular. The function field Frac(A) has characteristic zero and hence is perfect, so this finite-type regular fiber is smooth over that field. This implication is covered by [Stacks Project, Lemma 33.25.8](https://stacks.math.columbia.edu/tag/04QM).

For completeness, smoothness of the generic fiber implies f is smooth at every point over the generic point: flatness there is automatic because the base local ring is a field, and f is locally of finite presentation. The pointwise criterion and openness of the smooth locus are in [Stacks Project, Lemma 29.35.14 and Definition 29.35.1](https://stacks.math.columbia.edu/tag/01V4). The complement of that smooth locus is closed; properness of f makes its image closed. That image avoids the generic point. Its complement in P(L) is therefore a nonempty open set with smooth fibers. No immersion or jet-separation condition on the map defined by L is required.

These details justify the compressed generic-fiber step in the proof rather than amend its conclusion. Perfectness is essential to this particular regular-to-smooth argument; the proof explicitly works over C.

## 4. Every affine fiber

For q≠0, any abstract preimage p₀ is outside K. Consequently L=K⊕Cp₀ and the complement of P(K) in P(L) is exactly the affine chart whose points have the unique representative p₀+k. This gives an isomorphism with Ψ⁻¹(q). Basepoint-freeness passes from K to L. The smooth-member open set intersects this chart because P(L) is irreducible and both opens are nonempty. Smoothness is unchanged under nonzero rescaling of an equation, so this intersection gives precisely a nonempty open subset of smooth quintics in the affine fiber.

For q=0, the nonempty smooth-member open subset of P(K) pulls back under K\{0}→P(K). Since K\{0} is open in K, the pullback is also a nonempty open subset of the affine zero fiber. This spells out why the zero-fiber assertion has the same affine-open meaning as the other fibers. The zero polynomial itself is excluded.

The argument applies Bertini only to actual linear systems, then passes to a chart. It does not improperly apply linear-system Bertini directly to a translate. It is entirely existential and makes no coefficient choice or polynomial evaluation.

## 5. Determinantal geometry

Surjectivity of Ψ makes a,b,d independent linear forms. The quadratic ad−b² is nondegenerate on the three-dimensional quotient S₅/K, and its pullback has rank three and radical K. A rank-three quadratic over C is irreducible: a product of linear forms would have rank at most two. Its projective hypersurface has dimension 124, singular locus P(K), and vertex P(K), of dimension 122 and codimension three in P¹²⁵.

Away from the vertex the hypersurface is smooth. Its points have matrix rank one; outside the hypersurface the rank is two. These are parameter-space smoothness statements, unrelated to smoothness of any deformation moduli space. Every rank occurs among symmetric forms on a two-dimensional vector space, and every target fiber contains smooth quintics. Consequently no stated stratum vanishes on intersection with Ω. The matrix determinant and the binary-quadratic discriminant differ by the stated nonzero factor and sign; neither is the hypersurface-singularity discriminant of quintics.

## 6. Scalar equivalences and boundary

When c=0, all smooth restrictions have middle Ext dimensions 26. When c≠0, the established smooth fibers of rank-one and rank-two targets provide restrictions of dimensions 25 and 24, respectively. This proves each stated equivalence involving absence or existence of these dimensions. The smooth zero fiber also shows why existence of dimension 26 cannot characterize c=0. Since V(Q) is a proper hypersurface and its rank-two complement meets Ω, a general smooth quintic has dimension 24 conditional on c≠0.

Nothing here proves c≠0 or c=0. No actual HM map, selected quintic, polynomial instance, rank certificate, obstruction value, or conductor cofactor was evaluated. Only static proof files, source references for the geometric facts, abstract reasoning, and file hashes were used. No external application was written or changed.
