# Slope and normalizer exclusions for generic primary evaluation rank

Retain X=P(A0), A0=M0=V3, W'=M3, and the intrinsic evaluation map from EVALUATION-DEGENERACY.md. Its dual is

    beta:M2^* tensor O_X -> E^*,
    E^*=sl(W')^* tensor Omega_X^1(2).

The domain has rank10, the target rank12, and the generic rank of beta equals the generic rank of e_x:S2->M2. No selected evaluation is used.

## 1. Semistability, without importing a stability theorem

The bundle Omega^1(2) has rank4 and first Chern class3h. If it had a destabilizing saturated subsheaf of rank s=1,2,3 and determinant O(a), then a/s>=3/4, hence a>=s. Taking determinants gives a nonzero section of

    exterior^s Omega^1(2) tensor O(-a)=Omega^s(2s-a).

But H0(Omega^s(t))=0 for t<=s, by the exterior Euler/Koszul sequence. Since 2s-a<=s, this is impossible. Thus Omega^1(2) is slope-stable. The direct sum of three copies is semistable of slope3/4: the usual induction using intersection with one summand and projection to the others proves the slope inequality for every subsheaf. Therefore E^* is semistable of slope3/4. The nontrivial normalizer action on its three-dimensional multiplicity space does not change this underlying-bundle statement.

## 2. Determinant restrictions on a generic kernel

Suppose beta has generic rank r<10, and put k=10-r. Its kernel K is saturated in the trivial domain. It is also reflexive: locally it is the kernel of a map from a free module onto a torsion-free image, so the depth lemma gives the S2 condition, and it is locally free in codimension one. On smooth P4 its reflexive determinant is a line bundle, say det K=O(-d).

The determinant inclusion extends across codimension at least two to a nonzero map

    O(-d) -> exterior^k M2^* tensor O,

so d>=0. The image I of beta has first Chern class d h. Semistability of E^* implies

    d/r <=3/4, hence d<=floor(3r/4).

The kernel and its determinant carry the induced N-linearizations. The HM normalizer N=H semidirect SL2(F5) is perfect: [H,H] is the center of H, the coinvariants of H/[H,H]=F5^2 under SL2(F5) vanish, and SL2(F5) is perfect. Thus a line-bundle linearization cannot differ from the standard one by a nontrivial character.

The central generator acts on A0=V3 with weight3 mod5, on M2^*=V^* tensor W' with weight4, and on O(-d) with weight3d. Equivariance of the determinant inclusion therefore forces

    3d congruent 4k mod5, equivalently d congruent 3k mod5.    (*)

These bounds are necessary, not sufficient.

## 3. Generic rank nine is impossible

If r=9, the kernel is rank one and reflexive, hence K=O(-d). The bounds and (*) give

    0<=d<=6, d congruent3 mod5,

so d=3. Thus beta would have a nonzero N-equivariant inclusion

    O(-3) -> M2^* tensor O.

Such maps are invariants in M2^* tensor H0(O(3)). Here H0(O(3))=Sym^3(A0^*)=Sym^3(V1). The first Galois conjugate of HM Lemma 3.3(vi) gives

    Sym^3(V1)=V tensor (J5 direct-sum W_original),

not V tensor (J5 direct-sum W'). Consequently

    (M2^* tensor Sym^3(V1))^N
      = (W'^* tensor (J5 direct-sum W_original))^SL2(F5)=0.

We used the H-invariants in V^* tensor V, which are exactly the scalar line, before taking quotient-group invariants. The two irreducible two-dimensional representations W_original and W' are inequivalent; J5 has dimension five. Thus the required inclusion cannot exist. Generic evaluation rank nine is excluded.

## 4. Generic rank five is impossible as well

For r=5, k=5, the determinant restrictions give 0<=d<=3 and d congruent0 mod5, hence d=0. The determinant map is then a constant nonzero vector in exterior^5 M2^*. It is generically decomposable, so it determines a fixed five-dimensional subspace of M2^* equal to the generic fiber of K. Equivariance of K forces this subspace to be N-invariant. But M2^*=V^* tensor W' is N-irreducible by the HM isotypic criterion. This contradiction excludes generic rank five.

## 5. Generic rank eight is impossible

For r=8 and k=2, the bounds force d=1 or6. If d=1, the determinant inclusion would supply an invariant in

    exterior^2(M2^*) tensor A0^*.

The standard tensor exterior decomposition and HM representations give

    exterior^2(V^* tensor W')
      =V3 tensor [(W_original tensor U') direct-sum U'].

After tensoring with A0^*=V1 and taking H-invariants, neither multiplicity summand has a trivial quotient-group constituent. The first has negative binary-central parity, and U' is a nontrivial irreducible. Thus d=1 is impossible.

Suppose d=6. The saturation J of the image of beta in E^* has c1 at least6h and slope at most3/4. Since its rank is8, c1(J)=6h. Put F0=Omega^1(2), so the underlying bundle E^*=F0 direct-sum F0 direct-sum F0. The torsion-free quotient Q=E^*/J has rank4, c1=3h, and slope3/4. It is semistable: a destabilizing subsheaf would pull back to a destabilizing subsheaf of E^*, since J has the same slope.

Some summand map F0->Q is nonzero. If its kernel had positive rank, stability of F0 would make its image slope greater than3/4, contradicting semistability of Q. Thus it is injective of full rank. The induced map F0->Q** has determinant a nonzero section of O, hence is an isomorphism off a codimension-at-least-two subset. The inverse extends across this subset by reflexivity, so Q** is isomorphic to F0. Since F0 is contained in Q and Q in Q**, also Q=F0.

The quotient E^*=F0^3->F0 is a constant row because stability implies End(F0)=C. Its kernel J is therefore F0 tensor L for a two-dimensional multiplicity subspace L. Naturality makes J N-invariant, so L must be invariant in the irreducible representation sl(W')^*. This is impossible. Thus d=6 is excluded, and generic rank eight cannot occur.

This is a special-rank splitting argument; it does not silently replace semistability by a general direct-summand assertion.

## 6. Remaining ranks and a sharper primary-bad codimension

The earlier exterior/star argument proves generic rank at least five. Combining it with the exclusions above leaves only

    r=6 with d=2;
    r=7 with d=4;
    r=10 (zero generic kernel).

No remaining case is selected here. In particular, neither generic surjectivity nor the expected degree105 degeneracy curve is proved.

The Galois-conjugated HM Lemma2.5 additionally gives the pointwise bound rank(e_x)>=5, as detailed in PRIMARY-INJECTION-AND-FAILURE.md: rank four would force the star x wedge A0 to contain a full multiplicity fiber. Since generic rank five has been excluded, the rank-five locus is proper and has dimension at most3 in P4.

Consider the incidence ([x],[q]) with qx=0. Over the rank-five locus its projective fibers have dimension9, giving total dimension at most12. Over the complementary locus rank is at least6, so its fibers have dimension at most8 over P4, again giving dimension at most12. Its projective image is precisely the primary-bad quadratic locus in P(S2)=P14. Consequently that locus has codimension at least two.

This improves the previous generic-injection conclusion and codimension-at-least-one bound. It does not assert an exact codimension, full adjoint rank, or selected-point membership.

## Source and scope

Representation inputs are HM (1973), Section1 and (2.2), Lemma3.3(vi), equations(4.4),(4.11),(4.12), and the appendix. The cubic Galois conjugation changes W' to W_original and V3 to V; it is not the original-space cubic identity. Source: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

This supplies new exclusions for the actual generic evaluation rank. It does not infer a selected quadratic rank, full adjoint quadratic isomorphism, Q4 vanishing, or any original-source conclusion. No coefficient experiment or selected matrix evaluation was performed.
