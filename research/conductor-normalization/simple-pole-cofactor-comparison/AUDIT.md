# Preserved mathematical audit

This review concerns the source manuscript and its stated assumptions. It is preserved as mathematical history, not a new independent certification of all publication edits or of unpublished input theorems. Source and publication hashes are recorded in SOURCE-HASHES.json. A split manuscript’s module or polar application remains conditional in its destination unit.

# Independent audit: simple-pole cofactor comparison

Reviewed `PROOF.md` independently against the two short exact sequences, the normalization quotient sequence, Serre duality, and the Hilbert–Burch factorization. No actual matrix, rank, source class, or obstruction value was evaluated. No additional external source was required.

## Verdict

The comparison, secondary obstruction, conductor residual quotient, and dual criterion are mathematically correct. In particular equation (9) preserves both ambiguities that a normalization-only test can miss. There is no additional vanishing assumption on H²(B(1)).

## Checked points

1. **Naturality and sign.** Lifting an L-valued one-cocycle to p with dp=Δk gives d(p,0)=(b,A)(jk). Therefore δ_M n₁=H²(j)∂ with a plus sign.

2. **Correct quotient.** After quotienting H¹(M) by the image of H¹(B(2)), the left term is coker[5H¹(B)→4H¹(B(1))], and the right term is ker[5H²(B)→4H²(B(1))]. Neither can be replaced by the raw ambient group without an additional proof. Formula (2) is exact even if the individual H¹(B(2)) maps have kernels.

3. **Secondary invariant.** For du=jk, the closed lift is (p,0)−(b,A)u. Its remaining component is −Au. Thus formula (5) has the correct minus sign and defines the canonical map on ker α without a splitting.

4. **Hidden conductor kernel.** If a normalized class is a B(2) image, subtracting the same B(2) image downstairs puts it in ker n₁. Hence ker f=∂(ker n₁)=im(∂γ). With dc=Au and du=jk, the conductor class is represented by −bu modulo Δ, so κ=∂γ=−d₂. Both signs in the proof are compatible.

5. **Residual quotient (9).** Because ker ∂=I, one has ker(∂γ)=γ⁻¹(I). The first isomorphism theorem therefore gives im κ≅H⁰(Q)/γ⁻¹(I). The equality ker γ=im[H⁰(M)→H⁰(Q)] then gives the displayed two-stage quotient. Its denominator must include the preimage of I∩im γ, rather than only normalized global sections. For a fixed polar class x in ker f, the resulting residual class maps to x, so its vanishing is equivalent to x=0 and is independent of all the stated choices.

6. **Dual map.** Trace and Serre duality give α*=H²(jᵗ):5H²(B(−5))→H²(B(−1)). Degree-two pairings introduce no Koszul sign. The relation α*β*=0 is the transpose of β α=0.

7. **Hilbert–Burch criterion.** The twists in (11) are correct. The boundary h lands in the kernel used to define V_Z, and h a is contained in that kernel. A lift θ changes by im a, so t is well-defined. Adjusting θ by a class from im a proves exactly im α*={η∈ker r:t(η)=0}. Invertibility of the square map is therefore equivalent to the stated two structural conditions, without evaluating them.

8. **Cokernel filtration (13).** Since ker t=im α* inside ker r, the canonical quotient sequence gives 0→im t→coker α*→im r→0. Finite-dimensional duality identifies coker α* with (ker α)*, so the stated dimension identity is formal. In fact t is surjective onto V_Z: exactness of the Hilbert–Burch cohomology sequence makes h surjective onto the kernel defining V_Z, and every θ maps to an η in ker r. Thus im t=V_Z and the final version of (13), verified on a further read, is 0→V_Z→coker α*→im r→0. This strengthening requires no extra vanishing or rank calculation.

## Notation corrections verified

A second read verified that the normalization scheme is now denoted ṼD, the presentation matrix is R_mat, and the corrected class in the final conductor test is explicitly ξ_adj. The previously reported name collisions and representative ambiguity are resolved. Equation (9) and the final vanishing criterion are unchanged.

## Addendum: formal numerical lower bounds

The proposed numerical corollaries pass independent review. These are deductions from Riemann–Roch, duality, and exactness, not evaluations of a selected matrix or its actual rank.

### Sources and ambient groups

I read `../fourth-power-cohomology/PROOF.md`, Sections 1–2, and `../hm_primary_source_verification.md`, and independently viewed the saved primary-page image `../hm_decker_schreyer_p218.jpg`. The displayed proposition on printed p.218 of Decker–Schreyer, *Pullbacks of the Horrocks–Mumford bundle* (1987), explicitly gives h¹(End F)=24, h¹(End F(−1))=5, and H¹(End F(k))=0 for k≤−2. Trace splitting transfers the intermediate-cohomology statements to B.

The verified normalized Chern classes c₁(F)=−H and c₂(F)=4H² give ch(B)=3−15H²+(75/4)H⁴. The resulting polynomial is

    χ(B(t))=3 binom(t+4,4)−(15/2)t²−(75/2)t−25.

In particular χ(B(1))=−55. Duality and the negative-H¹ proposition give H³(B(1))=H¹(B(−6))*=0. Stability of F gives Hom(F,F(−6))=0, hence H⁰(B(−6))=0 and H⁴(B(1))=0. No stability assertion for B is necessary. Therefore

    h¹(B(1))=55+h⁰(B(1))+h²(B(1))≥55.

This does not assume either h⁰(B(1)) or h²(B(1)) vanishes.

### Hilbert–Burch boundary-image bound

Let K_HB=ker[4H³(B(−6))→5H³(B(−5))]. Serre duality gives

    dim K_HB ≥ 4h¹(B(1))−5h¹(B) ≥ 220−120=100.

Since V_Z=K_HB/im(h a) injects into coker α*, whose dimension is at most ten,

    dim im(h a)=dim K_HB−dim V_Z
                ≥90+4h⁰(B(1))+4h²(B(1))≥90.

Consequently h¹(Z,B(−1)|Z)≥90. The stronger independent surface bound below supersedes this last cohomology bound, while the boundary-image bound ≥90 remains separately valid.

### Sharper surface-cohomology bound

Writing G_Z=B(−1)|Z, the four-term Hilbert–Burch resolution gives

    χ(G_Z)=χ(B(−1))−5χ(B(−5))+4χ(B(−6)).

The same polynomial yields respectively 5, −22, and −55. Thus

    χ(G_Z)=5+110−220=−105.

Because G_Z is supported on the projective surface Z, its cohomology vanishes above degree two. Hence the exact identity and bound are

    h¹(G_Z)=105+h⁰(G_Z)+h²(G_Z)≥105.

No assumption of smoothness of Z, positive-twist vanishing, or an evaluated cofactor rank enters either numerical corollary.
