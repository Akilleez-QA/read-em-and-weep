# Historical scope-limited review receipt

This review concerns the original source, possibly a larger scope than the excerpt in this unit. It is not a review of normalized publication bytes.

# Independent audit: four equivariant mixed-operation parameters

## Verdict and audited version

The proof is correct subject to its explicitly inherited equivariant-resolution, cohomology, Kodaira–Spencer, and canonical-operation inputs. It establishes a four-dimensional space of operations satisfying exactly the stated equivariance, outer-reversal, and cyclic identities, with symmetric and alternating last-two-slot dimensions two each. It does not establish that the actual canonical operation is nonzero or that every eligible map is geometrically realizable.

The current audited `PROOF.md`, including the certificate extension in §7, has SHA-256:

    ba1f46a22eb3e581040b35251aeb0ba4f158b9c62bab50b257bd5b8226e09bde

The earlier version before §7 had SHA-256:

    828d3bc87954f27bbb9aebfef628298d76997e1ca499f85b72d25953276bf755

No correction is required.

## 1. Source and target representation identifications

The Euler sequence supplies the adjoint representation on projective vector fields. The natural orbit-family Kodaira–Spencer map is equivariant for the stabilizing group N. Its imported injectivity and the imported dimension 24 therefore identify U0 with End0(V). The proof correctly uses dimension only after constructing and controlling the map.

For U1, twisted Euler identifies H⁰(T_P(−1)) with V. Contraction of the invariant coefficient tensor of the linear equivariant differential yields an N-map j:V→U1. The formal coordinate-variation identity identifies the coordinate multiples of j with the rank-one directions of the untwisted Kodaira–Spencer map. If j were zero, that entire Kodaira–Spencer map would be zero, contradicting its known isomorphism. Since V is irreducible for H5 and dim U1=5, j is an isomorphism. This also resolves the possible V-versus-V* ambiguity without guessing from dimension or central character alone.

The identification U2=V1⊗Sym³W and its irreducibility are correctly imported from the full-symmetry proof. This audit independently read that proof but does not replace its geometric dependencies with a new cohomology calculation.

## 2. Ordering identities

Given arbitrary F(a,b,c) on U0⊗U1⊗U1, the formulas

    m110(b,c,a)=F(a,c,b),
    m101(b,a,c)=−F(a,b,c)−F(a,c,b)

satisfy all the stated reversal and cyclic equations. Conversely those equations force these formulas. The middle-placement reversal is precisely the symmetry of the displayed sum in b,c. Thus no symmetry or antisymmetry of F itself is forced, including on the diagonal b=c. The full tensor source, with both its symmetric and alternating sectors, is necessary.

## 3. Projector phases and the induced representation

The primary HM §1 isomorphism End(V)≅End(V1) carries the unique trivial summand to itself. It therefore identifies their trace-free parts. Tensor-Hom adjunction consequently identifies

    R=Hom_H5(V1,End0(V)⊗V1)

with Hom_H5(End(V1),End0(V1)) as a G-module. End(V1) has 25 distinct H5/C-character lines. The latter Hom space has a basis consisting of the projectors onto the 24 nontrivial character lines, with image regarded in End0(V1).

This basis has a genuine permutation action. If an element of G carries a line to another line with a nontrivial scalar factor, conjugation of its projector applies the factor once in the image and its inverse in the domain. They cancel. There is therefore no residual character of the stabilizer and no twisted induction in this argument.

The action on nonzero characters of H5/C is transitive; the stabilizer of a nonzero vector in the dual two-dimensional F5-space has order five and is conjugate to a unipotent subgroup P. Thus R=Ind_P^G(1). The proof correctly distinguishes this G-module R from the N-module End0(V), which has nontrivial H5 action.

## 4. Reciprocity and the dimension-only reversal of Hom

Evaluation on H5 multiplicity spaces gives the actual equivariant identifications leading to

    Hom_N(U0⊗U1⊗U1,U2)≅Hom_G(R⊗M,S),
    M=U′⊕W, S=Sym³W.

The next step exchanges the source and target of Hom only at the level of dimension. For complex finite-group representations, decomposition into irreducibles proves

    dim Hom_G(R⊗M,S)=dim Hom_G(S,R⊗M).

It need not give a canonical identification of those Hom spaces. The proof states the dimension equality correctly and does not claim such an identification. Tensor induction and Frobenius reciprocity then give the dimension of Hom_P(S|P,M|P).

The restriction of S to P contains each of the four nontrivial characters exactly once. The restriction of U′=Sym²W′ has one trivial character and two nontrivial characters; that of W has two nontrivial characters. Hence the total is four, with sector contributions two and two. Repeated nontrivial characters between the two summands of M do not affect this count: the count is with multiplicity. No assertion that M is the regular representation of P is needed.

## 5. Interpretation and bounded smoothness conclusion

Irreducibility of U2 implies that a nonzero eligible linear map is surjective. The associated four-scalar description requires choices of bases and provides no values of the actual operation. Projectivizing the nonzero eligible maps yields P³, a parameter space of algebraically allowed maps rather than a moduli or realization theorem.

The family-extension proof and its independent audit show that the particular second-order extension constraint, after trace transposition and the already-established reversal identity, is equivalent to cyclic zero. Therefore that constraint removes no further parameters. This conclusion is bounded: it does not say that all higher-order smoothness conditions, additional naturality conditions, or other geometric restrictions have been exhausted. The finished proof preserves this distinction explicitly.

## Sources and evidence boundary

Static reads for this audit included the finished proof, the full-HM-image-symmetry proof, Čech-transgression-primitives §5, the weight-two-Massey proof, and the family-extension-Massey-constraint proof and audit. The original Horrocks–Mumford paper was read for its normalizer, End-module identity, exterior-square multiplicity, and Lemma 3.3(v). The relevant character restrictions were checked abstractly against these representation identifications.

Only static reads, formal Euler/Kodaira–Spencer arguments, finite-group representation identities, a file checksum, and this local audit-file write were used. There was no literal matrix product, actual source/model/rank/polynomial-instance/point/jet/residual/Massey-value evaluation or execution, large computation, external write, or local Codex task.

## 6. Audit of the explicit four-component certificate

The proof extended by §7 was independently read and audited. Its SHA-256 is:

    ba1f46a22eb3e581040b35251aeb0ba4f158b9c62bab50b257bd5b8226e09bde

The extension is correct and requires no correction.

The chosen N-isomorphism J and the canonical character projector determine r_x0. Its P-invariance is exactly the previously checked cancellation of line phases. Base-coset extraction therefore gives an actual linear isomorphism

    Hom_G(R⊗M,S) → Hom_P(M,S),
    Φ ↦ (m ↦ Φ(r_x0⊗m)).

For a P-intertwiner t, the inverse formula

    Φ_t(r_(g x0)⊗m)=g t(g⁻¹m)

is well defined: replacing g by gp changes its right side to gp t(p⁻¹g⁻¹m), which equals g t(g⁻¹m) by P-equivariance. Its G-equivariance follows by transporting both r_(g x0) and m. Extraction and reconstruction are mutual inverses directly on the permutation basis, so no averaging factor is missing. This direct isomorphism does not rely on exchanging the direction of Hom as in the earlier dimension argument. In particular, §7 uses Hom_P(M,S), whereas §5 uses Hom_P(S,M) after exchanging Hom directions only for the dimension count. Both are valid, and their distinct roles must be retained.

The claimed coincidence of the two source weights is correct. HM defines W′ by the Galois automorphism sending fifth roots to their squares. If W has P-weights ±a, then W′ has weights ±2a, and Sym²W′ has weights 0,±4a=0,±a. Consequently M has one trivial weight and two copies of each of ±a; it does not have all five characters once. The target Sym³W has each nontrivial weight once. Thus the displayed four scalar components are exactly all possible P-intertwiner components. The trivial input line must map to zero, and the target weights ±2a receive no component under this base-coset extraction. Reconstruction still allows the full irreducible G-target.

The four character-projector formulas are valid abstract projections onto the relevant one-dimensional Hom spaces. Their simultaneous vanishing is equivalent to t=0, hence to F=0. The nonzero-component criterion is therefore a genuine abstract certificate, without computing a component of the actual operation. The symmetric/exterior decomposition is preserved by all the representation identifications, so the α components are the alternating sector and the β components the symmetric sector.

Finally, with the slot permutation understood as in formula (5), m101(b,a,c)=−2F_sym(a,b,c). Its vanishing removes exactly the β pair in this space of eligible maps and does not remove the α pair. Choice dependence and the absence of an actual-value or all-order realization claim remain appropriately explicit.

This extension audit used only the static appended proof, previously checked primary representation facts, abstract intertwiner and character identities, and a local audit update. The same evidence boundary applies.
