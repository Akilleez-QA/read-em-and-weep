# Structure and canonical direct images of the primary incidence

Work over C, and let projective spaces parametrize lines. Put A=M_0, S=S_2 and M=M_2, of dimensions 5, 15 and 10. Set Y=P(S), Z=P(A) x Y, and let p:Z -> Y be projection. The primary incidence i:I -> Z is the zero scheme of the ten bilinear equations m(q,x)=0. Let b:B -> Y be the primary maximal-minor scheme and pi:I -> B its projection, so p i=b pi.

## 1. Exact dependencies and claim

Use [PR555](https://github.com/Akilleez-QA/read-em-and-weep/pull/555) at commit ff5a3164337016e96e3a29a9ad37891130a66e29: B is an integral Cohen-Macaulay eightfold and pi is proper birational, with a scheme-level graph isomorphism over the rank-four locus. Use [PR556](https://github.com/Akilleez-QA/read-em-and-weep/pull/556) at commit 0fbd687207401fe715aa6aff2e22ee8a8de4081b: I is an integral local complete intersection of dimension eight, its ten equations form a regular sequence, and

    omega_I = Cdet tensor O_I(5,-5),
    Cdet = det(A*) tensor det(S*) tensor det(M).

The resulting canonical isomorphisms are

    O_B -> R pi_* O_I,
    R pi_* omega_I -> omega_B.

The second map is the duality trace, with absolute dualizing complexes normalized over C. In particular all positive higher direct images of both sheaves vanish. No normality or rational-singularity assertion is needed or made.

## 2. Pushforward of the actual Koszul complex

Let K be the Koszul resolution of i_*O_I, in cohomological degrees -10 through 0, with

    K^(-j) = exterior^j M* tensor O_Z(-j,-j).

The projective-space cohomology calculation gives

    R^q p_* K^0 = O_Y for q=0, and zero otherwise;
    R^q p_* K^(-j) = 0 for 1<=j<=4 and every q;
    R^q p_* K^(-j) = 0 for 5<=j<=10 unless q=4.

For j>=5 the remaining sheaf is

    exterior^j M* tensor Sym^(j-5) A tensor det(A) tensor O_Y(-j).

The determinant factor follows from Serre duality on P(A), whose dualizing bundle is det(A*) tensor O(-5). See [Stacks, cohomology of projective space](https://stacks.math.columbia.edu/tag/01XS), in particular its projective-bundle formula with the lines convention translated appropriately.

For precision about the actual unit map, O_Z[0] is a subcomplex of K: it is exactly its terminal degree-zero term. Let Q=K/O_Z[0]. Apply Rp_* to the resulting distinguished triangle. Since Rp_*O_Z=O_Y, this gives

    O_Y -> Rp_*K -> Rp_*Q -> O_Y[1].

The first map, followed by the Koszul augmentation, is the natural map O_Y -> R(p i)_*O_I, not an unspecified map between sheaves of the same rank.

The bounded hypercohomology spectral sequence for Q has terms

    E_1^(a,q) = R^q p_* Q^a => H^(a+q)(Rp_*Q).

Its only potentially nonzero terms have a=-j, q=4, 5<=j<=10. Their total degrees are 4-j, hence -6 through -1. Therefore H^n(Rp_*Q)=0 for all n>=0. Boundedness ensures convergence with finite filtrations; see [Stacks, Lemma 13.21.3](https://stacks.math.columbia.edu/tag/015J). Equivalently, this calculation can be performed over each affine open of Y with the finite standard affine cover of P(A).

The long exact cohomology sequence of the displayed triangle now proves

    O_Y -> (p i)_*O_I is surjective,
    R^n(p i)_*O_I = 0 for n>0.

This argument does not identify a spectral-sequence splice with an Eagon-Northcott differential merely by comparing its terms.

## 3. Identifying the quotient with the actual scheme B

The projection factors scheme-theoretically through B. One can also see this directly: on each standard chart of P(A), the incidence equation supplies a kernel vector with one invertible coordinate, so one column of the primary matrix is a linear combination of the other four. All five-by-five minors consequently vanish in the incidence coordinate ring.

Thus the preceding surjection factors as

    O_Y -> b_*O_B -> b_*pi_*O_I.

The second map is injective. Indeed, a regular function on any nonempty open of the integral scheme B which pulls back to zero is zero at its generic point, because pi is dominant. It therefore vanishes on that open. The second map is also surjective because its composite with O_Y -> b_*O_B is surjective. It is an isomorphism.

A closed immersion has exact, faithful direct image on quasi-coherent modules. Hence R^n(p i)_*O_I=b_*R^n pi_*O_I, and we obtain, by the canonical unit,

    R pi_* O_I = O_B.

In particular the kernel of the actual unit O_Y -> (p i)_*O_I is the ideal sheaf of B. This identifies the ideal arising from the Koszul pushforward, rather than assuming the desired identification from Betti numbers.

## 4. The canonical direct image

Both I and B are proper Cohen-Macaulay schemes, pure of dimension eight. Their absolute dualizing complexes normalized over C are respectively omega_I[8] and omega_B[8]; see [Stacks, Lemma 48.27.5](https://stacks.math.columbia.edu/tag/0FVZ).

For the proper morphism pi, proper duality identifies

    R pi_* RHom_I(O_I, omega_I[8])
      = RHom_B(R pi_*O_I, omega_B[8]).

The required hypotheses hold: the schemes are of finite type over C, the morphism is proper, O_I is bounded coherent, and the dualizing complexes are normalized relative to the same base C[0]. This is the normalized-dualizing-complex form of [Stacks, Lemma 48.20.9 and Example 48.20.11](https://stacks.math.columbia.edu/tag/0AU5). It requires neither smoothness of I nor flatness of pi.

Substituting the result of Section 3 and cancelling the common shift gives, via trace,

    R pi_* omega_I = omega_B.

Thus pi_*omega_I=omega_B and R^n pi_*omega_I=0 for n>0. Inserting adjunction and applying projection formula gives the more explicit formula

    omega_B = Cdet tensor O_B(-5) tensor pi_*O_I(5,0),
    R^n pi_*O_I(5,0)=0 for n>0.

The latter vanishing follows because O_I(5,0)=Cdet^(-1) tensor omega_I tensor pi^*O_B(5). The displayed formula is a statement about the canonical module of B; it does not say this module is invertible.

## 5. Contribution and limits

This supplies a derived structure-sheaf bridge and then its dual canonical-module bridge for the actual primary incidence morphism. It is stronger than knowing the Euler characteristic or the generic graph isomorphism. All arguments are structural and use the pinned geometric inputs; no selected source coefficients, matrix, or numerical ranks are evaluated. A resolution of singularities has not been constructed, so the direct-image statements do not by themselves establish rational singularities. These are mathematical proofs, not formally checked proof-assistant claims.
