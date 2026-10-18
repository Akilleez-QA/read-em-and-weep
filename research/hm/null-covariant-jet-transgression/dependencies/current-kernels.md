# Complete selected trace-free M0 in current coordinates

## Scope

This is a complete formal formula for the 00 and 10 entries of the trace-free, scalar-free, full-gerbe baseline M0. It uses physical first currents and trace-free normalized second jets, with row composition G=BA. It does not evaluate any HM source polynomial or claim that the new input representation is cheaper to construct. The second-jet survivor from `m0-second-jet-survivor.md` remains present.

## 1. Inputs and Lie operations

All first currents are traceless:

    L_i=A^(-1)D_i A,
    U_i=A^(-1)B^(-1)(D_i B)A,        i=1,2,3,4.

In this note H and J denote already trace-free normalized second jets:

    H_ij=(A^(-1)D_iD_j A)^0,
    J_ij=(A^(-1)B^(-1)(D_iD_j B)A)^0,
                      ij in {13,14,23,24}.

These are physical derivatives, including all endpoint/frame derivatives. Distinct derivative indices commute as in the pinned formula. No ordinary derivative of a moving stripped frame is substituted. Put

    K_12=[L_1,L_2]/4,       K_34=[L_3,L_4]/4,
    X_12=[U_1,U_2]/4,       X_34=[U_3,U_4]/4,
    T_i=L_i+U_i,
    K^G_12=[T_1,T_2]/4,     K^G_34=[T_3,T_4]/4.

Thus K_r=k_r(A), X_r=A^(-1)k_r(B)A, and K^G_r=k_r(G).

For traceless matrices write d(V,W)=tr(VW), B(V,W)=[V,W]. Both use the physical matrices at the same first-endpoint frame. The useful exact identity is

    (V W Z)^0 = ( d(V,W)Z - d(V,Z)W + d(W,Z)V )/2.  (1)

## 2. Complementary k derivatives without constructing u derivatives

For r=(i,j) and c outside that pair, define

    Z_c,r = ( [H_ci,L_j]+[L_i,H_cj] )/4
                               -[L_c,K_r]/2,
    Y_c,r = ( [J_ci,U_j]+[U_i,J_cj] )/4
                               -[U_c,X_r]/2.       (2)

Indices on H,J may be sorted because their underlying mixed physical derivatives commute. These are exactly

    Z_c,r = D_c k_r(A),
    Y_c,r = A^(-1)(D_c k_r(B))A.

To prove this, differentiate K_r=[L_i,L_j]/4 and use

    (D_c L_i)^0=H_ci-[L_c,L_i]/2.

The two resulting nested-bracket terms combine by Jacobi:

    [[L_c,L_i],L_j]+[L_i,[L_c,L_j]]=[L_c,[L_i,L_j]].

The same proof applies before conjugating the B-edge derivative. In particular Y is NOT obtained by differentiating X while holding the conjugating A fixed; the definition in (2) already respects its precise transported derivative meaning. If one does differentiate X, then

    D_c X_r=Y_c,r+[X_r,L_c].

## 3. Exact sum of each pair of mu terms

For p=(a,b), let r be the complementary pair, set

    D_r=X_r-K_r,       S_r=X_r+K_r,

and define the following traceless matrix:

    Q_p(r) = (1/4) {
        d(U_a,D_r)L_b - d(U_b,D_r)L_a
        -(d(U_a,L_b)-d(U_b,L_a))D_r
        +d(L_b,S_r)U_a - d(L_a,S_r)U_b
        +[Y_a,r,L_b]-[Y_b,r,L_a]
        +[U_a,Z_b,r]-[U_b,Z_a,r]
    }.                                                   (3)

The bracket notation [Y_a,r,L_b] here means [Y_{a,r},L_b], and similarly for the other three terms.

Precisely, this is

    Q_p(r) = {G^(-1)[mu_p(B k_r(B),A)
                                  +mu_p(B,A k_r(A))]}^0.

For verification, before trace-free projection the expression is 1/2 times

    U_a X_r L_b-U_b X_r L_a
    +Y_a,r L_b-Y_b,r L_a
    +U_a L_b K_r-U_b L_a K_r
    +U_a Z_b,r-U_b Z_a,r.

Use (VW)^0=[V,W]/2 for the derivative terms and (1) for the cubic terms. For one ordered pair the two cubic terms combine to

    (U_a X_r L_b+U_a L_b K_r)^0
      = ( d(U_a,D_r)L_b-d(U_a,L_b)D_r
                               +d(L_b,S_r)U_a )/2.

Antisymmetrizing a,b gives (3), preserving each original mu factor 1/2.

## 3a. Exact nested-current cancellation: the preferred Q kernel

The derivative objects in (2) need not be constructed in full. Define only their normalized-second-jet portions:

    ZH_c,r = ([H_ci,L_j]+[L_i,H_cj])/4,
    YH_c,r = ([J_ci,U_j]+[U_i,J_cj])/4,
                                      r=(i,j).

Then the exact equivalent of (3) is

    Q_p(r) = (1/4) {
         d(U_a,X_r)L_b - d(U_b,X_r)L_a
         +d(L_b,K_r)U_a - d(L_a,K_r)U_b
         +[YH_a,r,L_b]-[YH_b,r,L_a]
         +[U_a,ZH_b,r]-[U_b,ZH_a,r]
    }.                                                   (3')

This is an actual algebraic cancellation, not an input-cost assumption. For traceless 2 by 2 matrices,

    [[U,X],L]=2(d(X,L)U-d(U,L)X),
    [U,[L,K]]=2(d(U,L)K-d(U,K)L).

Substitute Y=YH-[U,X]/2 and Z=ZH-[L,K]/2 into (3). Set Delta=d(U_a,L_b)-d(U_b,L_a). The correction to the four derivative brackets, inside the braces of (3), is

    -d(X_r,L_b)U_a+d(X_r,L_a)U_b
    +Delta(X_r-K_r)
    +d(U_a,K_r)L_b-d(U_b,K_r)L_a.

It cancels the -Delta D_r term completely, cancels the K_r portion in the first two D_r terms, and cancels the X_r portion in the last two S_r terms. The four remaining scalar-vector terms are exactly those in (3'). All second-jet bracket terms are retained. The independent algebraic check agrees on these signs and factors.

## 4. Mixed Moyal block and complete answer

For the four signed index pairs

    (ij,kl,epsilon) = (13,24,+1), (14,23,-1),
                      (23,14,-1), (24,13,+1),

define

    C = (1/8) sum epsilon {
          [J_ij,H_kl]
          +d(U_i,U_j)H_kl
          +d(L_k,L_l)J_ij
        }.                                                (4)

This is exactly the trace-free normalized mixed second-derivative block with its required original factor 1/4. Determinant one was used only through
tr(A^(-1)A_kl)=d(L_k,L_l) and its B-edge counterpart.

The COMPLETE result is

    M0^0 = ([X_12,K_34]+[X_34,K_12])/2
           + Q_12(34) + Q_34(12) + C
           - b_12 K^G_34 - b_34 K^G_12.                   (5)

Here b_12 and b_34 are the original pinned gerbe scalars. The raw central gerbe term -b_12 b_34 G becomes -b_12 b_34 I after multiplication by G^(-1), and only then has zero trace-free projection. The two noncentral gerbe terms remain exactly as displayed. Formula (5) is the baseline M0, not the larger closed Rsharp representative; the latter's F and scalar-derivative corrections are separate.

## 5. Explicit selected-coordinate kernels

Represent a traceless matrix V by (z_V,x_V,y_V), meaning

    V = [[z_V,x_V],[y_V,-z_V]].

Then the two requested entries are z for 00 and y for 10. The necessary kernels are

    d(V,W)=2 z_V z_W+x_V y_W+y_V x_W,

    [V,W]_z=x_V y_W-y_V x_W,
    [V,W]_x=2(z_V x_W-x_V z_W),
    [V,W]_y=2(y_V z_W-z_V y_W).

To implement the selected outputs, build all three coordinates of the four K/X matrices and the eight second-jet derivative portions YH/ZH in (3a). Thereafter apply only the z,y kernels to the quadratic brackets, derivative brackets in (3'), mixed brackets in (4), and K^G. Scalar-vector terms in (3')-(5) likewise need only z,y. The trace products in (3')-(4) use all three coordinates of their arguments.

This supplies exact remaining kernels and does not construct a full u=gk, a derivative of u, or the scalar trace part of any normalized second jet.

## 6. Conditional straight-line scalar-product schedule

Count one multiplication of two possibly nonconstant scalar inputs as one scalar product. Rational scalings and additions are not counted here. All 48 scalar current/trace-free-second-jet coordinates and b_12,b_34 are GIVEN opaque inputs; construction, owned denominator alignment, coefficients, and detector weights are outside this count.

A full bracket needs 6 scalar products; its selected z,y outputs need 4; d needs 3. One simple schedule has:

- Four full K/X brackets: 24 products.
- Eight full YH/ZH matrices, two full brackets each using (3a): 96 products.
- Two selected quadratic brackets in (5): 8 products.
- The cubic/trace part of both Q terms in (3'): 40 products. Per Q: four traces cost 12 and four selected scalar-vector products cost 8.
- The four selected derivative brackets per Q: 32 products total.
- Mixed block C: 56 products. Four selected brackets cost 16, eight traces cost 24, and eight selected scalar-vector products cost 16.
- Two selected K^G brackets: 8 products.
- Two selected noncentral gerbe products: 4 products.

Total: 268 conditional scalar products. The exact cancellation from (3) to (3') saves 64 products in this same opaque-input schedule: 48 from the omitted nested-current derivative brackets, 12 from two fewer traces per Q, and 4 from one fewer selected scalar-vector product per Q. If instead the four primitive q inputs are given and each b is constructed as its prescribed (15/4) times one q-product, add 2.

This is an upper bound for this deliberately simple opaque-input schedule, not a minimal circuit, not a count of physical polynomial multiplications, and not comparable to the prior 531-node circuit without pricing the different input contracts. No runtime/peak-byte certificate is asserted. An implementation still requires authenticated owned-denominator constructions for these current/H/J inputs and justified sharing or detector-specific demands.

## Dependency scope

Companion references are identified by basename. A referenced file not supplied with this collection or its support-certificate companion is an external prerequisite, not an embedded proof or a verified relative link. The reading order and unresolved conditions are listed in `proof-notes-index.md`. Reported test results describe the source audit; this proof copy does not by itself constitute a new test run.
