# Type III has a canonical image–annihilator bundle with a nonsplit quotient extension

## 1. Scope and pinned hypothesis

Work over C on the original negative parameter line P(W), with the fixed determinant convention and physical G=SL2(F5) action. The sole mathematical dependency is PR1127, commit `60dda5a940d5ba7ee081a86cd1b1a783a5952a39`, `research/hm/primary-quotient-composition/PROOF.md`, retained byte-for-byte in `inputs/PR1127-PROOF.md`. Its Git blob is `80faeb68639dc5f644397a54d5ca7a12009f616f`. That proof and its dependencies are assumptions here, not proof-assistant verification.

PR1127 constructs actual canonical E=L⊕K with L=W'O(-3) and rank(K)=15, degree(K)=-48. The results below are CONDITIONAL on its necessary type III. They do not establish that type III occurs, select it among four types, or eliminate it.

Temporarily choose an equivariant bundle decomposition

    K = B ⊕ C ⊕ D1 ⊕ D2,
    B=V O(-2), C=T O(-3), D1=D2=V O(-4),

where dim(V)=3 and T=W⊗V has dimension6. This is a computation in a chosen decomposition, not a claim that the original primary C has been canonically complemented.

In this note J means the Jacobson radical of End_G(K), not the primary T-summand denoted J in PR1127. PR1127's type III Hom calculation shows that L is isolated in End_G(E), so End_G(E)=C×End_G(K) and its radical identifies with J. The radical is three-dimensional, spanned by the arrow C→B and the two arrows Di→C. It is intrinsic and satisfies J²=0.

## 2. The Euler arrows, not pointwise rank guesses

Choose determinant-compatible coordinates x,y for the formal parameter doublet. Under T=W⊗V define

    a: V O(-4) → C,           a=(x Id_V, y Id_V)^t,
    b: C → B,                b=(-y Id_V, x Id_V).

These are the invariant Euler maps after the fixed determinant identification; hence they are equivariant. Both relevant equivariant Hom spaces are one-dimensional by PR1127, so these nonzero maps span the radical channels, up to irrelevant nonzero rescaling. In particular the model does not assume an unproved formula for an actual source matrix.

The coefficient identity ba=0 is exact. The upper/lower three-row minors of a are x³ and y³. The left/right three-column minors of b are -y³ and x³. They cover P1 and prove constant ranks3. More strongly, on the chart x≠0 put

    ell_x=(x^(-1) Id,0),      rho_x=(0,x^(-1) Id)^t;

on y≠0 put

    ell_y=(0,y^(-1) Id),      rho_y=(-y^(-1) Id,0)^t.

In each chart ell a=Id, b rho=Id and a ell+rho b=Id_C. Thus the sequence

    0 → V O(-4) --a→ T O(-3) --b→ V O(-2) → 0             (1)

is exact as bundles everywhere, not only at sampled parameters. The displayed local inverses are chart certificates, not globally defined bundle splittings.

Let U have block b from C to B and zero other blocks. Let V1,V2 have block a from Di to C and zero other blocks. These span J. All nine products vanish: UVi=ba=0 and every other product vanishes by its block support. This explains J²=0 without turning that algebra identity into a bundle-splitting assertion.

## 3. Intrinsic image and common annihilator

Define the image sheaf S=J·K to be the image of the evaluation morphism J⊗K→K. Define Ann_K(J) as the kernel of K→J*⊗K, k↦(f↦f(k)). These constructions do not depend on a basis for J or any chosen bundle decomposition.

The images in the temporary decomposition are

    im(U)=B,        im(V1)=im(V2)=a(V O(-4))⊂C.

Consequently

    S=B⊕a(V O(-4)) ≅ V O(-2)⊕V O(-4).                    (2)

For a local vector (b0,c,d1,d2), U kills it exactly when bc=0, and Vi kill it exactly when a(di)=0. Since a is an injection and ker(b)=im(a), the common kernel is exactly B⊕im(a). Therefore

    J·K = Ann_K(J) = S.

The quotient is locally free, by (1):

    K/S ≅ (C/im(a)) ⊕ D1 ⊕ D2
        ≅ V O(-2) ⊕ 2V O(-4).                           (3)

Thus S is saturated of rank6 and degree-18, and K/S has rank9 and degree-30. In total E, J annihilates L and has no image there, so

    J·E=S,          Ann_E(J)=L⊕S.

The latter has rank8, degree-24, and E/Ann_E(J) has rank9, degree-30. These equalities are intrinsic. Indeed, any equivariant bundle automorphism preserves J by conjugation, and preserves both its evaluation image and common kernel. Moreover the two-sided ideal property shows the same image and annihilator are preserved by every global equivariant endomorphism. No compatibility with additional operators is asserted.

## 4. The extension is not split, even without equivariance

Although J²=0, the short exact sequence

    0 → S → K → K/S → 0                                 (4)

does NOT split as ordinary vector bundles. Twist by O(2). The known type gives h0(K(2))=3, since its degrees become 0,-1,-2 with multiplicities3,6,6. Equations (2)–(3) give h0(S(2))=3 and h0((K/S)(2))=3. A split (4) would force h0(K(2))=6, a contradiction.

Equivalently, (4) is, in the temporary decomposition, the direct sum of identity/trivial pieces with the Euler extension (1). There can be no right inverse B→C of b because Hom(O(-2),O(-3))=H0(O(-1))=0. Its nontriviality is compatible with local splittings on both charts. The nilpotent radical records compositions of global equivariant endomorphisms; it does not require the corresponding sheaf filtration to split.

## 5. Reproducible exact certificates and limitations

`verify.py` uses only Python's standard library, exact integer Laurent polynomials, and explicit full matrices. It constructs the 15×15 radical generators on K and their 17×17 embeddings on E. It checks all products coefficientwise, all four Euler minors, both chart homotopies, and full image/common-kernel factorization certificates. In particular, with F the vertically stacked radical generators and q the displayed quotient, it checks q=HF and F=Gq on each chart; with R the horizontally concatenated generators and z the inclusion of S, it checks R=zC and z=RD. These identities establish equal kernels and images over the whole chart, rather than testing sample points. Analogous certificates are checked on E. The degree/rank calculations, nonsplitting h0 obstruction and input hashes are checked explicitly.

Run `python verify.py` and `python -O verify.py`; both produce `RESULT.json`. No selected HM/source point, direction, matrix, derivative, jet, rank experiment, scan or burn is used. The code certifies the displayed universal algebra; the argument identifying it with the conditional equivariant channels uses the pinned Hom theorem and Euler equivariance. There is no positive-coordinate, invariant-quadratic, Gauss, full graded-module, source occurrence, geometric coverage or full-adjoint assertion. The original proof repair remains open.
