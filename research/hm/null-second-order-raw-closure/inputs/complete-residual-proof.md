# Complete raw residual: literal noncommutative lowering

## Result

The frozen `Source.residual` computes exactly the accepted complete five-term raw representative when `T` is supplied by the frozen `RawSource.T`. No missing term, coefficient, sign, endpoint, normalization-side or matrix-order discrepancy was found. This is a **conditional implementation theorem**: the transition, q, raw scalar and physical derivative leaf denotations and exact field operations remain its premises. It establishes the composition of these leaf bridges by checking the literal entire formula, rather than assuming that formula from a general congruence statement.

The checked files are `compiler.py` SHA256 `28e95b87adefaba0d4ec886a7ab272f252f376bbb1fc26e0a387bc05f896a386` and `raw_engine.py` SHA256 `c9804022b362277d63217c7674c4d6d3dff5941ae4210c30f51f3b5cf3868da9`. The latter lives in `sources/detector-realization/`, not `sources/scalar-compiler/`. The result does not establish equality to any uninspected current checkout.

## The mathematical source was read, not inferred from hashes

1. [Direct scalar-free reduction at 10810ee](https://github.com/Akilleez-QA/read-em-and-weep/blob/10810ee877fdaf291399198ad60d7dd0c316a42d/research/hm/null-proof-foundations/direct-scalar-free-pairing-reduction.md), §§1–4, specifies k, F, the full globalCross baseline, E and the five-term representative. Its baseline includes all gerbe terms *before* trace projection. Its equation (2) is the target formula.
2. [RS01 PROOF at ce8b3ee](https://github.com/Akilleez-QA/read-em-and-weep/blob/ce8b3eeae7159e2dcb146638789533360a3e32be/research/codex-swarm/full-source-application/PROOF.md), §3 equation (E), literally writes the seven kinetic plus three negative gerbe terms and the four mixed second-jet monomials. §4 writes both currents and both Fk corrections. The [independent review at the same immutable commit](https://github.com/Akilleez-QA/read-em-and-weep/blob/ce8b3eeae7159e2dcb146638789533360a3e32be/research/codex-swarm/full-source-application/review-independent.md) explicitly accepts this same-fresh-source identity under its listed premises. PROOF SHA256 is `01620dcda6a13a40ef3081f9c78382c58d1de17d14cc0bea75438d3973c396ed`.
3. BI01 PROOF §2 equation (3) literally specifies `R(s)=tf(M0)+Fq kp+Fp kq+Ep(sq)+Eq(sp)`; §3 equation (7) supplies the unsymmetrized raw scalar; §3 equation (8) gives its scalar first-order equation. The locally read PROOF has SHA256 `e14e83722d4e4da8d4160cd1661c32e8a37edd690561effe271135114a8078d7`, explicitly authenticated by the [BI independent review at e93cf712](https://github.com/Akilleez-QA/read-em-and-weep/blob/e93cf712f9da4926a8450cc870ed45a7bfc379ab/research/codex-swarm/source-boundary-analysis/review-independent.md). That review ACCEPTS the conditional fresh raw replacement theorem, not an obstruction verdict.

Thus RS supplies the complete residual formula and BI supplies its application to this raw scalar. The raw and N14 representatives have equal classes under the accepted BI premises; they are not asserted pointwise equal. This lowering proves the raw formula itself, not a pointwise substitution of raw s for N14 s in an equality of cochains. `pins.json` freezes every inspected source and acceptance text.

## Dictionary and primitive lowering

Use p=(0,1), q=(2,3), A=g_ij, B=g_jk, G=g_ik, with the row convention G=BA. Write D_a for the physical derivation. No matrix is transposed anywhere in this residual. Source `g` creates the physical row leaf; `gi` takes its inverse. The physical leaf theorem supplies its denotation separately.

`mu(r,B,A)` at lines 181–183 is

    mu_(a,b)(B,A) = [(D_a B)(D_b A) - (D_b B)(D_a A)]/2.

The written B-before-A order is preserved. `k(r,i,j)` at 178–180 is

    k_(a,b)(g) = -[(D_a g^-1)(D_b g) - (D_b g^-1)(D_a g)]/4
               = -mu_(a,b)(g^-1,g)/2.

Differentiating gg^-1=I gives D(g^-1)=-g^-1(Dg)g^-1, hence k=[L_a,L_b]/4 with L_a=g^-1D_a g. This also proves tr(k)=0, using ordinary matrix trace of a commutator. It does not allow nonlinear cochain reordering. The compiler derivative implements the inverse rule; raw `Mat.D` differentiates entries. Raw `Mat.inverse` uses the 2x2 adjugate, which equals the inverse only under the explicitly imported determinant-one premise. No claim about arbitrary non-SL2 inputs follows.

`mu2` at 184–188 is exactly

    1/4 [(D0D2 B)(D1D3 A) - (D0D3 B)(D1D2 A)
         -(D1D2 B)(D0D3 A) + (D1D3 B)(D0D2 A)].

Its four tuple rows are respectively (0,2,1,3,+1), (0,3,1,2,-1), (1,2,0,3,-1), (1,3,0,2,+1). D(D(B,a),b) denotes D_bD_a B; the accepted commuting physical derivations justify that displayed notation. The mixed Moyal square has two disjoint pair orders, so 2*(1/8)=1/4. Each axis is distinct inside these second derivatives; no repeated-axis factorial is missing. The checker uses commuting formal derivations, but never commutes matrix words.

`b` at 189–193 is the **ordered** Alexander–Whitney representative

    b_(a,b),ijk = (15/4) q_(a,ij) q_(b,jk).

It is not antisymmetrized, and its 15/4 is not the raw edge scalar's -15/8 correction. `F` at 194–197 is

    F_r = b_r - tr(G^-1 mu_r(B,A))/2.

The full curvature matrix is left normalized before its trace; no cyclic cochain trace step is used.

## Ten baseline terms, in literal list order

Set U_r,ab=g_ab k_r,ab. The code's local lambda `u` is precisely this baseline U, with no scalar s inserted. The `kin` list at lines 224–225 is:

1. U_p,jk U_q,ij
2. U_q,jk U_p,ij
3. mu_p(U_q,jk,A)
4. mu_q(U_p,jk,A)
5. mu_p(B,U_q,ij)
6. mu_q(B,U_p,ij)
7. mu2,mixed(B,A)

This is exactly RS §3(E) specialized to the scalar-free first transitions. Product differentiation in items 3–6 differentiates both g and k. k itself contains derivatives of g and g^-1, so these terms retain the mixed second derivatives and inverse/frame differentiation. Neither g nor its frame is frozen.

The three entries of `gerbe` at line 227 are:

8. -b_p U_q,ik
9. -b_q U_p,ik
10. -b_p b_q G

The last coefficient is -1: the mixed piece of -b²G/2 contains two scalar cross orders. The source constructs it with scalar `mul(bp,bq)` and scalar-times-matrix `smul(...,G)`. It is not a fourth kinetic term or an extra post-projection correction.

Line 228 forms M0=G^-1(sum of all ten terms). Thus its gerbe contribution is exactly -b_p k_q,ik - b_q k_p,ik - b_p b_q I after the genuine inverse cancellation. Right normalization or replacing the full baseline by crossResidual before gerbe subtraction changes the expression. The checker compares every one of the ten entries separately and compares the normalized total, before projection.

## Trace and the other four branches

`Circuit.tf` and raw `Mat.tf` both return X - tr(X)I2/2. Their actual return ASTs are checked separately. Rank is exactly two, and trace returns a 1x1 scalar in the implementation. Therefore trace(tf X)=0 and tf(cI2)=0. The baseline is projected only after all ten terms and left normalization have been formed. The central -b_p b_q I eventually cancels under tf, but it remains in the literal source and in the term-by-term test; it was not deleted from the baseline contract.

The final dictionary insertion order at 229–231 is exactly:

    baseline: tf(M0)
    Fk12: F_q k_p,ik
    Fk34: F_p k_q,ik
    E12: E_p(s_q)
    E34: E_q(s_p)

Both Fk factors have positive signs and complementary pairs. Because F is scalar, `smul(F,k)` has its stated scalar-times-matrix meaning. The code does not place either F inside the baseline trace or replace F by -tr(C)/2. Either change would lose the gerbe contribution.

At lines 214–219, for r=(a,b), solver pair t, `sij=T(t,i,j)`, `sjk=T(t,j,k)`, the source writes

    E_r(s_t)=1/2 [ (D_a s_t,jk)L_b - (D_b s_t,jk)L_a
                         + (D_b s_t,ij)U_a - (D_a s_t,ij)U_b ],
    L_d=A^-1(D_d A),
    U_d=A^-1 B^-1(D_d B)A.

All four signs, both endpoint positions, both derivative directions and every transport factor are retained. In particular U_d is not B^-1 A^-1(DB)A, an untransported B current, or a symmetrized expression. The raw call uses p to differentiate s_q and q to differentiate s_p, hence only complementary scalar derivatives. The scalar denotation bridge proves those derivatives with both endpoints and all four moving-frame blocks. Nothing here discards those derivatives or changes the raw unsymmetrized transport.

Determinant one gives tr(L_d)=D_d(log det A)=0, and conjugation gives tr(U_d)=0, so E is traceless. Together with tr(k)=0 this makes the complete representative traceless. This mathematical trace statement uses genuine inverse/determinant identities; the free-symbol checker intentionally does not impose them. It checks placement of trace projection instead.

## Raw engine linkage and ordered arithmetic

The parsed raw class has base `SC.Source` and overrides exactly one method, T. Its literal return is `((self.c.model.s_raw(tuple(p),a,b),),)`. The checker verifies that AST including pair and endpoint order. Thus every checked Source helper and residual method is inherited unchanged, with only the scalar solution replaced by the stated raw scalar leaf. `source_and_lift` constructs `RawSource(M)` and passes its residual to the lift. It does not reconstruct an alternate residual.

Raw `Mat.mul` is ordinary ordered multiplication: starting at the first factor, each next factor gives entry sum_j out_ij b_jh. Induction preserves exactly the written factor order, including four-factor U. `smul` multiplies each entry by s[0][0]; `trace` sums diagonal entries into a 1x1 wrapper; `add` and rational `scale` act entrywise. All factors are exact `Fraction`s. This is a source inspection of the index formulas, not execution of matrix products. Under the exact-field and derivative premises, these operations realize the formal algebra used above. The compiler's product derivative is the full ordered Leibniz sum, and its physical jets record differentiated frames; the raw path computes derivatives entrywise through the exact field. Physical derivative correctness is supplied by the separate curve/field bridge, not established by a finite sample here.

## Executable controls and their precise strength

Run `python -B check.py` and `python -BO check.py`. Both supplied receipts PASS. Every check uses explicit exception conditions, with no removable assertions.

The checker hashes all inputs, parses the frozen source with `ast`, and interprets only its selected Source methods in an invented free-symbol algebra. It never imports or executes a production module. It replaces T by independent formal scalar symbols. D obeys the formal Leibniz rule and commutes across directions; derivatives of inverse atoms remain independently named formal jets. Scalars and trace symbols are central; matrix words remain ordered. Trace is linear and tr(I2)=2; no cyclic word normalization, SL2 simplification, g_jk g_ij=g_ik substitution or physical polynomial product is performed.

A separately handwritten expected expression from the cited equations is compared term-by-term, then as all five components, then as their complete sum. The seven kinetic expansions contain [4,4,12,12,12,12,4] formal words; the three gerbe expansions contain [2,2,1]. The baseline plus trace correction has 130 words, the Fk terms 6 each, and the E terms 4 each: 150 total in this deliberately unreduced free algebra. These are invented-symbol counts, not physical coefficient, memory, degree or resource estimates.

Thirteen semantic mutations are rejected: reversed kinetic order, mu sign, mixed coefficient 1/8, a mixed-jet sign, gerbe sign, omitted last gerbe term, right normalization, F trace sign, Fk pair swap, E transport order, E endpoint substitution, E sign and k factor. Each mutation is interpreted as source AST and rejected by mathematical equality, not by changing the frozen input hash. The source is never edited. Separate checks inspect both actual tf return ASTs and the raw subclass dispatch. The checker is an auditable restricted interpreter for these pinned files, not a security sandbox for arbitrary untrusted Python.

## Scope still open

This bridge closes the narrow literal complete-residual composition obligation conditional on the already identified leaf denotations. It does not reprove their physical model, primitive/contraction, determinant or field premises, authenticate another checkout, prove HPL/selector/outer transport, establish regularity or resource admission, compute any detector value, or prove ID0=0. The accepted class comparison must not be confused with pointwise equality of the raw and N14 residuals. No production import, physical model/source/owner/jet evaluation, actual polynomial multiplication, patch application, external write or admission change occurred. Only local files in this deliverable directory were created.
