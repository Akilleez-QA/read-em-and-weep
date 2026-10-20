Publication context: this retained proof or audit may describe an intermediate bound or then-open branch. Read the unit overview for the current scope and later implications. Historical mathematical review is not a new formal verification.

# All square-zero canonical length-ten defects are excluded

## Statement and boundary

Let R be the completed regular local ring of dimension four at the canonical point, H its full stabilizer, and W=m/m². Let M be an H-equivariant rank-two reflexive R-module, free off the closed point, with equivariantly trivial determinant. Then its finite defect Q=Ext²_R(M,R) cannot satisfy both length(Q)=10 and m²Q=0.

This excludes every square-zero length-ten defect, not only the wedge family. It does not exclude the remaining non-square-zero length-ten families or improve the global lower bound by itself. All arguments concern abstract universal local modules and finite representations.

We use the audited necessary inequality β3(Q)−2β4(Q)≤2 and the audited equality-case result from wedge-defect-equivariant-obstruction/PROOF.md: when equality holds, Tor₁(D(Q),k) is self-dual as an actual H-representation, where D=Ext⁴_R(-,R). This convention already includes the determinant character; no extra determinant twist is applied to the self-duality condition.

## 1. The numerical inequality forces one radical shape

Take an invariant splitting Q=T⊕S with S=mQ, and write t=dim T, s=dim S, so t+s=10. Multiplication kills S. Let r_i be the rank of the induced Koszul map T⊗Λ^iW→S⊗Λ^(i−1)W, and put a=r4. The common parameter kernel in T has dimension t−a, and every differential factors through the active top quotient of dimension a. Consequently

    β3−2β4 = 20−r3+a,
    r3≤4a,       r3≤6s,       a≤t=10−s.

The necessary inequality implies r3−a≥18. The first bound gives a≥6, hence s≤4. If s≤3, the second bound gives r3−a≤18−6=12, impossible. Therefore s=4, t=6, a=6 and r3=24. In particular the inequality is an equality, the common parameter kernel on T is zero, and soc(Q)=S has dimension four.

## 2. The order-twenty subgroup fixes the representation shape

Restrict to L=⟨Z,g⟩≅C5⋊C4. Its irreducibles are four one-dimensional characters, all Z-trivial, and the unique four-dimensional irreducible V. Also W|L=V. Thus S, of dimension four, is either V or a sum of four characters.

If S is character-only, every character in T is killed by parameters. A six-dimensional T contains at most one V, giving active dimension at most four, contrary to a=6.

Hence S=V. If T is character-only, the multiplication adjoint embeds its active quotient into Hom_C(W,S). The character-isotypic part of Hom_C(V,V) has dimension four: each of the four L-characters occurs once, because V⊗χ≅V and Schur's lemma gives Hom_L(V,V⊗χ) dimension one. Thus a≤4, again impossible. We conclude

    T|L = V plus two characters,       S|L=V.

Put P=D(Q). Finite local duality identifies its underlying vector space with Q* twisted by (det W)*. Since soc(Q)=S, P has top U of dimension four, with U|L=V, and radical A of dimension six, with A|L=V plus two characters. Moreover m²P=0. In this paragraph A denotes the radical of P, not Ext¹(M,R).

The multiplication map μ:W⊗U→A is surjective. Betti reversal gives β0(P)=4 and β1(P)=10. Its first Koszul differential has rank six. The degree-two differential

    δ2: U⊗Λ²W → A⊗W

is between two 24-dimensional spaces. Since β1(P)=40−6−rank(δ2)=10, this map must be an isomorphism. The degree-one homology therefore consists exactly of the linear relation representation

    K=ker(μ:W⊗U→A),       dim K=10.

The equality-case condition requires K≅K*. In particular its restriction to B=⟨Z,D⟩≅C5² must be self-dual. Also invertibility of δ2 requires equality of the B-weight multisets of U⊗Λ²W and A⊗W. We show these two requirements are incompatible.

## 3. Exhaustive B-weight reduction

Use the weight convention W={(i,3i²):i∈F5×}; all entries below are modulo five. The opposite simultaneous convention gives the dual calculation and the same contradiction. The group g permutes B-weights by multiplying the first coordinate by an element of order four and the second by its square. For c∈F5, define the four-weight orbit

    O_c = {(i,ci²):i∈F5×}.

Since U|L=V, its four B-weight spaces are one-dimensional and form one such orbit O_c. Scalar μ5 characters and C4 linearizations do not change these B-weights. Likewise the nonzero-Z-weight part of A is O_d for some d. Its remaining two-dimensional part has Z-weight zero.

Compute W⊗U by setting its two nonzero first coordinates to i and j=ti. When t=−1, the four resulting weights are (0,(3+c)i²). If z=3+c is nonzero, these are (0,z),(0,−z), each twice; if z=0 all four weights are zero. The two-dimensional Z-trivial quotient of A must therefore have weights

    Z_z = {(0,z),(0,−z)},        z=3+c,

including two copies of (0,0) when z=0. Indeed for z≠0 the g-orbit is the pair, so both multiplicities must agree. This explicitly includes the full-H two-dimensional irreducibles, not merely sums of H-characters. Thus A has B-weight multiset O_d⊔Z_z.

The remaining values t=1,2,3 yield three four-weight orbits with slopes

    (3+ct²)/(1+t)².

Their exhaustive list is:

    c       three slopes
    0       2,2,3
    1       1,3,2
    2       0,4,1
    3       4,0,0
    4       3,1,4

The quotient A removes one of these three orbits, O_d. Its two zero-first-coordinate weights leave a self-dual pair in K automatically. The other weights in K are the two remaining orbits. Duality sends O_e to O_(−e), so K|B can be self-dual only if these two slopes form a multiset invariant under negation. Row by row, this forces exactly

    (c,d) = (0,2), (1,1), (2,0), (3,4), (4,3).

This list is necessary, not a claim of existence or H-self-duality for each row.

## 4. Every remaining row fails the invertible-Koszul character test

The B-weight multiset of Λ²W is O_0⊔Z_1: nonopposite wedges give the four weights (i,0), while opposite wedges give (0,1),(0,−1).

It suffices to compare weights with first coordinate one. In U⊗Λ²W their second coordinates, counted with multiplicity, are

    {4c,4c,c,c+1,c−1}.                                      (L)

For example the first three come from the nonzero first coordinates i=2,3,4 of U paired with 1−i in O_0; the last two come from Z_1.

In A⊗W the corresponding second coordinates are

    {2+d,2+4d,3+4d,c+1,−c}.                                (R)

Here the first three come from the first coordinates 2,3,4 of W paired with 1−i in O_d; the last two come from 3±z, where z=3+c.

For complete transparency, the following rows list multiplicities at second coordinates 0,1,2,3,4, respectively:

    c,d       multiplicities from (L)       multiplicities from (R)
    0,2       (3,1,0,0,1)                  (2,2,0,0,1)
    1,1       (1,1,1,0,2)                  (0,1,2,1,1)
    2,0       (0,1,1,3,0)                  (0,0,2,3,0)
    3,4       (0,0,3,1,1)                  (0,1,1,1,2)
    4,3       (1,2,0,1,1)                  (3,1,0,0,1)

Every row differs. Thus no B-equivariant isomorphism U⊗Λ²W≅A⊗W exists in any candidate case. This contradicts the necessary invertibility of δ2, completing the exclusion.

## Twists, scope, and dependencies

The proof allows all scalar μ5 characters and all choices of stabilizer extensions. Restriction to B forgets those choices, but the contradictions already hold on B. The determinant twist in passing from Q to P merely changes which orbit O_c occurs; all five possibilities were included. The equality criterion uses finite duality D=Ext⁴(-,R) exactly as audited and does not silently replace it by untwisted vector duality.

Dependencies: length-five-local-defect/PROOF.md for the numerical necessary inequality; wedge-defect-equivariant-obstruction/{PROOF,AUDIT}.md for the equality-case self-duality; length-two-local-defect/PROOF.md for H and its action; length-ten-local-defect/{PROOF,AUDIT}.md for background and the wedge numerical counterexample. The tables are evaluations of displayed formulas over F5, involving five abstract representation types only. No physical source/model matrix, operation, chosen input, rank instance, jet, or residue was evaluated. 
