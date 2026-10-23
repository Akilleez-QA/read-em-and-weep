# Reproduction and boundary

Run python verify.py and python -O verify.py.

Only nine fixed abstract character values in Q(√5) are used. The verifier checks Sym²V=1+D, three tensor identities, the imported invariant image tensored by V, and its character difference from the actual middle. It constructs no actual map or selected instance. Input authentication uses the two exact UTF-8 files named in audit-inputs/manifest.json when present; without them only the fixed character arithmetic is checked.

The universal image-sum inequality and actual factorization are mathematical inputs from the proof, not facts certified by these arithmetic checks. The resulting lower bound53 refers to im(C_D) inside V*⊗N₄. It is not the image dimension of q_D inside N₄, not the rank of a selected non-invariant quadratic, and not a measured matrix rank.

The canonical invariant line and normalization ε(q₀)=1 make q_inv independent of rescaling. No actual positive coefficients are evaluated. The result applies globally to the actual HM cohomology module and does not assume c-d-f or another source classification.

Expected arithmetic: invariant curry character2+6A+5V+6P+8D (dimension99); middle1+4A+2V+3P+3D (dimension46); forced non-invariant curry character1+2A+3V+3P+5D (dimension53).
