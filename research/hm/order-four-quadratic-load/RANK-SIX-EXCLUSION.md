# Excluding generic evaluation rank six by its determinant channel

Use the intrinsic dual evaluation beta:M2^* tensor O -> sl(W')^* tensor Omega^1(2) on X=P(A0), with A0=V3 and M2^*=V^* tensor W'. The prior slope and central-character bounds imply that generic rank six would give a saturated reflexive kernel K of rank four with det K=O(-2). We show that this is impossible. No selected evaluation or coefficient calculation is used.

## 1. The unique determinant channel

Write W for the unprimed two-dimensional quotient representation, U=Sym^2 W, U'=Sym^2 W', and J5 for the irreducible five-dimensional representation. HM exterior and symmetric-square identities give

    exterior^2 V^*=V3 tensor W,
    Sym^2 V3=V tensor U,
    exterior^2 V3=V tensor W',
    exterior^4 V^*=V,
    Sym^2 A0^*=Sym^2 V1=V2 tensor U.

The standard tensor identities

    Sym^2(exterior^2 T)=S_(2,2) T direct-sum exterior^4 T,
    exterior^2(exterior^2 T)=S_(2,1,1) T

applied to T=V^*, together with U tensor U=1 direct-sum U direct-sum J5, give

    S_(2,2) V^*=V tensor (U direct-sum J5 direct-sum W'),
    S_(2,1,1) V^*=V tensor ((W' tensor U) direct-sum U).

Now apply the Cauchy decomposition, retaining the full auxiliary group SL2(W'):

    exterior^4(V^* tensor W')
      = S_(2,2) V^* tensor 1
        direct-sum S_(2,1,1) V^* tensor U'
        direct-sum exterior^4 V^* tensor J5.

An N-equivariant determinant inclusion O(-2)->exterior^4 M2^* corresponds to an invariant after tensoring the last display with Sym^2 A0^*=V2 tensor U. Taking H-invariants pairs the V and V2 factors. The required U multiplicity occurs exactly once, in the first Cauchy summand:

- The first multiplicity space U direct-sum J5 direct-sum W' contains U once.
- In the second, W' tensor U tensor U' has negative binary-central parity and cannot contain U. The other term U tensor U' is the sum of the four-dimensional even representation and J5, so contains no U.
- The third multiplicity J5 does not contain U.

Thus the entire determinant map takes values in S_(2,2) V^*, the subspace fixed by the full auxiliary SL2(W'). This is stronger than invariance under the finite quotient group.

## 2. Decomposable values force a tensor-product kernel

At the generic point of X, the determinant inclusion is a nonzero decomposable four-vector spanning exterior^4 K_eta. A decomposable vector determines its four-dimensional subspace uniquely, for example by the condition v wedge omega=0. Since the vector is fixed by SL2(W'), the subspace K_eta is invariant under that group.

The standard two-dimensional representation W' is irreducible for this full SL2, and its representation algebra is End(W'). Every invariant subspace of V^* tensor W' is therefore E_eta tensor W' for a subspace E_eta of V^*. Here dim E_eta=2.

Because K is saturated in V^* tensor W' tensor O, it is uniquely determined by its generic fiber: it is the intersection of that generic fiber with the ambient locally free sheaf. Consequently the full SL2(W') preserves K as a sheaf, and

    K=E tensor W'

for a saturated rank-two subsheaf E of V^* tensor O. One may define E using the full-SL2 multiplicity sheaf Hom_SL2(W')(W',K). Reflexivity of K implies reflexivity of E. The N-action normalizes the auxiliary SL2 action and acts diagonally on the two ambient factors, so E inherits its natural N-linearization.

Since det W'=1,

    det K=(det E)^2.

Pic(P4)=Z and det K=O(-2) therefore imply det E=O(-1).

## 3. The second determinant contradiction

Taking the determinant of E inside the trivial bundle V^* tensor O gives a nonzero N-equivariant map

    O(-1) -> exterior^2 V^* tensor O.

It extends over the codimension-two singular locus by reflexivity. The normalizer is perfect, so its induced determinant linearization agrees with the standard linearization of O(-1); there is no character twist to insert.

The space of such maps is

    (exterior^2 V^* tensor A0^*)^N
      = (V3 tensor W tensor V1)^N.

After taking H-invariants, this is W^SL2(F5)=0. Hence the required determinant map cannot exist. This contradiction excludes generic evaluation rank six.

Combined with the earlier exclusions of ranks five, eight, and nine, and the generic rank-at-least-five bound, the remaining generic evaluation ranks are seven or ten. This result does not choose between them, establish full adjoint quadratic surjectivity, or evaluate the original quadratic/cubic pair.

## Dependency and verification scope

HM representation inputs are Lemma3.3(ii),(v), its Galois conjugates, and the appendix character table. The products U tensor U=1+U+J5 and U tensor U'=4_even+J5 are representation identities, not source-instance rank evaluations. The tensor Schur identities are universal. The sheaf argument uses the actual saturated kernel, not an assumed split cohomology model.

Primary source: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

No selected coefficient, matrix, rank evaluation, or experiment was performed.

Previous determinant bounds and rank exclusions: EVALUATION-RANK-EXCLUSIONS.md at d9ba47779a2a24579fb5608acfab7538eadc6f20 in https://github.com/Akilleez-QA/read-em-and-weep/pull/543 .
