> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Rank-eight kernel: global quotient, semistability, and codimension-two defect

## Result and scope

Work over C on X=P(V)=P4, with h=c1(O(1)), L=O(-1), U=(V tensor O)/L, and S=Sym²V. Retain the established N-equivariant operation, its canonical square relation, the rank-four subbundle A=L² tensor U of J tensor O, and the rank-eight branch

    generic rank Q=8, det F=O(-6), divisorial defect d=0,
    c2(F)=19 h².

Here b:L tensor S -> J tensor O, G=im b, F is its saturation, and T=F/G. Put [T]_2=a h². Define

    Ktilde=ker(b(1):S tensor O -> J tensor O(1)),
    K=(ker Q)(1), B=K(2).

Then the following statements hold globally as coherent-sheaf statements:

    0 -> O(-2) -> Ktilde -> K -> 0;
    rank K=2, K reflexive, c1(K)=-4h;
    c2(K)+a=9, c1(B)=0, c2(B)=5-a;
    B is slope-semistable with respect to O(1);
    a belongs to {0,5}.

The Chern integers suppress h². Semistability is proved, not assumed. The final step uses the usual characteristic-zero Bogomolov inequality. This document does not exclude the endpoint a=5. Conditionally on a=0, B cannot be locally free; a direct Riemann--Roch obstruction is supplied below.

## 1. The exact quotient is global

The symmetric-square sequence for 0->L->V tensor O->U->0 is

    0 -> L tensor V -> S tensor O -> Sym²U -> 0.       (1)

The first arrow is multiplication. It is a subbundle inclusion: after locally splitting V tensor O=L direct-sum U, its image is L² direct-sum (L tensor U), exactly the kernel of the projection to Sym²U. In particular its rank is five, not four.

The canonical operation identities imply that the restriction of b(1) to this subbundle maps onto A(1)=L tensor U. This restriction is the quotient L tensor V -> L tensor U followed by the established subbundle identification with A(1). Its kernel is L². Thus there is a commutative diagram whose rows are the exact sequence (1) and

    0 -> A(1) -> J tensor O(1) -> C(1) -> 0,

and whose vertical maps are the canonical surjection L tensor V -> A(1), b(1), and Q(1). The snake lemma, using surjectivity of the left vertical map as a sheaf map, gives

    0 -> L² -> Ktilde -> ker Q(1) -> 0.              (2)

Hence the requested quotient is precisely K globally. No equality merely away from a degeneracy locus, and no replacement of the quotient by its reflexive hull, is necessary. Equivalently, one can lift a local section of ker Q(1) to S tensor O and subtract a section of L tensor V having the same image in A(1).

The canonical line in (2) sends u² to its square tensor, so it is the same O(-2) line used in the rank-nine kernel argument.

## 2. Reflexivity and the Chern identity

The image of Q is torsion-free, since it is a subsheaf of the vector bundle C. The kernel of the map from the bundle L tensor Sym²U to this torsion-free image is reflexive: at every point of codimension at least two the depth lemma gives depth at least two; it is torsion-free and free in codimension one. Thus K and B are reflexive. The same argument applies to Ktilde.

The rank of b is 4+8=12, so Ktilde has rank three. Since d=0, c1(G)=c1(F)=-6h. From

    0 -> Ktilde(-1) -> O(-1)^15 -> G -> 0

we obtain c1(Ktilde(-1))=-9h and c1(Ktilde)=-6h. Sequence (2) then gives c1(K)=-4h, as also established by the pencil-discriminant proof.

Write c=c2(K). By (2),

    c2(Ktilde)=c+8.

For a rank-three sheaf E, twisting by O(-1) gives c2(E(-1))=c2(E)-2c1(E)+3. Consequently

    c2(Ktilde(-1))=c+23.

The degree-two part of the preceding exact sequence with source O(-1)^15 yields

    105=(c+23)+(-9)(-6)+c2(G),
    c2(G)=28-c.

Because T has support of codimension at least two, ch2(T)=a h². The sequence 0->G->F->T->0 therefore gives

    c2(F)=c2(G)-a=28-c-a.

Using c2(F)=19 proves c+a=9. Finally the rank-two twist formula gives

    c1(B)=c1(K)+4=0,
    c2(B)=c2(K)+2c1(K)+4=c-4=5-a.                (3)

These calculations use Chern classes of coherent sheaves in the Chow ring of the smooth ambient space; they do not presume local freeness at codimension-three points.

## 3. Negative-twist vanishing

Twisting (1) by O(m) gives

    0 -> V tensor O(m-1) -> S tensor O(m) -> Sym²U(m) -> 0.

For m<0, H0(O(m))=0 and H1(O(m-1))=0 on P4. Hence

    H0(Sym²U(m))=0 for every m<0.                  (4)

The kernel inclusion K->Sym²U gives

    B -> Sym²U(2).                                 (5)

Thus H0(B(-e))=0 whenever e>2. This vanishing applies to sheaf injections and does not require (5) to be a subbundle inclusion at every point.

## 4. Equivariance forces slope-semistability

Use the established H5 center generator acting by zeta on V and on L. It acts by zeta² on Sym²U and K, while O(2) has weight zeta^(-2). Hence the center acts trivially on B.

Suppose B were unstable. Its unique first Harder--Narasimhan subsheaf D is saturated of rank one, with positive slope. Since N preserves O(1) and the linearization of B, uniqueness makes D an N-equivariant subsheaf. A saturated subsheaf of a reflexive sheaf with torsion-free quotient is reflexive, by the depth lemma. Rank-one reflexive sheaves on smooth factorial P4 are line bundles. Therefore

    D=O(e), with e>0.

The induced linearization on this line has trivial central action, because it is a subobject of B. The standard linearization on O(e) has central weight zeta^(-e). Two linearizations differ by a character of N; every such character is trivial on the center of H5, which lies in its commutator subgroup. It follows that e=0 modulo 5. Since e>0, e>=5.

But D->B would give a nonzero section of B(-e), contradicting (4)--(5), since e>2. This proves slope-semistability of B.

The argument does not claim stability: when e=0 the central-character obstruction disappears, and uniqueness of a destabilizing positive-slope line is no longer available.

## 5. Bogomolov and the defect congruence

For a slope-semistable torsion-free rank-r sheaf E on a smooth complex projective n-fold polarized by H, the Bogomolov inequality is

    (2r c2(E)-(r-1)c1(E)²) H^(n-2) >= 0.

A directly verified primary reference stating this characteristic-zero form, including arbitrary dimension and torsion-free sheaves, is A. Langer, “Bogomolov’s inequality for Higgs sheaves in positive characteristic,” Inventiones mathematicae 199 (2015), 889--920, Introduction:

https://doi.org/10.1007/s00222-014-0534-z

Apply it to B, with rank two, c1=0 and H=h. It gives c2(B)>=0. Equation (3) then implies a<=5.

Effectivity of the top-dimensional cycle of T gives a>=0. The existing Heisenberg Hilbert-congruence theorem applies to the equivariant sheaf T, whose support has dimension at most two, and gives 5 divides a. Thus

    a=0 or a=5.

This strengthens the elementary dual-generation estimate a<=17. If a=0, T has no codimension-two component, but may still have support in codimension three or four; a=0 alone does not prove G=F.

## 6. Conditional non-local-freeness at a=0

If a=0, (3) gives c1(B)=0,c2(B)=5h². Suppose additionally that B were a vector bundle. As a rank-two bundle it would have c3=c4=0. Then

    ch(B)=2-5h²+(25/12)h⁴.

For P4, td1=(5/2)h, td2=(35/12)h², and the degree-four Todd term integrates to chi(O)=1. Hirzebruch--Riemann--Roch therefore gives

    chi(B)=2-5*(35/12)+25/12=-21/2,

which is impossible for an Euler characteristic. Hence a=0 forces the reflexive sheaf B to have a nonempty singular locus, necessarily of codimension at least three. This is a conditional obstruction only; it does not identify that locus or exclude a=0.

## Sources and evidence boundary

Existing local sources: ../rank-four-global-determinant/PROOF.md (bundle diagram and central characters), ../rank-nine-kernel-splitting/PROOF.md (square line, representation conventions), ../rank-eight-pencil-discriminant/PROOF.md (rank-two reflexive kernel), and ../heisenberg-defect-hilbert-congruence/PROOF.md (defect divisibility). The only new external mathematical input used here is the explicitly stated Bogomolov inequality above.

Only universal bundle identities, sheaf exact sequences, depth, equivariant Harder--Narasimhan uniqueness, cohomological vanishing, Chern classes, and Riemann--Roch were used. No actual source, operation, matrix, selected input, rank instance, jet, residue, or large computation was evaluated. The only write is this local proof artifact.
