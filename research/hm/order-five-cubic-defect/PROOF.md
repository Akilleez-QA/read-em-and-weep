# The order-five paired endpoint and its missing cubic contribution

Work over C on Y=P^4. Let F be the normalized Horrocks–Mumford bundle, B=End_0(F), and M_j=H^1(F(j)). Retain the fixed regular sequence u=t_2, v=t_3 of degrees two and three and the paired coefficient conventions of PR437. All cohomology below is on Y unless specified.

The whole paired order-five group has dual Q_5 plus Q_5, where

    Q_5 = H^1(B(5))/(u H^1(B(3)) + v H^1(B(2))).

Unlike the degree-six endpoint, this quotient cannot be reduced by simply replacing the primary module by M/(u,v)M. We construct an exact sequence

    C_2 --delta_v--> P_5 -> Q_5 -> 0,

where P_5 is an explicit primary-module cokernel and C_2 is a concrete section-resolution cohomology defect of dimension between 65 and 70. Its cubic connecting map must be retained. We also prove h^1(B(5))>=32, excluding an extension of the degree-six zero-target strategy to degree five. Neither Q_5 nor delta_v is evaluated.

## 1. Inputs and kernel sequences

Use the exact section resolution and primary cohomology pinned in PR167 and PR440:

    0 -> 2O(-8) -> 20O(-6) -> 35O(-5)
      -> 15O(-4) + 4O(-3) -> F -> 0.

Here F^vee=F(1), H^0(F(s))=0 for s<3, M is generated in degree zero with dimensions (5,10,10,2) in degrees 0,1,2,3 and zero elsewhere. H^2(F(s)) is zero except at s=-2, where its dimension is two. Serre duality gives H^3(F(s))=M_{-s-4}^vee and H^4(F(s))=H^0(F(-s-4))^vee.

Tensoring the section resolution by F^vee(t) resolves G(t)=End(F)(t), with

    E_0(t)=15F(t-3)+4F(t-2), E_1(t)=35F(t-4),
    E_2(t)=20F(t-5),         E_3(t)=2F(t-7).

Put K(t)=im(E_1(t)->E_0(t)) and L(t)=im(E_2(t)->E_1(t)). Thus

    0 -> E_3(t) -> E_2(t) -> L(t) -> 0,
    0 -> L(t) -> E_1(t) -> K(t) -> 0,
    0 -> K(t) -> E_0(t) -> G(t) -> 0.                 (1)

These are twists of fixed sheaf sequences, so their cohomology maps commute with polynomial multiplication. The trace splitting identifies positive intermediate cohomology of G(t) and B(t). PR440 proves H^2(K(t))=0 and the natural surjection p_t:H^1(E_0(t))->H^1(B(t)) for t>=3. PR167 gives H^2(B(t))=0 for t>=2. PR450 proves H^1(B(6))=0 structurally.

## 2. Exact whole paired endpoint

PR437 identifies the actual filtered coefficient at order five as

    B(-3)K_4 + B(-4)K_3 + B(-5)K_2,
    K_n=(u^a v^b : 2a+3b>=n).

The relevant resolutions are

    0 -> O(-7)+O(-8) -> O(-4)+O(-5)+O(-6) -> K_4 -> 0,

with columns (v,-u,0) and (0,v,-u),

    0 -> O(-7) --(u^2,-v)--> O(-3)+O(-4) -> K_3 -> 0,
    0 -> O(-5) --(v,-u)--> O(-2)+O(-3) -> K_2 -> 0.

Regularity of (u,v) ensures exactness globally, including the collision surface. Tensor these by B(-3), B(-4), and B(-5), respectively. The generator terms have twists (-7,-8,-9), (-7,-8), and (-7,-8); their H^2 vanish by Serre duality and H^2(B(t))=0 for t>=2.

The dual H^2 groups are therefore cokernels of the transpose syzygy maps on H^1. Their targets are respectively

    H^1(B(5))+H^1(B(6)), H^1(B(6)), H^1(B(5)).

PR450 kills every degree-six summand. In the first case the surviving map is (a,b,c)->va-ub from degrees 2,3,4; in the last it is (a,b)->va-ub from degrees 2,3. Each cokernel is Q_5. The middle group vanishes. Finite pushforward and exact character projection now give

    H^2(Z,I_D^5 E_pair)_chi^vee = Q_5 + Q_5.          (2)

All incoming images are retained. This is a whole-coefficient statement, not an assertion about its image in unrestricted cohomology or an actual source.

## 3. The degree-five primary presentation

At t=5, the first sequence in (1) gives H^2(L(5))=0: both H^2(E_2(5))=20H^2(F(0)) and H^3(E_3(5))=2M_{-2}^vee vanish. Hence H^1(E_1(5))->H^1(K(5)) is surjective. Since H^2(K(5))=0, the last sequence yields

    35M_1 --D_5--> 15M_2 + 4M_3 -> H^1(B(5)) -> 0. (3)

D_5 contains BOTH the linear block into 15M_2 and the quadratic block into 4M_3 of the section-resolution differential. Neither may be omitted.

The surjection p_3 has source 15M_0+4M_1. Define p_2 by the same cohomology construction, but do NOT assume it is surjective; its source is only 4M_0. Naturality proves that quotienting (3) by u im(p_3) and v im(p_2) gives

    35M_1 --D'_5--> 15(M_2/uM_0)
                    +4(M_3/(uM_1+vM_0)) -> P_5 -> 0,          (4)

and canonically

    P_5 = H^1(B(5))/(uH^1(B(3))+v im(p_2)).          (5)

The reduced map D'_5 is induced by D_5. No claim about its rank is made.

## 4. A necessarily large degree-two defect

At t=2, (1) gives canonical identifications

    H^2(L(2)) = 2M_1^vee,   H^3(L(2))=0.

Indeed H^2(E_2(2))=0, H^3(E_3(2))=2M_1^vee, H^3(E_2(2))=0, and H^4(E_3(2))=2H^0(F(1))^vee=0. Also H^1(E_1(2))=35M_{-2}=0. Thus the middle sequence in (1) gives

    0 -> H^1(K(2)) -> 2M_1^vee --a_2-->
         35H^2(F(-2)) -> H^2(K(2)) -> 0.             (6)

Its two central spaces have dimensions 20 and 70. Write r=rank(a_2). The first two vanishings H^0(E_0(2))=0 and H^2(E_0(2))=0 give, from the last sequence in (1),

    0 -> H^0(G(2)) -> H^1(K(2)) -> 4M_0 --p_2-->
         H^1(B(2)) -> H^2(K(2)) -> 0.               (7)

The scalar summand O(2) of G(2) supplies 15 independent sections. Therefore dim H^1(K(2))=20-r>=15, so 0<=r<=5. In particular

    C_2 := coker(p_2) = H^2(K(2)) = coker(a_2),
    dim C_2 = 70-r,          65<=dim C_2<=70.        (8)

This uses no value of H^0(B(2)), no selected differential rank, and no tensor-cohomology table. In particular p_2 is provably NOT surjective. Its omission is not a harmless extension of PR440's t>=3 surjectivity range.

## 5. The retained cubic connecting map and exact criterion

For c in C_2 choose b in H^1(B(2)) mapping to c under (7), and set

    delta_v(c) = class of vb in P_5.                (9)

Changing b by im(p_2) changes vb by v im(p_2), which is zero in (5). Thus (9) is well-defined and canonical relative to the fixed resolution and quotient identifications. Equivalently it is the map induced by multiplication by v between the cohomology sequences of (1) at degrees two and five, after quotienting the degree-five primary image by u and v im(p_2). Formula (7) explicitly supplies its domain and lifts; no arbitrary splitting is chosen.

Its image is exactly the image of vH^1(B(2)) in P_5. Consequently

    C_2 --delta_v--> P_5 -> Q_5 -> 0                (10)

is exact. Thus order-five whole-coefficient vanishing is equivalent to surjectivity of this specific cubic connecting map onto the cokernel (4). P_5=0 is sufficient but not necessary. A nonzero P_5 alone does not prove Q_5 nonzero. The nonzero defect C_2 does not prove that delta_v has nonzero image: that image remains an unresolved mathematical dependency.

The elementary dimension consequences are

    max(0,dim P_5-70) <= dim Q_5 <= dim P_5,
    dim Q_5 = dim P_5-rank(delta_v).

These distinguish missing cubic source classes from the primary multiplication quotient; they do not replace either incoming map by a dimension count.

## 6. A root-cause exclusion at degree five

The degree-six proof cannot simply be repeated with a vanishing target: H^1(B(5)) is necessarily nonzero. Here is a calculation from the Chern classes, not an imported cohomology table.

For normalized F, c_1(F)=-H and c_2(F)=4H^2. The splitting principle gives

    ch(B)=3-15H^2+(75/4)H^4.

On P^4, the coefficient of H^2 in exp(tH)td(P^4) is t^2/2+5t/2+35/12. Riemann–Roch therefore gives

    chi(B(t))=3 binom(t+4,4)
               -15(t^2/2+5t/2+35/12)+75/4,
    chi(B(5))=-22.

H^2(B(5)) vanishes by PR167. To check H^3 and H^4 without further input, use (1): H^3(E_0(5))=0 and H^4(E_1(5))=0, while groups in degrees five or higher vanish by dimension. This proves H^3(G(5))=0. Likewise H^4(E_0(5))=0 proves H^4(G(5))=0. Trace splitting gives the same vanishings for B. It follows that

    h^1(B(5))=h^0(B(5))+22.                         (11)

In fact h^0(B(5))>=10. Set E_HM=F(3), so h^0(E_HM)=4 and H^0(E_HM(-1))=0 by the primary table. The rank-two identity End_0(F)=Sym^2(F)(1) identifies B(5)=Sym^2(E_HM). Lemma 4.10 of Horrocks–Mumford (printed p. 73) proves that two linearly independent global sections of such a bundle have nonzero wedge. Its proof uses the saturated rank-one subsheaf and its line-bundle bidual, together with H^0(E_HM(-1))=0.

We claim Sym^2 H^0(E_HM)->H^0(Sym^2(E_HM)) is injective. If a nonzero quadratic relation existed, a constant change of basis over C would put it in rank-one, rank-two, rank-three, or rank-four normal form. Regard the resulting sections s_i at the generic point as binary linear forms over K=C(P^4); nonzero global sections remain nonzero there.

- Rank one has form s_1^2=0 and rank two has form s_1s_2=0, both impossible in the polynomial domain K[X,Y].
- Rank three has form s_1^2=s_2s_3. The independent global pair s_1,s_2 has nonzero wedge, so these linear forms are nonproportional and coprime. Then s_2 cannot divide s_1^2, contradiction.
- Rank four has form s_1s_4=s_2s_3. Again s_1,s_2 are coprime. Thus s_1 divides s_3, so s_3=f s_1 for f in K. This makes their wedge zero, contrary to Lemma 4.10 for the globally independent pair s_1,s_3.

All ten symmetric products are therefore independent. Equation (11) proves

    h^1(B(5)) >= 10+22 = 32.                        (12)

This is only a lower bound; equality is not asserted.

This rigorously excludes the zero-target route at degree five. It does NOT exclude surjectivity of the incoming (u,v) map or prove order-six optimality. The next question is genuinely the quotient (10), rather than vanishing of its ambient H^1 target.

## Dependencies, review boundary, and next ownership

- PR450, structural H^1(B(6)) vanishing, commit 54d1eafe617e042edc452cb66edb8e4f7c78d2bf:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/54d1eafe617e042edc452cb66edb8e4f7c78d2bf/research/hm/endpoint-structural-vanishing/PROOF.md
- PR437, exact paired filtration, commit 50e82ed233cd7729c38608194f990376eb832418:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/50e82ed233cd7729c38608194f990376eb832418/research/hm/paired-collision-filtration/PROOF.md
- PR439, retained transpose-syzygy endpoint method, commit bf6ce91fd73fbc96cb8ede65448dfedbc0328c7b:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/bf6ce91fd73fbc96cb8ede65448dfedbc0328c7b/research/hm/paired-collision-endpoint/PROOF.md
- PR440, kernel sequences and natural primary surjections for t>=3, commit 829e03411d04511f6cf04860bf18db4a70b12448:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/829e03411d04511f6cf04860bf18db4a70b12448/research/hm/degree-six-structural-reduction/PROOF.md
- PR167, primary cohomology and section resolution, commit 063da90fc4543304e87e701cdefcc08225412f17:
  https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/PROOF.md
  https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md

Primary references are Horrocks–Mumford (1973), https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf, and Decker (1990), Remark 2, https://www.numdam.org/article/CM_1990__76_1-2_7_0.pdf. The Chern classes use the normalized convention c_1=-1,c_2=4.

Current PR1 and PR437/439/440/450 were read on 2026-10-20. This bounded comparison does not claim an exhaustive novelty search. The concrete defect (6)-(10) and zero-target exclusion (12) go beyond merely renaming the endpoint. Next ownership is structural analysis of D'_5 and delta_v; actual-source filtration membership remains separate. No selected HM/source map, matrix, rank, generator, checker, or large computation was evaluated. No actual primitive, six-pure-condition result, module lift, algebraicity, or order-six optimality is asserted. Mathematical text review is distinct from formal verification.
