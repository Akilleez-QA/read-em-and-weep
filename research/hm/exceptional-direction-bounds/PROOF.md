# Self-adjoint pencil rigidity and exceptional fourth-square directions

## Statement and imported actual-source hypotheses

Work over C. Retain all actual-frame/source hypotheses of [PR747](https://github.com/Akilleez-QA/read-em-and-weep/blob/0a0ee30a5142477e54245b7c6f22d561abb4f5f1/research/hm/source-family-fourth-square-exclusion/PROOF.md), at commit 0a0ee30a5142477e54245b7c6f22d561abb4f5f1. Put A=H^0(P^1,O(2))=Sym^2 W, k=C(P^1), H=D5. The fixed k-vector space V and nonzero d in V are those of that theorem. Its identity is

    K_actual(a,h)=a^2 Phi_h(a),
    Phi_h(a)=a K_h-gamma S_h(a)d,                 (1)

where gamma is the fixed nonzero canonical normalization, h -> S_h identifies H with the trace-free self-adjoint endomorphisms of A, and h != 0 implies S_h != 0. Every section in (1) is represented in the same rational trivialization. PR747 proves E_h=ker Phi_h is proper for h != 0 and that K_actual vanishes precisely on E_h minus zero.

The new conclusions are:

1. If S_h has three distinct eigenvalues, dim E_h <= 1. Thus at most one projective negative direction has zero immutable class. Every other projective direction has nonzero actual fourth-square scalar.
2. More generally, dim E_h=2 is possible only when S_h has a two-dimensional ordinary eigenspace. This is strictly stronger than requiring a repeated characteristic root.
3. Such a two-dimensional kernel has exactly one of two forms: a nondegenerate eigenspace with spectrum (lambda,lambda,-2lambda), lambda != 0; or a degenerate eigenspace, in which case S_h is nonzero, has one-dimensional image, and S_h^2=0. In the second case K_h=0 and the kernel is a common-factor pencil ell W.

These are universal structural implications, not evaluations of any chosen h, a, source coefficient, point, derivative, or actual-instance matrix rank. None asserts nonvanishing of the separate fourth Bockstein.

## Exact normalization and pairing pin

The source theorem [ACTUAL-CANONICAL-RAW-CUBIC-HAS-A-NONZERO-LINEAR-LIFTING-CORRECTION.md](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-CANONICAL-RAW-CUBIC-HAS-A-NONZERO-LINEAR-LIFTING-CORRECTION.md), sections 2 and 6, proves

    Sym^2 A=1+D5,     L_can(a,h)=gamma S_h(a), gamma != 0.

Its invariant nondegenerate symmetric form B is unique up to scalar. The binary-quadratic apolar form is also invariant, so is proportional to B. Rescaling B does not alter self-adjointness. No normalization of gamma is chosen here, and no computation from the source theorem's earlier eigenline sections is repeated.

The needed universal pairing identities can be derived without selecting a source instance. For arbitrary independent ell,m in W, put u=ell^2, v=ell m, w=m^2. The discriminant quadratic form on A is proportional to B(a,a); every square (ell+t m)^2 is isotropic. Polarizing its identically zero discriminant gives

    B(u,u)=B(u,v)=B(v,w)=B(w,w)=0,
    B(u,w)=c != 0,       B(v,v)=-c/2.            (2)

For clarity, the last ratio follows from the coefficient of t^2 in B(u+2t v+t^2 w,u+2t v+t^2 w)=0. Nondegeneracy forces c != 0. Here t is a formal indeterminate; ell,m are abstract basis variables, not selected actual directions to be tested.

## 1. Rational multiplication on a pencil is constant

Lemma. Let S:A->A be B-self-adjoint. Suppose independent a,b in A satisfy

    S(a)=r a,       S(b)=r b

as rational sections for the same r in k. Then r belongs to C.

Proof. Let E=span(a,b). The identities hold on E by C-linearity. A pole of r must lie in the common zero divisor of E, with at most its common vanishing multiplicity, since rE consists of regular sections of O(2).

If E has no basepoint, r has no poles, hence is constant on P^1. Otherwise the common divisor has degree exactly one: two independent quadratics cannot have a common quadratic factor. Therefore E=ell W for an abstract nonzero linear form ell. Choose any complementary m and use u=ell^2,v=ell m,w=m^2 as in (2). The only allowed poles of r lie on the divisor of ell and have order at most one. Hence

    r=p+q m/ell,        p,q in C,
    S(u)=p u+q v,      S(v)=p v+q w.

Self-adjointness on u,v and (2) now give

    -q c/2 = B(S(u),v)=B(u,S(v))=q c.

Since c != 0 and char C=0, q=0. Thus r=p is constant in the basepoint case as well. QED.

Self-adjointness is essential to the second case: preservation as regular sections alone permits the simple pole. No assertion about S on all rational sections is used; S is only C-linear on A.

## 2. Application to the actual immutable kernel

Fix h != 0. If E_h has a nonzero member, (1) and d != 0 force K_h=t_h d for a unique t_h in k. Then

    E_h={a in A: S_h(a)=(t_h/gamma)a}.          (3)

If dim E_h >= 2, the lemma makes t_h/gamma a constant lambda. Consequently

    K_h=gamma lambda d,
    E_h=ker(S_h-lambda I).                     (4)

Conversely, if a scalar lambda has a two-dimensional eigenspace and K_h=gamma lambda d, (1) makes that eigenspace exactly E_h. Its dimension cannot be three because S_h is nonzero and trace-free. Thus (4), together with the two-dimensional eigenspace condition, is an exact criterion, not just an implication.

In particular simple spectrum excludes dim E_h >= 2, proving conclusion 1. The result does not claim that a possible one-dimensional kernel is an ordinary eigenline: without two independent sections, t_h/gamma may still be nonconstant. If K_h is not in kd there is no exceptional direction at all, as already observed in PR747.

## 3. Classification of a two-dimensional eigenspace

Suppose E=ker(S-lambda I) has dimension two for a nonzero trace-free B-self-adjoint S on A.

### Nondegenerate E

If B restricted to E is nondegenerate, A=E direct-sum E-perp. Self-adjointness makes the one-dimensional E-perp invariant. Trace zero forces its eigenvalue to be -2lambda. If lambda=0 then S=0, excluded. Thus lambda != 0, S is diagonalizable, and its eigenvalues, with multiplicities, are (lambda,lambda,-2lambda). Its repeated eigenspace is exactly E. Applied to (4), the additional immutable equality remains K_h=gamma lambda d.

### Degenerate E

If B restricted to E is degenerate, E-perp is a line Cu contained in E. Put T=S-lambda I. It kills E and, by self-adjointness, its image is contained in E-perp: for every x and e in E, B(Tx,e)=B(x,Te)=0. Thus T has the form

    T(x)=c B(u,x)u

for some c in C, because the annihilator of E is generated by B(u,-). Since u belongs to E-perp, B(u,u)=0. Therefore T^2=0 and tr T=0. Trace zero for S=lambda I+T gives 3lambda=0, so lambda=0. Nonzero S forces c != 0. Hence S is nonzero with one-dimensional image Cu, S^2=0, and E=ker S=u-perp.

An isotropic binary quadratic u is a square, up to a scalar: u=ell^2. Formula (2) identifies u-perp with ell W. Hence the degenerate eigenspace is precisely a common-factor pencil. Equation (4) requires K_h=0 in this case.

Conversely these two forms have two-dimensional eigenspaces; they yield a two-dimensional actual immutable kernel only if the corresponding equality in (4) also holds. Repeated characteristic roots alone are insufficient: for example the criterion excludes any nonzero nilpotent S with S^2 != 0. This exclusion is by the general argument, not by constructing or evaluating an example.

## 4. Pure-square directions and scope

The pure-square directions form the isotropic conic B(a,a)=0 in P(A). For simple-spectrum h there is at most one exceptional projective direction in all of P(A), and therefore at most one exceptional square direction.

Conditionally, if dim E_h=2, the classification also determines its intersection type with the conic. In the nondegenerate case B restricted to E_h is a nondegenerate binary form, giving two distinct square directions over C. In the degenerate case E_h=ell W, giving only the one square direction [ell^2], with intersection multiplicity two. These statements describe the zero set of the immutable class, not the full scalar-square zero set. They do not evaluate the location or existence of the actual kernel in any selected fiber.

The new dependency resolved is the common-basepoint gap in passing from a two-dimensional rational eigen-pencil to a repeated ordinary eigenspace. The resulting simple-spectrum bound strengthens PR747's possible projective line to at most a single projective point. The larger-kernel locus is restricted further to the two structural types above, with an explicit still-unevaluated canonical scalar compatibility.

Nonzero K_actual implies nonzero actual fourth-square scalar rho4 by the pinned source result. Zero K_actual is only necessary for rho4=0. Neither assertion identifies the separate beta4 boundary modulo im(beta2), and no algebraicity conclusion follows. No selected actual evaluation, model substitution, executable algebra, large computation, Gauss analysis, or identity-W work is used.
