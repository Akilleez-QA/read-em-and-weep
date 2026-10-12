# Twist −2 connecting map for the pinned four-term complex

The pinned complex on \(\mathbb{P}^4\), reconstructed from `research/hm/verify-hm-ext.js` (git blob `fa5231de92b61143e3406111d4af028284db6d55`), is

\[
C=\bigl[5\mathcal{O}(-1)\to 15\mathcal{O}\to 10\mathcal{O}(1)\to 2\mathcal{O}(2)\bigr],
\]

with \(C^u=\mathrm{ranks}[u]\,\mathcal{O}(u-1)\) and \(\mathrm{ranks}=[5,15,10,2]\). The differentials are the exterior-sign map, the paired contraction, and the paired evaluation from that source. Their consecutive compositions are zero as commutative polynomial matrices.

\(\mathrm{End}(C)(t)\) has terms \(\mathrm{Hom}(C^u,C^{u+r})(t)=(\mathrm{ranks}[u]\mathrm{ranks}[u+r])\,\mathcal{O}(r+t)\). At twist \(t=-2\) the stated \(E_1\) reduction leaves one connecting map

\[
d_5:H^4(\mathcal{O}(-5))^{10}\longrightarrow K,\qquad K=\ker\bigl(H^0(\mathcal{O})^{80}\to H^0(\mathcal{O}(1))^{10}\bigr).
\]

The target \(H^0(\mathcal{O}(1))^{10}\) is 50-dimensional, because \(h^0(\mathbb{P}^4,\mathcal{O}(1))=5\).

Over \(\mathbb{Z}\), and hence over \(\mathbb{Q}\) and \(\mathbb{F}_3\), this note computes the hypercohomology of \(\mathrm{End}(C)(-2)\) for the pinned perfect complex \(C\). The \(E_1\) reduction uses only line-bundle cohomology on \(\mathbb{P}^4\), which is free over \(\mathbb{Z}\). The integers \(a_2=10-\mathrm{rank}(d_5)\) and \(h^2=30-\mathrm{rank}(d_5)\) are the hypercohomology ranks of \(\mathrm{End}(C)(-2)\) under that reduction. Identifying \(a_2\) and \(h^2\) with \(\mathrm{End}(H)\) groups requires the separate assertion that \(C\) resolves the intended HM bundle over the field concerned. This note does not certify that assertion. It does not certify the \(D_8\) projector, choice independence, or any obstruction value. It does not re-prove the vanishing of the other \(E_1\) lines, and it does not rerun the large Ext model.

## Conventions

Cover \(U_i=\{x_i\neq 0\}\). A Laurent monomial \(x^a\) is a section of \(\mathcal{O}(\sum a_i)\) on \(U_I\) exactly when \(a_j\ge 0\) for every \(j\notin I\).

Čech differential, on ordered simplices: \((\delta c)_J=\sum_k(-1)^k c_{J\setminus\{j_k\}}\).

Hom differential in internal degree \(r\): \(f\mapsto d\circ f-(-1)^r f\circ d\). The precomposition sign is \(-1\) for \(r\) even and \(+1\) for \(r\) odd.

Total differential: \(D=\delta+(-1)^p d_{\mathrm{Hom}}\), with \(p\) the Čech degree. On each of the \(5340\) distinct terms checked for each contraction policy, \(\delta^2=0\), \(d_{\mathrm{Hom}}^2=0\) and \(\delta d_{\mathrm{Hom}}=d_{\mathrm{Hom}}\delta\), so \(D^2=0\).

Cone contraction. On a monomial strand that is not strictly negative, the pinned vertex \(v\) is the least index with exponent \(\ge 0\). The greatest-vertex comparison uses the greatest index. If \(v\) is the \(m\)-th vertex of an ordered simplex \(I\), then \(h(e_I)=(-1)^m e_{I\setminus v}\) when \(v\in I\), and \(0\) otherwise. For every strand of \(\mathcal{O}(d)\) with \(d\ge -4\) and every cochain of Čech degree at least \(1\), \(\delta h+h\delta=\mathrm{id}\). The ten source strands \(x_0^{-1}\cdots x_4^{-1}\) have no legal vertex; they are the \(H^4\) generators.

The zigzag multipliers of \(h\circ d_{\mathrm{Hom}}\) are \(-1,+1,-1,+1\) at Čech degrees \(4,3,2,1\), followed by one unsigned \(d_{\mathrm{Hom}}\) at degree \(0\). These are the signs forced by \(D=\delta+(-1)^p d_{\mathrm{Hom}}\). Each intermediate equation \(\delta(h(w))=w\) is checked on the cocycle being contracted.

Source order: column \(a\cdot 2+b\), with \(a=0..4\) in \(C^0\) and \(b=0..1\) in \(C^3\). The \(80\) constants are ordered as \(\mathrm{Hom}(C^0,C^2)\) (50 slots) then \(\mathrm{Hom}(C^1,C^3)\) (30 slots). The \(50\) target linears use monomials \(x_4,x_3,x_2,x_1,x_0\).

## Result

The \(50\times 80\) global-section map has rank \(50\) over \(\mathbb{Q}\) and over \(\mathbb{F}_3\). Every pivot is \(+1\), in columns \(0..49\), and the largest absolute entry and the largest elimination intermediate are both \(1\). The free columns are \(50..79\). The resulting \(30\) kernel vectors are a \(\mathbb{Z}\)-basis of a saturated direct summand: their free-variable submatrix is the identity.

The zigzag produces an \(80\times 10\) integral matrix. Every column is a Čech \(0\)-cocycle, hence a global section of \(80\,\mathcal{O}\), and lies in \(K\). Its coordinates on the kernel basis are the \(30\times 10\) matrix with exactly these nonzero entries, all equal to \(1\):

| row | column |
|---:|---:|
| 0, 25 | 0 |
| 10, 20 | 1 |
| 1, 26 | 2 |
| 11, 21 | 3 |
| 2, 27 | 4 |
| 12, 22 | 5 |
| 3, 28 | 6 |
| 13, 23 | 7 |
| 4, 29 | 8 |
| 14, 24 | 9 |

Rows \(5..9\) and \(15..19\) are zero. Each column is the sum of two distinct basis vectors, the twenty positions are disjoint, and a \(10\times 10\) minor equals \(1\).

Ranks of both the \(80\times 10\) matrix and the \(30\times 10\) matrix:

- over \(\mathbb{Q}\): \(10\)
- over \(\mathbb{F}_3\): \(10\)

Smith normal form over \(\mathbb{Z}\): invariant factors \(1,1,1,1,1,1,1,1,1,1\). There are no nontrivial elementary divisors. The map \(\mathbb{Z}^{10}\to K\cong\mathbb{Z}^{30}\) is split injective, and its cokernel is free of rank \(20\).

Therefore \(\mathrm{rank}(d_5)=10\). For the hypercohomology of \(\mathrm{End}(C)(-2)\), the \(E_1\) reduction gives \(a_2=0\) and \(h^2=20\). Identifying \(a_2\) and \(h^2\) with \(\mathrm{End}(H)\) groups requires the separate assertion that \(C\) resolves the intended HM bundle over the field concerned. This note does not certify that assertion, the \(D_8\) projector, choice independence, or any obstruction value. The precommitted prediction was \(\mathrm{rank}(d_5)=10\) over \(\mathbb{Q}\) and \(\mathbb{F}_3\). That prediction matches.

The full matrices, the kernel basis, pivot columns and the check record are the JSON printed by the program.

## Controls

Contraction vertices. Repeating the zigzag with the greatest legal contraction vertex reproduces the same \(80\times 10\) matrix. The maximum absolute difference is \(0\).

Square zero. For each contraction policy, least vertex and greatest vertex, the program checks every used input key \(y\) and every used Hom-image key \(w\): \(5340\) distinct terms per policy. On each of those terms, \(\delta^2=0\), \(d_{\mathrm{Hom}}^2=0\), \(\delta d_{\mathrm{Hom}}=d_{\mathrm{Hom}}\delta\), and the monomial is a section on its simplex. On every contractible term of Čech degree at least \(1\), both cone identities hold: \(\delta h+h\delta=\mathrm{id}\) for the least-vertex homotopy and for the greatest-vertex homotopy. Exactly ten strands have no contraction vertex: the source generators.

Negative controls.

- Reversing the sign in front of \(d_{\mathrm{Hom}}\) at one Čech degree only makes \(D^2\neq 0\). A used basis term in Čech degree \(3\) and internal degree \(-2\) has flipped cross term of absolute value \(2\). With the pinned sign the same cross term cancels.
- Reversing the Tot multiplier uniformly at any one of the four homotopy stages replaces the \(80\times 10\) image by its negative. The negative remains in \(K\). Kernel membership does not detect a global stage sign; the \(D^2\) witness does.
- Reversing that multiplier only on strands contracted at vertex \(0\) leaves the final matrix unchanged at the first three stages. At the last homotopy the same restricted flip produces a cochain whose Čech differential has \(200\) nonzero terms. It is not a global section, so it does not lie in \(K\).

Independent \(80\to 50\) rank. The block was rebuilt from the exterior-sign, contraction and evaluation formulas as a polynomial map, then again by applying the Čech Hom differential to constant Čech representatives. The two matrices agree. Elimination is separate from the zigzag.

No Macaulay2 binary is present, so there is no independent sheaf-cohomology oracle. Nothing was installed to supply one.

## External review report

An entrywise comparison with the separate JavaScript zigzag at commit `f968b53943ba2312f09fbc3e8f9d462e86bcaa34` matched all 800 \(d_5\) entries and all 4,000 ordinary-map entries, as reported in review comment 6130971886 on pull request 76. That comparison is an external review report. This program does not perform it.

## Run

From the repository root:

```
python3 research/hsd/twist-minus2-d5/certificate.py
```

The program uses only the Python standard library and exact integers. It prints one JSON object and exits \(0\) only if the asserted ranks, Smith factors, \(5340\)-term checks for each contraction policy, vertex-policy agreement, cocycle membership, and negative controls all hold.

Python optimized mode (`-O`, `-OO`, or `PYTHONOPTIMIZE`) strips `assert` statements. The proof checks of this certificate are asserts, so `main` refuses to run unless `__debug__` is true: the guard raises `SystemExit` before any computation or output. A refusal at entry tests that guard only. It does not exercise the downstream mutation and negative-control oracle. Paired degenerate controls must still pass the rank identity, and unpaired mutations must still fail their full-rank checks, in non-optimized runs.
