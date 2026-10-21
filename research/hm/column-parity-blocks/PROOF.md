# A square degree-twelve determinant controls the column kernel

## Inputs and conventions

Work over C. Let P=P(W'^*) parameterize columns, let G=SL2(F5), and use the actual normalizer representation extensions. Write T=V*, A=theta V, E=A*, U=Sym2 W0, U'=Sym2 W', Qspin=Sym3 W0=Sym3 W', and T4=W0 tensor W'. The reduced column Koszul map is denoted phi.

The exact dependencies are:

- [PR523, commit d02ae6cb6d324bad2b858c6969ed4ce8d43b5e42](https://github.com/Akilleez-QA/read-em-and-weep/blob/d02ae6cb6d324bad2b858c6969ed4ce8d43b5e42/research/hm/column-kernel-vanishing/PROOF.md): phi has source (U+R6) tensor O; the genuine G-action is obtained using Hom_Gamma(V,-); its kernel K has H0(K)=0; the residual parameter satisfies u=5 dim ker(phi) fiberwise.
- [PR521, commit 7f69d421d66038d2c55d20b1997aa818c98d29bd](https://github.com/Akilleez-QA/read-em-and-weep/blob/7f69d421d66038d2c55d20b1997aa818c98d29bd/research/hm/column-jump-orbits/PROOF.md): the target before taking multiplicities is E tensor Lambda2 T tensor O(2), and every nonempty invariant divisor on P has degree at least twelve; the unique degree-twelve invariant divisor is the reduced orbit Omega.
- [PR453, commit 56516a96a7eacfde0c8e272ca38db415cc7f294b](https://github.com/Akilleez-QA/read-em-and-weep/blob/56516a96a7eacfde0c8e272ca38db415cc7f294b/research/hm/cubic-invariant-target/PROOF.md): the representation identities T tensor A=V tensor (U'+W0) and E tensor E=V tensor (U+W').

The public primary source for the representation conventions is [Horrocks--Mumford (1973), Lemma 3.3 and the appendix](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf). In particular Lambda2 T=E tensor W0, U tensor W0=W0+Qspin, and Sym^d W' for d=0,1,2,3,4 is respectively 1,W',U',Qspin,J5. These irreducibles do not contain U.

## 1. Genuine parity blocks

The target multiplicity representation is determined by

E tensor Lambda2 T = (E tensor E) tensor W0
= V tensor ((U+W') tensor W0)
= V tensor (W0+Qspin+T4).

Thus phi is a genuine G-equivariant map

(U+R6) tensor O -> (W0+Qspin+T4) tensor O(2).

The central involution of G acts trivially on P and as +1 on O(2). It acts as +1 on U and T4, and as -1 on R6,W0,Qspin. Therefore phi is the direct sum of maps

alpha: U tensor O -> T4 tensor O(2),
beta: R6 tensor O -> (W0+Qspin) tensor O(2).

This is the eigenspace decomposition of the actual central involution, not a choice of an equivariant structure on ordinary bundles.

## 2. The even block is injective at every point

The block alpha is nonzero: if it were zero, its constant source U would give nonzero global sections of K, contrary to PR523. Let r be its generic rank, so 1<=r<=3. Every r-minor is a section of O(2r). The common maximal-rank determinantal divisor is G-invariant and has degree at most 2r<=6. It is empty because every nonempty invariant divisor has degree at least twelve. Hence alpha has constant rank r.

Suppose r=1. Its image is a line bundle O(d). It is globally generated as a quotient of U tensor O, so d>=0. Its injection into 4O(2) implies d<=2. The equivariant quotient U tensor O -> O(d) gives a nonzero intertwiner U -> H0(O(d))=Sym^d(W') (up to dual, which has the same irreducible character). Since U is irreducible, it would occur in that symmetric power. It does not occur for d=0,1,2, a contradiction.

Suppose r=2. The kernel is a line bundle O(-d). If J is the rank-two image, exactness gives deg J=d. It is globally generated, so d>=0; and it injects into 4O(2), so d<=4. The equivariant inclusion O(-d) -> U tensor O requires a nonzero invariant in U tensor H0(O(d)), hence the occurrence of U* in Sym^d(W'). This is impossible for d=0,1,2,3,4.

For both arguments, G-line bundle linearizations differ from the standard ones only by characters: the ratio is an invertible global function for each group element. The group G is perfect and therefore has no nontrivial characters. There is consequently no omitted linearization twist in the representation obstruction.

It follows that r=3. Thus alpha is injective on every fiber and its line cokernel has degree eight:

0 -> U tensor O -> T4 tensor O(2) -> O(8) -> 0.

The degree is eight, not six, since deg(T4 tensor O(2))=4 times 2. This is consistent with the equivariant quotient: Sym6(W') contains T4.

## 3. The odd square block is the only unresolved column map

Since alpha is injective on every fiber,

ker(phi)=ker(beta),
u(lambda)=5 dim ker(beta_lambda).

The map beta has rank-six source and target. Its determinant is a section of O(12). The determinants of the coefficient representations are characters of the perfect group G and hence trivial, so this section is an invariant binary form.

If det(beta) is nonzero, its zero divisor is exactly the reduced degree-twelve orbit Omega. Smith normal form at each point of that divisor shows that beta has corank one there and is invertible elsewhere. In this case the actual column parameter is zero outside Omega and five at its twelve points.

If det(beta) vanishes identically, this argument alone does not determine its generic rank or the surviving constant value of u. In particular this note does not infer nonvanishing from the existence or multiplicity one of an invariant of degree twelve.

The entire multiplicity cokernel also splits as

coker(phi) = O(8) direct sum coker(beta),

because phi is the direct sum of its parity blocks. Thus the fixed rank-one part of the cokernel is explicitly separated from the odd square-map defect. Restoring the five-dimensional Heisenberg factor tensors these identities by V.

## Scope and verification status

This is an authored structural reduction requiring independent mathematical review, conditional on the exact pinned inputs. No selected column, actual source-instance multiplication matrix, coefficient search, numerical rank computation, or large computation is used. The generic rank of beta and its determinant's nonvanishing remain unproved here. Original fixed-pair residual, higher-order lifting and algebraicity are separate unresolved questions. The argument has not been formally checked by a proof assistant.
