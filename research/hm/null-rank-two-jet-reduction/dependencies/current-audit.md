# Independent audit of complete current-coordinate M0

The complete formula in `m0-current-selected-kernels.md` is correct after correcting the schedule total from432 to332. All inputs remain physical first currents and tracefree normalized mixed second jets in the common first-endpoint frame.

For traceless V,W,Z, tf(VWZ)=(tr(VW)Z-tr(VZ)W+tr(WZ)V)/2. Differentiating K=[L_i,L_j]/4 and using tf(partial_c L_i)=H_ci-[L_c,L_i]/2 yields Z_c,r=([H_ci,L_j]+[L_i,H_cj])/4-[L_c,K_r]/2 by Jacobi. The corresponding B-edge identity gives Y_c,r with U,J,X. This is a transported derivative, not the derivative of X with its A-conjugation frozen; partial_c X=Y+[X,L_c].

The exact normalized mu pair before projection is

    ( (U_a X+Y_a)L_b-(U_b X+Y_b)L_a
          +U_a(L_b K+Z_b)-U_b(L_a K+Z_a) )/2.

Applying the triple identity to cubic terms and tf(VW)=[V,W]/2 to derivative terms gives the worker's overall1/4 grouping with D=X-K,S=X+K and all stated signs. The mixed Moyal block retains its four signs and original1/4 factor; determinant-one traces give its final1/8 expression. The quadratic term is([X12,K34]+[X34,K12])/2. Since G^-1 dG=L+U, the two noncentral gerbe terms are exactly-b12 K^G34-b34 K^G12. The central gerbe is removed only by exact tracefree projection.

The selected-coordinate bracket and trace kernels are correct. Given48 current/tracefree-second-jet coordinates plus two gerbe scalars, the listed category costs sum

    24+144+8+56+32+56+8+4=332.

Building both gerbe scalars from four primitive q values adds2, for334. This count excludes current construction, rational denominator alignment, source coefficients, weights, all other Rsharp terms and detector evaluation. It cannot be compared directly with the531-node circuit's different opaque-input contract.

`test_current_kernel_identities.py` passes5 methods:27 abstract sl2-basis checks of the triple identity,27 derivative-commutator checks,81 cubic mu-group checks,9 selected-kernel checks, and the scalar count sum. These are multilinear abstract-matrix identity controls; no physical HM polynomial or source jet is evaluated. Formula assembly has also been independently checked term by term against the full baseline.

## Further exact cubic cancellation

Write Y=YH-[U_c,X]/2 and Z=ZH-[L_c,K]/2, with YH,ZH retaining only the two normalized-second-jet brackets. For one ordered(U,L), the two correction brackets in Q give

    -[[U,X],L]/2-[U,[L,K]]/2
      =-d(X,L)U+d(U,L)(X-K)+d(U,K)L.

Adding the original D/S cubic expression cancels its D term and leaves exactly

    d(U,X)L+d(L,K)U.

Thus Q's cubic part becomes d(U_a,X)L_b-d(U_b,X)L_a+d(L_b,K)U_a-d(L_a,K)U_b, and its derivative brackets use YH/ZH. The overall1/4 is unchanged. The conditional schedule becomes24+96+8+40+32+56+8+4=268, or270 when constructing the gerbe scalars from q. This saves48 derivative-object bracket products and16 trace/vector products relative to332. An additional81 abstract-basis identity checks this substitution, and a seventh test checks the revised count. This remains an opaque-input scalar schedule, without a physical-source construction or resource certificate.
