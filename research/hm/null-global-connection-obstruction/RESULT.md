# Global connection obstruction for the conditional physical bundle

## Result and evidence boundary

Assume the imported exact A-identity receipt and the stated all-chart geometric identification from [the pinned global-Hom proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-cm-global-hom/PROOF.md), so that the physical four-term perfect complex is quasi-isomorphic to an actual holomorphic rank-two bundle F on the compact elliptic product X=C^4. Then:

- F has no global holomorphic connection, even a nonflat one.
- Its projective frame bundle has no global holomorphic PGL(2,C) connection, even a nonflat one.
- No holomorphic line twist F tensor L has a global holomorphic connection.
- Neither F nor any line twist admits a smooth projectively flat connection; in particular, no smooth flat connection exists.

These statements do not exclude ordinary smooth connections, local holomorphic connections, connections only on a proper open subset, or meromorphic/logarithmic connections with poles. They do not invalidate the auxiliary local Gamma formulas in the remainder normal form. The new conclusion is the global obstruction, not the already known Euler characteristic 7200.

The Chern-character and perfect-complex endomorphism-index calculations below require only the four terms, independently of the differential maps. Identifying them with the Chern classes and ordinary End-bundle cohomology of an actual F retains the A and geometric premises.

## 1. Universal characteristic calculation

Let N be the external product of the degree-one infinity line bundles on the four elliptic factors, theta=c1(N), and use rational cohomology. The physical class is

    [K_X] = -5[N^(-1)] + 15[N] - 10[N^3] + 2[N^5].

Consequently, in degrees at most eight,

    ch(K_X) = -5 exp(-theta) + 15 exp(theta)
              -10 exp(3 theta) + 2 exp(5 theta)
            = 2 -15 theta^2 + (75/4) theta^4.

The degree-two and degree-six components vanish. Under K_X ≃ F[0], ch1(F)=c1(F)=0 and ch2(F)=(c1^2-2c2)/2 give

    c2(F)=15 theta^2,
    Delta(F):=4c2(F)-c1(F)^2=60 theta^2.

Here “degree” in ch_j means complex degree j, so theta^2 lies in H^4(X,Q). For an actual rank-two F, c3 and c4 vanish; the computed ch4 is consistent with c2^2/12=225 theta^4/12=75 theta^4/4. Independently, converting the virtual Chern character to total Chern class yields 1+15 theta^2 through degree eight.

Write eta_i for the degree-two point class from elliptic factor i. Then theta=sum eta_i, eta_i^2=0, and integral_X eta_1 eta_2 eta_3 eta_4=1. Hence

    integral_X theta^4=4!=24,
    integral_X Delta(F) theta^2=60*24=1440 != 0.

In particular Delta(F) is nonzero already in real cohomology, not merely a possible torsion class.

Dualization negates odd Chern-character components, so here ch(F*)=ch(F). Multiplication gives

    ch(End F)=ch(F*) ch(F)=4-60 theta^2+300 theta^4.

Equivalently ch2(End F)=-Delta(F). Since c1(End F)=0, c2(End F)=Delta(F). The tracefree bundle has character

    ch(End_0 F)=3-60 theta^2+300 theta^4.

The same product formula is unconditional for the derived endomorphism perfect complex K_X^vee tensor K_X; it is not being silently identified with an underived End bundle before exactness is admitted.

The tangent bundle of X is holomorphically trivial, so Td(X)=1. Hirzebruch–Riemann–Roch therefore gives

    chi(X,End F)=integral_X ch4(End F)=300*24=7200.

The tracefree index is also 7200 because chi(O_X)=0. This is an independent characteristic-class consistency check on the old deck-character index, not a new cohomology-rank computation or proof of any detector value.

## 2. Why a holomorphic connection would contradict this class

A holomorphic connection on a holomorphic vector bundle E means a C-linear sheaf map

    nabla:E -> Omega_X^1 tensor E,
    nabla(fs)=df tensor s+f nabla(s).

It is not assumed flat. Combining it with the given Dolbeault operator defines a smooth complex connection whose curvature has type (2,0): locally its connection form is a holomorphic (1,0)-form A and curvature is dA+A wedge A. Chern–Weil then represents ch_j(E) by a closed form of type (2j,0). On the other hand, a Hermitian metric supplies the Chern connection with curvature type (1,1), representing the same class by a form of type (j,j).

On compact Kähler X, the direct Hodge decomposition of H^(2j)(X,C) makes the intersection of these two distinct summands zero for j>0 (with nonexistent types understood as zero). Thus all positive-degree Chern-character components vanish. In particular ch2(F) would vanish, contradicting -15 theta^2. This argument requires compact Kähler geometry, and is not an assertion about arbitrary non-Kähler manifolds or integral torsion.

This is the classical Atiyah obstruction theorem. A directly inspected primary research reference is Biswas–Dumitrescu, *Principal bundles with holomorphic connections over a Kähler Calabi–Yau manifold*, arXiv:2312.01399, introduction and Lemma 2.1, printed pages 1 and 4. It states real characteristic-class vanishing on compact connected Kähler bases and explains the induced connections on associated vector bundles. It cites Atiyah, *Complex analytic connections in fibre bundles*, Trans. AMS 85 (1957), Theorem 6, p.197. No Calabi–Yau or Ricci-flat strengthening is needed here.

- Directly inspected primary paper: https://arxiv.org/pdf/2312.01399
- Original primary paper: https://www.ams.org/journals/tran/1957-085-01/S0002-9947-1957-0086359-5/S0002-9947-1957-0086359-5.pdf

The AMS full PDF fetch returned 403; the original theorem location is reported via the inspected primary paper, not claimed as a new full-text inspection of Atiyah. The Hodge/Chern–Weil argument above supplies the needed proof independently.

## 3. Projective connection, precise meaning, and all line twists

Here a “holomorphic projective connection on F” means a holomorphic principal connection on its projective frame PGL(2,C)-bundle, equivalently a holomorphic splitting of that principal bundle's Atiyah sequence. This concerns the projective bundle P(F) over X. It does not mean a holomorphic normal projective connection on the tangent bundle of X or a projective coordinate structure on the base.

The conjugation representation PGL(2,C) -> GL(sl_2(C)) associates End_0(F) to this principal bundle. Every principal holomorphic connection induces a holomorphic connection in an associated representation: in local forms, apply the representation's Lie algebra differential to the connection form; the transformation law is preserved. Such a connection on End_0(F) would force

    ch2(End_0 F)=-60 theta^2=0,

which is false. Hence even a nonflat holomorphic projective connection is excluded. No lifting of a hypothetical PGL connection to GL is assumed in this argument.

For any holomorphic line bundle L with ell=c1(L), rank-two Chern-root identities give

    c1(F tensor L)=c1(F)+2ell,
    c2(F tensor L)=c2(F)+c1(F)ell+ell^2,
    Delta(F tensor L)=Delta(F).

More intrinsically End_0(F tensor L) is canonically End_0(F), and P(F tensor L)=P(F). A holomorphic connection on F tensor L would induce one on this unchanged endomorphism bundle, giving the same contradiction. This covers every holomorphic line twist, not just powers of N and not merely twists with vanishing first Chern class.

## 4. Smooth connections and finite covers

Every smooth complex vector bundle on this compact manifold admits a smooth connection, for instance the Chern connection after choosing a Hermitian metric. Nonzero Chern classes are therefore no obstruction to ordinary smooth connection existence.

A projectively flat smooth connection means curvature R=omega Id for a scalar two-form omega, equivalently vanishing curvature of the induced PGL connection. Its induced connection on End_0(F) has curvature T -> [R,T]=0, so End_0(F) would be flat and all its positive-degree real Chern characters would vanish by Chern–Weil. The computed nonzero ch2 forbids this. The same argument forbids a flat smooth PGL connection whether or not it lifts to a GL connection, using its adjoint representation. Ordinary smooth flat connections are a special case, and line twists cannot remove the obstruction.

For completeness, passing to a finite étale cover p:X'->X of positive degree d cannot help. The cover remains compact Kähler, and

    integral_X' p*Delta(F) p*(theta^2)=d*1440 != 0.

Thus the pullback discriminant is still nonzero; all the above exclusions persist after finite étale pullback and any line twist there. No conclusion of this form is asserted for infinite or noncompact covers: compactness and this nonzero pairing can fail.

## 5. Consequence for the local Gamma/current formalism

The remainder normal form uses local Gamma_End,d, overlap commutators, and homotopy corrections. A locally defined coefficient operator is not automatically a global holomorphic connection on F. Meromorphic poles and transition defects can be precisely what prevent the prohibited global extension. A globally defined smooth nonflat connection, if separately constructed, would also be compatible with this obstruction.

Accordingly, it would be invalid to promote the local differentiation rules to a nonsingular global holomorphic or projectively flat connection on the physical bundle without confronting this discriminant. It would equally be invalid to infer that the local formulas fail, that an actual current curvature term is nonzero in a specified chart, or that the surviving source/trace vanishes or does not vanish. This calculation determines none of those local coefficients or detector values.

The obstruction does not identify which particular poles, overlap terms, or homotopy corrections are necessary in a chosen presentation. It excludes the global interpretation, rather than deleting or evaluating any family in the complete remaining-target formula.

## 6. Performed check and reproducibility

`check.py` uses only Python's standard library and exact rational arithmetic in Q[t]/(t^5). It verifies the two Chern characters, total Chern class, rank-two line-twist discriminant identity, and HRR scalar. Its output is `check-results.json`.

Source dependencies:

- [Conditional bundle identification](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-cm-global-hom/PROOF.md).
- [Complete remainder normal form](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-complete-remainder-normal-form/RESULT.md).
- The earlier deck-character index is a consistency comparison, not a prerequisite for the characteristic-class proof. Its 7200 Euler value is reproduced by the universal calculation above.

The saved scalar arithmetic uses no physical source or jet values. It is a characteristic-class check, not a model-matrix product. No old Euler result is counted as new progress.
