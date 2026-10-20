# Independent review: pair quotient and global/relative bridge

## Verdict

RESULT.md passes this audit. Its finite multiplication splitting, block eigen decomposition, canonical alternating projector, and global Leray sequence are correct under the stated actual-bundle, geometric-linearization, and imported HM cohomology-rank premises. No actual obstruction value follows from these structural identifications.

## 1. Finite flatness and splitting

Multiplication m:P²×P²→P⁴ is finite of degree six: a quartic has finitely many degree-two subdivisors, and a reduced quartic has six ordered choices. Projectivity turns quasi-finiteness into finiteness. Smooth equidimensional source and smooth target justify the stated Cohen–Macaulay/miracle-flatness argument, including the discriminant. Thus F=m_*O is locally free of rank six.

The Künneth argument for intermediate cohomology vanishing is complete: mixed H⁰/H² factors never occur for equal twists because their nonvanishing ranges are disjoint. The Hilbert numerator is 1+4t+t², giving F≅O⊕4O(-1)⊕O(-2). For block exchange, the degree-n trace is dim H⁰(P²,O(n)), so its generator-trace numerator is (1-t)². Hence

F⁺≅O⊕O(-1)⊕O(-2),   F⁻≅3O(-1).

The eigensheaves are canonical, while their individual line-bundle splittings need not be.

## 2. Canonical twists and block sign

The elliptic full-deck-sign line M on Y=(P¹)⁴ has the ordinary product linearization. Its both-inner-odd quotient is O(-3,-3). The block exchange simply exchanges two degree-zero sheaf factors, with positive sign. The canonical bundle ω_{P²×P²} has the same block action because swapping two dimension-two factors contributes (-1)^(2·2)=+1.

In contrast, ω_Y=M⊗sign as S₄-linearized lines: permutations of the four dimension-one cotangent factors contribute the permutation sign. Both statements are necessary and consistent. No additional sign should be inserted into finite pushforward cohomology. Constant determinant-line conventions do not introduce a twist from the other P² factor.

The scalar H²(ω_{P²×P²}) vanishes by Künneth, so replacing End by End₀ in this degree-two group is justified canonically.

## 3. Canonical projector despite no S₄ action on the intermediate quotient

This is the potentially subtle point, and the manuscript handles it correctly. The subgroup H=< (12),(34) > is not normal in S₄, so S₄ does not act on the intermediate quotient X=Y/H. No such action is needed.

Let Q=ρ_*O_Y for ρ:Y→P⁴, and let F=Q^H=m_*O_X. The full S₄ averaging idempotent preserves Q^H because its image is Q^{S₄}=O. On a generic fiber, its restriction to F averages over the six H-orbits, giving (unit∘tr_F)/6. Since these are morphisms of locally free sheaves and agree on the dense étale locus, they agree everywhere. Equivalently, this follows from the canonical group projector and finite-duality construction.

On the dual F*, the corresponding projector is explicitly

φ ↦ φ(1)·(tr_F/6).

This confirms both the normalization and the direction of the inclusion/retraction in RESULT.md: inclusion of ω_{P⁴} is dual to tr_F/6, while retraction is dual to the unit. The complement is canonically F₀*⊗ω_{P⁴}, where F₀=ker(tr_F).

After converting M-alternation to ω_Y-invariance using the sign twist, this is exactly the full S₄ alternating projector on the prescribed D₈-sign sector. It is not merely an unrelated projector of the same rank. The τ-even complement is canonically defined, even though expressing it using O(-4) and O(-3) summands requires a noncanonical splitting.

Using the supplied twist ranks (2,10,20), finite duality yields block-even dimension 32, block-odd dimension 30, and a canonical 2+30 decomposition inside the block-even space. The two dimension-30 spaces are distinct; equality of dimensions does not identify them.

## 4. Global Leray sequence

For K=m*End₀(HM)⊗ω_X and s:X→P², the proof s_*K=0 is valid: it is torsion-free over the integral base and vanishes on the dense stable open. T=R²s_*K is supported on the bad plane parameters, with fiber identification supplied by top-degree base change. This does not assert that T is an ordinary dual of s_*K.

Only q=1,2 remain in the Leray spectral sequence, and the base has cohomological dimension two. In total degree two, E₂^{1,1} has no possible incoming or outgoing differential. The only relevant differential from E₂^{0,2} is d₂ into E₂^{2,1}. Thus the exact sequence

0→H¹(R¹s_*K)→H²(X,K)→H⁰(T)→H²(R¹s_*K)

is correct, with the last arrow d₂. In particular the middle map need not surject onto H⁰(T).

On the stable open U, relative duality and base change give R¹s_*K=V⊗ω_U, where V is rank 12 and dual to the plane-bundle deformation bundle. This yields H²(s⁻¹U,K)=H¹(U,V(-3)), up to the fixed determinant-line convention. The cotangent target argument in COTANGENT_TARGET.md was also checked: the second finite pair pushforward selects precisely O_h(-3), with no extra sign or base twist.

The Leray filtration is natural for the chosen projection. Block exchange sends it to the other projection’s filtration; it is not an endomorphism of this chosen relative spectral sequence. Therefore attaching block ± or full-alternation projectors termwise to the displayed sequence would be unjustified. RESULT.md explicitly avoids that mistake.

## 5. Remaining limits

The twist cohomology ranks were imported, not recomputed from a physical model. The geometry does not evaluate any retained class, establish injectivity of restriction to U, eliminate exceptional terms, compute H¹(U,V(-3)), or resolve comparison of the two fibrations. Rank 12 remains a sheaf rank, not a bound on global obstruction dimension. Scalar compensation and all-orders module existence remain separate.

No physical source/model/jet evaluation, matrix computation, or experiment was performed in this audit.
