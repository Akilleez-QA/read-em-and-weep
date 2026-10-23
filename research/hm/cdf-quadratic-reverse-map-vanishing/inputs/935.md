# The actual second Bockstein forces scalar invariant-product compatibility

## Theorem and scope

Assume an actual source127 c-d-f occurrence, with the simultaneous fixed-variable negative-pencil identification of PR924. Let C_N be the full represented algebra of its fixed negative pencil. Let Q:N2→N4 be multiplication by the canonical invariant positive-coordinate quadric q0. Then

    D_Q={e in C_N : e4 Q=Q e2}=C·1.

Consequently the algebra compatible with the aggregate positive-coordinate action q+ is also C·1. The only residual C² alternative in PR929 is impossible. This excludes an endomorphism-compatibility branch, NOT the c-d-f source or any source-dual pair.

The decisive extra input is the already proved NONZERO actual second Bockstein on the unique A summand of ker Q. A compatible surviving idempotent would place that A inside a block on which Q is onto and every negative quadratic preserves the block. Such a block has unobstructed formal kernel lifting, forcing that second Bockstein to vanish. The contradiction is structural. No selected actual coefficient, parameter, point, derivative, matrix, rank or large computation is used.

## 1. Authenticated immutable interface

The exact originals and Git blob identifiers are recorded in audit-inputs/manifest.json. All are in Akilleez-QA/read-em-and-weep.

1. PR924 at c6c25eaf0e5a67c27eee7c3ba4f000df55997692, research/hm/profile11-source127-cdf-pencil-algebra/PROOF.md, blob 83f5aee293995257459229e6b323522224ce8f3d. This gives the actual represented algebra, including singular elements, and its simultaneous compatibility with both negative arrows.
2. PR925 at 2be52725fe471efdc64d74bd87702b581f9f6a48, research/hm/profile11-source127-cdf-positive-generation/PROOF.md, blob becd3300950c2379d1f03294863d8335a83a1087. Its degree-zero generation argument proves the actual identity N4=im q+ + im q−.
3. PR929 at ad998827320a2302418730102cd2421943935784, research/hm/profile11-source127-cdf-invariant-branch/PROOF.md, blob 49a0b5ef9f6b2fa6fb5e46edd28fec4f4d73be79. This imports the geometric invariant-product theorem and proves the constituent bottleneck and surviving block characters used below.
4. PR933 at 804661fb49e245a8df884937bb8d38fb5d0dc17a, research/hm/positive-double-line/PROOF.md, blob a428ac4b4b8cb6b67b7b8e3b1625352468adeb05. It proves equality of actual embedded images im q+=im Q, not merely a character identity.
5. POSITIVE-FIRST-BOCKSTEIN-VANISHES-BY-CYCLIC-RAO.md at eeb1a11799ca38a60c37f6ba96f263ef8e20dd1c, blob fe4410bbba05060545b22ac6bc80aac8e7c62ce4. Its exact scope is every negative quadratic a in A=Sym²W and the two-term pencil q0+t a on H¹(B(2))_+→H¹(B(4))_+. It proves that the whole first Bockstein is zero and defines the canonical second one on the original kernel.
6. ACTUAL-SECOND-BOCKSTEIN-NONZERO-BY-ATIYAH-QUINTIC.md at 6c724c3b74e2ae4d6992d8c7b99b41c0715d69c0, blob 21c7af094d7088f38ab0ee8fc25b01952ea13d11. Its theorem is that the actual second Bockstein for THIS SAME pencil is zero on D and NONZERO on A. It uses the actual Atiyah-orbit map and the forced quintic extension, not a selected HM coefficient or instance calculation. Only nonvanishing is needed here, not any universal-symbol matrix, exceptional-axis geometry or generic-rank statement.

Write X=N2 and Y=N4, and retain PR929's normal-form coordinates:

    X=X_F⊕X_B,  X_F=V+P+2D,  X_B=A+V+2P+2D;
    Y=Y_F⊕Y_B⊕Y_L,
    Y_F=P+D,  Y_B=V+2P+2D,  Y_L=V+P.

Here A,V,P,D have dimensions 3,3,4,5. The algebra has elements e=(a,b,d,w), with w in a one-dimensional radical J, and product

    (a,b,d,w)(a',b',d',w')=(aa',bb',dd',a w'+d'w).

Its X action is diagonal with scalars a,b. Its Y action has scalars a,b,d on Y_F,Y_B,Y_L and one off-diagonal map η_w:Y_L→P⊂Y_F; nonzero w gives a nonzero P map. For every a in A, let T_a:X→Y denote actual multiplication by the negative quadratic a. Every e in C_N intertwines T_a, because it intertwines both negative linear arrows.

The actual invariant theorem is

    ker Q=A+D,  im Q=2V+3P+3D,  coker Q=P.       (1)

## 2. A surjective block cannot support a nonzero Bockstein

Let Q:X→Y and T_a:X→Y be linear maps over C, with T_a linear in an arbitrary parameter a. Suppose U⊂X and Z⊂Y satisfy

    Q(U)=Z,  T_a(U)⊂Z for every a.               (2)

Then every k in ker(Q|U) admits a formal lift in U[[t]] killed by Q+tT_a. In particular every defined successive kernel-to-cokernel obstruction for this two-term pencil vanishes on k.

Choose any linear right inverse s:Z→U of Q|U, and write M_a(t)=Q|U+t T_a|U. The endomorphism M_a(t)s of Z[[t]] equals id_Z+t(T_a|U)s, so is formally invertible. The expression

    k(t)=k−s(M_a(t)s)⁻¹M_a(t)k                 (3)

has constant term k and satisfies M_a(t)k(t)=0. This is a universal formal identity. Neither choosing a value of a nor evaluating any actual map is necessary. A linear section is an existence device, not a new actual datum or a canonical choice.

For the second obstruction alone there is an even shorter proof. The first correction u=−s T_a k belongs to U and satisfies Qu=−T_a k. The next error T_a u belongs to Z⊂im Q, so its class in coker Q is zero. When the global first Bockstein is zero, this class is the canonical second Bockstein, independently of the chosen correction. Thus

    β₂,a|ker(Q|U)=0 for every a.                (4)

## 3. The single invariant product reduces the algebra to two idempotent types

Combining the actual identities from PR925 and PR933 gives

    Y=im Q+im q−.                              (5)

We repeat the relevant algebra argument, rather than apply PR925 to a different map without checking its hypothesis. The set D_Q is a unital subalgebra of C_N. If e in D_Q has e2=λ id_X, then e4=λ on im Q by its defining equation and on im q− by negative-pencil commutation. Equation (5) forces e4=λ id_Y. The faithful represented action above then gives a=b=d=λ and w=0. Hence e=λ·1.

Consequently the algebra map

    D_Q→C²,  (a,b,d,w)↦(a,b)

is injective and contains the diagonal scalar algebra in its image. Its image is therefore either the diagonal or all of C². If D_Q is nonscalar, it contains the unique idempotent with (a,b)=(0,1). The algebra multiplication forces

    d²=d,  dw=w,

so this idempotent is precisely one of

    p_F=(0,1,0,0),   p_B(w)=(0,1,1,w).         (6)

This classification uses only Q compatibility and (5), not compatibility with the entire positive aggregate.

The p_B(w) type is impossible by the same invariant constituent bottleneck as PR929. Its source kernel is X_F and source image X_B; its target kernel is Y_F and target image is the graph-sheared Y_B⊕Y_L. A compatible Q is block diagonal for these decompositions. The V multiplicities in the kernel block are 1→0, and in the image block 1→2. Its image could therefore contain at most one V, whereas (1) gives two. The graph shear is accounted for and does not change these multiplicities.

Only p_F could remain.

## 4. The residual p_F contradicts the actual second symbol

Suppose p_F belongs to D_Q. Its source image is X_B and its target image is Y_B. Since it also belongs to C_N, it intertwines every T_a. Therefore

    Q(X_B)⊂Y_B,  T_a(X_B)⊂Y_B for every a.      (7)

Its complementary Q block is X_F→Y_F⊕Y_L. By equivariance the two maximal image characters are

    F block: V+P+D;
    B block: V+2P+2D.

Their sum is exactly the actual image character 2V+3P+3D in (1). For each irreducible the two block image multiplicities are bounded above by these maxima, so equality of their sum forces each bound to be attained. Consequently

    Q_B:X_B↠Y_B,   ker Q_B=A.                  (8)

This is also PR929's forced residual block footprint, now derived under the single-Q hypothesis. Since X_F has no A and X_B has exactly one A, this kernel is the UNIQUE A-isotypical subspace of X and hence exactly the A summand in the original ker Q. No unidentified copy of A or source normalization can evade this identification.

Apply the lemma of Section 2 with U=X_B, Z=Y_B and the actual negative multiplications T_a. Equations (7)-(8) imply that the actual second Bockstein vanishes on that entire A summand for every a. But input 6 proves that the same A-to-P quadratic family is nonzero. This is a contradiction.

Here is the explicit comparison with the imported normalization. Input 5 writes each original kernel vector as k=hξ and fixes ζ_a by aξ=q0ζ_a. For k in the A summand, h belongs to A. Its first correction for q0+t a is u0=−hζ_a, and its defined second obstruction is −π(a hζ_a)=π T_a u0. The block construction uses u=−s T_a k and has Qu=−T_a k=Qu0. Hence u−u0 belongs to ker Q. Global first-Bockstein vanishing gives π T_a(u−u0)=0. Therefore the exact imported second class equals π T_a u, which is zero because u∈X_B and T_a u∈Y_B⊂im Q. This compares the actual order-two obstruction without choosing a Schur normalization. It is neither a third/fourth gate nor a geometric normal-lifting invariant with a different target.

Thus p_F is impossible as well. Both nonscalar types in (6) have been excluded, so

    D_Q=C·1.                                    (9)

Every q+-compatible negative-pencil endomorphism is Q-compatible because q0 lies in Sym²V. Hence its algebra is contained in D_Q and contains the common scalars. It too is exactly C·1.

## 5. The authenticated quotient factorization and why it is not the decisive new step

For completeness, let I=im Q and let π:Y→P=Y/I be the actual quotient. Input 5 proves precisely

    π T_a(k)=0 for all a∈A and k∈ker Q.         (10)

It does not refer merely to positive-coordinate directions. Therefore the negative-square quotient map factors canonically through X/ker Q, which Q identifies with I:

    A⊗I --ψ--> P,   ψ(a⊗Qx)=π T_a x.          (11)

This is onto by (5). Equation (11) is a direct consequence of already proved first vanishing and image generation. It is useful bookkeeping, but the new exclusion in Section 4 uses the additional nonzero SECOND symbol and cannot be replaced by first-order vanishing alone. In particular a Type F multiplicity-line calculation is unnecessary: Type F itself has now been ruled out, rather than its remaining parameter being selected.

## 6. Contribution and boundaries

PR929 stopped at scalar or residual Type F C² compatibility. PR933 forced the invariant F-source quotient P component but did not eliminate that branch. The nonzero second Bockstein now excludes the residual branch by its forced surjective B block. Combining with actual image generation strengthens the conclusion: the SINGLE canonical invariant product, together with the fixed negative pencil, already has scalar commutant.

This theorem is conditional on actual c-d-f occurrence. Scalar compatibility is entirely consistent with such occurrence. No premise forces a nonscalar idempotent, no complete actual source is constructed or excluded, and no stable label or source-dual frontier changes. The proof does not evaluate a higher Bockstein, establish generic surjectivity of a single quadratic, identify any actual source parameter, or settle lifting or Weil-class algebraicity. The formal lifting lemma is used only inside the hypothesized invariant block to obtain a contradiction.

All imported results retain their original assumptions. The nonzero second symbol is not being re-proved from representation multiplicity one; its actual geometric nonvanishing theorem is essential. No universal-symbol coefficient table or actual selected computation is needed for this argument.
