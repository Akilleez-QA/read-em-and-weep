# Independent audit

## Verdict

The argument in PROOF.md is valid. It proves a necessary Sylow-five representation constraint: on a fixed exceptional-clock eigenspace, the actual kernel is a sum of four lines, one in each specified two-dimensional corrected-action eigenspace. No mathematical correction was required.

## Checks

1. **Groups and lifts.** The polynomial diagonal normal forms give |P|=625. The monomial-cycle relation gives g^5=1, while Zg=zeta gZ gives the order-125 Heisenberg subgroup H′. The exact relation DgD^-1=zeta gZ² and X=gD^-3Z^-3 prove normality and index five. The linear/projective orders and the distinction from the exceptional point stabilizer are consistent.

2. **Corrected operator.** In central character zeta³, X raises total Z-weight by three. The ratio of the proposed Q eigenvalues is zeta^[2((j+3)²-j²)]=zeta^(2j+3), exactly the conjugation factor for D on X. Thus B=DQ(Z)^-1 commutes with P, has fifth power one, and is natural under equivariant maps. The degree-three exponent formula is correct.

3. **Source multiplicities.** The Z-weight-zero Schur space has four one-dimensional repeated-index blocks with D-weights 1,1,4,4 and two distinct-index blocks of dimension two with weights 2 and 3. Consequently every nontrivial B-character has multiplicity two there, and the trivial character is absent. Primitive-central-character Heisenberg representation theory transports these multiplicities to every g-clock eigenspace. Each E_a therefore has dimension two.

4. **Target scalar normalization.** Using total Z-weight j, the relation on A forces D_j=delta zeta^(3j²), with delta^5=1. The exact normalizer conjugacy D~D^4 gives delta G(3)=delta^4 G(12). Reindexing by j↦2j gives G(3)=G(12), and the quadratic Gauss sum is nonzero, so delta=1. This removes the potentially consequential character shift. In basis coordinates with Z-weight 2j, the same exponent is 2j², so the two coordinate conventions agree.

5. **Target characters and kernel.** The Z-weight-zero part of exterior²V has D-weights 2 and 3. The established identity exterior²V=A tensor W therefore gives exactly these weights on W, and weights 1,2,3,4 once each on Sym³W. On A*, D agrees exactly with Q(Z), so B_J acts as identity tensor D on the four-dimensional factor. Each resulting five-dimensional B-eigenspace has primitive H′ central character and hence one copy of each g-character. Surjectivity of q remains surjectivity on simultaneous g/B eigenspaces by their spectral projectors. The four maps from dimension two to dimension one thus have one-dimensional kernels, proving L=ell_1 direct sum ell_2 direct sum ell_3 direct sum ell_4.

6. **Incidence and scope.** The imported universal formula gives residual rank five only when the displayed sum of five intersection dimensions equals five. The product (P1)^4 has dimension four, versus dimension sixteen for Gr(4,8). Membership in that product or in its stated incidence locus does not establish full-normalizer realization, global repeated-input injectivity, or existence of a rank-five point. The proof explicitly preserves these distinctions.

## Evidence boundary

This audit used static proof reads and symbolic finite-group, tensor, and character arguments only. No actual cubic-operation value, source coefficient, source input, rank instance, derivative, or residue was evaluated. The relevant imported universal rank formula and actual target identification were checked in the cited Heisenberg and cubic-module proofs.
