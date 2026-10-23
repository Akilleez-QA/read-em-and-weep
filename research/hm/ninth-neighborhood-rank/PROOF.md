# The actual ninth-neighborhood gate has constant rank twelve

Work over C with the actual normalized HM bundle F, B=End0(F), the positive fixed plane R, and the negative hyperplane pencil π:X→T=P(W*). Let p:X→P4 be the blowup along R and E its exceptional divisor. In a fiber H_λ≅P3, E is the plane R. Write D9=9E for the actual Cartier thickening inside X. Its fibers are the ordinary ninth neighborhoods 9R_λ inside H_λ, not the ambient ideal-power thickening of R in P4.

No actual HM coefficients, points, jets, derivatives, matrices or instance ranks are evaluated. The rank below is forced uniformly by duality and authenticated square exhaustion.

## 1. Exact inputs and result

All inputs are from Akilleez-QA/read-em-and-weep; INPUTS.json records exact commits, paths and Git-blob identities.

- NINTH: PR974, commit5ce277d0476224f9f3fdbc79d1750210a2169708, research/hm/uniform-third-neighborhood/PROOF.md. It identifies the actual positive derived cohomology of B(2)|D9 with the complex

      Θ: T30 → U15,                                  (1)
      U15=H2(R,B_R(-6)) O(8)=H0(R,B_R(3))* O(8),
      T30≅V O(2)⊕P O(2)⊕W O(5)
                  ⊕(A⊕V⊕P⊕D)O(4)⊕(A⊕V)O(6),

  in cohomological degrees one and two. It computes every derived fiber, without a constant-rank assumption. The source has rank30 and degree120, and the target rank15 and degree120. It also retains the plane facts H0(B_R(t))=0 for t≤1 and H1(B_R(t))=0 for t≤-5.
- EXHAUST: PR945, commit089003175d9e31a7cf6288ab7a9e3ac4d66a3e63, research/hm/exceptional-adjoint-exhaustion/PROOF.md. For every H_λ, all global B_H(3) sections are the three even products of its two F_H(2) sections.
- SQUARE: commitdb51525015bb7c5e825833d550d08dedf6f6ea96, research/hm/order-four-quadratic-load/HYPERPLANE-SQUARE-SURVIVORS.md. The actual two-section bundle is

      Y=π_*p*F(2)=W O(-3),
      0→Y→D O→A O(2)→0.

  Its products give the actual fiberwise injective square restriction

      s: Q:=Sym²Y → H O,
      Q≅A O(-6),   H=H0(R,B_R(3))=Sym²D.             (2)

All O(d) in these bundle statements are on T. Named self-dual representation identifications retain their usual scalar choices. Intrinsic statements below are expressed using Q, H and s.

We prove that Θ has rank TWELVE at every parameter, with canonical identifications

    coker Θ ≅ Q* O(8) ≅ A O(14),
    im Θ = ker[s* O(8): H* O(8)→Q* O(8)],          (3)
    rank ker Θ=18,   deg ker Θ=42,
    rank im Θ=12,    deg im Θ=78.

Equivalently, if S12=coker s is the actual square quotient, then

    im Θ ≅ S12* O(8).                               (4)

The exact output is a locally free cokernel with its actual quotient map, not only a generic rank. No Θ coefficient is selected, and the top polar σ, opposite bundle C and vertex δ are not determined by this theorem.

## 2. The finite ninth neighborhood has exactly the global positive squares

Fix any hyperplane H_λ. The ordinary normal degree-k layer of B_H(3) along its plane R is B_R(3-k) tensored with the corresponding one-dimensional normal coefficient. Its inversion sign is (-1)^k. For even k≥8, both H0 and H1 of this layer vanish: 3-k≤-5 and the stated plane vanishings apply. Odd layers have no positive invariant part under inversion. Exactness of taking the finite involution's eigenspaces therefore shows that

    H0(mR_λ,B_H(3))_+

is unchanged by every step after 7R_λ, in particular after 9R_λ.

This stabilized space equals H0(H_λ,B_H(3))_+. To verify this without assuming algebraization, use

    0→B_H(3-m)→B_H(3)→B_H(3)|mR_λ→0.

For sufficiently large m, H0(B_H(3-m))=0 by eventual negative-twist section vanishing. Also H1(B_H(3-m))=0: Serre duality on P3 identifies its dual with H2(B_H(m-7)), which vanishes for sufficiently large m by Serre vanishing. Thus restriction is an isomorphism for sufficiently large m; the preceding stabilization proves it is an isomorphism at m=9. This argument holds for every λ and does not assert these negative-twist vanishings specifically at m=9.

EXHAUST now gives

    h0(9R_λ,B_H(3))_+=3                            (5)

at every parameter. Both X→T and D9→T are proper flat families, and B restricted to them is locally free. For D9, flatness also follows from its finite filtration by vector bundles on R×T. Taking eigenspaces of derived cohomology is exact. More concretely, after the finite normal projection D9→R×T, the positive summand is a vector bundle with its finite filtration by the even layers; ordinary cohomology and base change applies to this summand over T. Constant positive h0 in (5), cohomology and base change, and restriction identify the actual section bundle with the global square bundle:

    (π_* B(3)|D9)_+ = Q=Sym²Y.                      (6)

The canonical map from (6) to H O is exactly s: restriction of a product is the product of the restrictions. This retains the actual square inclusion, not just its isomorphism type.

## 3. Relative duality and its linearization

The universal hyperplane is the projective bundle of lines in

    V O_T ⊕ O_T(-1).

The latter summand is the tautological negative line. Its determinant is O(-1), since det V is trivial. The relative canonical bundle and plane-divisor line bundle are consequently

    ω_X/T = p*O(-4)⊗π*O(1),
    O_X(E) = p*O(1)⊗π*O(-1).                       (7)

The second equality also follows from the projection of the tautological line to the negative summand. Adjunction for the relative Cartier divisor D9 gives

    ω_D9/T = (ω_X/T⊗O_X(9E))|D9
            =p*O(5)⊗π*O(-8)|D9.                   (8)

The family D9→T is a flat projective Gorenstein family of dimension two, even though its fibers are nonreduced. The full sheaf B(2)|D9 is locally free on D9. Apply relative duality to this FULL sheaf before taking central eigenspaces: its positive eigensubsheaf is not itself an O_D9-submodule. The trace pairing B*=B and (8) identify the dual coefficient as

    (B(2)|D9)*⊗ω_D9/T = B(3)|D9⊗π*O(-8).          (9)

There is no parity swap in this finite-surface duality. Along R, the normal direction contributes an odd factor to ω_X/T, while 9E contributes an odd factor as well. They cancel. Equivalently, O_T(-8) has even central character, as does O_R(5). Thus duality pairs the positive cohomology of B(2) with positive cohomology of B(3).

Fiberwise Serre duality, (5), and (9) give

    h2(9R_λ,B_H(2))_+ = 3

for every λ. The actual fiber complex (1) therefore has a three-dimensional cokernel at every parameter. Since its target has rank15, Θ has rank12 everywhere, and its kernel has rank18 everywhere. Its kernel, image and cokernel are vector bundles, and the relevant cohomology commutes with base change. Relative duality now gives the actual bundle identification

    (coker Θ)* ≅ Q O(-8),

which is the first statement of (3). In particular this argument excludes torsion in the cokernel; it is not a generic-rank inference.

The degree of Q is -18, hence deg(Q*O(8))=18+3·8=42. The two exact sequences associated with (1) then yield deg im Θ=120-42=78 and deg ker Θ=120-78=42.

## 4. The final quotient is dual to the actual square inclusion

The quotient map from U15 in (1) is the cohomology map from the top even normal layer

    B_R(-6)⊠O(8) → B(2)|D9.

Naturality of relative duality identifies its transpose with restriction of the dual section B(3)|D9 to the reduced plane R. This can also be checked by the local Gorenstein residue pairing: in O_R[z]/(z^9), the top layer z^8 pairs precisely with the constant term of a dual section. This is a universal local identity for a Cartier thickening, not a value of any actual coefficient or jet.

Under (6), restriction of dual sections is exactly the actual map s in (2). It follows that the quotient map is

    H* O(8) --s* O(8)--> Q* O(8),                    (10)

with the trace/duality normalizations retained. Thus im Θ is its kernel. Since s is a fiberwise injection, the actual square quotient S12 is locally free, and dualizing its short exact sequence proves (4).

This determines the image as an actual subbundle of the target, not only its rank, degree, or abstract isomorphism class.

## 5. Canonical kernel interpretation and remaining boundary

The same full-sheaf relative duality in cohomological degree one gives

    ker Θ ≅ ((R1π_* B(3)|D9)_+)* O(8).              (11)

The middle cohomology here is locally free of rank18 by the fiber duality and constant rank just proved. Equation(11) concerns the finite ninth neighborhood. It is not an identification with the global opposite bundle C, and no unproved global-to-finite H1 comparison is substituted for it.

The new structural result is that the actual previously undetermined thirty-to-fifteen gate has constant rank twelve, its cokernel is the dual actual square bundle with the precise twist, and its image is the annihilator of the actual square restriction. No selected actual map is evaluated. The source/frontier ledger, top σ, vertex δ and actual splitting of C remain unchanged.
