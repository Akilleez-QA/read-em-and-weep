# Full adjoint-section exhaustion on the fourth ambient plane neighborhood

Work over C with the actual normalized HM bundle F on P4, B=End0 F, and the positive fixed plane R. Put I=I_R and write mR for the ordinary ambient thickening O_P4/I^m. These are codimension-two plane neighborhoods in P4, NOT the hyperplane neighborhoods mR_lambda inside H_lambda.

Let G=SL2(F5), W the negative two-space, A=Sym2 W, S=Sym3 W, V the other even three-space, P the even four-space, D=Sym4 W and T6=Sym5 W. The central inversion has positive action on B_R and O_R(1), and negative action on normal linear forms W. Superscripts + and - below mean its full eigenspaces, not G-invariant subspaces.

No selected actual HM/source coefficient, point, jet, matrix, derivative, or instance rank is evaluated.

## 1. Inputs and exact result

The two immediate inputs in Akilleez-QA/read-em-and-weep are pinned with exact byte identities in INPUTS.json:

- BALANCED: PR976 at commit f23f8b9972d459c7c3ab532937964ef7f543b157, research/hm/balanced-first-cup-kernel/PROOF.md, exact proof SHA256 8498a0652b1345c89ebf2643a9d96853e0e2c60760e674425f97c68723aebb41. Its actual complete quadratic coefficient map is injective, with cokernel isomorphic to A:

      nu3: H0(B_R(3))=Sym2 D
          -> Sym2 W tensor H1(B_R(1)),
      ker(nu3)=0,       coker(nu3)=A.                     (1)

  This is the actual cup with the quadratic normal class zeta, not merely a map with these characters.
- UNIFORM: PR974 at commit 5ce277d0476224f9f3fdbc79d1750210a2169708, research/hm/uniform-third-neighborhood/PROOF.md. The actual degree-two coefficient family for sections of B_R(2) is the injection

      c: A O_T -> (V+P+D) O_T(2),
      coker(c) = (V+P) O_T(2) directsum W O_T(5),          (2)

  where T=P(W*). Its D block is a nonzero multiple of the twisted dual of the established y sequence; the other two blocks vanish. It retains the actual cup/transition identification. The following cohomology data follow from UNIFORM, with one standard propagation step made explicit: self-duality of B_R gives H2(B_R(1))=H0(B_R(-4))*=0, while H1(B_R(2))=0. Thus B_R is 3-regular on P2; persistence of Castelnuovo–Mumford regularity gives H1(B_R(3))=0. Likewise self-duality and the stated H0 vanishing give the listed H2 vanishings. Consequently

      H0(B_R(t))=0 for t<=1,
      H0(B_R(2))=A,    H1(B_R(2))=0,
      H0(B_R(3))=Sym2 D,    H1(B_R(3))=0,
      H1(B_R(1))=A+V,    H1(B_R)=V+P+D,
      H2(B_R(t))=0 for t=0,1,2,3.                        (3)

We prove the sharp finite vanishing

      H0(3R,B(3)) = W tensor A = W+S, purely odd,
      H0(mR,B(3)) = 0 for every m>=4.                     (4)

These are full section spaces. The complete remaining cohomology at the two decisive stages is

      H1(3R,B(3))^+ = A,     H1(3R,B(3))^- = 0,
      H2(3R,B(3)) = 0;

      H1(4R,B(3))^+ = A,
      H1(4R,B(3))^- = (V+P) tensor S + W tensor Sym6 W
                    = 2W' + 2S + 5T6,
      H2(4R,B(3)) = 0.                                  (5)

Thus the odd group on 4R has dimension 42, and total H1 has dimension 45. Named irreducible identifications in (5) need not be scalar-normalized.

## 2. Actual parity-filtered sheaves on the plane

The complement of the negative fixed line has its canonical normal projection rho onto R. Every mR lies in this complement, and rho restricted to mR is finite. Write E_m(t)=rho_*(B(t)|mR). Cohomology of E_m(t) on R is exactly cohomology of B(t) on mR; this uses finite pushforward, not a split model for F.

The actual ideal-power filtration has layers

      I^k B(t)/I^(k+1)B(t)
        = Sym^k W tensor B_R(t-k),                       (6)

of inversion sign (-1)^k. Taking either inversion eigensheaf is exact. Hence at m=3, t=3, the actual positive part has a short exact sequence

      0 -> Sym2 W tensor B_R(1)
        -> E_3(3)^+ -> B_R(3) -> 0,                     (7)

while the negative part has only one layer and is canonically

      E_3(3)^- = W tensor B_R(2).                       (8)

The boundary of (7) on H0 is precisely nu3. This is the actual quadratic normal transition/cup construction retained in the two inputs; equivalently it is the polynomial coefficient map whose evaluation in every negative direction is the authenticated first cup. Pure squares span Sym2 W, so these evaluations determine the full mixed-coefficient map. No associated-graded replacement of (7) is made.

Using (1) and (3), the cohomology sequence of (7) gives H0(E_3(3)^+)=0, H1(E_3(3)^+)=coker(nu3)=A and H2(E_3(3)^+)=0. Equation (8) and (3) give H0(E_3(3)^-)=W tensor A and no higher cohomology. This proves the statements at 3R.

## 3. The actual odd boundary at the fourth neighborhood

The new degree-three layer is negative, so E_4(3)^+=E_3(3)^+. The negative part fits into

      0 -> Sym3 W tensor B_R
        -> E_4(3)^- -> W tensor B_R(2) -> 0.             (9)

Its boundary is the actual map

      delta: W tensor A -> Sym3 W tensor H1(B_R).       (10)

We identify this map intrinsically, including all mixed normal coefficients. The positive part of the actual ambient E_3(2) has sequence

      0 -> Sym2 W tensor B_R
        -> E_3(2)^+ -> B_R(2) -> 0.                     (11)

Its coefficient boundary is the map encoded by c in (2). This follows from the same actual quadratic normal class and cup as UNIFORM; evaluation on the direction conic and polynomial polarization determine the complete coefficient tensor.

Multiplication by the global normal linear forms gives a morphism of the actual extensions from W tensor (11) to (9). It is well-defined because I times I^3 is contained in I^4, and B(2) times O(1) is B(3). On the quotients it is the identity of W tensor B_R(2). On the left-hand layers it is ordinary symmetric multiplication

      W tensor Sym2 W tensor B_R
        -> Sym3 W tensor B_R.

Naturality of connecting homomorphisms therefore identifies delta with multiplication of the quadratic coefficient map by W. Equivalently,

      delta = H0(c(1)):
        H0(A O_T(1)) -> H0((V+P+D) O_T(3)).             (12)

This argument uses actual sheaf multiplication, not a choice of a split formal bundle or a claim that higher transitions may be discarded. It also proves agreement of all mixed normal terms, rather than checking one or finitely many directions.

Since c is an actual vector-bundle injection, left exactness of H0 makes (12) injective. The H0 of the left term of (9) is zero by (3), so (9) gives H0(E_4(3)^-)=ker(delta)=0. The positive section space was already zero. This proves H0(4R,B(3))=0.

## 4. Exact fourth-neighborhood cohomology and persistence

The H1 and H2 of W tensor B_R(2) vanish, and H2(Sym3 W tensor B_R)=0. Thus (9) gives

      H1(E_4(3)^-)=coker(delta),   H2(E_4(3)^-)=0.       (13)

Twist (2) by O_T(1). Since H1(A O_T(1))=0, its sections identify the cokernel of (12) with H0(coker(c)(1)). The authenticated quotient in (2) then gives

      coker(delta) = (V+P) tensor Sym3 W
                       + W tensor Sym6 W.               (14)

The fixed identities V tensor S=W'+S+T6, P tensor S=S+2T6 and W tensor Sym6 W=W'+2T6 yield the odd character in (5). The positive eigensheaf has not changed, so its H1 is A and H2 is zero. These are actual cohomology identifications with the cokernel of the actual map, not dimensions assigned from an Euler characteristic alone.

For each later step (m+1)R -> mR, the new section kernel is H0(Sym^m W tensor B_R(3-m)). This is zero for every m>=2 by (3). Hence every restriction on H0 from that point onward is injective. Starting with the zero space on 4R proves (4) for all m>=4. This argument does not require later H1 obstructions to vanish or later extensions to split.

## 5. Contribution and distinction from hyperplane squares

The preceding results controlled the first cup and the individual hyperplane neighborhoods. The new conclusion is that no full adjoint section of B(3) survives the fourth ordinary ambient plane neighborhood: the even leading sections die by 3R, and the six odd linear-normal sections die at 4R. In particular four is the first ambient order with no sections, since the 3R space is nonzero.

This does not contradict the three actual product sections on every H_lambda. Extending on one normal line and extending simultaneously in both normal directions are different problems; (7) and (9) retain the mixed normal compatibility. The schemes mR here are defined by I_R^m in P4, not by a hyperplane ideal in H_lambda.

No secondary boundary rank, top polar sigma, opposite-pencil bundle row, vertex scalar, global odd-quadric section, source/frontier cut or algebraicity conclusion is inferred. The proof uses only ordinary ideal powers, actual sheaf maps, exact cohomology and fixed representation arithmetic.
