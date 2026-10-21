# Algebraic curve realizations of symmetry-breaking deformation jets

Work over C. The object is the canonical cubic image V=V51, not the original HM primary surface or the full-adjoint target. Every automorphism below fixes the base pointwise. A marked deformation has an identification of its special fiber with V.

## Pinned dependencies

- [PR614](https://github.com/Akilleez-QA/read-em-and-weep/pull/614), commit 73fbf75838c91804ca637b5916d6aac217240958: abstract deformations of V are unobstructed, T1(V) has dimension 576, and H0(Theta_V)=0.
- [PR627](https://github.com/Akilleez-QA/read-em-and-weep/pull/627), commit 7c3f76f2e55c5cc0c3356972b5d7d676544c943a, research/hm/cubic-formal-symmetry-breaking/PROOF.md: Gamma=Aut(V) acts faithfully on T1(V); T_free, the complement of all nonidentity fixed subspaces, is nonempty. Every v in T_free extends to a compatible abstract formal deformation.
- [PR628](https://github.com/Akilleez-QA/read-em-and-weep/pull/628), commit f08ff9c2760e4aef074cfe716b923d29d5e7ebe8, research/hm/cubic-effective-deformations/PROOF.md: every such formal deformation is effective as a projective flat finitely presented X over A=C[[t]], with an ample invertible sheaf L restricting to O_V(1).

## 1. Finite-jet algebraic realization

Theorem. Fix a compatible formal deformation of V with first-order class v in T_free, and an integer N>=2. There exist a smooth integral finite-type C-curve B, a C-point b, an etale morphism q:B -> A1_C with q(b)=0, and a projective flat finitely presented family Y -> B, such that:

1. Y_b is marked isomorphic to V.
2. Using t=q^*(the coordinate of A1), the marked family over O_(B,b)/(t^N) is isomorphic to the prescribed formal deformation over C[t]/(t^N).
3. Every positive-order Artin reduction Y_n=Y x_B Spec(O_(B,b)/(t^(n+1))) has trivial fixed-base automorphism group, for n>=1.
4. Aut_B(Y)={1}, and also Aut_(O_(B,b))(Y x_B Spec O_(B,b))={1}.

The curve and family may depend on N. No single curve family is asserted to match all jets of the prescribed formal deformation.

Proof of existence. Apply PR628 to obtain (X,L)/A. As L is ample and X is projective over the affine Noetherian base, choose a sufficiently large power L^m and a closed immersion X -> P^r_A defined by finitely many sections. Here r is fixed, independent of the Artin order. This uses a high-power polarization, not lifting the original ten degree-one sections.

Let P be the Hilbert polynomial of the special fiber for this embedding. Flatness and projectivity give a classifying morphism alpha:Spec A -> H=Hilb^P(P^r_C). This classical projective Hilbert scheme is of finite type over C, and its universal closed subscheme is projective and flat over H. Choose an affine open U of H containing alpha(0). The entire morphism alpha factors through U: the inverse image of U is open and contains the closed point of the local scheme Spec A, hence is all of Spec A.

Write U=Spec C[z_1,...,z_s]/(F_1,...,F_e). The morphism alpha is a finite tuple a_i(t) in C[[t]] satisfying F_j(a(t))=0. Set R=C[t]_(t), whose completion is A. R is an excellent regular local ring, in particular a Noetherian G-ring. Apply [Stacks, Theorem 16.13.2, 07QZ](https://stacks.math.columbia.edu/tag/07QZ) to this finite polynomial system and the integer N. It yields an etale R-algebra R', a maximal ideal p over (t) with residue field C, and a solution c_i in R' whose image in the completed local ring at p agrees with a_i modulo t^N. The completion at this chosen point is canonically C[[t]] as a completed R-algebra, because the map is etale and the residue field extension is trivial.

For clarity, the equivalent henselian route is [Stacks, Theorem 16.13.1, 07QY](https://stacks.math.columbia.edu/tag/07QY) over R^h. This excellent henselian local ring has completion A. The approximate solution is in R^h; the finitely many elements and their finitely many polynomial identities descend to one pointed etale neighborhood because R^h is the filtered colimit of these neighborhoods. This is also the reduction recorded in 07QZ.

The etale algebra R' and the finitely many c_i and relations spread out over C[t,1/g] for some g(0) != 0: R is the filtered localization of these rings, all presentations involved are finite, and etaleness spreads out. After restricting to an affine neighborhood of p, they give a finite-type scheme B etale over an open neighborhood of 0 in A1 and a morphism beta:B -> U. Take the connected component containing b=p. A smooth connected curve over C is integral: its regular local rings are domains, so distinct irreducible components cannot meet; components are open and closed. Thus B may be taken smooth and integral. Its distinguished point has residue field C and t is a uniformizer there.

Pull back the universal Hilbert family along beta. The resulting Y -> B is projective, flat, and finitely presented. The two Hilbert morphisms coincide modulo t^N at b, so their universal-family pullbacks are isomorphic as embedded families over C[t]/(t^N). Forgetting the embedding preserves this isomorphism and the special-fiber marking. This proves assertions 1 and 2. Notice that only a chosen finite jet, not the full tuple a_i(t), has descended. The Hilbert construction carries the chosen high-power polarization L^m on that jet; it does not assert descent of the original line bundle L itself to the curve family.

## 2. All Artin orders, not only the matched orders

Although the constructed family need only match the original one through order N-1, its first-order class is v. Let n>=1 and let phi be a fixed-base automorphism of Y_n. Its restriction to V is some gamma in Aut(V). Restricting further to first order shows that gamma fixes the Kodaira-Spencer class v. By the definition of T_free, gamma=1.

The kernel of automorphism restriction across a square-zero base extension, among automorphisms already equal to the identity on the preceding reduction, is the group of derivations into the extension ideal. For the step C[t]/(t^(k+1)) -> C[t]/(t^k), flatness identifies that ideal sheaf with O_V tensor_C (t^k)/(t^(k+1)). The kernel is therefore H0(Theta_V) tensor_C (t^k)/(t^(k+1)), which is zero by PR614. Starting with the now-trivial restriction on V and inducting proves phi=1. This proves assertion 3 for every n, including n>=N. It depends only on the matched first-order class and H0(Theta_V)=0, not on matching all the original formal coefficients.

## 3. Relative automorphisms of the actual curve family

First work over D=O_(B,b), a Noetherian DVR. If a D-automorphism of Y_D is the identity on all Artin reductions, its equalizer with the identity is closed because Y_D is separated. Let I be the coherent ideal of that equalizer. At a point y of the special fiber, I_y is contained in every t^k O_(Y_D,y). [Krull intersection, Stacks 00IP](https://stacks.math.columbia.edu/tag/00IP) gives I_y=0. The support of I is proper over Spec D, hence has closed image. A nonempty closed subset of Spec D contains its closed point, whereas this support misses the special fiber. Thus I=0. Assertion 3 proves Aut_D(Y_D)={1}.

Now let phi be a B-automorphism of Y. Its restriction to Y_D is the identity, hence so is its restriction to the generic fiber Y_eta. The generic fiber is schematically dense in Y because Y is flat over the integral curve B. Explicitly, on an affine base open Spec S with fraction field K and an affine open Spec C of its preimage, flatness makes C a flat S-module and therefore torsion-free; the map C -> C tensor_S K is injective. The coherent equalizer ideal of phi and the identity becomes zero after tensoring with K, so this injection forces the ideal itself to vanish on every such affine open. Therefore phi is the identity globally. This proves assertion 4.

This is a statement about automorphisms defined over B (or its local germ). It does not assert that arbitrary automorphisms of Y_eta or of the geometric generic fiber extend over B, and gives no conclusion that either of those groups is trivial.

## Contribution and boundaries

The earlier result produced effective families over C[[t]]. Here every prescribed finite jet of one of those families is realized over an honest smooth finite-type algebraic curve, with the same symmetry-breaking first-order class. The new family has no fixed-base automorphisms on any positive Artin neighborhood, on the local algebraic germ, or over the whole chosen integral curve. It is nonconstant as a marked deformation since v!=0.

No claim is made that the initially chosen infinite formal arc converges, is algebraic, or descends unchanged. No generic-fiber automorphism assertion, original-P9 embedded deformation assertion, selected-source evaluation, or original Weil-class/full-adjoint algebraicity conclusion is made. The proof uses only structural existence theorems and the pinned dependencies; no selected coefficients, points, derivatives, matrices, ranks, or large computations are evaluated. The result is an authored mathematical proof, not a formal proof-assistant check.
