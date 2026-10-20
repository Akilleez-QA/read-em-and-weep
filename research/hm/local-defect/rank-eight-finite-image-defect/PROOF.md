> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Conditional identification of the finite image-saturation defect

## Statement and dependency boundary

Work on X=P(V)=P^4 over C, with the convention that P(V) parametrizes lines. All Ext symbols below mean sheaf Ext, not global Ext groups. Retain the global sequences established in ../rank-eight-kernel-chern/PROOF.md:

    0 → O(-2) → Ktilde → B(-2) → 0,                 (1)
    0 → Ktilde(-1) → O(-1)^15 → G → 0,             (2)
    0 → G → F → D → 0.                            (3)

Here F is the saturation of G in the ambient trivial bundle, hence reflexive, and D denotes the image-saturation defect. Assume the already established codimension-two defect vanishing a=0. We explicitly make the additional conditional assumption

    c3(B)=0 and Sing(B) is finite.                  (H)

The intended justification of (H) is the separate small invariant-curve exclusion together with the established identification of the effective singularity curve cycle. This document does not prove that exclusion, and does not assert (H) unconditionally. In fact only the finiteness of Sing(B), rather than its Chern-class formulation, is needed for the argument below.

Set

    T = Ext²_X(B,O_X).

Then D is finite, and there is a canonical isomorphism induced by (1)–(3):

    Ext⁴_X(D,O_X) ≅ T(3).                          (4)

Consequently

    length(D)=length(T),   Supp(D)=Supp(T).

In the rank-two determinant-trivial isolated-singularity setting, both supports equal Sing(B). In particular D is nonzero because the established Riemann–Roch obstruction says B is not locally free.

If the sequences are N-equivariant with the specified linearizations, (4) is N-equivariant. In a completely linearization-safe form, define the finite-sheaf dual by

    Q^D = Ext⁴_X(Q,ω_X).

Then

    D^D ≅ T(3)⊗ω_X,
    D ≅ T^D(-3)⊗ω_X^(-1).                        (5)

Nonequivariantly these become D^D ≅ T(-2) and D ≅ T^D(2). Equivariantly, ω_X must retain its actual canonical linearization; this qualification matters.

## 1. Codimension-two vanishing removes all such components

The divisorial defect already vanishes, so D is supported in codimension at least two. Its codimension-two cycle is effective: the coefficient at each codimension-two generic point is the positive length of its nonzero stalk. Its class on P^4 is a h², with a=0. Every nonzero effective codimension-two cycle has positive degree. Therefore D has no codimension-two component at all, and

    codim_X Supp(D) ≥ 3.                           (6)

In particular G_x=F_x for every point x of codimension at most two. This conclusion uses positivity of the effective cycle, not merely a formal cancellation of Chern characters.

For completeness, reflexivity of F follows directly from saturation. The quotient of the ambient bundle by F is torsion-free. At a point whose regular local ring has dimension at least two, the depth lemma in that quotient sequence gives depth(F_x)≥2; F is torsion-free and is free at codimension-one points. Thus F is reflexive.

## 2. G is reflexive away from Sing(B)

Put U=X\Sing(B). At every x in U the module B(-2)_x is free, so (1) splits over the local ring O_{X,x}. Hence Ktilde_x is free. Sequence (2) is therefore a locally free resolution of G of length at most one on U.

The module G_x is torsion-free, since G is an image subsheaf of the ambient bundle. Let r=dim O_{X,x}=codim_X(x). For r≥3, the depth lemma applied to (2) gives

    depth(G_x) ≥ r-1 ≥ 2.

At r=2, (6) gives G_x=F_x, which has depth at least two. At r=1 torsion-freeness gives depth at least one, and the generic points impose no further condition. Thus G|U satisfies S2 and is torsion-free. It is reflexive on the regular scheme U.

Both G|U and F|U are now reflexive, and their given inclusion is an isomorphism outside a subset of codimension at least three, by (6). A reflexive sheaf on a normal scheme is the pushforward of its restriction across any closed subset of codimension at least two. Applying this to that inclusion yields

    G|U = F|U.

It follows that Supp(D)⊆Sing(B), so D has finite support under (H). This step does not infer reflexivity from projective dimension at most one at codimension two: that inference would be false. Equality with F at codimension two supplies exactly the missing depth condition.

## 3. Dimension shifting with every index recorded

A reflexive sheaf on a smooth fourfold has projective dimension at most two: at local dimension r≥2 it has depth at least two, and Auslander–Buchsbaum gives projective dimension at most r-2≤2; at dimensions zero and one it is free. Therefore

    Ext³_X(F,O_X)=Ext⁴_X(F,O_X)=0.

Apply sheaf Hom(-,O_X) to (3). The relevant exact segment is

    Ext³(F,O_X) → Ext³(G,O_X) → Ext⁴(D,O_X) → Ext⁴(F,O_X).

It follows that the connecting map is a canonical isomorphism

    Ext³(G,O_X) ≅ Ext⁴(D,O_X).                     (7)

Apply the same functor to (2). Because its middle term is locally free, its positive sheaf Ext groups vanish. The segment with indices two and three gives

    Ext²(Ktilde(-1),O_X) ≅ Ext³(G,O_X).            (8)

Twist (1) by O(-1):

    0 → O(-3) → Ktilde(-1) → B(-3) → 0.

The positive sheaf Ext groups of O(-3) vanish. The segment

    Ext¹(O(-3),O_X) → Ext²(B(-3),O_X)
       → Ext²(Ktilde(-1),O_X) → Ext²(O(-3),O_X)

gives a canonical isomorphism

    Ext²(B(-3),O_X) ≅ Ext²(Ktilde(-1),O_X).        (9)

Finally tensor-Hom compatibility for a line bundle gives

    Ext²(B(-3),O_X) ≅ Ext²(B,O_X)⊗O(3)=T(3).     (10)

Combining (7)–(10) proves (4). Each arrow is natural; no choice of a local splitting in Section 2 enters this isomorphism.

## 4. Finite duality, length, and support

At a closed point x, the ring R=O_{X,x} is regular local of dimension four. For a finite-length R-module Q, Ext^j_R(Q,R)=0 for j≠4 and Ext⁴_R(-,R) is an exact contravariant duality on finite-length modules. These assertions follow first for the residue field from the Koszul resolution and then for finite-length modules by a composition series; the biduality also follows from finite free resolutions and derived double duality. In particular

    length Ext⁴_R(Q,R)=length(Q),
    Ext⁴_R(Q,R)=0 ⇔ Q=0.

Applying this stalkwise to (4), and observing that tensoring by a line bundle preserves stalk length and support, proves the asserted equality of lengths and supports. In fact (4) identifies the local finite modules by duality, not only their numerical lengths.

To identify the support with Sing(B), use the isolated self-duality lemma proved by free resolutions in ../rank-eight-isolated-singularity/PROOF.md, Section 1. At an isolated nonfree point the rank-two determinant-trivial reflexive module B_x is self-dual, and

    Ext¹_R(B_x,R) ≅ Ext⁴_R(Ext²_R(B_x,R),R).

If Ext²_R(B_x,R) were zero, Ext¹ would also vanish, contradicting nonfreeness by a minimal free resolution. Thus T_x≠0 at every singular point; conversely it vanishes at every free point. Under (H), Supp(T)=Sing(B), hence Supp(D)=Sing(B).

The nonempty singular locus used here is an established input: a hypothetical rank-two vector bundle with c1=0,c2=5 on P^4 would have c3=c4=0 and χ(B)=-21/2 by Riemann–Roch, an impossibility. This does not require stability.

## 5. Equivariance and the canonical-bundle twist

Sheaf Ext, tensor-Hom compatibility, and connecting maps are functorial for equivariant coherent sheaves. Thus (4) is equivariant whenever (1)–(3) are equivariant with their given linearizations. This conclusion does not require choosing an equivariant local splitting or choosing an equivariant identification B≅B*.

Since ω_X is a line bundle, (4) gives the first isomorphism of (5). Applying finite duality again gives its second isomorphism. For lines in V, the Euler sequence or the determinant of T_X=Hom(O(-1),(V⊗O)/O(-1)) gives the canonical equivariant formula

    ω_{P(V)} ≅ O(-5)⊗det(V)^*.

Accordingly (5), with the standard linearization of O(1), reads

    D^D ≅ T(-2)⊗det(V)^*,
    D ≅ T^D(2)⊗det(V).

If the acting representation has determinant one, these character factors disappear; otherwise they must be retained. Forgetting equivariance always gives the displayed nonequivariant twists. Global Serre duality identifies H⁰(D^D) with H⁰(D)^* naturally, but one should not replace the sheaf duality formula by an untwisted identification of the representations H⁰(D) and H⁰(T)^*.

## 6. Transfer of the established orbit-length alternatives

The finite N-equivariant sheaf D is nonzero, so the orbit theorem in ../normalizer-minimal-point-orbit/PROOF.md, Section 7 applies directly. It also follows by transferring length(T). The unique projective normalizer orbit E of size 30 is the only orbit of size less than 125. Therefore

    length(D) ∈ {30,60,90,120} or length(D) ≥ 125.

If length(D)<125, then

    Supp(D)=Supp(T)=Sing(B)=E,

and the common stalk length of D and T at each of its 30 points is respectively 1, 2, 3, or 4. The equality of local lengths follows from (4), and their constancy follows from equivariance. In the length-30 case, D is nonequivariantly isomorphic to O_E for the reduced orbit. This does not determine its equivariant structure, nor prove that any of these alternatives is realized in the original geometric problem.

## Verification boundary

This is universal sheaf and local homological algebra applied to the established exact sequences. No actual geometric source, matrix, operation, selected input, rank instance, jet, residue evaluation, or large computation was used. Only this local proof artifact was written. The curve-exclusion hypothesis remains explicit and conditional until its separate proof is accepted.
