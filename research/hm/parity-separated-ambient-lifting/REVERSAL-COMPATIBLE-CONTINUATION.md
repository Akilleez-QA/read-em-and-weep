# Resolving local existence by parity averaging

## Scope and explicit additional input

The even/odd lifting theorems and odd bivector repair do not construct arbitrary prescribed local associative coefficients. They do, however, combine with the existing unrestricted invariant literal lifting theorem to produce an all-orders reversal-compatible normal-form continuation. This is stronger than leaving the local fifth-existence input as a new unknown, but it is not a fixed-product all-orders theorem.

The parity-separated ingredients are [PR409](https://github.com/Akilleez-QA/read-em-and-weep/pull/409), exact head `59fc9cdc40cf9a21fbb38549767829ff7471294f`, including its full PROOF.md and ODD-BIVECTOR-REPAIR.md. Use the following previously established input, with its own hypotheses retained:

**Invariant literal lifting input.** On the stated individually inversion-stable affine acyclic cover of a complex abelian variety, every invariant regular normalized differential algebroid presentation modulo h^N, N>=3, has an invariant literal lift modulo h^(N+1) when all three new coefficient types may vary. The local products, overlap maps, and triple units below degree N are preserved exactly.

The exact public source is the [literal small-extension proof](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6259748725). It proves that the defect cochain O of any coefficientwise trial lift is closed and that adding a primitive repairs all four descent equations while preserving the preceding coefficients literally. Its explicit application is the stated elliptic fourfold; its invariant HH^3 vanishing argument applies to the general abelian case under the same regular differential and affine-acyclic hypotheses. For the general form here, the literal lifting input is retained explicitly. This is not an inference from existence of some deformation or from equivalence of its reduction.

That source retains arity zero and the regular differential descent complex; this corollary does not replace those hypotheses by an unaudited formality assertion. Its historical statement about detector values is not adopted as a current frontier update.

## 1. Top-coefficient parity averaging

**Lemma.** Let mu^(<N) be a parity product associative modulo h^N. If it has a regular invariant associative lift mu_hat modulo h^(N+1), then it has such a lift satisfying reversal parity through degree N and preserving every lower coefficient.

Proof. Define a second product on ordinary functions by

  mu_hat^R(f,g;h)=mu_hat(g,f;-h).

For formal series this is the product obtained by applying h reversal and taking the opposite algebra. It is associative because both operations preserve associativity. Its coefficients are

  (mu_hat^R)_r(f,g)=(-1)^r (mu_hat)_r(g,f).

By the lower parity hypothesis these agree with mu_hat for every r<N. Associativity at the single new degree is an affine linear equation in the top coefficient: in every associator term containing mu_N, its partner is ordinary multiplication, because h times h^N vanishes. Therefore the midpoint of the two top coefficients is again a solution:

  mu_N^par(f,g)=(1/2)(mu_hat_N(f,g)+(-1)^N mu_hat_N(g,f)).   (1.1)

It has the required parity. Lower coefficients, normalization, regularity, differential character, and strict geometric invariance are preserved. QED.

No averaging of complete nonlinear descent presentations occurs. Only two associative local products with identical lower coefficients are averaged at their one linear lifting degree.

## 2. All-orders reversal-compatible continuation

**Corollary.** Under the invariant literal lifting input, every invariant reversal-compatible ambient presentation through degree at least two on the stipulated abelian cover has a coefficientwise formal continuation for which:

- every local product satisfies mu_r(g,f)=(-1)^r mu_r(f,g);
- every overlap map has only even coefficients;
- every triple unit satisfies tau(A)=A^(-1);
- every given coefficient is preserved literally.

In particular, the canonical fourth-order presentation in PROOF.md has such a continuation. The higher local products are selected during the construction and are not arbitrary immutable prescriptions.

Proof. Suppose a reversal-compatible invariant presentation is constructed modulo h^N, with N>=3. Apply the invariant literal lifting input to obtain an unrestricted invariant lift. Retain its associative local products and discard its new map and unit coefficients. Apply Lemma 1 chartwise to obtain invariant associative local products with the needed top parity; all lower coefficients are unchanged.

If N is even, Theorem 3.1 of PROOF.md applies to those now-fixed local products. Geometric inversion has no invariant H^2(T_X), so it supplies even new overlap maps and the uniquely normalized reversal-unitary triple units; the pentagon is automatic by even parity.

If N is odd, apply ODD-BIVECTOR-REPAIR.md. Its leading local homomorphism defects form an invariant Cech 1-cocycle in wedge^2 T_X. Since

  H^1(X,wedge^2 T_X)^iota=0,

change only the new local product coefficients by invariant biderivations to remove that defect. These modifications preserve their associativity and odd parity. Keep the new map coefficient zero. Inner descent is then automatic, and

  H^3(X,O_X)^iota=0

supplies the scalar top correction without spoiling reversal-unitarity. Every lower coefficient remains unchanged.

This constructs a compatible sequence of finite-order presentations. Their coefficientwise inverse limit is a formal differential algebroid over C[[h]]. Each coefficient is a regular differential operator of finite order, but no uniform differential-order bound, numerical-h evaluation, analytic convergence, or algebraization is asserted. All parity and descent identities hold coefficientwise. QED.

## 3. Precisely what has been resolved

For the canonical fourth-order presentation, associative local fifth extensions are already available existentially from the prior invariant literal lifting theorem, and Lemma 1 makes them antisymmetric. The odd bivector repair then glues adjusted fifth products with exactly the existing T and U and with F_5=0. Thus the fifth ambient existence dependency is resolved, conditional on that established literal lifting theorem, rather than remaining a newly unresolved local question.

The same reasoning provides a parity-compatible all-orders choice. It does not compute mu_5, the fifth scalar unit, or any later coefficient. It does not show that an arbitrarily prescribed mu_5 satisfies the fixed-product equation R_5=0; the counterexample in PROOF.md remains valid. It does not construct an all-orders fixed Moyal product, identify a period, lift a module, remove any retained source obstruction, or settle the pure diagonal six-condition problem.

This is a normal-form refinement of previously known unrestricted ambient existence. Its new content is simultaneous preservation of reversal parity, zero odd map coefficients, and reversal-unitary units, obtained by an explicit obstruction-by-obstruction construction rather than by silently averaging nonlinear data.

No assertion is made that an arbitrary preselected all-orders continuation is gauge-equivalent to one with these reversal properties. The theorem selects a compatible continuation of the given finite presentation; it does not classify all continuations.
