# Independent review: exterior derivations detect the column channel

## Verdict and assumptions

The universal exterior-algebra lemma and its application to the actual column W0 channel are correct over C, conditional on the actual equivariant decompositions and Koszul description pinned in PR526 (commit c887d466428bced729a73bbc8578a889e9ecaf45) and the single-channel reduction in the accompanying column-single-channel proof. This is an independent hand proof, not a proof-assistant verification. No selected source-instance evaluation, numerical rank experiment, or coefficient search is used.

## 1. Elementary proof of the universal lemma

Let T have dimension five and L:T -> exterior^2 T. Define

D_L(a wedge b wedge c) = L(a) wedge b wedge c - L(b) wedge a wedge c + L(c) wedge a wedge b.

Suppose D_L=0. Fix a basis e_1,...,e_5. For distinct i,a,b, let j,k be the remaining two indices. In D_L(e_i wedge e_j wedge e_k), the coefficient on the four-form with indices a,b,j,k can come only from the L(e_i) term: each other term contains e_i. Hence the coefficient of e_a wedge e_b in L(e_i) is zero.

It follows that L(e_i)=e_i wedge v_i, where v_i is unique modulo e_i. For fixed a, put b_i=(v_i)_a for i different from a. The equation D_L(e_i wedge e_j wedge e_k)=0, for a triple avoiding a, says b_i+b_j+b_k=0. There are four indices different from a. Subtracting these four three-term equations shows all b_i are equal; any equation then gives 3b_i=0. Thus b_i=0 in characteristic zero. This holds for every a, so L=0. Since both Hom(T,exterior^2 T) and Hom(exterior^3 T,exterior^4 T) have dimension fifty, L -> D_L is an isomorphism.

## 2. Exact coordinate-free inverse and signs

Choose a nonzero volume covector omega in exterior^5 T*. For A:exterior^3 T -> exterior^4 T define Phi(A):T -> exterior^2 T by

omega(Phi(A)(v) wedge alpha) = omega(A(alpha) wedge v).

This uses the perfect exterior pairing and defines a natural identification independent of rescaling omega. Let c(L)=sum_i contraction(e_i*,L(e_i)), and kappa(z)(v)=z wedge v. Extending L to the degree-one odd derivation on the whole exterior algebra gives on four-forms beta the identity D_L(beta)=-c(L) wedge beta. This identity is checked on the basis four-forms: only components of L(e_i) containing e_i contribute, with precisely the displayed negative contraction sign.

Apply the derivation rule to alpha wedge v, with alpha of degree three:

D_L(alpha wedge v)=D_L(alpha) wedge v-alpha wedge L(v).

Pairing with omega yields Phi(D_L)=L+kappa(c(L)). Moreover c(kappa(z))=-4z, so this endomorphism has eigenvalue 1 on ker c and eigenvalue -3 on im kappa. Its inverse is id+(1/3) kappa c. In particular, the elementary injectivity proof and the coordinate-free formula agree.

## 3. Nonvanishing of the actual projected Koszul differential

Use the actual equivariant isomorphism p:E tensor W0 -> exterior^2 T. Define

Psi:E tensor exterior^2 T -> Hom(W0,exterior^4 T),
Psi(e tensor alpha)(w)=p(e tensor w) wedge alpha.

Psi is equivariant and nonzero: for nonzero e,w the image p(e tensor w) is nonzero, and the exterior pairing of two-forms into four-forms is nondegenerate in the elementary sense that every nonzero two-form wedges nontrivially with some two-form. The target identifies with V tensor W0, using exterior^4 T=V and W0*=W0 in the actual normalizer representation. The target occurs with multiplicity one in E tensor exterior^2 T=V tensor (W0+Qspin+T4). Therefore Psi is a nonzero scalar multiple of the actual W0 projection.

At an arbitrary parameter lambda, trivialize the one-dimensional O(2) fiber. The degree-two column multiplication mu_lambda:Sym^2 T -> E is nonzero (indeed surjective by the established column Hilbert function). Before removing boundaries, its degree-four Koszul differential is

delta_lambda(t tensor a wedge b wedge c)=mu_lambda(t,a) tensor b wedge c-mu_lambda(t,b) tensor a wedge c+mu_lambda(t,c) tensor a wedge b.

If Psi delta_lambda were zero, fix any nonzero w in W0 and any t in T. Then the map L_t(a)=p(mu_lambda(t,a) tensor w) would satisfy D_(L_t)=0. Section 1 implies L_t=0. Since p(- tensor w) is injective, mu_lambda(t,a)=0 for every t,a, a contradiction. Thus Psi delta_lambda is nonzero for every parameter.

The preceding Koszul boundary is the standard exterior^4 T summand. Its composite with delta_lambda is zero because mu_lambda is symmetric, with pairwise cancellation. Therefore the nonzero composite descends to the reduced source. In the parity-block decomposition, only R6 maps to the W0 summand. Its reduced component is precisely gamma:R6 tensor O -> W0 tensor O(2). Consequently gamma is not identically zero. This proves the nonvanishing of the actual scalar, not merely existence of a possible intertwiner.

## 4. Contribution and limits

Combining this nonvanishing with the single-channel reduction excludes the constant-u=10 alternative. Together with that reduction's exclusion of constant-u=5 and the established jump classification, det(beta) is nonzero and u is zero away from the reduced twelve-point orbit Omega and five on Omega.

This conclusion concerns the column Koszul parameter. It does not solve the separate fixed-pair residual, higher-order lifting, or algebraicity questions. The argument is structural and valid at an arbitrary parameter, not an evaluation of a chosen actual HM instance.

## 5. Review of the full authored candidate

Independently read the complete candidate PROOF.md with SHA256 17b526e19da077856ec5227a853d85f88368b865ca7538ab43726d77445538f3. Approved conditional on its pinned inputs, including the now-pinned single-channel commit de70cfc2807897b350aeda600e552f6b6a93a300. Its choice L(e_i)=v_i wedge e_i has the opposite v_i sign to Section 1 above and yields the displayed positive triple sum correctly. Its contradiction needs only that Psi is some scalar multiple of the W0 projection; the stronger nonzero claim supplied above is not required for that direction.

The sheaf consequence is also correct. The determinant of beta has a simple zero at each point of Omega, so the DVR Smith exponents sum to one, yielding a length-one cokernel there. Generic invertibility and torsion-freeness of the domain imply zero kernel sheaf. The block decomposition then gives coker(phi)=O(8) direct sum coker(beta), with length twelve torsion. Tensoring with the five-dimensional constant V gives rank-five locally free contribution V tensor O(8) and torsion length sixty. The distinction between zero kernel sheaf and five-dimensional exceptional fiber kernels is maintained correctly, and no flatness assertion is made.

No mathematical correction or additional unproved nonvanishing dependency was found in this candidate.
