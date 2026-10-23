# Independent review of the separated terminal descendants

Verdict: PASS for the full expanded theorem: actual dimensions9,14,16,12,
length51, terminal character2T, the stated socle, exact minimal resolution
and annihilator (W)^4. This final receipt supersedes the earlier narrower
review. It is a mathematical review with exact replay, not a
proof-assistant verification.

## Actual terminal quotient and orientation

PR1058 identifies the genuine separated first three spaces and their actual
multiplication maps. PR1072 extends the same splitting through degree five
by natural cohomology maps; its explicit two determinant rotations cancel,
so the continued arrows are the original same-variable negative actions.
This is not an identification from equal characters.

The complete actual Koszul sequence of PR1052 splits compatibly under the
first-block and residual projectors. Restricting it gives the exact N0
sequence used in Section2. In W tensor Sym²W, the images
x tensor(y l)-y tensor(x l) are exactly the kernel of multiplication to
Sym³W. Passing to that quotient sends the other relations precisely to
the image of W times the quadratic polarization of Sym10W. Thus the
terminal quotient formula is the actual one, with its maps retained.

## Universal coefficient certificate

The relation matrix formula is ordinary multiplication on the first factor
of the pinned quadratic polarization, in the stated row order. The two
transvectants have degrees7 and5. Exact identities rank(Rel)=22, C Rel=0,
and rank(C)=14 prove equality of kernel and relation image. They are not
just a Clebsch--Gordan dimension comparison.

The P8 projection literal was checked against the authenticated PR1058
verifier. Its apolar adjoint supplies the same unique P8. The displayed
12-by12 determinant and full rank12 of C_P were independently replayed.
Sym³W tensor P=S+2T and the terminal target W'+2T exclude the S channel,
so the kernel is S and the image fills the full T-isotypical component.
All matrices are complete universal representation coefficient maps;
no actual source, cubic direction or coefficient value is substituted.

An additional independently constructed certificate was inspected and
replayed: it obtains polarization by expanding f(x+u,y+v), multiplies by
u,v, and computes relation rank22 and rank34 after adjoining the P image.
Thus its quotient-image rank is12 without using transvectants or the
production determinant. Its separate script is
/workspace/shared/verify-separated-terminal-complement/check.py.

## Actual transport and socle

Nonzero projection P_h->P8 is an isomorphism by multiplicity one. Naturality
through degree five transfers the universal rank12 to the projected actual
cubic image. The full actual image has rank at most12, because its source
is S+2T while actual M5=W'+3T has no S. Also W I4=0, so these are all
terminal descendants. Thus F5 has dimension12 and projects injectively
to the full T-isotypical part of N0,5. A residual graph remains possible;
the proof correctly does not equate F5 with the separated subspace itself.
The global degree-six cohomology vanishing kills all subsequent descendants.

The actual joint kernel in degree four is NC4. It is in the residual
block, whereas the first-block projection is injective on the quadratic
P_h descendants. The direct sum with I4 therefore gives intersection
F4 intersect NC4=I4 exactly. Degree-three socle vanishes by the injective
actual Koszul map, and degree-two socle vanishes by the separate first
multiplication maps. Hence only P in degree four and2T in degree five
remain. The length9+14+16+12=51 is correct.

The branch is specifically nonzero first-block projection, not the distinct
zero-first-block/nonzero-residual-projection branch. No actual coefficient,
branch occurrence, Q-stability, positive action or full Rao-module claim
is inferred.

## Expanded minimal resolution and annihilator

The resolution is derived from the actual socle, not the Hilbert numerator
alone. With generator degree shifted to zero, Tor2 is P in degree4 and2T
in degree5. The representation-valued numerator has coefficients
P+D, -S, -V, -(W'+S), -(V+D), 2T. Generation in degree zero consequently
forces Tor1 to be S in degree1, V in degree2, W'+S in degree3 and V+P+D
in degree4. Restoring the original shift by two gives exactly the displayed
free terms. The quartic P relation cannot be dropped: it cancels P only
in the numerator, not in the minimal resolution. The two P terms at
original degree6 are both retained; their equal-shift differential is
zero by minimality. Finite-group averaging supplies equivariant choices
of minimal generators and lifts.

Termination gives (W)^4 annihilation. In each lower positive degree1,2,3,
the action-map domain is irreducible W,A,S, respectively. Its image is
nonzero because the generators span the corresponding nonzero descendant
degree. Thus no lower homogeneous piece contains an annihilator. The
annihilator of a graded module is homogeneous, so inhomogeneous mixtures
cannot add further elements. The exact ideal is therefore (W)^4. These
claims concern the actual generated negative module only.

## Authentication, replay, and hash binding

All five immutable inputs were freshly independently fetched. Their remote
Git blobs agree with the retained files:

- PR1072: 65dda3e16ded2b79ad84c583f248b09c425e9881.
- PR1058 proof: 3d42713aaaf4078e3a1b44d8eb3d9f545daa880c.
- PR1058 verifier: 2c8921c229b1ab1c12963de34f85c4f33cebd436.
- PR1052: b0be6d47a234bbfc3e49f94c8cc295d8b5129a7d.
- PR1068: 5ae07c02624d70c0ccd33d7ec34202504173ff83.

Independent python verify.py and python -O verify.py pass all40 checks.
Both outputs agree byte-for-byte with final RESULT.json. Reviewed hashes:

- PROOF.md: 8ad27aec10fff6d135b6893806f59ad19a5c5ea15eca06fa2bf055d81a870bd5.
- verify.py: 3e8350b3c8c3d78c480119b9a8ccb1c90392126e6d7ee3237428b625c5fc9117.
- INPUTS.json: 3f1256218dc87a5210361b6f2d98c92a5f5b0a25696c52c809da4a55d42d9095.
- RESULT.json: 0fc55f0cee499db8e71a6a5ead9b449084aa491947bd167930e0afaaa3a1c8d8.

No public writes or actual source-instance evaluations were performed.
