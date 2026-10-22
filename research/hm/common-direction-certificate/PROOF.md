# Recovering a common exceptional direction from the kernel pencil

## Immutable inputs and scope

Use [PR747 at 0a0ee30a5142477e54245b7c6f22d561abb4f5f1](https://github.com/Akilleez-QA/read-em-and-weep/blob/0a0ee30a5142477e54245b7c6f22d561abb4f5f1/research/hm/source-family-fourth-square-exclusion/PROOF.md), [PR759 at 8688c748e3a655a6db793c4b96504aaafb55cbc9](https://github.com/Akilleez-QA/read-em-and-weep/blob/8688c748e3a655a6db793c4b96504aaafb55cbc9/research/hm/exceptional-source-locus/PROOF.md), and the common-direction dichotomy of [PR760 at d798dceb77b94b5dbb9457fb303984e595ce1874](https://github.com/Akilleez-QA/read-em-and-weep/blob/d798dceb77b94b5dbb9457fb303984e595ce1874/research/hm/rational-pole-strata/PROOF.md).

Work over C. Let A=H0(P1,O(2)), with nondegenerate symmetric apolar form B, and identify H with the five-dimensional space of all trace-free B-self-adjoint endomorphisms by h -> S_h. Let k=C(P1), let V be the fixed k-vector space, and fix d != 0 in V and gamma != 0 in C. The C-linear map K:H -> V remains unevaluated. In the common rational trivialization, put

    Phi_h(a)=a K_h-gamma S_h(a)d,    E_h=ker_C Phi_h.

The common-direction branch is the existence of a nonzero a0 in A with

    K_h=gamma (S_h(a0)/a0)d for every h.                 (1)

PR760 proves that if (1) fails then the exceptional-source locus { [h]: E_h != 0 } is proper closed. This note supplies an exact finite certificate for (1), reconstructing its only candidate from ker K, instead of searching over P(A). All ranks below are over C unless otherwise specified. They are symbolic conditions, not ranks computed for the actual HM map.

## 1. Evaluation is surjective, also at isotropic vectors

For every nonzero a in A the evaluation map

    ev_a:H -> A,    h -> S_h(a)

is surjective. Its kernel P_a has dimension two.

If B(a,a) != 0, rescale a and extend it to an orthonormal basis. An arbitrary first column can be prescribed in a symmetric matrix; its two other diagonal entries can be chosen to make the trace zero. This proves surjectivity.

If B(a,a)=0, choose a Witt basis U,T,W with U proportional to a, B(U,W)=1, B(T,T)=-1/2, and all other pairings zero. A general self-adjoint trace-free operator is

    S=[[x,b,c],[e,-2x,-2b],[g,-e/2,x]].                 (2)

Its first column (x,e,g) is arbitrary. Thus evaluation at U, and hence at a, is again surjective. This is a change of abstract basis, not a chosen-source evaluation.

Under (1), multiplication by gamma d/a0 is injective on A. Consequently

    rank_C K=3,    ker K=P_a0,
    r(H)=a0^(-1)A=H0(P1,O(div(a0))),                   (3)

where K_h=gamma r_h d. In particular the whole three-dimensional complete rational function system, not merely a subspace with poles bounded by div(a0), occurs. Its maximal pole divisor is exactly div(a0): basepoint-freeness of A prevents universal cancellation at any zero of a0.

## 2. Classification and reconstruction of the kernel pencils

Identify P_a with its image in End(A). Its common operator kernel is exactly Ca.

For B(a,a) != 0, use an orthonormal basis whose third vector is proportional to a. Then

    P_a={ [[x,y,0],[y,-x,0],[0,0,0]] : x,y in C }.
                                                               (4)

The common kernel is the third coordinate line. The generic member has rank two, and

    adj(S)=-(x^2+y^2) E33.

The rank-at-most-one subscheme in P(P_a) is the reduced degree-two divisor x^2+y^2=0. Its two members are rank-one square-zero; every other member has rank two.

For B(a,a)=0, in (2) the condition S(U)=0 gives x=e=g=0, so

    P_a={ [[0,b,c],[0,0,-2b],[0,0,0]] : b,c in C }.
                                                               (5)

The common kernel is CU. Every member is nilpotent. For b != 0 it has rank two and nilpotency index three; for b=0,c != 0 it has rank one and square zero. Here

    adj(S)=-2b^2 E13.

Thus its rank-at-most-one subscheme is the doubled point b^2=0. These are the two isometry types of the kernel pencils; in particular the repeated-root type of their rank-drop divisor detects isotropy of the recovered common direction.

Here and below the rank-drop scheme is defined by all 2 by 2 minors. The displayed adjugates show directly its reduced or doubled scheme structure.

There is a coordinate-independent finite recognition criterion. Let J be any two-dimensional subspace of H, choose a basis h1,h2, and set

    S(s,t)=s S_h1+t S_h2,
    adj(S(s,t))=s^2 A20+st A11+t^2 A02.

Then the following are equivalent:

(a) J=P_a for a nonzero a in A.
(b) det(S(s,t)) is identically zero, and the coefficient matrices A20,A11,A02 span a nonzero one-dimensional C-space.

When these conditions hold, the image of any nonzero matrix in that coefficient space is Ca, and is also the common kernel of J.

Proof. The normal forms (4)-(5) prove (a) implies (b), including the nonzero requirement. Conversely write adj(S(s,t))=q(s,t)R with q a nonzero scalar quadratic and R a nonzero constant matrix. The identity S adj(S)=det(S)I yields q(s,t)S(s,t)R=0. Since C[s,t] is a domain, S_h1 R=S_h2 R=0. At a generic (s,t), the adjugate is nonzero and the determinant zero, so S has rank two and R has rank one. Its image is therefore a line Ca annihilated by both operators. Hence J is contained in P_a. Both spaces have dimension two by section 1, so J=P_a. The normal forms show that their common kernel is precisely Ca. This also proves uniqueness and independence of the basis of J. QED.

The determinant identity alone does not provide a fixed image line for the adjugate. The certificate therefore explicitly requires the nonzero one-dimensional coefficient span, rather than treating all-singularity as a sufficient condition.

## 3. Necessary and sufficient normalized certificate

The common-direction identity (1) holds if and only if all the following conditions hold:

1. K(H) is contained in kd and rank_C K=3.
2. For J=ker K, its operator pencil satisfies criterion (b) in section 2.
3. Let Ca0 be the line recovered from its adjugate coefficient space, and define r:H -> k by K_h=gamma r_h d. For any three classes [h1],[h2],[h3] forming a basis of H/J, one has

       a0 r_hi=S_hi(a0),    i=1,2,3.                (6)

Conditions (6) are equalities of rational sections in the fixed rational frame. They do not silently assume that a0 r_hi is regular. Their vanishing implies regularity as well as the required normalization. Scaling a0 changes both sides by the same factor, and changing representatives by J changes neither side.

Proof of necessity follows from (1), section 1, and section 2. For sufficiency, section 2 gives J=P_a0. Both maps h -> a0 r_h and h -> S_h(a0) vanish on J. Equality on a basis of H/J therefore gives equality on all H, which is exactly (1). This also proves that only three quotient-channel identities remain after the kernel geometry has supplied the unique candidate direction. QED.

Equivalently, ev_a0 induces an isomorphism H/J -> A; the induced map [h] -> a0 r_h must equal this specific isomorphism, not an arbitrary injection with the same kernel. Kernel and image information alone cannot replace (6). Indeed formally replacing a common-branch r by c r, for c in C minus {0,1}, leaves its kernel and image unchanged. The reconstructed direction remains [a0], but (6) fails since ev_a0 is surjective. This describes the logical normalization defect without modifying the actual canonical K or gamma.

Everything in this certificate is finite-dimensional. K(H) is finite-dimensional over C despite V being a k-vector space. The determinant has four scalar coefficients; the adjugate has three matrix coefficients; (6) has three rational-section identities. No determination of their actual values is made here.

## 4. Exclusions and contribution to the open dependency

By PR760, failure of any step of the exact certificate excludes dense exceptional sources: a general source then has E_h=0. In particular rank_C K != 3, failure of K(H) subset kd, or a kernel pencil with no common operator kernel each gives a sufficient structural exclusion of the common-direction branch. If the pencil geometry passes but the three normalization identities fail, the same exclusion follows. An all-singular pencil by itself is not a passing result.

This advances the unresolved dependency from an existential identity over every direction and every source to one recoverable candidate line, a coefficientwise kernel-pencil test, and three explicit normalization identities. It also identifies the two possible kernel-pencil types, their rank-drop schemes, and the full rational-function image in the common branch. It does not choose the actual branch: no actual K, source coefficient, point, derivative, matrix, or rank has been evaluated, and no scan or executable algebra computation is used.

For the imported HM obstruction, nonzero a^2 Phi_h(a) implies nonzero actual fourth-square scalar rho4. Zero modular class is only a necessary vanishing gate. The independent fifth-neighborhood beta4 boundary modulo im(beta2) remains unresolved; neither higher-order integrability nor algebraicity is asserted. These claims are deductively authored. The independent review is recorded separately; they are not proof-assistant checked.
