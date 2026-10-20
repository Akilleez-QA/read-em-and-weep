> Publication scope: preserved mathematical proof/audit. Historical statements that rank eight remains open are superseded only after the final assembly and all its prerequisites. No source-instance evaluation or formal verification is claimed here.

# Isolated singularities: exact local duality and counterexamples

## Results and scope

Let B be the rank-two reflexive sheaf on P4 in the rank-eight branch, with c1(B)=0, c2(B)=5 and B ≅ B*. Its known failure of local freeness does **not**, just by reflexivity, rank two, self-duality, stability and these two Chern classes, imply a curve of singularities.

1. At any isolated singular point, B has projective dimension exactly two and depth exactly two. Its two local defect modules Ext¹(B,O) and Ext²(B,O) are nonzero Matlis duals and have equal lengths.
2. There is a universal local rank-two reflexive self-dual module on a smooth fourfold with exactly one singular point and both Ext modules equal to the residue field.
3. There exist stable rank-two reflexive sheaves on P4 with c1=0, c2=5, c3=0 and exactly one singular point.

Statement 3 does **not** supply the N=H5⋊SL2(F5) equivariance or the particular kernel presentation of the problem. In particular it does not establish existence in the original rank-eight branch. It rules out the proposed blanket local-algebraic or low-Chern-class obstruction. Further progress must use equivariance, the actual abstract kernel presentation, or additional numerical/cohomological constraints.

## 1. Exact local duality

Let (R,m) be a regular local ring of dimension four, and let M be a finite reflexive R-module, locally free on Spec R minus {m}. Write

    A = Ext¹_R(M,R), D = Ext²_R(M,R),
    Q^dagger = Ext⁴_R(Q,R) for finite-length Q.

Reflexivity and Auslander–Buchsbaum give pd M ≤ 2. Both A and D have finite length. The same is true for M*, which is reflexive and free on the punctured spectrum. There are isomorphisms

    Ext¹_R(M*,R) ≅ D^dagger,
    Ext²_R(M*,R) ≅ A^dagger.                         (1)

Here is a direct proof that also fixes all indices. Choose a finite free resolution

    0 → F2 → F1 → F0 → M → 0.

In its dual complex set

    C = im(F0* → F1*), K = ker(F1* → F2*),
    I = im(F1* → F2*).

Then

    0 → M* → F0* → C → 0,
    0 → C → K → A → 0,
    0 → K → F1* → I → 0,
    0 → I → F2* → D → 0.                            (2)

For every finite-length Q, Ext^j_R(Q,R)=0 for j<4, and Ext^j_R(Q,R)=0 for j>4 since R has global dimension four. Dimension shifting in the last two sequences gives

    Ext¹(K,R)=0,
    Ext²(K,R)=D^dagger,
    Ext³(K,R)=Ext⁴(K,R)=0.

The second sequence gives

    Ext²(C,R) ≅ Ext²(K,R)=D^dagger,
    Ext³(C,R) ≅ Ext⁴(A,R)=A^dagger.

The first sequence now proves (1).

If M≅M*, it follows that

    A ≅ D^dagger, D ≅ A^dagger,
    length(A)=length(D).                            (3)

The length equality uses the exact finite-length duality over the regular Gorenstein local ring R. It can also be checked by a composition series, because Ext⁴_R(k,R)≅k and all other Ext groups of k below degree four vanish.

If M is nonfree, D cannot vanish: if D=0 then (3) gives A=0, and a minimal free resolution has no positive last term. Thus both defects are nonzero, pd M=2 and depth M=2.

**Consequences.** An additional proof of pd B≤1 would exclude *isolated* nonfree points. Such a bound is not automatic for rank-two reflexive sheaves on a fourfold. In the isolated-only case, duality gives cancellation of the finite-length Ext classes, rather than a positive-length contradiction. The isomorphisms above apply at a genuinely isolated point; they are not asserted at a closed point lying on a singular curve, where Ext¹ need not have finite length.

## 2. Universal local counterexample

This is a universal commutative-algebra construction, not an evaluation of the operation, matrix, input, or rank instance in the problem.

Take R=C[x1,x2,x3,x4]_(x1,x2,x3,x4). Regard x as the column of the four parameters. Choose a constant invertible alternating 4-by-4 matrix J. Put

    a = x^t : R⁴ → R,
    b = Jx : R → R⁴,
    K = ker(a), M = K/im(b).

Because x^t Jx=0, b maps into K; because R is a domain and Jx≠0, b is injective. The generic rank of M is two.

Off m, the row a is surjective and the column b is unimodular. Locally there, K is free of rank three, and b gives a direct summand of K: a linear functional on R⁴ taking b to 1 restricts to such a functional on K. Thus M is locally free of rank two off m.

The exact sequences

    0 → K → R⁴ → m → 0,
    0 → R → K → M → 0

and depth(m)=1 give depth(K)=2 and depth(M)≥2. Since M is free off m, any torsion would be supported at m and would contradict positive depth. Therefore M is torsion-free and S2, hence reflexive.

For the Ext calculation, use Ext^j_R(k,R)=0 for j≠4 and Ext⁴_R(k,R)=k. The sequence 0→m→R→k→0 gives

    Ext¹(m,R)=Ext²(m,R)=0, Ext³(m,R)=k.

Consequently

    K* = coker(R --x--> R⁴),
    Ext¹(K,R)=0, Ext²(K,R)=k.

On dualizing 0→R→K→M→0, the map K*→R evaluates a functional on Jx. Its image is the ideal generated by the entries of Jx, namely m. It is well-defined on R⁴/Rx since x^tJx=0. Hence

    Ext¹(M,R)=R/m=k,
    Ext²(M,R)=Ext²(K,R)=k.                          (4)

In particular M is nonfree at m. Its determinant is trivial on the punctured spectrum, by the two split exact sequences there. The usual rank-two alternating determinant pairing gives M≅M* there, and extends to an isomorphism of reflexive modules on Spec R. This also proves self-duality without relying on a blanket theorem.

This example decisively disproves the statements “rank-two reflexive implies pd≤1 on a fourfold,” “rank-two self-dual reflexive singularities must contain a curve,” and “vanishing curve defect forces local freeness.”

## 3. Stable global examples with c2=5

### 3.1 A stable bundle on P3

Choose six pairwise disjoint lines Z=L1∪...∪L6 in P3. Their union is a smooth, disconnected local complete intersection of codimension two, and

    ω_Z ≅ O_Z(-2).

Hartshorne–Serre with determinant O(2) applies: H²(P3,O(-2))=0 and ω_Z⊗(ω_P3⊗O(2))^(-1)≅O_Z has a nowhere-zero section. It gives a rank-two vector bundle F and sequence

    0 → O → F → I_Z(2) → 0.

Set E=F(-1). Then

    rank E=2, c1(E)=0, c2(E)=6-1=5,
    0 → O(-1) → E → I_Z(1) → 0.

Two disjoint lines cannot lie in one plane, so H⁰(I_Z(1))=0. Thus H⁰(E)=0. Also H⁰(E(-d))=0 for every d≥0, directly from the twisted sequence. A saturated rank-one destabilizing subsheaf of E would be O(d) with d≥0, impossible by this vanishing. Therefore E is slope-stable.

### 3.2 The projective cone sheaf

Let S=C[x0,x1,x2,x3] and take the full graded section module

    P = ⊕_{t∈Z} H⁰(P3,E(t)).

It is a finite graded S-module. Its sheafification is E, it is locally free on the punctured affine cone, and its local cohomology H⁰_m(P) and H¹_m(P) vanish because it is the full section module. Thus depth_m(P)≥2. Together with local freeness off m this says P is reflexive.

Adjoin one degree-one variable y and define on P4=Proj S[y]

    B = sheafification of P⊗_S S[y].

Polynomial extension preserves the reflexive module property: for finite presented modules, Hom commutes with this flat base change, so the bidual map remains an isomorphism. Thus B is reflexive. Outside the vertex

    v=[0:0:0:0:1],

B is the pullback of E under the projection π:P4\{v}→P3. It is locally free there. On each hyperplane H avoiding v, π|H is an isomorphism, so B|H≅E.

The stalk at v is, after setting y=1, P_m. It is not free. Indeed a minimal graded free resolution of P remains minimal upon localization at m. If P_m were free, every positive free term would vanish, making P a graded free module and E a sum of line bundles. This contradicts stability. Hence Sing(B)={v}.

Restriction to a hyperplane avoiding v gives

    c1(B)=0, c2(B)=5, c3(B)=0,

because restriction on the corresponding Chow groups is injective and E is a rank-two vector bundle. The determinant of B is O; the rank-two determinant pairing on the free locus extends by reflexivity, giving B≅B*.

Finally B is slope-stable. A saturated rank-one subsheaf D with slope≥0 is reflexive: use the depth lemma with B reflexive and B/D torsion-free. Hence D=O(d), d≥0. A nonzero injection O(d)→B restricts nontrivially to a general hyperplane H avoiding v. It would give a nonzero map O_H(d)→E, contradicting stability of E.

This proves the claimed stable global example. We do not claim its fourth Chern class vanishes; it cannot be treated as a vector bundle in Riemann–Roch.

## 4. What equivariance still changes

The singleton singular locus of the construction in §3 prevents it from carrying an equivariant structure for the irreducible projective H5 action of the original problem: an equivariant singular locus consisting of a singleton would give an H5-invariant projective point, hence an invariant line in V, contradicting irreducibility.

Thus §3 is deliberately an example after forgetting N-equivariance. It shows that rank, stability, self-duality, c1=0 and c2=5 do not close the isolated-point branch. It does not disprove an obstruction that genuinely uses N-equivariance or the special kernel presentation. In a hypothetical equivariant isolated-point branch, the singular support must be a union of nontrivial finite projective N-orbits, and the local finite-length modules in §1 must transform compatibly.

## Sources and verification boundary

The local construction and duality above are proved directly by finite free resolutions, the depth lemma and the Koszul Ext calculation. No external local-rank theorem is needed.

For the only specialized existence input in §3, the primary source is E. Arrondo, *A home-made Hartshorne–Serre correspondence*, Revista Matemática Complutense 20 (2007), 423–443, Theorem 1, arXiv version printed p.3, with extension sequence and verification of local freeness on pp.3–4:

https://arxiv.org/pdf/math/0610015

The source explicitly permits a local complete intersection subscheme and requires H²(L*)=0 plus generation of det(N)⊗L* by r−1 sections. Our application uses r=2, L=O(2), and the single nowhere-zero section of O_Z. No connectedness hypothesis is imposed.

For independent context, the primary article *Self-duality of rank 2 reflexive modules*, Journal of Pure and Applied Algebra 16 (1980), 275–284, reports the alternating self-duality theorem for rank-two reflexive modules:

https://doi.org/10.1016/0022-4049(80)90033-X

Our use of self-duality is proved by determinant pairing and extension, rather than relying on unseen details of that article.

No original physical source, operation, input, actual rank instance, jet, residue, polynomial-instance test, or large computation was used. The local symbolic construction is independent universal commutative algebra.
