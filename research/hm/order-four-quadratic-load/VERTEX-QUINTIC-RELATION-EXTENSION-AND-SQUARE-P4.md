# The nonsplit quintic relation extension and the square-shadow P4

## Results

Use the actual spinor quotient over the negative line L=P(W), with the unique vertex module and its globally constant Loewy layers (W',A,W') O_L(2). The graded cubic and quintic relation bundles are

    K3=O_L(-2) subset Sym^3 W' O_L(1),
    K5=P4 O_L(-1) subset Sym^5 W' O_L.

The cubic multiples inside K5 give the exact sequence

    0 -> V O_L(-3) -> P4 O_L(-1) -> O_L(5) -> 0.  (1)

This sequence is necessarily nonsplit. Its equivariant extension space is one-dimensional, so it is the unique nonzero equivariant extension of this form, up to scalar identifications. In particular one must not replace the quintic relation by a single globally chosen binary quintic with polynomial base coefficients.

Let Q4 be the cover-degree-eight graded quotient of the even ordinary square-thickening algebra. Then

    0 -> P4 O_L(-8) -> Sym^8 W' O_L(-4)
      -> Q4 -> 0,                                 (2)

and twisting by six gives

    0 -> H0(Sym^8 W' O_L(2)) -> H0(Q4(6))
      -> P4 -> 0,                                 (3)

with dimensions 27,31,4. Thus the exact P4 square-shadow obstruction is canonically H1(P4 O_L(-2)). This supplies a specific relation bundle for the remaining smoothing comparison. It does not, by itself, identify that comparison with a nonzero map, so gamma nonvanishing is not asserted.

## 1. Global graded source and uniformity

For the negative projection, the odd spinor S(2) has graded terms

    Sym^(2n+1) W' tensor O_L(2-n), n>=0.

The positive coordinate generators are V O_L(-1). The actual vertex quotient has the global three-step associated graded W'O(2), AO(2), W'O(2). The global constancy follows from the unique normalized module: each collective action is generically onto its indicated constant-representation bundle, and a failure divisor would be G-invariant of degree at most3 or2, smaller than the minimum orbit size12.

The quotient and its Loewy graded pieces are therefore flat over L. Base change preserves the exact odd-spinor quotient. At every base point it has odd Loewy dimensions 2,3,2 and two odd generators, from the actual rank-two locally free middle term. The elementary local argument in VERTEX-EXT-ANNIHILATOR-LENGTH-EIGHT.md consequently applies fiberwise: the leading generators have orders3 and5 and are coprime. Thus the graded relation spaces used below have constant ranks at all fibers; no exceptional point or generic-only identification is suppressed.

## 2. Cubic and quintic kernels

The cubic map is the nonzero universal channel

    Sym^3 W' O_L(1) -> A O_L(2).

Its kernel is K3=O_L(-2), by the dual complete-cubic evaluation sequence proved in UNIVERSAL-CUBIC-EVEN-DEFECT-QUOTIENT-IS-TRIVIAL-V.md.

The quintic map is the nonzero channel

    Sym^5 W' O_L -> W' O_L(2).

Its global Hom space is one-dimensional because Sym^5 W'=T6=W' tensor A. Under that representation isomorphism it is id_W' tensored with the complete quadratic evaluation A O_L -> O_L(2), up to a nonzero scalar. It is therefore onto at every point. The quadratic evaluation kernel is W O_L(-1), so

    K5=W' tensor W O_L(-1)=P4 O_L(-1).             (4)

Nonvanishing of the quintic channel follows from the actual nonzero second Loewy layer; no value of the channel is evaluated.

Multiplication of the cubic relation by the positive degree-two forms gives a subbundle

    V O_L(-1) tensor K3=V O_L(-3) -> K5.

It is fiberwise injective because the cubic polynomial is nowhere zero. Its cokernel is a line bundle, since each fiber has a single independent quintic generator modulo the cubic multiples. Determinants in (4) give its degree5. Perfectness of G removes a character ambiguity, proving (1).

## 3. The generator extension is nonzero and canonical

If (1) split, its quotient O_L(5) would admit a nonzero map into P4 O_L(-1). But

    Hom(O_L(5),P4 O_L(-1))=P4 tensor H0(O_L(-6))=0.

Thus its class is nonzero. Its equivariant extension space is

    [V tensor H1(O_L(-8))]^G
      =[V tensor Sym^6 W]^G,

which is one-dimensional because Sym^6 W=V plus P4. Twisting (1) by one also identifies it as the evaluation sequence of the P4 subseries of binary sextics:

    0 -> V O_L(-2) -> P4 O_L -> O_L(6) -> 0.

The map on global sections is the unique inclusion P4 into Sym^6 W. Its series is basepoint-free: an invariant base divisor would have positive degree at most six, while every nonempty orbit has at least twelve points. This gives a second geometric identification of the same nonsplit extension.

## 4. The square relation in cover degree eight

Locally write the regular odd pair as f=f3+f5+..., g=g5+..., with f3,g5 coprime. The cover-degree-eight initial space of the ordinary square (f,g)^2 is exactly

    f3^2 Sym^2 W' + f3 g5 = f3 K5.

Indeed a leading degree-six contribution can come only from a constant multiple of f3^2. To obtain order at least eight that coefficient must vanish; the next possible terms are precisely a quadratic multiple of f3^2 and a constant multiple of f3 g5. Higher terms of f and g do not create an additional initial relation. Coprimality gives the expected rank four.

The twists are essential. K3 lies in the degree-three piece of S(2), K5 in its degree-five piece. Multiplying two odd spinor sections and passing to an ordinary function divides by the reflexive square S(2)^[2]=O(5). Hence

    K3 tensor K5 tensor O_L(-5)=P4 O_L(-8)

maps into the ordinary cover-degree-eight coordinate piece Sym^8 W' O_L(-4). Its image is exactly the square relation bundle. This proves (2). Fiberwise injectivity follows from the nowhere-zero cubic and the constant rank of K5.

Twist (2) by six. The left bundle becomes P4 O_L(-2), the middle becomes Sym^8 W' O_L(2). Their H0/H1 immediately give (3), with H1(Q4(6))=0. This cohomology calculation is independent of choosing any quintic-generator lift of (1).

## 5. Obstruction target and subsequent first-order vanishing

The actual even square-shadow obstruction on the cone is P4. Formula (3) realizes it as H1(P4 O_L(-2)). The nonzero generator extension and nonzero cokernel do not alone determine any smoothing coefficient.

Subsequently POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md proves the actual first smoothing map is zero, including gamma. POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md uses the relation bundle above to identify the actual second obstruction: its D5 input vanishes and its A input is a Serre-dual contraction. No first-order nonvanishing is asserted. The remaining task concerns higher obstructions and generic positive surjectivity.

## Evidence

Inputs are INVARIANT-CONE-UNIQUE-VERTEX-MODULE.md, VERTEX-EXT-ANNIHILATOR-LENGTH-EIGHT.md, UNIVERSAL-CUBIC-EVEN-DEFECT-QUOTIENT-IS-TRIVIAL-V.md, and WEIGHTED-STACK-SQUARE-SHADOW-AND-PRIMARY-SCALAR.md. All multiplication maps in this note are universal equivariant channels forced by the actual quotient; no actual coefficients or selected matrices are evaluated.
