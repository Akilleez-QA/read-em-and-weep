# Negative quadratic ranks sharpen the remaining Smith bounds

**23 October 2026 · PR1103, full immutable proof read**

[Immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/0c2da01cfa9440d25b38360a5742ee8b32f20d0f/research/hm/source2-negative-quadratic-degree-bound/PROOF.md), blob `d19ae749f54ec46eb667ffd70bc54868b595a227`.

## Actual rank bounds and determinant degrees

For the original positive 41→37 pencil Q+tT_a, every nonzero negative quadratic has rank T_a≤30; every square has rank T_a≤27. Thus each maximal 37-minor has polynomial degree at most thirty, or twenty-seven on the entire square conic. These are bounds, not asserted sharp instance ranks.

The genuine negative-module split has source dimensions 9+32 and target dimensions 16+21, with original arrows and variables retained. T_a respects this split, so rank≤9+21=30. No claim that Q preserves it is used.

On squares, complete polarization gives separated rank eight and N8 quotient rank ten. The actual residual image can add at most dim NC4=9, so full rank≤8+10+9=27, without splitting the residual extension. The square kernels are respectively Cℓ⁸ and ℓ⁴Sym⁴W. For comparison the nonsquare quotient-block ranks are nine and twelve; these are universal maps, not actual residual-coupling evaluations.

Multilinearity of determinants makes every coefficient using more than rank T columns vanish, even when Q mixes the blocks. This proves the polynomial-degree bounds directly for original minors.

## Current last-pivot ranges

Where the second symbol has rank three, the original first and third vanishings leave 33 unit pivots, three t² pivots and a final pivot t^e or no pivot. If finite, its maximal-minor valuation is 6+e, hence e≤24; on squares, e≤21.

For residual-large with α=0, the current ranges are therefore **5≤e≤24 generically** and **5≤e≤21 on every square**, or an absent pivot. The old 5–31 range was a valid earlier bound and is now sharpened. These ranges do not assert that every exponent occurs or that a pivot exists.

For residual α≠0, the exponent remains four away from the known exceptional support. At the twelve conic exceptional points, fourth vanishing instead gives 5≤e≤21 or absence. Every square has second rank three: the six second-rank-drop C5 axes are semisimple, off the conic. No last-pivot formula is supplied at those six rank drops.

No coefficient, pivot, mechanism or source occurrence is selected. The argument supplies a degree bound, not a fifth-symbol calculation or full-adjoint conclusion.
