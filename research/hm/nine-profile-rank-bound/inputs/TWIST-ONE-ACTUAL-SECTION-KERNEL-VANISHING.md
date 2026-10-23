# The actual rank-seventeen kernel has no twist-one sections

## Result

For the actual even twist-four hyperplane section bundle E = E4,+ on T = P(W*),

    H0(T,E(1)) = 0.

Consequently, if E is written nonequivariantly as a direct sum of line bundles O_T(a_i), every a_i is at most -2. With rank E = 17 and degree E = -54, one may write

    E = direct sum_(i=1)^17 O_T(-2-b_i),
    b_i >= 0,     sum b_i = 20.

This is a constraint on the actual splitting type, not a determination of it. It does not exclude generic rank two of the actual second fundamental form.

## 1. Direct proof using the actual relative sequence

The already proved uniform twist-four/twist-five hyperplane cohomology gives the actual equivariant identification

    E5,- = E4,+(1) = E(1).

The twist by O_T(1) is center-odd, so the right-hand side is physically inversion-odd, as required. This is not an identification that forgets the inversion linearization.

Let p : X = Bl_R(P4) -> P4 and pi : X -> T be the universal hyperplane family. By the definition of direct image and p_*O_X = O_P4,

    H0(T,E5,-)
      = H0(X,p*B(5))_-
      = H0(P4,B(5))_-.

The established actual exterior-symmetric evaluation resolution identifies multiplication as

    H0(P4,B(5)) = Sym^2 H0(P4,F(3)) = 1 + P4 + D5.

Every displayed summand is physically inversion-even; this parity is stated explicitly in TWIST-FIVE-GLOBAL-COHOMOLOGY-AND-BOUNDARY-DEFECT.md. In particular the odd group is zero. Therefore H0(E(1)) = 0.

No higher direct-image comparison or generic base change is needed for this global-section argument.

## 2. Independent common-annihilator/Koszul check

Use the actual kernel presentation

    0 -> E -> M3,- tensor O_T(-1)
      -> M4,+ tensor O_T -> 0,

where dim M3,- = 54 and dim M4,+ = 37. After twisting by O_T(1), global sections identify H0(E(1)) with

    { k in M3,- : u k = 0 and v k = 0 },

where u,v are a basis of the negative normal-coordinate space W. The middle source has odd physical parity: M3,- is odd and O_T(-1) tensor O_T(1) is even. The target's sections M4,+ tensor H0(O_T(1)) are also odd because H0(O_T(1)) is the negative two-space (up to the harmless dual convention).

The codimension-two ideal of the positive fixed plane R has its equivariant Koszul resolution. Tensoring it by B(5) gives

    0 -> B(3) tensor wedge^2 W
      -> B(4) tensor W
      -> I_R B(5) -> 0.

Its first map sends k, up to a common basis sign, to (-v k,u k). The determinant factor wedge^2 W is physically even, while W is odd. Since H0(B(4)) = 0, the cohomology sequence gives

    H0(I_R B(5))
      = ker[H1(B(3)) tensor wedge^2 W
             -> H1(B(4)) tensor W].

The physically odd block of this kernel is precisely the common u,v annihilator in M3,- (with its one-dimensional determinant factor). On the other hand,

    H0(I_R B(5))_- subset H0(B(5))_- = 0.

This proves the same vanishing and explicitly checks both twists and physical parity in the suggested Koszul route.

## 3. Splitting consequence and scope

By the splitting theorem for bundles on P^1, E is a direct sum of O_T(a_i). Since H0(O_T(a_i+1)) is zero exactly when a_i <= -2, the global vanishing proves the stated summand bound. The integers b_i = -a_i-2 are nonnegative, and their sum is

    -deg E - 2 rank E = 54-34 = 20.

This constraint may be retained in any further analysis of rank-two or higher Gauss transforms. It does not by itself supply a complete rank-two flag, select its rank profile, prove a contradiction for rank two, or establish maximal generic rank 13.

## Dependencies

- UNIFORM-TWIST-FOUR-FIVE-HYPERPLANE-COHOMOLOGY.md: the actual identity E5,- = E4,+(1).
- TWIST-FIVE-GLOBAL-COHOMOLOGY-AND-BOUNDARY-DEFECT.md: the actual multiplication description and physical evenness of H0(B(5)).
- POSITIVE-DOUBLE-HYPERPLANE-GAUSS-GATE.md: the actual rank-seventeen kernel and its degree.

No selected HM coefficients, actual matrix/rank evaluations, or local-model experiments are used.
