# The actual lower endpoint normal variation is nonzero

## Theorem and exact scope

Let T=H1(B_Q(-2))^G be the one-dimensional invariant first-normal direction. The actual lower-source variation, followed by the endpoint quotient, defines the linear map

    T -> Hom_G(D5, (Cplus/J) tensor Sym^2 A),
    Cplus/J=P4.

This map is NONZERO, hence has kernel ZERO. Its two-dimensional target is the space of quadratic endpoint families, not the space of cubic or fourth obstruction values.

More precisely, use the actual fixed physical and Serre conventions of the companion sources. For a=t^2, normalized abstract C5 eigenvectors X,Y, and the canonical apolar normal cocycle, the values are

    h=X^4:   0,
    h=XY^3:  (3k/(Bc)) [Y/z] != 0
                  in H1(Wprime O_L(-3)),  z=t/s.        (1)

For an actual nonzero normal direction eta, multiply BOTH values by its common nonzero scale c_eta. No invariant numerical value is assigned to this scale. The parameters B,c,k are nonzero symbolic parameters fixed by the actual smoothness and Atiyah comparisons, not selected coefficient values.

The P4 in (1) is the LOWER endpoint quotient Cplus/J. It is not the different copy P4=H1(B_Q(4))_+ used for the third Bockstein. The previously proved zero third variation and identically zero third Bockstein remain unchanged. No fourth Bockstein value, generic Smith exponent beyond the existing bound, or complete original repair follows here.

## 1. Actual comparison, not merely a formal cone computation

The proof combines the following checked actual inputs.

1. ACTUAL-NORMAL-TRACE-HAS-NONZERO-NILPOTENT-COMPONENT.md and ACTUAL-NORMAL-CLASS-HAS-A-NONZERO-LOWEST-VERTEX-DIAGONAL.md prove that every nonzero invariant normal direction has a nonzero trace-degree-eight component.
2. ACTUAL-LOWEST-NORMAL-CLASS-HAS-AN-APOLAR-REPRESENTATIVE.md identifies that component with c_eta times an explicit invariant cocycle and constructs compatible scalar trace lifts n_i. Its diagonal is 4/z in the apolar normalization. The actual scale c_eta is retained and is nonzero.
3. ACTUAL-ENDPOINT-QUOTIENT-IS-LOWEST-VERTEX-COHOMOLOGY.md proves the canonical quotient Cplus/J=H1(Wprime O(-3)). This is restriction followed by the LOWEST projection; the full restriction to the vertex open is injective and does not kill J.
4. ACTUAL-TWO-ENDPOINT-INPUTS-HAVE-COMPATIBLE-CONE-OPERATORS.md identifies the actual scalar and compatible operator separately for each h in (1), including both regular charts and full determinant-normalized root transport. Conic corrections and the remaining section-preserving ambiguity have degrees too high to change the degree-four operation.

The exact secondary formula is

    tau(gamma_4)=L_4(eta_8)-delta K,
    q(K_i)=T_4(n_i),
    L_4(E)=H DE+[A,E]+H rho E,
    T_4(s)=H Ds+u s.

Both the physical normal-equation term H rho and the trace lifts K_i are indispensable. The component-constant shadow cancels exactly against the global scalar null-homotopy; its removal is not a support-only inference.

## 2. Actual values from the fully corrected cochains

UNIVERSAL-HOMOGENEOUS-ENDPOINT-SECONDARY-SQUARE-CANCELLATION.md constructs the full regular K_i for X^4 and exhibits gamma_4 as a regular O(-3) coboundary. Thus its actual endpoint value is zero.

UNIVERSAL-HOMOGENEOUS-ENDPOINT-SECONDARY-XY3-NONVANISHING.md separately constructs the full regular K_i for XY^3 and proves the exact identity

    gamma_4 = 3kY/(Bc z) + z^-3 gamma_y(-1/z)-gamma_x,

where gamma_x and gamma_y are displayed regular linear binary forms on their full charts. The global dual test Y* tensor 1 in H0(Wprime* O(1)) has residue 3k/(Bc), which is nonzero. Hence this is a nonzero class, not merely a nonzero local term before global cancellation.

The actual comparison in Section1 transports these two homogeneous identities to (1). Multiplying the entire construction by c_eta preserves zero and nonzero. This is a direct calculation of the composite operation; no nonzero conclusion is inferred merely from nonzero constituent maps.

The combined independent audit ACTUAL-TWO-INPUT-ENDPOINT-VALUES-INDEPENDENT-AUDIT.md checks all cochain, physical-line, determinant, orientation and actual comparison conventions.

## 3. These are the two canonical kernel input lines

Keep the FIXED source identification I_f from ACTUAL-FOURTH-SQUARE-INPUT-REQUIRES-A-NONZERO-THIRD-SOURCE-CORRECTION.md. With its unnormalized transvectant convention, the universal tensor gives exactly

    I_f(X^4)=20736 B^2 c s t^3,
    I_f(XY^3)=5184 ABc^2 t^4.                            (2)

Both scalars are nonzero. Since L_can(a,h) is a nonzero scalar multiple of the second transvectant (a,I_f(h))_2, both h in (1) lie in K_a when a=t^2. The pair therefore identifies the mixed t^3s and pure t^4 kernel lines, respectively. It does not silently replace the actual positive D5 source by the negative binary quartic representation.

In particular the zero for X^4 is NOT, by itself, a proof that one named symmetric or alternating decomposition channel vanishes. The nonzero for XY^3 is an independent calculation. Any reconstruction of the entire two-coefficient family must retain the fixed identification (2) and its evaluation conventions.

## 4. Kernel statement and remaining boundary

The operator and secondary connecting diagram are linear in eta, quadratic in a, and linear in h. All constructions are G-equivariant. Thus they give the displayed linear map from T into the quadratic-family space. Its dimension is two because

    Sym^2 A tensor D5 = 1+A+V+2P4+3D5.

The nonzero value (1) proves the map is nonzero; since T has dimension one, its kernel is zero. This is an exact kernel theorem for the LOWER endpoint operation, not for an unidentified higher-normal obstruction map.

This result shows that omitting the endpoint contribution from the actual lower representative is not justified. Computing the next ambient division still requires its actual normal-coordinate scale and the complete relevant lift data, or a dual certificate that retains them. A nonzero lower endpoint class does not imply a nonzero fourth value.

## Reproduction

Run python verify_actual_endpoint_normal_variation_nonzero.py. It reruns the actual two-input comparison and both complete secondary calculations, then checks the source identities (2) and both canonical kernel equations. It uses unassigned formal parameters throughout. Frozen prior sources are unchanged.
