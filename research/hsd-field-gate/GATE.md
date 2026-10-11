# Field-validity gate for C0

High School Diploma. Text-only review of the pre-output contract for the residue-41 section of source23615 / module133174.

Pinned object: draft #64, commit `232cf11c2ca2a8cbaf315040aa0e4ae72c703d8e`, directory `research/hm/source23615-c0`. The seven files are `C0.md`, `source-definition.json`, `manifest.json`, `SHA256SUMS`, `INTEGRATION_CHECK.md`, `integration-check.json`, and `README.md`.

This note reads those files and the gate agreed on #1 (comments 6109977065, 6109991337, 6109995682, 6110080818). It evaluates no coefficient of the residue-41 section and builds no detector at another prime. Factorials, Segre classes, and Todd classes were analogies in an earlier draft of the gate; those words do not occur in the seven files, and this note does not use them as denominators.

**(a) does not imply (b).** An ordinary rational or integral expression can be pinned while every cross-prime transform remains unproved. Arithmetic in characteristic 3 is compatible with that pin. This gate treats the source as supplied to the extent the contract pins it.

## G1. Common source, split

### (a) The ordinary expression and its F3 section — pinned

(a) holds.

The ordinary source is the polynomial \(s_{23615}\) in the coordinates \((x_1,x_2,x_3,x_4)\). The ambient ring is the Laurent ring \(\mathbb{F}_3[x_1^{\pm 1},x_2^{\pm 1},x_3^{\pm 1},x_4^{\pm 1}]\). The contract states that this source is polynomial. "Ordinary" here means the source-coordinate polynomial, as opposed to the descended component \(Q(y)\).

The expression is pinned in three layers.

1. Sixteen tag polynomials, indices \(j<16\), are written in full in `source-definition.json` under `tagPolynomials`, in the order \(X_1,X_2,X_3,X_4,L_1,L_2,L_3,L_4,V_1,V_2,V_3,F_0,F_1,F_2,F_3,F_4\). Each coefficient is a base-10 integer string. The symbol \(F_3\) in that list is a polynomial tag. The coefficient field \(\mathbb{F}_3\) is a different object; `C0.md` §1 says so.
2. The recurrence for \(j\ge 16\) is
   \[
   s_j=\sum_{\mathrm{rows}}\frac{n}{d}\prod_{(k,e)} s_k^e,
   \]
   with the rational syntax \((n,d)\) reduced by \((n \bmod 3)\,(d \bmod 3)^{-1}\) after the check that \(d\bmod 3\neq 0\). The four rows \(s_{22954}\), \(s_{23283}\), \(s_{23543}\), and \(s_{23615}\) are written out, in `C0.md` §1 and again as `displayedSourceRows`. Every displayed numerator string is `1` or `2`, and every displayed denominator string is `1`.
3. Every remaining sum-node is pinned by the normalized-source digest `8067c59cd141b44741156bd5ac5d0ac2d7055177b6aee43ea9a09f1b600176fc`, the artifact `all-assignments.normalized.json`. The contract says those bytes fix every coefficient, factor, exponent, and earlier source reference, and that \(s_{23615}\) is that particular polynomial.

The \(\mathbb{F}_3\) section is pinned as a mathematical object, with no coefficient values filled in. For \(r=(2,1,1,1)\),

\[
Q(y)=C_r(s_{23615})(y),\qquad P_r(s_{23615})(x)=x^r Q(x_1^3,x_2^3,x_3^3,x_4^3).
\]

The code of \(r\) is \(2+3\cdot 1+9\cdot 1+27\cdot 1=41\), with \(x_1\) the least-significant digit and digits in \(\{0,1,2\}\). Read as a base-3 integer with \(x_4\) most significant, the same digits are \(1112_3\). The code is that encoding. Completeness means the full coefficient maps, absent terms included as zero. One component is requested. The contract imposes no 24-array shape, no 81-output shape, and no symmetry \(\sigma\).

The seven files display the tags and the four rows. They pin the rest of the expression by digest. They do not transcribe the transitive source DAG. That is a distribution boundary on the written expansion. It leaves the pin in (a) in place.

### (b) A cross-prime transform of the same coefficient — not proved here

(b) is not proved here.

No argument in the seven files shows that a transform at another prime returns the residue-41 coefficient. `README.md` states that the identities are specific to characteristic 3 and that no alternate-prime cross-check is claimed. `INTEGRATION_CHECK.md` states the positive requirement for any later prime: a separately valid source specialization, denominator checks, and identities valid in that characteristic. The same paragraph forbids importing \(H(x)^3=H(x^3)\) and the cube-weight pullout unchanged, and records that no such cross-check was performed.

Two steps are essential to characteristic 3, so they have no claim on another prime.

- The ring identity \(H(x)^3=H(x^3)\) for \(H\) with coefficients in \(\mathbb{F}_3\), and the pullout \(C_d(H^3 f)(y)=H(y)\,C_d(f)(y)\) that depends on it.
- The rearrangement \(s_{23615}=A+H^3 K\), which uses \(2\cdot 2=1\) in \(\mathbb{F}_3\). Over \(\mathbb{Z}\), each time that replacement sends a product of two coefficients \(2\) to the field element \(1\), the integral product is congruent to \(1\) modulo \(3\) and the difference is divisible by \(3\). The equality \(s_{23615}=A+H^3 K\) is an equality after reduction to \(\mathbb{F}_3\). Comment 6110289167 clarifies that this simplified equality uses \(2\cdot 2=1\) in \(\mathbb{F}_3\) and implies no cross-prime identification. The identity \(T=H^3 U\) with \(H=s_9 s_{13}\) and \(U=s_{10}^2 s_{14}^2\), by contrast, is a monomial identity and holds over \(\mathbb{Z}\).

The defining recurrence in `C0.md` §1 does not perform the replacement \(2\cdot 2=1\). The ordinary expression pinned in (a) is that recurrence, together with the tags and the normalized digest. The rearranged form is an optional \(\mathbb{F}_3\) identity.

What a result at another prime can support is a statement about a specialization that has been written down separately, with its own denominator check and its own identities. The seven files contain no such specialization. What such a result cannot support is equality with this residue-41 coefficient, sameness of the Cartier transform, or a verification of these carries. There is no canonical integral lift of an \(\mathbb{F}_3\) coefficient array supplied here, and this gate does not invent one.

## G2. Denominators that appear

Only denominator objects that occur in the seven files are listed. The four displayed rows are one of those objects. They are not a sample from which the other rows are inferred. Absence of a denominator, and invertibility of a denominator, are not read off those four rows.

| Object as written | Where it appears | Label |
| --- | --- | --- |
| Denominator string `1`, the second entry of every pair \((n,d)\) in `displayedSourceRows` (the same coefficients appear as the integer multipliers \(1\) and \(2\) in `C0.md` §1) | `source-definition.json`, `C0.md` §1 | Displayed, and checkable from the seven files. \(1\bmod 3=1\neq 0\), so the stated invertibility side condition holds for these pairs. |
| The schematic denominator \(d\) in the rule \((n \bmod 3)\,(d \bmod 3)^{-1}\), side condition \(d\bmod 3\neq 0\), applied to every sum-node | `C0.md` §1, `definitionRule` in `source-definition.json` | The rule is checkable as text. The pairs \((n,d)\) for sum-nodes other than the four displayed rows are not in the seven files. They sit in the omitted normalized source, inside the transitive DAG. Label: referenced, carried by the omitted dependency artifacts, and not determinable here. |
| Integer coefficient strings on the sixteen tags | `tagPolynomials` | No denominator slot is written. These strings are numerators (integer coefficients), so they are not entered in this table as denominators. The tags themselves are fully present and checkable. |
| The exponent quotient \((a+b-d)/3\) in the product formula | `C0.md` §3 | The Euclidean exponent quotient/carry. Comment 6110289167 clarifies that this is the carry in the rank-\(81\) free decomposition over the cube-coordinate subring, not a quotient by \(x_i^3-x_i\). The congruence \(a+b\equiv d\pmod{3}\) makes the carry integral. It is not a coefficient denominator, and the formula does not invert \(3\) in \(\mathbb{F}_3\). Listed so that this \(3\) is not mistaken for one. Checkable as text. |
| The words "denominator checks" | `INTEGRATION_CHECK.md`, last paragraph | A requirement placed on any future specialization at another prime. No integer denominator is named. The checks, if they are to cover the whole source, depend on the omitted full source. |

The factors named in the four rows include source indices that are neither tags (\(j<16\)) nor one of those four rows, for example \(s_{37}\), \(s_{2844}\), and \(s_{23117}\). By the recurrence, each such index is a sum-node with its own pairs \((n,d)\). Those pairs live in the omitted normalized artifact `all-assignments.normalized.json`, one of the thirty dependency artifacts, and in the transitive DAG, which these seven files do not contain. The README also excludes the separate initial plan `higher-cone-133174-plan.json`. Hash references identify those artifacts. They do not reproduce them.

Some tag coefficient strings are integers divisible by \(3\). Under the mandated reduction those terms become zero in \(\mathbb{F}_3\). That is numerator reduction. It is not a denominator, and it is not evidence that a denominator fails to invert. The hidden-denominator question for the omitted sum-nodes stays open; see the questions below.

## G3. Three statements, kept apart

### (i) The ring identity \(H(x)^3=H(x^3)\)

For \(H=\sum c_e x^e\) with \(c_e\in\mathbb{F}_3\),

\[
H(x)^3=\sum_e c_e^3\, x^{3e}=H(x^3).
\]

The first step is the freshman's dream: in characteristic 3, \((a+b)^3=a^3+b^3\), so cross terms drop and the cube of a sum is the sum of the cubes. The second step is \(c^3=c\) for every scalar \(c\in\mathbb{F}_3\). That scalar identity is Fermat on the prime field. `C0.md` §3 states the packaged form "In \(\mathbb{F}_3\), \(H(x)^3=H(x^3)\)" and the consequence

\[
C_d(H^3 f)(y)=H(y)\,C_d(f)(y).
\]

The symbol \(H\) is also reused for the specific factor \(H=s_9 s_{13}\). The general identity is what the pullout cites. Both uses are ring operations on polynomials, with the cubed polynomial evaluated as \(H(x^3)\) or, after descent, as the multiplier \(H(y)\).

### (ii) The specified Cartier residue decomposition

Euclidean residues, including for negative exponents. The representative of an exponent vector lies in \(\{0,1,2\}^4\).

\[
\operatorname{encode}(d)=d_1+3d_2+9d_3+27d_4,
\]

\[
P_r f(x)=\sum_{e\equiv r\pmod{3}} f_e x^e,
\qquad
C_r f(y)=\sum_{a\in\mathbb{Z}^4} f_{3a+r}\, y^a.
\]

The reconstruction \(P_r(f)(x)=x^r C_r(f)(x^3)\) is the bijection \(a\mapsto 3a+r\) onto the class of \(r\). The same Euclidean division gives \(f(x)=\sum_d x^d C_d(f)(x^3)\). These two sentences are integral exponent arithmetic. They do not use characteristic 3. Comment 6110289167 clarifies that the word quotient, in the quotient/cube-weight module construction, means this Euclidean exponent quotient/carry. The displayed sum is the rank-\(81\) free decomposition over the cube-coordinate subring. It is not a quotient by \(x_i^3-x_i\).

The product rule is also exponent arithmetic. For residue representatives \(a,b\in\{0,1,2\}^4\),

\[
C_d(fg)(y)=\sum_{a+b\equiv d} y^{(a+b-d)/3}\, C_a(f)(y)\, C_b(g)(y).
\]

The hypothesis \(a+b\equiv d\pmod{3}\) makes the carry an integer vector. For representatives in \(\{0,1,2\}\), the value \(a_i+b_i-d_i\) lies between \(-2\) and \(4\), and the only multiples of \(3\) in that range are \(0\) and \(3\). Each carry coordinate is therefore \(0\) or \(1\). The written product rule does not create a negative exponent in \(y\). The formula does not divide a coefficient by \(3\).

For a factor power \(e=3q+t\) with \(t\) the Euclidean residue in \(\{0,1,2\}\), the contract writes \(s_k^e=(s_k^q)^3 s_k^t\), pushes \(s_k(y)^q\) to the descended side, and sections the product of the \(t\)-powers. Together with linearity of the reduced scalar \(n/d\), this is the cube-weight step. Characteristic 3 enters when \((s_k^q)^3\) is replaced by using (i).

The optional rearrangement sets \(A=s_0 s_1 s_{15} s_{37} s_{23117}\) and builds \(K\) from the four rows so that \(s_{23615}=A+H^3 K\) and \(Q=C_r(A)+H\, C_r(K)\) in characteristic 3. Omitting \(U\) from \(T\), or omitting the final multiplication by \(H\), is declared invalid. The additive check writes the same root with \(U\) left inside the section:

\[
C_r(s_0 s_1 s_{15} s_{37} s_{23117})(y)
+2\, s_9(y)\, s_{13}(y)\, C_r(s_{10}^2 s_{14}^2 s_{23543})(y).
\]

That matches \(C_r(H^3\cdot U\cdot s_{23543})=H(y)\,C_r(U\cdot s_{23543})\), because the exponents on \(s_{10}\) and \(s_{14}\) are \(2\), not a multiple of \(3\). The outside factors \((9,1)\) and \((13,1)\) in `integration-check.json` are the exponent-\(1\) multipliers on the \(y\) side.

### (iii) \(x^3=x\) for point values only

For a point \(\alpha\in\mathbb{F}_3\), the field axiom gives \(\alpha^3=\alpha\). Inside \(\mathbb{F}_3[x_1,x_2,x_3,x_4]\), and inside the Laurent ring, \(x_i^3-x_i\) is a nonzero polynomial. Evaluation at \(\mathbb{F}_3\)-points is the only place (iii) holds.

The seven files do not substitute \(x^3\) by \(x\), and they do not impose \(x^3-x=0\), in either ring. The scalar fact \(c^3=c\) for \(c\in\mathbb{F}_3\) stays inside (i). It licenses no replacement of an indeterminate.

### Grading check on each written reduction

The Cartier grading is the coordinatewise Euclidean residue in \(\{0,1,2\}^4\), packed by `encode`. A single sum of the four exponents modulo \(3\) is coarser: classes with the same digit sum and different coordinates are different codes, and residue 41 is one specific code.

Coordinatewise residue grading alone cannot detect all folding. The legal cube sends an exponent \(e\) to \(3e\), whose class is \(0\). The fold \(x^{3i}\mapsto x^i\) changes that class when \(i\not\equiv 0\pmod{3}\), and that case can move a class-\(0\) monomial into class \(r=(2,1,1,1)\). The same shape of fold need not change the residue. The replacement \(x_1^9\mapsto x_1^3\) preserves residue \(0\) and changes the descended polynomial: descent sends \(x_1^9\) to \(y_1^3\) and \(x_1^3\) to \(y_1\). Exact exponent checks, including the reconstruction \(P_r(f)(x)=x^r C_r(f)(x^3)\), are required in addition to the grading. Arbitrary \(s\) and \(H\) need not each lie in a single residue class. The grading applies termwise, and a polynomial may meet several classes.

| Step in the contract | Exponent written | Class under the coordinatewise grading |
| --- | --- | --- |
| Reduction of a scalar \((n,d)\), and deletion of a zero coefficient | Exponent unchanged | Class unchanged |
| \(P_r\): keep \(e\equiv r\) | Exponent unchanged; other classes are dropped, not moved | The surviving class is \(r\) |
| \(C_r\): \(x^{3a+r}\mapsto y^a\), inverted by \(x^r Q(x^3)\) | Source exponent \(3a+r\) is recovered from \((a,r)\) | Class of \(3a+r\) is \(r\) for every \(a\), including negative \(a\) under Euclidean division |
| (i): \(c\,x^e\mapsto c\,x^{3e}\) | Exponent multiplied by \(3\) | Image class is \(0\). A fold \(3e\mapsto e\) fails this row only when \(e\not\equiv 0\pmod{3}\). When \(e\equiv 0\pmod{3}\), as in \(x_1^9\mapsto x_1^3\), the residue stays \(0\) and this row does not detect the fold |
| Pullout \(C_d(H^3 f)=H(y)\,C_d(f)\) | Each term of the cube lies in class \(0\), so the residue support of \(H^3 f\) equals the residue support of \(f\). \(H\) need not lie in one residue class. The multiplier \(H(y)\) lives in the descended variable | Residue support of the source factor is preserved. The multiplier is \(H(y)\), not \(H(x)\). \(H(y)\) may meet several classes |
| Product carry | On residue components, the class of a product term is the sum of the classes, reduced into the representative \(d\); only the multiple of \(3\) becomes the \(y\)-exponent. The factors need not each lie in one residue class | Output component keeps label \(d\). Storing \(a+b\) as a source exponent would change that label. A residue-preserving change of the \(y\)-exponent need not change the label |
| Split \(e=3q+t\) | Cube of \(s^q\) contributes only class-\(0\) terms; the section is taken on the product of the \(t\)-powers. \(s\) need not lie in one residue class | Residue support of \(s^e\) equals residue support of \(s^t\) |
| Rearrangement via \(2\cdot 2=1\) | No exponent is rewritten; \(T=H^3 U\) collects polynomial powers already present | Classes unchanged. The step is scalar arithmetic in \(\mathbb{F}_3\) |
| Root formula in `INTEGRATION_CHECK.md` | Same pullout: powers \(3\) on \(s_9\) and \(s_{13}\) become multipliers \(s_9(y)\) and \(s_{13}(y)\); powers \(2\) on \(s_{10}\) and \(s_{14}\) stay inside \(C_r\) | Same class accounting as the pullout row |

No row applies (iii) inside the ring.

## G4. Verification obligations

"Decidable from the contract alone" means that a pass or a fail can be settled by reading the seven files, without the omitted artifacts and without a coefficient evaluation.

| Obligation | Settlement from the seven files alone |
| --- | --- |
| A. Source oracle (`C0.md` §5). Derive both complete maps from the ordinary source and the accepted full-source seeds, by separately implemented arithmetic. Intermediate ordinary factors stay complete unless a residue-aware rule is independently proved. A guard stop is an unverified partial boundary. The oracle does not read candidate coefficients. | The obligation is stated. It is not decidable here. The normalized bytes, the sum-nodes beyond the four rows, the seed maps, and the seed-receipt artifacts named in the manifest are omitted. No coefficient map is present to compare. |
| B. Supplied-output replay (`C0.md` §5). On a candidate, check shape, coefficient set \(\{1,2\}\), the bijection \([a,c]\leftrightarrow[3a+r,c]\), counts, and any downstream linear identity. State which source obligations were regenerated. | No candidate is in the package, so no replay verdict exists. The bijection itself is the reconstruction proof in §3, which is readable. Replay of a real candidate is a later obligation. A pass of B is not a pass of A; the contract says this. |
| C. Transport and provenance (`C0.md` §5). Digests, dependency identity, seed receipts, frozen plan, continuation links, target, and schema. | Split. `SHA256SUMS` matches `C0.md`, `source-definition.json`, and `manifest.json`. The supplement hash inside `integration-check.json` matches `INTEGRATION_CHECK.md`. Those internal pins are checkable. Identity of the thirty external artifacts and of the initial plan is not decidable from these files. The flags `verifiedAgainstAcceptedInitialPlan` record prior checks; `README.md` says they are not checks reproduced here. A dependency digest, a journal digest, and a future output digest are three different objects. |
| Representation identity (`C0.md` §3). \(P_r(f)(x)=x^r C_r(f)(x^3)\). | Decidable as a written proof. It shows that the two maps are representations of one section. It does not show that a supplied array equals that section. |
| Rearrangement \(s_{23615}=A+H^3 K\) (`C0.md` §3). | Decidable as an \(\mathbb{F}_3\) identity from the four displayed rows and \(2\cdot 2=1\). It is not an equality of integral polynomials. It does not use the omitted rows. |
| Induction of the cube-weight construction over the whole source DAG (`C0.md` §3). | The inductive step is written. That every omitted node is an acyclic definition of that shape is not decidable here. |
| Mapping module133174 to source23615 against the pinned graph (`C0.md` §3, `INTEGRATION_CHECK.md`). | The factor lists are written in the supplement and in `integration-check.json`, with status `PASS_DEFINITION_ONLY`, `sourceCoefficientsEvaluated` false, and `targetOutputRead` false. Confirming those lists against `first-lazy-module.graph.json` requires the omitted graph. The package contains no checker that reruns the comparison. |
| Output schema `hm-large-connected-cone-component-v1` and the standing flags `completeStageValueKnown` and `wholeBlindPairingKnown` (`C0.md` §4). | The constraints that §4 writes down are readable, including that both flags stay false for this task. The schema document is not one of the seven files, and no output file is present, so a conformance verdict is not decidable here. |
| Synthetic controls (`C0.md` §6): monomials in all 81 codes and in negative exponents, cancellation, coefficient \(2\), cross-residue products, a nonconstant \(H\) with a nontrivial \(U\), full-source seeds against a single-residue substitute, one-at-a-time mutations, stop/resume. | Specifications are readable. Results are not in the package. The fixture artifacts are among the thirty omitted files. The closing sentence of §6 sends the actual input back to obligation A. |
| Denominator side condition on the whole source. | Settled for the four displayed rows, where every \(d\) equals \(1\). Settled for the tags, which have no denominator slot. Open for every other sum-node. |

### The additive root-integration check

The check is `INTEGRATION_CHECK.md` together with `integration-check.json`. It compares the two weighted terms at module133174 with the displayed formula for \(s_{23615}\), then invokes the cube-weight identity.

The structural check neither detects nor certifies producer coefficients. The supplement records that source coefficients were not evaluated and that no target output was read. A wrong coefficient in a later producer is invisible to this check. The status `PASS_DEFINITION_ONLY` is a statement about the written SUM, not about a computed residue-41 map.

It is common-mode with the conventions a producer of this contract must follow.

- The residue operator is the same \(C_r\), with the same code 41. An off-by-one in `encode`, or a swap of which coordinate is least significant, is shared by the formula and by the check. The check does not recompute the code from a second convention.
- The bridge from source powers \(3\) on \(s_9\) and \(s_{13}\) to the multipliers \(s_9(y)\) and \(s_{13}(y)\) is cited as "the cube-weight identity proved in C0". The supplement does not re-derive (i). A wrong shift — pulling \(H^3\) out as \(H(y)^3\), as \(H(x)\), or leaving the cube on the \(y\) side — sits in the text that both the check and the producer use.
- The recurrence coefficients and the flattening of product nodes are the same writing. The manifest records the graph as checked against the accepted initial plan. That plan is omitted. The seven files do not show a second, independent authoring of the factor list.

A digest of an operator set is a different typed object from a digest of a coefficient artifact. The supplement forbids treating those digests as equal. There is no hidden hash comparison that would break the common mode.

So the additive check is genuine evidence about the structural SUM under the contract's own conventions, and it is not an independent detector of those conventions.

## FMEA

Effect means effect on the residue-41 coefficient, the coefficient of the class \(r=(2,1,1,1)\) in \(s_{23615}\) after the mandated \(\mathbb{F}_3\) reduction. No value of that coefficient is computed here.

| Failure mode | Effect on the residue-41 coefficient | Detection |
| --- | --- | --- |
| A sum-node denominator divisible by \(3\) (a hidden factor \(1/3\) in the ordinary expression) | The reduction rule does not apply. The \(\mathbb{F}_3\) section is not the image of that rational expression. Reporting a residue-41 value as if it were that image is a false comparison. | On the four displayed rows, every written denominator is \(1\), and the side condition holds. On the tags, there is no denominator slot. On the remaining sum-nodes the test cannot be run from the seven files. The gate stays open there. Passing the four rows does not close it. |
| Reading an integer tag coefficient divisible by \(3\) as a bad denominator | The term is a numerator. Correct reduction sends it to zero and can delete a monomial from the \(\mathbb{F}_3\) polynomial, including from class \(r\). Treating the zero as an inversion failure rejects a legal reduction, or the converse accepts an illegal one. | Keep numerator reduction and denominator inversion in separate columns. Divisibility by \(3\) of a tag string is visible in `tagPolynomials`. It does not occupy a denominator slot. |
| Folding \(x^{3i}\mapsto x^i\) inside the source ring or the Laurent ring | When \(i\not\equiv 0\pmod{3}\), a class-\(0\) monomial moves to the class of \(i\). Terms enter or leave class \(r\), and the residue-41 coefficient changes with no change in the written scalar. When \(i\equiv 0\pmod{3}\), the residue is unchanged; that case is the next row. | Coordinatewise residue grading rejects this fold only when the residue changes. Grading alone does not detect every fold. Exact exponent reconstruction is required as well. A check of only the sum of coordinates modulo \(3\) misses a move between distinct codes of the same digit sum. |
| Residue-preserving fold (\(x^9\to x^3\)) passes grading check | The fold \(x_1^9\mapsto x_1^3\) preserves coordinatewise residue \(0\) and changes the descended polynomial: descent sends \(x_1^9\) to \(y_1^3\) and \(x_1^3\) to \(y_1\). A residue-41 coefficient read from the folded descent is not the residue-41 coefficient of the unfolded source. | Control: exact exponent reconstruction through the Euclidean quotient \(a\mapsto 3a+r\) and \(P_r(f)(x)=x^r C_r(f)(x^3)\), plus a must-fail fixture that applies \(x^9\mapsto x^3\) to one monomial and is required to be rejected. The fixture is specified and not run in this package. |
| Using (iii) where the text uses (i): replacing \(H(x)^3=H(x^3)\) by \(H(x)^3=H(x)\), or multiplying by \(H(x)\) on the source side | Exponents that should have been multiplied by \(3\) stay put, so class-\(0\) mass is left in other classes, including \(r\). | The written pullout multiplies by \(H(y)\) after descent, and the root formula writes \(s_9(y)\) and \(s_{13}(y)\). A multiplier still carrying the source variable \(x\) fails that reading. |
| Importing the pullout, or \(2\cdot 2=1\), into another characteristic and reading the output as this coefficient | The other prime computes a different element. Agreement or disagreement with a number at that prime says nothing about the residue-41 coefficient. | (b) is unanswered. `INTEGRATION_CHECK.md` forbids the import. This gate runs no such computation. |
| Shared convention error between the additive check and the producer (residue index, digit order, or Cartier shift) | `PASS_DEFINITION_ONLY` still holds, and the producer emits the section of the wrong class or the wrong pullout. The residue-41 coefficient is then the wrong one while the structural check still passes. | The check is independent of output values and common-mode on the convention, as in G4. Detection needs a derivation of `encode(2,1,1,1)=41` and of (i) that does not cite the paragraph the producer implements. The encoding arithmetic is available in §2 as a definition. The pullout proof is the same paragraph the supplement cites, so the supplement does not supply that second derivation. |
| Replacing \(s_{22954}\), or a full-source seed \(s_{22866}\) or \(s_{22874}\), by a single residue section | Product carries from the other 80 classes into class \(r\) are dropped. The residue-41 coefficient changes. | `C0.md` §1 forbids the substitution and requires every residue channel of an accepted full-source seed. The §6 control that rejects a single-residue seed is specified and not run in this package. |
| Omitting \(U\) from \(T\), or omitting the final factor \(H(y)\) | The descended polynomial is multiplied by the wrong element of \(\mathbb{F}_3[y]\). Every surviving coefficient of \(Q\), including residue 41's image, is scaled or shifted by that error. | The symbolic identity records both factors. The §6 control asks for a nonconstant \(H\) and a nontrivial \(U\). It is specified and not run here. The root formula in the supplement keeps both. |
| Sectioning each factor onto \(r\) separately | Cross-residue pairs with \(a+b\equiv r\) and \(a\neq r\) are dropped, so the carry into class \(r\) is lost. | The product formula is the detection. The §6 product fixtures are specified and not run here. |
| Treating an input-manifest digest and an output digest as the same test | A residue-41 map can be accepted or rejected because two hashes of different objects differed or agreed. Coefficient equality is untouched. | `C0.md` §5.C and `INTEGRATION_CHECK.md` assign the two digests different types. The earlier demand that those digests match is withdrawn. |
| A non-Euclidean remainder on a negative exponent | A negative exponent is placed in the wrong class in \(\{0,1,2\}^4\). If the wrong class is \(r\), or the right class was \(r\), the residue-41 coefficient gains or loses that monomial. | The contract requires Euclidean residues. The displayed tags have nonnegative exponents. The product carry on representatives in \(\{0,1,2\}\) has coordinates in \(\{0,1\}\), so that formula is not the source of a negative exponent. A negative source exponent in an omitted node or a seed is the case the rule must handle; whether any such exponent exists is open. |
| Promoting \(A+H^3 K\) from an \(\mathbb{F}_3\) identity to the integral source | Over \(\mathbb{Z}\) the two expressions differ by terms divisible by \(3\). Inside \(\mathbb{F}_3\), after a correct reduction, the section is the same. The damage is to (b): a cross-prime reading of the rearranged form is not a reading of the recurrence. | Keep §1 as the ordinary expression and §3 as an \(\mathbb{F}_3\) identity. The factor \(3\) in the integral difference is numerator content of that difference. It is not a denominator of §1. |

## Questions for null

These are the points on which the seven files do not determine the gate. Everything else above is a reading of the contract as written, except the sentences sourced to comment 6110289167, which record that comment's clarifications and evaluate no coefficient.

1. Denominators beyond the four rows. Does any pair \((n,d)\) in the normalized source `all-assignments.normalized.json`, for a sum-node other than \(s_{22954}\), \(s_{23283}\), \(s_{23543}\), and \(s_{23615}\), have \(3\mid d\)? The displayed pairs all have \(d=1\). This question is about the omitted pairs only.
2. Which expression is ordinary. Please confirm that the pinned ordinary expression is the §1 recurrence (integer tag coefficients, displayed numerators \(1\) and \(2\), denominator \(1\), remaining nodes in the normalized digest), and that \(s_{23615}=A+H^3 K\) is asserted only after reduction to \(\mathbb{F}_3\). If the ordinary expression is the rearranged form over \(\mathbb{Z}\), then (a) pins a different polynomial than the one read here. Comment 6110289167 clarifies that the simplified equality \(A+H^3 K\) uses \(2\cdot 2=1\) in \(\mathbb{F}_3\) and implies no cross-prime identification.
3. What "independently proved" allows the oracle to reuse. May obligation A invoke the cube-weight identity of `C0.md` §3 as a residue-aware rule, or must the oracle build \(C_r\) by Euclidean division on complete ordinary factors and treat the pullout only as a consequence? The phrase does not say independent of which text. The answer decides whether A is common-mode with the additive check.
4. The seed index for source 22866. The integration map sends module 128045 to source 22866. The pinned frontier artifact for that seed is named with 129656 (`ancestor-cone-129656-oracle-frontier-residue-continuation.json`). Is 129656 the cone whose full coefficient map is the accepted seed of \(s_{22866}\), or a different node? The seven files do not identify 129656 with 128045.
5. The receipt for source 22874. `full-source-22866-seed-receipt.json` is labeled as the 22866 audit. Which omitted artifact is the independent full-map receipt for \(s_{22874}\)? The manifest lists the 128874 cone files and does not give them that role name.
6. The output schema. Is `hm-large-connected-cone-component-v1` fixed by a document outside this package, and does that document add constraints beyond `C0.md` §4? The schema body is not among the seven files.
7. The word "quotient" in "quotient/cube-weight module construction". The product formula supports the carry reading \((a+b-d)/3\). Comment 6110289167 clarifies that quotient means the Euclidean exponent quotient/carry: the rank-\(81\) free decomposition over the cube-coordinate subring, not a quotient by \(x_i^3-x_i\). The word "module" is also the receiving module 133174.
8. Negative exponents on the actual input. The displayed tags are polynomials of nonnegative degree. Do any omitted intermediate sources, or the accepted full-source seeds, contain a negative exponent, so that the Euclidean rule is part of the residue-41 input rather than only part of the §6 fixtures?

## Boundary

The thirty dependency artifacts and the initial plan are not in this package. A complete denominator audit and a source regeneration both depend on them. The structural status `PASS_DEFINITION_ONLY` is a claim about an undistributed graph plus the identities written here. Publication of the contract authorizes no execution, asserts no output, and asserts no alternate-prime check.

No coefficient of \(Q\) or of \(P_r(s_{23615})\) was computed for this gate.
