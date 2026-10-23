# The remaining small-branch fourth scalar detects an actual Q-image incidence

## Theorem and scope

Assume the conditional actual source2 pure-V compatible-radical hypotheses
and the nine-dimensional generated endpoint. Retain the actual endpoint
submodule NC and put U_Q=Q(NC2). PR1069 gives the unique fourth-lift
coefficient relation R=gamma R1, with gamma possibly zero. Then

    gamma=0  if and only if  NC4⊂U_Q,
    gamma≠0 if and only if  U_Q∩NC4=I4.                 (1)

Equivalently, write D_C for the unique actual D summand in NC4=I4⊕D_C.
For any G-equivariant right inverse G_Q:im Q→N2, one has

    G_Q(D_C)⊂NR2,
    gamma=0 iff π2 G_Q(D_C)=0 iff G_Q(D_C)⊂NC2.         (2)

Here π:NR→N8 is the actual residual quotient from any genuine separated
negative-pencil presentation. The projected map in (2) is independent of
the equivariant right inverse. Its nonzero case is an isomorphism from
D_C onto the unique D8,2⊂N8,2; no repeated D subspace is silently identified.

The new mathematical input is the exact universal descendant calculation

    C2(a epsilon·df)=−14 rho_D(a)f.                    (3)

It identifies a nonzero transfer from the unique residual degree-two D to
the residual degree-four D. This converts the previously unselected
transfer scalar into the actual incidence (1), rather than inferring an
incidence from matching characters. Neither side of (1) is selected, and
Q is not assumed to preserve NC or NR. No source or endpoint is excluded.

## 1. Exact inputs and normalization

INPUTS.json authenticates four complete public proofs:

- PR795 at 3f811311d76914a555c7e7d0c5b887b41805aa6c: genuine negative
  separation N=N0⊕NR, residual exact sequence NC→NR→N8, and the fact
  that each fixed-pencil radical kills NR.
- PR1064 at bfc239e1c8624a0346394e1454b0bea3c976d40d: in the nine branch,
  h(NC4)=0 and h|NR4 descends to N8,4 with kernel V8+P8 and a nonzero
  isomorphism on its unique D8,4. It supplies the actual fixed-variable
  polarization quotient and the marked quartic normalization.
- PR1065 at fd75633464cd587856287cc7866520fb4105ef5b: the actual image
  U_Q=Q(NC2) has kernel I2, character V+P+D and dimension12; in the nine
  branch I4⊂U_Q. Its intersections are proved with actual maps, without
  Q-preservation of NC or NR.
- PR1069 at 41bc20cade3198306c492c0c46399d71eb0d51c4: the canonical
  transfer Π_a=hT_aG_Q, independence for equivariant G_Q, and exact
  R=gamma R1 in the nine branch. Its proof gives gamma=λν, where
  Π|D_C=λrho_D and the actual quadratic descendants modulo I4 are
  νL_a*, with ν≠0. Thus gamma=0 iff Π|D_C is the zero family.

All inherited actual-source hypotheses remain. In particular the original
Q kernel is A+I2 and the pure-V radical has im j2=I2=D. The negative
first block is N0,2=P+D. We distinguish the degree-two I2, degree-four
D_C, and the two residual quotient D constituents D8,2 and D8,4.
The same letter D only records their isomorphism type.

## 2. The Q preimage of D_C lies in the genuine residual submodule

Since NC4⊂ker h⊂im Q in the nine branch, G_Q is defined on D_C. Put

    k=G_Q|D_C : D_C→N2,        Qk=Id_D_C.              (4)

The right side means the actual inclusion D_C⊂N4. The homotopy identity
hQ=j2 and h(D_C)=0 give j2k=0.

Write e2 for the genuine N0 projector. Since k is equivariant, e2k takes
values in the unique D summand of N0,2=P+D. The radical j2 kills NR2;
on N0,2 its image is I2 of dimension five. Its P restriction is zero by
equivariance, so its restriction to that unique D is an isomorphism onto
I2. Thus j2k=j2e2k=0 implies e2k=0. This proves k(D_C)⊂NR2 using an
actual projector and the actual pure-V image, not Q-preservation.

If G_Q' is a different equivariant right inverse, G_Q'−G_Q maps im Q
into ker Q=A+I2. As in PR1069, im Q has no A constituent, so this difference
has image in I2⊂NC2. Consequently

    τ=π2 k : D_C→N8,2                                (5)

is independent of the right inverse. The unique D in
N8,2=A⊗Sym4 W=Sym6 W⊕Sym4 W⊕Sym2 W is D8,2. Therefore τ is either
zero or an isomorphism onto D8,2. This conclusion does not identify k
with a freely chosen embedding in NR2.

## 3. Exact nonzero universal D-to-D descendant

Use first-factor variables X,Y and second-factor variables x,y. The unique
D8,2 inclusion is represented, up to nonzero scalar, by

    e_D(f)=(Xy−Yx)(X f_x+Y f_y),       f∈Sym4 W.        (6)

The factor Xy−Yx is invariant for simultaneous SL2 action, and the
polarized derivative is equivariant. Formula (6) is nonzero and therefore
injective on the irreducible Sym4 W. Its three coefficients in X²,XY,Y²
are

    y f_x,    y f_y−x f_x,    −x f_y.                  (7)

The endpoint N8,4 is (A⊗Sym6 W)/Delta(Sym8 W). The fixed transvectant
quotient C=(C1,C2) identifies it with Sym6 W⊕Sym4 W, where C2 is the
unnormalized second transvectant. Explicitly, on a tensor g⊗u it is

    (g,u)_2=g_xx u_yy−2g_xy u_xy+g_yy u_xx.

The D8,4 projection is exactly this second component: Sym6 W=V+P has
no D. Multiplication by a negative quadratic a keeps the first factor
fixed. Applying C2 to a times (7), and differentiating, gives

    C2(a e_D(f))
      =Σ_(g,u) (g,a u)_2
      =−14(a_x f_y−a_y f_x)=−14rho_D(a)f,             (8)

where the three pairs (g,u) are those in (7). The verifier checks (8)
identically with all three coefficients of a and all five coefficients
of f algebraically independent. This is not a selected quadratic or
quartic value. It also verifies the inclusion and quotient normalization.
The number−14 belongs only to these universal conventions.

Equation (8) is a statement about the D projection of the descendant,
not the whole endpoint map: its V+P component is not asserted zero.
In particular the family D8,2→D8,4 is nonzero and is proportional to
rho_D in the actual reconstruction, with an unevaluated nonzero scalar.

## 4. Comparison with the canonical transfer

The actual residual quotient intertwines every negative quadratic:
π4 T_a=T_a^8 π2 on NR2. In the nine branch, PR1064 gives a descended
map

    hbar:N8,4→I2,     h|NR4=hbar π4,

which kills V8+P8 and is an isomorphism on D8,4. Since k(D_C)⊂NR2,
its descendants remain in NR4. Therefore the restriction of the canonical
transfer is literally

    Π_a|D_C=hT_a k=hbar T_a^8 τ.                       (9)

If τ=0, this family vanishes. If τ≠0, it identifies D_C with D8,2;
Equation (8) and the isomorphism hbar|D8,4 show that (9) is a NONZERO
family. Thus

    Π|D_C=0 iff τ=0.

PR1069's gamma=λν with ν≠0 then proves the first equivalence in (2).
Exactness of NC→NR→N8 gives τ=0 iff k(D_C)⊂NC2, proving the rest.
There is no inference that the whole Q map preserves either submodule.

## 5. Conversion into actual Q-image incidence

If k(D_C)⊂NC2, (4) gives D_C⊂U_Q. Conversely suppose D_C⊂U_Q=Q(NC2).
The equivariant surjection Q:NC2→U_Q admits an equivariant lift
k_C:D_C→NC2 of that inclusion. Its difference from k is an equivariant
map D_C→ker Q=A+I2. Since Hom_G(D,A)=0, this difference takes values
in I2⊂NC2. Hence k(D_C)⊂NC2 as well.

This explicitly handles the two D copies in NC2. No particular complement
to I2 is required, and any two equivariant lifts of D_C differ only in
I2. Thus repeated source D multiplicity introduces no ambiguity into
membership in NC2 or into τ.

We have proved gamma=0 iff D_C⊂U_Q. PR1065 gives I4⊂U_Q in this branch,
and NC4=I4⊕D_C has multiplicity-free P+D character. Therefore

    D_C⊂U_Q iff NC4⊂U_Q;
    D_C not contained in U_Q iff U_Q∩NC4=I4.

The intersection is equivariant, so there is no hidden partial D
intersection or graph between its nonisomorphic P and D constituents.
This establishes (1) using actual images and intersections.

## Reproduction and limits

Run python verify.py and python -O verify.py. The bounded verifier
checks four input hashes, the universal biform inclusion, the exact
transvectant quotient and identity (8), and the representation/dimension
facts used by the written proof. It does not construct Q, choose a
right inverse for actual matrices, evaluate gamma, or perform an
instance-rank calculation.

The incidence alternatives remain unselected. This result does not
assert Q(NC2)⊂NR4, and it does not extend to endpoint sixteen. It does
not use the nonzero P graph to infer nonzero gamma: the graph is killed
by Π. What is newly identified is the precise Q-preimage displacement
in the unique residual D channel that detects gamma in endpoint nine.
