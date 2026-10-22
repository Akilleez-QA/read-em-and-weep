# Exact first-jet descent on a fixed elliptic beta scroll

## Scope and input

This note concerns the fixed degree-fifteen beta scroll X, not the primary degree-fifteen surface and not the degree-thirty Chow hypersurface. Work over C. Let nu:R -> X be its finite smooth ruled normalization. Delete the finite rank-zero locus P (the twenty-five points associated with beta in kappa(C)), and put Xcirc=X minus P and Rcirc=nu^{-1}(Xcirc). On this open set the rank-one determinantal description is locally complete intersection and gives omega_Xcirc=O_Xcirc(C), where C consists of the twenty-five ruling lines. No Gorenstein assertion is made at P. Write C_R for the strict transform of C, agreeing with its Cartier pullback over Xcirc. Put f for a ruling fiber, h=nu*O_X(1), and J for the inverse image of the singular elliptic curve E.

The source geometry is ADHPR, *Syzygies of Abelian and Bielliptic Surfaces in P4*, Proposition 4.16(ii)-(iv), https://arxiv.org/pdf/alg-geom/9606013: the degree-fifteen scroll is smooth away from E, its exceptional identification is four-to-one along the graph curve, and each ruling meets E once. Consequently J is a smooth irreducible section and J -> E is an etale isogeny of degree four. In the established ruled coordinates, C0^2=1, C0.f=1, f^2=0, h=C0+7f, K_R=-2C0+f, and C_R=25f. Equalities of numerical classes below suffice for degrees; the dualizing identities are actual line-bundle identities.

## 1. Exact conductor, not merely its numerical class

On Xcirc, finite Gorenstein duality identifies the conductor, viewed as an ideal on Rcirc, with omega_Rcirc tensor nu*omega_Xcirc^{-1}. Since Rcirc is smooth this ideal is invertible. It is the unit ideal away from J, because normalization is an isomorphism over the smooth locus of X. Extending its reflexive hull across the finite complement in R gives O_R(-aJ) for an integer a>=1. Choose a general ruling f avoiding that complement. The conductor has degree K_R.f-(C_R).f=-2 on f. Since J.f=1, a=2. Therefore the conductor on Rcirc is exactly O_Rcirc(-2J), and its global reflexive hull is O_R(-2J). The global conductor may have additional finite-length structure at the omitted points; no assertion excluding this is made.

The graph's numerical class is J=C0+12f: it is a section, and h.J=20 because J -> E has degree four and E has degree five.

Take a general ambient quadric Q avoiding P. The normalized section Ybar=R intersect nu^{-1}Q is smooth, meets J transversely, and maps finitely to Y=X intersect Q. It is the normalization of Y. The ten points Q intersect E have four distinct preimages each, since J -> E is etale. Conductor formation here is compatible with this transverse Cartier cut. One precise justification is that nu_*O_R is maximal Cohen--Macaulay over the Gorenstein surface Xcirc, so its positive Ext into O_X vanishes; tensoring the duality description with O_Y therefore commutes with Hom. Equivalently, use finite curve duality and the compatible adjunction identifications for omega_Y and omega_Ybar. The resulting conductor on Ybar is O_Ybar(-2J|Ybar), with order exactly two on each of the forty branch points.

The genus calculations are p_a(Y)=56 and g(Ybar)=16. Indeed deg omega_Y=(C+2h).2h=110, while (K_R+2h).2h=30. The conductor has degree 2J.2h=80, and total delta is forty. At each of the ten singularities the normalization conductor colength is eight. For an integral Gorenstein curve this colength is twice the local delta invariant, so each local delta is exactly four.

## 2. The completed local ring and its exact four conditions

At one singular point, let B=direct_sum_{i=1}^4 C[[t_i]] be the completed normalization and A the completed local ring of Y. Its conductor c is direct_sum t_i^2 C[[t_i]]. Thus dim(B/c)=8 and dim(A/c)=8-delta=4.

Because A is local with residue field C, all four constant terms of an element of A agree. The diagonal constants belong to A. Hence A/c is the direct sum of the diagonal constants and a three-dimensional subspace V of the four-dimensional first-derivative space. There exist coefficients a_i such that

    A = { (f_i) in B : f_1(0)=f_2(0)=f_3(0)=f_4(0),
                         sum_i a_i f_i'(0)=0 }.

Every a_i is nonzero. Otherwise the i-th coordinate vector lies in V, so t_i (supported on branch i) lies in A. Its product with every element of B lies in A, because all terms of order at least two already lie in c. This puts t_i in the conductor, contrary to its exact order two. Conversely, nonzero a_i ensure that this displayed algebra has precisely the stated conductor. Branch parameters can individually be rescaled to normalize the coefficients, but there is no canonical global choice.

This proves exactly three matching-value conditions and one weighted first-derivative relation. No tangent-coordinate computation or assumed general position of four tangent lines is needed. In particular, imposing four independent derivative vanishings would be incorrect.

There is also a complete formal normal form. Rescale the branch parameters so that the derivative relation is the sum of the four derivatives. The elements

    x=(t1,0,0,-t4), y=(0,t2,0,-t4), z=(0,0,t3,-t4)

then generate A as a complete algebra. Their mixed products are all (0,0,0,t4^2); subtracting this from each square gives the individual first-three branch squares, and multiplication generates every higher branch power. Consequently

    A is isomorphic to C[[x,y,z]]/(xy-xz, xy-yz).

Indeed the two quadrics cut out the three coordinate axes and the diagonal line, with Hilbert function 1,3,4,4,...; the displayed surjection to A has exactly those graded dimensions and hence is an isomorphism. Thus the singularity is the complete intersection of two quadrics consisting formally of four lines with four tangent directions in general linear position in P2. This normal form is a consequence of the conductor calculation, not an extra assumption about tangent positions.

For any invertible sheaf L on Y, choose a local trivialization downstairs and its four pullbacks. A normalized section descends exactly when its four local coefficient series satisfy these same conditions. Different unrelated trivializations upstairs change the equations by their unit first jets, so the formula is to be used in compatible trivializations.

## 3. Eigenline descent and the remaining size of the space

Let L_k=omega_Xcirc^2 tensor O_Xcirc(k-5), restricted to Y (which lies entirely in Xcirc). Its normalized pullback is the restriction of D_k=2C_R+(k-5)h to Ybar. Its degree is

    deg D_k|Ybar = 100+30(k-5)=30k-50.

For k=3 and k=4 these degrees are forty and seventy. Both exceed 2g(Ybar)-2=30, so H1(Ybar,nu*L_k)=0 and h0 is respectively twenty-five and fifty-five.

The normalization sequence, tensored with L_k, gives an exact finite-dimensional sequence

    0 -> H0(Y,L_k) -> H0(Ybar,nu*L_k)
      -> C^40 -> H1(Y,L_k) -> 0.

Here C^40 denotes the direct sum of ten local four-dimensional discrepancy spaces, not a canonically based vector space. The middle map is explicitly the three value differences and one derivative relation at each singularity. Its entries depend on the actual branch gluing; no independence of the forty conditions has been proved or assumed.

Consequently h0(Y,L_3)-h1(Y,L_3)=-15, while

    h0(Y,L_4)=15+h1(Y,L_4) >= 15.

Thus even the exact conductor descent on this fixed quadric section cannot prove twist-four vanishing merely by absence of descended eigenline sections. It leaves at least fifteen such sections. This is a necessary ambient line-bundle condition, not a construction of actual endomorphisms or a solution of the twenty-dimensional boundary map. Any further exclusion must enforce the actual endomorphism/evaluation compatibility, or a stronger global condition not captured by this single section.

## Dependency boundary

The rank-one open-set dualizing identification omega_Xcirc=O_Xcirc(C) and the actual beta-scroll normalization dictionary are explicit inputs, separate from the cited source's abstract scroll description. A global Gorenstein assertion at the twenty-five rank-zero points is neither used nor justified. All curve conclusions avoid those points; only the reflexive hull of the surface conductor is identified globally. All conductor, local algebra, and cohomology implications above are proved from these inputs; there are no selected coefficients, numerical rank experiments, or external writes.
