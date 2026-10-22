# The actual Gamma has balanced normal bundle

## Statement and checked inputs

For the actual smooth rational sextic Gamma in P(U*)=P3, one has

    N_Gamma/P3 = O_P1(11) directsum O_P1(11).

This is a consequence of its actual equivariance, not a selected rank calculation. The proof below avoids apolarity and catalecticants entirely.

Read source: ACTUAL-GAMMA-CLEBSCH-CUBIC.md at e3c9ef8a5525a8d94890270f3f3bb4f6a85ece81, under research/hm/order-four-quadratic-load/ in Akilleez-QA/read-em-and-weep:
https://github.com/Akilleez-QA/read-em-and-weep/blob/e3c9ef8a5525a8d94890270f3f3bb4f6a85ece81/research/hm/order-four-quadratic-load/ACTUAL-GAMMA-CLEBSCH-CUBIC.md

PR1 coordination was read through comment6318225665 on 2026-10-21. Mr. Slop's current lane is the primary normalization-module resolution; this is separate secondary Gamma geometry. No external write is made here.

The pinned theorem proves:

- The actual U has the standard four-dimensional A5 representation, not the spin four-dimensional representation.
- Gamma is a faithfully acted-on P1, embedded with O_Gamma(1)=O_P1(6).
- Its point orbits have sizes 12,20,30,60. In particular there is no invariant effective divisor of degree between one and eleven.
- Gamma lies on its unique smooth A5-invariant Clebsch cubic Sigma, and its equivariant normal sequence is

      0 -> O_P1(4) -> N -> O_P1(18) -> 0.          (1)

All three bundles and arrows in (1) carry their actual geometric A5 actions. The degree-four subbundle is a genuine subbundle: its cokernel is locally free. These facts are the full geometric input.

## 1. Short proof by the canonical maximal subline

Restrict the Euler sequence of P3 to Gamma and compose with the tangent-to-normal quotient. This gives a surjection

    O_P1(6)^4 -> N.

Write the Birkhoff–Grothendieck splitting N=O(a) directsum O(b), with a>=b. Since N is a quotient of O(6)^4, every line quotient has degree at least six: if b<6, every map O(6)->O(b) is zero, contradicting the surjection. Thus b>=6. The normal sequence gives a+b=22.

Suppose a>b. The maximal-degree subline O(a) is canonical: it is the first Harder–Narasimhan subbundle, or directly the unique saturated degree-a subline because Hom(O(a),O(b))=0. It is therefore preserved by the actual A5 action. Its quotient Q=O(b) inherits a genuine A5 linearization.

Under a>b and a+b=22, one has 6<=b<=10. Compose the actual subbundle L=O(4) in (1) with the quotient:

    L -> N -> Q.

This is an equivariant map of line bundles. If nonzero, its zero divisor is A5-invariant and has degree b-4, which lies between two and six. No such invariant effective divisor exists. Hence this composite is zero, and L factors through the canonical O(a) subline.

The resulting map O(4)->O(a) has no zero. Indeed a zero would make the original inclusion L->N zero on that fiber, contradicting that L is a subbundle. A nowhere-zero map between line bundles is an isomorphism, so a=4. This contradicts a+b=22 and b<=10. Therefore the splitting cannot be unequal. It is necessarily

    N=O(11)^2.

The splitting is an ordinary bundle isomorphism. It is not an assertion that either degree-eleven summand alone admits an A5 linearization: it does not, by the odd-degree parity obstruction. The rank-two bundle and the full geometric sequence remain genuinely equivariant.

## Consequences and boundaries

The splitting gives h0(N)=24, H1(N)=0, and, for every integer m>=1,

    Sym^m(N*) = O(-11m)^(m+1).

Thus for every integer t the graded normal-neighborhood layer has exact cohomology

    h0(Sym^m(N*) tensor O_Gamma(t))
        =(m+1) max(6t-11m+1,0),
    h1(Sym^m(N*) tensor O_Gamma(t))
        =(m+1) max(11m-6t-1,0).

Here O_Gamma(t)=O_P1(6t). Since Gamma is a regular embedding, these are the layers I_Gamma^m/I_Gamma^(m+1), twisted by O_Gamma(t). They do not split the entire infinitesimal neighborhood or identify its extension maps. For the established flat f:Xhat->P3 and g:S=f^{-1}(Gamma)->Gamma, flat base change also gives the exact regular-embedding identities

    N_S/Xhat = g*O_P1(11)^2,
    I_S^m/I_S^(m+1) = g*O_P1(-11m)^(m+1).

They hold even though S need not be smooth, because regular embeddings and their conormal bundles are preserved under flat base change. No conclusion about K4, the actual ambient extension boundary, or full adjoint vanishing follows solely from the balanced normal bundle. All work is symbolic and coefficient-free.
