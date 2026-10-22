# Exceptional-pencil sources have codimension at least three

## Inputs and precise scope

Work over C and retain the actual-source hypotheses of [PR747](https://github.com/Akilleez-QA/read-em-and-weep/blob/0a0ee30a5142477e54245b7c6f22d561abb4f5f1/research/hm/source-family-fourth-square-exclusion/PROOF.md) and [PR752](https://github.com/Akilleez-QA/read-em-and-weep/blob/e0d0cb31fbef5c7d6f1148e2278fbce115239dcf/research/hm/exceptional-direction-bounds/PROOF.md). Put

    A=Sym^2 W,  dim A=3,  H=D5,  dim H=5,
    k=C(P^1),  V=(k[X,Y]/(f3))_8,  0 != d in V.

Let B be the nondegenerate invariant symmetric form on A. The fixed canonical identification

    S:H -> Sym^2_0(A,B)

is C-linear and invertible, and the fixed scalar gamma is nonzero. PR747 proves that h -> K_h in V is C-linear and that

    K_actual(a,h)=a^2 Phi_h(a),
    Phi_h(a)=a K_h-gamma S_h(a)d.

All sections use the same rational trivialization. Write E_h=ker_C Phi_h. For nonzero h, PR747 proves dim E_h<=2; nonzero immutable class implies nonzero actual global fourth-square scalar. The converse is not asserted. PR752 proves the exact criterion

    dim E_h=2 iff S_h has a two-dimensional eigenspace E_lambda
                      and K_h=gamma lambda d.                 (1)

These inputs concern the actual canonical source operation. No independent freedom to change its scalar is introduced.

## The new result

The projective sources for which S_h has a two-dimensional ordinary eigenspace form a smooth degree-four surface Sigma in P(H)=P^4, isomorphic to P(A)=P^2. Under this isomorphism, the exact locus

    X={ [h] in P(H): dim E_h=2 }

is the common zero locus of a finite system of homogeneous quadrics on P^2. This system is not the zero system: its inverse-B contraction equals gamma d != 0. Consequently X is empty or has dimension at most one, so it has codimension at least three in P(H). Its preimage is contained in a possibly reducible or nonreduced plane conic.

In particular every positive source outside X allows at most one exceptional projective negative direction. This includes sources on the repeated-eigenspace surface where the canonical compatibility fails, not only simple-spectrum sources. No source point or exceptional direction is selected or evaluated.

## 1. Uniform parametrization of the two eigenspace types

For v in A put q(v)=B(v,v) and define

    Q(v)(x)=B(v,x)v-q(v)x/3.                              (2)

This is self-adjoint and trace-free. It is nonzero whenever v!=0: the rank-one endomorphism x -> B(v,x)v cannot equal a nonzero scalar identity, and if q(v)=0 it is itself nonzero. Thus

    j:P(A) -> P(H),  [v] |-> [ S^{-1}Q(v) ]               (3)

is defined everywhere by quadrics.

If q(v)!=0, v-perp is a nondegenerate two-dimensional eigenspace with eigenvalue -q(v)/3, and Cv has eigenvalue 2q(v)/3. If q(v)=0, Q(v) is nonzero rank one with square zero, and its two-dimensional kernel is v-perp. These are precisely the two cases of PR752.

Conversely suppose nonzero self-adjoint trace-free T has a two-dimensional eigenspace E_lambda. If E_lambda is nondegenerate, let Cv=E_lambda-perp. The eigenvalues on E_lambda and Cv are lambda and -2lambda, with lambda!=0. Then

    T=(-3lambda/q(v)) Q(v).

If E_lambda is degenerate, PR752 gives E_lambda=v-perp for an isotropic v and T=c B(v,-)v=c Q(v), c!=0. Therefore the image of j is exactly the locus Sigma claimed above. In either case the two-dimensional eigenspace is unique and equals v-perp; its polar line recovers [v].

## 2. The surface is embedded, not merely parametrized

Use B to identify self-adjoint endomorphisms with Sym^2 A. The rank-one endomorphism v tensor B(v,-) corresponds to v tensor v; the identity corresponds to a nondegenerate rank-three tensor. Equation (2) is therefore projection of the quadratic Veronese surface in P(Sym^2 A)=P^5 away from the identity point.

Every secant or tangent line to the Veronese consists of symmetric tensors supported on a subspace of A of dimension at most two. Such tensors have rank at most two. The rank-three identity point lies on none of these lines. Projection consequently separates points and tangent directions, hence embeds the Veronese surface. Equivalently, point separation follows because a difference of two rank-one tensors has rank at most two, whereas a nonzero scalar identity has rank three. Tangent separation follows because v tensor w+w tensor v has rank at most two; if it is proportional to v tensor v after projection, the identity coefficient must be zero and w must be proportional to v.

For completeness the standard projective embedding criterion used here is the length-two subscheme criterion: a basepoint-free linear subsystem of a very ample line bundle defines a closed immersion when it separates every pair of points and every tangent vector. In this case these are exactly the rank arguments above. This establishes j as a closed immersion with pullback O_Sigma(1)=O_P2(2). Thus Sigma is smooth, has dimension two and degree (2H)^2=4. Its codimension in P^4 is two.

Under the induced SL2(W)-module identification Sym^2_0(Sym^2 W,B) ~= Sym^4 W, the surface becomes the locus of squares of binary quadratics. Indeed multiplication Sym^2(Sym^2 W)->Sym^4 W kills the one-dimensional invariant summand, and sends v tensor v to v^2. The identification here is transported through the fixed S. It does not identify an unspecified physical positive-coordinate marking with the negative W marking, and it selects no positive source coefficients.

The isotropic conic q(v)=0 parametrizes the rank-one square-zero boundary of Sigma. In the same transported binary-quartic marking it consists of fourth powers: v=ell^2 gives v^2=ell^4. Its image has degree four because j pulls O(1) back to O(2) on a degree-two conic. Outside this boundary the repeated eigenspace is nondegenerate. These are descriptions of the eigenspace surface, not assertions that canonical compatibility holds there.

## 3. The exact compatibility equations are quadratic

For each v let h(v)=S^{-1}Q(v). Its repeated eigenvalue, including the isotropic case, is

    lambda(v)=-q(v)/3.

By (1), the exact condition for dim E_h(v)=2 is

    Psi(v):=K_{h(v)}+(gamma/3)q(v)d=0 in V.              (4)

Since h -> K_h is C-linear and h(v) is quadratic, Psi is a V-valued homogeneous quadratic polynomial on A. The six coefficient vectors of this polynomial span a finite-dimensional C-subspace V0 of V, even though V itself is defined over k. Choosing any C-basis of V0 turns (4) into finitely many ordinary homogeneous quadratic equations over C. Thus its projective zero locus Z in P(A) is closed, and X=j(Z) is exactly the two-dimensional immutable-kernel source locus.

Changing the basis of V0 changes the list of equations but not Z. The construction involves coefficient vectors of a universal polynomial only; it does not evaluate an actual positive or negative source.

## 4. The compatibility system cannot vanish identically

This step uses linearity of K and nonzero d, not an unevaluated rank assertion.

Let e_i be any abstract basis of A, let B_ij=B(e_i,e_j), and let B^{ij} be the inverse matrix. For a vector-valued quadratic polynomial P(v), let P_pol be its symmetric polarization, so P(v)=P_pol(v,v), and define its B-contraction by

    ctr_B(P)=sum_{i,j} B^{ij} P_pol(e_i,e_j).

This is basis-independent. Direct tensor contraction gives

    ctr_B(q)=3,
    ctr_B( v tensor B(v,-) )=Id,
    ctr_B(Q)=Id-(3/3)Id=0.                            (5)

For example the second identity follows by applying the contraction to x and using sum B^{ij} e_i B(e_j,x)=x; polarization does not introduce a factor because the two symmetric terms agree after contraction.

Because S^{-1} and K are C-linear, (5) implies

    ctr_B(Psi)=K_{S^{-1}(0)}+(gamma/3)3d=gamma d != 0. (6)

Therefore Psi is not the zero polynomial. At least one of its scalar component quadrics in V0 is nonzero. Its zero locus Z lies in the plane conic defined by that nonzero component, hence has dimension at most one (or is empty). Closed immersion j then yields

    dim X<=1,   codim_{P(H)} X>=3                     (7)

whenever X is nonempty. This conclusion does not require identifying a component quadric, evaluating its coefficients, or solving it. The dimension bound is universal and remains valid if the conic is reducible, doubled, or if Z is finite.

A useful equivalent interpretation is that the scalar trace component of (4) cannot be canceled universally by the trace-free source term: K composed with Q has zero inverse-B contraction, whereas q(v)d has nonzero contraction. This is the root cause of the properness, not a genericity assumption about K.

## 5. The isotropic-boundary dichotomy

The entire isotropic parameter conic q(v)=0 lies in Z if and only if the C-linear map K:H->V is identically zero. Indeed on this conic, (4) is precisely K_{h(v)}=0. Under the transported marking of section 2, these h(v) are fourth powers ell^4. They span Sym^4 W: a linear functional vanishing on all (x+t y)^4 has all five coefficients zero, by the polynomial identity in the formal indeterminate t. Thus their span is H, and vanishing there forces K=0. Conversely if K=0 then (4) becomes Psi(v)=(gamma/3)q(v)d, so Z is exactly the isotropic conic, with its reduced scheme structure.

If K is not identically zero, at least one scalar component of K_{h(v)} restricts nontrivially to the isotropic conic. Pulling back along [ell]->[ell^2] gives a nonzero homogeneous quartic on P(W). Therefore Z meets that conic in at most four geometric points, or in scheme length at most four. This is a dichotomy, not a determination of which alternative holds for the actual source. It does not evaluate K. It supplies a finite bound on the rank-one square-zero boundary in the nonzero-K alternative.

## 6. Consequences and boundaries

The older eigenspace classification restricts a possible two-dimensional exceptional kernel to a codimension-two surface. Equation (6) strengthens this to codimension at least three for the actual canonical immutable kernel, without determining K at any source. In particular the set of sources with dim E_h<=1 contains a Zariski-open dense subset of P(H), and all sources on Sigma outside X=j(Z) also satisfy this bound.

At a point of X the whole exceptional pencil is determined by [v]: it is P(v-perp). In the nonisotropic case it meets the pure-square conic in two distinct points; in the isotropic case it is tangent and has one square point of multiplicity two, as proved in PR752. This is conditional incidence geometry, not the identification of an actual exceptional source.

Nothing here asserts X is nonempty, computes its degree or irreducible components, or identifies its points. The bound dim X<=1 does not establish that X is a conic; it only embeds its preimage in one. Nor does zero immutable class suffice for zero fourth-square scalar. Nonzero immutable class still implies nonzero actual rho4 by PR747, but rho4 is distinct from the fifth-neighborhood beta4 boundary modulo im(beta2). No beta4 value, algebraicity conclusion, source2 realization, or Gauss-label exclusion is obtained.

The derivation is purely structural linear algebra and projective geometry. No selected actual HM/source coefficients, points, derivatives, matrices or ranks, model substitutions, scans, or executable computation are used. The claims are deductively authored, not proof-assistant checked.
