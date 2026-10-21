# Excluding the constant fifteen-dimensional column strand

## Claim and inputs

The constant alternative u=15 in the column family is impossible. Combined with the low-degree parameter-kernel vanishing and jump exclusion, this yields the necessary classification: u is constant in {0,5,10}, or u is zero away from the unique twelve-point orbit and five on that orbit.

This note depends on [PR523, commit d02ae6cb6d324bad2b858c6969ed4ce8d43b5e42](https://github.com/Akilleez-QA/read-em-and-weep/blob/d02ae6cb6d324bad2b858c6969ed4ce8d43b5e42/research/hm/column-kernel-vanishing/PROOF.md), specifically:

1. The reduced map phi:C tensor O -> 10O(2), with C=U+R6 as an actual G=SL(2,F5) representation.
2. K=ker(phi) has no sections after twisting by O(2), so every splitting summand is O(-d) with d>=3.
3. All nonconstant rank behavior has generic u=0 and exceptional u=5. Thus u=15, if it occurs, is constant.

It also uses PR521, commit 7f69d421d66038d2c55d20b1997aa818c98d29bd, research/hm/column-jump-orbits/PROOF.md, for the family map and its generic-rank relation r=9-u/5. The representation table is Horrocks--Mumford (1973), Section 2.2, with binary symmetric-power identities from Section 3.3, as pinned in PR453, commit 56516a96a7eacfde0c8e272ca38db415cc7f294b, research/hm/cubic-invariant-target/PROOF.md. The representations U and R6 have dimensions three and six and central parities even and odd respectively. The only one-dimensional representation of G is trivial. Its two-dimensional irreducibles W0,W' are odd, and its three-dimensional irreducibles U,U' are even. Sym^3(W') and Sym^4(W') are irreducible of dimensions four and five respectively, so neither contains U or R6.

These are representation and bundle arguments, without a selected column evaluation or numerical rank calculation.

## Equivariant splitting principle

A G-equivariant bundle on P1 admits an equivariant version of its splitting by degrees:

K = direct sum_d M_d tensor O(-d),

where each M_d is a genuine G representation and O(-d) has its standard linearization. To justify the claim, split the ordinary degree filtration. It is G-stable, and any ordinary splitting of each split exact sequence can be averaged over the finite group to obtain an equivariant splitting. For a same-degree block, twisting by O(d) gives an equivariant trivial bundle; its global sections form the representation M_d and evaluation is an equivariant isomorphism. Since G is perfect, the standard line-bundle linearization has no nontrivial character ambiguity.

A one-dimensional block in degree d=3 or d=4 has no nonzero equivariant map to C tensor O: such a map would be an invariant in C tensor Sym^d(W'), and the stated irreducible symmetric powers contain neither U nor R6. Consequently no rank-one same-degree block at degree three or four can occur in K.

## Exhaustion at constant u=15

Suppose u=15. Then r=6, rank K=3, and J=im(phi) is a subbundle of 10O(2). The constant-rank sequence

0 -> K -> C tensor O -> J -> 0

is exact in vector bundles. Thus -deg K=deg J<=12. Every splitting degree of K is at least three. The only nondecreasing triples are

(3,3,3), (3,3,4), (3,3,5), (3,3,6), (3,4,4), (3,4,5), (4,4,4).

The triples (3,3,4), (3,4,4), (3,4,5) have a rank-one block in degree three or four and are already impossible.

### Triple (3,3,3)

The multiplicity representation M_3 has dimension three. If reducible, it has a one-dimensional trivial summand, since G has no nontrivial one-dimensional representations and the only smaller nontrivial irreducibles have dimension two. That trivial summand would give a forbidden degree-three line map. Thus M_3 is one of the even three-dimensional irreducibles.

Because O(-3) has odd central parity, the entire block K has odd parity and its map to C=U+R6 lands in R6 tensor O. Since K is a subbundle of C tensor O, the quotient (R6 tensor O)/K is a vector bundle. It has rank three and degree nine. It is a direct summand of J, hence a subbundle of 10O(2). But any rank-three subbundle of 10O(2) has degree at most six: each splitting summand has degree at most two. Contradiction.

### Triple (4,4,4)

The same reducibility argument makes M_4 an even three-dimensional irreducible. The entire block K is now even, so its map lands in U tensor O. Both bundles have rank three. Since K is a subbundle of C tensor O, their quotient must be locally free; it has rank zero and hence is zero. This would identify K with U tensor O, contradicting deg K=-12.

### Triple (3,3,5)

The dimension-two representation M_3 cannot contain a trivial line, so it is an odd two-dimensional irreducible. Combining its parity with O(-3), this block maps entirely to U tensor O. The dimension-one degree-five block is trivial as a multiplicity representation and maps entirely to the odd summand R6 tensor O. Therefore J decomposes as the direct sum of the two quotients. The first quotient

(U tensor O)/(M_3 tensor O(-3))

is a line bundle of degree six, since K is a subbundle and the two maps land in the separate parity summands. It embeds in 10O(2), which is impossible: Hom(O(6),O(2))=0.

### Triple (3,3,6)

Again the degree-three rank-two block has even total parity and maps into U tensor O. The degree-six line block also has even total parity and maps into U tensor O. Thus all of K maps into U tensor O, with both ranks three. Constant rank again forces an isomorphism, contradicting deg K=-12.

Every possible splitting type has been excluded. Hence the constant alternative u=15 cannot occur.

## Scope

This is a uniform structural exclusion, conditional on the preceding kernel vanishing proof and the pinned representation inputs. It does not identify the actual remaining constant value or prove the exceptional orbit occurs. It does not compute a selected HM/source multiplication matrix, perform a coefficient search, or establish original fixed-pair residual vanishing, higher-order lifting, or algebraicity. Status: authored proof requiring independent review, not formally checked.
