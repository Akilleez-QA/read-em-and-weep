# Supporting regularity theorem

This existing result is included as a prerequisite for the selected pole, detector and socle manuscripts. The older intermediate bounds are preserved as history; SHARPEST-BOUND.md records the stronger proved bounds under its precise hypotheses. No source membership is inferred.

# Degree-60 common collision support after the sharper regularity bound

Import the geometry, finite flat-base argument, and coordinate dimensions from ../finite-collision-detection/DOWNSTAIRS-DETECTORS.md. The strengthened regularity in PROOF.md gives

    H²(B₀(r−5)K_n)=0 for n≥r+7, r=0,1,2.

Thus the individual downstairs neighborhoods N₇,N₈,N₉ suffice for the constant, first-weight, second-weight coordinates respectively. A common choice is T=N₉=V(K₉), and all three restrictions

    H²(Y,B₀(r−5)) → H²(T,B₀(r−5)|T), r=0,1,2,

are injective by the exact restriction sequence. Their source dimensions remain 2,10,20 under the imported coordinate calculation. No target dimension or surjectivity of these restrictions is asserted.

## Explicit structure

Writing u=t₂ and v=t₃, with respective degrees two and three,

    K₉=(u⁵,u³v,u²v²,v³).

The generator degrees are (10,9,10,9); adjacent least-common-multiple degrees are (13,12,13). Hence

    0→O(−13)²⊕O(−12)→O(−10)²⊕O(−9)²→O→O_T→0.

The finite weight filtration has associated graded pieces O_N(−2a−3b) for 2a+3b<9. There are five monomials with b=0, three with b=1, and two with b=2. Thus the generic transverse length is 10 and

    degree(T)=10 degree(N)=60.

This is a surface thickening, not a set of sixty points. The filtration is not a canonical splitting. The imported flatness argument makes T Cohen–Macaulay of dimension two without a smoothness or Gorenstein assumption.

Dualizing the resolution by O(−5) yields the dualizing-module presentation

    0→O(−5)→O(5)²⊕O(4)²→O(8)²⊕O(7)→ω_T→0.

The induced maps on dual detector spaces are surjective:

    H⁰(T,B₀(5−r)|T⊗ω_T) ↠ H²(Y,B₀(−r)), r=0,1,2.

This follows from dualizing the injective obstruction restrictions, using trace self-duality and Serre duality. These are complete families of dual tests, not preferred bases or evaluated detector values.

## Upstairs/downstairs distinction

The common unweighted upstairs source order is I¹⁰, with the regular transport hypotheses in prerequisite full-target-collision-criterion, document PROOF.md. (see the unit INPUTS.md) Multiplication by σ and τ supplies ideal orders I¹¹ and I¹². The natural quotient maps from the corresponding upstairs order-ten neighborhood lead to downstairs coefficients modulo K₇,K₈,K₉ for r=0,1,2 respectively.

The common N₉ restriction theorem instead applies to the already-defined global coordinate classes. It does not silently promote the first two natural chain quotients from K₇ or K₈ to K₉. Restricting from N₉ to N₇ or N₈ reconciles the coordinate restrictions with those natural quotient targets.

All source/transport assumptions of the imported statements remain in force. No physical source, selected matrix, actual detector value or rank instance is evaluated.
