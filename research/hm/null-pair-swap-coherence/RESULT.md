# Exact pair-swap coherence in the square-zero ambient

## Result and scope

The ordered first-order pair ambient admits an explicit central overlap gauge to a literally signed-permutation-equivariant representative. Transporting that genuine action back supplies exact group/Čech coherence on the original ordered representative, including the swap-square and deck-conjugation relations. External tensoring the two pairs over k[s,t]/(s²,t²) preserves all these identities with the mixed units retained.

This closes the missing ambient pair-swap coherence for the stipulated first-order pair ambients and their specified square-zero external product. It does not identify a coarse invariant algebra with the independently prescribed corrected downstairs ambient, verify every quotient-atlas descent hypothesis, construct a module, or evaluate any of the thirty retained values.

## Read sources and conventions

Historical context: [6264327093](https://github.com/Akilleez-QA/read-em-and-weep/pull/1#issuecomment-6264327093). That comment leaves precisely the ordered-cup quantum swap gauge and coherence open. The mathematical inputs are:

- [research/hm/null-actual-source-factorization/physical-factorization/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9bb53d934ad86e50d8519a35d663f9a96fa481d/research/hm/null-actual-source-factorization/physical-factorization/RESULT.md): the specified upstairs mixed product, F=id, and actual A=(1+s b_P)(1+t b_Q), with complementary-coordinate support.
- [research/hm/null-actual-source-factorization/classical-root/RESULT.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/c9bb53d934ad86e50d8519a35d663f9a96fa481d/research/hm/null-actual-source-factorization/classical-root/RESULT.md): the genuine product root and canonical full signed-permutation linearization; its §6 isolates the ordered-cup caveat.

Everything below is formal cochain, group-action, and nilpotent algebra reasoning. No physical source/model/jet evaluation, physical matrix product, import, experiment was performed.

Work in characteristic zero (in particular, 2 is invertible). Use the full ordered Čech nerve of a group-stable product cover, not an index ordering that must be re-sorted after applying a permutation. The factor cocycles q_1,q_2 are the pulled-back scalar degree-one cocycles, and transformations of their chart labels are included in every group action. They obey δq_a=0 literally. The pair swap exchanges q_1 and q_2 literally on this nerve. Deck inversion in factor a negates q_a and fixes the other q. These are properties of the stipulated factor representatives, not inferences from their cohomology classes.

If a later cover is not group-stable, replace it by the labeled family of its translates and their common refinements. All formulas restrict from the original product cover; no assertion that every refined open is Cartesian is needed. Repeated indices are allowed in the nerve, with q_a,ii=0. Overlap gauge cochains need not be alternating in their two chart labels.

Use

    (δc)_ijk = c_jk - c_ik + c_ij,
    (q_1 cup q_2)_ijk = q_1,ij q_2,jk.

For a central invertible overlap cochain u, fix the gauge convention

    F^u_ij = Ad(u_ij) F_ij = F_ij,
    A^u_ijk = u_ij u_jk A_ijk u_ik^(-1).

This convention sends candidate module transition matrices G_ij to u_ij G_ij; it fixes the direction of every gauge used below.

## 1. The exact primitive and its sign

Put r_ij=q_1,ij q_2,ij. Since q_a,ik=q_a,ij+q_a,jk,

    (δr)_ijk
      = q_1,jk q_2,jk
        - (q_1,ij+q_1,jk)(q_2,ij+q_2,jk)
        + q_1,ij q_2,ij
      = -q_1,ij q_2,jk - q_2,ij q_1,jk.

For b=λ(q_1 cup q_2), define

    c_ij = (λ/2) r_ij,
    b_alt = (λ/2)(q_1 cup q_2 - q_2 cup q_1).

Then the literal identity is

    b_alt = b + δc.                                      (1)

There is no appeal merely to graded commutativity in cohomology. In particular δb_alt=0.

## 2. An exact central gauge, not just a first-order class

Over k[s]/s², take μ=m+sπ/2, F=id, A=1+s b. Define

    u_ij = 1+s c_ij,       u_ij^(-1)=1-s c_ij.

The weighted scalar s c_ij is central for μ: every noncommutative multiplication correction acquires a second s and vanishes. Thus ordinary products of these units agree with star products, and the gauge leaves F and the chart products unchanged. Exactly,

    A^u = A δu = 1+s(b+δc) = 1+s b_alt.                  (2)

Here δu=u_ij u_jk u_ik^(-1). The actual multiplicative Čech cocycle identity follows from δb_alt=0 and s²=0. These are the triple units themselves, not just their inner automorphisms.

## 3. Genuine action in the antisymmetrized representative

Let W_2=(Z/2)^2 semidirect S_2. Use a left action T_g on functions and cochains, for example pullback by g^(-1), so T_g T_h=T_gh. On the parameter set

    T_g(s)=χ(g)s,
    χ(g)=ε_1 ε_2 sign(σ)

for a signed permutation g=(ε,σ). The pair bivector π has this same character. The antisymmetrized scalar cocycle b_alt also has character χ: each inversion contributes its factor sign and the swap reverses the antisymmetrization.

Consequently μ, F=id, and A_alt=1+s b_alt are all invariant under the combined geometric/parameter action. The maps T_g are genuine algebra maps between the corresponding charts, compose exactly, commute with restrictions, and preserve the actual Čech triple units. Group-composition coherence units can be chosen to be 1.

In particular, for the swap τ,

    T_τ(s)=-s,  T_τ(π)=-π,
    T_τ(b_alt)=-b_alt,
    T_τ(c)=c,  T_τ(u)=u^(-1).

For either deck generator d, both s and c change sign, so T_d(u)=u. All statements include transformed cover labels.

## 4. Transport back: explicit weak-action cochains

Write A for the original ordered unit. Since A_alt=A δu is invariant,

    T_g(A) δ(T_g u) = A δu.

Define the central overlap cochain

    v_g = (T_g u) u^(-1).                              (3)

Then

    δv_g = A (T_g A)^(-1).                             (4)

Thus v_g is the gauge FROM the transformed ordered representative T_g(A) TO A: applying the stated gauge convention to T_g(A) gives A. This direction is essential.

An equivalent operational specification is to first send G to uG, apply T_g, then return by u^(-1). The resulting transition system is

    G |-> v_g T_g(G).

If G satisfies its row-module equation G_jk ⋆ G_ij = A_ijk ⋆ G_ik, then

    (v_g,jk T_g G_jk) ⋆ (v_g,ij T_g G_ij)
      = A_ijk ⋆ (v_g,ik T_g G_ik)

by (4). This is a conditional transport identity for arbitrary candidate transitions; it asserts no module exists.

The entire group law is exact at overlap level:

    v_g T_g(v_h)
      = (T_g u)u^(-1) (T_gh u)(T_g u)^(-1)
      = (T_gh u)u^(-1)
      = v_gh.                                         (5)

Centrality justifies the indicated cancellations. Also v_e=1. Equations δA=1, (4), and (5) are the Čech, mixed group/Čech, and group/group coherence equations. They give coherent action data with group-composition modification 1, rather than merely a projective action detected modulo the center. All higher associativity follows from (5) and T_g T_h=T_gh; all identities commute with restriction.

For the generators specifically,

    v_τ = u^(-2) = 1-2s c
        = 1-sλ q_1,ij q_2,ij,
    v_d1 = v_d2 = 1.

The swap square has no residual central unit:

    v_τ T_τ(v_τ) = 1.

Since T_d(v_τ)=v_τ for either deck generator,

    v_τ T_τ(v_d1) T_(τd1)(v_τ)
      = v_τ T_τ(v_τ) = 1 = v_d2.

Together with the exact geometric/parameter relation τd1τ=d2, this verifies deck conjugation, including its coherence multiplier. Deck squares and deck commutation are immediate. The same calculation covers the other conjugation relation. Thus the weak action on the original presentation is explicitly equivalent to the genuine action on the antisymmetrized one.

## 5. External product modulo (s²,t²): all cross units retained

For pairs P=12 and Q=34, use their respective b_P,c_P,u_P and b_Q,c_Q,u_Q with parameters s,t. The specified ambient is

    μ = m[1+sD_P/2+tD_Q/2+st D_P D_Q/4],
    F = id,
    A = (1+s b_P)(1+t b_Q).

The combined gauge is

    U = u_P u_Q
      = 1+s c_P+t c_Q+st c_P c_Q,
    U^(-1) = 1-s c_P-t c_Q+st c_P c_Q.                (6)

Every unit here is central for this mixed product. For example the possible correction to multiplication by s c_P involving D_P is divisible by s², and the one involving D_Q vanishes because c_P is supported on pair P. The same argument works for t c_Q. Corrections to the st term vanish by s²=t²=0. This uses exactly the complementary-factor support already established in the factorization audit.

Hence the full transformed triple unit is

    A_alt = A δU
          = (1+s b_P,alt)(1+t b_Q,alt)
          = 1+s b_P,alt+t b_Q,alt+st b_P,alt b_Q,alt. (7)

Its pentagon is the tensor product of the two actual pair pentagons. Both the gauge cross term in (6) and the triple-unit cross term in (7) are necessary; neither can be discarded by first-order reasoning.

For W_2 x W_2 the action on this representative is genuine. Transporting back gives

    V_g=(T_g U)U^(-1),
    δV_g=A(T_g A)^(-1),
    V_g T_g(V_h)=V_gh.                                (8)

If v_gP=1+s a_gP and v_gQ=1+t a_gQ are the two pair cochains, then

    V_g = v_gP v_gQ
        = 1+s a_gP+t a_gQ+st a_gP a_gQ.

For the simultaneous inner swap τ_P τ_Q this becomes

    V_(τPτQ)
      = (1-2s c_P)(1-2t c_Q)
      = 1-2s c_P-2t c_Q+4st c_P c_Q.                 (9)

The two inner swaps commute with their full units included. Each square is 1 and conjugation of either pair's deck generators is exact. These follow either directly from the separated supports or from (8).

If block exchange is included, interchange s and t and the two identically normalized pair presentations. Then U and A_alt are invariant under block exchange, its V is 1, its square is 1, and it conjugates the pair actions exactly. This gives the block-preserving signed-permutation subgroup (W_2 x W_2) semidirect S_2. No action of permutations taking the prescribed pair partition to a different partition is asserted for this two-parameter family.

## 6. What this supplies to root transport, and what remains

The above is actual restriction-compatible ambient group/Čech coherence on the chosen invariant cover and its refinements. Combined with the already proved genuine root-line groupoid cocycle, it supplies the input ambient action to the universal root/Morita change-of-ambient formulas. Those formulas can now be applied on both group and Čech arrows, retaining all their noncommutative order and mixed units. The resulting root-transported action may again be weak; its coherence follows from the genuine input identities, not merely from equality of inner automorphisms.

This does not by itself supply every effective quotient-atlas or overlap-bimodule residue-inertia hypothesis. Nor does it identify coefficient ideals, multiplication, or full triple units with a separately proposed corrected P² x P² ambient. Classical root inertia cancellation is not existence of an equivariant quantum module. These comparison and module obligations remain open, and all thirty retained obstruction values remain unknown.
