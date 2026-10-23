# Conic kernels: saturation, cubic lifting, and linear conic legs

This independently checks the precise conic extension of the frozen exact-C
theorem. All statements are over

    R = Q[FB^(+/-1), FC^(+/-1), FD^(+/-1)],
    S = R[x,y,z], q = xy+z^2, barS = S/(q), v=(x,y,z)^t.

Any extra markings may remain independent units. No points, parameter values,
matrix ranks, coefficient-fitting solve, or full-U completion are used.

## 1. Exact statement and scope

Let A be free of rank three and F=A tensor R^3 tensor S. Define

    H = {T in Sym^2 F : T(id_A tensor v)=0},
    barH = {T in Sym^2(F tensor barS) : T(id_A tensor v)=0 in barS}.

The contraction in these definitions is a literal polynomial contraction.
Then barH is saturated for the irrelevant ideal (x,y,z), and there is an exact
sequence of R-modules

    0 -> q H_1 -> H_3 -> barH_3 -> 0.                 (1.1)

Equivalently, every symmetric homogeneous cubic T whose contraction is
divisible by q has an explicit decomposition

    T = T_exact + q B,
    T_exact in H_3, B symmetric and homogeneous linear. (1.2)

The exact lift is unique modulo q H_1, not uniquely as a polynomial tensor.
Here H_1 is the three-dimensional alternating-A channel from the frozen
resolution. The claim is a relative polynomial theorem, not a fiber count.

This does NOT say that H/qH is saturated in every degree. It does NOT replace
an equation with A/C source ends by a literal q-annihilation equation. Such
source ends must first be retained or removed by an authorized, explicit
normalization. It does NOT identify full-U completions of the same lower
tensor and does NOT set a q-middle, higher-weight remainder, or anomaly to zero.

## 2. Saturation and restriction to the conic

Both S and barS have no irrelevant local cohomology in degrees zero and one:
their irrelevant depths are respectively three and two. For barS this follows
also from 0 -> S(-2) --q--> S -> barS -> 0, since q is a nonzerodivisor.

Write barH as the kernel of its contraction map between finite graded free
barS-modules, and let I be the image. The module I is a submodule of a free
module and has no irrelevant torsion. The local-cohomology sequence for

    0 -> barH -> free -> I -> 0

gives H^0_m(barH)=H^1_m(barH)=0. Consequently, in every degree,

    barH_d = H^0(Proj(barS), barH~(d)).                (2.1)

The same argument over S, or the frozen resolution, gives the corresponding
identity for H. This argument is valid over R, not merely over its fraction
field.

On P^2_R, the row v^t is the surjection O^3 -> O(1). Its kernel E is
Omega^1(1). Since this sequence splits on each standard coordinate chart,
the symmetric-tensor annihilator is locally exactly

    H~ = Sym^2(A tensor E).

In particular H~ is locally free. For the closed conic i:V(q) -> P^2_R,
the same chartwise splitting proves

    barH~ = i^* H~.                                  (2.2)

No assertion that tensoring a general kernel preserves exactness is needed.
It is the locally split vector-bundle description that proves (2.2).

As q defines a Cartier divisor, restriction gives

    0 -> H~(1) --q--> H~(3) -> i_* barH~(3) -> 0.

The proven frozen resolution, twisted by one, is

    0 -> O(-2)^18 -> O(-1)^36 direct-sum O^3
      -> H~(1) -> 0.

On relative P^2_R, H^1(O(n))=0 for every n and H^2(O(-2))=0. Its long exact
sequence therefore proves H^1(H~(1))=0. Combining restriction with (2.1)
proves (1.1). In particular the R-ranks are 3 -> 108 -> 105, as consequences
of the exact resolution and sequence, not evidence used to prove them.

## 3. Coordinate-free-in-coefficients polynomial correction

Here derivatives refer only to x,y,z, never to the physical markings. Let r
be any homogeneous quadratic three-vector, J_ij=partial_j r_i, and f=v^t r.
Euler's identity gives

    J v=2r, J^t v=grad(f)-r, Hess(f) v=2 grad(f).

Thus the symmetric linear matrix

    Gamma_plus(r) = J+J^t-(1/2)Hess(f)                (3.1)

satisfies Gamma_plus(r) v=r for EVERY quadratic r. The skew linear matrix

    Gamma_minus(r) = (J-J^t)/3                       (3.2)

satisfies the full off-kernel identity

    Gamma_minus(r) v=r-(1/3)grad(f).

It is a right inverse when v^t r=0. These are universal differential
identities, not reconstructed solutions of a coefficient matrix.

For a V-symmetric cubic block M with Mv=qr, (3.1) gives

    (M-q Gamma_plus(r))v=0.

For a V-skew cubic block W with Wv=qr, skew symmetry implies
q(v^t r)=v^t Wv=0; q is a nonzerodivisor, so v^t r=0. Formula (3.2) therefore
gives (W-q Gamma_minus(r))v=0.

For a full symmetric tensor T on A tensor V, write its three-by-three A
blocks as T_ab, so T_ba=T_ab^t. Put

    r_ab = (T_ab v)/q,
    r_ab^plus = (r_ab+r_ba)/2,
    r_ab^minus = (r_ab-r_ba)/2,
    B_ab = Gamma_plus(r_ab^plus)+Gamma_minus(r_ab^minus).

The plus block is V-symmetric and A-symmetric; the minus block is V-skew and
A-skew. Hence B_ba=B_ab^t. Blockwise B_ab v=r_ab, proving (1.2).

If a representative is changed by q B0, with B0 symmetric linear, the two
corrected exact lifts differ by q times an exactly annihilating linear
tensor. Thus the construction induces the canonical isomorphism
H_3/(q H_1) = barH_3, even though the displayed representative correction is
not unique.

For a constant C-source summand, a C/F cross-block has a scalar quadratic
defect r. The linear vector correction grad(r)/2 has scalar contraction r
by Euler. The C/C block needs no correction. Consequently the constant
physical splitting can include the C-source cross blocks without changing
the argument or discarding their source data.

## 4. Four linear conic legs and the complete shifts

Let C_w denote the matrix of cross product with w and put

    g=(y/2,x/2,z)^t=(1/2)grad(q),  v^t g=q,
    L=[C_v, g].

Then barK=ker(v^t:barS^3 -> barS(1)) is generated by the three linear Koszul
columns of C_v and the linear gradient-q column g. Indeed lift bar k to k
over S and write v^t k=q a. Then k-g a is an exact Koszul syzygy over S,
so k=C_v h+g a. This proves surjectivity without any field or point argument.
For homogeneous k of degree d, both h and a have degree d-1. If
w=k-g a, one may choose h=-curl(w)/(d+1), since C_v curl(w)=-(d+1)w.

Define the linear four-by-four matrices, with the indicated block sizes,

    D = [ v   -C_g ]             E = [ g^t   0 ]
        [ 0    v^t ],                [ C_v   g ].

The row order of D is (h_1,h_2,h_3,a), and its column order is
(b,t_1,t_2,t_3). The row/column orders reverse for E. The cross-product
identity C_v C_g=g v^t-q I gives

    L D=[0,q I_3],  D E=q I_4,  E D=q I_4.            (4.1)

Every relation on L modulo q is generated by D. To see this, lift it as

    C_v h+g a=q t.

Contracting by v gives a=v^t t. Thus C_v(h+C_g t)=0, and Koszul exactness
over S gives h+C_g t=v b. Hence (h,a)=D(b,t). For the later terms, if
D u=q w, multiplication by E and cancellation of q gives u=E w; the
analogous argument with D and E exchanged proves the other exactness.

Therefore the complete graded resolution is

    ... -> barS(-4)^4 --D--> barS(-3)^4 --E-->
        -> barS(-2)^4 --D--> barS(-1)^4 --L--> barK -> 0. (4.2)

All maps are linear; the four degree-one generators are genuinely needed,
as no nonzero constant relation exists. This periodic conic resolution must
not be confused with tensoring the two-step S-Koszul resolution with barS.

Under the frozen constant physical splitting, the literal conic C-kernel is

    Csource tensor barS direct-sum Rsplit(A tensor barK).

Thus its free generators have shifts Csource tensor barS and
A tensor barS(-1)^4, and its successive relation modules are
A tensor barS(-2)^4, A tensor barS(-3)^4, and so on. The differential has
zero Csource component. This is the exact graded source bookkeeping before
further A-source quotienting.

For a physical polynomial leg y with literal lambda(y)=q a, subtracting
Rsplit(id_A tensor g)a leaves an exact-C leg. It adds no direct Csource
component because Zeta Rsplit=0. Reconstructing the remaining exact leg
still uses the frozen relation

    Y Rel=-Acoeff H+C Zeta Acoeff H.

In particular its C shift must be retained. None of this identifies the
full-U completion of a conic leg or the completions of equivalent lower
representatives.

There is also a specific q-source remainder in a conic relation. For A-valued
parameters b,t put h=v b-C_g t and a=v^t t, blockwise. The identity over S is

    Rsplit(id_A tensor C_v)h + Ggrad a = q Rsplit(t),
    Ggrad=Rsplit(id_A tensor g).

Use the frozen constant generator conversion (with the harmless constant
change from its d2 convention to C_v) to write the first term as

    (Acoeff-C Zeta Acoeff) H_new + Y R_new.

Then the relation with every source shift retained is

    Y R_new + Ggrad a
      = -Acoeff H_new+C Zeta Acoeff H_new+q Rsplit(t). (4.3)

It becomes a source relation modulo q, but is not an exact source relation
over S unless its displayed q-leg remainder is included. Formula (4.3) does
not require any new physical coefficient assignment.

## 5. Reproduction

    python graded-leg-module/conic_verify_kernel_lifting.py

The reusable correction functions are in conic_kernel_lifting.py. The
verifier checks the differential formulas on wholly formal quadratic
vectors, both matrix-factorization identities, the signed Koszul homotopy,
and the complete three-A-channel cubic adapter with every potential and
linear-correction coefficient independent. The algebra proof establishes
coverage; the verifier checks the polynomial formulas. No frozen files are
modified.
