# Independent whole-proof review

## Verdict and exact target

PASS. No mathematical correction or required revision was found in the complete new proof. This is a review of its arguments, not an inference from the verifier's success.

Reviewed target: `PROOF.md`, 16069 UTF-8 bytes, SHA256 `135c74cc09d4f1da1fcae16c330e0c9d5a9d05d615e59a2461dd532cbb91a62f`.

The conclusion is correctly conditional on the complete retained actual-geometric hypotheses. It establishes the necessary restriction `delta in {0,12,20,24}` and the stated conditional cyclic defect at 24. It does not establish occurrence of any remaining value or exclude the whole branch. No other review was used to reach this assessment.

## Complete-source authentication and dependency audit

I freshly fetched all three complete originals with the GitHub file-read tool at the exact immutable commit/path pairs in `INPUTS.json`, omitting line-range arguments. I independently compared the returned UTF-8 bytes against the local inputs and checked byte lengths, SHA256, the GitHub-returned blob SHA1, and locally recomputed Git blob SHA1. Every comparison passed. `REVIEWER-AUTHENTICATION.json` records the results. Raw tool responses are local-only and excluded from the selected slice.

I read the complete three source files, not snippets. PR1210 supplies the actual rank-ten degree-minus-sixty-four subbundle, negative top bound, generic derivative rank two, coherent quotient sequence and saturated target. PR1209 supplies the everywhere-saturated actual third-jet identification, the quotient `J^-/F=O(4)`, and the retained fifteen-dimensional coefficient system with its four-dimensional coefficient kernel. Duality and self-duality identify the coefficient-section cokernel with the same representation P. ACTUAL supplies the physical representation conventions and the valid equivariant splitting argument. Its rank-seventeen classification or plateau bounds are not transferred to F. Transitive actual-geometric hypotheses are explicitly retained as assumptions, not silently reproved or discarded.

## Whole-proof audit

### 1. Actual objects and coherent-versus-saturated distinction

The proof consistently distinguishes `I=im beta_F` from its saturation `E`. I is torsion-free and hence locally free on the smooth line, but its inclusion in E is not assumed to be a subbundle. The exact quotient `F/F^-=I` is the correct object to use in the capacity argument. The two defects remain separate: the original t is zero, while delta measures the new torsion quotient E/I.

### 2. Two-column coherent backward capacity

The recursive kernels are saturated: the quotient by a kernel of a bundle map is torsion-free on the smooth curve. Since F is saturated in the constant ambient, every successive kernel remains saturated there. Every nonzero kernel has negative top degree because it is a subbundle of F. A derivative-zero saturated subbundle would define a constant Grassmannian map in characteristic zero and therefore have degree zero, so the flag must terminate by strict rank decrease.

For i at least one, the defining previous kernel condition places derivatives of Q_i in Q_(i-1). The second fundamental form therefore factors into the genuine normal subbundle `(Q_(i-1)/Q_i)(-2)`. Its kernel is exactly Q_(i+1), giving the coherent injection `R_i -> R_(i-1)(-2)`. This uses only differentiation of actual subbundles in the fixed constant ambient. There is no connection on R_i or I, and no replacement of a coherent image by its saturation.

The positive ranks consequently consist of k initial rank-two quotients followed by 10-2k rank-one quotients, with 1<=k<=5. Composing the coherent injections into `I(-2i)` preserves their possible zeros. The rank-two determinant bounds and rank-one top-degree bounds are valid without saturation. Their sum is exactly

    deg F <= (10-k)a+kb-(90-20k+2k^2).

The endpoint k=5 has no rank-one quotients, as the stated empty-sum convention requires. This is a structural flag argument, not a scan of bundle splittings.

### 3. High defect forces the actual full top line

For delta>=24, the substitution `a+b<=-12` and `a<=2` is valid because 10-2k is nonnegative. It gives the correct bound `deg F<=-68-2(k-1)^2<-64`, so a>2.

The degrees are then unequal, making the top line canonical and G-invariant. Its physical linearization is unique because G has no scalar characters. The component to O(2) vanishes by degree; the nonzero component to O(10) is invariant of degree 10-a in the interval from zero through seven. The invariant-divisor minimum forces degree zero. Thus a=10 and the actual top-line map is an everywhere isomorphism onto the canonical top subbundle of E. The conclusion `E_{>=10} subset I` is therefore established as an inclusion of coherent sheaves, not merely inferred from an abstract splitting type. Equivariant splitting of I is legitimate and is not claimed horizontal.

### 4. Quotient slope bound and forced endpoint

Since all ten ordinary degrees of F are at most -4 and sum to -64, each is at least -28. Projection of the actual quotient F->I to its lower split line is surjective; even its nonvanishing alone suffices to conclude `2-delta>=min F>=-28`. This proves delta<=30 for the high-defect case, while the remaining case already has delta<24.

At delta=30, a map to O(-28) forces a degree-minus-twenty-eight summand. The other nine degrees must all equal -4. The equivariant splitting `R9(-4)+O(-28)` follows from the retained finite-group splitting argument; the scalar multiplicity has no nontrivial character. No other candidate splitting is tested.

### 5. Partial/complete third-jet comparison and endpoint exclusion

The actual coefficient system is not replaced with the complete system. They share the same principal-parts target, and their evaluation maps commute with the actual constant inclusion of section spaces. The actual evaluation is everywhere surjective because its dual is the retained saturated third-jet inclusion. Accordingly the kernel comparison gives the everywhere-exact bundle sequence

    0 -> J^- -> Sym14 W(-4) -> P O -> 0.

Generic surjectivity alone would not suffice here; the proof uses the stronger correct hypothesis. The universal complete kernel is the fourth-power vanishing-line kernel, with rank fifteen and degree -60. The actual kernel has rank eleven and remains distinct.

Twisting this comparison and `0->F->J^-->O(4)->0` by four gives `chi_G(F(4))=-P-2D`. The calculation uses Euler-characteristic additivity and H1 vanishing for the nonnegative line twists in the comparison, not an unwarranted H1 vanishing for F(4). The forced endpoint instead has H0 equal to R9 and H1 equal to `Sym22 W`. The four fixed character identities then force `R9=2A+V`.

The actual injection `F(4)->Sym14 W O` induces an injection on H0. Since Sym14 W contains only one A, a source containing two copies of A cannot inject. This is a valid semisimple-representation contradiction excluding delta=30. The numerical dimensions and the Serre-duality exponent 22 agree throughout.

### 6. Orbit arithmetic and uniqueness of the length-twelve orbit

Every point stabilizer in the faithful projective A5 action is cyclic: its derivative character is injective for a finite group in characteristic zero. The available stabilizer orders are 1,2,3,5, giving orbit lengths 60,30,20,12. The effective determinant divisor is invariant, so its degree is a nonnegative sum of these lengths with orbitwise constant integral multiplicities. Combining delta<=30 with the exclusion of 30 leaves exactly the stated necessary set.

A5 has six order-five subgroups, each with two fixed points. Distinct such subgroups cannot share a fixed point because a point stabilizer is cyclic and cannot contain two distinct order-five subgroups. Each of the resulting twelve points has stabilizer order five. Therefore these points form the unique length-twelve orbit D12. Degree twenty-four necessarily gives the divisor 2D12. No actual point is selected or evaluated in this counting argument.

### 7. Conditional cyclic local defect

At delta=24, the actual inclusion of the full top line permits quotienting both I and E by that same line. The resulting rank-one subsheaf of O(2) is `O(2)(-D_delta)`, because its degree is -22 and its divisor is the determinant divisor of I in E. The preceding orbit result identifies D_delta with 2D12.

Consequently `E/I=O(2)/O(2)(-2D12)`. Locally, the included complete top line contributes a unit elementary divisor, while the determinant has order two. The elementary-divisor orders are therefore (0,2), not (1,1). This is a universal discrete-valuation-ring consequence of the actual sheaf inclusion, not a computation of a selected actual matrix. The torsion vanishes off D12.

### 8. Stopping boundary

The proof correctly states necessity rather than realization. It retains the existing actual third-jet information and proves a coherent derivative-image constraint using a finite backward flag. It supplies neither fourth-jet separation nor a new higher-order integrability or algebraicity theorem. Neither retained F18 splitting alternative nor either dual-extension class is excluded. Nothing depends on PR1211's middle-type classification.

## Code inspection and selected-only replay

I inspected `verify.py`, `characters.py`, and `REPRODUCE.md` before execution. The code performs exact fixed physical-W representation recurrences, a polynomial identity in an indeterminate k, elementary degree/orbit arithmetic, and exact input/proof hash checks. Its checks use explicit exceptions, so optimization does not remove them. The unused helper functions do not launch extra computations. No actual coefficient system, point, parameter, jet, tensor, matrix, instance-rank calculation, historical enumerator, or broad candidate search is executed.

Exactly the five top-level selected files and the three complete input files were copied into an otherwise empty isolated directory. Normal Python and optimized Python both exited zero and reported PASS with 52 explicit verifier checks. Bytecode writing was disabled; the directory still contained exactly those eight files afterward, with every byte unchanged. `REVIEWER-REPLAY.json` contains the selected manifest, exact commands, outputs, environment and results.

The replay corroborates only the bounded arithmetic and provenance checks. The preceding independent mathematical assessment supplies the whole-proof review. No GitHub writes, local Codex work, selected actual-instance evaluations, or large computations were performed, and `PROOF.md` was not edited.
