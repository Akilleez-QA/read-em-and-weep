# Independent audit: integral-quadric polar rank-drop exclusion

## Verdict

The classification and compatible-threefold exclusion in `PROOF.md` are correct over C. The Jordan cases are exhaustive, and the argument controls both a threefold over the rank-drop quadric and a dominant graph. No new computation or external/source operation is needed.

## 1. Cofactors and primitive linear kernel

Generic rank three ensures at least one nonzero cubic maximal minor. An integral quadric component has an irreducible homogeneous equation f, which divides every minor. The gcd therefore has degree two or three. Degree three makes the primitive cofactor vector constant; its kernel identity gives B_i(a,c)=0 for all a and i, hence a common radical vector. Degree two gives a linear vector Ta. Rank one would make all its entries multiples of one linear form, contradicting primitiveness. Thus rank T is two, three, or four. In particular there is no omitted rank-zero or rank-one case.

The identity B(a,Ta)=0 polarizes to T^t B+BT=0. The rank-three symmetrizer lemma applies to this space of forms because the operator on forms is the transpose of the symmetric-square operator on vectors; their kernel dimensions agree. It is not necessary to identify their kernel vectors directly.

## 2. Exhaustiveness of the Jordan cases

For rank three, the zero generalized eigenspace has exactly one Jordan block J_k. Its contribution to the kernel on symmetric squares is 1 for k=1,2 and 2 for k=3,4. The nonzero generalized eigenspaces contribute only opposite-eigenvalue pairings. The only way to reach dimension three is k=1 and semisimple nonzero spectrum (lambda,lambda,-lambda). This gives the stated net and reducible gcd zw.

For rank two, let d be the total dimension of the nonzero generalized eigenspaces. Their contribution to the rank is d, so d is 0, 1, or 2:

- d=1: the zero part has dimension three and rank one, necessarily J2 plus J1. There is no opposite nonzero eigenvalue; every invariant form annihilates the nonzero eigenspace. This violates the common-radical hypothesis.
- d=2: the zero part is a semisimple two-plane. The nonzero part contributes invariant pairings only when its eigenvalues are lambda and -lambda. Repeated nonzero eigenvalues, including a nontrivial J2 block, contribute none. The surviving opposite pair is necessarily semisimple, giving Sym²U* plus C(yz).
- d=0: the rank-two nilpotent partitions of four are precisely (3,1) and (2,2).

For J3 plus J1, applying x1 partial_x0+x2 partial_x1 to a general quadric leaves exactly span{x1²-2x0x2,x2²,x2x3,x3²}. For J2 plus J2, the derivation x1 partial_x0+x3 partial_x2 leaves exactly span{-x0x3+x1x2,x1²,x1x3,x3²}. Thus the listed invariant spaces are exhaustive. In each of these cases, and in the nonnilpotent opposite-pair case, a generically rank-three net has two binary-quadratic rows and one remaining row. Expanding the minors along the binary rows gives their binary Jacobian determinant times Ta, up to a common nonzero scalar. Since Ta is primitive, this determinant is exactly the cofactor gcd. It is a nonzero binary quadratic and hence reducible over C.

For rank four, the sum of products of opposite eigenvalue multiplicities can reach three only for a single opposite pair of multiplicities (3,1) or (2,2). Two distinct opposite pairs with multiplicities (1,1) contribute only two. In the (3,1) case, retaining dimension three requires the entire three-space to have trivial nilpotent part. In the (2,2) case, one nontrivial J2 block or two nontrivial J2 blocks give kernel dimension two, so dimension at least three again forces semisimplicity. The (3,1) gcd is a square; balanced (2,2) is the sole survivor.

A nonzero complementary cross tensor in the balanced case has rank one or two, exhaustively. Rank one yields the product gcd p2q2; rank two yields the normal form in the proof. Thus no singular-T or nonsemisimple-T branch survives the integral-quadric hypothesis.

## 3. Exact geometry of the surviving net

The displayed matrix has cofactor vector f(p,q)(p,-q), up to one overall sign, where f=p1q1+p2q2. Since (p,-q) never vanishes projectively, the entire set-theoretic rank-drop locus is exactly V(f), with no extra components. Its gradient is (q1,q2,p1,p2), which has no projective zero, so this quadric is smooth.

Rank is at least two everywhere: for p1 nonzero, the first two rows restricted to the Q columns have determinant p1²; for p2 nonzero, the first and third rows give determinant p2² up to sign. If p=0, the analogous P-column checks use q1 or q2. Hence rank is exactly two throughout D. The kernel over D is a rank-two vector bundle, so its projectivization is an integral projective threefold. At each point of P(P), the kernel is exactly P, not merely a subspace containing the first factor; the analogous assertion holds for Q.

## 4. Boundary completeness of the threefold exclusion

For rigor, interpret an ordered compatible threefold as the projective closure of an integral three-dimensional locus of independent compatible factors. Both membership ab in K and the wedge compatibility identity are polynomial and persist on that closure. The diagonal does not create a spurious threefold, since the original locus is generically off it.

A surface first-factor image lies in D by generic fiber dimension. Since D is integral and two-dimensional, that image equals D. The closure of the threefold is then a closed integral subvariety of the integral three-dimensional partner bundle of the same dimension, and therefore is the entire bundle. This justifies specializing to all of P(P) times P(P), including boundary fibers. On independent pairs in P the wedge identity says v(eb) lies in P. These products span Sym²P (alternatively their dense open subset forces the linear map to E/P to vanish). Thus v(Sym²P) is contained in P. The binary cubic e wedge v(e²) has a projective zero over C, also when identically zero, contradicting square avoidance.

If the first-factor image is all of P(E), the unique generic partner is Ta. The polynomial identity v(aTa) wedge a wedge Ta=0 holds identically because aTa belongs to K for every a. At a=e in P, differentiate in q in Q. Since Te=e and Tq=-q, the result is -2 v(e²) wedge e wedge q=0. Two independent Q directions force v(e²) to lie in Ce. This independently excludes the dominant graph.

The cited finite-partner-plane lemma excludes point and curve images without a genericity assumption on W. Consequently all possible image dimensions have been covered. Any larger-dimensional compatible component has an integral three-dimensional subvariety meeting its independent-factor open locus. Finally, multiplication of independent projective factors into rank-two symmetric tensors is finite (the two factors are recovered up to order), so the ordered bound transfers to the tensor locus.

## Minor editorial suggestion

The last sentence of the preceding boundary discussion could be incorporated into the main proof to make its use of projective closures explicit. This is a clarification, not a mathematical gap. No correction to the theorem or classification is required.

## Additional corollary: a dominant-dominant threefold has cofactor gcd degree at most one

This corollary does not require an integral quadric component of D. Assume generic polar rank three and an integral compatible ordered threefold dominating both copies of P(E). If the cubic maximal-minor gcd has degree three, its primitive kernel vector is constant, so the second factor is constant, contradicting dominance. If its degree is two, the primitive kernel is Ta for a linear map T. Dominance of the second factor forces rank T=4. The invariant-form identity still gives W contained in I_T, and dim I_T at least three. The rank-four classification above, which did not use irreducibility of the gcd, forces T to be semisimple with opposite eigenvalues and multiplicities (3,1) or (2,2).

Rescale T so the eigenvalues are +1 and -1. In the (3,1) case, choose nonzero e in the one-dimensional eigenspace and take two independent directions q1,q2 in the opposite three-dimensional eigenspace. In the (2,2) case, choose nonzero e in either eigenspace and take a basis q1,q2 of the opposite eigenspace. For a generic first factor a, the unique partner is Ta, so compatibility extends to the polynomial identity v(aTa) wedge a wedge Ta=0 for all a. Also aTa belongs to K identically. At a=e, this implies e² belongs to K, and differentiation in each qi gives a nonzero scalar multiple of v(e²) wedge e wedge qi=0. The intersection of span(e,q1) and span(e,q2) is Ce. Therefore v(e²) belongs to Ce, contradicting square avoidance.

Thus every remaining compatible threefold with factor-image dimensions (3,3) must have maximal-minor gcd of degree zero or one. This includes and excludes all reducible degree-two gcd cases as well as irreducible ones; no assertion about the remaining degree-zero/one cases follows without additional work.
