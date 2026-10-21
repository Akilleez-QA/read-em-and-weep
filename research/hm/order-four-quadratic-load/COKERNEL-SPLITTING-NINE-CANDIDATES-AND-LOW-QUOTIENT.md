# Nine equivariant cokernel splittings and their forced low-degree quotients

This theorem concerns the actual Horrocks–Mumford negative hyperplane pencil. Its cokernel C_lin is an everywhere locally free, globally generated bundle of rank five and degree 26 by the published [torsion-free corollary, immutable pin f5361eacee42eb3b7df75c69f01508b66722d395](https://github.com/Akilleez-QA/read-em-and-weep/blob/f5361eacee42eb3b7df75c69f01508b66722d395/research/hm/order-four-quadratic-load/TORSION-FREE-HYPERPLANE-AND-QUADRATIC-TARGETS.md). That corollary uses the [all-special-hyperplane theorem, immutable pin 5ce98e6bef1fd849353f563b1ccfc62f4d28b8d9](https://github.com/Akilleez-QA/read-em-and-weep/blob/5ce98e6bef1fd849353f563b1ccfc62f4d28b8d9/research/hm/order-four-quadratic-load/SPECIAL-HYPERPLANE-ADJOINTS-ARE-EXACTLY-SQUARES.md). Thus torsion-freeness and j=0 are established inputs, not additional hypotheses awaiting verification.

The deductions below use exact finite representation theory and actual cohomology sequences. They do not evaluate actual multiplication coefficients or ranks. The only remaining two-way alternative explicitly retained is the vanishing or nonvanishing of the exceptional boundary.

## Results

There are 29 equivariant splittings compatible with rank, degree, central parity and H0(C_lin). Imposing the independently determined H0(C_lin(-1)) character leaves 21. The actual joint-coefficient-span surjectivity excludes all degree-zero summands and leaves twelve equivariant splittings. Finally, the actual exceptional-boundary theorem and the exact character H²(B)=W exclude rows 5, 6, 12 below, leaving **nine equivariant splittings, with nine different ordinary splitting types**.

Every survivor has a degree at most two. Thus the balanced splitting O(5)^4 + O(6) is impossible. In fact h1(C_lin(-6)) is at least three for every survivor.

Every survivor has a nonzero equivariant quotient onto O(2). Every nonzero equivariant map to O(2) is surjective. For seven of the final nine survivors this quotient and its kernel are unique up to scalar; for the other two there is a projective line of such quotient maps and the present data do not select one.

## Inputs and notation

Let G=SL(2,5), the binary icosahedral group, act on P1=P(W). The two-dimensional defining representation W is self-dual. Use the following character conventions:

* 1, A=Sym²W, V, P, D=Sym⁴W are center-even, of dimensions 1,3,3,4,5.
* W, Wp, S=Sym³W, T=Sym⁵W are center-odd, of dimensions 2,2,4,6.
* A and V are the distinct three-dimensional irreducibles; W and Wp are the distinct two-dimensional irreducibles.

The actual equivariant exact sequence is

    0 -> A tensor O(-6) -> M2 tensor O(-1)
      -> M3 tensor O -> C_lin -> 0,

where

    M2 = 2W + 2Wp + 3S + 4T, dim M2=44,
    M3 = 1 + 4A + 2V + 3P + 3D, dim M3=46.

The actual presentation is proved in [EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md, immutable pin ff324d0d7f07300adbb9b6e830c3eecfa54eaa61](https://github.com/Akilleez-QA/read-em-and-weep/blob/ff324d0d7f07300adbb9b6e830c3eecfa54eaa61/research/hm/order-four-quadratic-load/EXACT-HYPERPLANE-ADJOINT-SYZYGY-BUNDLE.md). Together with the torsion-free theorem it gives rank 5, degree 26 and global generation. It has center-even action. The section characters used are

    H0(C_lin) = 1 + 3A + V + 2P + 2D,
    H0(C_lin(-1)) = 2W + Wp + 2S + 2T.

The first identity follows from H0(C_lin)=M3−A tensor Sym⁴W and A tensor Sym⁴W=A+V+P+D. For the second identity, let I be the image of M2 O(-1) in M3 O. Since I(-1) is a subsheaf of M3 O(-1), it has no sections. Also M3 O(-1) is acyclic. The two short exact sequences therefore give

    H0(C_lin(-1)) = M2 - A tensor Sym⁵W

in the representation ring. The identity A tensor T = Wp + S + 2T proves the displayed character. This argument imposes no selected rank condition.

## Why equivariant splitting is valid

Apply ordinary Birkhoff–Grothendieck. For the maximal splitting degree d, the evaluation image

    H0(C_lin(-d)) tensor O(d) -> C_lin

is the canonical maximal-degree subbundle, hence G-invariant. The quotient has smaller splitting degrees. The underlying extension splits, since Ext¹(O(e),O(d))=H¹(O(d-e))=0 for e<d. Choose any splitting and average its translates over the finite group G. The averaged map is still a splitting, and is equivariant, because the quotient map is equivariant and |G| is invertible over C. Iterate on the quotient.

Thus

    C_lin = direct sum over d of R_d tensor O(d)

equivariantly, with ordinary semisimple G-representations R_d. Global generation forces d>=0. Since the central involution acts on O(d) as (-1)^d and on C_lin as +1, R_d has central parity (-1)^d. Finally

    H0(C_lin) = sum R_d tensor Sym^d W.

There is no projective-representation ambiguity: the chosen SL(2,5) action gives the standard genuine linearization of every O(d).

## The geometric exclusion of degree zero

The actual vanishing H²(B(1))=0 and H¹(B_R(3))=0 give surjections

    W tensor H1(B(2)) -> H1(I_R B(3)) -> H1(B(3))

from the Koszul and plane-restriction sequences. Since W is inversion-odd, the even component gives

    W tensor M2 -> M3

surjectively. This is the joint span of the two coefficient maps of the universal linear pencil.

Dualizing the pencil, the map on global sections

    M3* -> M2* tensor H0(O(1))

is the dual of this joint-span map, so it is injective. Its kernel is H0(C_lin*), which therefore vanishes. As C_lin is globally generated, this is equivalent to all splitting degrees being at least one.

The actual vanishing H²(B(1))=0 is recorded in [LOWER-TWIST-EVEN-QUADRIC-PARITY.md](LOWER-TWIST-EVEN-QUADRIC-PARITY.md) and proved in [PR455, Section 3, immutable pin 8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4](https://github.com/Akilleez-QA/read-em-and-weep/blob/8cbbe482ee50c35d52ffcdf3efb837fa8cf96af4/research/hm/twist-one-structural-vanishing/PROOF.md). The plane vanishing follows from the actual Steiner symmetric-square resolution, also displayed in [LOWEST-COKERNEL-SUMMANDS-EXCEPTIONAL-BOUNDARY.md](LOWEST-COKERNEL-SUMMANDS-EXCEPTIONAL-BOUNDARY.md).

## Exact H²(B) character and the degree-one pruning

Use U=V+W for the actual ambient five-dimensional representation, and N=A+Wp for the outer monad representation. The normalized actual HM monad has K-class

    [F] = Wp tensor [Omega²(2)] - N tensor [O(-1)] - N tensor [O],
    [Omega²(2)] = Lambda²U tensor [O] - U tensor [O(1)] + [O(2)].

Thus, writing [F]=sum Fc_i [O(i)],

    Fc_(-1)=-N,
    Fc_0=Wp tensor Lambda²U - N,
    Fc_1=-Wp tensor U,
    Fc_2=Wp.

The actual equivariant determinant is det F=O(-1), so

    [B]=[F tensor F(1)]-[O].

All twists 1+i+j here are between -1 and 5; O(-1) is acyclic and chi(O(t))=Sym^t U for t>=0. The standalone exact verifier therefore computes

    chi_G(B) = sum Fc_i tensor Fc_j tensor chi_G(O(1+i+j)) - 1
             = W - 1 - A - V - D - 2T.

The established actual ambient deformation theorem gives H0(B)=H3(B)=H4(B)=0 and H1(B)=End_0(U). Direct character decomposition gives

    H1(B) = 1 + A + V + D + 2T.

Consequently **H²(B)=W**, the defining two-dimensional representation, not Wp. The verifier computes the necessary symmetric powers in two independent ways: Newton identities from exact Adams power maps on the nine conjugacy classes, and the direct symmetric-power formula for U=Sym²Wp+W. These agree exactly. Only universal representation operations are evaluated.

The actual blowup/exceptional-boundary argument separately establishes

    H1(C_lin(-3)) = coker[H0(B_R(3)) tensor H1(O_P1(-3)) -> H2(B)].

Its proof is [LOWEST-COKERNEL-SUMMANDS-EXCEPTIONAL-BOUNDARY.md](LOWEST-COKERNEL-SUMMANDS-EXCEPTIONAL-BOUNDARY.md).

Because H²(B)=W is irreducible, this cokernel is either zero or W. The boundary has not been evaluated. Since all splitting degrees are at least one, the only contribution to H1(C_lin(-3)) is the degree-one multiplicity representation R_1, tensored with H1(O(-2)). The latter representation is trivial: Serre duality uses K_P(W)=O(-2), since det W=1. Therefore

    R_1 = 0 or W.

Rows 5 and 6 below have R_1=Wp; row 12 has R_1=W+Wp. These three are impossible. The final nine survivors are rows 1–4 and 7–11. If the actual exceptional boundary is surjective, precisely rows 1–4 remain; if it is zero, precisely rows 7–11 remain. Neither alternative is selected here.

The actual ambient theorem used above is [EXACT-AMBIENT-ADJOINT-DEFORMATIONS.md](EXACT-AMBIENT-ADJOINT-DEFORMATIONS.md).

The monad/representation convention is independently checked in [verify_negative_vertex_scalar.py](verify_negative_vertex_scalar.py). The companion [verify_h2_B0_character.py](verify_h2_B0_character.py) is standalone, outputs h2_B0_character.json, and asserts the full decomposition rather than dimension or parity alone.

## The twelve intermediate splittings and nine final survivors

In the table R(d) means R tensor O(d). Multiplicities are representation multiplicities, not individual line counts. The last column is dim Hom_G(C_lin,O(2)).

| No. | Equivariant splitting | Ordinary degrees | Invariant Hom dimension |
|---|---|---|---|
| 1 | 1(2) + P(6) | 2,6,6,6,6 | 1 |
| 2 | 1(2) + Wp(5) + Wp(7) | 2,5,5,7,7 | 1 |
| 3 | 1(2) + V(4) + 1(12) | 2,4,4,4,12 | 1 |
| 4 | 1(2) + A(2) + 1(18) | 2,2,2,2,18 | 1 |
| 5 | Wp(1) + 1(2) + W(11) | 1,1,2,11,11 | 1 |
| 6 | Wp(1) + 1(2) + 1(10) + 1(12) | 1,1,2,10,12 | 1 |
| 7 | W(1) + V(8) | 1,1,8,8,8 | 1 |
| 8 | W(1) + Wp(5) + 1(14) | 1,1,5,5,14 | 1 |
| 9 | W(1) + W(3) + 1(18) | 1,1,3,3,18 | 1 |
| 10 | W(1) + 1(2) + Wp(11) | 1,1,2,11,11 | 2 |
| 11 | W(1) + 1(2) + 1(4) + 1(18) | 1,1,2,4,18 | 2 |
| 12 | W(1) + Wp(1) + 1(22) | 1,1,1,1,22 | 1 |

The exceptional-boundary constraint excludes rows 5, 6 and 12. The remaining rows have invariant Hom dimension one in rows 1–4 and 7–9, and dimension two in rows 10–11.

## The O(2) quotient and its canonicality

For a summand R(d), equivariant maps to O(2) are

    Hom_G(R, Sym^(2-d) W), for d<=2,

and zero for d>2. Among positive-degree summands, the only contributions are 1(2) and W(1). Their maps are respectively the identity on O(2) and the evaluation quotient W tensor O(1) -> O(2). Each nonzero map is surjective at every point. A nonzero combination across several contributing summands remains surjective, since its restriction to at least one summand is already surjective.

This proves the final column and the universal existence claim. In rows 1–9 and 12 the one-dimensional Hom space determines a unique projective quotient, hence a canonical kernel. In rows 10–11 individual quotients form P1; no individual kernel is selected by these data. Nevertheless their full invariant Hom space L canonically gives a surjection

    C_lin -> L* tensor O(2).

For dim L=2, this is a canonical rank-two quotient. Indeed every nonzero element of L is nonzero in each fiber's dual, so the fiberwise dual map L -> C_lin,p* is injective.

## What these inputs cannot distinguish

All 21 candidates before the no-degree-zero pruning, and hence all nine final survivors, are realizable by some equivariant linear complex with exactly the displayed abstract source, target and kernel. This is an abstract sufficiency statement, not a claim of occurrence in the actual HM family.

For each candidate C, take its equivariant evaluation resolution

    0 -> H0(C(-1)) tensor O(-1) -> H0(C) tensor O -> C -> 0.

Add A times the dual-twisted evaluation resolution of O(5):

    0 -> O(-6) -> Sym⁵W tensor O(-1) -> Sym⁴W tensor O -> 0.

The sum has kernel A O(-6), source character M2, and target character M3, using

    A tensor Sym⁴W = A + V + P + D.

Therefore the exact linear presentation and the displayed characters alone cannot choose a survivor. Additional actual-map geometry is essential.

A short independent obstruction to the balanced type is also available: if C=O(6)+R O(5), then R is center-odd of dimension four. Sym⁶W=V+P has no invariant, and R tensor Sym⁵W has no invariant because Sym⁵W=T is irreducible of dimension six and cannot occur in R*. This contradicts the one-dimensional invariant subspace of H0(C).

## Reproducibility and scope

Run:

    python verify_h2_B0_character.py
    python enumerate_equivariant_splittings.py

The enumeration script writes c_lin_splittings.json, retaining all 29 initial candidates, all 21 character-refined candidates, all twelve no-degree-zero candidates, all nine exceptional-boundary-compatible survivors and the conditional four-candidate list. Arithmetic is exact in Q(sqrt(5)); there is no floating point arithmetic.

The first enumeration solves nonnegative multiplicities of irreducible equivariant line blocks using exact character inner products. A second independently enumerates all ordinary five-part nonnegative degree partitions of 26, decorates each equal-degree block with every allowed representation, and compares class-function values directly. The two enumerations agree. The script also verifies the full irreducible character table by orthogonality and the sum-of-squared-dimensions identity.

The character convention agrees with [verify_negative_vertex_scalar.py](verify_negative_vertex_scalar.py), SHA256 e81f548a7e0ea4069ea293ca3b86b1110c2fd6c2906e8637d1441b35f6f14af2 at this check. Both verifiers accompanying the present theorem are self-contained and require only the Python standard library. They do not import that earlier verifier or access a repository, network service, or geometric coefficient file.

No actual HM multiplication entries, source-instance coefficients, minors, or ranks were evaluated. No claim of genericity or actual splitting is inferred from the finite enumeration.
