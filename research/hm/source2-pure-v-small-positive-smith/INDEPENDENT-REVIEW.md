# Independent review of the positive Smith profile

Verdict: PASS. The full final proof, checker and eight immutable input proofs
were reviewed independently. The original-page and local target comparisons
support the stated Smith profile. No mathematical blocker remains. This is
not a proof-assistant verification.

## Original symbols and the exact open locus

The first-zero input concerns the original positive pencil and its entire
kernel, using actual associative cohomological multiplication. Its scalar
called gamma in that earlier first-order discussion is not the later lift
coefficient gamma. There is no contradiction between first vanishing and
PR1075's nonzero quadratic-lift coefficient.

The third-zero input proves vanishing of the original third Bockstein, not
just a quotient-complex third. It also supplies exact rank3 of the original
second A map away from the six C5 axes, rank2 at those axes, and no other
rank-drop support. Its discussion of the additional specialized A kernel
is retained; the present Smith theorem excludes all those points.

PR1025 identifies the original corrected fourth on D with -sL. PR1069
places the endpoint-nine lift on R1, and PR1075 proves its coefficient
nonzero under the retained actual hypotheses. PR1044 gives the exact
nonic base scheme on that line. PR1046 transfers its entire projective
component ideal to the determinant-embedded original-fourth row, including
at the C3 rank-drop locus of L. Thus the finite scheme is exactly the
length46 disjoint union Z plus E12, with28 support points.

Away from the second-symbol scheme Sigma, its rank-one cokernel is a
line bundle and the determinant embedding is an isomorphism on fibers.
Since Sigma's support lies in the excluded E, ordinary nonzero evaluation
of the determinant row there is equivalent to nonzero original fourth
into its one-dimensional page target. The proof never uses tensor
injectivity of an ideal-sheaf inclusion at its singular fibers.
Consequently every direction outside the asserted support has second
rank3, full surviving kernel D, and fourth rank1. The conclusion does
not merely hold for a generic subset smaller than that stated open set.

## Formal elimination and determinantal conclusions

Rank33 of Q splits off33 units. Original first vanishing makes the entire
four-by-eight Schur residual divisible by t². Its second symbol has rank3,
so three t² factors split off, leaving a one-by-five row. Original third
vanishing then removes its t³ term, and nonzero fourth gives valuation
exactly4.

The proof explicitly retains the fourth correction E-CB after eliminating
the second-order pivot block. It does not replace the corrected fourth
by the raw lower-right coefficient. The checker independently verifies
this formal Schur identity with symbolic blocks. Once the last coefficient
row is nonzero, one unit pivot leaves four zero source columns.

Thus the Smith exponents are0 repeated33 times,2 repeated3 times,4 once.
The free kernel rank is4; the finite cokernel length and maximal-minor
valuation are10. The determinantal valuations2,4,6,10 at sizes34 through37
also follow. Row and column operations preserve the determinantal ideals,
not individual minors. The proof correctly claims that at least one
maximal minor has order10, not that all do.

The same argument works over C[[t]] at each allowed direction and over
C(P(A))[[t]] at the generic direction after trivializing the direction
line. Polynomiality in t then gives row rank37 on a nonempty open set,
not at every nonzero t. This rectangular positive-component statement
is not a full adjoint isomorphism, source realization or completed repair.
No profile at any exceptional direction is asserted.

## Independent authentication and replay

All eight remote originals were freshly fetched at their stated immutable
commits. Their returned Git blobs agree with the retained files:

- PR1019: bf63c14f76933d59fa7e3ac61aecb3366ac1b442.
- Original first-zero: fe4410bbba05060545b22ac6bc80aac8e7c62ce4.
- Original third-zero: 7c09fe95015d7c8d932b3a27be302ca09888112d.
- PR1025: d036adcf5bc2bfc53e07cd752ff180c5993251f7.
- PR1044: 516408c24d036634f0e03e29350815c2442d2880.
- PR1046: 018672738b8f206aef51ae163053ecad3400075a.
- PR1069: 827cd956e2eb574fd7d40d408e0450c8581fd7d2.
- PR1075: a9d464fd0d4a696e7dc956e6c7af2f3e80a0480e.

Independent python verify.py and python -O verify.py pass all50 checks.
The outputs match each other and final RESULT.json byte-for-byte. These
checks use only formal block variables and universal integer arithmetic;
no actual direction, coefficient or source-instance matrix is evaluated.

Reviewed final SHA256 hashes:

- PROOF.md: dabf743d9d9b7a40f39e30695fb505d2825895f97b086fdfd8bcb4302f641f57.
- verify.py: 8348018853ca64f2c82f0ef44cab47351357fc4e1ca50906e6c557abf2ed8f38.
- INPUTS.json: 245249490ddc5e5e5116d460074860e8169602879b107f259e4f0a6d056a8fa9.
- RESULT.json: cee56fa88bc91d14aecf8545c033f6fde7fcc02003564ea270e366bee0383000.

No public writes were performed during the review.
