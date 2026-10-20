# Derived reduction detects the ramified character

## Scope and result

This is a universal **synthetic algebra calculation**, not an evaluation of any physical deformation or obstruction. Assume a field `k` with `char(k) ≠ 2`. Put

\[
R=k[[x]],\quad A=R[\varepsilon]/(\varepsilon^2),\qquad
P=Rm\oplus Rn,\quad \varepsilon m=xn,\quad \varepsilon n=0.
\]

The ordinary guard and its character-frame theorem are already proved in [the ramification guard, §§1–4](https://github.com/Akilleez-QA/read-em-and-weep/blob/2c387062518fec4044568fe638760343b87cc25f/research/hm/null-ramification-guard/ramified-descent-0644/RESULT.md), with its [independent review](https://github.com/Akilleez-QA/read-em-and-weep/blob/2c387062518fec4044568fe638760343b87cc25f/research/hm/null-ramification-guard/ramified-descent-0644/REVIEW.md). This extension computes the entire derived comparison and its fiber, rather than republishing the ordinary guard.

**Derived comparison test.** For `Q=A^a⊕P^b`,

\[
\operatorname{Tor}^{A}_0(Q,R)=R^{a+b}\oplus(R/(x))^b,
\qquad
\operatorname{Tor}^{A}_i(Q,R)=(R/(x))^b\quad(i\geq1).
\]

In this class the following are equivalent:

1. `b=0` (no negative inertia character).
2. `Q` is flat over `A`.
3. `Q` is free over `A`.
4. `Tor_i^A(Q,R)=0` for some `i≥1`.
5. Derived reduction commutes with the invariant-cover reduction described below.

Consequently an explicitly compatible derived reduction provides a bounded test for the missing inertia-sensitive module transport. None of these statements asserts that an actual physical module has this synthetic character decomposition.

## 1. Periodic resolution and the whole derived object

Use homological indexing: degree `i` homology of derived tensor is `Tor_i`; a module written `T[i]` is concentrated in homological degree `i`.

The complex

\[
\cdots\xrightarrow{\varepsilon}A\xrightarrow{\varepsilon}A
\xrightarrow{\varepsilon}A\longrightarrow R\longrightarrow0
\]

is a free resolution of `R=A/(ε)`. Indeed every element of `A` is uniquely `r+εs`, so the kernel and image of multiplication by `ε` are both `εA`, and the augmentation has this kernel as well.

Tensoring with `P` gives the bounded-below free `R`-complex

\[
C_P=(\cdots\xrightarrow{N}P\xrightarrow{N}P\xrightarrow{N}P),
\quad N(m)=xn,\quad N(n)=0,
\]

with its rightmost term in degree zero. Since `x` is a nonzerodivisor in `R`,

\[
\ker N=Rn,\qquad\operatorname{im}N=xRn.
\]

Thus

\[
H_0(C_P)=Rm\oplus(R/(x))n,\qquad
H_i(C_P)=(R/(x))n\ (i\ge1).
\]

This identifies the full object in `D(R)`, not only its homology. Write `m_i,n_i` for the basis in degree `i`. The complex is the direct sum of `Rm_0[0]` and the two-term complexes

\[
Rm_{i+1}\xrightarrow{x}Rn_i\qquad(i\ge0),
\]

placed in degrees `i+1,i`. Each two-term complex resolves `R/(x)[i]`. The direct sum is locally finite in every chain degree. Therefore

\[
P\otimes_A^{\mathbf L}R\simeq
R[0]\oplus\bigoplus_{i\ge0}(R/(x))[i]
\quad\text{in }D(R).
\]

In particular `P` is `R`-free but is not `A`-flat, and it has infinite projective dimension over `A`. It becomes free over `A[1/x]`: the generator `m` has `εm=xn`, and `x` is then invertible. All the displayed defects are supported on the branch locus `x=0`.

## 2. The actual synthetic comparison map

Let

\[
B=k[[u]],\quad x=u^2,\quad D=B[s]/(s^2),
\]

and let `G=C₂` act by `u↦−u`, `s↦−s`. Then `D^G=A` with `ε=us`. Let `M=De` have sign linearization `g(e)=−e`. Its invariants are `P`, with `m=ue` and `n=se`.

There is a commutative square of rings

\[
A\longrightarrow D,\qquad R=A/(\varepsilon)\longrightarrow B=D/(s),
\]

and the inclusion of invariants, followed by reduction, gives a natural derived comparison

\[
\alpha_M:(M^G)\otimes_A^{\mathbf L}R
\longrightarrow(M\otimes_D^{\mathbf L}B)^G.
\]

Here `M` is `D`-free, so the target is simply `(Be)^G=R(ue)` in degree zero. Invariants are exact because `2` is invertible. Equivalently, the target is its derived-invariants object, and the augmentation to it defines the same natural map.

On the explicit complex `C_P`, this map sends `m_0↦ue`, `n_0↦0`, and all positive chain degrees to zero. It is a chain map because `N(P)⊆Rn`. Under the direct-sum description above,

\[
\alpha_M:R[0]\oplus\bigoplus_{i\ge0}(R/(x))[i]\longrightarrow R[0]
\]

is projection onto the first summand. Hence its homotopy fiber is

\[
\operatorname{Fib}(\alpha_M)\simeq
\bigoplus_{i\ge0}(R/(x))[i].
\]

The ordinary degree-zero discrepancy is exactly the coefficient-ideal discrepancy already observed in the source:

\[
(sM)^G=Rn,\qquad \varepsilon P=xRn,
\qquad (sM)^G/\varepsilon P\cong R/(x).
\]

Indeed the induced surjection `P/εP→(M/sM)^G` has this kernel. The derived computation supplies, in addition, a nonzero branch-supported defect in **every** positive degree.

## 3. General sums and the precise criterion

For an equivariant finite free cover module with character frame

\[
E=D^a\oplus(De)^b,
\qquad Q=E^G=A^a\oplus P^b,
\]

one obtains

\[
Q\otimes_A^{\mathbf L}R\simeq
R^{a+b}[0]\oplus\bigoplus_{i\ge0}(R/(x))^b[i],
\]

while

\[
(E\otimes_D^{\mathbf L}B)^G\cong R^{a+b}[0].
\]

The comparison is projection and has fiber `⊕_{i≥0}(R/(x))^b[i]`. In particular it is a quasi-isomorphism exactly when `b=0`. The equivariant character-frame existence for finite free `D`-modules is part of the independently audited source result; the calculation here applies immediately to any specified such frame.

The criterion stated at the beginning now follows: `b=0` gives a free module and a comparison isomorphism; flatness implies all positive Tor groups vanish; and the displayed positive Tor group vanishes in any one degree exactly when `b=0`. This is a criterion **within the stated family**, not an assertion that vanishing of one Tor group characterizes flatness for arbitrary modules over arbitrary rings.

There are two convenient finite witnesses:

- `Tor_1^A(Q,R)=(R/(x))^b` detects nonflatness and its character multiplicity.
- The kernel of `H_0(α_E)` is the same `(R/(x))^b`, detecting the reduction-comparison failure already without computing the infinite tail.

The infinite tail additionally proves that replacing ordinary reduction by derived reduction does not erase the failure: it records it faithfully.

## 4. Optional independent two-factor test

This extension distinguishes divisor-supported and intersection-supported failures. Set

\[
R_2=k[[x,y]],\quad
A_2=R_2[\varepsilon,\eta]/(\varepsilon^2,\eta^2).
\]

Let `P_x` be free of rank two over `R₂`, with `εm_x=xn_x`, and let `P_y` have `ηm_y=yn_y`. Define the `A₂`-module

\[
Q_{--}=P_x\otimes_{R_2}P_y,
\]

where `ε` acts on the first factor and `η` on the second. This is the double-negative invariant module of

\[
D_2=k[[u,v]][s,t]/(s^2,t^2),\quad x=u^2,\ y=v^2,
\]

under the two independent simultaneous sign actions, with `ε=us`, `η=vt`. For a double-negative generator `e`, its invariant basis is

\[
uv e,\quad vs e,\quad ut e,\quad st e.
\]

Resolve `R₂` over `A₂` by the total complex of the two periodic resolutions. Each total degree has finitely many free summands; the two resolutions are split exact over the base `R₂`, so their total complex is indeed a free resolution of `R₂`. After tensoring with `Q_{--}`, the resulting complex is `C_x⊗_{R₂}C_y`. The complexes `C_x,C_y` are bounded-below complexes of free `R₂`-modules, hence compute their derived tensor product.

From the one-factor decompositions,

\[
C_x\simeq R_2[0]\oplus\bigoplus_{i\ge0}(R_2/(x))[i],
\qquad
C_y\simeq R_2[0]\oplus\bigoplus_{j\ge0}(R_2/(y))[j].
\]

Transversality is essential: multiplication by `x` is injective on `R₂/(y)`, so

\[
R_2/(x)\otimes_{R_2}^{\mathbf L}R_2/(y)\simeq k[0].
\]

There are `n+1` ordered pairs `(i,j)` of nonnegative integers with `i+j=n`. Consequently

\[
\operatorname{Tor}^{A_2}_0(Q_{--},R_2)
=R_2\oplus R_2/(x)\oplus R_2/(y)\oplus k,
\]

and, for every `n≥1`,

\[
\operatorname{Tor}^{A_2}_n(Q_{--},R_2)
=R_2/(x)\oplus R_2/(y)\oplus k^{n+1}.
\]

These are actual direct-sum descriptions as `R₂`-modules. The synthetic cover reduction is `R₂(uv e)` in degree zero, and the comparison again projects onto its lone free degree-zero summand. Its fiber has the three torsion summands in degree zero and the displayed whole Tor group in every positive degree.

More generally, for character multiplicities `a_{++},a_{-+},a_{+-},a_{--}`, the invariant module of a corresponding equivariant free frame has

\[
\operatorname{Tor}^{A_2}_n(Q,R_2)=
(R_2/(x))^{a_{-+}+a_{--}}\oplus
(R_2/(y))^{a_{+-}+a_{--}}\oplus
k^{(n+1)a_{--}}\quad(n\ge1).
\]

In degree zero add `R₂^{a_{++}+a_{-+}+a_{+-}+a_{--}}` and replace the final multiplicity by `a_{--}`. Thus absence of all three nontrivial characters is equivalent, within this framed family, to flatness, freeness, vanishing of any positive Tor group, and the derived comparison being an isomorphism. This does not classify arbitrary modules over `A₂`.

## 5. What this does, and does not, establish for transport

An `A`-linear derived module identification compatible with the chosen reduction necessarily preserves the derived reductions and their Tor groups. Thus a candidate identification of the **synthetic** `A^a⊕P^b` with an `A`-free degree-zero model cannot satisfy that requirement when `b>0`. An abstract isomorphism of endomorphism rings is insufficient: for the source example `End_A(P)≅R[δ]/δ²`, but the natural coefficient map sends `ε↦xδ`, and the derived test retains this branch factor.

The bounded next check in any proposed physical-to-corrected comparison is therefore to specify its actual coefficient algebra, inertia action and reduction ideal; establish the relevant module-level transport; and check its reduction comparison, for example by a justified computation of `Tor₁` or the degree-zero comparison kernel. The formulas above supply a rigorous universal test case against which a proposed theorem can be checked.

They do **not** determine those data for an actual physical presentation, evaluate any physical obstruction, disprove existence of physical modules, or show that the required physical-to-corrected transport is impossible. This calculation does not discharge transport hypotheses in any application by itself. The new result isolates exactly what additional inertia-sensitive, reduction-compatible information those conclusions require.
