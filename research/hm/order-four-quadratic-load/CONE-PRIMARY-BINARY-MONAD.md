# The actual binary monad controlling the cone ruling bundle

## Setup and claim

Keep the established general rank-four cone Q, small resolution Y and ruling p:Y->P1. Put J=p_*pi^*(F_Q(2)). We use the open where every ruling plane has one of Boralevi's generic or divisor-stratum resolutions and Q is primary-good. Thus J has rank5, degree -10 and H0(J)=0. The following gives a new exact presentation and a smaller balancedness gate, not a proof of balancedness:

    5O(-2) -> 20O(-1) -> 10O

is a monad with middle cohomology J. Its maps are the actual primary multiplication maps restricted to the ruling, not arbitrary maps of these sizes.

## 1. Universal-plane Koszul calculation

Let S be the rank-two bundle of equations of the ruling planes inside the constant space H0(P4,O(1)). On this ruling S=O(-1)^2. For example the ruled cone has plane-vector subbundle O+O(-1)^2 in the constant five-space; its dual quotient is O+O(1)^2, whose evaluation kernel is O(-1)^2. This description is independent of a choice of cone coefficients.

On P4 times P1 the universal incidence Y has the relative Koszul resolution, tensored by F(2),

    F tensor det S -> F(1) tensor S -> F(2).

The established HM cohomology in these three twists is concentrated in degree one, of dimensions5,10,10. Applying derived projection to P1 therefore gives the three-term complex

    H1(F) tensor det S -> H1(F(1)) tensor S -> H1(F(2)) tensor O.

Its only cohomology is J in the middle. Indeed the two permitted plane resolutions give H0(F_P(2))=5 and H1=H2=0 on every fiber; the universal incidence is flat. Thus the left map is a subbundle injection and the right map a bundle surjection. Writing K0 for the right kernel gives exact sequences

    0 -> K0 -> 20O(-1) -> 10O -> 0,
    0 -> 5O(-2) -> K0 -> J -> 0.

In particular K0 has rank10 and degree -20.

## 2. The canonical 20-to-20 coefficient map

Twist the first exact sequence by O(1). Its H0 map is a canonical linear map

    C20 -> C20,

namely

    H1(F(1)) tensor H0(S(1))
      -> H1(F(2)) tensor H0(O(1)).

It comes from the actual multiplication H1(F(1)) tensor H0(P4,O(1))->H1(F(2)) and the ruling inclusion S->H0(P4,O(1)) tensor O. It is basis-independent; choosing bases merely writes the two ruling pencils as a block matrix using four linear forms.

Twisting the second exact sequence by O(1), the left term 5O(-1) is acyclic. Consequently the kernel and cokernel of this actual coefficient map are respectively H0(J(1)) and H1(J(1)). No matrix entries or ranks were selected or tested.

Because J has rank5 and degree -10, its splitting is O(-2)^5 if and only if H0(J(1))=0. Indeed this vanishing makes every summand have degree at most -2, so equality of total degrees forces all five to equal -2. Thus

    J=O(-2)^5 iff the canonical 20-to-20 map is invertible.

Equivalently K0=O(-2)^10. One direction follows from H0(K0(1))=0 and its rank/degree. The other follows because if J=O(-2)^5, the extension by 5O(-2) splits, as H1(O)=0.

## 3. Exact limitation

The right bundle map 20O(-1)->10O is surjective at every point of the ruling. This does NOT imply that its induced 20-to-20 map on twisted global sections is invertible. Its kernel bundle can have nonbalanced splitting while still having constant rank. Similarly, primary-goodness proves only H0(J)=0, not H0(J(1))=0.

The established negative splitting and total degree leave the following degree multisets for J (negative signs understood):

    (6,1,1,1,1), (5,2,1,1,1), (4,3,1,1,1),
    (4,2,2,1,1), (3,3,2,1,1), (3,2,2,2,1), (2,2,2,2,2).

The corank of the canonical 20-to-20 map is exactly the number of entries equal to one. It is therefore at most four, so this actual map has rank at least sixteen without evaluation. Corank zero is the balanced case; corank one uniquely gives (3,2,2,2,1); coranks two and three each allow two types; corank four uniquely gives (6,1,1,1,1). This map is NOT the rank-twenty full-adjoint lift boundary.

The next twist distinguishes every ambiguity. The actual map H0(20O(1))->H0(10O(2)) has dimensions40->30. Its kernel contains the canonical five-dimensional image of H0(5O), and its kernel modulo that image is H0(J(2)). In the displayed splitting order, the pairs (h0(J(1)),h0(J(2))) are

    (4,8), (3,7), (3,6), (2,6), (2,5), (1,5), (0,5).

Thus these two cohomology dimensions determine the complete splitting of J. The 40-to-30 map has rank 35-h0(J(2)), hence lies between27 and30. Again these bounds are deductions from the bundle structure, not sampled ranks.

No item is excluded by replacing the actual primary multiplication by a generic pencil. The canonical 20-to-20 determinant must be controlled using the actual module or further geometry. Even balanced J by itself does not prove twist-four adjoint vanishing; the ten-jump adjoint extension still carries actual map data.

## Provenance and scope

Inputs are the standard normalized HM cohomology, Boralevi's plane resolutions, and the checked cone construction in RANK-FOUR-CONE-RULING-GATE.md and CONE-TEN-JUMP-ADJOINT-PRESENTATION.md. The conclusions are structural bounds and splitting criteria, not an evaluation of the actual coefficient maps or a complete repair.
