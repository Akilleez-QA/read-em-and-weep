# Global first smoothing and the weighted third obstruction

## The comparison theorem

Fix a nondegenerate binary quadratic q_- with reduced roots lambda_1,lambda_2. Put

    D=(q_-=0)=H_1 union H_2,
    D_s=(q_-+s q_+=0),
    S_q=H0(Z(q_-),Sym^2 Y(1)),   dim S_q=6.

The space S_q consists of the actual global hyperplane squares multiplied by the corresponding normal linear forms, as in MIXED-ROOT-SQUARE-SMOOTHING-OBSTRUCTION.md. It is canonically a subspace of H0(B_D(4))_-.

Let d_gl be the first global smoothing obstruction for the family D_s. Let Theta be the weighted third obstruction on S_q from that note. There is a canonical commutative diagram

    S_q  --d_gl--> H1(B_D(4))_-
     |                  |
     | identity         | restriction rho
     v                  v
    S_q  --Theta--> coker(Delta_q).                   (1)

Thus Theta is precisely the finite-normal restriction of the global first smoothing obstruction. It is NOT asserted to equal the entire global obstruction, and rho is not asserted injective or surjective.

If b=rank(beta_lambda1)+rank(beta_lambda2), write

    h_i=h0(B_Hi(3))_+.

Then the middle space in (1) has the actual dimension

    h_1+h_2+4 <= 22-b.                                (2)

Consequently the known thirty-minus-b target of Theta contains a canonical smaller subspace im rho through which Theta factors. Its dimension is at most twenty-two-minus-b.

In particular, if beta has rank six at both roots, the forced squares exhaust the entire odd section space on D, and the full first global smoothing gate is

    d_gl:6 -> 10.                                    (3)

Theta is then its natural image in the eighteen-dimensional finite target. No rank of (3), no rank of rho, and no odd-quadric vanishing is proved here.

## 1. Which scaling parameter is being used

For the fixed smooth Q=(q_++q_-=0), the map

    h_epsilon(x,u,v)=(x,epsilon u,epsilon v)

has image, for epsilon nonzero,

    q_-+epsilon^2 q_+=0.

Thus for the global family D_s as normalized above,

    s=epsilon^2=t.                                   (4)

If instead a family is written q_++a q_-=0, its coefficient is a=epsilon^(-2). These two normalizations must not be interchanged. The present comparison uses (4) and does not extend the inverse-parameter family through zero.

An odd section vanishing on the fixed plane has at least one normal factor. Under h_epsilon its normal-degree-d component gains epsilon^d. Dividing the pullback section by epsilon gives a regular formal section. Hence a term of global smoothing order a and odd normal degree d contributes at weighted order

    t^(a+(d-1)/2).                                   (5)

This grading is the source of the different names "first global" and "third weighted."

## 2. The canonical finite target on the reducible quadric

Let J be the ideal of R in D, and let D_7 be the seventh ideal-power neighborhood defined by J^7. Projection onto R is defined on D_7 and finite. Define its odd eigensheaf, pushed to R, by

    N_5=(B_D(4)|D_7)_-.

Equivalently, it is the odd part of (J/J^7)B_D(4). The quotient on R has only positive character, so the latter identification loses no odd component. Its odd normal degrees are one, three, and five.

The ideal J on the normal crossing union splits branchwise: in local coordinates the algebra is O_R[u,v]/(uv), and J=(u) directsum (v). Multiplication by the normal linear form on each branch therefore gives

    N_5 = directsum_i E_lambda_i^2 tensor lambda_i*,  (6)

where E_lambda^2 is the actual even fifth-normal-neighborhood object for B_Hlambda(3) used to define beta. Formally, dividing a branch's odd degrees one,three,five by its normal coordinate leaves even degrees zero,two,four. Using a sixth rather than fifth truncation after division changes only an odd layer and does not change the invariant object.

The proved exact root sequences give

    H1(N_5)=coker[H0(Z,K(1))
                    --Delta_q-->H1(B_R(-1)) tensor H0(O_Z(5))].  (7)

This is an identification with the actual cokernel sheaf cohomology, not merely equality of dimensions. Restricting global cohomology from D to D_7 and taking odd parts defines the canonical rho in (1).

There is a further intrinsic target description. The normal-restriction exact sequence gives

    H1(B_D(4))_- --rho--> H1(N_5)
       --partial--> H2(J^7 B_D(4))_-.

Therefore

    im rho=ker partial.                              (8)

The extra compatibility in (8) is genuine. It is not supplied by rootwise beta vanishing alone. The same exact sequence also gives the precise vanishing condition

    Theta(a)=0 if and only if d_gl(a) lies in the image of
    H1(J^7 B_D(4))_- -> H1(B_D(4))_-.                 (8a)

Thus a zero weighted third class permits a global first obstruction supported in the higher normal ideal; it does not prove that the global first obstruction is zero. This is a cohomological assertion and does not assume flatness of a naively truncated smoothing family.

## 3. The global first obstruction in local lifts

Choose local projective frames near R, and let a be an actual global odd B_D(4) section from S_q. Choose local ambient lifts a_i. With a consistent gluing convention, write

    T_ij a_j-a_i=q_- c_ij,                            (9)

where T_ij are the actual transitions of B and c_ij are odd local B(2) sections. The first-order relation in D_s is q_-=-s q_+. Thus the first global smoothing class is represented by

    -q_+ c_ij modulo q_- .                           (10)

This also recovers the ambient cohomological definition: the connecting class of a is in ker(q_-:H1 B(2)_- -> H1 B(4)_-), and d_gl is multiplication by -q_+ into the cokernel, with the chosen gluing convention. Changing the overall convention changes both sides of (1) by the same sign.

Formula (9) uses the actual global hyperplane sections. It contains all their normal orders and all actual bundle transitions. In particular the quartic and sixth-normal transition terms are not assumed zero.

## 4. Pullback and comparison through weighted order three

Pull (9) back by h_epsilon and divide the lifted sections by epsilon. Write the odd normal expansion of c as c_1+c_3+c_5+..., where the subscript is its normal degree. On the fixed Q, q_-(u,v)=-q_+(x). The normalized gluing defect is consequently

    -t q_+ c_1 - t^2 q_+ c_3 - t^3 q_+ c_5
      modulo t^4,                                   (11)

after the corresponding homogeneous pullbacks. The leading normalized section is exactly the canonical element of S_q in E3^0. Its higher uncorrected coefficients are the actual normal expansions of the two global hyperplane square sections.

To compute rho(d_gl(a)), eliminate the degree-one and degree-three parts of (10) inside N_5. This is always possible at the level of cohomology: the degree-one H1 is H1(B_R(3))=0, while the actual first root boundary is onto, so the object through odd degree three has H1 zero. The remaining degree-five class is taken modulo the actual secondary image. By (7), this is exactly the cokernel Delta_q.

Apply the same local corrections to (11). A first global correction of normal degree d pulls back to weighted order 1+(d-1)/2. Thus its degree-one,three,five pieces give precisely the corrections at weighted orders one,two,three used to eliminate these components. Since the transitions T_ij are the actual transitions in both calculations, their quadratic, quartic, and sixth-normal interactions agree.

There is one possible additional effect which must be retained until taking the quotient. A local identity used on D holds only modulo q_-. Lifting it to the ambient neighborhood produces a q_- multiple. Substituting q_-=-s q_+ promotes that remainder by one GLOBAL smoothing order and lowers its normal degree by two. By (5), through weighted order three these extra terms have only the following possibilities:

    global order 2, normal degree 3;
    global order 3, normal degree 1.

Their weighted classes are respectively in the degree-three first image and in degree-one H1=0. Hence they disappear in exactly the quotient defining the weighted third differential, not before that quotient.

The only surviving contribution at weighted order three is therefore the global first-order, normal-degree-five class. This proves the commutativity of (1). Changes of local lifts change (10) by a coboundary; changes of the preceding weighted corrections add the first and secondary images. These are precisely the matching indeterminacies on the two sides.

This argument is a natural filtered comparison. It neither constructs a splitting of a higher formal neighborhood nor assumes that a global first-order lift exists.

## 5. The actual global target and the six-to-ten conditional gate

Mayer--Vietoris on D gives, in odd character,

    H1(B_D(4))_-
       =directsum_i H1(B_Hi(4))_-
       =directsum_i H1(B_Hi(3))_+ tensor lambda_i*.    (12)

The omitted plane terms vanish in odd character because B_R(4) has trivial fiber character. The normal multiplication in the second equality retains the line lambda_i*.

For each H_i its odd defining equation gives the actual ambient sequence

    0 -> H0(B_Hi(3))_+
      -> H1(B(2))_- tensor <ell_i>
      -> H1(B(3))_+
      -> H1(B_Hi(3))_+ -> 0.

The middle dimensions are 44 and 46. The final zero uses the proved H2(B(2))=0, and both ambient H0 groups vanish. Therefore

    h1(B_Hi(3))_+=h_i+2,

which proves the equality in (2). The hyperplane finite normal test gives

    3<=h_i<=dim ker beta_lambda_i=9-rank beta_lambda_i.

Adding proves the bound in (2). In particular im rho has codimension at least eight in coker Delta_q, regardless of any additional kernel of rho.

If both beta maps have rank six, the two bounds force h_1=h_2=3. Mayer--Vietoris then shows H0(B_D(4))_-=S_q, so (3) is the ENTIRE first global obstruction on odd sections of D, not just a subspace restriction. Injectivity of that actual six-to-ten map would imply odd-section vanishing for a general nearby smooth member by the standard first-obstruction/semicontinuity argument. No such injectivity is established here. Nor does injectivity of rho follow from the dimension count.

## 6. Extension to the entire globalizable root space

The comparison is not specific to squares. Set

    G_q=H0(B_D(4))_-
       =directsum_i H0(B_Hi(3))_+ tensor lambda_i*,
    k=dim G_q=h_1+h_2.

Each global hyperplane section has a unique leading plane restriction. Indeed the successive even normal layers after degree zero are B_R(1), B_R(-1), B_R(-3), and lower twists, all with H0 zero. Vanishing of the leading restriction therefore forces formal vanishing and hence global vanishing. The finite hyperplane test identifies its image exactly with ker gamma_lambda inside ker beta_lambda.

Consequently G_q is canonically the space of sections on the reduced two-point scheme Z of the rootwise kernel of gamma, twisted by O_Z(1). Here the kernels are taken after restriction to Z; no claim about base change for a rank-jumping kernel sheaf on all of P(W*) is needed. In particular

    G_q subset ker(Delta_q)=E3^0.

Every element has zero degree-seven gamma component, because it is globally defined on each hyperplane. The weighted third differential on G_q therefore has the same degree-five target coker Delta_q, and the proof of Sections 3--4 applies unchanged. Thus the whole globalizable subspace has a commutative diagram

    G_q --d_gl--> H1(B_D(4))_-
     |                  |
     | identity         | rho
     v                  v
    G_q --d3|G_q--> coker(Delta_q),

with actual dimensions k -> k+4 -> 30-b and k<=18-b. The restricted weighted third map is again linear in q_+. The square six-space is a canonical subspace of G_q, not a claimed description of all of it.

This gives the full global first-order gate and its finite weighted image even when beta has extra kernel or the hyperplanes possess adjoint sections beyond squares. No maximal-rank conclusion follows from these dimensions.

## Scope and sources

The established weighted operator is published at ef742e4fc591f38030b56cecbc0761e540f8f7eb. The actual hyperplane square bundle and exact h0(F_H(2))=2 are in HYPERPLANE-SQUARE-SURVIVORS.md. ODD-SECOND-SCALING-OBSTRUCTION.md supplies the actual E_lambda^2 and beta sequence, including the nonlinear fourth-order comparison. The ambient H2(B(2)) vanishing is PR167, Section 2, at immutable commit 063da90fc4543304e87e701cdefcc08225412f17, research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md.

The result identifies a natural restriction of the global first smoothing class, adds the compatibility kernel (8), and sharpens the available target bound. It leaves the actual ranks of d_gl, rho, and Theta unresolved.
