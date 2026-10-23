# The pure-V source2 quotient has a reduced twelve-point rank-drop divisor

## Theorem

Over C retain the source2 actual-source/normal-form hypotheses of the exact
PR790, PR792 and PR795 proofs in INPUTS.json, every balanced endpoint H_t,
and either residual coupling class. Let j be any nonzero pure-V radical
endomorphism and I=im(j). With the original fixed pencil variables, put
barN=N/I, of dimensions(36,48,33). Then:

1. Its first arrow barA_l has rank36 off the reduced invariant orbit D12,
   and rank35 precisely at D12. Here l is identified with its zero in P(W)
   using the fixed symplectic convention. The maximal-minor degeneracy
   scheme of the universal first arrow is exactly reduced D12, not merely
   its set of points. The common kernel of all barA_l is zero.
2. Every nonzero second arrow barB_l is onto the 33-dimensional last space.
3. The endpoint quotient L=NC/I is the genuine torsion evaluation pencil

       L2=H⁰(O(16)|D12), L3=H⁰(O(17)|D12),
       L4=H⁰(O(18)|D12)/res(A18+P_t),
       A_l(s)=l s, B_l(r)=[l r].                    (1)

   Its dimensions are(12,12,5) and characters(V+P+D,W'+S+T,D).
   The first arrow's determinant divisor is exactly D12. The dependence
   on the endpoint is retained in the embedded constant space in L4.
4. For the universal first-arrow sheaf map

       barA:barN2 O(-1) → barN3 O,

   the cokernel has torsion of length12, with length one at each point of
   D12. Modulo torsion its equivariant bundle is

       Sym⁸(W) O(1) ⊕ A O(5).                     (2)

   The torsion/bundle sequence splits equivariantly as a sequence of
   sheaves, not canonically. This does NOT claim a splitting of the full
   two-pencil quotient or of its residual extension.

No compatibility with actual invariant Q is assumed. These constraints
apply in particular if such compatibility holds, but no existence of a
compatible pure-V line is asserted. Unlike the non-V reductions, this
quotient is not claimed to preserve the actual Bockstein problem. No
actual coefficient, parameter, point, matrix or instance rank is evaluated;
no source or catalogue pair is excluded and no complete repair is claimed.

## 1. Exact inputs and genuine maps

PR790 gives N=N0⊕NR, with N0 the fixed complete degree-ten first block.
PR795 Sections2–3 give the genuine exact sequence of both fixed pencils

       0 → NC → NR → N8 → 0.                       (3)

NC is the endpoint evaluation pencil with spaces H⁰(O16), H⁰(O17),
H¹(EC)=H⁰(O18)/H_t, where H_t=A18+V18+P_t and EC=(P+D)O(-2).
The first arrows of N8 are A⊗[H⁰(O4) --l--> H⁰(O5)].

PR792 Sections5–7 establish, with actual embedded maps,

       I2=f12 H⁰(O4), I3=f12 H⁰(O5),
       I4=H¹(EV)=P ⊂ H¹(EC), EV=W'O(-3),           (4)

where f12 has reduced divisor D12 and V18=f12 V6. The map on I4 is
induced by the inclusion of evaluation sequences EV→EC. Its quotient
F=EC/EV is locally free and satisfies

       0 → F → (A18+P_t)O → O(18)|D12 → 0.         (5)

PR792 proves that H⁰(F)=0 for every balanced endpoint: restriction of
A18+P_t to D12 is injective, using the exclusion of the unique divisible
P endpoint. These are actual maps; an abstract character subtraction
would not suffice for what follows.

All three originals are pinned by immutable commit, URL, Git blob and
SHA256 and copied unchanged into inputs/. The only further ingredients
are natural cohomology, elementary local algebra and complete binary-form
multiplication.

## 2. Identifying the entire endpoint quotient

The exact sequences

       0 → O(k-12) --f12--> O(k) → O(k)|D12 → 0

at k=16,17 identify their section quotients with H⁰(O(k)|D12), since
H¹(O4)=H¹(O5)=0. This identifies the first two spaces of NC/I in(1).
Restriction and multiplication commute, so the induced first arrows are
exactly multiplication on the torsion sheaf, using the original l.

From 0→EV→EC→F→0, the imported H⁰(F)=0 and H²(EV)=0 give

       H¹(EC)/H¹(EV) ≅ H¹(F).

Taking cohomology in(5), using H¹((A18+P_t)O)=0, gives

       H¹(F) ≅ H⁰(O18|D12)/res(A18+P_t).           (6)

These identifications also preserve the second arrows. More explicitly,
restriction H⁰(O18)→H⁰(O18|D12) sends H_t to res(A18+P_t), because V18
is divisible by f12. Its induced map H⁰(O18)/H_t→the quotient in(6)
is onto. Its kernel is f12 H⁰(O6) modulo f12 V6, which is exactly the
embedded image H¹(EV) in(4), by naturality of the two evaluation sequences.
Thus [l r] maps precisely to [res(l r)] in(6). This proves BOTH arrows
of(1), not just its vertices.

The dimensions are12,12,12-7=5; the character calculation follows from
NC=(V+P+2D,W'+S+2T,P+D) and I=(D,T,P).

## 3. The torsion first arrow and surjectivity of the second

Because D12 is reduced, over C its section spaces are direct sums of
one-dimensional fibers, one for each point p of that divisor. This
fiber decomposition is used for a universal proof, not to select or
evaluate an actual source point. The first map in(1) acts in the p-fiber
by multiplication by l(p). A nonzero linear form has just one zero.
Hence this12×12 map is invertible unless its zero lies in D12, and has
rank11 in that case. Its determinant is a nonzero scalar times the
product of the twelve distinct linear equations l(p); its divisor is
exactly reduced D12. No scalar normalization or coefficients are needed.
There exists l avoiding all twelve points, so the common first kernel
is zero.

For the second arrow, if l avoids D12 the map from L3 to H⁰(O18|D12)
is an isomorphism. If l vanishes at p∈D12 its image is the coordinate
hyperplane of sections zero at p. The constant subspace res(A18+P_t)
is not contained in that hyperplane: A18 is basepoint-free by the exact
source geometry (also by absence of a nonconstant G-invariant common
factor of degree≤18 for the irreducible A subsystem: the only possible
orbit divisor has degree12, and Sym⁶W has no A). Consequently the sum
of that hyperplane and res(A18+P_t) is the whole torsion section space.
The induced B_l:L3→L4 is therefore onto in both cases, for every nonzero l.

For clarity, the parenthetical argument needs no additional imported
basepoint-free theorem. An invariant common divisor has degree at most18.
The projective orbit sizes12,20,30,60 in PR792 imply it must be D12.
Dividing A18 by f12 would embed A in Sym⁶W=V+P, impossible. Multiplicity
≥2 has degree≥24. Thus A18 is indeed basepoint-free.

## 4. Transfer to the full quotient without splitting its residual

Quotient(3) by I to obtain the exact sequence of pencils

       0 → L → K=NR/I → N8 → 0.                   (7)

Every nonzero first arrow of N8 is injective, by polynomial multiplication.
The kernel sequence in the commuting diagram for(7) therefore identifies
ker A_l^K with ker A_l^L, canonically. N0 first arrows are also injective.
Since barN=N0⊕K and dim barN2=36, the ranks in Theorem1 follow, as does
zero common kernel. There is no choice of a residual splitting in this
argument, so every coupling class is covered.

Every second arrow of N8 is onto: under the natural connecting isomorphism
N8_3≅H¹(T O(-4)), it is multiplication to H¹(T O(-3)), dual to the
injective map H⁰(O1) --l--> H⁰(O2), as in PR795 Section8.
Section3 proves the same surjectivity for L. The diagram(7) then makes
B_l^K onto: lift the quotient target using N8 and correct the residual
error using L. The N0 second arrow is onto as well. Indeed its middle
space identifies naturally with H¹(E0(-1)) through the evaluation
sequence twisted by -1, since the constant middle term O(-1) is acyclic.
Then B_l^0 is H¹(E0(-1))→H¹(E0), with E0=W O(-9), dual to injective
polynomial multiplication H⁰(O7)→H⁰(O8). Thus the full barB_l is onto.

## 5. Universal degeneracy scheme and cokernel bundle

Regard the arrow parameter as the same projective line via the invariant
symplectic identification. The universal A_L:L2 O(-1)→L3 O is an injective
sheaf map, since it is generically invertible. Its cokernel T_D is a
length12 torsion sheaf, with length one at each point of D12. Locally
at each such point its matrix is equivalent to diag(t,1,...,1), with t
a local uniformizer. This follows from the distinct simple zeros in
Section3, without any numerical evaluation.

The universal first arrows of N0 and N8 are subbundle injections. For
the scalar complete multiplication pencil P_m, its universal cokernel
is O(m+1): this is the standard exact evaluation/Koszul sequence

       0 → H⁰(Om)O(-1) → H⁰(O(m+1))O → O(m+1) → 0,

using the same symplectic identification of the parameter line. Therefore
coker A0=Sym⁸(W)O1 and coker A8=A O5.

Applying the snake lemma to(7) as a diagram of these sheaf maps gives

       0 → T_D → coker A_K → A O5 → 0.             (8)

No kernel term intervenes, since both A_L and A8 are injective as sheaf
maps. Ext¹(A O5,T_D)=H¹(A*⊗T_D(-5))=0 because a zero-dimensional sheaf
has no H¹. Finite-group averaging gives the equivariant vanishing as well.
Thus(8) splits equivariantly, noncanonically, and the genuine N0 direct
summand gives exactly(2) for the torsion-free quotient.

Locally coker barA is therefore O^12 ⊕ O/(t) at D12 and O^12 elsewhere.
Equivalently its presentation is locally the direct sum of the regular
full-column-rank blocks and diag(t,1,...,1). The ideal of36×36 minors is
(t) at those points and the unit ideal elsewhere. This proves that the
full first-arrow degeneracy scheme is reduced D12, including its scheme
multiplicity. It is strictly stronger than identifying a set-theoretic
rank-drop locus. The vector-bundle quotient has rank12 and degree24;
adding the torsion length12 gives total cokernel degree36, as required
by the universal source36 O(-1) and target48 O.

A splitting of this sheaf cokernel is not a splitting of(7) in the
category of two pencils. In particular no Q stability, full-module
splitting or further cancellation is inferred from(8).

## 6. Verification boundary

verify.py checks all exact input SHA256 and Git blobs, representation and
cohomology dimensions, and universal symbolic diagonal rank-drop algebra.
Synthetic torsion fibers verify full-coupling kernel preservation and last-
arrow surjectivity; these are bounded linear-algebra checks only, not
selected actual source data. The geometric identification, reduced orbit
and every-point conclusions are supplied by the written proof. No computed
rank chooses an actual endpoint or a Q-compatibility alternative.
