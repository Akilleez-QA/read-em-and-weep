# Exterior multiplication forces the column channel to be nonzero

## Inputs and result

Work over C with the actual normalizer action, the five-dimensional space T, and the parameter line P=P(W'^*). We use the following exact dependencies:

- [Column parity blocks, PR526, c887d466428bced729a73bbc8578a889e9ecaf45](https://github.com/Akilleez-QA/read-em-and-weep/blob/c887d466428bced729a73bbc8578a889e9ecaf45/research/hm/column-parity-blocks/PROOF.md): the reduced column differential is phi=alpha direct sum beta, where alpha:U tensor O -> T4 tensor O(2) is everywhere injective with cokernel O(8), and beta:R6 tensor O -> (W0+Qspin) tensor O(2). The column parameter is u(lambda)=5 dim ker(beta_lambda).
- [Single-channel reduction, de70cfc2807897b350aeda600e552f6b6a93a300](https://github.com/Akilleez-QA/read-em-and-weep/blob/de70cfc2807897b350aeda600e552f6b6a93a300/research/hm/column-single-channel/PROOF.md): constant u=5 is impossible, and constant u=10 is equivalent to the vanishing of the W0 component gamma of beta. If gamma is nonzero, the only remaining pattern is u=0 off the unique twelve-point orbit Omega and u=5 on Omega; the determinant of beta has reduced divisor Omega.
- [Actual target decomposition, PR453, 56516a96a7eacfde0c8e272ca38db415cc7f294b](https://github.com/Akilleez-QA/read-em-and-weep/blob/56516a96a7eacfde0c8e272ca38db415cc7f294b/research/hm/cubic-invariant-target/PROOF.md): Lambda2(T)=E tensor W0 and E tensor Lambda2(T)=V tensor (W0+Qspin+T4), with V=Lambda4(T).

The actual multiplication mu_lambda:Sym2(T) -> E is nonzero for every parameter: under Sym2(T)=E tensor Sym2(W'), it is binary evaluation at the nonzero parameter, up to the harmless one-dimensional fiber O(2)|lambda. These identifications and representations are those of [Horrocks--Mumford (1973)](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf), not independently selected replacement tensors.

We prove that gamma is nonzero without evaluating the actual differential at a selected source instance. Consequently the actual column parameter is exactly zero off Omega and five on Omega.

## 1. A universal exterior lemma in dimension five

Let T be any five-dimensional complex vector space. For L:T -> Lambda2(T), define

D_L(a wedge b wedge c)=L(a) wedge b wedge c - L(b) wedge a wedge c + L(c) wedge a wedge b.

Then the linear map L -> D_L from Hom(T,Lambda2(T)) to Hom(Lambda3(T),Lambda4(T)) is injective, hence an isomorphism since both spaces have dimension fifty.

Here is an elementary proof. Suppose D_L=0 and choose a basis e_1,...,e_5. Fix distinct indices i,j,k and let a,b be the two remaining indices. In D_L(e_i wedge e_a wedge e_b), the coefficient of the four-form with indices j,k,a,b comes only from L(e_i) wedge e_a wedge e_b: the other two terms contain e_i. Hence the coefficient of e_j wedge e_k in L(e_i) is zero. Thus

L(e_i)=v_i wedge e_i,

where we choose v_i with zero e_i coefficient.

For three distinct indices i,j,k, the displayed formula for D_L now gives

D_L(e_i wedge e_j wedge e_k)=(v_i+v_j+v_k) wedge e_i wedge e_j wedge e_k.

Fix an index l. For every triple i,j,k among the four indices different from l, the preceding equality gives v_i^l+v_j^l+v_k^l=0, where v_i^l is the e_l coefficient. Subtracting two such equations shows that all four numbers v_i^l are equal. Each triple sum is then three times their common value, so all vanish. This holds for each l, and consequently every v_i is zero. Therefore L=0.

This lemma concerns arbitrary exterior tensors. Its basis argument does not evaluate any actual HM multiplication or differential.

## 2. The actual exterior projection

Fix the actual equivariant isomorphism

p:E tensor W0 -> Lambda2(T).

Exterior multiplication defines an equivariant map

Psi:E tensor Lambda2(T) -> Lambda4(T) tensor W0^*,

by the coordinate-free rule

Psi(e tensor xi)(w)=p(e tensor w) wedge xi.

The representation W0 is self-dual. The target is therefore V tensor W0, and the target decomposition in the inputs has exactly one W0 summand. By equivariance and irreducibility, Psi is a scalar multiple of projection onto that summand. This assertion does not assume that its scalar is nonzero.

Before taking the Koszul-boundary quotient, the actual column differential at a parameter is

delta_lambda:T tensor Lambda3(T) -> E tensor Lambda2(T),

delta_lambda(t tensor (a wedge b wedge c))
 = mu_lambda(t,a) tensor (b wedge c)
 - mu_lambda(t,b) tensor (a wedge c)
 + mu_lambda(t,c) tensor (a wedge b).

One-dimensional O(2) fibers are suppressed in this formula; choosing a trivialization cannot affect vanishing. The differential annihilates the preceding Koszul boundaries, and its induced quotient map is the reduced differential phi of the inputs.

Suppose, for contradiction, that gamma is identically zero. The W0 projection of phi is then zero. Indeed its odd block is gamma and its even block has target T4. It follows that Psi composed with delta_lambda is zero at every parameter.

For a nonzero parameter lambda, any t in T and any w in W0, define

L_(t,w)(a)=p(mu_lambda(t,a) tensor w).

Evaluating Psi delta_lambda on w gives exactly D_(L_(t,w)). The universal lemma therefore gives L_(t,w)=0. Choose any nonzero w. The map e -> p(e tensor w) is injective because p is an isomorphism. Consequently mu_lambda(t,a)=0 for all t,a. Since products t a span Sym2(T), mu_lambda is zero, contradicting actual binary evaluation.

This argument is uniform in the parameter and uses only the defining multiplication and exterior maps. It does not select or calculate an actual source-instance matrix, rank, minor, or coefficient. The contradiction proves gamma is nonzero.

## 3. Exact column jumping and its sheaf meaning

The single-channel reduction now gives

u(lambda)=0 if lambda is not in Omega,
u(lambda)=5 if lambda is in Omega.

Equivalently det(beta) is a nonzero invariant section of O(12) whose divisor is the reduced orbit Omega. At each of its twelve points the fiber kernel of beta is one-dimensional. Since its determinant vanishes simply, the local cokernel is the residue field of that point: over the local discrete valuation ring, the Smith exponents have sum one. Thus coker(beta) is a torsion sheaf of length twelve, with length one at each point of Omega.

As a sheaf map beta is injective. It is generically an isomorphism, and its sheaf kernel would be a torsion subsheaf of a vector bundle on the integral smooth curve P, hence zero. Therefore the reduced column map phi has zero kernel sheaf and

coker(phi)=O(8) direct sum coker(beta).

This does not assert that the fiber maps are injective on Omega: fiber formation need not preserve the left exactness of this sequence. Their nonzero kernels there are precisely the torsion contribution detected by Tor under base change.

Restoring the five-dimensional Heisenberg factor V gives a free-rank-five contribution V tensor O(8) and a torsion contribution of total length sixty, length five at each point of Omega. The actual fiber kernel has dimension five at each of those twelve points and zero elsewhere. No flatness claim is made for this cokernel family.

## Scope

This is an authored structural proof, conditional on the exact pinned inputs and intended for independent mathematical review. It is not formally proof-assistant checked. No selected actual HM/source-instance evaluation, numerical rank calculation, coefficient search, or large computation was performed. The conclusion concerns this degree-four column differential. The original fixed-pair residual, higher-order lifting, and algebraicity questions remain separate.
