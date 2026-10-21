# Low second Chern class does not exclude the reflexive rank-three case

## Result

Stable reflexive rank-three sheaves F on complex P^4 with c1(F)=-1 and c2(F)=2 do exist, even with singular locus of codimension four. Hence those numerical invariants and slope stability alone cannot exclude the normalized rank-seven evaluation kernel.

There is nevertheless a new restricted equivariant exclusion: the particular two-relation linear-resolution class constructed below cannot have the normalizer linearization required of the actual kernel K. This does not classify all sheaves with c1=-1,c2=2 and does not exclude the full remaining rank-seven alternative.

## 1. A symbolic stable reflexive example

Use homogeneous coordinates x_0,...,x_4 and arbitrary pairwise distinct complex scalars lambda_0,...,lambda_4. Define

alpha:2O(-2) -> 5O(-1)

whose i-th row is (x_i, lambda_i x_i), and put F=coker(alpha). The 2-by-2 minors are

(lambda_j-lambda_i)x_i x_j, i<j.

Thus alpha has rank two away from the five coordinate points and rank one at each of them. Its generic rank is two, so it is injective as a sheaf map and

0 -> 2O(-2) -> 5O(-1) -> F -> 0                         (1)

is exact. This is an independent symbolic family, not the HM evaluation map and not a numerical test of any selected instance.

### Reflexivity

Away from the five points, F is locally free of rank three. Near the i-th point, x_i is invertible; elementary elimination splits off the corresponding unit entry of alpha. The local presentation becomes

0 -> R -> R^4 -> F_p -> 0,

where the first map is the column of four regular parameters, multiplied by nonzero constants. Its cokernel is nonfree and has projective dimension one and depth three over the regular local ring R of dimension four. It is torsion-free: a scalar multiple of the parameter column can belong to R^4 only with scalar in R, since the parameters have no common irreducible divisor. Therefore F is torsion-free, locally free in codimension one, and satisfies S2. It is reflexive. Its singular locus is exactly those five points.

### Slope stability

The resolution gives H^0(F(-d))=0 for all integers d>=0, using H^1(O(-2-d))=0. Dualizing and twisting gives the left-exact sequence

0 -> F^*(-1-d) -> 5O(-d) -> 2O(1-d).

For d>0 its middle space has no sections. For d=0, the induced map on constants sends (a_i) to

(sum_i a_i x_i, sum_i lambda_i a_i x_i),

and its first component already makes it injective. Thus H^0(F^*(-1-d))=0 for every d>=0.

Now mu(F)=-1/3. A destabilizing rank-one or rank-two saturated subsheaf must have determinant O(d) with d>=0. Its determinant map extends to the reflexive hull of the relevant exterior power. In rank one it contradicts H^0(F(-d))=0. In rank two, use

(Lambda^2 F)** = F^* tensor det(F)=F^*(-1)

to contradict H^0(F^*(-1-d))=0. Hence F is slope-stable.

### Chern classes

Equation (1) gives

c(F)=(1-h)^5/(1-2h)^2
     =1-h+2h^2+2h^3+5h^4.

In particular F has the requested first two Chern classes. Its twist K=F(-1) has

c(K)=(1-2h)^5/(1-3h)^2
     =1-4h+7h^2-2h^3+5h^4.

The nonzero fourth Chern class of this rank-three reflexive sheaf illustrates precisely why a rank-three vector-bundle Chern-class obstruction cannot be applied without local freeness.

## 2. The required normalizer linearization excludes this resolution class

Now impose the actual normalizer conventions as separate inputs: X=P(A_0) with A_0=V_3, the center has weight three on A_0 and weight two on H^0(O(1))=A_0^*, and the actual kernel K has central weight four. Let H be the Heisenberg subgroup; its nontrivial characters of H/Z(H) form a normalizer orbit of size 24.

Suppose this K had a resolution of the same form as the example's twist,

0 -> R_2 tensor O(-3) -> B_5 tensor O(-2) -> K -> 0,    (2)

with dimensions dim R_2=2 and dim B_5=5. The coefficient representations are intrinsic: B_5=H^0(K(2)), and R_2 is the degree-three linear relation kernel of multiplication B_5 tensor H^0(O(1)) -> H^0(K(3)). Thus a linearization of K induces normalizer representations and makes the relation map equivariant; one need not choose an equivariant resolution arbitrarily.

The central weight of B_5 is 4+2*2=3 modulo five. Its five-dimensional Heisenberg representation is therefore A_0. Consequently

(B_5 tensor H^0(O(1)))^H = End(A_0)^H

has dimension one, by irreducibility of the Schrödinger representation.

The central weight of R_2 is 4+2*3=0. Since dim R_2=2<24, normalizer invariance excludes every nontrivial H/Z(H) character. Thus R_2 is H-trivial. Its equivariant inclusion into B_5 tensor H^0(O(1)) would have image in that one-dimensional invariant space. This contradicts its dimension two.

Equivalently, both relation columns would be scalar multiples of the single tautological column, and could not define an injective rank-two sheaf map. Therefore no sheaf in resolution class (2) carries the required actual normalizer linearization.

This exclusion requires only the stated Heisenberg weights, orbit size and irreducibility; it does not evaluate either determinant channel of the actual evaluation map.

## 3. Exact classification boundary and sources

The existence statement and restricted equivariant exclusion above are proved directly. No claim is made that every stable reflexive sheaf with c1=-1,c2=2 has resolution (1). That missing classification is exactly what would be needed to promote the restricted exclusion to exclusion of the entire normalized c2=2 case. The normalized c2=7 case is untouched.

The following primary source was inspected:

C. Bertone and M. Roggero, 'Positivity of Chern classes for reflexive sheaves on P^N', arXiv:0709.3218v2, especially Introduction and Section 2, Lemma 2.1:
https://arxiv.org/pdf/0709.3218v2 .

It explicitly distinguishes higher Chern classes of reflexive sheaves from those of vector bundles, records preservation of reflexivity under a general linear restriction, and identifies the restricted singular locus. Its positivity and near-minimal classification theorems impose generation hypotheses; they are not a classification of arbitrary normalized stable sheaves with the invariants here. General restriction also does not, by that lemma alone, establish slope stability of the restriction.

A located P^4 classification source, 'Stable rank three vector bundles on P^4 with Chern classes (-2,4,0)', Journal of Pure and Applied Algebra 207 (2006), 299-317, explicitly concerns vector bundles and different Chern data:
https://www.sciencedirect.com/science/article/pii/S0022404905002422 .
Its scope cannot be silently extended to the reflexive kernel. No numerical nonexistence claim from it is used.

Current PR1 was read first. The work is confined to the remaining primary-evaluation rank-seven reflexive-sheaf issue. No selected HM coefficients, rank tests, or derived-excess calculations were performed.
