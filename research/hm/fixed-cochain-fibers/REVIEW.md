# Independent mathematical review

Verdict: PASS, relative to the explicitly pinned actual ambient vanishings
and the structural results of PR682–684. The bounded abstract-character
verifier passes, including each new irreducible decomposition.

The review checked the following points independently.

1. A closed fixed-duality cochain is equivalent to a parabolic middle
   section: alpha is a subbundle, so the source factor is unique and regular,
   and fixed duality supplies the right-arrow identity. The parabolic-to-B
   exact sequence therefore identifies closed cochains with Ncal sections
   when H0(B(t))=0. The pinned cyclic Rao source explicitly records these
   vanishings for t=2 and4.
2. The ambient rank50 resolution has twists O(t-1) and E(t). For t=2,4,
   positive Bott vanishing gives higher acyclicity of Ncal_X(t), and
   surjectivity of its global homotopy presentation. The symmetric tensor
   map is the standard self-dual homotopy middle component; uniqueness of
   the source identifies the associated full closed cochain. No global
   splitting of the monad is assumed.
3. Injectivity of the connecting map makes a class-zero completion restrict
   to Ncal_Q(4). H1(Ncal_X(2))=0 gives an ambient closed lift. The full
   cochain difference, including the source, vanishes on Q and is divisible
   by q. This proves the normal form N4+qD0(2). Its intersection is qN2,
   since q is a nonzerodivisor on the ambient degree-one cochain terms.
4. In that normal form, V=-dH. Every global exact V=dH is attained by
   C=-qH, and the kernel is exactly N4. Thus the211-dimensional family
   image is established by an exact sequence, not inferred from unrelated
   dimension counts or a tacit claim that every trivial hypercohomology
   class has a global primitive.
5. Ambient N4 restriction is onto Ncal_Q(4), then onto Ncal_Z(4) by PR684.
   The qH part has zero vertex restriction. The displayed joint vertex
   and divided-cochain map is consequently onto its stated images, with
   kernel the vertex-zero part of N4. This proves independence of the
   two reachable prescriptions without claiming arbitrary ambient vertex
   values are reachable.
6. The character formulas use the fixed physical center grading and all
   source blocks. They give N4 even dimension1236/family618, N2 dimension
   204/family102, D0(2) dimension627/family313, and the exact image dimension
   423/family211. The vertex image dimension108/family54 leaves1128/family
   564. Ordinary dimensions2450,400,1225,825 and vertex-fixed2220 agree
   with the separate Euler calculations.
7. The final fixed-family qualification and nonempty-fiber wording are
   explicit. Individual cochains use ordinary dimensions, not P2-family
   dimensions. The correction -qH leaves the third adjoint unchanged
   because its effect is divisible by q cubed on3Q.

No selected HM coefficient, point, derivative, matrix, numerical rank,
fourth Bockstein value, higher-lift existence, or algebraicity claim was
used or verified. This is independent mathematical review, not
proof-assistant formal certification.
