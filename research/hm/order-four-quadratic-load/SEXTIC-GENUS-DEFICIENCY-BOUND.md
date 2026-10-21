# A three-cubic sextic carrier has arithmetic genus at most two

## Inputs and scope

Assume the actual generic HM hyperplane branch a=0,b=3 has a positive-dimensional cubic base, and its canonical marked integral component D has degree six. The carrier construction, including smoothness of the 25 marked points Z on D, is THREE-CUBIC-SEXTIC-HEPTIC-DICHOTOMY.md at 435a20fc680c7ccecc3cbfd762a3d5ae97b76299. In particular D spans P3, has no quadric equation, and h0(I_D(3))=3.

Choose two general cubics from its three-dimensional cubic space forming a complete intersection Y of type (3,3). The residual curve R defined by I_R=I_Y:I_D is locally Cohen–Macaulay of degree three. It need not be reduced, connected, or Gorenstein. The previously established residual duality gives h1(O_R(-1))=h0(omega_R(1))=1.

The conclusion below handles nonreduced residuals rather than discarding them. It is not the genus-three four-cubic sextic branch.

## 1. Exact genus formula

Set t=h0(O_R(-1)), a nonnegative integer. Riemann–Roch for the locally Cohen–Macaulay degree-three curve R gives

chi(O_R(-1))=-3+1-p_a(R)=-2-p_a(R).

The left side is t-1. Therefore p_a(R)=-1-t.

The arithmetic-genus identity for directly linked locally Cohen–Macaulay curves in a (3,3) complete intersection is

p_a(D)-p_a(R)=(deg D-deg R)*(3+3-4)/2=3.

Consequently

p_a(D)=2-t.

Because D is integral and projective, H0(O_D)=C and p_a(D)=h1(O_D)>=0. Thus t is exactly one of 0,1,2, and the only possibilities are

(t,p_a(R),p_a(D))=(0,-1,2), (1,-2,1), or (2,-3,0).

If R is reduced then h0(O_R(-1))=0: restriction to each integral component is a line bundle of negative degree and has no nonzero section. Hence the reduced-residual case forces p_a(D)=2. The other two cases necessarily have nonreduced residuals; they are not asserted to occur.

For comparison, a conic disjoint from a line is a reduced degree-three curve of arithmetic genus -1 with h1(O_R(-1))=1. This example only shows numerical consistency of the residual conditions; it is not an actual HM realization or a construction of the linked D.

## 2. Low-degree deficiency is fixed by t

For n>=1, O_D(n) has degree 6n, strictly greater than deg omega_D=2p_a(D)-2<=2. Serre duality gives H1(O_D(n))=0 even if D is singular: its dualizing sheaf is rank-one torsion-free, and omega_D(-n) has negative degree and hence no sections. Therefore

h0(O_D(n))=6n+1-p_a(D)=6n-1+t.

The restriction exact sequence, h0(I_D(1))=h0(I_D(2))=0, and h0(I_D(3))=3 now give

h1(I_D)=0,
h1(I_D(1))=1+t,
h1(I_D(2))=1+t,
h1(I_D(3))=t.

In particular even the genus-two case is not ACM: its deficiency dimensions in degrees one and two are both one. The lower-genus possibilities have still larger deficiency. No vanishing in degree four or above is inferred here.

## 3. The determinant of the evaluation image has four to six sections

Let J be the image bundle of U tensor O_D -> E|D, using the actual transverse elementary modification at the 25 smooth marked points. Its determinant is L=O_D(5)(-Z), of degree five. Since 5>deg omega_D, duality again gives H1(L)=0, and Riemann–Roch gives

h0(L)=6-p_a(D)=4+t, hence h0(L) is 4, 5, or 6.

This is the dimension of the complete linear system of L. It is not automatically the rank of the map Lambda^2 U -> H0(L) supplied by the six global minors. Their image may be a proper subspace. Thus one cannot import the earlier argument that a three-section determinant forces a line/alpha/beta Grassmannian image. That argument belonged to a different genus-three or genus-four carrier.

## 4. The actual minor span is at least four

Let r be the dimension of the image of Lambda^2 U -> H0(L). The minors generate L, so their basepoint-free system defines the actual kernel map into Gr(2,U) with pullback of O(1) equal to L. Positive degree forces r>=2. If r=2, the image is a Grassmannian line. If r=3, its image spans P2; degree five is prime, so it is an integral plane quintic with a finite birational parameterization. The Plucker quadratic vanishes identically on its span, since a nonzero quadratic cannot contain an integral plane quintic. The plane is therefore an alpha or beta plane.

These line/alpha/beta alternatives are excluded for a generic moving family of marked integral sextics by the existing genus-independent arguments. The transfer was spelled out in Sections 4–5 of QUADRIC-CUBIC-SEXTIC-EXCLUSION.md at d0edac7da9a616efcdd99b449c1c7f91682e2529: the alpha proof uses the degree-ten section-zero scheme and H0(I_C E)=0; the beta proof uses the integral degree-fifteen surface reduction, the moving-degree-six Hodge contradiction off Gamma, and the elliptic-scroll exclusion on Gamma. None uses the arithmetic genus of D. Their primary proof pins are respectively 212f18bb3afb52171068d1aaf8a0dbfbf9954d2b, 3714d276821366f9b1230abb6cc60b81861bb878, 57839111ecf315c833651671c4cb633818994637, and 38c517ed358c08d776b59ab5def5856106dcdeb5.

Consequently the generic three-cubic sextic branch satisfies

4<=r<=4+t.

This is a generic-family conclusion, not an exclusion of an isolated exceptional hyperplane. In particular, for t=0 and p_a(D)=2, r=4; only in this case has the full determinant system been forced.

## 5. Genus two gives a second embedding on an integral quadric

Suppose t=0. The actual minor map is then defined by the complete four-dimensional space H0(L), and maps D to an integral nondegenerate curve D' in P3 with pullback degree five. The degree formula forces it to be finite birational onto a degree-five image: a nondegenerate curve in P3 has degree at least three, and the only relevant factorization of five is 1*5.

The finite birational map gives an injection O_D' -> f_*O_D with a finite-length quotient. Therefore p_a(D')>=p_a(D)=2, and the difference equals that length. Castelnuovo's arithmetic-genus bound for a nondegenerate integral quintic in P3 gives p_a(D')<=2. The quotient is zero, so the finite map is an isomorphism. Thus L gives an embedding of D as a degree-five genus-two space curve, not merely a parameterization.

The arithmetic bound used here is the same credited standard bound as in KAPPA-RATIONAL-SEXTIC.md: Di Gennaro, Section 2(v), https://link.springer.com/article/10.1007/s12215-022-00788-x . Here d-1=4=2*2+0, giving G(3;5)=binom(2,2)*2=2.

Moreover D' lies on one unique integral quadric: it is the restriction of the Plucker quadric to its P3 span. This restriction cannot vanish identically, since a smooth four-dimensional Plucker quadric has no projective three-plane. It cannot be reducible or a doubled plane, since the integral D' spans P3. Finally two independent quadric equations would either cut a degree-four complete intersection, too small to contain D', or have a common plane factor, again incompatible with an integral nonplanar curve. The quadric may be smooth or a cone; neither case is excluded here.

This is a second embedding of the same curve. Its original embedding as a sextic carrier in the hyperplane H still has no quadric equation; these two polarizations must not be confused.

## Boundaries

The three genus possibilities are necessary alternatives, not a classification or existence theorem. No actual HM coefficients, selected ranks, scans, or experiments were used. The exact residual invariant t packages the possible nonreduced contribution instead of assuming it vanishes. Excluding any remaining possibility, determining the span of the six restricted minors in the lower-genus cases, and proving the complete repair remain open.
