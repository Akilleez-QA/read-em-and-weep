> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Excluding the flat normalized residual kernel at rank eight

## Result and exact scope

Over the complex numbers, retain the equivariant bundle and representation setup of `../global-linear-image-plucker/PROOF.md` and `../rank-nine-kernel-splitting/PROOF.md`. Suppose the generic rank of Q is eight, and put

    S = Sym²V,
    Ktilde = ker(S ⊗ O → J ⊗ O(1)),
    K = Ktilde/O(-2),
    B = K(2).

The first inclusion in the quotient is the canonical square u ↦ u². Suppose the independently established Chern and semistability argument gives that B is reflexive, slope-semistable, of rank two, with c1(B)=0 and c2(B)=5−a, where a is a nonnegative multiple of five. Then

    a ≠ 5.

In particular, combined with Bogomolov's inequality, a=0 and c2(B)=5. This does not exclude generic rank eight; it excludes only its flat residual-kernel possibility. It makes no claim of local freeness of the remaining c2=5 kernel or absence of defects of codimension at least three.

## 1. Verified flat-reflexive theorem

A slope-semistable reflexive sheaf E on complex projective space P^n, n≥3, with c1(E)=c2(E)=0 is trivial.

A directly applicable primary research source is D. Guimarães and M. Jardim, *Moduli spaces of quasi-trivial sheaves*, arXiv:2108.01506v2, §2, Definition 2.4 and Lemma 2.5, printed pp.4–5:

https://arxiv.org/pdf/2108.01506

Their lemma says that a slope-semistable sheaf with these numerical vanishings on a “good” smooth polarized variety has trivial reflexive hull. Projective space satisfies their good-variety conditions; they explicitly include Picard-rank-one Fano manifolds. Applying the lemma to reflexive E proves the stated conclusion. No vanishing assumption on c3 or c4 is needed.

For the underlying theorem, C. Simpson, *Higgs bundles and local systems*, Publ. Math. IHÉS 75 (1992), Theorem 2, printed p.39, states that a semistable torsion-free Higgs sheaf with zero first and second Chern-character intersections, and which is reflexive, is an extension of stable Higgs bundles with vanishing Chern classes:

https://archive.numdam.org/item/PMIHES_1992__75__5_0.pdf

The theorem's statement was independently retrieved in the primary PDF's indexed text. A separately fully readable primary formulation is A. Langer, *Bogomolov’s inequality for Higgs sheaves in positive characteristic*, §5.1, Corollary 6:

https://link.springer.com/article/10.1007/s00222-014-0534-z

Use the zero Higgs field. On simply connected P^n, stable zero-Chern factors correspond to trivial irreducible local systems, hence have rank one and underlying bundle O. Extensions split since H¹(O)=0. This explains precisely why reflexivity suffices and why higher Chern classes need not be assumed away.

## 2. Consequence for the square-containing kernel

If a=5, Section 1 gives B=O² and hence K=O(-2)². The canonical exact sequence becomes

    0 → O(-2) → Ktilde → O(-2)² → 0.

Its extension group is

    Ext¹(O(-2)²,O(-2)) = H¹(O)² = 0.

Therefore Ktilde ≅ O(-2)³ as an ordinary sheaf. We do not need to identify any equivariant splitting. All original maps are N-equivariant, so the three-dimensional vector space

    T = H⁰(Ktilde(2))

has its intrinsic N-action. The sheaf inclusion Ktilde → S⊗O induces an injective N-linear map

    T → S ⊗ H⁰(O(2)) = S ⊗ Sym²V* = End(S).       (1)

The square inclusion supplies a nonzero N-invariant vector in T. Under (1), it is the identity endomorphism of S: evaluating the polynomial associated to id_S on u is exactly u².

Here the action on End(S) is conjugation. In particular the central subgroup Z(H5)=μ5 acts trivially, although it acts by a nontrivial scalar on S itself.

## 3. Why the entire three-dimensional module is H5-trivial

It is important not to replace “trivial central character” with “trivial H5 action” without proof.

Because Z(H5) acts trivially on T, the restriction of T to H5 factors through the abelian group H5/Z(H5) ≅ F5². Over C it decomposes into character spaces. The quotient G=N/H5=SL₂(F5) permutes those character spaces by its natural dual action on F5². It acts transitively on the 24 nonzero characters. Indeed every nonzero vector can be completed to a determinant-one basis, proving transitivity of SL₂(F5), and the dual action is equivalent to its natural action.

If any nontrivial character occurred in T, all 24 would occur with equal positive multiplicity, since conjugation by G gives isomorphisms of the corresponding weight spaces. This would force dim T≥24. Since dim T=3, only the trivial character occurs. Thus H5 acts trivially on T, and (1) lands in

    End_H5(S).                                            (2)

## 4. The exact nine-dimensional commutant

The already audited classical normalizer identity is

    S = A ⊗ R,       R = Sym²Q,

where A restricts irreducibly to H5, Q is an irreducible determinant-one two-dimensional G-module, and R is the irreducible three-dimensional G-module. This is established in `../rank-nine-kernel-splitting/PROOF.md`, §1, using the classical representation inputs documented in `../../full-hm-image-symmetry/PROOF.md`. The notation Q here denotes that two-dimensional representation, not the bundle map whose generic rank is being discussed.

By Schur's lemma,

    End_H5(S) ≅ End(R)

as G-modules. The identification is equivariant: conjugation on the A-factor fixes its scalar endomorphisms, and the remaining action is conjugation on End(R).

The determinant-one two-dimensional Clebsch–Gordan identity gives

    End(R) = Sym²Q ⊗ Sym²Q
           = 1 ⊕ Sym²Q ⊕ Sym⁴Q.                         (3)

All three summands are irreducible, of dimensions 1, 3, and 5, respectively. Irreducibility of Sym²Q is proved in the rank-nine proof. For completeness, the small character verification for Sym⁴Q is reproduced in `../rank-seven-cubic-plucker-obstruction/PROOF.md`, §4: its class values are

    (5,5,1,-1,-1,0,0,0,0)

on classes of sizes

    (1,1,30,20,20,12,12,12,12),

and its squared norm is (25+25+30+20+20)/120=1. These are universal representation-character calculations, not operation or rank evaluations.

## 5. Contradiction

The image of T in (2) is a three-dimensional G-submodule containing the scalar identity. By semisimplicity of finite-group representations over C, that invariant line has a G-stable complement of dimension two inside T. But (3) has exactly one trivial constituent and its other irreducible constituents have dimensions three and five. It has no two-dimensional submodule complementary to its invariant line. This is a contradiction.

Equivalently, a dimension-three submodule of the multiplicity-free module 1⊕3⊕5 must be its irreducible three-dimensional summand, which contains no invariant vector. Therefore the a=5 branch is impossible.

## Evidence boundary

Only existing proof files, primary research sources, sheaf exact sequences, standard cohomology, and universal finite-group representation identities were used. No actual operation, source matrix, multiplication, chosen input, rank instance, jet, residue, polynomial-instance test, or large computation was evaluated. The Chern identity, semistability, and divisibility of a remain explicitly imported hypotheses rather than silently reproved assertions.
