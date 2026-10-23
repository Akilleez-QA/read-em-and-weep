# Forced constant channels and the actual rank-three opposite core

Work over C on T=P(W*) with the standard G=2I linearizations and current irreducible labels. No selected actual HM/source coefficient, point, parameter, jet, derivative, matrix or instance rank is evaluated.

## 1. Immutable interface and statement

The exact immutable originals are recorded in INPUTS.json.

- NORMAL is PR1016 at b28df36d77a6cb514bd5ae50cb480f572d3eb2f7, research/hm/two-six-source-normal-form/PROOF.md. It supplies actual fiberwise-injective presentations with source (2T6) O(-1), quotient Fout=Q when λ≠0 and Fout=Q3 when λ=0, and targets

      (V⊕P) O⊕W' O(1)⊕S O(1)⊕A O(2),
      (V⊕P) O⊕W' O(1)⊕S O(1)⊕W O(3),

  respectively. Fix its inherited complement choices; all subsequent maps come from this actual presentation.
- BRANCHES is PR1009 at 0d75f42c4e79654c8fbef57e6ce56a1f06cdf9a1, research/hm/common-target-branches/PROOF.md. Its interface lists the four Q types O(12)⊕V O(4), O(18)⊕A O(2), W' O(5)⊕W' O(7), P O(6), and the three Q3 types O(14)⊕W' O(5), O(18)⊕W O(3), V O(8). Every degree of Fout is at least two.

We prove that the actual V, P and W' O(1) projections are successively forced onto. The resulting actual presentations are

    λ≠0: 0→W' O(-3)⊕O(-8)→S O(1)⊕A O(2)→Q→0,   (1)
    λ=0: 0→W' O(-3)⊕O(-8)→S O(1)⊕W O(3)→Q3→0.  (2)

Both source maps inject on every fiber. Each of the four block Hom spaces in either presentation is one-dimensional. The four actual coefficients are retained and not evaluated; this is a rank-three core with explicitly bounded universal channels, not a chosen four-scalar model.

## 2. Two complementary sextic evaluation systems

The fixed representation identity is Sym6 W=V⊕P. Both nonzero invariant systems V,P⊂H0(O(6)) are basepoint-free. Indeed their common-zero divisor, if nonempty, would be G-invariant of degree at most six. Every nonempty orbit of the projective icosahedral action has size at least twelve: stabilizers in a finite subgroup of PGL2(C) are cyclic, and A5 has no element of order greater than five. Thus no such divisor exists.

### The P evaluation kernel

Let KP be the kernel of P O→O(6). It has rank3 and degree−6, and is a subbundle of a constant bundle. Hence all its splitting degrees are at most zero; H0(KP)=0 because P embeds in H0(O(6)), so all degrees are at most−1.

H0(KP(1)) has dimension at most three and is a subrepresentation of P⊗W=W'⊕T6. Its only possible nonzero value is W'. Such a value would give an equivariant subbundle W' O(-1)⊂KP⊂P O. Since P=W'⊗W and its relevant Hom space is one-dimensional, this is the tensor Euler inclusion, with quotient W' O(1). Evaluation P O→O(6) would then factor through W' O(1). But

    Hom_G(W' O(1),O(6))=Hom_G(W',Sym5 W)=0.

This contradicts the nonzero evaluation. Therefore H0(KP(1))=0. Its three degrees are at most−2 and sum to−6, so KP is ordinarily O(-2)^3. Its multiplicity representation follows from

    H0(KP(2))=P⊗A−Sym8 W=V,

using P⊗A=V⊕P⊕D and Sym8 W=P⊕D. We have proved the actual universal sequence

    0→V O(-2)→P O→O(6)→0.                       (3)

### The V evaluation kernel

Let KV be the kernel of V O→O(6). It has rank2 and degree−6, with all splitting degrees at most−1. Since H0(KV(1)) embeds in V⊗W=T6 and has dimension at most two, it vanishes. Thus all degrees are at most−2. Next H0(KV(2)) embeds in V⊗A=P⊕D and again has dimension at most two, so it vanishes. Consequently KV is ordinarily O(-3)^2.

Its multiplicity representation is an odd two-dimensional representation, hence W or W'. The first is excluded because

    Hom_G(W,V⊗S)=Hom_G(V,W⊗S)=Hom_G(V,A⊕D)=0.

Thus KV=W' O(-3). Dualizing its evaluation sequence and twisting by O(-2) gives

    0→O(-8)→V O(-2)→W' O(1)→0.                  (4)

All these proofs concern fixed universal linear systems and representations, not an actual HM coefficient or selected parameter.

## 3. Force and remove the constant V projection

Project the actual target in Section 1 to V O. This source map cannot vanish, or Fout would surject onto V O. Such a quotient is impossible because every degree of Fout is positive.

Since V⊗W=T6, each nonzero T6 O(-1)→V O is the tensor Euler surjection, with kernel V O(-2). The actual map from the two T6 copies is a nonzero functional on their multiplicity space times this universal surjection. It is therefore onto on every fiber. Its kernel K9 has an exact sequence

    0→T_unused O(-1)→K9→V O(-2)→0,              (5)

where T_unused is the canonical kernel of that multiplicity functional, isomorphic to T6. This sequence admits an equivariant splitting because H1(O(1))=0, but that splitting need not be canonical and is not used to select new coefficients.

Taking the actual kernel of the target projection gives

    0→K9→P O⊕W' O(1)⊕S O(1)⊕Lpos→Fout→0,       (6)

where Lpos=A O(2) or W O(3).

## 4. A genuine obstruction forces the T_unused-to-P component

Suppose the restriction T_unused O(-1)→P O vanished. Then the P projection of K9 would factor through its quotient V O(-2) in (5). This factor is nonzero, since otherwise Fout would surject onto the constant P O, again impossible by positivity.

The Hom space Hom_G(V O(-2),P O) is one-dimensional. Its nonzero member is exactly the inclusion in (3), because V occurs once in P⊗A. Therefore (6) would induce an equivariant surjection Fout→O(6).

But Hom_G(Fout,O(6)) vanishes for every possible actual type. In the four Q cases the only potentially relevant atoms give V against Sym2 W=A, A against Sym4 W=D, W' against Sym1 W=W, or P against Sym0 W=1, respectively, all disjoint. In the three Q3 cases the corresponding tests are W' against W, W against Sym3 W=S, and no nonnegative twist at all. Higher-degree atoms contribute nothing.

This contradiction proves that the actual T_unused-to-P component is nonzero. Since T6=W'⊗A and P=W'⊗W, its unique channel is tensor contraction in

    0→W' O(-3)→T6 O(-1)→P O→0.                  (7)

It is onto on every fiber. Let K5 be the kernel of the full P projection of K9. The actual kernel diagram yields

    0→W' O(-3)→K5→V O(-2)→0.                    (8)

Both its ordinary Ext1 and ordinary Hom from V O(-2) to W' O(-3) vanish, because H1(O(-1))=H0(O(-1))=0. Thus (8) has a unique equivariant splitting. Removing the P target now gives an actual presentation with source K5=W' O(-3)⊕V O(-2) and target W' O(1)⊕S O(1)⊕Lpos.

## 5. Force and remove W' O(1)

The W' O(-3) source cannot map to the W' O(1) target, since

    Hom_G(W',W'⊗Sym4 W)=Hom_G(1⊕V,D)=0.

Thus that target projection factors through V O(-2). It is nonzero: otherwise Fout would surject onto W' O(1), impossible because every degree of Fout is at least two.

The Hom space Hom_G(V O(-2),W' O(1)) has dimension one, and (4) supplies a nonzero member. Hence this actual projection is onto with kernel O(-8). Pulling back that kernel in the uniquely split sequence (8) gives W' O(-3)⊕O(-8). Taking the actual target kernel proves (1) and (2). Their quotient Fout is locally free, so they inject on every fiber, including all exceptional parameters.

## 6. The four universal channels and the unresolved actual data

The four block Hom dimensions in the nonzero branch are

    dim Hom_G(W',S⊗Sym4 W)=1,
    dim Hom_G(W',A⊗Sym5 W)=1,
    dim (S⊗Sym9 W)^G=1,
    dim (A⊗Sym10 W)^G=1.

For the zero branch replace the second and fourth lines by

    dim Hom_G(W',W⊗Sym6 W)=1,
    dim (W⊗Sym11 W)^G=1.

Thus, after identifying the named summands and choosing nonzero universal generators, the actual core map has four scalar coefficients. Those identifications do not set their values, assert their independence, remove allowable automorphisms, or identify the maps with an arbitrary abstract model. The construction retains the actual kernel and quotient maps through every step.

The core source has rank3 and degree−14. Its targets have rank7 or6 and degree10. The cokernels therefore have rank4 or3 and degree24 as required.

The substantive new obstruction is the forbidden quotient Fout→O(6), which forces the constant P channel after the V reduction. The complementary sextic kernel sequence then forces the W' O(1) projection and yields the actual rank-three core. None of λ, the remaining C type, top obstruction rank or vertex scalar is evaluated, and no source/frontier case is removed.
