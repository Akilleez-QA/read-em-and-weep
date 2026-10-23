# The single-V quadratic type is excluded by backward evaluation

## Result and scope

In the hypothetical generic-SF-rank-three plateau `(k,l)=(3,2)`, the formal primal type

    E = V O(-2) + (Wprime+T6) O(-3) + 2V O(-4)

is impossible. Its coefficient tuple in the frozen eight-variable classification is
`(1,1,2,0,0,0,0,0)`. This is a new exclusion, disjoint from the eleven previously excluded types, leaving **at most 16 of the original 28 formal primal types**.

The proof uses only universal representation identities, bundle images and degrees, complete evaluation, extensions, invariant divisors, and backward persistence. It does not select any actual HM/source coefficients or evaluate any actual map, matrix, rank, parameter scan, or local model. It neither excludes the whole adjacent profile nor improves the established generic SF rank bound 3 or square-rank bound 27.

## 1. Frozen inputs

Read together with:

- `ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md`;
- `ADJACENT-RANK-THREE-GAUSS-EXCLUSION-AND-CONSTRAINTS.md`;
- `RANK-THREE-CUBIC-PAIRING-EXCLUDED-IN-ADJACENT-GAUSS-PROFILE.md`;
- `TWO-D5-BACKWARD-GAUSS-EXCLUSION.md`;
- `SIX-LARGE-QUADRATIC-MODULES-EXCLUDED-BY-BACKWARD-GAUSS.md`.

Write `Wp=Wprime`, `P=P4`, `D=D5`, `S=S4`, `T=T6`. The saturated plateau is

    F0 < K2 < K < E < F4 < F5,

of ranks `8,11,14,17,20,23`. In particular

    H0(K(2))=0,   H0(K2(3))=0,   H0(F0(4))=0.             (1)

The derivatives of K and K2 both have generic rank three. Every positive invariant torsion/divisor length is at least 12.

There are five possible dual types. In every one, Q has maximum ordinary degree at most eight, and its canonical cubic evaluation is `T O(-3)` inside Q*. Put

    phi: V O -> Q,
    psi: T O -> E*(1),
    B: V O -> T O(3).

The first two are injective on sections. If their ranks are a and b and the pairing rank is t, then `a+b-3<=t`. The frozen pairing theorem says that B is zero or has image `Wp O(1)`. The latter has section module P and cannot receive the nonzero representation V. Hence B=0.

All splittings below are equivariant bundle splittings, not horizontal ones. Finite-group averaging is valid, and G has no nontrivial one-dimensional characters.

## 2. Force the full first derivative quotient

The target of psi is

    E*(1) = V O(3) + (Wp+T) O(4) + 2V O(5).              (2)

Its image cannot have rank one. A globally generated rank-one image would be an odd-degree line O(e), with `1<=e<=5`, receiving T on sections. Only e=5 passes the section condition, but `Hom_G(O(5),E*(1))=0`.

Thus b>=2. Since a>=1 and B=0, the rank inequality forces

    a=1, b=2.

The image of phi is an even-degree line of degree at most eight whose sections contain V. The unique possibility is

    J=O(6).

For psi, the absence of any eligible line summand and the rank-two equivariant splitting conditions give precisely

    L=Wp O(e),    e=2 or 4.                              (3)

These image sheaves are saturated in their respective targets. For J, the maximum possible saturation defect is `8-6=2`; for L it is `2*5-2e`, namely six or two. A positive invariant defect cannot be smaller than 12.

Let I be the actual image of `beta_E(2):E(2)->Q`. Duality with the saturated L identifies its projected image in `T O(3)` with `L*(3)=Wp O(3-e)`. The kernel is rank one and contains the saturated J, so equals J. Consequently

    0 -> O(6) -> I -> Wp O(3-e) -> 0.

This extension splits because `H1(O(3+e))=0`. Therefore

    A_e := E/K = O(4) + Wp O(1-e).                       (4)

The projection onto the second summand vanishes on `V O(-2)`, because B=0. The restriction to the first summand is the V-subsystem evaluation of O(6), twisted by -2, and is surjective since J is the actual image of phi.

## 3. Its first evaluation kernel is canonical

Let N0 be the kernel of the surjective evaluation `V O -> O(6)`. It has rank two, degree -6, and no sections. Its equivariant splitting is

    N0=Wp O(-3).                                        (5)

Here is a complete argument. A rank-two equivariant bundle is either a two-dimensional irreducible coefficient representation at a single degree or the sum of two equivariant lines. In the first case degree forces degree -3; the possibilities are W and Wp. The inclusion into V O permits Wp but not W, since

    V tensor Sym^3 W = Wp+S+T.

In the line case, no sections and central parity force the degrees to be -2 and -4. But `Hom_G(O(-2),V O)=0`, since `Sym^2 W=A` does not contain V. This proves (5).

After twisting by -2 the kernel is `N=Wp O(-5)`. Write

    H=(Wp+T) O(-3)+2V O(-4),
    H_e=ker[H -> Wp O(1-e)].

The map defining H_e is surjective by (4), and K fits into

    0 -> Wp O(-5) -> K -> H_e -> 0.                     (6)

## 4. The e=4 branch

In `H -> Wp O(-3)`, only the Wp O(-3) summand can map nontrivially: the T coefficient is different, and

    Hom_G(V, Wp tensor W)=Hom_G(V,P)=0.

The scalar on Wp is therefore an isomorphism. Thus `H_4=T O(-3)+2V O(-4)`. The extension (6) splits, since its only potentially nonzero degree-two Ext term has coefficient `Hom_G(T,Wp)=0`. We obtain

    K=T O(-3)+2V O(-4)+Wp O(-5).                         (7)

Now consider

    beta_K(3): T O + 2V O(-1) + Wp O(-2)
                         -> O(5)+Wp O(-2).              (8)

By (1) its section map is injective; source and target section modules both equal T. Hence its T block is complete evaluation onto O(5). Only Wp O(-2) can map to the other target block by degree. Generic rank three forces that scalar to be an isomorphism. Therefore (8) is surjective, and

    K/K2 = A_4(-2)=O(2)+Wp O(-5).

Subtracting the two exact quotients from E gives

    chi_G(K2(4)) = D+2V.                                (9)

The next derivative, twisted by four, has target

    (K/K2)(2)=O(4)+Wp O(-3),

whose section module is D. But (9) forces H0(K2(4)) to contain 2V: every irreducible multiplicity in H0 is its Euler multiplicity plus its nonnegative H1 multiplicity. This contradicts `H0(F0(4))=0`.

## 5. The e=2 branch: four exhaustive kernel shapes

Here the surjection defining H_2 is

    (Wp+T) O(-3)+2V O(-4) -> Wp O(-1).                  (10)

The Wp O(-3) component is zero. The T component has a single scalar coefficient alpha because `Wp tensor Sym^2 W=T`; the two V components are multiples of one universal map because `Wp tensor Sym^3 W=V+D`.

If alpha is nonzero, the T component is complete evaluation of Wp O(2), twisted by -3. Its kernel is P O(-4), and the remaining extensions split. Thus

    H_2=Wp O(-3)+(P+2V) O(-4).

If alpha is zero, surjectivity forces a nonzero combination of the two V components. Changing their coefficient basis leaves one V summand in the kernel. The other map `V O(-4)->Wp O(-1)` must be surjective; its kernel is an equivariant line of degree -10, hence O(-10). Thus

    H_2=(Wp+T) O(-3)+V O(-4)+O(-10).

For either form, the only possibly nonzero equivariant extension in (6) is the one-dimensional space joining Wp O(-3) to Wp O(-5). Its nonzero class is the standard evaluation extension

    0 -> Wp O(-5) -> P O(-4) -> Wp O(-3) -> 0.

All other Ext terms vanish by degree or `Hom_G(T,Wp)=0`. Consequently K is one of exactly these four necessary bundle shapes:

    A: Wp O(-3)+(P+2V) O(-4)+Wp O(-5);
    B: (2P+2V) O(-4);
    C: (Wp+T) O(-3)+V O(-4)+Wp O(-5)+O(-10);
    D: T O(-3)+(P+V) O(-4)+O(-10).                       (11)

These are necessary forms, not realizability assertions.

## 6. The next derivative is surjective in all four shapes

The target is now

    beta_K(3): K(3) -> O(5)+Wp O.                        (12)

For shape A, its Wp section module must map isomorphically onto the constant Wp target, because it cannot map on sections to O(5), whose sections are T. The kernel of the projection onto Wp is therefore

    L0=(P+2V) O(-1)+Wp O(-2).

Generic rank three forces a nonzero map `L0->O(5)`. Its image is `O(5-delta)` with invariant delta>=0. Every source degree is at least -2, so a nonzero map to this image forces delta<=7. The invariant-divisor gap implies delta=0. Thus (12) is surjective.

For shape B, only the P summands can map to Wp O, since `Wp tensor W=P` does not contain V. Generic rank three requires the projection onto Wp to have rank two. A nonzero combination of the two P blocks is complete evaluation `P O(-1)->Wp O`; its kernel is again precisely L0 above. The same invariant-divisor argument proves surjectivity of (12).

For shape C, source and target section modules both equal Wp+T. Persistence makes the section map an isomorphism. It is complete evaluation of the globally generated target, so (12) is surjective.

For shape D, the T section module maps by complete evaluation onto O(5) and maps trivially to Wp O. The V O(-1) summand cannot map to Wp O. If the P O(-1) component of that projection were zero, its image would come solely from the remaining line O(-7), of rank at most one, contradicting generic rank three of (12). Therefore the P component is nonzero and is complete evaluation onto Wp O. Combined with the T component, this proves surjectivity.

We have proved in every branch

    K/K2 = A_2(-2)=O(2)+Wp O(-3).                       (13)

## 7. Final character obstruction

Use (4) and (13) in equivariant K-theory. Exact character arithmetic gives

    chi_G(K2(4))
      = chi_G(E(4))-chi_G(A_2(4))-chi_G(A_2(2))
      = V.                                             (14)

Thus H0(K2(4)) contains V, irrespective of any H1. But the target of the next derivative is

    beta_K2(4): K2(4) -> (K/K2)(2)=O(4)+Wp O(-1),

whose section module is D. Its section map cannot be injective, contradicting `H0(F0(4))=0`. This excludes e=2, completes both branches, and proves the claimed new exclusion.

## 8. Exhaustive remaining-type bookkeeping and reproduction

Run `python3 verify_single_v_backward_evaluation.py`. It first runs the frozen universal verifiers, enumerates and prints all 17 previously remaining coefficient tuples and their full primal splitting bundles, checks that the selected tuple is new, and records 16 survivors after this exclusion. It also checks the complete eligible image-block lists, all saturation bounds, character identities and Ext multiplicities, the four kernel shapes, the universal evaluation-sequence characters, the divisor bound, and both final Euler-character obstructions.

No map coefficients or ranks are evaluated by this verifier. The image, derivative, extension, and persistence arguments are the geometric proof above.
