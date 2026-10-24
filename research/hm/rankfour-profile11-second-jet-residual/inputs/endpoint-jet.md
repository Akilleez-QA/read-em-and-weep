# Intrinsic first jets force the balanced actual dual endpoint

## 1. Statement, scope and immutable inputs

Work over C with the original physical binary icosahedral group G=SL2(F5), the parameter line P(W*), its fixed determinant identification, and the actual constant ambient connection. The physical representations are W of dimension two, A_std=Sym2 W, S4=Sym3 W, D=Sym4 W and T6=Sym5 W. No change of parameter or linearization is made.

Assume the original actual saturated E in H O has rank seventeen, degree -54, derivative rank four and maximal ordered plateau (1,1), and its primal quotient is one of

    A_q=F+O(-8),
    F=O(2)+2O(4),       or       F=W O(3)+O(4).       (1)

This theorem does not concern the separate top-degree-four triplet A_std O(4)+O(-8).

The complete pair-defect theorem PR1197 at 0156405384eefb3efe08d724e682b4a839157bfc is retained in inputs/pair-defect.md. The original presentation and physical action are retained in inputs/actual.md at db51525015bb7c5e825833d550d08dedf6f6ea96. INPUTS.json gives full paths, URLs, lengths and hashes. We import their actual geometric premises, including the following conclusions of PR1197:

- There is a genuine constant decomposition H=C direct-sum J, dim C=21 and dim J=9. The actual E decomposes as E0 in C O and the complete octic Veronese line in J O.
- In the genuine constant ambient C* O, put S0=(C O/E0)*, L0=S0^- and B0=S0/L0. The actual S0 has rank five and degree -46; L0 has rank two and degree -18. There is a coherent injection, not assumed saturated,

      i:B0 -> F*(-2).                               (2)

- The original transpose determinant defect is t=12, and

      L0=W O(-9)       or       O(-8)+O(-10).        (3)

- The original actual dual endpoint and quotient decompose in constant ambient summands as

      L=S^-=L0 direct-sum Sym6 W O(-2),
      B=S/L=B0 direct-sum O(6).                     (4)

We prove:

1. The split form O(-8)+O(-10) in (3) is impossible. Necessarily L0=W O(-9).
2. Its ACTUAL second fundamental form has rank one everywhere, exact kernel O(-10), and saturated image isomorphic to O(-8) in B0(-2). The image is saturated even over the twelve-point defect support of (2).
3. The actual first osculating bundle of this O(-10) line is exactly L0. The actual positive modification L0^+ is saturated, of rank three and degree -24, with L0^+/L0=O(-6).
4. For the original endpoint, the actual second fundamental form has rank two everywhere and

      L^-=O(-10) direct-sum T6 O(-3),
      rank L^-=7,       degree L^-=-28.             (5)

The original defect remains twelve. Neither primal quotient in (1) is excluded or asserted realized. No assertion about completeness of the coefficient system of the new O(-10) line is made.

## 2. Actual derivative maps and the horizontal obstruction

For a saturated subbundle A of a genuine constant bundle V O, let beta_A:A->(V O/A)(-2) denote the actual second fundamental form. Its kernel A^- is saturated. Its positive modification A^+ is the inverse image of the saturation of image(beta_A)(2) in V O/A.

Since L0=S0^-, the actual beta_L0 lands in (S0/L0)(-2)=B0(-2). This is the ordinary differentiation of sections in the constant ambient C* O, followed by the appropriate quotient. It assigns no connection to B0. Composing with (2) gives the equivariant map

      gamma:L0 -> B0(-2) -> F*(-4).                 (6)

The last target is

      O(-6)+2O(-8),       or       W O(-7)+O(-8).    (7)

Every subbundle used below is saturated in C* O. If a nonzero such subbundle has zero second fundamental form, the constant connection preserves it. Its classifying map to the Grassmannian has zero differential and is constant in characteristic zero. The subbundle is therefore a constant subbundle and has degree zero. In particular, no negative bundle or line considered below is horizontal.

## 3. The fixed low-degree Hom spaces

Fixed determinant identifies W*=W. Clebsch--Gordan and the physical irreducibility of A_std and D give

      W tensor W=1+A_std,
      W tensor Sym3 W=A_std+D,
      W tensor A_std=W+S4.                          (8)

Consequently the following equivariant bundle Hom dimensions are fixed:

      Hom_G(O(-10),O(-6))=0,
      Hom_G(O(-10),O(-8))=0,
      Hom_G(O(-10),W O(-7))=0;

      Hom_G(W O(-9),O(-6))=0,
      dim Hom_G(W O(-9),O(-8))=1,
      dim Hom_G(W O(-9),W O(-7))=1,
      dim Hom_G(O(-8),W O(-7))=1.                   (9)

For example the first three section representations are D, A_std and W tensor Sym3 W=A_std+D, all without invariants. The penultimate Hom dimension is the multiplicity of W in W tensor Sym2 W=W+S4.

Use the canonical physical Euler maps

      epsilon:W O(-9) ->> O(-8),
      eta:O(-8) -> W O(-7),                         (10)

with respective exact sequences

      0 -> O(-10) -> W O(-9) -> O(-8) -> 0,
      0 -> O(-8) -> W O(-7) -> O(-6) -> 0.

Thus eta is saturated, epsilon is onto, and eta epsilon is nonzero and generates the corresponding one-dimensional Hom space in (9). These are universal Euler maps, not chosen actual coefficient evaluations.

## 4. A first-jet lemma for an arbitrary actual constant linear series

Let U=O(-d) be a saturated actual line in V O, where V is any constant finite-dimensional space. Assume U is contained in a saturated rank-two bundle M in V O and its actual second fundamental form factors through M/U, giving an isomorphism

      delta:U -> (M/U)(-2).                         (11)

Then the actual first osculating bundle of U equals M, and canonically

      M is isomorphic to P^1(O(d))*.                (12)

Here P^1 denotes the first principal-parts bundle. To prove this using the ACTUAL linear series, dualize U->V O. The resulting constant sections define a linear map V*->H0(O(d)); its image need not be the full section space. Taking the first jet of each of these constant sections, then extending O-linearly, defines

      ev_1:V* O -> P^1(O(d)).                       (13)

It is important that (13) is O-linear extension from constant sections, not the non-O-linear operation of taking jets of arbitrary O-linear combinations.

In a formal local coordinate and a local frame u of U, the dual of (13) has image generated by u and its derivative. This is the intrinsic local formula for principal parts, valid for any constant linear series. Condition (11) says exactly that the class of the derivative modulo U is a nonzero generator at every point. Thus (13) is onto everywhere. Its dual is a saturated rank-two inclusion with image precisely the full local preimage of M/U, namely M. In particular there is no saturation discrepancy. Naturality of jets and evaluation makes this identification equivariant whenever the data are equivariant.

We need (12) only for d=10. The canonical jet sequence is

      0 -> O(8) -> P^1(O(10)) -> O(10) -> 0.        (14)

For a transition function g, the difference of local jet splittings is dg/g. On the standard overlap for O(10), this is plus or minus 10 dz/z according to frame convention. The class of dz/z generates H1(Omega)=C, so (14) is nonzero in characteristic zero. The physical twisted Euler extension

      0 -> O(8) -> W O(9) -> O(10) -> 0             (15)

is also nonzero, because a split would require a map O(10)->W O(9), whose ordinary Hom space is zero. Since Ext1(O(10),O(8)) is one-dimensional, scaling a boundary line identifies (14) with (15).

This comparison also fixes the physical linearization, not merely the ordinary balanced splitting. Both sequences have their canonical G-linearizations. The Ext1 space is the trivial G representation, by Serre duality with H0(O). After the scalar adjustment, average an ordinary extension isomorphism fixing the boundary terms over finite G. Its average still induces the identity on both boundary terms and is therefore an equivariant isomorphism of extensions. Hence

      P^1(O(10))=W O(9),
      P^1(O(10))*=W O(-9)                           (16)

equivariantly for the physical W, not the other doublet W'. The group is perfect, so no one-dimensional character can alter the line linearizations. The proof of (12)-(16) requires no completeness of V*->H0(O(10)), and evaluates no selected actual point or jet.

## 5. Exclusion of the scalar-split endpoint

Suppose L0=O(-8)+O(-10), and let U be its lower direct summand O(-10), viewed as an actual saturated line in C* O. By (7) and the first three vanishings in (9), gamma in (6) kills U. Since i(-2) is injective as a sheaf map, beta_L0 itself kills U.

Therefore the actual second fundamental form of U in C* O factors as

      delta_U:U -> (L0/U)(-2)=O(-10).               (17)

It is nonzero by the horizontal obstruction. A nonzero map O(-10)->O(-10) is an isomorphism everywhere. The first-jet lemma applies with M=L0 and gives

      L0=U^+=P^1(O(10))*=W O(-9).

This contradicts the ordinary splitting O(-8)+O(-10). Thus the scalar-split option in (3) is excluded by the actual embedding, not by its section character alone.

## 6. The balanced endpoint has exact saturated rank-one image

Now L0=W O(-9). The last four Hom calculations in (9) force gamma to factor as

      gamma=j epsilon,
      j:O(-8) -> F*(-4).                           (18)

For F=O(2)+2O(4), j has zero O(-6) component and a constant direction in 2O(-8). For F=W O(3)+O(4), j has the form

      j=(a eta,b id):O(-8)->W O(-7)+O(-8)           (19)

for two scalars a,b. These describe universal Hom spaces, not selected values of actual coefficients.

The actual beta_L0 cannot vanish by the horizontal obstruction, and i(-2) is injective, so j is nonzero. Every nonzero j described above is a saturated inclusion. In the scalar case it is a nonzero constant direction in an equal-degree block. In (19), if b is nonzero the scalar projection gives a retraction; if b=0 then a is nonzero and eta is the Euler subbundle inclusion. These alternatives exhaust the Hom space.

Because epsilon is onto and i(-2) is a sheaf monomorphism, (18) implies that beta_L0 kills ker epsilon and descends to a map

      bar_j:O(-8) -> B0(-2),       i(-2) bar_j=j.    (20)

This is injective. It is also saturated in the ACTUAL B0(-2): the induced map

      B0(-2)/bar_j O(-8) -> F*(-4)/j O(-8)          (21)

is injective, and its target is locally free. The source is torsion-free and therefore locally free on the smooth curve. This verifies saturation even where the coherent injection i has its twelve-point torsion cokernel.

Since epsilon is everywhere onto and bar_j is a subbundle inclusion, beta_L0 has rank one everywhere, exact image bar_j O(-8), and exact kernel

      L0^-=ker epsilon=O(-10).                     (22)

For U=L0^-, its actual derivative again factors through (L0/U)(-2)=O(-10); it cannot vanish and is an isomorphism. Hence U^+=L0 and U^-=0. Untwisting the saturated image (20), the actual positive modification L0^+ is the preimage of bar_j O(-6) in S0. It is saturated in S0 and in C* O, and

      0 -> L0 -> L0^+ -> O(-6) -> 0,
      rank L0^+=3,       degree L0^+=-24.           (23)

No splitting of the rank-three extension (23) is needed here.

## 7. The original endpoint and the complete octic tail

The constant decomposition imported in (4) makes the actual derivative block diagonal. For clarity, the next derivative of its octic tail can be seen without an instance calculation. Fiberwise, the standard exact evaluation sequence

      0 -> Sym6 W O(-2) -> Sym7 W O(-1)
        -> O(6) -> 0

comes from the annihilator of the value and first derivative of the complete O(8) linear series. For a length-three infinitesimal neighborhood, H1(O(5))=0, so that same complete linear series separates second jets everywhere. Its next actual derivative therefore has rank one everywhere. In the fixed physical SL2-equivariant osculating flag it is the nonzero scalar multiple of the next binary evaluation row

      0 -> Sym5 W O(-3) -> Sym6 W O(-2)
        -> O(4) -> 0.                              (24)

Equivalently, the fiber of Sym6 W O(-2) is the space of degree-eight forms divisible by the square of the moving vanishing linear form. Differentiation modulo that space kills exactly the forms divisible by its cube. This gives (24) uniformly, with no chosen actual point, parameter value or coefficient.

The target of the original beta_L is B(-2)=B0(-2) direct-sum O(4). Equations (20)-(22) and (24) show that its exact image is the saturated direct sum bar_j O(-8) direct-sum O(4). Its rank is two everywhere, and its kernel is exactly (5). The rank and degree are

      1+6=7,       -10+6(-3)=-28.

As a consistency check, deg L=-32, so deg(L/L^-)=-4, equal to deg(O(-8)+O(4)). The defect t=12 of the preceding rank-four transpose map is unchanged. This is a new actual endpoint exclusion and exact kernel/image result, not a realization or exclusion of either primal form in (1).

## 8. Verification boundary

The accompanying checks verify only the fixed low-degree representation identities, the seven small Hom dimensions, Euler and jet rank/degree identities, and the relevant negative-horizontal/first-jet logical prerequisites as recorded scalar implications. They do not evaluate any actual HM/source coefficients, points, jets, tensors, matrices or instance ranks. The geometric argument, especially the actual-series jet surjectivity, physical extension comparison and saturation in (21), is reviewed independently as a whole proof. Complete immutable inputs and exact proof hashes are retained. No public write or merge is part of this packet.
