# Independent review: pure-V torsion evaluation quotient

Reviewed 2026-10-23 UTC separately from the author's self-check.

## Frozen files

- PROOF.md SHA-256: `29ac56c882d8bfcd0ced29692466d89139d2d1c3ac25e9bb00169dab5f428a02`
- verify.py SHA-256: `1122340705fdcfb558831258f93d8d086e475b63bf09296590cd38ec21ebaf4f`
- INPUTS.json SHA-256: `99fedb11ffdb24d212a234674312e87e44590fa4ecf045b898d858c571571c60`

Verdict: PASS for the conditional fixed-negative-pencil and universal
first-arrow cokernel assertions.

## Actual geometric interface

Read the full proof and checker. Re-read exact PR792 Sections5–7 and
checked use of the genuine PR795 residual sequence and first/last arrow
models. PR792 identifies actual first images as f12 H0(O4), f12 H0(O5)
and the last image as the embedded H1(EV)=P. It also supplies the saturated
quotient F=EC/EV and injectivity of restriction of A18+P_t to D12 for every
balanced endpoint. The present argument correctly uses these actual maps,
not only their ranks or isomorphic character spaces.

The first two quotient identifications with torsion-section spaces follow
from H1(O4)=H1(O5)=0. For the last quotient, the kernel of restriction
modulo H_t is f12 H0(O6)/f12 V6, exactly the imported embedded P.
Naturality therefore identifies both induced arrow families with the
claimed torsion multiplication/evaluation system. The endpoint-dependent
seven-dimensional constant subspace is retained rather than declared
independent of the endpoint.

## Rank, exact-sequence and sheaf checks

1. Reducedness of D12 gives one one-dimensional fiber for each of its
   twelve points. A nonzero linear form vanishes at at most one of them,
   simply. The torsion first arrow thus has rank12 or11 with reduced
   determinant divisor D12. A form avoiding D12 gives zero common kernel.

2. At a vanishing point the image of torsion multiplication is precisely
   a coordinate hyperplane. The constant section subspace is not contained
   there because A18 is basepoint-free. The supplied structural proof of
   basepoint freeness is valid: an invariant base divisor of degree at
   most18 could only be D12, which would force A into Sym6(W)=V+P.
   Thus the second arrow on the torsion quotient is onto at every nonzero
   linear form, including the twelve exceptional ones.

3. The genuine exact sequence L -> NR/I -> N8 transfers first-arrow
   kernels because N8 first arrows are injective. This needs no splitting
   of the residual extension and holds simultaneously in the original
   fixed coordinates. Surjectivity of both endpoint and N8 second arrows
   likewise transfers by lifting and correcting. The direct N0 summand
   contributes injective first arrows and surjective second arrows.
   Consequently the full ranks are36 off D12,35 on D12, and33 for every
   nonzero second arrow, with zero common first kernel.

4. The scalar complete multiplication pencil has universal cokernel
   O(m+1); its standard sequence has the indicated equivariant form under
   the fixed symplectic convention. Thus coker A0=Sym8(W) O1 and
   coker A8=A O5. The universal torsion first arrow is injective as a
   sheaf map even though its fiber map drops rank at D12.

5. The sheaf snake lemma gives0 -> T_D -> coker A_K -> A O5 -> 0.
   Since Ext1(A O5,T_D)=0, this splits as sheaves, equivariantly after
   finite-group averaging. This is not a splitting of the original
   two-pencil extension. It gives the asserted torsion-free quotient,
   rank12 and degree24, with additional torsion length12.

6. Locally at each point of D12 the cokernel is free of rank12 plus
   O/(t). Its presentation over the local DVR has maximal-minor ideal(t).
   Away from D12 the ideal is the unit ideal. Therefore the full36-column
   degeneracy scheme is genuinely reduced D12, not merely the same
   set-theoretic support or rank-drop count. Total cokernel degree36
   also agrees with48 O minus36 O(-1).

## Executed verification and limits

Independently executed `python verify.py` and `python -O verify.py`:
192 checks pass with identical JSON. All three exact input SHA-256 and
Git blob digests pass. The checker uses independent formal fiber
multipliers and synthetic extension matrices, not actual invariant-orbit
coordinates. Its nonreduced negative control appropriately distinguishes
rank support from scheme multiplicity. The universal proof, not these
finite controls, supplies the every-point assertions.

No Q compatibility is needed or inferred. The proof makes no Bockstein
preservation assertion for pure V, no claim of Q-stable summands, no
compatible-line existence, and no source exclusion or complete repair.
This independent review is supporting verification, not a separate new
mathematical deduction or proof-assistant certificate.
