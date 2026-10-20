> Scope: Historical unknown-value language describes what this argument does not decide, not the current status of later results. All stipulated geometric/source assumptions remain explicit. No actual source evaluation is asserted.

# Global connection obstruction: independent audit

## Verdict and dependency boundary

The claims in PR #1 comment 6257575487 are correct under its imported A/geometric premises: X is the compact complex abelian fourfold, F is the identified holomorphic rank-two bundle, theta=c1(N), and integral_X theta^4=24. The four-term expression must represent [F] in K-theory under those premises. This audit does not independently establish that geometric identification or any differential-map rank.

Source audited: https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6257575487 (created and last updated 2026-10-19 01:15:21 UTC).

## Universal characteristic arithmetic

Expanding -5 exp(-t)+15 exp(t)-10 exp(3t)+2 exp(5t) through degree four gives coefficients (2,0,-15,0,75/4). Therefore

ch(F)=2-15 theta²+(75/4) theta⁴,
c1(F)=0, c2(F)=15 theta²,
Delta(F)=4c2(F)-c1(F)²=60 theta².

In particular integral_X Delta(F) theta²=1440, so the discriminant and ch2(F) are nonzero in real cohomology. Dualization changes the signs of odd Chern-character components, which here vanish. Multiplication and removal of the scalar summand give

ch(End_0 F)=ch(F)ch(F*)-1=3-60 theta²+300 theta⁴.

The top coefficient is 4(75/4)+(-15)²=300. Since the tangent bundle of an abelian variety is trivial, td(X)=1; Hirzebruch–Riemann–Roch yields chi(X,End_0 F)=300*24=7200. This is an Euler characteristic, not an individual cohomology dimension or matrix rank. The rank-two identity ch4(F)=c2(F)²/12 also checks: 225/12=75/4.

## Holomorphic and projective connections

A holomorphic connection extends using the given Dolbeault operator to a smooth complex connection whose curvature has type (2,0). Its degree-2j Chern-character representative thus has type (2j,0). A Hermitian Chern connection represents the same class with type (j,j). Compact Kähler Hodge decomposition has zero intersection between these distinct summands for j>0; if 2j exceeds complex dimension, the former representative already vanishes. Consequently every positive-degree Chern character vanishes for a bundle with a holomorphic connection, without assuming flatness. Nonzero ch2(F) excludes such a connection on F.

A holomorphic PGL(2,C) connection on the projective frame bundle would induce a holomorphic connection on its adjoint bundle End_0 F. Its nonzero ch2=-60 theta² gives a contradiction, without requiring a lift of the principal connection to GL(2,C).

The cited primary source is verified: Biswas–Dumitrescu, “Principal bundles with holomorphic connections over a Kähler Calabi–Yau manifold,” Lemma 2.1, printed page 4, states the vanishing of positive-degree real characteristic classes for a holomorphic principal bundle with a holomorphic connection over a compact connected Kähler manifold. Its proof uses induced connections in associated representations and cites Atiyah, Theorem 6, page 197. Only that lemma is needed; the paper's stronger Calabi–Yau flat-existence theorem is unnecessary.

https://arxiv.org/pdf/2312.01399#page=4

For any holomorphic line bundle L, End_0(F tensor L) is canonically End_0 F and Delta(F tensor L)=Delta(F). Thus twisting cannot repair either holomorphic obstruction. Likewise, a smooth projectively flat connection would induce a flat adjoint connection and force the adjoint Chern character to vanish in positive degrees. Ordinary smooth nonflat connections are not excluded.

For a finite étale cover q:Y→X of degree d, Y is compact Kähler and

integral_Y q*Delta(F) (q*theta)²=1440d != 0.

The same arguments apply to q*F, its projective frame bundle, and every line twist on Y. Disconnected covers may be checked componentwise.

## Additional structural consequence

The trace-free Atiyah class a_0(q*F) is nonzero for every finite étale cover. It is the extension obstruction to a holomorphic splitting of the projective-frame Atiyah sequence. If zero, that principal bundle would have the holomorphic connection just excluded. Under the canonical identification of trace-free endomorphism bundles, a_0(q*F tensor L)=a_0(q*F): twisting adds only the scalar Atiyah class of L. Thus the obstruction remains nonzero after all these covers and twists. In particular, the full Atiyah class of each such twisted bundle is nonzero as well.

## Limits

This rules out nonsingular global holomorphic or smooth projectively flat connections on the indicated bundles. It makes no existence claim or exclusion about connections on particular open sets, or with meromorphic singularities. It identifies no individual local current coefficient and licenses no deletion of overlap, curvature, or homotopy terms. All retained detector values remain undetermined. No physical matrices, operations, inputs, ranks, jets, or residues were evaluated; the only arithmetic was universal scalar-polynomial expansion.

## Addendum: proper generically finite pullbacks

The connection obstruction actually persists under every proper generically finite surjective holomorphic map q:Y→X with Y a smooth compact Kähler fourfold. Ramification or exceptional divisors do not affect the argument. Such a map has positive topological degree d, equal to its generic degree. Naturality of Chern classes and the degree formula give

integral_Y Delta(q*F) (q*theta)²
= integral_Y q*(Delta(F) theta²)
= d integral_X Delta(F) theta²
= 1440d != 0.

Equivalently integral_Y ch2(End_0(q*F)) (q*theta)²=-1440d. This does not require q*theta to be a Kähler class: it is only a test cohomology class, and its nonzero pairing proves that the characteristic class is nonzero. The Kähler assumption on Y is used separately for the holomorphic-connection vanishing theorem.

Consequently q*F and every holomorphic line twist of it admit no holomorphic connection; their projective frame bundles admit no holomorphic PGL(2,C) connection; and they admit no smooth projectively flat connection. Their trace-free Atiyah classes remain nonzero. The argument covers finite ramified covers and modifications whenever the stated smooth compact Kähler source assumptions hold. For smooth projective flatness alone, the Kähler assumption is unnecessary, since flat adjoint curvature directly forces the same real characteristic class to vanish.

This addendum concerns only characteristic-class connection obstructions. It does not extend the separate prior CM-Hom or projective-isomorphism exclusion to ramified covers or modifications, does not produce a detector value, and does not address singular sources or nonproper maps. Also chi(End_0(q*F)) need not equal 7200d for general such Y, because td(Y) need not be 1.
