# Independent RS01 full-source closure review

## Disposition

**Accept RS01's source identity, closedness, and full-sign obstruction-class identification for the specified fresh first lift, under its explicit imported geometric and PR87 first-order premises. No blocking mathematical defect found at PR88 commit `d18d9810f7333d9f94a895c4e26985520cc60057`.**

The identity has the **positive** boundary:

`Rsharp = tf(M_fresh) + delta(s_q k_p + s_p k_q)`.

The baseline must be the complete `globalCross` at `u_r^0=g k_r`, including all three negative gerbe terms. Both complementary Fk terms and both four-term E currents are necessary. This acceptance gives a closed source with the correct class, not a numerical obstruction, an outer regularity certificate, or permission to execute physical coefficients.

Review source: [RS01 proof at the reviewed immutable pin](https://github.com/Akilleez-QA/read-em-and-weep/blob/d18d9810f7333d9f94a895c4e26985520cc60057/research/codex-swarm/full-source-application/PROOF.md).

## What was independently checked

Read RS01's proof, formal identities, constructor, contract, tests, published review, and direct source manifest. Read the pinned ambient two-jet, closure/character, first-order source, direct scalar-free reduction, transition-only lift, canonical FD theorem, FD/P/Q definitions, SC compiler, and accepted SC review/fix scope. The published RS review was treated as a prior report, not as evidence that this review's controls passed.

All **20 direct immutable source records** match both their SHA-256 and Git blob hashes. All **7 producer files** match the producer-ready marker; the marker itself matches SHA-256 `883490825f5d1b1156ad865e9852ef64e314322418409c9de3b71041f07d3616`. The bytes were obtained through read-only GitHub access. Hashes authenticate the definitions examined; they do not establish the mathematical hypotheses.

Twelve new independent tests pass normally and under `-O`, **24 successful executions total**. These use small exact rational/free-word algebra, file hashes, static Python AST inspection, and existing JSON metadata. No actual HM polynomial operation, source evaluation, physical jet, matrix payload, coefficient extraction, residual evaluation, occupied-support computation, or physical fiber enumeration was performed. The compiler was not executed and its graph was not regenerated. No repository edit, commit, push, or external post was made.

## 1. The actual first-order premise is used at the right point

For `r=p=(0,1), q=(2,3)`, RS fixes

`s_r=T_N14,r F_r`, `k_r=-mu_r(g^-1,g)/2`, `u_r=g(s_r I+k_r)`.

The accepted PR87 FD theorem supplies `delta s_r=F_r` for this same freshly evaluated source and the carrier14/legal1 source domain. It retains `Hrho+R(Kcov Pi+A h S Pi)`, including both signed prism branches and both standard branches. It is not merely the generic homotopy identity: the admitted raw primitive proves that the pair-character harmonic remainder vanishes. Closure of an arbitrary pair-character F would not suffice, because that scalar H² has dimension one.

The separate rank-two identity is correct. With `P_d=A^-1 V_d A`, `Q_d=A^-1 B^-1(V_d B)A`, logarithmic differentiation gives

`k(g)=[g^-1 V_a g,g^-1 V_b g]/4`,

`delta k=-([Q_a,P_b]-[Q_b,P_a])/4=-C+tr(C)I/2`.

The last equality uses the two-by-two traceless identity `QP+PQ=tr(QP)I`, so determinant one and rank two are genuine hypotheses. Therefore `delta(s_r I+k_r)=b_r I-C_r`; this is the full order-one module equation, not a projected or trace-only version.

This review imports the actual classical contractions, determinant-one transition theorem, coherent physical/deck frames, and accepted PR87 FD/P/Q source/domain correspondence. It does not re-prove them from model coefficient arrays. RS01's additional closure argument is what upgrades those first-order premises to a statement about its specified second-order source. PR87 acceptance alone was not global second-order acceptance.

Sources: [FD at PR87, §§4–6](https://github.com/Akilleez-QA/read-em-and-weep/blob/e011d7c2e0b79f1b885e001c9b0e39b97618a424/research/codex-swarm/source-domain-application/PROOF.md), [first-order source, §§3–4](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/first-order-source.md).

## 2. Ambient closure is proved before taking the character component

The declared ambient jet is specified concretely: commuting invariant derivations, `mu1=pi/2`, `mu2=pi*pi/8`, `Fij=1+h²Tij`, and `Aijk=1+h bijk+h² bijk²/2`. Associativity follows from the exponential construction for commuting derivations, with matrix products kept in their written order. No commutation of matrix coefficients is needed.

The AW signs are correct. For one pair,

`delta[(a_p cup q_q)V_q+(q_p cup a_q)V_p]`

`=((delta a_p) cup q_q)V_q-(q_p cup delta a_q)V_p={b,-}/lambda`.

Here `Vq=delta a`; the negative sign on `delta(q cup a)` is essential. Consequently `Ad_star(A)=1+h²{b,-}`, which gives the first descent identity. The second follows from the additive cocycle identity for b: star corrections between two order-h factors begin at h³, and the nontrivial action of F on h b also begins at h³. Thus both ambient coherence identities hold to the declared order.

Independently expanding the exact module-defect combination gives

`A Eikl + X Eijk - C Eijl - Fij(Ejkl) Z`

`=(AV-XA)W+(CD-AB)H`.

The two ambient coherence identities kill separate free-word remainders. Dropping either relation or reversing any one of the four defect signs leaves a nonzero formal remainder. Associativity is therefore being used with the correct noncommutative order.

Because defects of orders zero and one vanish, the h² coefficient is exactly

`Rikl+gkl Rijk-Rijl-Rjkl gij=0`.

For `Mijk=gik^-1 Rijk`, direct multiplication gives

`gil(delta M)ijkl=Rjkl gij-Rikl+Rijl-gkl Rijk`,

the negative of that identity. Right normalization does not give the same formal expression. A separate control with a nonzero order-one defect retains an extra `a1 E1` term, confirming that lower-defect vanishing cannot be skipped.

The terms `Tij(gjk)gij` and `-mu1(bijk,gik)` remain in this full ambient argument. They may be removed only when subsequently selecting the full-sign component, not from the original closure equation.

Sources: [RS01 §§1–2](https://github.com/Akilleez-QA/read-em-and-weep/blob/d18d9810f7333d9f94a895c4e26985520cc60057/research/codex-swarm/full-source-application/PROOF.md#1-the-actual-ambient-two-jet-and-both-coherence-identities), [pinned ambient second jet](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/ambient-second-jet.md).

## 3. The surviving source is seven kinetic plus three gerbe terms

Under the imported coherent deck linearization, the two actual first lifts have pair characters, including the fresh scalar solutions because the fixed cover maps and partitions are deck invariant. This is a statement in transported physical End frames. It does not require arbitrary unnormalized transition entries to be invariant.

T has trivial character. The same-pair pieces of `mu1(b,g)` also have trivial character; its cross-pair pieces vanish because b_p and b_q depend on disjoint coordinate sets. Character projection commutes with delta. The surviving full-sign source is therefore the stated seven kinetic terms plus

`-b_p u_q,ik-b_q u_p,ik-b_p b_q G`.

An independent enumeration of the two disjoint orders in the formal Moyal square gives coefficients `(+1,-1,-1,+1)/4`, not `/8`, with the left matrix derivative multiplied by the right matrix derivative. The mixed term of `-b²G/2` is `-b_p b_q G`.

The dictionary `g_ab=D_b(P_a I_b)^t D_a^-1` matches the transpose of the pinned source's diagonal-frame formula. Actual moving-frame derivatives must precede deck stripping, and nonlinear row products must precede transpose. Nothing here licenses freezing frame jets or assigning the completed scalar's tau^-4 conversion to every physical matrix entry.

Sources: [RS01 §3](https://github.com/Akilleez-QA/read-em-and-weep/blob/d18d9810f7333d9f94a895c4e26985520cc60057/research/codex-swarm/full-source-application/PROOF.md#3-why-its-full-sign-component-is-the-actual-seven-plus-three-source), [source function excerpts](https://github.com/Akilleez-QA/read-em-and-weep/blob/10810ee877fdaf291399198ad60d7dd0c316a42d/research/hm/null-operator-compiler/hm-pinned-source-formulas.js), [closure and characters §2](https://github.com/Akilleez-QA/read-em-and-weep/blob/08b73637d4136f91606aad332c46cafd064417f8/research/hm/current-scalar-residual-attribution/closure-and-characters.md#2-why-the-mixed-formula-is-exactly-the-full-sign-component).

## 4. The five-term reduction and boundary sign are exact

Set `kbar=A^-1 k_p,jk A`. Using `C_p^0=-kbar+k_p,ik-k_p,ij`, the scalar-linear terms involving s_q satisfy

`s_q,jk k_p,ij+s_q,ij kbar+(s_q,jk+s_q,ij)C_p^0`

`=-delta(s_q k_p)+(delta s_q)k_p,ik`.

Exchanging the two pairs gives the other Fk contribution. This derivation produces the minus boundary in `tf M-tf M0`, hence the **plus boundary** in `Rsharp-tf M`. The independent free-word control rejects the reversed boundary sign.

The two product rules in `G^-1[mu_p(B t_jk,A)+mu_p(B,A t_ij)]` give

`(t_jk+t_ij)C_p + 1/2[(Va t_jk)Lb-(Vb t_jk)La+(Vb t_ij)Ua-(Va t_ij)Ub]`,

with `L=A^-1 V(A)` and `U=A^-1 B^-1 V(B)A`. All four current terms, both endpoints, and the order inside U check independently. Each individual sign mutation and omission of the second endpoint fails the formal identity. Determinant one makes L and U traceless, so these are exactly the trace-free derivative terms.

The quadratic scalar terms and scalar gerbe corrections are central; they are not asserted zero. An independent abstract calculation of their difference gives

`-delta(s_p s_q)+(b_p b_q-c_p c_q)`,

which is generally nonzero. This verifies the distinction between trace-free elimination and pointwise equality of full matrix residuals.

Because M0 already includes `-b_p k_q,ik-b_q k_p,ik-b_p b_q I`, the corrections are `+F_q k_p,ik+F_p k_q,ik`. Using an uncorrected kinetic baseline with those same corrections would be wrong. The actual SC source uses the full gerbe baseline.

Source: [RS01 §4](https://github.com/Akilleez-QA/read-em-and-weep/blob/d18d9810f7333d9f94a895c4e26985520cc60057/research/codex-swarm/full-source-application/PROOF.md#4-trace-free-scalar-elimination-and-the-explicit-positive-boundary), [direct scalar-free reduction §§2–4](https://github.com/Akilleez-QA/read-em-and-weep/blob/10810ee877fdaf291399198ad60d7dd0c316a42d/research/hm/null-proof-foundations/direct-scalar-free-pairing-reduction.md).

## 5. Closure and class identification are distinct valid steps

Trace projection commutes with row-End delta, so the established ambient closure yields `delta tf(M)=0`. Adding `delta W` preserves closedness. This proves `delta Rsharp=0` for the whole sum. It does not prove that M0, either Fk term, or either E term is separately closed.

Class identification additionally needs the scalar cohomology argument. Characteristic zero gives the equivariant splitting `End E=O I direct-sum End0 E`; the central part of the already closed full-sign M is therefore closed. For the specified double-cover deck action, its scalar eigensheaf is `O(-2,-2,-2,-2)` on `(P1)^4`. Each factor has cohomology only in degree one, so the tensor has scalar cohomology only in degree four. In particular its H² is zero. The central part is thus exact in sheaf cohomology, and `Rsharp` has the same full-sign H² class as the chosen actual residual.

This does not supply a central primitive in a particular finite cutoff or with the outer5251 pole ledger. It also does not require a historical-order gauge comparison: the residual M is defined directly for the fresh lift. No Ext¹ rank table or global second-order vanishing assertion is needed for this argument.

Source: [RS01 §5](https://github.com/Akilleez-QA/read-em-and-weep/blob/d18d9810f7333d9f94a895c4e26985520cc60057/research/codex-swarm/full-source-application/PROOF.md#5-class-identification-without-evaluating-a-central-homotopy).

## 6. Binding and verification limits

The constructor signature accepts only `repo`; it does not expose a replacement source/ambient/closure callback. It authenticates pinned definitions and invokes the canonical FD application for both pairs. The source triple is strictly increasing in full common-source order, has one seed, and retains three separate occurrence identities. Repeated physical `(carrier,mask)` labels across different common tags are not incorrectly declared repetitions of the general lifted cochain.

All twenty existing source records are precisely the increasing triples of six universal slots. The checked metadata retains all five roots, seven kinetic terms, three negative gerbe terms, the left inverse on the outer edge, differentiated distinct-axis physical-jet descriptors, and all inner-solver branches. The first record uses slots `[0,1,2]`, matching the constructor's supplied-owner binding. No source graph was rebuilt or physical leaf lowered.

`compiler_source_contract` is a structural check, not a universal semantic validator of arbitrary forged JSON. The immutable graph authentication, inspected compiler formulas, and explicit source theorem provide its actual scope. The normal Python import/runtime environment is trusted; this review is not a sandbox-security review against hostile module replacement or mutation of private object state.

Public physical methods statically refuse unconditionally. This review did **not** replay the end-to-end constructor against a full Git checkout, execute the existing producer/in-repository independent suites, or re-audit the complete transitive P/Q implementation. It independently authenticated all direct RS pins, reviewed those bindings, and performed the focused tests listed here. The published 18-tests-per-mode report is not counted as this review's execution evidence.

Sources: [r_binding.py](https://github.com/Akilleez-QA/read-em-and-weep/blob/d18d9810f7333d9f94a895c4e26985520cc60057/research/codex-swarm/full-source-application/r_binding.py), [SC compiler source](https://github.com/Akilleez-QA/read-em-and-weep/blob/e011d7c2e0b79f1b885e001c9b0e39b97618a424/research/codex-swarm/scalar-compiler/compiler.py).

## Scope not discharged by RS01 itself

The following require their own scoped acceptance and cannot be inferred from this RS01 review. A separate acceptance of those packages is compatible with this report:

1. Inclusion and domain compatibility of the complete fresh source through the original physical J0–J3 resolution, with all frame/deck conversions and restrictions.
2. Complete outer54/legal29/target-unit5251 standard/prism/restriction regularity, including complementary derivatives of partitions and frames, faces, retained prefix ownership, and every selector row.
3. Actual complete owned fibers, physical coefficient/weighted-sum realization, and an aggregate execution/resource schedule.
4. Authenticated detector values and the global obstruction decision.

Historical nonlinear source/order equality remains unproved and is unnecessary for this particular fresh-source theorem. There is no physical arithmetic admission and no vanishing/nonvanishing verdict.

## Public replay without the review snapshot

Only this report and `test_rs01_closure.py` are needed for replay. The test defaults to read-only `git show` from immutable repository objects; no unpublished `sources` directory is required. Run from any directory, pointing to a checkout of `Akilleez-QA/read-em-and-weep`:

`python -B test_rs01_closure.py --repo /path/to/read-em-and-weep`

`python -BO test_rs01_closure.py --repo /path/to/read-em-and-weep`

When the script is inside that repository, `--repo` may be omitted. The checkout may be on any branch; all source reads use immutable commits. Its Git object store must contain these four commits:

- `d18d9810f7333d9f94a895c4e26985520cc60057` (reviewed PR88)
- `e011d7c2e0b79f1b885e001c9b0e39b97618a424` (PR87)
- `08b73637d4136f91606aad332c46cafd064417f8`
- `10810ee877fdaf291399198ad60d7dd0c316a42d`

The test retrieves the authenticated RS01 manifest from PR88 and follows its exact commit/path records. It does not fetch missing history, change branches, compile a graph, or instantiate physical source methods. The only executed producer module is the hash-checked, small `formal_identities.py` free-word module; other producer files are read as bytes, JSON, or Python AST.

The accompanying normal and optimized logs record 12 passing tests each against the byte-authenticated snapshot retrieved through GitHub. Exact commands used for these logs were `python -B test_rs01_closure.py --snapshot sources` and `python -BO test_rs01_closure.py --snapshot sources`. The Git transport was added for public reproducibility; a complete Git checkout was not available here, so these logs do not claim that transport was exercised. Both modes feed the same tests and authenticate the same immutable input bytes. This remains distinct from end-to-end constructor or physical execution.

Recommended publication evidence beside the two required files: `tests-normal.log`, `tests-optimized.log`, `review-receipt.json`, and `SHA256SUMS`. The optional snapshot and its separate checksum manifest need not be published.
