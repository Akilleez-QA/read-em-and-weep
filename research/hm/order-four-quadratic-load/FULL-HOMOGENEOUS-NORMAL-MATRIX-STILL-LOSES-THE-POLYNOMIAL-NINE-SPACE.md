# The full homogeneous normal matrix still loses the polynomial nine-space

## Precise obstruction

Keeping both entries K11 and K21 of the unmultiplied harmonic normal transition does NOT recover the full midpoint class in Cminus. Their coefficient bundle is already the rank4 bundle J_-=P4 O_L(-4), whose H1 is the effective12-space. The trace map is an isomorphism on this entire bundle, not an additional quotient. Thus the diagonal Gram subtraction and passage to the vector R lose no further cohomology from the full homogeneous matrix K.

The missing nine-space is instead the difference between a local polynomial coefficient lift and a genuine GLOBAL G(2) section. It is exactly Sym^8(Wprime)=P4+D5. A nonzero polynomial lift has a nonzero pure-positive octic wedge, whose restriction to the conic is nonzero; it cannot be the wedge of a global G(2) section. This supplies a concrete global-extension obstruction.

All statements concern the actual coefficient and Serre diagrams. No actual source coefficient, matrix/rank evaluation, or fourth value is computed.

## 1. Twist down the exact coefficient diagram

Use the ACTUAL bundles E8,J8,M8 from ACTUAL-DEGREE-EIGHT-NORMAL-OPERATOR-QUOTIENT.md and twist them by O_L(-2). Write

    E_-=E8(-2),   J_-=J8(-2),   M_-=M8(-2).

The exact sequences become

    0 -> J_- -> E_- -> M_- -> 0,
    J_-=P4 O_L(-4),
    0 -> O_L(2) -> E_- -> Sym^8(Wprime) O_L -> 0.     (1)

The last sequence is the actual wedge/polynomial coefficient sequence, not an assertion that E_- is a homogeneous subbundle of the global G(2).

Since H1(O_L(2))=H1(O_L)=0, and both left line degrees are nonnegative,

    H0(E_-)=A+Sym^8(Wprime),    dim12,
    H1(E_-)=0.

The displayed representation splitting can be taken uniquely equivariant: the bundle extension splits by H1(O(2))=0, and its equivariant splitting differences are Hom_G(Sym^8(Wprime),A)=0. This does not turn these coefficient sections into global G(2) sections.

The double-cubic description supplies

    M_-=A O_L(4)+V O_L(2),     h0(M_-)=24.

Also H0(J_-)=0 and h1(J_-)=12. Therefore(1) gives the exact cohomology quotient

    0 -> H0(E_-) [12] -> H0(M_-) [24]
      -> H1(J_-) [12] -> 0.                        (2)

## 2. The actual global midpoint quotient is different

ACTUAL-NEGATIVE-INVOLUTION-SECTOR-AS-SQUARE-QUOTIENT.md proves that the actual global operator boundary on this same M_- section space has kernel only the scalar A piece:

    0 -> A [3] -> H0(M_-) [24] -> Cminus [21] -> 0. (3)

This is proved by the complete global commutator sequence and the actual cone section theorem H0(G(2))_+=sigma(A+D5). Only its negative-involution A summand can enter M_-, and it is precisely the scalar O_L(2) piece of(1).

The A subspace in(3) is therefore the same A subspace in H0(E_-) in(2). Passing from(3) to(2) loses exactly

    H0(E_-)/A=Sym^8(Wprime),    dimension9.

Equivalently the commuting quotient diagram gives

    0 -> Sym^8(Wprime) -> Cminus -> H1(J_-) -> 0.   (4)

This is the actual square-boundary sequence, with the full Serre marking understood. It is not merely a dimension comparison between unrelated spaces.

## 3. Why the full K has no extra degree-eight information

In this degree and twist a trace-free coefficient gauge is

    K=[[k,0],[r,-k]],   k in O_L(2), r in V O_L(-6).

Conjugation under g_j=g_i+p f gives the extension law r_j=r_i+2p k_i with the matching diagonal change. Its coefficient bundle is exactly

    0 -> V O_L(-6) -> J_- -> O_L(2) -> 0.

The actual trace/square-ideal map is

    tr(N_j K)=2f g_j k-f^2 r.

Regularity of f,g makes it injective in these degrees, and its image is precisely the actual degree8 square-ideal piece. Hence it identifies J_- with P4 O_L(-4). It is already an isomorphism BEFORE taking cohomology.

The actual Gram primitive removes the diagonal cochain by a zero-cochain in this same coefficient complex. Its effect on the lower entry is exactly the pinned vector R. Consequently the classes of the full K and of R/nu contain identical H1(J_-) information. Keeping the eliminated diagonal, or declining to take the trace, cannot invert(4).

The scalar and normal-equation factors are those of the frozen full-frame theorem. This statement does not promote the homogeneous coefficient complex to a subcomplex of the global adjoint resolution.

## 4. An explicit conic obstruction to extending the extra coefficient lifts

Take an E_- coefficient section whose wedge is a nonzero

    F8 in Sym^8(Wprime).

Its wedge is a pure-positive physical quartic. Since the actual vertex complete intersection has socle degree6, F8 vanishes on the ENTIRE vertex scheme. But on the conic its restriction is the nonzero binary octic F8 itself: pure-positive quartics restrict onto Sym^8(Wprime), with the Cartan identification used throughout.

If this coefficient section extended compatibly to an actual global G(2) section, its wedge with sigma would be a section of I_Z(4). Such a wedge must vanish on the conic as well as on the vertex, contradicting F8|conic!=0. Equivalently the established exact calculation gives H0(I_Z(4))_+=0.

Thus every nonzero member of the nine-dimensional quotient H0(E_-)/A has a concrete obstruction to global extension. It is not licensed to subtract these sections as global adjoint coboundaries. The conic octic value identifies the obstruction space with the SAME nine-space Sym^8(Wprime).

This is compatible with the fact that the actual negative midpoint defect is vertex-supported: its polynomial ambiguity concerns which LOCAL coefficient lifts are restrictions of global tangent sections, not an omitted negative conic component of M.

## 5. What additional datum would recover the midpoint lift

To obtain the full Cminus class one needs the actual section of M_- modulo the scalar A image in(3), rather than only its coefficient boundary in(2). For the specified operator this means retaining the local normal ERROR itself,

    (O_i(N_tilde)-lambda_tilde N_tilde)/q0,

and its image in the tangent-modulo-conjugation module, with the actual midpoint matching, scalar/equation frames, and normal primitive. The transition K records differences of these errors; it does not fix their absolute polynomial component.

No claim is made that the existing leading local lower-triangular expression supplies this additional datum automatically. The existing degree bounds dispose of high-order stabilizers for the effective shadow, while a global extension comparison is required for the full class. The actual Cplus variation identified in ACTUAL-VECTOR-SHADOW-LOSES-THIRTEEN-LOWER-LIFT-DIRECTIONS.md remains a separate datum for reconstructing the full lower class; a different normalized dual route may bypass it.

## Verification

Run python verify_full_normal_matrix_polynomial_gap.py. It checks the twisted exact sequences, dimensions, representation quotient, complete coefficient trace identity, and the cover-degree obstruction. The actual wedge and global-boundary identifications are the cited geometric inputs, not consequences of those counts alone.
