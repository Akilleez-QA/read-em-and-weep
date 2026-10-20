# No line components in the rank-at-most-four locus

## Statement and dependencies

Use the Schrödinger representation V of H_5, A=H_5/Z(H_5)=F_5^2, and N=A semidirect G, G=SL_2(F_5), with its standard action on A. Use the N-equivariant residual rank loci Z_j and the decic-closure hypotheses and audited degree bound

    dim Z_5 <= 1,    deg Gamma_4 <= 125,

where Gamma_4 is the reduced curve part of Z_4. Import the theorem of ../canonical-line-rank-five-strengthening/PROOF.md: all twenty-five canonical odd reflection lines are disjoint from Z_4. Import also the exact splitting and reflection formulas of ../rank-three-line-rank-constancy/PROOF.md Sections 2, 3, 7, 8. In particular V=T direct sum W has positive and negative reflection eigenspaces of dimensions three and two, and they carry the standard irreducible representations of A_5 and binary A_5, respectively, as used in the canonical-line parity proof.

**Theorem.** Z_4 contains no projective line. In particular every irreducible component of Gamma_4 has degree at least two.

We prove a slightly more general orbit statement: any line whose N-orbit has at most 125 elements either is canonical or meets a canonical line. This is enough because an N-invariant closed set disjoint from all canonical lines cannot contain such a line.

## 1. The possible A-stabilizers

Let L=P(U) be a projective line and A_L its stabilizer. Its order is 1, 5, or 25. The last case is impossible: an A-invariant vector subspace is invariant under the irreducible Schrödinger representation of H_5, whereas dim U=2.

## 2. A line stabilized by an axis meets a canonical odd line

Suppose |A_L|=5. By G-conjugation take its axis to be generated projectively by Z, where Z e_k=zeta^k e_k. Its five eigenvalues are distinct, so U=span(e_i,e_j) for distinct i,j in F_5.

Let R e_k=e_{-k} and choose a=((i+j)/2,0) in A. The normalized conjugate reflection is

    R_a=W_a R W_a^{-1}=X^{i+j} R.

It satisfies R_a^2=I, has trace one, and its negative eigenspace has dimension two. It swaps e_i and e_j exactly. Hence e_i-e_j belongs to U and to the negative eigenspace of R_a. Thus L meets the canonical odd line P(W_a W).

This argument needs no orbit-size bound, and avoids ambiguity from scalar normalization: the displayed representative is an actual involution with the canonical trace-one normalization.

## 3. A small free A-orbit reduces to index one or five

Now suppose A_L=1. Let K=N_L and let H be its image under N->G. The projection K->H is an isomorphism. Its N-orbit has size

    [N:K]=25 [G:H].

If that size is at most 125, m=[G:H] is at most five. Values two, three and four are impossible: the transitive coset action would give a nontrivial perfect subgroup of the solvable group S_m, whereas G is perfect. Thus m=1 or m=5.

For m=1, K is a complement. The cocycle calculation in the imported proof conjugates it by A to G. The unique G-invariant 2-space is W, so L is canonical.

For m=5, the coset image of G lies in A_5 by perfectness. Every proper subgroup of A_5 is solvable, so the nontrivial perfect image is all of A_5. Its kernel has order two and is the center <z>. Consequently H contains z and is the inverse image of an A_4 point stabilizer in G/<z>=A_5. In particular H has order 24.

## 4. Removing the translation part over H

Write K as the graph of a cocycle c:H->A in the canonical semidirect product. Since z is central in H and acts as -I on A, comparison of c(zh) and c(hz) gives

    2c(h)=(1-h)c(z).

Set a=c(z)/2. Then c(h)=a-ha, so K=a H a^{-1}. After replacing L by a^{-1}L, its vector 2-space U is invariant under the canonical H.

No coprime complement theorem is used: although 5 divides |G|, this central-involution argument applies directly to both H=G and the order-24 subgroup.

## 5. The unique H-invariant 2-space is W

We verify the restriction facts rather than assume them. The positive representation T factors through A_5 and is faithful, since it is nontrivial and A_5 is simple. Its restriction to A_4 remains irreducible. One elementary proof is as follows. A_4 has three one-dimensional complex representations and one three-dimensional irreducible representation: its abelianization is C_3, it has four conjugacy classes, and the sum of squares of irreducible dimensions is twelve. If T restricted to A_4 were reducible, it would therefore be a sum of one-dimensional representations. Its Klein four subgroup would act trivially, contradicting faithfulness.

The negative representation W remains irreducible on H. Indeed z belongs to [H,H]. To see this, lift two distinct nonidentity elements of the Klein four subgroup of A_4 to x,y in H. Their squares are z because z is the unique involution in SL_2(F_5). Their commutator lies in <z>, since their images commute. If x and y commuted, then (xy)^2=x^2y^2=1; but xy projects to the third nonidentity element of that Klein four subgroup, impossible because the only elements with square one are 1 and z. Thus [x,y]=z. Every one-dimensional representation of H consequently sends z to +1. A decomposition of W into one-dimensional representations would contradict that z acts as -I on W.

Finally, the normalized central reflection R commutes with H and acts as +I on T and -I on W. Any invariant 2-space U splits as

    U=(U intersect T) direct sum (U intersect W).

Irreducibility of T|H and W|H forces U=W. Thus the m=5 candidate is again canonical. In fact its true stabilizer is larger, so no line has an N-orbit of exactly 125 elements with free A-action.

## 6. Apply the degree bound

If a line L lay in Z_4, every member of its N-orbit would also lie in Z_4. Because dim Z_4<=dim Z_5<=1, these distinct lines are irreducible components of Gamma_4. Hence the number of orbit lines is at most deg Gamma_4<=125.

Sections 1--5 imply that L either is canonical or meets a canonical odd line. Both alternatives contradict the imported disjointness of Z_4 from all canonical odd lines. Therefore Z_4 contains no lines and all its curve components have degree at least two.

This does not prove that Gamma_4 is empty, exclude conics or higher-degree components, or improve the rank-four compatible-fiber bound by itself. No actual source map or selected source input was evaluated; the proof uses only the abstract normalizer representation and the imported rank/degree theorems.
