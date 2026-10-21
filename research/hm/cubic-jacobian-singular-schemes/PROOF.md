# Intrinsic Jacobian singular schemes of the transverse cubic images

Status: independently mathematically reviewed (PASS); see REVIEW.md. Not formally checked. All arguments are universal symbolic algebra. No actual HM/source coefficients, actual matrices, point evaluations, numerical rank tests, scans, or computer algebra are used.

## 1. Input and theorem

The reviewed local result is pinned at Akilleez-QA/read-em-and-weep PR611, commit `12b28d33627cc0e8b283d142dc16439a51bb5e00`, `research/hm/cubic-branch-transversality/PROOF.md`, Sections 1, 4 and 5 ([immutable source](https://github.com/Akilleez-QA/read-em-and-weep/blob/12b28d33627cc0e8b283d142dc16439a51bb5e00/research/hm/cubic-branch-transversality/PROOF.md)). The pinned theorem supplies the following inputs over C. The reduced cubic images V and T have dimensions 4 and 2 respectively. They are smooth outside the same set Sigma of sixty reduced closed points. At every point of Sigma, their completed algebraic local rings are, respectively, A_4 and A_2, where for every integer d >= 1

    A_d = C[[u_1,...,u_d,v_1,...,v_d]]/(u_i v_j : 1 <= i,j <= d)
        = C[[u_1,...,u_d]] x_C C[[v_1,...,v_d]].

The conductor in each completed ring is its maximal ideal m. That result distinguishes this reduced conductor from the potentially nonreduced singular scheme. No new geometric input about the original surface is needed here.

For a pure d-dimensional complex variety Q, define its intrinsic Jacobian singular ideal and scheme by

    J_Q = Fitt_d(Omega_{Q/C}),       Sing_J(Q) = V(J_Q).

We use the convention that a presentation R^a -> R^b -> M -> 0 defines Fitt_k(M) by the (b-k)-minors of the presentation matrix. Thus Fitt_d of a rank-d free module is the unit ideal. Fitting ideals are independent of presentation and commute with base change; they define coherent ideal sheaves. See the Stacks Project, [Fitting ideals](https://stacks.math.columbia.edu/tag/07Z6) and [Fitting ideal sheaves](https://stacks.math.columbia.edu/tag/0C3C).

**Theorem.** For any essentially finite type complex local ring R with residue field C and completed C-algebra isomorphic to A_d,

    Fitt_d(Omega_{R/C}) = m_R^d.

In particular, writing I_Sigma for the reduced point ideal on the indicated variety,

    J_V = I_(Sigma/V)^4,           J_T = I_(Sigma/T)^2.

The local lengths of the two singular schemes at each point of Sigma are 69 and 5, respectively. Their total lengths are 4140 and 300. Their reduced support is Sigma, but neither Jacobian singular scheme equals the reduced conductor scheme.

## 2. The differential module that completion permits

Care is required: throughout this proof, the differential module of a completed local ring means continuous differentials with values in finite, adically complete modules. We never replace it by the unrestricted algebraic Kähler differential module of a formal power-series ring.

Let (R,m_R) be as in the theorem and let A be its completion. The finite A-module

    E = Omega_{R/C} tensor_R A

represents continuous C-derivations from A into finite A-modules N with their maximal-ideal-adic topology. Here are the details. A C-derivation delta:R->N satisfies

    delta(m_R^n) subset m_R^(n-1) N,       n >= 1,

by the product rule. It is therefore continuous and extends uniquely to a continuous C-derivation A->N, since N is complete and separated. The product rule passes to limits. Conversely every continuous derivation A->N restricts to R. The ordinary universal property on R and extension of scalars identify these derivations with Hom_A(E,N). This also shows that a continuous C-algebra isomorphism of completions preserves E up to canonical representing-module isomorphism. An isomorphism of complete local C-algebras is continuous because it preserves maximal ideals and their powers.

For S=C[[u_1,...,u_d,v_1,...,v_d]], continuous derivations into a finite A_d-module are uniquely specified by the images of the 2d variables: termwise formal differentiation converges in N, and every continuous derivation has this formula by approximation with polynomials. Such a derivation factors through A_d precisely when it annihilates the generators u_i v_j of the kernel. Indeed the product rule then annihilates every finite S-linear combination of these finitely many generators. Consequently the finite module representing these continuous derivations is

    E_d = coker(A_d^(d^2) -> A_d^(2d)),
    e_ij |-> v_j du_i + u_i dv_j.                       (1)

The representing property for finite modules identifies E with E_d after the given completed-ring isomorphism. For completeness, uniqueness needs no category of infinite modules: both representing modules are finite, so evaluating the natural Hom identifications on E and E_d and their identity maps gives mutually inverse module maps. Thus (1) really computes the completion of the original finite algebraic differential module, not a different differential theory.

## 3. The universal minor computation

Write m=(u_1,...,u_d,v_1,...,v_d) in A_d. Present (1) with a d^2-by-2d relation matrix, whose row (i,j) has v_j in column du_i, u_i in column dv_j, and zero elsewhere. Transposing this matrix gives the presentation-map convention and does not change its minor ideals. There are 2d generators, so Fitt_d(E_d) is its ideal of d-by-d minors.

Every entry belongs to m. Every d-by-d determinant is therefore in m^d. Hence

    Fitt_d(E_d) subset m^d.                              (2)

Conversely fix any sequence i_1,...,i_d in {1,...,d}; repetitions are permitted. Select the d distinct relation rows (i_j,j), j=1,...,d, and the d columns dv_1,...,dv_d. The submatrix is diagonal with entries u_(i_1),...,u_(i_d). Its determinant is the arbitrary pure degree-d monomial

    u_(i_1) ... u_(i_d).

Similarly, selecting relation rows (i,j_i), i=1,...,d, and columns du_1,...,du_d gives the arbitrary pure degree-d monomial v_(j_1)...v_(j_d). The rows remain distinct even when selected indices repeat, because their other indices are distinct.

Every mixed u-v monomial vanishes in A_d. Thus m^d is generated by precisely these pure degree-d monomials. They are all minors, so (2) is an equality:

    Fitt_d(E_d) = m^d = m_u^d direct-sum m_v^d.          (3)

The diagonal-minor argument avoids any cancellation or generic-rank assumption. It works also for d=1, where the usual node has reduced Jacobian singular scheme.

## 4. Faithfully flat descent and the global ideal

Fitting ideals commute with base change. Applying this to R->A and using Section 2 gives

    Fitt_d(Omega_{R/C}) A = Fitt_d(E_d) = m_A^d
                         = (m_R^d) A.

The completion of a Noetherian local ring is faithfully flat, so equality after extension implies equality of these ideals in R. This proves the local theorem without requiring the formal branch coordinates to algebraize. At a smooth point of Q of dimension d, Omega_{Q/C} is locally free of rank d, so J_Q is the unit ideal. At a point of Sigma the reduced point-ideal stalk is m_R. Equality of all stalks therefore proves the displayed global ideal identities. These are intrinsic identities on V and T: they do not depend on any embedding into projective or affine space, nor on choices of coordinates or generators for an ambient ideal.

For d>=2, m^d is strictly smaller than m because every element of m^d has order at least d, whereas each u_i has order one. Its radical is m. The Jacobian singular scheme is thus a nonreduced thickening of the conductor point, rather than the conductor itself. Here the phrase “Jacobian singular scheme” always means exactly Fitt_dim(Q)(Omega_{Q/C}); no different singular-locus convention is implicitly asserted to give the same scheme.

## 5. Lengths

A C-basis of A_d/m^d consists of 1 and all pure u-monomials and all pure v-monomials of total degree between 1 and d-1. In d variables the number of monomials of degree at most d-1 is binom(2d-1,d). Hence

    length(A_d/m^d) = 2 binom(2d-1,d) - 1.

Completion preserves the length of these finite-length quotients. For d=4 this is 2*35-1=69; for d=2 it is 2*3-1=5. Since the sixty points are distinct and the singular scheme is supported there, lengths add:

    length(Sing_J(V)) = 60*69 = 4140,
    length(Sing_J(T)) = 60*5  = 300.

## 6. Scope and provenance

This establishes only the intrinsic Jacobian singular ideals and their lengths from the reviewed transverse-branch local model. It does not replace the reduced conductor, alter the prior normalization results, or resolve any separate full-adjoint, prescribed-source, higher-lifting, or algebraicity gate.

