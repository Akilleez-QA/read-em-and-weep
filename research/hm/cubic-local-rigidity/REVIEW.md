# Independent review of formal local rigidity and nonsmoothability

## Verdict and reviewed version

**PASS: no mathematical correction is required for the stated theorem and the stated nonsmoothability consequence.** This is an independent mathematical review, not a proof-assistant verification.

Reviewed file: `PROOF.md`, Sections 1–9.

SHA-256 of the reviewed proof:

    c431816d57cf564caeb241f20951de873d45b720e5bbbddab481ce20d8372364

Before recording the final hash above, the reviewer changed only the proof status sentence from prepared for review to independently mathematically reviewed (PASS). The substantive proof text was unchanged; its pre-status-edit SHA-256 was `301cdefba26c528f6f40106089285e056b42af6eb587b9361ada45a0093796fd`.

The review checks the universal commutative-algebra and deformation arguments. It accepts the explicitly cited geometric inputs identifying the completed singular germs of the actual images with A_4 and A_2, and their smoothness elsewhere. It does not independently re-prove those geometric inputs, compute HM coefficients, or investigate the original HM source. The mathematical conclusion about the actual images follows once those cited inputs hold.

## Checks performed

1. **Correct degree-one deformation module.** The conormal cokernel is the correct continuous cotangent T^1 presentation. The argument does not incorrectly identify the entire cotangent complex with a two-term complex, assume that the conormal map is injective, or substitute Ext^1 of the ordinary differential module. The truncation statement is correct in degree one. The polynomial conormal-cokernel and lift-classification references cited in Section 2 support the corresponding ordinary algebraic statements. Section 5 independently supplies the required complete-local deformation argument.

2. **Conormal homomorphisms and constants.** Projecting the row syzygy to C[[u]] and reducing modulo u_i proves divisibility by u_i, using another u_k. Cancellation proves independence of the quotient from i. The column argument is identical. The common constant of each fiber-product pair consequently vanishes. Nonzero constants in a_j or b_i cause no problem: the inclusions C[[u]] and C[[v]] into A carry constants to equal constants on both branches. The displayed ambient derivation therefore realizes the entire conormal homomorphism. Only necessity of the displayed syzygies is needed; no completeness claim about a syzygy list is hidden in the proof.

3. **Small-extension flatness and corrections.** For a small extension with kernel K annihilated by the base maximal ideal, flatness gives an injective multiplication map K tensor R' to R', with image KR'. It identifies this image with K tensor_C A. Multiplication there factors through the special fiber, so the exact product identities give precisely the componentwise syzygies used in Section 3. Subtracting b_i and a_j from the respective coordinate lifts kills every product because K^2=0. These corrections remain in the total maximal ideal, including when their coefficients have nonzero constants on the special branches.

4. **The comparison homomorphism is genuinely an isomorphism.** Since the Artin base is finite-dimensional over C, its formal power-series quotient is the ordinary tensor product A tensor_C B' and is B'-flat. Surjectivity of the comparison map follows from its reduction and nilpotence of K; no unsupported finite-generation assumption on an additive cokernel is needed. After surjectivity, target flatness supplies the Tor vanishing needed to identify the kernel modulo K. The resulting identity L=KL forces L=0. Thus the proof extends a prescribed trivialization, rather than merely producing an unrelated one.

5. **Formal limits.** Compatible trivializations can be chosen inductively precisely because the preceding lifting statement preserves the previously chosen one. A Noetherian complete local ring is complete and separated for an ideal contained in its maximal ideal: ideal-adic Cauchy sequences are maximal-ideal-adic Cauchy, and the relevant ideals are closed. Hence the inverse-limit step recovers the given total ring and the claimed constant formal family. This does not assert convergence or algebraization of the trivializing coordinates.

6. **No-smoothing argument.** Section 7 correctly specializes to equal branch dimensions m=n=d. Completion preserves flatness and identifies the special completed local ring. Completion of the finite relative differential module represents the continuous relative derivations of the completed total ring; the product rule gives the needed continuity into finite complete modules. Its presentation has the stated Jacobian entries. The selected diagonal minors produce all pure degree-d monomials, while mixed monomials vanish, proving Fitt_d=(u,v)^d over C[[t]], not only after setting t=0. Generic smoothness of pure relative dimension d makes the original Fitting ideal a unit after inverting t, so it contains some t^N. Its completion cannot contain t^N, since quotienting by (u,v) yields C[[t]]. This contradiction does not require an algebraic section or algebraization of the formal coordinates.

7. **Algebraic local T^1 and its sheaf.** The added Section 8 is valid. A smooth local ambient presentation computes algebraic T^1 by finite modules. Flat completion commutes with Hom out of the finitely presented conormal module, and with the cokernel. Its completed presentation is the continuous cotangent presentation of the completed local ring. Faithful flatness then descends vanishing. Together with the given smoothness away from the finitely many singular points, this proves vanishing of the coherent local T^1 sheaf. The proof correctly separates this from global cotangent cohomology and does not eliminate possible H^1 of the tangent sheaf.

## Exact scope and limitations

- Local Artin C-bases are understood in the usual deformation-theoretic sense: residue field C and finite dimension over C. Families are Noetherian complete local and flat, with a marked special fiber. The complete-base extension has the analogous residue-field and completeness conventions.
- No chosen section, fixed ambient embedding, or fixed branch coordinates are part of the deformation problem. The nilpotent constant coordinate corrections are therefore allowed. A problem imposing such extra data requires separate analysis.
- Trivializations are not asserted to be unique; infinitesimal automorphisms may remain. No T^2 vanishing is needed or proved.
- The nonsmoothability conclusion applies to the specified flat finite-type families with smooth generic fiber of the same pure dimension, over the stated curve or discrete-valuation bases. It is not a claim of global rigidity or stationary embedded deformations.
- No conclusion is transferred to the HM source, full-adjoint construction, prescribed-source lifting problems, or unrelated algebraicity gates.

No counterexample to the theorem was found. As a boundary check, m=n=1 is the node and has T^1=C. The stated assumption m,n>=2 is sufficient but not sharp: the same argument also gives rigidity when exactly one branch has dimension one and the other has dimension at least two. This optional strengthening is not needed for A_4 or A_2 and does not affect the verdict.
