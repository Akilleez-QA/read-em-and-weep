# Affine normal-extension dependence of the actual secondary tensor

## Results and scope

Fix the actual cone bundle E=F_Q0 and its involution and G action. Equivariant extensions to the FIXED first ambient thickening 2Q0, with their reduction identification specified, form a torsor under

    T=H1(Q0,B_Q0(-2))^G=C.

This is a torsor, not a canonically based vector space containing the actual extension. The secondary operation of POSITIVE-THIRD-SECONDARY-MULTIPLICATION-TENSOR.md extends intrinsically to every member of this torsor. Its dependence is affine, with a canonical linear variation described below.

For the fixed actual Atiyah-derived quadratic family t(a) and fixed second-symbol quotient, the same construction yields an affine map from this torsor to the two-dimensional space of cubic gates. Its linear variation has an explicit Cech formula. Even if this variation were injective, that alone would show only that AT MOST ONE extension has zero cubic gate. It would not show that the actual extension is different from that point. No distinguished zero extension, or extension of every first-normal deformation to an ambient bundle, is supplied by the one-dimensional tangent-space computation.

We prove the affine dependence, the exact variation formula and all its choice-independence claims. We do not select the rank of the resulting linear map.

## 1. Cohomology inputs needed for an intrinsic construction

Write C=H1(B_Q0(2))_+ and P=H1(B_Q0(4))_+=P4. The positive lower restriction is surjective, since H2(B)_+=0: the actual H2(B)=W is inversion-odd. Thus C is the actual lower cokernel coker(q0:M_0,+->M_2,+), of dimension30.

We also have

    H2(B_Q0)_+=0,             H1(B_Q0)^G=C [xi|Q0].             (1)

For the first assertion use the restriction sequence B(-2)->B->B_Q0. Its adjacent groups are H2(B)_+=0 and H3(B(-2))=0. The latter follows from the negative symmetric-square monad, whose entire cohomology at twist -2 is in degrees1 and2.

For the second assertion, the invariant groups H1(B(-2))^G and H2(B(-2))^G are zero by NEGATIVE-MONAD-INVARIANT-SCALAR-IS-NONZERO.md. The restriction sequence identifies H1(B_Q0)^G with H1(B)^G=Cxi. In particular its generator is nonzero.

Finally

    a [xi|Q0]=0 in H1(B_Q0(2)) for every a in A,                (2)

because a xi=q0 zeta_a. We use the proved strong multiplication vanishing

    h H1(B_Q0(2))_+=0 in P for every h in D5,                   (3)

and the exact cone section theorem H0(B_Q0(4))_+=N(A+D5).

## 2. Secondary multiplication from a first-normal extension alone

Let F_tilde be any equivariant extension of E to 2Q0, and let B_tilde be its trace-free adjoint. The first-normal sequence, twisted by two, is

    0 -> B_Q0 -> B_tilde(2) -> B_Q0(2) -> 0.

By (1), every x in C admits a cohomology lift x_tilde in H1(B_tilde(2))_+. By (3), h x_tilde restricts to zero in H1(B_Q0(4)). Hence the twist-four normal sequence supplies y in H1(B_Q0(2))_+ such that

    q0 y=h x_tilde in H1(B_tilde(4)).

Define Psi_tilde(a,h,x)=a y in P.

Changing x_tilde changes y by h z, with z in H1(B_Q0)_+, modulo the next ambiguity. Its contribution a h z is zero by (3), applied to a z in C.

Changing y without changing q0 y changes it by the normal boundary of a section s=N r, r in A+D5. This boundary is r times the boundary of N, by O-linearity. The latter lies in H1(B_Q0)^G, hence is a multiple of xi|Q0 by (1). Its product with a is zero by (2). Thus the second ambiguity also disappears.

This defines a canonical tensor for every extension in the torsor. For the actual extension F|2Q0, choose x_tilde by restricting an ambient representative x in M_2,+. If q0 v=h x in the actual ambient module, restriction gives y=v|Q0. The tensor therefore agrees exactly with the previously constructed actual Psi. No formal extension beyond 2Q0 is needed for this comparison.

## 3. Exact affine variation formula

Let eta represent an element of T. Changing an extension by eta changes its adjoint transitions to first normal order by the action ad(eta); the base thickening and its local lifts are held fixed. All products of two normal parameters are zero.

Represent x by a Cech1 cocycle c with values in B_Q0(2). Choose a Cech0 cochain b in B_Q0(4) such that

    d b=h c.

It exists by (3). When the extension changes by eta, the change in the normal component of a lift of c is a Cech1 cochain tau in B_Q0 satisfying

    d tau=-eta dot c,                                            (4)

where dot denotes the graded adjoint action in a multiplicative acyclic resolution (or a compatible Cech model). Fix the differential convention

    d[alpha,beta]=[d alpha,beta]+(-1)^deg(alpha)[alpha,d beta].

The action is the graded commutator. In particular eta and c both have Cech degree1, so [eta,c]=eta cup c+c cup eta; whereas b has degree0, so [eta,b]=eta cup b-b cup eta. These signs are cohomological signs, independent of the ordinary polynomial twists. Existence of tau follows from H2(B_Q0)_+=0. The change in the divided class y is represented by

    h tau-eta dot b.

This is a cocycle: d(eta dot b)=-eta dot db=-eta dot(hc), which cancels h d tau. Consequently

    Delta_eta Psi(a,h,x)=[a(h tau-eta dot b)] in P.                (5)

This is linear in eta, a, h and x, after taking the indicated cohomology class. The fixed base-thickening terms cancel between the two extensions, so none are omitted from the DIFFERENCE formula. Formula (5) is not a formula for the absolute actual value unless a reference extension and its secondary tensor have also been specified.

If tau changes by a cocycle z, the output changes by a h z=0 by (3). If b changes by a section s=N r, the output changes by -a[eta,N]r. The bracket class [eta,N] lies in H1(B_Q0)^G and hence is proportional to xi|Q0; (2) kills it. The remaining representative changes can be checked explicitly in this same graded convention.

- If c is replaced by c+d kappa, where kappa is a degree0 cochain of twist2, choose b'=b+h kappa and tau'=tau+[eta,kappa]. Since d eta=0,

      d[eta,kappa]=-[eta,d kappa],

  so the new lift equation holds. Moreover

      h tau'-[eta,b']=h tau-[eta,b]

  exactly, because h is central of cohomological degree0.

- If eta is replaced by eta+d lambda, where lambda is a degree0 cochain of twist-2, choose tau'=tau-[lambda,c]. Since dc=0, d[lambda,c]=[d lambda,c], so this again solves the changed lift equation. The divided cocycle changes by

      -h[lambda,c]-[d lambda,b]
      =-[lambda,db]-[d lambda,b]
      =-d[lambda,b].

  Multiplication by a preserves this coboundary. Thus the output depends only on the class of eta. Combining these two checks handles simultaneous representative changes. Any additional choices of b or tau were already checked above.

The intrinsic construction in Section2 independently identifies this choice-free formula with the difference of the secondary tensors.

## 4. The precise cubic variation and its kernel criterion

Keep the ACTUAL cone quadratic class t(a)=[a zeta_a|Q0] fixed. Also keep the actual second-symbol image in P fixed. These are used merely to evaluate the family of secondary tensors; we do not claim that arbitrary first-normal extensions have ambient realizations and actual Bockstein sequences.

Define the affine cubic gate of an extension by

    G_tilde(a,h)=Psi_tilde(a,h,t(a)) modulo im beta2_a.

Its canonical linear variation is

    L:T -> Hom_G(D5 O_P(A)(-3), I_Z(6)),                          (6)

whose target has dimension two. For eta, choose c(a) representing t(a), b(a,h) with db=h c(a), and tau(a) with d tau=-eta dot c(a). Then

    L(eta)(a,h)=[a(h tau(a)-eta dot b(a,h))] modulo im beta2_a.    (7)

Thus the EXACT kernel condition is that the class in (7) belongs to im beta2_a for every a and h. This is a cohomological condition involving the actual adjoint action and nullhomotopies, not a test determined by representation multiplicity. Since T is one-dimensional, its kernel is either zero or all of T, but neither possibility is selected here.

If L is injective, an affine map with this linear part has at most one zero. There can also be no zero, if its affine image misses the origin in the two-dimensional target. Knowing L alone does not decide which case holds or where the actual extension lies. If L is zero, the cubic gate is independent of this first-normal variation, and its still-unknown constant value must be computed by another method.

## 5. Why ambient monad injectivity does not supply an arbitrary parameter

The same negative-monad theorem gives the connecting isomorphism

    T -> H2(B(-4))^G=C

from the restriction sequence B(-4)->B(-2)->B_Q0(-2), because the two adjacent invariant cohomology groups of B(-2) vanish. In particular nonzero normal variations do not lift to infinitesimal ambient deformations fixing the cone restriction: such lifts would have to come from H1(B(-2))^G=0. This distinguishes the first-normal extension torsor from a free family of globally realizable monads.

The monad subbundle condition selects nonzero lower coefficients and the actual ambient object. It does not, by itself, identify that object's affine cubic value with L applied to a nonzero tangent vector. Making that identification requires an additional actual comparison, rather than a choice of origin in the torsor.

## Evidence and remaining geometric input

All constructions concern the actual cone bundle and adjoint transition action. Inputs are the proved negative monad theorem, actual ambient H2(B)=W, the cyclic identity, cone rank33 closure, and the strong square-filtration multiplication vanishing. The companion verifier checks universal graded-Cech cancellation and twists; it does not evaluate actual coefficients or replace the geometric arguments.

The remaining normal-extension task is now precise: evaluate (7) on its invariant line, or compute an absolute reference value together with the actual extension comparison. The argument supplies neither a nonzero channel nor a cone-data-only formula for the actual third value.
