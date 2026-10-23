# Universal symmetric-kernel saturation and degree-three source quotient

This note is an exact, universal polynomial argument. It uses no specialization,
point evaluation, rank experiment, or coefficient-fitting solve. Its accompanying
verifier checks polynomial chain identities and the explicit reconstruction maps.

## 1. Setup and precise distinction between symmetric power and product image

Let R be the coefficient ring (in the application
Q[FB^(+/-1), FC^(+/-1), FD^(+/-1)], with any further independent markings adjoined),
let S=R[x,y,z], and write m=(x,y,z). All symmetric/exterior decompositions below
use that 2 is invertible. Let A be free of rank 3, V free of rank 3, and put

    r=(x,y,z)^t, F=A tensor V tensor S,
    delta=id_A tensor r^t, K=ker(r^t), N=A tensor K.

Define H to be the symmetric tensors in Sym^2 F whose contraction by delta in
one leg is zero. The same then holds in the other leg. Let mu:Sym^2 N -> H be
the natural product map. At the outset, Sym^2 N means the abstract symmetric
power; it is not assumed equal to its image.

Fix the following orientation:

    C = [[0,-z,y], [z,0,-x], [-y,x,0]],
    k_i = column i of C,
    q = x e2 wedge e3 - y e1 wedge e3 + z e1 wedge e2.

The identities r^t C=0 and C r=0 give the Koszul presentation

    0 -> S(-2) --r--> S(-1)^3 --C--> K -> 0.

## 2. The abstract symmetric powers have no hidden vertex torsion

The symmetric square of that one-relation presentation gives the exact sequence

    0 -> S(-3)^3 --(v |-> r odot v)--> S(-2)^6
      -> Sym^2 K -> 0.                                      (2.1)

Indeed Sym(K)=Sym(S(-1)^3)/(r_1 f_1+r_2 f_2+r_3 f_3); its
degree-two relation space is precisely the displayed multiplication image.
Multiplication by that nonzero polynomial is injective. Thus Sym^2 K has
m-depth at least 2. It is locally free away from V(m), and its map into
Sym^2(V tensor S) is injective there. Its kernel is m-power torsion, and
H^0_m(Sym^2 K)=0 proves that the map is injective everywhere. This explicitly
rules out vertex torsion in the abstract Sym^2 K.

For the exterior square, the exact Koszul complex, not a generic-rank argument,
gives

    Lambda^2 K = coker(S(-3)^3 --r wedge--> S(-2)^3)
               isomorphic to m S(-1),

under the actual wedge-product map. Its three products satisfy

    k2 wedge k3 = x q,
    k3 wedge k1 = y q,
    k1 wedge k2 = z q.                                    (2.2)

Consequently the abstract Lambda^2 K also has no vertex torsion. The Cauchy
decomposition, valid for this free A over a Q-algebra, is

    Sym^2(A tensor K)
      = (Sym^2 A tensor Sym^2 K)
        direct-sum (Lambda^2 A tensor Lambda^2 K).           (2.3)

Each summand injects into the corresponding summand for A tensor V. Therefore
mu is injective: in this particular universal Koszul module, the abstract
Sym^2 N really does equal its product image. This conclusion is proved, not
assumed from a general assertion about symmetric powers of torsion-free modules.

## 3. Complete kernel theorem and exact saturation defect

Under the Cauchy decomposition of Sym^2(A tensor V), contraction separates
the Sym^2 A and Lambda^2 A sectors. The symmetric V-sector is exactly Sym^2 K.
One proof is that both agree away from V(m), and (2.1) gives H^1_m(Sym^2 K)=0,
so the finite-support cokernel vanishes. An explicit constructive proof appears
in Section 4.

In the alternating V-sector, contraction of a bivector is zero precisely when
the bivector is a scalar multiple of q. This is the top nontrivial exactness
identity in the Koszul complex of the regular sequence x,y,z. Hence

    H = (Sym^2 A tensor Sym^2 K)
        direct-sum (Lambda^2 A tensor S(-1) q),

and there is an exact sequence

    0 -> Sym^2 N --mu--> H
      -> Lambda^2 A tensor (S/m)(-1) -> 0.                 (3.1)

In particular H is NOT generated entirely by N-products in degree 1, but

    H_d = (im mu)_d for every d >= 2.                     (3.2)

The defect is exactly three copies of R in degree 1 and zero in every other
degree. In degree 3 there is no defect. A minimal free resolution of H is

    0 -> S(-3)^18 -> S(-2)^36 direct-sum S(-1)^3 -> H -> 0.

A minimal free resolution of the abstract Sym^2 N, now proved equal to its
product image, is

    0 -> S(-4)^3 -> S(-3)^27 -> S(-2)^45 -> Sym^2 N -> 0.

Both give degree-three rank 108 over R; this count is a consequence of the
exact resolutions, not a rank test.

## 4. Constructive factorization without a coefficient solve

Let M be a symmetric 3 by 3 matrix of homogeneous degree d with M r=0.
For d >= 2 define the symmetric polynomial matrix of degree d-2

    B_ab = sum_{k,i,l,j} epsilon_(a k i) epsilon_(b l j)
             partial_k partial_l M_ij / [d(d+1)].          (4.1)

Then exactly

    M = C B C^t.                                         (4.2)

Here C_(ia)=sum_u epsilon_(i u a) r_u. To verify (4.2), contract the two
epsilon pairs. Its (p,q) entry before division by d(d+1) becomes

    r_i r_j partial_p partial_q M_ij
    - r_i r_l partial_p partial_l M_iq
    - r_k r_j partial_k partial_q M_pj
    + r_k r_l partial_k partial_l M_pq.

Differentiating M r=0, using symmetry, and using Euler's identity gives the
four terms as 2 M_pq, +(d-1) M_pq, +(d-1) M_pq, and d(d-1) M_pq.
Their sum is d(d+1) M_pq. This is a universal differential identity. For d=1
the same identity forces M=0; degree zero follows directly from M r=0.

For an alternating block W of degree d satisfying W r=0, write W=f Q,
where Q is the skew matrix of q, namely Q=-C. The scalar can itself be
recovered without division by a coordinate:

    f = (partial_x W_23 - partial_y W_13 + partial_z W_12)/(d+2).

This follows by differentiating the axial vector (W_23,-W_13,W_12)=f r.
For d >= 2, Euler's identity and (2.2) give the polynomial product lift

    f q = [(partial_x f)(k2 wedge k3)
           +(partial_y f)(k3 wedge k1)
           +(partial_z f)(k1 wedge k2)]/(d-1).             (4.3)

For a full symmetric A tensor V matrix T, decompose each A-block T_ab into
its V-symmetric and V-skew parts. Because T_ba=T_ab^t and every block kills r,
these lie respectively in the two Cauchy sectors. Apply (4.1) and (4.3) to
obtain an explicit N-product expression. Thus the degree-three claim is a
constructive polynomial theorem, not merely a dimension comparison.

## 5. Quotient by the free P4 A-source: unconditional module assertion

Let L=P4 tensor S(-1) inject into N, with P4 free of rank 4, and set Q=N/L.
Let LN denote the image of L tensor N under symmetric multiplication. The
defining universal property of Sym^2 gives

    Sym^2 Q = Sym^2 N / LN.

Since mu was proved injective, (3.1) descends to the exact sequence

    0 -> Sym^2 Q -> H/(LN)
      -> Lambda^2 A tensor (S/m)(-1) -> 0.                 (5.1)

This needs only module injectivity of L, not a fiber-rank condition. Therefore
actual cubic polynomial C-annihilating tensors, modulo these lower-weight
A-source products, are precisely cubic polynomial elements of Sym^2 Q.
A globally split constant C-source can be removed by an exact direct-summand
quotient and introduces no saturation defect of its own.

## 6. Global sections on P2: the source-subbundle condition and its certificate

For identifying polynomial quotients with all sheaf-global representatives,
one must additionally establish that the source is a subbundle. The supplied
physical 5 by 3 relation map is

    [ z/FB,       0,                 -3x/FD ]
    [ x/(6FB),   -FC*y/(2FB*FD),       0    ]
    [ 0,         -z/FC,               0    ]
    [-y/FB,       0,                  3z/FD ]
    [ 0,         -3x/FC,             -9y/FD ].

After multiplying its ten 3 by 3 minors by Laurent units, they are

    n012=x^2 z,                   n013=xy^2-yz^2,
    n014=FB FD x^3+3 FC^2 y^2 z,   n023=xyz-z^3,
    n024=yz^2,                    n034=x^2y-xz^2,
    n123=xz^2,                    n124=xyz,
    n134=FB FD x^2z+3 FC^2 y^3,    n234=y^2z.

Their ideal is exactly m^3: the mixed monomials are either displayed or
obtained as n013+n024 and n034+n123, and the remaining cubes are

    x^3=(n014-3 FC^2 n234)/(FB FD),
    y^3=(n134-FB FD n012)/(3 FC^2),
    z^3=n124-n023.

This is a symbolic exterior-cube certificate, with every physical marking
still free. No specialization is used. Thus the relation map has locally
free rank-two cokernel on P2, and the P4 inclusion is a subbundle there.

Write D5 for the free rank-five generator space. The symmetric presentation
is therefore an exact sequence of sheaves

    0 -> Lambda^2 A tensor O(-4)
      -> A tensor D5 tensor O(-3)
      -> Sym^2 D5 tensor O(-2)
      -> Sym^2 Q~ -> 0.                                  (6.1)

The corresponding polynomial complex is also exact: its first map is
injective over the fraction field, hence over S; its first cokernel has
m-depth >=2 by its length-one free resolution. Any kernel of the next map
is supported on V(m), so it vanishes by H^0_m=0. This avoids silently
assuming exactness of a symmetric-power complex at the vertex.

Twisting (6.1) by 3 gives the line-bundle complex

    0 -> O(-1)^3 -> O^15 -> O(1)^15 -> Sym^2 Q~(3) -> 0.

Split it into two short exact sequences. Since H^1(O(n))=0 on P2 for all n
and H^2(O(-1))=0, taking global sections gives exactly

    0 -> A tensor D5
      -> Sym^2 D5 tensor S_1
      -> H^0(P2,Sym^2 Q~(3)) -> 0.                        (6.2)

This is exactly the degree-three polynomial presentation. Thus

    (Sym^2 Q)_3 isomorphic to H^0(P2,Sym^2 Q~(3)),

with 15 degree-three source relations and quotient rank 30. Degree two
likewise agrees. Degree one instead has exactly three extra global sections,
coming from H^2(Lambda^2 A tensor O(-3)), consistently with (3.1).
No assertion about possible additional lower-degree phenomena is needed.

Equivalently, the lower source-ideal sheaf J has the exact presentation

    0 -> O(-2)^6 -> P4 tensor A tensor Omega^1 -> J -> 0.

For d>=1, H^1(Omega^1(d))=0 and H^2(O(d-2))=0, hence H^1(J(d))=0.
Moreover H^1(O(d-2))=0 identifies H^0(J(d)) with polynomial LN. This gives
the same no-hidden-source-homotopy conclusion in degree three directly from
the original N presentation.

## 7. Scope of the conclusion

These results exhaust the actual cubic polynomial lower-weight symmetric
C-annihilating representatives and their stated lower source quotient.
They do NOT discard higher-weight companions created when an A-source
homotopy is lifted as alpha_U/am-(bm/am) B. Nor do they claim that completed
full-U middle relations are exhausted: higher polynomial relations can leave
U-balanced VWW remainders. Those transports and any residual full-U relation
must be tracked separately. The absence of a degree-three saturation defect
does not by itself settle that different completion problem.
