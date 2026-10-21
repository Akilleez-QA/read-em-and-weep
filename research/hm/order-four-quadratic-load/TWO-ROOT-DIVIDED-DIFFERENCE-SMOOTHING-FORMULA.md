# The actual two-root smoothing map as divided differences and Hermite jets

## Result

The actual six-to-ten first smoothing obstruction admits a coefficient-free formula in terms of the moving hyperplane square bundle and the relative plane-restriction boundary. Both its cross-root and diagonal blocks are determined by this formula. The diagonal is a genuine derivative of the moving leading square, not an independently chosen map.

Choose an affine chart of the negative hyperplane pencil and write its equation as

    ell(z)=u+zv.

Let A=Sym^2 W. The actual moving square sections have leading plane map and ambient boundary map

    a(z):A -> S:=H0(B_R(3))=Sym^2 D,       degree<=6,
    k(z):A -> P0:=H1(B(2))_-,             degree<=5,
    mu_ell(z) k(z)=0.                                  (1)

Here a is the actual degree-six inclusion of A O_T(-6) into the constant plane section space, and k is the actual degree-five boundary syzygy of A O_T(-5). They are not maps chosen from their dimensions.

Let the monic root polynomial be

    P(z)=z^2-sigma1 z+sigma2,

so the corresponding actual negative quadratic is

    q_-=u^2+sigma1 uv+sigma2 v^2.

Represent a section of the rank-six root bundle A tensor K by c(z) modulo P. In the indicated local trivializations, put

    k(z)c(z)=P(z)G(z)+r0+zr1,
    a(z)c(z)=P(z)H(z)+b0+zb1.                          (2)

Then the quadratic source section has actual ambient boundary -r1. Write m_qplus for positive multiplication by q_+ on that ambient boundary, followed by projection to the actual cokernel. Its formula is exactly

    - delta_z(q_+ H(z)) restricted to Z=(P=0),         (3)

where delta_z is the relative boundary using the negative coordinate v:

    H0(B_R(5)) -> H1(B_Hz(4))_-.

SIGN CONVENTION. For the deformation D_s=(q_-+s q_+=0), GLOBAL-SMOOTHING-TO-WEIGHTED-THIRD.md defines d_gl by the gluing defect after substituting q_-=-s q_+. With its convention, d_gl=-m_qplus. Therefore (3), (8), and (14) below compute m_qplus; the signed deformation/Bockstein formulas are their negatives. In particular d_gl=+delta_z(q_+H(z)) on the natural root data. Both operators have exactly the same kernel. The earlier convention is retained, not silently changed.

The target is the actual root transform of this relative H1 sheaf. Formula (3) therefore retains its nonreduced root jets; it is not merely a pair of values at distinct roots.

Changing c by P h changes H by a h, whose image under delta_z after multiplication by q_+ is zero. Thus (3) is independent of the chosen representative. All affine-chart and frame changes agree because (3) is proved to equal the intrinsic positive ambient multiplication map; its conversion to the signed Bockstein is the minus sign just specified. Globally the map is

    (A tensor K) tensor Sym^2 V* tensor O_P(1)
       -> C_quad,

or, for a fixed q_+, A tensor K -> C_quad(-1). The displayed local formula has trivialized that tautological line, not removed it.

No injectivity or other rank assertion about this operator is made.

## 1. Actual moving sections and their line factors

Let E3=pi_*B_H(3)=A O_T(-6), proved in EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md. Its leading plane restriction is an injection

    a:E3 -> S tensor O_T.

The actual hyperplane restriction sequence identifies E3 with the kernel of H1(B(2))_- O_T(-1)->H1(B(3))_+ O_T. After twisting by O_T(1), this is the degree-five inclusion k:A O_T(-5)->P0 tensor O_T.

There is also a concrete description of a requiring no HM coefficient evaluation. With D=Sym^4 W and the actual hyperplane two-space ell^3 W subset D,

    a(ell)(w1 w2)=(ell^3 w1) symmetric-product (ell^3 w2).

Thus a is the actual universal degree-six square map. The target boundary delta_z below retains the actual bundle geometry; it is not replaced by a generic map.

On an affine cover of P4, choose local lifts S_alpha(z;c) of the actual moving hyperplane section, linear in c in A. They may be chosen polynomial of degree at most six in z. Indeed the local universal lifting problem after twisting by O_T(6) has kernel O_T(5), whose H1 is zero. Choose the boundary sign convention

    S_beta(z;c)-S_alpha(z;c)=ell(z) k_alpha,beta(z;c). (4)

The cocycle k represents the actual boundary in (1) and has degree at most five. Restricting the lifts to R gives a(z)c.

## 2. Cross-root and diagonal blocks directly from the boundary

Fix two distinct parameters r,s. Write rho_r for restriction of ambient cohomology to H_r, and let delta_r be the plane boundary using v. Restricting (4) at z=s to H_r gives

    rho_r(k(s)c)=delta_r(a(s)c)/(s-r),                (5)

because ell(s)|H_r=(s-r)v. Since a(r)c extends to H_r, delta_r(a(r)c)=0, and (5) may equivalently use the first divided difference

    rho_r(k(s)c)=delta_r((a(s)c-a(r)c)/(s-r)).         (6)

The diagonal formula follows by differentiating the actual family (4), not by assigning a limit to an unrelated matrix. At z=r,

    Delta S'_alpha = v k(r)+ell(r)k'(r).

Restricting to H_r gives

    rho_r(k(r)c)=delta_r(a'(r)c).                     (7)

Multiplication by the positive quadratic commutes with these actual connecting maps. The target-twist-four versions of (6)-(7) are consequently obtained by inserting q_+ inside delta_r.

If the extension of a fixed moving section is changed, its derivative at r changes by the leading restriction of an actual section on H_r. Such a term, also after multiplication by q_+, is killed by delta_r. Thus the diagonal block is intrinsic. Equivalently it is the second fundamental map of the subbundle E3 subset S O_T, composed with the relative boundary; no connection on E3 or on the target is chosen.

For source coordinates taken in the ambient boundary basis

    k(r)c_r+k(s)c_s,

the two target components are explicitly

    delta_r(q_+[a'(r)c_r+(a(s)c_s-a(r)c_s)/(s-r)]),
    delta_s(q_+[(a(r)c_r-a(s)c_r)/(r-s)+a'(s)c_s]).     (8)

These are all four blocks of m_qplus. The four blocks of d_gl are their negatives. Formula (8) uses ambient boundary coordinates. They differ by the complementary-root normal factors from the natural values of c in the root bundle, as made explicit next.

## 3. Natural root coordinates and the quadratic source boundary

The odd section on H_z is the negative normal coordinate times its even square section. On the present affine chart the normal coordinate is v, so root data c(z) gives

    v S_alpha(z;c(z)) on the root family.

Divide the polynomial local lift and its boundary by P:

    S_alpha(z;c(z))=P H_alpha+F_alpha,0+zF_alpha,1,
    k_alpha,beta(z;c(z))=P G_alpha,beta+r_alpha,beta,0+zr_alpha,beta,1.

Polynomial division of (4) gives

    Delta F0 = u r0-sigma2 v r1,
    Delta F1 = v r0+u r1+sigma1 v r1,
    Delta H_alpha = ell(z) G_alpha,beta+v r1.          (9)

Define local lifts of a section on the actual quadratic D by

    V_alpha=v F_alpha,0-u F_alpha,1.

Their differences are exactly

    Delta V_alpha=-(u^2+sigma1 uv+sigma2 v^2)r1
                 =-q_- r1.                           (10)

Also, on H_z with P(z)=0, the relation u=-zv gives

    V_alpha|H_z=v(F_alpha,0+zF_alpha,1)
                  =v S_alpha(z;c(z)).

Thus these are the actual root sections, including a nonreduced root scheme, and (10) proves that their quadratic restriction boundary is -r1.

For distinct roots, if c_r=c(r) and c_s=c(s), this boundary is

    -(k(s)c_s-k(r)c_r)/(s-r).                         (11)

This is the normalization appropriate to root values. In contrast, the boundary coordinates in (8) correspond to root values (s-r)c_r and (r-s)c_s. Retaining this factor is essential; a naive identification of the two source coordinate systems would give incorrect blocks.

## 4. Direct proof of the quotient formula, including double roots

The last identity in (9), restricted to the whole root family H_z with P(z)=0, gives

    Delta(H_alpha|H_z)=v(r1|H_z).

The plane restriction of H_alpha is the quotient H(z) in (2). Hence the actual relative connecting map satisfies

    delta_z(H(z))=rho_z(r1).                          (12)

Multiplying (12) by q_+, and using the quadratic boundary -r1 from (10), proves (3). This proof takes place over the entire root scheme. It does not extend an equality merely by comparing distinct-root fibers and does not identify the target with a split pair at a double root.

The map delta_z is the genuine relative boundary of

    0 -> B_Hz(4) --v--> B_Hz(5) -> B_R(5) -> 0

on the affine pencil. It is consequently a sheaf morphism into the actual relative R1 sheaf, and may be pulled back to a nonreduced root scheme. The target identity

    C_quad=nu_*eta*(C_lin(1))

from QUADRATIC-TARGET-FROM-HYPERPLANE-TORSION.md supplies its correct global interpretation, including possible exceptional torsion.

## 5. Divided differences and full Hermite form

For distinct roots r,s, put F(z)=a(z)c(z) and d=s-r. Evaluating the quotient H at the roots gives

    H(r)=[F(s)-F(r)-d F'(r)]/d^2 = F[r,r,s],
    H(s)=[F(r)-F(s)+d F'(s)]/d^2 = F[r,s,s].          (13)

Thus the actual root-normalized positive multiplication map m_qplus is

    (-delta_r(q_+ F[r,r,s]),
     -delta_s(q_+ F[r,s,s])).                         (14)

Terms in F' arising from differentiating c multiply a(r) or a(s) and are annihilated by the appropriate boundary, in agreement with (8).

For a double root, write P=(z-t)^2 and choose c(z)=c0+c1(z-t). The quadratic source boundary is

    -k'(t)c0-k(t)c1.                                  (15)

Modulo (z-t)^2, the quotient in (2) is

    H(z) = [a''(t)c0/2+a'(t)c1]
         +(z-t)[a'''(t)c0/6+a''(t)c1/2].              (16)

The full positive multiplication map m_qplus is still -delta_z(q_+H(z)) on that dual-number root scheme; the signed deformation obstruction d_gl is +delta_z(q_+H(z)). In particular the value at t is the boundary of the first bracket in (16), but the second target jet also involves the variation of the relative boundary itself. There is no canonical replacement by two independent constant target spaces. Formula (16) followed by the actual relative delta retains this variation automatically.

Equations (15)-(16) are an exact Hermite interpretation, not a smooth-quadric claim for a doubled negative root: adding only a positive block to a double negative block leaves a singular quadric. The global normal-direction operator nevertheless remains well-defined there.

## 6. Choice independence and line twists

Changing the root representative to c+P h changes the quotient H to H+a h. The actual relative boundary kills q_+a h as a sheaf identity because it is the plane restriction of q_+ times a moving hyperplane section. This remains true on a double root, including its derivative component. Thus the representative ambiguity is completely removed.

Changing the local ambient lifts changes the cocycles only by the corresponding actual restriction coboundaries. Changing a local frame of the moving square bundle changes a and c inversely. Finally, changing the affine pencil or its normal-coordinate frame changes the local formulas according to the tautological source and target lines, because the direct Čech calculation identifies each formula with the same intrinsic multiplication map.

More explicitly, at a hyperplane equation line L_z subset W, its negative normal-coordinate line is W/L_z. The source branch is

    E3_z tensor (W/L_z),

not E3_z alone. For two distinct roots, the complementary equation line maps isomorphically onto this quotient. The product of the two equation lines is the tautological negative-quadratic line. Globally, therefore, the intrinsic positive normal-direction map is

    (A tensor K) tensor (Sym^2 V* tensor O_P(1))
      -> C_quad.

The O_P(1) cancels the tautological O_P(-1) in the ambient source H1(B(2))_- O_P(-1). Formula (3) is its affine trivialization. No constant or parameter-line factor is being dropped to identify separate presentations.

## Scope

This gives an actual operator, including its diagonal derivative, cross-root divided differences, source normalization, and full double-root Hermite interpretation. It does not determine its kernel. The actual plane boundary still contains the required bundle-extension information; the formula does not set higher normal transition terms to zero or replace them by dimension counts. No actual HM coefficients, multiplication matrices, or ranks were evaluated.
