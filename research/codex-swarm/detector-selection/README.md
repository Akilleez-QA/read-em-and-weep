# Explicit 32 weighted scalar-output tests

This package selects the previously missing ten and two individual output labels using only small constant matrices on P4. It computes **no physical source coefficients and no obstruction value**.

The bounded producer succeeded: 9,464 sparse finite-field coefficient updates, 0.094259 seconds wall time, and 73,678,848 bytes peak **sampled aggregate process-group RSS**. See `run-receipt.json`. Sampling every 0.02 seconds is a watchdog, not a kernel-enforced memory ceiling; it cannot rule out a transient peak between samples. The node heap is separately capped at 64 MiB. No larger computation or physical arithmetic is authorized by this receipt.

## Labels

Use the scalar maps

`L_(i,b)(X) = X13[i,b] - sum_(a,k) gamma[i,a,k] X02[a,5b+k]`.

The invariant polynomial is `Q = X1 X2 Y3 Y4 + Y1 Y2 X3 X4`. On the chart `Y_i=1`, `Q=x1*x2+x3*x4`, and `v_k` denotes the homogeneous P4 coordinate (the elementary symmetric polynomial on that chart, including `v_0=1`). Every output label `(L,f)` means the Serre Laurent pairing

`[x1^-1 x2^-1 x3^-1 x4^-1] f * L(regular transported cochain)`.

It is not a point evaluation or a single Laurent position, and no value is supplied here. Homogeneously `v_k=sum_(|I|=k) product_(i in I) X_i product_(j not in I) Y_j`: there are no binomial denominators or alternating coefficient signs. For `f=sum_m f_m x^m`, the requested value is `sum_m f_m c[k(m)]`, where `k(m)=sum_(nu=1)^4 (2-m_nu)*3^(4-nu)`. Each exponent in these polynomials is at most two. The original-frame transport includes division by the deck product and the internal-degree-minus-two factor `tau^-4`.

Twenty labels are `(L_(i,b), Q^2)` for

`I20 = {(i,0): 5<=i<=10} union {(i,1): 0<=i<=14, i!=5}`.

The additional ten labels are:

| Map | Test polynomial |
|---|---|
| L_(5,0) | v_0 Q |
| L_(5,0) | v_1 Q |
| L_(5,0) | v_4 Q |
| L_(6,0) | v_0 Q |
| L_(6,0) | v_1 Q |
| L_(6,0) | v_2 Q |
| L_(7,0) | v_1 Q |
| L_(7,0) | v_2 Q |
| L_(8,0) | v_3 Q |
| L_(9,0) | v_4 Q |

The final two labels are `(L_(5,0), v_0^2)` and `(L_(5,0), v_1 v_4)`.

The original scalar maps satisfy `L=-L_(10,0)` and `L_minus=-L_(10,1)`. The signs in the displayed definition, not an inferred old-map name, define this package's labels.

## Reproduction and evidence

From the repository root:

```sh
python -B research/codex-swarm/detector-selection/run_bounded.py
```

This overwrites `selection.json` and `run-receipt.json`; it never runs the full finite oracle or any physical source evaluator. The outer supervisor stops on a 59-second wall deadline, sampled aggregate RSS above 512 MiB, or output above 2,000,000 bytes. The producer separately stops above 20 million coefficient updates. Successful reproduction is not an allocation of the held physical arithmetic budget.

`extract_constants.js` authenticates the source Git blob and evaluates only the constant/basis/matrix-constructor prefix before `function rankExact(input,ncols){`. The source's rank functions, zigzag, driver and full harmonic oracle are excluded. The saved rational-rank receipt is separately blob authenticated.

`select_detectors.py` checks twenty scalar-dual cycles over the integers, all boundary compositions, and all 100/300 multiplication candidates over the integers. Sparse elimination modulo 101 then gives boundary ranks 240/848 and selected augmented ranks 250/850. `selection.json` retains the actual labels, complete deterministic pivot logs, matrix digests, order policy, and independent rational boundary-upper-rank premise. The modular ranks alone are not being treated as rational upper bounds; see `proof.md`. The independent `review_selection.py` additionally reconstructs arrows and tuple bases without importing the producer, proves rational boundary ranks 240/848 by integer unit-pivot elimination with zero residual, proves outgoing ranks 150/350, and checks augmented modular ranks using a different pivot order. Its receipt and negative controls specify the exact review scope.

The certificate's SHA-256 is `54603e2e3634d73da740837081297800f3b2b3bb219aeccd22141ac27e58368d`. Its status is `selected_output_labels_only`; it explicitly reports physical evaluation false and the obstruction undecided. Independent review files in this directory describe which additional replays or tests actually ran.

## Explicit weighted coefficient requests

`weighted_requests.py` translates the selected labels into `weighted-requests.json`: 32 explicit linear combinations of the 81 harmonic Laurent coordinates, with exact integer polynomial weights, original-frame requirements, and unresolved source gates. It pins the selection digest and preserves `e=-m-1` and the base-three indexing convention. It does not read or supply any scalar coefficient values.

```sh
python -B research/codex-swarm/detector-selection/weighted_requests.py > research/codex-swarm/detector-selection/weighted-requests.json
python -B research/codex-swarm/detector-selection/check_weighted_requests.py
```

The checker verifies dual-index and direct polynomial controls, changed-input rejection, saved-request equality, and that every physical source/execution gate remains closed. This request translation is separate from the constant-matrix independence certificate.

## Remaining source bridge

Completeness is conditional on the inherited rational P4/Serre identifications and the actual full-sign class belonging to the D8-epsilon sector. To decide the obstruction, evaluate the complete corrected representative on these 32 labels using an authenticated regular comparison, including all frame, owner, gerbe-baseline and top-Cech homotopy terms. No such values are supplied here. The constant-row classification does not transfer the old scalar's special first-carrier merger, pole bounds, or low-cost numerator to the other maps. The old 78-summand compiler is not automatically a compiler for this family. The accepted 20-map-family theorem remains valid independently of this 32-weighted-output selection.
