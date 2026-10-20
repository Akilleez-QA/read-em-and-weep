# The unique 30-point orbit and a 250-point gap

## Result

For the standard projective Schrödinger normalizer

    G = A ⋊ K,   A = F5²,   K = SL2(F5),   |G| = 3000,

acting on P(V), dim V = 5, the 30 Heisenberg eigenlines form a unique orbit E. Every other point orbit has at least 250 points. This is a lower bound only: no existence or sharpness at 250 is asserted.

This refines the bound 125 in `../normalizer-minimal-point-orbit/PROOF.md`. Only universal finite-group representation arguments are used. In particular no actual geometric operation, source, matrix, selected input, rank instance, jet, or residue is evaluated.

## 1. Inputs and reduction to subgroup orders

The preceding proof establishes that E is the unique orbit with nontrivial A-stabilizers. On every other orbit A acts freely, so its size is 25k. For a point p in such an orbit, S = G_p has order 120/k, intersects A trivially, and projects isomorphically to a subgroup L of K of that order. Thus S is the graph of an A-valued cocycle on L. The earlier argument using perfection of K excludes k = 1,2,3,4.

If L contains c = −I, every such graph is conjugate by A to L itself. Indeed for its cocycle f, centrality of c and its action −1 on A imply

    2f(g) = f(c) − g f(c).

Writing a = f(c)/2 gives f(g) = a − ga. Consequently it suffices to analyze projective fixed lines of the standard subgroup L whenever c belongs to L.

Every even-order subgroup of K contains c: Cauchy's theorem gives an involution, and c is the unique involution of SL2(F5). For the latter assertion, an order-two matrix is diagonalizable in characteristic five with eigenvalues ±1; determinant one forces either I or −I.

## 2. Universal character facts used for the order-24 case

We use the standard linear complement K in the classical determinant-one Schrödinger normalizer H5 ⋊ K ⊂ SL(V), whose projectivization is the complement of the preceding proof. The following facts and their independent derivation also appear in Sections 2–4 of `../quintic-normalizer-exclusion/PROOF.md`.

The Weyl operators give a basis of End(V) indexed by A. Conjugation by an element g of K permutes their lines by its action on A. If g has no nonzero fixed vector in A, the only fixed Weyl line is the identity line, and therefore

    |tr(g | V)|² = tr(g | End(V)) = 1.

For c = −I, order two and determinant one consequently give eigenvalue multiplicities 1³,(−1)². Write V = V+ ⊕ V− for these eigenspaces, of dimensions three and two.

Every order-four element u of K has u² = c, is conjugate to diag(2,3), and is conjugate to its inverse. Its eigenvalues on A are 2 and 3, so the preceding trace identity applies. On V its i and −i multiplicities are equal and sum to two, hence are both one. Its 1 and −1 multiplicities sum to three; determinant one forces the −1 multiplicity to be even. The possibility of zero such eigenvalues would give trace three, contradicting the trace identity. Thus the spectrum is

    {1, −1, −1, i, −i}.

In particular tr(u | V+) = −1 and tr(u | V−) = 0. These arguments establish precisely the restricted character data needed below; no global character table or assumed irreducible decomposition is necessary.

## 3. Excluding k = 5: binary tetrahedral subgroups fix no line

Here |L| = 24. It contains c, so its quotient L/<c> is an order-12 subgroup of PSL2(F5) ≅ A5. Every order-12 subgroup of A5 is a point stabilizer A4 in its usual action on five letters: it cannot be transitive, and if it had no fixed letter its orbit partition would be 2+3, placing it in (S2 × S3)∩A5, a group of order six. A fixed letter puts it in an A4 of the same order.

The inverse image Q of the normal Klein four subgroup of this A4 is quaternion Q8. Indeed it has order eight and unique involution c, while each lift of a nonidentity Klein-four element has order four. It cannot be cyclic, since its quotient by <c> is not cyclic; thus it is Q8. In particular c is a commutator of two quaternion generators.

On V+, Q acts through its Klein-four quotient. Its character has value three at the identity and −1 at each of the three other elements. Averaging against the four Klein-four characters shows that its trivial-character multiplicity is zero and each of its three nontrivial-character multiplicities is one. The order-three quotient A4/V4 cyclically permutes these three characters by conjugation. Hence none of their one-dimensional eigenspaces is stable under L, and V+ has no L-stable line.

On V−, c acts by −1. But every one-dimensional character of L sends the commutator c to 1. Therefore V− also has no L-stable line. An L-stable line in V must be an eigenspace for c and thus lie in one of these two pieces. There are no such lines.

Since S is A-conjugate to L by Section 1, S cannot fix p. This excludes an orbit of size 125.

## 4. Excluding k = 6: the Borel fixes only an eigenline

Here |L| = 20. Its Sylow-five subgroup P is normal, because the number of Sylow-five subgroups divides four and is congruent to one modulo five. Every such P in K is conjugate to the lower unipotent subgroup. Its normalizer has order twenty: it is the lower triangular determinant-one subgroup, since the unique common fixed line of P in A must be preserved. Thus L is exactly this normalizer, after conjugacy in K.

In the universal Schrödinger model with basis e_i, i∈F5, the projective action of this lower triangular subgroup is generated by

    D e_i = ζ^(i²/2) e_i,
    M e_i = e_(2i),

where ζ is a primitive fifth root. Scalar normalizations do not affect invariant lines. The first induces the lower unipotent shear on Weyl labels; the second induces diag(2,3). These label transformations generate the lower triangular subgroup.

The three eigenspaces of D are

    C e_0,   span(e_1,e_−1),   span(e_2,e_−2).

The operator M fixes C e_0 and interchanges the other two eigenspaces. A line invariant under both generators must be contained in a D-eigenspace; neither of the last two can contain such a line because M takes it to the other disjoint eigenspace. Therefore C e_0 is the unique projective fixed point of L.

This point belongs to E, since it is an eigenline of the clock Weyl operator. Conjugating L in K, or conjugating its cocycle graph in A, keeps its unique fixed point inside the G-invariant set E. Therefore S cannot fix a point in a free A-orbit. An orbit of size 150 is excluded.

## 5. Excluding k = 7,8,9

Since k is an index of a subgroup in K, it divides 120. This excludes k = 7 and k = 9.

For k = 8 the subgroup L would have order fifteen. Its Sylow-five subgroup is normal, since its number divides three and is congruent to one modulo five. Hence L would lie in the order-twenty normalizer of that subgroup, contradicting Lagrange's theorem. Thus k = 8 is also impossible.

Combining all cases gives k ≥ 10 outside E, proving the claimed 250-point gap.

## 6. Finite-length equivariant consequences

Let Q be a nonzero finite-length coherent sheaf on P(V), equivariant for G or for a central cover inducing this projective action. If

    0 < length(Q) < 250,

then its invariant support cannot contain any orbit other than E. Hence Supp(Q) = E. Equivariance identifies stalk lengths along E, so every stalk has the same positive integral length m and

    length(Q) = 30m,   1 ≤ m ≤ 8.

Thus the possible lengths below 250 are 30,60,90,120,150,180,210,240. This is a necessary arithmetic condition, not a realization theorem. When the length is 30, the underlying coherent sheaf is O_E for the reduced set E, without any assertion about its equivariant structure.

In particular, for any conditional singularity or defect sheaf from the rank-eight discussion whose finite length is 5q, this gives

    0 < q < 50  ⇒  q ∈ {6,12,18,24,30,36,42,48},

and its support is exactly E. Where a finite singular locus is known to equal that support, it is likewise E. The precise sheaf-theoretic hypotheses remain those of the corresponding rank-eight proof; this group-theoretic refinement supplies no new existence or branch-exclusion assertion.

## Evidence boundary

The earlier proofs supply the standard projective normalizer and its determinant-one linear Schrödinger lift. All arguments here concern that universal representation, elementary subgroup structure, and invariant finite sets. The symbolic operators D and M are universal identities only. No actual geometric operation, source or matrix, input, rank instance, jet, residue, or large computation was used. Only this local proof artifact was written.
