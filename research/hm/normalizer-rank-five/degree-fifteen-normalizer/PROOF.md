# The HM normalizer allows a two-dimensional space of degree-fifteen invariants

## Result and implication for the outer determinant

Let H=H5 be the order-125 Heisenberg group in its faithful five-dimensional Schrödinger representation V, and let

    N=H⋊SL2(F5) ⊂ SL(V)

be its full classical Horrocks–Mumford normalizer. Then

    dim (Sym^15 V*)^N = 2.

More precisely, for Q=(Sym^15 V*)^H, the +1 eigenspace Q+ of the central involution c=−I in SL2(F5) is an A5-representation with character

    class:       1       2       3       5A      5B
    class size:  1      15      20       12      12
    character:  96      −4       3        1       1.

Consequently, the full normalizer does NOT give the degree-fifteen analogue of the quintic exclusion. If the operation f and its target J carry a genuine N-equivariant structure, the determinant δ constructed in outer-boundary-determinant/PROOF.md belongs, after trivializing its constant determinant factor, to this two-dimensional invariant space. Symmetry alone therefore permits a nonzero δ; it neither proves δ≢0 nor proves δ=0 for the actual operation. Nonemptiness of Ω remains unresolved by this argument.

The calculation below uses only abstract finite-group characters, Heisenberg conjugation, and small generating-function coefficient identities. No actual operation/source matrix, operation value, chosen input, rank witness, polynomial instance, jet, or residue is evaluated.

## 1. Basic character identities

Put S=Sym^15 V*. The central fifth roots act trivially on S. Every noncentral element of H has the five distinct fifth roots as eigenvalues on V*; hence its symmetric-power character generating function is 1/(1−s^5), and its trace on S is one. Since dim S=binom(19,4)=3876,

    dim Q = (5·3876+120)/125 = 156.                    (1)

For a∈SL2(F5), the projector onto H-invariants gives

    tr(a|Q) = (1/125) Σ_(h∈H) tr(ha|S).               (2)

If a has no eigenvalue one on W=H/Z(H)≅F5², each ha is conjugate by H to za for some central z. Indeed, the required conjugation equation modulo the center is solvable because I−a is invertible. Since z acts trivially on S, (2) becomes

    tr(a|Q)=tr(a|S).                                  (3)

Also End(V), under conjugation by H, is the sum of 25 distinct character lines indexed by W. When a has no fixed nonzero vector on W, only the identity line contributes to its trace. Thus

    |tr(a|V)|² = tr(a|End(V)) = 1.                    (4)

These observations are the same abstract tools as in ../quintic-normalizer-exclusion/PROOF.md.

## 2. The central involution and order-four lifts

The lift c=−I has order two. By (4), its trace on V is ±1. Because c∈SL(V), the number of negative eigenvalues is even, so its spectrum is (+1)^3(−1)^2. The same holds on V*. Consequently

    tr(c|Q) = [s^15] 1/((1−s)^3(1+s)^2)
            = [s^15] 1/((1−s)(1−s²)^2)
            = Σ_(j=0)^7 (j+1) = 36.

Therefore dim Q+=(156+36)/2=96. Only Q+ can contain N/H-invariants, and its action factors through SL2(F5)/{±I}≅A5.

Let a have order four in SL2(F5), so a²=c. Such an a is conjugate to its inverse. The spectrum argument from the quintic proof, using (4) and determinant one, gives

    Spec(a|V*)={1,−1,−1,i,−i}.

Hence

    tr(a|Q) = [s^15] 1/((1−s)(1+s)^2(1+s²))
             = [s^15] 1/((1+s)(1−s^4)) = −4.

Since ca=a^−1 is conjugate to a, tr(ca|Q)=−4 as well. Projection to Q+ gives

    tr(a|Q+)=(tr(a|Q)+tr(ca|Q))/2=−4.                 (5)

This is the trace on the A5 involution class.

## 3. Order-three and order-six lifts

Let b have order three in SL2(F5), and let ω be a primitive cube root. The elements b and b^−1 are conjugate, with a conjugating element that commutes with c because c is central. The multiplicities of ω and ω² on V are equal. If these multiplicities are B, then the multiplicity of 1 is 5−2B and the trace is 5−3B. Equation (4) forces B=2. Thus

    Spec(b|V*)={1,ω,ω,ω²,ω²}.

The c-positive and c-negative spaces of V have dimensions three and two. Conjugacy to b^−1 preserves both spaces, so within each of them the ω- and ω²-multiplicities agree. The displayed total spectrum forces the c-positive spectrum {1,ω,ω²} and the c-negative spectrum {ω,ω²}. Therefore

    Spec(cb|V*)={1,ω,ω²,−ω,−ω²}.

Both b and cb have no eigenvalue one on W, so (3) applies to both. Their generating functions yield

    tr(b|Q) = [s^15] (1−s)/(1−s³)^2 = 6,

    tr(cb|Q) = [s^15] 1/((1−s)(1+s+s²)(1−s+s²))
              = [s^15] (1+s)/(1−s^6) = 0.

Thus

    tr(b|Q+)=(6+0)/2=3.                              (6)

## 4. Unipotent spectra without operation matrices

We now treat an order-five element u of the quotient, which is a nontrivial unipotent on W. The fixed line F=ker(I−u) is also im(I−u).

Use the standard symplectic realization of H with its central extension W and a symplectically equivariant choice of Heisenberg lifts. This is the usual construction of the HM normalizer: the quotient acts on the W-coordinate and fixes the center. Choosing this realization imposes no condition on the operation f. The quotient action on H-invariants is independent of the representatives chosen in N.

Choose a generator y over F and a complementary Heisenberg generator x. For a primitive fifth root ζ, restriction of the Schrödinger representation to ⟨y,Z(H)⟩ decomposes V into five one-dimensional y-eigenspaces indexed by t∈F5, with eigenvalues ζ^t. The element x cyclically carries these five lines to one another. Since u fixes y, it acts by a scalar λ_t on each such line.

The abstract conjugation relation has the form

    uxu^−1 = ζ^β x y^k,     k≠0.

It follows, allowing a harmless change of sign in k according to the indexing convention, that

    λ_(t+1)/λ_t = ζ^(β+kt).

Thus λ_t=λ_0 ζ^(r t²+q t) for some r≠0. In the symplectic realization c takes the t-line to the −t-line and commutes with u. Hence λ_t=λ_(−t), forcing q=0. We obtain the eigenvalue multiset

    Spec(u|V)=λ{1,ζ^r,ζ^r,ζ^−r,ζ^−r},    r≠0.       (7)

The factor λ satisfies λ^5=1 because det u=1. This factor has no effect on Sym^15. Passing to V* replaces λ and ζ by inverses, which leaves the arguments below unchanged.

On each pair of lines indexed by t and −t, c has one +1 and one −1 eigenvalue. Its eigenvalue on the remaining t=0 line is +1 because tr(c|V)=1. Thus, again up to a scalar fifth root irrelevant in degree fifteen,

    Spec(cu|V*)={1,η,−η,η^−1,−η^−1},               (8)

where η is a primitive fifth root. The two conjugacy classes of order-five elements in A5 correspond to the two square classes of r; the next identities apply to every nonzero r.

## 5. The two degree-fifteen unipotent trace identities

For any primitive fifth root η, define

    T=[s^15] 1/((1−s)(1−ηs)^2(1−η^−1s)^2).

Since the five fifth roots are 1,η,η^−1,η²,η^−2, the generating function equals

    (1−s)(1−η²s)^2(1−η^−2s)^2/(1−s^5)^2.

Its numerator has degree five, constant coefficient 1 and leading coefficient −1. At degree fifteen, only numerator degrees zero and five can contribute. Therefore

    T=4−3=1.                                         (9)

Likewise set

    U=[s^15] 1/((1−s)(1−η²s²)(1−η^−2s²)).

Using 1/(1−s)=(1+s)/(1−s²) and then setting x=s² gives

    U=[x^7] 1/((1−x)(1−η²x)(1−η^−2x))
      =[x^7] (1−ηx)(1−η^−1x)/(1−x^5)
      =1.                                            (10)

Equations (7)–(10) prove tr(u|S)=1 and tr(cu|S)=1. This alone is not yet the trace of u on Q, because I−u is singular. The coset average is handled next.

## 6. The missing unipotent-coset average

Of the 125 elements h∈H, exactly 25 have image in F⊂W. If h lies over F, its image belongs to im(I−u), so hu is H-conjugate to zu for some central z. Its trace on S is therefore T=1.

If h lies outside F, choose a nonzero Heisenberg element y over F. It commutes with u, while its commutator with h is a nontrivial central fifth root. Consequently conjugation by y carries hu to ζ^j hu for some j≠0. The eigenvalue multiset of hu on V* is invariant under multiplication by the primitive fifth root ζ^j. As it has exactly five eigenvalues, it must consist of

    {λ,λζ,λζ²,λζ³,λζ^4}.

Its determinant is one, hence λ^5=1. Thus these are exactly the five fifth roots, and the generating function on symmetric powers is 1/(1−s^5). In particular its trace on S is again one.

Substituting all 125 traces in (2),

    tr(u|Q)=(25·T+100·1)/125=(T+4)/5=1.             (11)

On the other hand, cu acts on W with sole eigenvalue −1, so I−cu is invertible. Equation (3) and (10) give

    tr(cu|Q)=tr(cu|S)=1.

Therefore both order-five classes of A5 have trace

    tr(u|Q+)=(1+1)/2=1.                              (12)

## 7. Averaging and the determinant conclusion

The class sizes of A5 are 1,15,20,12,12. Combining (1), (5), (6), and (12),

    dim (Sym^15 V*)^N
      = dim (Q+)^A5
      = (96+15(−4)+20·3+12·1+12·1)/60
      = 120/60 = 2.

As a consistency check, the A5-character decomposes as

    Q+ ≅ 2·1 ⊕ 6·3 ⊕ 6·3′ ⊕ 7·4 ⊕ 6·5.

This last decomposition is optional; the averaging calculation does not require an irreducible character table.

Now assume genuine N-equivariance of the stipulated operation and its target J. The construction of κ and the quotient bundle C in the outer-boundary proof is natural in V, so Φ:C→J⊗O is N-equivariant. Taking determinants gives an invariant section of

    O(15) ⊗ det J ⊗ (det V)^−9.

The group N is perfect, as proved in the quintic-normalizer argument. Therefore its one-dimensional determinant representation det J is trivial; det V is already trivial since N⊂SL(V). Choosing nonzero trivializations identifies δ with an element of (Sym^15 V*)^N. A different trivialization rescales δ and does not alter its zero scheme.

Hence, if δ is nonzero, its hypersurface is a member of the projective pencil P((Sym^15 V*)^N)≅P¹. The dimension-two calculation shows that equivariant degree-fifteen scalar sections exist, so the representation-theoretic obstruction used at degree five is unavailable here. It does not show that the particular nonlinear determinant construction hits a nonzero member of that pencil. That question requires additional information about the actual equivariant operation or another structural argument.

## Sources and scope

The group, its symplectic Heisenberg realization, and the splitting of the normalizer are established in G. Horrocks and D. Mumford, “A rank 2 vector bundle on P4 with 15,000 symmetries,” Topology 12 (1973), §1, pp. 64–67. The same paper identifies the H-invariant quintic representation in §3, Theorem 3.5. Primary-source PDF:

https://www.dam.brown.edu/people/mumford/alg_geom/papers/1973a--Rk2BdleP%5E4-NC.pdf

For an independent literature context, Y.-H. He and J. McKay, “Sporadic and Exceptional,” §4.2, equation (4.15), gives the full normalizer Molien series. The proof here does not depend on deciphering or expanding that compressed formula:

https://arxiv.org/pdf/1505.06742

The determinant construction and its exact equivariance prerequisites are imported from outer-boundary-determinant/PROOF.md; the perfection and degree-five exclusion are in ../quintic-normalizer-exclusion/PROOF.md. The present result is solely a degree-fifteen symmetry calculation and its conditional implication. It leaves δ≢0 and Ω≠∅ open.
