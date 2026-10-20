# Simultaneous interpolation and a quintic reduction for the fixed pair

Work over C on Y=P^4. Let E=F(3) be the positive Horrocks–Mumford bundle, B=End_0(F), V=H^0(E), D=det V, and C the disjoint union of its twenty-five transverse evaluation-degeneracy lines. To avoid confusing a primary cohomology image with a line bundle, write T=i_*ell for the evaluation cokernel; ell has degree -1 on each component of C.

Fix nonzero u∈S_2 and v∈S_3. Put

    A=H^1(B(5)),  L=im[V⊗H^1(E)→A],
    U=uH^1(B(3))+vH^1(B(2)),  Q_5=A/U,
    R=A/(L+U).

Here dim A=32 and dim L=8 by PR456. All assertions below are structural: no selected coefficients, restrictions, or multiplication matrices are evaluated.

## 1. The missing quadratic residue model

The fixed-cubic interpolation proof gives the locally free resolution

    0→D O(-5)→Λ²V O→V⊗E→Sym²E→i_*ell²→0,        (1)

and its canonical duality identification

    ω_C⊗ell^(-2) ≅ D* O_C.                       (2)

Twist (1) by -2. Split it into its three image short exact sequences. Intermediate line-bundle cohomology vanishes, while the primary HM cohomology gives H²(E(-2))=H³(E(-2))=0. Also H⁰(ell²(-2))=0, and H²(B(3))=0 by PR167. Consequently

    0→V⊗H¹(F(1))→H¹(B(3))→H¹(ell²(-2))
      →D⊗H⁴(O(-7))→0.                          (3)

The first arrow is the natural cup product, not an arbitrarily chosen subspace. It is injective. Let P_3 denote its image and C_3=H¹(B(3))/P_3. Since h¹F(1)=10, the dimensions in (3) are 40,100,75,15, and dim C_3=60.

Serre duality applied to the same resolution identifies the last arrow's transpose with restriction, with the common determinant line in (2). Therefore

    C_3* ≅ D*⊗[H⁰(O_C(2))/res(S_2)].             (4)

In particular quadratic restriction is injective. Together with the cubic result, if P_2=V⊗H¹(F) and C_2=H¹(B(2))/P_2, then

    C_2* ≅ D*⊗[H⁰(O_C(3))/res(S_3)],
    (A/L)* ≅ D*⊗[H⁰(O_C)/C].                   (5)

The dimension h¹B(3)=100 here is a consequence of the geometric resolution and the cited vanishings, not a computational table input.

## 2. Exact paired interpolation

Multiplication by u and v carries P_3 and P_2, respectively, into L. Thus the projected image U in A/L is the image of

    C_3 ⊕ C_2 → A/L,  (x,y)↦ux+vy.

Naturality of (1), (2) and Serre duality identifies its transpose, after retaining the common D* factor, as

    [λ] ↦ ([λ u|C],[λ v|C])

from H⁰(O_C)/C to the direct sum of the two restriction cokernels in (4)-(5). It follows that

    R* ≅ D*⊗W(u,v),                             (6)

where W(u,v) is the space of tuples (λ_l) indexed by the twenty-five lines, modulo common constants, for which there exist f∈S_2 and g∈S_3 satisfying

    f|l=λ_l u|l,   g|l=λ_l v|l   for every l.   (7)

Restriction is injective in degrees two and three, so f and g are unique for a specified tuple. The same tuple must serve both equations. Taking two unrelated single-form interpolation kernels or counting them separately would not give (6).

The primary part has not disappeared. There is always an exact sequence

    0→L/(L∩U)→Q_5→R→0.                         (8)

Thus Q_5 vanishes if and only if both L⊂U and W(u,v)=0. In terms of M_j=H¹(F(j)), the condition

    uM_1+vM_0=M_3                                (9)

is sufficient for L⊂U: tensor (9) with V and use the natural cup maps. It is not claimed necessary, since other classes can also contribute to L∩U. Neither (9) nor L⊂U is assumed for the original fixed pair.

## 3. A quintic obstruction with an exact kernel

Assume now gcd(u,v)=1 in the polynomial ring, equivalently the two nonzero forms constitute a regular sequence. Let k be the number of component lines contained in both V(u) and V(v). For a tuple satisfying (7), define

    Φ([λ])=vf-ug ∈ H⁰(I_C(5)).                  (10)

Changing λ by a common constant changes (f,g) by that constant times (u,v), so leaves (10) unchanged. Equation (7) proves its restriction to C is zero.

The kernel of Φ has dimension exactly k and consists of classes represented by tuples supported on the common contained lines. Indeed vf=ug and coprimality imply u divides f and v divides g. Degree equality forces f=cu and g=cv with the same scalar c. Therefore λ_l=c on each line on which at least one of u or v does not vanish identically; only the k common contained lines leave λ_l free. Conversely those supported tuples have f=g=0 and lie in the kernel. At least one line is not common contained, since a nonzero quadric cannot vanish on all of C by injectivity of restriction, so these k classes remain independent modulo common constants.

Consequently there is an exact sequence

    0→C^k→W(u,v)→J(u,v)→0,                     (11)

where J(u,v)=im Φ is a subspace of H⁰(I_C(5))∩(u,v)_5. In particular dim R≥k. A common contained line is a genuine obstruction even after allowing the quadratic and cubic simultaneously.

## 4. No-common-zero case: exact quintic intersection

Suppose further that C∩V(u,v) is empty. On every component line the binary forms u|l and v|l have no common zero, hence are nonzero and coprime. This gives k=0.

For any h∈H⁰(I_C(5))∩(u,v)_5, write h=vf-ug with f∈S_2 and g∈S_3. Restriction to l gives v_l f_l=u_l g_l. Coprimality on l implies u_l divides f_l and v_l divides g_l; equal degrees force a common constant λ_l. Thus (7) holds. Changing the representation of h changes (f,g) only by c(u,v), by global coprimality, so changes λ only by a common constant. Hence (10) is an isomorphism

    W(u,v) ≅ H⁰(I_C(5))∩(u,v)_5.               (12)

This replaces simultaneous interpolation by an intersection of quintic spaces. The emptiness assumption is essential to this surjectivity argument. Having no component line contained in both forms gives injectivity in (10), but does not by itself justify (12).

## 5. Why the quintic target really has dimension six

The six invariant quintics of Horrocks–Mumford §3 generate the sheaf ideal of C and are linearly independent. Sheaf generation alone is not enough to conclude h⁰(I_C(5))=6: possible saturation sections must be excluded.

Apply the Eagon–Northcott complex to the rank-two evaluation map V O→E. Its degeneracy locus has codimension three and is transverse, so its maximal-minor resolution, twisted by det E=O(5), is exact:

    0→D⊗Sym²E*→Λ³V⊗E*→Λ²V O→I_C(5)→0.       (13)

In the transverse normal form, canceling unit maps in this nonminimal complex leaves the Koszul resolution of (x,y,z), which also verifies local exactness. Let K be the image of the middle map. Since E*=F(-2), H¹(E*)=0. Also Sym²E*=B(-5). The sequence defining K therefore gives an injection

    H¹(K) ↪ D⊗H²(B(-5)).

The sequence 0→K→Λ²V O→I_C(5)→0 identifies the quotient of H⁰(I_C(5)) by the six minors with H¹(K). By Serre duality, h²B(-5)=h²B(0)≤2, using the structural exterior-image bound of PR455. Thus there are at most two additional quintic sections.

All maps and spaces are stable under the HM normalizer N. The center acts trivially on degree-five polynomials, and the nontrivial characters of H_5/Z occur in a single orbit of size 24 under N/H_5=SL_2(F_5). Any nontrivial character in the quotient would therefore require dimension at least 24, impossible. Its invariant part is also zero: HM Theorem 3.5 says the entire invariant subspace of S_5 has dimension six, and these are precisely the six independent minors: HM §4, printed p.73, identifies the wedge of the invariant section space with all invariant quintics and then proves that every section is invariant. Thus the ordinary polynomial linearization here is the one in that explicit identification, not a choice made from dimension alone. Invariants are exact over C for this finite group. Hence the quotient is zero, proving

    h⁰(I_C(5))=6.                              (14)

This saturation exclusion uses PR455's proven bound, not a selected rank computation or a computational cohomology table.

Combining (8), (11) and (14) gives, for globally coprime u,v,

    k ≤ dim R ≤ 6+k,
    dim Q_5 ≤ 14+k.                             (15)

If primary coverage (9), or more generally L⊂U, holds, the latter improves to dim Q_5≤6+k. Under C∩V(u,v)=empty, (12) determines the residual dimension exactly by the six-dimensional quintic intersection. With L⊂U as well, Q_5=0 is equivalent to that intersection being zero.

## Dependencies and limits

- PR457, commit 961694c4f3c805f0d58508811a42da4030dce7a6, the exact resolution (1), duality (2), cubic and degree-five residue models; proof SHA256 a71ce5288ed568525d65236628092b4b2b9545957c5834295286d35191557d31:
https://github.com/Akilleez-QA/read-em-and-weep/blob/961694c4f3c805f0d58508811a42da4030dce7a6/research/hm/fixed-cubic-interpolation/PROOF.md
- PR456, commit 07c11a096970a58f5f275b1438d4df3a27a1c6dd, geometric target and primary image:
https://github.com/Akilleez-QA/read-em-and-weep/blob/07c11a096970a58f5f275b1438d4df3a27a1c6dd/research/hm/symmetric-evaluation/PROOF.md
- PR455, commit 8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4, structural h²B(0)≤2:
https://github.com/Akilleez-QA/read-em-and-weep/blob/8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4/research/hm/twist-one-structural-vanishing/PROOF.md
- PR167, commit 063da90fc4543304e87e701cdefcc08225412f17, primary cohomology and H²B(t)=0 for t≥2:
https://github.com/Akilleez-QA/read-em-and-weep/blob/063da90fc4543304e87e701cdefcc08225412f17/research/conductor-normalization/sharper-hm-regularity/SHARPEST-BOUND.md
- PR451, commit ed8841c18f103e71b84c0e9376e20a2a4ed2ef9c, the order-five fixed-pair quotient:
https://github.com/Akilleez-QA/read-em-and-weep/blob/ed8841c18f103e71b84c0e9376e20a2a4ed2ef9c/research/hm/order-five-cubic-defect/PROOF.md
- Horrocks–Mumford, Topology 12 (1973), §3, Theorem 3.5, §4 and the proof of Theorem 5.1:
https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

The contribution is a simultaneous fixed-pair residue criterion, exact separation of the remaining primary obstruction, and a six-dimensional quintic reduction with explicit hypotheses. No emptiness, primary coverage, or quintic intersection has been checked for the original selected pair. Its Q_5 remains unresolved. Actual-source membership, six pure conditions, higher-order module lifting and algebraicity remain separate. This is a mathematical proof for review, not formal verification.
