# The actual Gamma lies on the smooth Clebsch cubic

## Statement and scope

Work over C with E=F(3), U=H0(P4,E), and the actual evaluation-kernel curve Gamma in P(U*). On the established open used in PR543, Gamma is the smooth nondegenerate rational sextic of KAPPA-RATIONAL-SEXTIC.md. The following is a coefficient-free consequence of its actual normalizer action:

**Theorem.** The actual Gamma lies on exactly one cubic surface Sigma in P(U*), and it is the smooth A5-invariant Clebsch diagonal cubic. In particular Gamma is an effective Cartier divisor on Sigma, and

    H.Gamma=6,  Gamma^2=4,  K_Sigma=-H,
    O_Gamma(Gamma)=O_P1(4),
    0 -> O_P1(4) -> N_Gamma/P3 -> O_P1(18) -> 0.

Here canonical means that the one-dimensional invariant cubic equation space is intrinsic; its equation is determined only up to scalar. No splitting of the displayed normal extension is asserted. No choice of original HM coefficients, source matrices, minors, or ranks is made.

## 1. Actual source and representation audit

Coordination was read through PR1 comment 6318027515 (2026-10-21 14:03:48 UTC). This work concerns null's secondary Gamma geometry and full-adjoint extension interface, not Mr. Slop's primary Picard/conductor calculation.

The current immutable source is PR543 at

    6aff2e69c524f3888d35d703a4bbfb04e7a9066f,

research/hm/order-four-quadratic-load/KAPPA-RATIONAL-SEXTIC.md. That theorem identifies Gamma with each chosen HM component line L by an equivariant isomorphism kappa_L and proves

    kappa_L* O_P(U*)(1)=O_L(6).

Its normalizer input is the actual bundle representation, not an abstract four-dimensional guess. Specifically, PR557 at

    212f18bb3afb52171068d1aaf8a0dbfbf9954d2b,

research/hm/sextic-alpha-exclusion/ALPHA-EXCLUSION.md, pins Horrocks–Mumford (1973), equation (4.12), printed page 74, and the character table on printed page 81. These primary-source portions were read again for this deduction. They give U the irreducible character chi_4, with central -I acting with trace +4. This is NOT the other four-dimensional character chi_4^*, whose central trace is -4. The same section proves the Heisenberg action on U is trivial.

Because -I is an involution and has trace equal to dimension, it acts as the identity. The actual SL2(F5) action therefore descends to A5. The character on the A5 classes of orders 1,2,3,5,5 is

    (4,0,1,-1,-1).

Let V be the sum-zero hyperplane in the five-dimensional permutation representation of A5. Its character is the number of fixed letters minus one, which is exactly (4,0,1,-1,-1). Hence U and U* are each A5-isomorphic to V. This identifies the representation used below from actual source data. The invariant pairing on V identifies its dual with V; no coordinate identification of the original HM source is required.

The action on Gamma is faithful. Indeed the actual projective A5 action on P(U*) is faithful, and a projective transformation fixing the nondegenerate irreducible Gamma pointwise must be scalar: its fixed locus is a union of projective eigenspaces, so irreducibility and nondegeneracy force the whole ambient space to be one eigenspace. Via kappa_L, Gamma has a faithful A5 action on P1.

Primary source:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

Repository source:
https://github.com/Akilleez-QA/read-em-and-weep/blob/6aff2e69c524f3888d35d703a4bbfb04e7a9066f/research/hm/order-four-quadratic-load/KAPPA-RATIONAL-SEXTIC.md

Representation audit source:
https://github.com/Akilleez-QA/read-em-and-weep/blob/212f18bb3afb52171068d1aaf8a0dbfbf9954d2b/research/hm/sextic-alpha-exclusion/ALPHA-EXCLUSION.md

## 2. The invariant cubic space and its smooth equation

Use only the universal standard representation V={x_1+...+x_5=0}. This is a representation-theoretic model, not a choice or evaluation of actual HM coefficients. Put

    p_3=x_1^3+...+x_5^3.

Its restriction to V is nonzero and A5-invariant. Moreover every A5-invariant cubic on V is a multiple of it. Here is a direct proof avoiding an imported invariant table.

An invariant cubic on V has an A5-invariant lift to C[x_1,...,x_5]_3, by averaging any lift over the finite group. Any A5-invariant homogeneous polynomial of degree less than ten is S5-invariant. To see this, for one odd permutation tau write f as its tau-symmetric and tau-antisymmetric parts. The latter is invariant under A5 and changes sign under every odd permutation, hence is alternating. Each x_i-x_j divides it, so their degree-ten product divides it. In degree three this part is zero.

Symmetric cubics are spanned by p_1^3, p_1 p_2, and p_3. On p_1=0 only p_3 survives. This proves the invariant cubic space has dimension one and constructs its intrinsic surface Sigma.

It is smooth. A singular projective point of p_3=0 on the hyperplane p_1=0 would have gradients proportional, hence

    x_1^2=x_2^2=...=x_5^2.

If the common square is zero, all coordinates vanish, which is not a projective point. Otherwise each x_i equals one of plus or minus a fixed nonzero a. The sum of five such signs is an odd integer, never zero over C. This contradicts p_1=0. Thus Sigma is smooth. This is exactly the standard Clebsch diagonal cubic presentation.

## 3. An orbit-divisor proof of actual containment

A point stabilizer for a finite faithful subgroup of PGL2(C) is cyclic. One proof sends the point to infinity: the stabilizer is a finite affine group; averaging an affine orbit supplies a second fixed point; conjugating that point to zero places the stabilizer in C*. A finite subgroup of C* is cyclic.

The only possible orders of cyclic subgroups of A5 are 1,2,3,5. Consequently every A5 orbit on the faithfully acted-on Gamma=P1 has size

    60,30,20, or 12.

Any nonzero invariant section of O_Gamma(3)=O_P1(18) would have an invariant effective zero divisor of total degree eighteen. Such a divisor is a nonnegative integral sum of full orbits with their constant multiplicities. No nonnegative combination of 12,20,30,60 is eighteen. Therefore this invariant-section space is zero.

Now restrict the actual invariant cubic equation of Sigma to Gamma. The restriction map is equivariant, so the restriction is an invariant section of O_Gamma(3). It must be zero. This is scheme-theoretic containment because Gamma is reduced and the restricted section vanishes identically. Thus Gamma is an effective Cartier divisor on the smooth surface Sigma.

### Why no unverified binary linearization is hidden here

The ambient O(1) has its genuine A5 linearization from the actual linear representation U*. Its pullback to Gamma is O_P1(6), and its third power is the actual linearized O_P1(18) used above. The zero-divisor argument needs only this genuine linearization and faithful projective action, not any arbitrary lift to a binary group. Even a semi-invariant section would have an invariant zero divisor and give the same contradiction.

Equivalently, pull back the projective A5 action through SL2(C)->PGL2(C). Its binary icosahedral double cover acts naturally on O_P1(6); the central -I acts by (-1)^6=+1, so the linearization descends to A5. Two A5 linearizations of the same line bundle differ by a character; A5 is perfect and has no nontrivial characters. Therefore the actual pullback is this unique even-degree linearization. This verifies, rather than assumes, the proposed binary-invariant-degree-eighteen route. The orbit proof replaces the need to quote its invariant-ring presentation.

## 4. Cartier and normal consequences

Adjunction on the smooth cubic gives K_Sigma=-H. Since Gamma is a rational degree-six curve,

    -2=(K_Sigma+Gamma).Gamma=-6+Gamma^2,

hence Gamma^2=4. Its normal line in Sigma is O_Gamma(Gamma)=O_P1(4). The smooth normal sequence for Gamma subset Sigma subset P3 gives

    0 -> O_P1(4) -> N_Gamma/P3 -> O_Gamma(3) -> 0,

where the last term is O_P1(18). In particular det N_Gamma/P3=O_P1(22), recovering the degree used in the existing global conductor calculation by a stronger geometric description. The extension class, and hence the splitting of N_Gamma/P3, is not determined here.

## 5. There is no second cubic through Gamma

We first record the needed linearization obstruction without confusing genuine and projective representations.

**Parity lemma.** Every genuinely A5-linearized line bundle on a faithfully acted-on P1 has even degree.

Let K=C(P1). The extension K/K^A5 is Galois with group A5. A linearized line bundle has a one-dimensional semilinear generic fiber over K. By Hilbert theorem 90, or equivalently Galois descent for a one-dimensional vector space, that generic fiber has a nonzero invariant rational section. Its divisor is invariant. Every point orbit has one of the even cardinalities 12,20,30,60 computed above, so any invariant divisor, allowing negative coefficients, has even degree. The degree of the line bundle is therefore even.

For an explicit justification of the descent step, choose a rational generator s and write g(s)=a_g s. The averaging operator on rational sections sends f s to (sum_g a_g g(f))s. Distinct field automorphisms are linearly independent over K, so this operator is not identically zero; some f gives a nonzero invariant rational section. This uses only the faithful action on the function field and the genuine cocycle identity of the linearization.

There is no nonzero A5-invariant effective curve divisor of degree at most three on Sigma. Such a divisor has at most three distinct irreducible components. The induced homomorphism A5 to their permutation group is trivial by simplicity and order, so each component is invariant. The linear span of each component is an invariant projective linear subspace. Irreducibility of U* forces that span to be all P3. Its degree is consequently at least three; the only remaining case is an integral nondegenerate degree-three curve. Such a curve is a smooth twisted cubic (equivalently its arithmetic genus is zero by the degree-three Castelnuovo bound). Its O(1) would be O_P1(3) with the genuine A5 linearization inherited from P(U*). The action is faithful by nondegeneracy. The parity lemma excludes this odd degree.

Now let D=3H-Gamma on Sigma. It has

    H.D=3,  D^2=27-36+4=-5.

If |D| were nonempty, it would have a nonzero fixed divisorial part. Indeed a linear system without a fixed curve has two members with no common curve component, whose intersection is nonnegative, contradicting D^2<0. The fixed divisorial part is canonical and hence A5-invariant, since D is an invariant divisor class. It has degree at most H.D=3. The preceding paragraph excludes it. Thus H0(Sigma,O_Sigma(3H-Gamma))=0.

The cubic restriction sequence

    0 -> O_P3 -> I_Gamma(3) -> O_Sigma(3H-Gamma) -> 0

therefore gives h0(I_Gamma(3))=1. The Clebsch cubic is the unique cubic containing the actual Gamma, not merely the unique invariant cubic.

## 6. Exact ideal regularity and its coefficient-free resolution

There is no quadric through Gamma: multiplying any nonzero quadric equation by the four independent ambient linear forms would give four independent cubics through Gamma, contradicting Section5. Hence the coordinate Hilbert function in degrees 0,1,2 is 1,4,10. In degree three it is 20-1=19, equal to h0(O_Gamma(3)); therefore H1(I_Gamma(3))=0.

The two other conditions for 4-regularity are

    H2(I_Gamma(2))=H1(O_P1(12))=0,
    H3(I_Gamma(1))=0.

Thus I_Gamma is 4-regular. Its graded ideal is generated in degrees at most four, with one cubic and six minimal quartics: h0(I_Gamma(4))=35-25=10, and the cubic's four linear multiples are independent. Its coordinate Hilbert function is 6n+1 for every n>=3.

Let R=C[x_0,x_1,x_2,x_3] and I the saturated homogeneous ideal. The Hilbert numerator of R/I is

    1-t^3-6t^4+9t^5-3t^6.

The homogeneous coordinate ring is a domain of dimension two and depth at least one, so I has projective dimension at most two. In a minimal resolution there is no first syzygy of degree four: a relation among linear multiples of the single cubic and constant multiples of chosen minimal quartics would contradict their minimality. Regularity bounds every first syzygy degree by five. Therefore all first syzygies have degree five. Minimality and regularity then force all second syzygies to have degree six. The Hilbert numerator determines their multiplicities. The exact minimal resolution is

    0 -> R(-6)^3 -> R(-5)^9
      -> R(-3) directsum R(-4)^6 -> I -> 0.

All maps are the actual ideal maps of Gamma, not generic matrices. Their coefficients, chosen bases, and the induced ambient cohomology maps are not computed here. The proof determines the resolution's exact shape, not an automatic rank statement for a map obtained by applying another functor.

## 7. Exact upgrade of the ambient extension gate

Use the notation of AMBIENT-EXTENSION-CUBIC-REDUCTION.md: f:Xhat->P3 is flat, A=f*O(1), M=O_Xhat(2L-H), S=f^{-1}(Gamma), and put T=f^{-1}(Sigma). Let f_T:T->Sigma be the restricted flat morphism.

Because Gamma is Cartier on Sigma, flat pullback now identifies the previously unresolved ideal sheaf exactly:

    I_{S/T}=f_T* O_Sigma(-Gamma).

Thus S is an effective Cartier divisor on T, even though T itself need not be smooth or normal. The actual extension boundary has the line-bundle form

    H0(S,M|S) -> H1(T,M|T tensor f_T*O_Sigma(-Gamma)).

The established acyclicity of M(-3A) still gives H^i(Xhat,M)=H^i(T,M|T). Therefore the kernel of this boundary is exactly the actual ambient section space, using the previously proved injectivity of its restriction to S. No descent section is assumed extendable; no boundary rank or vanishing is asserted.

## Boundaries

This proves actual smooth Clebsch containment, uniqueness of its containing cubic, the Cartier upgrade, and the exact ideal-resolution shape. It does not yet identify Gamma with a specific conic class after choosing a six-line contraction, and it does not determine the normal-extension class, the splitting of K4, or the actual adjoint boundary. The primitive twist-four obstruction, prescribed source membership, higher lifting, and full proof repair remain open. There were no external writes or selected-instance experiments.
