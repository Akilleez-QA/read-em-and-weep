# Coordinate multiplication on the HM endomorphism cohomology is surjective

## Result

Let E=End H on P4, let L=H0(O(1))=V*, and put Jr=H2(E(-r)). The actual coordinate-multiplication maps

    mu21: L tensor J2 -> J1,
    mu32: L tensor J3 -> J2

are both surjective. The first assertion follows from an exact Koszul spectral sequence and audited vanishing; the second follows from a dimension obstruction in that same spectral sequence, followed by the already proved irreducibility of J2. No actual map, matrix, polynomial instance, or Massey value is evaluated.

The conditional propagation to actual cubic and retained operations is proved later in the cubic nonvanishing unit; it is not a premise here.

## 1. Inputs

The independently established cohomology rows give

    h2(E(-1))=10, h2(E(-2))=20,
    H3(E(-3))=0, H4(E(-4))=0.

The trace pairing identifies E with E dual. Serre duality on P4, together with h1(E(-1))=5 and stability h0(E)=1, gives

    h3(E(-4))=5, h4(E(-5))=1.

These are consequences of the primary Decker-Schreyer cohomology proposition and formal duality, as recorded in [the projective target directions manuscript](../../hm_primary_source_verification.md) and [the projective target directions manuscript](../foundation-p01/INVARIANT-COHOMOLOGY.md). The actual representation J2 is irreducible under the classical normalizer N by the full hm image symmetry manuscript (PROOF.md). Coordinate multiplication is N-equivariant by coherent-cohomology functoriality.

## 2. Universal exact Koszul complex

The evaluation L tensor O(-1) -> O is surjective. Its five sections have no common zero on P4, so their full sheaf Koszul complex is exact. Tensor it with the locally free E(-1), and place E(-1) in cohomological degree zero. Its term in degree p=-j, for 0<=j<=5, is

    K^p = exterior^j L tensor E(-1-j).

The finite hypercohomology spectral sequence therefore has

    E1^(p,q) = exterior^(-p) L tensor Hq(E(p-1)),
    -5<=p<=0, 0<=q<=4,
    d_r: (p,q) -> (p+r,q-r+1),

and abuts to zero in every total degree. Its d1 maps are the ordinary Koszul maps induced by actual coordinate multiplication on coherent cohomology. This is an exact sheaf-complex argument, not a claim that global sections of that complex are exact.

## 3. Surjectivity of mu21

At (p,q)=(0,2), the incoming d1 is precisely

    L tensor H2(E(-2)) -> H2(E(-1)).

There are no outgoing differentials because p=0 is the right endpoint. For r>=2, the only possible nonzero incoming differentials have sources

    r=2: (-2,3), whose E1 term is exterior^2 L tensor H3(E(-3))=0;
    r=3: (-3,4), whose E1 term is exterior^3 L tensor H4(E(-4))=0.

For r>=4 the source has q>=5 and vanishes. Hence the cokernel of mu21 survives to E-infinity. The abutment is zero, so that cokernel is zero.

## 4. Nonvanishing of mu32

Suppose, for contradiction, that actual multiplication L tensor J3 -> J2 is zero. The d1 into (-1,2), from (-2,2), is the alternating sum of such multiplication maps and is therefore zero. Its outgoing d1 is mu21, which is surjective by Section 3. It follows that

    dim E2^(-1,2) = 5*20 - 10 = 90.

No higher differential leaves this slot: for r>=2 its target p=-1+r is positive and outside the complex. The only potentially nonzero higher differentials entering it are

    d2 from (-3,3), with source dimension at most
       dim exterior^3 L * h3(E(-4)) = 10*5 = 50;

    d3 from (-4,4), with source dimension at most
       dim exterior^4 L * h4(E(-5)) = 5*1 = 5.

Every spectral-sequence page is a subquotient of the preceding page, so these E1 dimension bounds apply to the sources on the required pages. For r>=4 the source has q>=5 and is zero. Thus at most 55 dimensions can be removed from a 90-dimensional slot with no outgoing arrows. At least 35 dimensions would survive to E-infinity, contradicting the zero abutment. Therefore mu32 is nonzero.

Its image is an N-submodule of the irreducible J2, so mu32 is surjective. This final use of irreducibility does not substitute for the nonvanishing argument.

