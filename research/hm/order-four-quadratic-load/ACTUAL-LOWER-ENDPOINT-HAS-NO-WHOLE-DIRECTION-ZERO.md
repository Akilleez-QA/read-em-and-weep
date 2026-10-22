# The actual lower endpoint has no whole-direction zero

## Actual corollary

Let T=H1(B_Q(-2))^G be the invariant normal line. For EVERY nonzero eta in T and EVERY nonzero parameter a in A, the entire actual lower endpoint map

    q_eta(a,-):D5 -> Cplus/J=P4

is nonzero. Thus no nonzero parameter direction removes the whole endpoint contribution from the lower source. This does not say every individual source vector has a nonzero value, that the map is injective or surjective, or that the fourth obstruction is nonzero.

The new actual input is the checked nonzero value at fb574c01207099eeb63960da5cb23ad2f2498a84, ACTUAL-ENDPOINT-NORMAL-VARIATION-IS-NONZERO.md. The general whole-fiber detection theorem is Mr. Slop's PR662 at f75a18fd411350adda35dedf18751eee002a39bc, research/hm/endpoint-base-locus-exclusion/PROOF.md. The present corollary applies that structural theorem to the now-computed ACTUAL family, rather than leaving its nonzero hypothesis open.

## Proof with the actual hypothesis discharged

Put M=Hom(D5_source,P4). The actual quadratic family q_eta belongs to

    Hom_G(D5_source,P4 tensor Sym² A*).

Because Sym²A=1+D5_parameter and Hom_G(D5_source,P4)=0, polarization identifies it with an equivariant map

    T_eta:D5_parameter -> M,
    q_eta(a,-)=T_eta((a tensor a)_0).

The actual endpoint theorem gives a nonzero value for eta at the pure canonical square-kernel input, retaining its unknown nonzero normal scale. Hence T_eta is nonzero. Irreducibility of D5_parameter makes T_eta injective.

For a nonzero a, the trace-free tensor (a tensor a)_0 cannot vanish. If it did, the rank-one endomorphism aa^t would equal ((a,a)/3)I on the three-dimensional nondegenerate space A. The right side has rank zero or three, whereas aa^t has rank one even for isotropic a. This contradiction proves the assertion for every a, not merely a generic direction. Injectivity of T_eta completes the proof.

Equivalently, for each fixed nonzero a, the actual linear map from the invariant normal line T to Hom(D5_source,P4) has zero kernel. The argument does not address non-invariant normal directions.

## Square secant consequence and limits

PR661 at 1325647fd916bf2daa71b11efeae6d52cfefa2cd proves that every nonzero quadratic endpoint family restricts nontrivially to K_a at every nonzero square. Therefore the actual q_eta(a,-)|K_a is nonzero at EVERY square too. At the tested C5 square one canonical mixed input is zero while the pure input is nonzero; this is consistent with nonzero whole-fiber detection.

No all-direction secant assertion is made. The compulsory nonsquare exceptional axes in PR663 concern that different restriction. This corollary neither places the actual family in those exceptional kernels nor evaluates the next ambient division. The lower P4 here is not the positive third-Bockstein target P4, and the identically zero third Bockstein remains unchanged.

The full repair, fourth coefficient, generic section count and Smith bounds are not changed by this corollary. Its contribution is the actual exclusion of an endpoint-free parameter direction, conditional on the already checked source comparisons explicitly cited above.

Run python3 verify_actual_endpoint_no_direction_zero.py for universal trace-free tensor identities. The irreducibility argument and actual nonzero input are the mathematical proof; no actual coefficient or point is selected.
