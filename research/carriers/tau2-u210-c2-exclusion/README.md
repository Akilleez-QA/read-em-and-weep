# Conditional τ=2, U210, c=2 exclusion

The [proof](conditional-exclusion.md) gives a uniform exclusion for the normalized U=O(2)⊕O(1)⊕O, c=2 block **assuming h_Z|Δ=0 and H_Y|Δ a unit**, the full-Artin exceptional gate, and the corrected central criterion. This package does not prove a necessary-direction theorem or an unconditional U210,c2 exclusion.

## Mathematical dependency

The central presentation, half correction, and full-Artin rank input are [PR #54](https://github.com/Akilleez-QA/read-em-and-weep/pull/54), pinned to [220853ab400944402396e210e7475a73901621e1](https://github.com/Akilleez-QA/read-em-and-weep/blob/220853ab400944402396e210e7475a73901621e1/research/carriers/tau2-central-artin-gates/central-artin-gates.md). The proof states every additional hypothesis explicitly. This standalone checker imports no code or data from that PR.

## Reproduction

Tested with Python 3.12.14 and SymPy 1.14.0. From this directory:

```sh
python -m pip install -r requirements.txt
python audit_tau_two_u210_c2_exclusion.py > reproduced-output.txt
diff -u audit-tau-two-u210-c2-output.txt reproduced-output.txt
```

The checker regenerates `audit-tau-two-u210-c2-exact-data.json` deterministically. It verifies symbolic identities and universal block factorization, followed by reduced-pair/double-point stress tests. A failed check raises an exception and exits nonzero; checks remain active under Python optimization. The recorded output is a local exact computation, not an automated CI result or a formal proof of the geometric hypotheses.

The decisive result is det(Y)=−8 det(M) Res(a,H_Y)/a₂⁷. Its nonvanishing forces g₁=b=λ=0; the full-Artin square gate then forces κ=0 and the exceptional D-row loses rank.

## Boundaries

No full U210 or τ=2 classification, construction, stability, moduli, or mixed-Atiyah conclusion is asserted. The other c values, U111 cases, and directions outside the stated hypotheses remain untouched. Related work: [issue #52](https://github.com/Akilleez-QA/read-em-and-weep/issues/52).
