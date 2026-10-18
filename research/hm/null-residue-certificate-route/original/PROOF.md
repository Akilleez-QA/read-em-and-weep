# Rational divergence certificates for Laurent Serre tests

## Status and exact boundary

This packet proves an alternative mathematical certificate criterion. It computes no physical/model quantities and does not determine the actual obstruction. It does not activate, modify, or satisfy the operational admission conditions of any inert detector.

The mathematical input F is the SAME complete scalar rational expression after the prescribed whole-source weighting, scalar selector and deck extraction. It is not an arbitrary raw summand, a matrix entry before extraction, or a differently normalized representative. The following are separate hypotheses:

1. The geometric, same-source, frame, deck and regular-cover comparisons identify this F as a Laurent polynomial representative of the intended scalar cohomology class on the product two-chart cover of (P1)^4.
2. The fixed trace orientation identifies the retained pairing for a test section p with the coefficient of x^(-1,-1,-1,-1) in pF. For ID0, p=(x1*x2+x3*x4)^2; consequently the pairing is the 1:2:1 combination at (-3,-3,-1,-1), (-2,-2,-2,-2), (-1,-1,-3,-3).
3. Any supplied N/D is an exact rational-function representation of this SAME F, with D nonzero, over a characteristic-zero field. This representation alone does not establish hypotheses 1 or 2. In particular, a rational formal-series coefficient is not automatically the designated geometric pairing.

Ordinary partial derivatives below are derivatives in the rational x coordinates after the complete scalar extraction. They are not the physical curve derivations V_i. No extra deck-product division or frame factor is inserted.

## The theorem

Let k have characteristic zero, F belong to k[x1^+-1,...,x4^+-1], and p belong to k[x1,...,x4]. Put lambda_p(F)=[x^(-1,-1,-1,-1)]pF. The following are equivalent:

(a) lambda_p(F)=0.
(b) pF=sum_i partial_i G_i for Laurent polynomials G_i.
(c) pF=sum_i partial_i G_i for rational functions G_i in k(x1,...,x4).

### Proof

Write pF as a finite Laurent sum. Except for the exponent (-1,-1,-1,-1), each monomial c*x^a has an index i with a_i != -1. It is partial_i(c*x^(a+e_i)/(a_i+1)). This proves (a) implies (b), and (b) implies (c) is immediate.

For (c) implies (a), fix the field K=k((x1))((x2))((x3))((x4)). The polynomial ring embeds injectively in K, hence its fraction field embeds uniquely. The usual four partial derivations extend coefficientwise to K and agree with rational derivatives on the embedded fraction field. Define Res as successive extraction of exponent -1 in x4,x3,x2,x1, in that order. It annihilates partial_i G for every G in K: for the differentiated variable, the only possible contribution to exponent -1 would come from exponent zero, whose derivative is zero; for the other variables, coefficient extraction commutes with differentiation. For Laurent polynomials this Res is precisely their ordinary joint coefficient at (-1,-1,-1,-1). Apply it to (c).

The argument allows certificate poles not present in pF because it is a fixed formal iterated-residue argument. An analytic contour argument would instead need to justify avoiding all certificate poles. There is no claim that arbitrary rational iterated residues are independent of expansion order; only the Laurent left-hand side has that independence.

This is an elementary calculation of top-degree algebraic de Rham cohomology of the algebraic torus, giving a one-dimensional quotient by divergences. It does NOT reduce the unknown 30 pairings to one known scalar: the unknown linear functional still has 30 input values.

## Certificate interface without constructing the Laurent quotient

Suppose F=N/D, with N,D polynomials and D nonzero. For any nonzero polynomial Q and polynomials A_i, the exact polynomial identity

    p*N*Q^2 = D * sum_i (Q*partial_i A_i - A_i*partial_i Q)

certifies pF=sum_i partial_i(A_i/Q), hence lambda_p(F)=0 under the geometric hypotheses above. Equality must hold in the polynomial ring, not merely at sampled points or modulo unverified relations. Compact factored identities may provide proofs; no production identity is asserted in this packet.

For the restricted ansatz G_i=A_i/D^m, m>=1, the certificate simplifies to

    p*N*D^m = sum_i (D*partial_i A_i - m*A_i*partial_i D).

At a fixed denominator exponent and fixed numerator-support bounds, this is linear in unknown coefficients of A_i. Failure to find a certificate with those bounds has no nonvanishing consequence. There is no established small-certificate or computational-cap bound.

A common reduction/denominator infrastructure may be reused across the 30 authenticated p_j. A single identity with 30 independent formal parameters merely batches all 30 identities; it does not prove any of them for free. A successful certificate is a mathematical alternative to exact whole-quotient coefficient extraction, not a replacement inside the existing guarded implementation.

## Invented symbolic control and negative mutation

Set u=x1*x2 and v=x3*x4. Define invented Laurent polynomial

    F0=u^-3*v^-1 - u^-2*v^-2 + u^-1*v^-3.

Its three target coefficients are (1,-1,1), so their weighted sum is zero although no individual coefficient is zero. For p=(u+v)^2,

    p*F0 = u*v^-3 + v^-2 + u^-2 + u^-3*v = partial_1 G1,

where

    G1 = x1^2*x2/(2*x3^3*x4^3) + x1/(x3^2*x4^2)
         - 1/(x1*x2^2) - x3*x4/(2*x1^2*x2^3),
    G2=G3=G4=0.

Replace the middle coefficient -1 by 0. The resulting Fbad has lambda_p(Fbad)=2. Therefore no rational divergence certificate exists for p*Fbad by the theorem. The supplied checker verifies both coefficient and derivative identities, rejects the mutated certificate, and verifies the denominator-interface identity in an invented polynomial representation. All arithmetic concerns only these invented scalar examples.

## Relation to the current proof repair

The same-raw mixed-sector theorem proves Cech closure delta_row R_raw=0. Cech closure does not assert de Rham exactness of pF. Associativity does not supply this new certificate. The full S4/sign2 boundary and residual30 are left unchanged. ID0 and the actual obstruction remain unknown.

A global residue theorem would require accounting for other poles and infinity contributions; it does not alone force this chosen residue to vanish.

## Sources and matching assumptions

Verified online on 2026-10-18:

- Bostan, Lairez, Salvy, *Creative Telescoping for Rational Functions Using the Griffiths-Dwork Method*, https://arxiv.org/pdf/1301.4313, sections 2-4. This supplies the connection to reducing rational functions modulo divergences. Its complete Griffiths-Dwork reduction theorem assumes finite-dimensional homogeneous Jacobian quotient, corresponding to the stated projective smoothness condition. That condition has not been checked for any production denominator. The elementary exact-identity certificate here does not require it. The paper also distinguishes regular certificates for analytic integration from certificates introducing new poles.
- Stacks Project, *de Rham cohomology of a line bundle*, https://stacks.math.columbia.edu/tag/0FU8. Laurent grading and logarithmic residue explain the conceptual background. The precise elementary theorem used here is proved above, without importing a stronger geometric theorem.

Local context inspected: the public ID0 correctness-boundary proof, retained-ID0 certificate README, and same-raw second-order closure proof. Their geometric hypotheses are not replayed or discharged by this packet.
