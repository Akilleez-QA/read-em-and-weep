# Local nilpotent weak actions strictify by finite-group averaging

## Result

Yes. A genuine coherent weak action of a finite group whose coherence units are congruent to 1 modulo a stable nilpotent ideal can be made exactly strict by an inner gauge congruent to 1. The same holds for a separated complete multiplicative pronilpotent filtration. Invertibility of the group order is essential to the argument.

This closes the LOCAL weak-action gap in Section 7 of the root/Morita report, under the hypotheses below. It does not construct compatible gauges across a general algebroid atlas, identify the resulting invariant algebra with a prescribed downstairs model, or remove a nontrivial classical projective cocycle.

All proofs below are universal algebra. No physical source or jet values are evaluated in this argument. A separately supplied synthetic additive test is not used as evidence for the theorem.

## 1. Exact hypotheses and conventions

Let D be an associative unital ring and G a finite group of order n, with n·1_D invertible. Its inverse is central and fixed by every unital ring automorphism. Use either:

- a nilpotent two-sided ideal J, filtered by J^k, with J^N=0; or
- descending two-sided ideals J_1 ⊇ J_2 ⊇ …, with J_p J_q ⊆ J_{p+q}, such that D ≅ lim_k D/J_k as rings.

In the second case completeness AND separatedness are required. Each J_k is closed for this topology. Powers J^k are the main example, but the proof works for the stated general filtration. Write J_k for both cases. Assume all F_g preserve every J_k, and in the complete case are continuous automorphisms.

A coherent weak action consists of automorphisms F_g and units A(g,h) satisfying

    F_g F_h = Ad(A(g,h)) F_gh,
    A(g,h) A(gh,t) = F_g(A(h,t)) A(g,ht),
    A(g,h) ∈ 1+J_1.

The second equation is the actual pentagon, not merely equality of the associated inner automorphisms. A central defect in the pentagon cannot be ignored.

Initially assume normalized units:

    F_e = id,    A(e,g)=A(g,e)=1.

Section 5 explains normalization when these are not initially imposed. We use Ad(c)(x)=cxc^{-1}. A gauge c_g changes the data by

    F^c_g = Ad(c_g) F_g,
    A^c(g,h) = c_g F_g(c_h) A(g,h) c_gh^{-1}.           (1)

The claim is that there are c_g ∈ 1+J_1, with c_e=1 for normalized input, such that A^c(g,h)=1 for all g,h. In particular F^c_g F^c_h=F^c_gh exactly.

## 2. The graded action is genuine

Put V_k=J_k/J_{k+1}, viewed as an additive module. Conjugation by any u∈1+J_1 acts identically on V_k. For x∈J_k,

    uxu^{-1}−x = (ux−xu)u^{-1} ∈ J_{k+1},

because u−1∈J_1 and J_1J_k+J_kJ_1⊆J_{k+1}. Thus the weak composition law induces an honest action of G on V_k:

    g·[x] = [F_g(x)].

The same action on V_k is induced by every gauge in 1+J_1. No strict action on all of D has been assumed in obtaining this graded action.

## 3. One improvement step, including the sign

Suppose the current coherent normalized data have A(g,h)∈1+J_k. Set

    a(g,h) = [A(g,h)−1] ∈ V_k.

Reduce the pentagon modulo J_{k+1}. Products of two elements of J_k lie in J_{2k}⊆J_{k+1}, so its additive form is

    a(g,h)+a(gh,t) = g·a(h,t)+a(g,ht).                 (2)

This is the ordinary inhomogeneous 2-cocycle equation for the genuine action on V_k. Define

    b(g) = n^{-1} Σ_(t∈G) a(g,t).

Summing (2) over t, and using that t↦ht permutes G, gives

    a(g,h)+b(gh) = g·b(h)+b(g).

Equivalently,

    (δb)(g,h) := b(g)+g·b(h)−b(gh) = a(g,h).          (3)

Thus the suggested average has exactly the claimed sign, even with a nontrivial action on the graded coefficients.

Choose a lift β_g∈J_k of b(g). There is an explicit lift requiring no auxiliary splitting:

    β_g = n^{-1} Σ_(t∈G) (A(g,t)−1).

For normalized input β_e=0 exactly. Put d_g=1−β_g. It is a unit because β_g is nilpotent in the finite case; in the complete case its inverse is the convergent sum Σ_(r≥0) β_g^r. Formula (1), with d in place of c, gives modulo J_{k+1}

    A^d(g,h)
      ≡ (1−β_g)(1−F_g(β_h))(1+(A(g,h)−1))(1+β_gh)
      ≡ 1+a(g,h)−b(g)−g·b(h)+b(gh)
      = 1.

Consequently A^d(g,h)∈1+J_{k+1}. The omitted noncommutative products all contain at least two J_k factors and hence lie in J_{2k}⊆J_{k+1}. No commutativity of D, centrality of β_g, or unjustified reordering is used.

The new data remain coherent exactly, not merely modulo J_{k+1}: formula (1) is the usual exact inner gauge and preserves both weak-action identities. It preserves normalization since d_e=1. It also preserves every two-sided coefficient ideal that the old automorphisms preserve.

## 4. Iteration and convergence

Begin with C_g^(0)=1. At step k use the current action and units, choose the explicit β_g above, and set

    d_g^(k)=1−β_g^(k),
    C_g^(k)=d_g^(k) C_g^(k−1).

The order here matters: applying gauge d to the already C-gauged presentation is gauge dC on the original presentation. An exact substitution into (1) verifies this composition rule.

After step k,

    A^(k)(g,h)∈1+J_{k+1},
    C_g^(k)−C_g^(k−1)∈J_k.

In the nilpotent case J_N=0, the process terminates after step N−1 and gives A^(N−1)(g,h)=1 literally.

In the complete case, the C_g^(k) are Cauchy and converge to c_g∈1+J_1. The inverse gauges are Cauchy as well, or equivalently c_g is inverted by its convergent geometric series. Multiplication and the original continuous F_g commute with the limits. Therefore

    A^c(g,h) = lim_k A^(k)(g,h)=1,

where separatedness is what turns membership in every 1+J_k into equality to 1. The resulting F^c_g=Ad(c_g)F_g are continuous, filtration-preserving automorphisms and satisfy the group law exactly.

For every fixed filtration order only finitely many stages affect the answer. Hence the construction is compatible with truncation. Formal completeness without separatedness would at most identify a residual defect in ⋂_k J_k; it would not prove exact strictness. Mere existence of individually strictifiable truncations, with no compatible choice, would also be insufficient, but the recursive construction supplies compatible choices here.

## 5. Identity normalization

If the two displayed weak-action equations hold for all g,h,t but the identity data were not normalized, let u=A(e,e). The composition equation gives F_e=Ad(u). Applying the pentagon to (e,e,g) and (g,e,e), respectively, gives

    A(e,g)=u,    A(g,e)=F_g(u).

Gauge by c_e=u^{-1} and c_g=1 for g≠e. Substitution into (1) yields normalized data. Since u∈1+J_1, this preliminary gauge is also congruent to 1.

Apply the iteration to these normalized data. For initially normalized data the final gauge has c_e=1. For initially unnormalized data the composite gauge generally has c_e=u^{-1}, as it must to remove F_e and the specified unit coherence. Thus one must not demand c_e=1 without first normalizing the input.

## 6. Weak modules transport to strict modules

Use the operator convention for a weak equivariant left D-module M. Its additive bijections ρ_g satisfy

    ρ_g(d m)=F_g(d)ρ_g(m),
    ρ_gρ_h(m)=A(g,h)ρ_gh(m).

For normalized data take ρ_e=id. Given the gauge above, define

    ρ^c_g(m)=c_gρ_g(m).

Then

    ρ^c_g(d m)=F^c_g(d)ρ^c_g(m),
    ρ^c_gρ^c_h(m)=A^c(g,h)ρ^c_gh(m).

These identities follow directly by keeping the written order of the factors. Once A^c=1, the operators ρ^c form a genuine semilinear group action. The inverse transformation is ρ_g=c_g^{-1}ρ^c_g. D-linear equivariant morphisms are unchanged, so this is an equivalence between the corresponding weak-action and strict-action module categories. It applies degreewise to complexes whenever their structure maps are equivariant; no existence of a module is inferred.

The underlying D-module has not changed. In particular freeness and rank are preserved. Because c_g≡1 mod J_1, the original and transported actions on M/J_1M agree, as do the original and transported algebra maps on D/J_1. If J_1⊆Jac(D), they also agree on M/Jac(D)M. In a nilpotent or complete multiplicative setting J_1⊆Jac(D): for x∈J_1 and d∈D, 1−dx is inverted by a finite or convergent geometric series. Thus residual inertia representations are unchanged. A nontrivial residual root character must already have been removed by the preceding Morita transport; this gauge cannot remove it.

For topological modules, require continuity of the original operators and the module operations. Finite free modules with the induced complete filtration satisfy the needed conditions, and the transported operators remain continuous.

## 7. Coefficient ideals and reductions

Let I be a two-sided ideal stable under all original F_g. Inner conjugation by any unit preserves I exactly. Hence every intermediate and final F^c_g also preserves I. The weak module submodule IM is carried to itself by every original and transported operator.

Gauge formulas therefore commute with passage to D/I and M/IM whenever those quotients are defined. In the finite case, the explicit recursive formula is natural under compatible quotient maps. In the complete case require the relevant quotient to carry the compatible complete topology, for example D/I with I closed and D/I complete, when asserting equality of the entire recursive construction with the construction on that quotient. Irrespective of such an effectivity assertion, the already constructed gauge reduces algebraically and makes the quotient action strict.

If I contains J_1, the reduced gauge is the identity. For an arbitrary I, it need not be the identity: preservation of I is weaker than a fixed prescribed identification of the quotient action. The conclusion is compatibility by the induced gauge, not literal agreement with some independently chosen quotient trivialization.

When a central coefficient ring is fixed pointwise by the original action, inner gauges leave its image fixed pointwise. More generally any specified action on central coefficient elements is unchanged. Stable two-sided ideals generated by parameter directions, including mixed ideals, stay stable. This supplies no equality between invariants of an ideal product and products of invariant ideals, nor any identification of coefficient multiplication with a proposed downstairs model.

The explicit recursion is natural for strict maps of the entire filtered weak-action data: maps intertwining each F_g and carrying each A(g,h) to its counterpart commute with the finite averages, gauges, and convergent limits where defined. This limited functoriality is useful, but does not turn weakly compatible overlap maps into strictly compatible ones without further work.

## 8. Conditional join with the invariant-basis theorem

Assume additionally that:

1. D is genuinely local, with m=Jac(D) and residue field k;
2. the acting finite group fixes k pointwise and n is invertible in D;
3. a weak equivariant M exists and is finite free over D;
4. its residual action on M/mM is trivial;
5. all coefficient ideals under consideration are stable two-sided ideals.

Strictify the weak algebra action and transport M as above. Since the gauge is 1 modulo m, hypotheses 2 and 4 persist. Put

    B = D^{G,c} = {d∈D : F^c_g(d)=d for all g},
    P = M^{G,c} = {m∈M : ρ^c_g(m)=m for all g}.

The local invariant-basis theorem in the trivial-inertia report now applies legitimately. It proves that P is finite free over B and that the canonical map

    D⊗_B P → M

is an equivariant isomorphism for the strictified action. Moreover, for each stable two-sided ideal I,

    B/(I∩B) ≅ (D/I)^{G,c},
    P/(I∩B)P ≅ (M/IM)^{G,c}.

Thus the combined result supplies effective free-module descent, with the actual invariant coefficient ideals, AFTER local Morita untwisting has produced the stated coherent weak data and trivial residual representation. It removes the separate need to assume that this weak local action was already strict.

It remains conditional on existence of M and on the actual local, residue-field, finiteness, stability, and coherence hypotheses. At a point moved by part of the group, first restrict to a group acting on the one local ring, or supply a suitable orbit/semilocal construction. If the full decomposition group acts nontrivially on k, additional residue-field descent is still needed. The theorem does not identify B with an independently prescribed algebra or establish a global coarse-space equivalence.

## 9. Global and classical limitations

### General algebroid gluing

This is a theorem about a finite group acting weakly on ONE filtered algebra. Applying it separately on charts gives strict local group actions, but the chart-to-chart coherence must also be transformed and checked. There is no averaging over the Čech directions in this proof. Consequently one cannot infer that all overlap weak units become 1, that local invariant algebras glue as an ordinary prescribed sheaf of algebras, or that the local gauges satisfy a separately required global compatibility.

If actual global sections of one complete sheaf algebra carry the full weak action on invariant opens, and the explicit data restrict strictly, the recursion is restriction-compatible there. This is a favorable extra situation, not a consequence for an arbitrary algebroid presentation or an atlas whose opens are moved by G. The total quotient-stack groupoid may retain nontrivial gluing even after strictifying every isotropy action.

### Classical Schur cocycles

The assumption A(g,h)≡1 mod J_1 is substantive. It forces the specified classical coherence units to be trivial, not just their inner automorphisms. If reduction gives a nontrivial k×-valued projective cocycle, a gauge congruent to 1 cannot change it at all. Invertibility of |G| kills positive-degree cohomology of the additive graded modules used above, not arbitrary multiplicative H²(G,k×). This proof must not be used to erase a general classical Schur multiplier or an unspecified gerbe class.

Even when F_g already satisfy the group law as automorphisms, a central A(g,h) still matters to the weak module problem. It is covered by this proof if A(g,h)∈1+J_1 and the pentagon holds exactly; it is not covered merely because its inner automorphism is trivial.

### No missing-model conclusion

The result changes the chosen action by an explicit inner gauge; it neither changes the underlying algebra product nor identifies that product with a proposed physical or corrected product. It evaluates no mixed obstruction, creates no module, and proves no physical-to-corrected ambient comparison. The remaining global compatibility and ambient-identification obligations in the root/Morita report are unchanged.

## Inputs

Read in full:

- ../../null-root-morita-inertia/root-morita-0719/RESULT.md
- ../../null-root-morita-inertia/trivial-inertia-0719/RESULT.md

The proof of strictification is derived directly from the stipulated composition law and pentagon, with finite additive averaging on each filtration layer.
