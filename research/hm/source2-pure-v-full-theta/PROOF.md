# The full Koszul-homotopy operator and a two-generator odd action

## Result and limits

Retain the actual source2 pure-V compatible-radical hypotheses. Use the
actual maps X_l:M2->M3, Y_l:M3->M4, h:M4->M2 and

    delta(z)=x tensor Y_y z-y tensor Y_x z.

Define on ALL of M3, not just ker j3,

    Theta=X(Id_W tensor h)delta.

Put H=ker Q3, J=ker j3, K=H intersect J and F3=W im h. Then

    im Theta=(F3)_T,       rank Theta=12,
    Theta^2=j3 Theta=Theta j3=j3^2=0,
    Q3 Theta=0,           Theta(F3)=0.                 (1)

There is a canonical marked complement

    L_Theta=Theta(H),       (F3)_T=I3 direct-sum L_Theta,
    L_Theta is isomorphic to T,                        (2)

where I3=im j3. The subspaces in (2) are actual images, not chosen
multiplicity lines. On H both j3 and Theta have rank6, common kernel K,
and distinct images I3 and L_Theta. As a module for

    A=C[epsilon,eta]/(epsilon,eta)^2,
    epsilon acts by j3, eta by Theta,

one has the equivariant isomorphism TYPE

    H is isomorphic to T tensor A plus (3W'+3S)_trivial. (3)

The isomorphism in (3) need not be canonical: the cyclic generator in the
T multiplicity space requires a lift. The two operators and their marked
image lines are canonical in the fixed inherited conventions.

This is an operator structure on degree-three odd cohomology H, not an
extension of Theta to the negative pencil, a global polynomial-module
endomorphism, an odd nullhomotopy, or a gate-nonvanishing theorem.

## 1. Four immutable inputs

INPUTS.json authenticates complete proofs at these exact commits:

- PR1085, 7d1c49ea66c54039f6adbbc27cac54222961784e,
  research/hm/source2-pure-v-mixed-syzygy/PROOF.md: F3=I3 direct-sum
  X(W tensor P_h), character W'+2T, and F3 is contained in K. It gives
  hY_l(J) contained in I2 and hY_l(F3)=0, the actual Koszul convention,
  and s:I4->P_h inverse to Q2 on P_h.
- PR1086, acb56908fd28ff019515b7ad9945f9b539f8614a,
  research/hm/source2-pure-v-odd-quadratic-rank/PROOF.md: H has
  character3W'+3S+3T and im Q3=3T inside M5=W'+3T.
- PR1089, f8dfebc8c12cbefd3b17422fa1220629e90af78e,
  research/hm/source2-pure-v-alternating-vanishing/PROOF.md:
  j3(H)=I3, K=3W'+3S+2T, K_T=(F3)_T, and Theta(NR3)=I3 with
  NR3 contained in J. It retains hQ2=j2, Q2h=j4, j2h=0 and actual
  radical intertwining. Its Theta had the restricted domain NR3.
- PR1094, 79b84d3b21cdbc76bb19d3a973e09981936dda32,
  research/hm/source2-pure-v-terminal-transfer-incidence/PROOF.md:
  on J the same formula factors as Theta=ell Q3, with ell:im Q3->I3
  onto, C=ker ell. In particular Theta(K)=0. This restricted formula
  is an OLD input, not the new full-domain formula proved below.

All input hypotheses remain. No Q-preservation of NC or NR, and no
commutation of h with negative multiplication, is assumed.

## 2. The full-domain quotient formula

Since im h=I2 direct-sum P_h, Theta lands in F3. The given hY_l(F3)=0
implies Theta(F3)=0. Hence Theta^2=0 already. Radical intertwining
j3X_l=X_lj2 and j2h=0 give j3Theta=0. Since im j3=I3 is contained in
F3, also Theta j3=0. The radical identity j3^2=0 is retained.

Actual invariant-quadratic commutation and Q2h=j4 give

    Q3 Theta(z)=x j4Y_yz-y j4Y_xz
               =x Y_yj3z-y Y_xj3z=0.                 (4)

The last equality is ordinary commutativity of the two actual negative
coordinates into degree five. Thus Theta also lands in H.

Let q:F3->F3/I3 be the quotient, identified with W tensor P_h by the
INJECTIVE actual first multiplication from PR1085. For any v in M3,

    Q2 hY_l(v)=j4Y_l(v)=Y_l j3(v).

The last expression lies in I4. Since hY_l(v) belongs to im h and Q2s
is the identity on I4, this proves the literal congruence

    hY_l(v)-sY_lj3(v) belongs to I2.                   (5)

Applying X and passing to q gives

    q Theta = d j3,
    d=(Id_W tensor s) delta|I3 : I3 -> W tensor P_h.    (6)

Here delta|I3 maps into W tensor I4 and is injective by the full actual
Koszul injection. Thus d is injective, with image the unique T constituent
of W tensor P_h=W'+T. Formula (6) has its displayed plus sign in the
fixed determinant convention; no scalar matching of abstract copies is
needed.

Since j3 is onto I3, qTheta has rank6. Its inverse image over zero is
controlled exactly: qTheta(v)=0 iff j3(v)=0. Therefore

    im Theta intersect I3 = Theta(J)=I3,              (7)

where surjectivity uses NR3 contained in J and Theta(NR3)=I3 from PR1089.
The rank of Theta is consequently6+6=12. Its quotient image has no W'
component, and its intersection with I3 is T. Equivariance then puts
its full image in (F3)_T; their equal dimensions prove equality. This
excludes a hidden W' image without identifying subspaces by character
alone. It also gives ker Theta contained in J.

## 3. The canonical complementary image on odd cohomology

Restrict (6) to H. The actual surjection j3:H->I3 has kernel K.
PR1094 gives Theta(K)=0, or one can see it from Theta(J) contained in I3,
K_T=(F3)_T, Theta(F3)=0, and Hom_G(W'+S,T)=0.
Thus Theta|H factors through H/K=I3. Equation (6) shows its quotient
image has rank6 and that its kernel is exactly K. It follows that

    rank(Theta|H)=6,     Theta(H) intersect I3=0.

Its image is contained in (F3)_T and is therefore the complementary T
in (2). This complement is an actual canonical image even though an
arbitrary splitting of H->I3 need not be canonical.

Both j3 and Theta annihilate K and have images in K. The two images
span K_T=(F3)_T. Choose any equivariant lift of the single T quotient
H_T/K_T. On each multiplicity generator u, the three vectors

    u, j3u, Theta u

form a basis of that three-dimensional multiplicity space: the latter
two vectors lie in independent marked lines, and u projects nontrivially
to the quotient. In this basis the operators are multiplication by
 epsilon and eta on A. This proves (3). On the other isotypical
constituents3W'+3S both operators vanish by equivariance, since their
images have type T.

Thus the radical image of this A-action on H is (F3)_T and its socle
(the common operator kernel, not the negative-coordinate socle) is K.
The representation of A is faithful. Every nonzero scalar combination
alpha j3+beta Theta on H has rank6 and kernel K; the two image lines
remain distinct rather than cancelling.

## 4. Relation to the old terminal plane and verification

The full-domain kernel has the intrinsic description

    ker Theta = J intersect Q3^{-1}(C),               (8)

using ker Theta contained in J and PR1094's restricted factorization.
Its character is3W'+3S+4T and dimension42. This does not extend the
factorization Theta=ell Q3 to all M3: such an extension would contradict
Theta(H)=L_Theta nonzero. The distinction of domains is essential.

The current coordination thread through its PR1094 update and the four
full inputs were read before the new deduction. Their restricted Theta
image and terminal plane are reused; the full image, canonical complement
and two-generator operator module are the new conclusions.

Run python verify.py and python -O verify.py. The checker authenticates
four immutable inputs, checks the formal determinant quotient signs,
rank/dimension arithmetic, and the universal regular-module matrices.
These normal forms verify the algebra after the actual-map proof; they
are not actual source matrices or evidence for a selected source instance.
No actual HM coefficients, parameters, directions, points, jets or ranks
are evaluated. No source, gate incidence, or remaining mechanism is selected.
