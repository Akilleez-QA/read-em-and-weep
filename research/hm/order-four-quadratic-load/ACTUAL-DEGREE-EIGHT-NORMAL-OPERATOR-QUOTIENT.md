# The actual degree-eight normal operator quotient has dimensions 32 -> 36 -> 4

## Exact quotient, not a value assertion

On the negative projection line L=P(W), let M8 be the cover-degree-eight piece of the ACTUAL vertex sheaf M(4)=omega_(2Z)(5). The global positive operator boundary on this piece is the exact quotient

    0 -> H0(E8) -> H0(M8) -> P4 -> 0,
          dim32      dim36      dim4.                (1)

The tangent coefficient bundle E8 and its gauge subbundle J8 are explicit:

    0 -> T6 O_L(-1) -> E8 -> S4 O_L(7) -> 0,
    0 -> V O_L(-4) -> J8 -> O_L(4) -> 0,
    0 -> J8 -> E8 -> M8 -> 0.                       (2)

In fact J8 is identified by the actual square-ideal map with P4 O_L(-2). This pins the quotient in (1) to the already proved GLOBAL P4 obstruction; it is not an inference from the dimension of a local residue space.

The actual corrected residue must still be inserted into (1). No nonzero value is claimed.

## 1. Tangent coefficients and line factors

The minimal ideal generator lines on the root gerbe of L are O(-9/2), O(5/2), as checked in the full-frame matching theorem. Consequently the two G frame lines are O(9/2), O(-5/2). A tangent matrix of diagonal cover degree8 has the form

    R=v3 S2+u5 S1,

with v3 of cover degree3 and u5 of cover degree5. After physical twist4, their coefficient bundles are respectively

    Sym³(Wprime) O(9/2+4-3/2)=S4 O(7),
    Sym⁵(Wprime) O(-5/2+4-5/2)=T6 O(-1).

The triangular transition g->g+p f mixes the second coefficient by p times the first. This gives the first sequence of (2), retaining the actual nonsplit transition rather than choosing a split bundle. Both H0 and H1 of T6 O(-1) vanish, so

    H0(E8)=H0(S4 O(7)), dim32;  H1(E8)=0.           (3)

## 2. The gauge bundle and its actual nonzero extension

A trace-free gauge matrix K of the required degree has the form

    K=[[k,0],[r,-k]],

where k has cover degree0 and r has cover degree2. The upper-right entry would have degree-2 and is absent. Their bundles are O(4) and V O(-4). Conjugation by [[1,0],[p,1]] sends r to r+2p k, so the extension class is twice the ACTUAL quintic-generator class. It is nonzero.

The connecting map is

    H0(O(4))=D5 -> V H1(O(-4))=V tensor A=P4+D5.     (4)

It is nonzero without evaluating coefficients: if multiplication by every quartic killed the nonzero extension class e in V H1(O(-8)), Serre duality would make e annihilate every product of a quartic and a quadratic. Those products span H0(O(6)), contradiction. Equivariance and irreducibility make (4) the D5 inclusion. Therefore

    H0(J8)=0,  H1(J8)=P4.                          (5)

There is also a direct actual identification. The square-ideal map is

    tr(NK)=2fg k-f²r.

Its image is exactly the degree8 ideal piece f² Sym²(Wprime)+fg, and it is injective on the rank4 coefficient bundle by regularity of f,g. The known generator relation sequence therefore identifies

    J8 = (I_Z²(6))_(degree8) = P4 O_L(-2).          (6)

The factor2 in the quotient generator is precisely the factor2 in the transition r->r+2pk.

## 3. The canonical-module quotient and its cohomology

The commutator map corresponds under the fixed tangent convention to evaluation

    K sigma=(k f, r f-k g).

It is injective in this graded piece: its first component forces k=0, and the second then forces r=0. Its cokernel is the degree8 tangent-modulo-conjugation module M8. Thus the last sequence of (2) is exact.

Its ranks and degrees are

    rank(E8)=10, deg(E8)=22,
    rank(J8)=4,  deg(J8)=-8,
    rank(M8)=6,  deg(M8)=30.

The actual homogeneous (3,5) family is flat, so these are vector bundles on L. Equations (3),(5) give (1), H1(M8)=0, and h0(M8)=36. This proof uses no selected fiber or actual rank test.

## 4. Why this is the global boundary rather than merely a local one

Let U=X minus the conic C. The Serre quotient G(4)->I_Z(6) sends the degree8 tangent coefficients to

    sigma wedge v=f u5-g v3.

Since the actual vertex quotient algebra has socle degree6, its degree8 ideal is the entire coordinate piece. Thus

    0 -> O_L(4) -> E8 -> Sym^8(Wprime) O_L(2) -> 0.   (7)

Its kernel is v=sigma rho, where rho has cover degree0 and physical twist4. The target has27 global sections, and the kernel has5, recovering32. Since H1(O_L(4))=0 the section map is onto. In fact (7) splits, uniquely G-equivariantly: H1(O_L(2))=0 gives splitting, while [(Sym^8 Wprime) tensor H0(O_L(2))]^G=0 gives uniqueness.

The global comparison is given by the actual wedge diagram, not by extending chosen polynomial tangent representatives. The Serre map G(4)->I_Z(6), v |-> sigma wedge v, descends modulo the gauge image to

    M(4) -> (I_Z/I_Z^2)(6) subset O_(2Z)(6),

because

    sigma wedge (K sigma) = -trace(NK).

The kernel is the scalar class-of-N piece O_Z(4). On vertex cover degree8 this gives the exact sequence

    0 -> O_L(4) -> M8 -> Q4(6) -> 0,                 (8)

where Q4 is the actual degree8 square algebra quotient: I_8 is the full octic space. The square-ideal sequence is

    0 -> P4 O_L(-2) -> Sym^8(Wprime) O_L(2)
      -> Q4(6) -> 0.                                (9)

Thus E8 can intrinsically be defined as the fiber product

    M8 times_(Q4(6)) Sym^8(Wprime) O_L(2).

It fits both (7) and 0->J8->E8->M8->0. The polynomial coefficient description gives this same bundle: its map sends v to its class and sigma wedge v. The map is fiberwise injective at every base point: a coefficient gauge with zero wedge has 2gk=fr, forcing k=r=0 in degrees0 and2 by the actual uniform coprimality. It is therefore an isomorphism of equal-rank bundles. No literal homogeneous subbundle of the actual G|U is asserted.

The actual boundary diagram commutes, up to the displayed fixed sign. POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md equations(2),(8) identify

    H1(B_Q(4))_+ -> H1(I_Z^2(6))_+
      -> H1(P4 O_L(-2))

as isomorphisms. Hence the boundary of (9), composed with (8), is exactly the actual global boundary on M8. This is stronger than a dimension match and requires no Hartogs assertion for polynomial representatives. The27-dimensional polynomial image in H0(Q4(6)), together with the5-dimensional scalar kernel H0(O4), gives exactly the32-dimensional kernel in H0(M8).

Actual determinant-one stabilizers I+tN do not affect this intrinsic diagram; on a tangent R they change R by t[N,R], a commutator. The conic part is removed by POSITIVE-MIDPOINT-OPERATOR-BOUNDARY-IS-VERTEX-ONLY.md. Exactness of the actual global sequence supplies global G(4) representatives for these kernel CLASSES, without claiming that a specified polynomial E8 representative itself extends.

## Remaining calculation and reproduction

Insert the full corrected harmonic Hessian residue, including its unique quintic primitive and scalar/equation factors, into this explicit quotient. A nonzero element of H0(M8) can still lie in the 32-dimensional image in (1). The eventual third Bockstein also quotients by the actual second-symbol image.

Run verify_degree_eight_operator_quotient.py. The script verifies universal matrix identities, line degrees, and P1 dimensions. The actual nonzero extension and the pinned global comparison are the geometric proofs above, not numerical assumptions.
