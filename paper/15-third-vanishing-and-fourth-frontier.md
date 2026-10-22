# 15. The actual third Bockstein vanishes; the fourth-order frontier

## 15.1 The theorem and its precise target

**Theorem.** For the actual positive HM pencil, the cubic third gate is zero:

    Ψ: D5 O_(P(A))(−3) → I_Σ(6),       Ψ = 0.

Moreover the specialized third Bockstein vanishes in every projective smoothing direction, including the additional A-kernel line at each of the six second-symbol axes. The [integrated proof][T] supplies this specialization statement separately; it is not inferred by assuming kernel formation commutes with base change.

Here Ψ denotes the final cubic gate, after the actual second-symbol quotient. Earlier chapters also use Ψ for the secondary tensor or its unquotiented P4 value; this theorem does not say that every input to that tensor, every lower vector class, or every local residue is zero. The generic section count remains four or five. No fourth coefficient, generic surjectivity, or complete original repair is proved.

## 15.2 Why changing the meromorphic source computes the same actual class

The [source-change theorem][SC] proves both the complete finite cocycle identity and its full coefficient-frame covariance. With a fixed global positive binary basis, z=t/s and the oriented opposite coordinate v=−1/z, the actual source relation and effective scalar have affine transformations

    m_y=z²m_x−3zh,
    Γ_y=z^(−2)Γ_x−4kz^(−3)a_x²h.

The derivative of the transition coefficient contributes another inhomogeneous term. In the complete vector formula, its contribution together with that of m is exactly canceled by the affine Γ contribution. Thus R_y=z⁶R_x, the transition of V O_L(−6). The nonzero Atiyah scalar, Gram primitive, and source-versus-target convention are all retained.

If two global meromorphic normalized quintic generators differ by ℓf, their source coefficients differ by −ℓn and their Gram primitives by τ(ℓ,n). The finite cocycle identity says their vector principal parts differ by those of one global meromorphic section of V O_L(−6). They therefore give the same vector-cohomology class in H¹(V O_L(−6)), even before its connecting A quotient. This effective comparison does not identify the full lower C/J₀ class; see [Section 16.3](16-canonical-fourth-input-and-complete-test.md#163-what-the-lower-vector-shadow-actually-retains). This is not an assertion that arbitrary local scalar differentials glue globally.

In a fixed global positive Gram identification, q₀=ν₀q with one nonzero constant ν₀. Both equations acquire the same factor in induced relative frames. The physical representative R/ν₀ is retained; an arbitrary nonconstant equation factor cannot be inserted without transporting the numerator and bundle frame too.

## 15.3 The square channel is zero, despite a nonzero lower class

The [divisor-defined two-chart construction][D] gives a meromorphic lift of the actual nowhere-zero quintic on the cubic support. Its source relation, canonical scalar correction and unique Gram primitive are the actual ones. For a=t² and the detectable input h=X⁴ at an arbitrary C5 stabilizer pair, its principal parts are

    R_x/ν₀ = αY²z^(−2)/ν₀,
    R_y/ν₀ = −4αY²v^(−4)/ν₀,       α ≠ 0,

modulo regular terms. Cup by a makes the first regular; the second becomes the principal part of a global meromorphic section of V O_L(−4), with constant x expression −4αY²/ν₀. The cup is therefore zero already in H¹(V O_L(−4)) for this detectable input.

Only this input can reach the final square quotient by the C5 character calculation. The other inputs vanish in that quotient, not necessarily before it. The square restriction lies in a unique equivariant channel D5→Sym¹⁸W, and every nonzero member is basepoint-free. Its zero full fiber therefore forces the whole actual square channel to vanish. [Square-vanishing proof][S].

The lower class need not be zero: after one global meromorphic subtraction, its sole principal part is −5αY²v^(−4)/ν₀ in V O_L(−6), nonzero even modulo the connecting A by its character. This also explains why [Section 13.9](13-canonical-diagonal-and-vector-cochain.md#139-a-uniform-c5-simple-root-and-a-nonzero-opposite-pole-contribution) remains correct. A nonzero full opposite-pole residue in the orthogonal representative is compatible with cancellation in the global final sum. The earlier open residue-sum question is closed, not the local nonvanishing theorem retracted.

## 15.4 Actual cokernel-fiber vanishing at the six axes

At a semisimple C5 axis a=st, the [axis calculation][A] uses the same divisor-defined source but recomputes the actual scalar correction and Gram primitive for h=XY³. In its abstract coefficient-line notation, the primitive is A/(Bc) z^(−4), not zero. These A,B are tensor-line symbols in the source proof, not the representation A or the adjoint bundle B.

The complete cochain has

    principal_part_x(R)=α₁XYz^(−6)+α₂XYz^(−1),
    R_y regular.

Cup by a=z leaves only α₁XYz^(−5) as a pole. Its upper y-frame expression is −α₁XYv, regular. Thus the actual cup is exact before both the connecting D5 quotient and the second-symbol quotient. The normalizer gives the other detectable input h=X³Y. The actual second-symbol cokernel has weights 4,6, so every other input vanishes there by characters.

This proves zero in the actual fiber

    I_Σ(6)/m_p I_Σ(6) = coker(β₂,p),

not ordinary evaluation in O(6), which would already vanish automatically on Σ. This distinction supplies the extra order of vanishing needed next.

## 15.5 Six length-four ideals and the septic-conic argument

The [six-axis geometry][G] proves that β₂ has rank two at every axis. The normalizer allows rank zero or two, while rank zero at six points would force total degeneracy length at least 36, contradicting length Σ=24. The tangent weights 2,8 cannot map the weight-zero kernel to the cokernel weights 4,6. Hence the local ideal has no linear terms.

Its two residual generators have colength at least four. The six points exhaust length 24; their quadratic weights force nonzero initial terms x²,y². Thus Σ consists exactly of six length-four complete intersections with local ideals (x²,y²), not six reduced points or the ordinary double-point ideals m².

Square vanishing gives Ψ=δΨ₁, where each component of Ψ₁ is a degree-seven form in I_Σ. The discriminant δ is a unit at each semisimple axis. Actual fiber vanishing therefore gives membership in m_p I_Σ,p ⊂ m_p³, not just in I_Σ,p.

The six axes have no three collinear and lie on no conic. For each omitted axis, the conic through the other five is irreducible; the six conics are distinct. A septic with triple zeros at all six axes meets each such conic with multiplicity at least 15, exceeding the Bézout degree 14 unless the conic is a component. Six such components have total degree 12>7. Every component of Ψ₁ is consequently zero, proving Ψ=0.

## 15.6 Specialization and the remaining finite exponent

Away from the six axes the second symbol has rank three, so its kernel is exactly D5. At an axis, rank two leaves one additional A-kernel line of weight zero. The direction a also has weight zero, whereas the specialized cokernel has weights 4,6. The cubic third differential is equivariant and therefore kills this extra line. Equivariant lift choices exist by finite-group averaging. There are no other rank-drop points by the length-four classification. This completes the statement about every specialized third Bockstein.

For a general direction the positive pencil has 33 unit Smith factors and three factors of valuation two. Its last row either remains zero, giving a permanent cokernel and five positive sections, or has finite Smith exponent e. Third vanishing gives e≥4; the degree bound on a nonzero maximal minor of the 37-row linear pencil gives

    6+e ≤ 37,       hence 4 ≤ e ≤ 31.

A nonzero correctly iterated fourth or later obstruction would give rank 37 and four sections. The fourth coefficients have not been evaluated. A permanent cokernel would give rank 36 and five sections. Neither outcome is selected here, and neither would by itself complete source recovery, lifting, or Weil-class algebraicity.

## 15.7 The corrected fourth representative and its four channels

The [fourth-order reduction][F4] fixes an equivariant Schur reduction with residual map

    F(t,a)=t²B₂(a)+t³B₃(a)+t⁴B₄(a)+⋯.

The actual second symbol β:A O(−2)→P4 O is injective as a sheaf, despite its rank-two fibers at the six axes. Third vanishing therefore gives a unique polynomial linear correction

    L:D5 O(−3)→A O(−2),       B₃|D5=βL.

Its equivariant coefficient space is one-dimensional relative to the fixed reduction. This lifting correction is distinct from the first-normal variation map called L in Section 4.11. The later canonical raw-cubic theorem proves a nonzero L_can for the fixed actual probe; [Chapter 16](16-canonical-fourth-input-and-complete-test.md) supplies that normalization and its comparison boundary. The arbitrary Schur correction L must be transported before identifying it with L_can; independence from changes of Schur reduction is not asserted. Correcting the source by h−tL(a)h gives the fourth representative

    W₄(a)h = B₄(a)h−B₃(a)|A L(a)h

modulo the actual second-symbol image, not B₄|D5 alone. This D5 family does not describe the fourth value on the extra specialized A-kernel line.

Equivalently, in the source proof's convention q₀−ta, the actual ambient identities q₀ζₐ=aξ and q₀vₕ=ahζₐ give a linear b(a,h)∈A with [avₕ]=[abζₐ]. The next division and fourth class are

    q₀wₕ=a(vₕ−bζₐ),       [awₕ] modulo im β₂,ₐ.

The correction b agrees with L only in compatibly chosen Schur coordinates. This sign convention is stated explicitly rather than silently substituted into Section 4's q₀+ta formula.

The fourth gate has target H⁰(I_Σ(10)), whose character is 1⊕A⊕2V⊕3P4⊕4D5 and dimension 42. Thus there are four allowed equivariant coefficients. The discriminant exact sequence divides them into two square-visible and two discriminant-divisible channels. Unlike third order, the square part is not one-dimensional. These are structural reductions only: none of the four actual coefficients has been evaluated. The [supplementary verifier][F4V] checks the formal extraction and character arithmetic.

## 15.8 Evidence boundary

The proof uses exact actual-source, full-frame, normal-operator and cokernel comparisons, followed by geometry. The [integration verifier][V] reruns the universal source/frame, square, axis and six-point checks and checks the extra-kernel character and Smith bounds. Symbolic identities use arbitrary nonzero tensor-line symbols, not selected HM coefficients or actual-instance map/rank experiments. These supplementary checks do not replace the geometric arguments or constitute proof-assistant certification.

## Pinned source references

[T]: https://github.com/Akilleez-QA/read-em-and-weep/blob/86e5aed779f0ff64a83cf9dbe169cb2e7283b346/research/hm/order-four-quadratic-load/ACTUAL-THIRD-BOCKSTEIN-VANISHES-IDENTICALLY.md
[SC]: https://github.com/Akilleez-QA/read-em-and-weep/blob/86e5aed779f0ff64a83cf9dbe169cb2e7283b346/research/hm/order-four-quadratic-load/ACTUAL-MEROMORPHIC-QUINTIC-SOURCE-CHANGE-PRESERVES-VECTOR-CLASS.md
[D]: https://github.com/Akilleez-QA/read-em-and-weep/blob/86e5aed779f0ff64a83cf9dbe169cb2e7283b346/research/hm/order-four-quadratic-load/UNIVERSAL-DIVISOR-QUINTIC-TWO-CHART-SHADOW-CANCELLATION.md
[S]: https://github.com/Akilleez-QA/read-em-and-weep/blob/86e5aed779f0ff64a83cf9dbe169cb2e7283b346/research/hm/order-four-quadratic-load/ACTUAL-THIRD-BOCKSTEIN-VANISHES-ON-SQUARE-DIRECTIONS.md
[A]: https://github.com/Akilleez-QA/read-em-and-weep/blob/86e5aed779f0ff64a83cf9dbe169cb2e7283b346/research/hm/order-four-quadratic-load/ACTUAL-SEMISIMPLE-C5-AXIS-VECTOR-CUP-VANISHES.md
[G]: https://github.com/Akilleez-QA/read-em-and-weep/blob/86e5aed779f0ff64a83cf9dbe169cb2e7283b346/research/hm/order-four-quadratic-load/THIRD-GATE-VANISHING-AT-SIX-AXES-KILLS-RESIDUAL-CHANNEL.md
[V]: https://github.com/Akilleez-QA/read-em-and-weep/blob/86e5aed779f0ff64a83cf9dbe169cb2e7283b346/research/hm/order-four-quadratic-load/verify_actual_third_vanishing_frontier.py

[F4]: https://github.com/Akilleez-QA/read-em-and-weep/blob/2f81e3510505ad842fb9bb00ff3a667cd36ea17f/research/hm/order-four-quadratic-load/FOURTH-BOCKSTEIN-AFTER-ACTUAL-THIRD-VANISHING.md
[F4V]: https://github.com/Akilleez-QA/read-em-and-weep/blob/2f81e3510505ad842fb9bb00ff3a667cd36ea17f/research/hm/order-four-quadratic-load/verify_fourth_bockstein_reduction_channels.py
