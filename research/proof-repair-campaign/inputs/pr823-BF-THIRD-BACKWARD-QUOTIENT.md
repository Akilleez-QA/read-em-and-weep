# The third backward derivative is forced to be saturated rank two

## Conditional scope

This note is a continuation only for G3.11.73682b4c817f and its nonzero-J source E=(P+D) O(-2)+T O(-3)+O(-8)+O(-10). It uses the independently reviewed quartic subsystem in BF-SUBSYSTEM.md (SHA256 087d0b78196b7c0d5e773375e603359450e0e9fb0ebb3003734c44eea4e133b9), published in PR819 at immutable commit 03fee9278072f9ac00a5fcee5deb04b7fce61ae5:

https://github.com/Akilleez-QA/read-em-and-weep/blob/03fee9278072f9ac00a5fcee5deb04b7fce61ae5/research/hm/profile11-balanced-low-positive-subsystems/BF-SUBSYSTEM.md

Original-data and earlier lemma pins are recorded in that public proof and its dependency manifest. No unpublished continuation is a dependency.

Set K_i=E^{(-i)}. The reviewed input gives E/K_1=O(-10)+W O(5), K_1/K_2=W O(3), and the actual quartic flag

    F=(P+D) O(-2), F^-=T O(-3), F^{--}=V O(-4),
    0 -> O(-10) -> V O -> W O(5) -> 0.

The derivative of F^- onto V O(-2), followed by the quotient to W O(3), has kernel an extension of O(-12) by F^{--}. Thus F^{--} lies in K_2. Its derivative in the quartic flag is onto (F^-/F^{--})(-2)=V O(-4). Its further quotient to (K_1/K_2)(-2)=W O(1) is the twist by -4 of the displayed surjection. Hence the derivative of K_2 contains the whole W O(1). Outward Gauss ranks are nonincreasing and at most two, so this is its entire saturated derivative image. Therefore

    K_2/K_3=W O(1).

This proves that extra input here rather than importing it. Rank and degree subtraction now gives rank K_3=10, degree K_3=-62. Its derivative lands in W O(-1) and has generic rank at most two. Strict-top iteration gives maxdeg K_3<=-5.

The result proved here is

    K_3/K_4=W O(-1)

with saturated derivative image and no divisor correction. This is a forced quotient, not a source or label exclusion.

## 1. Complete small support calculation for K_3

The preceding exact sequences and the known E Euler characters give

    H1(K_3(4))=A+P+D,
    chi_G(K_3(5))=-W.                              (1)

For example, H0(K_3(4))=0 by maxdeg<=-5, so the first equality follows from its Euler character. All uses of (1) are at these two twists; no general envelope is rerun.

For an irreducible block U O(-j), j>=6, its contribution to H1(K_3(4)) is U tensor Sym(j-6)W and must be a subcharacter of A+P+D. It has dimension (j-5)dim U<=12 and parity U=(-1)^j. This gives exactly the following supported blocks, with their two H1 contributions:

    block        H1 at twist4    H1 at twist5
    A O(-6)          A                 0
    P O(-6)          P                 0
    D O(-6)          D                 0
    Wp O(-7)         P                 Wp
    S O(-7)          A+D               S
    O(-8)            A                 W
    V O(-8)          P+D               T
    W O(-9)          A+D               W+S
    O(-10)           D                 S
    Wp O(-11)        A+P+D             S+T
    O(-14)           P+D               Wp+T

Completeness: at j=6 only A,P,D are supported. At j=7 the odd tensor-with-W identities give just Wp and S. At j=8, only coefficients 1,A,V,P fit the dimension bound; A tensor A contains 1, P tensor A contains V, and precisely 1 and V survive. At j=9 only W,Wp fit; W tensor S=A+D survives, whereas Wp tensor S=V+D does not. At j=10 only the trivial coefficient fits and gives D. At j=11 only W,Wp fit; W tensor T has V, while Wp tensor T=A+P+D survives. At j=12 only the trivial coefficient fits and gives V+P, forbidden. Odd j>=13 exceed the dimension bound. At even j=14 and 16, the only coefficient is trivial; its contributions are P+D and A+V+D, respectively, so only j=14 survives. At j>=18 even the trivial coefficient exceeds the bound.

Degree-minus-five blocks contribute their coefficients to H0(K_3(5)). Equation (1) requires H1(K_3(5)) to contain W. In the complete table, only O(-8) and W O(-9) can supply it. Both consume the entire A budget, so exactly one occurs. Combining the remaining P,D budget and then matching (1) gives the eight necessary splittings:

    S O(-5)+P O(-6)+W O(-9);
    (S+Wp) O(-5)+Wp O(-7)+W O(-9);
    (P+D) O(-6)+O(-8);
    S O(-5)+P O(-6)+O(-8)+O(-10);
    Wp O(-5)+D O(-6)+Wp O(-7)+O(-8);
    (Wp+S) O(-5)+Wp O(-7)+O(-8)+O(-10);
    T O(-5)+(V+1) O(-8);
    (Wp+T) O(-5)+O(-8)+O(-14).

Every displayed type has rank ten and degree minus sixty-two. This classification is necessary, not a realization claim.

Strict-top applied to K_3 gives an injection

    H0(K_3(5)) -> H0(W O(4))=S+T.

The four types with a Wp coefficient at degree minus five are therefore impossible. Exactly four types remain:

    I:   S O(-5)+P O(-6)+W O(-9);
    II:  (P+D) O(-6)+O(-8);
    III: S O(-5)+P O(-6)+O(-8)+O(-10);
    IV:  T O(-5)+(V+1) O(-8).                       (2)

The W O(-9) row and type I are essential and must not be omitted.

## 2. Generic derivative rank one is impossible

A rank-zero derivative is impossible for the nonzero negative saturated K_3: it would be a constant subbundle.

Suppose its generic derivative rank were one. Its saturation in W O(-1) would be an equivariant line O(k). It has k<=-1, and parity plus absence of nontrivial one-dimensional G characters force k to be even, hence k<=-2.

In type II, strict-top at twist six injects P+D, of dimension nine, into H0(O(k+6)), whose dimension is at most five. This is impossible. In type IV the twist-five injection would inject T, of dimension six, into at most four sections, again impossible.

For types I and III, strict-top at twist five injects S, of dimension four, into H0(O(k+5)). This forces k=-2. The S top map to O(-2) is its full cubic section system and is therefore onto everywhere. Consequently the raw derivative image of K_3 is already exactly O(-2), not a proper subsheaf of it. Thus the actual quotient is

    K_3/K_4=O(-2).

The displayed P O(-6) summand maps trivially to this quotient, since Hom_G(P,Sym4 W)=Hom_G(P,D)=0. Hence P O(-6) is a subbundle of K_4. Strict-top gives maxdeg K_4<=-6, so its twist-six sections contain P.

But the actual derivative of K_4 lands in (K_3/K_4)(-2)=O(-4). Strict-top once more requires an injection

    H0(K_4(6)) -> H0(O(2))=A.

Its source contains P, which cannot inject into A. This contradiction excludes the rank-one case in I and III as well.

Thus K_3 has generic derivative rank two in every remaining type.

## 3. The full rank-two image is saturated

In type II restrict the derivative to its top (P+D) O(-6). Strict-top injects P+D into H0(W O(5)), of dimension twelve. The restricted map cannot have rank one, since an equivariant saturated line O(k), k<=-2, would provide at most five sections after twist six. Its twist-six image is globally generated and has degree 10-delta, where delta is its torsion cokernel length. Therefore

    9 <= h0(image)=12-delta,

so delta<=3. A nonzero invariant divisor has degree at least twelve. Hence delta=0 and the top block already surjects W O(-1).

In type IV the same reasoning applies to T O(-5): rank one would give at most four sections, while rank two and global generation give

    6 <= 10-delta,

so delta<=4 and again delta=0.

For types I and III, the unique S O(-5) -> W O(-1) channel factors through the standard Euler O(-2) subline. This follows from W tensor Sym4 W=S+T and the nonzero Euler composition of the full cubic S system. Strict-top makes the channel nonzero, so its image is exactly O(-2).

Compose the full derivative with the Euler quotient

    W O(-1) -> O.

Its S component is zero since S does not occur in Sym5 W=T. Its W O(-9) component in type I is zero since W does not occur in Sym9 W=S+T. Its O(-8), O(-10) components in type III are zero since neither Sym8 W=P+D nor Sym10 W=A+V+D contains 1. Thus only P O(-6) can map nontrivially to O.

Generic rank two forces that P channel to be nonzero. Its four independent degree-six sections have no common zero: any common divisor would be invariant and have degree at most six, less than twelve. Hence it is onto O. Together with the already-surjective Euler O(-2) component, this proves that the full derivative image is all W O(-1).

In every case the image is saturated. Therefore

    K_3/K_4=W O(-1),
    rank K_4=8, degree K_4=-60.

## Boundary

The proof uses an exhaustive small support resolution only to distinguish actual derivative channels and apply the strict-top connection obstruction. It does not assert realizability of any listed splitting, evaluate any actual source instance, or exclude the label. Fresh independent review is required.
