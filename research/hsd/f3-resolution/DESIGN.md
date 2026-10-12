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
x_i^{N}\in I_5(\varphi_0)=\mathrm{Fitt}_0(M),\qquad M=\mathrm{coker}(\varphi_0^{\mathsf T}),
\]

with each minor named by its five row indices and with cofactor polynomials written down, again checked by multiplication only. Stacks Project, tag 07Z6: for a presentation \(R^{15}\to R^5\to M\to 0\), the \(0\)th Fitting ideal is the ideal of \(5\times 5\) minors. The module \(M\) is the one in §3, and \(I_5(\varphi_0)\) denotes that ideal.

A checked identity of either form proves projective emptiness of the rank-\(<5\) locus of \(\varphi_0\): the locus misses every standard chart, and those charts cover \(\mathbb{P}^4\). This document does not exhibit either identity and does not assert that emptiness.

### 2.1 Exponents: equivalent existence, different minima

Let \(A=\varphi_0^{\mathsf T}\). Write \(N^*\) for the least positive integer such that \(AB=x_0^{N^*}I_5\) for some \(15\times 5\) matrix \(B\), and write \(e\) for the least positive integer such that \(x_0^e\in I_5(\varphi_0)\). For each column let \(N_j\) be the least positive integer such that \(x_0^{N_j}e_j\) lies in the image of \(A\), so \(N^*=\max_j N_j\) whenever every \(N_j\) is finite. If these integers are finite, then

\[
N^*\le e\le 5N^*,
\]

and, because the entries of \(\varphi_0\) are linear, so that \(I_5(\varphi_0)\) is generated by quintics,

\[
\max(N^*,5)\le e\le\sum_j N_j\le 5N^*.
\]

This is the matrix form of \(\mathrm{Ann}(M)^5\subseteq\mathrm{Fitt}_0(M)\subseteq\mathrm{Ann}(M)\) for a module on five generators. Stacks Project §15.8, tag 07ZA, records the right-hand inclusion; Eisenbud, *Commutative Algebra*, Proposition 20.7, records both inclusions. One direction is Bézout: from \(x_0^e=\sum_J f_J\det(A_J)\), place the adjugate of each \(A_J\) into the rows indexed by \(J\). The sum multiplies to \(AB=x_0^e I_5\), so a minor membership at exponent \(e\) is a matrix witness at the same exponent. The other direction is Cauchy–Binet: \(AB=x_0^{N^*}I_5\) puts \(x_0^{5N^*}\) in \(I_5(\varphi_0)\). Stacking minimal column witnesses gives \(AB=\mathrm{diag}(x_0^{N_1},\ldots,x_0^{N_5})\), and Cauchy–Binet then puts \(x_0^{\sum_j N_j}\) in \(I_5(\varphi_0)\). The receipts \(N_j\) of the certified-column rule in the search-policy section determine the minor-side upper bound with no extra search.

The two forms are equivalent for eventual existence of some finite exponent. They are not equivalent for the minimal exponent. A degree-capped minor-membership negative is not a negative for the matrix witness. In particular, failure to find a maximal-minor membership through exponent \(7\) does not establish failure of the primary matrix-witness search through exponent \(7\). A matrix witness at \(N\le 7\) forces minor membership only by exponent \(\sum_j N_j\le 5N\le 35\). That comparison is a bound. It is not a claim that the factor \(5\) is attained for this \(\varphi_0\), and it does not enlarge the search. The generic linear example \(A=x_0 I_5\) has \(N_j=1\) and \(I_5=(x_0^5)\), so \(e=5=\sum_j N_j=5N^*\); the constant \(5\) is sharp for some matrices and is not improved here.

The bounded-degree oracle of this contract is the primary graded matrix-column test and its exact dual, as specified in the search-policy section. A minor-membership positive at exponent \(e\), once the adjugate matrix is written down and the product is multiplied, is a matrix positive at \(N=e\). A later result file must say which form was multiplied, and every receipt carries one of the certificate types in §8: `matrix-column`, `minor-membership`, or `dual`.

Sources for this distinction: pull request 78, comments 6131529423 and 6131552413.

## 3. The module \(M\)

Let \(R\) be \(\mathbb{Z}[x_0,\ldots,x_4]\) before the coefficient reduction, and \(\mathbb{F}_3[x_0,\ldots,x_4]\) for the certificate. Define

\[
M=\mathrm{coker}(\varphi_0^{\mathsf T})
\]

for the transposed bundle map

\[
\varphi_0^{\mathsf T}:15\mathcal{O}\longrightarrow 5\mathcal{O}(1).
\]

Then \(\mathrm{Fitt}_0(M)=I_5(\varphi_0)\). Stacks Project, tag 07Z6, supplies the Fitting ideal. Since \(\mathrm{Fitt}_0(M)\subseteq\mathrm{Ann}(M)\) (Stacks Project §15.8, tag 07ZA), \(M\) is naturally a module over \(R/I_5(\varphi_0)\). Its support is

\[
\mathrm{Supp}\,M=V(\mathrm{Fitt}_0 M),
\]

the locus where \(\varphi_0\) has rank less than \(5\). This contract does not define that module by a slash quotient. The notation \(\mathrm{coker}(\varphi_0^{\mathsf T})/I_5(\varphi_0)\) is not used.

The untransposed cokernel of \(5\mathcal{O}(-1)\to 15\mathcal{O}\) is a different sheaf. On the rank-\(5\) locus that map is injective and the cokernel has rank \(10\). Its \(0\)th Fitting ideal is zero. \(M\) is not that cokernel.

Reading ranks uses local unit-minor splitting plus the two complex identities of §1.3. Stacks 00MR records the Buchsbaum–Eisenbud analysis of exactness of finite free complexes; Lemma 10.102.2 is the unit-coefficient splitting: after a basis change, an invertible matrix entry splits off an identity summand. A unit \(5\times 5\) minor is the same splitting after a basis change on the five selected rows. Fiber ranks are the ranks of those split maps at closed points.

Raw rank sums are not a rank computation. In particular the Buchsbaum–Eisenbud count \(\mathrm{rank}(\varphi_0)+\mathrm{rank}(\varphi_1)=\mathrm{rank}(15\mathcal{O})\) is the wrong numerical test on this complex: the middle cohomology is expected to have rank \(2\), and \(5+8=13\) leaves that \(2\) inside the middle term \(15\). See §4 for the fiber dimensions that replace the sum.

## 4. Rank identity

This identity retires a separate \(T_1\). For the authentic pinned maps, over every field and every \(v\neq 0\),

\[
\mathrm{rank}\,\varphi_1(v)=3+\mathrm{rank}\,\varphi_0(v).
\]

The argument, via \(W=\ker b\), \(E_v\), and the volume pairing \(A_v\), is as follows.

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

A separate \(8\times 15\) chart reduction for \(\varphi_1\) is not part of this bounded job. This document does not budget it, and a later launch under §6 does not run it.

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

### 5.3 Pointwise paired control at \(p_*\)

This control is pointwise at \(p_*=[1:0:0:0:0]\). It is not a polynomial complex, and it does not assert that the mutated data satisfy \(\varphi_1'\circ\gamma'=0\) as matrices of polynomials. It guards against a vacuous identity oracle that only ever sees the authentic maps and prints ranks \((5,8)\) without a point where both sides drop.

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

Four components each read a single repeated bivector; the fifth reads one complementary pair. The map \(b':(\Lambda^2 V^*)^2\to k^5\) is surjective of rank \(5\): the five coordinate functionals \(\eta\mapsto\eta(e_0\wedge e_j)\) for \(j=1,\ldots,4\) and \(\eta\mapsto\eta(e_3\wedge e_4)\) are independent, and each standard basis vector of \(k^5\) is hit by a one-sparse \((\eta^+,\eta^-)\). Thus \(\ker b'\) has dimension \(15\). That dimension is recomputed from \(b'\) in the procedure below. It is not inherited from the authentic kernel.

For these bivectors, \(b'\gamma'\) is not the zero matrix. On column \(4\),

| Row \(i\) | Entry \((b'\gamma')_{i,4}\) |
|---|---|
| \(0\) | \(-x_2\) |
| \(1\) | \(+x_1\) |
| \(2\) | \(+x_4\) |
| \(3\) | \(-x_3\) |
| \(4\) | \(0\) |

The signs are exactly the ones in the table: \(-x_2,+x_1,+x_4,-x_3\), and the last entry \(0\). Those are the column-\(4\) entries \(\pm x_1,\pm x_3,\pm x_4\) together with the \((i=0)\) entry \(-x_2\). The four linear forms vanish together only on the line through \(p_*\). Off that line, column \(4\) of \(\gamma'(v)\) is not in \(\ker b'\), so \(\gamma'(v)\) is not contained in \(\ker b'\). On the line, membership is the pointwise check at \(p_*\) in the procedure below; the columns are homogeneous, so the check covers the line. Sources for the column-\(4\) entries: pull request 78, comments 6131521254 and 6131574903.

The basis \(U_i,V_i,Z_i\) of §1.2 is a basis of \(\ker b\) for the authentic bivectors only. It is not a basis of \(\ker b'\). The authentic list is not reused. For this mutated \(b'\) and the authentic vectors \(U_i=(\mathrm{dual}(w_i^+),0)\), with \(w_i^+=e_{i+2}\wedge e_{i+3}\), the component \(b'(U_i)_j\) is the pairing of \(w_i^+\) with \(w_j^{-'}\). That pairing is \(0\) for every \(j\) when \(i\in\{0,4\}\), and it equals \(1\) at the two positions below.

\[
\begin{aligned}
U_0&=(\mathrm{dual}(e_2\wedge e_3),0)\in\ker b',\\
U_4&=(\mathrm{dual}(e_1\wedge e_2),0)\in\ker b',\\
b'(U_1)_4&=1,\qquad U_1=(\mathrm{dual}(e_3\wedge e_4),0),\\
b'(U_3)_0&=1,\qquad U_3=(\mathrm{dual}(e_0\wedge e_1),0).
\end{aligned}
\]

The claim \(b'(U_0)_0=1\) is false and is withdrawn. The two evaluations \(b'(U_1)_4=1\) and \(b'(U_3)_0=1\) are the counterexamples. The authentic list is not reused. Build \(\gamma'\) in \((\Lambda^2 V^*)^2\).

Sources for the withdrawn claim and the two counterexamples: pull request 78, comments 6131776264 and 6131777532.

Unit minor. On the authentic basis of \(W\), \(b'\) sends the five vectors \(U_3\), \(V_1\), \(-V_4\), \(-U_2\), \(U_1\) to \(e_0,e_1,e_2,e_3,e_4\) in that order. The matrix of those images is \(I_5\), so the determinant is \(1\). The minor is a unit in \(\mathbb{Z}\). Therefore \(b'\) restricted to \(W\) is surjective after every base change, including reduction to \(\mathbb{F}_3\), and

\[
\dim(W\cap\ker b')=10
\]

over every field, including \(\mathbb{F}_3\). This unit minor is the certificate for that dimension. A rank table computed over one field is not a substitute for it. The nonzero entries of the images \(e_0\) and \(e_4\) are the counterexamples \(b'(U_3)_0=1\) and \(b'(U_1)_4=1\).

Sensor at the control point. At \(p_*=[1:0:0:0:0]\), on the representative \(e_0\), the mutated column is

\[
\gamma'_4=(\mathrm{dual}(e_3\wedge e_4),\mathrm{dual}(e_1\wedge e_2)).
\]

Direct contraction gives \(b'\gamma'_4=0\) and \(b\gamma'_4=-e_4\). The second value places \(\gamma'_4\) outside \(W=\ker b\). Adjoining it to a basis of \(W\) raises the rank from \(15\) to \(16\), so the matrix \([W\mid\gamma'_4]\) has rank \(16\).

A later runner performs all five of the following steps over \(\mathbb{F}_3\), and does not skip any of them by quoting §4. The unit-minor identity is integral and remains \(I_5\) after reduction to \(\mathbb{F}_3\).

1. Build the five columns \(\gamma'(v)=(\varphi_v(w_i^{+' }),\varphi_v(w_i^{-'}))\) in the ambient \(20\)-dimensional space \((\Lambda^2 V^*)^2\). Do not expand them in the authentic \(U,V,Z\) basis.
2. Verify the unit minor: \(b'\) on \((U_3,V_1,-V_4,-U_2,U_1)\) equals \(I_5\), with determinant \(1\). Record \(\dim(W\cap\ker b')=10\) from that minor, over every field, including \(\mathbb{F}_3\).
3. Independently construct a basis matrix \(E'\) of \(\ker b'\) by elimination on the \(5\times 20\) matrix of \(b'\). Require \(b'E'=0\) and \(\mathrm{rank}(E')=15\). Do not take the columns of \(E'\) from the authentic basis of \(W\).
4. Exact ambient reconstruction. Produce coefficients \(g'\) with \(E'g'=\gamma'(p_*)\) in the ambient coordinates of \((\Lambda^2 V^*)^2\). A ker-membership flag that does not exhibit this equality is not a pass. The column \(\gamma'_4\) lies in the column space of \(E'\) and does not lie in \(W\).
5. Compute the rank of the contraction \(\iota_{p_*}\oplus\iota_{p_*}\) restricted to the column space of \(E'\).

Expected values, and the only passing report: the unit minor is \(I_5\) with determinant \(1\), \(\mathrm{rank}(E')=15\), the reconstruction \(E'g'=\gamma'(p_*)\) holds, \(\mathrm{rank}\,\gamma'(p_*)=1\), the restricted contraction has rank \(4\), and \(4=3+1<8\). The two ranks are computed separately. The relation \(4=3+1\) is the numerical check at \(p_*\), not the claim that §4 supplies a polynomial identity for \(b'\). A pass is evidence about this point. It is not evidence about a second complex.

Required report:

```
control: paired-sparse-b-prime
point: [1:0:0:0:0]
ambient: (Lambda^2 V*)^2
unit_minor: I_5
unit_minor_det: 1
dim_W_intersect_ker_b_prime: 10
ker_basis: E'
b_prime_E_prime: 0
rank_E_prime: 15
reconstruction: E' g' = gamma'(p*)
gamma4_outside_W: rank [W | gamma'4] = 16
rank_gamma: 1
rank_contraction_on_ker: 4
identity: 4 = 3 + 1 < 8
```

Any other report fails the run. A ker-membership check without the reconstruction fails the run. An oracle that cannot return a drop below \(8\) fails this control.

Sources for the unit minor and the reconstruction sensor: pull request 78, comments 6131895075 and 6131921721.

### 5.4 Synthetic checker control

This control tests the polynomial certificate checker. It does not test the rank identity of §4. It requires no rational search and no rational reconstruction. A pass is not an authentic certificate for the pinned maps over \(\mathbb{Q}\), and it does not close the fiber-rank gate of §7. The fixture label is `synthetic-ab-x0`. A receipt that uses any other label for these matrices, or that calls them an authentic \(\mathbb{Q}\) certificate, a Horrocks–Mumford witness, or a rank certificate, fails the run. The square sharpness example \(A=x_0 I_5\) in §2.1 is a different matrix and is not this fixture.

The sentence “QQ should pass by HM” is not a specification and is not this control.

Shapes match the primary certificate: \(A\) is \(5\times 15\) and \(B\) is \(15\times 5\). Entries lie in \(\mathbb{Z}[x_0]\). Rows and columns are indexed from \(0\).

Direct encoding, used by the polynomial certificate checker:

\[
A_{p,q}=\begin{cases}
x_0 & \text{if }0\le q\le 4\text{ and }p=q,\\
0 & \text{otherwise,}
\end{cases}
\qquad
B_{r,c}=\begin{cases}
1 & \text{if }0\le r\le 4\text{ and }r=c,\\
0 & \text{otherwise.}
\end{cases}
\]

In blocks, \(A=[x_0 I_5\mid 0]\) with the zero block of shape \(5\times 10\), and \(B\) is \(I_5\) in rows \(0\) through \(4\) with zeros in rows \(5\) through \(14\). The identity is

\[
AB=x_0 I_5.
\]

Grading-builder encoding. This placement is required when the same fixture is exercised through the authentic \(\tau\)-grading builder of the search-policy section. Column \(a\)'s factor \(x_0\) is placed at row \(t\equiv -a\pmod{5}\), instead of on the diagonal, and \(B\) receives the matching embedding:

\[
A_{p,q}=\begin{cases}
x_0 & \text{if }0\le q\le 4\text{ and }p\equiv -q\pmod{5},\\
0 & \text{otherwise,}
\end{cases}
\qquad
B_{r,c}=\begin{cases}
1 & \text{if }0\le c\le 4\text{ and }r\equiv -c\pmod{5},\\
0 & \text{otherwise.}
\end{cases}
\]

The rows occupied by columns \(0,1,2,3,4\) are \(0,4,3,2,1\). The product is again \(x_0 I_5\). For \(a\not\equiv 0\pmod{5}\), a builder that leaves column \(a\)'s \(x_0\) on the diagonal is not this encoding. The label remains `synthetic-ab-x0`. A pass of this encoding is not an authentic \(\mathbb{Q}\) certificate.

Tests of the direct encoding. All three are mandatory.

1. Over \(\mathbb{Q}\), multiply \(A\) by \(B\) and require entrywise equality with \(x_0 I_5\). The arithmetic is exact on the integer coefficients.
2. Over \(\mathbb{F}_3\), reduce those same integer coefficients modulo \(3\) and require the same entrywise equality in \(\mathbb{F}_3[x_0]\).
3. Rejection. Replace the nonzero coefficient \(A_{0,0}=x_0\) by \(2x_0\). Leave every other entry of \(A\) and every entry of \(B\) as in the positive fixture. The \((0,0)\) entry of the product is \(2x_0\). Over \(\mathbb{Q}\), \(2x_0\neq x_0\). Over \(\mathbb{F}_3\), \(2\not\equiv 1\). The checker must reject the mutated pair on both fields. A checker that accepts it fails the control.

Column \(0\) sits at row \(0\) in both encodings, because \(-0\equiv 0\pmod{5}\). When the grading-builder path runs, it repeats the same three tests on its own matrices, with the same mutated coefficient \(A_{0,0}=2x_0\).

Required report for the direct encoding:

```
control: synthetic-ab-x0
encoding: direct
field_QQ: pass
field_F3: pass
mutant_coefficient: A[0,0] = 2 x0
mutant_rejected: yes
authentic_QQ_certificate: no
```

When the grading-builder path runs, the same report is emitted with `encoding: grading-builder`. Any other product, any accepted mutant, or a report that sets `authentic_QQ_certificate` to yes, fails the run.

Source: pull request 78, comment 6131776264. The exact encoding and the three tests are part of this bounded contract.

## Search policy and algebraic reuse

This section amends the reuse rules already recorded from pull request 76, comment 6131466767, and the acceptance in comment 6131487929. The one-chart transport is comment 6131224687. The \(\tau\)-grading and block shapes are comments 6131271739, 6131301416, and 6131302250. These rules are not a witness, and they do not authorize a search from this document. The byte, memory, and wall-clock figures they refer to are the proposals in §6, not an execution release.

### One-chart cyclic transport

\(G=\varphi_0\), the pinned \(15\times 5\) matrix. The symbols \(x_0,\ldots,x_4\) of §2 are the homogeneous coordinates. On the standard chart they are written \(v_0,\ldots,v_4\), with the same index order, so \(v_k=x_k\).

Only \(B_0\) is searched. It is a \(15\times 5\) matrix of homogeneous forms of degree \(N-1\) satisfying

\[
G(v)^{\mathsf T} B_0(v)=v_0^{N} I_5.
\]

Define \(\sigma\) on the basis by \(\sigma(e_j)=e_{j+1}\), indices modulo \(5\). On coordinate tuples that action is the right cyclic shift

\[
\sigma(v_0,\ldots,v_4)=(v_4,v_0,v_1,v_2,v_3).
\]

The tuple \((v_1,\ldots,v_4,v_0)\) is \(\sigma^{-1}\) and is not the definition of \(\sigma\). Define \(C\) and \(R\) by the same \(+1\) shift of basis labels. \(C\) sends source basis vector \(j\) to source basis vector \(j+1\). \(R\) acts separately inside each of the three blocks of five and sends the basis vector of index \(j\) in that block to the basis vector of index \(j+1\). Consequently

\[
\sigma^{-i}v=(v_i,v_{i+1},v_{i+2},v_{i+3},v_{i+4}).
\]

Set

\[
B_i(v)=R^{i} B_0(\sigma^{-i}v)\,C^{-i}.
\]

The entrywise formula is unchanged. Indices are modulo \(5\):

\[
B_i[5b+t,\,a](v)=B_0[5b+(t-i),\,a-i](v_i,v_{i+1},v_{i+2},v_{i+3},v_{i+4}).
\]

The two displays agree. The argument of \(B_0\) is \(\sigma^{-i}v\), and \(R^{i}(\,\cdot\,)C^{-i}\) carries the entry at row \(t-i\), column \(a-i\) to row \(t\), column \(a\).

Covariance, and every transported product, must be checked. For each \(i=0,\ldots,4\),

\[
G(v)=R^{i} G(\sigma^{-i}v)\,C^{-i}.
\]

\(R\) and \(C\) are permutation matrices, so \(C^{-1}=C^{\mathsf T}\) and \((C^{-i})^{\mathsf T}=C^{i}\). A pass of the covariance identity, together with \(G(w)^{\mathsf T} B_0(w)=w_0^{N} I_5\) at \(w=\sigma^{-i}v\), yields

\[
G(v)^{\mathsf T} B_i(v)=C^{i}\bigl(G(w)^{\mathsf T} B_0(w)\bigr)C^{-i}=w_0^{N} I_5=v_i^{N} I_5,
\]

because the zeroth coordinate of \(\sigma^{-i}v\) is \(v_i\).

The four matrices \(B_1,\ldots,B_4\) are this cyclic index shift. They are not searched. Covariance is replayed as a precondition on the authenticated \(G\). Each of the five products, including the product for \(B_0\), is then replayed by exact multiplication against that \(G\) and against its own named right-hand side \(v_i^{N} I_5\). A match to some other \(v_j^{N} I_5\), or a match only as a set of five right-hand sides, fails the named-transport contract. Transport does not replace those five multiplications.

Sources for the shift: pull request 78, comments 6131776264 and 6131777532.

Named-chart check and geometric coverage are different oracles. Since \(v_k=x_k\), the monomials \(v_i^{N}\) and \(x_i^{N}\) name the same chart.

The transport contract uses the named check. Chart \(i\) passes that contract only when the replay equals the named right-hand side \(v_i^{N} I_5\). A permutation of \(\{v_0^{N} I_5,\ldots,v_4^{N} I_5\}\) fails the contract. Covariance remains a precondition of the contract.

The coverage oracle is the geometric conclusion. Five authenticated identities whose right-hand sides are a permutation of

\[
\{x_0^{N} I_5,\ldots,x_4^{N} I_5\}
\]

still prove that every standard chart carries a unit multiple of \(I_5\), after the charts are relabeled by that permutation. The oracle is this set equality. It does not repair a failed named-transport check, and a failed named-transport check does not by itself refute the geometric conclusion.

Accepting “some \(x_j^{N} I_5\)” on each chart, without the five indices exhausting \(\{0,1,2,3,4\}\), fails both oracles. A repeated index and a missing index are neither coverage nor the named contract.

Sources for the split: pull request 78, comments 6131895075 and 6131921721.

The search count is five columns of \(B_0\). Without the transport there would be \(25\) chart-column problems, five charts times five columns. The count is not \(15\). This job does not budget the \(25\)-problem search, and it does not budget a separate \(8\times 15\) chart reduction for \(\varphi_1\).

### Five \(\tau\)-graded blocks

Give \(v_k\) weight \(k\bmod 5\). Then \(\mathrm{wt}(v_0)=0\). For exponent \(N\) write

\[
s=\binom{N+3}{4},\qquad t=\binom{N+4}{4}.
\]

These count monomials of degree \(N-1\) and \(N\) in five variables. Label a row \((a,\beta)\) by \(\mathrm{wt}(\beta)+2a\) and a column \((r,\alpha)\) by \(\mathrm{wt}(\alpha)-2(r\bmod 5)\). The coefficient matrix of \(B_0\) splits into five blocks, one block for each column, each of shape \(t\times 3s\) with \(5s\) initial nonzeros. The right-hand side of column \(j\) occupies only the block whose label is \(2j\bmod 5\). Solve those five blocks, one right-hand side each. Do not flatten them into one \(5t\times 15s\) system, and do not assume one factorization serves all five blocks.

At the proposed cap \(N=7\), \(s=210\) and \(t=330\), so each block is \(330\times 630\) with \(1050\) initial nonzeros.

### Solver, order, pivots, failure

The solver is deterministic Gaussian elimination over \(\mathrm{GF}(3)\). No random pivot, no probabilistic rank, and no Gröbner basis.

Monomials are listed in graded reverse lexicographic order (grevlex) with

\[
x_0>x_1>x_2>x_3>x_4
\]

(equivalently \(v_0>\cdots>v_4\)). Total degree decides first. For equal degree, the first exponent difference read from \(x_4\) back toward \(x_0\) decides, and the monomial with the smaller exponent there is larger. Inside a block, unknown columns are ordered by that order on the monomial, then by increasing row index \(r\). Equation rows are ordered by the same order on the monomial, then by increasing equation index \(a\).

Pivot rule, fixed: at each step, among columns that still contain a nonzero in the remaining rows, take the least column index; among nonzero entries in that column, take the least row index. Scale that pivot to \(1\) in \(\mathrm{GF}(3)\) (the inverse of \(2\) is \(2\)). Eliminate. The rule does not use a Markowitz score.

Free variables are set to \(0\). After the pivots above, every unknown that was not selected as a pivot is assigned \(0\) in \(\mathrm{GF}(3)\), and back-substitution determines the pivot unknowns. The recorded column is that particular solution. No other particular solution is emitted.

The exact dual is recovered from the same elimination. The process stores the accumulated left multiplier \(E\in\mathrm{GL}_t(\mathrm{GF}(3))\), initially \(I_t\), and updates \(E\) by each row operation applied to the augmented block. On inconsistency, some row of \(E[A\mid b]\) equals \((0\mid c)\) with \(c\neq 0\). That row of \(E\), scaled by \(c^{-1}\) in \(\mathrm{GF}(3)\), is the dual column \(y\), and the scaling enforces \(y^{\mathsf T} b=1\). The certificate check is exact multiplication: \(y^{\mathsf T} A=0\) and \(y^{\mathsf T} b\neq 0\).

A nonzero coefficient whose \(\tau\)-label is not the label of the block being solved is a failed assertion. The process exits \(1\). The coefficient is not dropped, and the solve does not continue on the block with that coefficient removed.

Failure:

- If the block is inconsistent, emit the dual column \(y\) recovered above. That dual excludes the column at the exponent where it was found and, by multiplication by a power of \(v_0\), at every smaller exponent. It does not exclude a larger exponent, it does not exclude another column, and it does not supply a geometric bad point. On the ladder the process records the dual and continues at the next exponent for that column. Exit \(3\) is used only when a dual at the cap \(N=7\) leaves no common witness at any exponent \(\le 7\).
- If a proposed cap in §6 is hit before the elimination finishes, the status is `inconclusive` and the process exits \(2\). No dual is emitted on a cap, and a cap is not a bounded-degree negative.

### Fill-in

Cancellation over a finite field defeats a pattern-only prediction of fill-in. The contract therefore uses the dense ceiling of the augmented block: \(t\times(3s+1)\) entries. At \(N=7\) that ceiling is \(330\times 631=208230\) entries of \(\mathrm{GF}(3)\) per block, for any pivot order, including the order fixed above. The solve holds one augmented block at a time. Public context for why a sparsity pattern is not the bound: Bouillaguet–Zimmermann, parallel structured Gaussian elimination, and Dumas–Villard, sparse rank over \(\mathrm{GF}(p)\). The \(208230\)-entry figure is the ceiling of that one augmented block. It is not the whole working set.

The ceiling excludes dual row-operation tracking, monomial indexes, and runtime overhead. Representation is fixed as follows. A coefficient of \(\mathrm{GF}(3)\) is one byte in \(\{0,1,2\}\), the encoding of §6.2. The augmented block is one dense row-major array of \(t(3s+1)\) such bytes: \(208230\) entries at \(N=7\). Dual row-operation tracking is the left multiplier \(E\) of the solver section, a second dense array of shape \(t\times t\) in the same one-byte encoding. At \(N=7\), \(t=330\) and \(t^2=108900\), so \(E\) holds up to \(108900\) coefficients. \(E\) is a working array of the solve. It is not a retained artifact and it is not added to the byte ledger of §6.2. Monomials are addressed by the grevlex rank fixed in the solver section. Exponent vectors are not stored beside the block. An explicit monomial index, if a later runner builds one, lies outside the \(208230\) count. Runtime overhead, including allocator state and the one replay product in hand, likewise lies outside that count.

The enforceable bounds on the augmented block, on \(E\), on any monomial index, and on runtime overhead are the whole-process controls of §6.3: wall-clock time \(600\) seconds and resident set \(1\) GiB, measured on the process. Crossing either limit is exit \(2\).

Source for the exclusion and the representation: pull request 78, comment 6131776264.

### Certified columns and the degree schedule

1. A chart witness at exponent \(N\) is equivalent to \(v_0^N M=0\), with \(M=\mathrm{coker}(G^{\mathsf T})\) and standard generators \(\bar e_j\). Define \(N_j=\min\{N:v_0^N\bar e_j=0\}\), allowing \(\infty\). The common threshold is \(\max_j N_j\). There is no finite witness if any \(N_j=\infty\).

2. Once column \(b_j\) is certified by \(G^{\mathsf T} b_j=v_0^n e_j\), every later exponent \(N\ge n\) uses \(v_0^{N-n} b_j\). That column is not solved again. Because \(\mathrm{wt}(v_0)=0\), the lift stays inside its \(t\times 3s\) block. Assemble only at the maximum successful exponent, and only after all five columns are certified or lifted to that same exponent, and only before the five chart multiplications.

3. A completed inconsistent dual for one column at \(N\) excludes the common witness for every exponent \(\le N\) for that column. It does not invalidate an already certified other column.

4. The degree schedule is the increasing ladder \(N=1,2,3,4,5,6,7\), inside the degree proposal of §6. Finding any witness does not use a binary search for the minimal exponent. Binary refinement is used only if a minimum-degree claim is itself required, which this job does not require.

Dense Gaussian elimination on one augmented block costs on the order of \(\min(t,3s)^2\cdot\max(t,3s)/2\) field operations. Five blocks, summed over the ladder, come to about \(2.23\times 10^8\) field operations if every block is factored at every degree. The doubling schedule \(N=1,2,4\) and then the cap \(N=7\), which is the doubling schedule that stays inside the cap, comes to about \(1.73\times 10^8\) field operations on the same model. This estimate is about \(1.29\times\) smaller for the displayed doubling schedule, while certified-column reuse means it need not be better in an actual run. No new cost experiment is part of this contract. The ladder is the schedule because a column that certifies at a small \(n\) is lifted rather than refactored, and a dual at \(N\) is available before the next degree is built. A timeout or a cap remains `inconclusive`, not empty, and not a geometric bad point.

Source for the wording of the comparison: pull request 78, comment 6131776264.

The primary graded test and its exact dual are the only oracles that may emit a bounded-degree negative. A minor-membership computation is not this schedule.

## 6. Resource proposals

The figures in this section are proposals. They are not an execution release, not a Nullstellensatz degree theorem, and not a license to launch. Review may tighten them. No launch proceeds under this document.

There is no per-chart time budget and no independent-chart search budget. The \(2\cdot 10^6\)-byte witness allowance is withdrawn. It is not replaced by any draw on the protected failure reserve.

### 6.1 Degree proposal

Each searched entry of \(B_0\) is homogeneous of degree \(N-1\), and the schedule of the search-policy section uses only \(1\le N\le 7\). At \(N=7\) the total degree is \(6\). The transported matrices \(B_1,\ldots,B_4\) have the same degree. This proposal does not include an exponent above \(7\), and it does not include a minor-membership search. The minor-membership form in §2.1 remains an accepted certificate when a matrix of that form is multiplied; it is not a search this job runs.

### 6.2 Byte proposal, drawn from the unallocated \(294117\) bytes

Pull request 78, comment 6131521254, records the ledger figure used here: \(294117\) bytes were unallocated, and the protected failure reserve stays untouched. Every line of the checked table is drawn from those \(294117\) bytes. Nothing is drawn from the reserve. A line that would overflow that pool is a cap hit: exit \(2\), with no transfer from the reserve. The remainder after the checked table is the only pool for the source, header, manifest, and zero-write account that follows it.

The reference encoding of a \(\mathrm{GF}(3)\) coefficient is one byte in \(\{0,1,2\}\). Monomials are implicit in the grevlex order of the search-policy section and are not stored. Artifact caps below are byte caps on that encoding.

| Item | Accounting | Bytes |
|---|---|---|
| Retained copy of the verifier blob `fa5231de92b61143e3406111d4af028284db6d55` | file size of that blob | \(11565\) |
| Retained copy of the prose-model blob `fad0e87f0e30ec916e18fd47feea584c7d8eaae6` | file size of that blob | \(9115\) |
| Run log, including the assembly list, the column index, and the certificate type of every receipt | text cap | \(32768\) |
| The \(B_0\) witness | \(15\times 5\) entries, degree \(N-1\), so \(75\cdot s\) coefficients. At \(N=7\), \(s=210\) and \(75\cdot s=15750\) | \(15750\) |
| Dual witnesses | at most one per column of \(B_0\), kept at the largest inconsistent exponent for that column; each has \(t\) coefficients. At \(N=7\), five duals are \(5\times 330\) | \(1650\) |
| Per-replay receipts | five receipts, \(512\) bytes each: chart index, exponent, certificate type `matrix-column`, and pass or fail. Not the product | \(2560\) |
| Failure receipts | text cap for a failed composition, a failed control, or a failed assertion | \(8192\) |
| Total drawn | sum of the lines above | \(81600\) |
| Left unallocated | \(294117-81600\) | \(212517\) |
| Protected failure reserve | not a source and not a destination | \(0\) drawn |

The products of the five replays are \(25\cdot t\) coefficients each (\(8250\) coefficients at \(N=7\)). Readers recompute them by multiplication. They are not stored. The transported matrices \(B_1,\ldots,B_4\) are the cyclic index shift of \(B_0\). They are not stored. A column certified at exponent \(n<7\) is stored at degree \(n-1\); the byte line above is the cap, which is the \(N=7\) size.

The checked figures in the table stay as written: the pinned inputs are \(11565\) and \(9115\) bytes, the listed total is \(81600\), and the remainder from the \(294117\) unallocated pool is \(212517\). Those lines are not recomputed here.

The \(212517\) bytes are the only pool for the categories omitted from the table. They are not drawn from the protected failure reserve, and they do not increase the checked total \(81600\).

| Item | Treatment | Bytes |
|---|---|---|
| Runner source | measured file size, drawn from the \(212517\) | measured |
| Verifier source | measured file size, drawn from the \(212517\) | measured |
| Test source | measured file size, drawn from the \(212517\) | measured |
| Headers and manifests | measured file size, drawn from the \(212517\) | measured |
| Temporary files | zero-write: not retained in the artifact store | \(0\) |
| Cache files | zero-write: not retained in the artifact store | \(0\) |

Zero-write means the process does not keep temporary or cache files. Each of those two lines is present, at charge \(0\), so the category is not omitted. A temporary or cache file that is retained fails the zero-write rule and the run exits \(1\). Its measured size is still drawn from the \(212517\), so a retained file is not an uncounted write. The sum of the measured source, header, and manifest sizes, together with any such retained bytes, must be at most \(212517\). A larger sum is a cap hit: exit \(2\), with no transfer from the reserve. Bytes of the \(212517\) that these lines do not consume stay unallocated.

Source for the checked figures and for this remainder account: pull request 78, comment 6131776264.

### 6.3 Memory and wall-clock proposals

Both limits cover construction of the pinned matrices, the controls in §5.1–§5.4, the graded solves, and all five replay multiplications. The synthetic checker control of §5.4 is inside this clock and inside this resident-set account. A fresh rational search is outside both.

| Proposal | Limit |
|---|---|
| Whole-job wall-clock time | \(600\) seconds |
| Resident set | \(1\) GiB |

The solve holds one augmented block at a time. Its dense ceiling at \(N=7\) is \(208230\) entries, which excludes the dual tracker of up to \(108900\) coefficients, monomial indexes, and runtime overhead (search-policy section). Those arrays, that overhead, and the five replay products computed one at a time sit inside the \(1\) GiB proposal. The \(600\)-second limit and the \(1\) GiB limit are whole-process controls: both are measured on the process, and crossing either one is exit \(2\). There is no separate per-chart clock.

Hitting either limit, including a timeout, yields status `inconclusive`. That status is not a zero, not a non-membership, and not a nonempty locus. The process must not exit \(0\) on a cap.

Exits, still proposals:

- \(0\) only when the compositions of §1.3, the controls of §5.1–§5.4, and a multiplied positive certificate all hold;
- \(1\) on a failed assertion, including a failed control;
- \(2\) on inconclusive (cap, timeout, or an elimination that did not finish);
- \(3\) when a completed exact dual at the degree cap is recorded. That exit is a bounded-degree negative. It is not exit \(0\) and it is not exit \(2\). It makes no geometric claim. See §7.

### 6.4 Out of scope

In scope for a later launch, if one is separately released, is only: the composition identities of §1.3, the controls of §5.1–§5.4, the graded solve in the search-policy section, and the five replay multiplications. The control in §5.4 is the synthetic checker fixture `synthetic-ab-x0`.

Out of scope for this job:

- a \(\mathbb{Z}\)-saturation;
- an integral bad-prime diagnostic;
- a reduction modulo any prime other than the coefficient prime \(3\);
- a fresh rational search;
- a rational reconstruction used as a search;
- reading a pass of `synthetic-ab-x0` as an authentic certificate over \(\mathbb{Q}\).

The synthetic replay of §5.4 is inside the wall-clock and resident-set proposals above. A fresh rational search is not, and the fixture does not release one.

## 7. What success means

Success is a future run, not this document. It means all of the following, and nothing further.

A degree-cap negative, including a completed exact dual at the proposed cap \(N=7\), supplies no geometric bad point. A timeout or any other cap hit supplies none either. Only an exact positive witness closes the fiber-rank gate: the five multiplied identities \(G^{\mathsf T} B_i=x_i^{N_i} I_5\), or a minor-membership certificate that has actually been multiplied, including the adjugate matrix of §2.1. Those named identities are the transport contract of the search-policy section. A minor-membership negative does not close the gate and does not refute the matrix witness. A pass of the synthetic fixture `synthetic-ab-x0` in §5.4 does not close the gate.

Geometric coverage is the separate oracle in that same section. Five authenticated identities whose right-hand sides are a permutation of \(\{x_0^{N} I_5,\ldots,x_4^{N} I_5\}\) prove that every standard chart splits, after relabeling. That coverage does not satisfy the named-transport contract. Accepting an unspecified \(x_j^{N} I_5\) on each chart, without the indices exhausting \(\{0,1,2,3,4\}\), proves neither the contract nor the coverage.

Over an algebraic closure of \(\mathbb{F}_3\), the authentic pinned maps have fiber ranks \((5,8,2)\) at every \(v\neq 0\), read from a multiplied rank-\(5\) certificate for \(\varphi_0\), the identity of §4, and the evaluation matrix of \(\varphi_2\).

\(C\otimes\mathbb{F}_3\) then has fibers \((0,2,0,0)\). It resolves a rank-\(2\) sheaf \(H\): the cohomology is that rank-\(2\) sheaf in the middle slot, and the other three cohomologies vanish. Local splitting is the unit-minor splitting of §3 together with constant rank, not a sum of global matrix ranks.

Only after that resolution statement do the \(\mathrm{End}(C)(-2)\) groups computed at `80ea7e98a09ef6c3f10285cb6d0eedc8bc7f979c` become \(\mathrm{Ext}^*(H,H(-2))\) over \(\mathbb{F}_3\).

Success does not transfer a characteristic-\(0\) ambient obstruction. It does not establish choice independence of the pin. It does not produce an obstruction value.

## 8. FMEA

| Failure mode | Effect | Detection | Mitigation |
|---|---|---|---|
| Pinned-map drift | A witness for a different complex is reported as a certificate for \(C\). | Rebuild \(\varphi_0,\varphi_1,\varphi_2\) from §1.2 and compare the sparse term list with blob `fa5231de92b61143e3406111d4af028284db6d55` before any search. | Abort on the first differing term. Do not search. |
| Basis drift against `fa5231de` | A correct multiplier for a permuted \(U,V,Z\) order or a flipped \(\varepsilon\) is accepted. | Entrywise match to the sign formula and the row order in §1.2, not merely vanishing of the two compositions. | Compositions are necessary and not sufficient. Fail closed on any basis mismatch with the blob. |
| Vacuous identity oracle | A checker that never sees a rank drop prints \(\mathrm{rank}\,\varphi_1=8\) for the authentic maps without testing the identity. | The pointwise control of §5.3 returns \(\mathrm{rank}\,\gamma'(p_*)=1\) and restricted-contraction rank \(4\), with \(4=3+1<8\), from an independent \(E'\) and the reconstruction \(E'g'=\gamma'(p_*)\). | The control is mandatory, ambient, and pointwise at \(p_*\). It is not a second complex. An oracle that only accepts \((5,8)\) fails. |
| Authentic \(U,V,Z\) basis used for \(\ker b'\) | The paired control is evaluated in the wrong \(15\)-plane. | The unit minor on \(U_3,V_1,-V_4,-U_2,U_1\) is \(I_5\), so \(\dim(W\cap\ker b')=10\) over every field, including \(\mathbb{F}_3\). Also \(U_0\) and \(U_4\) lie in \(\ker b'\), while \(b'(U_1)_4=1\) and \(b'(U_3)_0=1\). At \(p_*\), \(b'\gamma'_4=0\) and \(b\gamma'_4=-e_4\), and \([W\mid\gamma'_4]\) has rank \(16\). | Require \(b'E'=0\), \(\mathrm{rank}(E')=15\), and the ambient equality \(E'g'=\gamma'(p_*)\). A ker-membership flag alone fails. The authentic list is not reused. |
| Named-transport contract | A product is accepted under the wrong chart name, or a permutation of correct right-hand sides is accepted as the transport. | Covariance \(G(v)=R^{i} G(\sigma^{-i}v)\,C^{-i}\) fails for some \(i\), or the replay for index \(i\) is not the named \(v_i^{N} I_5\). | Keep the named-chart check. Chart \(i\) passes only against \(v_i^{N} I_5\). Use \(\sigma(e_j)=e_{j+1}\). A permutation fails this row even when the coverage oracle passes. Transport does not replace the multiplications. |
| Geometric chart coverage | A missing chart is reported as projective coverage, or a named-transport failure is reported as a geometric failure. | The set of authenticated right-hand sides is not \(\{x_0^{N} I_5,\ldots,x_4^{N} I_5\}\), or a complete permutation is logged as a geometric negative. | The coverage oracle is that set equality. A permutation proves coverage after relabeling and does not prove the named-transport contract. Accepting “some \(x_j^{N} I_5\)” on each chart, without the indices exhausting \(\{0,1,2,3,4\}\), fails this oracle and fails the named contract. |
| Nonzero free variable in a recorded column | A later lift differs from the column the elimination selected. | A stored unknown that was not a pivot is nonzero. | Set every free variable to \(0\) before back-substitution. Emit only that particular solution. |
| Cross-grade coefficient dropped | A block is solved after a term from another \(\tau\)-label has been discarded. | A nonzero coefficient whose label is not the block label is absent from the failure log. | Exit \(1\). Do not drop the coefficient. |
| Degree-capped minor-membership negative read as a matrix-witness negative | A false fiber-rank kill. | The only negative on record has certificate type `minor-membership`. | Tag every receipt `matrix-column`, `minor-membership`, or `dual`. Only the primary graded test and its exact dual may emit a bounded-degree negative. A minor positive at exponent \(e\), once the adjugate matrix is multiplied, is a matrix positive at \(N=e\). |
| `assert` stripped by `PYTHONOPTIMIZE` | A later Python runner loses its predicates under `python -O` or `PYTHONOPTIMIZE` set, and exits \(0\). | Launch refuses to start unless `sys.flags.optimize==0` and `PYTHONOPTIMIZE` is unset. | Certificate predicates raise. Bare `assert` is not on the proof path. This document has no runner; the row binds any later one. |
| Claim inflation to \(\mathrm{End}(H)/O_2\) | Fiber ranks are reported as an \(\mathrm{End}(H)\) calculation, as \(\mathrm{Ext}\) groups before the resolution hypothesis, or as an obstruction value \(O_2\). | The result banner is restricted to the sentences in §7. A file that states an obstruction value, a characteristic-\(0\) transfer, or choice independence is a failed run. | The conditional identification with \(\mathrm{Ext}^*(H,H(-2))\) is allowed only after the resolution statement, and it is not an obstruction computation. |
| Assemble before every column is at the same \(N\) | A partial maximum is published as a common chart witness. | The assembly log lists a column that is not certified or lifted to that \(N\). | Assemble only after all five columns of \(B_0\) are certified or lifted to the same \(N\). Without transport the count would be \(25\) chart-column problems; that search is not this job, and the count is not \(15\). |
| Re-solve of a certified column | Wasted cost, and a risk of basis drift against the stored column. | A column index that already has a stored \((b_j,n)\) is submitted to a new solve. | Refuse the re-solve. Store \((b_j,n)\) and lift by \(v_0^{N-n}\). |
| Dual kill read across columns | An inconsistent dual for one right-hand side aborts certified columns of other indices. | The dual log does not name a single column index. | Dual kill is per right-hand side. The log names the column index. |
| Degree doubling without a cost model | A timeout or a cap is read as emptiness. | The degree schedule has no operation-count comparison. | The search-policy section fixes the ladder \(N=1,\ldots,7\). The displayed doubling estimate is about \(1.29\times\) smaller and need not be better once certified columns are reused. A cap remains `inconclusive`. No new cost experiment. |
| Independent-chart search, or a separate \(\varphi_1\) chart reduction, run inside this job | A second search path spends the proposals of §6. | The log lists more than the five columns of \(B_0\), or an \(8\times 15\) reduction. | Refuse. This job searches five blocks of \(B_0\), transports, and replays five multiplications. |

## 9. Stop

This pull request is the design. Witness construction does not start here. The \(B_i\) are not built. No Gröbner basis, Macaulay2 session, or other computer-algebra search is part of the deliverable.

Review is requested on the pointwise paired control, the module \(M\) without a slash quotient, the exponent comparison of the two certificate forms, the amended search policy, the resource proposals, and the synthetic checker control in §5.4. Stop after that review request. Witness construction remains unstarted. The proposals in §6 do not release a launch.
