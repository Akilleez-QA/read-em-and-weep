# A finite vertex-jet reduction of the fifth norm class

## Scope and inputs

Work with the actual cone Q, fixed positive/negative coordinate decomposition and physical-even marking. Write J for the ambient ideal of the vertex line L. Its order j corresponds to binary-cover degree 2j. Set f=a^4 h, with nonzero negative quadratic a and nonzero positive quadratic h; f has J-order two. Retain the local norm errors of [PR769 at 1599ab33ec5392433da49fcfbd0bddd5ba1482d3](https://github.com/Akilleez-QA/read-em-and-weep/blob/1599ab33ec5392433da49fcfbd0bddd5ba1482d3/research/hm/ideal-valued-fifth-norm/PROOF.md):

    w_j-w_i=f tau(c_ij),    w_i in O_Q(16),

whose class modulo ambient global scalars is the fifth norm obstruction. [PR770 at b242300110c33627eb77ee5ab36cc81fffa359e4](https://github.com/Akilleez-QA/read-em-and-weep/blob/b242300110c33627eb77ee5ab36cc81fffa359e4/research/hm/faithful-fifth-norm/PROOF.md) identifies this obstruction faithfully with the fifth adjoint boundary, and with beta4 after quotient by the second-symbol image.

Use the actual ordinary STACK square Qsq=pi_*(I_Z^2(6)), not the square of a coarse ideal. The pinned [square-filtration theorem at 8d8b5be4ce62c3055bb53be9e16d29cc63072f04](https://github.com/Akilleez-QA/read-em-and-weep/blob/8d8b5be4ce62c3055bb53be9e16d29cc63072f04/research/hm/order-four-quadratic-load/POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md) gives the vertex square quotient R_L, J^6 R_L=0, physical-even graded pieces in orders 0,2,4, and the top relation sequence

    0 -> P4 O_L(-2) -> Sym8 U tensor O_L(2) -> Q4(6) -> 0.

The new assertion is a finite-jet reduction of the norm errors BEFORE source division. It does not evaluate the resulting class.

## 1. Separate the vertex without losing the obstruction

Let A_L=ker(O_Q(6) -> R_L). Then J^6 O_Q(6) is contained in A_L. The conic and vertex square supports are disjoint. In the physical-even sector the conic quotient is O_C(6), and its entire space of global sections lifts by cover-degree-twelve ambient sextics, which vanish on R_L because J^6 R_L=0. Consequently

    H1(Qsq)_+ -> H1(A_L)_+

is an isomorphism. This follows either from the two restriction cokernels, using H1(O_Q(6))=0, or directly from the pinned conic normalization. Thus we may use

    C_L=O_Q(16)/(f A_L)

instead of the full norm quotient. Its quotient of global sections by ambient scalars is H1(A_L), since multiplication by the non-zero-divisor f identifies A_L with its image and H1(O_Q(16))=0.

## 2. Strict source multiplication, including zeros of a

The associated graded ambient algebra along L is the even binary polynomial algebra over O_L, with its line-bundle twists. It is a domain locally on the integral line. The leading form of f is the nonzero section a^4 h of order two. Multiplication by it is injective on every ambient graded piece as a sheaf. This remains true at zeros of a: a nonzero local equation on the smooth integral line is a non-zero-divisor, although not a unit.

It follows that multiplication by f is strict for this filtration:

    (f O_Q(6)) intersect J^8 O_Q(16) = f J^6 O_Q(6).

Indeed a local section with order less than six has a nonzero leading form whose product with a^4h is nonzero, and therefore its product has order less than eight. This is a sheaf statement; it is not division over C(L). Since J^6 O_Q(6) is contained in A_L, we obtain

    (f A_L) intersect J^8 O_Q(16) = f J^6 O_Q(6).       (1)

Away from L the same equality is immediate because J is the unit ideal.

## 3. High norm tails are globally removable

The physical-even restriction map

    H0(O_Q(6))_+ -> H0(O_Q(6)/J^6 O_Q(6))_+

is surjective. In fact the ambient coordinate splitting on the vertex thickening gives precisely the three even pieces

    O_L(6),  Sym4 U tensor O_L(4),  Sym8 U tensor O_L(2),

and each is lifted by its corresponding global homogeneous polynomial piece. This ambient splitting does not assert a splitting of the actual square quotient. Together with H1(O_Q(6))=0, it proves

    H1(J^6 O_Q(6))_+=0.                              (2)

Put C_<16=O_Q(16)/(f A_L+J^8 O_Q(16)). By (1), the kernel T of C_L -> C_<16 fits into

    0 -> f J^6 O_Q(6) -> J^8 O_Q(16) -> T -> 0.

Multiplication by f identifies the first term with J^6 O_Q(6). Equation (2) therefore says that every even global section of T lifts to an ambient global section of J^8 O_Q(16).

Hence the natural map

    H0(C_L)_+/im H0(O_Q(16))_+
       -> H0(C_<16)_+/im H0(O_Q(16))_+                (3)

is injective. To verify this directly, subtract an ambient lift of a class whose image is ambient; the remainder is a global section of T, hence ambient by (2). The domain of (3) is the actual norm obstruction space. Thus norm errors with the same truncation below cover degree sixteen determine the same fifth obstruction. In particular, a globally defined norm class represented entirely in cover degree at least sixteen is zero. This conclusion does not assume any homogeneous generators for I_Z, nor any filtered choice in source-divisor normalization.

## 4. Only the cover-degree-twelve norm block can contribute

The smallest physical-even order of A_L is four, corresponding to cover degree eight. Therefore f A_L has smallest even order six, corresponding to cover degree twelve. Modulo J^8 its even part consists only of this order-six relation image. All lower even blocks of the local w_i glue globally in the ambient vertex thickening. They can be removed by ambient polynomials, since the relevant coefficient bundles at twist sixteen have nonnegative degrees.

After this subtraction, only the cover-degree-twelve block remains in (3). The cover-degree-eight block in particular is removable; it is a section of

    Sym8 U tensor O_L(12),

and is lifted by the corresponding global polynomial. Any lower scalar blocks arising from a different choice of scalar lift are removable by the same argument. The relation image in the degree-twelve block is the actual leading multiplication of a^4h with the degree-eight square relation. One must retain this image as a sheaf along the whole L; replacing a by a generic invertible scalar loses the obstruction.

This is a precise finite-jet statement: truncating modulo J^8, discarding the globally liftable blocks below order six, and retaining the order-six relation image does not discard any fifth norm obstruction. No assertion of a globally homogeneous splitting of the square thickening is used.

## Contribution and limits

The cover-degree-eight norm-error block cannot detect the fifth norm obstruction: it is ambient-removable. Only the cover-degree-twelve norm-error block can contribute; higher norm tails are rigorously excluded using strict source multiplication and global cohomology, rather than informal division by h or a. No reduction to particular matrix jets is asserted.

The actual cover-degree-twelve norm class and its membership in the second-symbol image remain unevaluated. No beta4 nonvanishing, higher lift existence, or algebraicity conclusion is made. The proof uses only structural sheaf, filtration and cohomology reasoning, with no selected actual coefficients, points, derivatives, matrices, ranks, or large computation. It is an authored proof, not proof-assistant verification.
