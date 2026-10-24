# Independent whole-proof review

## Verdict and exact target

PASS. No blocking mathematical gap was found in the complete frozen proof, conditional on its explicitly retained actual-geometric hypotheses. This verdict covers the argument itself, not merely the arithmetic checker.

Reviewed target: `PROOF.md`, 16075 UTF-8 bytes, SHA256 `c0b961a3a851b21906218865208c304df8390dedb72b73fb9e2b912a33d68d0b`. The proof was not edited. Review completed on 2026-10-24 UTC.

All three complete originals in `INPUTS.json` were independently freshly fetched through GitHub read tools at their exact immutable commits, without line-range filters. Their complete decoded bytes equal the packet copies. The independent byte lengths, SHA256 hashes, computed Git blob SHA1s, and GitHub-returned blob SHA1s all match. `REVIEWER-AUTHENTICATION.json` records those checks; raw fetched-response duplicates remain local only.

The three sources were read as complete documents. The imported flags, actual jet identifications, ambient dimensions, degrees, and backward-kernel identity used here agree with them. In particular, PR1210 supplies `S^-=T2`, the actual saturated flag with `J^-/F=O(4)`, rank five and degree minus sixty-four for `S`, and the unchanged local defect bound. PR1209 supplies the actual first, second, and third jet maps and saturated images. Its quotient `J/J^-=O(12)` dualizes to `T3/T2=O(-12)`. ACTUAL supplies the physical representation and equivariant-splitting conventions; none of its rank-seventeen conclusions is applied to `S`.

## 1. Actual extension and equivariant conventions

Dualizing the actual quotient `J^-/F=O(4)` in the fixed constant pairing gives exactly `0 -> T3 -> S -> O(-4) -> 0`. Saturation of the imported flags makes this a bundle sequence, not only an equality at the generic point. Its degrees agree: minus sixty plus minus four is minus sixty-four.

For a finite group over characteristic zero, taking invariant extension classes is legitimate. The relevant Hom bundle is `Sym3 W tensor O(-11)`; equivariant Serre duality therefore gives the stated `Sym3 W tensor Sym9 W` invariant space. There is no missing determinant character because `det W=1`. The Clebsch-Gordan summands are precisely degrees twelve, ten, eight, and six, and only degree twelve contains an invariant. Thus the extension space really is one-dimensional, and its invariant line lies in the Cartan summand rather than an arbitrary tensor summand.

The proof's `W`/`W*` notation is consistent after its explicitly declared invariant alternating identification. This identification must be used coherently, not as an independent arbitrary self-duality of each symmetric power. With it, `H1(O(-11))` is the dual of the degree-nine section space, multiplication on cohomology is dual to multiplication of sections, and therefore acts as contraction. Changing the normalization of the alternating identification or divided-power conventions only rescales the displayed nonzero universal maps; it does not alter their kernels. No actual relative scalar is fixed.

## 2. Binary apolar complete intersection

The included proof is sufficient using its explicitly stated standard two-variable free-resolution theorem. For a nonzero class represented by homogeneous `h`, the polynomial `h(f)` is nonzero. If its degree is positive, at least one first derivative is nonzero in characteristic zero; hence that class is not in the socle. Degree twelve has one-dimensional image, and larger degrees vanish. This establishes exactly one socle line in degree twelve, not only an upper bound for its dimension.

The top Koszul complex has term `(R/Q)(-2)`, so its top homology is the socle shifted by minus two. Consequently the final minimal free module is `R(-14)`. The quotient has rank zero over the fraction field, and the minimal degree-zero free module has rank one; the rank Euler characteristic then forces two minimal generators. Finite length makes the Hilbert numerator divisible by `(1-z)^2`, giving the degree sum fourteen. The two generators have no common factor, since a common factor would leave a positive-dimensional quotient. This proves the asserted complete-intersection structure without an apolar instance calculation.

The equal-degree case is handled correctly. Ordering the generator degrees gives `a<=7`. If `a<7`, the degree-`a` piece of the ideal is one-dimensional and invariant under the group. Perfection of the group makes its character trivial, contradicting the minimum invariant-divisor degree. Therefore both generator degrees equal seven. Their two-dimensional representation is necessarily `W'` inside `Sym7 W=W'+T6`. The sole syzygy begins in degree fourteen, so multiplication by the generator space gives the asserted degree-eight and degree-nine pieces without hidden earlier relations.

These arguments apply to every nonzero element of the universal invariant line. They do not choose a coefficient expression for that line or evaluate the actual geometric extension class.

## 3. Cup product and polarization

For `k=m+4`, the connecting map has exactly the source and target shown in equation (15). It is cup product by the extension class. Under the dual conventions above this contracts the degree-nine factor of the Cartan polarization, rather than contracting an unrelated tensor or differentiating a quotient bundle.

The identity in equation (16) is valid universally: contraction of `m` of the nine slots in the second factor of a fully symmetric degree-twelve tensor is a nonzero scalar multiple of the `(3,9-m)` polarization of its `m`th contraction. The scalar is nonzero in characteristic zero throughout `0<=m<=9`. Multiplication composed with that polarization is a nonzero scalar multiple of the identity, so polarization is injective. The equality of the connecting-map kernel with the apolar ideal piece follows.

The cutoff is essential and is respected. At `m=9` the polarization has second degree zero and is still injective. At `m=10` the cohomology target vanishes, and the argument does not extrapolate the apolar-kernel equality there. Instead twist fourteen is treated independently using `T3(14)=S4(-1)`, whose zeroth and first cohomology both vanish.

## 4. Forced middle splitting

The cohomology values force the largest ordinary degree to be minus eleven and its multiplicity representation to be exactly `W'`. Thus its rank-two block is the canonical highest-slope subbundle, not a chosen complement to a lower-degree block.

At twists twelve and thirteen that block accounts for all global sections, eliminating ordinary summands of degrees minus twelve and minus thirteen. The remaining three summands have degree at most minus fourteen and total degree minus forty-two, which forces each degree to equal minus fourteen. At twist fourteen the representation identity cancels `W' tensor Sym3 W=V+D` from `Sym10 W=A+V+D`, leaving exactly `A` as the final coefficient representation. This establishes the nonzero middle type rather than assuming it from the dimension of the extension space.

For the zero class, equivariant splitting gives the other stated type. The highest-slope `O(-4)` maps isomorphically to the quotient since no nonzero map from it to `T3` exists. Its claimed actual complement property is therefore justified. Neither case is asserted to be realized under the full geometric hypotheses.

## 5. Actual canonical incidence

The proof correctly starts again with the actual canonical `U`, not an arbitrarily embedded abstract `W'(-11)`. Its map to the actual scalar quotient cannot vanish because the ordinary Hom space from `U` to `T3` is zero. The degree-seven entries of this nonzero equivariant row have an invariant common-zero divisor of degree at most seven. The invariant-divisor minimum therefore forces no common zeros, proving surjectivity everywhere.

Its kernel is a saturated line of degree minus eighteen, also saturated in `S` and in `T3`. The absence of scalar characters fixes the stated line linearization. The invariant degree-six Hom space to `T3/T2` vanishes, placing the kernel in the actual `T2`. The Hom space from that scalar line to `T2=A(-16)` is one-dimensional. The imported actual scalar-to-second-jet inclusion is a nonzero member of the same space, so the two images coincide. No choice of their nonzero scalar ratio is needed.

This establishes the actual equalities `U intersect T3=U intersect T2=T0` and `U+T3=S` on every fiber. The addition map has precisely the antidiagonal `T0` kernel, giving the stated pushout sequence. The argument does not mistake abstract splitting data for ambient incidence.

## 6. Intrinsic derivative of U

The distinction between the two derivatives is correct. The restriction of `beta_S` to `U` has sheaf kernel `T0` and coherent image abstractly `O(-4)`; this does not assert that its image is saturated in the normal target.

For the intrinsic derivative, a local section in `U^-` has derivative in `U`, hence in `S`, so it lies in `S^-=T2`. Thus `U^-` is contained in the actual intersection `T0`. A rank-one backward kernel would be a saturated line in `U` with the same generic line as the saturated `T0`, hence would equal `T0`. Its derivative containment, together with saturation of `U` in the constant ambient, would imply `T0^+=T1` lies in `U`. But `T1` also lies in `T2`, whose intersection with `U` is the rank-one `T0`, contradicting the rank-two first-jet bundle. Rank two for the kernel is already excluded by its containment in `T0`; a rank-zero subsheaf of a vector bundle is zero. Therefore `U^-=0` and the intrinsic derivative has generic rank two.

This proves only generic injectivity. It neither proves everywhere maximal derivative rank nor identifies the coherent derivative image with its saturation. No fourth-jet or algebraicity conclusion is hidden in the argument.

## 7. Replay, scope, and remaining boundary

Before execution, the complete `verify.py`, `characters.py`, and reproduction instructions were inspected. They contain fixed small character recurrences, the displayed universal identities, hash checks, and rank/degree arithmetic; no actual form, point, parameter, jet, tensor, matrix, or instance rank is evaluated. The recurrence validates fixed representation identities, not a broad candidate search. The explicit `require` checks remain active under optimization.

An otherwise empty temporary directory received only the eight files listed in `REPRODUCE.md`: the proof, input manifest, reproduction note, two Python files, and three complete input files. Normal Python and optimized Python both exited zero with identical PASS output and 55 checks. The selected source files remained unchanged. `REVIEWER-REPLAY.json` gives file hashes and both complete outputs. The imported character module also performs its fixed recurrence checks on import; the reported count of 55 is the verifier's explicit check counter, not a claim to count every imported comparison.

The checker does not mechanize the socle/free-resolution proof, the universal polarization identity, the geometric saturation arguments, or the derivative containment proof. Those were reviewed independently above. The conclusion remains conditional on all retained source and section gates and the specified full-positive coherent-image branch. The original defect stays zero; the new local defect is still zero or between twelve and thirty-six. No extension class is selected, no whole branch is excluded, and no realization, fourth-jet separation, higher-order integrability, or algebraicity result is claimed.

No revision is required for the reviewed frozen target. No GitHub mutation or upstream submission was performed.
