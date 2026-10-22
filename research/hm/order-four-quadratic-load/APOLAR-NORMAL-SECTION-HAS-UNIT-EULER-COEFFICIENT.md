# The apolar normal class acting on the section has unit Euler coefficient

## Result

For the normalized apolar lowest normal cocycle eta_8 whose diagonal Euler coefficient is FOUR, the class of eta_8 sigma in the scalar Euler channel of H1(U,G(-2)) has coefficient ONE:

    [eta_8 sigma]=[sigma/z].                       (1)

This is obtained after retaining compatible regular Serre lifts of its nonzero wedge quotient. Merely multiplying the diagonal by sigma would give the wrong coefficient.

The calculation is universal in unassigned nonzero A,B,c,lambda. It uses the actual marked vertex eigenextension, its regular quintic targets, the full apolar cocycle and its compatible scalar shadows. The actual normal generator is c_eta times this normalized cocycle, with c_eta still unknown and nonzero. The actual conic marking is not reset, and no ambient second-normal lift or fourth obstruction is evaluated.

## 1. Physical coefficient lines and exact reduction

Use f,g,p_x,p_y^x, eta_8, n_x,n_y^x from ACTUAL-LOWEST-NORMAL-CLASS-HAS-AN-APOLAR-REPRESENTATIVE.md and its verifier, with

    sigma_x=(f,g_x),   g_x=g+p_x f,
    eta_x=[[d_eta,0],[r_eta+2p_x d_eta,-d_eta]],
    n_y^x-n_x=q(eta_x),
    d_eta=4/z+1/(d z^6)-d z^4,   d=Bc^2/A.

The wedge convention is sigma wedge v=f v2-g_x v1. Directly,

    sigma wedge(eta_x sigma)=-q(eta_x)=-delta n.

Thus choose regular local V_i satisfying

    sigma_i wedge V_i=-n_i.                        (2)

The relevant sequence for G(-2) is

    0 -> O_L(-2) --sigma--> (G(-2))_8
      -> I_Z(0)_8=Sym^8(Wprime) O_L(-4) -> 0.      (3)

The component degrees of V_i are three and five. From the marked vertex frame lines O(9/2),O(-5/2), their coefficient lines are

    O(9/2-2-3/2)=O(1),
    O(-5/2-2-5/2)=O(-7).

Consequently the full y-to-x transport is

    V_y^x=P(p_x-p_y^x) diag(z,z^-7) V_y(-1/z),
    P(p)=[[1,0],[p,1]],   w=-1/z.                 (4)

The shadow is physical twist zero, degree eight, hence O(-4), so the y lift is n_y=z^4 n_y^x after substitution. These line factors are essential for (1).

The invariant H1 of the quotient in (3) is zero, as in the actual lowest normal-class argument. Moreover H0 of that entire quotient is zero because its base line is O(-4). Hence the invariant scalar Euler channel is unambiguously identified by (3). The explicit cochain calculation below realizes that identification rather than relying solely on its dimension.

## 2. Explicit regular lifts

A finite exact construction works in each chart. Take j with j g_i=1 modulo f_i in the polynomial ring in X over the field of all remaining UNASSIGNED variables, and set

    v1=rem(n_i j,f_i),
    v2=(g_i v1-n_i)/f_i.

Then f_i v2-g_i v1=-n_i identically. Temporary denominators are removed by adding sigma_i times a scalar; this does not change the wedge.

For the x chart the required scalar addition is -2/z. For the y chart it is -1/w. The complete raw first components, before these additions, are

    v1,x=Y(2A X^2+Bc XYz^3+B Y^2z)/z,
    v1,y=Y(2A X^2w^3-Bc XY-B Y^2w^2)/w.

After the scalar additions the COMPLETE regular lifts are

    V_x=( -2Ac X^3z+3Bc XY^2z^2-BY^3,
          -Bc lambda X^3Y^2/(2A)+3B^2c lambda XY^4z/A^2 ),

    V_y=( Ac X^3+3A X^2Yw^2-2B Y^3w,
          3A lambda X^4Yw/(Bc^2)-lambda X^2Y^3/(2c^2) ).

The verifier checks these complete final V_x,V_y and proves that ALL their entries are polynomial in the base chart coordinate and both positive variables. Thus the temporary coefficient-field inversion introduces no unresolved positive-variable or base poles.

It also verifies (2) in both charts, before forming a cohomology quotient.

## 3. The scalar cochain and its exact regular splitting

Using (4), the entire vector residual is

    eta_x sigma_x - V_y^x + V_x = sigma_x r,
    r=1/z+1/(d z^6)-d z^4.                       (5)

Both components of (5) are checked exactly. In particular r has no positive-variable dependence.

Define regular scalar cochains for O(-2) by

    r_x=d z^4,       r_y=w^4/d.

Then the volume-compatible coordinate w=-1/z gives

    r=1/z+z^-2 r_y(-1/z)-r_x.                    (6)

The two additional terms in (5) are therefore a genuine regular scalar coboundary. Equation (6) proves (1), with normalized coefficient exactly one. This coefficient is not the uncorrected diagonal coefficient four: the regular Serre lifts supply the other three units.

## 4. Bracket convention and the retained actual normalization

With J=[[0,-1],[1,0]], put

    n=sigma sigma^T J,
    tau(v)=sigma v^T J+v sigma^T J.

The verifier proves directly

    [eta,n]=tau(eta sigma),      tau(sigma)=2n.

Thus, in this explicitly marked nilpotent convention, the scalar reduction of the bracket is 2[n/z]. A different pre-existing sign or scale in the symbol N must be transported; it is not silently identified with n.

For the actual normal generator the lowest scalar Euler coefficient is c_eta, not an asserted absolute number one. The actual conic extension is already fixed, and its corrections raise the weighted degree by eight, so they do not alter this lowest scalar reduction. Restriction to U does not license replacing the global actual bundle by a different conic extension.

If a separately fixed global class xi in H1(B_Q) has unique preimage xi_G under tau, and xi_G restricts in this same marking as kappa[sigma/z] in H1(G(-2)), then (1) gives the comparison c_eta/kappa. Equivalently xi restricts as kappa tau([sigma/z]); in the stated nilpotent marking tau([sigma/z])=2[n/z]. This note determines neither that pre-existing conic-marked kappa nor an ambient normal displacement. It provides the exact normalized comparison leg needed to compare them, without choosing either to equal one.

## Reproduction

Run python verify_apolar_normal_section_euler.py. It imports the exact actual apolar reconstruction, constructs both regular wedge lifts, checks their complete target transport, proves (5) and (6), and checks the bracket marking. All parameters stay unassigned; no actual-instance rank, selected coefficient, or ambient second-normal lift is used. Frozen sources are unchanged.
