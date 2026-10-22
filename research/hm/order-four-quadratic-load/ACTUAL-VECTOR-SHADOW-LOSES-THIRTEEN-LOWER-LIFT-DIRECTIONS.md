# The canonical vector shadow loses thirteen lower-lift directions

## Exact comparison result

Put C=H1(B_Q(2))_+, with its actual Serre-involution splitting C=Cminus+Cplus of dimensions21+9. Let xi_Q be the nonzero restriction of the actual cyclic class. The following are actual cohomological statements, not a selected source calculation.

1. The cyclic image J=D5·xi_Q is NONZERO and is exactly the D5 summand of Cplus=P4+D5. Thus dim J=5.
2. The ambient divided class v_h, defined by q0 v_h=a h zeta_a, has a canonical restriction in C/J. The ambient kernel ambiguity restricts exactly to J.
3. A corrected cone operator O of symbol k a h D_a can be chosen odd under the Serre involution. Its actual first-normal lifting obstruction b_e in C is affine in the normal-extension parameter e centered at the midpoint. Its midpoint value lies in Cminus, and its linear variation lies in Cplus.
4. The actual ambient restriction v_h|Q agrees with b_actual modulo J. The vector cochain R/nu gives the image of b_mid, and hence of v_h|Q, in the effective12-space C/R_common=H1(P4 O_L(-4)). It is NOT a representative of the whole class in C.
5. Even after the legitimate J ambiguity is removed, the map from C/J to the effective12-space has kernel

       (P4+D5)_minus + (P4)_plus,       dimension13.      (1)

The first summand is the polynomial nine-space lost from the midpoint class. The second contains the actual normal variation modulo J. No value of either missing component is asserted.

Consequently one cannot feed R minus the third source correction into the next ambient q0 division as though it were the actual restricted v_h. To reuse R as a full lower representative one must recover the data in(1), or prove that the omitted contribution is immaterial. A different method, such as the normalized dual certificate, may bypass their recovery; this note does not claim that recovering them is sufficient to perform the next normal division.

## 1. The cyclic five-space is actually nonzero

This needs an actual multiplication diagram, not the existence of two nonzero legs.

The Serre sequence twisted by minus two and the acyclicity of O_X(-2) give

    H1(G(-2)) = H1(I_Z) = H0(O_Z)/C.

The actual zero scheme has two disjoint components, the conic and the vertex. Its invariant global functions are the two component constants; the additional V is nilpotent and has no invariant part. Thus the invariant line of H1(G(-2)) is represented by

    z=(1 on the vertex, 0 on the conic), modulo global constants.

The actual tangent inclusion G(-2)->B_Q maps this invariant line NONTRIVIALLY onto C xi_Q. Indeed FIRST-NORMAL-ADJOINT-DEFECT-IS-INVARIANT-ACYCLIC.md Section3 identifies its composite with the invariant evaluation map from H1(B_Q(-2)) with the actual bracket [eta,N], and proves that bracket nonzero. In particular z maps to a nonzero scalar multiple of xi_Q.

Now multiply this SAME representative by h in D5. The result is the section h|Z on the vertex and zero on the conic. It is purely vertex cover-degree4. The actual residue theorem identifies this pure space with H1(G)_+ and embeds it into C through G->B_Q(2). The maps commute with multiplication by h.

Under the actual cubic quotient, the resulting section is precisely the image of h under

    Q0:D5 -> H0(V O_L(2)).

The exact sequence

    0 -> Wprime O_L(-3) -> D5 O_L -> V O_L(2) -> 0

gives injectivity of Q0, because H0(Wprime O_L(-3))=0. Therefore h z, and consequently h xi_Q, is nonzero for every nonzero h. This proves an injection D5->C.

The invariant xi_Q has Serre-involution sign+, as proved from the actual block-Euler Atiyah class in the midpoint theorem. Positive h also has sign+. Hence this image lies in Cplus. Since Cplus=P4+D5 has a unique D5, its image is precisely that summand. This proves the assertion about J without an actual matrix or coefficient evaluation.

The diagram uses the ACTUAL Serre tangent inclusion and ACTUAL polynomial restriction at both twists. Finite-group multiplicity is used only after the nonzero composition has been identified explicitly.

## 2. What the actual ambient division determines

Let e denote a marked first-normal extension of the fixed cone bundle. Center its affine parameter at the midpoint and normalize its scale, if desired, so that

    delta_e(N)=e xi_Q,       e_actual=1.

The midpoint boundary is zero and the actual endpoint boundary is nonzero, so this is legitimate. The normal sequence at twist4 has the fragment

    H0(B_Q(4))_+ --delta_e--> C --q0--> H1(B_e(4))_+.

The actual cone section theorem says H0(B_Q(4))_+=N(A+D5). By O-linearity,

    delta_e(Nr)=e r xi_Q.

Every negative r in A kills xi_Q on the cone. Section1 proves that the remaining image is e J. At the actual endpoint the kernel of normal multiplication q0 is therefore exactly J.

The ambient equation q0 v_h=a h zeta_a restricts to this normal equation. Two ambient choices differ by the original kernel (A+D5)xi, and their cone restrictions differ exactly by J. Thus v_h|Q is canonical modulo J, not in C itself. No additional splitting or polynomial choice has been made.

## 3. Exact affine law for the operator obstruction

Fix a corrected cone operator O with symbol H D_a, H=k a h, and the physical determinant-line action. In local cone frames write O=H D+A. For any marked extension e, choose arbitrary local lifts of O to that extension. Their normal gluing discrepancy is a cocycle in B_Q(2); write its class as b_e(O). It is independent of these local lift choices.

For clarity, fix the discrepancy convention

    O_j - P_e O_i P_e^(-1) = q0 K_e,      b_e=[K_e].

If a local normal transition is changed by

    P_e=(I+e q0 eta_ij) P_mid,

then first-order expansion gives the EXACT change

    K_e=K_mid+e[H D eta_ij+[A_j,eta_ij]+H r0 eta_ij],
    r0=D(q0)/q0                                      (2)

in the transported target frame. Here D(q0) denotes the derivative of the local equation representative. The globally tangent field annihilates the physical equation section with its line action; this does not justify deleting r0 in an arbitrary local equation frame. Formula(2) retains that action and is a universal square-zero operator identity.

Changing a representative of eta or changing local normal operator lifts adds the corresponding Cech coboundary. Therefore b_e is affine in e. Its linear part is the induced differential-operator action in(2) on the ACTUAL invariant extension direction, not an arbitrarily chosen normal cocycle.

Changing O by an allowed cone section Nr changes b_e by e r xi_Q. Hence its midpoint value is independent of O, and its actual endpoint class is independent of O modulo J.

The specified operator lifting comparison before the final cup says

    q0 b_e = a h zeta_e

in the first-normal cohomology, with zeta_e=k At_(F_e)(D_a), up to the fixed common boundary sign. This is the direct local Atiyah obstruction identity, not an inference of uniqueness from that equation. At the actual endpoint zeta_e is the restriction of the actual ambient zeta_a. The normal exact sequence of Section2 therefore gives

    v_h|Q = b_actual modulo J.                       (3)

This is the lower comparison needed here. The already published third-value theorem only needed its product by a.

## 4. The involution localizes the normal variation

Let rho be the actual Serre involution on the cone data, and let J_normal(e)=-e be its reflection on the centered normal torsor. Keep the actual assignment a->D_a fixed. The negative polynomial a has rho sign-, whereas D_a commutes with the negative-block scalar transformation and positive h has sign+. Thus the symbol H D_a has sign-.

Replace O by its odd average (O-rho(O))/2. This has the SAME specified symbol, the same fixed determinant convention, and is still a corrected cone operator. The correction space is a vector space of cone sections, so this averaging does not require an ambient realization of the midpoint.

Naturality of the normal lifting obstruction gives

    rho_C b_e(O)=b_(-e)(rho O)=-b_(-e)(O).           (4)

Write b_e=b_0+e b_1. Comparing the constant and linear coefficients in(4) yields

    b_0 in Cminus,             b_1 in Cplus.         (5)

The midpoint value b_0 is independent of the cone-operator choice. Odd choices differ only by N times positive D5 quadratics, so their slopes differ by J. Equivalently, after passing to C/J the residual actual variation lies in Cplus/J=P4.

This is stronger than knowing a b_e is independent of e: it identifies the common-kernel sector in which the lower variation lives. It does not evaluate that sector.

## 5. Exactly what the vector cochain remembers

The actual negative-sector theorem identifies

    Cminus = epsilon H0(Q4(4)),

with the Serre-marking sign epsilon retained. Its effective quotient is the actual square boundary

    0 -> Sym^8(Wprime) -> H0(Q4(4))
      -> H1(P4 O_L(-4)) -> 0.                       (6)

The polynomial kernel is P4+D5, of dimension9. On the full C the common multiplication kernel is this polynomial nine-space plus Cplus, of dimension18.

The harmonic transition theorem computes the lower trace/square-ideal shadow of b_mid. The target-frame Gram subtraction and vector reduction are exact Cech boundaries, so R/nu gives exactly the image of b_mid under(6). The finite meromorphic-source law preserves this class. No inverse of(6) was constructed in those calculations.

By(3)-(5), b_actual-b_mid lies in Cplus modulo J, and Cplus is killed by the effective quotient. Consequently

    image(v_h|Q)=image(b_mid)=[R/nu]
       in H1(P4 O_L(-4)).                          (7)

Thus(7) is indeed an actual effective12 comparison, not merely an equality after cup with this particular a. But it does not upgrade R to a full C representative.

Finally J lies in Cplus and has dimension5. Quotienting the actual common-kernel exact sequence by J gives

    0 -> (P4+D5)_minus + (P4)_plus
      -> C/J -> H1(P4 O_L(-4)) -> 0.                (8)

The splitting into involution signs is canonical; no splitting of the negative-sector sequence(6) is chosen. Its dimensions are13 -> 25 -> 12. These are dimensions of an exact geometric quotient, not a substitute for any actual value calculation.

## Consequence for the fourth calculation

The canonical raw cubic and its nonzero source correction remain valid because they use only a times(7). A construction that reuses R as the next lower input must retain the actual lower class modulo J, or prove that the omitted contribution is immaterial; the effective image alone does not justify that substitution. A chosen lift of R can miss both the midpoint polynomial nine-space and the endpoint positive four-space. Their being killed by ONE quadratic multiplication does not make their next normal secondary operation zero.

No actual fourth coefficient, matrix rank, normal parameter value, or source instance has been evaluated. All previously frozen files are unchanged.

## Sources and verification

The geometric inputs are ACTUAL-NEGATIVE-INVOLUTION-SECTOR-AS-SQUARE-QUOTIENT.md; LOWER-CONE-COHOMOLOGY-PERFECT-NEGATIVE-ACTION.md; MIDPOINT-NORMAL-EXTENSION-HAS-UNIQUE-SQUARE-ZERO-ADJOINT.md; FIRST-NORMAL-ADJOINT-DEFECT-IS-INVARIANT-ACYCLIC.md Section3; POSITIVE-SERRE-RESIDUE-AND-CANONICAL-CONE-OPERATOR-CORRECTION.md Sections1-3; the actual midpoint operator comparison; and the harmonic/vector/source-frame comparison notes.

Run python verify_vector_shadow_lower_lift_comparison.py. It checks the universal finite operator-transport identity with the equation-frame term, the involution/affine coefficient identity, line twists, exact representation subtraction, and P1 acyclicity used in the cyclic-injection proof. The actual commuting Serre diagram is proved above, not replaced by a rank calculation.
