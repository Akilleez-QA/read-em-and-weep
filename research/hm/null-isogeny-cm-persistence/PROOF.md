# Conditional CM obstruction after every finite isogeny

## Result

Work over C. Retain precisely the historical A-identity premise, geometric identification, and rank-two bundle F on X=C^4 from the two checked input proofs. Put G=σ*F. The imported conclusions used here are

    det(F) ≅ det(G) ≅ O_X,
    Hom_X(F,G⊗L)=0 for every L∈Pic⁰(X).

For every finite isogeny q:Y→X and every M∈Pic⁰(Y),

    Hom_Y(q*F,q*G⊗M)=0.                                      (1)

Consequently P(q*F) and P(q*G) are not isomorphic over Y. If an automorphism τ of Y satisfies q∘τ=σ∘q, then P(q*F) has no global regular automorphism covering τ. The same statements hold for every connected finite étale cover q:Y→X, without choosing a new map on the target X.

These are conditional global regular statements. They neither reauthenticate A nor exclude rational or meromorphic maps. No model evaluation or additional constant-chain-map calculation is needed.

## 1. What is imported, and what is new

The base proof proves Hom_X(F,σ*F)=0 from the historical A premise and the constant-chain-map elimination certificate. The projective extension proves Hom_X(F,σ*F⊗L)=0 for every nontrivial L∈Pic⁰(X), using the internal Hom amplitude [−3,3], the four-dimensional cohomology support, and the disappearance of the zero-power column for nontrivial L. Together these establish the all-L hypothesis above, including L=O_X.

It is important to import **all** Pic⁰ twists. Untwisted Hom vanishing alone would not suffice: finite pullback can introduce morphisms through torsion-character twists downstairs. The proof below closes exactly that possibility.

## 2. Two isogeny facts, with an elementary splitting proof

Let H=ker(q)(C). In characteristic zero q is finite étale and is an H-torsor, with H a finite abelian group. The dual morphism

    q^∨=q*:Pic⁰(X)→Pic⁰(Y)

is an isogeny and is therefore surjective. This is the dual exact sequence theorem: [Milne, Abelian Varieties, Theorem 11.1, printed p.18](https://www.jmilne.org/math/xnotes/AVs.pdf#page=18).

There is a decomposition into line bundles

    q_*O_Y ≅ ⊕_{χ∈H^∨} T_χ,                                  (2)

where T_1=O_X, each T_χ is torsion in Pic⁰(X), and q*T_χ≅O_Y. The sign in the correspondence between χ and T_χ depends on whether translations act by pullback or inverse pullback; the decomposition over all characters is unaffected.

Here is a direct proof, avoiding any unproved semisimplicity claim for arbitrary sheaves. The O_X-linear deck action gives orthogonal idempotents

    e_χ = (1/|H|) Σ_{h∈H} χ(h)^(−1) h

on q_*O_Y. Their images T_χ form a direct sum. Étale-locally the torsor is trivial, so q_*O_Y is the algebra of functions on H, and each character eigenspace has rank one. Thus T_χ is a line bundle. Multiplication of character functions gives an isomorphism T_χ⊗T_ψ→T_{χψ}, checked on that same étale cover. In particular T_χ has finite tensor order. The tautological trivialization of the pulled-back torsor gives q*T_χ≅O_Y.

For a complex abelian variety, every torsion line bundle belongs to Pic⁰: NS is torsion-free. One elementary complex proof uses the exponential sequence, which embeds Pic/Pic⁰ in H²(Y,Z), a torsion-free group for a real torus. The algebraic version is the injection NS(Y)→Hom(Y,Y^∨), whose target has no torsion.

The original primary source states this splitting explicitly: [Oda, Vector Bundles on an Elliptic Curve (1971), Corollary 1.7, printed p.53 / PDF p.13](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D4C47973AF703C135CD1DAD559732A0F/S0027763000014367a.pdf/vector-bundles-on-an-elliptic-curve.pdf#page=13). Despite its title, Section 1 treats abelian varieties in arbitrary dimension. The corollary decomposes the pushforward of the structure sheaf into lines killed by pullback when the dual isogeny is separable, as it is over C. Oda's convention includes characteristic zero. This directly confirms (2); the elementary proof above also makes the character and torsion details explicit.

## 3. Projection formula gives the desired vanishing

Take any M∈Pic⁰(Y). By surjectivity choose L∈Pic⁰(X) with q*L≅M. Ordinary pullback–pushforward adjunction and the projection formula give

    Hom_Y(q*F,q*G⊗M)
      ≅ Hom_Y(q*F,q*(G⊗L))
      ≅ Hom_X(F,q_*q*(G⊗L))
      ≅ Hom_X(F,(G⊗L)⊗q_*O_Y)
      ≅ ⊕_χ Hom_X(F,G⊗L⊗T_χ)
      = 0.

Every L⊗T_χ belongs to Pic⁰(X), including any summand where it becomes trivial. Both those cases are covered by the imported hypothesis. This proves (1), with no restriction on the degree or kernel of q.

The adjunction here is q* left adjoint to q_*, not a duality adjunction involving q^!. No canonical-bundle correction appears. Independently, ω_Y≅q*ω_X≅O_Y because q is étale; equivalently, an abelian variety has trivial cotangent bundle after choosing invariant differentials. Thus there is no hidden ramification or canonical twist.

## 4. Projectivization and determinant

Set E=q*F and E'=q*G. Both have rank two and trivial determinant. An isomorphism P(E)≅P(E') over Y implies E≅E'⊗M for some line bundle M on Y. For clarity, this is the actual projective-bundle statement, not merely a Brauer-class comparison: pull back O(1), divide by O(1), and obtain a line bundle trivial on each projective-space fiber. Cohomology and base change descends it to Y; pushing forward O(1) gives the stated tensor relation, possibly replacing M by its inverse according to orientation. See [Stacks, projective bundles](https://stacks.math.columbia.edu/tag/01OA) and the detailed argument in the checked projective input.

Taking determinants gives M²≅O_Y. Since Y is an abelian variety, this implies M∈Pic⁰(Y). The assumed bundle isomorphism would then be a nonzero member of the Hom group in (1), a contradiction. Therefore the two projective bundles are not isomorphic over Y.

If q∘τ=σ∘q, functorial pullback gives

    τ*(q*F) ≅ q*(σ*F)=E'.

An automorphism of P(E) covering τ yields an isomorphism P(E)≅P(τ*E) over Y (or its inverse, depending on graph convention). The established nonisomorphism excludes it. No lift τ is asserted to exist for an arbitrary q.

## 5. Connected finite étale covers and translations

A connected finite étale cover q:Y→X of an abelian variety over C acquires an abelian-variety structure after choosing y₀∈q^(−1)(0), with y₀ as identity, and then **the original map q** is an isogeny. This standard theorem is recorded in [Milne, Remark 15.3, printed p.28](https://www.jmilne.org/math/xnotes/AVs.pdf#page=28), citing Mumford §18.

Concretely, write X^an=V/Λ. A pointed connected finite cover is V/Λ'→V/Λ for a finite-index subgroup Λ'⊂Λ. Its pulled-back ample polarization is ample, so it is a projective complex torus and hence an abelian variety. Choosing a point over zero removes any affine translation term in q. Choosing a different point over zero changes the group-law presentation by a translation on Y; it does not change q as a map of varieties, Pic⁰(Y), or the asserted Hom groups. In particular, no replacement of F by a translate on X has been silently made.

A lift τ of σ can itself have a translation term. With a chosen y₀ over zero, write τ=t_a∘φ, where a=τ(y₀)∈ker(q) and φ preserves the origin. Then q∘φ=σ∘q. Since τ is an automorphism, so is φ. This causes no change to the pullback identity in §4. For the CM automorphism induced by a linear action S on V, a lift on this same cover exists exactly when SΛ'=Λ'; not every finite-index sublattice is required to satisfy that condition.

The all-twist Hom conclusion and the comparison P(q*F)≄P(q*σ*F) hold on every connected finite étale cover regardless of whether such a lift exists. The language “no projective CM lift upstairs” is only used when τ is specified with q∘τ=σ∘q.

## 6. Optional additional consequence: self-twists remain absent

The checked projective input also proves Hom_X(F,F⊗L)=0 for every nontrivial L∈Pic⁰(X). This implies the same vanishing upstairs for every nontrivial M∈Pic⁰(Y): choose L with q*L=M. None of L⊗T_χ can be trivial, since its pullback is M. Applying the same direct-sum formula therefore gives zero in every summand.

Consequently q*F has no nontrivial line-bundle self-twist: any self-twist has square-trivial determinant twist, hence lies in Pic⁰(Y), and the nontrivial case is excluded. This does not assert that all projective automorphisms over the identity are trivial.

## 7. Boundaries and audit

The new deduction is formal from the checked all-Pic⁰ vanishing. It does not require Y to be a product of elliptic curves, nor does it re-run the amplitude argument on Y. It concerns the same finite cover q in both pullbacks. It establishes nothing about arbitrary base changes, ramified finite maps, different covers in the two arguments, arbitrary automorphisms of Y unrelated to σ, or rational/meromorphic bundle isomorphisms.

Inputs: [projective CM extension, PR #93](https://github.com/Akilleez-QA/read-em-and-weep/blob/f5d1226a57bb30cc61127821008920922c19db41/research/hm/projective-cm-extension/PROOF.md) and [conditional global-Hom proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/4659e4425c6b5ab6b1899e6af93656ac03ff0862/research/hm/null-cm-global-hom/PROOF.md). The cited primary references were checked in the original preparation; no fresh source authentication or test execution is claimed here. No separate independent review artifact is bundled.
