# Historical scope-limited review receipt

This review concerns the original source, possibly a larger scope than the excerpt in this unit. It is not a review of normalized publication bytes.

# Independent audit of inversion eigenspaces

## Verdict

**PASS, with the imported hypotheses kept explicit.** The representation-theoretic proof correctly gives

- full-deck Ext² inversion dimensions `(176,176)`;
- `[22]` multiplicity-space dimensions `(12,18)`;
- retained D8-epsilon sign-kernel dimensions `(12,18)`;
- the two-dimensional S4-sign block entirely negative;
- whole D8-epsilon dimensions `(12,20)`.

No mathematical correction is required in the inspected proof. The conditional complete-source conclusion in §7 is valid. It leaves a twelve-dimensional possible target and supplies no obstruction value or vanishing verdict.

## 1. Global action, chain blocks, and Hom traces

The referenced projective-lift proof constructs the lift as `(a,r)` on the fiber product with `P(H)`, with `r²=1`. Its square is simultaneous deck inversion, so its induced End/cohomology action is involutive on both the invariant and full-deck sectors. The lift commutes with the geometric S4 action: permutations act on the X factor and trivially on the projective H factor. Tensoring E by the scalar line Q has no residual End character.

For reversal `π(i)=4−i`, the full-chain theorem has affine multiplier `−1`, hence the four coefficient blocks really are `P_π`, `M_π`, `−I₂⊗P_π`, `−I₂`. In particular the third block has dimension ten. There is one fixed index of π, and M consists of three unsigned copies of P. The coefficient traces are therefore `(1,3,−2,−2)`, and every block squares to one. The natural binary-quartic coefficient map identifies the pullback of O(1) with L for the displayed reversal lifts, so no unrecorded line scalar must be added to the coefficient blocks.

The degree-r Hom traces use the inverse action on the source coefficient space. Since all these blocks are involutions, their traces multiply exactly as written. The traces for `r=0,1,2,3` are `18,1,−8,−2`, with equal traces in negative degrees. The internal-complex alternating signs in equation (1) are all correct.

## 2. Negative twists: determinant and Koszul signs

With the specified action on H⁰(O(1)), the equivariant canonical bundle of one P¹ is O(−2) tensored by the determinant character. Thus H¹(O(−2)) has inversion eigenvalue −1. For O(−3), Serre duality gives the dual of the ordinary two-dimensional section representation, together with that same determinant factor. Its inversion action is consequently equivalent to `−J`.

The four determinant factors contribute `(-1)^4=+1` to simultaneous inversion. A geometric permutation of four H¹ factors contributes its Koszul sign. More explicitly, on each cycle the trace from `−J` gains `(-1)^length`, whose product over all cycles is again +1; the remaining tensor-permutation trace is w(s). Therefore H⁴(L⁻²) and H⁴(L⁻³) have joint traces `sgn(s)` and `sgn(s)w(s)`, respectively. L⁻¹ is acyclic. This independently checks both signs in the two negative-twist terms of equation (1).

Only ordinary cohomological trace identities are involved. No fixed-point or localization formula is needed.

## 3. KS79 equivariance and the invariant trace

The supplied full coefficient-family theorem gives injectivity from the 79-dimensional projective tangent. The family is pulled back from Y, so its KS image is in the deck-invariant T¹. The independent classical-cohomology row `(1,79,352,0,0)` makes this injective map an isomorphism onto T¹.

Equivariance is justified on Y itself, avoiding a false assumption that N is inversion-invariant. Pullback by j sends a coefficient tuple s to j*s; the target reversal identifies the corresponding H pullbacks and returns the parameter to `R(j*s)`. The original coefficient tuple is fixed as an actual vector, because `j*v=Rv` and `R²=1`. The tangent is intrinsically `Hom(kv,W⊗k⁵/kv)`; the action on kv is trivial, so identifying it with the displayed quotient introduces no additional character. Thus the trace is `tr(js|W)tr(R)−1=w(s)−1`. The geometric factor permutations act trivially on the five target-coordinate labels and fix v.

Substitution into the Euler identity gives equation (2). The cycle-trace lists for W, Sym² of the two-dimensional factor, and Sym³ of that factor are correct. The resulting invariant T² joint trace row is exactly `(0,0,−24,0,4)`.

## 4. Equivariant Serre duality

The formal differential identity gives `a*(dx/y)=i dx/y`. On the fourfold canonical volume, simultaneous inversion therefore has eigenvalue +1, geometric S4 permutations have eigenvalue sgn, and deck action has the full-deck character. The trace pairing on End and equivariant Serre duality pair the invariant and full-deck degree-two sectors with precisely this sign twist. Inverses do not change the inversion eigenvalues or the S4 class characters here.

Accordingly `V≅(T²)*⊗sgn` for the joint inversion/S4 representation, and its trace row is `(0,0,−24,0,−4)`. The ordinary full-deck function eigensheaf does not acquire a second permutation sign. At the identity permutation this trace is zero, proving `(176,176)` from dimension 352.

## 5. Multiplicity extraction and D8 restriction

The independent classical dimensions and the equivariant finite-pushforward decomposition give `[22]` multiplicity `20+10=30` and sign multiplicity 2. For class sizes `(1,6,3,8,6)` and `[22]` character `(2,0,2,−1,0)`, orthogonality gives multiplicity-space inversion trace −6. This proves `(12,18)`. The sign extraction gives trace −2 on a two-dimensional block, so that block is wholly negative.

The D8 character specified in the proof is exactly `sgn|D8`. The induced character is `sgn⊕[22]`, because induction of the trivial D8 character is the permutation representation on the three pairings, namely `1⊕[22]`. Frobenius reciprocity therefore selects one epsilon line from each copy of `[22]`, not the two-dimensional whole representation. This is why the retained kernel has `(12,18)`, whereas the full `[22]` isotypic component has `(24,36)`.

The canonical central sign projector separates the sign component inside V_epsilon. Since inversion commutes with S4, it preserves both summands and acts only on the multiplicity factor of the `[22]` evaluation decomposition. The whole epsilon space consequently has `(12,20)`.

## 6. Source binding and the conditional twelve-dimensional consequence

The inspected source-binding addendum and its retained public excerpts identify the exact same geometric D8 action and character `(-,-,+)`. They explicitly require transport of complete admissible descent data, full-deck choice independence, and comparison with the complete corrected source. They do not replace that action by naive permutations of harmonic coordinates. The proof correctly retains these conditions and does not turn the noncanonical graded representatives Q and Q² into canonical isotypic or inversion eigenvectors.

The separately audited root-gerbe theorem establishes inversion invariance for the same actual class only under its named source identities and complete-descent premises. Combining that theorem with the retained-source identification gives membership in the +1 eigenspace of the retained target, of dimension twelve. The two projectors commute, so their order is immaterial. The identification of full-deck degree-two End and End₀ cohomology is also correct: H²(O_X) is supported on deck characters involving exactly two factors and has no full-deck component.

The dual negative eigenspace has dimension eighteen and annihilates an invariant retained class. This means eighteen independent linear combinations in any complete retained dual system; it does not identify eighteen individually named existing detector rows as zero. The existing row basis can mix eigencharacters, and no change-of-basis or source value is supplied.

The final paragraph of §7 correctly records a strengthening from the proved sign trace: once the same class is known both to belong to V_epsilon and to be inversion-invariant, its sign component is automatically zero, because that component is entirely inversion-negative. Thus the separately imported full-alternation boundary is not necessary for this particular twelve-dimensional reduction, although retaining it as an additional premise is conservative and valid. The final paragraph was statically reread after its addition.

## 7. Exact remaining qualifications

There is no outstanding internal sign, trace, dimension, or representation-theoretic gap. This audit does not independently reconstruct the classical HM theorem, re-authenticate source identities, or prove the actual-source membership premises. Those remain the explicit inputs stated by the proof and its referenced packets. Ordinary projective symmetry by itself still would not imply source-obstruction invariance; the separately supplied root-gerbe transport is essential for that application. No conclusion about zero versus nonzero obstruction follows from the twelve-dimensional target.

