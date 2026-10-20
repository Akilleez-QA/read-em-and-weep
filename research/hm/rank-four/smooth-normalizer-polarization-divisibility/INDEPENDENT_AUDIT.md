# Independent audit: normalizer polarization divisibility

## Verdict

The proof in PROOF.md is correct. Every integral curve invariant under the standard projective Schrödinger normalizer N = F_5^2 semidirect SL_2(F_5) has degree divisible by 50. The conclusion applies to singular embedded curves after passing to their normalization; smoothness of the embedded curve is not needed. In particular no invariant integral curve has degree 70.

The audit uses only abstract projective representations, finite group actions on smooth curves, and line-bundle descent. No actual source tensor, coefficient, operation value, point sample, or rank instance was evaluated.

## 1. Linearization and order-five lifts

The preimage of N in SL_5(C) has central kernel mu_5. Its natural action on O(-1) therefore induces a genuine N-action on O(5). This statement requires neither a choice of Weil splitting nor an assumed linear action of N on O(1).

The displayed matrices X, Z, and D all lie in SL_5: X is a five-cycle, and the exponent sums for Z and D are zero modulo 5. A matrix B = zeta^c X^a Z^b D^t acts by a cyclic shift with a quadratic phase. If a is nonzero, its fifth power sums this quadratic over all of F_5, giving zero. If a is zero, its diagonal entries are fifth roots. Thus B^5 = I in all cases. Every projective order-five element has quotient either identity or a nontrivial unipotent in SL_2(F_5), and the latter is conjugate to the shear represented by some D^t. The representatives cover translations and translated unipotents. Changing an SL_5 lift multiplies it by mu_5 and does not change its fifth power.

In particular translated unipotents do not acquire order 25 in this central extension. As an independent check, use Weyl operators W(a) with product W(a)W(b) = zeta^(omega(a,b)/2) W(a+b). For a unipotent s = I+J, J^2 = 0, the fifth power of W(a)T has vector sum 5a+10Ja = 0 and central exponent

    (1/2) omega(a,Ja) sum_{0 <= i < j <= 4}(j-i)
      = (1/2) omega(a,Ja) * 20 = 0 in F_5.

An order-five lift acts on a fixed projective line through a fifth root. Its action on O(5) is consequently trivial. This also holds on the pullback fibre at every fixed point of a curve normalization.

## 2. Faithfulness and possible inertia

Let nu: X -> C be the normalization of an integral invariant curve. The action of N lifts uniquely to X. The span of C is invariant under the irreducible Schrödinger representation, so it is all of P^4. If an element acts trivially on X, it fixes C pointwise. The fixed locus of its finite-order projective transformation is the union of its projective eigenspaces. Irreducibility of C places it in one eigenspace, and its full span forces that eigenspace to be all of the representation. The element is therefore the identity in N. Thus the action on X is faithful.

In characteristic zero a finite stabilizer on a smooth curve embeds in the multiplicative tangent-line group and is cyclic. The element-order argument in PROOF.md correctly gives precisely the allowed possibilities 1, 2, 3, 4, 5, 6, 10; it introduces no order 25 or order 20 case. In particular an order-ten inertia group has a unique order-five subgroup, whose action on the fifth-power polarization is trivial. Nothing stronger about the full order-ten fibre character is assumed or needed.

## 3. Rational section and local multiplicities

For M = nu^* O_C(5), Hilbert 90 applies to the one-dimensional semilinear C(X)-space of rational sections because the action on X, and hence on its function field, is faithful. It produces a nonzero invariant rational section. Regularity is unnecessary, and its divisor may have negative multiplicities.

At any point with inertia divisible by 5, restrict to its order-five subgroup. Its tangent character is primitive and its fibre character on M is trivial. Comparison of the first nonzero Laurent term of the invariant section forces its valuation to be divisible by 5. This conclusion is independent of whether one uses the action or inverse action convention on functions and fibres.

An orbit of inertia order e has 3000/e points. Its contribution to deg M therefore belongs respectively to

    3000 Z, 1500 Z, 1000 Z, 750 Z, 3000 Z, 500 Z, 1500 Z

for e = 1, 2, 3, 4, 5, 6, 10. Their greatest common divisor is 250. Thus 250 divides deg M = 5 deg C, proving 50 divides deg C. The pullback degree equality holds for a finite birational normalization, including for singular C.

## 4. Independent weaker descent check

For excluding degree 70 alone one can avoid the full stabilizer list and rational-section arithmetic. Restrict to a Sylow-five subgroup P = F_5^2 semidirect C_5, of order 125. Its nonidentity elements have order 5. On the smooth normalization every stabilizer in P is cyclic, hence trivial or of order 5; its action on M is trivial in either case. The equivariant line bundle therefore descends to X/P. Consequently 125 divides deg M, or equivalently 25 divides deg C. This independently excludes degree 70 and checks the essential five-primary obstruction.

## 5. Consequences and scope

The degree-seventy smooth-frontier theorem immediately supplies the needed integrality for a reduced invariant curve of total degree seventy without line or conic components, so the new obstruction completes that exclusion under its stated dependencies. Its genus and RH signature classifications are not used.

The stronger integral-curve theorem does not alone claim every reduced invariant curve has degree divisible by fifty: components might be permuted by N. Component stabilizers and orbit sizes must still be addressed before extending the conclusion to an arbitrary reducible invariant curve. Nor does it prove existence of invariant curves in degrees divisible by fifty.
