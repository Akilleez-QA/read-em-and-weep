# Excluding the cubic ghost by extremal quadratic growth

Work over C with S=Sym(T), dim T=5, and H the dual HM cohomology module of PR483. Put W=W′=H_0, E=A*, and L=ker(S⊗W→H). The argument uses the actual normalizer-equivariant module and the pinned structural identifications, but evaluates no selected HM or source instance.

We prove that the optional cubic Betti parameter r of PR483 is zero. Consequently H has a presentation with its ten quadratic relations alone, and the Fitting ideal of PR495 has no minimal quintic generators: c=0.

## 1. Inputs and a five-quadrics lemma

The following inputs are pinned below:

- S_2=E⊗Sym²W and L_2=E⊗W; both identifications are equivariant.
- The inclusion L_2→S_2⊗W is, up to a nonzero scalar, id_E⊗r, where for a basis x,y of W,
  r(x)=x²⊗y−xy⊗x and r(y)=xy⊗y−y²⊗x.
- T⊗E=A⊗(U⊕W), U⊗W=R_6, and W⊗W=1⊕U′, with U′=Sym²W. Thus
  T⊗L_2=A⊗(R_6⊕1⊕U′), with each indicated summand irreducible and multiplicity one.
- H has no linear relations. Its linear syzygy space among the quadratic relations is either zero or the unique summand A⊗U′, of dimension fifteen. Its dimension is the same parameter r that counts minimal cubic relations; r∈{0,15}.

Lemma. Let Q⊂S_2 have dimension five. The kernel of T⊗Q→S_3 has dimension at most ten. If it has dimension ten, then Q=ℓT for a nonzero linear form ℓ∈T.

Proof. Write J=(Q). The quotient has h_2=15−5=10=binom(5,2). Macaulay's growth theorem gives h_3≤binom(6,3)=20, so dim(TQ)≥35−20=15 and the kernel has dimension at most25−15=10. Equality gives h_3=20. Since J is generated in degree two, Gotzmann persistence applies and gives h_n=binom(n+3,3) for all n≥2. In particular S/J has Krull dimension four.

Choose a homogeneous minimal prime P of J with dim(S/P)=4. Such a prime exists by the dimension of S/J. It has height one in the polynomial UFD S, hence P=(p) for a homogeneous irreducible polynomial p. The nonzero quadrics in Q are divisible by p, so deg p≤2. If deg p=2, then Q⊂(p)_2=Cp would have dimension at most one, a contradiction. Therefore p=ℓ is linear. Since Q⊂J⊂(ℓ), we obtain Q⊂ℓT. Both spaces have dimension five, proving equality. This reasoning neither assumes saturation nor excludes embedded components by fiat.

The only general Hilbert-function results used here are Macaulay's theorem and Gotzmann persistence; see Juan C. Migliore, The Geometry of Hilbert Functions, Theorems 2.6 and 2.11, especially the generation hypothesis preceding Theorem 2.11:
https://academicweb.nd.edu/~jmiglior/Hilb.pdf

## 2. What the optional syzygy summand would force

Fix a basis e_1,…,e_5 of E. Under the identification E⊗Sym²W→S_2, write α_i,β_i,γ_i for the images of e_i⊗x²,e_i⊗xy,e_i⊗y² respectively. These fifteen quadrics form a basis of S_2. The ten quadratic relation columns are therefore

r_i(x)=−β_i x+α_i y,
r_i(y)=−γ_i x+β_i y.

Suppose r=15. Let F:A⊗W→T⊗E denote the equivariant inclusion of its A⊗W summand. Tensoring with W, the unique A⊗U′ summand of T⊗L_2 is the image of A⊗Sym²W under F⊗id_W. By multiplicity one it is precisely the assumed linear syzygy space.

For each a∈A put u=F(a⊗x) and v=F(a⊗y), regarded as five-component columns of linear forms. The symmetric-square inclusion means that the following three elements of (T⊗E)⊗W are syzygies:

u⊗x,  v⊗y,  u⊗y+v⊗x.

Here the symbols x,y in the final factor index the two quadratic relation columns, not multiplication by coordinate variables. Applying the relation map to the first two syzygies gives

u·α=u·β=0,  v·β=v·γ=0.

Applying it to the mixed syzygy gives

u·γ+v·β=0,  u·β+v·α=0.

It follows that u·γ=v·α=0 as well. Thus every vector in the ten-dimensional subspace image(F)⊂T⊗E is simultaneously a linear syzygy of each of the three columns α,β,γ. These equations are universal tensor coefficient identities; no actual polynomial coefficients have been evaluated.

## 3. Contradiction from three extremal quadratic spaces

For each of the three columns, the map E→S_2 is injective, since the full fifteen-entry array is a basis. Its image Q_α, Q_β or Q_γ has dimension five, and T⊗E identifies with T⊗Q for that column. Section 2 places the same ten-dimensional image(F) inside each corresponding multiplication kernel. The lemma implies that each kernel has exactly dimension ten and

Q_α=ℓ_α T,  Q_β=ℓ_β T,  Q_γ=ℓ_γ T

for nonzero linear forms ℓ_α,ℓ_β,ℓ_γ.

Set B=span(ℓ_α,ℓ_β,ℓ_γ)⊂T, so dim B≤3. All fifteen basis quadrics would then lie in BT. But the natural quotient S_2→Sym²(T/B) has kernel BT, hence

dim(BT)=15−binom(6−dim B,2)≤12.

This contradicts their spanning all fifteen dimensions of S_2. Therefore r=15 is impossible and r=0.

## 4. Consequences and remaining questions

The full minimal Betti family of H from PR483 specializes to

F_0=2S,
F_1=10S(-2),
F_2=20S(-4)+sS(-5),
F_3=sS(-5)+20S(-6),
F_4=10S(-8),
F_5=2S(-10),

with s∈{0,1} still unresolved. No cancellation of equal-degree free summands is used. The cubic relations and cubic second syzygies vanish because the alternative has been structurally excluded.

Let D=Fitt_0(H). Its presentation now has only quadratic entries. By the definition of Fitt_0 for a two-generator module, D is generated by the two-by-two minors of this quadratic presentation, all in degree four. PR495 determines D_4=V⊗(Q_spin⊕U), of dimension35, and already proves that the only possible extra generators had degree five. Therefore the previously unresolved parameter c∈{0,24,48} is exactly zero, and D=(D_4).

This also resolves the sole parameter in the full adjoint-module resolution of PR487. With K_j=H¹(End_0(F)(j−1)), its minimal free modules are now exactly

F_0(K)=5S,
F_1(K)=S(-1)⊕15S(-2),
F_2(K)=10S(-4)⊕10S(-6)⊕60S(-7)⊕25S(-8),
F_3(K)=2S(-6)⊕140S(-8)⊕75S(-9),
F_4(K)=80S(-9)⊕75S(-10),
F_5(K)=32S(-11).

This is substitution into the already exhaustive family of PR487, not a new assertion about the matrices of its differentials. Similarly PR492 forces q=0 for the scalar algebra, but its parameters u and v are not selected here.

This determines the minimal generating degrees of D, not all its higher syzygies. It also does not decide the scalar middle parameter s, the original fixed-pair/source quotient, higher-order lifting, or algebraicity.

## Exact dependencies and verification status

- PR487, the exhaustive adjoint-module Betti family:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/78ac933a94e1f0440de8e485f80dc669d222d142/research/hm/complete-adjoint-betti/PROOF.md
- PR492, the canonical cubic relation parameter:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/720d25905320ffcbcd5433c6f61a92b2634afef8/research/hm/scalar-betti-family/PROOF.md
- PR483, the cubic alternatives and full H Betti family:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/e2ec3f19519b314ca119fb0f60ad9f41ed12af90/research/hm/dual-betti-family/PROOF.md
- PR479, the multiplicity-one decomposition T⊗E and the optional syzygy representation:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/b57cf851bb244706acfe6c6485d4dfa54ceb6519/research/hm/quadratic-shadow-exclusion/PROOF.md
- PR490, the canonical quadratic inclusion (Section 3):
  https://github.com/Akilleez-QA/read-em-and-weep/blob/1c5ad353bb5f1808150f64cde3c29b92c6e13d91/research/hm/dual-tensor-bridge/VERIFICATION.md
- PR495, the quartic Fitting space and former quintic alternatives:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/b972aa22b72658b419e2c8948a56e0eec7f59e13/research/hm/fitting-thickening/PROOF.md

This is an authored structural proof with independent and root mathematical reviews, conditional on the pinned inputs; it is not formally checked by a proof assistant. No selected actual HM/source-instance evaluation, numerical matrix or rank computation, coefficient search, or large computation was used.
