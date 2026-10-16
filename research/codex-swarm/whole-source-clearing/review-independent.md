# CLR-R2 final independent review — 2026-10-16

**Disposition: ACCEPT the actual finite whole-F polynomial identity and its
217/210 coordinate-degree bound, conditional on the authenticated contraction
identities. HOLD physical homogeneous-source/geometric admission and arithmetic
execution.** No producer defect requiring a fix was found. This supersedes the
pending disposition in `review-staging.md`; that historical file is unchanged.

Read README, PROOF, clearing.py, the complete parsed source-integration artifact,
producer-ready, staging notes and both test modules. Subsequently read
`review-degree.md`; its independent conclusion agrees with the argument below.
No wait, physical-source evaluation, physical polynomial multiplication,
differentiation, expansion, rank search, detector scan or GitHub mutation was
performed. Only `test_independent.py` and this report were written.

All five producer SHA256 values match `producer-ready.json`:

| File | SHA256 |
|---|---|
| README.md | `89877380e925c6166f7805ddcb4cbc165e6938c09f46783920c6793c5823f0eb` |
| PROOF.md | `3ea2b68a04168f76ba217b2b43470c41657124b550111c72a3eb10b60dd89361` |
| clearing.py | `2cc26945328dba5069d0b79888416b4d9d48b4031336fe266b2ffc103db3abef` |
| source-integration.json | `a7070e531edd2d034c7ddac8899cf4fcc7e880d4bb3adf5d0d37c8abb7b86a4c` |
| test_clearing.py | `ca54ca6cb20a1b9e87df9e33bc8d8af2cc3111a850b1db82ac1b4ad92dcd001e` |

Independent tests authenticate six exact source digests, including the order
note, at `10810ee877fdaf291399198ad60d7dd0c316a42d`. Expectations reuse the
staging source notes; the combined-pole code pin is additionally checked.
The generated artifact equals `build(REPO)` structurally in full. This is
metadata/circuit regeneration, with no physical coefficient execution.

The actual transition theorem is explicit. With E_b=I_b P_b=
1-gamma H0_b-H1_b delta and the pinned contractions, P_a E_b I_c=P_a I_c.
Consequently K_ab=(P_a I_b)^t satisfies K_bc K_ab=K_ac and
K_ab inverse=K_ba. For g_ab=D_b K_ab D_a inverse, differentiation gives

    partial_i g_ab = D_b T_ab,i D_a inverse,
    T_ab,i = partial_i K_ab + Q_b,i K_ab - K_ab Q_a,i.

Here Q_v,i=m_v,i*(x_i²+1)/(2*x_i*(x_i²-1))*sigma, sigma=diag(1,-1).
The ordered trace cancels intermediate D factors and the outer conjugation.
The pinned mu factor 1/2 and scalar correction 1/2 give exactly

    F12 = (15/4) q_01,0 q_12,1
          - (1/4) tr[K20 (T12,0 T01,1 - T12,1 T01,0)],
    q_ab,i = (m_b,i-m_a,i)/x_i.

Both endpoint Q terms are necessary. q belongs only in the gerbe. The receipt
binding is authenticated; the physical contraction checker was not rerun.
Source-first evaluation followed by signed extension is the defined cochain.
An artificial counterexample confirms that raw nonlinear recomputation after
permuting the source triple gives a different result. Sorting and inserted
source calls remain schema instructions rather than executable coefficient
circuits; no cross-order equivalence follows.

Literal primary denominators are -H; auxiliary denominators are -v1*a,
a=v1*v3*v4. Thus H² clears each primitive with multiplier -H or -v3*v4,
respectively, without borrowing another occurrence's factor. All 360 primitive
entries were checked as exponent/shape metadata, including their weighted
numerator inequalities. K20, T12 and T01 contribute H ledgers (2,0,2),
(0,3,3), (3,3,0), totaling (5,6,5). Each pair derivative occurs once;
owned ell powers are at most one. Binary-mask q rewriting is exact for all
four mask cases. C=H^14*ell0*ell1 therefore clears the entire sum. The DAG
constructs P_finite=N_F*H0^9*H1^8*H2^9, including the legal-factor lifts,
with all denominator occurrences retained separately.

I independently challenged the degree proof before reading the native degree
review. In one coordinate over the other coordinates' rational field, actual
H degrees are 4/5/3 for carrier0/primary1..4/auxiliary5; assigned degrees are
5/5/4. Primitive weight excesses are 1/0/2. Transposition gives K_rs weight
r-s. Closed trace weights telescope, giving excess 2n0+4n5. Clearing loses
14(n0+n5), and every mask-zero ell=1 loses another degree against its assigned
degree. The pair-target gap is therefore at most

    1 - 12n0 - 10n5 - z_i.

Only n0=n5=z_i=0 remains: all three carriers1..4 and masks_i=1. Then all
endpoint Q_i equal rf_i*sigma and

    T_rs = partial_i K_rs - 2(r-s)*rf_i*K_rs,
    2rf_i = 1/x_i + 2/[x_i*(x_i²-1)].

For ANY rational f with degree<=w=r-s, write f=x^w*u with u regular at
infinity. Then partial f-w*f/x=x^w*partial u has degree<=w-2;
the rf remainder has degree<=w-3. This includes w=0 and -1 and zero leading
coefficients. Each ordered trace word gains the extra degree separately;
no cancellation between words is assumed. The relevant gerbe factor vanishes.
This proves the critical bound. Off-pair differentiation preserves the chosen
coordinate bound. Polynomiality already proved, these rational degree bounds
give polynomial bounds217/210 and the stated multihomogenization candidate.

Both seeds retain four E34 branches: coordinates [2,3,3,2], two shared edges
per seed, four combined edges total. Full artifact equality preserves selector
and weight bindings. Independent controls check tail-owner edges, tracefree
wrappers, separate output C/Z owners, tag-matched inclusive inserted domains,
and the complete numerator

    C_a*C_b*Z*B + Z*sum_u(Qhat_u*P_uab)
                  - C_a*Z*sum_uv(Qhat_u*Qhat_v*P_uvb).

B retains its complete R(Kcov Pi+A h S Pi)F meaning and support[-1668,5248].
The extra C_a in prism2 is present. The single quotient-rule derivative acts
after this combination; Delta retains each labelled positive factor once.
These are correct conditional recipe bindings, not instantiated B coefficients.

Tests: independent normal **11/11**, optimized **11/11**; actual local full
suite normal **17/17**, optimized **17/17**. Every invocation used `timeout
60s` and `python -B`; none approached the cap. Commands use unittest discovery
in `research/codex-swarm/whole-source-clearing`, pattern `test_independent.py`
or `test_*.py`, with `-O` for optimized runs. Final full suites, after the
source-pin addition, completed in 0.359s/0.361s. Artificial exact first-jet
controls match the entire DAG to differentiated physical-frame toy matrices
and detect wrong Q normalization, either missing endpoint, reversed products,
and -1/2 instead of -1/4. Initial reviewer-test failures were an obsolete staged
field assertion and an incorrect four-owner assumption for seed30; both were
reviewer controls, corrected without changing producer files.

**Held gaps:** identifying this homogenization with the intended physical
homogeneous character/deck/infinity frame; executable complete B/partition and
inner quotient coefficient circuits, instantiated supports and source calls;
raw-v5/tracefree projection comparison and historical source-order transport;
full detector assembly and arithmetic/resource admission. Finite degree217
alone discharges none of these. All six producer admission/execution gates
remain false. The accepted finite theorem does not release geometric admission.
