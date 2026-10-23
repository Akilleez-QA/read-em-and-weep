# The actual degree-six restriction defects are the cohomology of E(2)

Work over C with G=SL2(F5), negative coordinate space W, positive fixed plane R=P(V), and parameter line T=P(W*). Fix the determinant identification W≅W*. All maps below retain the actual cohomology module and parameter pencil; no selected coefficient, point or parameter is evaluated.

## 1. Exact inputs and provenance

INPUTS.json records five immutable originals in Akilleez-QA/read-em-and-weep:

- TERMINAL, PR1052 at 64e4fdd771a14a764c6e119d2eb25b0237d83622, research/hm/negative-string-terminal-gate/PROOF.md. It proves the actual exact Koszul sequence

      0 -> M3 -> W tensor M4 -> M5 -> 0,
      M3=H1(B(3))_-=3W'+3S+6T6,
      M4=H1(B(4))_+=2V+4P+3D,
      M5=H1(B(5))_-=W'+3T6.                       (1)

  It retains the actual onto parameter pencil 0 E->M3 O(-1)->M4 O->0, its rank17 degree-54 kernel E, and H0(E(1))=0. It also authenticates H1(B(6))=0, H2(B(t))=0 for t>=2, H3(B(t))=0 for t>=-1, H0(B(4))=0, H0(B(5))=1+P+D, and the positive parity of B_R(t). Its selected U4≅D has an actual next arrow f5:T6->M5 whose vanishing remains unresolved.
- ACTUAL, commit db51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/ACTUAL-EQUIVARIANT-SPLITTING-AND-GAUSS-PERSISTENCE.md: the original actual E pencil, equivariant splitting conventions and finite necessary E catalogue.
- PLANE, PR967 at 39c5f4fbc012f4ec57ffc56d5de18cedb3571d60, research/hm/fourth-normal-obstruction/PROOF.md, Section1: the actual plane resolution 0 A O_R(-3)->D O_R(-2)->F_R->0.
- CATALOG and FRONTIER, PR942 at 3cd8a620e7268cf86fb8cc019d35f04d3cb6b448, research/proof-repair-campaign/four-pair-composition/inputs/catalog.json and frontier.json: the fixed necessary source alternatives, not realizations. Their four pairs have E indices10,10,14,13. CATALOG's upstream input hash for ACTUAL is a52685fc9e7c89abf26171a15989cedeaf3bd101a2edde790a24f9cfe0179256, which the checker matches against the exact ACTUAL bytes. Section1 of ACTUAL identifies E with precisely the pencil above, not a distinct equal-rank bundle. Its names P4,S4,D5 are P,S,D here.

The actual theorem in Sections2–4 is unconditional on the necessary-pair ledger. The numerical alternatives in Section5 are explicitly conditional on their stated E type. No candidate is realized or excluded by this proof.

## 2. Natural identification of the next module maps

Write the actual pencil as

    0 -> E -> M3 O(-1) -> M4 O -> 0.              (2)

Since H0 and H1 of O(-1) vanish, its connecting map identifies

    M4 ≅ H1(E).                                  (3)

Twisting (2) once and taking cohomology gives

    0 -> M3 -> H0(O(1)) tensor M4 -> H1(E(1)) -> 0,

where left injectivity is H0(E(1))=0. Under the determinant identification this is exactly (1), hence gives

    M5 ≅ H1(E(1)).                               (4)

These isomorphisms identify multiplication maps, not merely spaces of equal character. For any parameter-linear section, multiply the whole sequence (2) by that section to map it to its twist. Naturality of the connecting maps identifies multiplication H1(E)->H1(E(1)) with the map from M4 into the displayed quotient of H0(O(1)) tensor M4.

To make the determinant convention explicit, use formal negative variables x,y and parameter variables u,v so the universal pencil is u m_x+v m_y. Its map on sections after twisting is s↦u tensor m_x(s)+v tensor m_y(s). The map from this coefficient target to actual M5 is

    u tensor t ↦ m_y(t),    v tensor t ↦ -m_x(t).

Commutativity kills the source. This quotient map is the actual Koszul map (1), after the determinant rotation u↦y, v↦-x. It is an isomorphism on the cokernel by (1). Thus the preceding twist diagram identifies the actual multiplication maps after this fixed invertible equivariant rotation. This is a universal formal-coordinate identity, not evaluation of an actual map at a chosen parameter. In particular it identifies the simultaneous kernels and cokernels canonically with the determinant convention fixed.

## 3. Intrinsic maximal-slope description of the joint kernel

Tensor the Euler sequence on T by E(2):

    0 -> E -> W tensor E(1) -> E(2) -> 0.         (5)

Because H0(E(1))=0, its cohomology gives

    0 -> H0(E(2)) -> H1(E) -> W tensor H1(E(1))
      -> H1(E(2)) -> 0.                           (6)

The middle arrow is simultaneous multiplication, with the determinant convention of Section2. Consequently (3)–(4) turn (6) into the actual sequence

    0 -> H0(E(2)) -> M4 -> W tensor M5
      -> H1(E(2)) -> 0.                           (7)

There is a geometric interpretation of its kernel. H0(E(1))=0 implies that every Birkhoff--Grothendieck degree of E is at most-2. Therefore evaluation defines a canonical subbundle

    E_{-2}:=image[H0(E(2)) tensor O(-2) -> E]
           ≅ H0(E(2)) tensor O(-2).               (8)

It is the maximal slope -2 part (or zero if there is no such summand). Naturality of (5) for E_{-2}->E identifies the injection H0(E(2))->H1(E) in (6) with the image of H1(E_{-2}). Indeed Euler for O(-2) has connecting isomorphism H0(O)->H1(O(-2)), and H1(E_{-2}(1))=0. Thus the joint-negative kernel in actual M4 is exactly the actual subspace H1(E_{-2}).

This can also be checked on each lower summand O(-d), d>=3. Serre duality turns joint multiplication on H1 into the surjective binary multiplication W tensor Sym^(d-3)W->Sym^(d-2)W, so its joint kernel is zero. The degree-2 summands instead map to H1(O(-1))=0. This check does not choose a splitting or position for the canonical subspace (8).

## 4. Both actual restriction defects, not just an Euler difference

Let

    rho:H0(P4,B(6))_+ -> H0(R,B_R(6))              (9)

be actual restriction. The target has only positive parity. Twist the two-negative-coordinate Koszul sequence to obtain

    0 -> B(4) -> W tensor B(5) -> I_R B(6) -> 0.

Because H0(B(4))=0 and W tensor H0(B(5)) is entirely negative, its positive cohomology sequence, using H2(B(4))=0, is

    0 -> H0(I_R B(6))_+ -> M4 -> W tensor M5
      -> H1(I_R B(6))_+ -> 0.                    (10)

The middle arrow is the same actual joint multiplication as in (7). This proves natural identifications of its two defects with H0(E(2)) and H1(E(2)). The restriction sequence and H1(B(6))=0 then give the actual exact sequence

    0 -> H0(E(2)) -> H0(P4,B(6))_+ --rho-->
      H0(R,B_R(6)) -> H1(E(2)) -> 0.             (11)

In particular

    ker rho ≅ H0(E(2)) ≅ H1(E_{-2}),
    coker rho ≅ H1(E(2)).                        (12)

The first isomorphism in (12) identifies the actual boundary image in M4, not merely its abstract representation. Equations (7),(10) make the assertion independent of a chosen bundle splitting. This resolves the missing restriction-kernel dependency of TERMINAL in terms of the already defined actual E, without pretending that E's realized splitting is known.

For completeness, all dimensions and characters can be checked without any restriction-map evaluation. H1(B(6))=H2(B(6))=H3(B(6))=0 are authenticated in TERMINAL. H4(B(6))=H0(B(-11))*=0 by stability. Therefore H0(B(6)) is its Euler character. The same normalized-monad lambda-ring formula as TERMINAL, with Sym2 F(7), gives the positive part

    H0(B(6))_+ = 4A+3V+5P+5D,   dimension66.     (13)

On the plane the symmetric-square resolution of PLANE, twisted by7, is

    0 -> Lambda2 A tensor O_R(1)
      -> A tensor D tensor O_R(2)
      -> Sym2 D tensor O_R(3) -> B_R(6) -> 0.

It is exact because it is the symmetric-power resolution of a locally free quotient. All three terms have no higher cohomology, so B_R(6) has no higher cohomology. Their Euler character yields

    H0(B_R(6)) = 4A+4V+5P+5D,   dimension69.     (14)

The exact fixed nine-class checker verifies (13)–(14). Their difference V is consistent with (11); it is not used to infer injectivity or choose a kernel.

## 5. Conditional values on the pinned remaining source alternatives

Read only the four source pairs in FRONTIER and their three referenced fixed E entries of CATALOG. They are

    E10=P O(-2) + 2D O(-2) + O(-8) + W O(-9),
    E13=P O(-2) + D O(-2) + T6 O(-3) + W O(-9),
    E14=P O(-2) + D O(-2) + V O(-4)
                       + P O(-4) + O(-8).        (15)

Each is rank17 degree-54. The two source126 pairs use E10, the c-d-f pair uses E14, and the source2 pair uses E13; these descriptions do not alter the source ledger. No actual tensor or instance is computed. This is a bounded check of three fixed bundle types.

For E10, (8) and (12) give

    ker rho = P+2D, dimension14,
    coker rho = V+P+2D, dimension17,
    rank rho=66-14=52.                            (16)

For either E13 or E14 they give

    ker rho = P+D, dimension9,
    coker rho = V+P+D, dimension12,
    rank rho=66-9=57.                             (17)

The representation equalities describe isomorphism types; no canonical splitting of the cokernel into V and the kernel is asserted. They also follow directly from H1(E(2)): E10 contributes H1(O(-6))=D and W tensor H1(O(-7))=W tensor T6=V+P+D; E13 contributes just the latter; E14 contributes V+P+D from its three remaining summands.

Thus injectivity of rho is ruled out for every one of these pinned necessary alternatives. This is conditional on that E type, not a new unconditional realization theorem or a claim that the necessary ledger is machine-certified geometry.

## 6. The selected terminal D still requires an incidence decision

TERMINAL's marked U4≅D is an actual selected line in the D-multiplicity space of M4=2V+4P+3D. By its symmetric continuation and (7),

    f5=0  if and only if  U4 subset H1(E_{-2}).    (18)

If one nonzero vector of U4 lies in the joint kernel, equivariance and irreducibility put all of U4 there. The D multiplicity of that kernel is two in E10 and one in E13/E14. Mere existence of these D copies does not locate the selected U4 among them. The nonzero kernel (16) or (17) therefore does not prove that f5=0. Conversely it blocks the proposed strategy of proving the full restriction injective on any remaining candidate.

The new actual constraint is the intrinsic location of all restriction sections and the joint-negative socle in the maximal degree-minus-two cohomology of E, with both restriction defects determined functorially. Neither terminal branch, source occurrence, opposite type, vertex scalar nor smoothing result is selected. No actual HM/source coefficient, point, parameter, derivative, jet, matrix, instance rank evaluation or large scan was used.
