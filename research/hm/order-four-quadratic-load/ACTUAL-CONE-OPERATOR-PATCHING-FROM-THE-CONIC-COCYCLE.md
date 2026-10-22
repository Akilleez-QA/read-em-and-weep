# Exact cone-operator patching from the actual conic cocycle

## Result and limitation

For the same uniform square input a=t²,h=X²Y², the homogeneous cone operator can be patched explicitly through the actual conic Serre cocycle. This constructs a genuine trace-free adjoint operator on the ACTUAL cone bundle with the prescribed symbol and physical section-line scalar. It incorporates the higher-cover correction to the connection instead of pretending that the homogeneous connection already glues on the actual bundle.

The result identifies ONE such cone operator, not necessarily the fixed ambient-probe operator. The latter comparison has a precise remaining freedom: global ell N with ell in H0(O_X(2)). No q-normal connection, midpoint extension to 3Q, endpoint comparison, or fourth-Bockstein value is supplied.

All A,B,c,lambda,k,rho_C remain unassigned symbolic parameters. This is a uniform tensor identity over the stabilizer orbit, not an actual-instance evaluation or rank test.

## 1. Finite gauge identity with no omitted quadratic terms

Use the old oriented nilpotent

    n=sigma sigma^t J0,   J0=[[0,-1],[1,0]],   n²=0.

The actual conic theorem uses N_C=-n, so its section-preserving frame change is

    S=I-t n,   S^(-1)=I+t n.

Let the homogeneous cone operator be H D+ad_A, with the natural determinant-line action retained, and suppose

    H Dn+[A,n]=Lambda n.

Its transformed connection is exactly

    S A S^(-1)-H(DS)S^(-1)
       =A+(H Dt+Lambda t)n.                              (1)

Indeed expansion gives the linear term t([A,n]+H Dn)+H Dt n and the quadratic term t²[-nAn+H(Dn)n]. Multiplying the preservation identity on the right by n gives H(Dn)n=nAn. Thus the entire quadratic term cancels. No small-t assumption is made.

This identity uses the actual scalar coefficient t in the chosen physical O(-2) frame. It does not set Dt=0 on the mistaken premise that t is an abstract Cech class.

## 2. The exact coefficient and its regular split

For the square input, in z=t/s coordinates the established cone data are

    a=z², h=X²Y², H=k z²h,
    D=2z² partial_z+z(X partial_X+Y partial_Y),
    u=-2kA X⁴z²/B-2kA X³Y/(Bc)-2k XY³z/c,
    Lambda=4zH-u,
    t=rho_C/z.

Here Lambda includes the natural determinant action; the physical section-line scalar is -u. Since t has positive-cover degree zero,

    Dt=-2rho_C,
    C:=H Dt+Lambda t=2rho_C H-rho_C u/z
      =2rho_C k[z²X²Y²+(A/B)zX⁴+(1/c)XY³
                              +(A/(Bc))X³Y/z].            (2)

The coefficient C is a physical O(2) section of cover degree four, so its coefficient bundle on L is O_L(2-4/2)=O_L(0). Therefore the additive scalar patching equation in common coefficient variables is exactly

    c_y-c_x=C.

A regular split is

    c_x=-2rho_C k[z²X²Y²+(A/B)zX⁴+(1/c)XY³],
    c_y=-2rho_C k A X³Y w/(Bc),   w=-1/z.                 (3)

Both expressions are regular on their full coefficient charts. Adding c_i n to the local homogeneous connection therefore provides the required actual conic correction, once the full root and determinant transport is checked.

## 3. Both the original and corrected full transports are checked

It is necessary to verify that the homogeneous operator itself glues on the homogeneous eigenextension; otherwise (2) would omit an additional old centralizer cocycle. The verifier performs this check independently from the cone section-line equations.

Specifically it recovers A in each regular chart from the actual cubic/quintic pair and scalar inverse. If sigma=(f,g), write A=[[b,c0],[d,-b]], with

    c0=-2ka² n_h,
    m=(H Df+c0 g)/f,
    b=Lambda/2-m,
    d=((Lambda-m)g-H Dg)/f.

These satisfy H Dsigma+A sigma=(Lambda/2)sigma. The actual n_h, u, regular targets, and their line factors are those already verified in ACTUAL-MIDPOINT-ABSOLUTE-SECTION-FOR-THE-FOURTH-SQUARE-INPUT.md; no new inverse or arbitrary source value is substituted.

Put z=Z². On root coordinates the global derivation becomes

    D_root=Z³ partial_Z+Z²(X partial_X+Y partial_Y).

Let P0 be the actual triangular/root-frame transition of the pure vertex eigenextension, as identified in ACTUAL-GLOBAL-SERRE-LIFT-FROM-THE-CONIC-COCYCLE.md. It has determinant Z^(-4), and the operator has physical O(4) weight Z^(-8). The full trace-free transport is

    A_y=Z^(-8) tf(P0 A_x P0^(-1)-H_x(D_root P0)P0^(-1)).  (4)

Here tf removes half the trace. This is the necessary determinant connection term, not a discarded scalar error. The verifier proves (4) exactly for the homogeneous connection in BOTH actual regular triangular charts.

Now set P_actual=P0 S_x and A_actual,i=A_i+c_i n_i. With the root-coordinate changes in c_y and n_y retained, it verifies the stronger full identity

    A_actual,y
       =Z^(-8) tf(P_actual A_actual,x P_actual^(-1)
                          -H_x(D_root P_actual)P_actual^(-1)).    (5)

Thus (3) really patches an operator on the actual cone bundle; it is not merely a formal additive split in a guessed coefficient line. The finite identity (1), both chart calculations, and the physical O(4)/determinant factors are independently included in the verifier.

The patching first constructs the operator on U=X minus C. The sheaf of first-order operators from the actual adjoint bundle to its O(4) twist is locally free: it is the Hom bundle from the first jet bundle. Reflexive Hartogs therefore extends this genuine operator uniquely across codimension-two C. Its prescribed scalar symbol, adjoint-derivation form, and determinant-normalized conditions extend as well, since they are bundle identities already holding on U. This is not an extension from an unverified homogeneous model.

Since n sigma=0 and [n,n]=0, this correction changes neither the prescribed section-line equation nor the nilpotent preservation equation. The physical scalar -u is unchanged. The root-frame determinant term in (4) transports Lambda correctly; omitting it would not.

## 4. Exact normalization freedom

Two trace-free cone operators with this same symbol and this same physical section-line action differ by a global trace-free endomorphism T satisfying T sigma=0. For a regular local pair f,g, the rows of T are syzygies of (f,g), hence have the form (alpha g,-alpha f) and (beta g,-beta f). Trace zero gives alpha g=beta f, so alpha=ell f and beta=ell g. Thus

    T=ell n.

The twist of T is O(4), whereas n is an End(G)(2) section. Therefore ell is a genuine section of O_X(2). This proves the exact remaining ambiguity

    H0(X,O_X(2)) n.                                      (6)

Within the cover-degree-four sector used in (3), two regular splits differ by Sym^4(Wprime) tensor H0(O_L(0)), of dimension five. The displayed Laurent split fixes that sector's common polynomial freedom. It does not independently fix all of (6) or compare the resulting operator to a chosen ambient fixed-probe normalization.

Consequently this note resolves cone-bundle patching and constructs a genuine prescribed-symbol operator, but it must not be used to identify a canonical ambient lower lift without that last normalization comparison. Nor does knowing the cone operator determine its q-order connection. The second-normal formula retains that separate connection through [K,t]+[K,n]_1.

## Reproduction

Run python verify_cone_operator_conic_patching.py. The script reruns the full actual Serre-lift checks, reconstructs both homogeneous cone connections, verifies (4), checks the exact finite identity (1), verifies the explicit coefficient and split (2)-(3), and checks the complete actual transport (5). Its calculations are universal symbolic identities, with no actual parameter assignment, rank, or scan. The regular-sequence proof of (6) is stated above; the script also checks its universal displayed kernel representative.
