# Historical mathematical review receipt

This receipt describes the original proof at its original hash below. It is preserved as historical evidence, not represented as a review of the normalized publication bytes. See PUBLICATION-CHECK.md for the independent final-publication review and its exact proof hash.

# Independent audit: the five twist-four obstruction blocks

## Verdict

The proof in PROOF.md is correct as a structural restriction. It establishes a canonical quotient-source kernel description of H⁰End₀(F)(4), with exactly five possible irreducible constituents of dimensions 20, 25, 10, 20, and 30. It does not establish the value of any of the five map restrictions or choose which constituents occur.

The coefficient identifications G=V₃⊗(χ₅⊕W) and P=V*⊗χ₃, the target decomposition, the companion cohomology, and the conditional minimal-generator assertion all pass. The final numerical compatibility assertion in §6 also passes.

Audited final PROOF.md SHA-256:

    3b88b7758e1a0f4e8eebf0aa30ca890b3a3148eba42ca84b5b60cfb011ed9a3d

## 1. Sources and independent character check

I read the audited twist-three proof and the twist-two proof and audit, inspected the rendered character appendix of Horrocks–Mumford, and read the relevant text of the primary PDF: (2.2), Lemma 2.4, Lemma 3.3, (4.11), (4.12), and the cohomology table.

The displayed nine character rows agree with the primary appendix, including the distinction between χ₄ and the spinorial Q=χ₄#, and between W and W′. As a check independent of the supplied matrix-inversion script, I reconstructed the rows and used their class-weighted inner products with class sizes

    1, 1, 30, 20, 20, 12, 12, 12, 12.

The rows are orthonormal, and the coefficient, source, target, and cubic-multiplication identities agree. This is only finite character arithmetic, not evaluation of a bundle map.

The required five-dimensional tensor identities have the correct Galois labels. For example V₁²=X⊗(χ₃⊕W′) follows by Galois conjugation from V²=V₁⊗(χ₃′⊕W), and its dual gives V₃²=V⊗(χ₃⊕W′). Likewise V⊗V₃=X⊗(χ₃′⊕W) is the Galois conjugate of the identity in HM Lemma 2.4(ii). All quotient characters involved are self-dual.

## 2. Coefficient signs and cohomological degrees

At twist zero, the resolution's only nonzero line-bundle cohomology is

    A⊗Sym³V → D⊗V → G

in total degrees 1, 2, and 3. Its cohomology is H¹F=V₃, 0, 0. Thus

    [G]=[D⊗V]−[A⊗Sym³V]+[V₃].

In particular the final sign is positive. Character substitution gives G=V₃⊗(χ₅⊕W), of dimension 35.

At twist −1, the only row is

    A⊗Sym⁴V → D⊗Sym²V → G⊗V → P

in total degrees 1 through 4. F(−1) is acyclic, so this complex is exact, giving

    [P]=[G⊗V]−[D⊗Sym²V]+[A⊗Sym⁴V].

The character identity in §3 gives P=X⊗χ₃, of dimension 15. The virtual identities identify actual representation isomorphism classes because the coefficients are actual finite-dimensional N-modules over C and that category is semisimple; they do not assert particular isomorphisms or differential values.

The extra input H¹F(2)=V⊗W′ is also correct. Twisting the resolution by 2 leaves only A⊗H⁴O(−6)=W′⊗V, in total degree 1. Independently, it is exactly HM (4.11) after changing from their bundle F(3) to the normalized F.

## 3. Twist-four spectral sequence

Tensoring by F∨(4)=F(5) gives, in columns −3,−2,−1,0,

    A F(−3), D F(−1), G F,
    P F(1) ⊕ χ₄ F(2).

F(−3) and F(−1) are acyclic. For F, F(1), and F(2), only H¹ survives. In particular H⁰ vanishes at all three twists, H² vanishes away from twist −2, and duality excludes H³ and H⁴ here.

The entire page is therefore

    L=G⊗V₃ → R=P⊗V₁⊗W′ ⊕ χ₄⊗V⊗W′

in positions (−1,1) and (0,1), of dimensions 175 and 190. There is no incoming differential and no higher differential. Consequently the kernel and cokernel are canonically H⁰End(F)(4) and H¹End(F)(4), and all higher cohomology vanishes.

Independent character decomposition gives

    L=V⊗(χ₅⊕χ₆⊕2χ₄⊕2Q⊕χ₃⊕χ₃′⊕W),
    R=V⊗(χ₅⊕3χ₆⊕χ₄⊕Q⊕χ₃′⊕2W).

The dimension checks are 5·35=175 and 5·38=190.

## 4. Canonical quotient, not a chosen complement

The trace splitting embeds S₄ into H⁰End(F)(4), hence into L through the canonical edge identification. This embedded scalar subspace lies in the kernel, so the map descends to δ₄:L/S₄→R and

    ker δ₄=(ker d₁)/S₄ ≅ H⁰End₀(F)(4).

This is the correct canonical construction relative to the chosen equivariant resolution. Since χ₄ and Q each occur twice in L, one should not replace it by an allegedly distinguished complement selected solely from the character decomposition. PROOF.md correctly uses the quotient instead.

Subtracting the scalar character

    S₄=V⊗(χ₄⊕Q⊕χ₃⊕χ₃′)

gives the multiplicity-free quotient

    L/S₄ ≅ V⊗(χ₄⊕χ₅⊕W⊕Q⊕χ₆).

HM (2.2) makes its five constituents irreducible and pairwise inequivalent. Thus each is either wholly in the kernel or absent. The target multiplicities are respectively 1,1,2,1,3; the proof appropriately does not call every restriction a scalar.

No constituent in this residual source is missing from the target. The target decomposition alone therefore does not force any residual kernel block to survive.

## 5. Companion cohomology and numerical restriction

The Euler characteristic of End(F)(4) is 175−190=−15. Removing the scalar Euler characteristic χO(4)=70 gives

    χEnd₀(F)(4)=−85.

Together with higher-cohomology vanishing this proves h¹=85+h⁰. The possible h⁰ values are subset sums of 20,25,10,20,30. No claim is made that each such subset is geometrically realizable.

## 6. Minimal quartic generators and cubic compatibility

The established vanishing in degree 2 implies vanishing in every lower degree: multiplication by a nonzero homogeneous polynomial embeds any lower section space into degree 2, since the bundle is locally free and the base is integral. Thus the degree-four minimal-generator quotient is indeed M₄/S₁M₃.

Under the nonzero cubic alternative, M₃=V₁⊗χ₃, and

    S₁⊗M₃
    =V⊗(χ₃′⊕W)⊗χ₃
    =V⊗(χ₄⊕χ₅⊕W⊕Q).

The identities χ₃′χ₃=χ₄+χ₅ and Wχ₃=W+Q pass independently. In particular there is no V⊗χ₆ constituent in the multiplication domain, hence none in its image. Consequently the unique possible V⊗χ₆ constituent of M₄ maps isomorphically to the corresponding isotypic summand of M₄/S₁M₃. If present, it is a genuinely new 30-dimensional minimal quartic-generator block. This is not an existence claim and does not say the other types could not also give new generators.

Finally, multiplication by a fixed nonzero linear form is injective on M₃, so the full multiplication image has dimension at least 15. Its equivariant representation is a quotient of the multiplicity-free domain with constituent dimensions 20,25,10,20. The smallest available subset sum at least 15 is 20. Therefore M₃≠0 implies h⁰B(4)≥20, and h⁰B(4)=0 or 10 implies M₃=0.

## Boundary

No mathematical blocker was found. The unresolved task is the actual zero/nonzero status of the five irreducible restrictions, which this audit intentionally does not evaluate. No selected HM map, section, source membership, cofactor, or pairing instance was computed, and no external service was modified.
