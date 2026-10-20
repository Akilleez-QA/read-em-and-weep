# Order-five vanishing with the quadratic held fixed

Work over C. Keep the HM bundle F and its coefficient-space coordinates fixed. Put B=End_0(F), let C be the union of the twenty-five evaluation-degeneracy lines, and write W=H0(I_C(5)), of dimension six. For nonzero forms u in S2 and v in S3, set

    Q5(u,v)=H1(B(5))/(u H1(B(3))+v H1(B(2))).

This note restricts the coordinate-orbit theorem further: u itself is fixed, and only its orthogonal group moves the associated binary-quartic cubic. It does not evaluate the original pair.

## 1. Fixed-quadratic hypotheses

Choose a quadratic u in the nonempty open O of PR459. Explicitly:

- Q=V(u) is smooth;
- W restricts injectively to H0(Q,O_Q(5));
- uM1=M3, where Mj=H1(F(j));
- Q contains none of the component lines of C.

Let v be obtained together with u from the universal binary-quartic pair (12I,6J) by one simultaneous linear coordinate change, allowing harmless nonzero scalings of the forms. Thus the coefficient vector space carries a transported SL2 action isomorphic to Sym4(C2), u is its invariant nondegenerate quadratic, and v is a nonzero invariant cubic. Define G=SO(u), a connected algebraic group of dimension ten, and let G act on forms by inverse pullback. This action preserves u exactly.

The cubic class j=v mod uS1 in A3=H0(Q,O_Q(3)) is nonzero. Otherwise v=u times a linear form. Invariance and cancellation in the polynomial domain would make that linear form SL2-invariant, impossible in the nontrivial irreducible Sym4 representation.

## 2. The projective cubic orbit has dimension seven

The transported SL2 subgroup preserves j. Its Lie algebra embeds in g=so(u), and as SL2 representations

    g = Lambda2(Sym4(C2)) = Sym6(C2) direct sum Sym2(C2).

For completeness, Sym4 has weights 4,2,0,-2,-4. Taking sums of distinct weights gives the weights of Sym6 together with those of Sym2; complete reducibility proves the displayed decomposition. The embedded sl2 is the unique Sym2 summand.

The projective tangent action

    g -> Hom(Cj,A3/Cj)

is SL2-equivariant and kills that Sym2 summand. On the irreducible Sym6 summand it is either injective or zero. The zero alternative is impossible. Indeed, it would make the entire Lie algebra stabilize Cj. In characteristic zero the closed line stabilizer would then have full dimension, so connectedness of G makes the line G-stable. A connected semisimple group has no nontrivial algebraic characters, hence j would be G-invariant.

There is no nonzero G-invariant section of O_Q(3). The orthogonal group G is transitive on the projective smooth quadric: an isometry of isotropic lines extends by a Witt basis, and its determinant can be corrected on the nondegenerate complementary space. An invariant section has invariant zero set. Transitivity makes this zero set either empty or all of Q. A nonzero section cannot have the latter zero set, and an empty zero set would trivialize O_Q(3), which is impossible since its restriction to a line in Q has degree three. Thus j cannot be invariant.

The tangent rank is consequently seven, and the projective stabilizer has dimension three. Therefore the projective orbit

    Omega=G.[j] in P(A3)

has dimension seven. This counts the projective orbit, not an additional scalar direction.

## 3. Exceptional orthogonal parameters have codimension at least two

PR459 constructs a closed subset D3(u) in P(A3) of dimension at most five: the cubic classes dividing some nonzero section in the six-dimensional restricted space W_Q. Its complement satisfies

    W intersect (u,b)_5 = 0

for every lift b of a class outside D3(u).

Since dim Omega=7, Omega is not contained in D3(u). Let

    Z={h in G : h.[j] lies in D3(u)}.

This is closed. Every fiber of the orbit map G -> Omega is a coset of the three-dimensional projective stabilizer. Since dim(D3(u) intersect Omega) is at most five, dim Z is at most eight. Thus Z has codimension at least two in G, and G minus Z is nonempty open.

For h outside Z, put v_h=h.v. Its restriction to Q is nonzero, hence u does not divide v_h; smooth u is irreducible, so u and v_h are coprime. Because u contains none of the component lines, the common-contained-line kernel in PR458 is zero. Its residual tuple map therefore injects into the zero space W intersect (u,v_h)_5. The residual quotient vanishes. The fixed primary surjectivity uM1=M3 removes the remaining primary quotient, proving

    Q5(u,v_h)=0 for every h in G minus Z.

The actual failure set is contained in Z, not asserted equal to it. Neither W_Q nor the HM bundle is assumed G-invariant: G moves the cubic orbit, while the bad-factor set is defined using the fixed W_Q. This is precisely why comparison of their dimensions is used.

## 4. A punctured fixed-u algebraic curve avoiding every exceptional parameter

The Cayley transform identifies the principal open

    X={A in so(u) : det(Id-A) is nonzero}

with G_cay={h in G : det(h+Id) is nonzero}, by

    H=(Id-A)^(-1)(Id+A),   A=(H-Id)(H+Id)^(-1).

To check this, represent u by a symmetric invertible U. The identity A^t U+UA=0 gives H^t U H=U. Also A is similar to -A^t, so det(Id-A)=det(Id+A), and det H=1. Conversely orthogonality gives the stated u-skew relation for A. The formulas are mutually inverse, and H+Id=2(Id-A)^(-1). Both opens contain the identity or zero respectively.

Let B_exc be the inverse image of Z intersect G_cay in X. Its dimension is at most eight by Section 3. Radial projection

    so(u) minus {0} -> P(so(u))=P9

therefore sends B_exc minus {0} into a constructible set whose closure has dimension at most eight. Choose a nonzero direction [A] outside this proper closed subset. This is an existential open-direction choice, not a selected coefficient or matrix evaluation.

For every t not equal to zero for which det(Id-tA) is nonzero, the point tA cannot belong to B_exc: its radial direction would be [A]. On the principal open T={t in A1 : det(Id-tA) is nonzero}, the curve

    H(t)=(Id-tA)^(-1)(Id+tA),   v_t=H(t).v

is regular, satisfies H(0)=Id, and preserves u exactly. Consequently

    Q5(u,v_t)=0 for every t in T minus {0}.

The domain T contains zero because its defining determinant equals one there; its complement in A1 is finite. The improvement over an unspecified generically good curve is that every nonzero parameter in this domain is good. The HM bundle stays fixed. The special value at zero remains undetermined. Avoidance along a punctured curve does not establish first-order surjectivity, a nonzero transverse derivative, or a torsion-length bound at zero.

## Dependencies and scope

- PR139, c5fb4a0bcc3c8e35093fcfcff9a73a79a45a18e5, identifies the invariant pair (12I,6J):
https://github.com/Akilleez-QA/read-em-and-weep/pull/139
- PR449, e4b6acdd27d8da8be4052c117ea2dca0f48f46ff, supplies the primary-good quadratic open:
https://github.com/Akilleez-QA/read-em-and-weep/blob/e4b6acdd27d8da8be4052c117ea2dca0f48f46ff/research/hm/quadratic-failure-cone/PROOF.md
- PR458, b46c3b48a8b10a7d0656fde247f2c3f258d1fd23, supplies six quintics, the residual injection and primary separation:
https://github.com/Akilleez-QA/read-em-and-weep/blob/b46c3b48a8b10a7d0656fde247f2c3f258d1fd23/research/hm/pair-interpolation/PROOF.md
- PR459, 0d4dcd49536c229ce0a602c6c3d37cf821ce85a5, supplies O and the five-dimensional bad-factor locus:
https://github.com/Akilleez-QA/read-em-and-weep/blob/0d4dcd49536c229ce0a602c6c3d37cf821ce85a5/research/hm/generic-order-five/PROOF.md
- PR460, edbbce6a0632e86e12beb8351cf9391a0d7d4ff7, supplies the simultaneous coordinate-orbit framework with F fixed:
https://github.com/Akilleez-QA/read-em-and-weep/blob/edbbce6a0632e86e12beb8351cf9391a0d7d4ff7/research/hm/coordinate-orbit-order-five/PROOF.md

The new result is fixed-quadratic restricted-fiber genericity, the codimension-two bound on exceptional orthogonal parameters, and a punctured algebraic fixed-quadratic curve through the starting positioned pair with no nonzero exceptional parameter in its domain. The hypothesis u in O has not been verified for the original u0, and the original cubic may remain exceptional even when it holds. No conclusion about the original source instance, actual retained source values, six pure conditions, lower orders, module lifting or quantization algebraicity follows. No selected coefficients, multiplication matrices, numerical ranks, generators/checkers, parameter searches or large computations were evaluated. This is authored mathematics for review, not formal machine verification.
