# Type IV radical image and annihilator: doubled Euler geometry

## Scope and authenticated input

Work over C on the original negative parameter line with fixed G=SL2(F5) action and determinant convention. The mathematical dependency is PR1127 at commit `60dda5a940d5ba7ee081a86cd1b1a783a5952a39`, `research/hm/primary-quotient-composition/PROOF.md`, retained and hashed in INPUTS.json. Its results and dependencies are assumed, not proof-assistant verified here.

CONDITIONALLY on its necessary type IV, the canonical complement K in E=L⊕K, L=W'O(-3), has type

    K = C1 ⊕ C2 ⊕ D,
    C1=C2=T O(-3),         D=V O(-4),         T=W⊗V.

The notation denotes a temporary equivariant decomposition. PR1127 proves End_G(E) has a two-dimensional square-zero Jacobson radical J, consisting of the two maps D→Ci, and that L is isolated. Thus J is also the radical of End_G(K). No assertion that type IV occurs or is selected is made.

## Universal Euler calculation

Choose determinant-compatible formal coordinates x,y. With Id on V define

    a=(x Id,y Id)^t: V O(-4)→T O(-3),
    b=(-y Id,x Id): T O(-3)→V O(-2).

The Euler sequence 0→V O(-4)→T O(-3)→V O(-2)→0 is equivariant and exact. The two minors x³,y³ certify that a is everywhere a subbundle inclusion; b has minors -y³,x³ and is everywhere onto. On x≠0 the left inverse of a is (x^-1 Id,0), and a right inverse of b is (0,x^-1 Id)^t. On y≠0 they are (0,y^-1 Id) and (-y^-1 Id,0)^t. Each pair satisfies a ell+rho b=Id. These are formal chart identities, not sampled ranks.

The one-dimensional equivariant Hom channel V O(-4)→T O(-3) is spanned by a. Write V1,V2 for its embeddings into C1,C2. They span J. All four products ViVj vanish because every Vi kills C1⊕C2.

## Intrinsic three-step filtration

Let S be the image of evaluation J⊗K→K and A the common annihilator ker(K→J*⊗K). The two independent image channels give

    S = a(V O(-4)) ⊕ a(V O(-4)) ⊂ C1⊕C2,
    S ≅ 2V O(-4),                 rank6, degree-24.

Because a is injective, V1(k)=V2(k)=0 precisely when k's D component is zero. Hence

    A=C1⊕C2 ≅ 2T O(-3),           rank12, degree-36,
    A/S ≅ 2V O(-2),               rank6, degree-12,
    K/A ≅ V O(-4),                rank3, degree-12.

In particular S is a proper subbundle of A. Both S⊂A and S⊂K are saturated: their quotients are respectively 2V O(-2) and 2V O(-2)⊕V O(-4). A is saturated as well. The image and annihilator definitions are intrinsic because J is canonical; an auxiliary decomposition is only used to compute their types. The ideal property also makes them invariant under every global equivariant endomorphism.

On total E the image is still S and the common annihilator is L⊕A, of rank14 and degree-42. Its quotient is V O(-4). There are no claims about operators outside the global equivariant bundle endomorphism algebra.

## Nonsplit middle extension

The intrinsic sequence

    0 → S → A → A/S → 0

is the doubled Euler extension and is nonsplit even as ordinary vector bundles. After twisting by O(2), A has type12 O(-1), so h0(A(2))=0. Meanwhile S(2) has type6 O(-2) and (A/S)(2) has type6 O, so the direct sum would have h0=6. This is impossible. Thus J²=0 again does not imply that its induced bundle filtration splits. The different sequence 0→A→K→K/A→0 does admit a splitting in the displayed type; no canonical choice is claimed.

## Exact reproduction and limitations

`python verify.py` and `python -O verify.py` produce the same RESULT.json, with109 checks:68 inherited universal type III/Euler controls and41 type IV controls. The standard-library code uses exact integer Laurent polynomials and full15×15 and17×17 matrices, not sampled points. Two-chart image and common-kernel factorization identities and quotient homotopies prove the specified image, annihilator and saturation certificates. The input SHA256 and Git blob are checked.

The universal matrices do not independently prove the pinned representation or primary-geometry inputs. No actual source point, direction, tensor, matrix, derivative, jet, scan or one-shot experiment is evaluated. There is no type selection, positive/Q/Gauss compatibility, geometric coverage, full-adjoint invertibility or completion of the original repair.
