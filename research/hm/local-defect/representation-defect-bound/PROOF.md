Publication context: this retained proof or audit may describe an intermediate bound or then-open branch. Read the unit overview for the current scope and later implications. Historical mathematical review is not a new formal verification.

# Representation imbalance strengthens the isolated self-dual rank bound

## Theorem

Let (R,m,k) be a regular local complex algebra of dimension four with residue field k=C, acted on by a finite group H fixing the closed point. Let M be an H-equivariant reflexive R-module of rank r, free away from the closed point, and assume an **equivariant** isomorphism M≅M*. Set

    Q=Ext²_R(M,R),   D(N)=Ext⁴_R(N,R),
    A=D(Q),   V=Tor₁^R(A,k),   s=dim(A/mA),
    d=dim V−2s=β₃(Q)−2β₄(Q).

For a finite-dimensional complex H-representation V put

    a_H(V)=Σ_{ρ irreducible} dim(ρ) max(m_ρ(V)−m_ρ(V*),0)
          =(1/2)Σ_ρ dim(ρ)|m_ρ(V)−m_ρ(V*)|.

Then

    r ≥ d+a_H(V).                                           (T)

In particular, for rank two one necessarily has d+a_H(V)≤2. No hypothesis on a symmetric or alternating choice of self-duality is needed. Rank-two equivariantly trivial determinant is one sufficient source of the required self-duality. The theorem applies in all ranks, not just rank two.

A representation-level version is useful: let

    J_H(V)=⊕_ρ ρ^{⊕ max(m_ρ(V)−m_ρ(V*),0)}.

For any module M as above there is a cokernel T of an equivariant map V*→V such that J_H(V) is a direct summand of T and

    dim T≤r−d.

Thus the prescribed excess irreducibles must fit into a space of dimension at most r−d. This is a necessary condition, not a realization criterion.

## 1. Why the duality identity is valid in every rank

Initially write A_M=Ext¹_R(M,R). Reflexivity and Auslander–Buchsbaum give pd M≤2. Both A_M and Q have finite length by the punctured-spectrum freeness assumption. Choose an equivariant minimal free resolution

    0→F₂→F₁→F₀→M→0.

Such resolutions exist by equivariantly splitting each finite-dimensional generator quotient; averaging is available in characteristic zero. In the dual complex set

    J=im(F₁*→F₂*), K=ker(F₁*→F₂*), C=im(F₀*→F₁*).

There are exact sequences

    0→J→F₂*→Q→0,
    0→K→F₁*→J→0,
    0→C→K→A_M→0,
    0→M*→F₀*→C→0.

Finite-length modules N satisfy Ext^j_R(N,R)=0 for j≠4. Dimension shifting in the first two sequences gives Ext¹(K,R)=0 and Ext²(K,R)=D(Q). The third sequence then gives Ext²(C,R)≅D(Q), and the fourth gives

    Ext¹_R(M*,R)≅D(Q).

All constructions are equivariant. The assumed equivariant self-duality identifies the left side with A_M. Hence A_M≅A, with no extra character. No rank argument occurs in this proof.

Dualizing a minimal length-four resolution of a finite-length module reverses its generator representations, giving

    Tor_i^R(D(N),k)≅Tor_{4−i}^R(N,k)*.         (1)

The duality D here is Ext⁴(-,R), so its canonical-character factor is already included. For example D(k)=k⊗(det(m/m²))*; one must not add this character again to (1). In particular μ(A)=β₄(Q) and V*≅Tor₃(Q,k).

## 2. The precise Tor-cokernel budget

Write b_i=β_i(Q). Minimality gives rank F₂=b₀. The cover F₁*→J has b₁ minimal columns and u additional columns for some u≥0. Ordinary invertible column operations split off these redundant columns, so numerically

    rank F₁=b₁+u,
    rank F₀=r+b₁+u−b₀,
    μ(K)=b₂+u.

This uses no equivariant splitting of the redundant summands. The first two exact sequences above give a natural equivariant isomorphism Tor₁(K,k)≅Tor₃(Q,k)≅V*. The Tor sequence of 0→C→K→A→0 has the exact segment

    V*→V→C/mC→K/mK→A/mA→0.

Let T be the cokernel of its first arrow. Then there is an exact sequence

    0→T→C/mC→K/mK→A/mA→0.                    (2)

Consequently, with t=dim T,

    μ(C)=t+b₂+u−b₄.

Since F₀* surjects onto C, μ(C)≤r+b₁+u−b₀. Thus

    t≤r+b₁−b₀−b₂+b₄
     =r−b₃+2b₄=r−d,                         (3)

using the finite-length Euler identity b₀−b₁+b₂−b₃+b₄=0. This proves the exact budget rather than only its equality case.

## 3. The representation bound and testable certificates

Semisimplicity makes an equivariant map V*→V a collection of maps between multiplicity spaces for each irreducible ρ. Its ρ-isotypic rank cannot exceed min(m_ρ(V*),m_ρ(V)). Its cokernel therefore contains at least max(m_ρ(V)−m_ρ(V*),0) copies of ρ. Summing gives dim T≥a_H(V), and (3) proves (T).

This lower bound is the exact minimum cokernel dimension among all H-equivariant linear maps V*→V: take maximum-rank maps in every multiplicity block. The actual Tor map may obey additional constraints, so equality in this minimum does not establish realizability.

The second expression for a_H follows because dim V=dim V*, making total positive weighted imbalance equal total negative weighted imbalance.

Several consequences permit certificates without a full H-decomposition:

1. For every subgroup L⊂H,

       r≥d+a_L(V|L).

   Indeed the same Tor map is L-equivariant. In particular a_L(V|L)≤a_H(V), as is also clear by comparing the two minimum-cokernel optimization problems.

2. For an element h of finite order, let n_λ be the multiplicity of its eigenvalue λ on V. Then

       r≥d+(1/2)Σ_λ |n_λ−n_{λ⁻¹}|.

   This is the subgroup test for L=⟨h⟩. Only abstract eigenvalue multiplicities are involved.

3. A weaker character-only certificate is

       r≥d+(1/2)|χ_V(h)−χ_V(h⁻¹)|.

   To prove it, subtract the paired eigenvalue sums and apply the triangle inequality and |λ|=1. Integer rounding of the right side is allowed. A subgroup with several commuting generators can be substantially stronger than every individual element test.

## 4. A strict strengthening for a whole abstract family

Use the canonical abstract stabilizer and cotangent representation from ../wedge-defect-equivariant-obstruction/PROOF.md:

    H=μ₅×(B⋊C₄),  B≅C₅²,
    W|B has weights (i,i²/2), i∈F₅×.

Let P=W⊕Λ²W with multiplication x·v=x∧v and x·s=0. This is a finite-length module of length ten. The established abstract Koszul calculation gives

    μ(P)=4,   Tor₁(P,k)≅Sym²W,   dim Tor₁(P,k)=10.

For arbitrary H-characters χ₁,…,χ_n, n≥1, consider the finite-length module

    Q=⊕_{j=1}^n (D(P)⊗χ_j).

Then A=D(Q)=⊕_j(P⊗χ_j⁻¹), so s=4n, dim V=10n, and d=2n. Every H-character restricts trivially to B, by the conjugation relations gZg⁻¹=Z³ and gDg⁻¹=D⁴. Thus V|B consists of n copies of Sym²W|B.

Its ten weights, with multiplicities, are

    S={(a,4a²):a≠0} ∪ {(a,0):a≠0} ∪ {(0,1),(0,4)}.

The dual weight multiset is

    −S={(a,a²):a≠0} ∪ {(a,0):a≠0} ∪ {(0,1),(0,4)}.

The first four weights in the respective displays are disjoint, while the remaining six agree. Therefore

    a_B(V|B)=4n.

The theorem proves the necessary rank bound

    r≥6n.                                                   (4)

The scalar generator inequality alone gave only r≥2n. The previous equality-case test ruled out r=2n; (4) additionally rules out every self-dual rank 2n<r<6n for this entire family, irrespective of the character twists. In particular a single character-twisted wedge defect cannot be the isolated Ext² defect of an equivariantly self-dual reflexive module of rank 3, 4, or 5, as well as rank 2. This is strictly more than an equality-case restatement. The bound r≥6n is necessary; no module of rank 6n is asserted to realize it.

Imbalances can cancel for other families: a_H(V⊕V*)=0. Thus this argument does not justify adding individual a_H values for arbitrary different summands. The additivity used above is valid because all the restrictions to B have identical imbalance direction.

## 5. Mixed wedge and residue-field families

One can also include arbitrary character-twisted residue fields. For nonnegative integers n,m with n+m>0, set

    Q=(⊕_{j=1}^n D(P)⊗χ_j) ⊕ (⊕_{j=1}^m k⊗ψ_j),

where all χ_j and ψ_j are H-characters. Each residue-field summand has (β₃,β₄)=(4,1), so d=2(n+m).

The determinant of W restricts trivially to B, since its four weights sum to (0,0). Since every ψ_j|B is trivial and D(k)=k⊗(det W)*, each residue-field summand contributes W|B to V|B. The weights of W are (a,3a²), a≠0; those of W* are (a,2a²), a≠0. These two four-element sets are disjoint from each other and from the wedge imbalance sets (a,4a²) and (a,a²), and from the common six wedge weights. Thus there is no cancellation between the two kinds of imbalance:

    a_B(V|B)=4(n+m).

Consequently every equivariantly self-dual isolated realization must have

    r≥6(n+m).

This includes pure residue-field families (n=0) and mixed families. The computation is entirely representation-theoretic and does not assert that any permitted rank is attained.

## Scope and dependencies

The universal theorem is independent of the canonical stabilizer application. Its only hypotheses are four-dimensional regular local algebra, finite semisimple symmetry, punctured-spectrum freeness, reflexivity, and equivariant self-duality. For a nontrivial determinant rank-two module the self-duality hypothesis must be replaced by a correctly twisted version; it cannot silently be dropped.

The application uses only the established abstract wedge-module Betti calculation and stabilizer weights in ../wedge-defect-equivariant-obstruction/PROOF.md. The generator setup is also recorded in ../length-five-local-defect/PROOF.md, and the rank-independent isolated duality in ../rank-eight-isolated-singularity/PROOF.md §1.

This does not improve any global numerical defect-length bound, classify other length-ten modules, or evaluate any actual defect. All calculations are universal algebra and representations. No physical source-model matrix, operation, input, rank instance, jet, or residue was evaluated. 
