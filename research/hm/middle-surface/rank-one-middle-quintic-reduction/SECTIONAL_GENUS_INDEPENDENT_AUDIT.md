# Independent audit: sectional genus of the invariant integral quintic

## Scope and verdict: PASS

The proposed theorem is mathematically correct over the established algebraically closed characteristic-zero ground field: an integral invariant quintic surface Y in P4 with the established Heisenberg Hilbert congruence and irreducible ambient representation has sectional arithmetic genus exactly one. This audit checks the geometric argument independently and reviews the completed SECTIONAL_GENUS.md.

No normality, smoothness, local Cohen–Macaulayness everywhere, arithmetic Cohen–Macaulayness, or linear normality hypothesis on Y is needed. No source application was changed and no source tensor, operation, matrix, jet, or evaluation was performed.

## 1. The potentially delicate hyperplane-section issue

An integral finite-type surface is Cohen–Macaulay at all points of codimension zero or one: the corresponding local rings are respectively fields or one-dimensional Noetherian domains. The Cohen–Macaulay locus is open for a scheme of finite type over a field. Consequently its complement on Y is a finite set of closed points. A general hyperplane H avoids this set.

The hyperplane equation is a nonzerodivisor on O_Y because Y is integral and is not contained in H. Therefore C=Y intersect H is a locally Cohen–Macaulay curve. In particular it has no embedded associated points. Bertini irreducibility gives irreducible support, and Bertini on the smooth locus of Y gives generic reducedness. A general section is not contained in the singular locus of Y, whose dimension is at most one. Generic reducedness plus the absence of embedded associated points implies that C is reduced. Thus C is integral as a scheme, not merely generically integral.

This explicitly resolves the possible non-S2/non-Cohen–Macaulay surface concern. It would be insufficient merely to assert irreducibility of the support and then compute its reduced genus.

Primary reference for irreducibility: [Stacks Project, Bertini theorems](https://stacks.math.columbia.edu/tag/0G4C).

## 2. Nondegeneracy is retained

The linear span of invariant Y is an invariant projective linear subspace. Its underlying nonzero vector subspace is invariant under the lifted Heisenberg representation. Irreducibility of that five-dimensional representation forces the span to be all P4.

To check that C spans H=P3, use the exact sheaf sequence

    0 -> O_Y --ell--> O_Y(1) -> O_C(1) -> 0.

Since Y is integral and projective over the algebraically closed field, H0(O_Y) is one-dimensional. The five independent ambient linear sections in H0(O_Y(1)) therefore restrict to a four-dimensional subspace of H0(O_C(1)). Equivalently the only ambient linear form vanishing on C modulo those vanishing on Y is the equation ell of H. Thus C is nondegenerate in H, and h0(C,O_C(1))>=4. This does not require any vanishing of H1(O_Y) or linear normality.

## 3. The weak genus bound works for singular curves

Choose a sufficiently general point of P3 outside C and project C to P2. The induced morphism f:C->D is finite and birational onto an integral plane curve D. One precise justification is Stacks Project Lemmas 43.23.1 and 43.23.2(1): fix a smooth point of C; general projection is finite and is an isomorphism over a neighborhood of its image, hence is birational.

The projection linear system is basepoint-free on C and consists of sections of O_C(1), so f*O_D(1)=O_C(1). Since f has degree one, D has degree five. No normalization of C is substituted in this assertion.

There is an exact sequence

    0 -> O_D -> f_*O_C -> Q -> 0,

where Q has finite support and length q>=0. Since a plane quintic has arithmetic genus six, Euler characteristics give

    p_a(C)=6-q.

If q=0, f is an isomorphism: a finite morphism is the relative spectrum of its direct-image algebra. Then the line-bundle identity gives h0(C,O_C(1))=h0(D,O_D(1))=3, contrary to nondegeneracy. The last equality follows from

    0 -> O_P2(-4) -> O_P2(1) -> O_D(1) -> 0

and H1(P2,O_P2(-4))=0. Therefore q>=1 and p_a(C)<=5. Finally C is integral and proper, so h0(O_C)=1 and p_a(C)=h1(O_C)>=0.

This is a bound on arithmetic genus of C itself; singularities and the normalization genus do not cause a gap.

Primary projection reference: [Stacks Project, Projections, Lemmas 43.23.1–2](https://stacks.math.columbia.edu/tag/0B1N).

## 4. Congruence and conclusion

For

    P_Y(t)=5 binom(t,2)+(6-g)t+chi(O_Y),

the regular hyperplane exact sequence gives

    P_C(t)=P_Y(t)-P_Y(t-1)=5t+1-g.

Thus g is exactly the arithmetic genus just bounded. The already established congruence g=1 modulo 5, together with 0<=g<=5, forces g=1.

This conclusion does not by itself prove chi(O_Y)=0, smoothness, normality, existence, classification, or exclusion of Y. The separately established condition chi(O_Y)=0 modulo 5 remains a congruence only.

## Final draft review

Reviewed the completed SECTIONAL_GENUS.md: PASS for the theorem and its main proof (Sections 1–4 and 6). Its argument improves the independently checked generic-projection route above: for any center p outside C, projection is finite; degree multiplicativity gives 5=[k(C):k(D)] degree(D), while nondegeneracy excludes degree(D)=1. Primality of five forces a birational plane-quintic image. This is correct and removes any need for a generic-projection theorem.

The Stacks Lemma 37.32.3 hypotheses cited in the draft were checked against the primary source and hold as stated. No missing reducedness, embedded-point, normality, or polarization assumption was found.

The supplementary sharper Castelnuovo discussion in Section 5 is not needed for the theorem and its bibliographic claims were not independently audited here. The PASS does not rely on them. The decisive conclusion remains g=1, with chi(O_Y) only constrained modulo five.
