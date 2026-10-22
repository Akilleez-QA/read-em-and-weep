# Full third-normal vanishing by an actual scaling degeneration

## Theorem

Let R=P(V_+) be the positive fixed plane of HM inversion, W=V_-*, and B=End_0(F). For a general smooth inversion-even quadric Q, put C=Q intersect R and I=I_(C/Q). Then

       H0(Q,I^3 B_Q(4))=0,
       h0(Q,I^2 B_Q(4))_+ <= 9.

More precisely, fix any smooth positive conic and any nondegenerate negative-block direction. Along the nonzero scalar multiples of that block both conclusions hold outside a finite set of parameters. Hence they hold on a dense open of negative blocks for every fixed smooth positive conic, and on a nonempty open of the whole smooth-even family.

All actual sections are therefore detected by normal jets of degrees zero, one, and two. In particular the odd first-normal-jet map is injective into its 42-dimensional target. These target dimensions and the bound nine are not asserted dimensions of global section spaces.

The argument does not depend on the separate generic doubled-conic or second-normal Atiyah-class result. It uses an actual scaling family and an exact decomposition of finite ideal-power quotients.

## 1. Actual plane cohomology

The fixed-plane theorem gives the stable Steiner resolution

       0 -> A tensor O_R(-3) -> D tensor O_R(-2) -> F_R -> 0.

INVARIANT-CONIC-SECOND-NORMAL-COLLAPSE.md proves H0(B_R(1))=0. Its proof uses the actual identification A=the three-dimensional A5 representation different from V_+, followed by the injectivity of every Steiner fiber map. This vanishing is not a consequence of stability alone. Multiplication by a nonzero form gives H0(B_R(t))=0 for all t<=1.

The symmetric-square resolution at twist two is

       0 -> wedge^2 A tensor O_R(-3)
         -> A tensor D tensor O_R(-2)
         -> Sym^2 D tensor O_R(-1)
         -> B_R(2) -> 0.

Line-bundle cohomology gives h0(B_R(2))=3 and H1(B_R(2))=0. Twisting once more gives H1(B_R(3))=0. By self-duality and Serre duality,

       H1(B_R(-5))=H1(B_R(-6))=0.                         (1)

For any plane conic C, all three odd restrictions

       B_R(1)|3C,  B_R(-1)|2C,  B_R(-3)|C

have no global sections: their restriction kernels on R are all B_R(-5). Similarly

       B_R|3C,  B_R(-2)|2C,  B_R(-4)|C                   (2)

have no global sections, since their kernels are B_R(-6). Finally the restriction B_R(2)->B_R(2)|4C also has kernel B_R(-6), so

       H0(B_R(2)) -> H0(B_R(2)|4C) is an isomorphism,
       h0(B_R(2)|4C)=3.                                  (3)

Here nC means the plane Cartier thickening defined by q_C to the power n. No balance or splitting-type hypothesis is used in these restriction calculations.

## 2. The actual scaling family is proper and flat on finite jets

Fix nondegenerate positive and negative blocks and write

       Q:q_+(x)+q_-(y)=0,
       C=Q intersect R,  I=(y_1,y_2).

On U=P4 minus P(V_-), projection onto R identifies U with the total space of V_- tensor O_R(1). For every scalar epsilon there is a morphism

       g_epsilon:U->U,  (x,y)|->(x,epsilon y).

At zero it is projection onto the zero section R. At a nonzero parameter it is an automorphism taking Q onto the smooth even quadric

       Q_epsilon:q_+(x)+epsilon^(-2)q_-(y)=0.             (4)

It fixes C, identifies its ideal and all powers, and commutes with inversion. Moreover O_U(1)=p*O_R(1), so the twist four is preserved even in the limiting pullback.

Let Z=V_Q(I^9). It is projective and has reduced support C, hence is contained in U. On Z times A1 form

       M=(I^3/I^9) tensor g*B(4).

The first module is pulled back from the fixed scheme Z; the second is locally free. Thus M is flat over A1. The map p|Z:Z->R is finite: it is affine as a restriction of the vector-bundle projection and proper because Z is projective. Consequently

       N=(p times id)_* M

is coherent, flat over A1, and compatible with base change. Its fiber cohomology is exactly that of M, since p|Z is finite. Proper upper semicontinuity applies on the projective plane R.

For parity calculations, inversion acts trivially on R and A1, so its positive and negative eigensummands in N are coherent flat direct summands. One must take parity after this finite pushforward: on Z itself the action is nontrivial on the structure sheaf, so an eigensheaf need not be an O_Z-submodule. This distinction does not affect the full sheaf N but makes its parity use precise.

## 3. Exact harmonic decomposition of the ideal powers

For the fixed nondegenerate binary form q_-, let H_m be its degree-m harmonic space. The binary Fischer decomposition is

       Sym W = directsum_(m,j>=0) q_-^j H_m,
       dim H_0=1,  dim H_m=2 for m>0.

It respects total fiber degree m+2j and inversion parity (-1)^m. Universally, one can verify it by using isotropic coordinates for a nondegenerate binary form: each monomial is uniquely a quadratic power times a pure power of one of the two coordinates. This is a general algebraic identity, not a selected actual quadratic computation.

Locally on R, let f=q_+. The quadric algebra is O_R[y_1,y_2]/(q_-+f). Since the Fischer decomposition is free over C[q_-], substituting q_-=-f gives the genuine O_R-module direct sum

       p_*O_(Q intersect U)=directsum_(m>=0) H_m tensor O_R(-m).

The ideal I^n is the image of all fiber polynomials of degree at least n. In the m-th summand its exact image is the power

       f^a(n,m),  a(n,m)=max(0,ceil((n-m)/2)).             (5)

Indeed the contributing degrees are m+2j>=n, and their sum is the smallest such f-power. No different harmonic summands can cancel, since the relation preserves m. This proves the full ideal formula, not merely its associated graded version.

For I^3/I^9, put a=a(3,m), b=a(9,m). Its m-th summand is

       H_m tensor O_((b-a)C)(-m-2a)                      (6)

when b>a. The extra twist minus2a is multiplication by q_+ to the power a.

The odd indices m=1,3,5,7 give respectively

       H_1 tensor O_3C(-3),  H_3 tensor O_3C(-3),
       H_5 tensor O_2C(-5),  H_7 tensor O_C(-7).          (7)

The even indices m=0,2,4,6,8 give

       H_0 tensor O_3C(-4),  H_2 tensor O_3C(-4),
       H_4 tensor O_3C(-4),  H_6 tensor O_2C(-6),
       H_8 tensor O_C(-8).                                (8)

The index1 term starts with q_+, while the index0 and index2 even terms start with q_+ squared and q_+, respectively. Retaining these factors is essential for the twists.

## 4. Vanishing at the limiting bundle

At epsilon zero, g_0*B(4)=p*B_R(4). The actual action on B_R and O_R(4) is positive, since U evaluates onto F_R(3) with scalar inversion action. Projection formula and (7)--(8) give

       (N_0)_- = 4 copies of B_R(1)|3C
                 directsum 2 copies of B_R(-1)|2C
                 directsum 2 copies of B_C(-3),

       (N_0)_+ = 5 copies of B_R|3C
                 directsum 2 copies of B_R(-2)|2C
                 directsum 2 copies of B_C(-4).

All summands have no sections by Section 1. Hence H0(N_0)=0. Upper semicontinuity gives H0(N_epsilon)=0 on a Zariski-open neighborhood of zero. This open contains nonzero parameters, and its complement in A1 is finite. Transport through (4) proves actual finite-jet vanishing

       H0((I^3/I^9) tensor B_Q(4))=0                     (9)

for the corresponding smooth even quadrics. The same conclusion holds outside finitely many nonzero scalar negative blocks, since epsilon->epsilon^(-2) is a finite surjection on C*.

## 5. Passage to global sections and the whole even family

The established uniform ideal-power theorem gives H0(Q,I^7 B_Q(4))=0 for every smooth even Q. Hence H0(I^9 B_Q(4))=0. The exact sequence for I^9 contained in I^3 injects H0(I^3 B_Q(4)) into the group in (9), proving the main vanishing.

The finite-jet condition is open as the negative block varies: the conic ideal is a relative regular immersion, so its associated graded pieces, and therefore finite ideal-power quotients, are flat over the parameter space. Finite pushforward to R works as in Section 2. The scaling family supplies a nonempty open for every fixed positive conic. The space of nondegenerate negative blocks is irreducible, and so is the whole smooth-even parameter space. The theorem therefore holds generically in both senses stated.

The actual parity identity identifies the kernel of the odd first-normal-jet map with H0(I^3 B_Q(4))_-. Its vanishing proves first-jet detection, not surjectivity onto the 42-dimensional jet space.

## 6. The second-normal positive kernel is at most nine-dimensional

Apply the same family to the positive part of I^2/I^10, using Z=V(I^10). Formula (5) gives the limiting decomposition, after tensoring by B_R(4),

       3 copies of B_R(2)|4C,
       2 copies of B_R|3C,
       2 copies of B_R(-2)|2C,
       2 copies of B_C(-4).

The first three copies come from harmonic indices0 and2, of dimensions1 and2. The index0 term starts with q_+, while the index2 term starts without it. Indices4,6,8 give the remaining three terms. By (2)--(3), the limiting section dimension is exactly nine.

Semicontinuity bounds the general positive finite-module section dimension by nine. Uniform H0(I^10 B_Q(4))=0 injects H0(I^2 B_Q(4))_+ into this finite-module space, yielding the claimed bound. The finitely many nonempty parameter opens needed for this bound and the main theorem have nonempty intersection.

This proves an upper bound, not equality and not the threshold at most four needed in an exact-corank-four argument.

## Consequences and limits

All actual adjoint sections are detected by normal degrees zero, one, and two. On every smooth positive conic the published conic-pencil theorem excludes its largest possible splitting jump; the three finite graded layers consequently have section dimensions27,42,45, all with H1 zero. Their parities give finite restriction targets72 even and42 odd. These are not claimed global section dimensions.

At the invariant positive conic the earlier theorem gives eta=zeta_C=xi=0 for every negative block, yet the present scaling theorem still gives generic third-normal vanishing along that block family. There is no contradiction: later obstructions can kill sections even when the second-normal commutator factor is zero. Injectivity of that earlier factor was sufficient, not necessary.

The first-order odd extension obstruction and the lower-order positive excess boundary remain open. Neither exact even corank four nor full adjoint vanishing follows from these finite-jet conclusions.

## Sources and verification boundary

INVARIANT-CONIC-SECOND-NORMAL-COLLAPSE.md supplies H0(B_R(1))=0 from the actual opposite-three representation and Steiner fiber injection. FIXED-CONIC-PARITY-JETS-AND-POSITIVE-GATE.md supplies the actual parity identities and uniform seventh-power vanishing. The actual conic-pencil theorem supplies the final uniform finite-neighborhood dimensions; it is not needed for the scaling vanishing itself.

The new scaling family and exact harmonic module decomposition are proved above. verify_harmonic_jet_decomposition.py checks only their universal integer exponents, multiplicities and twists. No selected HM/source coefficient, actual matrix-rank test, scan, or experiment is used.
