# The residual positive three-space: a secondary obstruction and an actual division theorem

## Results

The proved first positive scaling boundary has kernel

    H0(B_R(2)) tensor <q_->,

of dimension three. Two further exact conclusions are available.

1. Its next obstruction is a canonical map from this three-space to an eighteen-dimensional quotient, rather than to the entire finite-neighborhood obstruction space. Its formula retains the actual fourth-normal comparison term and the first lifting correction.
2. On a nonempty open of smooth even quadrics, an ACTUAL even section of I_C^2 B_Q(4) whose actual degree-two normal jet is divisible by q_- must vanish. This follows from simplicity of the two cone surfaces cut out by the factors of q_-.

These statements do not yet show that the three scaling survivors vanish. Divisibility of a reduction at the scaling limit is not divisibility of an actual nearby section or of its actual normal jet. The established generic bound remains at most three until the new secondary map or a later obstruction is proved nonzero.

## 1. Setup and the first obstruction

Let R=P(V) be the positive fixed plane, W the dual negative two-space, B=End_0(F), and

    Q:q_+(x)+q_-(y)=0,
    C=Q intersect R,  I=I_(C/Q).

Both blocks are nondegenerate. Put S=H0(B_R(2)), so dim S=3. The established actual cohomology is

    H1(B_R(2))=0,  H1(B_R(-6))=0,
    H1(B_R)=V directsum 4 directsum 5,  dim H1(B_R)=12.

Use the scaling family g_epsilon(x,y)=(x,epsilon y) and the proper flat finite module (I^2/I^10) tensor g_epsilon*B(4), taking its positive part after finite pushforward to R. Its limiting section space is S tensor Sym^2 W.

The actual ambient second-normal class zeta gives the first boundary

    L_q:S tensor Sym^2 W -> T_q,
    T_q=H1(B_R) tensor H_4(q_-),
    H_4(q_-)=Sym^4 W/(q_- Sym^2 W).

Here dim T_q=24. The actual cup scalar is nonzero, so

    rank L_q=6,
    ker L_q=S tensor <q_->.                            (1)

The inclusion T_q into the finite-module H1 is injective: its harmonic-index-four component uses H1(B_R)->H1(B_R|3C), whose kernel is zero by H1(B_R(-6))=0. The two lower harmonic components vanish through H1(B_R(2))=0. These are actual cohomology maps, not merely dimension comparisons.

## 2. The actual fourth-normal term cannot be discarded

Use inversion-equivariant local projective frames and put t=epsilon squared. Relative to the pullback of End(F_R), write the actual projective transition automorphisms to order t squared as

    exp(t ad(zeta_ij) + t^2 ad(rho_ij)) modulo t^3.

The coefficient zeta_ij has normal degree two and values in B_R(-2). The coefficient rho_ij has normal degree four and values in B_R(-4). All formulas use the usual transport by the reference bundle transitions.

The cocycle condition is the Baker–Campbell–Hausdorff condition

    delta rho = -one-half [zeta_ij,zeta_jk],             (2)

with the sign determined by the common transition convention. Thus rho need not be a cocycle and cannot be set to zero just because

    (H1(B_R(-4)) tensor Sym^4 W)^A5=0.

That invariant-space vanishing removes an independent invariant homogeneous choice after the lower data have been fixed; it does not remove the nonlinear term required by (2).

## 3. The exact three-to-eighteen secondary boundary

Take a first survivor s0=q_- s, where s belongs to S. The first lifting equation reduces, using q_-=-q_+, to

    delta k = -q_+ [zeta,s].                            (3)

Its right side is a B_R(2)-valued normal quadratic cocycle. The vanishing H1(B_R(2))=0 allows k to be chosen as a local B_R(2)-valued normal quadratic section. Importantly, this correction need not have normal degree four: the quadric relation has lowered its displayed normal degree.

For transition compatibility written as s_j(t)=exp(t ad zeta_ij+t^2 ad rho_ij)s_i(t), the next obstruction is represented by

    [rho,s0] + [zeta,k] + one-half [zeta,[zeta,s0]].

After substituting q_-=-q_+ in the first and third terms, it is represented by the B_R-valued normal quartic cocycle

    tau(s)=[zeta,k] - q_+[rho,s]
                    - one-half q_+[zeta,[zeta,s]].       (4)

The first lifting equation and (2) show that (4) is a cocycle. Equivalently, it is the coefficient of the next compatibility equation for the actual family. One may establish the cocycle identity before truncating the normal neighborhood, then restrict to I^2/I^10.

Project (4) to harmonic degree four. Its lower harmonic pieces again vanish through H1(B_R(2))=0. The resulting class is well-defined modulo im L_q: changing k by a global element of S tensor Sym^2 W adds exactly its first boundary. Changes of local projective frames have the same harmless effect by naturality of successive lifting obstructions.

Consequently the actual secondary obstruction is canonically

    d_secondary:S -> T_q / im L_q,
    dim S=3,  dim(T_q/im L_q)=24-6=18.                 (5)

The injection of T_q into the finite obstruction space ensures that the quotient in (5) is not concealing an additional relation. Every relative global section which survives the first boundary must reduce to an element of ker d_secondary. The usual finite free module over the localized scaling parameter line therefore gives the sharpened conditional bound

    generic h0(I^2 B_Q(4))_+
          <= 3 - rank(d_secondary).                    (6)

In particular, nonzero d_secondary would improve the bound to at most two, and injective d_secondary would eliminate the positive second-normal kernel. No rank or nonvanishing of (5) is claimed here.

## 4. An exact quotient along the two cone surfaces

Factor q_-=uv, up to a nonzero scalar, and put

    D_u=Q intersect (u=0),  D_v=Q intersect (v=0).

These are the rank-three quadric cone surfaces over C, with the two distinct negative vertices. The universal ideal identity is

    I^2/(uv) = O_Du(-2) directsum O_Dv(-2).             (7)

The two maps are multiplication by v squared and u squared, respectively. Locally modulo uv, I^2 is generated by u squared and v squared, their intersection is zero, and their annihilators are the opposite linear factors. This proves (7) globally, with the stated twists. There is no deletion of the cone vertices.

Tensoring (7) by the ambient locally free B(4) gives the exact sequence

    0 -> B_Q(2) --q_- --> I^2 B_Q(4)
      -> B_Du(2) directsum B_Dv(2) -> 0.               (8)

Thus H0(B_Q(2))=0 only makes the global second-normal space inject into two cone restriction spaces. It does not by itself make that space zero.

## 5. General cone surfaces are simple

The established HM plane classification says that the entire unstable-plane locus is the surface S25 in Gr(3,5). The mixed planes

    P(L,p)=span(L,p),  L a line in R, p in P(V_-),

form a three-dimensional family. Consequently a general mixed plane has stable F|P.

Fix one stable such plane in H_p=span(R,p). Degenerate the positive quadratic to the square of the equation of L. The cone D(q_+,p) inside H_p then degenerates to the doubled plane 2P. Its endomorphism restriction fits into

    0 -> B_P(-1) -> B|2P -> B_P -> 0.

Stability gives H0(B_P)=H0(B_P(-1))=0, hence H0(B|2P)=0. The family of quadratic Cartier divisors in H_p is proper and flat, and the ambient bundle remains locally free. Upper semicontinuity yields a nonempty open of simple cones with smooth positive base conic.

Allowing p to vary gives a nonempty open in the irreducible parameter space of positive conics and negative vertices. Pulling this open back for each of two ordered distinct vertices gives two dense opens in their common irreducible parameter space; their intersection is nonempty. Thus, on a nonempty open of smooth even quadrics,

    H0(B_Du)=H0(B_Dv)=0.                                (9)

This argument asserts a global nonempty open. It does not assert simplicity for every fixed positive conic.

The plane-locus input is Boralevi, The Horrocks–Mumford bundle restricted to planes, Theorem 3.1, printed pages 6–7:
https://arxiv.org/pdf/math/0602002

Only its geometric unstable-plane locus is used, not a displayed matrix or rank criterion.

## 6. A valid actual-jet division theorem

Assume (9), the established lower-good condition H0(B_Q(2))=0, and let sigma be an even global section of I^2 B_Q(4). Suppose its ACTUAL degree-two jet belongs to

    H0(B_C(2)) tensor <q_->.

Its restriction to each cone has zero degree-two term because the corresponding negative direction is a zero of q_-. It therefore vanishes to order at least three along C on that cone. The degree-three normal layer is odd, whereas sigma is even, so its degree-three term also vanishes. Hence

    sigma|D_i belongs to I_(C/D_i)^4 B_Di(4)
                      = t_i^4 B_Di,

where t_i is the negative hyperplane coordinate on D_i. Equivalently, in (8) the cone quotient section h_i is even and vanishes on C; after its first division by the odd t_i, the quotient is odd and again has zero restriction to C, forcing a second division.

The conic C is an effective Cartier hyperplane divisor on the entire cone. Its equation t_i is a unit near the vertex, which lies outside R. These divisions are therefore valid for the locally free restricted bundle everywhere, including the singular vertex.

By (9), both restrictions of sigma vanish. Their union is the Cartier divisor (q_-=0), so (8) gives sigma=q_- tau for a global tau in H0(B_Q(2)). The lower-good vanishing forces sigma=0.

Thus the harmonic second-normal jet map

    H0(I^2 B_Q(4))_+
      -> H0(B_C(2)) tensor (Sym^2 W/<q_->)

is injective on this nonempty open. This is an actual geometric division theorem, not merely a statement about an associated graded module.

## Remaining issue

The first scaling survivors reduce to q_- S at epsilon zero. This does not say that an actual nearby section has q_- divisible degree-two jet: its jet may acquire a nonzero harmonic component in higher powers of epsilon. The cone theorem excludes actual divisible jets but does not forbid that deformation away from divisibility.

Formula (5) is the next exact obstruction to such lifting. Proving its nonvanishing requires more than zeta!=0, the first cup scalar, lower-twist vanishing, or the absence of an invariant free fourth-normal class. Until that obstruction or a later one is settled, the secure generic bound is at most three.

No selected HM/source coefficients, evaluated actual matrix ranks, scans, or experiments are used.
