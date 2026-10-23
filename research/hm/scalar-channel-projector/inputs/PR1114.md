# The full repeated-V positive pencil is a rank-one perturbation

## Result and boundaries

Use the actual normalized HM cohomology module over C with the fixed
G=SL2(F5) action. Let V be the positive three-dimensional irreducible,
N2=H1(B(2))_+, P3=H1(B(3))_+, N4=H1(B(4))_+, and retain ACTUAL
multiplication a:V tensor N2 -> P3 and b:V tensor P3 -> N4.
Let E=(N2)_V and F=(N4)_V be the FULL isotypical subspaces, both 2V,
and r:N4 -> F the canonical isotypical projection. Thus r is NOT the
single residual projector row p_V e0 used in PR1111.

The canonical invariant quadratic gives an actual isomorphism
Q=Q2|E:E -> F. For the actual positive two-step product

    T_F(x,y,z) = r b(x,a(y,z)),     z in E,

the unique scalar constituent of P3 forces a rank-at-most-one
endomorphism K of the two-dimensional multiplicity space of E. In
the invariant normalization specified below the effective channels are

    C0 = Q K,
    C1 = Q (3K-Id)/4,
    C2 = (3/20) Q (K+Id).                              (1)

In particular K^2=(tr K)K and det K=0. The normalized coefficient of
the traceless positive quadratic is S=(9K-Id)/10 and satisfies

    (10S+Id)^2 = (10 tr S+2)(10S+Id),
    det(10S+Id)=0.                                    (2)

These are universal polynomial identities for the actual multiplicity
pencil, not evaluations of its entries or its trace. The full first
arrow a restricted to V tensor E has image dimension in {12,14,17}.
There is a canonical actual V_s in E: its multiplicity line is the
kernel of the first scalar-channel functional. On V tensor V_s the
actual first arrow has image character V+D and dimension exactly 8.

Now add the actual source2 pure-V compatible-radical, residual-large,
and R=0 hypotheses of PR1108. Retain its actual V_h, V_C and genuine
negative projector e0. Let V_R=(NR4)_V and let

    B0 = b(V tensor (P3)_1) subset F.

Here B0 is zero or one actual V. Then the following are equivalent:

    (i)  p_V e0 b(V,a(V,V_h)) = 0;
    (ii) B0 is contained in NR4, OR V_h=V_s.             (3)

If neither alternative in (ii) holds, the projected product on V_h is
nonzero and trace-free, all three effective channels survive, and
a|V tensor V_h is injective. Equivalently the full projected product
factors through the actual quotient Gamma of PR1108 exactly in (3).

Neither incidence in (3) is decided. R=0 is not asserted realized or
excluded. No original source pair, higher-order gate, fifth class or
algebraicity statement is decided. All image dimensions above are
structurally forced possibilities or deductions, not selected-instance
matrix/rank computations.

## 1. Immutable inputs

INPUTS.json retains four complete originals at exact commits, with
Git blob and SHA256 authentication.

* PR931, e28d3b74d4288239426ad1e675e806310fadf8be:
  N2=A+2V+3P+4D, P3=1+4A+2V+3P+3D, ker Q2=A+D, and the
  actual image of a has character 1+3A+2V+3P+3D. The tensor products
  V tensor A=P+D, V tensor V=1+V+D, V tensor P=A+P+D,
  V tensor D=A+V+P+D are given there.
* PR933, 804661fb49e245a8df884937bb8d38fb5d0dc17a:
  N4=2V+4P+3D; the actual positive product is b(Id tensor a), with
  ordinary positive commutativity. Its invariant contraction is Q2.
* PR1111, f74c5ad30de84707239086d4d3d964546c5dc2f0:
  the three nonzero channel tensors F0,F1,F2, their completeness,
  the commutativity equation and invariant contraction constants.
* PR1108, c1e2c2e0013a45ff2345a687d2077d7f7e322cef:
  under residual-large E=V_C direct-sum V_h, Gamma has kernel V_h;
  with R=0 additionally V_h=ker(e0 Q2|E), Q2(V_h)=V_R, and
  Gamma=chi(e0 Q2)|E for the actual induced isomorphism chi.

The first three sections below do not need the source2 hypotheses.
Section 4 retains ALL hypotheses of the fourth input. No character
label is substituted for any actual embedded subspace.

## 2. The actual two-copy scalar bottleneck

Write L=Hom_G(V,E) and M=Hom_G(V,F), both two-dimensional; the
evaluation maps V tensor L -> E and V tensor M -> F are canonical
isomorphisms. Since ker Q2 has no V, its restriction Q:E -> F is an
isomorphism. Write Q also for its induced isomorphism L -> M.

Choose an invariant metric on V whose inverse quadratic is the fixed
canonical q defining Q2. Over C this is possible by rescaling the
invariant metric, since both invariant spaces are one-dimensional and
q is nonzero. This chooses a FORMULA convention, not a value of an
actual HM coefficient. Normalize the invariant volume compatibly.
The tensors of PR1111 become

    F0(x,y,z)=x(y dot z),
    F1(x,y,z)=y(x dot z)-z(x dot y),
    F2(x,y,z)=y(x dot z)+z(x dot y)-(2/3)x(y dot z).

They respectively factor through 1,V,D in y tensor z. Completeness of
these three channel spaces gives unique Cj:L -> M with
T_F=sum Fj tensor Cj. These are actual composites with b and r; the
second arrow is not discarded. Componentwise PR1111 gives

    C0=C1+(5/3)C2,       Q=-C1+5C2.                  (4)

Let H=(P3)_1, an actual one-dimensional trivial representation. The
scalar first-arrow restriction is represented, with the displayed F0
normalization, by a map s:L -> H. The actual scalar second arrow is
represented by d:H -> M. Thus C0=d s.

The map s is onto: the actual reachable middle in PR931 contains H,
and among V tensor N2 only V tensor E has scalar constituents. This
also shows that V_s=V tensor ker s subset E is a canonical embedded
V. It is the KERNEL line of the first scalar functional, not a chosen
complement or the scalar image. The map d may be zero; no faithfulness
of the second arrow is assumed.

Set u=Q^{-1}d and K=u s. Then rank K is at most one, and
K^2=u(su)s=(su)K, with tr K=su. Solving (4) proves (1).

For clarity, the traceless-coordinate part is determined by the
coefficient alpha=C1+C2 of x(y dot z)+y(x dot z). The remaining
coefficient is beta=C2-C1. On trace-free symmetric quadratics the
beta term contributes zero. Formula (1) gives

    Q^{-1}alpha=S=(9K-Id)/10.

Its exact normalization is the displayed metric-tensor convention.
It follows that 10S+Id=9K and tr K=(10 tr S+2)/9, proving (2).
In particular -1/10 is an eigenvalue of S. This is stronger than a
dimension bound: the whole multiplicity operator satisfies (2).

## 3. First-arrow image restrictions and the canonical V_s

Let a_j be the actual first arrow on J tensor L for J=1,V,D.
Its multiplicity ranks are r0=1 and r1,r2 in {0,1,2}. Nonzero
irreducible images of different J are disjoint. The coefficient Cj
factors through a_j, so its multiplicity rank is at most rj.

Let t=tr K. Since det K=0, the two eigenvalues of K with multiplicity
are 0,t, including the possible nilpotent case t=0. Consequently

    det(3K-Id)=1-3t,       det(K+Id)=1+t.             (5)

Each shifted operator has rank at least one, since a rank-at-most-one
K cannot be a nonzero scalar multiple of Id. Their determinants cannot
both vanish: t cannot equal both 1/3 and -1. Thus r1,r2 are both at
least one and at least one is two. The only possible pairs are
(2,1),(1,2),(2,2), giving total dimensions

    1+3r1+5r2 in {12,14,17}.                         (6)

If dimension 12 occurs then t=-1; if dimension 14 occurs then t=1/3.
These implications are NOT reversed: b can kill a nonzero part of a_j.
If K=0, both shifted operators are invertible, so the dimension is 17.
This includes s nonzero with d=0.

On ker s, K=0, so C1=-(1/4)Q and C2=(3/20)Q there. Since Q is
injective, both coefficients are nonzero on that line. Both actual
a_V and a_D are therefore nonzero and injective on their irreducible
restrictions. The scalar restriction vanishes by definition. Hence
a(V tensor V_s) has exactly character V+D and dimension 8. Its
V-isotypical projected two-step output lies in the actual Q(V_s).
This last assertion concerns rT only, not other target irreducibles.

## 4. Exact comparison with the zero-fourth correction

Assume residual-large and R=0 as in PR1108. Let M0 and MR be the
one-dimensional multiplicity spaces of (N0,4)_V and V_R. The actual
negative projector gives rho:M -> M0 with kernel MR. Let

    lambda=rho Q:L -> M0,       L_h=ker lambda.

PR1108 proves lambda nonzero, V_h=V tensor L_h, and V_C transverse
to V_h. This identification is conditional on R=0. No positive
projector on P3 is postulated: rho acts only AFTER the actual b.
Since e0 is equivariant, it cannot send any other target isotypical
part into V. Thus p_V e0=rho r on N4: the single projected row here
is exactly the specified actual projector, not a substituted copy.

The three effective coefficients after rho are

    c0=lambda K,
    c1=(3 lambda K-lambda)/4,
    c2=(3/20)(lambda K+lambda).                      (7)

On L_h their values are in the ratio 1:3/4:3/20. The whole projected
product vanishes there iff lambda K|L_h=0. Since K=u s and s is onto
the one-dimensional H, this vanishing holds exactly when

    lambda u=0, OR s|L_h=0.                          (8)

Indeed if both factors are nonzero, their composite between lines is
nonzero. The first alternative is rho d=0, namely B0 subset NR4.
The second is ker lambda=ker s, namely V_h=V_s. This proves (3),
including the d=0 case in its first alternative.

If neither holds, (7) is nonzero on L_h in all channels, while its
invariant contraction is lambda|L_h=0. Each corresponding a_j is
nonzero on an irreducible, proving injectivity on 1+V+D (dimension9).

Finally a linear map on Sym2 V tensor E factors through
Id tensor Gamma iff it kills Sym2 V tensor ker Gamma. The latter
kernel is Sym2 V tensor V_h. Thus the quotient factorization assertion
is precisely (3), using the actual Gamma, not a character-equivalent
copy or a claimed extension of e0 to the middle.

## 5. Universal sharpness and nonselection of the incidences

The restrictions cannot be improved from these local positive diagrams
alone. Here are explicit UNIVERSAL representation diagrams, not actual
HM coefficient matrices. Take L=M=C2, Q=Id, H=C, s=(1,0), and
u=(t,0)^T. Let K=u s, and use (1). Form an intermediate representation

    U=H plus (V tensor (L/ker C1))
        plus (D tensor (L/ker C2)).

The first arrow is the scalar map s and the quotient maps on V,D.
The second arrow on these three summands is given by the intertwiners
F0,F1,F2 and their induced Cj (on H use d=u). Thus their product is
sum Fj Cj. Equation (4) proves positive-positive commutativity and
contraction Q=Id. Extend this to a graded module with zero outgoing
arrows from its final degree; all remaining commutation relations then
hold. For t=-1,1/3,1 the first-arrow image dimensions are respectively
12,14,17. For t=0 the scalar first arrow remains nonzero but d=0,
and the dimension is again17. These examples can be padded by unused
representations to fit P3's character, but are NOT asserted to satisfy
HM cohomology, negative-arrow relations, or source occurrence.

The two incidences in (3) are genuinely distinct at this interface.
With Q=Id, lambda=(1,0), L_h=C e2, use these exact formal data:

* s=(1,0), u=e1: V_h=V_s but scalar output is not residual.
* s=(0,1), u=e2: scalar output is residual but V_h is not V_s.
* s=(1,1), u=e1: neither incidence holds and the projected product
  on V_h is nonzero trace-free.

The same construction supplies commuting positive diagrams in each
case, with Gamma=lambda and the abstract actual-row identities of the
interface. No assertion is made that these diagrams extend to the full
negative HM/source module. They prevent inferring either incidence
merely from the displayed positive and multiplicity identities; they
do not establish realizability of any surviving source mechanism.

## Reproduction and remaining dependency

Run python verify.py and python -O verify.py. The bounded exact checker
authenticates all four sources, verifies the universal tensor equations,
polynomial rank-one identities, determinant exclusions, support cases,
and the finite sharpness/countermodel controls. Formal variables and
universal models are used, never actual HM/source coefficients, points,
parameters, jets, derivatives, matrices, ranks or scans.

The next structural question is concrete: must the actual scalar
second-arrow image lie in NR4, or must the actual scalar first-arrow
kernel V_s equal the canonical homotopy kernel V_h? If neither, the
nonzero trace-free projected correction is forced, but this alone is
not a fifth-symbol computation. The present theorem supplies no answer
to these incidence questions and makes no higher-order or algebraicity
claim.
