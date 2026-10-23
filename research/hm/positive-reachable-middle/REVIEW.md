# Independent review: positive reachable middle

Independent mathematical review dated 2026-10-23.

## Verdict

PASS for the theorem as stated, relative to its explicitly imported geometric and cohomological results. The exact restriction cokernel, the 43-dimensional first-arrow image, the 80-dimensional relation space, and the canonical common cancellation subspace with the stated 56-dimensional representation lower bound follow. No mathematical correction to the proof is required.

The review is not a formal proof-assistant certificate and does not recursively re-prove every theorem cited by the five imported sources.

## Exact reviewed artifacts

SHA256:

- PROOF.md: 2f135afb909aa11483274a1eae49cbb3aa311f36b66b478bbeab59ad38072f8b
- verify.py: fc37f9c8b3b28a80cd98b83b52483da40b2aff0006da5c87b7fb34ba272f6634
- audit-inputs/manifest.json: ad20c5523fce7b2c3b8c80acb9ecf401efa84adcf2df86313b0bd61c195ec49d
- REPRODUCE.md: e5cd3cd7693fd967a490d3e94742cffbd2d073a52b4fae887120762a96a323fa

The reviewed final proof includes the sentence, “The comparison is bounded to these pinned dependencies.”

## Authentication of the imported originals

Each of the five files was independently retrieved twice from Akilleez-QA/read-em-and-weep: by its immutable Git blob and by the exact commit and repository path in manifest.json. Both retrievals agree byte-for-byte with the copied audit input. Recomputing Git's blob hash from the UTF-8 bytes gives:

- DEMAND.md: 94238a92e6ba8c2acb4eb75adfcdfedf3bacab4d
- ACTUAL-MONAD.md: 4d2737b94c19b84816382984db9ecb91af66ef0e
- TWIST1.md: 2881e6e4fdd1ff4fd3c1e909b00bd1a8a962a099
- REGULARITY.md: 58785a8799c43fd2c7da089d0ddc5e05822132a9
- INVARIANT.md: 019c1f31773476f0a4877d88632ce5d46fbd4b9f

The imported interfaces actually say what the new proof needs: the actual middle character and invariant normalization; the maximal fixed-line splitting with physical signs; structural H²B(1)=0; the primary section resolution and cohomology support, including H²B(2)=0; and the invariant product's source, kernel and image characters. No source substitutes an abstract generic map for the actual multiplication.

## Mathematical checks

### 1. Higher cohomology

Tensoring the primary locally free section resolution with F*(t) is exact. Using F*=F(1) yields precisely the four terms E₀ through E₃ printed in the proof. For a resolution indexed homologically, the controlling diagonal is H^(i+j)(Eⱼ), not H^(i−j)(Eⱼ).

For t=0,1, H³E₀(t) dualizes to H¹F(−t−1) and H¹F(−t−2), both outside the primary support. H⁴E₁(t) dualizes to H⁰F(−t), which vanishes. Higher diagonal groups exceed the dimension of P⁴. This proves H³B(0)=H³B(1)=0. For H⁴B(0), the only potentially nonzero diagonal term dualizes to H⁰F(−1) and H⁰F(−2), again zero. The trace splitting transfers each conclusion from End(F) to B.

### 2. Ideal Koszul and restriction arrows

The three positive coordinate forms define the negative line as a regular linear complete intersection. Their ideal Koszul sequence has twists 0,1,2 after tensoring by B(3), with factors Λ³V, Λ²V and V exactly as written. Local freeness of B preserves exactness.

For the first short exact kernel sequence, the segments

    Λ²V⊗H²B(1) → H²J → Λ³V⊗H³B(0),
    Λ²V⊗H³B(1) → H³J → Λ³V⊗H⁴B(0)

have zero outer terms. Hence H²J=H³J=0. The second short exact sequence therefore makes V⊗H¹B(2)→H¹(I_L B(3)) surjective and kills H²(I_L B(3)), using H²B(2)=0. The restriction long exact sequence now proves both surjectivity onto H¹(B|L(3)) and equality of its kernel with the actual positive-coordinate multiplication image.

This argument does not assume H⁰ restriction surjectivity or H¹(I_L B(3))→H¹B(3) injectivity. Neither is needed. It explicitly eliminates the higher obstruction groups instead of ignoring a Koszul transgression. Taking the positive eigenspace is exact in characteristic zero, and V is positive, so the source becomes V⊗N₂.

### 3. Fixed-line signs, determinants and quotient character

The authenticated split F|L=O(3)₋⊕O(−4)₊ yields off-diagonal Hom degrees ±7 with negative physical inversion sign and a tracefree diagonal O with positive sign. Twisting by O(3), negative on L, gives O(10)₊⊕O(3)₋⊕O(−4)₊. Thus only the last summand contributes positive H¹, of dimension three.

The imported splitting's determinant calculation is consistent: det K=M^−1 up to the constant determinant of the section space; det(K*⊗Q)=M Q³=O(3), whereas M Q=O(5). Therefore Q=O(−1) and M=O(6), followed by the stated twist back to F. On the G-equivariant level any constant determinant character is trivial because G is perfect.

On P(W*), equivariant Serre duality gives H¹(O(−4))=(Sym²W)* after using det W=1. The latter determinant is trivial, and A=Sym²W is self-dual. No hidden character changes A into the other three-dimensional representation V. The restriction quotient is canonical as H¹(B|L(3))₊; its displayed isomorphism with A does not select a scalar normalization or a splitting of restriction.

### 4. Representations and relation space

The four fixed tensor identities have the stated A/V convention. They give

    V⊗N₂ = 2+7A+6V+8P+10D,
    R = 1+3A+2V+3P+3D,
    E = 1+4A+4V+5P+7D.

Their dimensions are 123, 43 and 80 respectively. The character of E comes from the actual short exact sequence with image R, not from a generic-rank assertion. The first-arrow result alone says nothing about injectivity of the second arrow on R.

### 5. Canonical cancellation

The invariant normalization gives C_inv=ε♯⊗Q with ε♯ invertible, so ker C_inv=V⊗ker Q has character A+V+2P+2D and dimension 24. Actual associativity of positive multiplication gives C₊=b̃a. Consequently C_D=−C_inv on E=ker a, and S=C_inv(E) is canonically contained in both channel images.

The kernel of E→S is exactly E∩(V⊗ker Q), establishing the stated short exact sequence. Bounding its irreducible multiplicities by those of V⊗ker Q leaves

    1+3A+3V+3P+5D,

of dimension 56. All coefficients are nonnegative, so semisimplicity proves existence of the asserted subrepresentation in S. It does not prove equality, identify the entire intersection, or provide a canonical complement. The separate 99−43 image-sum check agrees. The statement that im C₊ embeds in R is valid as a semisimple representation statement; its natural relationship to R is a quotient, not a specified canonical embedding.

Since the curried image of a bilinear factorization through a middle M has dimension at most dim M, the bound excludes a standalone positive-linear factorization of q_D through a middle of dimension 46 or 43. It does not obstruct the actual sum q_inv+q_D.

## Verifier and scope

Both python verify.py and python -O verify.py were independently run and passed. The executable was inspected: it uses exact fixed abstract character arithmetic in Q(√5), elementary support/sign bookkeeping and immutable-input hashing. Runtime requirements remain active under optimization. These checks supplement, rather than replace, the sheaf and cohomology argument above.

No actual HM/source coefficients, points, matrices, derivatives or instance ranks were evaluated. No large computation or external write was performed. The result does not assert an exact 43-dimensional full curry image, a 56-dimensional image in N₄, equality in the cancellation bound, a full-module relation classification, or any source exclusion or source-dual-pair decrement.
