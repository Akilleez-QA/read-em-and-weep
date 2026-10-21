# Original-polarization curve realization and forced loss of sections

Work over C. Let V=V51 and L0=O_V(1), the ample line bundle of its canonical cubic embedding V in P9. This concerns V, not the original primary surface or the full-adjoint problem.

## Pinned inputs

- PR611, commit 12b28d33627cc0e8b283d142dc16439a51bb5e00: V is projective and integral, L0 is ample, and H2(O_V)=0.
- PR614, commit 73fbf75838c91804ca637b5916d6aac217240958: abstract deformations are unobstructed, dim T1(V)=576, and H0(Theta_V)=0.
- PR615, commit 24bc9b741c287f8ac207bd9df4de4c07c50bea2f: h0(L0)=10 and the complete system gives the stated embedding.
- PR622, commit c6a7c691f8ecd8562505546f993c755fb03b24fb: every embedded Artin deformation of V in P9 is a projective translate reducing to the identity; in particular its underlying marked abstract first-order class is zero.
- PR627, commit 7c3f76f2e55c5cc0c3356972b5d7d676544c943a: the nonempty open T_free in T1(V) consists of classes fixed by no nonidentity element of Aut(V). Every such class extends formally.
- PR628, commit f08ff9c2760e4aef074cfe716b923d29d5e7ebe8: every compatible polarized formal system (X_n,L_n), with L_0=L0, is effective as a projective flat finitely presented pair (X,L) over C[[t]]. Compatible L_n exist by H2(O_V)=0.
- PR629, commit 3ad872801158107d8fa71fa578f2ea948efd9f25: finite-jet algebraic-curve approximation using a Hilbert scheme and Artin approximation; fixed-base automorphism triviality depends only on matching a class in T_free.

All PR links are https://github.com/Akilleez-QA/read-em-and-weep/pull/ followed by the displayed number. The conclusions below are conditional on these pinned inputs.

## 1. Realization retaining the original line bundle

Theorem. Let (X_n,L_n) be any compatible marked polarized formal deformation of (V,L0) over C[t]/(t^(n+1)). For every N>=1 there exist a smooth integral finite-type C-curve B, a point b in B(C), an etale map q:B -> A1 with q(b)=0, a projective flat finitely presented family f:Y -> B, and an f-ample invertible sheaf M on Y such that

    (Y,M) modulo t^N is isomorphic to (X_(N-1),L_(N-1)),

where t=q^*(coordinate), and the isomorphism respects the special-fiber marking. Thus the original polarization itself, not merely an unspecified power, is retained on the prescribed jet. B and the pair may depend on N.

Proof. Put A=C[[t]]. Use PR628 to algebraize the whole chosen polarized system to (X,L)/A. Choose one sufficiently large integer m so that both L^m and L^(m+1) are relatively very ample and admit embeddings

    i_m:X -> P^r_A,       i_(m+1):X -> P^s_A

with their pullback O(1)'s identified with these powers. This is the standard eventual very-ampleness property of an ample invertible sheaf on a projective scheme over a Noetherian affine base. The product i=(i_m,i_(m+1)) is a closed immersion: it is the graph of i_(m+1) over the first closed immersion, and projective space is separated.

Let Z=P^r_C x P^s_C, with its Segre embedding and ample O_Z(1,1). The embedded X is an A-point alpha of the finite-type projective Hilbert scheme H=Hilb^P(Z), where P is its Hilbert polynomial for O_Z(1,1). One may regard H as the closed Hilbert subscheme inside the Hilbert scheme of the Segre ambient projective space, imposing containment in the fixed closed subscheme Z. Its universal family U is a closed subscheme of Z x H and is projective and flat over H.

Crucially there is an actual invertible sheaf on this entire universal family:

    M_univ = O_Z(-1,1)|_U.

On the A-family it pulls back to L^(-m) tensor L^(m+1)=L, with the chosen isomorphism. No extraction of an m-th root in a relative Picard group is needed. The two consecutive powers retain the information discarded by a single-power embedding.

Choose an affine finite-type neighborhood H0 of alpha(0). Since Spec A is local, alpha factors through H0. Present H0 by finitely many polynomial equations over C. Artin approximation over the G-ring R=C[t]_(t), with completion A, gives an exact solution on a pointed etale R-neighborhood congruent to alpha modulo t^N. Here the precise result is [Stacks 07QZ](https://stacks.math.columbia.edu/tag/07QZ). Spreading its finite presentation and its finitely many solution coordinates over C[t,1/g], with g(0)!=0, gives a finite-type curve etale over an open subset of A1 and a morphism beta:B -> H0. Restrict to the connected component containing the distinguished point b. This is smooth and integral: a regular curve's distinct irreducible components are disjoint, hence open and closed. The residue field at b is C, and the completed local parameter is t. This is exactly the finite-presentation spreading step in PR629.

Pull back (U,M_univ) along beta, obtaining (Y,M). Agreement of the Hilbert points modulo t^N is agreement of the embedded subschemes inside the fixed Z, not just agreement of their abstract isomorphism classes. Consequently restriction of the fixed O_Z(-1,1) gives the required isomorphism of pairs on that jet. In particular M_b=L0 is ample.

Finally shrink B around b so that M is relatively ample. This is justified by [Stacks 0D2S](https://stacks.math.columbia.edu/tag/0D2S): for a proper family, an invertible sheaf ample on one fiber is relatively ample over a neighborhood of that fiber. This shrinking preserves the pointed etale curve, the matching jet, and projectivity and flatness of Y. The theorem follows.

The auxiliary equalities M^m=O_Z(1,0)|_Y and M^(m+1)=O_Z(0,1)|_Y need not hold on the whole approximating family; they hold on its prescribed jet. Neither equality is required for the theorem. Relative ampleness comes from the preceding openness argument, not from an unproved extension of those equalities.

## 2. Symmetry-breaking specialization

Take N>=2 and a formal system whose abstract first-order class v lies in T_free. The preceding theorem matches v. Every automorphism of any positive Artin reduction of Y restricts to gamma in Aut(V) fixing v, hence gamma=1. Each successive identity-reducing kernel is H0(Theta_V) tensor the square-zero base ideal and is zero. Thus all these scheme automorphism groups are trivial. Proper formal faithfulness over O_(B,b), followed by flat schematic density over integral B, gives

    Aut_(O_(B,b))(Y_(O_(B,b)))=1,       Aut_B(Y)=1,

as proved in detail in PR629. These are scheme automorphisms fixing the base. If a polarized automorphism is defined as a scheme automorphism together with a chosen isomorphism of line bundles, scalar automorphisms of the line bundle still exist; no assertion that that unrigidified pair-automorphism group is trivial is intended.

## 3. Nonzero abstract motion forces degree-one section loss

Proposition. Let (Y,M)/B be any projective flat family over a smooth integral pointed curve as above with M_b=L0 and nonzero marked abstract first-order class v. Then

    h0(Y_eta,M_eta) <= 9,

where eta is the generic point. In particular this applies to every symmetry-breaking family of Section 2. The original polarization persists and remains ample, but its ten special-fiber sections cannot all persist.

Proof. Work over the DVR D=O_(B,b), with fraction field K and uniformizer t. Let E=H0(Y_D,M). Properness makes E a finite D-module. Flatness of Y_D and invertibility of M imply multiplication by t on M is injective, hence E is torsion-free and therefore free over D. Its rank d equals h0(Y_K,M_K), since localization, being flat base change, commutes with H0 here.

The sequence 0 -> M --t-> M -> L0 -> 0 gives an injection

    E/tE -> H0(V,L0).

Hence d<=10. If d=10, this injection is an isomorphism. A D-basis of E therefore restricts to a basis of the complete ten-dimensional special-fiber system. Restrict these ten sections to Y_1 over D/(t^2). They generate M_1 by Nakayama: the cokernel of evaluation is coherent and zero modulo the nilpotent ideal (t). They define a morphism

    g_1:Y_1 -> P9_(D/(t^2))

whose special fiber is the original embedding V -> P9, after identifying the chosen basis with that system. The morphism is proper because Y_1 is proper and the target is separated. It is quasi-finite since the spaces have the same underlying points as their special fibers. A proper quasi-finite morphism is finite. Its direct-image algebra quotient O_(P9) -> (g_1)_*O_(Y_1) is surjective modulo t, and hence surjective by nilpotence; finite pushforward commutes with this base change. Therefore g_1 is a closed immersion.

Y_1 is flat over D/(t^2), so it is an embedded first-order deformation of V in P9. PR622 says it is a projective coordinate translate of the constant family, reducing to the identity. Its underlying marked abstract first-order class must be zero, contradicting v!=0. Thus d cannot equal 10, proving d<=9.

The argument is independent of which compatible lift of L0 was chosen. It does not claim a specific surviving section or an exact generic value of h0. After shrinking to a nonempty open of B, semicontinuity gives the same at-most-nine bound on all its fibers; no selected evaluation is involved.

## Contribution and limits

The two-consecutive-power Hilbert construction closes the original-polarization omission in PR629. It realizes every chosen finite polarized formal jet on a finite-type curve, without a Picard-root assumption. The section-loss proposition explains why this does not contradict the complete P9 embedded rigidity: actual abstract motion with this ample line bundle necessarily loses at least one of the original ten sections.

No claim is made that the entire initial formal arc descends unchanged, that the generic-fiber automorphism group is trivial, that every generic fiber has a specified embedding, or that the original HM/full-adjoint/prescribed-source/higher-lifting/Weil-class algebraicity problems are solved. No selected source coefficients, points, derivatives, matrices, ranks, or large computations are evaluated. This is an authored mathematical proof conditional on pinned inputs, not proof-assistant verification.
