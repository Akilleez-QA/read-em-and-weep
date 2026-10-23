# The internal second symbol vanishes under full-radical Type II compatibility

## Scope, inputs, and statement

Work over C. Write G for the icosahedral group on even binary forms, A=Sym²W (dimension3), D=Sym⁴W (dimension5), and P for the four-dimensional irreducible. Let X=P(A), with O(−1) the tautological line. All assertions about the actual complexes assume an actual source126 Type II occurrence and compatibility of its **entire** two-dimensional radical J with the invariant quadratic Q. They do not assert that this hypothesis occurs.

The immutable inputs, with exact local copies and hashes in INPUTS.json, are:

1. [PR973](https://github.com/Akilleez-QA/read-em-and-weep/blob/f48c517d776b7f82ee1f96787da722223431a565/research/hm/source126-typeII-radical-naturality/PROOF.md): the actual subcomplex S, original complex M, quotient T, radical chain maps, first-symbol formula, and canonical second-symbol factorization.
2. [PR966](https://github.com/Akilleez-QA/read-em-and-weep/blob/4d0a6713a9c81fe669967e1d23838bdc8f4162b6/research/hm/source2-pureV-quadratic-discriminant/PROOF.md): the universal multiplication D→P has rank4 except at ten reduced directions. PR973 identifies this family with the actual quotient first symbol; no source2 occurrence is imported here.
3. [The existing global third-vanishing theorem](https://github.com/Akilleez-QA/read-em-and-weep/blob/db51525015bb7c5e825833d550d08dedf6f6ea96/research/hm/order-four-quadratic-load/ACTUAL-THIRD-BOCKSTEIN-VANISHES-IDENTICALLY.md): the actual original second symbol has generic rank3 and kernel D, and the original third Bockstein is zero. Its six-axis and square calculations are **imported**, not claimed as new work.

The new conclusion is that the actual **internal second** Bockstein of S is identically zero. Before importing the original third vanishing, naturality confines it to a canonical one-dimensional space of quadratic bundle maps. The third vanishing then kills that remaining alternative. This does not prove full-J existence, remove a catalogue pair, select any later symbol, or complete the original repair.

## 1. Actual first-page bundles and the internal second symbol

At Q the sequence 0→S→M→T→0 has

    H⁰(S)=H⁰(M)=A+D,  H¹(S)=D,
    H⁰(T)=D,  H¹(M)=H¹(T)=P.

The inclusion on H⁰ and projection η on H¹ are isomorphisms. The connecting map δ:H⁰(T)→H¹(S) is an isomorphism, with convention δ([x̄])=[Qx]. PR973 proves that the internal first symbol is

    b_S,a(k,h)=λ a k,  λ≠0,

and its D restriction is zero. Absorb the fixed nonzero λ into the A identification. Its cokernel is the rank-two bundle E defined by

    0→A⊗O(−1) --m--> D⊗O→E→0.                 (1)

The map m is fiberwise multiplication by the nonzero quadratic a and is injective everywhere. The first-page kernel, with degree-one convention, is D⊗O(−1).

Here is an explicit construction of the internal second symbol, including its grading. Choose a fixed G-equivariant right inverse H of Q_S on im Q_S, possible by averaging over the finite group. Represent D⊂ker Q_S by its actual degree-zero cycles. Since the first symbol vanishes on D, T_a h belongs to im Q_S for every a and h∈D. Put

    u(a,h)=−H T_a h,    Q_S u=−T_a h.

Then T_a u is quadratic in a. Its class in H¹(S)=D, modulo the first-symbol image aA, defines

    s:D⊗O(−2)→E.                               (2)

Changing H changes u by a ker Q_S-valued linear polynomial, so changes [T_a u] only by aA. Thus (2) is well-defined and G-equivariant on all X, not merely a rational symbol. This is the second differential on the D first-page kernel after one further O(−1) twist. It is not the original second Bockstein of M.

## 2. Radical naturality leaves one universal quadratic channel

The quotient first family is a nonzero scalar times multiplication

    b_T:D⊗O(−1)→P⊗O,  h↦[a h] in Sym⁶W/V.

By input2 its degeneracy locus is finite. Its kernel is a line bundle: as the kernel of a map of locally free sheaves with torsion-free image on the smooth surface X, it is reflexive, hence locally free of rank one. Determinants off the finite degeneracy locus, followed by unique extension, give

    κ:O(−5)→D⊗O(−1).                           (3)

The G-linearization has no extra character because G=A5 has no nontrivial one-dimensional characters. The original binary center acts trivially throughout.

PR973 gives radical chain maps j:T→S for the entire Q+tT_a family. They have j¹:P→D zero and some j⁰:D→D a nonzero scalar. Naturality of the second differential, restricted to the quotient first kernel (3), therefore gives

    s ∘ κ(−1)=0: O(−6)→E.                      (4)

This can also be checked directly: a quotient first-cycle has a first correction in T; applying j produces an S correction, and its second class is the image under j¹ of the quotient second class, hence zero. The correction ambiguity is exactly the internal first image already divided out in E. Equality on the dense constant-rank open suffices, since both sides of (4) are maps into the vector bundle E.

The representation dimensions are

    dim Hom_G(D⊗O(−2),E)=2,
    dim Hom_G(O(−6),E)=dim H⁰(E(6))^G=1.        (5)

For completeness, on the five A5 conjugacy classes of sizes1,15,20,12,12, the characters of A and D are

    χ_A=(3,−1,0,φ,1−φ),   χ_D=(5,1,−1,0,0),
    φ=(1+sqrt(5))/2.

Let h_n=χ_SymⁿA. Since A has determinant1 and Λ²A≅A,

    h_n=χ_A h_(n−1)−χ_A h_(n−2)+h_(n−3).

From (1) and H¹(O(n))=0 on P²,

    χ_H⁰(E(n))=χ_D h_n−χ_A h_(n−1), n≥0.     (6)

The character inner products in (6) give (5); the checker reproduces them exactly.

The restriction map in (5) is nonzero. Let Δ be the invariant quadratic discriminant on A, and π:D⊗O→E the quotient in (1). The map Δπ belongs to the first space. Generically κ_a is not contained in aA: otherwise the restriction of b_T to aA would have a kernel, contrary to the generic rank3 of the original second symbol and PR973's factorization. Away from Δ=0 as well, (Δπ)κ is nonzero. Consequently the kernel of restriction along κ(−1) has dimension exactly one. The actual s lies in that line, before applying input3's third-vanishing conclusion.

## 3. A rank-one exclusion for quadratic equivariant maps into E

Every nonzero G-equivariant f:D⊗O(−2)→E is generically surjective.

Suppose instead that f has generic rank one. Saturate its image in E and call the saturated sheaf L. Then E/L is torsion-free. At a closed point of the smooth surface, the depth lemma applied to 0→L→E→E/L→0 gives depth L≥2; hence L is reflexive and therefore a line bundle O(k). Equivalently one may first extend the rank-one reflexive hull and its map into E across the finite missing set. The saturation is G-stable, so this line and both factor maps inherit compatible G-linearizations. The canonical linearization of O(k) is the only one, since A5 has no characters.

The nonzero injection O(k)→E requires H⁰(E(−k))≠0. Twisting (1) by −2 gives H⁰(E(−2))=0; the same vanishing holds for every more negative twist. Thus k≤1. The nonzero factor D⊗O(−2)→O(k) requires k≥−2 and D occurring in Sym^(k+2)A. For k=−2,−1,0,1 these multiplicities are respectively0,0,1,0, since

    Sym⁰A=1, Sym¹A=A, Sym²A=1+D,
    Sym³A=A+V+P.

Only k=0 remains. But (1) gives H⁰(E)=D, so H⁰(E)^G=0. An equivariant injection O→E is impossible. This contradiction proves the claim. No stability theorem or numerical slope assumption is used.

## 4. Comparison with the original third differential

We now use the already proved original third vanishing, retaining all correction terms and quotient conventions.

For h∈D choose the S-valued first correction u as in Section1. Then T_a u is an S degree-one vector. Since H¹(S)→H¹(M) is zero, its class in the original cokernel vanishes, and there is a second correction v∈M⁰ with

    Q_M v=−T_a u.

Its quotient v̄ is a Q_T-cycle and

    δ([v̄])=−[T_a u] in H¹(S)=D.

The original third Bockstein at h is [T_a v] modulo the image of the original second differential. Projection to H¹(T)=P therefore gives

    η β₃,M,a(h)=− b̄_T,a δ⁻¹ s_a(h),            (7)

where b̄_T,a is b_T,a followed by quotient by b_T,a δ⁻¹(aA). This is exactly the original second-image quotient by PR973. Changing u by an S kernel vector changes the expression only by that quotient; changing v by an original kernel vector contributes the original first differential, which is zero.

In bundle degrees, s is (2), the map induced by b_T is E(−1)→coker(β₂,M), and (7) composes s(−1) with that map. Thus both sides have parameter degree three. The identification of the two copies of D through δ is fixed and equivariant; by irreducibility it differs from any chosen normalization only by a nonzero scalar.

One can also eliminate the Q-contractible pairs and use the formal block matrix

    [[s(t), δ(t)], [0, q(t)]].

Here s₁|D=0, q₁=b_T and δ₀=δ is invertible. The original Schur complement is −q(t)δ(t)⁻¹s(t). Its cubic coefficient on D is exactly −q₁δ₀⁻¹s₂: terms involving q₂ or δ₁ multiply s₁|D=0. This confirms that (7) hides no higher correction term.

On the dense open where b_T has rank4 and the original second A symbol has rank3, b̄_T has rank one on the rank-two E. Input3 says the left side of (7) is zero. Hence the image of s is generically contained in a line. Section3 says that a nonzero equivariant s would have generic rank two. Therefore

    s=0 on all X.                              (8)

The last extension uses that a morphism of vector bundles vanishing generically is zero. In particular the internal second differential vanishes in every parameter direction, not only away from the ten quotient directions or six original-second axes.

## 5. Consequences and limits

Under full-J Type II compatibility, S has internal first symbol λ·multiplication on A, zero on D, and now **zero internal second symbol on the surviving D**. The first unresolved internal symbol is therefore of order at least three. The two-dimensional universal quadratic Hom space and its one-dimensional naturality kernel remain valid universal statements; the actual member of that kernel is forced to be zero by the original third-vanishing theorem.

This is a new comparison and internal vanishing result, not a new proof of the previously known original third vanishing. It does not select the internal third, original fourth, or eventual generic surjectivity. No actual instance matrix or chosen HM parameter is evaluated.

## Reproduction

Run `python verify.py` and `python -O verify.py`. The bounded exact checker authenticates all three pinned inputs, computes the character dimensions and rank-one obstruction, and checks the second/third correction signs in a synthetic block complex and in a formal Schur-complement expansion. These algebraic checks support, but do not replace, the sheaf and actual-complex comparisons proved above.
