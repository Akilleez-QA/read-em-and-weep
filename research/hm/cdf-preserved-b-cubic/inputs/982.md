# A two-dimensional internal cubic gate for the original fourth Bockstein

## Statement and exact scope

Work over C, with G=A5 acting on the even binary forms A=Sym²W and D=Sym⁴W. Put X=P(A). Assume an actual source126 Type II occurrence whose entire two-dimensional radical J is compatible with the invariant quadratic Q. This is a conditional hypothesis, not an existence assertion.

The actual annihilator complex S has a well-defined internal third symbol

    r:D⊗O_X(−3)→E,
    0→A⊗O_X(−1) --a multiplication-->D⊗O_X→E→0.       (1)

It belongs to a canonical **two-dimensional** subspace of the three-dimensional equivariant Hom space. Moreover r is nonzero if and only if the original fourth Bockstein on its generic surviving D kernel is nonzero. Neither alternative is selected here. This identifies a finite-dimensional internal cubic gate; it does not prove generic surjectivity or remove any source or catalogue pair.

Immutable inputs (exact copies and hashes in INPUTS.json):

- [PR979](https://github.com/Akilleez-QA/read-em-and-weep/blob/db4c20c05f18d5e2494d99eb4c359828446919c9/research/hm/source126-typeII-internal-second/PROOF.md): the internal second symbol vanishes under these hypotheses. It retains the original third-vanishing and original-second generic-rank3 inputs. Those older results are not new conclusions of this packet.
- [PR973](https://github.com/Akilleez-QA/read-em-and-weep/blob/f48c517d776b7f82ee1f96787da722223431a565/research/hm/source126-typeII-radical-naturality/PROOF.md): the actual sequence S→M→T, radical chain maps, internal first multiplication channel and original second-symbol factorization.
- [PR966](https://github.com/Akilleez-QA/read-em-and-weep/blob/4d0a6713a9c81fe669967e1d23838bdc8f4162b6/research/hm/source2-pureV-quadratic-discriminant/PROOF.md): the universal quotient multiplication family, its rank4 locus, and the nonzero Wronskian of the sextic V subsystem. PR973 transfers this family to T without importing a source2 occurrence.

## 1. Global construction and independence of the cubic symbol

At Q,

    H⁰(S)=H⁰(M)=A+D, H¹(S)=D,
    H⁰(T)=D, H¹(M)=H¹(T)=P.

The connecting δ:H⁰(T)→H¹(S) and projection η:H¹(M)→H¹(T) are isomorphisms; fix δ([x̄])=[Qx]. Normalize the nonzero internal first A scalar so that b_S,a(k,h)=a k. The actual negative perturbation is written T_a and is linear in a.

Choose a fixed G-equivariant right inverse H of Q_S on its image. For h in the surviving D kernel let

    u₁⁰(a,h)=−H T_a h.

It is linear in a and satisfies Q_S u₁⁰=−T_a h. Its second residual [T_a u₁⁰] in H¹(S)=D is quadratic. PR979 says its projection to E is zero. Since multiplication A⊗O(−1)→D⊗O is an injective subbundle map, this residual factors uniquely and globally as a·k₁(a,h), with k₁ linear in a and valued in A. This is a sheaf factorization, not pointwise division by a chosen coefficient: the factor map is D⊗O(−2)→A⊗O(−1), so its entries are global linear polynomials. It is equivariant by uniqueness.

Set u₁=u₁⁰−k₁, interpreting A as its actual kernel summand. Then

    Q_S u₁=−T_a h,  [T_a u₁]=0 in H¹(S).

A second S-valued correction exists globally:

    u₂=−H T_a u₁,  Q_S u₂=−T_a u₁.

It is quadratic in a. The class of T_a u₂ modulo aA defines the cubic map r in (1).

Here is the choice check. Two normalized u₁ choices differ by a ker Q_S-valued linear polynomial. Their residuals both vanish in H¹(S), so the A component of their difference has zero multiplication by a and is therefore zero. Their difference is D-valued. The resulting change in the third class is the internal second symbol applied to that D-valued difference, modulo aA, and is zero by PR979. Changing u₂ by a kernel-valued quadratic polynomial changes the third residual only by the first image aA. Thus r is independent of all lift choices. This also proves its global regularity and G-equivariance, rather than assuming a spectral-sequence class automatically globalizes.

## 2. The quotient kernel and third-order radical naturality

By PR973 the quotient first family is the nonzero multiplication channel

    b_T:D⊗O(−1)→P⊗O,  h↦[a h] in Sym⁶W/V₆.

Its kernel is κ:O(−5)→D⊗O(−1), as in PR979. Every radical j gives a chain map T→S for the whole perturbed family; j¹:P→D is zero and some j⁰:D→D is a nonzero scalar.

On the dense open where b_T has rank4, the quotient first cokernel is zero. Hence its first kernel survives to the next two pages, with zero second and third target. Equivalently, after cancelling the Q-contractible pairs, the quotient differential is t times a matrix whose leading coefficient is onto; its first kernel admits corrections through every prescribed finite order by this surjectivity. Applying j and using the first and second internal vanishings gives third-differential naturality

    r ∘ κ(−2)=0:O(−7)→E.                             (2)

The possible lift changes are precisely those handled in Section1. Both sides extend as bundle maps on X, so equality on that dense open proves (2) globally, even over the ten exceptional quotient directions. No assumption that quotient kernel formation commutes with specialization is used.

## 3. Exactly two equivariant cubic parameters remain

The A5 character recurrence and exact sequence (1) give

    dim Hom_G(D⊗O(−3),E)=3,
    dim H⁰(E(7))^G=1.                                 (3)

Explicitly, with class sizes(1,15,20,12,12), characters

    χ_A=(3,−1,0,φ,1−φ), χ_D=(5,1,−1,0,0),

and h_n=χ_SymⁿA, use

    h_n=χ_A h_(n−1)−χ_A h_(n−2)+h_(n−3),
    χ_H⁰(E(n))=χ_D h_n−χ_A h_(n−1).

These are exact character identities; the accompanying checker verifies (3). In particular the second number is one, not two.

We show that restriction along κ(−2) is nonzero. Let Δ be the invariant quadratic discriminant on A and let

    ρ(a)h={a,h}₁=a_x h_y−a_y h_x

be the first binary transvectant. With π:D⊗O→E, the cubic map

    f_a=Δ(a) π_a ρ(a)                                  (4)

is equivariant. It suffices to show πρ κ is not the zero map. Although Δ vanishes on the square conic, multiplication by its nonzero polynomial cannot kill a nonzero bundle map on the integral X.

Take a **general**, unselected square a=ℓ², and let p be the zero of ℓ on P(W). The V₆ linear series is basepoint-free and immersive by PR966. Its Wronskian is a nonzero section of O_P¹(12). Outside its finite zero divisor the vanishing sequence is exactly(0,1,2). Consequently the unique nonzero V₆ section v vanishing on2p has order exactly2 there. The quotient kernel at a is generated by h=v/ℓ², so h is not divisible by ℓ.

The following computation is universal and does not choose an actual HM direction. In coordinates with ℓ=x, write h=Σ_(i=0)^4 h_i x^(4−i)y^i, with h₄≠0. Then

    ρ(x²)h=2x h_y ≡8h₄ xy³ modulo x²Sym²W.

It is nonzero in E_[x²]. Therefore πρ κ is nonzero, and so is its product by Δ in (4). This proves that the restriction map

    Hom_G(D⊗O(−3),E)→H⁰(E(7))^G

has rank one. Its kernel, which contains the actual r by (2), has dimension exactly two. This is a canonical linear subspace independent of normalizations of κ, Δ, or the irreducible identifications. It does not assert that every vector in that space is realized by the actual complex.

## 4. Every nonzero equivariant cubic map is generically onto

Let f:D⊗O(−3)→E be nonzero. Suppose it has generic rank one. Saturate its image. The quotient in E is torsion-free, so the depth lemma on the smooth surface shows that the saturated image is a reflexive rank-one sheaf, hence O(k). It is G-stable, and A5 has no character ambiguity in its linearization.

The nonzero injection O(k)→E requires k≤1 because H⁰(E(−2)) and all more negative twists vanish by (1). The source factor requires k≥−3 and D occurring in Sym^(k+3)A. For k=−3,−2,−1,0,1 these multiplicities are

    0,0,1,0,2.

Thus only k=−1 or k=1 remains. The first would require a nonzero invariant section of E(1), but H⁰(E(1))^G=0 by the character formula. The second would require H⁰(E(−1))≠0, whereas twisting (1) by−1 and using H¹(O(−2))=0 gives H⁰(E(−1))=0. Both alternatives are impossible. Thus any nonzero f, including any nonzero actual r, has generic rank two.

## 5. Exact comparison with the original fourth Bockstein

Use the normalized S corrections u₁,u₂ of Section1. They are also first and second corrections in M. The third residual T_a u₂ lies in S¹. Since H¹(S)→H¹(M) is zero, choose v₃∈M⁰ with

    Q_M v₃=−T_a u₂.

Its image v̄₃ is a quotient Q_T-cycle, and

    δ([v̄₃])=−[T_a u₂] in H¹(S).

The original first and third differentials are zero, while the original second image is b_T δ⁻¹(aA), by the retained inputs. Projection to H¹(T) consequently gives

    η β₄,M,a(h)=− b̄_T,a δ⁻¹ r_a(h),                  (5)

where b̄_T is the map induced after quotienting by the original second image. A change in u₂ by a kernel correction contributes only that second image after applying the connecting comparison; changes arising from u₁ are removed by the vanishing lower differentials. More concretely, the displayed normalized corrections are an allowed representative of the actual original fourth differential, so (5) is its value in the correct page target, not a newly defined symbol of the same dimensions.

The grading in (5) is r:D O(−3)→E followed, after twisting by−1, by b̄_T:E(−1)→cokerβ₂,M. Both sides have degree four. The assertion is needed only on the dense open where the original second has rank3 and b_T has rank4. There its domain is exactly the original surviving D; specialized additional A kernels at the six axes are not asserted to have been computed.

For an independent correction-term check, cancel the Q-contractible pairs while preserving S→M→T. The reduced matrix has upper triangular form [[s(t),δ(t)],[0,q(t)]], with δ₀ invertible. After the Section1 domain normalization, s₁|D=s₂|D=0 and s₃|D represents r. In the original Schur complement −q(t)δ(t)⁻¹s(t), the quartic D coefficient is therefore exactly −q₁δ₀⁻¹s₃. Terms containing q₂, δ₁, or δ₂ multiply s₁ or s₂ and vanish. Quotient by the original quadratic A image is precisely the quotient in (5).

On the dense open in question, b̄_T:E→cokerβ₂ has rank one and a one-dimensional kernel. Therefore (5) and Section4 show

    r=0  ⇔  the generic original fourth Bockstein is zero.    (6)

Indeed if the composition is zero, r has generic rank at most one and must vanish; if r is nonzero, it is generically onto E, so composition with b̄_T is nonzero. This is an equivalence, not a nonvanishing assertion.

## 6. What has and has not advanced

The actual full-J Type II fourth-order question is now represented by a canonical two-dimensional space of internal cubic maps, with zero versus nonzero faithfully detected by the original fourth Bockstein. The construction and comparison are new; the original third vanishing and the six-axis original-second results remain imported facts.

The two-dimensional parameter space is not a probability, an exhaustive count of all global proof approaches, or proof that any nonzero member is realized. No actual coefficient is selected, no later obstruction is evaluated, no four-pair frontier is decremented, and no complete repair is claimed.

## Reproduction

Run `python verify.py` and `python -O verify.py`. The exact checker authenticates the three public inputs, computes character dimensions and possible rank-one factors, verifies the universal square transvectant residue, and checks all terms of the formal quartic Schur expansion. A synthetic complex also verifies normalized lifting and the fourth-symbol sign. These tests support, rather than replace, the actual-complex and sheaf arguments above.
