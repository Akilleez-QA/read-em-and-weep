# τ=2 central gluing and full-Artin rank gates

A focused conditional result for the normalized block

- E = O(-5,1) ⊕ O(-3,1), T = O(-2,2) ⊕ O(-1,1)
- W = O(c,0) ⊕ O(-c,0), c ≥ 0, with its actual weighted transitions
- L = [[ell,h],[0,a]], with degrees (3,1), (1,1), (2,0)
- ell primitive, a nonzero, and ell,h independent on every reduced point of V(a)

Normalization is a hypothesis. The support of V(a) can be two reduced points or one double point.

## Result

[The proof](central-artin-gates.md) gives:

1. The full primary condition and the half-corrected central obstruction in H¹(N), together necessary and sufficient for central gluing and isotropy.
2. An exact presentation of N retaining h² and the full length-two base torsion.
3. The ordinary determinantal rank gate and an exact exceptional gate in the first-stage data.
4. The full-Artin consequence of the exceptional coprime-quadratic gate: the primary equation forces the support-line relation over the entire length-two divisor.

This does not classify splittings, exclude branches, solve the central equations, construct a globally surjective family, or establish stability or mixed-Atiyah vanishing. No bound on c is asserted. Weighted first-stage spaces are not replaced by W = O².

## Reproduce

From this directory, using Python 3.10 or later:

```sh
python -m pip install -r requirements.txt
python run_checks.py
```

The recorded run used Python 3.12 and SymPy 1.14.0. `verification.txt` contains the complete output of both standalone scripts. Each script builds its own symbolic data and imports no prior research code or saved tensor. The runner preserves assertion checks even if PYTHONOPTIMIZE is set. These are exact algebra/model checks accompanying the proof, not a machine formalization of the sheaf argument or an automated-CI claim.

Public context: [issue #52](https://github.com/Akilleez-QA/read-em-and-weep/issues/52). [PR #53](https://github.com/Akilleez-QA/read-em-and-weep/pull/53) treats a separate τ=1 result; it is unchanged and is not a dependency of these tests.
