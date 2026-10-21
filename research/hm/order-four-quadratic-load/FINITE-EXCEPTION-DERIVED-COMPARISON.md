# Extending the actual two-term comparison across finitely many parameters

## 1. A local-cohomology extension lemma

Let T be a smooth threefold, Z a finite closed subset, and j:T-Z->T. Let A and B be complexes of vector bundles concentrated in degrees0 and1. Then restriction is an isomorphism

    Hom_D(T)(A,B) -> Hom_D(T-Z)(j*A,j*B).

Indeed the internal derived Hom is represented by the ordinary Hom complex, whose degrees are -1,0,1 and whose terms are vector bundles. For a vector bundle on a smooth threefold, local cohomology supported at finitely many points vanishes in degrees below3, by depth3. The support hypercohomology spectral sequence therefore shows

    H^i(R Gamma_Z R Hom(A,B))=0 for i<2.

The localization triangle gives the asserted isomorphism in degree0. Thus a given derived isomorphism off Z extends uniquely, as does its inverse, and their compositions equal the identities by uniqueness. This lemma would not follow from the same argument for a codimension-two exceptional curve: the degree -1 Hom term matters.

## 2. Actual geometric exceptional set

For fixed good Q, set Zeta={kappa(z):z in C intersect Q}, the fifty distinct marked parameters. On Q times (T-Zeta), evaluation B->E has rank exactly one on its degeneracy family: rank zero would require x in C intersect Q and B=kappa(x). Thus the quotient line, regular residual Cartier divisor, relative adjunction, and quotient-graph construction used in GENERIC-BETA-ABELIAN-INTERPOLATION.md are defined on this larger open, including Gamma minus Zeta.

The local model makes the finite exception explicit. At a point of C intersect Q, normalize the nonzero section u_0 by a local frame of E. The evaluation rows are then [1,h_1(x),h_2(x),h_3(x)] and [0,x,y,z], where transversality makes x,y,z regular parameters. Write nearby hyperplanes B using the basis u_i-a_i u_0. The universal curve family is locally the rank-at-most-one locus of

    [h_1(x)-a1,h_2(x)-a2,h_3(x)-a3; x,y,z].

The change a_i prime=a_i-h_i(x) identifies this total-space germ with the rank-one matrix cone [-a1 prime,-a2 prime,-a3 prime; x,y,z]. This is a total-space coordinate change, not a target-preserving coordinate change: the original evaluation morphism still projects to a_i=a_i prime+h_i(x). No assertion about its fibers is deduced by projecting to a_i prime.

It is the cone over the Segre P1 times P2, singular only at the origin. The quotient graph comparison is an isomorphism off that point; the resolved evaluation replaces it by the quotient P1. No Gorenstein claim is made for this determinantal cone at the excluded point. Removing Zeta removes all such points from the family.

The quotient graph lifts to the evaluation blowup because the evaluation base ideal pulls back to the Cartier divisor (C intersect Q) times the parameter open. Conversely the source projection together with f maps the blowup family to this constant-rank-one degeneracy family. These maps are inverse on the complement of that Cartier divisor and hence everywhere, using the same local rank-one normal form and transverse Q as in the existing graph comparison. No smoothness of each curve fiber is required; the family is relatively lci/Gorenstein there.

The universal Hilbert–Burch multiplication complex and relative duality therefore give the actual derived isomorphism

    R f_*M |(T-Zeta)
       = [V tensor O --theta--> P tensor O(1)] |(T-Zeta),

in degrees0 and1, with the same constant determinant line V=det(U) tensor R20*. The parameter twist in the quotient line is retained exactly as in the source note.

## 3. Global derived identification and multiplication compatibility

The Beilinson theorem gives a global locally free two-term model for R f_*M. The theta complex is also globally locally free in degrees0 and1. Section1 consequently extends the actual isomorphism in Section2 to all T:

    R f_*M = [V tensor O --theta--> P tensor O(1)].

In particular

    f_*M=ker theta,    R1 f_*M=coker theta

including the fifty formerly exceptional parameters. Taking global cohomology identifies ker Theta with H0(B_Q(4)) and coker Theta with H1(B_Q(4)), not just as spaces of equal dimensions but through this actual derived comparison.

Compatibility with the primary multiplication map follows functorially. On the theta model, H1((R f_*M)(-1))=P, and multiplication by U=H0(O(1)) induces exactly the quotient map

    U tensor P -> coker Theta.

On the actual geometric model the same multiplication is the previously used primary map U tensor H1(F_Q(2))->H1(B_Q(4)). Hence their dual images coincide under the induced cohomological identifications. This supplies the missing compatibility between the theta annihilator subspace and the Schur-resolution subspace; it is not a dimension argument.

This theorem does not prove theta has zero constant kernel. It identifies the complete actual derived object and makes its degeneracy and jet-prolongation descriptions compatible, while retaining their actual differential.
