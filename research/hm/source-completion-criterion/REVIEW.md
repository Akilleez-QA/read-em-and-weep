# Independent mathematical review

## Verdict

PASS, with the scope clarifications recorded below. I independently checked the fixed-middle criterion, signs, source blocks, singular-quadric globalization, character arithmetic, parabolic exact sequences, middle restriction vanishing, and the new canonical comparison with adjoint cohomology. I read the two pinned actual-source dependencies through the read-only GitHub connector at commit `8d8b5be4ce62c3055bb53be9e16d29cc63072f04` and ran the bounded verifier. No selected actual HM/source coefficients, points, matrices, ranks, or fourth value were evaluated, and no GitHub writes were made.

The main new result is an exact constructive criterion for a chosen middle operator, together with the exact source-lift ambiguity and a canonical identification of its parabolic obstruction group. It is not a new proof of abstract existence for the actual input: that existence is already supplied by the pinned fifth-neighborhood note. The revised proof correctly states this distinction.

## 1. Signs, trace, source blocks, and divisibility

In an alternating frame, write `beta=alpha^t J` and `T^t J=-JT`. Direct multiplication gives

    (T alpha-alpha R)^t J
      = alpha^t T^t J-R^t alpha^t J
      = -beta T-R^t beta.

Thus the right-arrow sign is exactly correct. Fixed duality of the degree-one cochain is `f_right=f_left^t J`. Closedness then says

    alpha^t J f_left+f_left^t J alpha=0,

which is equivalent to symmetry of `alpha^t J f_left`, not antisymmetry. This also verifies the sign in the definition of the tangent subbundle.

The alternating trace is `tr(T)-tr(R)-tr(-R^dagger)=0`. It imposes no trace-free condition on R. Its four source blocks AA, AU, UA, UU must remain, as the pinned actual canonical-lift note explicitly confirms.

The criterion uses a nonzero quadratic q, so Q is an effective Cartier divisor of P4. Since the monad has locally free cohomology and is exact at its ends, its two relevant short exact sequences split locally. Consequently alpha remains a subbundle after arbitrary base change to Q, including at singular points. This is the correct reason that the quotient factor R_Q is regular and globally unique; no inverse matrix on an open set or rational extension is needed.

The restriction kernel is exactly `q End(S) H0(O(2))`, and H1(O(2))=0 supplies a global R. Divisibility by q is a sheaf assertion in each locally free ambient cochain term. Hence the locally defined quotients glue uniquely, and `q dV=0` implies `dV=0`. No smoothness, normality, or reducedness of Q is used.

For averaging, q and the input family must carry the fixed compatible equivariant structure. In the actual application q is the invariant physical quadratic. One may average an equivariant family of prescribed data; one may not average arbitrary nonequivariant data and assert that its values are unchanged. This is a precision condition, not a defect in the intended actual setting.

## 2. Exact ambiguity and representations

For a fixed T, the factor R_Q is unique. Therefore all lifts differ by qH with `H in End(S) tensor H0(O(2))`. The sign of the induced change is

    V' = V-d(H,0,-H^dagger).

The left component of this coboundary is `-alpha H`. Consequently fixing V as a cochain removes the ambiguity completely. Allowing V to vary leaves its ambient cohomology class unchanged. The revised proof correctly warns that this cannot force equality with a separately prescribed class v_h.

The ordinary ambiguity dimension is 25*15=375. Independently of the character script, its even dimension is

    (2^2+3^2)*(dim Sym^2 V+dim Sym^2 W)
      +(2*2*3)*dim(V tensor W)
    =13*9+12*6=189.

Using the abstract binary-icosahedral tensor products, the diagonal contribution is

    (2*1+A+V+D)(1+A+D)
      =4*1+8*A+5*V+6*P+10*D,

and the off-diagonal contribution is

    2*T6*T6=2*1+4*A+4*V+4*P+6*D.

Their sum is exactly `6*1+12*A+9*V+10*P+16*D`. Pairing with
`P2=1+A+V+2*P+3*D` gives 6+12+9+20+48=95. These calculations use the fixed complex representations; over a nonsplitting characteristic-zero field one should interpret them after the appropriate scalar extension. The 95-dimensional ambiguity is unrelated to the 1095-dimensional middle-family compatibility kernel.

The revised verify.py performs bounded exact character arithmetic over Q(sqrt(5)), checks irreducible orthogonality, and asserts the displayed new dimensions and ranks. It passes. It is an arithmetic certificate, not a proof of the geometric exact sequences or vanishing claims.

## 3. Tangent and parabolic bundles

The quotient `E/A0` has rank 7. Pairing its image with A0 yields a surjective local map to all A0-bilinear forms. Taking the alternating part has rank 10; its kernel has rank 35-10=25. The induced map from this kernel to symmetric bilinear forms has kernel Hom(A0,F), so its ranks are 10+15=25.

In a local symplectic splitting `E=A0+F+A0*L`, the lower F block of a skew endomorphism is arbitrary and the lower A0*L block is symmetric. All paired blocks can be supplied, which proves the surjection `sp(E)->D`. Its kernel P has rank 78-25=53. The Levi ranks are 25+3 and the nilradical associated-graded ranks are 10+15. The twists `Hom(F,A0)` and `Sym^2 A0 tensor L^-1` are correct.

These are local split-bundle arguments over rings with 2 invertible, so they remain valid on singular Q. They prove exactness of sheaves without asserting any global splitting. The connecting class and its vanishing criterion follow exactly from the long cohomology sequence. When a lift exists, its differences are H0(P_Q(4)).

## 4. Independent middle-restriction vanishing

The imported positive-twist Bott statement supports H1(sp(E)(2))=0. There is also a direct independent check. Let `G_i=U tensor Lambda^(3+i) H`. The exterior Euler complex resolves E by

    0 -> G2 O(-3) -> G1 O(-2) -> G0 O(-1) -> E -> 0.

In characteristic zero its graded symmetric square resolves Sym^2 E. After twisting by `L^-1 O(2)`, its five resolution terms have line twists

    1, 0, -1, -2, -3.

The leftmost term is Sym^2 G2, since G2 has even complex degree. Every term has vanishing higher cohomology on P4; moreover O(-1), O(-2), O(-3) are entirely acyclic. The resolution therefore has no positive hypercohomology. Since `sp(E)=Sym^2 E tensor L^-1`, this proves the required H1 vanishing without any selected monad calculation. The Q-to-X middle lift is consequently unobstructed in this degree.

## 5. Canonical comparison with the adjoint group

The new Section 4 is correct. Under `sp(E)=Sym^2 E tensor L^-1`, the image `A0 odot E tensor L^-1` preserves A0 and sends A0-perp into A0, so it acts trivially on F. Conversely local block inspection shows that every element of P acting trivially on F has precisely this form. Its rank is

    dim Sym^2 A0 + dim(A0 tensor F) + dim(A0 tensor A0*L)
      =15+10+25=50.

This rank-50 bundle is the kernel of P->sp(F), not the rank-25 nilradical. The symmetric multiplication presentation has kernel `Lambda^2 A0 tensor L^-1`, giving the asserted ranks 60-10=50 and 53-50=3.

After twist four, the presentation is exactly

    0 -> Lambda^2 S O(3) -> S tensor E(4) -> N(4) -> 0,

with the common constant determinant line retained. Its terms are locally free, hence restriction to Q stays exact. The restriction sequences for O_Q(3) and E_Q(4), together with the stated positive Bott vanishing, show that both have zero positive cohomology. The presentation then proves H^i(N_Q(4))=0 for every i>0. Therefore the canonical map H1(P_Q(4))->H1(sp(F)_Q(4)) is an isomorphism and H0(P_Q(4))->H0(sp(F)_Q(4)) is surjective. Since F has rank two, sp(F)=End_0(F), as claimed.

Optional numerical corollary, independently checked: h0(E(4))=560, h0(E(2))=90, and h0(O_Q(3))=35-5=30. Thus

    h0(N_Q(4))=5*(560-90)-10*30=2050,
    h0(P_Q(4))=2050+h0(B_Q(4)).

These are universal bundle-cohomology counts, not selected actual-instance ranks.

## Scope correction resolved during review

The pinned actual fifth-neighborhood note already constructs abstract global cochains C_h from the proved cohomological divisions. Hence the new connecting class for its actual f is already known abstractly to vanish. The author added this clarification and the independent distinction between an arbitrary divided class [V] and a separately prescribed v_h. Those are important limits: the criterion does not evaluate a chosen primitive, the fourth Bockstein, or a higher-order extension, and vertex/ramification compatibility does not replace the whole-Q quotient equality for a chosen T.

No remaining substantive mathematical correction is required within these hypotheses.
