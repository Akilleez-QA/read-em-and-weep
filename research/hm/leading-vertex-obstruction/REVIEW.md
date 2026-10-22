# Independent mathematical review

## Verdict and reviewed version

PASS, conditional on the explicitly pinned geometric inputs. No mathematical correction remains outstanding in the reviewed proof. This is independent mathematical review, not proof-assistant formalization and not an evaluation of any actual HM/source instance.

Reviewed PROOF.md SHA-256:

    23dfa351615c0c46f0eb2de055fd7bc36ccc1cb6ac90ba317aad92cbaaef32f3

Reviewed verify.py SHA-256:

    9f725e2ef730a4efdc66b3ed7ebe69a30096982313ba138c806785e640cb9437

The review checked the PR685 global completion classification, PR691 scalar factorization and PR692 actual harmonic-frame/order statements against their proof texts. The pinned square-filtration theorem at commit 8d8b5be4ce62c3055bb53be9e16d29cc63072f04 was fetched independently to check the uniform quotient dimensions, relation-bundle sequence and polynomial restriction identification.

## Checks

1. In the fixed harmonic frame, the negative-coordinate source a is q-independent and has binary weight zero over k=C(L). This permits extracting a squared from the square coefficient. A change of equation or trivialization not preserving these conventions would require rederivation; none is made.

2. The degree-ten scalar square term is uniquely a^3 h tr(n8 K_{-2}). All cubic products involving the J3 coefficients have weight at least twelve. Regularity and parity leave only a constant lower entry in K_{-2}; the nonzero upper entry -u0 f3^2 of n8 forces its vanishing by domain cancellation. This does not invert h as a regular function.

3. The eight displayed ordered cubic products are exhaustive. Their minimum weight is twelve, so only P,M,R contribute there. A trace-free rank-two matrix over the commutative ambient coefficient algebra has scalar square; taking the harmonic coefficient and its leading weight preserves this property. Thus scalar extraction tr/2 has the stated normalization.

4. After K_{-2}=0, the only fourth-coefficient term at weight twelve is a^3 h tr(n8 K0). Its divided degree-eight contribution is in f3^2 Sym^2 + k f3 g5 = (I0^2)8. The identity first establishes polynomial divisibility of C by h for the actual data, rather than presuming that divisibility. Equation (2) is consequently valid in the associated degree-eight quotient.

5. The regular-pair trace equation has weight-four kernel D=ell[[f3/2,0],[g5,-f3/2]], with ell of degree one. Direct substitution into 2 f3 g5 x-f3^2 z+g5^2 y verifies the sign. The ambient dimension is 15 and the kernel dimension is 2; the image has dimension 13, agreeing with the degree-twelve square-ideal component and the cited socle bound. The resulting affine two-dimensional solution space is a local homogeneous space, not global completion freedom.

6. Changing R by D affects exactly four cubic products and introduces no quadratic D term. The undivided target in (5) is essential: an arbitrary trace-kernel change need not preserve h-divisibility. Global changes classified in PR685 instead change L2 only at weight at least eight and therefore leave R unchanged, with a,h,b,Ua fixed.

7. Section 4 is a valid additional global criterion. The pinned uniform fiber quotient dimension five gives constant rank four for the rank-four-to-rank-nine relation map, hence a locally free quotient Q4(6). A generically zero quotient section is zero everywhere on integral L. Since H0(P4 O_L(-2))=0, the global 27-dimensional polynomial block injects into H0(Q4(6)). Together these facts prove the equivalence in (6), including source-zero points, without extending square-ideal membership by Hartogs or replacing the full filtered ideal by its initial ideal.

## Scope retained and improvements incorporated

The final version explicitly retains the h-divisibility caveat for arbitrary local changes, separates local affine freedom from global completion freedom, and adds the verified relation-bundle argument for global scalar detection. No numerical rank of the residual map is inferred. The criterion is not decided: neither vanishing nor nonvanishing of the actual scalar is established. The scalar-square gate is not identified with a later Bockstein value, higher-order lifting or algebraicity.

The bounded verifier was run independently and returned:

    PASS: eight ordered cubic tags; leading-degree isolation; four retained variation tags; weighted kernel and dimension audit.

This audit checks finite symbolic index and dimension bookkeeping only. It does not verify the pinned geometric theorems, compute actual coefficients, or constitute formal verification.
