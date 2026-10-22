# The remaining rank-seven alternative has two determinant channels

Retain X=P(A0), A0=V3, M2^*=V^* tensor W', and the intrinsic map beta:M2^* tensor O -> E^*, E^*=sl(W')^* tensor Omega^1(2). Prior structural exclusions leave generic rank seven or ten. In the rank-seven case its saturated reflexive kernel K has rank three and det K=O(-4).

This note identifies the exact determinant space, excludes its pure cubic Cauchy channel, and reduces the actual rank alternative to independence of two natural covariant images. It does not evaluate either image.

## 1. Exact channel decomposition

Put W=W_original, U=Sym^2 W, U'=Sym^2 W'. Write J4+ and J4- for the even and odd four-dimensional quotient representations, J5 for the five-dimensional representation, and J6 for the six-dimensional one. Cauchy decomposition gives

    exterior^3(V^* tensor W')
      =S_(2,1)V^* tensor W'
       direct-sum exterior^3 V^* tensor Sym^3 W'.

The elementary Schur identity S_(2,1)T=(T tensor exterior^2 T)-exterior^3 T, together with HM tensor identities, gives

    S_(2,1)V^*=V1 tensor (J4- direct-sum J4+),
    exterior^3 V^*=V1 tensor W.

The quotient-group products are

    J4- tensor W'=U' direct-sum J5,
    J4+ tensor W'=W direct-sum J6,
    W tensor Sym^3 W'=U direct-sum J5.

Thus

    exterior^3 M2^*=V1 tensor
      (U direct-sum U' direct-sum 2J5 direct-sum J6 direct-sum W).

The first Galois conjugate of HM Lemma3.3(vii) is

    Sym^4 A0^*=Sym^4 V1
      =V3 tensor (J4+ direct-sum J4- direct-sum U direct-sum U').

Taking H-invariants first, then quotient-group invariants, proves

    C=Hom_N(O(-4),exterior^3 M2^* tensor O)

has dimension exactly two. Choose nonzero generators sigma_U and sigma_U' of its two irreducible-pairing channels. Their normalizations are arbitrary. The sigma_U image lies in exterior^3 V^* tensor Sym^3 W'; sigma_U' lies in S_(2,1)V^* tensor W'.

## 2. A pure cubic-channel decomposable vector has a common W'-line

Here is a general linear-algebra lemma. Let T be a vector space and R two-dimensional. Suppose a nonzero decomposable omega in exterior^3(T tensor R) lies entirely in exterior^3 T tensor Sym^3 R. Then its three-plane is E tensor L for a three-dimensional E in T and a line L in R.

To prove it, contract omega by any functional in T^* tensor R^*. Its projection to Sym^2 T tensor exterior^2 R is zero: as an SL2(R)-map, such a projection would require a trivial constituent in Sym^3 R tensor R^*, whereas that tensor decomposes as Sym^4 R direct-sum Sym^2 R. For decomposable omega, its contractions span exterior^2 of the three-plane. Thus every independent pair u,v in that plane has zero singlet projection.

Choose a basis of R and write u=(a,b), v=(c,d) in T direct-sum T. The zero-singlet condition is a d=b c in Sym^2 T. If a,b are independent linear factors, unique factorization in Sym(T) gives c=lambda a and d=lambda b, contradicting independence. Therefore u has tensor rank one. Taking u=(a,0), the same equation forces d=0, so every v in the plane has the same R-line. This proves the lemma.

## 3. The pure sigma_U channel cannot be a generic kernel determinant

Suppose sigma_U had generically decomposable values. They define a generic three-plane K_eta=E_eta tensor L_eta by the lemma. Saturate these generic subspaces separately in V^* tensor O and W' tensor O, obtaining an N-linearized rank-three sheaf E0 and a line sheaf L. Uniqueness of these two factors makes their N-linearizations natural. Write det E0=O(-a) and L=O(-b). Their inclusions in trivial bundles give a,b>=0.

The determinant values of sigma_U may a priori have a common divisorial zero. If that divisor has degree t>=0, saturation of its generic three-plane gives

    det K=O(-4+t), hence a+3b=4-t<=4.

This slightly stronger bookkeeping avoids assuming the arbitrary covariant is already a saturated kernel determinant. The center acts trivially on W', while its action on O(-b) has weight3b mod5. Since N is perfect, there is no character twist, so b is divisible by5. The inequality gives b=0. Then L is a constant N-invariant line in the irreducible two-dimensional W', impossible.

Thus sigma_U is not generically decomposable, even without assuming that it arises as the actual kernel determinant.

## 4. At most two abstract Plucker ratios

Substitute omega_(s,t)=s sigma_U+t sigma_U' into the universal quadratic Plucker equations of Gr(3,M2^*) in P(exterior^3 M2^*). Each equation becomes a section-valued homogeneous binary quadratic in (s,t). The pure-U exclusion proves that these equations are not all identically zero as functions of the ratio [s:t]. Choose any nonzero scalar coefficient of one of these section-valued quadratics. Its projective zero set has at most two points. Therefore the common Plucker-ratio set is finite of cardinality at most two, and it does not contain [1:0]. This is a set-theoretic bound, not a reducedness or multiplicity assertion.

No candidate ratio is asserted to exist. Generic decomposability is equivalent here to the vanishing of the section-valued equations, since a section vanishing on a dense open vanishes identically.

## 5. The exact actual-beta test is linear

There is a canonical exterior contraction

    delta_beta:exterior^3 M2^* tensor O
      -> exterior^2 M2^* tensor E^*,

sending v1 wedge v2 wedge v3 to the alternating sum of the remaining pair tensored with beta(vi). Applying it to the two-dimensional equivariant covariant space gives

    D_beta:C -> Hom_N(O(-4),exterior^2 M2^* tensor E^*).

For any linear map f, the kernel of this exterior contraction is exterior^3 ker(f). This follows by splitting its domain into ker(f) and a complement: on the summands with at least one complement factor, contraction is injective, with the usual nonzero degree factor in characteristic zero.

If generic rank beta is ten, delta_beta is generically injective, and D_beta is injective. If generic rank is seven, its generic kernel is the line exterior^3 K_eta. The actual determinant inclusion det K=O(-4) supplies a nonzero element of ker D_beta. Any other such element is a scalar multiple: the ratio is a rational function regular in codimension one, because K is saturated and its determinant inclusion has no divisorial zero, hence it is a global regular function on projective space.

Consequently D_beta has rank either one or two, with the exact alternatives

    generic rank beta=7 iff rank D_beta=1;
    generic rank beta=10 iff rank D_beta=2.

In the first case the unique annihilated determinant ratio has automatically decomposable generic values and belongs to the at-most-two Plucker candidate set above. Independence of D_beta(sigma_U) and D_beta(sigma_U') is not proved or evaluated here. This criterion retains the actual beta and does not replace it by an arbitrary equivariant map.

## Sources and boundaries

Representation inputs: HM (1973), Lemma3.3 and its Galois conjugates, (2.2), and the appendix character table. The Schur decompositions, pairwise polynomial-factor argument, and exterior contraction are general identities. Primary source: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

The new conclusions are exact channel count, exclusion of the pure-U Plucker ratio, finiteness of abstract candidate ratios, and the linear actual-beta criterion. Generic rank ten, full adjoint quadratic surjectivity, and the original Q4 quotient remain unproved. No selected HM coordinates, covariant values, coefficients, matrices, numerical ranks, or experiments were used .

Pinned preceding exclusions: RANK-SIX-EXCLUSION.md at d6ddff0f1a663df9b102a9fd8d8f915f2d9142d6, and EVALUATION-RANK-EXCLUSIONS.md at d9ba47779a2a24579fb5608acfab7538eadc6f20, in https://github.com/Akilleez-QA/read-em-and-weep/pull/543 .
