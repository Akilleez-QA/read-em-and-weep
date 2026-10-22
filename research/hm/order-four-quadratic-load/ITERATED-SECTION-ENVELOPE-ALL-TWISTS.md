# A periodic certificate closes all iterated-section twists for the26 survivors

## Result and exact scope

All26 labels retained by the finite iterated-section application satisfy **every twist in that same envelope family**, in both orientations: primal d=3, rank F=14, J=A, and dual d=2, rank F=10, J=B. There are no further exclusions from extending these particular tests beyond twist11. The frontier remains26.

This does not assert realizability or satisfaction of other necessary conditions. It does not rule out sharper envelopes using additional information about the same bundles. The new result is a finite completeness certificate for the specific unrestricted iterated-section characters already used.

## Character periodicity

Let Reg_p denote the parity-p part of the regular representation of the binary icosahedral group: an irreducible rho of central parity p occurs with multiplicity dim rho, and all other irreducibles occur with multiplicity zero. Its dimension is60. With W the standard two-dimensional representation, for every t>=0,

    Sym^(t+60) W - Sym^t W = Reg_(t mod2),
    sum_(k=0)^29 Sym^(t+2k) W = ((t+30)/2) Reg_(t mod2).    (1)

To see this directly, the standard eigenvalues of noncentral group elements have orders dividing60, and their squares have nontrivial orders dividing30. The character formula

    (zeta^(t+1)-zeta^(-t-1))/(zeta-zeta^(-1))

is60-periodic at each noncentral element, while its sum over30 consecutive same-parity degrees is zero. At the two central elements the characters are respectively the dimensions and parity-signed dimensions. These observations give (1) on every conjugacy class. For odd parity the scalar in the second identity may be a half-integer, but every odd-parity irreducible has even dimension, so all multiplicities are integers.

The same character formula expresses chi_G(O(t)) for every integer t, including negative t. Hence for any center-even equivariant bundle F of rank n,

    chi_G(F(r+60))-chi_G(F(r))=n Reg_(r mod2).       (2)

This uses only its rank, not its splitting type. Equivariant twists of the actual E, Q*, K and L have exactly this central parity convention.

## An eventual nonnegative recurrence

For one orientation, write a=deg J, lambda_max and lambda_min for the extreme ordinary splitting degrees of rank-three J, and

    D(r)=sum_(j=1)^(r-d+1) H0(J(r-2j))-chi_G(F(r)).

Choose the explicit integer threshold

    R=max(d, lambda_max+2d-2, -lambda_min,
          ceil((2n-a-90)/3)).

For r>=R, the displayed finite target sum already includes every nonzero term of the infinite sum over j>=1: after the last included j, even the highest line degree is negative. Reindexing after increasing r by60 therefore gives

    target(r+60)-target(r)=sum_(k=0)^29 H0(J(r+2k)).

Also r>=-lambda_min, so these thirty H0 characters equal their Euler characters. Applying (1) to each ordinary splitting degree, with its equivariant coefficient representation, gives

    sum_(k=0)^29 H0(J(r+2k))=((3r+a+90)/2) Reg_(r mod2).

Subtracting (2) proves the exact recurrence

    D(r+60)-D(r)=((3r+a+90-2n)/2) Reg_(r mod2).     (3)

By the chosen threshold, its scalar is nonnegative. The actual J is center-even, so a is even. When r is even the scalar is an integer; when r is odd its possible half-integrality is canceled by the even dimensions of odd-parity irreducibles. Thus (3) is always a genuine representation for r>=R.

It follows that checking every d<=r<=R+59 proves genuineness for **all** r>=d: for a larger twist, subtract a multiple of60 to reach its anchor in [R,R+59], then add genuine increments. This is a proof-derived finite bound, not an empirical stopping point.

## Reproduction

Run `python3 verify_iterated_section_envelope_all_twists.py` to generate `iterated-section-envelope-all-twists.json`. The standalone verifier pins the baseline144 and the frozen26-label certificate; it does not modify either or import another checker. It reproduces exact Q(sqrt(5)) character arithmetic, checks (1) on a complete60-residue period, derives R for each of52 orientations, checks every required finite twist, and verifies (3) at all sixty anchor residues for each orientation. Every tested character is genuine. The largest required anchor twist is89.

The proof above justifies extrapolation beyond the finite calculation; checking examples alone would not. The output retains the26 stable IDs and records each orientation's rank, degree, threshold and last checked twist. No actual coefficients, points, matrices, actual-instance ranks, scans, spikes or consumed experiments are involved. No frontier decrease or whole-profile closure is claimed.
