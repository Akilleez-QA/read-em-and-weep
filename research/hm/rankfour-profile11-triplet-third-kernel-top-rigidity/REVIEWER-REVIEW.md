# Independent ENTIRE-proof review

## Verdict and exact binding

**ENTIRE-proof PASS**, conditional on the complete retained actual-geometric hypotheses and transitive assumptions stated in the three direct originals. No blocking mathematical gap was found in the frozen proof.

- Reviewed file: `PROOF.md`, every section and all 20,248 UTF8 bytes.
- Frozen SHA256: `c501c094dfe7cff853f8b0a64552b4a59478581a2d11921ec5f8f70f34bb0542`.
- Review date: 2026-10-24 UTC.
- Exact approved conclusion: original `K3=(V_alt+P+D)(-4)+O(-10)` in the retained full-positive, original `t=0`, local `delta=12`, residual simultaneous rank-seven `k=2` geometry forces `top F<=-6` and `F=(D+P)(-6)+O(-10)` as equivariant bundle type.
- This is not a verdict excluding or realizing K3, not a claim about `F^-`, and not a whole-branch, original higher-jet, or algebraicity result.

I read the entire frozen proof, all three complete direct original proofs, `INPUTS.json`, `REPRODUCE.md`, and both complete Python sources. I did not edit the frozen proof or either checker. The mathematical verdict below is separate from the finite arithmetic replay.

## Fresh independent source authentication

I made six new read-only GitHub connector calls: for each original, a complete immutable-path fetch with base64 encoding and a separate complete Git-blob fetch. I decoded and compared the full path response, full blob response, and retained local input byte-for-byte. For all three, the complete length, SHA256, and independently recomputed canonical Git blob SHA1 agree with the pinned identities. The path response's reported Git blob and immutable display URL also agree.

1. `inputs/lifted-jets-and-kernel-two.md`: commit `c565bd8b5b65829e99bdd96a7c5f076b01050465`; 13,703 bytes; SHA256 `0165fa9a854879e5b2c67885f3b0bede6c3f48b34e1c761c0ca846645a3247fa`; Git blob `cb46875b07d8d79e82aebe980685c418d975d87b`.
2. `inputs/five-kernels.md`: commit `7d71f0e2a3963cff64a069198f4415c5cfd0fe9b`; 8,501 bytes; SHA256 `4d06da768074a6e813ed295a088d862ce328a4cd33b739e88e20ac1f315de36a`; Git blob `163ba2126b6130befcc2351db7f6910d85fac2ec`.
3. `inputs/quartic-normal-map.md`: commit `06385eec63b85efac6cc25441d4b58d4fa5a8adb`; 15,127 bytes; SHA256 `205256f2772d21d81025e6c511a52de564bfd7e9e0d94cce79fc3f684b6d17ba`; Git blob `243adcdfe618e0792f330534c5c74931ad2741ac`.

The full targets, methods, measurements, and raw-response hashes are in `REVIEWER-AUTHENTICATION.json`. Fresh raw responses are retained solely in the three `REVIEWER-FRESH-*.json` files and must remain excluded from publication and selected replay. This authenticates the complete direct originals; it does not purport to have freshly reauthenticated every transitive historical input.

## Whole-proof geometric audit

### Section 1: hypotheses and actual objects

The proof correctly distinguishes the full-positive coherent image assumed in this retained branch from PR1198's theorem establishing that image only for K1 and K2. It does not extend that earlier theorem to K3 by inference. The rank/degree of K3 are 13 and -58, and the actual quotient A(2) has rank 3 and degree 6, giving rank 10 and degree -64 for K^-.

The actual constant map p and its fiberwise isomorphism on K^- are explicitly retained from the lifted-jets input. That input establishes Z4 in F, Z5 not in F, and the actual lifted Zhat4 in K^- and Zhat5 in K before assuming K2 in its later exclusion argument. These facts therefore remain available under K3. Its construction of the lifted degree-ten curve uses the coefficient span and then an actual negative-degree projection to H(-2), rather than differentiating an inverse bundle isomorphism.

The formula F6=D(-14)+W(-9) is supported directly by Section 1 of the complete quartic-normal-map input: U4=h(T4) has type D(-14), and the retained actual decomposition is F6=U4 direct-sum Z1 with Z1=W(-9). No claim about the quartic normal map's quotient connection is imported. The proof only uses original jets through order six, within the retained separation through order nine.

### Section 2: strict top and coherent W' row

A nonzero section of K^-(4) has a nonzero constant vector in the top coefficient block of K(4). Thus it produces a nowhere-zero, saturated ordinary O(-4) line in K, even if the vector is not G-invariant. The quotient K/L still has top -4. Since L lies in the actual derivative kernel, projecting its derivative modulo L gives a genuine O-linear map into (K/L)(-2), whose top is -6. Its vanishing makes this actual subbundle horizontal in the original constant ambient, contradicting its negative degree. The strict bound top F<=-5 is justified.

At that bound, H0(F(5)) is exactly the top coefficient representation. Its injection into H0(K(5)) permits only S4, T6, W'. For an actual W'(-5) summand, both components of the actual coherent derivative vanish: the lower by ordinary degree, the upper because Sym15 W=S4+2T6 has no W'. Using the coherent image O(10)+O(-10), rather than replacing its lower line by O(2), is essential and is done correctly. The induced internal derivative into (F/B)(-2) vanishes by degree, so the negative-horizontal contradiction applies again.

### Sections 3-5: unique placement and the actual octic backward ladder

The hypothetical nonzero S4(-5) map into K^- has no V_alt(-4), P(-4), or O(-10) component. Its sole possible target is the actual D(-4) block Q. The relevant Hom has dimension one, and the universal complete quartic evaluation sequence gives its nonzero generator, with kernel S4(-5) and quotient O. This proves injectivity and saturation; these are not assumed from an abstract representation occurrence. Saturation passes from this kernel through Q and K to the original constant ambient, and also to K^-.

Because R3 lies in K^-, its derivatives lie in K. Their projection modulo Q is O-linear since the scalar-derivative term lies in R3 subset Q. The target (K/Q)(-2) has top -6, so this projection vanishes. This is the key actual-geometric degree argument and does not differentiate K/Q itself.

The three subsequent second fundamental forms have the correct targets:

- R3=S4(-5) to (R4/R3)(-2)=O(-2), with kernel R2=A(-6).
- R2=A(-6) to (R3/R2)(-2)=O(-4), with kernel R1=W(-7).
- R1=W(-7) to (R2/R1)(-2)=O(-6), with kernel R0=O(-8).

Each row is an actual derivative because the preceding kernel gives the required derivative containment. Each is proved nonzero independently: otherwise the corresponding saturated negative-degree subbundle would be horizontal in the constant ambient. Each equivariant Hom is one-dimensional; its universal complete cubic, quadratic, or linear evaluation row is everywhere onto. Thus all kernels and all displayed quotient lines are saturated with exactly the asserted twists. The bottom derivative R0 to (R1/R0)(-2)=O(-8) is nonzero and hence an isomorphism. The induced maps between the higher successive line quotients are also isomorphisms. Therefore the forward-span statement is justified, not merely suggested by matching bundle types.

### Sections 6-7: projection and the annihilation rectangle

Every Rj for j<=3 lies inside K^-, so constant p is injective on all terms used. Its images are saturated subbundles of F, retain their bundle types, and retain the actual derivative containments. The proof does not use p-injectivity on R4 and never differentiates the inverse of p|K^-.

For a local lift r of the nonzero octic line, r through its third derivative lies in F subset ann(T3). The full identities with 0<=a,b<=3 are therefore valid as local-function identities. Differentiating them successively produces the triangular extension (a,b)=(0..2,4), (0..1,5), (0,6). These implications use both terms of the product rule and the already-vanishing adjacent entry. They prove annihilation of every original jet through six, not just a top pairing. The line consequently maps nontrivially into the actual intersection F6. Ordinary Hom from O(-8) to its two summands D(-14) and W(-9) is zero, since the section degrees are -6 and -1. This is a valid contradiction and proves the stronger Hom_G(S4(-5),K^-)=0.

### Section 8: T6 extension comparison inside actual K

After the other constituents are excluded, a nonzero degree-minus-five part can contain only one T6, because rank F=10. Its complement has rank four and top at most -6. The actual D(-6)=Z4 cannot project to lower degrees, and its same-degree projection to that complement is zero because no rank-four coefficient space contains irreducible D. Thus Z4 lies in the T6(-5) summand.

The Hom from D(-6) to T6(-5) is one-dimensional. Its nonzero universal evaluation-kernel inclusion has quotient O, so the actual inclusion has precisely this quotient. Lifting this summand through the actual p-isomorphism is an algebraic bundle operation, not a connection transport. Both resulting inclusions of the fixed actual Zhat4 into T6(-5) are nonzero elements of the same one-dimensional Hom space. There is therefore an equivariant isomorphism between their targets whose restriction on that actual Zhat4 is the identity.

The two maps from actual Zhat5 into actual K now agree on actual Zhat4, so their difference factors through Zhat5/Zhat4=O. H0(K)=0 annihilates that difference. This forces equality of the actual embedded images, hence Zhat5 subset K^- and Z5 subset F, contradicting the retained noncontainment. The proof requires no ordinary Ext vanishing and does not silently identify unrelated abstract extensions. It correctly yields absence of T6 and top F<=-6.

### Section 9: exact cohomology cutoffs and splitting budget

At twist five the low O(-10) in K contributes H1=S4; the top blocks contribute H0=S4+3T6+W'. The quotient A(7) has that same H0, yielding chi(F(5))=-S4. At twist four the low line contributes H1=D, the top contributes V_alt+P+D, and A(6) has V_alt+2P+2D, yielding chi(F(4))=-P-2D. The previously proved top cutoff kills both H0 groups, so these are the genuine H1 representations in the statement.

For an irreducible atom R(-j), j>=7, its twist-five H1 is R tensor Sym^(j-7) W of dimension (j-6)dim R. These are genuine positive contributions, so their sum being the single irreducible S4 forces exactly one atom with multiplicity one. The three integer factorizations of four exhaust the possibilities; the two doublets at j=8 give 1+A and P, not S4. Thus only S4(-7) and O(-10) survive. The former contributes A+D at twist four and would leave the impossible coefficient representation P+D-A. The latter contributes D and forces the top coefficient P+D. The final type has rank 10 and degree -64 as required.

### Section 10 and global scope

The stated boundary is accurate. All differentiations in the new argument occur in actual embedded subbundles of constant ambients. Birkhoff splittings are used only to describe morphisms. No quotient connection, horizontal splitting, inverse differentiation, selected actual coefficient or point evaluation, original degree-eighteen jet extrapolation, or existence assertion occurs. The only numerical computations are fixed small universal representation identities, degrees, and formal differentiation implications.

## Checker-source inspection and isolated replay

I inspected both complete Python sources. The main verifier pins the entire frozen proof length/hash and all complete direct input identities. Its checks use explicit exceptions, not assertions removed by optimization. The character source performs 81 fixed exact-rational McKay identity checks; its recurrence computes only fixed small universal symmetric-power products. There is no source-instance input, broad search, network access, package installation, or remote write in either program. As the verifier itself states, its arithmetic PASS does not certify geometric actuality, saturation, or the logical implications audited above.

I created a newly empty isolated directory and copied only the eight files listed in REPRODUCE.md, preserving relative paths. Both standard-library-only runs used empty PYTHONPATH and PYTHONDONTWRITEBYTECODE=1:

- Normal Python: PASS, 77 main guards and 81 character checks.
- Optimized Python (-O): PASS, 77 main guards and 81 character checks.

The two complete stdout byte strings are identical, each 3,978 bytes, with SHA256 `518b85c3d6885c8dbb0fd8e8f1a4c4bfab4eed4a1d743dda4779847a47a5000c`. Both processes exited zero and emitted no stderr. The selected directory contained exactly the same eight files after replay, with no bytecode or cache creation. `REVIEWER-REPLAY.json` records the copied-file manifest, environment, commands, complete outputs, and measurements.

## Final assessment

The frozen entire proof passes independent review at the exact hash above. Its two main new mechanisms are valid: the unique quartic placement forces an actual octic ladder whose constant projection contradicts the known F6 top; the remaining T6 top must coincide with the forbidden actual fifth lifted jets by a comparison factoring through O. The resulting strict cutoff makes the small irreducible cohomology budget decisive. No revision of the frozen proof is required for this conditional conclusion.
