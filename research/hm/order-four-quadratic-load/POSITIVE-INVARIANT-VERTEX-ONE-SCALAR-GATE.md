# A one-scalar conditional gate for positive excess

## The correct remaining objective

The actual positive multiplication block is H1(B(2))_+ -> H1(B(4))_+, of dimensions 41 and 37. Its kernel is H0(B_Q(4))_+ and its cokernel is H1(B_Q(4))_+. Thus the goal is surjectivity and positive section dimension exactly four, NOT vanishing of positive sections. The independently established generic odd vanishing does not itself settle this positive block.

The existing finite-normal description, after eliminating the fourth-order positive branch, has the same cohomology as a positive 72-to-68 complex: a 45-to-68 second-jet gate followed by a 27-to-cokernel restriction gate. The following is a different new conditional reduction, at the invariant positive vertex q0, not a new claim about those existing ranks.

## 1. Exact invariant-vertex representation bounds

Write A=Sym^2 W, D5=Sym^4 W, P4 for the genuine four-dimensional representation, and V for the other genuine three-dimensional representation. The actual monad Euler character, using the proved cohomology concentration at ambient twists two and four, gives

H1(B(2))_+ = A + 2V + 3P4 + 4D5,
H1(B(4))_+ = 2V + 4P4 + 3D5.

Since q0 is invariant, Schur decomposition bounds rank(m_q0)_+ by 6+12+15=33. Its kernel always contains A+D5 and its cokernel always contains P4. If it attains rank 33, these are the entire kernel and cokernel. This rank equality is a hypothesis, not a consequence of the bound. If it does not attain 33, its rank is at most 30: the nonzero common irreducibles have dimensions 3,4,5, so a multiplicity-rank deficiency costs at least three dimensions.

## 2. The only first negative-smoothing coefficient

Assume rank(m_q0)_+=33. Negative quadratic directions form A. The first Bockstein of the actual pencil q0+t a is the equivariant bilinear map

A tensor (A direct-sum D5) -> P4.

Character arithmetic gives Hom_G(A tensor A,P4)=0 and dim Hom_G(A tensor D5,P4)=1. Therefore it vanishes on the forced A summand and is gamma times the unique nonzero coupling on D5. The vanishing or nonvanishing of the scalar gamma is independent of all choices of irreducible identifications. Gamma is not evaluated here.

## 3. The universal coupling has generic rank four

The unique coupling is Cartan multiplication followed by projection:

Sym^2 W tensor Sym^4 W -> Sym^6 W -> P4,

where Sym^6 W=V direct-sum P4. It is nonzero because Cartan multiplication is surjective. Fix a nonzero quadratic a with two roots. Multiplication by a embeds Sym^4 W into Sym^6 W; its image consists of sextics vanishing on that length-two root divisor. The kernel of the projected coupling therefore identifies with the kernel of evaluation

V -> O(6)|_(root divisor).

Evaluation of any three-dimensional linear system of binary sextics at two general points has rank two. Indeed on the complement of its common zeros, evaluation defines a map to P(V*). If every general pair gave proportional evaluation functionals, that map would be constant. All three sections would then be proportional as rational functions, contradicting their linear independence. Hence a pair with independent evaluations exists, and independence holds on a nonempty open set of pairs. It descends to a nonempty open of quadratics. This argument does not require claiming independence at every pair or choosing an actual quadratic.

Thus the displayed evaluation has kernel dimension one for a general a. The universal projected multiplication Sym^4 W -> P4 then has rank 5-1=4.

## 4. Consequence for the actual positive block

Under the two hypotheses rank(m_q0)_+=33 and gamma nonzero, the actual first Bockstein has rank four for general negative directions. The generic rank of a linear pencil is at least its special rank plus the first Bockstein rank: cancel an invertible special block, and its Schur complement has first coefficient equal to that Bockstein. Hence the actual positive block has rank at least 33+4=37, which is full target rank.

It follows that these two hypotheses suffice for generic positive excess zero and h0(B_Q(4))_+=4. Combined with generic odd vanishing, this would give exact full-adjoint corank four on a general smooth inversion-even quadric. Smoothness causes no issue: the nonempty open of negative quadratics with distinct roots gives smooth q0+t a for nonzero t, and intersects the nonempty rank open.

Conversely, failure of generic positive surjectivity forces either rank(m_q0)_+<=30, or rank33 with gamma=0. Neither alternative is excluded. In particular the newly uniform primary hyperplane section bundle does not alone prove rank33 or gamma nonzero, so it is not used to manufacture either assertion.

## Evidence and reproduction

The actual ambient blocks and cohomology concentration are FULL-ADJOINT-PENCIL-INVOLUTION-BLOCKS.md. The remaining finite-normal positive goal is recorded in GENERIC-EVEN-QUARTIC-JET-ELIMINATION.md and BALANCED-CONIC-FINITE-OBSTRUCTION-COMPLEX.md. The exact character calculation is independently reproduced by verify_positive_invariant_vertex_gate.py using the existing monad K-class helper. The two-point evaluation proof above is coefficient-free. No actual HM coefficients, matrices, selected ranks, experiments, or external writes are used.
