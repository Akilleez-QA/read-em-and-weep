# Independent review: completion-separated fifth boundary

## Verdict and exact artifact

PASS. No substantive mathematical defect was found in the stated result or its scope.

This review binds to `PROOF.md` with SHA-256:

`307b1d96ba9bffd582ebbe8c1f3ef9dfb963031c56526514745295ac2085b346`

The review independently checked the weight argument, exact completion law, all normal-index and physical-twist bookkeeping, the two boundary signs, the source-free reference construction, equivariance, and the exact-image conclusion. It is an authored mathematical audit of the cited structural inputs, not proof-assistant verification or a reproof of their entire dependency trees.

## Dependency verification

The following local proofs were fetched at the immutable commits used by the proof and compared byte-for-byte with the copies read during this audit. All comparisons agreed:

- PR685, `449a8df60662bd7a1d93e318ea4f7e6dab28e5ad`, `research/hm/third-lift-uniqueness/PROOF.md`.
- PR739, `9b67dae4d91e81b9e514f4072bfc3774ffd0028f`, `research/hm/actual-scalar-compatibility/PROOF.md`.
- PR777, `490337fee9e8f06fa8bf3e893ab646a37f996bf2`, `research/hm/global-subleading-residue/PROOF.md`.
- PR778, `e527b939f9a8f5cf8967f32048a23a9d830d77c9`, `research/hm/normal-transition-channel/PROOF.md`.
- PR779, `89e02759fde0924a787a8f145d814aceaab93c40`, `research/hm/normal-extension-comparison/PROOF.md`.
- PR780, `c82c3a3b6b513e80a5af21f06ecc52170cb0a056`, `research/hm/transition-boundary-formula/PROOF.md`.

The following original files were also fetched and read at `8d8b5be4ce62c3055bb53be9e16d29cc63072f04`, under `research/hm/order-four-quadratic-load/`:

- `ACTUAL-MULTIPLIED-NILPOTENT-HAS-A-CANONICAL-SQUARE-ZERO-LIFT.md`, Git blob `240b39cc35b02287fb135a39a1b056a05e9cfb20`.
- `ACTUAL-MULTIPLIED-NILPOTENT-COHERENCE-FIXES-ENDPOINT-SCALE.md`, Git blob `72fc7b17cd750ac9f7790ae58001db29f7f09e94`.

The physical filtration proof PR774 was additionally read to check regularity, saturation, parity, and the all-point nature of the coefficient modules. No actual-family coefficient extraction or instance evaluation was performed.

## 1. The first-lift lower bound is valid without source division

The physical-even filtration permits only nonnegative weights in multiples of four. Because `U_a|Q=aN` starts in weight eight, a possible lower-weight term of `U_a` modulo `q²` is exactly `qD0`, with `D0` a regular trace-free coefficient of weight zero. A weight-zero term of `U_a` itself cannot restrict to zero on the cone unless it is zero: divisibility by `q` would require negative weight.

At total weight twelve, the square-zero equation has precisely the contribution `q a{n8,D0}`. Products involving the `q`-part of the weight-eight term have a second factor of `q` and vanish on `2Q`; the square of a cone-leading term starts at sixteen. Injectivity of the last-layer map gives `a{n8,D0}=0` on `Q`.

For a trace-free rank-two pair the anticommutator is its scalar trace times the identity. With the regular leading cubic/quintic pair and `D0=[[x,0],[z2,-x]]`, the relevant scalar is `u f3(2g5 x-f3 z2)`. Regularity of `(f3,g5)` forces `x=z2=0`; this is the same injective coefficient map established in PR780. Multiplication by the fixed nonzero base section `a` is injective on the regular coefficient modules. The proof therefore does not divide by `a`, discard its zeros, or use a merely generic coefficient calculation.

This proves the stated all-point lower bound along `L`, and hence `U_a,8=H(U0)+qH(U1)` modulo `q²`, with `U0=a n8`.

## 2. The exact law gives precisely the asserted weight-sixteen change

PR685 supplies actual sections, rather than only raw monad expressions, and its fourth-lift freedom is `q³Nt`. Multiplication by `a` therefore gives exactly

`ΔK=-q² a U_a tilde(s)+q³ aNt` on `4Q`.

The three possible changes have lower weights sixteen, twenty, and twenty for `s_A`, `s_D`, and the independent fourth-lift term, respectively. Replacing the ambient scalar lift by `tilde(s)+qc` also starts at twenty after multiplication by `q²aU_a`. Thus no term can alter `K12` or any of its fixed harmonic coefficients `A0,...,A3`.

At weight sixteen only the source `s_A` remains. Because it and `a` are base-only coefficients, they commute with the homogeneous harmonic lift and its coefficient operations. The change is exactly

`-q² a s_A H(U0)-q³ a s_A H(U1)` modulo `q⁴`.

Consequently `ΔB1=0`, `ΔB2=-a s_A U0`, and `ΔB3=-a s_A U1`. PR777's frame correction has weight four. Since `U_a` now starts at eight and the difference starts at sixteen, that correction cannot change either required leading piece. The same fixed normalization is used for every completion; no extra completion-dependent frame is silently introduced. Setting `B4=0` is the fixed local extension convention, not a claimed global gauge.

The twists check independently: `U0,U1` have physical twists four and two; multiplication by `a s_A` adds four; thus `B2,B3` have twists eight and six. Their overlap operators remove four and two, leaving the required twist four.

## 3. Variation, sign, faithfulness, and fixed normal contribution

The PR780 formula is linear with all overlap, scalar, and equation-line transports understood in the target chart. Substituting the two negative coefficient changes into its two negative transport terms yields the positive variation

`ΔC=a s_A(M2(U0)+M1(U1))`.

Both full representatives are genuine boundary cocycles, so their difference is a cocycle. The argument does not falsely infer that either transport or normal part of a single representative is separately closed.

PR685 explicitly distinguishes the `q+ta` and `q-ta` conventions. In the latter, used here, the actual fifth-boundary variation is `-beta2_a(s)`. The canonical first-lift source separately verifies agreement of its monad-division convention with target-minus-transport Čech boundaries. These two inputs establish the minus sign in `E(beta2_a(s_A))=-[Theta_a(s_A)]`.

All `s_A` occur in the classified completion torsor, while the `D5` and independent fourth-lift directions disappear from the leading representative. Since `E` is the faithful isomorphism of PR780, the resulting classes give the full exact image, not a generic image, a saturation, or only an inclusion. Constancy of every `A_r` gives constancy of the complete displayed normal-transition cochain in the fixed chart convention. It does not give that cochain an independent cohomology class.

## 4. The source-free cocycle has an independent justification

The coherence identities used here are exact identities of induced sections on `2Q`. On a negative chart, `N_r=U_(r²)/r²` divides only by a chart unit. The established lower bound applies also to `U_(r²)`. Hence both the source correction `-q κ_conn α′N_r` and the change `-2κ_conn qN/(rt)` start at weight twelve, not eight. Their presence in the actual first-normal geometry has not been discarded at an order where it contributes.

It follows that the weight-eight section is independent of the negative generator and factors as

`U_a,8=a m`, where `m=H(n8)+qH(T4)` modulo `q²`.

The source-free gluing argument is valid for a reason stronger than closure after scalar multiplication. PR778 proves exact ambient multiplicativity of the weight-zero triangular transitions `T0`; this is not the generally false multiplicativity of arbitrary harmonic lifts. The actual-versus-reference adjoint correction starts at weight four, and its action on a weight-eight section begins at twelve. Differences between the actual local lifts `N_r` also begin at twelve. Thus the weight-eight representatives `m_i` glue modulo `q²` for the exact reference transitions, including the physical line factors.

Their third-neighborhood connecting cocycle is the quotient of `m_i-Ad(T0_ij)m_j` by `q²`, restricted to `Q`. It has weight zero and physical twist `2-4=-2`, and therefore lies in `J0(-2)`. There is no local `q²` coefficient in the chosen `m_i`. Extracting the transported coefficients gives exactly `-M2(n8_j)-M1(T4_j)=-Theta_ij`. The exact reference cocycle proves closure. In particular the proof does not attempt to deduce closure of `Theta` by canceling a section with zeros in a source-multiplied expression.

The canonical `U_a` family is equivariant by the first-lift theorem. Its weight-eight quotient is intrinsic because the physical filtration is preserved by frame changes. Generator independence gives an equivariant source-free quotient. On comparing translated normalized charts, higher-weight frame corrections cannot change this quotient, and the remaining weight-zero transport has the exact, natural ambient lift of PR778. The reference boundary is consequently equivariant. This proves invariance of `[Theta]` without assuming equivariant individual frames or a global normalization.

## 5. Exact image and limits of the comparison with κ

Substitution of the source-free factorization yields the exact normalized identity

`E(beta2_a(s_A))=-[a² s_A Theta]`.

The extra factor of `a` is essential: one comes from multiplying the classified `J4` change to obtain `K`, and one from `U_a,8=a m`. With `s_A` of twist two, multiplication by `a²s_A` maps `J0(-2)` to `J0(4)` exactly.

The already-established nonzero second symbol forces `[Theta]` to be nonzero. This direction of implication requires neither injectivity of multiplication on cohomology nor a source-value test. The invariant-line theorem of PR778 and nonvanishing theorem of PR779 then imply `[Theta]=cκ` for some nonzero constant in the fixed conventions. Consequently the two source-multiplied image subspaces are equal:

`E(im beta2_a)=a²A·[Theta]=a²A·κ`.

The proof correctly stops at equality of subspaces. It neither sets `c=1` nor computes its sign, nor identifies the scalar `κ_conn` with the cohomology class `κ`. No normalized equality with a separately normalized κ-multiplication map follows from invariant-line dimension alone, and none is claimed.

The conclusions are limited to the classified even completion and fourth-lift changes, with the source data, canonical first lift, marking, normalized charts, and harmonic convention fixed. They do not evaluate `beta4`, prove a nonzero pairing with its normal term, eliminate the transition class, or supply a new exceptional-fiber or rank theorem.

## Verification scope

All checks were structural: universal trace-free rank-two identities, filtration and equation-line bookkeeping, exact sequences, the pinned coherence identities, and functorial Čech boundaries. No actual values, points, source derivatives, selected matrices, source evaluations, scans, or large computations were used.
