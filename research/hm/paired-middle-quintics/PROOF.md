# Complete rational normal quintics in the nontrivial middle cycle spaces

Work over C with the actual module H, its balanced symmetric degree-five trace pairing, and the actual finite normalizer N of the Heisenberg group Gamma. Parameter twists are on P(W'), not internal grading shifts. This argument evaluates no selected parameter or source instance.

## Pinned dependencies

- [PR528, commit bd9a26837bb79b2e21cf35d6586d3ba3d6ca83fa](https://github.com/Akilleez-QA/read-em-and-weep/blob/bd9a26837bb79b2e21cf35d6586d3ba3d6ca83fa/research/hm/middle-family-parity/PROOF.md): the actual column sequence 0 -> End_0(T) O -> (E tensor Lambda3 T) O(2) -> F -> 0; C=H/M=A O(1); B=D5(C); V=Tor2(B)_5=(F O(1))*.
- [PR531, commit 39671b0c8bf41a253c031336aed719f9d465ef9b](https://github.com/Akilleez-QA/read-em-and-weep/blob/39671b0c8bf41a253c031336aed719f9d465ef9b/research/hm/middle-trivial-nonvanishing/PROOF.md): H2=E tensor Q, Q=Sym3(W'), with quotient H2 -> C2=E O(3) given by cubic evaluation. The trivial middle block is nonzero and generic b is either 0 or 24.
- [PR537, commit e8a3b656cf947d348d334b4033aa0ce63e468deb](https://github.com/Akilleez-QA/read-em-and-weep/blob/e8a3b656cf947d348d334b4033aa0ce63e468deb/research/hm/paired-middle-stabilizers/PROOF.md): for nontrivial chi, U_chi=(End_0 T)_chi and L_chi=(End E)_chi are coefficient lines for the full inverse-image stabilizer; inverse-character coefficient lines are dual by trace. Their inverse-pair scalar has the standard C5 linearization on O(10).
- [PR499, commit 1112189481554b0353c64178e3adc0dede2c3fbe](https://github.com/Akilleez-QA/read-em-and-weep/blob/1112189481554b0353c64178e3adc0dede2c3fbe/research/hm/middle-euler-ghost-exclusion/PROOF.md): the internal-degree-five Koszul complex K(H)_5 is acyclic.
- [PR518, commit b17c7cac111568f9b45876a2ad8fae4e46578841](https://github.com/Akilleez-QA/read-em-and-weep/blob/b17c7cac111568f9b45876a2ad8fae4e46578841/research/hm/middle-obstruction-symmetry/PROOF.md): the central lift pairing is symmetric, with formula q(b,c)=<d^{-1}b,c>.

The binary representation weights used below are those of Horrocks--Mumford (1973), Section 3.3 and character appendix: on an order-five subgroup, if W' has weights zeta^r,zeta^{-r}, then W0 has weights zeta^(2r),zeta^(-2r), after exchanging the two eigenlines if necessary. Public source: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf .

## 1. The actual quadratic column map has both square coefficients nonzero

Fix chi != 1. Let C be its order-five stabilizer in N/Gamma and C_tilde its inverse image. The actual sequence is

0 -> U_chi O -> L_chi tensor W0 O(2) -> F_chi -> 0.

The coefficient ratio U_chi tensor L_chi^{-1} has trivial Gamma action and hence descends to a character of C. The map is a nowhere-zero vector of quadratic forms. Choose C-eigen-coordinates x,y of weights zeta^r,zeta^{-r}. The six weights of W0 tensor Sym2(W'^*) are, as residues divided by r,

4, 2, 0, 0, -2, -4 modulo 5.

Only the zero weight occurs twice. Every nonzero weight occurs once, and its eigenspace is a single monomial in a single W0 eigenline. Such a section has a zero on P1, contradicting fiberwise injectivity of the actual column map. Therefore the ratio character is trivial: U_chi and L_chi are isomorphic as C_tilde coefficient lines. In suitable eigenbases the map is

1 |-> (a x^2, b y^2), with a b != 0.

Indeed the zero-weight space is the span of the two square monomials in the opposite W0 eigenlines; either coefficient zero would again give a common zero. This conclusion proves nonvanishing of these two quadratic coefficients without computing them.

## 2. Constant six-dimensional cycle spaces

Write K_i=H_{5-i} tensor Lambda^i T and Z_chi=ker(d:K_2,chi -> K_1,chi). For a nontrivial chi the dimensions of the actual Koszul strand, from degree four to degree one, are

0 -> 2 -> 8 -> 8 -> 2 -> 0.

The two endpoint terms K5 and K0 have no nontrivial characters. The displayed dimensions follow from H1=T tensor W', H2=E tensor Q, their trace duals, and the fact that each character occurs once in End(T) and End(E). Acyclicity gives dim Z_chi=6 and identifies K_3,chi / d(K_4,chi) with Z_chi.

The perfect exterior-trace pairing identifies the annihilator of Z_chi in K_3,chi^{-1} with d(K_4,chi^{-1}). This is also immediate from adjointness of the Koszul differentials and exactness. Consequently the lift formula defines a constant nondegenerate bilinear pairing

P_chi: Z_chi x Z_chi^{-1} -> C,
P_chi(b,c)=<z,c>, where dz=b.

It is well-defined, nondegenerate, and independent of lifts. The opposite pairing is its transpose. The family pair scalar is its restriction to the two actual moving Tor2(B) lines, not an arbitrary form chosen afterwards.

## 3. The moving Tor line is a complete rational normal quintic

Dualize the actual chi^{-1} column sequence after tensoring by O(1). Using the trace identifications of coefficient lines gives

0 -> V_chi -> L_chi tensor W0* O(-3) -> L_chi O(-1) -> 0.

Here Section 1 was used to identify U_chi with L_chi. The last map is a row of two nonzero square monomials. Its kernel vector is, up to exchange of coordinates and nonzero constants,

(-b y^2, a x^2).

The inclusion B3 -> H3 is dual to H2 -> C2. By PR531 this is the cubic Veronese inclusion. Hence the actual line V_chi=Tor2(B)_5,chi -> K_2,chi is represented by

lambda^3 tensor (-b y^2, a x^2),

where lambda has coordinates x,y. Its eight coordinates, in monomial bases of Sym3(W'^*) and W0*, are nonzero constant multiples of

x^3 y^2, x^2 y^3, x y^4, y^5;
x^5, x^4 y, x^3 y^2, x^2 y^3.

Thus their span as binary forms is the entire six-dimensional H^0(P1,O(5)). The linear span of the moving vectors in K_2,chi therefore has dimension six. Every moving vector lies in Z_chi by the definition of Tor2(B), and dim Z_chi=6, so that span is exactly Z_chi.

Equivalently, the actual inclusion V_chi -> Z_chi O induces an isomorphism from the dual constant cycle space (with its coefficient line removed) onto H^0(O(5)). This is not just a degree calculation: every quintic monomial has occurred. The induced map P1 -> P(Z_chi) is the complete degree-five Veronese embedding, a rational normal quintic. In particular no proper constant subspace of Z_chi contains all these Tor lines.

All the identifications can be made C_tilde-equivariant. With the coefficient line retained, the cycle space is L_chi times the standard six-dimensional degree-five Veronese representation. The coefficient factor for chi^{-1} is its trace dual. Therefore the nondegenerate pairing P_chi, after removing these dual factors, is an ordinary C-invariant bilinear pairing between two copies of the degree-five Veronese space.

## 4. Exact residual bilinear restriction kernel

Use quintic coordinates z_i=x^(5-i)y^i, 0<=i<=5, on both Veronese spaces. Absorb all harmless nonzero binomial constants into the two basis identifications. A C-invariant bilinear form can have entries only when i+j is divisible by five. Its only allowed matrix entries are

p_00, p_05, p_50, p_55, p_14, p_41, p_23, p_32.

The actual form is nondegenerate by Section 2. Its diagonal Veronese restriction is

p_00 x^10 + (p_05+p_50+p_14+p_41+p_23+p_32) x^5 y^5 + p_55 y^10.

Reordering the basis into the block {0,5} and the four singleton rows shows that nondegeneracy is equivalent to

p_14 p_41 p_23 p_32 (p_00 p_55 - p_05 p_50) != 0.

In particular the four entries p_14,p_41,p_23,p_32 of the actual form are nonzero, although their values are not calculated.

Thus the unresolved actual zero-scalar alternative is now precisely the three linear equations

p_00=0, p_55=0,
p_05+p_50+p_14+p_41+p_23+p_32=0

on this eight-dimensional invariant bilinear-form space, together with nondegeneracy. In that zero-scalar branch, p_05 and p_50 must also be nonzero. Identical vanishing would therefore be cancellation among six nonzero antidiagonal terms, not absence of the actual pairing couplings. The kernel is five-dimensional. It does contain nondegenerate forms: a matrix with only its six antidiagonal entries nonzero, those entries equal to 1,1,1,1,1,-5, is invertible and its restriction is zero. This is an abstract universal tensor example, not an evaluation or replacement of the actual HM form.

Consequently the rational-normal-quintic result does not itself eliminate the all-zero branch. Nondegeneracy, stabilizer equivariance, and full spanning alone cannot do so. Any remaining exclusion must use additional actual multiplication information to show that the actual pairing avoids this explicit restriction kernel. The example does not assert compatibility with every other normalizer or actual multiplication constraint.

## Contribution and limits

The new step identifies the actual nontrivial moving Tor line as a complete rational normal quintic in the whole constant six-dimensional cycle space, proves the two actual stabilizer-square coefficients nonzero, and gives an exact finite-dimensional tensor obstruction to paired nonvanishing. This resolves the possible missing span dependency and excludes a constant-proper-subspace explanation of identically vanishing scalar sections.

It does not choose the actual generic branch: b_generic remains 0 or 24. It does not resolve the fixed source pair, higher-order lifting, or algebraicity. This is authored structural mathematics conditional on the pinned inputs, awaiting independent review and not formally checked.
