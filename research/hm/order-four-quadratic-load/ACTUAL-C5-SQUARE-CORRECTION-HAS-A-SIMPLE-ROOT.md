# The actual C5 square correction has a simple root

## New actual conclusions

Let x be ANY point of the reduced twelve-point polar orbit E on the negative line L=P(W). Its order-five projective stabilizer has one other fixed point y, which is also in E. Let a be a nonzero square negative quadratic with zero divisor 2x. In the unique positive-quartic character that can contribute to the final third quotient at a, let h be nonzero.

This is a UNIFORM theorem over the entire stabilizer orbit. The symbols t^2 and X^4 below are arbitrary normalized abstract eigenvectors for the stabilizer of an arbitrary x, not a selected actual HM point, source coefficient, or test case. No actual source coefficient, matrix, or rank is evaluated.

For the ACTUAL canonical global scalar correction

    Q(u(a,h)) = k a Lie_(D_a)(Qh),
    Q:D5 O_L -> V O_L(2),   k != 0,

the following statements hold.

1. The vector-valued section u has a simple common zero at x, and NO other common zero. In particular u(y) is nonzero. Consequently u is not divisible by a.
2. In the regular affine frame at x, the actual scalar representative Gamma=u+2k a a_z h also has exact order one. Its quotient Q(Gamma) has exact order five. Thus restriction to the cubic hides a nonzero, much lower order, scalar-extension contribution.
3. In the orthogonal polar normal form, R is regular at x. Its double principal part at the opposite fixed point y is also zero. The FULL physical R/nu nevertheless has a nonzero simple principal part at y, in the character detected by the final one-dimensional quotient. In a volume-compatible chart with a=1, it is

       Res_y(R/nu) = (2k/(15nu(y))) tau(r_y,m_h,y(y)) != 0.

   The coefficient m_h,y is the REGULAR TARGET coefficient. The proof retains every term and uses the exact universal ratio u(y)=-8k m_h,y(y), not just the nonvanishing of the two summands.

This nonzero residue belongs to the actual specified polar representative. It is NOT a statement that its cohomology class or the final third value is nonzero: global meromorphic coboundaries and the residues at the other ten poles can still cancel its class. The proof uses exact sequences, stabilizer weights, and identities of arbitrary abstract invariant tensors, not chosen actual coefficients or an actual-instance matrix evaluation.

## 1. All linearization conventions

Choose a lift of the stabilizer of order ten, with primitive eigenvalue alpha. We list weights as exponents modulo ten. On W the weights are +1,-1; on Wprime they are +3,-3. The two negative fixed points are specified by their TAUTOLOGICAL fiber weights:

    point                  x             y
    O_L(-1) fiber          +1            -1
    O_L(d) fiber           -d            +d
    tangent T_L fiber      -2            +2.

Let s,t be negative linear SECTIONS of weights -1,+1, with s(x)!=0, t(x)=0, s(y)=0, and t(y)!=0. Thus a=t^2 up to a nonzero scalar, and a has section weight 2. At x use z=t/s. The function w=s/t at y has weight -2, dual to the tangent weight there. For the actual local connection formulas one MUST instead use the volume-compatible coordinate v=-s/t: the Hamiltonian vector field D_(t^2) is +2 partial_v, whereas it is -2 partial_w. Sections 6-7 below use v, not the incorrectly oriented w. The homogeneous pair (t,-s) preserves the volume of (s,t).

Choose abstract eigenvectors X,Y of Wprime with weights +3,-3. This is an arbitrary stabilizer-adapted representation basis, not a numerical HM model. The relevant positive spaces have weights

    V=Sym^2 Wprime:        X^2:6, XY:0, Y^2:4;
    D5=Sym^4 Wprime:       X^4:2, X^3Y:6, X^2Y^2:0,
                           XY^3:4, Y^4:8;
    A=Sym^2 W:            s^2:8, st:0, t^2:2;
    P4:                   2,4,6,8.

The actual second symbol is quadratic in a and has rank three on square directions, since its degeneracy scheme misses the discriminant. Its image at a=t^2 therefore has the three weights

    2*2 + {8,0,2} = {2,4,6}.

The final quotient has weight 8. The third symbol is cubic in a, so it can detect only h of weight 8-3*2=2, namely h=X^4 up to a nonzero scalar. This identifies the channel without assigning a sign to an unspecified fiber.

## 2. The two actual cubic fibers and the Gaussian right-hand side

Let f be the actual invariant (3,3) cubic defining the quotient kernel. Its fiber is nowhere the zero cubic, and

    ker Q_x=f_x Wprime,     ker Q_y=f_y Wprime.

Since O_L(3) has fiber weight -3 at x and +3 at y, invariance and the four distinct weights in Sym^3 Wprime force

    f_x is a nonzero multiple of X^2Y,
    f_y is a nonzero multiple of XY^2.                    (1)

No value of either nonzero proportionality constant is used. For h=X^4, the section Qh has weight 2 in V tensor H0(O_L(2)). Consequently

    Qh = c0 XY t^2 + c1 Y^2 s^2,   c0*c1 != 0.           (2)

Both nonvanishing statements follow from (1): X^4 is divisible by neither f_x nor f_y, and hence Qh is nonzero in both fibers. This is an exact kernel argument, not inference from two nonzero composable maps.

The homogeneous Hamiltonian derivation associated with a=t^2 is, in the stated volume convention,

    D_a = -2t partial_s.

Thus the actual right-hand side is

    F=k a D_a(Qh) = -4k c1 Y^2 s t^3,                    (3)

up to the common fixed nonzero normalization of a and h. In particular F is nonzero. The actual map H0(Q(2)) is an isomorphism because its kernel Wprime O_L(-1) is acyclic, so (3) determines u uniquely.

## 3. The opposite-fiber obstruction is nonzero

Twisting the actual quotient by one gives

    0 -> Wprime O_L(-2) -> D5 O_L(1)
      --Q(1)--> V O_L(3) -> 0.

Its section boundary is the surjection

    delta:H0(V O_L(3)) -> Wprime.                        (4)

After apolar identifications, the dual map is a nonzero equivariant inclusion

    delta^*:Wprime -> V tensor Sym^3 W.

The target contains Wprime exactly once. The first positive transvectant with f gives a second nonzero map between these same representations:

    b -> (b,f)_1,   Wprime -> V tensor Sym^3 W.

It is nonzero because f has positive degree three and characteristic is zero. Therefore delta^* is a nonzero scalar multiple of this derivative map. This proves an identification of maps in a one-dimensional Hom space after proving that BOTH maps are nonzero; no nonzero-composite shortcut is used.

Now pair delta(Y^2 t^3) with X. The positive derivative (X,f)_1=partial_Y f has a nonzero X^2 s^3 term by (1). The product apolar pairing of Y^2 t^3 with X^2 s^3 is nonzero, and no other monomial contributes. Hence

    delta(Y^2 t^3) != 0.                                (5)

The opposite-point convention is important: the negative apolar pairing with t^3 extracts the s^3 coefficient, which is the fiber at x, NOT the fiber at y.

If u(y) were zero, the section u would be divisible by s, say u=s u1 with u1 in H0(D5 O_L(1)). Dividing (3) by s would put a nonzero multiple of Y^2 t^3 in image H0(Q(1)), contradicting (5). Therefore

    u(y) != 0.                                         (6)

This is a value-nonvanishing theorem for the actual inverse, proved by global exact-sequence geometry. It does not choose or compute an actual source coefficient.

## 4. The root at x is simple, not double

The section u is quadratic in a and linear in h, hence has weight 6. The weight-6 part of D5 tensor H0(O_L(2)) has the three monomial lines

    XY^3 t^2,   X^3Y st,   Y^4 s^2.

Since F(x)=0, one has u(x) in ker Q_x. But the sole possible nonzero value from the third line is Y^4, which is not in (X^2Y)Wprime. Its coefficient is therefore zero. Consequently

    u = b0 XY^3 t^2 + b1 X^3Y st.                        (7)

Statement (6) says b0!=0. Also b1!=0: otherwise u=t^2 v for a nonzero constant quartic v proportional to XY^3. Dividing Q(u)=F by t^2 and evaluating at x would give Q_x(v)=0, again impossible because XY^3 is not divisible by X^2Y. Thus b0*b1!=0.

The two quartics in (7) are linearly independent, so u has precisely the common factor t and no other common zero. Its order at x is exactly one. In the affine chart s=1, the correction 2k a a_z h is of order three, since a=z^2. Hence Gamma also has exact order one at x, with leading coefficient in the nonzero X^3Y kernel line.

On the other hand, the actual identity

    Q(Gamma)=2k a^2 (Qh)_z

and (2) give exact order five at x because c0!=0. The ambient scalar Gamma is therefore not divisible even by a, despite the much higher vanishing of its cubic-quotient restriction. This proves why the global extension correction cannot be omitted from the vector cochain.

## 5. What survives in the polar normal form

The polar theorem identifies the nonzero residue line C r_p with ker M_p, where M=M_kappa:V O_L(2)->V O_L(6) is regular nilpotent at p in E. At x the target/source twist difference shifts the positive V weight by +4:

    6 -> 0 -> 4 -> 8 (absent).

At y it shifts the positive V weight by -4:

    4 -> 0 -> 6 -> 2 (absent).

Rank two forces both arrows in each chain to be nonzero. Thus

    r_x is a nonzero multiple of Y^2,
    r_y is a nonzero multiple of X^2.                    (8)

These are the two fixed points in the SAME negative polar orbit E; their images are the opposite fixed square lines in the positive conic. No interchange of the two projection-ramification orbits is assumed.

At x, every term in the bracket multiplied by a^2 in the pinned polar formula has at most a double pole, while a^2 has order four. The scalar term has p of order minus one and Gamma of order plus one. Thus the ENTIRE R is regular at x, including the global scalar correction.

At y the polar theorem gives the double coefficient (k/15)a(y)^2 tau(h,r_y). It vanishes because tau(X^4,X^2)=0. Hence both fixed points have zero double coefficients in the detectable h channel, with the stronger total regularity at the root x.

The simple scalar term at y is different. In the chart t=1, a is constant and Gamma=u. Equations (6)-(8) imply

    tau(r_y,u(y)) is a nonzero multiple of
      tau(X^2,XY^3)=12 XY.                               (9)

It therefore gives a nonzero simple principal part of the isolated scalar summand. Multiplication by a and division by the physical unit nu cannot remove this nonvanishing.

For completeness, its LOCAL contribution to the actual final residue test is nonzero as well. The dual line annihilating image beta2_a has weight 2 in P4-dual. For nonzero c in that line, the fiber i_y^t c is a nonzero multiple of XY: its required positive weight is 2-2=0, and the kernel of i_y^t is the weight-4 line supplied by q_y^t:O_L(-6)|y->P4-dual. Thus a i_y^t c pairs nontrivially with (9), since the V pairing is nondegenerate on its weight-zero line.

The remaining issue at this one pole is cancellation with the other summands of R. The next two sections settle that local cancellation by an exact ratio. They still do not evaluate the sum of residues from the other ten points or the global meromorphic coboundary correction that removes the double layer.

## 6. Weights reduce the entire residue to one actual diagonal coefficient

Use the oriented coordinate v=-s/t and the frame t=1, so a=1 and a_v=0. Choose a stabilizer-equivariant REGULAR quintic lift g_y; finite-group averaging of any regular lift supplies one without changing its normalized quotient. Compare it with the actual orthogonal meromorphic lift by g_y=g_perp+p f.

The transition p is an invariant meromorphic section of V O_L(-8). Its coefficient of v^j must have positive weight 2j-2. The actual section n_h in V O_L(6) has weight 2, so its coefficient of v^j has positive weight 2j-4. The available V weights therefore force

    p = r_y/v + p1 XY v + O(v^3),    r_y in C* X^2,
    n_h = n0 X^2 + n2 XY v^2 + O(v^4),   n0 != 0.        (10)

In particular p has NO constant or quadratic term and n_h has NO linear term. The two leading coefficients n0 and r_y are nonzero by the regular nilpotent chain and Qh(y)!=0. These are expansions dictated by actual equivariance, not substitute local models.

The universal quadratic pairings imply

    tau(p,n_h)=O(v^3),    tau(p,p)=O(v^2),
    tau(h,p_v) has no polar part.                        (11)

For example the possible terms before these orders pair X^2 with X^2 or XY and hence vanish. The last assertion uses tau(X^4,X^2)=0.

Write m_y=(h f_v-n_h g_y)/f for the regular target coefficient. The SOURCE coefficient is exactly m_perp=m_y+n_h p. Its pole is in C X^4/v, and its constant coefficient is m_y(0) because p0=n1=0. Inserting (10)-(11) in the FULL pinned R formula leaves

    Res_y R = -tau(r_y,4k m_y(0)+u(y))/30
            = tau(r_y,b_y(0))/15,
    b_y=-u/2-2k m_y.                                    (12)

No target-frame term has been discarded. Formula (12) is in the volume-compatible v coordinate; using w=s/t in the derivative defining m_y would reverse its sign and give an erroneous ratio.

## 7. A universal symplectic-socle identity fixes the remaining ratio

We now derive an identity valid for EVERY abstract nonzero invariant cubic tensor with these representation identifications. The four letters below denote arbitrary maps between one-dimensional stabilizer eigenspaces. No value is chosen or evaluated at any actual HM point. In ordinary monomial conventions write the tensor as

    f = A X^2Y s^3 + B Y^3 s^2t + C X^3 st^2
        + D XY^2 t^3.                                   (13)

All four line maps are nonzero: f is the equivariant isomorphism between the two irreducible cubic four-spaces, and their stabilizer characters are distinct. This is stronger than assuming just f_x and f_y nonzero.

Both cubic four-spaces have their nondegenerate alternating apolar form, unique up to scalar. An equivariant isomorphism preserves those forms up to a nonzero scalar. Comparing its two opposite eigenspace pairs gives the tensor identity

    AD + BC = 0.                                        (14)

For clarity, the ordinary unnormalized cubic apolar values are <X^3,Y^3>=36 and <X^2Y,XY^2>=-12, while <st^2,s^2t>=12 and <s^3,t^3>=36. Applying these to the map from the positive DUAL cubic space gives BC/(3AD)=-1/3, which is exactly (14). Thus (14) is a universal symplectic identity, not a guessed coefficient relation.

The actual socle functional has coefficient line O_L(2):

    lambda:Sym^6(Wprime) -> H0(O_L(2)).

It is nonzero and annihilates both f Sym^3(Wprime) and g_y Wprime. Stabilizer weights force its only possible monomial values to be

    lambda(X^6)=c s^2,       lambda(XY^5)=d s^2,
    lambda(X^3Y^3)=e st,     lambda(X^5Y)=j t^2,
    lambda(Y^6)=l t^2,
    lambda(X^4Y^2)=lambda(X^2Y^4)=0.

The four cubic-annihilation identities are

    A j+B e+C c=0,   C j+D e=0,
    A e+B d=0,       B l+C e+D d=0.

Together with (14) they give

    c=-2B e/C,   d=-A e/B,   j=-D e/C,   l=-2C e/B.      (15)

Here e!=0, since otherwise the same identities would make the nonzero lambda vanish entirely.

Pair Q(u)=k a D_a(Qh) with the CONSTANT positive quadratics X^2 and Y^2 using the actual socle pairing. For u=U XY^3 t^2+V X^3Y st from (7), these equations read

    U e+V j=-4k c,       U d+V e=0.

Equations (14)-(15) yield the universal inverse value

    U=4k B/C,   V=4k A/C.                               (16)

This is derived from the socle pairing itself, not by constructing or evaluating a quotient matrix.

Finally, stabilizer weights give g_y(0)=alpha X^5+beta Y^5. The ACTUAL fiberwise coprimality of the cubic and quintic gives alpha*beta!=0. The identity lambda(g_y Y)=0 and (15) imply

    beta/alpha=-BD/(2C^2).                              (17)

In the oriented coordinate v=-s/t, equation (13) gives f_v(0)=-C X^3 and f(0)=D XY^2. Since n_h(0)=n0 X^2, the defining identity h f_v-n_h g_y=f m_y gives n0 alpha=-C and then

    m_y(0)=(C beta/(D alpha)) XY^3
          =-B/(2C) XY^3 != 0.                           (18)

Combining (16) and (18) proves the exact actual ratio

    u(y)=-8k m_y(0),   b_y(0)=2k m_y(0).                 (19)

Inserting this in (12) proves the claimed NONZERO full simple residue

    Res_y(R/nu)=(2k/(15nu(y))) tau(r_y,m_y(0)) != 0.      (20)

The physical normalization contributes no derivative correction at y because its double coefficient is zero. If the square a is not normalized to 1 in this chart, (19)-(20) carry a(y)^2 in the terms multiplying m_y, and the final cup by a contributes one further a(y). The actual nonzero k and nu(y) are retained.

Equation (20) also pairs nontrivially with the local final test a i^t c described in Section 5. It is uniform for all twelve choices of x, not an actual-instance sample. It still does NOT give a nonzero global class: the full Serre criterion is a sum over all twelve poles, and the exact polar theorem proves that global meromorphic coboundaries can alter individual principal parts. No equality of a nonzero local residue with the third Bockstein is asserted.

## Dependencies and reproduction

Use ACTUAL-VECTOR-SHADOW-HAS-A-TWELVE-POINT-POLAR-NORMAL-FORM.md for the actual Gram maps, residue lines, cochain, and final residue test; ACTUAL-CONE-DIAGONAL-IS-CANONICAL-RESIDUE-INVERSE.md for the actual u and Gamma identities; UNIVERSAL-CUBIC-EVEN-DEFECT-QUOTIENT-IS-TRIVIAL-V.md for the actual cubic quotient; ACTUAL-POSITIVE-ATIYAH-MULTIPLICATION-SURJECTS-ONTO-NINE-SPACE.md for the socle functional and its O(2) coefficient line; and VERTEX-QUINTIC-RELATION-EXTENSION-AND-SQUARE-P4.md for actual fiberwise cubic/quintic coprimality. The second-symbol rank on squares and cubic homogeneity are established actual inputs, not new assertions of this note.

Run python verify_c5_square_correction_simple_root.py. It checks the universal character multiplicity, every displayed stabilizer/fiber weight, the actual-compatible twist arithmetic, the homogeneous Hamiltonian identity, the universal apolar and transvectant nonzero pairings, and the symbolic identities (15)-(20) modulo the universal relation (14). The latter are identities in independent formal symbols, not a source-instance calculation or a local-model experiment. It does not construct, substitute, evaluate, or scan any actual HM/source coefficient or map matrix. The exact-sequence and geometric arguments are supplied above.
