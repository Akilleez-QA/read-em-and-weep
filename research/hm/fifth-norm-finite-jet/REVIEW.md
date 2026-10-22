# Independent review: finite vertex-jet reduction of the fifth norm

## Reviewed artifact and verdict

- Reviewed file: `PROOF.md`.
- Exact SHA256: `3e0e9cef6120688bd794e3a911e498c28251d9820a8b9ae972ebc45fdecdf659`.
- Review date: 2026-10-22 UTC.
- **PASS.** No mathematical defect was found in the actual scalar finite-jet theorem: the projection, strict intersection identity, cohomology vanishing, injection, and physical-even lower-grade removal are all valid.
- The earlier conditional matrix-weight section has been removed. The revised artifact correctly states that no reduction to particular matrix jets is asserted. I read the complete revised file and verified that the actual theorem and its proof in Sections 1–4 are unchanged.

This is an independent deductive review, not proof-assistant certification. It does not evaluate the norm class, the second-symbol quotient, or beta4.

## Exact sources checked

The following remote source files were read at the exact cited commits, rather than inferred from PR summaries:

1. [Ordinary stack-square filtration](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md), especially Sections 1–2. Returned blob SHA: `7fe07b9b6971e089abf74b4526fe8adb07d242be`.
2. [PR769 ideal-valued norm construction](https://github.com/Akilleez-QA/read-em-and-weep/blob/1599ab33ec5392433da49fcfbd0bddd5ba1482d3/research/hm/ideal-valued-fifth-norm/PROOF.md). Returned blob SHA: `a421d2dfbc2aafba50684620ef5d13ac6b561a83`.
3. [PR770 faithful norm comparison](https://github.com/Akilleez-QA/read-em-and-weep/blob/b242300110c33627eb77ee5ab36cc81fffa359e4/research/hm/faithful-fifth-norm/PROOF.md). Returned blob SHA: `dd0489148189fdc8dfd8d9c18dd8f2d8ea32761f`.
For comparison with the removed conditional section, I also read [PR713 generic leading-jet theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/5b3943980ecaef78ee7f56fbc015d40955fb24f0/research/hm/leading-vertex-obstruction/PROOF.md). Returned blob SHA: `fe33455d86f6094f9b5d31350869a4eba066302f`.

Current PR1 was also checked. Its latest comment read was [6348953364, 2026-10-22 19:04:45 UTC](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6348953364). The present statement agrees with that frontier: scalar-square nonvanishing is not identified with beta4, faithfulness is already resolved, and the norm class remains unevaluated. The bulk PR-fetch endpoint returned a transport error; the read-only REST metadata/comment route succeeded. There is no remaining source-access blocker.

## 1. Projection to the vertex quotient

The pinned square-filtration source supplies all the necessary distinctions:

- Qsq is the tame pushforward of the ordinary square on the smooth stack, not a square of the coarse ideal.
- The conic and vertex quotient supports are disjoint.
- The conic quotient's physical-even part is O_C(6), while its conormal part is odd.
- J^6 R_L=0, with physical-even vertex grades 0, 2, 4.

The pure-positive sextic block has cover degree twelve. It restricts isomorphically to H0(O_C(6)) and lies in J^6, so its restriction to R_L is zero. Thus every conic component of the restriction cokernel can be killed independently of the vertex component. More explicitly, if a vertex section is ambient, subtract that ambient section first; the remaining conic section is removed by the pure-positive sextic block. This proves both surjectivity and injectivity of

    H1(Qsq)_+ -> H1(A_L)_+.

The map of scalar quotients induced by f Qsq subset f A_L has this map as its connecting-map comparison. Since f is a non-zero-divisor, replacing the full norm quotient by C_L does preserve the actual obstruction class and its complete ambient quotient, not merely its dimension.

## 2. Strict multiplication survives every source zero

On a negative-coordinate chart meeting L, the associated graded ambient ring is the even binary polynomial ring over the local ring of L, with the indicated twists. It is a domain. The leading form of f has order two and is a^4 h. At a zero of a, this leading form is still a nonzero element of that domain; it is not a unit, and its specialization to a closed fiber may vanish. The proof needs sheaf-level injectivity, not fiberwise injectivity or an invertible leading coefficient.

For s outside J^6, choose its first nonzero grade r<6. The product of its leading form and a^4 h is nonzero in grade r+2<8. Therefore fs cannot belong to J^8. This establishes

    (f O_Q(6)) intersect J^8 O_Q(16) = f J^6 O_Q(6).

Because J^6 O_Q(6) is contained in A_L, the asserted identity with f A_L follows. Outside L, J is the unit ideal and A_L=O_Q(6). No rational division or extension from C(L) is used.

## 3. Vanishing and injectivity of truncation

The fixed ambient positive/negative coordinate decomposition gives the actual ambient jet decomposition, viewed over L using the coordinate projection from a neighborhood of L. Its physical-even part at twist six and orders below six is

    O_L(6) + Sym4 U tensor O_L(4) + Sym8 U tensor O_L(2).

Every global section of each coefficient bundle is the restriction of the corresponding ambient polynomial block. This is a decomposition of the ambient thickening and does not assume a decomposition of the actual stack-square quotient. Together with H1(O_Q(6))=0, the restriction sequence gives

    H1(J^6 O_Q(6))_+=0.

The exact kernel sequence for truncation is correctly derived from the strict intersection:

    0 -> f J^6 O_Q(6) -> J^8 O_Q(16) -> T -> 0.

Multiplication by f identifies its first term with J^6 O_Q(6), compatibly with physical parity. Hence H0(J^8 O_Q(16))_+ surjects onto H0(T)_+. If a global section of C_L becomes ambient after truncation, subtract the ambient lift; the remainder lies in H0(T)_+ and is ambient by this surjectivity. This proves equation (3).

The argument uses neither a surjectivity assertion for H0(C_L)->H0(C_<16) nor a homogeneous presentation of the actual square ideal. It applies to the whole norm-class space, so it also preserves the subsequently transported second-symbol quotient.

## 4. Lower-grade removal and the surviving sheaf

The ambient restriction map to R_L is the identity in physical-even grades zero and two. Therefore an even local section of A_L has no term below order four. Its grade-four kernel is exactly the pinned relation bundle P4 O_L(-2) inside Sym8 U tensor O_L(2). Odd ambient grades have negative physical parity, and taking the even summand is exact over C.

Since f has order two, its even relation image modulo J^8 lies only in order six. All lower even blocks of the norm errors therefore glue as ordinary global ambient jet sections. At twist sixteen their coefficient bundles are

    O_L(16), Sym4 U tensor O_L(14), Sym8 U tensor O_L(12),

and every global section lifts to its ambient polynomial block. Subtraction removes them without affecting the obstruction. Order seven is physical-odd, and order eight and above are killed by the truncation. Thus only ordinary order six, equivalently cover degree twelve, remains.

For clarity, the surviving relation can be written as the sheaf image of the injective map

    P4 O_L(-2) -> Sym12 U tensor O_L(10),

obtained by composing the actual grade-four relation inclusion with multiplication by a^4 h. The quotient must retain the actual, generally non-saturated image. In particular the quotient can have torsion at zeros of a; replacing a by an invertible element of C(L) loses precisely information the proof correctly retains.

As a consistency check, the cokernel E_f of this displayed map satisfies

    H0(E_f) / im H0(Sym12 U tensor O_L(10))
        = H1(P4 O_L(-2)) = P4.

The equality follows from H1(Sym12 U tensor O_L(10))=0 and uses the full image sheaf, including source-zero torsion. This is consistent with the established norm target and explains why retaining the order-six relation is essential. No splitting of the square thickening is required: higher actual relation terms vanish after multiplication and truncation.

## 5. Revision check and presentation notes

The initial version had SHA256 `f06be1409416548f6b16cebfa7d530144e26570100556b097f9917399bc00438`. It included a conditional matrix-weight interpretation relying on extra global frame and transition hypotheses not proved by PR713. That interpretation was not used by Sections 1–4. The final version removes it completely and keeps the invariant norm-error truncation theorem only. This resolves the sole presentation recommendation from my initial examination.

The final editorial revision adds direct immutable links to PR769, PR770, and the square-filtration source, and removes the obsolete “harmonic-weight” wording from the scope sentence. Reversing exactly these changes reproduces the previously reviewed SHA256 `86038c6b038447586ef203ceb547d86e4e386fc524cbdc0961222b7a52eb0e44`. Thus the final changes are verified to be editorial only, and PASS applies to the final hash above. No outstanding recommendations or blockers remain.

## Scope compliance

No actual HM coefficient, selected source or point, matrix, rank, derivative, or local model was evaluated. No large computation was run. No remote file, comment, PR, or other external state was written. The only output is this local review. The theorem reduces the necessary scalar data; it does not compute their class, prove beta4 nonvanishing or vanishing, establish higher lifting, or infer algebraicity.
