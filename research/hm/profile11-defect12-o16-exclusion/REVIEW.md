# Independent exact-version review: the three defect-twelve O(16) exclusions

## Verdict and reviewed version

**PASS.** The reviewed proof correctly excludes exactly the three stated maximal profile-(1,1) labels, subject to the pinned actual-bundle and necessary-catalog inputs. No mathematical defect was found. In particular, the transfer from the zero-defect theorem requires only saturation of the highest positive line, not saturation of the entire original derivative image. The new proof establishes that partial saturation independently and supplies its own constant-projection and horizontal-top argument.

The reviewed file is `PROOF.md`, titled “Saturation of the positive line excludes three defect-twelve O(16) labels,” with exact SHA-256

    a377136f70014ca0d7913e3a652e5bf8bd1a06a316a622fdf9911f434ce1bf0e

This review was completed on 2026-10-23. The proof was not modified. The verdict attaches to those exact bytes, not to an unspecified later revision.

The three conclusions are:

- G3.11.1e318198128e, source_index25;
- G3.11.6795493ae8cd, source_index26;
- G3.11.a5d4e292b34e, source_index36.

The checks below independently reconstruct the saturation argument, source reduction, polar obstruction, and constant-projection contradiction. No conclusion about any other label, source2, or the original global rank goal is included.

## 1. Immutable dependencies actually inspected

The main transferred dependency was fetched and read at its exact public commit:

- [PR802 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/e484640a6565c278321bf6557860262c1ac1b7df/research/hm/profile11-o16-constant-span-exclusion/PROOF.md), commit `e484640a6565c278321bf6557860262c1ac1b7df`, Git blob `98a1bd6123e148476da0b997d879aecbf885ec97`.

Its Sections 2–5 were checked as the proposed transferable argument. Its later Sections 6–7 were also read to distinguish the identities that are not available at defect twelve.

The following five original files were fetched at commit `db51525015bb7c5e825833d550d08dedf6f6ea96`. The three prose inputs, the exact relevant catalog rows, and the frontier label records were inspected:

1. [ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md), Git blob `b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3`.
2. [NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md), Git blob `d7506dae49b4be43230450c4132bd5db91f137ef`.
3. [ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md), Git blob `dcacf0bcdef8377c1ed7654e5b82659ea409456e`.
4. [one-one-endpoint-necessary-pairs.json](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json), Git blob `fe0afa410d89340d3082dc814277f89fbb582c19`.
5. [rank-three-quotient-frontier-144.json](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json), Git blob `8b5971092f9ef762584912609fd5e9301c4e271d`.

For the scope of the reusable lemmas cited inside PR802, the following exact proofs were also fetched and read:

- [PR796 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md), commit `d2b43060c83328dd5118aee6b9288fcfa0c873ac`, Git blob `46a0de762000f21182f6d3168f3ecfd63adaf75f`. Only its saturated derivative-image construction and its separate profile-free quadratic Gauss-gap lemma are pertinent.
- [PR799 proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/2172e4a7abbbe232f9f448bea6fa01dee7927460/research/hm/profile11-quadratic-polar-obstruction/PROOF.md), commit `2172e4a7abbbe232f9f448bea6fa01dee7927460`, Git blob `a62a56f6b8f97e02b3eab6fe3a47ec3bedb6c6b1`. Its universal first-polar generation argument is pertinent.

These are substantive mathematical inputs, not evidence that any necessary formal source is realizable. This audit did not rerun their catalog generators or claim to reprove all earlier HM constructions.

## 2. Exact label, defect, and source-overlist check

The three frontier records give the stable labels and source indices claimed in the proof. The corresponding zero-based catalog rows are exactly:

    index25:
      A_q=O(-10)+O(-8)+O(16),
      B_q=O(-18)+O(-6)+O(8),
      a=-2, b=-16, defect=12;

    index26:
      A_q=O(-10)+O(-8)+O(16),
      B_q=O(-18)+O(-4)+O(6),
      a=-2, b=-16, defect=12;

    index36:
      A_q=W O(-9)+O(16),
      B_q=O(-18)+O(-4)+O(6),
      a=-2, b=-16, defect=12.

In all cases the determinant formula gives `-6-a-b=12`, independently confirming the catalog's defect field.

Rows 25 and 26 have precisely these four compatible tuples, with no additional tuple:

    (0,0,0,0,0,2,0,1),
    (0,0,0,0,1,1,0,1),
    (0,0,1,0,0,1,0,1),
    (0,1,0,0,0,1,0,1).

Row 36 has those four and precisely these four additional tuples:

    (0,0,0,0,0,1,1,0),
    (0,0,0,0,1,0,1,0),
    (0,0,1,0,0,0,1,0),
    (0,1,0,0,0,0,1,0).

The tuple-to-bundle conversion follows directly from the pinned actual-source formula. For tuple `(a,b,c,d,e,f,g,h)`, its degree-minus-two coefficient is

    R2=(c+g+h-1)V+(d+e+g+h)P+(f+g)D,

and the lower part is

    a Wp O(-3)+b T O(-3)+c V O(-4)+d P O(-4)
      +e Wp O(-5)+f O(-8)+g W O(-9)+h O(-10).

Substitution yields, in order,

    E0  =(P+2D) O(-2)+2 O(-8)+O(-10),
    U6  =(2P+D) O(-2)+Wp O(-5)+O(-8)+O(-10),
    E3  =(V+P+D) O(-2)+V O(-4)+O(-8)+O(-10),
    E6  =(P+D) O(-2)+T O(-3)+O(-8)+O(-10),

    E10 =(P+2D) O(-2)+O(-8)+W O(-9),
    U13 =(2P+D) O(-2)+Wp O(-5)+W O(-9),
    E12 =(V+P+D) O(-2)+V O(-4)+W O(-9),
    E13 =(P+D) O(-2)+T O(-3)+W O(-9).

The names U6 and U13 are local names, not new numerical source indices. All eight displayed types have rank 17 and degree -54. The corresponding source lists at indices 46 and 51, used in PR802, were checked as well: they are respectively the same four and eight tuples. Thus there is no missing source in the transfer.

## 3. The new positive-line saturation argument is valid

Let `Q=(H O)/E`. The pinned input gives the actual injective transpose factorization

    A_q -> B_q^*(-2) -> Q(-2).

The second arrow is saturated because it is dual to a locally free quotient of Q*, with the indicated twist. The middle bundles for indices 25, 26, and 36 are respectively

    O(16)+O(4)+O(-10),
    O(16)+O(2)+O(-8),
    O(16)+O(2)+O(-8).

Every morphism from the O(16) summand of A_q to a lower summand of the middle bundle vanishes: its Hom space is a space of sections of a negative line bundle. The restricted morphism to the remaining O(16) is a scalar. That scalar cannot be zero, since the original map is injective as a sheaf map. It is consequently an isomorphism at every point.

Write `S=i(O(16))`. It is exactly the highest direct summand of the middle bundle. Thus the quotient of the middle bundle by S is locally free, and so is the quotient of Q(-2) by the middle bundle. The exact sequence formed by these two quotients shows that `Q(-2)/S` is locally free. This proves saturation of S in the actual target.

This does not make `i(A_q)` saturated. Off-diagonal maps from negative source summands into the highest target summand cause no problem: the image of the positive source line itself is already the full highest target summand. The remaining defect is compatible with torsion in the quotient directions below that line. The proof neither discards that torsion nor uses it as if it vanished.

## 4. The onto top map and saturated derivative-image sequence

For each source above, the canonical top-slope block is `F=R O(-2)`, with rank 14, 13, 12, or 9. It is saturated in E and hence in H O. Degree considerations force the restriction of `E -> A_q` to F to land in the positive O(16).

The kernel of the original quotient is E^-. The pinned strict-top lemma gives `H0(E^-(2))=0`. Therefore

    R=H0(F(2))=H0(E(2)) -> H0(O(18))

is injective. This is an actual kernel argument, not an unsupported inference from the rank of F.

The base divisor of the resulting equivariant section system would be invariant. Every nonempty projective A5 orbit has at least twelve points, so a nonzero base divisor would leave at most `h0(O(18-12))=7` independent sections. Since `dim R>=9`, this is impossible. Thus the actual map `p:F -> O(16)` is onto, and

    0 -> K0(2) -> R O -> O(18) -> 0

is exact as a sequence of bundles.

Here is the saturation argument with its hypotheses separated. Set

    U=(E/F)(-2),
    V0=(H O/F)(-2),
    I=image(beta_F),
    J=image(K0 -> U).

The quotient `V0/U` is Q(-2). The image of I in this quotient is exactly S, because p is onto. Its kernel is exactly J, since S receives the injective positive-line map. Hence

    0 -> J -> I -> S -> 0,
    0 -> U/J -> V0/I -> Q(-2)/S -> 0.

Whenever J is saturated in U, both outside terms in the second sequence are locally free, and so is V0/I. Therefore I is saturated. Untwisting gives the actual sequence

    0 -> F -> F^+ -> I(2) -> 0.

Only S and J need be saturated. No hypothesis about the full image of beta_E appears in this argument.

If J=0, the quotient is `F^+/F=O(18)`. The profile-free quadratic Gauss gap applies: for a saturated `O(-2)^r` with Gauss rank one and first quotient O(b), either `b=2r` or `b<=r-1`. Indeed quadratic values and first two derivatives span the constant coefficient space. The derivative of F^+ kills F, so that space has dimension r+1 or r+2. Its degree and, in the latter case, the nonzero derivative map

    O(b) -> O(2r-b-2)

give exactly those two alternatives. This proof makes no use of E^+ being an interior stage.

## 5. Independent check of the complete small kernel reduction

The relevant character identities are

    Sym18 W=A+V+2P+D,
    Sym19 W=W+Wp+S+2T,
    P W=Wp+T,  D W=S+T,  V W=T,
    A W=W+S,   Wp W=P,
    Sym6 W=V+P,  Sym7 W=Wp+T.

From the exact top sequence,

    H1(K0(2))=Sym18 W-R,
    chi(K0(3))=R W-Sym19 W.

Since `H0(K0(2))=0`, every K0 degree is at most -3. A block `U O(-j)` with j>=4 contributes `U Sym(j-4)W` to H1(K0(2)); this must fit inside A+V+P. Positivity prevents cancellation. The complete supported list is

    A O(-4), V O(-4), P O(-4), Wp O(-5), O(-6), O(-10),

with H1 contributions A, V, P, P, A, V+P, respectively.

The short completeness check is valid. At j=4 only A,V,P occur. At j=5 only `Wp W=P` fits: `W W=1+A`, `S W=A+D`, while T exceeds the dimension budget. At j=6 the trivial coefficient gives A; the other possible small coefficients give `A A=1+A+D` or `V A=P+D`. At j=7 the only eligible odd coefficients are W and Wp, and their products with S contain D. At j=8 the trivial coefficient gives D. At odd j>=9 the smallest odd coefficient already exceeds the ten-dimensional budget. At j=10 the trivial coefficient gives V+P; at j=12 it gives P+D. At even j>=14 even the trivial coefficient is too large. This leaves exactly the six listed blocks.

Their contributions to chi(K0(3)) are respectively

    0, 0, 0, -Wp, -W, -T.

Degree-minus-three blocks contribute their genuine coefficient representation. Matching the H1 budget and this Euler character gives exactly:

    R=2P+D:
      (Wp+T) O(-3)+V O(-4)+O(-6);

    R=V+P+D:
      T O(-3)+P O(-4)+O(-6),
      or (Wp+T) O(-3)+Wp O(-5)+O(-6);

    R=P+D:
      V O(-4)+P O(-4)+O(-6),
      or Wp O(-3)+V O(-4)+Wp O(-5)+O(-6),
      or T O(-3)+O(-6)+O(-10).

These are necessary exact kernel possibilities, not an assertion of their realizability.

The source eliminations then follow:

- For E0 and E10, K0(2) has rank 13, degree -18, and strictly negative degrees. Its most negative degree is at least -6, so every K0 degree is at least -8. The target `(E/F)(-2)` has degrees at most -10; therefore J=0. The gap excludes r=14,b=18.
- For U6 and U13, all K0 degrees are at least -6 and all target degrees at most -7. Thus J=0, and the gap excludes r=13,b=18.
- For E3 and E12, the only possible equal-degree component is `O(-6) -> V O(-6)`. It is zero because `Hom_G(1,V)=0`. Again J=0, and the gap excludes r=12,b=18.
- In the W O(-9) quotient case, E6 cannot surject onto that rank-two summand: only its O(-10) line can contribute. Thus E6 is excluded for the third label too.

The remaining matching cases are exactly

    E=(P+D) O(-2)+T O(-3)+L,
    A_q=O(16)+L,

where `L=O(-8)+O(-10)` for the first two labels and `L=W O(-9)` for the third.

For the first two kernels in the last row, the apparent extra channels vanish: `O(-6) -> T O(-5)` would require a trivial constituent of T W, and `Wp O(-5) -> T O(-5)` would require Wp=T. Neither is possible. Thus J=0 in those cases.

For the third kernel, only the O(-10) line can contribute. Its map to `T O(-5)` belongs to the unique quintic channel, since T=Sym5 W. If nonzero, it is the complete tautological quintic line and has no fiberwise zeros. In the E6 case a scalar map to the O(-10) target is also possible; if this is the only nonzero component it is an isomorphism. A graph combining these components remains a subbundle. Therefore the only alternatives are J=0 and the saturated `J=O(-10)`. This checks all saturation hypotheses required by the derivative-image sequence.

## 6. The polar obstruction transfers without full derivative saturation

For a genuine quadratic inclusion `R O(-2) -> H O`, the value-plus-first-derivative image at a variable line l is the coefficient image of `R tensor lW`. Thus the first-polar map

    R tensor W tensor O(-1) -> H O

has image equal to the raw first osculation. The saturated-image sequence already proved that this raw first osculation is F^+. Consequently F^+(1) is globally generated, and F^+ is also a subbundle of a constant bundle. Its splitting degrees are only 0 and -1.

If `J=O(-10)`, the sequence gives rank 11 and degree -8 for F^+. Its equivariant Euler characters are

    chi(F^+)=-P-D-Sym6 W+Sym18 W=A,
    chi(F^+(1))=Sym19 W-Sym5 W=W+Wp+S+T.

Since `A W=W+S`, these identities force

    F^+=A O+(Wp+T) O(-1).

The constant three-space C is the actual image of H0(F^+) in H. Projection by this constant space gives the actual saturated subbundle

    Rlin=F^+/(C O)=(Wp+T) O(-1)

of `(H/C) O`. Its saturation follows from the locally free quotient `H O/F^+`, not from an assumed property of the projection of E.

The projected map from F has exactly three multiplicity-one channels:

    lambda:P O(-2) -> Wp O(-1),
    mu:P O(-2) -> T O(-1),
    nu:D O(-2) -> T O(-1).

There is no D-to-Wp channel. The nu channel cannot vanish, since that would embed rank-five D O(-2) in rank-three C O. The lambda channel cannot vanish either: its absence would make the projected image have rank at most six, hence `F intersect C O` have rank at least three. Equality of ranks would put C in F generically. Because F is saturated in H O, the map `C O -> H O/F` would then vanish identically; this would contradict H0(F)=0. This reasoning is sheaf-theoretic and does not assume constant rank for an arbitrary fiberwise intersection.

The nonzero lambda and nu channels have the exact standard sequences

    0 -> Wp O(-3) -> P O(-2) -> Wp O(-1) -> 0,
    0 -> D O(-2) -> T O(-1) -> O(4) -> 0.

If mu=0, the projected F contains the full Wp O(-1) summand. Its derivative lands in Rlin, because the derivative of the projected F does. A linear subbundle reaches its constant coefficient span after one forward transform, so Rlin would contain a nonzero constant subbundle. This is impossible since H0(Rlin)=0.

If mu is nonzero, its restriction and projection give

    gamma:Wp O(-3) -> O(4).

This map cannot be zero. Otherwise the composite `P O(-2) -> O(4)` would factor through Wp O(-1), but the relevant equivariant Hom is `Hom_G(Wp,Sym5 W)=0`. The composite would therefore vanish and mu would factor through D O(-2), contradicting `Hom_G(P,D)=0`.

The nonzero gamma is a pair of independent degree-seven sections. Irreducibility of Wp gives their independence; equivariance makes their common base divisor invariant. A divisor of degree at most seven cannot contain a nonempty invariant orbit of degree at least twelve. Hence gamma is onto everywhere. Together with the two exact Euler sequences, this shows that the entire projected map `F -> Rlin` is onto everywhere.

Every local section of Rlin therefore lifts locally to F, whose derivative projects into Rlin. Thus Rlin is horizontal in the constant quotient `(H/C) O`. In characteristic zero a horizontal subbundle has constant Grassmannian map and degree zero, contradicting `deg Rlin=-8`.

This exhausts the nonzero internal-image case. Every connection used above is inherited from a genuine constant ambient quotient, and every required saturation follows from the partial positive-line argument and saturation of J. No step uses that the raw derivative image of E equals E^+.

## 7. Actual constant projection in the remaining zero-channel case

For J=0 with `rank F=9`, the actual derivative-image sequence gives

    rank F^+=10,
    deg F^+=-18+18=0,
    F^+/F=O(18).

Every degree of a subbundle of H O is nonpositive. A saturated degree-zero subbundle must therefore be trivial. Its global sections embed as a genuine constant subspace, so

    F^+=C0 O,
    C0=A+V+P,
    dim C0=10.

The character is `chi(F^+)=-P-D+Sym18 W=A+V+P`. No abstract complement is being made horizontal.

The actual inclusion of `F^+/F` into `H O/F` projects into Q as exactly `S(2)=i(O(16))(2)`. This follows from the derivative-image sequence: its kernel on projection is J(2)=0. Consequently

    E intersect (C0 O)=F,
    (E+C0 O)/E=S(2)=O(18).

Crucially, S(2) is saturated in Q by Section 3 of this review. The sum `E+C0 O` is its full preimage in H O, and

    H O/(E+C0 O)=Q/S(2)

is locally free. This proves that the sum is saturated.

Since C0 is an actual constant subspace, quotienting by it gives the actual embedded subbundle

    Z=(E+C0 O)/(C0 O)=E/F=T O(-3)+L

in `(H/C0) O`. Its ambient quotient is exactly `H O/(E+C0 O)`, already proved locally free. Thus Z is saturated. This is the needed projection-saturation proof; local freeness of E/F alone would not have sufficed.

## 8. The final factorization and horizontal contradiction are valid

Under constant projection by C0, the original derivative of E is followed by

    Q(-2) -> (Q/S(2))(-2).

This kills the entire image of the positive O(16) line. The quotient map `E -> A_q/O(16)=L` kills F, so it descends to E/F. Functoriality of the constant connection therefore gives the actual factorization

    beta_Z:
      Z=E/F -> L -> (H O/(E+C0 O))(-2).

It is immaterial whether the final image is saturated. Neither `Z^+/Z=L(2)` nor an exact identification of the full Gauss kernel of Z is needed.

Let `M=T O(-3)` be the canonical top block of Z. It is an actual saturated subbundle: its quotient is L. Every map from M to L is zero by ordinary degree, since the target degrees are -8,-10, or -9. The displayed factorization thus proves `beta_Z|M=0`. In particular, differentiating M lands in Z.

Modulo M, that derivative is the well-defined O-linear internal second fundamental form

    M -> (Z/M)(-2)=L(-2).

The scalar Leibniz term disappears modulo M. The map is again zero by ordinary degrees, because the target degrees are -10,-12, or -11. Therefore differentiating M lands in M itself, inside the genuine constant bundle `(H/C0) O`.

The resulting Grassmannian map has zero differential, hence is constant over C. Its subbundle must have degree zero. But M has rank six and degree -18. This contradiction eliminates the last remaining case, completing all three full-label exclusions.

## 9. Dependency boundary, limitations, and contribution

The defect-zero hypothesis in PR802 Sections 2–5 is used only to establish that the positive O(16) image is saturated in Q(-2). The reviewed proof replaces precisely that use with the scalar-isomorphism argument. The later arguments require saturation of I, obtained from S and J by the exact quotient sequence, not saturation of the full derivative of E.

The audit explicitly does not import:

- `E^+/E=A_q(2)` at defect twelve;
- the identity `Z^+/Z=L(2)`;
- a claim that the raw original derivative image is saturated;
- `H0(E^+)=0`;
- `(E^+)^-=E` or an interior-stage hypothesis;
- a horizontal connection on an arbitrary abstract bundle complement.

The source-overlist data remain necessary formal inputs. This review checks their exact relevant entries and the derivation of all displayed source splittings; it does not recertify the entire historical catalog or construct actual source instances. The mathematical reasoning uses exact sequences, abstract representation identities, universal polar/Euler maps, and degree arguments. No selected actual coefficients, parameters, points, derivative values, matrices, source-instance ranks, selected-model experiments, scans, or large computation were used. The result is an independent mathematical audit, not proof-assistant certification.

The new valid contribution is that an isomorphically mapped highest positive summand can remain saturated even when the full determinant defect is positive. Here this permits the quadratic polar obstruction to transfer and proves saturation of the constant-projected source directly. The final contradiction only needs its derivative to factor through a lower-degree bundle. Those observations establish exactly the three named exclusions and no broader claim.
