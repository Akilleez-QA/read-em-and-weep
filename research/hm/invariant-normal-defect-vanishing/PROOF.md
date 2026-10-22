# Invariant acyclicity of the actual first-normal adjoint defect

## Result and scope

Let X be the smooth weighted stack P(1,1,2,2), with physical O_X(1)=O_wt(2), and let Gamma=SL_2(F_5) be the finite symmetry group. Write G for the actual rank-two Serre bundle, sigma for its invariant regular section, I=I_Z for its zero ideal, B=End_0(G), and L=det(G)=O_X(2). Let 2Z denote the ordinary square thickening V(I^2), not the square of a coarse annihilator ideal.

The new conclusion is

    H^0(O_(2Z)(1))^Gamma = H^1(O_(2Z)(1))^Gamma = 0.

Consequently the actual first-normal tangent-modulo-conjugation quotient

    D = M(-2) = omega_(2Z)(-1)

is invariantly acyclic:

    H^0(D)^Gamma = H^1(D)^Gamma = 0.

Higher cohomology vanishes because the support is one-dimensional. This is a statement about this specific quotient sheaf. It does not assert acyclicity of the surrounding deformation complex, a lift of a differential operator, gluing to a specified first-normal bundle, or vanishing of the absolute positive cubic obstruction.

## Pinned inputs

All paths below are in `research/hm/order-four-quadratic-load/` of Akilleez-QA/read-em-and-weep.

1. [Global defect and dualizing twist](https://github.com/Akilleez-QA/read-em-and-weep/blob/71c684df379a32aa6d1f84d6af440d59e4cc20c0/research/hm/order-four-quadratic-load/GLOBAL-NORMAL-ADJOINT-DEFECT-DUALIZING-TWIST.md): M=omega_(2Z)(1), D=M(-2), and proper Cohen--Macaulay duality. The stack has omega_X=O_X(-3).
2. [Actual square sequence](https://github.com/Akilleez-QA/read-em-and-weep/blob/71c684df379a32aa6d1f84d6af440d59e4cc20c0/research/hm/order-four-quadratic-load/WEIGHTED-STACK-SQUARE-SHADOW-AND-PRIMARY-SCALAR.md), Sections 1--2: sigma is regular, det G=O(2), and 0 -> G -> B(2) -> I^2(4) -> 0, with first map multiplication by sigma under B(2)=Sym^2G.
3. [Negative invariant cone groups](https://github.com/Akilleez-QA/read-em-and-weep/blob/71c684df379a32aa6d1f84d6af440d59e4cc20c0/research/hm/order-four-quadratic-load/NORMAL-QUADRATIC-BRACKET-COMPONENT-SHADOW-GATE.md), Sections 1 and 4: H^1(B(-2))^Gamma=C eta and H^2(B(-2))^Gamma=0. Stack and cone cohomology agree for B by exact tame coarse pushforward. The trace pairing identifies B with B*.
4. [Serre-residue double-cover theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/0a93b2a6413ec612b935c299086a07a37de00dcb/research/hm/order-four-quadratic-load/NORMAL-QUADRATIC-NONZERO-BY-SERRE-RESIDUE-DOUBLE-COVER.md), Section 2: H^0(G*)=0 and H^1(G*)=W' tensor W'=1+V. These groups follow from the displayed ambient spinor presentation and the actual primary cohomology. The later geometric dependency on the three monad channels is supplied explicitly by [PR643's proof](https://github.com/Akilleez-QA/read-em-and-weep/blob/356a3b8d2da36f5b3e2034cc5c6adf82757a33cc/research/hm/three-channel-monad-family/PROOF.md).
5. [Midpoint square-zero adjoint theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/0fdb493ec11b0f51e0a2d61841c24c067cec9ef5/research/hm/order-four-quadratic-load/MIDPOINT-NORMAL-EXTENSION-HAS-UNIQUE-SQUARE-ZERO-ADJOINT.md): for N corresponding to sigma^2, the actual map eta -> [eta,N] from H^1(B(-2))^Gamma to H^1(B)^Gamma is nonzero. This uses the two distinct ambient extension endpoints, their midpoint, and the nonzero endpoint boundary; it is not inferred merely from dimensions.

These are mathematical dependencies, not a fresh independent proof of the entire HM foundation. The deduction below checks their twists, the actual map between the two invariant lines, and its consequence.

## 1. The exact sequence and its Serre-dual map

Twist the square sequence by minus three:

    0 -> G(-3) --j--> B(-1) -> I^2(1) -> 0.       (1)

Serre duality on X, with omega_X=O(-3), identifies the transpose of

    H^2(j): H^2(G(-3)) -> H^2(B(-1))

with

    H^1(j^vee): H^1(B(-2)) -> H^1(G*).            (2)

There is no twist ambiguity: B(-1)^* tensor omega_X=B(-2), while G(-3)^* tensor omega_X=G*. Also G*=G tensor L^(-1)=G(-2).

The map j^vee is evaluation by sigma, followed by G(-2)=G*, up to a fixed nonzero scalar. We verify this rather than assume it from dimensions.

Locally trivialize L and write omega(a,b)=a wedge b. Use the rank-two identification J:Sym^2G -> End_0(G) tensor L defined by

    J(a b)(w) = (a omega(b,w) + b omega(a,w))/2.

For a tracefree T, preservation of the alternating form infinitesimally gives

    omega(Ta,b)+omega(a,Tb)=0.

A rank-one trace calculation therefore gives

    tr(T J(sigma v)) = omega(v,T sigma).

The right side is precisely the functional on v obtained from T sigma by the determinant identification G(-2)=G*, with a possible common sign according to that identification's convention. Thus (2) is the claimed evaluation map. This identity is universal in a rank-two bundle and uses no selected actual coefficients or point evaluations.

## 2. Nonzero bracket forces the evaluation map to be nonzero

The same universal identification is equivariant for the tracefree infinitesimal action. Thus

    [T,J(sigma^2)] = J(2 sigma (T sigma)).          (3)

Restoring line factors, the sheaf bracket B(-2) -> B with N in B(2) factors as

    B(-2) --T maps to T sigma--> G(-2)
           --multiply by 2 sigma--> Sym^2G(-2)=B.

Formula (3) remains a factorization on H^1 because sigma is a global section. The midpoint theorem states that [eta,N] is nonzero. Hence the evaluation class eta sigma in H^1(G(-2))=H^1(G*) is nonzero. Both source and target invariant parts of (2) are one-dimensional, by pinned inputs 3--4. Therefore (2) is an isomorphism on invariants. Its Serre transpose H^2(j) is also an isomorphism on invariants.

All dualities are Gamma-equivariant. Taking Gamma-invariants is exact over C and the invariant Serre pairings remain perfect. The canonical line identifications carry no hidden Gamma-character, since Gamma is perfect. No larger block-torus character is being suppressed or used.

## 3. Cohomology of the square ideal at twist one

Serre duality and the pinned groups give

    H^1(B(-1))^Gamma = H^2(B(-2))^{Gamma,*} = 0,
    H^2(B(-1))^Gamma = H^1(B(-2))^{Gamma,*} = C,
    H^2(G(-3))^Gamma = H^1(G*)^{Gamma,*} = C,
    H^3(G(-3))^Gamma = H^0(G*)^{Gamma,*} = 0.

Consequently the relevant part of the invariant long exact sequence of (1) is

    0 -> H^1(I^2(1))^Gamma -> C --isomorphism--> C
      -> H^2(I^2(1))^Gamma -> 0.

Both ideal groups vanish.

For completeness, O_X(1) has H^0=V+W and no invariant section. Its positive-degree cohomology vanishes: the exact tame coarse pushforward is O_Q(1), and the quadric hypersurface sequence

    0 -> O_P4(-1) -> O_P4(1) -> O_Q(1) -> 0

gives this directly from projective-space line-bundle cohomology. Apply invariants to

    0 -> I^2(1) -> O_X(1) -> O_(2Z)(1) -> 0.

The preceding vanishings yield

    H^0(O_(2Z)(1))^Gamma = H^1(I^2(1))^Gamma = 0,
    H^1(O_(2Z)(1))^Gamma = H^2(I^2(1))^Gamma = 0.

This retains the entire ordinary square thickening, including possible nilpotent sections; it is not an argument from reduced-support negativity.

## 4. The defect quotient and the remaining comparison

The ordinary square of a codimension-two regular ideal is Cohen--Macaulay of dimension one. Proper Cohen--Macaulay duality for its dualizing sheaf gives

    H^i(omega_(2Z)(-1))^Gamma
       = H^(1-i)(O_(2Z)(1))^{Gamma,*}, i=0,1.

Both sides vanish in the stated degrees. Combining this with the independently established identification D=omega_(2Z)(-1) proves the result.

This removes both invariant global sections and invariant degree-one cohomology of the normal adjoint defect quotient. The next distinct task is to compare the actual Hessian overlap discrepancies and their surrounding tangent/gauge or differential-operator complex to this quotient. A quotient with vanishing H^1 does not by itself kill cohomology in the image sheaf or guarantee a chosen lift through that image. Likewise H^0(D)^Gamma=0 does not say every nonglobal local defect is zero. Those comparison maps, prescribed-bundle gluing, and the absolute cubic gate remain open here.

## Verification status

Authored structural deduction from the pinned inputs. The local transpose and bracket identities are verified above in a general rank-two frame; cohomology follows from exact sequences and equivariant duality. No selected HM/source instance, numerical rank, large computation, or formal proof assistant check is used or claimed.
