> Publication scope: Choice independence and explicit finite averaging for a supplied coherent atlas, not construction of that atlas. Historical statements about unresolved mixed classes refer to the source stage; this packet does not supersede the separately stated conditional mixed-vanishing result in PR145.

# Choice-independence of conditional invariant Morita descent

## Result and scope

For one **supplied, coherent weak equivariant Morita atlas**, two systems of filtration-trivial local strictifications produce equivalent invariant algebroids. The comparison sends

\[
d\longmapsto B_i dB_i^{-1},\qquad
p\longmapsto B_i pB_j^{-1}.
\]

It respects the actual composition maps, the descended locally free module problem, and compatible coefficient ideals. Different comparison units give explicit inner natural isomorphisms; comparisons for three or more strictifications satisfy the required coherence. This is independence **up to coherent equivalence**, not equality of invariant subrings or uniqueness of an equivalence.

There is also an explicit finite averaging formula for the comparison units. Once the strictifications are actual sheaf sections and the filtration ideal is locally radical, the comparison does not require another inverse-limit construction.

The starting descent criterion is [PR 1 comment 6263380151](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6263380151), created and last updated 2026-10-19 at 08:50:01 UTC. Its argument was independently checked in the accompanying source audit. The local strictification theorem and its H¹ comparison are the prior conditional results used below. No physical atlas is constructed or identified here, and no physical operation, matrix, module obstruction, or retained value is evaluated.

## 1. The supplied data and locality assumptions

Work on a specified quotient atlas, with actual restriction-compatible sheaves and actual coherent overlap data. We write a common finite group \(G\) in the formulas. For stabilizer charts, each displayed formula is interpreted after the **supplied** restrictions to the relevant overlap group; change-of-group and group/Čech coherence are part of the supplied atlas, not conclusions of this proof.

On chart \(i\), let \(D_i\) be a sheaf of associative unital rings with a two-sided ideal \(F^1D_i\), preserved by the weak action. Require \(|G|\) to be invertible wherever that group acts, and require every section in \(1+F^1D_i\) to be a unit locally. Sufficient conditions are the complete separated multiplicative filtered-ring hypotheses of the prior theorem on a basis of section rings, or the simpler condition

\[
F^1D_{i,x}\subseteq \operatorname{Jac}(D_{i,x})
\]

at every relevant stalk. A section whose germs are units is a sheaf unit: its local inverses are unique and glue. All comparisons below take place on opens where the displayed strictification sections exist.

The normalized weak action on \(D_i\) is denoted \((\phi_i,a_i)\), with

\[
\phi_i(g)\phi_i(h)=\operatorname{Ad}(a_i(g,h))\phi_i(gh),
\qquad a_i(g,h)\in 1+F^1D_i.
\]

Its specified coherence satisfies the usual cocycle equation. The overlap \(P_{ij}\) is an actual Morita-invertible \((D_i,D_j)\)-bimodule, with weak semilinear maps \(\sigma_{ij}(g)\) satisfying

\[
\begin{aligned}
\sigma_{ij}(g)(dpe)&=\phi_i(g)(d)\sigma_{ij}(g)(p)\phi_j(g)(e),\\
\sigma_{ij}(g)\sigma_{ij}(h)(p)
 &=a_i(g,h)\sigma_{ij}(gh)(p)a_j(g,h)^{-1}.
\end{aligned}
\]

There are actual equivariant bimodule isomorphisms

\[
\mu_{ijk}:P_{ij}\otimes_{D_j}P_{jk}\longrightarrow P_{ik},
\]

with the specified associative and unit coherence; identify \(P_{ii}=D_i\) with its usual unit maps. These maps and identities hold as sheaf data, not merely at completed stalks.

Assume the source criterion's additional local hypotheses: the overlaps are locally free of left rank one and, after strictification, have trivial residue inertia and locally available invariant generators. Assume the corresponding local finite-free, trivial-residue-inertia module descent theorem, and the required atlas/stack effectiveness. These hypotheses establish invariant Morita descent; the present proof compares its choices.

Let \(Q_i(g),R_i(g)\in 1+F^1D_i\) be two normalized systems of **actual local strictification sections** for the same weak atlas. The inverse-gauge convention is

\[
\psi_i(g)=\operatorname{Ad}(Q_i(g)^{-1})\phi_i(g),
\qquad
\chi_i(g)=\operatorname{Ad}(R_i(g)^{-1})\phi_i(g),
\]

and both transformed coherence units are exactly one. On overlaps put

\[
S^Q_{ij}(g)(p)=Q_i(g)^{-1}\sigma_{ij}(g)(p)Q_j(g),
\quad
S^R_{ij}(g)(p)=R_i(g)^{-1}\sigma_{ij}(g)(p)R_j(g).
\tag{1}
\]

These are strict actions. They are the source's convention with \(c_i=Q_i^{-1}\) or \(R_i^{-1}\). Write

\[
A_i^Q=D_i^{\psi_i},\quad A_i^R=D_i^{\chi_i},\qquad
\overline P_{ij}^Q=P_{ij}^{S^Q},\quad
\overline P_{ij}^R=P_{ij}^{S^R}.
\]

The source criterion makes these invariant data into Morita atlas presentations of algebroids \(\mathcal A^Q,\mathcal A^R\).

**Locality boundary.** Merely constructing \(Q,R\), or their comparison units, in isolated completed stalks is not enough to give the sheaf sections assumed here. If strictification sections exist only on a refinement, use that refinement. Nothing below proves their existence on an actual physical atlas.

## 2. An explicit H¹ comparison by finite averaging

Fix one chart and omit its index. Set

\[
r_g=Q_g^{-1}R_g,\qquad u_g=r_g^{-1}=R_g^{-1}Q_g.
\]

The strictification coherence equations give

\[
r_{gh}=\psi_g(r_h)r_g,
\qquad
u_g\psi_g(u_h)=u_{gh}.
\tag{2}
\]

This is the nonabelian H¹ cocycle from the prior theorem. Here it admits the particularly simple solution

\[
B=\frac1{|G|}\sum_{h\in G}u_h.
\tag{3}
\]

Indeed, reindexing the finite sum in (2) gives

\[
u_g\psi_g(B)=\frac1{|G|}\sum_hu_g\psi_g(u_h)
 =\frac1{|G|}\sum_hu_{gh}=B.
\]

Every \(u_h\) is in \(1+F^1D\), so \(B\in1+F^1D\). The unit hypothesis makes \(B\) invertible. Consequently

\[
u_g=B\psi_g(B^{-1}),\qquad
R_g=\phi_g(B)Q_gB^{-1},\qquad
\chi_g=\operatorname{Ad}(B)\psi_g\operatorname{Ad}(B^{-1}).
\tag{4}
\]

All orderings in (4) are essential in a noncommutative ring. Formula (3) is a finite sum of actual sections and commutes with ordinary sheaf restrictions that keep the same group presentation. It supplies a comparison section without choosing lifts in infinitely many filtration quotients. If a group is changed, the new averaging formula need not give the same section, but any two resulting comparison sections are related by Section 6.

The finite average requires neither a logarithm nor characteristic zero. Completeness was one sufficient way to ensure \(1+F^1D\) consists of units; comparison itself only needs that unit property. This simplification does not eliminate the complete-filtration hypotheses used to **construct** the strictifications in the earlier theorem.

Choose such a \(B_i\) on each chart. All possible solutions of (4) are

\[
B_i'=B_ic_i,\qquad
c_i\in(1+F^1D_i)^{\psi_i}.
\tag{5}
\]

To verify the converse, equality of the formulas for \(R_i(g)\) implies
\(\phi_i(g)(c_i)Q_i(g)=Q_i(g)c_i\), which is exactly \(\psi_i(g)(c_i)=c_i\).

## 3. Comparison of rings, overlaps and composition

Define

\[
\beta_i(d)=B_idB_i^{-1},\qquad
\beta_{ij}(p)=B_ipB_j^{-1}.
\tag{6}
\]

Equation (4) makes \(\beta_i:(D_i,\psi_i)\to(D_i,\chi_i)\) equivariant. For the overlaps, (4) gives both

\[
R_i(g)^{-1}\phi_i(g)(B_i)=B_iQ_i(g)^{-1},\quad
\phi_j(g)(B_j^{-1})R_j(g)=Q_j(g)B_j^{-1}.
\]

Therefore

\[
\begin{aligned}
S^R_{ij}(g)(B_ipB_j^{-1})
 &=R_i(g)^{-1}\phi_i(g)(B_i)\sigma_{ij}(g)(p)
       \phi_j(g)(B_j^{-1})R_j(g)\\
 &=B_iS^Q_{ij}(g)(p)B_j^{-1}.
\end{aligned}
\tag{7}
\]

Thus **the displayed direction is Q→R**, and it is \(p\mapsto B_ipB_j^{-1}\), not its inverse. The inverse comparison is \(p\mapsto B_i^{-1}pB_j\). Moreover

\[
\beta_{ij}(dpe)=\beta_i(d)\beta_{ij}(p)\beta_j(e).
\]

Taking invariants gives ring isomorphisms \(A_i^Q\to A_i^R\) and invertible semilinear overlap isomorphisms
\(\overline P_{ij}^Q\to\overline P_{ij}^R\).

In the balanced tensor, the middle factors cancel:

\[
\begin{aligned}
\mu_{ijk}(\beta_{ij}(p)\otimes\beta_{jk}(q))
 &=\mu_{ijk}(B_ipB_j^{-1}\otimes B_jqB_k^{-1})\\
 &=B_i\mu_{ijk}(p\otimes q)B_k^{-1}\\
 &=\beta_{ik}(\mu_{ijk}(p\otimes q)).
\end{aligned}
\tag{8}
\]

The source criterion identifies the **specific** invariant balanced tensors with the invariants of these tensors by invariant rank-one generators. Equation (8) is compatible with that natural map. Hence the supplied invariant compositions and all their associativity identities are preserved. The identity overlaps are preserved because \(\beta_{ii}=\beta_i\) and \(\beta_i(1)=1\).

The maps (6) thus give an isomorphism of the displayed Morita atlas presentations and an equivalence

\[
F_B:\mathcal A^Q\simeq\mathcal A^R.
\]

This argument uses no assertion that invariants commute with arbitrary tensor products.

## 4. The descended module equivalence and its direction

Use left modules. A descended module is given by left \(A_i^Q\)-modules \(N_i\) and coherent transition maps

\[
\theta_{ij}:\overline P_{ij}^Q\otimes_{A_j^Q}N_j\longrightarrow N_i.
\]

Transport along (6) gives an equivalence \(E_B\) from the Q-module descent category to the R-module descent category. Its chart \(i\) is the **same additive sheaf** \(N_i\) with action

\[
a'\cdot_B n=\beta_i^{-1}(a')n\qquad(a'\in A_i^R),
\tag{9}
\]

and transition map

\[
\theta^B_{ij}(p'\otimes n)
 =\theta_{ij}(\beta_{ij}^{-1}(p')\otimes n).
\tag{10}
\]

Semilinearity makes (10) balanced, and (8) proves the transition coherence. The inverse transport uses \(B_i^{-1}\). Local finite freeness, ranks, and the source criterion's module subcategory are preserved.

This equivalence agrees with the descent of a given compatible weak module. Namely, suppose \(M_i\) has weak semilinear action \(T_i(g)\) and weak-equivariant gluing
\(P_{ij}\otimes M_j\to M_i\). Its two strictifications are

\[
T_i^Q(g)=Q_i(g)^{-1}T_i(g),\qquad
T_i^R(g)=R_i(g)^{-1}T_i(g).
\]

Equation (4) yields

\[
T_i^R(g)(B_im)=B_iT_i^Q(g)(m).
\tag{11}
\]

Thus \(m\mapsto B_im\) is a semilinear isomorphism from the Q-invariants to the R-invariants, or equivalently an \(A_i^R\)-linear isomorphism

\[
\lambda_{B,i}:E_B(M_i^{T^Q})\longrightarrow M_i^{T^R}.
\tag{12}
\]

It respects gluing because
\((B_ipB_j^{-1})\otimes(B_jm)\) maps to \(B_i\theta_{ij}(p\otimes m)\).
It is natural in equivariant module maps. Since \(B_i\equiv1\pmod{F^1}\), this comparison acts identically on the residual quotient whenever that quotient kills \(F^1M_i\), and on the associated graded when a compatible filtration is supplied. No nontrivial residual inertia representation is removed.

## 5. Compatible ideals and quotient module problems

Let \(I_i\subset D_i\) be weak-action-stable two-sided ideal sheaves, compatible with the actual Morita overlaps:

\[
I_iP_{ij}=P_{ij}I_j=:K_{ij}.
\tag{13}
\]

Inner conjugation preserves every two-sided ideal. Consequently both strict actions preserve \(I_i\), and

\[
\beta_i(I_i)=I_i,\quad \beta_{ij}(K_{ij})=K_{ij},\qquad
\beta_i(J_i^Q)=J_i^R,
\quad J_i^Q=I_i\cap A_i^Q,\quad J_i^R=I_i\cap A_i^R.
\tag{14}
\]

For clarity, the descended overlap ideal really is the invariant intersection. In an invariant left generator \(e_{ij}\), write \(e_{ij}b=\rho_{ij}(b)e_{ij}\), where the source criterion proves \(\rho_{ij}:D_j\to D_i\) is equivariant and is an algebra isomorphism. Equation (13) gives \(\rho_{ij}(I_j)=I_i\). Therefore, in either strictification,

\[
K_{ij}\cap\overline P_{ij}
 =J_i\overline P_{ij}
 =\overline P_{ij}J_j.
\tag{15}
\]

Equations (14)–(15) show that \(F_B\) identifies the descended ideal data and quotient algebroids. Similarly \(E_B\) identifies \(J_i^QN_i\) with the corresponding \(J_i^R\)-submodule, so it induces the equivalence of quotient module descent problems.

The finite-group averaging operator gives, locally and hence as sheaves,

\[
A_i^Q/J_i^Q\simeq(D_i/I_i)^{\psi_i},
\qquad
A_i^R/J_i^R\simeq(D_i/I_i)^{\chi_i}.
\tag{16}
\]

The module analogue follows in the invariant finite-free frames from the source criterion. The comparison is compatible with these identifications, because it is equivariant and preserves the ideals. Neither (15) nor (16) assumes flatness or arbitrary two-sided base change. If \(I_i\) does not contain \(F^1D_i\), the comparison on the quotient is still an isomorphism but need not be the identity.

## 6. Ambiguity is an inner natural isomorphism

Let \(B_i'=B_ic_i\) be another family of solutions, as in (5), and put

\[
v_i=B_i'B_i^{-1}=B_ic_iB_i^{-1}\in(A_i^R)^\times\cap(1+F^1D_i).
\tag{17}
\]

Then

\[
\beta_i'=\operatorname{Ad}(v_i)\beta_i,\qquad
\beta_{ij}'(p)=v_i\beta_{ij}(p)v_j^{-1}.
\tag{18}
\]

Regard \(P_{ij}\) as arrows \(j\to i\). Equation (18) is exactly

\[
\beta_{ij}'(p)v_j=v_i\beta_{ij}(p),
\]

so the units \(v_i\) define a natural isomorphism

\[
\eta_{B,B'}:F_B\Longrightarrow F_{B'}.
\tag{19}
\]

For the **covariant transport of left modules** defined by (9), the corresponding transformation has the inverse orientation on the underlying N:

\[
\alpha_{B,B',i}:E_B(N_i)\longrightarrow E_{B'}(N_i),
\qquad n\longmapsto c_i^{-1}n
 =\beta_i^{-1}(v_i^{-1})n.
\tag{20}
\]

Indeed \(\beta_i'^{-1}(a')=c_i^{-1}\beta_i^{-1}(a')c_i\), proving linearity. Also

\[
\beta_{ij}'^{-1}(p')=c_i^{-1}\beta_{ij}^{-1}(p')c_j,
\]

so (20) respects (10), by balancing the factors \(c_j,c_j^{-1}\). For the concrete invariant modules in (12),

\[
\lambda_{B'}\circ\alpha_{B,B'}=\lambda_B,
\]

because \(B_ic_i(c_i^{-1}m)=B_im\). All these transformations preserve the ideal and quotient subcategories.

For three choices \(B,B',B''\), the natural transformations compose exactly:

\[
(B_i''B_i'^{-1})(B_i'B_i^{-1})=B_i''B_i^{-1}.
\tag{21}
\]

The corresponding module transformations compose in the inverse order required by (20). Thus differences between comparison sections are coherent, including on overlaps of a further refinement.

This constructs a specified natural isomorphism from the two witnesses. It does **not** assert that no other natural isomorphisms exist: invariant central units, for example, can give nontrivial automorphisms. Neither the invariant subring nor the comparison equivalence is being declared uniquely determined as a literal object.

## 7. Triple comparisons and higher coherence

Label strictification systems by \(a,b,c,\ldots\). Write \(B_i^{ba}\) for a comparison from system \(a\) to system \(b\), and write \(F^{ba}\) for the corresponding algebroid equivalence. If \(B^{ba}\) and \(B^{cb}\) are chosen, their ordered product

\[
B_i^{cb}B_i^{ba}
\tag{22}
\]

compares \(a\) to \(c\), because

\[
Q_i^c(g)=\phi_i(g)(B_i^{cb}B_i^{ba})
 Q_i^a(g)(B_i^{cb}B_i^{ba})^{-1}.
\]

With product comparisons, both the ring and overlap maps satisfy

\[
F_{B^{cb}}\circ F_{B^{ba}}=F_{B^{cb}B^{ba}}
\tag{23}
\]

exactly on the displayed atlas. The corresponding transports satisfy the same equality with the actions defined in (9).

If \(B^{ca}\) was independently chosen, define its discrepancy by the **target invariant** unit

\[
v_i^{cba}=B_i^{ca}(B_i^{cb}B_i^{ba})^{-1}\in(A_i^c)^\times.
\tag{24}
\]

Section 6 gives the comparison 2-isomorphism

\[
F^{cb}F^{ba}\Longrightarrow F^{ca}
\]

with component \(v_i^{cba}\). For four labels, the two coherence paths agree because

\[
v_i^{dca}\,\beta_i^{dc}(v_i^{cba})
 =v_i^{dba}\,v_i^{dcb}
 =B_i^{da}(B_i^{dc}B_i^{cb}B_i^{ba})^{-1}.
\tag{25}
\]

This is the pseudofunctor associativity coherence; all longer associativity/pentagon comparisons telescope in the same way. Choose \(B^{aa}=1\) for the identity constraints, which also follows from averaging equal strictifications. Inverse comparisons may be chosen as \((B^{ba})^{-1}\); independently averaged inverse comparisons are naturally isomorphic by the same formulas.

Changes of witnesses are also compatible with horizontal composition. If \(B\to B'\) and \(C\to C'\), set \(v=B'B^{-1}\), \(w=C'C^{-1}\). The horizontal component is

\[
w\,\operatorname{Ad}(C)(v)
 =C'B'(CB)^{-1},
\tag{26}
\]

which is exactly the component for the composite witnesses. Equations (21), (25) and (26) supply the full choice-change coherence required here.

## 8. Passing from local comparisons to the descended statement

When \(Q,R\) are sections on the displayed charts, formula (3) directly supplies \(B_i\) there and respects ordinary restriction. If only a finer cover carries the needed sections, work on that common refinement. On intersections, any two comparison sections differ by (17), and (21) is the exact natural-transformation cocycle. Under the stipulated effective algebroid-stack descent, these local equivalences and their natural isomorphisms glue to an equivalence of the descended algebroid stacks. The same statements hold for their specified module problems and ideal quotients.

Therefore the invariant algebroid/module/ideal descent attached to one supplied weak equivariant Morita atlas is independent of filtration-trivial strictification choices **up to the explicit coherent equivalences above**. A finite average gives a useful restriction-natural pairwise comparison, but it is not generally multiplicative under triple comparison; (24)–(25) are the correct replacement for strict transitivity.

What remains outside the theorem is unchanged: existence of the actual physical atlas, actual overlap bimodules and all their coherence, availability of the local modules and their trivial residue inertia, actual sheaf effectiveness, identification with a specified full mixed ambient, and evaluation of the physical obstruction. The theorem supplies no single preferred global algebra, no arbitrary bimodule full-faithfulness or tensor-base-change theorem, and no numerical physical conclusion.
