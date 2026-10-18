## Inverses and split differentials

With unweighted frames

    U0=(gamma,I,H1 W), Q0=(H0;P;L delta),
    U1=(W,eta), Q1=(L;ev),

one obtains

    U0Q0 = gamma H0 + IP + H1 WL delta
          = gamma H0 + IP + H1 delta - H1 eta ev delta = Id15,
    U1Q1 = WL + eta ev = Id10.

The direct 3x3 Q0U0 block multiplication has diagonal blocks Id5, Id2, and L(delta H1)W=Id8; the off-diagonal blocks vanish by the displayed premises and delta gamma=0. Likewise Q1U1 has diagonal Id8,Id2 and zero off-diagonals. These formal word reductions are checked without actual matrix construction.

Define diagonal column weights

    S0=diag(nu^-2 Id5, 1, nu^-2, nu^2 Id8),
    S1=diag(Id8,nu^2 Id2).

Then U0phys=U0 S0, U1phys=U1 S1, with inverses S0^-1 Q0 and S1^-1 Q1. The two cohomology columns have DIFFERENT weights: first 1, second nu^-2. Replacing them with a common weight would change the connection.

For the scaled differentials nu^-2 gamma, nu^-2 delta, nu^-2 ev, the first is the first five columns of U0phys. The second sends the last eight columns of U0phys to the first eight columns W of U1phys and kills the other columns. The third sends the last two columns nu^2 eta of U1phys to Id2 and kills W. Thus the splitting differential is constant under these same premises, with extreme frames Id5 and Id2.

## Differentiation and exact block formulas

Lines 147–149 multiply columns of U by w[j], divide rows of Q by w[i], differentiate the weighted U, multiply in the order D(Uphys)Qphys, and negate. They do not differentiate Q and do not use Q D(U). For any diagonal S with invertible scalar entries,

    -D(US) S^-1 Q = -(DU)Q - U diag(Dw_j/w_j)Q.

This is a Leibniz identity, independent of UQ=Id. Invertibility is used only to identify Qphys as the geometric inverse. It follows that the resulting connection is flat in the split basis: D(Uphys)+[-D(Uphys)Qphys]Uphys=0. Subtracting the old connection gives B, rather than the split connection itself.

Write rho=D(nu)/nu and alpha=alpha_o(D). Let E22=diag(0,1) in the two cohomology coordinates. The literal output is

    rank 5,  k=-1: B_-1 = +alpha Id5;
    rank 15, k= 1: B_0 = -(DU0)Q0
                           +2rho gamma H0 +2rho I E22 P
                           -2rho H1 W L delta -alpha Id15;
    rank 10, k= 3: B_1 = -(DU1)Q1 -2rho eta ev -3alpha Id10;
    rank 2,  k= 5: B_2 = -5alpha Id2.

By H1 eta=0, H1WLdelta=H1delta, so the rank-15 formula admits that simplification. No derivative is omitted from DU0 or DU1: in particular D(H1W) and D(eta) retain their product/quotient contributions. The rank-5 plus sign is forced by subtracting k alpha with k=-1; the rank-2 term is not zero merely because its moving basis is the identity.

On the finite curve y_i²=x_i³-x_i, V_d x_i=delta_di y_i and V_d y_i=delta_di(3x_i²-1)/2. For mask m and nu=product_i(y_i/x_i)^m_i,

    rho = m_d y_d (x_d²+1)/(2x_d(x_d²-1)),
    alpha = m_d y_d/(x_d(x_d²-1)).

The former is the logarithmic derivative of nu, the latter the old connection from first-order-source.md §1. Their distinct numerators are essential. The code's line 151 equals alpha; it does not erroneously substitute rho. At infinity this statement refers to the same rational connection after authorized coordinate transport, not to a newly zero connection; this report does not audit that transport.
