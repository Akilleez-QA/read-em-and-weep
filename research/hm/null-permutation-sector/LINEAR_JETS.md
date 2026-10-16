# Same-array alternation also kills Q2

This is a formal refinement of the symbol calculation, conditional on exactly the same source-to-ordered-nerve naturality bridge as ORDERED_NERVE.md. It does not establish that bridge or remove the scalar derivative terms E.

Let Alt denote the normalized signed sum over all 24 permutations of four derivative labels, with every current and Hessian index transformed together, at fixed transitions A,B and fixed tuple positions. In equation (13) of the complete raw-remainder decomposition, each summand involving H_cd is invariant under c<->d. Every coefficient multiplying H_cd uses only a,b; its occurrences inside traces have the same symmetry. Each summand involving J_ab is invariant under a<->b, including the terms in which J occurs inside a trace. These are symmetries of individual four-slot tensor expressions before contraction with the displayed signed complementary pattern.

For any tensor expression F invariant under an odd slot transposition t, pair g with g t in its full alternating sum. Their values agree and their signs are opposite. Thus Alt(F)=0. Applying this separately to each summand of equation (13) proves

    Alt(Q2)=0.

This proof uses only H_cd=H_dc and J_ab=J_ba. It does not assume pointwise Omega=0, any relation between currents on different edges, scalar closedness, or vanishing of a global class. Together with the previously verified identity Alt(Omega)=0, it leaves the formal same-array expression

    Alt(Rraw)=Alt(Q4)+Alt(E_p(s_raw,q)+E_q(s_raw,p)),

provided the entire scalar/gerbe representative is transformed by the genuine source action. The E terms can still contain second derivatives. One must not simply relabel scalar pair indices if the scalar representative lacks strict pair covariance.

## A necessary negative control

The quartic term does not vanish universally under this alternation. With h=diag(1,-1), e=E12, f=E21, take

    L=(h,e,f,0), U=(0,0,0,h).

These are admissible formal determinant-one current data, for example from A=exp(x0*h+x1*e+x2*f), B=exp(x3*h). The Q4 formula gives normalized full alternation -h/12. This is an invented formal control, not an actual source specialization or a nonzero cohomology class. In particular eliminating Q2 is not sufficient to finish even the two-dimensional channel.

## Evidence boundary

The preceding argument is a tensor identity. Its applicability to a globally closed source representative remains subject to the ordered-nerve extension, complete first-order scalar/gerbe descent, and geometric permutation transport checks. It changes no execution allowance and does not rerun the consumed fixed-source attempt.

Pinned algebraic decomposition: [complete raw remainder, equation (13)](https://github.com/Akilleez-QA/read-em-and-weep/blob/631e0278268dda828d64ec5458ca208c8273e459/research/hm/null-source-integration/complete-raw-remainder/PROOF.md). The self-contained check_linear_jets.py copies the displayed rational matrix formulas and tests 20 invented symmetric-jet inputs plus the quartic negative control, normally and with Python optimization. Finite controls supplement the slot-involution proof; they do not replace it.
