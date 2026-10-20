# Independent audit: retained filtration and weighted duality trace

> Historical qualification: the filtration and its first quotient remain valid. Statements below denying an unconditional canonical twenty-dimensional projection apply only to the bare filtered bundle, not its additional cubic algebra structure. The later [canonical cubic splitting](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6277692474) resolves that overbroad conclusion; it supplies no vanishing of the thirty conditions.

## Verdict

The mathematical reduction is correct at the admitted source/cohomology scope. It canonically organizes the thirty retained conditions into a ten-dimensional first quotient test and a twenty-dimensional kernel test available only after the first vanishes. It does not prove either test vanishes. The discriminant-weighted canonical finite trace correctly realizes the first test, including on the branch locus.

Audited FILTRATION-RESULT.md together with null-pair-quotient-bracket/pair-quotient-0512/RESULT.md, null-mixed-duality-reversal/DUALITY-RESULT.md, null-canonical-alternating-transfer/RESULT.md, null-mixed-module-equation/RESULT.md, null-module-boundary-audits/semiregularity-sector/RESULT.md, and null-corrected-pure-lift/corrected-relative-lift/RESULT.md by static reading. The upstream geometric and HM twist-rank premises remain imported. 

## 1. Canonical line and exact cohomology

For G of isomorphism type O(-1)⊕O(-2), W=H⁰(G(1)) is intrinsically a line. Evaluation W⊗O(-1)→G has constant rank one: in any auxiliary splitting it is the nonzero constant section of the O summand of G(1). Consequently its image L is a canonical subbundle and Q=G/L is a line bundle of type O(-2). This remains true when the corresponding function vanishes at all reduced points of a nonreduced fiber; reduced point-values are not a test for the rank of this bundle map.

The extension splits abstractly, already seen through that auxiliary splitting, or through Ext¹(Q,L)=H¹(O(1)) tensored with a constant line. No chosen splitting is needed to define L or Q. Splittings are generally nonunique, with differences in Hom(Q,L).

After tensoring by B₀, all connecting maps vanish because a splitting exists. Thus the H² sequence is short exact without any assumption about H¹ or H³ of twisted B₀. The dual sequence has order

    0 → H²(B₀⊗Q*⊗ω_Y) → H²(B₀⊗G*⊗ω_Y)
      → H²(B₀⊗L*⊗ω_Y) → 0.

Trace self-duality of B₀ and Serre duality identify this as the dual of the detector sequence. Its kernel has dimension twenty, and its quotient has dimension ten. The imported ranks suffice; there is no new rank computation.

## 2. Staged class and cochain independence

The first class is restriction to L, hence a quotient of the obstruction space, dual to the canonical ten-dimensional detector subspace. If it vanishes, injectivity of the kernel inclusion gives a unique twenty-dimensional preimage. Pairing that preimage against a quotient detector by any lift is independent of the lift precisely because the first ten pairings vanish.

For cocycle c and a primitive p of its restricted cocycle, choose a cochain lift p̃. The difference c−δp̃ is kernel-valued and closed. Changing p̃ while holding p fixed changes that kernel cocycle by a kernel coboundary. Changing p by a degree-one quotient cocycle changes the kernel class by its connecting homomorphism, which is zero by abstract splitting. Changing c within its cohomology class preserves the same unique preimage. This justifies the construction without pretending p is canonical or assuming H¹ vanishes.

## 3. Discriminant generator, twist, and normalization

On the standard binary-form realization, symmetric bilinear sections form Sym²(Sym²V*), whose decomposition into Sym⁴V* and the determinant-square line is the usual discriminant-polarization decomposition. The algebra trace to H⁰(O_Y(1)) is SL(V)-equivariant. It kills the invariant discriminant line because Sym⁴V* has no SL(V)-invariants. The discriminant polarization is nonzero and symmetric, so it spans W. This is an exact geometric construction of the evaluation line, not an assumed named summand of a Horrocks basis.

With Δ(ax²+bxy+cy²)=b²−4ac, half-polarization gives σ(q,r)=bb′−2(ac′+a′c). Full polarization differs by two. Either convention gives the same vanishing test, but its numerical representative must use the stated convention. Constant determinant lines remain present until fixed binary-volume conventions or a nonzero generator are chosen. Intrinsically the first target is H²(B₀⊗L*⊗ω_Y), not a scalar-normalized H²(B₀(-4)) until σ is chosen.

The coefficient twist is exact:

    σ·C_X ∈ H²(X,m*B₀⊗ω_X⊗m*O_Y(1)),
    Tr_m^ω(σ·C_X) ∈ H²(Y,B₀⊗ω_Y(1)) = H²(Y,B₀(-4)),

with constant canonical/determinant lines understood. If λ∈Hom(m_*O_X,ω_Y), then Tr_m^ω(sλ)=λ(s). This is the duality trace, so there is no factor 1/6. The separate algebra-trace projector onto constants has the factor 1/6; confusing the two would change the formula. The weighted map kills the constant-dual component since Tr(σ)=0, and kills the odd component by parity. Finite duality makes the construction global across ramification.

## 4. Source normalization and failed shortcuts

The raw normalized defect g_ik⁻¹R_ijk need not itself be tracefree. Its trace is a scalar coboundary, so one must use tf(g_ik⁻¹R_ijk), equivalently the scalar-normalized representative already supplied by null-mixed-module-equation. This precision correction is now applied and verified in FILTRATION-RESULT.md; it changes no class or conclusion.

The known unweighted alternating primitive cannot simply be multiplied by σ to produce the weighted trace primitive. Indeed σ is not pulled back from the base: if σ=m*a, trace-zero would force 6a=0. It therefore cannot be moved through full permutation averaging as a base coefficient. This diagnoses the proposed deduction, without claiming that the desired weighted class is nonzero.

The inspected pure relative Atiyah-square result establishes pure lifting only. It supplies no identity identifying the complete mixed source, which includes pure-lift cross terms and ambient/overlap/unit interactions, with the discriminant-weighted scalar Atiyah expression. A principal-symbol calculation similarly does not calculate this finite-duality coefficient evaluation. The report correctly says a new chain-level identity or justified comparison is needed.

Existing symmetry constraints allow the entire retained target, and the first-quotient map is surjective. This proves those constraints alone cannot imply first-stage vanishing, without constructing a counterexample for the fixed actual source. Ordinary semiregularity's blindness to the enclosing retained isotype likewise adds no first-stage equation.

## Conclusion

Approved at the stated imported-premise scope. Both the explicit tracefree-representative and polarization-normalization precision corrections recorded above have been applied and verified in FILTRATION-RESULT.md. The useful new outcome is a canonical, geometrically explicit first test. All thirty retained values remain unevaluated and unproved zero.
