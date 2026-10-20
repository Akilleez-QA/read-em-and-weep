# Rank-four curve degree: empty or exactly one hundred

## Result

In the standard complex projective Schrödinger-normalizer setting, every nonempty N-invariant reduced curve in P4 whose integral components have degree at least5 has total degree at least100.

More precisely, if such a curve has degree less than125, its degree is divisible by50 and hence is at least100. Consequently, under the established rank-four hypotheses,

    Γ4 is empty, or deg Γ4=100.

The degree125 endpoint is excluded by the independently audited complement/plane-quintic argument cited in §5 below. This concerns the reduced curve support. It neither proves nonemptiness nor excludes degree100, and says nothing new about isolated points or scheme multiplicities.

## 1. Imported results

Write N=A⋊G, A=F5², G=SL2(F5), so |N|=3000.

1. ../smooth-normalizer-polarization-divisibility/PROOF.md and INDEPENDENT_AUDIT.md: every N-invariant integral curve has degree divisible by50. The proof works on its normalization, even when the embedded curve is singular. It supplies the canonical N-linearization of O(5), trivial fibre action for order-five inertia, and the N-element order list1,2,3,4,5,6,10.
2. ../rank-four-degree-sixty-lower-bound/PROOF.md: no N-invariant integral curve has degree≤55. Every A-stable integral curve spans P4 and has degree divisible by5.
3. ../rank-four-degree-fifty-equality/PROOF.md, §2: every A-stable integral curve of degree5 or10 has N-orbit size at least20.
4. ../rank-four-degree-three-four-exclusion/PROOF.md and its line/conic dependencies: every integral component of Γ4 has degree≥5. The rank-four reduced degree bound≤125 and N-invariance are established there and in its cited dependencies.

The remaining proof uses only these results and elementary finite-group and divisor arithmetic. The independent audit and direct disjoint-normalization argument are recorded in ../rank-four-degree-hundred-audit/AUDIT.md.

## 2. Direct total-degree divisibility on the disjoint normalization

This section gives the shortest proof and the stronger exclusion of total degrees105,110,115,120. The component-stabilizer argument below is independent corroboration of the lower bound100.

**Lemma.** If every component of an N-invariant reduced curve C spans P4, then50 divides deg C.

Let X be the disjoint union of the smooth normalizations of its components, with the induced N-action and equivariant line bundle M=ν*O_C(5). For every x∈X, the stabilizer N_x preserves the connected component X_i containing x. Its action on X_i is faithful: any element fixing X_i pointwise fixes the associated nondegenerate embedded component pointwise and is the identity in PGL5. Thus N_x is cyclic, with order in1,2,3,4,5,6,10.

There is an N-invariant rational section of M, nonzero on every component. To construct it, choose one component X_i from each N-orbit of components. Its stabilizer K_i acts faithfully on its function field, so Hilbert90 supplies a nonzero K_i-invariant rational section of M|X_i. Translate that section to all other components in the orbit. K_i-invariance makes the extension well-defined and N-invariant. Repeat for each component orbit.

At each point whose stabilizer has order divisible by5, the coefficient in the section's divisor is divisible by5, by the same order-five fibre-triviality argument as in the audited integral proof. Each N-orbit of points has size3000/r, irrespective of which components it meets. Its divisor contribution is therefore a multiple of250, by the integral proof's list

    3000,1500,1000,750,3000,500,1500

for r=1,2,3,4,5,6,10. Summing yields250|deg M=5 deg C, proving the lemma. Connectedness, irreducibility, and smoothness of the embedded curve are unnecessary.

Now suppose deg C<125 and every component has degree≥5. An A-orbit of25 components costs at least125. An A-orbit of five has six conjugate stabilizer axes and therefore belongs to an N-orbit with at least30 components, costing at least150. Hence all components are A-stable and span P4. The lemma gives50|deg C. For positive degree below125 the only possibilities are50 and100. The established exclusion of nonempty invariant reduced curves of total degree≤55 (which requires only absence of line/conic components) eliminates50. Therefore deg C=100. Under the rank-four upper bound125 the only residual degrees are100 and125.

## 3. Polarization divisibility for two component stabilizers

Let D be any A-stable integral curve, K=N_D, H=K/A≤G, and X its smooth normalization. The A-stability implies that D spans P4. Therefore K acts faithfully on X: an element fixing D pointwise has D contained in one eigenspace of a linear representative, and the full span makes that representative scalar.

The line bundle M=ν*O_D(5) is K-linearized by restriction of the canonical N-linearization. The already audited lift lemma shows that every order-five subgroup fixing a point of X acts trivially on its fibre. By Hilbert90, M admits a nonzero invariant rational section. Its divisor is K-invariant, and at a point whose cyclic stabilizer order r is divisible by5 its coefficient is divisible by5. Thus an orbit of inertia r contributes

    (|K|/r) m, with 5|m when 5|r,

to deg M=5 deg D. Negative coefficients are allowed. These statements apply to singular D via normalization without any smoothness hypothesis on D.

### 3.1 Component orbit size five

Here |H|=24 and |K|=600. The possible element orders of K are contained in

    1,2,3,4,5,6.

For completeness, an affine element is (a,s) with s∈H. If s−I is invertible, a translation conjugates (a,s) to (0,s), so its order equals the order of s. The orders of s belong1,2,3,4,6 by the G-order list and Lagrange's theorem for |H|=24. If s−I is singular, s is identity or unipotent, and (a,s)^5=1 by the calculation in the polarization proof. No order10 can arise from a quotient element of order2, since that element is −I and s−I is invertible. This proves the asserted list without any classification of H.

For inertia orders1,2,3,4,5,6 the orbit contributions are respectively multiples of

    600,300,200,150,600,100.

Their greatest common divisor is50. Hence50 divides deg M=5 deg D, and

    10 divides deg D.

### 3.2 Component orbit size six

Here |H|=20 and |K|=500. Intersecting the global element-order list with the divisors of500 gives the possibilities

    1,2,4,5,10.

For these inertia orders the orbit contributions are respectively multiples of

    500,250,125,500,250.

Their greatest common divisor is125. Thus125 divides deg M=5 deg D, and

    25 divides deg D.

Again no classification or splitting of K beyond its inclusion in N and containment of A is needed.

## 4. Corroborating componentwise proof below100

Suppose C is a nonempty N-invariant reduced curve of total degree d<100, all of whose integral components have degree≥5.

An A-component orbit has size1,5,or25. Size25 would cost at least125 degrees. If it has size five, its stabilizer is an axis (order-five subgroup) of A. The standard G-action is transitive on the six axes. Conjugating this orbit gives six disjoint A-orbits, because their stabilizer axes differ and A is abelian. The N-orbit therefore contains at least30 components and costs at least150 degrees. Both cases contradict d<100. Every component is consequently A-stable and has degree divisible by five.

Let D be one component, e=deg D, and m=|N·D|. The action on components factors through G. If m=1, the global polarization theorem gives50|e. Since e<100, necessarily e=50, contrary to the integral exclusion through55.

Suppose m>1. Then m≥5: the permutation image of perfect G in S_m is perfect, whereas S_m is solvable for m≤4. If e=5 or10, the established orbit lower bound m≥20 gives me≥100, a contradiction.

Otherwise e≥15. The inequality me<100 with m≥5 and five-divisibility forces e=15 and m∈{5,6}. More explicitly, e≥20 would already give me≥100; with e=15 one has m≤6.

If m=5, §3.1 gives10|e, contradicting e=15. If m=6, §3.2 gives25|e, again a contradiction. All component possibilities have been exhausted. Thus such C cannot exist.

Applying this to Γ4 yields the stated lower bound100. The pre-existing upper bound125 and total-degree five-divisibility remain unchanged.

## 5. Exclusion of the degree125 endpoint

The endpoint argument is given in ../rank-four-degree-hundred-audit/ENDPOINT_125_EXCLUSION.md and independently verified in ENDPOINT_125_INDEPENDENT_AUDIT.md in that directory. Here is its complete reduction.

If all components are A-stable, they span P4 and §2 gives50|125, impossible. Otherwise the axis-stabilized orbit still costs at least150, so a free A-orbit of25 components must occur. The degree budget forces exactly25 quintic components, forming one N-orbit. Its stabilizer is a complement to A and is translation-conjugate to G: the central involution z=−I makes every complement cocycle c satisfy2c(h)=(1−h)c(z), hence c is a coboundary.

After conjugation the component's vector span is a G-subrepresentation of V=T⊕W, of dimensions3 and2. Span W would make the curve a line, impossible. In full span V, a quintic has normalization genus≤1, whereas perfect G cannot act faithfully on a genus-zero or genus-one curve: in genus zero its central involution forces its image into a solvable centralizer; in genus one its image lies in the abelian translation group. Faithfulness follows from full span.

In span T, the quintic's equation would span an invariant line in Sym5(T*), which must be trivial because G is perfect. But its A5 character on the classes1,2,3,5a,5b is(21,−3,0,1,1). Averaging with class sizes1,15,20,12,12 gives(21−45+12+12)/60=0. Hence no plane quintic exists. These cases exhaust the endpoint and exclude total125.

Combining with §2 yields Γ4 empty or of reduced total degree exactly100.

## 6. Verification scope

No actual source tensor, coefficient, selected input, operation matrix or value, rank instance, jet, or residue was evaluated.   The principal audit target is the disjoint-normalization extension in §2. The two subgroup order lists, two gcd computations, and component-orbit exhaustion give an independent route to the lower bound100.
