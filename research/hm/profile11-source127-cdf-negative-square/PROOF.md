# The exact c-d-f negative-square cokernel and restricted relation space

## Result and scope

Assume an actual source127 c-d-f occurrence. Write

    q_-:Sym2(W) tensor N2 -> N4,
    q_-(uv tensor x)=B_u A_v x

for the aggregate symmetric-negative quadratic action on the fixed actual pencil. Its image has dimension 30 and character V+3P+3D. Its intrinsic cokernel Pi has dimension seven and character V+P. The restricted quadratic relation space Z=ker q_- has dimension 93 and character

    Z=1+5A+6V+6P+7D.

We prove actual natural exact sequences identifying these spaces, rather than inferring them from character subtraction. Actual degree-zero generation then implies that all positive quadratics together surject onto the precise missing quotient Pi.

Z is the kernel of this restricted product map only. It is not the full five-variable module's minimal relation space, nor even the kernel of the full degree-two product on K3. These are universal conditional identities, not a selected-instance matrix or rank calculation. They do not exclude c-d-f or realize an abstract parameter by the actual HM module.

## 1. Exact dependency interface

All paths refer to Akilleez-QA/read-em-and-weep.

1. PR924 at c6c25eaf0e5a67c27eee7c3ba4f000df55997692, research/hm/profile11-source127-cdf-pencil-algebra/PROOF.md, Git blob 83f5aee293995257459229e6b323522224ce8f3d. Its normal-form input gives the actual direct-sum inclusion over the fixed base. Section 4 authenticates the simultaneous covariant identification with both fixed actual negative maps, using one determinant convention. We use the exact cohomology functor, not just its representation characters.
2. PR925 at 2be52725fe471efdc64d74bd87702b581f9f6a48, research/hm/profile11-source127-cdf-positive-generation/PROOF.md, Git blob becd3300950c2379d1f03294863d8335a83a1087. Its Section 2 proves the actual aggregate identity N4=im q_++im q_- from the independently authenticated degree-zero cover. No individual positive quadratic is asserted to supply that image.

The source coordinates and representations are those of PR924. In particular W is the defining two-space, A=Sym2 W, S=Sym3 W, D=Sym4 W, T=Sym5 W, and P,V,Wp denote the other established irreducibles. In any one of the proved constant normal forms,

    H=C10 direct-sum C11 direct-sum C9,
    C10=A+V+P, C11=A+V+D, C9=P+D,
    E=F direct-sum B direct-sum L,
    F=(P+D)(-2), B=(V+P)(-4), L=O(-8),
    Q=Q_F direct-sum Q_B direct-sum Q_L,
    Q_F=O(18), Q_B=S O(7), Q_L=(Wp+T) O(1).   (1)

The three block sequences 0->E_X->C_X O->Q_X->0 are actual direct summands of 0->E->H O->Q->0. No normal-form parameter is chosen.

## 2. The canonical six-term sequence

The covariant reconstruction gives

    N2=H0(Q(-2)), N3=H0(Q(-1)), N4=H1(E).

Let delta:H0(Q)->N4 be the connecting map. Since H1(H O)=0 it is surjective, and H0(E)=0 identifies its kernel with the actual constant space H. Thus

    0 -> H -> H0(Q) --delta--> N4 ->0.          (2)

The fixed determinant identification W isomorphic to H0(O(1)) defines the ordinary multiplication map

    mu:Sym2(W) tensor H0(Q(-2)) -> H0(Q).       (3)

The simultaneous actual-pencil formulas of PR924 are A_t(s)=t s and B_t(u)=delta(t u). Therefore the actual symmetric-negative quadratic action is exactly

    q_-=delta mu,                              (4)

with the same variables, not merely an isomorphic product map. Symmetry follows from ordinary multiplication. There is no evaluation at a negative point or variable in this argument.

Put Z=ker q_- and Pi=coker q_-. Equations (2)-(4) give the canonical six-term exact sequence

    0 -> ker mu -> Z --mu--> H
        -> coker mu -> Pi ->0.                 (5)

For clarity, mu carries Z into H because delta mu vanishes there. Its kernel is ker mu. Its image is H intersect im mu. The map from H is the inclusion into H0(Q) followed by the quotient by im mu; its kernel is that same intersection. Finally the quotient is H0(Q)/(H+im mu), canonically equal to Pi by (2) and (4). This proves exactness without introducing an unproved complement or saturation inference.

## 3. The image and seven-dimensional quotient

For d>=2, the multiplication Sym2 W tensor Sym^(d-2) W -> Sym^d W is onto. Every degree-d binary monomial factors as a quadratic times a degree-(d-2) monomial. This is a universal polynomial identity.

Apply this to Q_F=O(18) and Q_B=S O(7), tensoring the latter multiplication by the fixed coefficient representation S. The scalar quotient block Q_L contributes nothing to H0(Q(-2)), because its line degree is one. Consequently, in (1),

    im mu=H0(Q_F) direct-sum H0(Q_B),
    dim im mu=19+4 times 8=51.                 (6)

Each block boundary H0(Q_X)->H1(E_X) is onto by H1(C_X O)=0. Its kernel is C_X since all E_X have negative degree. Because the quotient sequences in (1) are actual block summands, (6) intersects H exactly in

    H_minus:=H intersect im mu=C10 direct-sum C11,
    dim H_minus=21.                           (7)

Thus (4) has image

    im q_-=N4,F direct-sum N4,B
           =(P+D)+(V+2P+2D)=V+3P+3D,          (8)

of dimension 9+21=30. The cokernel in this normal form is N4,L=H1(O(-8)), whose character is Sym6 W=V+P. Intrinsically it is the quotient Pi in (5), independent of a chosen normal-form splitting.

The second half of (5) can be displayed as the actual short exact sequence

    0 -> H/H_minus -> coker mu -> Pi ->0.       (9)

In normal-form labels, H/H_minus=C9=P+D and coker mu=H0(Q_L)=(Wp+T) tensor W. The universal identity Sym7 W tensor W=Sym8 W+Sym6 W therefore gives dimensions 9,16,7 and the same quotient character. This character identity is a check of (9), not its proof. The subspace H_minus is intrinsic as defined in (7); only its description by the indicated block names uses a normal form.

## 4. The exact restricted quadratic relation space

For d>=4, the universal Clebsch-Gordan decomposition gives

    ker[Sym2 W tensor Sym^(d-2) W -> Sym^d W]
          isomorphic to Sym^(d-2) W + Sym^(d-4) W.

The map is the top symmetric product and is onto, so the other two summands are precisely the kernel. We only use d=18 and d=7, both inside the stated range. Tensoring by the fixed coefficient S in the second block yields

    ker mu=Sym16 W + Sym14 W
                  + S tensor (Sym5 W+Sym3 W).  (10)

Here and below equality of character expressions denotes representation isomorphism, not a canonical splitting of the six-term sequence. The dimensions of (10) are 17+15+4(6+4)=72.

The first half of (5) is the actual exact sequence

    0 -> ker mu -> Z -> H_minus ->0.            (11)

Surjectivity onto H_minus is immediate from its definition as H intersect im mu: every vector in that intersection has a preimage under mu, and that preimage belongs to Z. Therefore dim Z=72+21=93.

For the explicit G-character, use

    Sym16 W=V+P+2D,
    Sym14 W=A+V+P+D,
    S tensor T=A+V+2P+2D,
    S tensor S=1+A+V+P+D.

The last identity also follows directly from Sym3 tensor Sym3=Sym6+Sym4+Sym2+Sym0. These give

    ker mu=1+3A+4V+5P+6D,
    H_minus=2A+2V+P+D,
    Z=1+5A+6V+6P+7D.                         (12)

Finite-group representations over C are semisimple, so (11) splits as a G-representation, but no distinguished splitting is asserted. In particular (12) does not determine the actual embedding of Z into Sym2 W tensor N2; that embedding retains the actual quotient data.

Together, the restricted multiplication has the exact four-term presentation

    0 -> Z -> Sym2(W) tensor N2 --q_---> N4
          -> Pi ->0.                           (13)

Its dimensions are 0->93->123->37->7->0. As a consistency check, Sym2(W) tensor N2 has character 1+5A+7V+9P+10D, which is the sum of Z and the thirty-dimensional image in (8).

## 5. The exact target of the required positive action

The pinned generation theorem proves the equality of actual images

    N4=im q_+ + im q_-,
    q_+:Sym2(T_+) tensor N2 -> N4.

Composing q_+ with the intrinsic quotient N4->Pi therefore gives a surjection

    chi_+:Sym2(T_+) tensor N2 -> Pi,
    Pi isomorphic to V+P.                     (14)

This identifies the exact seven-dimensional quotient that the positive quadratics must supply. The quotient is natural; identifying it with a particular N4,L complement is optional and depends on normal-form coordinates. No individual positive quadratic is selected, and no statement about its separate image is made.

Equation (14) does not determine the full q_+, the actual embedding of its kernel, or its other target components. It does not choose between the scalar and C^2 positive-compatible algebras of the generation theorem, force a full five-variable window lift, or force a full-module lift. The intrinsic seven-dimensional quotient and (11) provide a narrower exact compatibility interface, not an exclusion of a nonempty abstract family.

No source, source-dual pair, stable label or frontier count changes. No selected actual HM/source data or matrix is evaluated and no large computation is used.
