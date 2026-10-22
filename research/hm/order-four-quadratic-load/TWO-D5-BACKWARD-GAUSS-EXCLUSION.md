# Two-D5 backward Gauss exclusion

## Result and scope

In the hypothetical generic-rank-three profile `(k,l)=(3,2)`, all three
formal primal splitting types whose quadratic section module contains
`2D5` are impossible. These are precisely the three types that the frozen
adjacent-profile argument restricted to a derivative image
`O(4) + O(8)` and dual type 3 or 5.

Together with the two earlier primal exclusions, this leaves **at most 23
of the original 28 formal primal types** for `(3,2)`. The exceptional type
with no quadratic sections remains among them. This does not exclude the
profile `(3,2)` or generic rank three. The established bounds generic SF
rank at least 3 and positive-square rank at least 27 do not change. No
smoothing or generic-section-count conclusion is asserted.

The new ingredient is to follow the next backward derivatives after the
forced positive image. Complete evaluation kernels and ordinary degree
bounds then leave an inaccessible negative line in a required rank-three
derivative quotient.

Only abstract representation arithmetic, hypothetical bundle splittings,
universal evaluation sequences, differentiation, and invariant-divisor
bounds are used. No selected HM/source coefficients, actual-instance map
or rank evaluations, scans, or local-model experiments are used. Frozen
inputs and their verifiers are left unchanged.

## 1. Frozen input and notation

Use `ADJACENT-RANK-THREE-GAUSS-EXCLUSION-AND-CONSTRAINTS.md`, particularly
Sections 5 and 8, and its frozen inputs
`ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md` and
`EXCEPTIONAL-CUBIC-GAUSS-CORNER-EXCLUSION.md`.

Write `P=P4`, `D=D5`, `S=S4`, `T=T6`. The standard odd two-space is `W`,
the other odd two-space is `W'`, and `A=Sym^2 W`.
All bundles are on the binary-icosahedral parameter line. Representations
in tensor products with line bundles are coefficient spaces. We write
`O(e)` with its standard linearization. The group is perfect, so no
unrecorded character can twist a line.

For `(k,l)=(3,2)`, the rank-three plateau is

    F0 < F1 < F2 < F3=E < F4 < F5.

Put `K=E^-=F2`, `K2=E^{--}=F1`. Both K and K2 are interior stages, so

    K^+=E,       K2^+=K,
    rank(beta_K)=rank(beta_K2)=3.                         (1)

Persistence gives

    H0(K(2))=0,       H0(K2(3))=0.                       (2)

For the three types under consideration, the frozen argument gives

    R=H0(E(2)) = P+2D or 2D,
    phi: R O -> Q,       im(phi)=J=O(4)+O(8),
    psi: T O -> E*(1),   rank(psi)=1,
    B=0.                                                  (3)

Both phi and psi are injective on global sections. The dual bundle Q* is
one of the frozen types 3 or 5. Their two largest ordinary degrees in Q
are 8 and 6. The three primal types are exactly

    E_A = (P+2D) O(-2) + 2O(-8) + O(-10),
    E_B = (P+2D) O(-2) + O(-8) + W O(-9),
    E_C = 2D O(-2) + W' O(-3) + V O(-4) + 2O(-8).          (4)

These formulas concern formal necessary types, not realizations.

## 2. The full derivative quotient is forced

### 2.1 The rank-one dual image

The image of psi is a globally generated center-odd line O(e). Injectivity
on sections requires T in `Sym^e W`. Every ordinary degree in E*(1) is at
most 11, 10, or 9 in the three cases. Testing the odd degrees against

    Hom_G(O(e), E*(1))

gives exactly

    E_A: e=9 or 11;
    E_B: e=9;
    E_C: e=9.                                             (5)

This is finite character arithmetic, reproduced by the verifier. For
example, invariants of degrees 2, 4, and 6 are absent. The available
section modules are `Sym^9 W=S+T` and `Sym^11 W=W+S+T`.

The image O(e) is saturated in E*(1): its possible saturation defect is
bounded by the maximum ordinary degree minus e, at most 2 in (5). A
positive equivariant torsion length is at least 12, so the defect is zero.

### 2.2 Saturation of the quadratic image

The saturation of J in Q has degree at most `8+6=14`, by the determinant
inclusion into `wedge^2 Q`. Since `deg J=12`, its possible defect is again
at most 2, hence zero. Thus J is saturated in Q.

Put

    I = im(beta_E(2): E(2) -> Q).                         (6)

The projection to the cubic evaluation dual `T O(3)` is the negative
transpose of psi, twisted by 3. Since O(e) is saturated in E*(1), duality
gives a surjection

    E(2) -> O(3-e).

The subsequent injection `O(3-e) -> T O(3)` is the dual of the surjection
`T O -> O(e)`. Thus the projected image of I is exactly O(3-e).
Its rank-two kernel contains J because B=0, and equals J because J is
saturated in Q. Consequently

    0 -> J -> I -> O(3-e) -> 0,
    I = O(4) + O(8) + O(3-e),
    E/K = I(-2) = O(2) + O(6) + O(1-e).                  (7)

The extension splits because its two extension groups are
`H1(O(e+1))` and `H1(O(e+5))`, both zero. Averaging makes this splitting
equivariant. No splitting of a differential operator is being asserted.

## 3. Universal evaluation kernels

For any n at least 1, complete evaluation on the parameter line has the
equivariant exact sequence

    0 -> Sym^(n-1) W O(-1)
      -> Sym^n W O
      -> O(n) -> 0.                                      (8)

One direct proof uses the tautological O(-1) line of binary linear forms
vanishing at a point: multiplication with degree n-1 forms identifies the
fiberwise evaluation kernel. This is an SL2-equivariant universal
identity, hence also valid for the binary icosahedral subgroup.

The relevant characters are

    Sym^3 W=S,       Sym^4 W=D,
    Sym^6 W=V+P,     Sym^7 W=W'+T,
    Sym^8 W=P+D.

Define

    C = S+W'+T,       C' = A+V+P.                        (9)

Then

    H0(J)=P+2D,
    ker(H0(J) O -> J) = C O(-1),
    H0(O(3)+O(7))=C,
    ker(C O -> O(3)+O(7)) = C' O(-1).                  (10)

These are complete evaluation statements. They do not identify the
ambient derivative with any chosen coordinate formula.

## 4. Excluding E_A and E_B

Here R=P+2D=H0(J). Since phi is injective on sections, it identifies R
with the full section module of J. Its kernel, before the twist by 2, is
therefore

    ker(R O(-2) -> J(-2)) = C O(-3).                     (11)

Write `E=R O(-2)+H`, with H the high negative part displayed in (4).
The map from `R O(-2)` to the last quotient line O(1-e) in (7) vanishes
by degree. Thus the quotient map restricts to a surjection

    H -> O(1-e).

If H_tail denotes its kernel, K fits into

    0 -> C O(-3) -> K -> H_tail -> 0.                       (12)

Each H_tail below has all ordinary degrees at most -8, so this extension
splits. Equivariant averaging is again legitimate.

### 4.1 All high kernels

The complete list is

    E_A, e=11: H_tail=2O(-8);
    E_A, e=9:  H_tail=O(-8)+O(-10);
    E_B, e=9:  H_tail=W O(-9), or H_tail=O(-8)+O(-10).          (13)

For E_A, this follows directly by degree and the absence of degree-two
invariants. For E_B, a map `O(-8)+W O(-9) -> O(-8)` consists of a scalar
on the first line and a scalar multiple of the unique evaluation
`W O(-9) -> O(-8)`. If the first scalar is nonzero, its kernel is the
graph W O(-9). If it is zero, surjectivity forces the latter evaluation
to be nonzero, and (8) gives kernel `O(-8)+O(-10)`.

### 4.2 Immediate exclusions

The next derivative, using (1) and (7), is

    beta_K(3): K(3) -> (E/K)(1)
                       = O(3)+O(7)+O(2-e).              (14)

For `E_A,e=11`, the source is `C O+2O(-5)`, and the last target line is
O(-9). Every map to that line is zero by degree, so the derivative has
rank at most 2, contradicting (1).

For the E_B branch with `H_tail=W O(-9)`, the source is `C O+W O(-6)`,
and the last target line is O(-7). The same contradiction follows.

### 4.3 The common remaining high kernel

It remains to consider e=9 and `H_tail=O(-8)+O(-10)`. Now

    K(3)=C O+O(-5)+O(-7),
    (E/K)(1)=O(3)+O(7)+O(-7).                            (15)

By (2), the section map of (14) is injective. Both its source and target
section modules are C, so it is an isomorphism. Therefore the restriction
of (14) to `C O` surjects onto `O(3)+O(7)`: it is complete evaluation
up to an automorphism of C. Its projection to O(-7) is zero by degree.

The O(-5) summand cannot map to O(-7). Generic rank 3 now forces the
constant map from the last O(-7) summand to O(-7) to be nonzero. It is an
isomorphism, and (14) is surjective onto its entire target. Its kernel is

    K2(3)=C' O(-1)+O(-5),
    K2=C' O(-4)+O(-8).                                  (16)

Indeed the complete-evaluation kernel is given by (10); the extension by
O(-5) splits because `H1(O(4))=0`. Contributions of the two negative
source summands to the positive target do not change this exact kernel
calculation.

Since (14) is surjective,

    K/K2 = O(0)+O(4)+O(-10).

The next required rank-three derivative is consequently

    beta_K2(4): C' O+O(-4) -> O(2)+O(6)+O(-8).           (17)

There is no map from either source degree 0 or -4 to O(-8). This
contradicts (1) and excludes the last branches of E_A and E_B.

## 5. Excluding E_C by an ordinary kernel bound

Here e=9 and

    E/K=O(2)+O(6)+O(-8).

Only the final `2O(-8)` in E_C can map to the last quotient line.
The surjection to that line has kernel O(-8) on this two-line block.
Put

    F=2D O(-2)+W' O(-3)+V O(-4),
    L=ker(F -> O(2)+O(6)).                              (18)

The map `2D O(-2) -> O(2)+O(6)` is already surjective, since its twist
by 2 is phi onto J. Thus K fits into

    0 -> L -> K -> O(-8) -> 0.                          (19)

The map on the two D section copies is injective into

    H0(J)=D+(P+D).

Its map to the D-isotypic part is an isomorphism. Changing the coefficient
basis of the source therefore identifies this evaluation kernel with

    N := ker(2D O(-2) -> O(2)+O(6))
       = S O(-3) + B0(-2),                              (20)

where `B0=ker(D O -> O(8))`. The second map in this definition is the
D-subsystem evaluation and is surjective, as also follows from the
surjectivity to J after the coefficient basis change. It has

    rank B0=4,     deg B0=-8,     H0(B0)=0.

Every ordinary summand of B0 therefore has degree at most -1. Since the
four degrees sum to -8, every one is also at least -5. Hence every
ordinary degree in N is at least -7.

There is an exact sequence

    0 -> N -> L -> W' O(-3)+V O(-4) -> 0.                (21)

It follows that L(7) is globally generated: both end bundles after this
twist are globally generated, and `H1(N(7))=0`, so their sections lift.
Thus every ordinary degree in L is at least -7. Likewise (19) implies
that K(8) is globally generated, so every ordinary degree of K is at
least -8.

But the next derivative has target

    beta_K: K -> (E/K)(-2)=O(0)+O(4)+O(-10).             (22)

No summand of K can map to O(-10). Its rank is at most 2, contradicting
(1). This excludes E_C.

## Verification

Run `python3 verify_two_d5_backward_gauss_exclusion.py` in this directory.
It runs the frozen arithmetic inputs without modifying them, checks all
three primal types, enumerates the rank-one image degrees, checks the
saturation bounds and evaluation characters, exhausts the relevant
ordinary kernel-degree partitions, and checks every final negative-line
obstruction and the remaining formal-type count.

The derivative, saturation, evaluation-kernel, and extension arguments
are proved above. The script is not an actual map/rank test and does not
replace those geometric proofs.
