# The actual lower endpoint uses both parity channels

## Actual conclusion

The actual lower endpoint family has nonzero components in BOTH one-dimensional parity channels of

    Q=Hom_G(D5_source,P4 tensor Sym²A*)=Qplus+Qminus.

Parity means interchange of the parameter D5 and source D5 slots after removing the scalar trace from Sym²A. This is a statement about the now-calculated actual family, not merely about which equivariant formulas are available. It does not give an absolute scalar or a numerical channel ratio.

## Inputs and proof

Use the actual two-input theorem in PR543 at fb574c01207099eeb63960da5cb23ad2f2498a84, and the fixed source identification there:

    I_f(X⁴)=20736 B²c st³,
    I_f(XY³)=5184 ABc² t⁴.

All displayed factors are nonzero. At a=t², the actual family vanishes on st³ and is nonzero on t⁴. The parameter harmonic tensor is a nonzero multiple of t⁴.

PR661 (1325647fd916bf2daa71b11efeae6d52cfefa2cd) identifies the channels, up to fixed nonzero factors, as

    Bplus(b,h)=projection_P_in_Sym8(bh),
    Bminus(b,h)=projection_P_in_Sym6((b,h)_1).

For the pure input h=t⁴, the alternating first transvectant (t⁴,t⁴)_1 is zero. The actual nonzero pure-input value therefore forces the coefficient of Bplus to be nonzero.

For the mixed input h=st³, the symmetric value is the P4 projection of st⁷. This projection is NONZERO. Indeed Sym8 W=D5+P4. If its P4 projection vanished, st⁷ would lie in the invariant five-dimensional D5 linear series of degree eight. Its root of multiplicity seven would violate the Wronskian bound from PR663 (ad3ab59f6fbbbb3e5bde1da58b3b92a1f49c6889): an invariant k-dimensional degree-n series with a root of multiplicity m and root orbit of size N satisfies

    N max(0,m-k+1) <= k(n-k+1).

Here N>=12, k=5, n=8, m=7, so the lower bound is 36 while the total Wronskian degree is 20. The bound includes base points and holds over C in characteristic zero.

Write the actual family as u Bplus+v Bminus in any fixed nonzero channel generators. We have u!=0 and Bplus(t⁴,st³)!=0. Its actual mixed-input value is zero. Hence

    v Bminus(t⁴,st³)=-u Bplus(t⁴,st³)!=0,

which forces v!=0. Both actual channels occur. In particular the zero mixed input is a cancellation between channels, not absence of one channel.

For an independent consistency check, (t⁴,st³)_1=-4t⁶. Its P4 projection in Sym6 is also nonzero: the complementary V3 cannot contain a sextic with a root of multiplicity six, since 12(6-3+1)=48>3(6-3+1)=12.

## Limits and reproduction

The actual fourth Bockstein is still uncomputed, and the actual third is still identically zero. These parity channels belong to the LOWER endpoint quotient Cplus/J=P4. The result neither determines the actual family relative to the nonsquare exceptional secant kernel lines nor gives its absolute normal scale.

Run python3 verify_actual_endpoint_both_parities.py. It checks the universal transvectants and the exact Wronskian inequalities without selecting any actual HM coefficients or numerical source points. The actual input values, canonical identification and representation interface are the pinned mathematical dependencies, not consequences of this arithmetic alone.
