# Current independent mathematical review

Date: 20 October 2026. Verdict: scoped PASS for the exact edition bound in CURRENT-REVIEW-BINDING.json.

## Mathematical verification

The four-term exponential character has coefficients (2,0,-15,0,75/4). For the stipulated rank-two bundle this gives c1=0, c2=15 theta^2, discriminant 60 theta^2, and ch(End_0 F)=3-60 theta^2+300 theta^4. The nonzero pairing is 1440. The abelian-base HRR value is 7200, an Euler characteristic rather than a cohomology dimension. The rank-two fourth-character identity is consistent with these coefficients.

A holomorphic connection yields a Chern-character representative of type (2j,0), while the Hermitian Chern connection gives type (j,j). Compact Kähler Hodge decomposition forces positive-degree classes to vanish. A holomorphic projective-frame connection induces a holomorphic adjoint connection, so the adjoint second character excludes it without assuming a GL lift. This is precisely the needed consequence of Biswas–Dumitrescu, arXiv:2312.01399v1, Lemma 2.1 on printed page 4, which was read directly. Its cited Atiyah theorem was not separately inspected. The stronger flat-existence theorem is unnecessary.

Line twists preserve the adjoint bundle and discriminant. A smooth projectively flat connection gives a flat adjoint connection and contradicts its nonzero real second character; arbitrary smooth connections are not excluded. The trace-free Atiyah class is the obstruction to splitting the projective Atiyah sequence, so it is nonzero and unchanged by line twists under the canonical endomorphism identification.

For proper generically finite surjective holomorphic q:Y→X between smooth compact fourfolds, the complex orientation makes the generic degree positive, and the degree formula gives the nonzero characteristic pairing 1440 deg(q). No positivity of q*theta is required. Compact Kähler Y is needed for the holomorphic-connection argument, but not for the smooth projective-flatness contradiction. Neither ramification nor exceptional divisors affect this cohomological pairing. The general-source Euler characteristic is not inferred by scaling the abelian-base result.

## Source and overlap review

The characteristic computation and finite étale consequences already occur in public comment 6257575487 and PR105. This edition supplies a reviewed proper-generically-finite extension and explicit trace-free Atiyah consequence; it does not recount the old characteristic computation as novel. The geometric source and precise public editions are bound in IMMUTABLE-DEPENDENCIES.json. The existing A/geometric identification and K-class remain assumptions; no local source operation or rank is reverified.

The historical status language is qualified by SCOPE.md. The later conditional mixed-obstruction vanishing theorem in PR145 concerns a different assertion and does not produce an excluded global holomorphic connection. Conversely the present obstruction computes no mixed-module value. All mathematical formulas in the preserved proof and addendum were reviewed; only scope/provenance/review material was added to this edition. This is static mathematical review and byte authentication, not formal proof-assistant certification or a source computation.
