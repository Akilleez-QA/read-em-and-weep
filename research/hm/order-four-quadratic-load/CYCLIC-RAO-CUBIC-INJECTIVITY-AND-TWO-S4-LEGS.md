# Cubic injectivity in the actual cyclic Rao module

## New result

Let B=End_0(F), q0 the invariant positive quadric, N the canonical invariant section of B_Q0(2), and xi=delta_q0(N) in H1(B). Then the actual graded multiplication map

    H0(O_Q0(3)) -> H1(B(3)),  h |-> h xi

is injective. Equivalently Ann(xi)_3=q0 S_1. Its image has character

    A + 2P4 + D5 + 2S4 + T6

and dimension thirty. This is a statement about actual multiplication, not an expected generic rank.

## 1. Definition and lower degrees

Ambient H0(B(2))=0 implies xi is nonzero. The restriction sequence makes q0 xi=0. Naturality of its connecting maps gives delta_q0(Nh)=h xi for every homogeneous polynomial h. Multiplication by N embeds O_Q0 into B_Q0(2), since Q0 is integral and N is nonzero. Thus all polynomial multiples of N are independent modulo q0.

The established vanishings H0(B(3))=H0(B(4))=0 already make the cyclic maps in degrees one and two injective. In degree three the target restriction sequence has the nonzero ambient group H0(B(5))=Sym^2 U, U=H0(F(3))=P4. The following argument excludes precisely its possible intersection with the polynomial multiples of N.

## 2. Excluding a cubic annihilator

Let Z be the kernel of h -> h xi from H0(O_Q0(3)). Each h in Z has Nh equal to the restriction of some beta in H0(B(5)). This lift is unique: the kernel of restriction is q0 H0(B(3))=0. The resulting map Z -> H0(B(5)) is injective and equivariant.

The nilpotent N vanishes on the reduced conic C0. Indeed, locally there the actual spinor filtration has quotient an ideal of the conic times a line bundle; if the two local ideal generators are f,g, the nilpotent matrix has entries -fg,-g^2,f^2,fg, all vanishing on C0 (in fact to second order). Consequently every beta arising above restricts to zero on C0.

The actual four-space U generates F_C0(3). Its associated integral nondegenerate ruled surface in P(U*)=P3 has at most one independent quadratic equation. Under H0(B(5))=Sym^2 U this proves

    dim ker[H0(B(5)) -> H0(B_C0(5))] <= 1.

Thus dim Z <=1. The group G is perfect, so any one-dimensional representation is trivial. However H0(O_Q0(3)) has no trivial constituent. Indeed its character is Sym^3(V+W) - (V+W), the subtraction being q0 times linear forms; the exact universal character calculation gives A+2P4+D5+2S4+T6. Hence Z=0.

This argument uses the actual conic generation and the actual ambient symmetric-square identification, rather than a Hilbert-series expectation for a free cyclic module.

## 3. Both S4 and T6 legs from D5 are active

The degree-two cyclic kernel summands at q0 are represented by negative quadratics A, positive harmonic quadratics D5, and the odd mixed component T6. Negative linear multiplication of D5 is the polynomial map

    W tensor D5 = S4 direct-sum T6 -> H0(O_Q0(3)).

It is injective: this is the bidegree (positive two, negative one) harmonic subspace, and the only q0-multiples in that bidegree are q0 W, disjoint from D5 tensor W. Cubic cyclic injectivity therefore proves that both intrinsic multiplicity vectors a_S and a_T of this actual multiplication are nonzero.

Negative multiplication of A also produces a copy of S4=Sym^3 W, represented by pure negative cubics. This copy is linearly independent of the S4 from D5, since the two have different positive/negative bidegrees in the polynomial quotient. Therefore the S4 multiplicity space of H1(B(3))_- contains two independent active lines, one from A and one from D5. The multiplication W tensor A has its usual polynomial antisymmetry kernel; no injectivity of that full tensor product is asserted.

## 4. Exact scope and remaining gamma gate

The positive first smoothing scalar is still the actual quotient class of q_minus h xi in H1(B(4))/q0 H1(B(2)), for h in D5. The cubic injection does not prove that this degree-four class is nonzero. In particular it does not turn the nonzero first-leg vector into a proof that the second-leg covector has nonzero pairing with it.

Dependencies: INVARIANT-CONE-SPINOR-FILTRATION-AND-NILPOTENT.md; TWIST-FIVE-GLOBAL-COHOMOLOGY-AND-BOUNDARY-DEFECT.md; the ruled-surface restriction bound in DIAGONAL-SCALAR-LIFT-NONPRODUCT-OBSTRUCTION.md; and POSITIVE-GAMMA-TWO-LINEAR-STEP-CRITERION.md. The new proof does not require choosing an actual coefficient, matrix, or rank sample.
