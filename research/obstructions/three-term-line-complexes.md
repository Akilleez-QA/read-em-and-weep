# Appendix: three-term one-polarization line-complex obstruction

Status: reconstructed proof capsule, 2026-10-10. This is a scoped argument about three consecutive degrees. It does not exclude longer complexes, and no executable spectral-sequence calculation is claimed here.

## Hypotheses

Let X be a complex abelian fourfold and L an ample line bundle with θ=c₁(L). Let M be a bounded complex of vector bundles concentrated in three consecutive cohomological degrees. Every term is a finite direct sum of L^r⊗P with r∈Z and P∈Pic⁰(X).

Assume ch(M) is nonzero and belongs to span{exp(i√dθ),exp(−i√dθ)} for a rational d>0. Use HKR conventions in which π∈H⁰(Λ²T_X) acts by contraction and B∈H²(O_X) by wedge.

Claim: the semiregularity map cannot be injective on im(ev_M). Equivalently, some ξ annihilates ch(M) but ev_M(ξ) is nonzero.

The criterion being tested is the one discussed in [Markman v2, Lemma 11.3 and Question 11.4](https://arxiv.org/html/2509.23403v2). This appendix concerns particular objects, not a negative answer to that general question.

## 1. Reduce the complex and choose a maximal summand

If a differential between identical line summands has a nonzero constant entry, split off the corresponding contractible isomorphism block using ordinary Gaussian cancellation. Repeat finitely many times. This preserves the derived object, its character and the three-column amplitude.

Choose a remaining summand T=L^r⊗P with globally maximal exponent r, occurring in degree p.

All outgoing components from T vanish:
- to a lower exponent, H⁰ of the negative ample difference is zero;
- to the same exponent with a nonisomorphic Pic⁰ difference, H⁰ is zero;
- to an identical summand, the constant block has been cancelled.

The inclusion therefore defines a chain map s:T[−p]→M. There may be incoming maps to T; the argument does not assume otherwise.

## 2. The summand’s H²(O_X) survives

Compute hypercohomology of T∨⊗M by the column spectral sequence

E₁^(j,q)=H^q(X,T∨⊗M^j) ⇒ H^(j+q)(X,T∨⊗M).

The distinguished summand in column p contributes H²(O_X). This group is six-dimensional. Every class can be represented by a Dolbeault-closed form supported on that summand; its horizontal differential is zero, so it has no outgoing higher differential.

For possible incoming differentials d_k from (p−k,2+k−1):

- A lower-exponent summand has cohomology only in degree 4, by Kodaira vanishing and Serre duality on the abelian fourfold. The first possible incoming differential would have k=3, hence source column p−3. Three consecutive columns do not contain both p and p−3.
- A same-exponent nonisomorphic Pic⁰ difference is acyclic.
- An identical maximal summand may have H¹,H²,H³,H⁴. It is NOT acyclic. However every outgoing sheaf map from it vanishes after the cancellation above. Its Dolbeault representatives already have zero horizontal differential, so every outgoing higher differential from these classes vanishes. In particular the apparent k=2 contribution from H³ is zero.
- The k=1 incoming map from an identical maximal summand is also zero.

Thus the chosen H²(O_X) injects into the abutment via s. Precisely,

s_*:Ext²(T[−p],T[−p])=H²(O_X)
→Ext²(T[−p],M)

is injective.

This is the amplitude-sensitive step. With four or more columns, a lower-exponent H⁴ class can reach the distinguished H² through d₃.

## 3. Choose a compensated Hochschild class

Choose nonzero π and let Π=ιπ(θ²)/2∈H²(O_X). Since θ is a polarization, contraction induces an isomorphism between Λ²H⁰(T_X) and Λ²H¹(O_X), so Π≠0 for nonzero π.

Set ξ=π+dΠ. The exponential identity

ιπ exp(zθ)=z²Π exp(zθ)

shows ξ·ch(M)=0.

For T=L^r⊗P, Pic⁰ twisting does not change its Atiyah/Chern class. Evaluation is

ev_T(ξ)=(r²+d)Π∈H²(O_X),

which is nonzero because d>0. Any uniform nonzero normalization factor in the HKR/Atiyah convention must be used consistently in both formulas; it does not alter the argument.

## 4. Apply naturality

Evaluation is a natural transformation. Therefore

ev_M(ξ)∘s = s[2]∘ev_(T[−p])(ξ).

The right side is nonzero by the injection in step 2. Hence ev_M(ξ)≠0, even though ξ annihilates ch(M).

Compatibility of the semiregularity map with HKR contraction gives σ_M(ev_M(ξ))=0. Consequently σ_M is not injective on im(ev_M).

## Scope and checks

The proof uses dimension four, ampleness, line-power/Pic⁰ terms, three consecutive degrees, and a nonzero imaginary-secant character with d>0. Dropping any of these requires a new argument.

In particular:
- the signed-twist numerical monad is within scope, regardless of whether its endpoints are exact;
- longer-amplitude line complexes are outside scope;
- non-line middle bundles are outside scope;
- the four-term cancelled HM line model can have an actual d₃ and is not excluded.

The proof is reconstructed as an explicit argument. No symbolic or formal proof engine was run for this appendix. The key equal-maximum case is handled explicitly rather than incorrectly treating those summands as acyclic.
