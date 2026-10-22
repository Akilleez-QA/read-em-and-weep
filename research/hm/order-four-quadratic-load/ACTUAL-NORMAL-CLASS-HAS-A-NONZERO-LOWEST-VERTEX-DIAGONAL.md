# The actual normal class has a nonzero lowest vertex diagonal

## Result and scope

The actual invariant normal class eta in H1(B_Q(-2)) has a canonical nonzero trace-degree-eight vertex component. Its diagonal projection is a NONZERO multiple of the Euler class in H1(L,O_L(-2)). Thus the first relevant vertex coefficient is not an arbitrary trace lift: it is forced and nonzero by the actual nilpotent shadow coefficient beta.

This is a statement about the lowest associated homogeneous cohomology component. It is not a global homogeneous representative of eta, an evaluation of the endpoint secondary P4 class, or a fourth Bockstein value.

## 1. The coefficient bundle and actual trace comparison

Use the same residue-normalized homogeneous vertex presentation as the actual degree-eight quotient theorem. In trace degree eight, a trace-free adjoint of physical twist -2 has the form

    K=[[d,0],[r,-d]],

where d has positive-cover degree zero and r degree two. Its coefficient bundle J_eta has exact sequence

    0 -> V O_L(-10) -> J_eta -> O_L(-2) -> 0.       (1)

Indeed the two vertex frame lines are O(9/2),O(-5/2), so the lower entry has line O(-9) before its degree-two coordinate factor, hence O(-10) afterwards. The upper entry would have cover degree -2 and is absent. Under the actual generator transition g->g+p f,

    r -> r+2p d.

The extension is therefore the actual twice-quintic extension, not a chosen split bundle.

The trace map is

    K -> tr(NK)=2fg d-f²r.                          (2)

The already established actual square-ideal identification J8=P4 O_L(-2), twisted by -6, gives

    J_eta = J8(-6) = (I_Z²)_degree8 = P4 O_L(-8).   (3)

This can also be checked directly: regularity and coprimality of f,g make (2) fiberwise injective on the rank-four coefficient bundle, whose target has the same rank. The determinant and line factors in (1) have total degree -32, agreeing with (3). The simultaneous opposite trace convention changes (2) by a common sign only.

## 2. Its invariant cohomology is detected by the diagonal

The exact character identities are

    Sym^8 W=P4+D5,     Sym^6 W=V+P4.

Consequently

    H1(V O(-10))^G=(V tensor Sym^8 W)^G=0,
    H1(J_eta)^G=(P4 tensor Sym^6 W)^G=C.

The base is a line, so H2(V O(-10))=0. Taking invariants in (1) proves that the diagonal map is an ISOMORPHISM

    H1(J_eta)^G -> H1(O_L(-2))=C.                 (4)

No nonzero composite is inferred merely from dimensions: (4) follows from the exact sequence with its zero end terms.

## 3. Why this is the actual leading component

The homogeneous vertex eigenextension is identified with the actual marked homogeneous presentation by the full residue/determinant comparison. The actual cone bundle on U differs from it by the exact conic correction I+tN_C, as proved in ACTUAL-CONIC-RESIDUE-FORCES-VERTEX-SERRE-COCYCLE.md. Conjugation by this correction raises the weighted trace degree by eight. The homogeneous triangular generator changes preserve that degree.

The smallest possible trace degree for an even adjoint of twist -2 is six: it consists only of the constant lower entry with coefficient O_L(-9). Its invariant H1 is zero, because H1(O(-9))=Sym^7 W has no invariant. Thus truncation through degree eight canonically extracts from the actual invariant cohomology class eta its component in H1(J_eta)^G. No lower nonzero invariant component is available to alter it; the conic correction cannot feed into this truncation, since its degree shift is eight.

The actual square shadow is

    q(eta)=delta(alpha e_v+beta n8).

Here e_v is the vertex component constant, of degree zero, and n8 is the actual invariant nilpotent section of degree eight. The constant is already a global section on U, so its boundary restricts to zero there. The degree-eight trace of eta is therefore

    q(eta)_degree8 = beta delta(n8).                (5)

The ordinary square-ideal sequence identifies delta(n8) with the nonzero generator of H1(P4 O_L(-8))^G: degree-eight ambient polynomial sections lie in Sym^8(Wprime) O_L(-4), whose H0 vanishes. Thus the nonzero n8 has nonzero connecting image. This is the actual square-ideal map (3), not a different shadow with the same dimension.

ACTUAL-NORMAL-TRACE-HAS-NONZERO-NILPOTENT-COMPONENT.md proves beta!=0. Equations (3),(5) therefore show that the extracted class in H1(J_eta)^G is nonzero. Equation (4) proves that its diagonal is a nonzero multiple of [1/(uv)] or, in the u=1 coefficient chart, [1/z]. The nonzero multiple depends on the fixed actual normal-class and residue normalization; no numerical value is assigned.

Higher components of eta can still matter in later operations. In particular this leading result alone neither identifies the full normal operator cocycle nor evaluates the two endpoint quadratic P4 channels.

## Sources and verification

The actual vertex frame factors, extension, and trace identification are in ACTUAL-DEGREE-EIGHT-NORMAL-OPERATOR-QUOTIENT.md, Sections 1-4. The actual conic correction is in ACTUAL-CONIC-RESIDUE-FORCES-VERTEX-SERRE-COCYCLE.md. The nonzero coefficient beta is the new conic-neighborhood theorem cited above. The square shadow and invariant n8 are in NORMAL-QUADRATIC-BRACKET-COMPONENT-SHADOW-GATE.md.

Run python verify_normal_class_lowest_vertex_diagonal.py. It checks the exact abstract characters, line twists, triangular conjugation and trace identities. No actual coefficient, actual-instance matrix or rank is evaluated. The actual geometric identifications are explicit dependencies.
