# The actual negative-involution sector is the degree-eight square quotient

## Result

Let C_minus be the21-dimensional negative eigenspace of the actual Serre involution on H1(B_Q(2))_+. There is a natural identification, up to the fixed boundary sign,

    C_minus = epsilon H0(Q4(4)),

where epsilon is the extra Serre-marking character of weight-1. Under it the ACTUAL multiplication by a negative quadratic a is

    H0(Q4(4)) -> H1(P4 O_L(-4))=P4 tensor A
      --cup a--> H1(P4 O_L(-2))=P4.                (1)

Consequently multiplication by every nonzero a has rank4. Its common kernel on C_minus is the canonical9-space Sym^8(Wprime)=P4+D5. Including the positive eigenspace, the common kernel has dimension18, and the remaining12-dimensional quotient is P4 tensor A with its perfect quadratic contraction.

This identifies the whole actual lower multiplication map; it does not evaluate the particular corrected operator class needed by the third Bockstein.

## 1. The actual degree-eight source and its finite action

The double-cubic theorem gives the vertex piece of M(4) as

    M8=A O_L(6) plus V O_L(4).

The corresponding piece of M(2) is

    M8(-2)=A O_L(4) plus V O_L(2).                 (2)

Its section dimension is15+9=24. Its class-of-N subbundle is O_L(2); quotienting gives Q4(4)=W O_L(5) plus V O_L(2).

Here is an actual finite-action check, not a character-dimension guess. The Serre involution phi acts trivially on the base L. There are no equivariant cross-Hom maps between A O6 and V O4: one direction has negative line degree, while the other is Hom_G(V,A tensor A)=0. Thus phi acts by a scalar on each summand. The actual global boundary from each summand to P4 is nonzero, by ACTUAL-SQUARE-QUOTIENT-SPLITTING-AND-BOTH-BOUNDARY-CHANNELS.md (the A summand surjects onto its W O7 quotient). Since P4 has phi weight+1, both scalars are+1. Twisting down by the physical O_L(2) changes the scalar by mu^(-2)=-1. Hence the entire space in (2) has phi weight-1.

The intrinsic coordinate action on Q4(4) has weight+1, as in ACTUAL-LOWER-COHOMOLOGY-SERRE-INVOLUTION-SPLITTING.md. The wedge quotient carries the additional epsilon from the Serre marking. These are consistent, not two interchangeable linearizations.

## 2. The global boundary is an isomorphism after the scalar kernel

Let J2 be the image of B_Q(2)->G(2). The exact sequences are

    0 -> epsilon O_X -> B_Q(2) -> J2 -> 0,
    0 -> J2 -> G(2) -> M(2) -> 0.

H1(O_X)=H2(O_X)=0 identifies H1(J2) with H1(B_Q(2)). Therefore the boundary on (2) has kernel exactly the image of global H0(G(2))_+.

The established primary calculation in WEIGHTED-STACK-SQUARE-SHADOW-AND-PRIMARY-SCALAR.md Sections3-4 gives

    H0(G(2))_+=sigma H0(O_X(2))_+=A plus D5.

There is also a direct check that H0(I_Z(4))_+=0. The cover-degree8 block restricts isomorphically to the conic quartics O_C(8), so it cannot occur in a section vanishing on Z. The cover-degree0 block must vanish on the reduced vertex. The remaining cover-degree4 ideal piece is f times Wprime with coefficient bundle Wprime O_L(-1), which has no global sections. The Serre sequence then gives the same H0(G(2)) statement without an unproved extension of polynomial representatives.

With sigma fixed by the Serre marking, these have phi weights-1 and+1 respectively. Since (2) has weight-1, only the A piece can enter its kernel. It does enter: negative quadratic scalars times the class of sigma give precisely the injective O_L(2) subbundle in (2). Hence the kernel has dimension3 and the boundary image has dimension21. The known actual target negative eigenspace has dimension21, so the resulting map is an isomorphism onto C_minus. No polynomial tangent representative is assumed to extend globally; only the exact global cohomology sequence is used.

Since H1(O_L(2))=0, quotienting by this scalar kernel identifies the source with H0(Q4(4)), with the epsilon linearization described above.

## 3. Naturality identifies the actual multiplication map

The actual wedge and trace diagram is compatible with multiplication by a. At twist4 the global target is identified with the degree8 square-ideal boundary, as proved in ACTUAL-DEGREE-EIGHT-NORMAL-OPERATOR-QUOTIENT.md. Thus the actual product is the boundary after multiplication

    H0(Q4(4)) --a--> H0(Q4(6)) -> H1(P4 O_L(-2)).

The square-ideal sequences at twists4 and6 form a commutative multiplication diagram. The source sequence is

    0 -> P4 O_L(-4) -> Sym^8(Wprime) O_L
      -> Q4(4) -> 0.

Its boundary is onto H1(P4 O_L(-4)), because the middle bundle has no H1. Its kernel is exactly Sym^8(Wprime). This proves the factorization (1).

Serre duality pairs H1(O_L(-4)) perfectly with H0(O_L(2))=A into H1(O_L(-2)). For every nonzero a the resulting functional is nonzero, so (1) has rank4. The intersection of its kernels over all a is precisely the9-dimensional polynomial image.

The positive9-dimensional eigenspace C_plus is already annihilated by all A by the actual Serre involution. Therefore the common kernel on the full30-dimensional C is18-dimensional, with quotient canonically P4 tensor H1(O_L(-4)).

## 4. Relation to the actual operator

The corrected cone operator O has symbol k a h D_a and twist4. The operator used for the third value is O0=a O. Choose local normal lifts by the same multiplication; since a commutes with the nilpotent, its defect section has r=a r1 with r1 in M(2). Extracting degree8 respects this multiplication. Therefore the particular third value is obtained by feeding the actual corrected operator class into (1), followed by reduction modulo the actual second-symbol image.

The theorem does not compute that particular class. Surjectivity of the lower multiplication map does not imply that its value on that class is nonzero.
