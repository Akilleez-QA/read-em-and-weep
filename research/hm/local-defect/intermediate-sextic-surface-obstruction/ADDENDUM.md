> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Degree24 plane-section necessity and proposed exclusion

This addendum uses notation and established bounds from PROOF.md.

## 6. Further degree24 constraint: the plane section is a complete intersection

In Section5 the general plane section D necessarily has a quartic, and hence is CI(4,6).

Indeed suppose p4=0. We already know p5<=2 and c4=0, so c5<=p5 and, since z5=0, z6<=c6<=p5+p6. If p5<=1, then H_D(5)>=20 and a=24 forces H_D(6)>=21; thus p6<=7 and p5+p6<=8, contrary to z6=9.

It remains p5=2. Consider the gcd degree t of the quintic space. Section2 excludes t=1,2,3 for length24.

For t=0, link D in CI(5,5). The residual has length1. Formula(1) at k=6 uses residual twist1, so p6=h0(I_CI(5,5)(6))=6. Again p5+p6=8.

For t=4, write h for the common quartic. The residual D' to h is nonempty and lies in an intersection of two distinct lines, so has length1. Thus the trace T=D intersect V(h) has length23. Choose a sextic coprime to h. T lies in their CI(4,6), with residual length1; formula(1) at k=6 gives h0(I_T(6))=7. Since h is not an equation of D, there is a quadric b such that hb does not vanish on D: choose b nonvanishing at every point of its finite support, so multiplication by b is locally invertible on O_D. Yet hb vanishes on T. Therefore I_D(6) is a proper subspace of I_T(6), giving p6<=6. Once more p5+p6<=8, a contradiction.

Consequently p4=1. Since D has length24 and lies in a quartic-sextic complete intersection of length24, it equals that complete intersection scheme-theoretically.

This proves a necessary complete-intersection plane-section condition. It does not itself lift the quartic to C or Z, and does not claim to exclude the remaining degree24 branch.

## 7. Reflexivity completes the degree24 exclusion

Assume additionally that E in Section5 is reflexive, as in the established application E=F*. Then (24,12) is also excluded. This section supplies the extra purity and lifting arguments; Section6 alone did not imply this conclusion.

### 7.1 Purity and the curve section

The exact sequence O^11 -> E -> I_Z(6) shows at every ambient point of codimension at least3 that depth(I_Z)>=2: the free term has depth at least3 and the reflexive term has depth at least2, so the depth lemma applies. From 0->I_Z->O->O_Z->0 we get depth(O_Z)>=1 there. Therefore Z has no associated points of codimension3 or4. Its support has codimension at least2, so Z is a pure surface without embedded lower-dimensional associated subvarieties.

At points of codimension3 the local dimension of O_Z is1 and its depth is at least1. Thus Z is Cohen--Macaulay along every curve; its non-Cohen--Macaulay locus is at most finite (the Cohen--Macaulay locus is open for schemes of finite type over C). A general hyperplane avoids this finite locus. Its section C is consequently a pure Cohen--Macaulay curve.

### 7.2 Two quintics force a quartic on C

Section6 proves that the general plane section D of C is CI(4,6), with unique quartic q and dimensions p5=3,p6=7. Suppose c4=0. Then restriction of quintics from C to D is injective, and

    9=z6<=c6<=c5+7,

so c5>=2. Choose two independent quintic equations f,g of C. Their restrictions to any sufficiently general plane remain independent (the kernel would be a multiple of a quartic equation of C). Those restrictions lie in q times the linear forms; two independent such linear forms are coprime. Hence the gcd of the restricted f,g is exactly the quartic q.

For fixed f,g, the gcd after restriction to a general plane is precisely the restriction of their global gcd h. Indeed, after removing h, the coprime residual polynomials in P3 have common zero locus of dimension at most1, and its general plane section is finite; their restrictions therefore have no common curve. It follows that h has degree4 and its restriction is proportional to q.

Thus h vanishes on C intersect L for every sufficiently general plane L. To conclude scheme-theoretic vanishing, set T equal to the image of multiplication O_C(-4) --h--> O_C. Choose a general plane regular also on the quotient O_C/T; a general plane avoids its finitely many zero-dimensional associated points and contains none of its positive-dimensional associated subvarieties. Tensoring 0->T->O_C->O_C/T->0 with that plane therefore embeds T restricted to the plane into O_D. Right exactness of tensoring the defining surjection O_C(-4)->T shows this embedded restriction is exactly the image of multiplication by h on O_D, which is zero. A nonzero one-dimensional sheaf has positive degree and thus nonzero general plane section (choose the plane regular on it as well). Hence T must have finite support. Since C is pure, O_C has no nonzero finite subsheaf, so T=0. Thus h is a quartic equation of C, contradicting c4=0.

We have proved c4=1. Choose a sextic equation of C coprime to its quartic h: the restriction of the surface sextic system has no fixed divisor in P3, so this is possible. C is contained in CI(h,s) of degree24. Both curves have degree24. The kernel of O_CI(h,s)->O_C has zero generic multiplicity on every component, hence finite support. A complete-intersection curve is pure and has no nonzero finite subsheaf, so the kernel vanishes. Thus

    C=CI(4,6) in P3.

### 7.3 Lifting from the complete-intersection curve

A complete-intersection curve in P3 has surjective ambient-polynomial restriction in the precise cohomological sense needed here:

    H0(P3,O(t))->H0(C,O_C(t)) is surjective for every integer t.

This follows directly from its two-term Koszul resolution and vanishing of intermediate cohomology of line bundles on P3. In particular its negative-twist H0 vanishes.

Because Z is pure with no zero-dimensional subsheaf, H0(Z,O_Z(t))=0 for all sufficiently negative t. Here is a scheme-theoretic verification, also used in ../degree-fifteen-quintic-obstruction/PROOF.md, Section3. At each closed point the nonzero stalk of O_Z has depth at least1. Auslander--Buchsbaum over the regular local ring of dimension4 gives projective dimension at most3; at other points local dimension is at most3 anyway. Therefore sheaf Ext^4(O_Z,omega_P4)=0 everywhere. In the local-to-global Ext spectral sequence computing Ext^4(O_Z(t),omega_P4), the terms with p+q=4 are H^p(sheaf Ext^q(O_Z,omega_P4)(-t)). For sufficiently negative t every term with p>0 vanishes by Serre vanishing, and the p=0,q=4 term is zero. Global Ext^4 therefore vanishes. Serre duality identifies it with the dual of H0(O_Z(t)), giving the assertion.

Use the regular hyperplane sequence

    0 -> O_Z(t-1) -> O_Z(t) -> O_C(t) -> 0.

Induction from sufficiently negative t proves H0(P4,O(t))->H0(Z,O_Z(t)) surjective for every t. Indeed, restrict a section to C, lift it to a polynomial on P3 and then P4, subtract that polynomial, and divide the remaining section by the hyperplane equation. The previous twist supplies the induction step. For negative t, the same argument uses the vanishing on C.

Since H1(P4,O(t))=0, we obtain H1(I_Z(t))=0 for every t. In particular the ideal restriction sequence at degree4 makes H0(I_Z(4))->H0(I_C(4)) surjective. The quartic equation of C therefore lifts to a quartic equation of Z. But Section5 proved z4=0 by Heisenberg divisibility. This contradiction excludes c2(E)=24.

Subject to the established reflexivity of E, the sole remaining ordered rank-eight pair is therefore (19,17).
