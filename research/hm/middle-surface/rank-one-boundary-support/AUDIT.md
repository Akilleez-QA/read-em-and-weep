# Independent audit: rank-one boundary support curves

Verdict: PASS, with the exact limited scope stated below.

Audited on 2026-10-19. Frozen PROOF.md SHA-256:

`d2ef79c9cd9e026b8420b038ddeaa03db919d9751983883dcb53ce44678adec9`

The audit also read `/research/hm/middle-surface/flag-boundary-resolution/PROOF.md` and `/research/hm/middle-surface/flag-boundary-resolution/ADDITIONAL_RANK_TWO.md`. It uses universal algebraic geometry only, without inspecting or evaluating a physical source, running a rank experiment, or changing an external application.

## 1. Input and normalization

At residual rank one, the scalar annihilator Q is a nonzero quadratic functional on Sym²E, with kernel of dimension nine. The rank of this quadratic form must not be confused with residual rank one. A limiting five-plane is forced to equal K∩Sym²A precisely when Q|A is nonzero. At a factor hyperplane, this intersection has dimension six and equality cannot be inferred.

Normalization of a complete integral curve is legitimate: the support map pulls back, remains nonconstant, and all pointwise incidence hypotheses persist. No regular choice of the five-planes is needed. Integrality and projectivity give H⁰(O)=C. The proper augmented kernel/support graph in the foundational proof supplies the required pointwise incidences even when the actual kernel dimension jumps.

## 2. Bundle types and scheme-theoretic regularity

The proof defines L=a*O(1), the quotient line of the universal covector E⊗O→L. With this convention λ is correctly a section of L. If instead L denoted the tautological equation subline in E*, the corresponding bundle would be L*. There is no error in the convention actually used in PROOF.md.

When Q|A is everywhere nonzero, it is a line subbundle of Sym²A*, not merely a subsheaf. The quotient is locally free. Fiberwise vanishing of the image of aV in the quotient implies vanishing as a section because the normalized curve is reduced. Thus λ is globally regular.

The exact sequence (3) is correct. The ideal of a hyperplane in quadratic degree consists of its equation times a unique linear form. Twisting by L cancels the tautological equation-line twist, so the preimage is a section of the trivial E* bundle. Hence the divided covector ℓ is constant. This argument neither silently discards torsion nor extends meromorphic data across zeros of Q|A.

The shear normalization Sℓ(ef)=(ℓ(e)f+ℓ(f)e)/2 gives Sℓ(e²)=ℓ(e)e and aSℓ=aℓ with the polynomial pairing used throughout. It therefore preserves the condition of being a compatible square.

## 3. The common-zero argument

After subtracting the shear, the image of K lies in the intersection W of the support hyperplanes, with dimension at most two. A linear extension to Sym²E with values in W exists. Three homogeneous quadrics Q,F₁,F₂ in four variables have a nonzero common zero over C by the height bound and the Nullstellensatz. This remains true if one or both Fᵢ vanish, if the intersection has excess dimension, or if Q is reducible or a square. No reducedness or smoothness of the quadric is used.

Consequently every complete nonconstant support curve avoiding factor hyperplanes is excluded. Rank(Q)≥3 guarantees that avoidance, since a quadratic form with a linear factor has rank at most two.

## 4. Every pencil is excluded, including nonreduced quadrics

For a pencil with two-dimensional base W, Q|W=0 implies Sym²W⊂K_t at every nonexceptional support. There are at most two exceptional supports, so intersecting two distinct nonexceptional supports gives v(Sym²W)⊂W. The binary cubic then supplies a compatible square.

If Q|W≠0, no pencil member can divide Q. The polynomial proof in Section 5 is valid: after substituting t=−x/y and clearing powers of y, the extra factor is a nonzero binary polynomial, all of whose linear factors lie in the pencil. It is coprime to Q. UFD cancellation therefore gives divisibility by Q with its full multiplicities, including Q=ℓ₀². Restricting the resulting linear quotient M to W and cancelling Q|W proves M∈span(x,y). The final two coprime-linear-form divisions have the stated signs and give a single shear.

There is also a shorter independent verification of this second case: Q|W≠0 ensures Q|A is nonzero for every support in the pencil, so Sections 2–4 apply directly. The longer polynomial calculation is sound, though unnecessary.

## 5. Residual rank zero

For K=Sym²E, the quadratic vector map defines a section of the quotient in

0→O(1)→E⊗O(2)→T(P³)(1)→0.

Its vanishing at [e] is exactly v(e²)∈Ce. The Chern calculation is correct:

c₃(T(P³)(1))=(32−24+8−1)h³=15h³.

A nowhere-zero section would give a trivial line subbundle and rank-two locally free quotient, forcing this top Chern class to vanish. Thus a compatible square exists. Residual rank zero is impossible under square avoidance, without any support-curve hypothesis.

## 6. Exact conclusion and remaining gap

Combined with the independently established rank-two finiteness theorem and full-flag positivity, a finite bad middle locus would require a residual-rank-one point with a positive-dimensional family of limiting supports. At such a point the scalar annihilator quadric must have rank at most two; any complete nonconstant support-curve component must have nonlinear image and meet a factor hyperplane.

The proof does not exclude those remaining nonlinear curves meeting factor hyperplanes. At those exceptional points, Q|A vanishes and the proportionality scalar can have poles. No general removal of those poles is established. The proof also does not exclude a bad locus containing a curve, establish existence of a rank-five family, or give a scheme-length bound on support fibers.
