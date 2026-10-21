# Proof repair: current progress and remaining obstruction

**Craig Ward** · Working paper v0.3 · 21 October 2026  
Adjoint theorem cutoff: 22:57 UTC. V51 comparison: PR634.

## The problem

This repository develops a proof-repair program in the Horrocks-Mumford setting. The immediate problem is to determine the sections of the trace-free adjoint bundle B = End₀(F), restricted to a general smooth inversion-even quadric Q. The broader source-recovery, lifting, and Weil-class algebraicity objectives remain open. Narrowing the possible maps and eliminating incorrect routes is part of the mathematical result, not a substitute for a completed proof.

## Main result so far

For general smooth Q in the specified family,

    h⁰(B_Q(4))₋ = 0,
    h⁰(B_Q(4))₊ ∈ {4, 5},
    h⁰(B_Q(4)) ∈ {4, 5}.

The subscripts are the physical inversion eigenspaces. “General” means a nonempty Zariski-open set, not every quadric or special fiber. The current proof does **not** decide between four and five. [Integrated theorem][G].

## Why the search space is smaller

1. **Odd sector closed.** The last special D5 octic nonextension excludes the remaining residual rank-two branch. The actual six-to-ten smoothing map is injective, giving generic odd vanishing. [Proof][O].
2. **Positive cone rank fixed.** At the invariant rank-three cone q₀, the actual positive map has source dimension 41, target dimension 37, rank 33, kernel A ⊕ D5 of dimension eight, and cokernel P4 of dimension four. [Proof][R].
3. **The first-order route is excluded.** The cyclic Rao identity aξ = q₀ζₐ makes the entire first Bockstein zero. The former scalar γ is zero, not unknown; nonzero individual linear legs do not imply a nonzero composite. [Proof][F].
4. **Second order advances three ranks, not four.** The square filtration kills D5. The remaining A-to-P4 quadratic family has a nonzero actual scalar by Atiyah differentiation of the nonsplit quintic extension, and its universal symbol has generic rank three. Hence generic positive rank is at least 36. [Filtration][S]; [actual nonvanishing][N]; [rank consequence][G].

## The remaining gate

After second order in a general negative direction, the surviving source is D5, of dimension five, and the remaining target is a line. A nonzero third or later Bockstein would give rank 37 and four sections. If the last target survives all higher obstructions along the pencil, the rank stays 36 and the section count stays five. No higher nonvanishing is claimed here. Closing this gate would still not automatically solve the original source or algebraicity problem.

## Read the working paper

- [Paper index and abstract](paper/README.md)
- [Current theorem and notation](paper/01-current-status.md)
- [Completed exclusions and superseded routes](paper/02-completed-exclusions.md)
- [Odd-sector proof](paper/03-odd-sector.md)
- [Positive-sector proof](paper/04-positive-sector.md)
- [Separate V51 deformation geometry](paper/05-v51-comparison.md)
- [Dependencies, reproducible checks, and change log](paper/06-dependencies-and-changelog.md)

The V51 comparison reports the separately attributed construction of 636/576-dimensional algebraic slices whose completions represent marked polarized/abstract Artin deformation classes. It is not an input proving the remaining adjoint obstruction, groupoid representability, or algebraicity of arbitrary formal arcs.

## Repository layout and provenance

- **This README** is the current progress paper; [paper/](paper/README.md) holds its focused sections.
- **[upstream/openai-math/](upstream/openai-math/README.md)** preserves the original OpenAI/math snapshot unchanged, including manuscripts, Lean sources, reasoning traces and licenses. See [archive provenance](upstream/README.md).
- **Research proofs and verifiers remain in their existing pull requests and immutable commits.** This reorganization does not merge or certify every research branch. [PR543](https://github.com/Akilleez-QA/read-em-and-weep/pull/543) contains the current adjoint proof chain; [PR1](https://github.com/Akilleez-QA/read-em-and-weep/pull/1) records mathematical coordination.

## Evidence and version policy

These are authored mathematical arguments with supplementary universal identity checks, not proof-assistant certificates. The references below pin immutable source versions because the research pull requests remain in development. No selected Horrocks-Mumford coefficient or actual matrix-rank experiment is used in the results summarized here. The paper is maintained in modular Markdown; a PDF is not part of this working edition.

## Pinned source references


[O]: https://github.com/Akilleez-QA/read-em-and-weep/blob/ec080c229105457eafcd2583c8a47b362627a62e/research/hm/order-four-quadratic-load/SPECIAL-D5-OCTIC-NONEXTENSION-EXCLUDES-A12.md
[R]: https://github.com/Akilleez-QA/read-em-and-weep/blob/eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c/research/hm/order-four-quadratic-load/POSITIVE-INVARIANT-VERTEX-RANK-33-PROVED.md
[F]: https://github.com/Akilleez-QA/read-em-and-weep/blob/846968261441fef2cad247d22b66d37aed3f0f8f/research/hm/order-four-quadratic-load/POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md
[S]: https://github.com/Akilleez-QA/read-em-and-weep/blob/04fb081d710f1d7e175f252601b96dddcd93106e/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md
[N]: https://github.com/Akilleez-QA/read-em-and-weep/blob/9f28cb10c38d7a0e29c1eb994594325fea7f22bf/research/hm/order-four-quadratic-load/ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md
[G]: https://github.com/Akilleez-QA/read-em-and-weep/blob/72aa6fb732a803eb9201f45f1f82e60f54d296b4/research/hm/order-four-quadratic-load/POSITIVE-GENERIC-FOUR-OR-FIVE-SECTIONS.md
