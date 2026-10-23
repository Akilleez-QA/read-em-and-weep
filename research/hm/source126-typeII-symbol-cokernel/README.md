# Universal hidden-symbol scheme and bundles

Under PR965's nonzero-mu alternative, this packet upgrades the set-theoretic
rank conic to exact scheme and sheaf statements:

- Homogeneous maximal-minor ideal: Delta·(alpha,beta,gamma)^3.
- Projective degeneracy scheme: reduced discriminant conic C.
- Cokernel: i_*O_C(2).
- Ambient kernel K: rank three, c1=-6, c2=12.
- Kernel after restricting the map to the conic: Sym³W O_P1(-3), rank four.
- Restriction of K itself: Sym²W O_P1(-4), rank three.

The difference between the last two is the nonzero Tor line O_P1, via
complete cubic evaluation. The raw affine ideal is not (Delta).

No actual value of mu is selected, and no original map surjectivity or
source exclusion is claimed. All calculations are universal binary-form
identities. The direct immutable input is PR965 at
de8e1d1a90d6f41dffa74df7cc7220c4e84bf4e7.

Run python verify.py and python -O verify.py: 146 checks and identical
RESULT.json. All 56 maximal minors are checked; ten quotient cubics have
coefficient determinant 2^40. PROOF.md gives the full geometric argument.
