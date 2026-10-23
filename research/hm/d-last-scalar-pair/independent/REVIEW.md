# Independent whole-proof review: D-source scalar pair50

## Verdict and immutable scope

PASS, relative to the explicitly pinned actual geometric inputs. The reviewed proof excludes precisely original D-source ordered pair50, with A=O(-8)+O(2)+O(4) and B=O(6)+O(-4)+O(-6), in maximal Gauss-rank-three profile(1,1). It does not itself establish coverage of every profile or complete the original proof repair.

The exact author artifacts reviewed are:

- PROOF.md SHA256 `590dfb8da397d866059bf341b66eca2c7e408819fbf3fa2d7257313ab1f5d619`.
- verify.py SHA256 `1098eec3826a8bb35afc523cc93ba3be1116e31d5837b9a069855317547ce98f`.
- RESULT.json SHA256 `6ae1126050a074efcc989a7b7536ca8bb230078f9ce9167e553144d75278d5ea`.
- INPUTS.json SHA256 `1ff429f45d8bc9cd3a23ff9d65f1564add97fe50a13a644d9a7359f673f1f1ae`.

All eight full immutable public originals were freshly fetched with the connected GitHub reader, compared byte-for-byte to the retained inputs, and authenticated by SHA256 and Git blob identity. The stored fresh responses contain public source text only. Authentication was not inferred from the author's previous checks. The whole proposed proof and the relevant full dependency arguments were read.

## Highest-risk bridges examined

1. **Actual nested images, not saturated replacements.** Twisting the genuine derivative injection G_(j+1) -> G_j(-2) by 2j+2 gives G_(j+1)(2j+2) -> G_j(2j). Its composition into B is precisely the next composite image. Thus I_(j+1) is a subsheaf of I_j. On equal-rank stretches the generic plane is fixed, and the determinant divisor is effective; degree cannot increase. This excludes disappearing torsion rather than incorrectly discarding it.

2. **Exhaustive small deficits.** Invariant Hom degrees in wedge2 B and B give respectively {0,2,12} and {0,10,12} within budget12. There are nineteen raw height-seven allocations: seven placements of12 and twelve placements of one2 plus one10. The latter require incompatible exact rank-two planes. Monotonicity on each equal-rank stretch leaves exactly j3 or j7. Rank-two deficit12 is not presumed to be a saturated constant plane.

3. **Height bound and the two easy heights.** PR1163 gives F8=0 from actual source global generation after twist8 and actual spanning. This does not rely on a guessed full coefficient system. Height five violates strict-top. Height six supplies a saturated degree-minus-six line with derivatives through six in S; polynomial Taylor inversion puts a nonzero constant coefficient vector in S. Saturation extends the dense-chart containment globally.

4. **Partial apolarity and dual convention.** For a possibly proper coefficient quotient q:Sym^n W -> R, q* embeds R* into the full dual polynomial space. Actual annihilation of the projected osculating vectors implies annihilation of the universal osculating fiber after this injection. Its annihilator is l^(k+1) Sym^(n-k-1), independent of whether q is injective. With pairing <x^(n-i)y^i,x^i y^(n-i)>=(-1)^i/binom(n,i), pairing with (u x+v y)^n evaluates the polynomial at (v,-u). Thus a common homogeneous factor becomes its fixed determinant rotation in every actual coordinate. It still has a projective zero over C. The actual line map is zero in that fiber, impossible for a saturated line subbundle. No unsupported identification of q with a complete system is made.

5. **Exact coefficient span.** The factor map has exactly the claimed active coefficient space because all higher source degrees have zero Hom and the surviving coefficient map is nonzero into a multiplicity-one irreducible. Spanning of E, or of the residual F, forces equality of R* with the span of those image fibers. Mere containment would not suffice, and is not used. The j7 image is F12 Sym8; the final residual image is F12 Sym10.

6. **Genuine constant splitting in the j3 case.** Injectivity of the successive graded derivative maps gives eight independent generic jet directions of the actual terminal O(-8). Since every proper quotient of Sym8=P+D has dimension at most five, the coefficient system is complete. The projection of the embedded source onto the full degree-eight line has only its O(-8) block active. Its coefficient image supplies a constant complement, proving the split of the ambient and embedded bundles. Derivatives are block diagonal only after this construction. The residual ranks/degrees are rank(F)=16, deg(F)=-46, rank(S_F)=5, rank(L_F)=3, deg(L_F)=-36, B_F=O(-4)+O(-6).

7. **Residual rational-line classification and saturation.** Saturating the common generic image once gives J'=O(e) in B_F. Degree addition and parity give e in {-8,-6,-4}. Invariant Hom gaps exclude -8 and identify the two remaining exact coordinate lines. An invariant torsion divisor has degree zero or at least12. The bottom case demands total6, impossible; the top case and nested actual images force divisors (0,0,12), hence terminal O(-22). Saturation in B_F is carefully distinguished from saturation of that terminal line in the constant ambient.

8. **Final active V channel.** Multiplication by nonzero invariant F12 embeds the unique V of Sym6 into Sym18; multiplicity one identifies this with the only available V channel. Basepoint-freeness of the sextic net follows from minimum invariant orbit size12. Its two negative syzygy degrees sum6, so twisting by4 kills H1 and proves V Sym4=Sym10. The common-factor contradiction is therefore justified without a numerical rank or selected source instance.

No unresolved gap was found in these bridges. The evidence is a mathematical review with bounded exact controls, not Lean or other proof-assistant verification.

## Reproducible supporting evidence

The author's verifier produced exactly its committed RESULT.json under both normal and optimized Python: 906 reported controls, plus its imported character module checks. Independent verify_independent.py uses direct class-size character inner products rather than importing the author's character checker, integer budget compositions rather than its product enumeration, and formal symbolic apolar pairings with an indeterminate parameter. It reports 18,419 checks, including 17,550 universal apolar annihilation identities, 520 factor sign/exponent identities, and all residual deficit and line-degree cases. It never substitutes a parameter value. Normal and optimized outputs are identical.

The independent verifier SHA256 is `34964a01a4ffa5991152d9d7bbd6225a49fcb33cdd7dbfb97749d234094a552f`; its RESULT.json SHA256 is `5b1b4ada4f5f39f8c682948b7e710eb5c612f2017c5c1af192f540e3ae9b34f4`.

Run `python verify_independent.py` and `python -O verify_independent.py`, comparing each output with RESULT.json. Run `python authenticate.py PATH_TO_AUTHOR_PACKET` and its optimized counterpart, comparing with AUTHENTICATION.json. The authentication checker accepts the packet path as an argument and uses no machine-specific path.

No actual HM/source coefficients, points, jets, parameters, tensors, matrices, numerical ranks, stopped experiments, or historical enumeration reruns were used. No external write was performed during this review.
