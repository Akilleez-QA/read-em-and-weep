# Generic quartic and quintic multiplication: the exceptional-image obstruction

## New deductions and notation

Use the actual graded extension from PR538:

0 -> L -> K -> N -> 0,
K_j=H^1(B(j-1)), L_j=U tensor H^1(F(j-3)),
N subset P, P_j=D tensor M_(6-j)^*, M_d=H^1(I_C(d)).

The discrepancy E=P/N is supported in degree one and has dimension six. In particular L_1=L_2=0, K_1=N_1, K_2=N_2=P_2, and N_6=P_6. The target primary subspace L_6 has dimension eight.

We prove generic full-Rao residual surjectivity for quartics and quintics. For actual quintic multiplication we obtain an exact two-part obstruction and, in particular, prove that full cohomological surjectivity is impossible. None of these assertions evaluates a selected polynomial or a selected multiplication map.

## 1. Generic full-Rao surjectivity in degrees four and five

For e=4 or 5, put W_e=S_e and let U_l^(e) be the image of H^0(O_l(e))^* in W_e^*. Each has dimension e+1. The rank function r_e(A)=dim(sum_(l in A) U_l^(e)) is invariant under the primitive normalizer action on the 25 lines. Write R_e=r_e(C).

PR541's coarsest-optimal-partition argument gives

tau_e=min(25e,R_e-1).

For e=4, R_4<=dim S_4=70, so tau_4=R_4-1. For e=5, R_5<=dim S_5=126, so R_5-1<=125=25e and again tau_5=R_5-1. Equality of the two candidate partition costs causes no problem: the formula uses a minimum, not a strict inequality.

For f nonzero on every component, define

F_f={g in S_e : g|l belongs to C(f|l) for every l}.

The admissible residue tuples modulo diagonal constants are F_f/(I_C(e)+C f). The generic-hyperplane theorem therefore gives their generic dimension R_e-1-tau_e=0, without requiring injective global restriction. Dualizing yields a nonempty Zariski-open locus Omega_e on which

f:P_(6-e) -> P_6 is surjective.

This is full-Rao surjectivity. In degree five the source is P_1, not its proper actual-image subspace N_1.

## 2. Quartics: a pure primary lift obstruction

Let g belong to Omega_4. Since K_2=N_2=P_2 and N_6=P_6, the actual multiplication diagram has exact rows

0 -> 0 -> K_2 -> P_2 -> 0,
0 -> L_6 -> K_6 -> P_6 -> 0.

Let T_g=ker(g:P_2 -> P_6). The actual extension gives the lift boundary

delta_g:T_g -> L_6.

Concretely, a residual class t has a unique lift to K_2 because L_2=0. Multiplication by g sends that lift into L_6; this is delta_g(t). The snake lemma gives

0 -> ker(g:K_2 -> K_6) -> T_g --delta_g--> L_6
  -> coker(g:K_2 -> K_6) -> 0.

Consequently the generic-residual-open quartic defect is exactly L_6/im(delta_g), of dimension at most eight. Actual quartic surjectivity is equivalent to delta_g being onto. Residual surjectivity alone does not establish that condition. No rank for delta_g is asserted here.

## 3. Quintics: exceptional image before the primary boundary

Let f belong to Omega_5. Set

T_f=ker(f:P_1 -> P_6), E=P_1/N_1,
rho_f:T_f -> E,
A_f=ker(rho_f), B_f=coker(rho_f).

The map rho_f is the restriction of the quotient map P_1 -> E. The snake lemma for N subset P gives

0 -> ker(f:N_1 -> P_6) -> T_f --rho_f--> E
  -> coker(f:N_1 -> P_6) -> 0.

Thus A_f and B_f are precisely the kernel and cokernel of actual residual multiplication. In particular, full-Rao surjectivity lifts to actual residual surjectivity if and only if rho_f is onto. This is a concrete exceptional-image obstruction, distinct from the primary lift boundary.

Equivalently, dualizing the actual residual map gives the transversality criterion

im(f^*:P_6^* -> P_1^*) intersect E^* = 0,

where E^* is canonically embedded in P_1^*. On Omega_5, f^* is injective, so this intersection has dimension dim B_f. After retaining the common determinant factor, this is the intersection of fM_0 with the exceptional six-dimensional subspace of M_5. No arbitrary splitting of P_1 is involved.

Because K_1=N_1, the actual primary extension supplies

delta_f:A_f -> L_6.

For a in A_f, use its unique lift in K_1 and multiply by f; its image lies in L_6. There is an exact sequence

0 -> ker(f:K_1 -> K_6) -> A_f --delta_f--> L_6
  -> coker(f:K_1 -> K_6) -> B_f -> 0.

Equivalently, the cohomological cokernel has the exact obstruction filtration

0 -> L_6/im(delta_f) -> coker(f:K_1 -> K_6) -> B_f -> 0.

In purely algebraic terms, full cohomological surjectivity would require both rho_f and delta_f to be onto. The HM dimensions below show that these conditions cannot hold simultaneously.

## 4. The quintic obstruction cannot disappear

Use the already established quintic saturation I_C(5)=the six independent minors. Since C is 25 disjoint lines,

R_5=126-6=120,
dim M_5=25*6-120=30,
dim P_1=30,
dim P_6=dim M_0=25-1=24.

It follows that dim T_f=6 on Omega_5. Also dim E=6 and dim N_1=24. Hence dim A_f=dim B_f=:a_f, with 0<=a_f<=6.

The exact sequence above yields

dim coker(f:H^1(B(0)) -> H^1(B(5)))
  =8+a_f-rank(delta_f)
  =8+dim ker(f:H^1(B(0)) -> H^1(B(5))).

In particular this cokernel has dimension between eight and fourteen on Omega_5. It never vanishes. Indeed the source has dimension 24 while the target has dimension 24+8=32, so no quintic whatsoever can give full cohomological surjectivity, whether or not it belongs to Omega_5.

If rho_f is onto, it is an isomorphism between six-dimensional spaces. Then A_f=B_f=0, and actual residual multiplication N_1 -> P_6 is an isomorphism. The actual cohomological image fK_1 is consequently a complement to L_6 in K_6, and its cokernel is canonically identified with L_6 through the inclusion of the latter. It does not cover the primary target.

More generally, an actual quintic map is injective on Omega_5 exactly when delta_f is injective on A_f. This is the sharp eight-dimensional-cokernel criterion, and it is weaker than actual residual surjectivity. No such injectivity or transversality is claimed for a generic or selected quintic here.

## Scope and sources

Current PR1 was read before beginning. Its latest relevant update identifies PR541's already published generic linear/quadratic corollaries at cc906bec64ce411c87c67a1add4b1bbcb355c7be; they are not reproduced as new results here.

- PR541, primitive partition closure and generic-hyperplane residual formula: https://github.com/Akilleez-QA/read-em-and-weep/pull/541 . The generic-hyperplane theorem and primitive action are imported as established there, not claimed new here.
- PR538, actual image extension and six-dimensional exceptional correction, commit 3d0b833b1a22680a4ac1ea793fdeec378730de21: https://github.com/Akilleez-QA/read-em-and-weep/pull/538 .
- The required quintic saturation is rederived in PR538's DEGREE-ONE-CORRECTION.md at the above pin; this avoids importing the older complete-resolution chain.

No selected coefficients, maps, ranks, primary boundaries or original-pair memberships were evaluated.  The new output is the quartic/quintic residual consequence and the exact exceptional-plus-primary obstruction, including the unavoidable quintic cohomological defect. It is not an assertion of complete proof repair.
