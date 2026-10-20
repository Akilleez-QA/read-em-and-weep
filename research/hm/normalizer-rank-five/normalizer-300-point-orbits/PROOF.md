# Exactly two 300-point orbits, both excluding simple isolated defects

## Result

Let G=A⋊K, A=F5², K=SL2(F5), be the standard projective Schrödinger normalizer on P(V), dim V=5, with its stipulated determinant-one lift N=H5⋊K⊂SL(V).

There are exactly two G-orbits of size 300. They are represented by

    p+=[e1+e−1],    p−=[e1−e−1].

Both have projective stabilizer C10, A-conjugate to the product of a Sylow-five subgroup of K and its central involution. Their linear N-stabilizers are μ5×C10. The two orbits are distinguished by the eigenvalue +1 or −1 of the unique involution of their linear stabilizer on the represented line.

Neither orbit can support a length-one isolated defect Ext²(B,O) of an N-equivariant rank-two reflexive sheaf with equivariantly trivial determinant. The minus orbit is excluded by the determinant-character identity alone. On the plus orbit that identity permits two defect characters, but the stronger necessary alternating-form condition from the same local theorem excludes both. Thus each supported 300-point orbit contributes at least 600 to the total defect length.

Every orbit other than the canonical 30-point orbit, the unique 250-point orbit, and these two 300-point orbits has at least 375 points. This last statement is a lower bound, not a classification or realization statement at 375. All local conclusions below are necessary constraints; no existence of a sheaf or defect is asserted.

## 1. Stabilizers of order ten and their cocycles

The established point-orbit theorem says that outside the canonical orbit E, A acts freely. A point in an orbit of size 300 therefore has stabilizer S of order ten, projecting isomorphically to an order-ten subgroup L≤K. It is the graph of a cocycle f:L→A.

K has a unique involution c=−I. Hence c∈L. The Sylow-five subgroup P of L is normal, because its number divides two and is one modulo five. Since c is central and disjoint from P,

    L=P×⟨c⟩≅C10.

All these subgroups are conjugate in K by Sylow conjugacy. Centrality of c and its action −1 on A give the cocycle identity

    2f(g)=f(c)−g f(c).

Thus f(g)=a−ga, with a=f(c)/2. Conjugation by an element of A reduces S to L. A lift of this conjugating element in H5 also conjugates the corresponding linear representations and stabilizers.

## 2. Stable lines and exact stabilizers

Choose the usual universal Schrödinger basis ei, indexed by i∈F5, and a primitive fifth root ζ. The selected P has determinant-one generator

    D ei=ζ^(i²/2) ei,

and c acts by reflection

    c ei=e−i.

Here 1/2=3 in F5. These are universal representation identities, not evaluated geometric source matrices. In particular det D=1, D has order five, c has order two and determinant one, and they commute.

The D-eigenspaces are

    C e0                       with eigenvalue 1,
    span(e1,e−1)               with eigenvalue ζ³,
    span(e2,e−2)               with eigenvalue ζ².

Taking the c-eigenlines inside them gives exactly five L-stable lines:

    C e0, C(e1+e−1), C(e1−e−1), C(e2+e−2), C(e2−e−2).

The first belongs to E. None of the other four does. To see this directly, a nontrivial Weyl translation with nonzero shift has a five-cycle on the coordinates, so any eigenvector has all five coordinates nonzero. A nontrivial clock operator has five distinct eigenvalues, so its eigenvectors have exactly one nonzero coordinate. Thus a vector with exactly two nonzero coordinates cannot have a nontrivial projective A-stabilizer, whereas points of E do.

For any of the other four lines, its full stabilizer contains L, so its orbit has at most 300 points. The prior 250-point gap says its stabilizer has order at most twelve. Its order is divisible by ten; consequently it is exactly ten. This proves that all four lines have exact stabilizer L and orbit size 300. Their full stabilizer in N is exactly μ5×L, because N→G has central kernel μ5 and L is an actual linear complement subgroup.

## 3. Exactly two orbits

The universal permutation operator M ei=e2i normalizes P and c. Its determinant-one representative is −M∈K. Projectively it carries

    [e1+e−1] to [e2+e−2],
    [e1−e−1] to [e2−e−2].

Thus the four noncanonical lines form at most two G-orbits. Every 300-point orbit has a stabilizer conjugate to L by Section 1 and is therefore represented among these four lines.

The two signs cannot be in the same orbit. The full linear stabilizer μ5×C10 has a unique involution, namely c. Any lift in N of a proposed conjugating element carries that unique involution to the unique involution of the target stabilizer. Conjugation preserves its eigenvalue on the represented line, but those eigenvalues are +1 and −1 for the two signs. This is impossible. There are therefore precisely two orbits, each of size 300.

## 4. The necessary local conditions

Let R be the local ring at one of these points, W=m/m² its cotangent representation, and δ=det W. Suppose M=Bp is rank two, reflexive, free on the punctured spectrum, with equivariantly trivial determinant. If its defect has length one, write

    Ext²_R(M,R)=kχ

for a character χ of its full N-stabilizer H. The audited local theorem in ../../local-defect/minimal-local-defect-character/PROOF.md proves both of the following necessary conditions:

    δ³=χ⁻⁴,
    W admits a nondegenerate alternating form with values in η=χ⁻²δ⁻¹.

The second is the nondegenerate quotient Λ²W→η established in Section 2 of that theorem; it is stronger than its wedge-square character identity. We use both, without claiming sufficiency or constructing a module.

For g∈SL(V) preserving a line with eigenvalue λ, the cotangent determinant is λ⁵. Hence at both representative points,

    δ(D)=1,    δ(z)=1 for z∈μ5,
    δ(c)=+1 at p+,    δ(c)=−1 at p−.

The central μ5 acts trivially on the local coordinates, so the displayed central value is also immediate geometrically.

### 4.1. Minus orbit

At p−, evaluation of δ³=χ⁻⁴ at the actual order-two element c gives

    −1=χ(c)⁻⁴=1.

No character χ satisfies the necessary condition. Thus a length-one defect is impossible on the minus orbit.

### 4.2. Plus orbit: determinant-compatible characters still fail

At p+, δ is trivial on all of H=μ5×⟨D,c⟩. The determinant identity forces χ⁴=1. Since μ5 and D have order five, χ is trivial on both, and χ(c) can be either +1 or −1. These are exactly the two characters satisfying the determinant identity; neither is asserted to occur as a defect.

For either choice, η=χ⁻²δ⁻¹ is the trivial character. Thus a simple defect would require an H-invariant nondegenerate alternating form on W.

The line at p+ has D-eigenvalue ζ³. The cotangent weights are the line eigenvalue divided by the remaining V-eigenvalues. Consequently the multiset of D-weights on W, written as exponents modulo five, is

    {3,0,1,1}.

More explicitly the four cotangent character spaces correspond to the complementary vectors e0, e1−e−1, e2+e−2, e2−e−2. Their (D-exponent,c-sign) pairs are

    (3,+), (0,−), (1,+), (1,−).

An invariant bilinear form can pair a D-weight a only with weight −a. The weight-three space has no weight-two partner; likewise the weight-one spaces have no weight-four partners. Therefore every invariant alternating form is degenerate (in fact its only potentially self-pairing weight-zero space is one-dimensional, so every such alternating form is zero). This contradicts the necessary nondegeneracy.

Hence the plus orbit also excludes length-one defects. Conjugation transports these conclusions to every point in the corresponding orbit.

## 5. The next orbit-size gap and finite-length consequences

Outside E, an orbit has size 25k where k=[K:L] divides 120. After k=12, the next possible divisor is 15: neither 13 nor 14 divides 120. The prior results classify k=10 as the unique 250-point orbit, rule out k=11, and bound all earlier noncanonical possibilities; Sections 1–3 classify k=12. Thus every remaining orbit has size at least 375.

For an isolated equivariant rank-two defect sheaf T=Ext²(B,O), local lengths are constant on each orbit. A supported 300-point orbit has local length at least two by Section 4, and therefore contributes at least 600. The earlier 250-point obstruction gives contribution at least 500 from its orbit. It follows that any nonzero such T with total length strictly below 375 must be supported on E alone. Its total length is 30m with 1≤m≤12, subject to all separately established stronger canonical-stalk restrictions. In particular, using the independently established canonical lower bound m≥9, the only necessary numerical possibilities below 375 are

    270, 300, 330, 360.

This arithmetic conclusion does not assert realization of any value, and the canonical m≥9 input is separate from the orbit and local arguments proved here.

## Inputs and evidence boundary

Inputs: ../normalizer-refined-point-gap/PROOF.md; ../normalizer-250-simple-defect/PROOF.md and AUDIT.md; ../normalizer-minimal-point-orbit/PROOF.md as cited there; and ../../local-defect/minimal-local-defect-character/PROOF.md. The optional last numerical refinement uses the separately supplied canonical m≥9 result and is not needed for any new proof above.

Only elementary finite-group structure, universal Schrödinger representation identities, and the established local algebra obstruction are used. No actual physical source-model matrix, operation, chosen input, rank instance, jet, or residue was evaluated. No source-app write, upstream change, installation, subgroup search, or large computation was performed. The only write is this local proof artifact.
