# Marked-doublet derivative rank and its twelve-point defect

## 1. Setting, dependencies, and scope

Work over C on the fixed parameter line X=P(W*) with the physical action of G=SL2(F5), W its coordinate doublet and W' the other doublet. O(n) has its standard linearization. All one-dimensional characters of the perfect group G are trivial. All statements below use this marking, not an unmarked ordinary splitting.

The three complete immutable public inputs retained in INPUTS.json are PR1127 at 60dda5a940d5ba7ee081a86cd1b1a783a5952a39, PR1129 at d1238732f42df5c70ba4430e230428d2cf699bbe and PR1135 at 24e713fe352f4ff8f70cd2e86940afa70df99c5c. These are dependencies with written proofs, not proof-assistant certificates. PR1127 constructs the canonical saturated L=W'O(-3) in the actual E. Its retraction is not assumed to commute with the Gauss derivative. PR1129 proves that the actual derivative quotient A_q receives an injective coefficient map W'+T -> H0(A_q(3)). In particular the ACTUAL restricted morphism f:L -> A_q is nonzero. A_q=E/ker(beta_E) is locally free; its induced injection into the original ambient Q(-2) need not be saturated. No canonical-pencil ambient is substituted for that original inclusion.

We derive statements about this actual restriction using only nonvanishing and equivariance. More generally the arguments apply to any nonzero equivariant f:L -> A into a vector bundle A on X. They do not enumerate source or quotient profiles, prove that a proposed A occurs, or provide new profile exclusions. PR1135 records the invariant-divisor minimum used below; we also prove the requisite orbit facts here.

## 2. Rank-one threshold

Suppose f has generic rank one. Let B be the saturation of its coherent image in A. On a smooth curve B is a line subbundle, preserved by G because saturation is intrinsic. Write B=O(e). Any linearization differs from the standard one by a character of G, so no character twist is suppressed. The factorization L -> B is nonzero, hence

    0 != Hom_G(W'O(-3),O(e)) = Hom_G(W',Sym^(e+3) W).

For e+3<0 the right side is zero by absence of sections. For degrees0 through6, W' is absent from Sym^n W. Thus e>=4. On the other hand, if the ordinary splitting degrees of A are a1>=a2>=..., a nonzero map O(e)->A requires e<=a1. Consequently:

    If a1<=3, every nonzero f has generic rank two.             (1)

This proves only generic rank two, not fiberwise injectivity. The input coefficient injection does not claim a rank-eight primary fiber injection.

The bound is sharp for abstract equivariant bundle maps. Sym7 W=W'+T gives a nonzero two-section W' system in H0(O(7)), and thus W'O(-3)->O(4). Its common zero divisor is invariant and has degree at most7. The orbit minimum12 proved below makes it empty. This is an everywhere-surjective bundle map with kernel O(-10), with its induced equivariant linearization. It is a universal existence control, not an actual Gauss realization. In particular (1) cannot be extended to a1<=4 using these hypotheses alone.

## 3. Invariant divisors on the marked line

The projective action is the faithful A5 action on P1. A finite subgroup fixing a point is cyclic: conjugate that point to infinity, use averaging to give a common second fixed point, and embed the group in C* by the multiplier. Cyclic subgroups of A5 have orders1,2,3,5. Thus orbit sizes are60,30,20,12. Any nonempty invariant effective divisor has degree at least12.

There is precisely one orbit of size12. A5 has24 elements of order5, hence six subgroups of order5. Each such subgroup fixes exactly two points. Distinct such subgroups cannot share a fixed point because a point stabilizer is cyclic. These twelve points form a G-invariant set, and their stabilizers have order5, so they form a single orbit. Therefore an invariant effective divisor of degree12 is exactly that reduced orbit, each point of multiplicity one.

## 4. Rank-two saturation criterion

Suppose f has generic rank two and let B be its rank-two saturated image in A. The induced f:L->B is injective as a sheaf: its kernel is torsion and L is locally free. Its cokernel is torsion. Put b=deg B. Since det W'=1, taking determinants gives a nonzero equivariant map

    O(-6)=det L -> det B=O(b).

Its effective divisor D has degree delta=b+6 and is invariant. Thus delta=0 or delta>=12. The inclusion B->A induces a nonzero determinant map O(b)->wedge^2 A. Its highest ordinary splitting degree is a1+a2, so b<=a1+a2. We conclude:

    If a1+a2<=5, then delta=0 and f identifies L with B.        (2)

Indeed 0<=delta<=11, so the orbit minimum forces zero. Thus in this case the sheaf image equals its saturation, and A/f(L) is locally free. If a1+a2<-6 the same inequalities instead prohibit generic rank two altogether. Statements (1) and (2) are separate conditions: (2) assumes generic rank two; it does not assert it without (1) or another argument.

## 5. The conditional target O(-8)+W O(3)

Suppose A is equivariantly isomorphic to O(-8)+W O(3). Its positive block A_+=W O(3) is intrinsic as the top-degree subbundle; a displayed splitting is used only to describe the quotient. Degree gives Hom(L,O(-8))=0, so every f factors through A_+. The exact identity

    W tensor Sym6 W = W'+2T

gives dim Hom_G(L,A_+)=1. Thus any nonzero f is the unique channel up to a nonzero scalar; no value of that scalar is needed. By (1) it has generic rank two. Its determinant is a nonzero invariant section of O(12), because deg A_+=6 and deg L=-6. Section3 implies that its divisor is precisely the reduced twelve-point orbit.

It follows that f has fiber rank two away from these twelve points and rank one at each point of the orbit. To verify the latter assertion, use a uniformizer t in the local discrete valuation ring. If the matrix had rank zero modulo t, all four entries would be divisible by t, and its determinant by t^2, contrary to the simple zero. Since the determinant vanishes, the fiber rank is not two either. Local Smith normal form is consequently diag(1,t) up to units. The positive-block cokernel is a length-one skyscraper at each point, total length12:

    0 -> W'O(-3) -> W O(3) -> T_D -> 0,
    length(T_D)=12, support(T_D)=D reduced.

Its equivariant fiber characters are not identified here; the notation T_D does not assert an equivariant trivialization as O_D. As a plain sheaf it is locally isomorphic to O_D.

Inside the full A, the saturation of f(L) is A_+, whereas f(L) is isomorphic to L and is NOT saturated. The full cokernel fits 0->T_D->coker(f:L->A)->O(-8)->0; under the stipulated equivariant direct splitting it is O(-8) plus T_D. In particular only the positive-block cokernel has finite length. This example sits exactly outside (2): a1+a2=6 and delta=12. It proves the cutoff5 is sharp for abstract nonzero equivariant maps with this domain, without asserting occurrence as an actual derivative quotient.

## 6. Reproduction and limits

Run python verify.py and python -O verify.py. Both print the same RESULT.json. The standard-library checker authenticates all full inputs, verifies the exact nine-class character identities, first W' occurrence, degree12 invariant dimension, finite A5 orbit arithmetic and local valuation implications. These tests support the written geometric proof, not its replacement. In particular a character Hom dimension alone is not used to assume generic rank two: Section2 supplies that proof first.

No selected actual source coefficient, HM point, parameter, tensor, jet, matrix, rank experiment, scan, one-shot experiment or local-model spike is evaluated. The twelve points are specified invariantly as an orbit, not by selected actual coordinates. No compatibility of a canonical projector with Q multiplication or Gauss operations is assumed. This packet provides a conditional marked restriction theorem and sharp universal controls, not a source/profile exclusion, coverage theorem, full-adjoint invertibility or complete original proof repair.
