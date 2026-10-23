# Independent review of the monad-torus negative-pencil bridge

Verdict: **PASS, conditional on the pinned actual-monad and cohomological-origin inputs.** No mathematical counterexample or blocking gap found. This is a structural argument about a specified monad family, not a computed commutant value or actual-source evaluation.

Reviewed file: `work/swarm/frontier-plan/COMMUTANT-GAUGE-BRIDGE.md`.

Reviewed SHA256: `3a13a8999b21c46e801383e56541112182a23e771d6204d496277048aa5dd0a4`.

The final clarity revision was read back: the theorem quantifies points of (C*)^3, equation (2) specifies theta:g*B_t -> B_t', and equation (3) writes Phi_j=H^1(theta_j) composed with pullback. This review is bound to those final bytes.

## Exact source inspection

Read the entire proposed proof and the following pinned texts, rather than PR summaries:

- PR643 at `356a3b8d2da36f5b3e2034cc5c6adf82757a33cc`, `research/hm/three-channel-monad-family/PROOF.md`.
- The actual cohomological Gauss gate at `063216038f3aefd65617651c2426721efafc7f9b`, `research/hm/order-four-quadratic-load/POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md`.
- The actual monad input at `8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4`, `research/hm/twist-one-structural-vanishing/PROOF.md`.
- The negative invariant scalar and determinant-valued b-square notes at `78053cfaec46a334c8714da084948356e467259e`, under `research/hm/order-four-quadratic-load/`.
- The producer's local copy of `ACTUAL-AMBIENT-ATIYAH-MULTIPLIER-IS-THE-MONAD-RATIO.md` at the PR758 pin, for its matching pullback and determinant conventions. Its deeper multiplier conclusions are not needed here.
- PR790's complete proof and section 6 were read in the preceding independent source2 gate review; only that actual-tensor identification is used in the proposed corollary.

The actual HM foundation and all upstream cohomology theorems were not independently re-proved. The proposed bridge does not purport to re-prove them either.

## Variance and the full-monad comparison

PR643 defines H as coordinate functions on P(H*). Its stated block weights are therefore pullback weights, with g*l=mu*l for every negative l. With lambda=1, the coordinate pullback takes (a,b,c) to (a,mu^2 b,mu c). The proposed s=a'/a and r=c'/(mu c), together with mu^2=(b'/a')/(b/a), then give exactly (a',b',c'). All quantities divided by are nonzero in the torus.

This transformation concerns the full self-dual monad. PR643 explicitly uses the inverse source gauge on the left and dual source gauge on the right. Its coordinate pullback preserves the determinant-valued exterior pairing. Thus there is an actual chain isomorphism after pullback, not just equality of left-arrow representation types. Taking middle cohomology gives an isomorphism u:g*F_t -> F_t'.

The induced map on trace-free endomorphisms is theta:g*B_t -> B_t', q -> u q u^(-1). Pullback commutes with End for locally free bundles, and conjugation preserves trace. No determinant trivialization is required and no extra Delta character twists End_0. This directly addresses the potential determinant-line error; the determinant factor is retained where the monad comparison needs it, then cancels under the End functor.

## Multiplication naturality and removal of the correct scalar

Using theta and the same compatible linear lift for every O(j), the precise map is Phi_j=H^1(theta tensored with the twist identification) composed with pullback. Pulling back the sheaf map that multiplies by l gives multiplication by g*l. Hence

    Phi_(j+1) m_l(t) = m_(g*l)(t') Phi_j
                       = mu m_l(t') Phi_j.

The direction and scalar in equation (5) are correct; replacing mu by its inverse without also reversing the pullback would be incorrect. The scalar is identical for both basis variables and for both arrows because g acts as one scalar on the entire negative two-space and the twist identifications are multiplicatively compatible.

For Psi_j=mu^(2-j)Phi_j,

    Psi_(j+1)m_l(t)
      =mu^(1-j)mu m_l(t')Phi_j
      =m_l(t')Psi_j.

This proves both same-l identities simultaneously, including the second arrow's exponent -2. No independent conjugacy for each arrow or unrecorded GL(W) relabeling is used.

## G, inversion, and twists

The block coordinate transformation centralizes G on H. The two source gauges are scalars on fixed irreducible G-summands. The natural cotangent/exterior and line-bundle pullbacks, the determinant-compatible chain isomorphism, and theta are consequently G-equivariant. They intertwine the specified central inversion in the actual monad conventions; a possible scalar change in a bundle isomorphism would disappear on End_0 in any event.

Thus the H^1 maps preserve the required inversion eigenspaces. A negative coordinate has odd inversion character, so the same multiplication-natural diagrams restrict to the actual even/odd/even spaces H^1(B(2))_+, H^1(B(3))_-, H^1(B(4))_+. Their dimensions and characters transfer from the actual member by these maps; no equal-dimension argument substitutes for a map comparison.

## Attempts to break the conclusion and retained limitations

1. **General variable changes:** if g acted nonscalarly on W, scalar rescaling by graded degree would not in general remove the variable relabeling. The proof uses only a scalar action on W, so this counterexample mechanism is excluded by its actual construction.
2. **Positive variables:** a positive v scales by lambda. The displayed rescaling would leave factor lambda/mu on its multiplication maps. Thus this does not establish a fixed full-Sym(H) module isomorphism. The text correctly restricts the claim to Sym(W) and disclaims preservation of fixed positive forms and higher-boundary normalizations.
3. **Independent cohomology identifications:** arbitrary unrelated identifications of the three representations do not imply a pencil isomorphism. Here all Phi_j arise from the same sheaf isomorphism and compatible twists, so that failure is avoided.
4. **Boundary triples:** a nonzero vector with one zero channel need not be a subbundle monad. The final theorem explicitly quantifies two points of (C*)^3, and Section 2 retains all nonzero channel factors. Thus it excludes this failure at the statement level.
5. **Coefficient-field descent:** a chosen square root mu need not lie in an arbitrary smaller field. The theorem is stated over C and claims no isomorphism over Q or over a separately fixed exact coefficient field. A future constructive certificate must record any needed field extension and all channel bases; this argument does not supply them.
6. **Full-bundle simplicity:** an isomorphism of truncated modules transports their complete endomorphism algebras but does not extend arbitrary truncated endomorphisms to the full module or bundle. The proposed result does not make that inference.

## Algebra action and actual-source scope

Simultaneous conjugation by the three Psi maps is an algebra isomorphism on all commuting triples, including singular ones. It is covariant; the opposite-algebra issue in the separate constant-inclusion reconstruction is not being reused here. Intertwining transports the actual algebra action, so radicals, all radical image sums and kernel intersections, idempotent image-pencil systems, and intrinsic subquotients constructed from these data are carried along legitimately.

The comparison with the unit-parameter member is confined to the same fixed irreducible-channel monad family. PR643 puts the actual normalized HM monad in that torus. This removes dependence of the negative-pencil isomorphism type on a nonzero channel ratio, but it does not authenticate a newly invented pencil with matching characters. Nor does it calculate the invariant. PR790's separate conditional bridge is still needed for a source2 comparison.

No actual coefficients, ranks, tensor entries, selected points, or source values were evaluated in this review. The structural result is suitable for a focused proof PR with its stated C-field and actual-input boundaries retained.
