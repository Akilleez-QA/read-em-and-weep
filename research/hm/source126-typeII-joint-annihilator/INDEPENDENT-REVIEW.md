# Independent verification: Type II common annihilators

## Frozen artifacts

Reviewed 2026-10-23:

- PROOF.md SHA256 `3cbbff00b37a4e280a9a1d5a3e0c277e220eedc5c77e8055baf5a4cced2b25cc`
- verify.py SHA256 `b3b39b0695e9e251937af87a7b9e84103b0259fd65f97a809d6131ff6feee0ba`
- RESULT.json SHA256 `b8308db5bdaaf29e3a7d973edb0eebbbbf535db37e086e3515c7fabb056d01f1`

Outcome: the new deductions are valid relative to the nine pinned interfaces. The preliminary six-row list is correctly strengthened to four by a genuine Type II nonzero-row argument. No mathematical blocker remains. This review checks the new deductions and the supplied imported interfaces, not the entire antecedent geometric proof chain and not proof-assistant verification.

## Independently checked arguments

1. **Shared-D geometry retained.** The only actual constant endpoint splitting used is F plus R. The proof never splits the reconstructed Type II R into independent X and Y pencils. The source common-kernel multiplicity d in the two residual D copies describes an arbitrary subrepresentation, not a distinguished copy.

2. **Joint D nonvanishing.** The independent P-on-X and V-on-Y restrictions permit a radical with nonzero constant A coefficient. Since R spans Hbar, its image has A in its coefficient span. A bundle image contained in P O(-2) cannot have this span, since P tensor A=V+P+D. Natural Serre duality respects the target summands, so joint zero D endpoint action would imply precisely that impossible bundle factorization. With just one residual D target-source copy, joint nonvanishing means zero common kernel there.

3. **New unconditional Type II bound r≥1.** This strengthening was independently derived during review. If all P rows vanished, every radical bundle map would land in 2D O(-2). Restriction to the actual X=O(-8) must then vanish because Sym6 W=V+P has no D. Type II X spans P+D, forcing every radical's constant D coefficient to vanish. The pinned independent restriction equations instead allow that coefficient to be prescribed arbitrarily, contradiction. The argument uses X solely as an actual bundle subobject with known constant span, and therefore does not conflict with shared-D constant geometry. Unlike the separate Type I polar proof, this argument specifically needs Type II's nonzero D support in X.

4. **Four footprints.** The exact common kernels give Z=2V+(4-r)P+2D and U=A+2V+(2+epsilon)P+(2+d)D. Full-J compatibility puts the original multiplicity-free square-zero kernel A+D in U, so the restricted image character is exactly 2V+(2+epsilon)P+(1+d)D. The constituent bounds, global P-injectivity, and exclusion of surjective restrictions give six preliminary rows. The independently proved r≥1 removes the two rank-zero rows, leaving precisely (1,0,0),(1,0,1),(1,1,0),(2,0,0). Their endpoint dimensions are respectively (27,28),(32,28),(31,28),(27,24).

5. **Same actual second obstruction.** For a surjective restricted Q, corrections can be chosen within U, making their second class zero in the original cokernel. The difference from the original canonical correction lies in the original kernel. Entire original first-Bockstein vanishing therefore proves equality of the second classes; the pinned nonzero A-to-P family gives the contradiction. No claim that it is nonzero at each individual quadratic is needed here.

6. **Quotient map proved, not guessed.** Original P-injectivity proves quotient P-injectivity by the common-annihilator identity; original D-surjectivity proves quotient D-surjectivity. The resulting quotient kernel is (1-d)D and quotient cokernel is (r+epsilon-1)P. Only (1,0,1) gives an acyclic quotient. The block contraction displayed for that branch is the correct acyclic-quotient contraction, with formal inverses having no negative t powers. It is not transferred to the other three branches.

7. **Exact non-acyclic branches.** Since restricted and original kernels are the identical A+D subspace, the six-term cohomology sequence reduces to the displayed injection of quotient-kernel D into the restricted cokernel. In the two P-surplus branches, it is an isomorphism onto that entire cokernel D, whose map to the original P cokernel is zero. In the remaining d=0 branch, it injects into D+P and leaves the P image. These are canonical exact-map statements, not arbitrary chosen splittings.

8. **Forced internal first symbol.** The review independently supplied this deduction as well. In either P-surplus branch, an identically zero restricted first symbol on A would allow all first corrections within U. Their second classes would map to zero in the original cokernel, contradicting the same actual second-symbol theorem after the first-correction comparison. Thus the internal first symbol is nonzero. Because A tensor A=1+A+D with distinct irreducibles, its D-valued equivariant channel is uniquely binary-quadratic multiplication up to nonzero scalar. Polynomial multiplication by each nonzero quadratic is injective, giving rank exactly three on A for every nonzero a. There is no contradiction with zero original first Bockstein: inclusion kills the internal D cokernel.

## Reproducible execution

Executed both `python verify.py` and `python -O verify.py`. Each passed 129 checks. Their entire JSON outputs were byte-identical and had SHA256 `b8308db5bdaaf29e3a7d973edb0eebbbbf535db37e086e3515c7fabb056d01f1`, matching RESULT.json. All nine retained inputs passed SHA256 and Git-blob authentication. The tests include synthetic constituent diagrams and exact polynomial rank certificates; they are not actual HM instances. The Sym6 Hom check is an imported-character diagnostic, not a new independent derivation by the checker; its mathematical justification is the fixed McKay interface used in the written proof.

## Scope

The new r≥1 theorem is independent of Q compatibility, but the four footprint list and internal-symbol consequences require compatibility of the entire J. No row is asserted realizable. No Type II source, source-dual pair, or frontier label is excluded. The quotient D obstruction is retained where non-acyclic. No full-module extension, actual coefficient evaluation, generic full-rank result, or complete proof repair is claimed.

Final checker comments explicitly identify the Sym6 statement as the imported PR944 interface. This comment-only clarification was inspected and both 129-check runs were repeated with the same exact JSON result.
