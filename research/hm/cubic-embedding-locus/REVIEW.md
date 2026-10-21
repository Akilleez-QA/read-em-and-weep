# Independent review: exact cubic embedding locus

Verdict: **PASS**, relative to the explicitly pinned inputs. No mathematical gap was found in Theorem (a)–(d). This is an independent mathematical review, not formal proof-assistant verification.

Reviewed file: `PROOF.md`, final SHA256 `75afda202609d76b2780bfeff6824c6780457bf39a6b21a9306bdd9430b17601`. The review began with SHA256 `fc6c8d72e2440327db94089e6160c44def3199d16d0e7febd8c589f7a88c2e43`; the final version changes only its status sentence to record this review, not its mathematics.

The review read the complete proof and the local pinned predecessor proofs for PR602 and PR603, checked the actual-primary/modular dictionary and the stabilizer representation input, and independently checked the cited BHM passages against the published PDF. No actual coefficient, matrix, source point, jet, numerical rank, or kernel intersection was selected or evaluated. In particular this review does not determine the common dimension r.

## 1. The line classification is exhaustive

For a line in S, the reduced closure of its inverse image away from Z is integral and finite birational over that line. Its coordinate rings lie in the line's function field and are integral over its integrally closed coordinate rings, so the map is an isomorphism. This argument does not assume that the whole inverse image of the line has no extra isolated points.

The resulting rational curve C has H.C=1. The nef fiber class gives n=F.C>=0. If n>0, then (5I).C=5-10n<0. Since the class 5I has the effective representative consisting of the torsion sections, positivity of intersection of distinct integral curves on the smooth normalization forces C to be one of those sections. If n=0, C is an irreducible fiber component. The stated fiber configuration then supplies exactly the other sixty possibilities. Distinctness of the images follows from injectivity of normalization off a finite set.

The modular geometry also gives the required precise node incidence: the twenty-five section lines are node-free, and each component line has exactly two distinct node endpoints. In particular the proof correctly rejects the incomplete twenty-five-line classification. It makes no assertion about reducedness of the Fano scheme.

## 2. Cubic restriction is proved, rather than inferred from degree

The irreducibility proof for Sym^3(R*) is sound. Perfectness and the central sign exclude one-dimensional constituents. A reducible four-dimensional representation must therefore contain a two-dimensional invariant subspace. A base divisor of its cubic pencil would be invariant and of degree at most three. Faithfulness of the projective A5 action and cyclicity of point stabilizers imply that every orbit has at least twelve points, excluding such a base divisor. The resulting degree-three morphism has an invariant ramification divisor of degree four, again impossible. The equivariant, nonzero restriction map is consequently surjective.

Thus the HM-line restrictions are the complete cubic systems, not merely basepoint-free subsystems of O(3). On each two-node component line, the generated bundle O(1) necessarily has its complete two-dimensional section space. Both line-restriction assertions are genuine embeddings.

## 3. Incidence kernels and exceptional intersections

PR602's proportional-cubics argument applies exactly where a positive-dimensional incidence kernel meets the complement of S. Its principal image ideal defines the scheme-theoretic intersection with the reduced node scheme, forcing a line with three distinct nodes. PR603 excludes this. A linear space of dimension at least two contained in the integral degree-fifteen surface would force S to be a plane, so every remaining positive-dimensional incidence kernel is a line from the established list. Hence B has rank three or four everywhere on V.

The identity Phi(E_z)=P(ker L(z)) follows from inclusion by incidence and equality of dimensions: both sides are linear P3s. It is not an assumption that the syzygies cut out all fibers. Linearity of L then gives the exact equality

    P(K_ell)=Phi(E_z) intersect Phi(E_w).

At a non-node point of ell, ker L has dimension two, so dim K_ell<=2. Each point of this intersection has two distinct preimages because the two exceptional divisors are disjoint. Its incidence kernel contains ell and hence equals ell. Belonging to intersections associated with two distinct lines would force a projective kernel of dimension at least two. This proves pairwise disjointness, including for component lines sharing an endpoint node.

## 4. The ambient point and tangent argument is complete

At rank four, q Phi=pi proves that two preimages must lie in one pi-fiber; the embedding on an exceptional divisor handles the only nontrivial possibility. For tangent separation, the displayed blowup chart correctly proves ker(dpi)=T(E_z) at an exceptional point. Since Phi restricted to E_z is a linear embedding, no nonzero ambient tangent vector is lost. This explicitly handles all ambient exceptional directions, not only tangent vectors to Y.

At rank three outside Sigma, a component-line kernel would put the target in the corresponding exceptional-image intersection. Thus only a node-free HM line can occur. The fiber is confined to that line and has one point by its cubic embedding. Differentiating the homogeneous incidence identity with dPhi(v)=0 gives B(y)dx=0 modulo the source point, so dpi(v) is tangent to that same projective kernel line. Its cubic immersion then forces v=0. This inference is valid in projective tangent spaces and uses no converse incidence assertion on S.

## 5. Finite separation really gives an isomorphism

The local algebra in Section 7 is correct. For finite birational A subset B with one point above the closed point, B is local and has the same residue field C. Tangent injectivity gives m_B=m_A B+m_B^2. Nakayama applied over B to m_B/m_A B gives m_B=m_A B. Thus B=A+m_A B, and the finite A-module B/A equals m_A(B/A), so a second Nakayama application gives B=A. The coherent normalization quotient then vanishes on a neighborhood.

Consequently the normalization is an isomorphism off Sigma, and that open subset of V is smooth. Every point of Sigma has at least two normalization preimages and is therefore nonnormal, hence singular. This proves both claimed reduced-locus equalities, not just containments. No unjustified claim about scheme structure or local analytic type is made.

For the surface, restricting the ambient isomorphism identifies the reduced closed image T minus Sigma with the corresponding open subset of the smooth closed surface Y. This proves smoothness and the stated isomorphism there. It does **not** prove that every point of T intersect Sigma is nonnormal on T, and the theorem and its boundary explicitly refrain from that stronger assertion.

## 6. Symmetry and source audit

The BHM passages checked were Section 3.3, Proposition 6 and its proof (printed pp.50–51); Section 4.2 (p.57); Section 4.3, Lemma 9 (pp.58–59); Lemma 12 and Proposition 9 (pp.63–64); and Section 5.2, Proposition 13 (p.69). They support, respectively, cusp transitivity, section/component incidence and the group action, the divisor-class relation, component degree and vertex pairing, and the identification of section images with HM lines. Proposition 13 is not an exhaustive line classification.

Source: [Barth–Hulek–Moore, Shioda's Modular Surface S(5) and the Horrocks–Mumford Bundle](https://mathweb.tifr.res.in/Documents/Publications/Studies/Vector-Bundles-On-Algebraic-Varieties.pdf).

The within-fiber transitivity argument is valid: the translation group's image in the pentagon automorphism group is contained in the rotations, and it cannot be trivial because a transitive action on all twenty-five sections cannot preserve each proper five-section incidence subset. A nontrivial subgroup of the order-five rotation group is the whole group. Combined with cusp transitivity this gives one orbit of sixty component lines. Transport through the actual-primary dictionary and the invariant complete cubic system makes the exceptional-image intersections equivariant, without choosing equivariant resolution matrices.

Thus all sixty dimensions equal one r in {0,1,2}. The alternatives and the equivalence between r=0, normality of V, and a closed immersion of the resolved cubic map follow exactly as stated. No value of r follows from this review, and none was sought.

## Conclusion

The proof establishes a new exact reduced singular/nonnormal locus for the finite ambient normalization and an isomorphism everywhere outside it. The unresolved obstruction is precisely the common, unevaluated intersection dimension r. The separate normalization behavior of T along T intersect Sigma and all larger lifting/algebraicity goals remain outside the result.
