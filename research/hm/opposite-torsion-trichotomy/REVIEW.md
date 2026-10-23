# Independent mathematical review

Verdict: PASS, conditional on the exact imported geometric results of PR934. No new actual-geometric dependency or selected-instance computation is required by the reviewed derivations. This is an independent mathematical review, not formal proof-assistant verification.

Reviewed proof SHA256: `12062795f28bdec7a2e32d421bbe667ada30d0ba98d83186750a6d4a1ee54206`.

Reviewed checker SHA256: `9a35377c451a8610bdf3e836abbbce33066d52155269bf1b85d508bb7bce1a8a`.

The review includes the final section on the vertex-ideal extension, not just the numbered theorem.

## Input binding and scope

I read the complete proposed proof and the complete local exact PR934 input at `https://github.com/Akilleez-QA/read-em-and-weep/blob/8c9847612b5f575b987cec9c62b72b099d745e44/research/hm/reduced-opposite-pencil/PROOF.md`. The input's SHA256 is `69e72653c1b7fe6925743c877210f0ee5714b284d9e1d370afd8bff279e4c1d8`, its Git blob SHA1 is `91dc4bc5c629e7ee3ba2694d2c05a4768b89b7ef`, and its size is 15,657 bytes. These agree with INPUTS.json and REPRODUCE.md. This review verifies that local binding; the author's separate remote/raw-byte comparison is not represented as my own remote check.

The imported facts used here are the actual 26-to-31 sheaf-injective presentation, the target character, the exceptional support bound, the equivariant binary two-space parameter action, and the actual exact sequence `0 -> O(10) -> D_vert -> C -> 0`. The earlier geometric proofs behind those statements are not re-proved here. No HM coefficients, selected parameter values, actual source instances, matrices, derivatives, or instance ranks were evaluated. There was no publishing or upstream action.

## 1. Orbit support, length budget, and local defects

The argument is correct after the support-based clarification made during review. Global generation descends from C to F, and F is locally free because it is torsion-free on a smooth curve. Its nonnegative splitting degrees give `length Z <= 26`.

A point stabilizer in a finite subgroup of PGL2(C) is cyclic: its tangent representation is faithful, since a finite-order automorphism fixing a point with derivative one is the identity. The possible A5 stabilizer orders therefore give orbit sizes 60, 30, 20, and 12. The six subgroups of order five have pairwise disjoint pairs of fixed points, giving the unique 12-orbit. A nonempty G-stable torsion support contained in a twelve-point set must be precisely that orbit. This does not assume that an otherwise unused exceptional set is invariant when Z is zero.

Equal stalk lengths on the orbit now give `length Z = 12m`, with `m = 0, 1, or 2`. The DVR classification distinguishes `R/(x^2)` from `k + k`; both have length two, but their Tor1 dimensions are one and two respectively. Thus the proof correctly avoids conflating total length, minimal generator number, and nilpotence order. The annihilator and fiber-kernel conclusions follow.

## 2. Canonical evaluation block and noncanonical splitting

The cohomology of the given presentation canonically identifies its target with H0(C). For any globally generated coherent M on P1, the kernel of complete evaluation is locally free, has vanishing H0 and H1, and hence is a sum of O(-1). This remains true for a torsion M; a locally free kernel need not have locally free quotient.

Because H1(Z) vanishes, the coefficient-space sequence of global sections is exact. Applying the snake lemma to the evaluation diagram gives `0 -> K_Z -> K_C -> K_F -> 0`. Twisting by O(1) gives the corresponding exact constant source-space sequence. Consequently both the subpencil and quotient pencil are actual functorial constructions, not just matching characters or dimensions.

The square torsion block has size h0(Z), equal to its length. Over a DVR, the valuation of the determinant of a square injective presentation equals the length of its cokernel, proving the divisor m Omega without selecting an actual matrix. Equality of two section divisors on P1 gives their equality up to nonzero scalar, so the f12 and f12-squared claims follow.

Finally `Ext1(F,Z) = H1(F* tensor Z) = 0`. Averaging a sheaf splitting over finite G preserves the right-inverse identity and gives an equivariant splitting. Complete evaluation then gives compatible constant source and target changes. The original proof properly distinguishes the canonical included block from its noncanonical complement.

## 3. Three maximal characters and six equivariant bundles

For m=2 the stalk's two character composition factors induce to the global-section representation on the orbit. Using composition factors is valid for both cyclic and reduced length-two modules; reducedness is not being assumed.

The C5 restriction weights yield the three indicated induced representations by Frobenius reciprocity. Direct subtraction of all six unordered induction pairs from `1 + 3A + V + 2P + 2D` gives exactly the three nonnegative results stated in the proof.

A globally generated rank-five degree-two bundle has only the two ordinary splitting types `O(2) + 4O` and `2O(1) + 3O`. Its degree filtration is intrinsic, and the relevant extension groups vanish; finite-group averaging therefore makes its splitting equivariant. For the first type, the unique O(2) multiplicity character is trivial because G has no nontrivial one-dimensional characters. For the second, the two-dimensional multiplicity is center-odd, so the binary-icosahedral representation conventions restrict it to W or W'. The identities `W tensor W = 1 + A` and `W' tensor W = P` give exactly the six displayed bundles. No two listed alternatives are being identified merely because their global-section characters agree.

## 4. Actual cotangent character and the cyclic exclusion

The crucial cotangent weight is justified, rather than replaced by an arbitrary primitive C5 character. For a lift of an abstract order-five stabilizer element to G, write its W eigenvalues as a and a^-1. Its two projective eigenlines have tangent weights a^2 and a^-2, up to interchanging the lines or dualizing W. The cotangent weights are their inverses. The nontrivial Sym2(W) weights are the same pair a^2, a^-2. Thus, under the proof's normalization `A|C5 = 1 + zeta + zeta^-1`, the actual cotangent character is zeta or zeta^-1, not zeta^2 or zeta^-2.

For a cyclic length-two module, multiplication gives an equivariant isomorphism `(m/m^2) tensor (Z/mZ) -> mZ`. Hence the two characters differ by precisely the cotangent twist. In the middle pattern their exponents both belong to `{1,-1}`. Their possible differences are 0, 2, and -2 modulo five, none of which is 1 or -1. Cyclic length two is therefore impossible. The remaining DVR type is k+k, giving annihilation by I_Omega and fiber-kernel dimension exactly two. This is a structural exclusion, not an actual-point test.

## 5. Vertex-ideal extension consequence

The added consequence is correct. Pulling the extension back to `Z_t = k^2` yields `0 -> R -> M -> k^2 -> 0`. Since the quotient of D_vert,t by M is free, their torsion submodules coincide. The ordinary local extension space is `Ext1_R(k^2,R) = k^2`. The zero class gives `R + k^2`; any nonzero class can be changed to `(1,0)` and gives `R + k`, with the kernel R included by a uniformizer in the free summand. These exhaust the local module types. Thus one or two residual torsion lengths survive at each point. Transitivity forces the same type on the whole orbit, giving total length 12 or 24. No actual extension class is chosen or evaluated.

In particular the argument does not mistakenly identify tors(D_vert) with tors(C) in general, nor does it claim which of its two allowed lengths occurs.

## Bounded checks and resolved issue

I inspected verify.py and executed both `python verify.py` and `python -O verify.py`. Both returned PASS with the three expected character patterns and two bundle alternatives per pattern. The checker uses explicit RuntimeError checks, so optimization does not remove its assertions. Its computation is confined to fixed abstract character arithmetic and tiny representation-multiplicity lists. It does not verify the sheaf or local-extension arguments; those are covered by the mathematical reasoning above.

The initial draft's only identified assumption-clarity issue was its implicit invariance of the exceptional twelve-point set. The revised proof resolves that issue by working with G-stable torsion support and proving the uniqueness of the 12-orbit. The final version also replaces 'subbundle sheaf' by the precise 'locally free subsheaf' for a torsion evaluation kernel. I verified by reversing exactly those terminology and status edits that the final proof has no other changes from the fully reviewed mathematical version.

No unresolved mathematical gap was found within the stated imported assumptions. No conclusion selects m, proves occurrence of a listed maximal case, proves local freeness of C, resolves actual source membership, changes a frontier count, or establishes mixed-map solvability or algebraicity.
