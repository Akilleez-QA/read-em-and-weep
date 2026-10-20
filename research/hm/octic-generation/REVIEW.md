# Independent scoped mathematical review

## Verdict and frozen object

**PASS within the stated dependency scope.** I found no mathematical obstruction in the new argument. In particular, the proof establishes nonvanishing of the actual multiplication map, not merely a representation-theoretically allowed map. The asserted absence of octic generators follows. With the imported sextic and septic conclusions and regularity bound, the asserted list of six quintic and ten sextic minimal generators follows.

Reviewed file: `PROOF.md` in this directory.

Exact SHA-256: `7b7f1f173e1bddb06599e0e3cfe83f3b5ed8ae1881aa6cab1937a9a676284c09`.

This is an independent mathematical review, not formal proof-assistant verification. The frozen proof was not edited. No selected HM/source instance, coefficient search, numerical matrix/rank calculation, polynomial generator construction, or large computation was used. The rank-six calculation below is derived from universal bundle cohomology for an arbitrary hyperplane; it is not an evaluation of the HM multiplication map.

## Scope and checked dependencies

I read the following four pinned public dependency proofs:

- [Exact sextic saturation](https://github.com/Akilleez-QA/read-em-and-weep/blob/a091db646c2ad9ba73d0893f4d92ff54891aaf0c/research/hm/exact-sextic-saturation/PROOF.md), SHA-256 `105812f9f0414a744c3d8b881edf4d3cd3b651ab0a59d6ee4e82a6ef0e9c1a3e`.
- [Exact septic saturation](https://github.com/Akilleez-QA/read-em-and-weep/blob/b378990352d5f9bba3aaed27a0b6e0ff4683e15c/research/hm/exact-septic-saturation/PROOF.md), SHA-256 `2d60f124d55bae90989b39051c88057e5a083237b0b4603a6128b483433146fd`.
- [Septic multiplication](https://github.com/Akilleez-QA/read-em-and-weep/blob/8bdc576a17726fa348efec82a7644f83074f34e1/research/hm/septic-multiplication/PROOF.md), SHA-256 `49e1cd6d0db85e093a087d6023823d91bd8c72cd166fa60b6e3f4c609d818f75`.
- [Primary septic channel](https://github.com/Akilleez-QA/read-em-and-weep/blob/36ea1150b72014f9cae106917cde2e234e45aff1/research/hm/septic-primary/PROOF.md), SHA-256 `91bed29fa0887e04d4d9259863bd476be294185c56c99c955d67457a9b5e44fe`.

Their relevant constructions are consistent with the uses in the frozen proof: the normalized equivariant monad, the graded symmetric-square complex, the two-entry computation of B(-2), the representation labels, natural EN exact sequences, absence of septic generators, and injectivity of cubic quintic products. The review is conditional on the established geometric EN setup, the disjoint-line description, and earlier low-degree saturation results; it does not reprove the whole preceding research chain.

I also checked the original [Horrocks–Mumford paper](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf). Particularly relevant are criterion (2.2), Lemma 2.4(ii), equation (4.2), the cohomology table, and the Appendix. The potentially dangerous tensor identity V* ⊗ V3 = V1 ⊗ (U ⊕ W′) is specifically Lemma 2.4(ii), not an interchange of the two three-dimensional representations. Equation (4.2), with the original bundle shifted by -3, also supports generation of normalized H¹F in degree zero.

## 1. Universal Bott multiplication: pass

On P(V), use rho = (4,3,2,1,0). For S_lambda Q*(t), the convention used in the proof gives shifted tuple (t+4,lambda_1+3,lambda_2+2,lambda_3+1,lambda_4). Applying it gives:

- S_(2,2)Q*(-2): (2,5,4,1,0), sorted as (5,4,2,1,0), with exactly two inversions; subtracting rho gives (1,1,0,0,0).
- S_(2,2)Q*(-1): (3,5,4,1,0), sorted as (5,4,3,1,0), with exactly two inversions; subtracting rho gives (1,1,1,0,0).

Each has sole cohomology in degree two, of dimension ten. The other summands are O(-3) and O(-2), both acyclic on P4. Thus the two cohomology modules are respectively Λ²V* and Λ³V*, with the indicated SL(V)-linearizations. The duals are consistent with S1=V*. No ambient determinant correction survives on SL(V).

For an arbitrary hyperplane H=P(U), a complement to U in V splits Q*|H as Q_H* ⊕ O. Exterior squaring gives K|H = Λ²Q_H* ⊕ Q_H*. Symmetric squaring gives precisely the four summands in the proof: Sym²(Λ²Q_H*)=S_(2,2)Q_H*, the mixed term is S_(2,1)Q_H* ⊕ Λ³Q_H*, and the last term is Sym²Q_H*. There is no missing multiplicity or additional determinant summand in rank three.

On P3, with rho=(3,2,1,0), their twists by -1 have:

- S_(2,2): shifted (2,4,3,0), two inversions, resulting highest weight (1,1,1,0); sole H² of dimension four.
- S_(2,1): shifted (2,4,2,0), repeated 2; acyclic.
- Λ³Q_H*(-1)=O_H(-2); acyclic.
- Sym²Q_H*(-1): shifted (2,4,1,0), one inversion, resulting highest weight (1,0,0,0); sole H¹ of dimension four.

The restriction splitting is not required to be normalizer-equivariant; it is used only to compute ordinary cohomology of an arbitrary hyperplane restriction. The restriction long exact sequence, including H¹G(1)=0 and H³G=0, therefore gives exactly the displayed five-term sequence. Its middle map has rank six and is nonzero for every nonzero linear form cutting out H.

Finally, Λ³V* occurs once in V* ⊗ Λ²V*. The multiplication is SL(V)-equivariant, so its nonvanishing proves that it is a nonzero scalar multiple of wedge. This scalar is genuinely established, rather than assumed from multiplicity one.

## 2. Symmetric-monad cohomology and its multiplication: pass

The degree conventions are correct: the symmetric complex J resolves Sym²F=B(-1), so J(-2) computes B(-3) and J(-1) computes B(-2). Exterior powers at the two odd-degree ends and the additional A ⊗ A* summand in degree zero are the correct graded symmetric-square terms.

For J(-2), the line bundles appearing have degrees -4,-3,-2 and are acyclic on P4. Its left K term is K(-3)=Ω²(-1), also acyclic. Its right K term is K(-2)=Ω², with sole H²=C. In the central term, the Λ²K part is S_(2,1,1)Q*(-2), with shifted tuple (2,5,3,2,0), so it is acyclic. The Sym²K part contributes exactly section 1's H². This leaves only (0,2) and (1,2), as asserted.

For J(-1), the corresponding central Λ²K tuple is (3,5,3,2,0), again singular. The only other nonzero contribution is K(-2) at (-1,2). This agrees with the previously proved injective differential and with the sole H² cokernel for B(-2).

Equivariant Serre duality is applicable because B is self-dual and N lies in SL(V). It gives H³B(-3)=H¹B(-2)*=0, forcing the right differential of J(-2) to be onto. Its kernel has dimension twenty. The identifications Λ²V*=A* ⊗ W and Λ³V*=A ⊗ W use the same W, not W′: they follow from Λ²V=A ⊗ W, duality, and unimodularity/self-duality of W.

Under U ⊗ W = W ⊕ Sym³W, both W and Sym³W occur once. Thus the source kernel is the A* ⊗ Sym³W summand and the target cokernel is the A ⊗ Sym³W quotient. Isomorphisms with named abstract tensor products can carry nonzero scalar choices; the kernel, image and quotient subspaces are intrinsic. Nothing in the argument requires a preferred normalization.

Crucially, multiplication is a chain map J(-2)→J(-1). On the central E1 term it is id_U tensored with universal wedge. Each relevant total-degree-two cohomology group has exactly one spectral-sequence graded piece. The source is a kernel in that position; the target is a cokernel in that position. Therefore the actual induced multiplication is the restriction of central multiplication to that kernel followed by the cokernel projection. There is no hidden higher differential, alternative filtration piece, or extension correction.

## 3. The spin restriction: pass

The tensor identity V* ⊗ A* = A ⊗ (U ⊕ W′) is correctly labeled. After applying the Heisenberg multiplicity-space equivalence, wedge is a nonzero map (U ⊕ W′) ⊗ W → W. The W′ ⊗ W factor is the ordinary T4, not the spin Q4, and cannot map to W. The U ⊗ W factor contains W exactly once. Consequently wedge on this multiplicity space is a nonzero scalar multiple of the natural trace-free endomorphism action Sym²W ⊗ W → W.

The two copies of U in the next step must be distinguished conceptually. One is the unchanged Sym²W from the central symmetric-square complex. The other is the multiplicity factor in V* ⊗ A*. Decomposing V* ⊗ A* does not mix the unchanged first U factor with the final W factor. Hence the asserted kernel inclusion and quotient projection remain respectively the standard polarization Sym³W→Sym²W⊗W and standard multiplication Sym²W⊗W→Sym³W, up to nonzero constants.

For a trace-free endomorphism a of W and a pure symmetric cubic v1v2v3, the resulting map is

(1/3) [v1v2·a(v3) + v1v3·a(v2) + v2v3·a(v1)].

This is exactly one third of the usual derived action on Sym³W. It is nonzero, as the proof's h⊗e³ test shows. This is a symbolic calculation in an abstract two-dimensional representation, not a selected HM map evaluation. It proves nonvanishing after both the actual kernel restriction and the actual cokernel projection.

The target A ⊗ Q4 is irreducible by criterion (2.2), since A is irreducible on the Heisenberg subgroup and Q4 is irreducible on the quotient. Therefore the actual cohomology multiplication onto H²B(-2) is surjective. Nonvanishing alone would not suffice without this irreducibility, and the proof supplies it.

## 4. EN naturality and ideal generation: pass

At degrees seven and eight, the EN complexes are twists of one fixed complex, so multiplication by a linear form commutes with all arrows and their connecting homomorphisms. The old-product identifications R_d=H¹K_d come from the second short exact sequence; they are not arbitrary representation isomorphisms.

The first short exact sequence at degree eight yields

0 → Λ³V_s ⊗ H¹F(1) → H¹K8 → D ⊗ H²B(-2) → 0

because H¹B(-2)=0 and H²F(1)=0. Separately H⁰F(1)=0, together with H¹B(-2)=0, gives H⁰K8=0 and hence injection of cubic quintic products. The degree-seven row is the corresponding established sequence. All determinant factors are retained consistently, and D is trivial as in the dependency conventions.

For clarity, the needed primary multiplication also follows directly from the monad: its degree-zero right term gives M0=A*, and its degree-one right term gives M1 as a quotient of A*⊗S1. The relevant intermediate H¹ vanishing follows from the two monad short exact sequences and acyclicity of the line-bundle terms. Thus S1⊗M0→M1 is onto as an actual graded-module map, not just by dimensions.

Tensoring the degree-seven row by S1 preserves exactness. Surjectivity on its left term and on its right quotient implies surjectivity on the middle term by the stated lift-and-subtract argument. No splitting of the EN extension, canonical or otherwise, is needed. The dimensions 20,40 and 20 for the indicated terms are consistent, but not used to replace this argument.

Since S1(S2 I5)=S3 I5, surjectivity modulo old quintic products implies S1 I7=I8. Combined with the independently established S1 I6=I7 and regularity eight, this excludes every additional generator degree. The lower-degree counts then give exactly six generators in degree five and ten in degree six. The proof properly declines to infer the remaining syzygy modules or a complete resolution.

## Issues and limits

No blocking issue was found. A useful optional citation clarification would be to name HM Lemma 2.4(ii) explicitly beside V*⊗A*=A⊗(U⊕W′), and HM equation (4.2) beside primary-module generation; neither omission is a logical gap given the stated dependencies.

This pass is restricted to the generator-degree theorem and its stated assumptions. It does not certify original fixed-pair intersections, actual-source membership, pure conditions, higher-order lifting, algebraicity, or any complete Betti table. No conclusion about those separate questions follows from this review.
