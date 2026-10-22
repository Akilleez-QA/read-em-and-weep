# Independent review

Status: PASS, including the full cochain elimination in Section 5.

The review checked the geometric argument against the source-completion
criterion, the two published cone-closure arguments quoted in the proof,
the abstract character calculation, and the affine-family interpretation.
This is mathematical review plus bounded exact arithmetic, not proof-assistant
certification or evaluation of an actual HM instance.

## Geometry and source input

The first kernel sequence is the inverse image of H0(Pcal(4)) under the
surjective restriction map from ambient skew sections. Its kernel is exactly
q H0(sp(E)(2)). The second sequence is exact on sections because the rank50
bundle Ncal(4) is acyclic. These facts justify addition of characters without
assuming a global splitting of the monad or parabolic bundle.

The published preserving-cone proof gives precisely N(A+D) only for preserving
sections. The separately published moving-line proof forces every even adjoint
to preserve the filtration, using the ordinary square ideal and the cubic
relation. Combining both is necessary and sufficient for the input
H0(B_Q(4))_+=A+D. The draft does combine them and does not infer this from
only one conditional statement.

The character formulas have the correct twists: E(4) uses symmetric powers
3,2,1 and E(2) uses 1,0; subtracting restriction by invariant q gives the
formula printed for E_Q(4). The skew twist-two symmetric-square complex has
only its first two terms with nonzero global sections. Delta is trivial as a
Gamma character, but the geometric determinant factor is not discarded.
Changing the simultaneous source/middle scalar parity convention leaves
S E and Lambda^2 S unchanged and hence does not alter Ncal or skew characters.

## Independent dimension and family cross-check

Besides running verify.py successfully, the family dimensions can be checked
without the full irreducible decomposition. On A5 the parameter P2 has
character30 at identity,2 at involutions, and0 at both order-five classes and
order-three elements. Therefore, for every center-even representation M,

    dim Hom_Gamma(P2,M) = (dim M + trace_M(g))/2,

where g is an involution in A5, lifted to an order-four element of Gamma.

At the central element z, H has eigenvalues (1,1,1,-1,-1), U has trace-2,
and S has trace1. Thus O_Q(3) has trace2, E_Q(4) trace10, and Lambda^2 S
trace-2. Ncal consequently has trace14 and ordinary dimension2050, giving
its even dimension1032. At the order-four lift, H has eigenvalues
(1,-1,-1,i,-i) and U trace0; all G_i have trace0, and Lambda^2 S has trace0.
It follows that the trace of Ncal_+ there is0, so its family dimension is516.

For sp(E)(2), the central trace is26 and ordinary dimension850, yielding
even dimension438. At the order-four lift Sym^2 G_0 has trace2 and H trace-1,
while G_1 G_0 has trace0. Its even trace is-2, giving family dimension218.
The A+D contribution has dimension8 and involution trace0, hence family4.
Their sums are1478 and738. Subtraction from the pinned ambient family1203
therefore gives465 exactly.

The source twist-four term has ordinary dimension25*70=1750, central trace6,
even dimension878, and involution trace2. Its family dimension is440.
Adding the source-lift ambiguity95 to738 gives833, and the full cochain image
has family dimension1203+440-833=810. The character decompositions printed in
the proof agree with the exact nine-class verifier.

## Affine and scope audit

For a fixed forcing, subtraction of any one solution identifies the solution
set with the homogeneous kernel. Pointwise existence on all a,h suffices for
polynomial P2-family existence: tensors a squared tensor h span
Sym^2 A tensor D by polarization, and the cochain image is linear. One can
choose a linear lift of the resulting finite-dimensional image and average
it over Gamma. No rational dependence on a or selected coefficient evaluation
is needed.

For fixed T the source ambiguity is exactly qH, and the divided V changes by
a coboundary. Conversely V is uniquely recovered from the full C because
multiplication by q is injective on ambient cochain bundles. Thus the833 count
is both the full completion-triple dimension and the homogeneous full-cochain
kernel dimension used in Section 5. It is not a gauge quotient and does not
apply unchanged if V or its class is prescribed separately.

No dimension subtraction with the distinct1095 vertex/ramification kernel
was used. No actual primitive, fourth Bockstein, higher extension, or
algebraicity conclusion is claimed. No blocker remains for the stated result.

## Additional divided-class elimination

The further consequence using the divided cohomology class is also valid.
The composite K -> H0(Pcal(4)) -> H0(B_Q(4)) is surjective. A homogeneous
completion restricts to a closed monad endomorphism inducing its corresponding
section b, and the fixed connecting convention gives

    delta_q(b)=[dC/q]=-[V].

This equality identifies the actual class-variation map, rather than merely
comparing dimensions. The source ambiguity95 changes only a coboundary.
The pinned CYCLIC-RAO-CUBIC-INJECTIVITY-AND-TWO-S4-LEGS.md, Section 1, was
read directly and explicitly supplies the established vanishing H0(B(4))=0.
The restriction long exact sequence therefore makes delta_q injective.
Its even image is isomorphic to A+D, so the equivariant P2-family class
variation has exact rank4. Its kernels have family dimensions734 for middles
and829 for full completions. The even character of the former is obtained
by subtracting A+D from K_+, not by subtracting an unrelated constraint space.

For affine forcing, a prescribed class is attainable if and only if its
difference from one attainable class lies in this connecting image; if
attainable, its fixed-class fiber has the stated kernel dimensions. A
pointwise existence theorem for individually chosen v_h does not by itself
establish that an arbitrary prescribed family of those choices is polynomial
and Gamma-equivariant. The family statement should retain that hypothesis
or use the explicit class-match criterion. No sign or normalization adjustment
of the fixed boundary is needed.
