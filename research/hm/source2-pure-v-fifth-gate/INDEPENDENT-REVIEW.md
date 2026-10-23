# Independent review: the conditional fifth gate

## Verdict and frozen files

Under the retained actual-source hypotheses and the additional actual vanishing R=0, the proposed quotient fourth and original fifth are correctly defined as global sheaf symbols. The two-dimensional target, one-dimensional cubic-lift gauge, explicit basis classes and generic conditional Smith consequence are sound. The actual fifth class is not determined or asserted realizable.

- `PROOF.md` SHA256: `fd436d47461fc729137108d951a6b8c4f8f81418d0571ce3fbbe1b0060ba4b97`.
- `verify.py` SHA256: `7028739bc02584c9ac368bef2af4e523292cd39caf50c7fccbd0b00624fb17a5`.

## Global corrections and page audit

**Raw vanishing is sufficient for the new correction.** PR1025 gives global polynomial x1,x2 using constant equivariant inverses of qbar. Its uniqueness theorem identifies the raw equivariant f0x2 with R, not merely with a class modulo im B. Thus the actual hypothesis R=0 gives f0x2=0. The endpoint identity then gives f1 Tbar x2=0. Since f1 induces the stated isomorphism on H1(U), ker f1=im qbar; a constant equivariant inverse produces a global homogeneous cubic x3. No direction-dependent minor, local chart denominator, or generic-fiber argument is needed.

The next symbol is the class of Tbar x3. Its transformed representative is L f0x3, so its canonical class lies in the embedded J=im L/im B. Differences of admissible correction strings contribute only preceding symbols or the B-image of the appropriate A correction. The preceding P symbols vanish under the hypothesis, and the target quotient retains precisely im B. This gives the canonical s4, not a canonical cubic representative.

**No additional A source sheaf.** The second-symbol restriction to A is injective as a sheaf. Hence its sheaf kernel in A+P is exactly P, and the original surviving source sheaf is D. The later zero symbols retain these sheaves. Extra A vectors in specialized fibers at the six rank-drop points do not define an extra global page source. The proof correctly refrains from identifying page formation with specialization there.

**Original fifth and sign.** The original corrections x=s(p), y,z,w satisfy qx=p, qy=−Tx, qz=−Ty, qw=−Tz. The additional w exists because the raw zero lift makes iota([Tz])=0. Setting p=L_a d gives the original string d,−x,−y,−z,−w. Its fifth representative is −Tw, while the quotient fourth has representative Tbar w. This proves iota beta5=−s4 L with the exact minus sign. Generic surjectivity of L and torsion-freeness of J prove the converse implication from identically zero original fifth to zero s4, not only the forward implication.

## Cubic lifting space and independent coefficient checks

Twisting the pinned J resolution by four gives A O(2)+O(−1)→D O(3)→J(4). Vanishing of H1 of all line bundles on P2 and H0(O(−1)) gives the exact equivariant lifting quotient. Independent finite-group character arithmetic verifies dimensions three for Hom(P,D tensor Sym3 A), one for Hom(P,A tensor Sym2 A), and therefore two for the quotient. These are symmetric powers of the three-dimensional parameter representation A. The ambiguity is the m-channel only, with no kappa contribution. This describes all equivariant lifts of a fixed symbol, not freedom to choose the actual symbol.

A separately written coefficient computation used falling-factorial transvectants and the pinned universal representation model. It independently verified, on all quadratic and P coefficients,

    C4−C1/4 = −a(a²,Ep)_4/720.

The right side is nonzero and is explicitly an m-valued cubic gauge. The production full-coefficient rank-three calculation and C3=C2 therefore leave C1,C2 as a basis of lift classes. A separately reconstructed signed cofactor row of the second symbol and full original fifth rows also gave the exact coefficient minor

    20480 sqrt(5)/27

at the stated indices. This proves independence without evaluating a direction. The determinant rows annihilate the gauge, so the certificate concerns genuine classes rather than arbitrary cubic representatives. The universal nonzero classes establish a nontrivial possible target, not an actual nonzero source value.

## Generic Smith consequence and boundary

For the original 37-by-41 block over the generic direction field, the prior elimination supplies 33 unit factors and three factors of valuation two. Under R=0 the remaining row starts at order at least five. A nonzero fifth class makes its final exponent exactly five and the maximal-minor valuation eleven; a zero fifth class leaves exponent at least six or an absent pivot. This is not a full-adjoint profile or a statement about all singular fibers. Further actual identities may constrain the two coefficients; the proof explicitly does not claim to exhaust those identities.

## Authentication and reproduction

All six complete input artifacts were independently retrieved at the exact commits and paths in `INPUTS.json`. Retrieved bytes matched the retained inputs exactly, and independently computed SHA256 and Git blob hashes matched the manifest:

| Input | Commit | Git blob |
|---|---|---|
| 1019 | `3fb2475ffb275c5789acbaa8f9f84ed272713785` | `bf63c14f76933d59fa7e3ac61aecb3366ac1b442` |
| Third vanishing | `db51525015bb7c5e825833d550d08dedf6f6ea96` | `7c09fe95015d7c8d932b3a27be302ca09888112d` |
| 1025 | `09f1377f83b027ca27eea0b3a9f40a1b92c6c466` | `d036adcf5bc2bfc53e07cd752ff180c5993251f7` |
| 1097 | `2ddc4b01fa96e7ce7830b093f4df5a29dafd2187` | `990fa9adedade88b951b805aed94e6a395a7d71b` |
| 1031 proof | `7150cf97eeebe473bcd7c61c1f968c73625d92ef` | `0694e96e2d17a53b68d625ec6065f8bf513cd083` |
| 1031 model | `7150cf97eeebe473bcd7c61c1f968c73625d92ef` | `a7ca4755e50c85fe7fc20a757125127a05de4056` |

Independent executions of `python verify.py` and `python -O verify.py` passed all 31 checks, with outputs byte-identical to each other and `RESULT.json`. Explicit checker failures remain active under optimization. The additional independent character, gauge and full-row-minor computations described above also passed.

This authenticates the immediate inputs and their use without claiming a recursive reproof of all ancestral geometry. The page/correction reasoning was audited separately from symbolic ranks. No actual source coefficients, directions or instance ranks were evaluated. Independent mathematical review completed 2026-10-23.
