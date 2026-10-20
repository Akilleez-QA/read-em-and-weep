> Publication scope: Theorem A existence overlaps PR124; the distinct contribution is Theorem B comparison and scalar-inertia constraints. Historical statements about unresolved mixed classes refer to the source stage; this packet does not supersede the separately stated conditional mixed-vanishing result in PR145.

# Local pronilpotent strictification of weak finite-group actions

## Scope and source

This conditional algebraic theorem addresses the **local, filtration-trivial coherence** part of the gap identified in [PR 1 comment 6261960300](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6261960300), posted 2026-10-19 at 07:24:37 UTC. The source supplies the exact inverse-gauge/Morita formulas and, separately, a strict-action invariant-frame lemma. The theorem below proves existence and comparison of local strictifications under explicit additional hypotheses. It does not verify those hypotheses for the physical ambient, identify that ambient, globalize the gauges, or compute any operation, matrix, input, detector, or physical value.

## 1. Hypotheses and conventions

Let D be an associative unital ring, possibly noncommutative, with a descending filtration by two-sided ideals

D = F^0 D ⊇ F^1 D ⊇ F^2 D ⊇ …,

such that F^i D · F^j D ⊆ F^(i+j) D for all i,j ≥ 0. Assume the natural ring map D → lim_n D/F^n D is an isomorphism. Thus the filtration is separated and complete, its ideals are closed, and multiplication is continuous. Let G be a finite group of order m, and suppose m·1 is invertible in D. Its inverse is central and fixed by every unital automorphism. Write U_n=1+F^n D for n≥1. Geometric series show these are groups of units.

A normalized weak action consists of filtration-preserving unital automorphisms φ_g and units a_g,h∈U_1 satisfying

(1) φ_g φ_h = Ad(a_g,h) φ_gh,

(2) a_g,h a_gh,k = φ_g(a_h,k) a_g,hk,

with φ_e=id and a_e,g=a_g,e=1. Here Ad(a)(d)=a d a⁻¹. Normalization is an explicit hypothesis; equivalently one may start with a normalized presentation of a unital weak action. No merely outer action without specified coherent units is being asserted to admit a lift.

For normalized gauges q_g∈U_1, q_e=1, use exactly the source's order:

(3) ψ_g = Ad(q_g⁻¹) φ_g,

(4) b_g,h = q_g⁻¹ φ_g(q_h)⁻¹ a_g,h q_gh.

These obey (1)–(2) with ψ,b in place of φ,a. This follows by substitution; the factor φ_g(q_h)⁻¹ is on the LEFT of a_g,h. A gauge with b_g,h=1 is called a strictification. Merely making b central would not suffice here.

## 2. Elementary filtration facts

For n≥1, multiplication induces an isomorphism of abelian groups

U_n/U_(n+1) → F^n D/F^(n+1) D,  1+x ↦ [x].

Indeed xy∈F^(2n)⊆F^(n+1). If t∈U_r and x∈F^s D, then

Ad(t)(x)−x ∈ F^(r+s) D.

Consequently inner conjugation by U_1 acts trivially on every graded piece F^s/F^(s+1), including s=0. The weak φ_g therefore induce a genuine G-action on every graded piece; equation (1) becomes strict there. Every subsequent U_1 gauge induces the same graded action.

The additive groups V_n=F^n/F^(n+1) admit division by m: multiplication by m⁻¹ in D preserves each ideal and commutes with G. This is the precise averaging hypothesis.

## 3. One-step strictification, with explicit averaging

Suppose a current normalized weak action (θ,c) has c_g,h∈U_n. Set α_g,h=[c_g,h−1]∈V_n. Reducing (2) modulo F^(n+1) yields

(5) α_g,h + α_gh,k = g·α_h,k + α_g,hk.

All discarded products lie in F^(2n)⊆F^(n+1); θ induces the genuine action of Section 2. Define

(6) x_g = m⁻¹ Σ_(k∈G) α_g,k.

Summing (5) over k and reindexing hk gives

(7) α_g,h = x_g + g·x_h − x_gh.

In particular x_e=0. Choose any lifts x̃_g∈F^n, taking x̃_e=0, and set r_g=1+x̃_g. Apply (3)–(4) to θ,c with gauge r. Its new coherence has class

[c'_g,h−1] = −x_g − g·x_h + α_g,h + x_gh = 0.

Thus c'_g,h∈U_(n+1). This proves the needed degree-two vanishing by an explicit formula rather than invoking a nonabelian cohomology assertion.

## 4. Existence and convergence theorem

**Theorem A.** Under Section 1, there are normalized gauges Q_g∈U_1 for which

ψ_g=Ad(Q_g⁻¹)φ_g,   Q_g⁻¹φ_g(Q_h)⁻¹a_g,h Q_gh=1.

In particular ψ is an actual action on the same underlying ring D, with unchanged action on the associated graded ring.

**Proof.** Start Q_g^(0)=1 and apply Section 3 at n=1,2,… . If the current aggregate gauge is Q and the new correction is r, the aggregate gauge is **Q r**, since

Ad(r⁻¹)Ad(Q⁻¹)=Ad((Q r)⁻¹).

The coherence formula also composes in this order, by direct substitution. After stage n, Q^(n)=Q^(n−1)r^(n), with r^(n)∈U_n, and its coherence belongs to U_(n+1). For every fixed N, the Q^(n) are eventually constant modulo F^N. Completeness produces Q_g∈U_1; inverse products converge as well, or use the geometric-series inverse of Q_g. Each φ_g is continuous because it preserves the filtration. Therefore formula (4) for the limiting Q reduces to 1 modulo every F^N. Separatedness gives equality to 1 in D. Formula (1) now gives ψ_gψ_h=ψ_gh exactly. Normalization persists at every stage. ∎

No separate completeness of an automorphism group is needed: the limiting automorphisms are explicitly Ad(Q_g⁻¹)φ_g. Completeness without separatedness would give coherence only in 1+∩F^n, not necessarily 1. Multiplicativity and the ideal conditions are needed in all error estimates. No characteristic-zero or logarithm/Baker–Campbell–Hausdorff hypothesis is used.

**Finite nilpotent version.** If F^(N+1)D=0 and the remaining hypotheses hold, no completion hypothesis is necessary: U_n consists of units by finite geometric series, and stages n=1,…,N give an exact strictification. More generally the construction on D/F^(N+1) gives strictification to order N; the successive construction above chooses these truncations compatibly. This refers to finite filtration order, not to a torsion hypothesis on individual units.

## 5. Comparison of choices: nonabelian H¹ vanishing

**Lemma.** For any strict filtration-preserving G-action ψ on D and normalized cocycle u_g∈U_1 satisfying

u_g ψ_g(u_h)=u_gh,

there exists B∈U_1 such that u_g=B ψ_g(B⁻¹).

**Proof.** For a cocycle valued in U_n, let v_g=[u_g−1]∈V_n. Then v_gh=v_g+g·v_h. Put z=m⁻¹Σ_h v_h. Summing gives v_g=z−g·z. Choose z̃∈F^n and t=1+z̃. The gauge-transformed cocycle t⁻¹u_g ψ_g(t) has class −z+v_g+g·z=0, and remains a cocycle for the same ψ. Iterating with aggregate B multiplied on the right by t produces convergent B∈U_1 for which B⁻¹u_gψ_g(B)=1. The finite nilpotent version terminates. ∎

**Theorem B.** Let Q,R be two normalized U_1-valued strictifications of the same weak action. Write ψ=Ad(Q⁻¹)φ and χ=Ad(R⁻¹)φ. Then there exists B∈U_1 with

(8) R_g = φ_g(B) Q_g B⁻¹,

(9) χ_g = Ad(B) ψ_g Ad(B⁻¹).

**Proof.** Put r_g=Q_g⁻¹R_g. By the composition order in Section 4, r gauges the strict action ψ to χ and has trivial resulting coherence. Thus

r_gh=ψ_g(r_h)r_g,

so u_g=r_g⁻¹ satisfies the cocycle identity in the lemma. Hence r_g=ψ_g(B)B⁻¹. Multiplying on the left by Q_g gives (8), and conjugation gives (9). ∎

The comparison unit is not unique. If B is one solution, all solutions are Bc with c∈U_1 fixed by every ψ_g. Indeed equality of the two coboundaries is equivalent to c=ψ_g(c). The result is existence and the stated ambiguity, not a distinguished strictification or a canonical global descent datum. Comparisons are coherent with reduction because B≡1 modulo F^1, and can be constructed by the same compatible finite-order process.

## 6. Compatible modules and preservation of residual inertia

Fix a left D-module M with a normalized weak semilinear action T_g, meaning bijective additive maps with

T_g(dm)=φ_g(d)T_g(m),   T_gT_h(m)=a_g,h T_gh(m),   T_e=id.

For any gauge Q, define

S_g(m)=Q_g⁻¹ T_g(m).

Then S_g is ψ_g-semilinear and

S_gS_h(m)=Q_g⁻¹φ_g(Q_h)⁻¹a_g,h T_gh(m)=b_g,h S_gh(m).

Thus a strictification of the ring weak action simultaneously strictifies every such compatible module. This is the module-map analogue of the source's LEFT-multiplication convention. It does not require or introduce a global module. Matrix conventions for right modules should be translated explicitly rather than reversing these products silently.

If M carries a filtration compatible with that of D, then S_g and T_g induce the same map on every associated graded piece: (Q_g⁻¹−1)F^sM⊆F^(s+1)M. In particular their actions on M/F^1M are identical. More generally any two-sided ideal J containing F^1 gives identical actions on M/JM. No topology or completeness on M is required for this conclusion or for defining S_g: the already constructed element Q_g⁻¹ acts algebraically on M.

In the local-ring setting, suppose D has maximal ideal 𝔪 and residue field k, with F^1⊆𝔪, and φ acts trivially on k. Then ψ acts trivially on k and the residue-fiber G-representation on M/𝔪M is literally unchanged. Thus all residual inertia characters, including any nontrivial root character, survive. Strictification cannot turn a sign representation into the trivial representation.

For Q,R and B as in Theorem B, multiplication L_B:M→M compares the two resulting strict module actions:

S^R_g = L_B S^Q_g L_(B⁻¹).

This is a semilinear equivalence over the algebra isomorphism Ad(B), and reduces to the identity modulo F^1M. It is generally not a D-linear equivalence over the identity of the ring. This distinction prevents a false assertion that the original literal action or its fixed subring was preserved.

## 7. Conditional invariant-frame corollary

Add the following hypotheses: D is local with residue field k; F^1⊆𝔪; the residual action on k is trivial; M is finite free as a left D-module; its given compatible weak action has trivial residual representation on M/𝔪M. Apply Theorem A and Section 6. The strictified module action has trivial residual representation. Averaging arbitrary lifts of a residue basis by m⁻¹Σ_g S_g gives invariant vectors with that same residue basis. Their coordinate matrix is invertible modulo 𝔪, hence invertible over D (the matrix Jacobson-radical criterion), so they form a free D-basis.

With A=D^ψ and N=M^S, that basis identifies N with a finite free left A-module and the natural map

D⊗_A N → M

is an isomorphism. Every original φ-stable two-sided ideal I is also ψ-stable, because inner conjugation preserves two-sided ideals. Averaging proves A→(D/I)^G is surjective, with kernel I∩A. The invariant frame then gives

N/(I∩A)N ≅ (M/IM)^G,

where the right-hand invariants use the **strictified** action S. This recovers the source's reduction-compatible finite-free statement without assuming D is flat over A.

Trivial residual inertia is indispensable to this argument. For a nontrivial residual character, Section 6 preserves that obstruction instead of removing it. An ideal I not containing F^1 is still preserved when originally stable, but the action on M/IM need not agree with the original weak action; only quotients containing F^1 have literal equality of residual maps.

## 8. Exact boundary of the new result

Proved: a normalized weak finite action with all coherence units in 1+F^1 admits a filtration-trivial strictification; the choices are related by a single filtration-trivial inner conjugacy; compatible module actions strictify simultaneously and retain their residual inertia; the source's invariant-frame descent applies when its local, finite-free, residue-trivial hypotheses also hold.

Not proved: that an actual transported mixed ambient has this complete filtered presentation, that its coherence units reduce to 1, that the required local modules exist and are free, that their residual inertia is trivial, that local gauges glue globally, or that the strictified fixed ring equals any preassigned literal coarse ambient. Comparisons are local equivalences over an inner algebra isomorphism, not an identification with the unchanged physical action. All retained physical values remain untouched.
