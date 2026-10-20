> Current actual-bundle specialization: the degree-one-kernel exclusion rules out a=1. The a=1 formulas below are historical conditional algebraic derivations, not current actual alternatives.

# Line-and-ideal-square factorization of the square detector

## Inputs and scope

Work over C. Retain the actual regular embedding i:W=P²→Y=P⁴, ambient G=B(-1), E=i*F with det(E)=O_W(-2), c₂(E)=16, and B_W=End₀(E). Thus G_W=B_W(-2). All twists below on W are plane twists. We use the audited bound that every saturated line O(a)⊂E has a≤1. The square detector is the transpose of r_W:H²(Y,G)→H²(W,G_W).

If H⁰(B_W(-1))=0, this detector is zero. Otherwise there is a unique saturated line K=O(a) of nonnegative degree, a=0 or1, and an actual extension

    e: 0→K→E→I_Z⊗T→0,
    T=det(E)⊗K⁻¹=O(-2-a), length Z=a²+2a+16.

The constructions below retain this extension and its inclusion, not merely a, Z, or a vector space of dimension3/10. No actual HM matrix or rank is evaluated.

## 1. The entire negative module and its vanishing bound

Put N=K⊗T⁻¹=K²⊗det(E)⁻¹=O(2a+2). Quotient, inclusion I_Z⊂O, and inclusion K⊂E give a canonical nilpotent injection j:N→B_W. Its value is the homomorphism E→I_Z T→T→K→E with the N coefficient understood.

For every integer k>0, a nonzero f:E→E(-k) has zero trace and determinant and satisfies twisted Cayley–Hamilton f(-k)f=0. Its saturated kernel O(b) produces a nonzero section of O(2b+2-k), hence b≥0. Therefore it is K by uniqueness. Conversely every section of N(-k) gives such an f. Consequently

    H⁰(B_W(-k)) = j H⁰(N(-k)), k>0.

If no nonnegative saturated line exists all these spaces vanish. In particular H⁰(B_W(t))=0 for t≤−5, universally. For a=0 the only nonzero negative twists are k=1,2, of dimensions3,1; for a=1 they are k=1,2,3,4, of dimensions10,6,3,1.

These identifications commute with multiplication by homogeneous polynomials whenever both twists stay negative. All compositions of these negative-twist endomorphisms are zero, since they factor through the same quotient and line. Equivalently this is the strictly-negative portion of the graded line module H⁰_*(N), with square-zero endomorphism composition; it is not claimed to be closed under polynomial multiplication into nonnegative twists.

## 2. A scalar ideal-square quotient, not just parameter renaming

Trace pairing dualizes j to c:B_W→N⁻¹. Its scheme-theoretic image is

    image(c)=I_Z²⊗N⁻¹.

Indeed, locally trivialize K and E and write the inclusion as v=(x,y). The quotient is the ideal (x,y), and Z is locally a complete intersection: at its points x,y form a regular sequence because E is locally free and Z is zero-dimensional. The nilpotent matrix is, up to a consistent sign,

    [ -xy   x² ]
    [ -y²   xy ].

For a trace-free matrix [u v;w -u], its trace pairing with this matrix generates the ideal (x²,xy,y²); the coefficient2 is invertible. Thus the image is the ordinary ideal square, including its scheme structure. The doubled zero scheme defined by I_Z² has length3 length(Z), namely48 or57, by I_Z/I_Z² locally free of rank2 over O_Z.

More precisely there is an exact sequence

    0→K⊗E⊗det(E)⁻¹→B_W→I_Z²⊗N⁻¹→0.           (1)

Under B_W≅Sym²E⊗det(E)⁻¹, the first arrow is symmetric multiplication by the section K→E; the last arrow is the square of the quotient E→I_Z T, up to the trace-pairing scalar convention. Locally the two syzygies of (x²,xy,y²) generate the kernel. This also proves exactness at the nonreduced points of Z; one cannot replace I_Z² by a line bundle there.

Twisting (1) gives the particularly simple sequence

    0→E(a)→B_W(-2) --c'→ J→0,
    J=I_Z²(-2a-4).                                (2)

Furthermore H²(E(a))=H⁰(E(-a-1))*=0: twist the defining extension by -a-1, whose outer terms are O(-1) and I_Z(-3-2a), both without sections. Hence

    H²(B_W(-2)) --H²(c')→ H²(J)
                      ≅ H²(O(-2a-4))             (3)

are isomorphisms. The latter equality uses the zero-dimensional quotient by I_Z². This is an independent cohomological verification of the detector-space identification.

## 3. Exact ambient factorization and vanishing criterion

Let u:G→i_*G_W be actual restriction and set

    v_e = i_*c' ∘ u : G→i_*J.

Then the entire ambient detector, with the line-coordinate source, is precisely

    H⁰(N(-1)) = Ext²_Y(i_*J,ω_Y)
        --v_e*→ Ext²_Y(G,ω_Y)=H²(Y,B(-4)).         (4)

Indeed regular-embedding duality gives Ext²_Y(i_*J,ω_Y)=Hom_W(J,ω_W). Since Hom(I_Z²,O_W)=O_W, this is H⁰(O(2a+1)). Pullback along c' identifies this space with H⁰(B_W(-1)) via j. Thus (4) is the original Gysin detector, not an alternative ambient functional.

For any actual ambient class η the following exact scalar-ideal criterion holds:

    r_W(η)=0  iff  H²(v_e)(η)=0 in H²(J).

Equivalently test it against every polynomial in H⁰(O(2a+1)) using Serre duality for J. The ideal-square quotient and exact rank-two kernel (2) provide genuine additional structure; no evaluation of v_e is implied. In particular the abstract Z and length do not determine v_e: the actual extension e, inclusion K→E, embedding i, and ambient restriction remain in its definition. Rank is not determined by dimensions or (3).

## 4. The ribbon already detects every extendable global section

Let C be the fixed smooth conic with equation q, and D=mC. The quotient B_W/jN is torsion-free on W. Locally the three entries of j have no common codimension-one factor; a rank-one subsheaf of a vector bundle with this property is saturated on the smooth surface. Thus tensoring j with O_D remains injective for every m≥1. Write

    j_D:N(-1)|D ↪ B_W(-1)|D.

For the actual global detector sections the restriction kernel is exactly

    ker[H⁰(B_W(-1))→H⁰(D,B_W(-1)|D)]
       = q^m j H⁰(O(2a+1-2m)).                  (5)

This follows either from the divisor sequence and the negative-module formula, or from injectivity of j_D. In particular:

- a=0: restriction to C is injective and its image has dimension3.
- a=1: restriction to C has kernel q H⁰(O(1)), dimension3, and image dimension7.
- For either a: restriction to 2C is injective, distinguishing all3 or10 actual global detector parameters.

There is also a precise finite extendability criterion, stronger than uniqueness alone. Restriction

    H⁰(W,N(-1))→H⁰(2C,N(-1)|2C)

is an isomorphism, since its kernel is H⁰(O(2a-3))=0 and H¹ of any plane line bundle is zero. Therefore

    image[H⁰(W,B_W(-1))→H⁰(2C,B_W(-1)|2C)]
           = H⁰(2C,j_2C(N(-1)|2C)).              (6)

A section on 2C extends to W if and only if its image in the quotient by this actual line subsheaf is zero; the extension is then unique. Its coefficient extends uniquely as a plane linear form (a=0) or cubic (a=1). Composing that inverse coefficient restriction with (4) gives an exact 2C realization of the ambient detector on the subspace (6).

This does NOT identify all H⁰(2C,B_W(-1)|2C) with global sections. The earlier8C result established existence and uniqueness for the full section space; here the actual restricted nilpotent line supplies the additional extendability test. Knowing only the splitting of E|C or an arbitrary line on 2C does not supply that subsheaf.

## 5. Zero-scheme intersection explains reduced-conic saturation loss

Let R=Z∩C scheme-theoretically. On the smooth curve C it is an effective divisor, locally with I_Z O_C=(t^r). The restricted K→E|C vanishes to order r; its saturated line is K|C(R). The nilpotent matrix entries therefore have common factor t^(2r). Consequently the saturation of j_C(N(-1)|C) in B_W(-1)|C is

    N(-1)|C(2R),

and the saturation quotient has length2 length(R). This finite torsion is extra apparent freedom if one replaces the actual image by its saturation; it is not extra globally extendable detector data. The quadratic multiplicity agrees exactly with the I_Z² contraction in (1).

For 2C, keep the actual entries modulo q² and their actual image rather than substituting reduced-curve saturation: nilpotent transverse data and the extension can matter. Formula (6) is valid without any transversality assumption on Z and C. If C avoids Z, the nilpotent line is already a subbundle on C and2C, but the a=1 three-dimensional kernel in (5) still exists; it comes from divisibility by q, not from intersection torsion.

## Boundary

This proves a scalar ideal-square factorization, a universal negative-twist vanishing, and a necessary-and-sufficient line-membership criterion on2C. It selects neither a nor the actual rank or value of the ambient map.
