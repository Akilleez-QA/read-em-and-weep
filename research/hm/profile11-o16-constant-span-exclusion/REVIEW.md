# Independent mathematical review: the two zero-defect O(16) labels

## Verdict and exact object reviewed

**PASS.** The argument in `PROOF.md` excludes both complete labels

    G3.11.16ee1aa30a9c
    G3.11.db4688c30472

under the actual-bundle and necessary-source-catalog inputs explicitly pinned in that proof. I found no mathematical defect in the complete small-kernel classification, the internal-image saturation arguments, first-polar generation, the three-channel obstruction, or the final constant-projection argument. In particular, the proof really establishes saturation of the projected source before using its connection and really establishes the exact Gauss kernel `Z^-=T O(-3)`.

The reviewed proof has SHA256

    a18a6990f719592d71853692157161a9ca5fe6b7f2a78edacbfa060bb3513459

The proof was not edited during this audit. The verdict applies to those exact bytes, not to a later revision.

The audit uses formal representation identities, exact sequences of bundles, and universal differentiation arguments only. No actual HM/source coefficient, parameter, point, derivative value, matrix, source-instance rank, or selected-model experiment was evaluated. No large computation or all-twist envelope was run.

## 1. Immutable public dependencies read

Repository: `Akilleez-QA/read-em-and-weep`.

The first five files below were fetched at commit

    db51525015bb7c5e825833d550d08dedf6f6ea96

under `research/hm/order-four-quadratic-load/`. The fetched contents were checked against the returned Git blob identities. The SHA256 values below are for the exact fetched UTF-8 file bytes, without an added newline.

1. [ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md)

       SHA256 a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256
       Git blob b93e0b3589ef71cf2c029fd07a6bdb1da8ba92b3

2. [NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/NEGATIVE-GAUSS-KERNELS-STRICTLY-LOWER-THE-TOP-SLOPE.md)

       SHA256 53ff5daf7e656bb1ec2dcf5feebd2813e2dbfbd6489a3a65117960f492b4cc08
       Git blob d7506dae49b4be43230450c4132bd5db91f137ef

3. [ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ONE-ONE-ENDPOINT-DEGREE-WINDOWS-AND-159-NECESSARY-PAIRS.md)

       SHA256 8d3f7f9f0492484edc104cf070ed72be4b969545a1e4b184be37a00dc5e7cac0
       Git blob dcacf0bcdef8377c1ed7654e5b82659ea409456e

4. [one-one-endpoint-necessary-pairs.json](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/one-one-endpoint-necessary-pairs.json)

       SHA256 6002ad138a41d98c351130a29703722979f31b8da90d7c75a120f28bf89480eb
       Git blob fe0afa410d89340d3082dc814277f89fbb582c19

5. [rank-three-quotient-frontier-144.json](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/rank-three-quotient-frontier-144.json)

       SHA256 a6fc9ec680d1866782e0233c234c5d80d398e9fc77734b59e61040ffc92021ad
       Git blob 8b5971092f9ef762584912609fd5e9301c4e271d

6. [profile12-quadratic-block-exclusion/PROOF.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/d2b43060c83328dd5118aee6b9288fcfa0c873ac/research/hm/profile12-quadratic-block-exclusion/PROOF.md), at commit `d2b43060c83328dd5118aee6b9288fcfa0c873ac`.

       SHA256 622763aac375db7e17bc7cab472f1afda0477b0f769371a3b3ef845cd5c9e3b1
       Git blob 46a0de762000f21182f6d3168f3ecfd63adaf75f

   Only the profile-free saturated derivative-image and quadratic Gauss-gap arguments are used. The interior-stage vanishing elsewhere in that file is not imported.

7. [profile11-quadratic-polar-obstruction/PROOF.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/2172e4a7abbbe232f9f448bea6fa01dee7927460/research/hm/profile11-quadratic-polar-obstruction/PROOF.md), at commit `2172e4a7abbbe232f9f448bea6fa01dee7927460`.

       SHA256 3a55f2c37548c7b05bf0f39f775ab37807c9f852d3601f77271fc0dd052022ed
       Git blob a62a56f6b8f97e02b3eab6fe3a47ec3bedb6c6b1

   The universal first-polar construction was checked directly, rather than treating a prior label exclusion as a substitute for it.

Both JSON files were parsed in full; the relevant label and source records were compared exactly. No historical status field was mistaken for the new exclusion theorem.

## 2. Exact labels and complete source overlists

The frontier records identify the first label with source index 46 and the second with source index 51. Both are profile `11`, with original defect zero, total quotient degrees `a=-2`, `b=-4`, and the exact splittings stated in the proof:

    index 46: A_q=O(-10)+O(-8)+O(16), B_q=O(-18)+O(6)+O(8);
    index 51: A_q=W O(-9)+O(16),     B_q=O(-18)+W O(7).

The index-46 source tuple list is exactly

    (0,0,0,0,0,2,0,1),
    (0,0,0,0,1,1,0,1),
    (0,0,1,0,0,1,0,1),
    (0,1,0,0,0,1,0,1).

The index-51 list contains precisely those four, followed by

    (0,0,0,0,0,1,1,0),
    (0,0,0,0,1,0,1,0),
    (0,0,1,0,0,0,1,0),
    (0,1,0,0,0,0,1,0).

The actual-source formula gives the top coefficient

    R_2=(c+g+h-1)V+(d+e+g+h)P+(f+g)D,

with the lower blocks encoded by `a,b,c,d,e,f,g,h` as in the pinned source theorem. Substituting the eight listed tuples gives exactly `E0,U6,E3,E6,E10,U13,E12,E13` in the proof, including the two easily omitted extra types with top coefficient `2P+D`. Thus neither exclusion silently drops a compatible source.

These are necessary overlists. Their use does not require, and this review does not assert, realizability of any member.

## 3. The onto top quotient and actual-image saturation

The actual assumptions supply a saturated `E` in `H O`, rank 17 and degree -54, with `H0(E(1))=H0(E^-(2))=0`. The canonical maximal-slope block `F=R O(-2)` is saturated in both `E` and `H O`. Since all negative summands of `A_q` have degree at most -8, its quotient map restricts to `p:F -> O(16)`.

Twisting by two and taking sections makes `R -> H0(O(18))` injective, because its kernel lies in `H0(E^-(2))`. Every relevant `R` has dimension at least nine. A nonempty invariant common zero divisor has degree at least 12, since the smallest projective icosahedral orbit has that size. Dividing by such a divisor would leave at most seven independent sections. Therefore `p` is everywhere onto, and the exact sequence (2) in the proof is justified as a sequence of bundles, not merely generically.

Defect zero identifies the derivative image with the saturated `B_q^*(-2)` inside `Q(-2)`. In particular the positive `O(16)` is saturated there. For the internal image `J`, put

    U=(E/F)(-2),  Vamb=(H O/F)(-2).

The image `I` of the actual derivative of `F` satisfies `I intersect U=J` and maps onto the positive line in `Q(-2)`. Thus, when `U/J` is locally free, `Vamb/I` is an extension of `Q(-2)/O(16)` by `U/J`. It is locally free. This proves precisely the saturation required for the actual `F^+` sequence. It does not assume that an image sheaf is saturated just because it is locally free.

The quadratic gap is valid independently of the profile: quadratic values and first two derivatives generate the constant coefficient span, while the derivative of `F^+` factors through its rank-one quotient. Hence that span has rank `r+1` or `r+2`. The first case gives `b=2r`; the second gives a nonzero map `O(b) -> O(2r-b-2)` and therefore `b<=r-1`.

## 4. Complete small K0 classification

The exact sequence `0 -> K0(2) -> R O -> O(18) -> 0` gives

    H0(K0(2))=0,
    H1(K0(2))=Sym18 W-R,
    chi(K0(3))=R W-Sym19 W.

I independently checked the stated decompositions of `Sym18 W`, `Sym19 W` and all needed tensor products by exact abstract character arithmetic. This used only the character-function prefix of an existing arithmetic helper; its envelope, input-dependent main body and selected-source computations were not executed. The argument itself is the following finite support calculation.

For `j>=4`, an irreducible block `U O(-j)` contributes `U Sym^(j-4)W` to `H1(K0(2))`, a genuine subcharacter of `A+V+P`. Thus `(j-3)dim U<=10`, with central parity `(-1)^j`. The complete support is

    A O(-4), V O(-4), P O(-4), Wp O(-5), O(-6), O(-10),

and the respective contributions are `A,V,P,P,A,V+P`.

Here is the completeness check. At `j=4`, only `A,V,P` occur in the budget. At `j=5`, `W W=1+A`, `S W=A+D`, and `T W=V+P+D`, leaving only `Wp W=P`. At `j=6`, besides the trivial coefficient, only `A,V` fit dimensionally, and `A A=1+A+D`, `V A=P+D` exclude both. At `j=7`, the only dimensional candidates are `W,Wp`; their products with `S` are `A+D,V+D`. At `j=8`, only the trivial coefficient fits and produces the forbidden `D`. Odd `j>=9` already exceed dimension ten. At even `j=10,12`, only the trivial coefficient fits, giving `V+P` and the forbidden `P+D`, respectively. For `j>=14`, even the trivial coefficient exceeds the dimension bound.

Degree-three blocks supply exactly their coefficient to `chi(K0(3))`. The six supported lower blocks contribute `0,0,0,-Wp,-W,-T`. Matching both characters consequently yields exactly:

    R=2P+D:
      (Wp+T) O(-3)+V O(-4)+O(-6);

    R=V+P+D:
      T O(-3)+P O(-4)+O(-6), or
      (Wp+T) O(-3)+Wp O(-5)+O(-6);

    R=P+D:
      V O(-4)+P O(-4)+O(-6), or
      Wp O(-3)+V O(-4)+Wp O(-5)+O(-6), or
      T O(-3)+O(-6)+O(-10).

In each row the `-W` in the required Euler character forces `O(-6)` rather than `A O(-4)`. The remaining `V,P` budgets then give exactly the displayed alternatives, including the joint `V+P` contribution of `O(-10)`. All six resulting bundles have the required rank `dim R-1` and degree `-2 dim R-16`. No additional degree-three coefficient can be inserted, because it would change the exact Euler character.

## 5. Source reductions and saturated internal images

For `E0,E10`, `K0(2)` has thirteen negative degrees summing to -18, so each is at least -6 and each degree of `K0` is at least -8. Its internal target has degrees at most -10. Thus `J=0`, and `r=14,b=18` violates the gap.

For `U6,U13`, the classified kernel has degrees at least -6, while the internal target has degrees at most -7. Again `J=0`, and `r=13,b=18` violates the gap.

For `E3,E12`, the only nonnegative-degree Hom channel not ruled out ordinarily is `O(-6) -> V O(-6)`, which is zero equivariantly. Thus `J=0`, and `r=12,b=18` violates the gap. In the second label, `E6` cannot surject onto `W O(-9)`, since only its single `O(-10)` summand can contribute, with image rank at most one.

The remaining matching sources are therefore precisely `E6` for the first label and `E13` for the second. For their first two possible kernels, the only additional apparent channels vanish by `Hom_G(1,T W)=0` and `Hom_G(Wp,T)=0`. For the third kernel, only `O(-10)` can contribute. Its map to `T O(-5)` is the unique nonzero quintic tautological channel; for `E6` there is also the scalar map to the lower `O(-10)`.

A nonzero quintic channel has no fiber zero, because it is the tautological `Sym5` line. A nonzero scalar channel is an isomorphism onto its line summand. Either component, and hence a graph with both components, makes the total map a saturated line embedding. Consequently the only possibilities are `J=0` and a saturated `J=O(-10)`. This supplies the saturation hypothesis used above in every case.

## 6. First polars and the nonzero-channel obstruction

For a quadratic inclusion with coefficient map `a:R Sym2 W -> H`, the value and first derivative at an arbitrary line `l` are exactly `a(R lW)`. This is the image of the global polar morphism `R W O(-1) -> H O`. Once the derivative image is known saturated, this morphism is onto the actual `F^+` everywhere. Therefore `F^+(1)` is globally generated, and its simultaneous inclusion in a constant bundle restricts its degrees to 0 and -1.

When `J=O(-10)`, the actual exact sequence gives rank 11, degree -8, and

    chi(F^+)=A,
    chi(F^+(1))=W+Wp+S+T.

Since `A W=W+S`, it follows that `F^+=A O+(Wp+T) O(-1)` as an equivariant bundle. Crucially `C=H0(F^+)` is the genuine constant three-space inside `H`. Quotienting by it gives a saturated embedded `Rlin=(Wp+T) O(-1)` in the constant quotient. This does not equip an abstract complement with an invented connection.

The projected `F` has exactly the three channels `lambda,mu,nu` in the proof. `nu` cannot vanish, since that would put the rank-five `D O(-2)` in the rank-three constant kernel. If `lambda=0`, the projected image has rank at most six, so the intersection of `F` with `C O` has rank three. Generic containment of `C O` in saturated `F` implies containment as sheaves: its map to the locally free `H O/F` vanishes generically and hence everywhere. This contradicts `H0(F)=0`. Thus both `lambda` and `nu` are nonzero.

Their one-dimensional channel spaces identify them, up to scalars, with the everywhere exact sequences

    0 -> Wp O(-3) -> P O(-2) -> Wp O(-1) -> 0,
    0 -> D O(-2) -> T O(-1) -> O(4) -> 0.

The second sequence is multiplication by the tautological line, with quotient `Sym5(W/l) O(-1)=O(4)`.

If `mu=0`, the projected image contains the full `Wp O(-1)` summand. Each local section lifts locally to `F`, so its derivative lies in `Rlin`. A pure linear bundle reaches its constant coefficient span after one differentiation. Since `Rlin` is saturated in the constant quotient, that constant span lies in it, contradicting its zero global sections.

If `mu` is nonzero, let `q:T O(-1) -> O(4)`. The composite of `q mu` with `ker lambda=Wp O(-3)` cannot vanish. If it did, `q mu` would factor through `Wp O(-1)`, but `Hom_G(Wp,Sym5 W)=0`. It would then be zero on all `P O(-2)`, forcing `mu` to factor through `D O(-2)`, contrary to `Hom_G(P,D)=0`. Thus the composite `gamma` is nonzero. Its two degree-seven sections are independent by irreducibility of `Wp`; an invariant common divisor would have degree at most seven but at least twelve. Hence `gamma` is onto everywhere.

Together `lambda`, `nu`, and `gamma` make the whole projected map onto `Rlin`: first lift its `Wp` component through `lambda`, then lift the remaining `T` quotient through `gamma` and its kernel through `nu`. Local lifts to `F` show that all derivatives of `Rlin` stay in `Rlin`. Its Grassmannian map is therefore constant, impossible for a subbundle of degree -8. This proves the nonzero-channel exclusion with no endpoint no-section assumption on `E^+`.

## 7. The zero channel and exact constant projection

For `J=0`, the actual `F^+` has rank ten and degree zero. Every splitting degree of a subbundle of a constant bundle is nonpositive; hence all ten are zero. The inclusion of this trivial bundle in `H O` is a constant matrix, so this is a genuine constant subsystem `C0 O`, with character `C0=A+V+P`.

The important intersection assertion follows from the actual image diagram, not only from degree: the induced `F^+/F -> E^+/E` is precisely the isomorphism onto the saturated positive `O(18)`. Consequently

    E intersect (C0 O)=F,
    (E+C0 O)/E=O(18).

Both `E^+/(E+C0 O)=L(2)` and `H O/E^+` are locally free. Their extension `H O/(E+C0 O)` is locally free. This proves the claimed saturation of the sum. Only after this step does constant projection produce the actual saturated bundle

    Z=(E+C0 O)/(C0 O)=E/F=T O(-3)+L

inside `(H/C0) O`.

Projection by a constant space commutes with differentiation. More explicitly, the sheaf surjection `E -> Z` lets every local section of `Z` lift locally to `E`; its derivative is the projection of the derivative of that lift. Conversely the projection of every local section and derivative of `E` is generated by local sections and derivatives of `Z`. Thus their raw first spans agree after projection. The original defect zero makes the raw first span of `E` equal to `E^+`, and `E^+/C0 O` is saturated because its ambient quotient is `H O/E^+`. It follows that

    Z^+=E^+/(C0 O),
    Z^+/Z=L(2).

The derivative of `Z`, with target twisted by -2, is the original quotient map `E -> A_q`, followed by the quotient by its positive `O(16)` and factored through `E/F`. This is onto `L`. There is no possible extra divisor or torsion correction here.

In the actual bundle splitting `Z=T O(-3)+L`, all maps from `T O(-3)` to `L` vanish by ordinary degrees. The remaining map `L -> L` is onto and therefore an isomorphism. Thus its kernel is exactly the canonical top block:

    Z^-=T O(-3).

This is an identity for the actual Gauss kernel, not merely an abstract candidate. Its derivative already lies in `Z`; its further internal map to `(Z/T O(-3))(-2)=L(-2)` vanishes by degrees. Therefore this rank-six block is horizontal in the genuine constant quotient. A horizontal subbundle in characteristic zero has constant Grassmannian map and, by saturation, degree zero. Its actual degree is -18. This is the final contradiction.

## 8. Verification boundaries

The two complete source overlists are exhausted. No use is made of `H0(E^+)=0`, `(E^+)^-=E`, a horizontal Birkhoff-Grothendieck splitting, or an unproved assertion that constant projection preserves saturation. Constants in the endpoint `E^+` are allowed and are used constructively.

This is an independent written mathematical audit with a small exact abstract-character cross-check, not proof-assistant certification. The established actual HM bundle inputs and the necessity/completeness of the pinned historical source catalog are inputs; the entire underlying HM construction and the full historical 159-pair enumeration are not reproved here. The new classification and all new geometric inferences needed for these two labels were checked directly above.

The result does not exclude source2, any unnamed label, or a positive-defect counterpart. It does not establish the original global rank goal, a smoothing theorem, or realization of a formal source. No publication or external repository change was made as part of this review.
