# Conditional exclusion of the degree-60 quadratic-deficiency case

This argument is conditional on the hypotheses proved in the companion degree-sixty frontier, and on the established nonexistence of an N-invariant integral quintic surface. It does not evaluate any actual source, matrix, polynomial instance, or obstruction.

## Hypotheses and Rao multiplication

Let C be an integral N-stable degree-60 curve in P(V)=P4 over C, with normalization X of genus326 and L=nu*O_C(1). Assume h0(X,L)=5, I_C(2)=I_C(3)=0, h0(C,O_C(2))=h0(X,L²)=20. Write M_n=H1(I_C(n)); thus dim M2=5. General hyperplane section Gamma has h_Gamma(1)=4 and h_Gamma(2)=10.

The complete series L³ is basepoint-free and birational, because it contains the cubed embedding series. If h0(X,L³)>=45, the central Heisenberg divisibility and the Castelnuovo bound in P44 give g(X)<=pi(180,44)=286. (For larger dimension the bound only decreases.) Thus h0(X,L³)<=40, and dim M3 is 0 or5: h0(C,O_C(3)) lies between35 and40 and is divisible by5.

Use the audited HM conventions S1=V*, A has central character zeta². M2 is the unique five-dimensional extension of the weight-zeta^-2 Heisenberg representation, hence M2=A*. If M3 is nonzero, likewise M3=A. Uniqueness holds because two extensions differ by a character of SL2(F5), which is perfect. HM Lemma3.3(ix) and duality give

V* tensor A* = A tensor (T* direct-sum W'*) .

Neither T nor W' has a trivial constituent. Thus Hom_N(V* tensor M2,M3)=0, whether M3=0 or A. Actual graded Rao multiplication vanishes. In the hyperplane restriction sequence, since I_C(2)=I_C(3)=0, we obtain

H0(I_Gamma(3)) = ker(M2 --ell--> M3) = M2.

Consequently dim I_Gamma(3)=5 and h_Gamma(3)=15.

## Extracting an integral quintic using full sectional monodromy

Shrink to a dense open U of transverse hyperplanes such that all Hilbert-function and base-locus data used below are constant. Let B_H be the scheme-theoretic base locus of the five cubics through Gamma_H.

1. B_H has no surface component. A common quadratic factor leaves at most four independent cubics; a common cubic leaves only one. A common linear factor l leaves five quadrics q_i. Linear general position puts at most3 points of Gamma_H on l=0, so each q_i contains at least57 points. Uniform position and h_Gamma(2)=10 say that any10-point subset imposes ten independent quadratic conditions. No nonzero q_i can contain57 points. This rules out every possible common hypersurface factor.

2. Two general cubics in the system therefore form a complete-intersection curve of degree9. All geometric curve components of B_H occur in this intersection, so there are m<=9 of them and their total reduced degree is<=9. A third general cubic avoids every component of this complete intersection that is not a curve component of B_H. Bezout then bounds the number of isolated reduced points of B_H by27. This uses only the elementary excess-intersection version: on every non-base complete-intersection component, the third cubic has at most three times that component's degree zeros; their total is<=27.

3. Over K=C(U), take the geometric generic curve components of the relative cubic base locus. They spread after a finite separable splitting extension. Shrink U so its normalization in that extension is finite etale, all components spread to flat families, and point/component incidence is constant. This gives a finite etale labeling cover of the components. Combine this permutation action with the action on the60 points Gamma_H to obtain a finite group G with maps p:G->S60 and q:G->S_m. The map p is surjective by full sectional monodromy of an integral complex curve. Shrinking U preserves surjectivity. Put K=ker(q). Its image p(K) is normal in S60. If p(K) did not contain A60, it would be trivial, so S60 would be a quotient of G/K, a subgroup of S_m. This is impossible since m<=9. Thus p(K) contains A60 and acts transitively on Gamma_H.

Since60>27, some point of Gamma_H lies on a curve component D of B_H. The group K fixes D while acting transitively on Gamma_H; incidence is preserved, so D contains all60 points. Give D its reduced structure: it is integral and nondegenerate. It has no quadric because Gamma_H has none, and it lies on all five cubics.

4. Let e=deg D. If e>5, Laudal's lemma for integral space curves says that the general plane section Z of D cannot lie on a conic: otherwise e>2²+1 would lift a quadric to D. Hence h_Z(2)=6 and h_Z(3)>=6. Thus dim I_Z(3)<=10-6=4. But restriction I_D(3)->I_Z(3) is injective because I_D(2)=0, contradicting dim I_D(3)>=5. Therefore e<=5. If e<=4, normalization and h0 of a line bundle give h0(D,O_D(2))<=2e+1<=9, forcing a quadric through D. Thus e=5.

There is only one such component D because all curve components together have degree<=9. It is therefore canonically determined by Gamma_H. The unique geometric generic quintic is Galois-fixed, hence descends to K=C(U). Its Hilbert-scheme point extends over an open subset of U. Pull back the universal family and shrink once more so its fibres are geometrically integral, degree5, and contain Gamma_H. This supplies the required flat family over U. The map U to the hyperplane Grassmannian is a dominant smooth open immersion, so the smooth-base and smooth-dominant-map requirements of (0.1) hold exactly.

## Lifting and invariance

Apply Chiantini–Ciliberto, Theorem0.2, to X=C, with (s,h,r,n)=(5,3,4,1), m=1. Their degree bound is

D(s,h,r,n)=(r+h-3)s+k(k-1)(r-n-1)+2 epsilon k-2,
where s-1=k(r-n-1)+epsilon and 0<=epsilon<r-n-1.

Here k=2, epsilon=0 and D=20+4-2=22. The hypothesis h+n>=r holds with equality 3+1=4. Since60>22, the union of D_H is an integral degree5 surface S containing C.

Such a quintic surface is unique. If S' is another, general hyperplane sections D_H and D'_H are integral degree5 curves in P3 and contain60 common points. Distinct integral degree5 curves have at most25 intersection points by Bezout (equivalently generic projection to the plane). Hence D_H=D'_H for general H, and S=S'. N-stability of C then forces N-stability of S. This contradicts the established prohibition of N-invariant integral quintic surfaces.

## Sources and verification boundary

- HM tensor identity: Horrocks–Mumford, Topology12 (1973), Lemma3.3(ix), printed p70, as recorded and audited in the companion cubic module proof: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf .
- Full sectional monodromy in characteristic zero: Borys Kadets, Sectional monodromy groups of projective curves, introduction/abstract: https://arxiv.org/abs/1809.07293 . The elementary component-kernel deduction above is supplied here, rather than attributed to the source.
- Laudal's lemma: Chiantini–Ciliberto, introduction, printed p96, and Bothmer–Gallet–Schicho, Appendix B, TheoremB.5: https://arxiv.org/pdf/2012.05120 . The latter explicitly states the integral-curve form used here.
- General-codimension lifting: Luca Chiantini and Ciro Ciliberto, A few remarks on the lifting problem, Asterisque218 (1993), Theorem0.2, printed p97: https://numdam.org/item/AST_1993__218__95_0.pdf . The required flat family has integral curve fibres, and its base dominates the hyperplane space; these hypotheses are established above.

An independent audit should especially check the relative-base-locus labeling construction, the elementary isolated-point bound in Step2, and matching the lifting theorem's family hypotheses. No h_Gamma(4) assertion or Davis plateau theorem is used.

Source visual verification: downloaded the primary lifting PDF and viewed rendered printed pages95 and97. The actual signs are h+n>=r and 0<=epsilon<r-n-1, confirming the equality case and k=2,epsilon=0. The displayed theorem and formula were visually checked, not inferred from OCR.
