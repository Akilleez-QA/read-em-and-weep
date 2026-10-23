# Independent review: source127 a-b-c-f structural reduction

## Verdict and reviewed object

**PASS for the stated partial, necessary structural reduction.** The proof establishes that the low D row cannot vanish. If the high row vanishes, the actual D block and its first span form the standard degree-six osculating flag in their actual constant span. If both rows are nonzero, the combined external map is everywhere onto and its kernel has one of the two stated equivariant splittings. It does not establish that either remaining case is realizable, exclude the whole a-b-c-f source, or remove a profile label or necessary pair.

This review is independent of the proof's authoring argument. I read the entire frozen proof and the cited high-only proof, checked the actual-presentation and strict-top inputs and the relevant original catalog records, reconstructed the sheaf arguments, and independently recomputed the small fixed character checks using the affine E8 McKay graph rather than the verifier's quadratic-number character table. The supplied verifier also passed. The verifier is supporting evidence for fixed representation arithmetic, not a substitute for the sheaf reasoning below.

Reviewed bytes, SHA256:

- `PROOF.md`: `0131265788f518421265bb94ffd8d3f78f2e60753ac3fc515c6810c9b69803de`
- `verify.py`: `595dd2b34c8ea3d391c380914ae63ae5dddb3fe7ad0004b0afcddbe0e38fc6d4`
- `REPRODUCE.md`: `f7aeca601a8efeecf2f3a401bbd5ec3a6109a72f01fda40e3187da14b31c2c59`
- `audit-inputs/manifest.json`: `11305a5ed1ed2d4fcaf31cbfbaf8dd92c4124dc25958107b37c45919157b9756`

Neither the frozen proof nor its verifier was changed during review.

## 1. Authenticated inputs and precise dependency boundary

I recomputed each Git object hash as SHA1 of `blob <byte length>\0` followed by the exact file bytes. All five match the manifest:

| Local input | Git blob | SHA256 of local bytes |
|---|---|---|
| ACTUAL.md | b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3 | a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256 |
| STRICT-TOP.md | d7506dae49b4be43230450c4132bd5db91f137ef | 53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08 |
| pairs.json | fe0afa410d89340d3082dc814277f89fbb582c19 | 6002ad138a41d98c351130a29703722979f31b8da90d7c75a120f28bf89480eb |
| frontier.json | 8b5971092f9ef762584912609fd5e9301c4e271d | a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad |
| HIGH-D-KERNEL.md | 3448047b9f67b258955f0fe53c3368b6f7615d9e | a886ede0c620726e422df8b897cdfaaa35da6d3698fb2130fa4d90d517c5e72d |

The first four are pinned to commit `db51525015bb7c5e825833d550d08dedf6f6ea96`; the last is pinned to `2db172b32dc014c06521a3fcba20261db5bb00fa`. Exact repository paths and immutable source URLs are in the authenticated manifest. Hash matching authenticates these supplied source bytes; no claim of a fresh remote retrieval is needed.

The catalog row with zero-based index 127 has A=[(-8,one),(2,one),(16,one)], B=[(-18,one),(-4,one),(6,one)], defect zero, and contains the tuple (1,1,1,0,0,1,0,0). The frontier record has ID G3.11.cce6e3ba4eeb, profile 11, source_index 127 and original_defect zero. Substitution into the actual splitting formula gives exactly

    E = D(-2) + Wp(-3) + T(-3) + V(-4) + O(-8).

This has rank 17 and degree -54. The negative highest degree and strict-top result give the actual H0(E)=0 and H0(E^-(2))=0. As in the pinned high-only proof, the original defect-zero convention is used to identify the derivative image with A_q and hence the saturated first quotient with A_q(2)=O(-6)+O(4)+O(18). No positive-defect source is silently included.

Only Sections 2-3 of HIGH-D-KERNEL.md are transferred as a conditional kernel theorem, together with its elementary image lemma. The use of two D multiplicities in its Section 2 is solely to produce a high-only subblock in that other source. In the present low-row-zero branch, strict-top already forces the unique top D block to have nonzero high row. Once that row exists, the basepoint and cohomology arguments use only D(-2)->O(16), not the other summands of E.

More explicitly, a nonzero D-valued degree-eighteen row has five independent coefficient sections. A common invariant divisor has degree at most 14. Its only possible positive degree is 12, because there is no invariant of degree 14 and the central involution rules out odd degrees. Dividing a degree-12 factor would require D in Sym6 W=V+P, which is impossible. The row is therefore onto. The kernel has rank 4, degree -26, H0(K(2))=0, H1(K(2))=A+V+2P, and chi(K(3))=-W-Wp-T. The allowed higher-degree atoms in the pinned proof force O(-10), O(-6), and Wp(-5), respectively supplying the required negative T, W, and Wp; they fill rank 4. Thus the transferred kernel is precisely

    O(-6) + Wp(-5) + O(-10).

No whole-source conclusion from the other source is transferred.

## 2. Actual derivative images and saturation

Let beta_F be the derivative of the saturated subbundle F in the constant ambient bundle, let K be the kernel of its external component to Q(-2), and let J be the image of K in (E/F)(-2). These are actual coherent images, not formal summands chosen by character subtraction.

Write I=im(beta_F), L0 for the external image, and B=(H O/F)(-2). The exact sequences of image sheaves give

    0 -> J -> I -> L0 -> 0,
    0 -> (E/F)(-2)/J -> B/I -> Q(-2)/L0 -> 0.

When both indicated quotients are locally free, B/I is locally free. Consequently I is saturated. Its untwisted preimage M in H O is also saturated, and

    M/F = I(2),
    (E intersect M)/F = J(2) inside E/F.

The last identity is the kernel of the actual projection M/F -> Q. It is stronger than an abstract isomorphism: it identifies the embedded subsheaf of the original E/F. This validates every later use of the original R=Wp(-3), the graph line, and the retained scalar factor.

For a quadratic inclusion F=D(-2), the first polars provide a surjection D W O(-1) -> M; Euler's identity includes the values. Thus M(1) is generated. Since M lies in a constant bundle, every splitting degree of M is either -1 or 0. This is used only after proving saturation; it does not assert that a chosen splitting is horizontal.

In the low-row-zero branch the internal target is

    Wp(-5) + T_src(-5) + V(-6) + O(-10).

The exact Hom possibilities from the transferred kernel are:

- Wp(-5) -> Wp(-5), one scalar channel;
- O(-10) -> T_src(-5), one channel;
- O(-10) -> O(-10), one scalar channel.

There is no channel from O(-6), and no further channel from either other atom. In particular the T-valued quintic row cannot be dropped. Its common zero divisor, if nonempty, would have invariant degree at most 5, contradicting the minimal invariant orbit size 12. It is a saturated line inclusion. A nonzero equal-degree scalar component is an isomorphism. Therefore the full image J0 of the scalar kernel line is saturated, including when both T and scalar components occur. Its image has no intersection with the separate Wp factor. The four alternatives for J in the proof are exhaustive and saturated.

For J=0 or Wp(-5), degree(M) is 8 or 2, impossible in a constant bundle. For J=J0, rank(M)=7 and degree(M)=0, so M is an actual constant seven-space, with representation A+P. For J=Wp(-5)+J0, rank(M)=9 and degree(M)=-6, giving three degree-zero and six degree-minus-one directions. The two Euler characteristics identify these as A and T, respectively. The constant A is canonical as the global sections of M. The remaining T(-1) is not assumed to be a horizontal summand.

## 3. Constant high capture and the scalar component

In the constant-seven-space case M maps onto the saturated high line L. Projection by the actual constant M gives a saturated E/N in (H/M) O. In the linear case, the canonical constant A cannot map to O(-6) or O(4): the first Hom vanishes by degree and the second because A is absent from Sym4 W. Its high map is nonzero, since otherwise A would be contained in E, contradicting H0(E)=0.

For A O -> O(18), the three coefficient sections are independent. A common divisor has degree at most 16. Degrees 14 and 16 have no invariant and odd degrees are impossible, so only degree 12 remains. A residual degree-six A covariant is impossible because Sym6 W=V+P. Thus A captures the whole saturated L, not merely its generic fiber.

It follows that E+A is saturated in H O and that E'=(E+A)/A is saturated in (H/A) O. The projected derivative image is exactly the two remaining rows O(-8)+O(2); constant projection removes L coherently from the saturated original image. Since M/A also embeds as a saturated bundle and A already captures the image of M in Q, there is an actual sequence

    0 -> M/A = T_lin(-1) -> E' -> E/N -> 0.

No splitting of this extension is used.

Let S0=J0(2). If it has nonzero scalar component, S0 is the graph of a map from the original O(-8) into T_src(-3). The quotient of T_src(-3)+O(-8) by that graph is T_src(-3). Thus the quotients displayed in Section 3 are correct as actual bundles: the constant case retains R+T_src(-3)+V(-4); the linear case retains T_src(-3)+V(-4).

All of these factors, and T_lin(-1), have zero Hom to O(-8) by degree. Applying the left-exact Hom(-,O(-8)) sequence to the possibly nontrivial extension proves Hom(E',O(-8))=0. The constant case has the same direct vanishing. Both contradict the retained negative derivative row. This eliminates the scalar component without discarding the possible T component or assuming that E' splits.

## 4. The T-only component and the trapped cubic family

The nonzero T-only map is unique up to scale and is the complete quintic Euler inclusion. Dualizing complete degree-five evaluation and twisting gives

    0 -> O(-8) -> T_src(-3) -> D(-2) -> 0.

Crucially, this quotients the T_src factor; it does not consume the separate original scalar O(-8). Hence the two E/N quotients in Section 4 retain that original scalar exactly as claimed.

In the constant case, the original R=Wp(-3) has no external row after removal of the high line: Hom(R,O(2))=0 because Wp is absent from Sym5 W, and the negative row vanishes by degree. Its possible derivative into the remaining factors of E/N, after twisting by -2, also vanishes by degree. R is saturated in the projected constant ambient bundle, so zero second fundamental form makes it a constant subbundle in characteristic zero. Its negative degree is a contradiction.

For the linear case, the following coefficient-kernel fact supplies the needed actual geometry. If B=U(-1) embeds in C O and C is its constant coefficient span, write mu:U W -> C for its coefficient map and Z=ker(mu). At a line ell in W, mu is injective on U tensor ell. Thus projection of Z to U tensor (W/ell) is injective; a coefficient relation is precisely the condition that the transverse derivative lies back in B. Using W O/ell=O(1), this identifies the derivative kernel as Z(-2) inside B. This is an equality of bundle kernels, not merely equality of characters.

The projection of F=D(-2) into M/A=T_lin(-1) is nonzero because rank(F)=5 exceeds rank(A)=3. The one-dimensional equivariant Hom space consists of the universal multiplication-by-ell inclusion, which is everywhere injective. Its derivative stays in M/A because the derivative of F stays in M. The coefficient kernel consequently contains D in

    T W = D + V + P.

The constant span C_T is a quotient of V+P. A saturated negative rank-six bundle cannot span at most six constants: in rank six it would equal that constant bundle, and smaller rank is impossible. Therefore C_T=V+P and the coefficient kernel is exactly D.

The identity N/F=R+S0 inside E/F places the entire original R inside M. Choose an equivariant abstract splitting M=A O+T(-1). Its projection of R to A is zero because A Sym3 W=W+S+T has no Wp; this justifies injection of the original R into M/A without interpreting the splitting as horizontal. Its coefficient span is both a quotient of Wp Sym3 W=V+D and a subrepresentation of V+P. It is nonzero and therefore exactly V. Its rank-two family cannot be a constant plane, since that would give a proper constant coefficient span. Its saturated first span is consequently all V O.

On the other hand, the external derivative of R in E' vanishes after high capture, and its derivative toward E'/T_lin(-1) has target D(-4)+V(-6)+O(-10), all too negative. Thus the actual derivative of R stays in T_lin(-1). Saturation of the latter implies that the saturated first span V O lies in it, contradicting H0(T_lin(-1))=0. This eliminates the final low-row-zero case.

This argument never assigns an osculating rank to a nonconstant extension by adding abstract ranks. It traps an actual coefficient span inside an actual saturated negative subbundle.

## 5. Low-only row and the standard flag

After the preceding exclusion, the low row is nonzero. If the high row is zero, the low row is the complete quartic evaluation D(-2)->O(2), hence is onto with kernel S(-3). Every internal target has degree at most -5, so this kernel has zero internal derivative image. The image lemma applies with J=0 and the saturated external O(2).

The actual first span has rank 6 and degree -6. Since its only possible splitting degrees are -1 and 0, it is entirely linear. Its equivariant twist-one sections identify it as T(-1). The inclusion D(-2)->T(-1) is the unique Euler inclusion. The coefficient-kernel argument in the previous section then forces the actual constant span to be V+P=Sym6 W.

The coefficient map T W -> V+P kills D and is nonzero on both remaining irreducibles. Each appears with multiplicity one. Rescaling the two irreducible summands by a constant equivariant automorphism therefore identifies this map with symmetric multiplication Sym5 W tensor W -> Sym6 W. The embedded D(-2) is then the image of multiplication by ell twice. These are exactly the standard U_4^6 and U_5^6 subbundles. The constant span of F and of its first span agree, since taking first polars does not leave the original coefficient span. This proves the claimed actual standard-flag identification up to constant equivariant isomorphism, not a choice or evaluation of source coefficients.

## 6. Combined-row surjectivity

If the high row is nonzero, its restriction to the low kernel S(-3) cannot vanish. Otherwise it factors through the quotient O(2), giving an invariant degree-14 form. There is none, so such a factorization would make the high row zero.

A nonzero S-valued degree-19 row has four independent coefficient sections, so any common invariant divisor has degree at most 16. Only degree 12 is possible in that range. Removing it would require S in Sym7 W=Wp+T, which is absent. Thus the restricted row S(-3)->O(16) is onto. Combining this with the low surjection proves that F->O(2)+O(16) is everywhere onto, not merely generically of rank two.

The exact sequence now gives rank(K)=3, degree(K)=-28, H0(K(2))=0,

    H1(K(2)) = A+V+2P+D,
    chi(K(3)) = -W-Wp-2T.

For example the low row is already an isomorphism on the coefficient D at twist two, so injectivity there does not require a numerical rank experiment.

## 7. Independent exhaustive rank-three splitting check

Equivariant splitting is legitimate by the characteristic-zero splitting argument in the actual input. Since H0(K(2))=0, every degree is at most -3. Rank three has only the following coefficient-dimension partitions: 3, 1+1+1, or 2+1. There are no nontrivial one-dimensional representations. A single three-space at one degree would make the total degree divisible by 3, contrary to -28.

For scalar lines, central parity forces even degrees, and degree -4 would contribute a forbidden trivial representation to H1(K(2)). Therefore each scalar degree is at most -6. The five unordered positive degree triples summing to 28 are exhaustive. Their characters are:

| Positive degrees | H1(K(2)) | chi(K(3)) |
|---|---|---|
| 6,6,16 | 1+3A+P+D | -3W-S-T |
| 6,8,14 | 2A+V+2D | -W-2S-T |
| 6,10,12 | A+V+2P+D | -W-Wp-2T |
| 8,8,12 | P+3D | -Wp-2S-T |
| 8,10,10 | 2V+2P+D | -S-2T |

For U(-j)+O(-k), U is W or Wp, j is odd and at least 3, k is even and at least 6, and 2j+k=28. These give precisely five pairs and ten choices:

| U | j,k | H1(K(2)) | chi(K(3)) |
|---|---|---|---|
| W | 3,22 | A+V+2P+D | W-Wp-S-2T |
| Wp | 3,22 | A+V+2P+D | -S-2T |
| W | 5,18 | 1+2A+V+P+D | -2W-Wp-S-T |
| Wp | 5,18 | A+V+2P+D | -W-2Wp-S-T |
| W | 7,14 | 2A+V+2D | -W-2S-T |
| Wp | 7,14 | A+2V+2D | -S-2T |
| W | 9,10 | 2V+2P+D | -S-2T |
| Wp | 9,10 | A+V+2P+D | -S-2T |
| W | 11,6 | A+V+2P+D | -W-Wp-2T |
| Wp | 11,6 | 1+2A+V+P+D | -2W-Wp-S-T |

These tables were independently obtained from the McKay tensor rules

    W*1=W, W*W=1+A, W*Wp=P, W*A=W+S,
    W*V=T, W*P=Wp+T, W*S=A+D,
    W*D=S+T, W*T=D+V+P,

and the recurrence Sym(n+1)=W Sym(n)-Sym(n-1). For an atom U(-j), its twist-two H1 is U Sym(j-4) when j>=4 and zero when j=3; its twist-three Euler characteristic is U for j=3, zero for j=4, and -U Sym(j-5) for j>=5. Thus the degree-minus-three edge cases are included, rather than accidentally discarded by a higher-degree atom list.

Exactly the scalar triple (6,10,12) and the two-space/line choice (W,11,6) satisfy both required characters. Their ranks and degrees are 3 and -28. This proves the two stated necessary kernels and exhausts all equivariant rank-three splitting patterns. It is not an enumeration of maps, selected source models, parameters, or instances.

## 8. Scope, restrictions, and publication assessment

The supplied verifier ran successfully on the exact pinned bytes. The independent representation calculation was confined to the fixed nine irreducibles, symmetric powers needed by the argument, five scalar triples, and ten two-space/line options. No actual HM/source coefficients, parameter choices, points, derivatives, matrices, source-instance ranks, models, scans, or large computation were used. All work was performed in the supplied cloud filesystem; no local Codex or user-computer execution was used.

The actual internal images of either surviving two-row kernel have not been classified or excluded here. The review does not turn a kernel character into an internal vanishing assertion. Nor does the standard low-only flag alone determine every later Gauss gain. The whole a-b-c-f realizability question and full-profile test remain open.

No blocking mathematical gap was found in the frozen proof at the stated scope. The partial reduction is suitable for publication with its five exact input pins and this review. Any subsequent stronger exclusion must retain the surviving internal channels and separately justify its actual-image and saturation steps.
