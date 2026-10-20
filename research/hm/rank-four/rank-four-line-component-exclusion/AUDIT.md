# Independent audit: rank-four line-component exclusion

## Verdict

PASS, conditional on the explicitly imported rank-locus and degree hypotheses. The argument proves that every projective line with normalizer orbit of size at most 125 either is a canonical odd reflection line or intersects one. Consequently an invariant rank-four locus of dimension at most one, with reduced curve degree at most 125 and disjoint from the canonical lines, contains no line.

No correction to PROOF.md is required. This audit independently checks the new group, representation, cocycle, intersection, and degree-counting deductions. It does not claim a new proof of the imported global degree bound or the canonical rank-at-least-five theorem.

## 1. Exhaustion of translation stabilizers

The translation group A is a two-dimensional vector space over F_5. Its subgroups have orders 1, 5, or 25. A projectively A-stable line corresponds to a vector two-space preserved by every linear Heisenberg lift: scalar choices cannot affect subspace preservation. Thus the order-25 case contradicts irreducibility of the five-dimensional Schrödinger representation. No intermediate stabilizer order is omitted.

For an order-five stabilizer, SL_2(F_5) is transitive on the one-dimensional subspaces of A. Conjugating to the Z axis is legitimate. A Z-invariant vector subspace is a direct sum of its distinct eigenlines, since the five eigenvalues are simple. A two-space is therefore exactly span(e_i,e_j) for distinct indices.

## 2. Explicit negative reflection point on an axis-pair line

Write s=i+j and a=(s/2,0), with arithmetic in F_5. The Weyl representative W_a is simply X^(s/2), so there is no scalar phase in the calculation

    R_a = W_a R W_a^(-1) = X^s R.

On a basis vector, R_a e_k=e_(s-k). It is an actual involution. The unique fixed basis index is k=s/2, and the remaining four basis indices form two swapped pairs. Its trace is therefore one and its negative eigenspace has dimension two. In particular,

    R_a e_i=e_j,
    R_a e_j=e_i,
    R_a(e_i-e_j)=-(e_i-e_j).

The nonzero vector e_i-e_j lies on the axis-pair line and in W_a W. This proves the claimed intersection with the canonical odd line, with the correct negative sign and normalization. It works for every distinct i,j, including a pair containing zero or a pair with i+j=0. It requires no orbit bound.

## 3. Exhaustion of subgroup indices in the free case

When A_L=1, projection sends K=N_L injectively into G; writing H for the image gives |K|=|H|. Since |N|=25|G|, the orbit formula is exactly

    |N L|=25[G:H].

The bound 125 therefore gives indices m in {1,2,3,4,5}. For m=2,3,4 the coset action is nontrivial and transitive. Its image is perfect because G is perfect, but is a subgroup of the solvable group S_m, hence solvable. A nontrivial finite group cannot be both perfect and solvable. All three indices are excluded.

At m=5, perfectness kills the sign character, placing the image in A_5. A nontrivial perfect subgroup of A_5 must be A_5, as its proper subgroups are solvable. The image has order 60, so the kernel has order two. SL_2(F_5) has exactly one nonidentity involution: an element with square I is diagonalizable over F_5 with eigenvalues ±1, and determinant one forces it to be I or -I. Hence the kernel is the center. The preimage of the stabilizer of the coset H is H itself, and its image is an A_4 point stabilizer. This proves that H has order 24 and contains z=-I. Index one gives H=G. There are no other cases under the stated bound.

## 4. Cocycle removal in both surviving cases

The trivial intersection K intersect A makes K the graph of a cocycle on H. For either H=G or the order-24 subgroup, centrality of z and its action -I on A yield

    c(zh)=c(z)-c(h),
    c(hz)=c(h)+h c(z),
    2c(h)=(1-h)c(z).

With a=c(z)/2, this is c(h)=a-ha. In the semidirect product, conjugation of (0,h) by (a,1) gives (a-ha,h), exactly the required graph. Thus K=aHa^(-1), with the stated sign. Conjugating L by a^(-1) makes its vector two-space invariant under the canonical H. Division by two is legitimate in F_5. This proof applies even though |G| is divisible by five and does not assume a coprime-order splitting theorem.

## 5. Restriction and uniqueness checks

The honest linear representations and the normalized central action used here are available from the earlier parity proof, Sections 1–2, together with the canonical splitting proof. This matters: the assertions about characters and one-dimensional representations concern that honest lift, not unspecified projective lifts.

For H=G, the imported uniqueness of the invariant two-space W applies directly. It also follows from the irreducibility of T and W, dimensions three and two, and the distinct central eigenvalues.

For |H|=24, T factors through A_5 and is faithful: its kernel is normal in the simple group A_5, and T is nontrivial. A_4 has three one-dimensional irreducibles and one three-dimensional irreducible, as follows from its four conjugacy classes, abelianization C_3, and the sum-of-squares formula. If the three-dimensional restriction T|A_4 were reducible, it would be a sum of characters. Every such character is trivial on the Klein four subgroup, contradicting faithfulness. Thus T|H is irreducible.

For W|H, choose lifts x,y of two different nonidentity Klein-four elements. Each has square z: its square lies in {1,z}, while square one would force it to be 1 or z and have trivial image. Their commutator lies in {1,z}. If they commuted, (xy)^2=z^2=1, although xy has nontrivial Klein-four image, a contradiction. Therefore their commutator is z, proving z belongs to [H,H]. Every character of H sends z to 1. Since z acts on W as -I, semisimplicity rules out a decomposition of W into two characters. Hence W|H is irreducible.

Finally, invariance under the central reflection makes any candidate U split into its intersections with T and W. Both intersections are H-invariant. The irreducible three-space T cannot contribute to a two-space, and the irreducible two-space W can contribute only zero or all of W. Thus U=W. In particular the index-five candidate actually has the larger canonical stabilizer after conjugation; there is no free-A line orbit of size exactly 125.

## 6. From orbit size to exclusion in the rank locus

N-equivariance takes any line in Z_4 to another line in Z_4. The assumed dimension bound dim Z_4<=dim Z_5<=1 ensures that each such line is an irreducible component of the reduced curve part Gamma_4. Distinct orbit lines are distinct components, each of degree one. Hence their number is at most deg Gamma_4, irrespective of possible intersections, scheme multiplicities, or isolated points. The imported degree bound gives the needed orbit bound of 125.

The orbit classification then makes the original line either canonical or intersect a canonical line. Both alternatives contradict the imported set-theoretic disjointness of Z_4 from every canonical odd line. The desired conclusion follows. A positive-dimensional irreducible projective component of degree one is a line, so every remaining curve component has degree at least two.

## Scope and verification boundary

The proof does not exclude conics, higher-degree curves, or a nonempty Gamma_4, and does not independently improve any compatible-fiber bound. The supplied artifacts correctly state these limits.  It performed no actual source-map evaluation, selected-source-input evaluation, numerical tensor experiment.
