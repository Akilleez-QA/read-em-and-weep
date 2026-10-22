# The last positive Smith factor and its canonical third obstruction

## Hypotheses and scope

Retain the actual positive pencil M(t)=q0+t a from V=H1(B(2))_+ of dimension41 to U=H1(B(4))_+ of dimension37. At t=0 its rank is33, its kernel is (A+D5)xi, and its cokernel is P4. The first Bockstein is zero.

Assume the actual second scalar is nonzero. The proved square-filtration formula says beta2 vanishes on D5, and the universal symbol theorem says its A-input has generic rank three. Work over the function field of P(A), or at any direction where this rank is three. No conclusion below assumes generic surjectivity of M.

## 1. Only one Smith factor remains

Over the formal power series field at t=0, elimination splits33 unit Smith factors. Since beta1=0 and beta2 has rank3, three further factors have valuation exactly2. There remains a single target coordinate against five source coordinates. Either its remaining row is identically zero, or the common valuation of its entries is a finite integer e>=3. Thus the possibilities are

    generic rank36, source kernel dimension5, target cokernel dimension1;

or

    generic rank37, source kernel dimension4, target cokernel zero,
    Smith valuations 0 repeated33 times, 2 repeated3 times, and e.

In the second case every maximal37-minor is divisible by t^(6+e). At least one such minor is a nonzero polynomial of degree at most37, since the pencil is linear. Hence 6+e<=37 and

    3<=e<=31.

Consequently the correctly iterated higher Bocksteins of orders3 through31 constitute a finite exact gate. If all vanish, the last row is permanently zero and the generic positive cokernel has dimension one. A first nonzero such Bockstein has rank one and supplies the final rank. This refers to the successive obstruction quotients, not repeated application of one chosen matrix.

## 2. Canonical third class on D5

The actual cyclic identity is a xi=q0 zeta_a. For h in D5, use the canonical first correction

    x0=h xi,  x1=-h zeta_a.

The square-filtration theorem beta2(D5)=0 says a h zeta_a lies in im(q0:V->U). Choose v_h(a) in V with

    q0 v_h(a)=a h zeta_a.

Since q0 is a fixed map of finite-dimensional G-representations, an equivariant linear splitting of its image gives a choice polynomial of degree two in a and linear in h. Set x2=v_h(a). Then

    M(t)(x0+t x1+t^2 x2)=t^3 a v_h(a).

The third Bockstein is

    beta3_a(h xi)=[a v_h(a)]
      in P4 / im(beta2_a:A->P4).

Changing v_h by an original kernel vector changes its class in P4 by beta1, hence not at all. Changing the first correction by an original kernel vector changes this third class by im beta2. These are exactly the standard correction ambiguities, so the displayed quotient class is canonical.

The second scalar being nonzero makes its A-map injective at the generic direction. Therefore the surviving source is precisely D5 and the surviving target is a line. The third class is the first possible final-rank obstruction.

## 3. Global form of the third gate

Let P(A)=P2 parameterize the negative directions. The quadratic second symbol has exact sheaf presentation

    0 -> A O_P2(-2) -> P4 O_P2 -> I_Z(6) -> 0,

where Z is its established zero-dimensional maximal-minor scheme of length24. This is Hilbert--Burch for the rank-three quadratic symbol; the scalar multiplying it is nonzero and does not change Z. The quotient is an ideal sheaf, not a line bundle at Z.

The polynomial choice above and the canonical quotient define an actual global map

    D5 O_P2(-3) -> I_Z(6).

Equivalently the third gate is an equivariant D5-valued system of degree-nine forms vanishing on Z. This description is valid as a coherent-sheaf map across Z. At Z the second A-map can lose rank and the full third-page source has additional directions; no assertion that D5 exhausts that special-fiber source is made.

Twisting the presentation by three and taking sections gives

    H0(I_Z(9)) = (P4 tensor Sym^3 A*) / (A tensor A*),

because H1(O_P2(1))=0. Its dimension is40-9=31 and its exact character is

    A + 2V + 3P4 + 2D5.

Hence the space of universal equivariant third gates has dimension two. The actual map occupies a specific point of this two-dimensional space; no claim is made that either coefficient is nonzero. A nonzero actual third map supplies the final generic rank, while zero leaves orders4 through31 to be determined.

## Evidence

The earlier proofs supply rank33 and beta1=0. POSITIVE-SECOND-BOCKSTEIN-SQUARE-FILTRATION.md supplies vanishing on D5, and POSITIVE-SECOND-BOCKSTEIN-UNIVERSAL-SYMBOLS.md supplies rank3 and the Hilbert--Burch presentation when the second scalar is nonzero. The companion verifier checks the universal character quotient, exact dimension arithmetic, formal correction expansion, and finite Smith bound. It evaluates no actual coefficient or rank.
