# Independent audit of the degree-fifty proof and sharp genus addendum

Author: AUDIT

## Verdict

The argument in PROOF.md is valid under its stated representation-theoretic and genus-obstruction dependencies. The argument in ADDENDUM.md is valid for the explicitly stated affine group F₅²⋊SL₂(F₅). It establishes the sharp abstract minimum genus 326, not the existence of a degree-50 projective curve. No mathematical defect was found in the core arguments.

This review independently checked the displayed algebra and deductions in both files, read the imported binary-group genus-through-thirteen proof, and checked the relevant degree-divisibility and nondegeneracy passages in the named dependencies. It does not independently re-establish the rank-four geometric hypotheses or their entire upstream dependency chain.

## 1. Component and integrality arguments

- A component orbit under A has size 1, 5, or 25. Since all component degrees are at least three, size 25 contributes at least 75. Size five has an order-five stabilizer, and the six conjugate axes force six disjoint A-orbits, contributing at least 90. These exclusions use only the stated absence of lines and conics.
- The surviving A-stable components are nondegenerate and have degree divisible by five. The projective-eigenspace argument correctly proves faithfulness on the normalization, including for singular integral curves.
- Castelnuovo gives genus at most nine for degree at most ten in P⁴. The equation g=25q−24+10t gives exactly (g,q,t)=(1,1,0) and (6,0,3) in that range. In particular, dropping the genus-six case would be an actual gap; the current proof repairs it correctly.
- For genus one, the translations form a normal subgroup of the elliptic automorphism group; conjugation on the translation subgroup A factors through the origin-fixing group of order at most six. The prescribed faithful action of K/A on A therefore bounds |K/A| by six. This does not incorrectly bound the entire elliptic automorphism group.
- For genus six, the deck-field argument gives a faithful K/A-action on the rational A-quotient. Its three branch points form an invariant set, and pointwise fixation of three points forces the identity. Hence |K/A|≤6 in this case as well.
- Consequently every such small component has at least twenty N-translates, contributing at least 100. Perfectness of G rules out component orbits of sizes two through four. Any larger nontrivial component orbit at total degree 50 has component degree five or ten and has just been excluded. Thus all components are N-stable. The imported exclusion through degree 45 then forces a single degree-50 component.

## 2. Normalization genus and étaleness

The degree-50 Castelnuovo bound is 376: 49=3·16+1 and 3·16·15/2+16=376. Thus the A-quotient genus is at most sixteen. Its G-action is faithful because the automorphisms of C(X) fixing C(X)^A are exactly A. The imported genus obstruction therefore leaves 14, 15, or 16.

For genus sixteen, Riemann–Hurwitz gives value 1/4. A positive-genus quotient cannot occur: quotient genus one gives zero or at least 1/2, and larger genus gives at least two. For a rational quotient, three or four branch points are necessary. The exact allowed element orders 2,3,4,5,6,10 give precisely the unordered signatures (3,4,6), (4,4,4), and (2,2,2,4). The elementary reciprocal enumeration in the proof is complete.

All three candidate signatures are correctly excluded. The unique involution disposes of (2,2,2,4). Projection to A₅ turns (3,4,6) into a generating (3,2,3) triple; two three-cycles whose product is an involution cannot generate A₅, by their supports. Projection turns (4,4,4) into three involutions with product one, which generate at most a Klein four group.

At quotient genera 14 and 15, the formula g(X)=25g(Y)−24+10n bounds the number n of A-branch points by five and two respectively. The branch set is G-invariant. Cyclic stabilizers in the faithful G-action have order at most ten, so every orbit contains at least twelve points. Thus n=0. The genera are exactly 326 and 351. This argument proves étaleness of the normalized cover and does not assert smoothness of the embedded support.

## 3. Sharp abstract construction

The matrices R and S in ADDENDUM.md have exact orders three and four; RS=[[1,0],[1,1]] has exact order five. Lower unipotents and their S-conjugates give all elementary matrices, hence generate SL₂(F₅). The displayed diagonal-factorization identity has the correct signs.

For every nonzero v∈F₅², x=(0,R), y=(v,S), and w=(xy)⁻¹ have exact orders 3,4,5 and product one. The identities I+S+S²+S³=0 and Σ₀⁴(I+J)^i=5I+10J=0 justify the affine orders, while the projections rule out smaller orders.

Writing H=⟨x,y⟩, its surjection to G makes H∩A an invariant F₅-subspace. Irreducibility gives either A or zero. In the zero case the cocycle c satisfies 2c(g)=(I−g)c(−I), so it is a coboundary. The value c(R)=0 and det(I−R)=3 force its defining vector to vanish, contradicting c(S)=v≠0. Hence H=N. No enumeration is needed.

The generating product-one triple legitimately defines a connected regular cover of the three-punctured sphere. Riemann existence and compactification give a smooth projective complex curve with faithful N-action and exactly the required inertia. Riemann–Hurwitz gives 2g−2=3000·13/60=650, hence genus 326.

Every inertia group intersects A trivially, including the order-five inertia, whose projection still has order five. Normality of A extends this conclusion to all conjugate inertia groups. Thus A acts freely and the quotient has genus fourteen. Conversely the imported lower bound g(X/A)≥14 implies g(X)≥326 for every faithful N-action. The abstract minimum is therefore exactly 326.

## 4. Identification of the affine group with the normalizer

The final addendum explicitly identifies its affine group with the projective normalizer and includes the following valid central-involution splitting argument. I checked this revision after the initial review.

In any extension 1→A→N→G→1 with the prescribed action, choose a lift t of the central involution −I∈G. Conjugation by t inverts A. Since t²∈A is fixed by t, it equals its own inverse and is therefore the identity. All lifts of −I are conjugate by A, because btb⁻¹=(2b)t in additive notation. For any n∈N, the conjugate ntn⁻¹ is such a lift; multiplying n by a suitable element of A produces an element centralizing t with the same image in G. Consequently C_N(t) surjects onto G and intersects A trivially. It is a complement, proving N≅A⋊G with precisely the standard action used in the construction.

This supplies the identification from the already stated hypotheses; no additional splitting theorem or assumption is necessary. The initial request to make this link explicit has been resolved in the reviewed final text.

## 5. Scope and verification limits

The addendum sharpens an abstract group-action statement only. It does not construct a Schrödinger-compatible line bundle of degree 50, an embedding in P⁴, or a curve satisfying rank-four equations. The surviving genus-351 case is neither constructed nor excluded. An abstract genus-326 example cannot by itself settle projective realization.

Only mathematical proof files and their stated relevant dependencies were inspected. No actual source tensor, source coefficient, selected source input, or problem-specific operation matrix was evaluated. The displayed two-by-two matrices are abstract finite-group data.
