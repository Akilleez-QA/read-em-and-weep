# Independent audit: conic-component classification

**Verdict: PASS, conditional on the expressly imported hypotheses and representation/rank inputs.**

This review independently checked `PROOF.md`, including the stabilizer calculations and both vector-bundle arguments, against `../rank-four-line-component-exclusion/PROOF.md` and `../rank-three-250-plane-exclusion/PROOF.md` with its addendum. The existing `AUDIT.md` identifies itself as a self-audit; this file is a separate review. No actual source tensor, selected source input, or source-map evaluation was used. 

## 1. Exhaustion of stabilizers and the free-A case

The possible conic stabilizers in A have order 1 or 5. Indeed stabilization of the conic implies stabilization of its three-dimensional span, while an A-invariant span would lift to a proper invariant subspace of the irreducible Heisenberg representation. This excludes order 25 without needing a faithful linear action of the quotient A itself.

When A_C is trivial, projection identifies N_C with a subgroup H of G and gives orbit size 25[G:H]. Since distinct conics in a locus of dimension at most one are distinct reduced curve components, each contributes degree two. The budget is therefore 50[G:H]≤125, forcing index at most two. Perfectness excludes index two. The central involution acts as -1 on A, so the cocycle identity 2c(h)=(1-h)c(z) conjugates this complement to G even though 5 divides |G|.

The only invariant three-space is T, since V=T⊕W consists of inequivalent irreducibles of dimensions three and two. A conic equation spans an invariant line in Sym²(T*); perfectness makes its character trivial. The decomposition Sym²T=1⊕P5 leaves exactly one equation up to scalar. Its invariant quadratic is nondegenerate: its radical would be a proper invariant subspace of irreducible T. Thus the resulting conic is genuinely smooth, and every free-A conic satisfying the degree budget belongs to this canonical orbit.

## 2. Axis-stable orbit bound: at least 300

For a fixed order-five axis, its five distinct eigenspaces force the span to be a coordinate triple. There are exactly ten triples. Each has a unique arithmetic-progression center: two possible centers a,b in the same triple would imply 3(a-b)=0 in F5. This proves uniqueness; the ten choices of center and unordered nonzero step then exhaust the triples.

For three distinct weights, the only possible repeated quadratic weight is a square at the center paired with the product of the two other coordinates. Quadratic monomials sharing a variable cannot collide in weight, and there cannot be two different centers. A nondegenerate eigenquadratic consequently has exactly the form x_c²+λx_(c-d)x_(c+d), with both coefficients nonzero. This verifies that no smooth eigenconic type was omitted.

The affine transformations of the indices supplied by translations and the diagonal torus are transitive on the ten triples. G is transitive on the six axes. A plane cannot be invariant under two axes: their Heisenberg lifts generate the irreducibly acting Heisenberg group. Hence these produce exactly 60 distinct span planes.

The quadratic-phase element D is a normalizer element preserving each such coordinate plane. Its two monomial phases differ by ±2d² modulo five. This number is nonzero, so its action multiplies λ by a primitive fifth root. Its first five translates are distinct and have the same span. Transporting this fact to each of the 60 planes gives at least 300 distinct orbit conics, of total degree at least 600. Only a lower bound is claimed; extra conics over a plane cannot weaken it. This excludes the axis-stable case under degree 125.

## 3. Exact canonical count and the degree-75 remainder

The canonical conic is G-stable. Its A-stabilizer is therefore a G-invariant subgroup of A. Irreducibility of the standard G-action on F5² leaves only zero or all of A, and the latter is excluded by its proper span. The A-orbit has exactly 25 members; G-stability then shows it is already the full N-orbit.

Every conic component must lie in that same orbit by the preceding classification. If one occurs, equivariance forces all 25 to occur. Their reduced total degree is 50. Removing those components leaves degree at most 125-50=75. The imported no-line theorem and the exclusion of every other conic leave only components of degree at least three. This is a statement about the reduced curve part, with no assertion about nonreduced structures or isolated points.

## 4. Containment in Z4 and parity ranks 5/3

The plane addendum explicitly proves even rank at least five and odd rank at least three at every point of the invariant conic, including isotropic points. With the imported residual-rank normalization rank b=2 rank Q, containment in Z4 supplies total rank at most eight. Since the parity images are complementary, both lower bounds must be equalities everywhere: even rank five and odd rank three.

This step is conditional on the earlier parity/rank theorems and their hypotheses; the present audit does not certify an actual source operation satisfies them.

## 5. Elimination of the pure-T T constituent

If both pure-T constituents survive, their inequivalence makes the combined coefficient map injective on T⊕P5. For nonzero u, the cross-product operator C_u has rank two even when q(u)=0. The universal fixed-u map is represented, up to invertible conventions, by S↦SC_u. A symmetric S annihilating im C_u=u-perp has image in Cu, and hence is a scalar multiple of uu^t. Conversely uu^tC_u=0. Its kernel is exactly that line, including on the conic.

On C≅P1 the tautological line of P(T) is O(-2). The kernel line in O(-2)⊗Sym²T has the additional quadratic dependence u², so it is O(-6). The resulting pure-T image bundle has rank five. Equality with the full even image follows from fiberwise containment and equal constant rank, so the mixed map factors through this image bundle I.

After twisting its resolution by O(2), the cohomology sequence is

    0 → Sym²T → H⁰(I(2)) → H¹(O(-4)) → 0.

Finite-group representations over C split. For the binary representation U0 parametrizing this particular conic, Sym²U0≅T and det U0=1, so equivariant Serre duality gives H¹(O(-4))≅T. In particular this is T, not the inequivalent T'=Sym²W. Thus H⁰(I(2))≅1⊕P5⊕T contains no T'. The equivariant mixed map must vanish. Since the conic spans T, its linear coefficient map vanishes identically, contradicting repeated-input injectivity via cyclic zero. The T constituent is therefore killed.

## 6. Containment of all mixed coefficients in the specific H

After that elimination, the pure-T image has constant rank four in its particular surviving P5 image H. Full even rank five implies that the projection of the mixed family to J_even/H has rank at most one along the conic.

If nonzero, saturating its generic image gives an equivariant line subbundle L=O(-d) of the trivial quotient-target bundle. The inclusion forces d≥0, while a nonzero map O(-2)⊗T'→L forces d≤2. Its fiber lines therefore span at most h⁰(O(d))≤3 dimensions of the fixed quotient target. Saturation handles rank-drop points; constant projected rank was not assumed.

Because C spans T and the mixed map is linear in u, this span is the full coefficient image in the quotient. It is thus a nonzero G-quotient of T'⊗T=P4⊕P5, whose smallest possible nonzero dimension is four. The contradiction forces the projection to vanish. Accordingly all mixed coefficients lie in this same H, not merely in some sum of five-dimensional isotypic components. Even rank five then makes the even image equal to the fixed H at every point of C.

## Conclusion and limits

All five requested checkpoints pass. No corrective change to `PROOF.md` is required. The conclusion is a conditional classification and necessary coefficient restriction: it does not exclude the canonical 25-conic orbit, establish its actual occurrence, exclude higher-degree components, or prove that Γ4 is empty. Imported degree, no-line, representation, and parity-rank results retain their own verification requirements.
