# Forced irreducible channels of the actual scalar span

## Inputs and statement

Work over C. Use [PR696 at 958244d6d9d3b326f66c073a9d669717c953ec32](https://github.com/Akilleez-QA/read-em-and-weep/blob/958244d6d9d3b326f66c073a9d669717c953ec32/research/hm/scalar-parameter-descent/PROOF.md) for the actual equivariant polynomial rho:A x D -> T of bidegree (3,1), where

    dim A=dim V=3, dim P=4, dim D=5,
    T=A+2V+2P+2D.

Use [PR766 at a43b46c98e53716978d0a7750843f2224b4d2408](https://github.com/Akilleez-QA/read-em-and-weep/blob/a43b46c98e53716978d0a7750843f2224b4d2408/research/hm/uniform-full-scalar-exclusion/PROOF.md) for injectivity of h -> rho(a,h) for every nonzero a. All representations have trivial binary center, so their action factors through the icosahedral group G=A5.

Let M be the C-linear span of ALL values rho(a,h). Equivariance makes M a G-submodule. Write

    M = x A + y V + z P + w D,
    0<=x<=1, 0<=y,z,w<=2.

Then M contains at least one of the following four representations as a submodule:

    A+P, V+P, A+D, V+D.                 (1)

In particular dim M>=7, and the projections of the actual family to BOTH the combined A/V and the combined P/D isotypic blocks are nonzero. Thus the actual family cannot take all its values in A+2V, even though that block has dimension9. If dim M=7, its representation type is A+P or V+P.

These are NECESSARY constraints, not a claim that any of the four minimal representations is realized by a uniformly injective equivariant family. They do not determine the actual multiplicities.

## 1. The projective stabilizer injection

Suppose a nonzero vector a spans a one-dimensional character chi of a subgroup K of G. Equivariance and cubic homogeneity give

    g rho(a,h) = rho(ga,gh) = chi(g)^3 rho(a,gh).

Thus h -> rho(a,h) is an injective K-map

    D|K tensor chi^3 -> M|K.                    (2)

This uses no value, coefficient, or matrix of the actual family. It applies simultaneously to all abstract character lines occurring in A|K.

## 2. A Klein-four subgroup forces a P or D channel

Let K be a Klein-four subgroup, with nontrivial characters alpha,beta,gamma. The restrictions are

    A|K = V|K = alpha+beta+gamma,
    P|K = 1+alpha+beta+gamma,
    D|K = 2*1+alpha+beta+gamma.

For completeness these follow from the character values on the identity and each of the three involutions: A and V have (3,-1), P has (4,0), D has (5,1). Fourier inversion on K gives the displayed multiplicities.

Each nontrivial character chi occurs in A, and chi^3=chi. Twisting D by chi makes its chi-multiplicity2 and all other character multiplicities1. Applying (2) for all three chi gives exactly

    z+2w >= 1,
    x+y+z+w >= 2.                              (3)

In particular z+w>=1: some P or D channel is compulsory. This conclusion is stronger than any dimension bound alone.

## 3. The dihedral normalizer forces a three-dimensional channel

Let C5 be an order-five subgroup and K=N_G(C5), its dihedral normalizer of order10. Write epsilon for the character trivial on C5 and -1 on its five involutions, and E1,E2 for its inequivalent two-dimensional irreducibles. Then, up to interchanging E1 and E2,

    A|K = epsilon+E1, V|K = epsilon+E2,
    P|K = E1+E2, D|K = 1+E1+E2.

Here the C5 restrictions have exponent multisets 0,1,4 for A, 0,2,3 for V, 1,2,3,4 for P, and 0,1,2,3,4 for D. The order-two character values -1,-1,0,1 distinguish epsilon from the trivial character in A,V,D. The involutions have trace zero on each Ej. These observations prove the restrictions without choosing actual source data.

The epsilon line in A supplies (2), and epsilon cubed is epsilon. Twisting either Ej by epsilon preserves its isomorphism class. Consequently the domain in (2) is

    epsilon+E1+E2.

Since P and D have no epsilon constituents, injectivity forces

    x+y >= 1.                                  (4)

This excludes output supported only on P and D, including the otherwise allowable P+D and 2D types. Combined with (3), it forces BOTH a three-dimensional channel and a P/D channel.

## 4. Exact minimal-support classification of the stabilizer tests

Equations (3) and (4) are equivalent to

    x+y >= 1, z+w >= 1.

Indeed these imply x+y+z+w>=2 and z+2w>=1. They therefore hold exactly when M contains one of the four types in (1). Each of those types satisfies all the Klein-four and dihedral-normalizer inequalities, including the E1,E2 multiplicities. Thus the tests used here give precisely these four minimal supports, not a sufficiency theorem for uniformly injective polynomial families.

Cyclic tests give no further exclusion. The nontrivial cyclic orders in G are2,3,5. At order2, D has multiplicities(3,2) and A has both signs, so all twists require both multiplicities at least3. At order3, A has exponents0,1,2 but their cubes are1; D has multiplicities(1,2,2). At order5, D is regular, so every twist requires every character at least once. Each type in (1) passes these tests. The bounded verifier checks all54 multiplicity tuples, identifies exactly the four minimal passing tuples, and checks the cyclic tests. Passing is not sufficient for an actual family.

## 5. Independent geometric dimension check

Uniform injectivity gives a vector-bundle inclusion on P(A)=P2,

    D tensor O(-3) -> M tensor O,

with locally free cokernel E of rank dim M-5. Writing t=c1(O(1)),

    c(E)=(1-3t)^(-5)=1+15t+135t^2.

A rank0 bundle has c1=0, and a rank1 bundle has c2=0. Therefore dim M>=7 independently of representation theory. The representation argument also forces the high-dimensional irreducible channel and classifies the two possible dimension7 types, which the Chern computation does not do.

## Scope

M is the span of outputs of ONE actual family, not the23-dimensional space of possible equivariant coefficient families from PR696. Nonzero output means a nonzero global section, not a nowhere-vanishing section on the physical quadric. This result does not compute the separate fourth Bockstein beta4, does not assert a first-order obstruction, and proves no higher-order integrability or algebraicity conclusion. The proof is deductive and the verifier checks bounded abstract representation arithmetic only; neither evaluates an actual HM coefficient, source point, derivative or matrix.
