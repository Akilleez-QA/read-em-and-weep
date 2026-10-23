# Compatibility restrictions and torsion elimination

**Craig Ward · 23 October 2026 · Structural update through PR946**

The necessary relation remains **four pairs across three stable labels**, distributed **2 + 1 + 1**. The new results narrow compatibility inside those cases and settle the opposite-pencil torsion question. They do not remove another catalogue pair, identify an actual source realization, or complete the original proof repair.

## Source126 has no compatible semisimple separation

[PR944](https://github.com/Akilleez-QA/read-em-and-weep/blob/84d7c9b3ee57c0a12c9e99816ec690cd8ea7ffbc/research/hm/source126-invariant-compatibility/PROOF.md) assumes an actual source126 occurrence with its fixed negative-pencil algebra and lets Q be the canonical invariant positive quadratic product. Its compatible subalgebra has the form

    D_Q = C·1 ⊕ J_Q,    J_Q ⊂ J,    J_Q² = 0,
    dim J_Q ∈ {0,1,2}.

The proof reconstructs the endpoint characters of every constant vertex in all three residual templates. Every idempotent, including arbitrary radical shears, is conjugate inside the negative-pencil algebra to a vertex-subset projector. A compatible such projector would split the invariant product into two blocks whose constituentwise image bounds have dimension at most 23 or 30, whereas the imported actual image has dimension 33. Thus only the idempotents zero and one remain.

Polynomial functional calculus then forces every compatible element to have scalar diagonal part. This proves the displayed local commutative algebra shape without assuming that the radical of a subalgebra automatically equals its intersection with the ambient radical. **The square-zero part need not vanish.** The package records 173 supporting checks, including all fourteen nontrivial vertex subsets and controls preventing an unjustified scalar conclusion.

## Generation removes the Type III zero-source direction

[PR946](https://github.com/Akilleez-QA/read-em-and-weep/blob/893e14c2aee0391cdc881679c5015a8aac48ac24/research/hm/source126-nilpotent-generation/PROOF.md) adds the actual subspace identity

    N4 = im Q + im q_minus.

It comes from source-independent degree-zero generation and equality of the actual positive aggregate image with im Q. It is not a direct-sum claim or an identification of the multiplication maps themselves.

For a negative-pencil endomorphism e whose first endpoint e2 is zero, commutation gives e4(im q_minus)=0. Consequently

    im(e4 Q) = im e4.

If e is Q-compatible, this forces e4=0. Equivariant Serre duality and the constant normal form make the fourth endpoint faithful on the source126 radical. Together with the scalar part, this proves that restriction D_Q → End_G(N2) is injective.

In Type III, J has two one-dimensional arrow spaces J_X and J_Y. A nonzero X-arrow has zero first endpoint but a nonzero P-to-P fourth-endpoint channel. The image identity therefore proves

    im(j_X,4 Q) = P,       rank(j_X,4 Q) = 4.

No nonzero pure X-arrow is compatible. Hence **dim J_Q ≤ 1 in Type III**, whereas Types I and II retain the bound two. If a nonzero compatible line exists, it is a graph C(y+t x) over J_Y; neither existence nor the scalar t is determined. The same identity for the X-vertex projector proves that the X-target projection of Q is onto V+P, of dimension seven. These ranks are deduced structurally, not obtained by evaluating an actual matrix.

The 1,326 supporting checks include 1,008 parity regressions and a synthetic control showing that the actual image-generation premise cannot be dropped. Multiplicity-free kernel and cokernel actions alone do not eliminate a square-zero radical: its induced actions can both vanish. The proof does not claim scalarity or exclude either source126 pair.

## The actual opposite-pencil torsion is zero

[PR945](https://github.com/Akilleez-QA/read-em-and-weep/blob/089003175d9e31a7cf6288ab7a9e3ac4d66a3e63/research/hm/exceptional-adjoint-exhaustion/PROOF.md) resolves the torsion alternatives left by PR936. For every negative hyperplane H_t, including all twelve exceptional doubled-plane determinants, it proves

    H0(H_t, B(3)) = Sym² H0(H_t, F_HM(2)),
    dimension three, with all sections inversion-even.

The exceptional argument does not extrapolate from generic fibers. A general section has zero curve consisting of a conic disjoint from a Ferrand double conic. Invariant supports exclude line-supported alternatives, while reduced reducible conics are retained. The five-dimensional even cubic space and uniqueness of the containing cubic prevent the Ferrand linear coefficient from aligning with the simple determinant plane. Ordinary-ideal-square restrictions and two controlled divisions then show that the only sextic in the square of the curve ideal is the square of its determinant cubic.

Only after this independent exhaustion does the exact base-change sequence give zero Tor1 at every parameter. Thus the actual rank-five degree-26 opposite-pencil cokernel C is locally free. In particular:

- The reduced **26-to-31** pencil has zero fiber kernel everywhere.
- The distinct vertex-restricted **40-to-43** pencil has a two-dimensional fiber kernel everywhere, exactly the vertex-vanishing products of the two primary sections.
- The vertex-ideal higher-direct-image extension also has locally free middle term. Its splitting is not established.

These two pencil kernels must not be conflated. The nonzero torsion patterns studied conditionally in PR936 and PR938 are excluded for this actual C under the pinned hypotheses. Their conditional calculations are not retroactively invalidated.

## Verification scope and current boundary

The source126 results are written proofs with pinned source interfaces, supporting reproducible checks and independent mathematical reviews. The complete PR945 proof and its five source interfaces were read in the supporting review, with byte counts and SHA256/Git-blob hashes matched. The official [Bănică–Manolache 1983 scan](https://www.imar.ro/~increst/1983/19_1983.pdf) was retrieved and relevant classification, Ferrand and tripling pages inspected; the new parity and ordinary-square argument was checked directly. This is not a rederivation of every imported HM theorem or formal proof-assistant verification.

No actual HM coefficient, selected point, parameter, matrix or instance rank was evaluated. No additional source-dual pair or stable label is removed. The unchanged exact accounting remains [PR942's four-pair certificate](https://github.com/Akilleez-QA/read-em-and-weep/blob/3cd8a620e7268cf86fb8cc019d35f04d3cb6b448/research/proof-repair-campaign/four-pair-composition/README.md).

The splitting type of the now torsion-free bundle C, the possible compatible mixed radical line, the remaining mixed multiplication constraints, actual source compatibility, physical construction and higher lifting/algebraicity remain open. The [four-pair progress figure](figures/current-four-pair-frontier.svg) and the historical six- and 146-pair checkpoints remain unchanged.
