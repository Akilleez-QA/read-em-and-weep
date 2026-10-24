# Rank-one Gauss transforms force an impossible complete-flag degree

## Result and precise scope

For the actual subbundle on T = P^1 in the positive double-hyperplane Gauss gate,

    0 -> E -> V tensor O_T -> Q -> 0,
    dim V = 30,  rank E = 17,  deg E = -54,
    Q = D_lin(1),

its second fundamental form has generic rank at least 2. Consequently the actual positive double-hyperplane multiplication has generic rank at least 26:

    rank(l^2 : M_2,+ -> M_4,+) = 24 + rank(SF_l) >= 26

on a nonempty open subset of the parameter line. Equivalently, on that open set,

    h0(B_(2H_l)(4))_+ <= 15,     dim coker(l^2)_+ <= 11.

This is a lower bound, not maximal rank 13 for SF. It does not improve the rank-36 invariant-cone smoothing bound, determine a Bockstein coefficient, or improve the unresolved generic four-or-five section count. The two specializations remain distinct.

The proof is characteristic-zero geometry of saturated subbundles of a trivial bundle on P^1. It uses no selected HM coefficients, actual matrix/rank evaluations, or local-model experiments.

## 1. The two actual nondegeneracy hypotheses

The actual cohomology description gives

    E = ker[54 O_T(-1) -> 37 O_T].

In particular, H0(E) = 0: E injects into a sum of O_T(-1). Thus E contains no nonzero constant subbundle of V tensor O_T.

The established presentation

    0 -> 41 O_T(-1) -> 54 O_T -> D_lin -> 0

shows that D_lin is locally free and globally generated. Dualizing its quotient map and twisting by O_T(-1) gives

    Q* = D_lin*(-1) -> 54 O_T(-1)

injectively, so H0(Q*) = 0. Consequently E is contained in no proper constant subbundle W tensor O_T of V tensor O_T: otherwise a nonzero constant covector annihilating W would factor through Q, giving a nonzero section of Q*. In this precise sense the fibers of E span all of V.

These properties concern the actual inclusion E -> V tensor O_T and its actual quotient. No splitting type of E or Q is required.

## 2. General rank-one flag theorem

Let k be a characteristic-zero field, let T = P^1_k, let V be an N-dimensional k-vector space, and let

    F subset V tensor O_T

be a saturated rank-r subbundle, where 0 < r < N. Assume

    H0(F) = 0,     H0((V tensor O_T/F)*) = 0.

Write d for the trivial algebraic connection on V tensor O_T and Omega = Omega_T = O_T(-2). The second fundamental form is the O_T-linear map

    beta_F : F -> (V tensor O_T/F) tensor Omega,
    s |-> ds modulo F tensor Omega.

If beta_F has generic rank 1, then there exists a complete flag of saturated subbundles

    0 = F_0 subset F_1 subset ... subset F_N = V tensor O_T,
    rank F_i = i,     F_r = F,

such that

    dF_i subset F_(i+1) tensor Omega                (0 <= i < N)

and each induced morphism of line bundles

    theta_i : F_i/F_(i-1) -> (F_(i+1)/F_i) tensor Omega

is nonzero for 1 <= i < N. In particular,

    deg F <= -r(N-r).                              (1)

All kernels in this construction are sheaf kernels; all forward images are saturated. We do not identify these subbundles' fibers with the possibly enlarged pointwise kernels at ramification points.

### 2.1. Saturation and differentiation

On a nonsingular curve, a coherent subsheaf of a vector bundle is saturated precisely when its quotient is torsion-free; that quotient is then locally free. A saturated subsheaf is uniquely determined by its generic fiber: locally it is the intersection of that generic subspace with the ambient free module.

For any saturated subbundle A of V tensor O_T, set

    A^- = ker(beta_A).

The quotient A/A^- is the image sheaf of beta_A, hence torsion-free. Since (V tensor O_T)/A is also torsion-free, (V tensor O_T)/A^- is torsion-free as well. Thus A^- is saturated in the ambient trivial bundle, and by its definition

    dA^- subset A tensor Omega.                    (2)

Define A^+ as follows. Saturate the image of beta_A in

    ((V tensor O_T)/A) tensor Omega,

tensor this saturated image by Omega^(-1), and take its preimage in V tensor O_T. Then A^+ is saturated, its rank is rank(A) + generic-rank(beta_A), and

    dA subset A^+ tensor Omega.                    (3)

This is an intrinsic definition; choosing a coordinate is unnecessary. Saturating the forward image enlarges the target subbundle rather than introducing a pole. Equation (3) therefore holds as a statement about regular local sections everywhere on T.

Whenever A subset B subset C are saturated subbundles and

    dA subset B tensor Omega,     dB subset C tensor Omega,

differentiation induces an O_T-linear map

    B/A -> (C/B) tensor Omega.                     (4)

Indeed the Leibniz term s df lies in B tensor Omega and vanishes modulo B, while changing a representative by a section of A changes the derivative by a section of B tensor Omega. This proves both O_T-linearity and independence of representatives, without excluding any parameter.

### 2.2. A saturated derivative-invariant subbundle is constant

Suppose A is saturated and beta_A = 0. At the generic point, put K = k(z) and U = A_K subset V tensor K. Then partial_z(U) subset U.

Choose a coordinate projection p : V -> k^a, with a = dim_K U, such that p restricts to an isomorphism on U over K. Choose the unique generic frame u_1,...,u_a of U with p(u_j) the standard constant basis. Since partial_z(u_j) lies in U and its projection is zero, partial_z(u_j) = 0. In characteristic zero the constants of k(z) under partial_z are exactly k, so the u_j belong to V. Thus U = W tensor K for a k-subspace W of V. Saturation then gives

    A = W tensor O_T.

The same conclusion holds if beta_A is zero only generically, because beta_A is a morphism between locally free sheaves and a generically zero such morphism is zero everywhere.

### 2.3. Backward construction reaches rank zero in steps of one

Start with F_r = F and F_(r-1) = F_r^-. The assumed generic rank 1 gives rank F_(r-1) = r-1, and (2) gives dF_(r-1) subset F_r tensor Omega.

Inductively suppose F_i has rank i > 0, is contained in F, and

    dF_i subset F_(i+1) tensor Omega,
    rank F_(i+1) - rank F_i = 1.

Then beta_(F_i) has image in the line bundle

    (F_(i+1)/F_i) tensor Omega,

so it has generic rank at most 1. Its rank cannot be zero: by Section 2.2, F_i would then be a positive-rank constant subbundle of F, contradicting H0(F) = 0. Hence beta_(F_i) has generic rank exactly 1. Put F_(i-1) = ker(beta_(F_i)). This is saturated, has rank i-1, and differentiates into F_i tensor Omega.

The induction reaches F_0 = 0, with no skipped ranks. For r = 1 the first kernel is already F_0 = 0.

### 2.4. Forward construction reaches the whole ambient bundle in steps of one

Set F_(r+1) = F_r^+. It is saturated, has rank r+1, and contains dF_r after tensoring by Omega.

Inductively, suppose i > r, F_i has rank i, and

    dF_(i-1) subset F_i tensor Omega.

Then beta_(F_i) vanishes on F_(i-1), so it factors through the line bundle F_i/F_(i-1). Its generic rank is at most 1. If i < N it cannot have rank zero: Section 2.2 would identify F_i with a proper constant subbundle containing F, contradicting H0((V tensor O_T/F)*) = 0. Hence it has generic rank 1. Set F_(i+1) = F_i^+ and continue.

At rank N the saturated subbundle must be the whole V tensor O_T. Thus the process cannot stop early or skip ranks.

### 2.5. All adjacent line derivatives are regular and nonzero

The two constructions give dF_(i-1) subset F_i tensor Omega and dF_i subset F_(i+1) tensor Omega for every 1 <= i < N. Apply (4) to define theta_i.

For each such i, beta_(F_i) has generic rank 1, and theta_i induces the same nonzero generic map after dividing by F_(i-1). Thus theta_i is a nonzero morphism of line bundles on all of T.

Write

    L_i = F_i/F_(i-1),     d_i = deg L_i.

Since Omega has degree -2, theta_i has an effective zero divisor Z_i and

    delta_i := deg Z_i = d_(i+1) - d_i - 2 >= 0.   (5)

Possible derivative zeros, including those at ramified or special parameters, contribute only nonnegative delta_i. There are no poles: the ambient connection is regular, and the construction and descent above used saturated subbundles throughout.

## 3. Universal degree identity

Since F_N is trivial,

    sum_(i=1)^N d_i = 0.

Equation (5) gives

    d_i = d_1 + 2(i-1) + sum_(j<i) delta_j.

Consequently

    0 = N d_1 + N(N-1) + sum_(j=1)^(N-1) (N-j) delta_j,

and

    deg F_r = r d_1 + r(r-1) + sum_(j=1)^(r-1) (r-j) delta_j.

Eliminating d_1 yields the exact integer identity

    N deg F_r = -N r(N-r)
                -(N-r) sum_(j=1)^(r-1) j delta_j
                -r sum_(j=r)^(N-1) (N-j) delta_j.  (6)

Every coefficient of every delta_j on the right after the leading term is strictly negative. Since all delta_j are nonnegative integers, (6) proves (1). Ramification makes the bound stronger, never weaker. Equality would force every delta_j = 0 and d_i = 2i-N-1; no equality classification is needed here.

## 4. Apply the theorem to the actual bundle

Sections 1 and 2 verify all hypotheses for N = 30 and r = 17. If the actual SF had generic rank 1, then

    deg E <= -17(30-17) = -221,

contradicting deg E = -54. More explicitly, (6) would require

    13 sum_(j=1)^16 j delta_j
    +17 sum_(j=17)^29 (30-j) delta_j = -5010,

which is impossible for effective zero-divisor degrees delta_j.

Generic rank zero is also impossible: Section 2.2 would make E constant, contrary to H0(E) = 0 (or deg E = -54). Thus generic rank(SF) >= 2.

The previously proved actual identity rank(l^2) = 24 + rank(SF_l) now gives generic rank(l^2) >= 26. This is a generic assertion, not a rank-at-every-parameter assertion: the SF may drop rank at isolated parameters. The flag contradiction assumed generic rank one and remained globally valid at every possible ramification point.

## Dependencies and reproduction

- [Positive double-hyperplane Gauss gate](POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md): actual subbundle inclusion, actual derivative identification, and exact fiber rank formula.
- [Uniform twist-four and twist-five hyperplane cohomology](UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md): rank, degree, quotient bundle, and uniform local freeness.
- [Exact hyperplane adjoint syzygy bundle](EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md): the actual ambient multiplication kernels.

Run `python verify_rank_one_gauss_flag_degree.py`. The verifier proves the universal coefficient identities symbolically, verifies their sign certificates, and specializes only the established integer ranks and degrees. It does not evaluate any HM map or prove the geometric hypotheses by computation; those are proved above and in the dependencies.
