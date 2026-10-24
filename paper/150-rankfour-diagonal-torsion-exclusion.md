# 150. The rank-four diagonal plateau is excluded with ramification retained

**Craig Ward · 24 October 2026 UTC · A fifth coarse rank-four stratum removed**

## Exact new reduction

The [diagonal theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/e9fc227794240494ac941b8a8541d2f9caedc9a4/research/hm/rankfour-diagonal-plateau/PROOF.md) excludes actual generic SF rank four with ordered maximal plateau (k,l)=(2,2), under its retained geometric and physical-marking hypotheses. It does not assume source Z or use the four-source classification.

The necessary bad coarse frontier decreases from **23 to 22**. Four rank-four bins remain: (1,1), (1,2), (2,1), (3,1). Eighteen higher-rank bins remain, grouped as 6,4,2,2,1,1,1,1 at ranks five through twelve. The optional source-labeled refinement decreases from 92 to 88, not four additional coarse exclusions. These are necessary containers, not realizations, equal-work units or proof-completion percentages.

[Chapter149](149-backward-dual-cubic-image-bound.md) remains a partial image reduction within (3,1), not its closure. Generic SF≥4 and square rank≥28 are unchanged. No SF≥5, positive-square surjectivity, full-adjoint invertibility or original repair is proved.

## Nine degree cases, including positive defects

The hypothetical actual chain has ranks 9,13,17,21,25 with E=F₂. The reversed annihilator chain has ranks 5,9,13,17,21 with Q*=D₂. Persistence bounds all ordinary endpoint slopes by −4, hence a=deg F₀≤−36 and b=deg D₀=deg F₄≤−20.

The regular adjacent rank-four derivative maps have determinant defects δ_i. Exact degree elimination gives

    a+b=−76+δ₁+2δ₂+δ₃.

With a=−36−2u and b=−20−2v, parity and the invariant-divisor gap give

    2u+2v+δ₁+2δ₂+δ₃=20,
    c₁=−13+u−δ₁/2∈2ℤ.

The middle defect δ₂ is zero. A length-twenty outer defect violates quotient determinant parity. Nine cases remain: five unramified endpoint pairs (−38,−38), (−42,−34), (−46,−30), (−50,−26), (−54,−22), and each of (−38,−26), (−42,−22) with either δ₁=12 or δ₃=12. The proof does not suppress these positive-defect cases.

## The torsion terms are part of the exact identity

Set B=L₂, so L₃=B(2). The actual torsion cokernels satisfy

    0→L₁→B(−2)→T₁→0,
    0→B(2)→L₄(−2)→T₃→0.

Their lengths are δ₁ and δ₃. The two sides of the actual filtration give

    [E]−[F₀]=[B(−2)]+[B]−[T₁],
    [Q]−[D₀*]=[B(2)]+[B(4)]+[T₃(2)].

Consequently

    [F₀]−[D₀*(−4)]=[E]−[Q(−4)]+[T₁]+[T₃(−2)].

A length-twelve defect is a line sheaf on the reduced exceptional orbit of twelve points. The point stabilizer has order ten; all five center-even characters O_Δ(r), r=0,2,4,6,8 modulo ten, are retained. Their Euler characters are χ(O(r+t))−χ(O(r+t−12)). For an upper defect, r describes T₃(−2), so the twist is not lost. Torsion is not replaced by twelve trivial characters.

## Genuine cohomology gives a finite domain

The actual quotient sequences and persistence force

    P_pr=χ_G(B(2))−χ_G(E(2))=H¹(F₁(2)),
    P_du=−χ_G(B(−2))−χ_G(Q*(2))=H¹(D₁(2)).

They imply four representation-valued inequalities:

    H¹(B(1))≤W′+3T₆,
    H¹(B)≤P_pr,
    H⁰(B)≤P_du,
    H⁰(B(−1))≤W+2S₄+3T₆.

These follow from the actual quotient maps, successive H¹ surjections, Serre duality and vanishing of H¹ of torsion. No quotient H¹ term is assumed zero without proof.

An endpoint of rank r and total degree d has every ordinary degree in [d+4(r−1),−4]. For B, the first inequality bounds negative blocks and forces all ordinary degrees to be at least −10; rank four and total degree d_B then give the complete window [−10,d_B+30]. Both independent enumeration methods use these proved finite domains, not historical source records or an empirical cutoff.

Exact endpoint/torsion identities and the four inequalities leave 359 formal tuples. They are necessary data only. A torsion-safe subbundle test rejects 187 and leaves 172.

## The subbundle test does not assume a horizontal splitting

For a negative-degree direct summand S of an endpoint A, if both its Hom space to the outer derivative target and Hom_G(S,(A/S)(−2)) vanish, its actual derivative vanishes in the constant ambient. Its Grassmannian classifying map would be constant, contradicting its negative degree.

The actual outer targets inject into B(−4) on the F₀ side and B*(−6) on the D₀ side. Using those larger targets remains valid with positive torsion. The argument proves derivative invariance from two Hom vanishings; it does not declare the Birkhoff splitting horizontal.

Every remaining tuple has

    D₀=W′ O(−5)+V O(−4),
    B=O(−8)+C,

where C is one of

    O(2)+O(4)+O(6),  O(2)+W O(5),
    W O(3)+O(6),     A O(4).

There are 132 unramified tuples with (a,b)=(−54,−22), and **40 tuples with δ₁=12** and (a,b)=(−42,−22). In all 172, δ₃=0. Positive lower ramification therefore survives to the final geometric contradiction.

## The final contradiction covers all 172 tuples

Because δ₃=0, the reversed endpoint derivative lands in

    D₀→B*(−6)=O(2)+C*(−6).

Every slope of C*(−6) is at most −8, whereas D₀ has slopes −5 and −4. Its derivative has zero component into C*(−6), so its rank is at most one. Rank zero would make D₀ constant despite degree −22. Its actual rank is therefore one, forced by universal Hom vanishing rather than an instance computation.

Let U be its smallest constant span and n=dim U. The successive rank-one transforms reach U after n−5 steps. They lie in the reversed plateau stages for the first four steps; reaching a constant bundle earlier would contradict the interior no-constant-subbundle property. Thus n≥9. The complete rank-one flag degree bound gives 22≥5(n−5), hence n=9.

In that actual invariant nine-dimensional span, the complete flag has unit rank increments. With endpoint rank five, the exact weighted determinant-defect identity requires

    9(22−5·4)=18
      =4∑_(j<5) jε_j+5∑_(j≥5)(9−j)ε_j.

Each ε_j is zero or at least twelve. The right side is either zero or at least 48, never eighteen. This excludes all 172 residual tuples, including all forty with positive lower defect, and completes the ordered (2,2) exclusion.

## Evidence and boundary

The frozen proof SHA256 is `0fcfaf0258427ae436572b386587ea1652718ed2ce7d0ffb23482af0f83eae25`. The final independent review SHA256 is `15a17253c78c6664aaddea5b798285c52725a5d1b9b05e731481f7a65f26d05b`. The author certificate has 26,178 checks and 28 executed mutations; the independent certificate has 11,331 checks and 22 executed mutations. Normal and optimized outputs agree. The complete sets of 359 intermediate and 172 residual tuples agree, not just their counts. Five complete immutable originals, including the full rank-one flag theorem, are authenticated.

The calculations certify universal necessary character and degree consequences, not the original geometric premises or a proof-assistant formalization. Actual coefficients, chosen parameters, jets, matrices and instance ranks are not evaluated. Earlier chapters and the delivered PDF retain their historical cutoffs.
