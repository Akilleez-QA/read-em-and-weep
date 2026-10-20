> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Degree nineteen: low-twist necessities

All schemes are over C; reducedness, integrality and ACM are not assumed. Let E be the reflexive rank-12 sheaf with c1=6,c2=19, central weight2, generated outside codimension two and h0(E)>=20. Eleven general sections give 0->O^11->E->I_Z(6)->0. A general regular flag yields a curve C and length19 plane scheme D, with sextic ideal having no fixed curve. Write z_j,c_j,p_j for their ideal dimensions in degree j.

## Unconditional elementary bounds

We prove

    p_j=0 (j<=3), p4<=2, p5<=5, p6<=11;
    z4=0, z5 in {0,5}, h0(E)<=30.

A cubic and a coprime sextic meet in length18, so p3=0. If two quartics exist, let h be their gcd of degree t<=3. The residual to h lies in CI(4-t,4-t), while the trace on h has length at most6t. Thus

    19<=6t+(4-t)^2.

Only t=3 is possible, with equality. The residual has length1 and the trace length18. Taking the gcd of the entire quartic space and two general divided members proves the same assertion for that gcd. Division embeds the quartic space into the linear ideal of a length1 plane scheme, which has dimension2. Hence p4<=2. In fact p4=2 means a common cubic, length18 trace, and length1 residual.

For quintics, if p5>=2 take the gcd h of their entire space, of degree t<=4. Two general divided quintics are coprime. Put D'=D:h; its length a' satisfies

    19-6t<=a'<=(5-t)^2.

Division embeds I_D(5) into I_D'(5-t). The following bounds cover every t.

- t=0: link D in CI(5,5). The residual B has length6. Plane liaison gives p5=2+h1(I_B(2)). A length6 scheme has Hilbert function at least3 at degree2, so p5<=5.
- t=1: D' lies in CI(4,4) and has length at least13. Its residual B has length at most3. Liaison gives h0(I_D'(4))=2+h1(I_B(1))<=3.
- t=2: D' lies in CI(3,3) and has length at least7. Its residual has length at most2. Liaison gives h0(I_D'(3))=2+h1(I_B(0))<=3.
- t=3: D' is nonempty (indeed has length at least1). Its quadratic ideal has dimension at most5.
- t=4: the divided linear space has dimension at most3, which suffices.

Thus p5<=5. (For t=4 the deliberately coarse bound3 avoids any unnecessary assumption that p4=0.) The finite-scheme Hilbert function satisfies H_D(5)=21-p5>=16 and grows strictly until reaching19. Consequently H_D(6)>=17 and p6<=28-17=11.

Restriction gives c4<=p4<=2 and z4<=c4. Since z4=h0(E(-2)) has nontrivial central weight4, it is divisible by5; hence z4=0. Next c5<=c4+p5<=7 and z5<=c5<=7. Weight3 divisibility yields z5 in {0,5}. Finally

    c6<=c5+p6<=18,
    z6<=z5+c6<=23,
    h0(E)=11+z6<=34.

Weight2 divisibility sharpens this to h0(E)<=30. If z5=0, the same argument gives h0(E)<=29, hence h0(E) in {20,25}.

The liaison identity used here is h0(I_A(k))-h0(I_CI(u,v)(k))=h1(I_B(u+v-3-k)), valid for arbitrary finite plane schemes and their complete-intersection residuals. The strict Hilbert-function growth follows by reduction modulo a linear form avoiding the finite scheme.

## Conditional strengthening using generic generation by J*

Suppose, in addition, the injected irreducible 20-dimensional representation J* in H0(E) generates E at its generic point. Then z5=0, and therefore

    h0(E(-j))=0 for all j>=1; h0(E) in {20,25}.

Indeed, if z5=5, let W=H0(E(-1)). The multiplication image U=S1 W in H0(E) has dimension at least15. Here is a direct proof of the product bound. Choose a linear functional on the generic fiber with rational coefficients whose map on the finite-dimensional space W is injective. To construct one, trivialize the generic fiber, clear denominators in a basis of W on an affine chart, and multiply its finitely many polynomial coordinates by sufficiently widely separated monomial powers before summing. Their monomial supports become disjoint, so the resulting map is injective on W. Clearing a common homogeneous denominator identifies its image with a five-dimensional space of homogeneous polynomials of one degree. Choose an echelon basis with five distinct leading monomials. Each monomial has five linear multiples; the sets of multiples of two distinct monomials intersect in at most one monomial. Thus their union has at least25-C(5,2)=15 monomials. They are leading monomials of products, proving the bound for the scalar image and hence for U.

Both U and J* are invariant under the full symmetry group. Since dim H0(E)<=30, their intersection has dimension at least5. Irreducibility gives J* subset U. But all sections of U lie generically in the subspace spanned by the five sections W, of dimension at most5. They cannot contain a generically rank12 generating space J*. This contradiction proves z5=0.

### Verification in the actual application

The established sequence is 0->F->J tensor O->R->0, with R torsion-free and therefore locally free at all codimension-one points of the smooth ambient space. Dualizing there gives a surjection J* tensor O->F*=E. Consequently J* generates E outside a subset of codimension at least two, in particular at the generic point with rank12. The hypothesis of the preceding argument is thus satisfied in the actual application, not merely conditional.

Therefore the actual degree19 branch necessarily satisfies

    h0(E(-j))=0 for every j>=1;
    h0(E) is either20 or25.

Mere injectivity of J* would not suffice, but the established dual sequence supplies precisely the stronger generation property needed. No rank-eight exclusion is claimed here.

## Further necessity when the plane section has no quartic

If p4=0, the quintic bound improves to p5<=3. In the gcd analysis above, t=1,2 already give this bound. For t=3, a linear equation of D' would multiply by h to a quartic equation of D. Thus D' spans the plane, and its quadratic ideal has dimension at most3. For t=4, D' is nonempty, so its linear ideal has dimension at most2.

For t=0, the length6 residual B in CI(5,5) satisfies h1(I_B(3))=p4=0, hence H_B(3)=6. Necessarily H_B(2)>=5: otherwise the first differences of the finite-scheme Hilbert function (an Artinian quotient in two variables) have reached a value at most1 by degree2, and can never increase thereafter; this would give H_B(3)<=5. Consequently h1(I_B(2))<=1 and p5<=3.

Now H_D(5)>=18 and strict growth to length19 gives H_D(6)=19, hence p6=9. Also c4=0, so c6<=p5+p6<=12. Under the generic-generation conclusion z5=0, this forces z6<=12 and h0(E)=20. Equivalently, h0(E)=25 requires a quartic equation on the general plane section D.

## Evidence boundary

This is abstract sheaf, residual and Hilbert-function geometry. No actual source, matrix, operation, selected input, rank instance, jet or residue is evaluated. The only new write is this local proof artifact.
