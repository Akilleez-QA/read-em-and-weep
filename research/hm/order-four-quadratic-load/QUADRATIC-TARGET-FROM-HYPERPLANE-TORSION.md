# The quadratic obstruction target is the root transform of the hyperplane cokernel

## Exact target identity

Retain T=P(W*), P=P(Sym^2 W), the universal root divisor Z, and its maps eta:Z->T and nu:Z->P. Let

    C_lin = coker[H1(B(2))_- O_T(-1) -> H1(B(3))_+ O_T],
    C_quad = coker[H1(B(2))_- O_P(-1) -> H1(B(4))_- O_P].

These are the actual cokernel sheaves of the universal multiplication maps. Then there is a canonical global isomorphism

    C_quad = nu_* eta*(C_lin tensor O_T(1)).          (1)

It includes double roots, exceptional roots, and intersections of their parameter lines. Together with the established kernel A tensor nu_*O_Z(-5), this describes both ends of the actual six-to-ten smoothing construction by the same degree-two root correspondence.

## 1. Functorial proof

On the universal hyperplane X, restriction to the positive plane gives

    0 -> p*B(3) tensor pi*O_T(1)
      -> p*B(4) -> B_R(4) external-tensor O_T -> 0.

The last term is entirely even. Taking odd derived direct images, with the center-odd O_T(1) retained, gives

    (R1 pi_*p*B(4))_- = C_lin tensor O_T(1).           (2)

The projection eta:Z->T is flat. Flat base change therefore identifies the corresponding first direct image for X_Z->Z with the pullback of (2). The other projection nu is finite, so has no higher direct images on coherent sheaves.

Finally, the uniform conductor sequence from GLOBAL-NEGATIVE-QUADRATIC-KERNEL-BUNDLE.md is

    0 -> B_D(4) -> (p_Z)_*B_XZ(4)
      -> B_R(4) external-tensor O_P(-1) -> 0.

Its last term is entirely even, so it induces an isomorphism of odd derived direct images. This proves (1), not only an equality of its generic ranks.

## 2. Canonical torsion and locally free quotient

Let T_lin be the torsion subsheaf of C_lin and let F_lin=C_lin/T_lin. The quotient is a rank-five vector bundle on T. The uniform hyperplane jump theorem proves that T_lin is supported on the twelve order-five parameters, with the same local length j at each, where j belongs to {0,1,2}.

Pullback by the flat map eta and pushforward by finite nu are exact. Hence

    0 -> nu_*eta*(T_lin(1)) -> C_quad
      -> nu_*eta*(F_lin(1)) -> 0.                     (3)

The last term is locally free of rank ten: eta*F_lin(1) is locally free on Z, and nu is finite flat of degree two. The first term is supported on the twelve lines

    L_t={q in P : q(t)=0},

one for each exceptional t. Therefore the first term in (3) is exactly the torsion subsheaf of C_quad. This description is canonical. A splitting of C_lin into torsion and free quotient, although it exists on the curve, is neither needed nor claimed canonical.

Each L_t is tangent to the binary discriminant conic at the double-root point q=2t. The phrase 'tangent line' here concerns that discriminant conic in the negative-quadratic parameter plane, not the positive invariant conic.

## 3. The local root-jet module, including the double-root point

Choose a local coordinate z on T at an exceptional point t. A local torsion summand of C_lin is O_T/(z^e), with its actual one-dimensional generator character retained. The tensor factor O_T(1) in (1) is also retained; it is locally trivial for the following algebra description but cannot be discarded from the equivariant identity.

Write the universal quadratic near t as

    q(z)=a+bz+cz^2.

On a root chart the transformed module is

    J_e = O_P[z]/(z^e, a+bz+cz^2).                    (4)

This is the finite pushforward of the actual pulled-back torsion summand, not an unrelated module with the same support.

For e=1, (4) is O_P/(a), the structure sheaf of L_t, tensor the fixed coefficient line from T_lin(1)|t.

For e=2, the module has generators 1,z and relations a+bz=0 and az=0. Thus its local presentation is

             [ a  0 ]
    O_P^2 -- [ b  a ] --> O_P^2 -> J_2 -> 0.          (5)

At a generic point of L_t, b is a unit. The module is then cyclic and isomorphic to O_P/(a^2). At the double-root point 2t, both a and b vanish, so its fiber needs two generators. It must not be replaced everywhere by the structure sheaf of a doubled line without tracking this special behavior.

The alternative length-two local torsion type O/(z) directsum O/(z) transforms instead into two copies of O_Lt, with their coefficient characters. These two torsion types have the same cycle multiplicity along L_t but different generic fiber jumps.

T_lin is a direct sum of its point-supported pieces. Formula (1) preserves that direct sum. Thus intersections of different exceptional lines are handled by the direct sum of the corresponding modules; no unexplained gluing term is introduced at q=t_i+t_j.

## 4. Exact bookkeeping for the possible jumps

At a simple root t the local summand O/(z^e) contributes one additional section, irrespective of e>=1. At a doubled root 2t it contributes min(e,2) additional sections. More generally the contribution for a root of multiplicity m is min(e,m).

One way to see this is the exact hyperplane base-change sequence over the DVR, now with quotient O/(z^m). The extra term is

    Tor_1(O/(z^e),O/(z^m)),

which has length min(e,m). The generic square bundle contributes three times the root length. The conductor sequence preserves odd cohomology, so summing over the root scheme gives

    h0(B_Dq(4))_- = 6 + sum_{t,a} min(e_{t,a},m_t),    (6)

where e_{t,a} are the elementary-divisor exponents of T_lin at t and m_t is the multiplicity of t in q. Terms from nonexceptional roots are zero. The right side concerns the actual sheaf on D_q, including double hyperplanes; no smoothness of D_q is assumed.

In particular, distinct good roots and doubled good roots both give exactly six. Two distinct exceptional roots give two separate fiber-excess contributions. A doubled exceptional root has excess equal to its local torsion length j, which can differ from the excess at a simple occurrence of that root.

The dual dimension is h1(B_Dq(4))_-=h0(B_Dq(4))_-+4, from the actual ambient 44-to-48 presentation and H2(B(2))=0. This is consistent with the same target sheaf C_quad in (1).

## 5. Numerical invariants and remaining question

The free quotient F_lin has degree26-12j. The root transform nu_*eta*(F_lin(1)) has rank ten and first Chern class (26-12j)h. The transformed torsion contributes 12j h, so c1(C_quad)=26h, as obtained independently from the global multiplication complex.

None of these formulas determines j, its elementary divisors, or the rank of the positive-normal smoothing map. They identify the actual target and its possible exceptional structure while preserving the global twists and the distinction between torsion length and individual fiber cohomology.
