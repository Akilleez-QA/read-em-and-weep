# Rank ten: exact global resolution and a smaller exceptional set

Retain the equivariant operation and bundle hypotheses of ../../local-defect/rank-one-quadratic-flag-nef/PROOF.md and ../../local-defect/global-linear-image-plucker/PROOF.md. The assertions below are conditional on generic rank(Q)=10; they do not establish that generic rank.

## 1. The actual image is saturated

Write X=P(V)=P^4, G=im(b), F its saturation in J⊗O_X, and R=(J⊗O_X)/F. The rank-ten argument in rank-ten-pure-divisorial-defect/PROOF.md identifies G as a vector bundle and gives

    0 → O_X(−3) → O_X(−1)^15 → G → 0.

The degree-two determinant branch has already been excluded. The present PROOF.md excludes the remaining positive-degree divisorial branch (k,d)=(7,5). Therefore (k,d)=(12,0). Purity of F/G, proved in the cited rank-ten argument, forces F/G=0. Thus F=G and there is an exact global resolution

    0 → O_X(−3) → O_X(−1)^15 → O_X^20 → R → 0.

The sheaf R is torsion-free of rank six. From its K-theory class,

    ch(R)=20−15 exp(−h)+exp(−3h)=6+12h−3h²+⋯.

Consequently c1(R)=12h and c2(R)=75h².

## 2. Exceptional quadratic basepoints have codimension at least two

Let L=O_X(−1), U=(V⊗O_X)/L, and C=(J⊗O_X)/A, where A=L²⊗U is the established rank-four subbundle. The linear bundle map underlying the normal quadrics is

    Q: L⊗Sym²U → C,

with domain rank ten and target rank sixteen. Since d=0, b has generic rank fourteen at every codimension-one point; equivalently, Q has rank ten at every such point. One can also see this directly from the saturated injection of bundles G→O_X^20: over a codimension-one local DVR, its torsion-free quotient R is free, so the injection splits and retains rank fourteen in the residue field. Quotienting by the rank-four subbundle A gives the corresponding assertion for Q.

Let Z be the closed rank-drop locus where the linear map Q has rank at most nine. It is defined by its maximal minors. It is proper by the generic-rank hypothesis and has no divisorial component, so dim Z≤2 (with the empty case allowed).

Let E⊂X be the exceptional set where the normal quadratic system has a projective basepoint. If [p]∈P(U_u) is such a basepoint, then p≠0 and p²≠0 in Sym²U_u. Its tensor with any nonzero element of L_u lies in the kernel of Q_u. Therefore rank(Q_u)≤9, and

    E ⊂ Z,    hence dim E ≤ 2.

Here E is closed, since it is the image of the projective quadratic incidence in P_X(U). The conclusion concerns the exceptional set in X; it does not bound the entire incidence by two, because its fibers over E may be positive-dimensional.

No global full-rank assertion is made: Q can still drop rank in codimension at least two, and R has only been proved torsion-free, not locally free. All statements use the global resolutions and universal sheaf geometry, with no actual operation evaluations or rank instances.
