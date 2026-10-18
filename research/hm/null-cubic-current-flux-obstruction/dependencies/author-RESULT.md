# Cubic-current flux ansatz: exact dual incompatibility certificate

## Result

The specified universal multilinear cubic-current ansatz is **inconsistent**:

    M2 = sum_(a=1)^4 V_a F_a + R4

has no solution when F_a is a rational linear combination of cubic invariant vector expressions in the three axes other than a, each axis appearing once, with arbitrary L/U choices, and R4 contains currents only. Nested brackets do not enlarge this ansatz in rank two. The conclusion is restricted to this ansatz; it is not a general nonexistence or nonzero-residue theorem.

A dual functional supported on eight independent jet-tensor coefficients annihilates every allowed cubic-flux divergence, but evaluates to 1/8 on M2. This is a fully explicit certificate, independent of the reported elimination rank.

## Input and exact transport

The sole mathematical input is `dependencies/RESULT.md`, SHA256

    2b07d868ec9c1fc5e38503623a8556ff7b3c71e3df76c3550385560602584db5

Use its fixed first-row frame, d(X,Y)=tr(XY), T=L+U, and literally A-transported B currents and jets. The physical derivative identities are

    V_a L_b = H_ab - [L_a,L_b]/2,
    V_a U_b = J_ab - [L_a,U_b] - [U_a,U_b]/2.

H_ab=H_ba and J_ab=J_ba. In particular the moving-transport term -[L_a,U_b] is retained. For this obstruction it suffices to project onto terms linear in H or J: every displayed commutator instead produces a quartic-current term after differentiating a cubic flux. This projection does not set those commutators to zero in the physical identity.

Set N=8M2. The target used is the entire supplied expression

    N = sum_e e {
       a_ab H_cd + b_cd J_ab
       - d(U_a,H_cd)L_b + d(U_b,H_cd)U_a
       - d(T_a,H_cd)U_b
       - d(J_ab,L_c)U_d - d(J_ab,L_d)U_c },

    a_ab = d(L_a,U_b)+d(U_a,L_b)+d(U_a,U_b),
    b_cd = d(L_c,L_d)+d(L_c,U_d)+d(U_c,L_d),

with precisely the four signed entries

    (a,b,c,d,e) = (1,3,2,4,+1), (1,4,2,3,-1),
                  (2,3,1,4,-1), (2,4,1,3,+1).

No full S4 alternation, jet family omission, or central-term manipulation is made.

## Completeness of the finite ansatz

For each axis a choose L or U at each of the three remaining axes. For each of the resulting eight choices X,Y,Z, use the three columns

    d(X,Y)Z, d(X,Z)Y, d(Y,Z)X

in F_a. This gives 4*8*3=96 columns. Rank-two identities reduce every requested nested bracket to this span:

    [[X,Y],Z] = 2(d(Y,Z)X-d(X,Z)Y).

Other bracket nestings reduce by antisymmetry and Jacobi. Thus including separate nested-bracket unknowns would only duplicate this column span.

The target rows are indexed by a symmetric jet axis pair (six choices), jet type H/J (two), the current type at each remaining axis (four), and one of three invariant tensor placements: 6*2*4*3=144 rows. For a fixed variable support these three tensor placements are independent. Indeed for a nondegenerate invariant form on the three-dimensional traceless rank-two space, contracting their rank-four tensors using the inverse form gives a Gram matrix with diagonal 9 and off-diagonal 3, whose eigenvalues are 15,6,6. Different formal supports are independently graded. This is a tensor argument, not an evaluation of physical currents or jets.

## Eight-row certificate

For a formal jet-current expression P, let [d(X,Y)Z]P denote its coefficient in the preceding invariant tensor basis. Define

    Lambda(P) =
        [d(L3,U1)H24]P
      + [d(L1,U3)H24]P
      + [d(J13,L2)L4]P
      - [d(H12,U3)L4]P
      - [d(H23,U1)L4]P
      + [d(J13,L4)L2]P
      - [d(H14,U3)L2]P
      - [d(H34,U1)L2]P.

The corresponding coefficients in N, in this order, are

    1, 1, 0, 0, 1, 0, 0, 0.

Consequently

    Lambda(N)=1,             Lambda(M2)=1/8.

The positive coefficient of d(H23,U1)L4 arises from the negative signed (a,b,c,d)=(1,4,2,3) entry, specifically -d(U_a,H_cd)L_b. The two positive H24-output coefficients arise from a_13 H24. All other listed target coefficients are absent.

To verify annihilation without trusting a solver, enumerate the only eight columns meeting this support. Each line below gives a cubic flux column and its two certificate contributions, +1 and -1:

    V1 d(L4,U3)L2:  +d(J13,L4)L2, -d(H14,U3)L2
    V1 d(L2,U3)L4:  +d(J13,L2)L4, -d(H12,U3)L4
    V2 d(L1,U3)L4:  +d(L1,U3)H24, -d(H12,U3)L4
    V2 d(L3,U1)L4:  +d(L3,U1)H24, -d(H23,U1)L4
    V3 d(L4,U1)L2:  +d(J13,L4)L2, -d(H34,U1)L2
    V3 d(L2,U1)L4:  +d(J13,L2)L4, -d(H23,U1)L4
    V4 d(L1,U3)L2:  +d(L1,U3)H24, -d(H14,U3)L2
    V4 d(L3,U1)L2:  +d(L3,U1)H24, -d(H34,U1)L2.

The minus signs in this table are Lambda's weights, not derivative coefficients. All other columns contribute zero. Therefore Lambda(sum_a V_a F_a)=0 on the jet-linear projection for every allowed F. A quartic-current R4 has no jet-linear component and also pairs to zero. This contradicts Lambda(M2)=1/8.

## What this does and does not establish

The precise cubic-flux proposal cannot remove all of M2's jets. This does not preclude fluxes with jets, other derivative orders or axis supports, non-polynomial/non-universal coefficients, additional source families, or cancellation after all terms of the actual target are combined. It does not determine any actual source value, residue, pole domain, cohomology class, or closure property.

The pre-existing identity and all its terms remain intact:

    R_alg = Q4 + sum_a nabla^P_a Phi_a + C4 + M2.

No new ordinary cubic flux is available in the tested ansatz. In particular the existing nonconstant dual-kernel derivative must remain. With K(X)=d(W,X), P_a=L_a/2, the supplied weighted formula still reads

    K(R_alg) = sum_a V_a K(Phi_a)
             + K(Q4+C4+M2)
             - sum_a K_;a^P(Phi_a),

    K_;a^P(X)=d(V_a W+[L_a/2,W],X).

This retains the full derivative of every coefficient, weight, test, HPL factor, selector and prescribed transpose represented by W. Even a hypothetical ordinary cubic flux identity would give a separate -sum_a K_;a(F_a) term, with K_;a(X)=V_a(K(X))-K(V_a X); it could not license a constant-kernel simplification. No K, W, source, owner or jet values are constructed or evaluated here.

## Reproduction

`solve.py` uses only Python's standard library, exact Fraction arithmetic, formal labels, and sparse linear algebra. It expands all four signs of N, differentiates all 96 basis columns in the jet-linear projection, and tracks exact row operations. It verifies the certificate against every column and the full target with explicit exceptions (not assert statements). Output reports 144 rows, 96 columns, rank 94, and inconsistency. `certificate.json` contains the eight rows and weights in machine-readable form. `CHECK.txt` records ordinary and optimized runs. The rank is supplementary; the displayed certificate itself proves inconsistency.

No actual model/source/owner/current/jet values, physical matrix-polynomial products, production imports, network access or external writes were used. All writes are restricted to the requested local output directory. This is the author's formal check; independent audit is separate.
