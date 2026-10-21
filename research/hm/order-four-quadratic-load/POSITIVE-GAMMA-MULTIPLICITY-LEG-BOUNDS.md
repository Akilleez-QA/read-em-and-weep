# Actual multiplicity-leg bounds for the positive smoothing coefficient

These bounds concern the actual two consecutive negative-linear multiplication maps

L:W tensor H1(B(2))_+ -> Y=H1(B(3))_-,
R:W tensor Y -> H1(B(4))_+.

They do not require the rank-33 hypothesis on q0. That hypothesis is used only in the final application to gamma. No selected multiplication coefficients or matrices are evaluated.

## 1. Uniform geometry at both ends

For every nonzero negative linear form u, L_u is injective. The hyperplane restriction sequence identifies its kernel with H0(B_Hu(3))_-, which vanishes uniformly, including exceptional hyperplanes.

For every such u, R_u is surjective. The same ambient sequence in the next twist identifies its cokernel with H1(B_Hu(4))_+, which is uniformly zero. The latter vanishing is proved in UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md, sections 1-2: residual chains give higher vanishing, the twist-five plane sequence gives h0(B_H4)_+=17 and h0(B_H4)_-=3, and Euler characteristic 15 leaves h1=5 entirely odd. Its published source is commit adabd228c6160b626fe1c9d9297aad00d349bca5, research/hm/order-four-quadratic-load/UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md.

The actual representations are

H1(B(2))_+=A+2V+3P4+4D5,
Y=3W-prime+3S4+6T6,
H1(B(4))_+=2V+4P4+3D5.

## 2. Three first-leg injections

Let L_D:C4 -> C6 denote the multiplicity map from the four source D5 copies through the T6 constituent of W tensor D5=S4+T6 into Y. Then L_D is injective. Otherwise a nonzero kernel vector selects an actual D5 subrepresentation whose entire linear multiplication factors through a single S4 copy. At fixed u this has rank at most four on a five-dimensional source, contradicting uniform injectivity.

Likewise L_P:C3 -> C6 is injective: W tensor P4=W-prime+T6, and losing the T6 leg would force a fixed-u four-dimensional P4 source into a two-dimensional W-prime. Also L_V:C2 -> C6 is injective because W tensor V=T6 has no other possible constituent.

These are actual ranks of multiplicity maps proved by uniform geometry, not evaluations of actual presentation matrices.

## 3. Three second-leg surjections

Let R_P:C6 -> C4 be the T6-to-P4 multiplicity map of R. Suppose its image has a nonzero quotient Q. Project the P4-isotypical target onto P4 tensor Q. The T6 contribution disappears, while W tensor S4=A+D5 has no P4. Only W tensor W-prime=P4 remains.

At fixed u, every W-prime contribution lands in the same two-dimensional subspace I_u, the image of u tensor W-prime under this unique tensor identification. Hence the projected image lies in I_u tensor Q, a proper subspace of P4 tensor Q. This contradicts surjectivity of R_u. Therefore R_P is surjective.

Similarly R_V:C6 -> C2 is surjective, since only W tensor T6 contains V. Finally R_D:C6 -> C3 is surjective: modulo its image, only W tensor S4 can supply D5, and at fixed u that contribution lies in the same at-most-four-dimensional subspace of the five-dimensional D5 model. Uniform surjectivity again gives a contradiction.

The common fixed-u image subspace is essential: independent multiplicity copies do not supply independently rotated subspaces because the relevant irreducible tensor maps each have multiplicity one.

## 4. Forced nonzero composite and the remaining scalar

The middle T6 multiplicity space has dimension six. Thus

rank(R_P L_D) >= 4+4-6 = 2,
rank(R_P L_P) >= 4+3-6 = 1,
rank(R_D L_D) >= 3+4-6 = 1.

In particular the full actual D5-to-P4 two-linear-step channel cannot vanish identically across all source and target multiplicities.

Now impose the rank-33 hypothesis at q0. Let d0 be the nonzero source multiplicity vector selecting its unique D5 kernel and let eta be the nonzero P4 target multiplicity covector defining its cokernel. The earlier criterion reads

gamma = a nonzero normalization times eta R_P L_D d0.

Both legs are now known nonzero: L_D d0 is nonzero by injectivity, and eta R_P is nonzero by surjectivity. Moreover their ambient composite has rank at least two. Nevertheless the particular pairing may still vanish. A nonzero vector and nonzero covector need not pair nontrivially, even when the full composite has rank two. This note does not claim otherwise and does not select gamma's value.

The remaining geometric target is the incidence condition between the q0-selected kernel line and cokernel hyperplane under this actual rank-at-least-two composite. Proving that they are not incident would establish gamma nonzero; the uniform leg bounds alone do not.

Reproduction: python verify_positive_gamma_leg_bounds.py. It checks the representation identities and exact dimension inequalities. The actual injectivity and surjectivity proofs are the uniform geometric arguments above.
