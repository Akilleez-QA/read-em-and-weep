# Design: F₃ fiber-rank certificate for the pinned Horrocks–Mumford complex

Status of this document: design contract only. It does not construct multiplier matrices, does not run a witness search, and does not assert that any degeneracy locus is empty.

The complex is the pinned four-term perfect complex on \(\mathbb{P}^4\)

\[
C=\bigl[5\mathcal{O}(-1)\xrightarrow{\varphi_0}15\mathcal{O}\xrightarrow{\varphi_1}10\mathcal{O}(1)\xrightarrow{\varphi_2}2\mathcal{O}(2)\bigr].
\]

A later run may certify fiber ranks of these three maps over an algebraic closure of \(\mathbb{F}_3\). This file is the contract that run must meet.

## 1. Pinned input

Tree: commit `add03476d9055aa00e1e00778eea6332cf8e01cc`.

| Role | Path | Git blob |
|---|---|---|
| Verifier that rebuilds the maps | `research/hm/verify-hm-ext.js` | `fa5231de92b61143e3406111d4af028284db6d55` |
| Prose model of the same maps | `research/hm/ext-model.md` | `fad0e87f0e30ec916e18fd47feea584c7d8eaae6` |

Scope of \(\mathrm{End}(C)(-2)\), not of this certificate: pull request 76 at head `80ea7e98a09ef6c3f10285cb6d0eedc8bc7f979c`, note `research/hsd/twist-minus2-d5/NOTE.md`. That note computes hypercohomology of the perfect complex. It does not prove that \(C\) resolves a rank-2 sheaf.

### 1.1 Published linear algebra

Let \(V\) have basis \(e_0,\ldots,e_4\) and volume \(\mathrm{vol}(e_0,\ldots,e_4)=1\). Indices are modulo 5. Write

\[
w_i^+=e_{i+2}\wedge e_{i+3},\qquad w_i^-=e_{i+1}\wedge e_{i+4}.
\]

These ten bivectors are a basis of \(\Lambda^2 V\). Let \(B=(\Lambda^2 V^*)^2\) and

\[
b(\eta^+,\eta^-)_i=\eta^+(w_i^-)-\eta^-(w_i^+).
\]

\(W=\ker b\) is 15-dimensional, with the published basis

\[
U_i=(\mathrm{dual}(w_i^+),0),\quad
V_i=(0,\mathrm{dual}(w_i^-)),\quad
Z_i=(\mathrm{dual}(w_i^-),\mathrm{dual}(w_i^+)).
\]

For \(v\in V\) and a bivector \(w\),

\[
\varphi_v(w)(u_1,u_2)=\mathrm{vol}(v,w,u_1,u_2).
\]

The columns of the first map are \(\gamma_i(v)=(\varphi_v(w_i^+),\varphi_v(w_i^-))\in W\). On \(W\), the coordinate along \(Z_i\) is \(\eta^+(w_i^-)\), which equals \(\eta^-(w_i^+)\) precisely because \(b\) vanishes. The verifier uses the first of those two expressions.

Row order of every \(15\)-row matrix in this contract is \(U_0,\ldots,U_4\), then \(V_0,\ldots,V_4\), then \(Z_0,\ldots,Z_4\). Column \(a\) of \(\varphi_0\) is \(\gamma_a\).

### 1.2 How the verifier rebuilds the three matrices

Coordinates on \(V\) are \(x_0,\ldots,x_4\). All three maps are matrices of linear forms. Shapes:

| Map | Shape | Source to target |
|---|---|---|
| \(\varphi_0\) | \(15\times 5\) | \(5\mathcal{O}(-1)\to 15\mathcal{O}\) |
| \(\varphi_1\) | \(10\times 15\) | \(15\mathcal{O}\to 10\mathcal{O}(1)\) |
| \(\varphi_2\) | \(2\times 10\) | \(10\mathcal{O}(1)\to 2\mathcal{O}(2)\) |

Let \(\varepsilon(a_0,\ldots,a_4)\) be the sign of that sequence as a permutation of \(\{0,1,2,3,4\}\), or \(0\) if the entries are not distinct. The coefficient of \(x_k\) in row \(r\), column \(a\) of \(\varphi_0\) is \(\varepsilon(k,p,q,s,t)\), where the pairs \((p,q)\) and \((s,t)\) are:

| Rows \(r\) | Basis vector | \((p,q)\) | \((s,t)\) |
|---|---|---|---|
| \(0\le r\le 4\) | \(U_r\) | \(w_a^+\) | \(w_r^+\) |
| \(5\le r\le 9\) | \(V_{r-5}\) | \(w_a^-\) | \(w_{r-5}^-\) |
| \(10\le r\le 14\) | \(Z_{r-10}\) | \(w_a^+\) | \(w_{r-10}^-\) |

That is the expansion of \(\mathrm{vol}(v,\,\cdot\,,\,\cdot\,)\) in the basis above, and it is the formula implemented by the pinned verifier.

Target of \(\varphi_1\): two copies of \(V^*\), rows \(5h+j\) for factor \(h\in\{0,1\}\) and basis vector \(e_j^*\). Contraction of \(\mathrm{dual}(e_p\wedge e_q)\) on factor \(h\) contributes \(+x_p\) on row \(5h+q\) and \(-x_q\) on row \(5h+p\). The fifteen columns are:

| Columns | Vector | Contractions |
|---|---|---|
| \(i\) | \(U_i\) | \(\mathrm{dual}(w_i^+)\) on factor \(0\) |
| \(i+5\) | \(V_i\) | \(\mathrm{dual}(w_i^-)\) on factor \(1\) |
| \(i+10\) | \(Z_i\) | \(\mathrm{dual}(w_i^-)\) on factor \(0\), and \(\mathrm{dual}(w_i^+)\) on factor \(1\) |

\(\varphi_2\) is paired evaluation \((\alpha,\beta)\mapsto(\alpha(v),\beta(v))\). Its matrix is

\[
\begin{pmatrix}
x_0&x_1&x_2&x_3&x_4&0&0&0&0&0\\
0&0&0&0&0&x_0&x_1&x_2&x_3&x_4
\end{pmatrix}.
\]

### 1.3 Hard assertions before any minor or witness work

Over \(\mathbb{Z}[x_0,\ldots,x_4]\), before reduction to \(\mathbb{F}_3\) and before any minor, multiplier, or chart search:

\[
\varphi_1\circ\varphi_0=0,\qquad\varphi_2\circ\varphi_1=0.
\]

These are polynomial matrix identities. The pinned verifier already aggregates coefficients of each quadratic monomial and throws if any coefficient survives. A later runner repeats that integral check on the matrices rebuilt in §1.2. A nonzero coefficient aborts the run. The check is not a saturation, not a bad-prime scan, and not evidence about ranks.

## 2. Primary certificate form

Work over \(\mathbb{F}_3[x_0,\ldots,x_4]\). The primary certificate is five matrices \(B_0,\ldots,B_4\), each \(15\times 5\), and five positive integers \(N_i\), such that

\[
\varphi_0^{\mathsf T} B_i = x_i^{N_i} I_5.
\]

Verification is exact multiplication of polynomial matrices over \(\mathrm{GF}(3)\), entry by entry, against the diagonal monomial matrix. No Gröbner basis, no saturation computation, and no rank oracle is part of this check.

\(\varphi_0\) is \(15\times 5\), so \(\varphi_0^{\mathsf T}\) is \(5\times 15\) and the product is \(5\times 5\). On the standard chart \(D(x_i)\) the right-hand side is a unit times \(I_5\), so \(\varphi_0^{\mathsf T}\) is split surjective and \(\varphi_0\) has rank \(5\) at every point of the chart.

Alternate form, accepted in place of the matrix identity: an explicit membership

\[
x_i^{N}\in I_5(\varphi_0)=\mathrm{Fit}_0\bigl(\mathrm{coker}(\varphi_0^{\mathsf T})\bigr),
\]

with each minor named by its five row indices and with cofactor polynomials written down, again checked by multiplication only. Stacks 07Z6: for a presentation \(R^{15}\to R^5\to M\to 0\), the \(0\)th Fitting ideal is the ideal of \(5\times 5\) minors. Here \(M=\mathrm{coker}(\varphi_0^{\mathsf T})\) for the transpose reading of §3, and \(I_5(\varphi_0)\) denotes that ideal.

A checked identity of either form proves projective emptiness of the rank-\(<5\) locus of \(\varphi_0\): the locus misses every standard chart, and those charts cover \(\mathbb{P}^4\). This document does not exhibit either identity and does not assert that emptiness.

The two forms are alternatives for this one rank-\(5\) statement. A later result file must say which form was multiplied.

## 3. T₂ definition

\[
T_2=\mathrm{coker}(\varphi_0^{\mathsf T})\;/\;I_5(\varphi_0)
\]

for the transposed bundle map

\[
\varphi_0^{\mathsf T}:15\mathcal{O}\longrightarrow 5\mathcal{O}(1).
\]

Stacks 07Z6 supplies the Fitting ideal. \(\mathrm{Fit}_0\subseteq\mathrm{Ann}\), so \(T_2\) is that cokernel regarded as a module over the quotient by \(I_5(\varphi_0)\). Its support is the rank-\(<5\) locus.

The untransposed cokernel of \(5\mathcal{O}(-1)\to 15\mathcal{O}\) is a different sheaf. On the rank-\(5\) locus that map is injective and the cokernel has rank \(10\). Its \(0\)th Fitting ideal is zero. \(T_2\) is not that cokernel.

Reading ranks uses local unit-minor splitting plus the two complex identities of §1.3. Stacks 00MR records the Buchsbaum–Eisenbud analysis of exactness of finite free complexes; Lemma 10.102.2 is the unit-coefficient splitting: after a basis change, an invertible matrix entry splits off an identity summand. A unit \(5\times 5\) minor is the same splitting after a basis change on the five selected rows. Fiber ranks are the ranks of those split maps at closed points.

Raw rank sums are not a rank computation. In particular the Buchsbaum–Eisenbud count \(\mathrm{rank}(\varphi_0)+\mathrm{rank}(\varphi_1)=\mathrm{rank}(15\mathcal{O})\) is the wrong numerical test on this complex: the middle cohomology is expected to have rank \(2\), and \(5+8=13\) leaves that \(2\) inside the middle term \(15\). See §4 for the fiber dimensions that replace the sum.

## 4. Rank identity

This identity retires a separate \(T_1\). For the authentic pinned maps, over every field and every \(v\neq 0\),

\[
\mathrm{rank}\,\varphi_1(v)=3+\mathrm{rank}\,\varphi_0(v).
\]

The Mr. Slop argument, via \(W=\ker b\), \(E_v\), and the volume pairing \(A_v\), is as follows.

Fix a field \(k\) and \(v\in V\setminus\{0\}\). Interior product \(\iota_v:\Lambda^2 V^*\to V^*\) has image \(\mathrm{Ann}(v)\) and kernel of dimension \(6\). Set \(K_v=\ker(\iota_v\oplus\iota_v)\), so \(\dim K_v=12\). The volume pairing

\[
A_v:\Lambda^2 V/E_v\xrightarrow{\sim}\ker\iota_v,\qquad E_v=\ker\varphi_v=v\wedge V,
\]

is an isomorphism: both sides have dimension \(6\), and \(\varphi_v(w)\) lands in \(\ker\iota_v\). The induced pairing \(\langle\alpha,\beta\rangle_v=\mathrm{vol}(v\wedge\alpha\wedge\beta)\) on \(\Lambda^2(V/kv)\) is perfect in every characteristic (its Gram matrix is a unit multiple of three hyperbolic planes).

Thus \(\mathrm{rank}\,\varphi_1(v)=\dim W-\dim(W\cap K_v)\). With \(\dim W=15\),

\[
\dim(W\cap K_v)=\dim K_v-\mathrm{rank}(b|_{K_v})=12-\mathrm{rank}(b|_{K_v}),
\]

so \(\mathrm{rank}\,\varphi_1(v)=3+\mathrm{rank}(b|_{K_v})\). Transporting \(b|_{K_v}\) across \(A_v\oplus A_v\) identifies that rank with

\[
\dim\mathrm{span}\bigl\{(w_i^-,\,-w_i^+)\bmod E_v^2\bigr\}.
\]

The automorphism \(J(\alpha,\beta)=(\beta,-\alpha)\) of \((\Lambda^2 V/E_v)^2\) is invertible in every characteristic, preserves \(E_v^2\), and carries \((w_i^+,w_i^-)\) to \((w_i^-, -w_i^+)\). Therefore the span has the same dimension as

\[
\mathrm{rank}\,\varphi_0(v)=\dim\mathrm{span}\{\gamma_i(v)\},
\]

which is legitimate because each \(\gamma_i(v)\) lies in \(W\) for the authentic bivectors. This is the identity.

Consequences for the authentic maps, at every \(v\neq 0\):

- A projective rank-\(5\) certificate for \(\varphi_0\) alone forces \(\mathrm{rank}\,\varphi_1(v)=8\).
- Euler evaluation forces \(\mathrm{rank}\,\varphi_2(v)=2\). The matrix in §1.2 has two nonzero rows supported on complementary columns, and each row is \(v\) itself.

Fiber dimensions of the complex of vector spaces, writing \(r=\mathrm{rank}\,\varphi_0(v)\):

| Slot | Dimension |
|---|---|
| \(\ker\varphi_0\) | \(5-r\) |
| \(\ker\varphi_1/\mathrm{im}\,\varphi_0\) | \(12-2r\) |
| \(\ker\varphi_2/\mathrm{im}\,\varphi_1\) | \(5-r\) |
| \(\mathrm{coker}\,\varphi_2\) | \(0\) |

At \(r=5\) the fibers are \((0,2,0,0)\).

Separate membership in \(I_8(\varphi_1)\), and a separate vanishing proof for the right-hand homology, are off the proof path for the authentic maps. The identity and the evaluation matrix supply those two ranks once the rank-\(5\) certificate for \(\varphi_0\) is in hand.

Optional cross-check, not a proof obligation: an \(8\times 15\) chart reduction for \(\varphi_1\). On each \(D(x_i)\) one may exhibit polynomial multipliers whose product with \(\varphi_1\) is \(x_i^{M} I_8\) after projection onto an \(8\)-row quotient. Exact multiplication may be used to cross-check the identity. A missing or inconclusive reduction does not touch the proof, and a successful reduction is not a substitute for the \(\varphi_0\) certificate.

## 5. Controls

Controls run after the integral composition assertions and before any authentic witness search. They use the same shapes and the same multiplication-or-point rules. They are not certificates about the authentic maps.

A negative control passes only when it reports both the sentence `no witness / saturation not unit` and the explicit point below with the rank below. The point is the proof: it lies on a standard chart, the relevant matrix has rank strictly below the certificate threshold there, so no chart identity of the primary shape exists, and every maximal minor vanishes at the point, so the saturation of that minor ideal by the irrelevant ideal is not the unit ideal. A timeout without that point is a failed control, not a pass.

### 5.1 Unpaired negative control: \(x_0\)-deleted \(\varphi_0\)

Delete the coefficient of \(x_0\) in every entry of the authentic \(\varphi_0\). Call the result \(\varphi_0^{\setminus 0}\). It is still \(15\times 5\), linear in \(x_1,\ldots,x_4\).

At \(p_*=(1,0,0,0,0)\), every surviving entry is zero, so

\[
\mathrm{rank}\,\varphi_0^{\setminus 0}(p_*)=0.
\]

Required report:

```
control: x0-deleted-phi0
report: no witness / saturation not unit
point: [1:0:0:0:0]
rank: 0
```

### 5.2 Unpaired negative control: \(\varphi_1\) on its first five forms

The first five forms are the domain restriction of \(\varphi_1\) to \(U_0,\ldots,U_4\), verifier columns \(0\) through \(4\): the five contractions \(\mathrm{dual}(w_i^+)\) on the first factor of \(V^*\). The matrix is \(10\times 5\). It is not the first five target rows.

At \(p_*=(1,0,0,0,0)\) the only nonzero entries are

| Row | Column | Value |
|---|---|---|
| \(4\) | \(2\) | \(-1\) |
| \(1\) | \(3\) | \(+1\) |

from the rule in §1.2: column \(i=2\) has \(w_2^+=e_4\wedge e_0\), contributing \(-x_0\) on row \(4\); column \(i=3\) has \(w_3^+=e_0\wedge e_1\), contributing \(+x_0\) on row \(1\). Rank is \(2\).

Required report:

```
control: phi1-first-five-forms
report: no witness / saturation not unit
point: [1:0:0:0:0]
rank: 2
```

There is no \(8\times 8\) minor of a \(10\times 5\) matrix. The ideal of \(8\times 8\) minors is \((0)\).

### 5.3 Paired degenerate positive control

One sparse \(b'\), with \(\gamma'\) and \(\varphi_1'\) rebuilt from the same bivectors. This is the guard against a vacuous identity oracle that only ever sees the authentic maps and prints ranks \((5,8)\) without a case where both sides drop.

Bivectors, indices modulo \(5\):

\[
\begin{aligned}
w_i^{+'}&=w_i^{-'}=e_0\wedge e_{i+1} &&\text{for }i=0,1,2,3,\\
w_4^{+'}&=e_1\wedge e_2,\\
w_4^{-'}&=e_3\wedge e_4.
\end{aligned}
\]

\[
b'(\eta^+,\eta^-)_i=\eta^+(w_i^{-'})-\eta^-(w_i^{+' }).
\]

Four components each read a single repeated bivector; the fifth reads one complementary pair. This \(b'\) is surjective of rank \(5\): the five coordinate functionals \(\eta\mapsto\eta(e_0\wedge e_{j})\) for \(j=1,\ldots,4\) and \(\eta\mapsto\eta(e_3\wedge e_4)\) are independent, and each standard basis vector of \(k^5\) is hit by a one-sparse \((\eta^+,\eta^-)\). Thus \(W'=\ker b'\) has dimension \(15\), and the rank identity of §4 applies verbatim, with constant \(3\).

At \(p_*=(1,0,0,0,0)\), \(\varphi_{p_*}\) vanishes on \(e_0\wedge V\), so the columns \(i=0,1,2,3\) of \(\gamma'\) are zero. The remaining column is \((\varphi_{p_*}(e_1\wedge e_2),\,\varphi_{p_*}(e_3\wedge e_4))\neq 0\). It lies in \(\ker b'\): for \(i<4\) both bivectors contain \(e_0\), and for \(i=4\)

\[
\mathrm{vol}(e_0\wedge e_1\wedge e_2\wedge e_3\wedge e_4)
-\mathrm{vol}(e_0\wedge e_3\wedge e_4\wedge e_1\wedge e_2)=1-1=0.
\]

So \(\mathrm{rank}\,\gamma'(p_*)=1\). The identity gives \(\mathrm{rank}\,\varphi_1'(p_*)=4\), and \(4=3+1<8\).

A later runner rebuilds \(\gamma'\) and \(\varphi_1'\) from \(b'\) by the same formulas as §1.2, evaluates both matrices at \(p_*\) over \(\mathbb{F}_3\), and requires the ranks \(1\) and \(4\). Required report:

```
control: paired-sparse-b-prime
point: [1:0:0:0:0]
rank_gamma: 1
rank_phi1: 4
identity: 4 = 3 + 1 < 8
```

Any other triple fails the run. An oracle that cannot return a drop below \(8\) fails this control.

## Search policy and algebraic reuse

Source: null, pull request 76, comment 6131466767. These are reuse rules for a future graded search. They are not a witness, and they do not authorize a search from this document.

### Naming

\(G=\varphi_0\), the pinned \(15\times 5\) matrix. On the pull request 76 thread the Heisenberg generator and the \(5\)-cycle already reduce five chart searches to one chart matrix \(B_0\), followed by four deterministic transports and five independent multiplications. In this section \(G^{\mathsf T}\) means that graded chart matrix in the one-chart \(B_0\) coordinates after that transport. It is not a new map, and it does not replace the pinned \(\varphi_0\).

The chart coordinate \(v_0\) is the weight-\(0\) variable in the \(\tau\)-grading of that same thread: \(\mathrm{wt}(v_0)=0\). The symbols \(x_i\) of §2 are the homogeneous coordinates on the same \(\mathbb{P}^4\); \(v_0\) is the chart variable of weight \(0\).

For exponent \(N\), write \(s=\binom{N+3}{4}\) and \(t=\binom{N+4}{4}\). One graded column splits into blocks of shape \(t\times 3s\). Those shapes are the blocks named below. The numeric launch caps of §6 are unchanged.

### Reuse rules

1. Write \(M=\mathrm{coker}(G^{\mathsf T})\) over \(\mathbb{F}_3[v_0,\ldots,v_4]\), with standard quotient generators \(\bar e_j\). A chart witness at exponent \(N\) is equivalent to \(v_0^N M=0\). For each column define \(N_j=\min\{N:v_0^N\bar e_j=0\}\), allowing \(\infty\). The common threshold is \(\max_j N_j\). There is no finite witness if any \(N_j=\infty\).

2. Once an individual column \(b_j\) is certified by \(G^{\mathsf T} b_j=v_0^n e_j\), every later exponent \(N\ge n\) uses \(v_0^{N-n} b_j\). That column needs no new solve. Because \(\mathrm{wt}(v_0)=0\) in the \(\tau\)-grading already in the design thread, this lift stays in its required graded \(t\times 3s\) block. Keep certified columns. Solve only unresolved right-hand side blocks. Assemble at the maximum successful exponent before all five chart multiplications.

3. A completed inconsistent dual for one column at \(N\) excludes the common witness for every exponent \(\le N\) for that column. It does not invalidate already certified other columns.

4. Finding any witness needs no binary search for the minimum exponent. Binary refinement is useful only if minimum degree is itself required. Degree doubling has no constant cost advantage when linear-system costs grow rapidly with \(N\) (\(s=\binom{N+3}{4}\), \(t=\binom{N+4}{4}\), blocks \(t\times 3s\)). A degree schedule should be compared in measured or justified cost units under the existing launch caps. A timeout or a cap remains inconclusive, not empty.

## 6. Resource caps

These caps are mandatory launch gates. They are not a Nullstellensatz degree theorem. Review may tighten them. No later launch proceeds without all four gates in force.

| Gate | Cap |
|---|---|
| Degree | Each entry of each \(B_i\) has total degree at most \(6\). Each exponent satisfies \(1\le N_i\le 7\). |
| Bytes | The serialized witness and its multiplication transcript occupy at most \(2\cdot 10^6\) bytes. |
| Wall-clock time | At most \(120\) seconds for each chart, and at most \(600\) seconds for the whole launch. |
| Memory | At most \(1\) GiB resident set. |

Hitting a cap, including a timeout, yields status `inconclusive`. That status is not a zero, not a non-membership, and not a nonempty locus. The process must not exit \(0\) on a cap. Suggested exits: \(0\) only when compositions, all three controls, and a multiplied certificate all hold; \(1\) on a failed assertion; \(2\) on inconclusive.

Integral work allowed in the launch is the composition identities of §1.3 and the constant arithmetic inside the controls. A \(\mathbb{Z}\)-saturation, an integral bad-prime diagnostic, a reduction modulo any prime other than the coefficient prime \(3\) of the certificate, and a rational reconstruction are out of scope. They are not \(\mathbb{F}_3\) or \(\mathbb{Q}\) content of this contract, and they must not be run.

## 7. What success means

Success is a future run, not this document. It means all of the following, and nothing further.

Over an algebraic closure of \(\mathbb{F}_3\), the authentic pinned maps have fiber ranks \((5,8,2)\) at every \(v\neq 0\), read from a multiplied rank-\(5\) certificate for \(\varphi_0\), the identity of §4, and the evaluation matrix of \(\varphi_2\).

\(C\otimes\mathbb{F}_3\) then has fibers \((0,2,0,0)\). It resolves a rank-\(2\) sheaf \(H\): the cohomology is that rank-\(2\) sheaf in the middle slot, and the other three cohomologies vanish. Local splitting is the unit-minor splitting of §3 together with constant rank, not a sum of global matrix ranks.

Only after that resolution statement do the \(\mathrm{End}(C)(-2)\) groups computed at `80ea7e98a09ef6c3f10285cb6d0eedc8bc7f979c` become \(\mathrm{Ext}^*(H,H(-2))\) over \(\mathbb{F}_3\).

Success does not transfer a characteristic-\(0\) ambient obstruction. It does not establish choice independence of the pin. It does not produce an obstruction value.

## 8. FMEA

| Failure mode | Effect | Detection | Mitigation |
|---|---|---|---|
| Pinned-map drift | A witness for a different complex is reported as a certificate for \(C\). | Rebuild \(\varphi_0,\varphi_1,\varphi_2\) from §1.2 and compare the sparse term list with blob `fa5231de92b61143e3406111d4af028284db6d55` before any search. | Abort on the first differing term. Do not search. |
| Basis drift against `fa5231de` | A correct multiplier for a permuted \(U,V,Z\) order or a flipped \(\varepsilon\) is accepted. | Entrywise match to the sign formula and the row order in §1.2, not merely vanishing of the two compositions. | Compositions are necessary and not sufficient. Fail closed on any basis mismatch with the blob. |
| Vacuous identity oracle | A checker that never sees a rank drop prints \(\mathrm{rank}\,\varphi_1=8\) for the authentic maps without testing the identity. | The paired control of §5.3 returns ranks \(1\) and \(4\) with \(4=3+1<8\). | The control is mandatory and uses \(b'\), not the authentic \(b\). An oracle that only accepts \((5,8)\) fails the launch. |
| `assert` stripped by `PYTHONOPTIMIZE` | A later Python runner loses its predicates under `python -O` or `PYTHONOPTIMIZE` set, and exits \(0\). | Launch refuses to start unless `sys.flags.optimize==0` and `PYTHONOPTIMIZE` is unset. | Certificate predicates raise. Bare `assert` is not on the proof path. This document has no runner; the row binds any later one. |
| Claim inflation to \(\mathrm{End}(H)/O_2\) | Fiber ranks are reported as an \(\mathrm{End}(H)\) calculation, as \(\mathrm{Ext}\) groups before the resolution hypothesis, or as an obstruction value \(O_2\). | The result banner is restricted to the sentences in §7. A file that states an obstruction value, a characteristic-\(0\) transfer, or choice independence is a failed run. | The conditional identification with \(\mathrm{Ext}^*(H,H(-2))\) is allowed only after the resolution statement, and it is not an obstruction computation. |
| Assemble before every column is at the same \(N\) | A partial maximum is published as a common chart witness. | The assembly log lists a column that is not certified or lifted to that \(N\). | Assemble only after all five columns, or all fifteen before transport, are certified or lifted to the same \(N\). |
| Re-solve of a certified column | Wasted cost, and a risk of basis drift against the stored column. | A column index that already has a stored \((b_j,n)\) is submitted to a new solve. | Refuse the re-solve. Store \((b_j,n)\) and lift by \(v_0^{N-n}\). |
| Dual kill read across columns | An inconsistent dual for one right-hand side aborts certified columns of other indices. | The dual log does not name a single column index. | Dual kill is per right-hand side. The log names the column index. |
| Degree doubling without a cost model | A timeout or a cap is read as emptiness. | The degree schedule has no measured or justified cost comparison. | Compare schedules in cost units under the caps of §6. A cap remains `inconclusive`. |

## 9. Stop

This pull request is the design. Witness construction does not start here. The \(B_i\) are not built. No Gröbner basis, Macaulay2 session, or other computer-algebra search is part of the deliverable.

Review is requested on the corrected \(T_2\) reading, the retirement of a separate \(T_1\), the three controls, the launch caps, and the search-policy reuse rules from comment 6131466767. Stop after that review request. Witness construction remains unstarted.
