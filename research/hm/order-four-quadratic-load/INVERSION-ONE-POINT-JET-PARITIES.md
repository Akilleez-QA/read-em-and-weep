# Inversion on the actual one-point theta interpolation

## Result and normalization

Use the actual symmetric type(2,10) polarization P, the subgroup G=K(Theta) of order25, and rho:A -> B=A/G from ONE-POINT-SEMIHOMOGENEOUS-INTERPOLATION.md. The inversion note proves that the actual P linearization has character+1 over all16 points of A[2]. For n=1,3, write

    rho_*P^n = V_n tensor W_n,

where V_n is a five-dimensional multiplicity space and W_n is the simple rank-five bundle already constructed. There is a uniquely sign-normalized involution on V_n having trace+1, hence parity dimensions(3,2). With this normalization the induced involution on W_n has the following actual parities:

    W_n fiber over0:                    (3,2),
    H0(W_1):                            (4,0),
    H0(W_3):                           (20,16),
    H0(W_1 tensor O/m_0^2):              (7,8),
    H0(W_3 tensor O/m_0^4):             (24,26),
    H1(W_1 I_0^2):                      (3,8),
    H1(W_3 I_0^4):                      (4,10).

The two last spaces have dimensions11 and14. Tensoring them with the multiplicity representation(3,2) recovers exactly the original55-space parity(25,30) and70-space parity(32,38). This determines the smaller genuine parity gates without replacing the actual multiplier by independent block maps.

## 1. The involution lift, including its sign

Set F_n=rho_*P^n. Its endomorphism algebra is the actual twisted group algebra of G and is Mat_5(C), as proved in the preceding note. It has a basis of deck operators indexed by g in G. Conjugation by the actual inversion on F_n maps the g-summand to the -g-summand, with possible nonzero scalar factors. The only fixed index is g=0, whose basis vector is the identity endomorphism and is fixed with coefficient+1. Thus the trace of this algebra automorphism is1.

Every automorphism of Mat_5(C) is inner. Choose an implementing matrix J_n. Since the algebra automorphism has order2, J_n^2 is scalar; rescale to make J_n^2=1. Conjugation by J_n on End(V_n) then has trace (trace J_n)^2. Consequently (trace J_n)^2=1. Choose the unique sign with trace J_n=+1. Its two eigenspaces have dimensions3 and2. This is the positive-trace inversion lift, equivalent to e_j -> e_-j in a compatible Schrödinger presentation, but it requires no chosen theta coefficients or coordinate matrices.

After the decomposition F_n=V_n tensor W_n, factor the actual inversion as J_n tensor I_n. The remaining factor I_n is an inversion linearization on W_n because it commutes with the full matrix algebra, and I_n^2=1. Changing the matrix-unit decomposition conjugates these structures. Reversing the sign of J_n would reverse the sign of I_n; the trace+1 normalization removes exactly this ambiguity.

## 2. Fiber and section characters

At0 in B, the fiber of F_n is the direct sum of the25 fibers of P^n over G. Inversion pairs every summand except the one over0. Its character there is+1 by the actual polarization linearization. Hence

    trace(F_n|0)=1.

Since trace(J_n)=1, it follows that trace(W_n|0)=1. Its rank is5, giving fiber parity(3,2).

The same argument works at every two-torsion point of B. The odd-degree isogeny rho induces an isomorphism A[2] -> B[2], so each fiber has exactly one inversion-fixed point upstairs, with P^n character+1. Thus all16 fixed fibers of W_n have trace1. Holomorphic Lefschetz, or the equality H0(F_n)=H0(P^n), gives

    trace H0(W_n)=4.

The already proved section dimensions4 and36 yield the section parities(4,0) and(20,16). Higher cohomology vanishes because it vanishes for the ample P^n and F_n is five copies of W_n.

## 3. One-point jet characters

Inversion acts by -1 on both tangent directions at0. The associated graded of the m-th jet filtration is

    W_n|0 tensor directsum_(0<=j<m) Sym^j(T_0*B).

Thus the jet trace is

    trace(W_n|0) times sum_(0<=j<m) (-1)^j(j+1).

It equals -1 for m=2 and -2 for m=4. The dimensions are respectively5*3=15 and5*10=50, giving jet parities(7,8) and(24,26). This uses the equivariant filtration and does not assume an arbitrarily trivialized jet bundle.

Actual beta restriction proved H0(W_1 I_0^2)=H0(W_3 I_0^4)=0. The jet evaluation exact sequences therefore give cokernel parities

    (7,8)-(4,0)=(3,8),
    (24,26)-(20,16)=(4,10).

Tensoring with(3,2) gives

    (3,2) tensor (3,8)=(25,30),
    (3,2) tensor (4,10)=(32,38),

as required by the independently computed25-point characters.

## 4. What even multipliers do, and do not, simplify

The actual quadric space has parity(9,6). For an even q, its multiplication morphism F_1 I_0^2 -> F_3 I_0^4 is equivariant. Under the decompositions, the multiplicity Hom(V_1,V_3) has parity(13,12). Even total morphisms can therefore contain both an even multiplicity factor times an even W-bundle morphism and an odd multiplicity factor times an odd W-bundle morphism. The resulting11-to14 cohomology blocks are linked by a common q, not independent and not generally diagonal.

The original55-to70 even map splits only as25 -> 32 and30 -> 38, with neither block forcing a kernel. The global twenty-boundary has the separate mismatch(8,12) -> (4,16) on the common-good locus. More robustly, the unconditional equivariant Euler proof in INVERSION-EVEN-QUADRICS-ARE-ADJOINT-BAD.md forces at least four actual full-adjoint sections on every smooth even quadric, without any good-flank assumption.

For a generic quadric neither even nor odd parity is preserved, so these block restrictions do not apply. This addendum asserts no rank for an actual selected multiplier, no independence of the blocks, and no generic full-adjoint vanishing.

Sources and dependencies: ADHPR, Proposition8.4(ii), for the actual all-even polarization, https://arxiv.org/pdf/alg-geom/9606013v2 ; ONE-POINT-SEMIHOMOGENEOUS-INTERPOLATION.md for the actual matrix-algebra decomposition and evaluation injectivity; INVERSION-EVEN-QUADRICS-ARE-ADJOINT-BAD.md for the global parity obstruction. Universal integer character checks are reproducible with verify_inversion_characters.py.
