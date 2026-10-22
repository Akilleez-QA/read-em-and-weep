# Compact normalization of the dominating Gamma inverse image

This deduction concerns only the component dominating Gamma, not additional components of a special raw inverse image. It uses the canonical smooth double-cover W, finite canonical map W -> P1 x P4, and the smooth-modular point-blowup proof in SMOOTH-MODULAR-EVALUATION-BLOWUP.md. The finite canonical map at cusps is proved separately in CANONICAL-CUSP-COMPONENTS.md. Choose a general Q so that its fifty marked points have distinct smooth modular parameters κ(z_i).

## 1. Incidence equations extend, without a special-net identification

The evaluation incidence equations hold on the dense smooth-modular part of W by the exact beta-scroll dictionary. They therefore hold everywhere on the integral smooth W. This is merely extension of vanishing regular equations; it does not assert equality with the entire special determinantal surface.

Fix a marked point z_i. In a local frame and constant basis of U the evaluation matrix is

    [1 h_1 h_2 h_3; 0 a_1 a_2 a_3],

where a_i are coordinates on Q near z_i and h_i vanish there. Write the target point on Gamma homogeneously as [b_0:b_1:b_2:b_3]. On a target affine chart all b_i are regular and at least one is a unit. Put c_i=b_i-b_0 h_i. The incidence identities are

    a_i c_j-a_j c_i=0.

At any preimage of z_i with target B different from κ(z_i)=[1:0:0:0], some c_j is a unit. Hence

    (a_1,a_2,a_3)=(a_j),

and the quotient coordinate extends as

    [u:v]=[b_0 a_j:c_j].

This remains valid when b_0=0. Substitution into evaluation gives the vector a_j(b_0,b_1,b_2,b_3). In particular the pullback evaluation base ideal is precisely (a_j).

## 2. No extra point bases at cusps

The zero locus of a_j is a Cartier divisor on W. It cannot contain a vertical curve: such a curve would map to the single point (B,z_i), contrary to finiteness of W -> P1 x P4. It cannot contain any new horizontal component: over the smooth modular open, the known preimage divisor of z_i is exactly the torsion lift D_i. Its multiplicity is one on that open. Thus globally, wherever B differs from κ(z_i),

    div(a_j)=D_i.

A Cartier divisor on a smooth surface has no extra isolated zero components. This proves there are no additional quotient indeterminacies or evaluation-ideal corrections at any cusp. Notice the argument uses a unit component c_j and the resulting principal ideal; it is not an extension assertion for arbitrary rational maps to P1.

The only remaining points with B=κ(z_i) are over the smooth modular locus. Their behavior has already been proved: one simple point base P_i on D_i, resolved by one ordinary blowup, and all other preimages extend by the vector-proportionality argument.

## 3. Finite normalization map

Let b:Wtilde=Bl_{P_1,...,P_50}W -> W. The quotient map now extends everywhere to P_Q(E). The pullback evaluation base ideal is invertible: it is the strict transform of the sum of the D_i, as proved locally at P_i and by the unit-component argument elsewhere. Hence it lifts to Xhat.

The image is the closure of the smooth-modular component, therefore the component of f^{-1}(Gamma) under discussion. The map is proper and birational. A positive-dimensional fiber not lying in a new point-blowup exceptional curve would contradict finiteness of W -> P1 x P4. Each new exceptional curve maps isomorphically to the original quotient P1 over z_i by the local simple-pencil calculation. Thus the map is quasi-finite, hence finite. Since Wtilde is normal, it is the normalization of that dominating component.

This leaves open whether the full raw inverse image has additional components lying over cusp parameters. Such components do not alter the normalization statement for the dominating component.

## 4. Corrected global tautological formula

Write F_i for the fifty point-blowup exceptional curves, C_S for the sum of the twenty-five torsion sections on S, and F for the modular fiber class. The local ideal calculation gives globally

    sum E_i|Wtilde = b^*pi^*C_S - sum F_i.
    A|Wtilde = b^*pi^*(6F).
    L|Wtilde = b^*pi^*(C_S+6F) - sum F_i.

Here A=f^*O(1)=L-sum E_i and C_S=5I. The ambient hyperplane class is b^*h with h=ξ+I on W. Consequently the original eigenquotient line 2L+(k-5)h restricts to

    b^*(pi^*(10I+12F)+(k-5)h) - 2 sum F_i.

This formula does not prove an eigenquotient exclusion. In particular the resulting twist-four linear series can still have many sections after fifty double-point conditions.
