# The reduced conductor curve and its value/derivative filtration

Use the integral lci surface S=f^{-1}(Gamma), its smooth finite normalization nu:Wtilde -> S, and the exact conductor O_Wtilde(-2J) established in GLOBAL-GAMMA-CONDUCTOR-GRAPH.md. All quadrics are chosen in the common open used there. This note does not assume J is smooth.

## 1. The reduced conductor image

In the fixed w-coordinate modular family, let Y be the quadric section of the smooth modular surface S(5). Its divisor class is 2H, with H=I+2F, H²=15, K=3F, and H.F=5. General Q gives a smooth connected, hence integral curve. Its genus is

    1+(2H)(2H+3F)/2 = 46,

and Y -> Gamma has degree (2H).F=10.

Let D be the reduced image of J in S. The map (modular parameter, source w-coordinate) on S maps D into Y: this holds on the dense smooth modular locus by the graph dictionary and extends because D is reduced and the modular incidence equations are regular. Here the canonical modular family is taken in its (parameter,w) incidence presentation, not just its singular degree-fifteen image in P4.

Both D and Y are finite over Gamma. Thus D -> Y is proper and quasi-finite, hence finite. On a general modular fiber the four graph points over each singular point have one image in D, and the map D -> Y is one-to-one and birational. Since Y is normal, this finite birational map is an isomorphism. Consequently the reduced conductor image is exactly the smooth curve Y.

Write i:Y -> S and p:J -> Y. J is a reduced Cartier curve in the smooth surface Wtilde, without vertical components. It is Cohen--Macaulay, and its finite map to the smooth curve Y is flat. Its generic degree is four, so p_*O_J is a vector bundle of rank four. The trace divided by four splits O_Y -> p_*O_J. In particular

    V = p_*O_J / O_Y

is a vector bundle of rank three, including at cusp parameters. Smoothness or etaleness of p at cusps is not asserted.

## 2. Exact filtration and the nilpotent-action caution

Put N=nu_*O_Wtilde/O_S. Restriction to J gives a surjective map

    N -> i_*V.

The image of O_S in nu_*O_J is exactly O_Y because D is the reduced image of J. Denote the kernel by i_*Dline. More explicitly its sections are the image in N of sections vanishing along J upstairs.

The ideal I_Y annihilates this kernel. Indeed its pullback is contained in O_Wtilde(-J); multiplying by an upstairs section vanishing on J lands in O_Wtilde(-2J), the conductor, which is already contained in O_S. The kernel is a subsheaf of the pure one-dimensional CM sheaf N, so it has no zero-dimensional torsion. Its generic rank over Y is one by the four-branch first-jet calculation. It follows that Dline is a line bundle on the smooth curve Y. Thus there is an exact sequence of sheaves on S

    0 -> i_*Dline -> N -> i_*V -> 0.

Only the two graded pieces are asserted to be O_Y-modules. N itself generally is not: a transverse nilpotent can multiply a value discrepancy into a derivative discrepancy. Treating N as a rank-four bundle on Y would lose this action and is unjustified.

## 3. Degrees of the two layers

The established intersections give p_a(J)=241, hence chi(O_J)=-240. Since chi(O_Y)=-45,

    chi(V)=-195, deg(V)=-60.

The normalization sequence gives chi(N)=55-365=-310. Hence

    chi(Dline)=-115, deg(Dline)=-70.

These statements use arithmetic genus, so remain valid without assuming J smooth. In particular no Riemann--Hurwitz formula for a smooth four-sheeted cover has been invoked.

## 4. Eigenline twists and bundles on Gamma

The graph strict transform is disjoint from the strict transforms of all fifty torsion lifts D_i. The latter are the pullbacks of the ambient exceptional E_i. This follows from the proved simple transverse intersection at each P_i before blowing up. It does NOT mean that J is disjoint from the point-blowup exceptional curves F_i: it meets each F_i once.

Consequently the ambient tautological identity L=A+sum E_i restricts on Y to L|Y=A|Y=O_Y(6F). For M_k=O_Xhat(2L+(k-5)H)|S, its restriction to Y is therefore the actual line bundle

    A_k=O_Y(12F+(k-5)H).

Its degree is 120+30(k-5)=30k-30, namely sixty and ninety for k=3,4.

Tensoring the filtration by M_k and pushing along the finite map Y -> Gamma gives an exact sequence of vector bundles

    0 -> P_k -> E_k -> V_k -> 0,

where E_k is the rank-forty actual conductor target in ACTUAL-GAMMA-CONDUCTOR-BUNDLE-GATE.md. The two layers have the following ranks and degrees:

    k=3: rank(P_3)=10, deg(P_3)=-65;
         rank(V_3)=30, deg(V_3)=-45.
    k=4: rank(P_4)=10, deg(P_4)=-35;
         rank(V_4)=30, deg(V_4)=45.

Indeed tensoring Dline adds deg A_k to its Euler characteristic, while tensoring the rank-three V adds three times that degree; degree of a vector bundle on P1 is Euler characteristic minus rank. Their sums recover deg(E_3)=-110 and deg(E_4)=10.

This separates the actual conductor target into value matching and derivative matching. A candidate normalized eigenline section first maps into the rank-thirty value target; only a section passing this test has a derivative obstruction in the rank-ten subbundle. The extension and actual maps remain essential. No splitting, generic injectivity, or actual endomorphism vanishing follows merely from these ranks and degrees.

## 5. A degree-120 discriminant without a smoothness assumption on J

The finite-flat algebra B=p_*O_J has rank four and degree -60, since it is O_Y plus the value bundle V. Its trace pairing is generically nondegenerate in characteristic zero. Taking its determinant therefore gives a nonzero discriminant section of (det B)^{-2}, whose degree is exactly120. Its zero divisor on the smooth curve Y has length120, counted with multiplicity.

Over the smooth modular locus the graph-to-singular-elliptic-curve map is multiplication by two in an elliptic family, hence etale; restricting by Q preserves etaleness. Thus this discriminant divisor is supported above cusp parameters. This is an exact discriminant-degree statement for a finite-flat algebra. It does not assume J smooth, identify individual ramification indices, or replace the arithmetic genus calculation by an unjustified smooth-curve Riemann--Hurwitz formula.

## 6. Exact derivative line from finite duality

The degree -70 calculation can be upgraded to an actual identification. Put I=I_Y in O_S and Abar=nu_*O_Wtilde(-J), regarded as a fractional ideal. Then O_S intersect Abar=I and there is an exact sequence

    0 -> I -> Abar -> i_*Dline -> 0.

Finite Gorenstein duality and conductor O(-2J) give Hom_S(Abar,O_S)=Abar. The sheaf Abar is maximal Cohen--Macaulay, so its positive Ext into O_S vanishes. Dualizing the displayed sequence yields

    I^dual / Abar = Ext^1_S(i_*Dline,O_S)
                 = i_*(Dline^dual tensor omega_Y tensor omega_S^{-1}|Y).

The intersection identity gives an injection O_Y=(O_S+Abar)/Abar into the line bundle on the right. Its degree is zero: Dline has degree -70, and omega_Y tensor omega_S^{-1}|Y also has degree -70. Therefore this injection is an isomorphism. This proves the canonical identification

    Dline = omega_Y tensor omega_S^{-1}|Y.

Since Y avoids the ambient exceptional divisors, adjunction gives omega_S|Y=O_Y(10F+2H), whereas omega_Y=O_Y(3F+2H). Hence

    Dline = O_Y(-7F),
    Dline tensor A_k = O_Y(5F+(k-5)H).

No assumption that the cusp singularities share the smooth-fiber local analytic model was used.

## 7. Both twisted derivative layers have no global sections

For k=3 the last line bundle has degree -10, so has no sections. For k=4 it is O_Y(5F-H), of degree20; its vanishing requires an actual argument, not its degree.

Let f_S:S(5)->P1. The bundle E=f_{S*}O(3I) has rank15 and degree -55, and R1 f_{S*}O(3I)=0. Indeed each smooth elliptic fiber has degree15, while every component of an I5 fiber has positive degree3, which also gives H1=0 by duality. Surface Riemann--Roch gives chi O(3I)=-40 and thus deg E=-55.

The actual Heisenberg linearization on O(H) induces one on O(3I)=O(3H-6F), with nontrivial central character. The group acts trivially on the modular parameter line. The unique irreducible representation with this central character has dimension five. Therefore E is its tensor product with a rank-three bundle on P1. In particular its splitting degrees occur in blocks of five; write the three degrees as a,b,c, with a+b+c=-11.

There are no sections of O(3I+2F). Its intersection with each of the twenty-five torsion sections is -1, so any effective representative would contain their entire sum, of class5I. Subtracting leaves -2I+2F, of negative fiber degree, impossible. Hence H0(P1,E(2))=0, forcing a,b,c<=-3. Their sum then forces every degree to be at least -5. Equivalently the only possible unordered triples are (-5,-3,-3) and (-4,-4,-3). In either case H1(P1,E(4))=0, and thus

    H1(S(5),O(3I+4F))=0.

Now use the divisor sequence for Y in |2H|:

    0 -> O(5F-3H) -> O(5F-H) -> O_Y(5F-H) -> 0.

The middle term has no sections by negative fiber degree. By Serre duality the H1 of the first term is dual to H1(O(3H-2F))=H1(O(3I+4F)), already zero. Therefore H0(Y,O_Y(5F-H))=0.

It follows that H0(Gamma,P_3)=H0(Gamma,P_4)=0 for the derivative subbundles in Section4. Consequently the map H0(E_k)->H0(V_k) is injective. For k=3,4,

    ker[H0(G_k)->H0(E_k)] = ker[H0(G_k)->H0(V_k)].

Thus for global normalized candidate sections, matching the actual values along the reduced conductor already forces the derivative condition. This is a genuine simplification of the sufficient actual-vanishing gate to the rank-thirty value target. It does not assert that the remaining value map is injective, nor that arbitrary fixed-fiber values satisfy the derivative condition.
