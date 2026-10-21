# Closing the exceptional image defect and isolating its fixed-pair effect

## Result and scope

Retain the actual geometric extension of PR538, with K_j=H¹B(j−1), primary submodule L=U⊗H¹_*(F)(−3), and actual image N=N_im inside P_D=D⊗M_{6−j}*, where M_d=H¹I_C(d), U=H⁰E and D=det U. This note proves

P_D/N=Q_exc⊗k(−1),   dim Q_exc=6,                 (1)

without using the complete ideal resolution or the degree-zero generation of either module. It gives a canonical description of Q_exc as the kernel of an eight-to-two cohomological map.

All three degree-five/six residual fixed-pair quotients can be computed with the full Rao dual P_D. For the ordinary quadratic/cubic two-stage primary test, the intermediate annihilator differs from its full-Rao counterpart by an explicit quotient of Q_exc, hence at most six dimensions. The squared-quadratic intermediate annihilator agrees exactly with the full-Rao one. The primary lift boundary on the exceptional directions is not assumed to vanish.

The exact defect dimension and H²B computation are known in the longer chain. The new contribution is a shorter dependency path from the primary monad/evaluation geometry and the explicit consequences for replacing N_im by the full Rao dual. No original pair or source instance is evaluated.

## 1. The extended exceptional EN sequence

Let G₅⊂H⁰I_C(5) denote the image of the six evaluation minors, equivalently the image of Λ²U. Put

Q₅^sat=H⁰I_C(5)/G₅.

At d=5 the Eagon–Northcott complex is

0→D⊗B(−5)→Λ³U⊗F(−2)→Λ²U⊗O→I_C(5)→0.

Let Z be its image in Λ²U⊗O. The right short exact sequence gives H¹Z=Q₅^sat and H²Z=M₅. The primary fact H¹F(−2)=0 gives the exact segment

0→Q₅^sat→D⊗H²B(−5)→Λ³U⊗H²F(−2)
  →M₅→D⊗H³B(−5)→0.

The final zero uses H³F(−2)=H¹F(−2)*=0. Dualizing, applying Serre duality and tensoring by D yields

0→Q_exc→U⊗H²F(−2)→H²B(0)→D⊗(Q₅^sat)*→0.       (2)

Here Q_exc=(P_D/N)_1, exactly the image defect of PR538. All identifications use the common determinant normalization, not choices on separate lines. In particular

dim Q_exc=8−h²B(0)+dim Q₅^sat.                    (3)

Formula (2) makes explicit why a bound on H²B alone does not yet determine the defect: a quintic saturation surplus would contribute to it.

## 2. A direct two-dimensional H²B calculation

This section reproduces the independent mechanisms of PR455 §§1–3 and PR471 §2, not the latter's ideal-resolution conclusions.

Use ambient V of dimension five, T=V*, the Heisenberg subgroup H, normalizer 𝒩 and quotient G=𝒩/H=SL₂(F₅). Write A=V₁, A*=V₃ and W for the two-dimensional quotient representation in the normalized monad

A⊗O(−1)→W⊗Ω²(2)→A*⊗O.

Write W′ for its two-dimensional Galois conjugate. The published HM identities include Λ²V=A⊗W, Λ²A*=V⊗W′ and the irreducibility of Sym²W of dimension three. These follow from the primary representation construction and Lemma 2.4, not a chosen monad matrix evaluation.

The graded symmetric square of the monad, twisted by one, computes B. Every term has zero positive cohomology. For the only non-elementary central terms, with Q the rank-four universal quotient, use

Sym²(Λ²Q*)=S_(2,2)Q*⊕Λ⁴Q*,
Λ²(Λ²Q*)=S_(2,1,1)Q*.

After twisting by one, the two Schur terms have repeated shifted Bott weights (5,5,4,1,0) and (5,5,3,2,0), so are acyclic, while Λ⁴Q*(1)=O. Thus H²B is the cokernel of the actual final section map

H⁰(W⊗Ω²(3))⊗A*→Λ²A*⊗T.                         (4)

### Universal upper bound

Let R be the image of the original monad map H⁰(W⊗Ω²(3))→A*⊗T. Primary h¹F(1)=10 gives dim R=25−10=15. The map (4) is the exterior image of A*⊗R, up to a common invertible scalar.

For any 15-dimensional subspace R⊂C⁵⊗C⁵, its exterior image in Λ²C⁵⊗C⁵ has dimension at least 30. To prove this without evaluating R, choose a product diagonal one-parameter subgroup with 25 distinct tensor weights and degenerate R to a coordinate subspace. If r_j coordinates occur over column j, then Σr_j=15 and 0≤r_j≤5. The exterior image in that column has dimension 10−binom(5−r_j,2)=r_j(9−r_j)/2≥2r_j. Summation gives 30 at the limit. Equivariance preserves rank off the limit, and rank cannot increase on specialization. Therefore h²B≤50−30=20.

As an H-module the target of (4) is 2End(V). Its invariant part has dimension two; its other characters are the 24 nontrivial characters of H/Z(H), each with multiplicity two. The normalizer acts transitively on those 24 characters. Any nonzero such orbit in the quotient H²B would have dimension at least 24, impossible. Thus H²B is H-invariant and h²B≤2.

### Matching lower bound and exact character

The H-invariants of the source of (4) are 1⊕Sym²W: indeed H⁰Ω²(3)=Λ³V*=Λ²V=A⊗W, so that source is End(A)⊗(W⊗W). The H-invariants of the target are W′. There is no G-map from either the trivial representation or the irreducible three-dimensional Sym²W to the irreducible two-dimensional W′. Hence the invariant part of (4) is zero. Invariants are exact over C for this finite group, so

H²B(0)≅W′,   h²B(0)=2.                           (5)

No stability argument, H¹B dimension, adjoint Hilbert table, or Rao resolution is used in this calculation.

## 3. Quintic saturation and the exact exceptional dimension

By (2) and (5), dim Q₅^sat≤2. The original HM Theorem 3.5 identifies the entire invariant quintic space S₅^H as six-dimensional. The primary section argument on printed p.73 identifies it with the six evaluation minors. Hence

G₅=S₅^H⊂H⁰I_C(5).

The quotient Q₅^sat has zero H-invariant part, by exactness of invariants. Its central character is trivial. Any nontrivial H/Z(H) character would bring the entire 24-element normalizer orbit, contradicting its dimension at most two. Therefore

Q₅^sat=0,   H⁰I_C(5)=G₅,   h⁰I_C(5)=6.           (6)

This excludes extra saturated quintics rather than inferring their absence from sheaf generation alone.

Sequence (2) consequently simplifies to

0→Q_exc→U⊗H²F(−2)→W′→0,                         (7)

proving dim Q_exc=8−2=6. Together with PR538's support result, it proves (1). Since the quotient is supported in degree one it is annihilated by S_+.

The canonical representation statement is that Q_exc is the kernel in (7). No identification with a separately named six-dimensional irreducible is needed or asserted.

As another consequence, M₅ has dimension 25·6−(126−6)=30. Hence N₁ has dimension 30−6=24, and since L₁=0, h¹B(0)=24. This recovers the known dimension independently of the full ideal resolution; it is not a new dimension claim.

## 4. Residual fixed-pair quotients ignore the exception

Return to N=N_im⊂P_D with quotient (1). For any homogeneous pair u of degree two and v of degree three, the natural comparison

(N/(u,v)N)_d→(P_D/(u,v)P_D)_d

is an isomorphism for d=5 and d=6. Indeed the only involved components are d,d−2,d−3, respectively (5,3,2) and (6,4,3), none of which is one. Inclusion is equality on every involved source and target, including their actual multiplication images.

For the squared pair (u²,v), the same argument at d=6 uses degrees (6,2,3), so

(N/(u²,v)N)_6≅(P_D/(u²,v)P_D)_6.                 (8)

These isomorphisms are canonical and do not require N=S(P_D)_0 or a regularity assumption on the pair. Thus all three residual quotients for the order-four decomposition may use the full Rao dual. The separate primary cancellation in the actual K quotients remains necessary.

## 5. The ordinary second-stage kernel has an explicit exceptional part

Set Nbar=N/vN and Pbar=P_D/vP_D. In degree four there is an exact sequence

0→C_exc→Nbar₄→Pbar₄→0,
C_exc=v(P_D)₁/vN₁.                              (9)

Here the degree-four numerators agree, while the degree-one denominators can differ. Multiplication by v induces a surjection Q_exc→C_exc, so dim C_exc≤6. No rank is asserted for that map at a fixed v.

At degree six, Nbar₆=Pbar₆, because both numerator and denominator use nonexceptional degrees six and three. Multiplication by u kills C_exc in this common target: for p∈(P_D)₁,

u(vp)=v(up),   up∈(P_D)₃=N₃.

It follows, by taking kernels in the commutative comparison square, that

0→C_exc→ker[u:Nbar₄→Nbar₆]
  →ker[u:Pbar₄→Pbar₆]→0.                         (10)

Surjectivity on the right follows explicitly: lift any full-Rao kernel class through (9); its u-image maps to zero in Pbar₆ and Nbar₆→Pbar₆ is an isomorphism, so its u-image is already zero.

Thus the ordinary second-stage domain is the full-Rao annihilator plus a controlled exceptional extension of at most six dimensions. It is not asserted to split canonically. In particular the actual primary lifting boundary ∂_u from PR535 need not vanish on C_exc; replacing the domain by the full-Rao kernel without accounting for those directions could omit primary cancellations.

## 6. The square second-stage domain agrees exactly

In degree two the v-quotients use only degrees two and −1, both nonexceptional. Therefore Nbar₂=Pbar₂, regardless of whether the degree-minus-one component vanishes. Their degree-six targets also agree, so

ker[u²:Nbar₂→Nbar₆]=ker[u²:Pbar₂→Pbar₆].           (11)

This equality does not assume M₇=0. The degree-minus-one component is retained equally on both sides. The first-stage v-annihilator used in degree six also agrees for N and P_D because its source and target are degrees three and six. Thus the only exceptional-domain correction among these two-stage tests is (10).

## 7. Dependencies, attribution, and what remains

The actual extension and one-degree support are from PR538. The extended sequence (2), the reduced monad/saturation proof of the six-dimensional defect, and the precise fixed-pair comparisons (8)–(11) are assembled here without PR475/476 or any complete ideal-resolution input. The universal exterior-image bound and orbit exclusion are credited to PR455; the invariant-target calculation appears independently in PR471 §2; the saturation mechanism appears in PR458. The old numerical conclusions are recovered, not claimed as first discoveries.

Primary facts used from Horrocks–Mumford: the representation construction and Lemma 2.4, Theorem 3.5's invariant quintics, the section-wedge identification on printed p.73, and the primary cohomology on pp.72–74. The proof does not use any selected coefficients or rerun an experiment.

Still open here: the fixed v rank Q_exc→C_exc; the actual primary boundary on C_exc and on the remaining annihilator; the original pair's residual quotient values; source membership, higher-order lifting and algebraicity. No equality N=S(P_D)_0 is asserted.

Pinned references:
- PR538 at d5d9bd997145b0ecf7d7bd659a19fb7845afb75f:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/d5d9bd997145b0ecf7d7bd659a19fb7845afb75f/research/hm/actual-primary-image-extension/PROOF.md
- PR535 at 704c4f497a6eb031fa9d223c6ac06cf8a4d27774:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/704c4f497a6eb031fa9d223c6ac06cf8a4d27774/research/hm/two-stage-primary-correction/PROOF.md
- PR455 at 8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4, §§1–3:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4/research/hm/twist-one-structural-vanishing/PROOF.md
- PR471 at a38c45f91c3f29134c6c8d0a2c51d5e8d1e002d9, §2 only:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/a38c45f91c3f29134c6c8d0a2c51d5e8d1e002d9/research/hm/rao-socle/PROOF.md
- PR458 at b46c3b48a8b10a7d0656fde247f2c3f258d1fd23, §5:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/b46c3b48a8b10a7d0656fde247f2c3f258d1fd23/research/hm/pair-interpolation/PROOF.md
- Primary paper:
  https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

Authored mathematical reasoning for independent checking, not formal verification.
