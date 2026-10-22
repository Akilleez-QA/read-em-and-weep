# Exact single-line realization of the ramification functional

## Scope and dependencies

Work over C with the determinant markings, nonzero monad-channel ratio c, bundle E=U tensor Lambda^2 ker(x), and ramification data of [PR678](https://github.com/Akilleez-QA/read-em-and-weep/blob/f47c81086e5bd17be4ba714e43fa7f6226d41beb/research/hm/ramification-family-target/PROOF.md). Use the complete cubic-transvection presentation of [PR676](https://github.com/Akilleez-QA/read-em-and-weep/blob/b7fd2c946b39301bdb226af362674e1b2e755097/research/hm/global-skew-middle-presentation/PROOF.md). All lines below are arbitrary ramification joining lines; no actual point or coefficient is evaluated.

The conclusion concerns one entire line at a time, not simultaneous interpolation over twelve lines. It does not impose the coupled monad-source equations or establish a Bockstein value, higher-order lift, or algebraicity.

## 1. A constant Lagrangian containing the regularized input

Fix a ramification pair with nonzero positive and negative covectors v,w. On its joining line use x=t v+s w. Put K0=ker(v) intersect ker(w), choose ev in V and ew in W with v(ev)=w(ew)=1, and put e(t,s)=s ev-t ew. Then

    F|L = K0 O direct-sum O(-1)e,
    E|L = N O direct-sum S O(-1),
    N=U tensor Lambda^2 K0, S=U tensor K0.

Both summands have rank six and are Lagrangian for beta:E tensor E -> O(-1): their self-pairings vanish, and their mutual pairing is perfect. For the moving summand, this follows because every two-form contains e; for the constant summand, Lambda^4 K0=0.

Write C=Cmix and B=Bmix. PR678 gives the regularized input

    Ytilde=sY=t^2 C-c s^2 B.

It lies in E at every (t:s). Contraction with t v+s w and comparison of the four cubic monomials shows i_v C=i_w C=i_v B=i_w B=0. Therefore C,B belong to N. Both are nonzero: at s=0, C is the C-channel image of nonzero z0, and at t=0, B is the B-channel image of nonzero u; the A-channel vanishes at the negative endpoint t=0. Fiberwise injectivity of the full left-monad arrow gives nonvanishing in each case. If C and B were proportional, their nonzero proportionality and c would yield a mixed (t:s), t s nonzero, with Ytilde=0. There Y is the full left-monad image of the nonzero source vector (-u/a_m,z/c_m), contradicting injectivity. Thus C and B are independent.

Equivalently, there is a direct homogeneous proof: the full left arrow sends the regularized source (-s u/a_m,t z0/c_m) to Ytilde. This source never vanishes on P1, so injectivity proves nonvanishing even at both endpoints.

In particular Ytilde is a nowhere-zero section of E(2). The injection O(-2)->N O has quotient O(2) direct-sum O^4: on span(C,B), its two coordinates t^2,-c s^2 have no common zero and determinant gives quotient O(2).

## 2. Removing the universal endpoint factor

Let lambda0 be the fixed VV Cartan functional attached to w, so lambda_(s w)=s^3 lambda0. It kills N: the mixed sector is killed by definition; the VV part is U tensor Lambda^2 ker(v), precisely the A(v,U) image, which lambda0 annihilates. The identity lambda Abar=0 on the entire projected A-image is pinned in section 2 of the [actual mixed-value argument](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/ACTUAL-RAMIFICATION-DETECTS-A-NONZERO-MIXED-FORM-MIDDLE-VALUE.md); here A(v,u)=u tensor i_v(tau), so A(v,U)=U tensor Lambda^2 ker(v). Intrinsically, under the marked Cartan identification the bicubic is F(r,w)=lambda_w(r^3). Ramification of the negative projection makes its positive derivative zero; together with F=0 and Euler homogeneity this gives lambda_w(r^2 uprime)=0 for every uprime in U. This is the whole projected A(v,U) image, not merely the special kernel vector u.

On the moving summand,

    lambda0(e(t,s) wedge k)=s lambda0(ev wedge k).

Including U, write this as lambda0|S O(-1)=s ell, for a constant nonzero row ell on S. Nonzeroness follows because VV projection E_x->U tensor Lambda^2 V is onto whenever s is nonzero, while lambda0 is a nonzero functional. Thus lambda0 divided by s defines a regular surjection E|L -> O(-1), zero on N.

A determinant-skew T:E|L->E|L(4) has a block D:N O->S O(3). Under the perfect pairing S=N*, this block is symmetric. The other blocks are invisible to the functional on Ytilde. Consequently

    lambda_(s w)(T Y)=s^3 ell(D(t,s)(t^2 C-c s^2 B)).             (1)

This proves the endpoint factor geometrically, without choosing a rational trivialization of beta.

## 3. Exact local image and kernel

For ell nonzero, the constant contraction map Sym^2 N* -> N*, D -> ell D, is onto. Equivalently, a symmetric bilinear form can be prescribed arbitrarily on one nonzero argument; extend that argument to a basis. Its kernel has dimension 15 and admits a constant linear complement.

Since C,B are independent, (1) divided by s^3 has the form

    t^2 f(t,s)-c s^2 g(t,s),

with f,g arbitrary binary cubics. The homogeneous ideal (t^2,s^2) contains every binary form of degree at least three. In particular these expressions fill H0(O(5)). At the bundle level the normalized functional is a surjection

    sp(E)(4)|L -> O(5).

Its kernel has splitting

    O(3)^19 direct-sum O(1) direct-sum O(4)^36 direct-sum O(5)^21. (2)

Indeed the symmetric block contributes 15 O(3) from row contraction, four O(3) from annihilating C and B, and O(1) from the sole syzygy (c s^2,t^2). The other two skew blocks are O(4)^36 and O(5)^21. All summands of (2) have vanishing H1. Hence the six-dimensional scalar image is exact, and the kernel on sections has dimension 384 in the 390-dimensional line-operator space.

## 4. Lifting to global operators, including vertex-zero lifts

Restriction of the constant Koszul generators U tensor Lambda^3 H onto H0(L,E(1)|L) is onto. In the decomposition H=K0 direct-sum span(ev,ew), the Lambda^3 K0 part is the kernel; Lambda^2 K0 tensor span(ev,ew) gives N tensor H0(O(1)); and K0 tensor Lambda^2 span(ev,ew) gives the constant S summand. Tensor U throughout. Thus its kernel has dimension two and its image dimension eighteen.

In particular every constant S section of E(1)|L has a global contraction lift with no N component on L: for k in K0, contraction of u tensor ev wedge ew wedge k is -u tensor e(t,s) wedge k, up to the common exterior sign convention. Transvections of these lifted sections, multiplied by arbitrary global cubics, realize exactly the desired symmetric block D on L and no other block there. Every binary cubic lifts from ambient P4. Therefore the normalized map from global twist-four skew operators onto H0(O(5)) is surjective.

There is a stronger lifting statement. Let Z=P(W*) be the entire negative vertex. A binary cubic divisible by t lifts to a global cubic in I_Z(3): choose a positive linear form restricting to t and lift the remaining binary quadratic. Therefore the same construction with f,g divisible by t gives global operators vanishing on the whole Z, and their normalized image is

    t (t^2,s^2) H0(O(2)) = t H0(O(4)).                         (3)

The equality follows since every degree-four monomial is divisible by t^2 or s^2. This is the full five-dimensional space of normalized quintics vanishing at the negative endpoint. Conversely, any operator vanishing on Z has normalized value q(0,1)=0, so (3) is the exact image of all vertex-zero operators, not only a lower bound from the constructed subfamily.

## 5. Center-even realization and the remaining global obstruction

Let J be the center. It preserves L and Z, acts as +1 on the mixed-input ambient sector, and as -1 on the VV-output sector (including the U factor). Thus JY(t,s)=Y(t,s), whereas Y(t,-s)=-Y(t,s), and lambda0 composed with J equals -lambda0. For F_T(t,s)=lambda_(s w)(T(t,s)Y(t,s)), direct substitution into (J.T)(x)=J T(Jx) J^(-1) gives F_(J.T)(t,s)=-F_T(t,-s). Writing F_T=s^3 q_T yields q_(J.T)(t,s)=q_T(t,-s). Therefore center-even operators give exactly the even-in-s binary quintic receiving subspace

    span(t s^4, t^3 s^2, t^5).

The scalar map is equivariant for this center action, as follows directly from the monad equivariance and lambda_(s w)=s^3 lambda0. Averaging a lift over the center is therefore the projector onto this receiving subspace; it preserves the condition of vanishing on Z. Each of these three monomials belongs to (3). Thus all three coefficients L1,L3,L5 on an individual ramification joining line are realized by center-even global skew operators vanishing along the entire negative vertex.

A linear right inverse can be written without selecting any actual numerical data. For prescribed coefficients alpha,beta,gamma choose dual rows a,b on N with a(C)=1,a(B)=0,b(C)=0,b(B)=1. Put f=gamma t^3+beta t s^2 and g=-(alpha/c)t s^2, and r=f a+g b. Let n_ell in N represent ell under S=N*, choose theta in N* with theta(n_ell)=1, and set

    Q_r=theta tensor r+r tensor theta-r(n_ell) theta tensor theta.

Then Q_r(n_ell,-)=r and r(Ytilde)=alpha t s^4+beta t^3 s^2+gamma t^5. Each coefficient of Q_r is a cubic divisible by t. Lift Q_r using the pure-S transvections and vertex-vanishing cubic lifts above, then average over the center. The output is unchanged. This is a structural right-inverse construction with arbitrary frame choices, not an evaluation of the actual source instance.

This eliminates a single-line globality/skewness/vertex obstruction, not the simultaneous twelve-line obstruction. Different lifts used for different lines need not have compatible restrictions on the others. Averaging over the full Gamma does not preserve a prescribed single-line value. Thus the image of the 1113-dimensional Gamma-equivariant parameter family in the eighteen simultaneous conditions remains undetermined. The next dependency is simultaneous operator interpolation, not scalar interpolation and not a local linewise failure.
