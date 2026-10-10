# Appendix: local Poisson obstruction at a normalized crossing

Status: recovered local proof capsule with a freshly executed polynomial check, 2026-10-10. This appendix proves the local obstruction under the explicit model below. Global character and transport statements require their own hypotheses; no global theorem is inferred solely from a local matrix.

## 1. Local model and grading

Let R=C[[x₁,x₂,y₁,y₂]], or the corresponding analytic regular local ring. Let I=(x₁,x₂), J=(y₁,y₂). The two smooth surface branches are transverse and their normalization separates them.

Consider the two-term object [R→R/I⊕R/J], with R in degree 0, the quotient sum in degree 1, and diagonal restriction. Combining the two Koszul resolutions and cancelling the diagonal free summand gives the free model P:

P⁻¹=R², P⁰=R⁴, P¹=R,

with

d⁻¹ =
[−x₂   0
  x₁   0
   0  −y₂
   0   y₁],

d⁰=[x₁,x₂,y₁,y₂].

Changing a branch basis may change displayed signs but not the conclusion. Direct multiplication gives d⁰d⁻¹=0.

This is the normalized isolated-crossing model used for the corrected partial-normalization secant object in [Markman v2, §12](https://arxiv.org/html/2509.23403v2). A line twist is locally trivial and does not change this test.

## 2. First-order star-product defect

Take the convention

f⋆g=fg+(h/2){f,g} mod h²,

so [f,g]⋆=h{f,g} mod h². Keeping the displayed matrices as initial lifts, their composition is

d⁰⋆d⁻¹ =
[x₂⋆x₁−x₁⋆x₂, y₂⋆y₁−y₁⋆y₂].

Thus its coefficient of h at the closed point is

[−{x₁,x₂}(0),−{y₁,y₂}(0)].

For π=∂x₁∧∂x₂ it is [−1,0]. More generally it is nonzero whenever at least one of the two displayed pairings is nonzero at the point.

For an abelian fourfold, global holomorphic bivectors evaluate onto the exterior square of the tangent space at any point. Therefore a global bivector with the required nonzero value exists, even if its coefficients in these local branch coordinates are not constant.

## 3. No differential correction removes the defect

End²(P)=Hom_R(P⁻¹,P¹)=R^(1×2). A degree-one correction consists of maps

a:P⁻¹→P⁰ and b:P⁰→P¹.

Its differential in End(P), up to the harmless convention-dependent sign, is d⁰a+b d⁻¹. Every entry lies in the maximal ideal m=(x₁,x₂,y₁,y₂), since every entry of both d matrices lies in m.

Hence no degree-two boundary has a nonzero constant term. The star-product defect [−1,0] represents a nonzero class in H²End(P). There is no End³ term, so it is automatically closed.

Changing the first-order lifts of the differentials adds exactly such a boundary. A derived first-order module deformation would, on this perfect local model, provide corrected differentials with square zero. The surviving class is therefore an obstruction, not merely a defect of one arbitrary lift.

## 4. Relation to the compensated secant direction

Normalize HKR action so a holomorphic bivector π acts by contraction and a gerbe class B∈H²(O_X) acts by wedge. Put Π=ιπ(θ²)/2.

For a polarization class θ of type (1,1),

ιπ exp(zθ)=z²Π exp(zθ).

Therefore ξ=π+dΠ annihilates both exp(i√dθ) and exp(−i√dθ), and hence any character in their span.

A gerbe class becomes trivial on a sufficiently small local neighborhood. Its contribution cannot cancel the nonzero local Poisson obstruction above. Consequently, whenever a global object F has both:
1. that imaginary-secant character, and
2. this normalized transverse-crossing local model,

the chosen ξ annihilates ch(F) but evaluates nontrivially on F. Naturality then gives a nonzero element of im(ev_F) in the kernel of semiregularity. This rejects the weak image-injectivity criterion for that object.

## 5. Exact boundary of this appendix

The cited §12 prints an O(Θ) twist; the reconstructed character audit requires O(3Θ). The complete global character calculation, including the number and placement of normalized points, is not reproduced here. Thus application to the named cyclic object should cite or supply that separate audit.

Similarly, transporting the obstruction to a polarized Weil tangent through Orlov equivalence is a separate statement and is not proved by this local appendix. This proof does not refute Markman’s general Question 11.4 and does not disprove a Weil-class algebraicity theorem.

## 6. Fresh execution

The companion verify-node-poisson.js checks the ordinary matrix product and the first-order bracket with π=∂x₁∧∂x₂ using exact sparse polynomials.

Executed output on 2026-10-10:
- ordinary product: [0,0];
- twice the first-order Moyal coefficient: [−2,0];
- obstruction row: [−1,0].

This checks the displayed matrix algebra, not the separate global character or Orlov-transport claims.
