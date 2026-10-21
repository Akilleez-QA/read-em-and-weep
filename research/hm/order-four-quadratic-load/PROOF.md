# The unavoidable non-primary quadratic load at order four

## New result

Put A=H¹B(1), X=H¹B(2), T=H¹B(4), and let P_2 subset X, P_4 subset T be the actual primary cup images. For a cubic v define k_v=dim ker[v:A->T]. For a quadratic u define

s(u,v)=dim((uP_2+vA)/vA),
R(u,v)=T/(vA+uP_2).

Then multiplication by u induces an intrinsic map from the65-dimensional residual source N_2=X/P_2, and an exact sequence

N_2 --bar u--> R(u,v) -> Q4(u,v) ->0,
dim R(u,v)=30+k_v-s(u,v),
0<=s(u,v)<=4 rank[u:H¹F(0)->H¹F(2)]<=20.

Consequently the cubic-alone quotient always has dimension at least30, and the remaining map from the quadratic residual source always has a target of dimension at least10+k_v. In particular, if Q4=0, at least10 independent residual quadratic classes are indispensable. Direct primary quadratic coverage and cubic multiplication, even combined, can never cover H¹B(4).

This is an actual new obstruction to the seemingly plausible strategy of treating the cubic as the sole sufficient multiplier, or repairing it only with primary quadratic images. It does not assert that the lower bounds are attained for a selected or general pair.

## 1. Dimensions from the actual image/residue model

PR532 gives actual residue duals N_j*=D* tensor (H⁰O_C(5-j)/res S_(5-j)), and actual primary image P_j=U tensor H¹F(j-2). Primary HM cohomology gives dim H¹F(0)=5, dim H¹F(2)=10, and H¹F(-1)=0. Thus dim P_2=20, dim P_4=40, and P_1=0.

One may use PR463's known cubic/quartic restriction injectivity, but a shorter dependency route is available from the exact quintic result now proved in the PR538 refinement: I_C(5)=S_5^H. It implies I_C(4)=0 directly. Indeed if nonzero f lies in I_C(4), then for every linear form ell the quintic ell f is H-invariant. For h in H,

(h ell)(h f)=ell f.

For two independent linear forms ell_1,ell_2, elimination in the polynomial domain gives (h ell_1)ell_2=(h ell_2)ell_1. Coprimality forces h ell_i to be the same scalar multiple of ell_i. Since this holds for all independent pairs, h acts scalarly on S_1. Choosing a noncentral Heisenberg element contradicts the Schrödinger action. Therefore I_C(4)=0, and I_C(3)=I_C(1)=0 follow by multiplying a hypothetical lower-degree ideal section by a nonzero complementary form.

An alternative needs only dim I_C(5)=6, not its full invariant identification: two independent quartics p,q would give dim(S_1p+S_1q)>=9. Each summand has dimension5, and their intersection has dimension at most1 because the least common multiple has degree at least5 (degree5 permits only its scalar multiples in the intersection). Hence dim I_C(4)<=1. But I_C(4) is an H-subrepresentation of S_4 with nontrivial central character, so its dimension is a multiple of5 by the primary Heisenberg irreducible classification. It must therefore be zero. This is the dimension-only dependency route.

The disjoint25 lines have h⁰O_C(d)=25(d+1), so the actual residue identifications give

dim A=dim N_1=125-70=55,
dim N_2=100-35=65,
dim N_4=50-5=45,
dim T=40+45=85.

No selected restriction map is evaluated; the injection used here follows from the invariant-quintic identity and polynomial-domain argument.

## 2. Cubic-alone coverage is impossible by at least thirty dimensions

Rank-nullity for v:A->T gives

dim(T/vA)=85-(55-k_v)=30+k_v>=30.

This is unconditional for every cubic, including those in the cubic-good open for the DIFFERENT map H¹B(2)->H¹B(5). The latter open cannot remove this dimensional obstruction one degree lower.

There is a complementary primary interpretation. If the cubic residual map N_1->N_4 happens to be onto, its kernel has dimension55-45=10. These ten possible lifts can hit at most ten dimensions in the40-dimensional primary target, leaving at least30 full cubic-cokernel dimensions. If the residual map is not onto, the full lower bound still holds by rank-nullity. No residual surjectivity is asserted here.

## 3. Isolate the necessary quadratic residual contribution

Multiplication by u sends P_2 into P_4 naturally; under the actual cup injections its image has dimension4r_u, where r_u=rank[u:H¹F(0)->H¹F(2)]<=5. Some of this image may already lie in vA. Its image after quotienting by vA therefore has dimension s(u,v)<=4r_u<=20.

Hence quotienting the cubic cokernel by this entire direct primary quadratic contribution gives

dim R(u,v)=30+k_v-s(u,v)>=10+k_v.

The map x->ux modulo vA+uP_2 is constant on classes x modulo P_2, so it canonically descends to bar u:N_2->R(u,v). Its cokernel is exactly T/(vA+uX)=Q4(u,v). Thus Q4=0 if and only if this65-dimensional residual-source map is onto. In particular its required rank is precisely30+k_v-s(u,v), not merely whatever is needed to cover the residual target N_4.

Even without evaluating k_v or s, the intermediate quotient T/(vA+uP_2) has at least10 dimensions. Therefore no proof using only cubic coverage plus the quadratic primary source can establish Q4=0. At least10 independent classes from X/P_2 must participate in full coverage. If cubic multiplication has kernel, the minimum load increases by k_v; if the direct quadratic primary image has rank smaller than20 or intersects vA, it increases further.

The quotient formulation does not choose a splitting of primary and residual spaces and does not assume their extension is split. It is consequently compatible with all the primary cancellation mechanisms in PR535/538, while identifying a numerical load those mechanisms must meet in this specific order-four degree.

## 4. Exact linear coverage does not erase this obstruction

For a proper linear form ell, the new exact-linear theorem gives ell:H¹B(4)->H¹B(5) onto. Thus every cubic-good v can cover the degree-five target while the preceding degree-four cubic cokernel still has dimension at least30. There is no descent of that degree-five surjectivity to the lower degree. Likewise Q5=0 does not imply the displayed residual-quadratic map bar u is onto. This explains exactly why the new cubic-alone and linear classification results stop short of Q4.

## Sources, comparison, and boundary

Current PR1 was read through the exact-linear-failure update before this derivation. The distinct order-four summand and its dimensions are in PR463; general r=1 residue/Tor criteria are in PR532/534; primary lift corrections are in PR535/538. The present result does not claim these formulas as new. Its contribution is the cubic-alone impossibility, intrinsic reduced quadratic-source criterion, and unavoidable at-least-ten-dimensional non-primary quadratic load in the actual order-four quotient.

- PR532 residue model: https://github.com/Akilleez-QA/read-em-and-weep/blob/5f08a072fa8d3bdf12007a6aab2f374c85c5e503/research/hm/residue-restriction-ambiguity/PROOF.md
- PR463 order-four decomposition: https://github.com/Akilleez-QA/read-em-and-weep/blob/8ec3631dcd6937e6cc7491d0200c1c78b5d21434/research/hm/order-four-residue/PROOF.md
- PR538 exact-quintic refinement at3d0b833b1a22680a4ac1ea793fdeec378730de21: https://github.com/Akilleez-QA/read-em-and-weep/pull/538
- PR541 generic cubic and exact linear coverage: https://github.com/Akilleez-QA/read-em-and-weep/pull/541

No selected coefficient, HM/source matrix, rank evaluation, experiment, or claim of Q4 vanishing has been made.

## Exact statement in the project’s K grading

With K_j=H¹B(j-1) and L_j its actual primary submodule, put D(u,v)=K_5/(vK_2+uL_3) and N_3=K_3/L_3. Then

N_3 --u--> D(u,v) -> Q4(u,v) ->0,
dim D(u,v)=85-rank(v:K_2->K_5)-rank[uL_3 -> K_5/vK_2]>=10.

Thus Q4=0 if and only if this specific induced map N_3->D(u,v) is onto. The numerical necessary condition that its rank be at least10 is not itself sufficient; the full required rank is dim D(u,v). No selected value of either rank is asserted.
