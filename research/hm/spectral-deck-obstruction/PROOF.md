# The Gram spectral module obstructs a deck lift and determines an A4 cover

Status: independently mathematically reviewed (PASS), conditional on the pinned input; see REVIEW.md. Work over C. No selected HM coefficients, points, matrices, ranks, or scans are evaluated. All assertions are conditional on the pinned input below; they are not proof-assistant certificates.

## Pinned input and notation

Use [PR654's Gram spectral geometry](https://github.com/Akilleez-QA/read-em-and-weep/blob/f0c94ff7979652c094da3efaa11fea4629dbf59a/research/hm/gram-spectral-geometry/PROOF.md), commit f0c94ff7979652c094da3efaa11fea4629dbf59a. It constructs a smooth connected genus-ten curve pi:S->L=P1, given by lambda^3=d with d a section of O_L(12) having twelve simple zeros Omega. The cover is cyclic of degree three; let sigma act by lambda->zeta_3 lambda. Its only ramification is total ramification over Omega.

The actual self-adjoint Gram operator M:E->E(4), E=O_L^3, determines a spectral line bundle B with pi_*B=E and

    T=B tensor pi^*O_L(-4),  T^2=O_S,  T != O_S.

It also determines Theta=B tensor pi^*O_L(-1), an ineffective even theta characteristic. These are facts about the actual spectral module, not choices made to fit degrees. The curve S is distinct from the original genus-four trigonal support D.

## 1. No nontrivial invariant two-torsion class

For any degree-zero line bundle F on S, its norm Nm_pi(F) has degree zero on P1, hence is trivial. The norm–pullback identity for this cyclic cover gives

    F tensor sigma^*F tensor (sigma^2)^*F = pi^*Nm_pi(F) = O_S.

This identity does not require pi to be etale. Indeed, represent F by a divisor Z on the smooth curve S. The divisor identity pi^*pi_*Z=sum_(j=0)^2 (sigma^j)^*Z holds at unramified points and at ramified points alike: at a totally ramified point both sides have multiplicity three. It descends to the displayed identity of line-bundle classes.

If F is two-torsion and sigma^*F=F, this identity reads F^3=O_S. Together with F^2=O_S it implies F=O_S. Therefore

    Pic(S)[2]^(sigma)=0.

Apply this to T. Its three classes T, sigma^*T, and (sigma^2)^*T are distinct and nontrivial, and their product is trivial. Consequently they are exactly the nonzero elements of a subgroup

    H=<T,sigma^*T> of Pic(S)[2],  H isomorphic to (Z/2)^2.

The deck generator acts on H by a three-cycle on its nonzero elements.

Since every pi^*O_L(k) is deck-invariant, neither B nor Theta is isomorphic to its pullback by sigma or sigma^2. In particular neither admits a line-bundle automorphism covering either nonidentity deck transformation. This is stronger than an obstruction to choosing a compatible linearization: the necessary isomorphism of line-bundle classes already fails. Twisting B or Theta by any line bundle pulled back from L cannot remove the obstruction.

Equivalently, no global invertible frame transformation of E conjugates M to zeta_3 M or zeta_3^2 M. Such a conjugacy would identify the corresponding spectral modules and induce one of the forbidden deck isomorphisms of B. This excludes a global deck-symmetric identification of the actual module, not local diagonalization on an unramified open set.

## 2. The conjugates determine a connected etale Klein-four cover

The Kummer exact sequence on the smooth projective connected complex curve S identifies H^1(S,mu_2) with Pic(S)[2]: the possible kernel is C^*/(C^*)^2, which is zero. Thus T and sigma^*T define independent nonzero etale double-cover classes. Take their fiber product over S and call it q:Y->S.

This fiber product is a connected etale cover of degree four, with group

    K=Hom(H,mu_2) isomorphic to (Z/2)^2.

For example, via the complex topological fundamental group the two independent Kummer classes give a homomorphism pi_1(S)->(Z/2)^2. Failure of surjectivity would give a nonzero linear combination of those classes equal to zero. Surjectivity proves connectedness. The same construction algebraically uses the two double-cover algebras O_S plus T and O_S plus sigma^*T, with chosen square trivializations. The resulting pushforward is

    q_*O_Y = O_S plus T plus sigma^*T plus (sigma^2)^*T

as an O_S-module; its algebra multiplication comes from the double-cover construction, rather than from an unchosen direct-sum multiplication. Different square trivializations give isomorphic covers over C. The isomorphism class of the cover depends only on H; no canonical trivializations, basis, or deck lift are claimed.

## 3. The composite is an A4 Galois cover

Because sigma preserves H, it preserves the common kernel of the corresponding two Kummer characters. The associated connected cover therefore admits lifts of sigma to Y. Equivalently, the pullback by sigma has the same Kummer subgroup and is isomorphic to q. Such a lift is an automorphism of Y covering sigma, and its choices differ by K.

The composite f=pi q:Y->L is Galois: its four automorphisms over S together with lifts of each of the three automorphisms of S/L give twelve distinct automorphisms over L, equal to deg f. Its group G fits into

    1 -> K -> G -> <sigma> -> 1.

Conjugation on K is dual to the action on H (possibly with the inverse generator, according to pullback convention). In either convention it cyclically permutes the three nonzero elements of K and has no nonzero fixed element. Choose any lift g of sigma. Then g^3 lies in K and is fixed by conjugation by g, simply because g commutes with its own third power. Hence g^3=1. Its image has order three, so g has order exactly three and gives a splitting. Thus

    G = K semidirect Z/3, with the nontrivial order-three action,
    G isomorphic to A4.

The final identification sends K to the identity and the three double transpositions in A4, with a three-cycle acting by conjugation. The splitting exists but is not asserted canonical. This argument needs neither a lift of sigma to B nor an additional symmetry of the original HM geometry.

The cover q is etale, so Riemann–Hurwitz gives

    2g(Y)-2 = 4(2g(S)-2)=72,  hence g(Y)=37.

The degree-twelve map f has branch locus exactly Omega. Above each of its twelve points are four points of Y, each with ramification index three. Its inertia groups are cyclic of order three. Independently,

    2g(Y)-2 = -24 + 12*4*(3-1)=72.

In particular the cover is etale over S, not over P1.

## 4. The individual double cover and its normal closure

Let X_T->S be the connected etale double cover defined by T. It has genus 1+2(10-1)=19. The composite X_T->L has degree six and is not Galois. In the A4 extension just constructed its subgroup is the order-two subgroup ker(K->mu_2) determined by T. The three such order-two subgroups are permuted by sigma and have trivial intersection, so this subgroup is not normal and has trivial core. Consequently Y->L is exactly the normal closure of X_T->L, not merely some Galois cover dominating it.

This also gives a direct interpretation of the obstruction: the individual double cover associated with the actual T is not deck-invariant over the cubic base cover, while the cover generated by its three conjugates is.

## 5. A balanced tetragonal quotient

Choose a lift g as in Section 3, and form the smooth projective quotient C=Y/<g>. Write h:C->L for its induced map. Since <g> has order three in A4, h has degree four and is not Galois. The permutation action of A4 on the four cosets of <g> is its usual degree-four action. Each inertia generator has order three and acts as a three-cycle with one fixed point. Thus h has profile (3,1) over each point of Omega and no other branching. Riemann–Hurwitz gives

    2g(C)-2 = -8 + 12*(3-1)=16,  hence g(C)=9.

There is also an exact splitting, not only a degree count:

    h_*O_C = O_L plus V tensor O_L(-4).

To prove this, push the decomposition in Section 2 along pi. On its summand pi_*O_S the g-invariant part is O_L, since g acts there through sigma. The other three summands pi_*T, pi_*sigma^*T, and pi_*(sigma^2)^*T are cyclically permuted by g. Their invariant part maps isomorphically to any one of them by projection: the other two components of an invariant section are forced by its first component, and the sole consistency condition is g^3=1. Finally

    pi_*T = pi_*(B tensor pi^*O_L(-4)) = V tensor O_L(-4).

Taking invariants is exact in characteristic zero and gives the pushforward from the quotient. This proves the splitting. Its second summand is trace-free: every nontrivial K-character summand has zero trace for Y->S, hence for Y->L, and restriction to <g>-invariants divides this latter trace by three. Thus the usual Tschirnhausen bundle (h_*O_C/O_L)^dual is O_L(4)^3, balanced. As a separate genus check, chi(O_C)=chi(O_L)+3chi(O_L(-4))=1-9=-8.

The choice of g and the displayed identifications need not be canonical. The existence of this tetragonal quotient and its balanced splitting are independent of any further lift of HM symmetries. No assertion about a Prym or Recillas correspondence is needed.

## Contribution and limits

The actual spectral line cannot be made invariant under the cubic deck action, even after a base-line twist. Any simplification requiring a global conjugacy M~zeta_3 M, or a deck linearization of B or Theta, is therefore rigorously excluded. The next structural objects are the connected genus-37 A4 cover, the genus-19 double cover whose normal closure it is, and a genus-nine tetragonal quotient with exactly balanced Tschirnhausen bundle O_L(4)^3.

No A5 lift or compatibility with additional HM symmetries is asserted. No torsion class is transferred to the genus-four support D. This does not evaluate the actual R-class, its final contraction or second-symbol quotient, the third Bockstein, or any source-instance or algebraicity claim. Those remain separate open questions.
