# Heisenberg Hilbert constraints and the invariant quintic surface

## Hypotheses and new conclusions

Let S⊂P4 be an integral surface invariant under the projective order-25 quotient of the order-125 Heisenberg group H5. Use the standard irreducible five-dimensional coordinate representation, with nontrivial central character on degree-m coordinates when 5 does not divide m. Every irreducible H5 representation with nontrivial central character has dimension five. No normality, smoothness, or Cohen–Macaulay hypothesis on S is imposed.

Write d=deg S, g for the arithmetic genus of a general hyperplane section, and χ=χ(O_S). Then

 d≡0 mod5,   g≡1 mod5,   χ≡0 mod5.

In addition, S is nondegenerate and lies on no quadric. For an invariant integral quintic surface R these constraints sharpen to

 g=1, χ(O_R)=0, h1(O_R)=1, h2(O_R)=0,
 h0(O_R(m))=5m(m+1)/2 and H1(O_R(m))=H2(O_R(m))=0 for m≥1.

All restriction maps H0(P4,O(m))→H0(R,O_R(m)) are surjective for m≥0. This last statement is restriction-surjectivity, not an assertion that the homogeneous coordinate ring is integrally closed or that R is normal. In fact R is not arithmetically Cohen–Macaulay because H1(O_R)=1.

For an invariant degree-ten integral surface, the elementary arithmetic Castelnuovo bound gives g∈{1,6,11,16}. No assertion that these alternatives all occur is made.

## 1. The full congruence, not just degree divisibility

The Hilbert polynomial has the form

P_S(m)= (d/2)m²+(d/2+1−g)m+χ.

This follows by taking its first difference, the Hilbert polynomial dm+1−g of a general hyperplane section. Thus 2P_S has integer coefficients. For every sufficiently large m not divisible by five, Serre vanishing identifies P_S(m) with h0(O_S(m)). That H5 representation has nontrivial central character, so its dimension is divisible by five. For each of the four nonzero residue classes modulo five choose sufficiently large m in that class. The polynomial 2P_S reduced modulo five vanishes at all four nonzero residues. Its degree is at most two, so all its coefficients vanish. These are d, d+2−2g, and 2χ, giving the three stated congruences.

## 2. Hyperplane sections and absence of quadrics

The linear span of S is invariant. Irreducibility of the coordinate representation forces it to be P4. A general hyperplane section Γ⊂P3 is integral. Indeed Bertini gives generic reducedness and irreducibility, and the hyperplane may avoid the finite non-Cohen–Macaulay locus of the integral surface: every codimension-one local ring is a one-dimensional domain and hence Cohen–Macaulay. The resulting curve section is Cohen–Macaulay and generically reduced, hence reduced. It is nondegenerate: the hyperplane ideal sequence and H1(I_S)=0 (from H0(O_S)=C) identify any linear equation of Γ with a linear equation of S.

Let W be the four-dimensional space of coordinate sections of O_Γ(1). Multiplication W⊗W→H0(O_Γ(2)) has no zero divisors because Γ is integral. Hopf's dimension lemma gives image dimension at least seven, so h0(I_{Γ/P3}(2))≤10−7=3. The restriction map H0(I_S(2))→H0(I_Γ(2)) is injective because its kernel is the hyperplane equation times H0(I_S(1))=0.

Meanwhile H0(I_S(2)) is an H5 representation of nontrivial central character, and its dimension is a multiple of five. Being at most three, it is zero. This proves the no-quadric assertion for every such invariant integral surface, independently of its degree.

## 3. Sectional genus in degrees five and ten

For an integral nondegenerate curve of degree d in P3, write d−1=2a+b with 0≤b≤1. Arithmetic Castelnuovo gives

0≤g≤a(a−1)+ab.

For d=5 this is 0≤g≤2, and the congruence forces g=1. For d=10 it gives 0≤g≤16, and the congruence leaves 1,6,11,16.

Source checked: V. Di Gennaro, “The genus of curves in P4 and P5 not contained in quadrics,” Section 2(v), https://link.springer.com/article/10.1007/s12215-022-00788-x . The statement concerns arithmetic genus of integral curves, not merely geometric genus of smooth curves.

## 4. The quintic is linearly normal

Now let R have degree five, and Γ be its general integral genus-one hyperplane section. The dualizing sheaf of Γ is rank-one torsion-free of degree zero, whether or not it is invertible. For m≥1, duality and negativity give H1(O_Γ(m))=0; Riemann–Roch gives h0(O_Γ(m))=5m.

The hyperplane sequence at m=1 shows

h0(O_R(1))≤h0(O_R)+h0(O_Γ(1))=1+5=6.

Nondegeneracy gives h0(O_R(1))≥5; H5 central character forces this dimension to be divisible by five. Therefore h0(O_R(1))=5, and the ambient linear restriction is an isomorphism. Equivalently H1(I_R(1))=0.

The hyperplane ideal sequence at degree two now makes H0(I_R(2))→H0(I_Γ(2)) surjective. Section 2 gives a zero source, so Γ lies on no quadric. Because h0(O_Γ(2))=10=h0(P3,O(2)), the quadratic restriction map is an isomorphism and H1(I_Γ(2))=0.

## 5. Higher restrictions, cohomology, and χ=0

The ideal sheaf I_Γ is 3-regular: its required groups are

H1(I_Γ(2))=0,
H2(I_Γ(1))=H1(O_Γ(1))=0,
H3(I_Γ)=0.

The last equality follows from the ideal sequence and the dimension-one property of Γ. Castelnuovo–Mumford regularity therefore gives H1(I_Γ(m))=0 for all m≥2. Thus every section of O_Γ(m), m≥2, lifts to a degree-m polynomial on its ambient P3, and hence to a polynomial on P4. In particular O_R(m)→O_Γ(m) is surjective on global sections for every m≥2.

Induction starting with the already proved surjectivity at m=1 proves ambient restriction-surjectivity for R in every m≥1: given a section on R, lift its restriction on Γ by an ambient polynomial; their difference is the hyperplane equation times a section on R of degree m−1, to which the induction hypothesis applies.

For m≥1, the hyperplane sequence and H1(O_Γ(m))=0 give H2(O_R(m−1))≅H2(O_R(m)). By Serre vanishing, H2(O_R(m))=0 for all m≥0. For m≥2, the additional global-section surjectivity just proved gives H1(O_R(m−1))≅H1(O_R(m)). Again Serre vanishing yields H1(O_R(m))=0 for all m≥1.

The Hilbert polynomial in genus one is P_R(m)=5m(m+1)/2+χ(O_R). At m=1 its Euler characteristic is h0(O_R(1))=5, because both higher groups vanish. Hence χ(O_R)=0. At m=0, h0=1 and h2=0 give h1=1. The stated formula for all positive twists follows at once.

## Boundaries

The result constrains the invariant integral quintic alternative in the residual degree-five fundamental cycle. It does not apply to the separate orbit-of-five-planes alternative. No normality, local Cohen–Macaulayness of R, or integral closedness of its coordinate ring is inferred. The proof does not classify R or exclude it. No selected coefficients, numerical matrix ranks, parameter scans, or prohibited experiments are used.
