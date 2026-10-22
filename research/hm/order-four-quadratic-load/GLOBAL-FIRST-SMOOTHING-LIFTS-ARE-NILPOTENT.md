# Global first-order lifts of the positive kernel remain nilpotent

Let h be a positive quadratic in D5, and suppose the even section N h of B_Q0(4) admits an inversion-even lift Phi over the first-order quadric q0+epsilon c, with c a negative quadratic and epsilon²=0. Then det(Phi)=0. This is a necessary consequence of an actual global lift, not a proof that a lift exists.

The determinant is zero on the central fiber, hence det(Phi)=epsilon d for an even global section d of O_Q0(8).

At the generic vertex, N has matrix entries of cover orders at least6,8,10, and h has cover order4. Thus N h has positive-coordinate order at least5. Choose local ambient representatives preserving that order. Their determinant is divisible by q0 and has order at least10, so the quotient by q0 has order at least8. This contributes only order at least8 to d. The correction term, the determinant derivative paired with Phi modulo epsilon, has order at least5. Therefore d has vertex order at least5, and inversion-even parity increases this to at least6.

Near C0, N is the square of a section vanishing to first normal order, so N h vanishes to order at least2 in the negative normal coordinates. Choose ambient lifts preserving that order. The determinant quotient by q0 retains negative-coordinate order at least4, because q0 is independent of the negative coordinates. The correction pairing has order at least2. Consequently d vanishes to order at least2 on C0.

An even octic with these two properties has only positive-coordinate degree6 and negative-coordinate degree2. Its vertex initial term is therefore a section of Sym12(W-prime) tensor O_P(W)(2). The order-six term of the correction pairing is divisible by the actual cubic f3: the leading and next entries of N h all contain f3, and the ambient determinant/q0 term starts at order8 and cannot contribute. Higher local corrections and units preserve this divisibility.

The everywhere nonzero cubic line is O(-3) subset Sym3(W-prime) tensor O. Its multiplication into Sym12 has constant rank. Generic divisibility therefore holds globally, placing d in

    H0(P(W), Sym9(W-prime) tensor O(-1))=0.

Thus d=0, and the tracefree lift Phi remains nilpotent by Cayley--Hamilton.

This does not imply a flat spinor deformation: LOCAL-CI-NILPOTENT-LIFTS-DO-NOT-DETECT-GAMMA.md explicitly constructs local nilpotent lifts without such a conclusion. The global nonvanishing question is still the existence and gluing of these constrained lifts. Inputs are the actual conic first jet, the unique vertex module, and its nowhere-zero cubic relation; no selected coefficient or actual matrix rank is evaluated.
