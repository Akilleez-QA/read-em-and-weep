# The unique 375-point orbit and its simple-defect obstruction

## Result

Let G=A⋊K, where A=F5² and K=SL2(F5), act on P(V) through the standard projective Schrödinger normalizer, dim V=5. Use its stipulated determinant-one lift N=H5⋊K⊂SL(V).

There is exactly one G-orbit of size 375. Its projective point stabilizer is A-conjugate to a Sylow-two subgroup Q≅Q8 of K, and its full linear stabilizer is correspondingly conjugate to μ5×Q. For a fixed Q there are exactly three Q-stable lines in V; its order-24 normalizer acts transitively on them.

At each point of this orbit there is an actual order-four element of the N-stabilizer with cotangent determinant −1. Consequently the orbit cannot support a length-one isolated defect Ext²(B,O) of an N-equivariant rank-two reflexive sheaf B with equivariantly trivial determinant. If supported, it contributes at least 750 to total defect length.

Every orbit other than the canonical 30-point orbit E, the unique 250-point orbit, the two 300-point orbits, and this unique 375-point orbit has size at least 500. Thus any nonzero isolated defect satisfying the stated sheaf hypotheses and having total length strictly below 500 is supported on E alone. These are necessary constraints, not existence statements about sheaves or realization of defect lengths.

## 1. Order-eight subgroups and cocycles

Since |K|=120, an order-eight subgroup Q is a Sylow-two subgroup. All such subgroups are conjugate. The unique involution of K is c=−I, so c belongs to Q. Its image Q/⟨c⟩ has order four in K/⟨c⟩≅A5. As A5 has no element of order four, this image is a Klein four group.

Every lift of a nonidentity element of Q/⟨c⟩ has square c: its square lies in ⟨c⟩, and square one would produce an involution different from c. Thus all six elements outside ⟨c⟩ have order four. In particular Q is quaternion Q8. For example, for lifts x,y of different nonidentity quotient elements, both have square c; they cannot commute, since then (xy)²=c²=1 although xy lies outside ⟨c⟩. Their commutator must therefore be the nontrivial element c of the central kernel. These give the quaternion relations, and in particular c is a commutator.

A point on a 375-point orbit is outside E, so the established free-A theorem makes its projective stabilizer S project isomorphically onto an order-eight subgroup Q of K. Write S as the graph of a cocycle f:Q→A. Since c is central in Q and acts as −1 on A, the cocycle identities give

    2f(g)=f(c)−g f(c).

With a=f(c)/2 this reads f(g)=a−ga, so S is A-conjugate to Q. Conjugation lifts to N and preserves the relevant linear stabilizer representations. Therefore it suffices to classify Q-stable lines in the standard linear complement K⊂N.

## 2. Exactly three Q-stable lines

The universal character facts established in ../normalizer-refined-point-gap/PROOF.md, Section 2, give the c-eigenspace splitting

    V=V+⊕V−,       dim V+=3,       dim V−=2,

and, for every order-four element u of K,

    Spec(u|V)={1,−1,−1,i,−i}.

In particular tr(u|V+)=−1. The representation of Q on V+ factors through Q/⟨c⟩≅V4; its character has values 3 at the identity and −1 at all three nonidentity elements. Taking inner products with the four V4-characters shows that V+ is the direct sum of the three distinct nontrivial characters, each once, with no trivial constituent.

Thus V+ has exactly three Q-stable lines, one for each nontrivial character of V4. There are no Q-stable lines in V−: a one-dimensional character of Q sends its commutator c to 1, whereas c acts as −1 on V−. This also proves the irreducibility of the two-dimensional Q-representation V−, since a reducible complex representation of dimension two would have a one-dimensional constituent. Any Q-stable line in V must be a c-eigenline, so these three lines are all of them.

For each of the three lines ℓ, its nontrivial V4-character takes value −1 on two of the three nonidentity elements. A lift u∈Q of either such element has actual order four in K⊂N and acts on ℓ by −1.

## 3. Exact stabilizers, existence, and uniqueness

Let p be any of the three Q-stable lines. It cannot belong to E, since |G_p|=100 on E, and a subgroup of order eight cannot lie in a group of order 100. The established noncanonical orbit gap implies |G_p|≤12. But G_p contains Q, so its order is divisible by eight. The only such positive integer at most twelve is eight. Hence

    G_p=Q,       |G·p|=3000/8=375.

This proves existence and exact stabilizers without assuming that a point orbit of size 375 was already known. Since N→G has central kernel μ5 and Q is an actual linear subgroup, the full inverse image of Q is μ5×Q. This is the full N-stabilizer at p.

To see transitivity on the three lines, first describe the normalizer. A Klein four subgroup U of A5 is the subgroup of double transpositions fixing one letter. Indeed, after conjugating one nonidentity element to (12)(34), any commuting involution must lie in its centralizer in A5, namely {1,(12)(34),(13)(24),(14)(23)}. Thus U is this group, with common fixed letter 5. Its normalizer is precisely the A4 stabilizing that letter: a normalizing permutation preserves the common fixed set, and A4 normalizes its Klein four subgroup. Therefore N_K(Q), the full inverse image of N_A5(U), has order 24. Conjugation by its quotient of order three cyclically permutes the three nonidentity elements of U, and also its three nontrivial characters.

The three character spaces in V+ are consequently permuted transitively by N_K(Q). They lie in one G-orbit. Finally every 375-point stabilizer is conjugate to Q by Section 1 and Sylow conjugacy, and every resulting fixed point is among these three lines. Hence this orbit is unique.

## 4. Exclusion of a simple isolated defect

At a representative p=[ℓ], choose the actual order-four u from Section 2, whose eigenvalue on ℓ is λ=−1. For an element g∈SL(V) preserving ℓ with eigenvalue λ, the tangent space is Hom(ℓ,V/ℓ); hence

    det(T_p P(V))(g)=λ^(−5),
    δ(g):=det(T_p* P(V))(g)=λ^5.

In particular δ(u)=−1. Let H be the full N-stabilizer of p. If the isolated defect of M=B_p had length one, write Ext²_R(M,R)=kχ for a character χ of H. The established local theorem in ../../local-defect/minimal-local-defect-character/PROOF.md gives the necessary identity

    δ³=χ^(−4).

Since u has order four in H itself, χ(u)^4=1, while δ(u)^3=−1. Evaluating the identity at u is a contradiction. This does not assume that χ descends to G_p, and thus includes possible central μ5-characters. Conjugation carries the order-four witness to every other point in the orbit.

The local theorem requires reflexivity, rank two, local freeness on the punctured spectrum, and equivariantly trivial determinant. These are precisely the sheaf hypotheses stipulated here, with isolated singularities supplying the punctured-spectrum condition. No assertion is made for modules lacking these hypotheses.

## 5. The 500-point gap and the below-500 consequence

Every point outside E has trivial A-stabilizer. Its orbit size is therefore 25k, where k=[K:L] divides 120. The previous results exclude all k<10, classify k=10 as the unique 250-point orbit and k=12 as the two 300-point orbits, and this proof classifies k=15 as the unique 375-point orbit. Between 15 and 20 there is no divisor of 120. There are also no unaccounted divisors between 10 and 15. Hence every remaining orbit has size at least 25·20=500. This does not claim existence at 500.

For a nonzero isolated defect T=Ext²(B,O), equivariance makes stalk lengths constant along each orbit. The prior results exclude simple defects on the 250-point orbit and on both 300-point orbits, giving respective contributions at least 500 and 600. Section 4 gives contribution at least 750 on the 375-point orbit. Every remaining noncanonical orbit contributes at least 500 just by its size.

It follows that

    0<length(T)<500  ⇒  Supp(T)=E,
    length(T)=30m,   1≤m≤16.

The prior canonical simple-defect obstruction additionally gives m≥2. Any independently established stronger bound on canonical stalk length can be substituted here. In particular, if an application separately supplies m≥10, the necessary numerical possibilities below 500 are exactly

    300, 330, 360, 390, 420, 450, 480.

This last list is conditional on that separate m≥10 input; the present proof neither derives it nor asserts realization of any listed length.

## Inputs and evidence boundary

Inputs read: ../normalizer-300-point-orbits/PROOF.md and AUDIT.md; ../normalizer-250-simple-defect/PROOF.md; ../normalizer-refined-point-gap/PROOF.md; ../../local-defect/minimal-local-defect-character/PROOF.md. The normalizer character and earlier gap facts are used exactly as stated there. The optional m≥10 application is explicitly conditional.

Only universal abstract finite-group representations, elementary subgroup structure, and the established local algebra obstruction were used. No actual physical source-model matrix, operation, chosen input, rank instance, jet, or residue was evaluated. No source-app write, upstream change, installation, search over subgroups, or large computation was performed. The sole write is this local proof artifact.
