# The exact middle pairing: a twelve-dimensional radical and marked S complement

**23 October 2026 · PR1091, read in full**

[Immutable proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/e88f289033dd638591b6bf73ff2b2dc890b9708a/research/hm/source2-pure-v-middle-pairing/PROOF.md), blob `5615f2b1c73e6753cf9fd18ed8da7f55c0e02c3b`.

## Actual pairing and exact dimensions

Retain actual source2 nonzero pure-V compatible-radical hypotheses. Write J3=ker j3, K3=ker Q3∩ker j3 and F3=W im h. The curried actual pairing is

    A_h:J3 → W*⊗I2,    A_h(v)(n)=hY_n v.

It is well-defined and onto W*⊗I2=S+T, with exact kernel character 3W′+2S+4T. It kills F3. On the sixteen-dimensional quotient K3/F3 its image is exactly the unique S in W*⊗I2, and

    0 → R_pair → K3/F3 --Ā_h→ S → 0,
    R_pair ≅ 2W′+2S,    dim R_pair=12.

R_pair is the actual joint radical of the pairing, not a chosen sum of multiplicity copies. The canonical marked string S_can=U3 supplies an actual complement after passage to the quotient:

    K3/F3 = R_pair ⊕ S̄_can,    dim S̄_can=4.

These are exact vector-space and map dimensions, **not eliminated fractions of a search space or completion measures**.

| Space or mechanism | Exact dimensions | Meaning |
|---|---|---|
| Degree-three common-kernel quotient K3/F3 | 16 = 12 + 4 | Pairing radical plus actual marked S complement |
| Residual-large degree-five terminal piece | 6 | Marked residual T; generated-module length 45 |
| Nonzero-N0 degree-five terminal piece | 12 | 2T, possibly a residual graph; generated-module length 51 |

The last two rows concern different degree-five spaces and unselected mechanisms, not summands of the first row.

## Surjectivity with actual maps

For v∈J3, Q2hY_n v=j4Y_n v=Y_nj3v=0; intersecting im h with ker Q2 puts the value in I2. If h|NC4 is nonzero, the actual Koszul isomorphism NC3→W⊗NC4 and the surjection NC4→I2 make A_h onto.

If h|NC4=0, the genuine quotient NR→N8 permits descent. Its D channel is λ times the second transvectant, with λ≠0 forced by the marked D_can and no numerical scalar chosen. The relevant universal map

    U:A⊗Sym⁵W → W*⊗Sym⁴W,    U(u)(ℓ)=C2(ℓu)

has rank ten and kernel the complete polarization of Sym⁷W. Multiplication by ℓ acts only on the second polynomial factor. A specified ten-by-ten determinant is 70808371200, and multiplication after polarization is 21 times the identity. These are full representation-map certificates, not sampled source ranks.

The T output is detected by xC2(yu)−yC2(xu)=2(a,g)₁. The S output is detected by C2(ℓ(Xy−Yx)²g)=84ℓg. Actual quotient naturality transports the result without splitting NR or choosing a lift of N8.

All S copies in J3 lie in K3, since the targets of Q3 and j3 have no S. The entire T-isotypical part of K3 equals that in F3 and is killed; W′ also maps to zero. Thus the restriction has exactly S image and radical 2W′+2S, not just a rank bound.

## Why the complement is canonical, and only on this quotient

The coherent actual marked string satisfies Y_n f3(s)=f4(ns), with f3 mapping onto S_can and h f4 an isomorphism to I2. Hence the pairing on S_can is literally h f4(ns). It is nonzero, and its curried restriction is an isomorphism onto the unique S image. S_can⊂K3 and S_can∩F3=0, so its quotient image canonically splits the sequence above.

Writing a=Ā_h and b=a|S̄_can, the projector is inclusion·b⁻¹·a. It has kernel R_pair and image S̄_can and is unchanged by rescaling the coherent identifications.

The resulting pairing quotient has parameter sequence

    0 → ((K3/F3)/R_pair)⊗O(−1) → I2⊗O → O(4) → 0.

It is cubic-to-quartic multiplication up to an unselected nonzero scalar, with the quotient canonically identified with S̄_can. This does **not** choose a complement to F3 inside the pairing kernel or give a negative-horizontal, Q-module or positive-module splitting. The marked S is not identified with the separate opposite-pencil S-to-D channel in [the collaborator report](113-opposite-forced-channels-source-report.md).

## Remaining boundary

Endpoint sixteen remains necessary, with its two terminal mechanisms unselected. The alternating coefficient is already zero by PR1089, but the symmetric diagonal R, including zero versus nonzero, remains unselected. This pairing theorem supplies neither a source-pair cut nor a positive/full-adjoint conclusion. Four necessary pairs remain. Its finite coefficient and projector checks support, rather than replace, actual-map and coherent-quotient arguments.
