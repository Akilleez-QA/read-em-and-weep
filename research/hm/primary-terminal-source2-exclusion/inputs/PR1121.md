# The transported scalar channel is one quarter of an actual projector

Work over C with the actual normalized Horrocks--Mumford bundle F,
B=End_0(F), G=SL2(F5), coordinates T=V+W, and the notation of
PR1114 and PR1118. Let E=(H1(B(2))_+)_V and F4=(H1(B(4))_+)_V
be the full two-copy V isotypical spaces. Let Q:E->F4 be the actual
isomorphism defined by the canonical invariant positive quadratic q.
The scalar channel operator K_mult is PR1114's K on the two-dimensional
multiplicity space of E, not the full graded cohomology module.

Then

    tr K_mult=1/4, K_mult^2=K_mult/4.                   (1)

In particular Pi=4K_mult is a canonical rank-one projector on
multiplicity space. Define the induced operator K_E=Id_V tensor K_mult
on E using its canonical isotypical evaluation. The image of K_E is
the ACTUAL V constituent of the primary--adjoint submodule in
H1(B(2))_+; its kernel is the actual scalar first-channel kernel V_s.
Thus E has the canonical decomposition

    E=E_prim direct-sum V_s,                            (2)

with K_mult eigenvalues1/4 and0 on these two multiplicity lines.
The scalar second image B0=V H is exactly Q(E_prim), not an arbitrarily
chosen copy of V. Nonzero nilpotency and trace0 are excluded structurally.

Both shifted channel operators in PR1114 are consequently invertible.
The actual first positive arrow on V tensor E has image character
1+2V+2D and dimension17. The former possibilities12 and14 are excluded.

This is a normalized trace identity forced by the actual primary
tensor factor and invariant contraction. No actual coefficient,
parameter, point, derivative, jet, matrix, instance rank or scan is
evaluated. In particular it is not the failed scalar-reachability
argument that proposed trace1/3.

## 1. Exact dependencies and their distinct roles

INPUTS.json authenticates five complete originals at their immutable
commits, with Git blob, SHA256 and length:

* PR477, ff87076794e97238150485b12183c3cd0f4711e4,
  research/hm/adjoint-primary-extension/PROOF.md: the actual
  G-equivariant graded R=Sym(T) module injection

      L=U tensor Aprim(-3) -> Kgraded,
      U=H0(F(3)), Aprim_d=H1(F(d)),
      (Kgraded)_j=H1(B(j-1)).                         (3)

  It constructs the map from evaluation Eagon--Northcott and Serre
  duality, establishes R-linearity, and only then proves injectivity.
  It also gives the primary dimensions5,10,10,2 in degrees0..3.
* PR1050, ec18a0fd62c4a9495adf6aad9564d379afc42b62,
  research/hm/canonical-negative-string/PROOF.md: U=P and the current
  normalized equivariant monad, whose elementary primary characters
  are rechecked in Section2. The positive P has dimension4.
* PR1118, f794fb1295693e7d2d9067013e5bd019d2a284a9,
  research/hm/positive-middle-faithfulness/PROOF.md: the unique scalar
  H in H1(B(3))_+, B0=VH a nonzero embedded V, rank K_mult=1, and
  im K_E=Q^-1 B0. This is the actual second arrow.
* PR1114, fc79bc119a251c16d386467333f55cd46dc75367,
  research/hm/repeated-v-channel-pencil/PROOF.md: the exact metric
  convention q=sum e_i^2, the actual isomorphism Q, scalar composite
  C0=d s=Q K_mult, canonical V_s=V tensor ker s, and full effective
  channels

      C1=Q(3K_mult-Id)/4,
      C2=3Q(K_mult+Id)/20,
      S=(9K_mult-Id)/10.                             (4)

  It also supplies the conditional negative-projector interface,
  used only in Section6 below with all its original hypotheses.

* PR1120, 62587a0adde566cac718ee13c28ee13c239389e5,
  research/hm/scalar-cyclic-module/PROOF.md: the preceding independent
  slice identifies the actual scalar and its first positive image in
  the primary submodule and determines its full cyclic annihilator.
  Its locations and character calculations are rederived in Sections2--3
  for the trace audit, retaining their exact original source maps.

This continuation pins the published cyclic slice explicitly. It does
not use its full cyclic-annihilator result or global levelness to
deduce the trace; the new ingredient is the coevaluation trace identity.

## 2. The primary spaces and the two actual arrows

The normalized monad has terms Nmon O(-1), W' tensor Omega2(2),
Nmon O, with Nmon=A+W', A=Sym2 W. Since O(-1) and Omega2(2)
are acyclic, its two short exact image sequences give

    Aprim_0=A+W'.                                   (5)

In twists1 and2 the monad terms have no higher cohomology; for
Omega2(3),Omega2(4), this follows from the exterior Euler complex and
the exact global-section Koszul complex in positive degree. Hence
Hq(F(t))=0 for q>=2 and t=1,2. The K-class retained in PR1050 gives

    chi F(1)=-(P+W+S4), chi F(2)=-(1+A+T6),
    S4=Sym3 W, T6=Sym5 W.

The primary h1 dimensions10,10 in PR477 then give h0=0, so

    Aprim_1=P+W+S4, Aprim_2=1+A+T6.                 (6)

These fixed representation identities are checked on all nine abstract
classes, not by evaluating either monad arrow. The linearizations are
the actual current ones: P,A,V are positive and W,W',S4,T6 negative.

Put X=(Aprim_0)_+=A, Z=(Aprim_1)_+=P, and
Y=(Aprim_2)_A=A. They are distinct ACTUAL cohomology spaces. Actual
positive multiplication restricts to maps

    a:V tensor X -> Z, b:V tensor Z -> Y.            (7)

For the first restriction parity leaves only Z. For the second, the
positive target is1+A, and V tensor P=A+P+D has no scalar, so its
image lies in Y. Both arrows are inherited from the primary module,
not arbitrary intertwiners. Their nonzero scale factors are not chosen.

The invariant quadratic acts on X by the actual map

    Q_X:X->Y, Q_X=sum_i b_i a_i,                    (8)

where a_i=a(e_i,-), b_i=b(e_i,-), and {e_i} is any orthonormal basis
for PR1114's invariant bilinear metric whose inverse is q. Equation
(8) is the actual R-module action, with no factor3 or alternate
quadratic normalization inserted.

## 3. Prove Q_X invertible and identify the actual image line

The shift in (3) gives the following positive primary pieces:

    B-degree2: (L3)_+=U tensor X=P tensor A=V+P+D;
    B-degree3: (L4)_+=U tensor Z=P tensor P=1+A+V+P+D;
    B-degree4: (L5)_+=U tensor (1+A)=V+2P+D.          (9)

Since (3) is an injection, the scalar in U tensor Z has a nonzero
image in H1(B(3)). Uniqueness of H in PR1118 identifies that image
with H itself. Thus H is located in the ACTUAL primary submodule.
R-linearity then puts B0=VH in (L5)_+. That space has one V, and
PR1118 proves B0 is a nonzero V, so B0=(L5)_V.

Let E_prim=(L3)_V, an actual nonzero V in E. R-linearity says that
the restriction of Q2 to L3 is Id_U tensor the actual primary
q-action. On U tensor X this is Id_U tensor Q_X, because invariant
multiplication cannot map X=A to the distinct scalar or T6 target.

If Q_X were zero, Q2 would kill E_prim. This contradicts PR1114's
injectivity of Q on the FULL E. Hence Q_X is nonzero. Its domain X
and target Y are irreducible of the same type A, so Q_X is an
isomorphism. This is not inferred from a dimension coincidence alone.

Consequently Q maps E_prim isomorphically onto the unique primary V
in (L5)_+, namely B0. Since Q:E->F4 is an isomorphism, this proves

    Q^-1 B0=E_prim=im K_E.                        (10)

This establishes the required actual inclusion before the trace
calculation. No isotypical label is substituted for a multiplicity line.

## 4. Coevaluation fixes the scalar normalization

Choose a nonzero h in the actual line H subset U tensor Z. This
identifies U with Z*: viewed as U*->Z, the invariant tensor h is
a nonzero map between irreducible copies of P and hence an isomorphism.
Under the induced identification U tensor Z=End(Z), h becomes Id_Z.
Changing h rescales this identification consistently and changes none
of the final operator or trace ratios.

Use the same identification to write U tensor X=Hom(Z,X) and
U tensor Y=Hom(Z,Y). Actual positive multiplication by y on the first
space is f |-> a_y f; multiplication by x on End(Z) is g |-> b_x g.
In particular the scalar second arrow sends h to b_x. By (10), the
map

    j:V->E_prim, j(z)=Q_X^-1 b_z                     (11)

is the actual inverse-Q transport of V->B0. It is injective by
PR1118 and is exactly an identification of that embedded V, not a
chosen unrelated intertwiner.

The invariant scalar projection in End(Z) is

    g |-> (tr_Z g / dim Z) Id_Z = (tr_Z g/4) h.       (12)

Indeed the invariant endomorphisms are precisely scalar identities
by Schur's lemma. Trace is invariant, equals4 on Id_Z, and vanishes
on every nonscalar irreducible component. The ambient scalar projection
in H1(B(3)) restricts to (12), since its scalar is the same actual H.

Define the invariant bilinear form on V

    beta(y,z)=tr_Z(a_y Q_X^-1 b_z).                  (13)

Because Hom_G(V tensor V,C) is one-dimensional, beta=c(y dot z)
for some scalar c. Trace cyclicity for the rectangular maps and (8)
give, without evaluating any a_i or b_i,

    sum_i beta(e_i,e_i)
      = tr_X(Q_X^-1 sum_i b_i a_i)
      = tr_X(Id_X)=3.                               (14)

The left side is3c since dim V=3. Thus c=1. In particular (12) on
the first multiplication of j(z) is exactly

    pr_H a_y j(z)=(y dot z)h/4.                     (15)

Applying the actual scalar second arrow and transporting by Q^-1,
the effective scalar channel on E_prim is

    Q^-1 b_x pr_H a_y j(z)=(1/4)(y dot z)j(x).       (16)

PR1114 defines its scalar-channel coefficient through the tensor
F0(x,y,z)=x(y dot z). Thus (16), in precisely that convention,
says K_mult is multiplication by1/4 on the multiplicity line
corresponding to the actual image (10).
Its rank is1 by PR1118. Hence its other eigenvalue is0 and it is
diagonalizable, proving tr K_mult=1/4 and K_mult^2=K_mult/4.

Equations (14)--(16) cancel all unknown nonzero primary arrow scales
against the ACTUAL inverse Q_X. No unknown scale was set equal to1.
The factor1/4 is dim X/(dim V dim Z)=3/(3*4), not a value obtained
by an actual coefficient, point, parameter or matrix evaluation.

## 5. Canonical splitting and exact first-arrow image

PR1118 gives ker K_mult=ker s in multiplicity space. Since Pi=4K_mult
is an idempotent, its induced operator Pi_E=Id_V tensor Pi=4K_E
has actual image E_prim and kernel V_s, providing (2) canonically. On the E_prim and V_s
multiplicity lines, respectively, the Q-transported channels (4) are

    Q^-1 C0:  1/4,   0;
    Q^-1 C1: -1/16, -1/4;
    Q^-1 C2:  3/16,  3/20;
    S:         1/8,  -1/10.                        (17)

In particular C1 and C2 each have multiplicity rank2. Every Cj
factors through the corresponding actual first-arrow restriction a_j.
Its multiplicity domain is two-dimensional, so each of a_V and a_D
must also have multiplicity rank2. The scalar first arrow has rank1
by PR1114. The nonisomorphic images1,V,D are disjoint, giving exact
image character1+2V+2D and dimension1+6+10=17.

This is a structural rank theorem for the complete actual arrow,
not an actual-instance rank computation. It excludes the earlier
dimension12 and14 alternatives and the rank-one nilpotent operator.

## 6. Negative projector: a sharper alternative, not a selected incidence

Only here assume ALL the source2 pure-V compatible-radical,
residual-large, and zero-fourth-obstruction hypotheses of PR1114
Section4. Keep its genuine e0, V_h and V_R=(NR4)_V. PR1118 gives

    p_V e0 b(V,a(V,V_h))=0
      iff B0=V_R OR V_h=V_s.                        (18)

Put L_h=Hom_G(V,V_h), viewed as a line in Hom_G(V,E).
In multiplicity space the two alternatives are im K_mult=L_h and
ker K_mult=L_h. Equation (1) makes those lines distinct, so these
alternatives cannot hold simultaneously. Equivalently (18) is now
an exclusive alternative WHEN the projected product vanishes.
Neither alternative is asserted to hold; the case where neither
holds remains possible, with the nonzero trace-free projected product
described in PR1114. The invariant trace in (1) is not that projected
product's trace, which concerns a different target row.

The failed route through a presumed scalar reachable in B-degree5 is
unnecessary and is not repaired by asserting such reachability. This
proof instead uses the actual constant U tensor primary factor,
the complete scalar projection (12), and contraction by the same q
that defines Q. It does not move e0 to the middle, identify primary
and negative-pencil blocks by character, or decide a fourth/fifth gate,
source occurrence, separated-correction normalization, Smith exponent,
or algebraicity.
