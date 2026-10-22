# Independent structural review

Reviewed `PROOF.md` at SHA256:

    64ca84b58edcfc20410bdc2b31dd9b0b1cd9d0add001aa5005b3339953230e8f

Outcome: PASS. This is an independent mathematical review, not proof-assistant certification.

## Source identification

Both cited files were read directly at commit `8d8b5be4ce62c3055bb53be9e16d29cc63072f04`. The vertex/quintic note, sections 1–2, explicitly identifies the actual flat quotient and its cubic relation subbundle. The universal cubic note alone would not establish that actual identification; the proof correctly uses the companion to supply it. The latter note's sections 1–2 establish the complete cubic series and its dual evaluation arrow; section 3 explicitly confirms that A and V are nonisomorphic irreducible three-spaces.

Twisting the actual relation line by O(-1) gives O(-3) in the trivial Sym^3 U bundle. Its projective morphism therefore pulls back O(1) to O(3). The determinant pairing convention identifies dual binary modules equivariantly, so neither the projective morphism nor the tangent-vector-field argument confuses W with U. A change of local generator by a nonzero scalar does not change its projective cubic or its multiplicity pattern.

## Arguments checked

1. Geometric generic containment in the pure-cube locus implies containment of the entire image: the source is reduced and the locus is closed. The inverse of the Veronese on its image supplies an equivariant factorization. Degree forces a projective isomorphism, whose pushforward on global tangent fields would identify A with V, a contradiction.
2. The pure-cube twisted cubic is defined set-theoretically by quadrics. Their pullbacks have degree six. A single triple fiber would supply an invariant orbit of at least twelve zeros to every pullback and hence force the forbidden global containment. This uses the orbit bound on the negative projective line, unaffected by the binary center.
3. If all cubics were singular, absence of triple cubics makes their repeated and residual projective factors unique. They descend over C(L), extend to morphisms from the smooth complete line, and are equivariant by uniqueness. The degree identity 3=2 deg(r)+deg(s) is incompatible with irreducibility (excluding degree zero) and A not isomorphic to V (excluding degree one). Thus the discriminant pullback is not identically zero.
4. The universal binary cubic discriminant has degree four, so its nonzero pullback has degree twelve. Its invariant effective divisor and the minimum orbit size twelve force one orbit with multiplicity one at every point. The absence of triple cubics makes every singular fiber double plus simple; all others have three distinct factors.
5. The PR764 proof was also read. Its necessary condition applies to the same actual regular cubic/quintic pair, with arbitrary fixed nilpotent first-normal lift. Noncube therefore excludes image(K) contained in k d and hence the common-direction alternative. No converse or extra equivariance of the modular gate is assumed.

No actual coefficient, point, root, derivative, discriminant, source pair, matrix or rank was evaluated. The review consists of source reading and structural mathematical deductions. The conclusion concerns the specified cubic relation and source-operator obstruction; it does not identify the fourth Bockstein or establish algebraicity.
