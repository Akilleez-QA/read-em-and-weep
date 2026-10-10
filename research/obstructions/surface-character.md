# Appendix: two surface-ideal character obstructions

Status: explicit proof and exact polynomial checks reconstructed on 2026-10-10. The calculations below are a fresh derivation of the recorded contradictions, not a claim that an earlier full proof or execution log was recovered.

## Setup

Let X be a complex abelian fourfold, θ=c₁(L) an ample class, and d>0 rational. Consider the imaginary secant space spanned by exp(i√d θ) and exp(−i√d θ). A rank-one character in this space with first Chern class aθ necessarily has components

ch₀=1, ch₁=aθ, ch₂=−dθ²/2, ch₃=−adθ³/6, ch₄=d²θ⁴/24.

Indeed, write it as A exp(i√d θ)+B exp(−i√d θ), impose A+B=1 and i√d(A−B)=a, and expand. No positivity of A or B is assumed.

The secant-carrier context is [Markman v2, §12](https://arxiv.org/html/2509.23403v2). The contradictions below are deductions, not claims quoted from that paper.

## Proposition 1: complete-intersection ideals

Suppose Z is a codimension-two regular complete intersection of divisors with classes bθ and cθ, where b,c>0. Then I_Z⊗L^a cannot have the displayed secant character for d>0. Numerically trivial line twists do not affect this conclusion.

The Koszul resolution gives

ch(I_Z(aθ))=exp((a−b)θ)+exp((a−c)θ)−exp((a−b−c)θ).

Put B=b+c. Comparing the degree-two numerator with −d gives

d=2bc−a².

The degree-three equation, after substituting d, is

(a−b)³+(a−c)³−(a−B)³+ad
=bc(3B−4a)=0.

Since bc>0, a=3B/4. For degree four, the difference between the numerator and d² is

bc(−8a²+12aB−4B²−2bc).

Substitution of a=3B/4 reduces this to bc(B²−4bc)/2. Thus B²=4bc, or (b−c)²=0. Hence b=c, a=3b/2 and d=2b²−9b²/4=−b²/4<0, contradiction.

This excludes the specified one-polarization complete-intersection ideal. It does not exclude arbitrary ideals, complexes or higher-rank bundles.

## Proposition 2: smooth surfaces with proportional canonical class

Suppose i:S→X is a smooth embedded surface, and K_S is numerically proportional to h=i*θ. Then I_S(aθ) cannot have the displayed secant character for d>0.

Write v=∫_X θ⁴>0 and A=(a²+d)/2. Because T_X is trivial, Grothendieck–Riemann–Roch gives

ch(i_*O_S)=i_*(td(T_S))
=[S]−i_*K_S/2+i_*(K_S²+c₂(S))/12.

This uses the Todd expansion for a surface. See [GRR](https://stacks.math.columbia.edu/tag/02UO) and [Todd classes](https://stacks.math.columbia.edu/tag/02UN).

Multiplying 1−ch(i_*O_S) by exp(aθ) and comparing secant components gives:

1. [S]=Aθ².
2. i_*K_S=(4a/3)Aθ³.
3. K_S²+c₂(S)=(3a⁴+2a²d−d²)v/2, where Chern numbers are integrated over S.

For step 3 explicitly, the degree-four component is

a⁴v/24 − a²Av/2 + (a/2)∫_S K_Sh − (K_S²+c₂(S))/12 = d²v/24.

Use ∫_S K_Sh=(4a/3)Av and simplify.

The tangent-normal exact sequence implies c₁(N)=K_S and c₂(N)=K_S²−c₂(S). Self-intersection gives ∫_S c₂(N)=[S]²=A²v. Combining with step 3 yields

K_S²=(7a⁴+6a²d−d²)v/8.

Now use the numerical-proportionality hypothesis K_S≡kh. Step 2, paired with θ, gives k=4a/3 because ∫_S h²=Av>0. Consequently

K_S²=(16a²/9)Av=8a²(a²+d)v/9.

Equate the two expressions and cancel v. Multiplication by 72 gives

9(7a⁴+6a²d−d²)−64a²(a²+d)
=−(a²+d)(a²+9d)=0.

Both factors are positive when d>0 and a is real, contradiction.

The exact hypothesis matters: surfaces with canonical class independent of h are not excluded. The argument also does not assert nonexistence of all smooth-surface secant constructions.

## Reproducibility

The companion JavaScript file verify-surface-character.js uses sparse integer arithmetic over Z[a,b,c,d]. It was executed on 2026-10-10 and passed five identities:
ci_ch2, ci_ch3, ci_ch4, ci_substitution, surface_factorization.

It checks polynomial manipulations. It does not machine-prove GRR, the tangent-normal sequence, self-intersection or the geometric hypotheses. A standard Node.js runtime can execute it with no dependencies.
