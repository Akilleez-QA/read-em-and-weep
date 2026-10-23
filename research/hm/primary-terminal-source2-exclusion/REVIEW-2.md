# Independent whole-proof review 2

Verdict: **PASS for the stated conditional exclusion.** I found no mathematical blocker in the complete proof. The conclusion must retain the complete actual-source transfer and nonzero pure-V Q-compatible radical hypotheses of PR1072; it is not an unconditional exclusion of every formulation called source2.

Reviewed snapshot:

- PROOF.md SHA-256: `7be070050a035ceec64c5698fd1ae70857225a405e1a43d4cbebc4019f5a342a`.
- verify.py SHA-256: `0c990122d3a27e06830e6edec8c48d79f3f0adec42d70beebbe780e50571b08a`.
- INPUTS.json SHA-256: `fc06c58155ac4c49e570d7b27f0ce2ef78e745a1a7610df8e2abd037065ffde4`.

This is a mathematical review of the entire candidate argument, including its actual-map premises, not merely a checker pass or a character comparison. It is not proof-assistant certification or a fresh proof of every upstream HM theorem.

## 1. Independent authentication

I independently fetched all five complete originals through the GitHub connector at the exact immutable commits in PROOF.md. I reconstructed each Git blob SHA from the returned UTF-8 bytes, computed SHA-256 and length, and compared those bytes with the corresponding files in inputs/. All five matched exactly. I then checked the independently obtained records against every corresponding authentication field of INPUTS.json.

| Original | Returned/recomputed Git blob | SHA-256 | Bytes |
| --- | --- | --- | ---: |
| PR477 | 1cb91b7f5b7da08b6653c7fa48487ff7c3fd7198 | 0325c7b3cf237e27d4466e17c50cdb7f1a5cd874c310f32c03516acc250a2a38 | 10321 |
| PR486 | 93a379dc422c45b4fad210d782169abc3583c286 | 0e7df08243d9cd60c812d29f57a88edd8bd87880670f640f7e6ac4562d740e41 | 10493 |
| PR1120 | af00766042cdc7e100731aa69b9ad8d32db0209f | b47031d81c8c138aa5f1b4c4cee992f9ae04ee74adb8c403cedd2e74c51a2d2e | 10894 |
| PR1121 | 719ba5260fa9d0d1b548c867c2504d627552ba24 | 9e9fdc021f3c9dbec4f09dad1c0aa3e4a4a634227d6d65e50de7ac56fb88581b | 12423 |
| PR1072 | 65dda3e16ded2b79ad84c583f248b09c425e9881 | deed62f4bb764abe7d1e819b780a09dfbbe0a36f8fdb608cba24c0b0187e6735 | 9164 |

Exact URLs, byte-comparison results and supplemental source digests are recorded in AUTHENTICATION-REVIEW-2.json. To interrogate the delicate projector bridge, I additionally fetched and read PR1056 at 875e86e2eec36a050e9a626735199681762e43ec, PR795 at 3f811311d76914a555c7e7d0c5b887b41805aa6c, and PR1068 at 05e8b33eb87e9f36aa30500145cc42bc0ea00df8. These are the originals referenced by PR1072, not substitutes chosen by matching characters.

## 2. Primary inclusion, grading and physical parity

PR477 first constructs the maps from the evaluation Eagon--Northcott resolution and Serre duality, proves polynomial-linearity, and only afterward proves injectivity. Thus the relevant map really is U tensor Aprim(-3) into K, with the polynomial action on the primary factor. No module splitting is needed or asserted. Its nonsplit nature is harmless here.

The grading translation is exact: L5=U tensor H1(F(2)) lies in K5=H1(B(4)); L6=U tensor H1(F(3)) lies in K6=H1(B(5)). PR1120 and PR1121 use the current physical marking, identify U=P as positive, identify H1(F(2))_+=1+A, and identify the entire H1(F(3))=W as negative. Their monad calculation is converted from an Euler character into actual cohomology using higher-cohomology and H0 vanishing; the candidate does not mistake a K-class for cohomology.

Consequently V kills the actual Y=H1(F(2))_+: its image would have to be positive inside the entirely negative H1(F(3)). This statement concerns the primary module, not all of H1(B(5)). Tensoring by the positive constant U preserves the needed parity. The source and target of the primary terminal pencil therefore really are subspaces of M4=H1(B(4))_+ and M5=H1(B(5))_-.

## 3. Levelness forces the actual curry isomorphism

If c(y)=0, every negative coordinate kills y; parity already kills all positive-coordinate products. For a fixed nonzero u in U, polynomial-linearity makes the image of u tensor y an element of the full five-variable socle of K in degree 5. PR486 proves that the socle is concentrated in degree 6. Injectivity of the actual primary map then forces u tensor y=0 and hence y=0.

This is a valid use of global levelness, not negative-coordinate levelness or a selected-direction nonvanishing assumption. The dimension equality is used only after injectivity has been proved. Thus the actual curry Y -> Hom(W,Z), with Z=H1(F(3)), is an isomorphism. It is the given multiplication, not a selected normalization of abstract intertwiners. No unknown arrow scale has been assigned a value.

## 4. Exact universal evaluation pencil

Let L=O(-1) be the actual parameter line in W. The kernel of Hom(W,Z) tensor L -> Z is Z tensor (W/L)* tensor L. Since det W is trivial and W/L is O(1), this is Z O(-2). The arrow is fiberwise onto because all linear maps W -> Z occur, so it is an exact sequence of vector bundles everywhere, not merely generically. Tensoring by U gives source dimension 16, target dimension 8, and kernel 8O(-2) of degree -16.

The frozen proof explicitly uses PR1072's original parameter line, or a common fixed determinant pullback for both pencils. There is no independent rotation of the primary pencil. Equivariant linearizations also agree: the negative Z and O(-1) factors have the required physical central signs. No sign ambiguity can alter the bundle degrees or the actual commutative coefficient diagram.

## 5. The source2 first block extends to the actual terminal degree

This is the most important premise to audit. PR795's separation E=E0 direct-sum ER is a genuine constant-block separation of the evaluation construction, transported only under its stated actual-source/common-pencil hypotheses. It is not inferred from the splitting character of E.

PR1056 identifies M4 with H1(E) and M5 with H1(E(1)) using the same actual source-pencil kernel. It explicitly states M4=H1(B(4))_+ and M5=H1(B(5))_-. Its determinant rotation identifies cohomological parameter multiplication with actual negative multiplication. PR1072 Section 2 then checks the second rotation from the diagonal resolution and shows that the two cancel, recovering the original fixed-parameter next pencil.

Therefore the genuine inclusion/projection maps of E0 and ER induce coefficient-space projectors in both degrees 4 and 5 which intertwine each of the two actual negative-coordinate arrows. Applying the diagonal resolution to E0=W O(-9) gives exactly the first-block kernel W O(-8), not W O(-9), at the terminal step. Its coefficient dimensions are 16 and 14. Twisting 0 -> (P+D)O(-2) -> ER -> T6 O(-3) -> 0 by one kills the left term's cohomology, so H1(ER(1)) has dimension 6. This establishes the actual residual target, rather than selecting one of the three ambient T6 copies by character.

No extension of the homotopy is needed. No commutation of the projectors with positive coordinates or Q is needed. The candidate uses only the negative projectors already supplied by the exact source theorem.

## 6. Hom vanishing and final contradiction

The Hom direction in the lemma is correct: a coefficient morphism from the primary pencil to the first block sends O(-2)-kernel summands into O(-m)-kernel summands. The corresponding Hom is H0(O(2-m)), which vanishes for m>2. Once the source coefficient map kills its kernel, the exact quotient factors it through A2 O. There are no maps A2 O -> C1 O(-1), so that coefficient map is zero. Surjectivity of the primary pencil then forces the terminal coefficient map to be zero as well.

This is stronger than just vanishing of the kernel map, and the factorization step is essential and valid. It applies without equivariance and hence also with it. The m=2 boundary would permit morphisms; the proof does not claim otherwise.

Composing the actual primary inclusions with e0 therefore gives zero at both terminal coefficients. In degree 5 the original injective 8-dimensional primary target must land in ker(e0)=NR5, which is 6-dimensional. This is impossible. The optional W' versus T6 argument reaches the same conclusion but is not necessary. Neither primary/source character equality nor positive-projector preservation is smuggled into the contradiction.

## 7. Checker and scope

I inspected verify.py and ran both normal Python and Python -O. Both returned PASS with 56 controls, and their complete output bytes agree with RESULT.json. The script has no selected HM/source-instance data. Its only pencil systems are small formal universal controls; the nonzero m=2 case and zero m=3,8 cases agree with the sheaf argument.

The final checker uses an independently specified W' character row, so the displayed product identity is not tautological. I inspected this final revision and reran both modes after the change. Actual cohomology identifications and actual-map facts remain supplied by the authenticated written inputs and the mathematical review, not certified by this arithmetic.

The entire proposed deduction is sound relative to its pinned structural inputs. It excludes the conjunction of actual-source hypotheses that supplies PR1072's genuine negative separation and terminal residual. It neither disproves the existence of the abstract universal source2 models nor selects an actual remaining source, decides an original polynomial pair, proves higher-obstruction vanishing, or establishes algebraicity. No selected actual coefficient, tensor, matrix, point, parameter, derivative, instance rank, scan, large computation, or public write was used in this review.
