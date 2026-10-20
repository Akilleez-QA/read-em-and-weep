# The exact adjoint section resolution and level endpoint

Work over C. Let S=Sym(T), dim T=5, F the normalized Horrocks–Mumford bundle, E=F(3), B=End_0(F), and V_s=H^0(E), dim V_s=4. Use the actual graded multiplication modules

    G_j=H^0(B(j-1)),   K_j=H^1(B(j-1)),   H_j=H^1(F(j)).

The minimal free resolution of G has exactly the terms

    0 -> 32S(-11) -> 80S(-9) + 75S(-10)
      -> 140S(-8) + 75S(-9)
      -> 10S(-6) + 60S(-7) + 25S(-8) -> G -> 0.       (1)

In particular the adjacent degree-nine terms do not cancel. Also K is level: its socle is precisely K_6, of dimension 32. These are assertions about the actual modules, not generic substitutes. The proof constructs exact module sequences and uses their Tor sequences; no selected multiplication coefficients or ranks are evaluated.

## 1. Pinned inputs

PR485 at 251d9a62e97b36ad61191bfa603cdb384a3839f3 proves that G has depth 2, projective dimension 3 and regularity 8. Its minimal generators have dimensions 10,60,25 in degrees 6,7,8; its first syzygies in degree 8 have dimension 140. The only possible shifts in successive free modules are

    F0:6..8, F1:8..9, F2:9..10, F3:10..11.

It also proves an exact symmetric-evaluation complex. Write Delta=det(V_s), a constant one-dimensional space, and let i:C->P^4 be the union of the 25 disjoint transverse evaluation-degeneracy lines. The evaluation cokernel is i_*ell, with ell|line=O(-1). The complex is

    0 -> Delta O(-5) -> Lambda^2 V_s O -> V_s E
      -> B(5) -> i_*ell^2 -> 0.                        (2)

The primary full section module has resolution

    0 -> 2S(-5) -> 20S(-3) -> 35S(-2)
      -> 4S + 15S(-1) -> Gamma_*E -> 0.               (3)

Primary cohomology H is generated in degree zero, has dimensions 5,10,10,2 in degrees 0..3 and is zero elsewhere. Its four nonzero pieces are irreducible normalizer representations. In the usual notation these are A*, A tensor W', V tensor W', and W'. This follows from the primary cohomology calculations in Horrocks–Mumford §4, together with the irreducibility criterion (2.2) and character table. PR480 proves generation and the complete linear presentation directly from the monad.

PR477 supplies the actual exact sequence

    0 -> L=V_s tensor H(-3) -> K -> N -> 0,            (4)

where M_d=H^1(I_C(d)), P_j=M_(6-j)* and N=SP_0 is an actual submodule of P. K has support 0..6 and dim K_6=32.

## 2. Levelness of K

The restriction sequence identifies M, as a graded S-module, with the cokernel of

    S -> direct sum of the 25 line coordinate rings.

This holds in all integer degrees: line-bundle H^1 on P^4 vanishes, and the line section modules have no negative pieces. Each line coordinate ring is generated in degree zero. Hence M is generated in degree zero. Graded duality then says the socle of P is concentrated in degree 6, with dimension dim M_0=24. Since N is a submodule of P, it has no socle below degree 6.

For d=0,1,2, the primary socle in degree d is the kernel of the equivariant adjoint multiplication map

    H_d -> Hom(T,H_(d+1)),   h |-> (t |-> t h).

It is an invariant subspace of the irreducible H_d. The map is not zero: generation in degree zero implies T H_d=H_(d+1), and H_(d+1) is nonzero. Its kernel is therefore zero. Thus Soc(H)=H_3 has dimension 2. Tensoring with the constant space V_s and shifting shows Soc(L) is concentrated in degree 6.

If a homogeneous socle element of K has degree below 6, its image in N is a lower-degree socle element and hence zero. Exactness of (4) places it in L, where it must again be zero. Since K has no pieces above degree 6, every element of K_6 is in its socle. Consequently

    Soc(K)=K_6,   dim Soc(K)=32.                       (5)

No splitting of (4) is asserted or used.

## 3. Last term and a preliminary one-parameter table

For the full section module, local cohomology gives H_m^2(G)=K. Graded local duality over the five-variable polynomial ring gives

    Ext^3_S(G,S(-5)) = K^vee,

where (K^vee)_d=Hom_C(K_(-d),C). In a minimal length-three free resolution, the minimal generators of this Ext module are the duals of the final free summands: the image of the preceding dual differential lies in the irrelevant ideal times the final dual free module. Equation (5) says K^vee has 32 minimal generators, all in degree -6. Since Hom(S(-b),S(-5)) has its generator in degree 5-b, the final term is precisely 32S(-11).

The Hilbert numerator of G is

    10t^6 + 60t^7 - 115t^8 + 5t^9 + 75t^10 - 32t^11.  (6)

For example it follows by multiplying its Hilbert series by (1-t)^5: G_6=10 and, for j>=7, dim G_j=chi(B(j-1)), where

    chi(B(t))=3 binom(t+4,4)-(15/2)t^2-(75/2)t-25.

This gives dim G_7,...,G_11=110,335,680,1175,1853. The sum of numerator coefficients is 3, as required by rank B=3.

The shift windows and known generators from PR485, together with (6), now leave just a nonnegative integer a:

    F1=140S(-8)+aS(-9),
    F2=(a+5)S(-9)+75S(-10),
    F3=32S(-11).                                      (7)

Equal shifts in adjacent terms do not justify cancellation. The following actual module sequence determines a.

## 4. The image and line-residue section modules

Split (2), after twisting by t, into

    0 -> Delta O(t-5) -> Lambda^2 V_s O(t) -> A_t -> 0,
    0 -> A_t -> V_s E(t) -> J_t -> 0,
    0 -> J_t -> B(5+t) -> i_*ell^2(t) -> 0.            (8)

Here A_t and J_t are twists of fixed image sheaves. Define graded modules

    mathcal A_j=H^0(A_(j-6)),
    mathcal J_j=H^0(J_(j-6)),
    R_j=H^0(C,ell^2(j-6)).

These definitions include every integer degree. Intermediate line-bundle cohomology on P^4 vanishes, so the first sequence of (8) gives H^1(A_t)=H^2(A_t)=0 for every t, and an exact sequence

    0 -> Delta S(-11) -> Lambda^2 V_s S(-6)
      -> mathcal A -> 0.                              (9)

The second sequence gives both

    0 -> mathcal A -> (V_s tensor Gamma_*E)(-6)
      -> mathcal J -> 0                               (10)

and H^1(J_t)=V_s tensor H^1(E(t)). The latter group is nonzero only when t+3 lies in 0..3, hence, with t=j-6, only in degrees j=3..6.

Each component of ell^2 has degree -2 on its line. Noncanonically, as an S-module,

    R = direct sum over 25 lines of (S/I_line)(-8).    (11)

Thus R is zero below degree 8. In the last sequence of (8), the graded connecting map R_j->H^1(J_(j-6)) is zero in every degree because the supports of its source and target are disjoint. Taking sections therefore gives the actual exact graded sequence

    0 -> mathcal J -> G -> R -> 0.                    (12)

All maps in (9),(10),(12) are induced by sheaf maps and commute with polynomial multiplication. Exactness here is not inferred from dimensions.

## 5. The degree-nine relation space is exactly 75-dimensional

Tensor (3) with V_s and shift by 6. Its free terms resolving the middle module of (10) have dimensions and shifts

    F0=16S(-6)+60S(-7), F1=140S(-8),
    F2=80S(-9), F3=8S(-11).

Lift the injection in (10) to these free resolutions and take its mapping cone using (9). This is a free resolution of mathcal J. At degree 6 the map from Lambda^2 V_s to V_s tensor V_s is the standard alternating inclusion, hence injective. Its six scalar pairs can be canceled. The resulting, not necessarily minimal, free resolution has terms

    F0=10S(-6)+60S(-7),
    F1=140S(-8),
    F2=80S(-9)+S(-11),
    F3=8S(-11).                                      (13)

The determinant factors do not affect dimensions. No other cancellation is assumed. A free resolution whose first free term is 140S(-8) implies Tor_1(mathcal J,C)_9=0, and its zeroth free term implies Tor_0(mathcal J,C)_9=0. These assertions remain true even if (13) is not minimal: after tensoring with C, its chain groups in the indicated positions and degree are zero.

A line in P^4 has ideal generated by three independent linear forms. Its coordinate ring has their Koszul resolution. Equation (11) therefore gives

    Tor_1(R,C)_9 = C^75.                              (14)

Apply the Tor sequence to (12), in internal degree 9:

    Tor_1(mathcal J,C)_9 -> Tor_1(G,C)_9
      -> Tor_1(R,C)_9 -> Tor_0(mathcal J,C)_9.

Both outer terms are zero by (13). Hence there is an actual isomorphism

    Tor_1(G,C)_9 ≅ Tor_1(R,C)_9,

and a=75 in (7). This proves the full resolution (1). In particular the 80 degree-nine second syzygies and 75 degree-nine first syzygies are both minimal. Their coincidence of internal degree is not a license to remove them. No matrix rank was calculated to establish this.

## 6. Consequence for the adjoint cohomology tail

PR485 gives actual isomorphisms Tor_i(K,C)_n ≅ Tor_(i-2)(G,C)_n for n>=7 and 2<=i<=5. Combining them with (1) determines the whole high tail:

    Tor_2(K)_7:60, Tor_2(K)_8:25;
    Tor_3(K)_8:140, Tor_3(K)_9:75;
    Tor_4(K)_9:80, Tor_4(K)_10:75;
    Tor_5(K)_11:32.

All other entries with n>=7 and 2<=i<=5 vanish. This does not alter or decide the separate lower-degree cubic ambiguity.

## Dependencies and verification boundary

- PR485, section generators, compact symmetric-evaluation complex, depth, regularity and high-tail comparison: https://github.com/Akilleez-QA/read-em-and-weep/blob/251d9a62e97b36ad61191bfa603cdb384a3839f3/research/hm/section-tail/PROOF.md
- PR477, actual nonsplit primary–Rao extension and cohomology supports: https://github.com/Akilleez-QA/read-em-and-weep/blob/ff87076794e97238150485b12183c3cd0f4711e4/research/hm/adjoint-primary-extension/PROOF.md
- PR480, complete primary linear presentation: https://github.com/Akilleez-QA/read-em-and-weep/blob/0fa60123ee683a771a97c0150108a0c3c4f2e516/research/hm/quartic-presentation/PROOF.md
- PR167, primary section resolution: https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md
- Horrocks–Mumford (1973), §2(2.2), §4 and character appendix: https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

This is a structural mathematical proof, not a formal proof-assistant check. It determines the actual full section Betti table and the entire high adjoint syzygy tail, not just allowable shifts. It does not evaluate the original fixed polynomial pair, its Tor correction, selected-source membership, higher-order lifting, or algebraicity. No selected HM/source-instance evaluation, numerical multiplication matrix or rank, coefficient search, generator/checker, or large computation was performed.
