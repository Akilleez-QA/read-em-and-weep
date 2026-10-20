# Independent audit: canonical-line rank-five strengthening

## Verdict and scope

**PASS, conditional on the stated imported hypotheses and results.** I checked all sections of `PROOF.md`, including the additional rank-five rigidity statement in Section 4. No mathematical gap was found. The line theorem is independent of the global decic-closure assumptions. The degree gap is conditional on those assumptions and the previously established invariant-curve classification.

This audit uses abstract representation theory, vector bundles on the projective line, and local intersection multiplicities. No actual source-instance evaluation is claimed. The audited proof was not modified.

The dependency check included:

- `../canonical-line-parity-exclusion/PROOF.md`, especially its representation identities, constant-rank image-bundle construction, and rank bounds;
- `../rank-three-curve-constraints/PROOF.md`, especially its local multiplicity argument and the classification of arbitrary invariant reduced curves of degree at most 37;
- `../rank-three-line-rank-constancy/PROOF.md`, Section 7, for the identification of the possible twenty-five-line orbit with the canonical odd reflection lines.

These dependencies remain conditional inputs, rather than claims that the underlying source map or decic closure has been newly verified here.

## 1. Small-target lemma

The lemma is valid for every two-dimensional complex representation B, without any assumption that B is irreducible or isomorphic to W. Since Sym^2 T = 1 + P_5 and P_5 is irreducible,

    Hom_Gamma(W tensor P_5, B)
      = Hom_Gamma(P_5, W* tensor B) = 0.

A nonzero map from the irreducible P_5 would be injective, whereas W* tensor B has dimension four. Thus only the invariant quadratic contraction survives. Applying this independently to each two-dimensional summand proves the stated extension to a direct sum. The normalizing scalar of q is immaterial.

## 2. Constant sections and the rank-four possibilities

The imported constant-rank result applies to both parity pencils. Their image bundles are genuine subbundles, with ordinary splitting O(-1)^a + O^b. Consequently H^0(I) has dimension exactly b; its evaluation embeds it as the fixed subspace of constant target sections contained in every fiber. This is intrinsic and equivariant, so it does not require an equivariant choice of Birkhoff–Grothendieck splitting.

For the odd pencil, the fixed two-dimensional H is contained in this constant subspace. The central involution acts as -1 on its constant sections because it fixes the base and acts as -1 on J_-. Perfectness of Gamma makes the determinant character trivial. Thus b is even and at least two. Given rank four, the only possibilities are (a,b)=(0,4) and (2,2), exactly as stated.

In the first case the image is the fixed representation C. Maschke's theorem supplies an invariant two-dimensional complement to H, allowing the small-target lemma to be applied to each summand.

## 3. Equivariant quotient construction in the second case

When (a,b)=(2,2), the quotient by H tensor O is ordinarily O(-1)^2. Projection along an invariant complement of H in J_- embeds that quotient into the complementary trivial bundle. This is a subbundle: fiberwise its kernel before quotienting is exactly H, and the remaining cokernel is the already locally free cokernel of the original image inclusion.

Let F denote the quotient and U the canonically linearized tautological O(-1). The ordinary bundle F tensor U* is trivial of rank two. Evaluation therefore gives an isomorphism

    U tensor H^0(F tensor U*) -> F,

and evaluation is equivariant. The central involution acts as -1 on F and on U, hence as +1 on B=H^0(F tensor U*). Thus B descends to A_5. Complete reducibility and the absence of nontrivial one- or two-dimensional A_5 representations imply B is two copies of the trivial representation.

The inclusion U tensor B -> J' tensor O corresponds, by global sections after twisting, to a Gamma map W tensor B -> J'. Its fixed linear span is therefore a quotient of W + W, and is a sum of at most two copies of W. All mixed values lie in H plus this fixed span. The small-target lemma consequently applies exactly as required.

No equivariant splitting of the original image bundle is being silently assumed. The chosen invariant target complement and the quotient suffice. In fact an ordinary bundle splitting, if desired here, can be averaged over the finite group to obtain an equivariant splitting, but the argument does not need that additional observation.

## 4. Contradiction and rank transfer

Over C the nondegenerate ternary q has a nonzero isotropic vector t. The derived form f(t,u,t)=q(t)h(u) vanishes for every u in W. Outer symmetry and the cyclic identity then give 2f(t,t,u)=0. Repeated-input injectivity at t would put a nonzero u in Ct, contradicting W intersect T=0. This excludes both rank-four possibilities.

Thus the odd block has rank at least five, the even block at least four, and their complementary target eigenspaces give total rank at least nine. The imported identity rank b=4+rank Q gives residual rank at least five. Normalizer equivariance gives the same assertion on all twenty-five canonical lines, including every point of each line. Hence these lines do not merely fail to be components of Z_4: they are disjoint from Z_4.

## 5. The curve-degree range 40 through 125

At the generic point of any reduced curve component C of Z_4, the rank of b over the residue field is s<=8. After splitting off an invertible s-square block, every ten-minor belongs to the square of the maximal ideal of the three-dimensional regular local ring O_(P^4,eta_C).

Under dim Z_5<=1, three degree-ten members of the minors' linear system can be chosen as a regular sequence. Their pure curve complete intersection has degree 1000 and contains every C in question as a component. In the generic local ring their parameter ideal q satisfies q subset m^2. The same length comparison as in the imported proof gives

    length(R/q) >= 2^3 = 8.

Summing multiplicities times degrees gives 8 deg Gamma_4<=1000, hence deg Gamma_4<=125. The chosen complete intersection need not be invariant. No claim of a better multiplicity is needed.

The existing component-orbit classification is explicitly for any nonzero normalizer-invariant reduced curve of degree at most 37, not only curves in Z_3. It therefore applies to Gamma_4 whenever its degree is at most 37. Its only remaining configuration is a free A-orbit of twenty-five lines. The identification of this orbit as the canonical odd lines uses Section 7 of the line-rank-constancy proof; this identification is an important part of the dependency chain. The new line theorem excludes that configuration.

Finally Gamma_4 is A-invariant as a reduced cycle, so its degree is divisible by five. Excluding all positive degrees at most 37 and imposing that divisibility yields the exact stated necessary range

    deg Gamma_4 in {40,45,50,...,125},

unless Gamma_4=0. In particular, degrees 38 and 39 are excluded by divisibility, not by an extension of the small-curve classification. This does not establish existence at any listed degree, exclude all curves, eliminate isolated points, or improve a compatible-fiber bound.

## 6. Additional rigidity at residual rank five

Residual rank five means total rank nine. The established separate lower bounds force parity ranks exactly (4,5).

For the even block of rank four, the kernel of the map O(-1) tensor (W tensor T) -> I_+ has rank two. Its H^0(K(1)) is an invariant subrepresentation of the irreducible six-dimensional W tensor T and is proper, hence zero. Both kernel splitting degrees are therefore at most -2. Since deg K=-6+a, this gives a<=2 and b>=2.

The constant image is a subrepresentation of the span of the even coefficients, and that span is a quotient of T + P_4 + P_5. Semisimplicity justifies using this decomposition for subrepresentations of the quotient as well. With b between two and four, the only possible dimensions are b=3, with constant representation T, and b=4, with constant representation P_4. If b=3 the remaining quotient is an ordinarily O(-1) line bundle on which z acts positively. Twisting by canonical O(1) would yield an ordinarily trivial line bundle with a one-dimensional Gamma representation on sections having z=-1. Perfectness excludes it. Thus I_+=P_4 tensor O equivariantly.

For the odd block of rank five, b is even and at least two, so b is two or four. If b=4, its quotient is O(-1). Its linearization agrees up to character with the canonical one, and Gamma has no nontrivial characters. Its span in a complementary target is consequently a copy of W. The constant image splits as H plus another two-dimensional representation, so the same small-target argument excludes this case.

When b=2, the constant subspace is exactly H and the quotient is U tensor B for a three-dimensional A_5 representation B, by the same equivariant evaluation argument checked above. If B is trivial the mixed-value span consists of copies of W, giving the isotropic contradiction. Every nontrivial semisimple three-dimensional A_5 representation is one of its two irreducible three-dimensional representations. This proves precisely the stated necessary form. It does not assert that either form can actually occur.

## Suggested clarification, not a correction

For maximal citation precision, Section 3 could explicitly cite Section 7 of `../rank-three-line-rank-constancy/PROOF.md` alongside the small-curve classification when it calls the surviving orbit canonical. The identification is already available in the stated dependency chain, so its omission as a separate citation is not a mathematical gap.
