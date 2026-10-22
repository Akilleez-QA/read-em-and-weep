# Abstract balanced degree-eighteen systems form a projective line minus two points

## Result and exact scope

The final necessary system of PR751 (commite21d50b6bd7d124dc419beeb8c27fa3b9ef3e169) is abstractly feasible. More precisely, let G be the binary icosahedral group, W its defining representation, and

    H subset Sym18 W,    H isomorphic to A_std+V+P.

The equivariant subsystem H is parameterized by the projective line of P multiplicity lines in Sym18 W. Exactly two distinct points fail the no-linear-syzygy condition. At every other point its evaluation sequence is

    0 -> (P+D)O(-2) -> H tensor O -> O18 -> 0.

Dually this gives the required abstract balanced presentation

    0 -> O(-18) -> H* tensor O -> (P+D)O2 -> 0.

This does not assign a parameter to the fixed actual source, prove that the original source realizes any such system, or remove a quotient label. It shows that this final abstract balanced-presentation condition alone is not a no-go theorem.

## 1. The parameter line and the only variable multiplication blocks

Exact characters give

    Sym18 W=A_std+V+2P+D,
    Sym19 W=W+S+Wp+2T,
    Sym17 W=S+Wp+2T,
    A_std tensor W=W+S,
    V tensor W=T,    P tensor W=Wp+T,    D tensor W=S+T.

The A_std and V subspaces of H are uniquely determined. The P subspace is a line ell in its two-dimensional multiplicity space. Scalar changes in the irreducible identifications do not change H. Thus the subsystem parameter is exactly P1.

Consider ordinary polynomial multiplication

    m_ell:H tensor W -> Sym19 W.                       (1)

Its source and target have the same character. The W block is nonzero: full multiplication Sym18 W tensor W->Sym19 W is onto, and only the unique A_std source contributes W. Section2 proves that its S block, also from A_std alone, is nonzero.

The Wp block is a linear form a(ell) on the P multiplicity space. It is nonzero as a form, because full multiplication is onto Wp and only the two P sources can contribute it. The T block is a two-by-two multiplicity matrix. Its first column comes from the fixed V, and its second depends linearly on ell. Let b(ell) be its determinant. We will prove that b is nonzero and has a different zero from a. Therefore, up to a nonzero constant, the full ordinary determinant is

    det(m_ell)=a(ell)^2 b(ell)^6.                       (2)

This is a symbolic representation-block statement, not an actual-instance determinant computation.

## 2. A universal Clebsch identity proves the fixed S block is nonzero

Write Sym^n W as degree-n binary forms. Let f20 be any nonzero G-invariant degree-twenty form; its invariant space has dimension1. The usual polarization map

    Sym20 W -> Sym18 W tensor Sym2 W

is nonzero and injective. Its value on f20 gives the unique A_std=Sym2 W copy in Sym18 W.

Under tensor-Hom adjunction, the S=Sym3 W component of multiplication on this copy is obtained by applying the standard skew insertion on the coefficient factor, followed by multiplication on the first factor. The resulting SL2-equivariant map is nonzero. This can be checked universally on the highest-weight vector of the entire Sym20 representation, using x,y for the first factor and u,v for the coefficient factor:

    x^18 u^2  maps to  x^18 y u^3 - x^19 u^2 v.         (3)

The right side is nonzero. The map is therefore injective on the irreducible SL2 module Sym20 W. In particular its value on the nonzero invariant f20 is nonzero. This proves the S block in (1) is nonzero. The monomial in (3) tests a universal intertwiner; it is not a selected invariant or an actual-source coefficient assignment.

## 3. A second universal identity prevents an identically zero T determinant

There is the exact multiplication sequence

    0 -> Sym17 W --delta--> Sym18 W tensor W
      -> Sym19 W -> 0,
    delta(f)=x f tensor y - y f tensor x.              (4)

On T multiplicity spaces the middle term has four columns, one from V, two from P and one from D; the target has dimension2 and the kernel has dimension2.

The V column is nonzero. Indeed the unique V in Sym18 W is f12 V6, where f12 is a nonzero degree-twelve invariant and Sym6 W=V6+P6. Multiplication V6 tensor W=T->Sym7 W is nonzero, since multiplication of a nonzero polynomial by x or y is not identically zero. Hence its T map is an isomorphism onto the unique T in Sym7 W, and multiplication by f12 preserves nonzeroness.

Suppose b were identically zero. Then the V and both P columns would all land in the same one-dimensional T multiplicity line. Their three-dimensional domain would contain a two-dimensional kernel, exhausting the entire kernel in (4). Thus the full T-isotypic kernel delta(Sym17 W)_T would have zero D tensor W component.

The following universal identity contradicts that conclusion. There is a unique Sym20 summand in Sym17 W tensor Sym5 W. A highest-weight vector for it is

    t=x^17 u^4 v - x^16 y u^5.

Apply delta on the first factor, and contract W tensor Sym5 W->Sym4 W on the coefficient factors, with y tensor g mapping to -partial_u g and x tensor g to partial_v g. The result is

    t maps to -4 x^18 u^3 v + 4 x^17 y u^4,             (5)

which is nonzero. The resulting SL2-equivariant map is injective on its Sym20 summand. Apply it to f20: its image is nonzero. Since Sym5 W=T and Sym4 W=D are irreducible for G, this says exactly that a T-isotypic element of the kernel in (4) has nonzero D tensor W component. This contradicts the preceding consequence of b=0. Therefore b is a nonzero linear form.

Equations (3) and (5), checked as formal polynomial identities, are the only extra Clebsch nonvanishing inputs beyond exact characters and polynomial multiplication.

## 4. The two exceptional lines are distinct

Take the multiplicity line ell0=f12 P6. The T images of both V18=f12 V6 and this P copy lie in the single T copy inside f12 Sym7 W. Hence b(ell0)=0.

But a(ell0) is nonzero. Full multiplication Sym6 W tensor W->Sym7 W is onto Wp, and V6 tensor W=T has no Wp component. Therefore P6 supplies Wp nontrivially, and multiplication by nonzero f12 preserves it. Thus a and b have distinct projective zeros.

It follows that precisely two parameter points fail (1): at the b-zero the linear syzygy character is T, while at the a-zero it is Wp. Their dimensions are6 and2 respectively. Everywhere else (1) is an isomorphism. No parameter point in this nonempty open set is chosen or identified with an actual source.

## 5. No linear syzygies is exactly the balanced presentation

For a parameter outside the two exceptional points, H is basepoint-free. If all its forms vanished at a point, all of H tensor W would also vanish there, contradicting surjectivity onto Sym19 W. Its evaluation kernel F is therefore locally free of rank9 and degree -18. The isomorphism (1) says H0(F(1))=0. Thus every ordinary splitting degree of F is at most -2; their sum is -18, forcing all nine to equal -2.

The coefficient representation is recovered from the evaluation sequence:

    H1(F)=Sym18 W/H=P+D.

Therefore F=(P+D)O(-2). Conversely, this splitting has H0(F(1))=H1(F(1))=0, so the multiplication map (1) is an isomorphism. This proves the claimed exact classification of the abstract balanced locus.

## Reproduction and restrictions

Run `python3 verify_abstract_degree_eighteen_balanced_systems.py` to produce `abstract-degree-eighteen-balanced-systems.json`. The standalone checker pins PR751's note, verifies all exact characters and multiplicities, and checks the two universal highest-weight polynomial identities and the final rank/degree/cohomology identities. The proof supplies the semisimple multiplicity-space argument and its geometric consequence.

This is a universal symbolic calculation. No group-invariant form's coefficients, actual-source coefficients or parameter point are selected. No actual-instance matrix/rank evaluation, scan, spike or consumed experiment occurs. The original quotient label and its same-source realization problem remain unresolved by this result.
