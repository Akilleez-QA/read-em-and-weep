# The hypothetical rank-seven kernel is stable, with second Chern class 7 or 12

Let beta:M2^* tensor O -> sl(W')^* tensor Omega^1(2) be the actual dual primary evaluation on X=P(A0), A0=V3. Assume its generic rank is seven. The established determinant restriction gives an exact sequence

    0 -> K -> M2^* tensor O -> I ->0,

where K is saturated reflexive of rank3, det K=O(-4), and I is torsion-free of rank7. Crucially I is an actual quotient of the trivial bundle, so is globally generated, not merely generated away from codimension two.

The new conclusions are slope stability of K and

    c2(K)=7h^2 or12h^2,
    c2(I)=9h^2 or4h^2, respectively.

The universal Heisenberg congruence is credited to PR240; this is a new application to this different actual kernel. No identification with the older trilinear residual map is used.

## 1. Stability using the canonical destabilizing subsheaf

Suppose K were not slope-semistable for O(1). Its maximal destabilizing Harder-Narasimhan subsheaf F is canonical, so inherits the N-action. This equivariance is not claimed for arbitrary subsheaves. Let s=rank F, equal to1 or2, and write det F=O(-d).

Since F lies in the trivial M2^* bundle, its determinant inclusion gives d>=0. The center acts on M2^* with weight4 mod5 and on O(-d) with weight3d. Perfectness of N removes a possible character twist. Therefore

    3d congruent4s mod5, or d congruent3s mod5.

Destabilization requires -d/s>-4/3.

For s=1 this gives d<=1, inconsistent with d congruent3 mod5. For s=2 it gives d<=2, hence the congruence forces d=1. But the determinant inclusion would then give an invariant in

    exterior^2 M2^* tensor A0^*.

Its multiplicity decomposition is

    exterior^2(V^* tensor W')
      =V3 tensor [(W tensor U') direct-sum U'],

where W is unprimed and U'=Sym^2 W'. After tensoring by A0^*=V1 and taking H-invariants, the first summand has negative binary-central parity and the second is a nontrivial irreducible. Neither has an invariant. Thus d=1 is impossible as well.

K is semistable. Since gcd(3,4)=1, a proper rank-one or rank-two subsheaf cannot have the same slope -4/3. Hence K is stable.

## 2. The credited Heisenberg congruence, with the weight rescaling explicit

PR240 proves that on P(V), when the center acts on V with weight1 and a coherent sheaf of rank n has uniform central weight w, its Chern classes satisfy

    c_i congruent binom(n,i)(-w)^i mod5.

Here the projective coordinate representation is A0=V3, of weight3, while K has weight4. Rescaling the central generator to make the coordinate weight one changes the sheaf weight to 4/3=3 mod5. Thus

    c2(K) congruent binom(3,2)*3^2=27=2 mod5.

This uses the existing general congruence, not a newly claimed congruence theorem. Its hypotheses apply directly to K as an H-equivariant coherent sheaf; no local freeness in codimension two is required.

The immutable source is PR240 at 448020d24955b3a545452a8ce7f10612f3df9f6d, research/hm/local-defect/full-support-equivariant-chern-congruences/PROOF.md:
https://github.com/Akilleez-QA/read-em-and-weep/blob/448020d24955b3a545452a8ce7f10612f3df9f6d/research/hm/local-defect/full-support-equivariant-chern-congruences/PROOF.md

## 3. Bogomolov gives the lower bound

The characteristic-zero Bogomolov inequality for slope-semistable torsion-free sheaves on a smooth projective variety states

    (2r c2-(r-1)c1^2) h^(dim X-2)>=0.

For rank3 and c1=-4h this gives 6 c2(K)-32>=0, interpreting c2(K) by its integer coefficient. Hence c2(K)>=6, and the congruence refines this to c2(K)>=7.

This standard external theorem is used in its torsion-free, higher-dimensional form, not merely for surface bundles. A primary research reference stating this form is A. Langer, “Bogomolov's inequality for Higgs sheaves in positive characteristic,” Inventiones Mathematicae, introduction:
https://link.springer.com/article/10.1007/s00222-014-0534-z

## 4. A direct positivity proof for the actual globally generated image

We include a self-contained proof of the following classical positivity fact, without claiming novelty for the lemma: if a torsion-free sheaf G of rank r on smooth projective space is globally generated, then its second Chern class has nonnegative degree.

Choose r-1 general global sections. On the open set where G is locally free, global generation makes the evaluation at each point onto. The incidence condition that these sections are dependent has codimension two in the parameter space of their values. Therefore their degeneracy has codimension at least two for a general choice. The non-locally-free locus of G also has codimension at least two. Consequently the resulting injection

    O^(r-1) -> G

is a direct subbundle at every codimension-one point.

Its quotient is torsion-free. Indeed a section of G whose generic value lies in the span of the chosen sections can be written as a rational linear combination of them. At every height-one point the direct-subbundle property makes its coefficients regular. Normality implies those coefficients are regular everywhere on each affine open, so the section already lies in O^(r-1). This is exactly saturation.

The rank-one torsion-free quotient embeds into its double dual, the line bundle det G. Thus it is I_Z tensor det G for a subscheme Z of codimension at least two. The exact sequence gives

    c2(G)=c2(I_Z tensor det G)=[Z]_codimension2,

an effective codimension-two cycle (possibly zero). This proves the required positivity without choosing a plane disjoint from a codimension-two singular set.

Apply this to G=I. The exact sequence defining I gives c(K)c(I)=1, so

    c2(K)+c2(I)=c1(K)^2=16h^2.

Since c2(I) has nonnegative degree, c2(K)<=16. Combining this with c2(K)>=7 and c2(K)=2 mod5 yields exactly7 or12. The corresponding c2(I) values are9 and4.

## Scope

This is a necessary geometric restriction on the hypothetical generic-rank-seven kernel. It does not show that either Chern pair is realized, rule out rank seven, prove generic rank ten, or settle the full adjoint quadratic map or original Q4. The proof uses no selected polynomial, coefficient, multiplication matrix, source value, or rank experiment. 
