# A single inherited core block detects the top opposite obstruction

Work over C with G=2I and the standard parameter-line linearizations. No selected actual HM/source coefficient, point, parameter, matrix, rank, jet or derivative is evaluated.

## 1. Immutable interfaces and result

INPUTS.json authenticates these exact originals:

- CORE: PR1017, commit 7cd8baebbec29ad21def1f8b30e19c707a87aed5, research/hm/rank-three-opposite-core/PROOF.md. It supplies the actual fiberwise-injective presentations

      0→W' O(-3)⊕O(-8)→S O(1)⊕Lpos→Fout→0,       (1)

  with Lpos=A O(2), Fout=Q when λ≠0, and Lpos=W O(3), Fout=Q3 when λ=0. The inherited branch identifications below specify Q and Q3. All inherited complement choices are retained. The W' O(-3)-to-S O(1) Hom space is one-dimensional.
- BRANCHES: PR1009, commit 0d75f42c4e79654c8fbef57e6ce56a1f06cdf9a1, research/hm/common-target-branches/PROOF.md. It supplies the intrinsic zero-branch splitting Q=O⊕Q3.
- QUOTIENT: PR996, commit 54dc2b2b301f8a7e453b3101d5813c643beed71a, research/hm/opposite-second-degree-bound/PROOF.md. Section6 supplies the actual sequence 0→Q→C→O(2)→0.
- AMPLE: PR994, commit 48727e1f5fd5ab079c21b8b39af608f7d91fabab, research/hm/opposite-ample-exclusion/PROOF.md. Section6 authenticates ker σ=H0(C(-12))^G for the actual map between canonical two-dimensional spaces, and identifies its rank-one case exactly with C=O(2)⊕O(12)⊕V O(4), row9. Its vertex extension scalar is then the sole remaining possible invariant extension ambiguity.

Let a denote the actual W' O(-3)-to-S O(1) block of (1), or its scalar after choosing a nonzero generator of its one-dimensional Hom space. We prove

    a=0 ⇔ H0(C(-12))^G≠0 ⇔ rank σ=1
        ⇔ C=O(2)⊕O(12)⊕V O(4).                  (2)

The block a is forced nonzero in the λ=0 branch. Although its scalar normalization and the core presentation involve choices, its zero/nonzero status is independent of every permitted choice by (2). This determines neither its actual value nor the remaining vertex scalar.

## 2. The universal rank-two block has a balanced quotient

Let u:W' O(-3)→S O(1) be any nonzero member of the unique channel. Shift by O(-1), obtaining W' O(-4)→S O. If its generic rank were one, its saturated image would be a G-linearized line O(-e) inside a constant bundle, with e≥0. Since G has no nontrivial characters, the nonzero factor W' O(-4)→O(-e) would require W' in Sym^(4−e)W. This is impossible: for degrees0..4 those symmetric powers are 1,W,A,S,D, and negative twists have no sections. Thus u has generic rank two.

Its maximal minors are sections of O(8). Their common-zero divisor is G-invariant and has degree at most eight. Every nonempty projective icosahedral orbit has size at least twelve, as established in CORE. Consequently that divisor is empty: u injects on every fiber. Let B be its quotient, a bundle of rank2 and degree10.

Since B(-1) is a quotient of the constant S O, its two ordinary splitting degrees are nonnegative; hence B has degrees at least one. Its central action is even, because the source and target of u both have even total parity. If B were unbalanced, equivariant Birkhoff splitting and the absence of nontrivial one-dimensional G representations would force both degrees to be even. They sum to10 and are positive, leaving only (2,8) and (4,6).

The first would give a nonzero equivariant quotient S O(1)→O(2), impossible since Hom_G(S,W)=0. The second would give a nonzero quotient S O(1)→O(6), impossible since Hom_G(S,Sym5 W)=Hom_G(S,T6)=0. Therefore B=R O(5) for an odd two-dimensional representation R, namely W or W'.

Twist the quotient sequence by O(-4). Its cohomology, together with H1(R O(1))=0, gives

    R⊗W=(W'⊗T6)−(S⊗W)=P.

Indeed T6=W'⊗A, W'⊗W'=1⊕V, V⊗A=P⊕D and S⊗W=A⊕D. Thus R=W', because W⊗W=1⊕A whereas W'⊗W=P. We have proved the universal exact sequence

    0→W' O(-3) --u→ S O(1)→W' O(5)→0.          (3)

No actual map coefficient or parameter was chosen in this argument.

## 3. The universal invariant cohomology pairing is nonzero

Twist (3) by O(-12). The quotient becomes W' O(-7). Both of its invariant cohomology groups vanish:

    H0(W' O(-7))=0,
    H1(W' O(-7))^G=Hom_G(W',Sym5 W)=0.

Finite-group invariants are exact in characteristic zero. Hence (3) induces an isomorphism

    H1(W' O(-15))^G --u_*→ H1(S O(-11))^G.       (4)

Both spaces are one-dimensional: equivariant Serre duality identifies their dimensions with the multiplicities of W' in Sym13 W and S in Sym9 W, respectively. These bounded fixed-character identities are included in verify.py. In particular, no hidden vanishing of a recoupling constant is being assumed: exactness proves that the universal pairing (4) is nonzero.

## 4. Extract the actual core block from cohomology

Twisting (1) by O(-12) makes every source and target summand have strictly negative degree. The long exact sequence therefore identifies H0(Fout(-12))^G with the kernel of the invariant H1 source-to-target map.

All invariant H1 summands except those in (4) vanish. The exact fixed-character tests are

    H1(O(-20))^G=(Sym18 W)^G=0,
    H1(A O(-10))^G=Hom_G(A,Sym8 W)=0,
    H1(W O(-9))^G=Hom_G(W,Sym7 W)=0.              (5)

Consequently the invariant H1 map in either branch is exactly a times the universal isomorphism (4). It follows that

    dim H0(Fout(-12))^G = 1 if a=0, and 0 otherwise. (6)

The actual sequence 0→Q→C→O(2)→0 identifies H0(Q(-12)) with H0(C(-12)), because H0(O(-10))=0. In the zero branch Q=O⊕Q3 and H0(O(-12))=0, so the same identification holds with Fout=Q3. Thus (6) holds with C in place of Fout. AMPLE now proves (2).

There is also a direct forced-nonvanishing argument in the zero branch. If a=0 there, the W' O(-3) source subbundle of (1) would map solely into W O(3). Fiberwise injectivity of (1) would make this an everywhere-injective map between two rank-two bundles, hence an isomorphism. Their degrees are−6 and6, a contradiction. Therefore a≠0 for every inherited zero-branch presentation.

## 5. Contribution and limits

This gives a concrete root cause for the unique remaining rank-one top-obstruction possibility: it is precisely disappearance of the inherited W'-to-S block in the rank-three core. The universal nonzero cohomology pairing has been proved geometrically, not inferred only from equal dimensions. The zero branch forces that block to survive. These statements preserve actual maps and are stable under all permitted presentation choices.

No further C row is excluded, and the actual block is not evaluated. If it vanishes, λ is necessarily nonzero and the actual C is row9; the vertex extension scalar remains unresolved. If it does not vanish, σ has rank two and AMPLE implies that the vertex extension splits equivariantly. This is a one-channel actual obstruction criterion, not a new abstract classification or an assertion about an arbitrary four-scalar model.
