# Two possible splitting types for the actual first-cup kernel

Work over C with G=SL2(F5) and T=P(W*). Write A=Sym2 W, S=Sym3 W, D=Sym4 W, T6=Sym5 W, V=Sym2 W', and P for the even four-dimensional representation. All twists are on the parameter line T with the standard equivariant linearization.

This is a structural classification of possibilities for the actual first-cup kernel K, not an evaluation selecting a case. No actual HM coefficient, point, jet, matrix, derivative or instance rank is chosen.

## 1. Exact input and result

The sole immediate input is PR971 at commit f96962f2219e096821c3dec50712cc0108abea8f in Akilleez-QA/read-em-and-weep, research/hm/forced-secondary-w-extension/PROOF.md, with exact byte identity recorded in INPUTS.json. Its original first-cup and quotient premises are retained. It proves actual equivariant sequences

    0 -> D O(-4) -> K -> P O(2) -> 0,
    0 -> K -> H O -> J O(2) -> 0,                       (1)

where

    H=1+P+2D,       J=A+V,
    rank K=9,      deg K=-12.

In particular K is an actual subbundle of a trivial bundle. Taking sections of the first sequence gives a connecting map

    partial: V+P+D -> A+V+P+D.                         (2)

Its V component is already proved nonzero by the input.

We prove that the P component of (2) is nonzero as well, and that the actual K is equivariantly isomorphic to one of the following two bundles:

    K = T6 O(-1) directsum A O(-2),                    (I)
    K = D O directsum S O(-3).                         (II)

Case I occurs precisely when the D component of (2) is nonzero; case II occurs precisely when that component is zero. The theorem does not select that scalar and does not assert that both alternatives are realized by actual HM bundles. In case II the constant D subbundle is the canonical evaluation image H0(K) O; an arbitrary complementary splitting is not asserted canonical.

## 2. Constant sections really give constant subbundles

Because K is a subbundle of H O, its global sections form a linear subrepresentation H0(K) of H. The evaluation map

    H0(K) O -> K

is fiberwise injective: after composition with K -> H O it is exactly the inclusion of the fixed subspace H0(K) in H at every fiber. Therefore its cokernel is a vector bundle, itself embedded in (H/H0(K)) O.

Consequently all ordinary splitting degrees of K are nonpositive. If H0(K)=0 they are strictly negative. The same conclusions apply to the quotient by its full constant evaluation subbundle.

We use equivariant Birkhoff–Grothendieck splitting. This follows from ordinary splitting and the canonical slope filtration: its ordinary splittings can be averaged over finite G to make them equivariant. A pure-degree summand O(d)^r has the form R tensor O(d) for the representation R=H0(O(-d) tensor O(d)^r). Thus the character computations below identify equivariant multiplicity representations, not only ordinary ranks.

## 3. Exclude the P constant-section possibility

From (1), H0(K) embeds in H0(P O(2))=P tensor A=V+P+D. It also embeds in H=1+P+2D. Hence H0(K) can contain only P and D, each at most once; in particular V is absent, in agreement with the imported V-channel conclusion.

Suppose H0(K) contained P. Section 2 would give a subbundle P O -> K. After twisting by one, its sections P tensor W=W'+T6 would inject into H0(K(1)). But the first sequence of (1), twisted by one, injects H0(K(1)) into

    H0(P O(3))=P tensor S=S+2T6,                    (3)

because H0(D O(-3))=0. This target has no W' constituent, a contradiction. Therefore H0(K) has no P, and

    H0(K)=0 or D.                                  (4)

Equivalently, the P component of the actual connecting map (2) is nonzero and hence an isomorphism on its multiplicity-one P summand. Since its V component is also nonzero, its only undetermined constituent is D. This proves the stated equivalence between the two values in (4) and the D component in (2).

## 4. No constant sections forces the first splitting type

Assume H0(K)=0. All nine ordinary splitting degrees are strictly negative, so

    h0(K(1)) <= 9.                                 (5)

Taking cohomology of (1) after twisting by one gives

    0 -> H0(K(1)) -> S+2T6 -> S+T6 -> H1(K(1)) -> 0. (6)

Here H1(D O(-3))=D tensor W=S+T6 and H1(P O(3))=0. In the representation ring, (6) says

    [H0(K(1))]=[T6]+[H1(K(1))].                    (7)

The last group is a quotient of the multiplicity-free S+T6. Any nonzero possibility has dimension at least four, which would make h0(K(1)) at least 6+4=10, contrary to (5). Therefore

    H1(K(1))=0,       H0(K(1))=T6.                 (8)

Vanishing of H1(K(1)) says that every splitting degree of K is at least -2. Together with strict negativity, rank nine and degree -12, this gives six summands O(-1) and three summands O(-2). The coefficient of the first group is T6 by (8).

In (2), H0(K)=0 implies that every V,P,D source constituent maps injectively, while the target has the additional A. Hence H1(K)=A. Only the O(-2) summands contribute to H1(K), and H1(O(-2)) is the trivial representation. Their multiplicity representation is therefore A. This proves case I.

## 5. A constant D forces the second splitting type

Assume H0(K)=D. Section 2 gives the canonical constant subbundle D O and a quotient K', of rank four and degree -12, embedded in (H/D) O. Its global sections vanish: this follows from the exact sequence and H1(D O)=0, since H0(D O) -> H0(K) is an isomorphism. Thus all splitting degrees of K' are negative.

The sequence

    0 -> D O -> K -> K' -> 0

splits equivariantly. Indeed the ordinary extension group is D tensor H1((K')*), which is zero because the dual splitting degrees of K' are positive. Averaging a splitting makes it G-equivariant. This proves existence of an equivariant direct sum, not uniqueness of a complement.

Equation (3) and the constant summand give

    H0(K(1)) = (D tensor W) + H0(K'(1))
             = S+T6+H0(K'(1))  contained in S+2T6.

Therefore H0(K'(1)) is either zero or a single T6. Since K' has rank four and strictly negative degrees, h0(K'(1))<=4; T6 has dimension six. It follows that H0(K'(1))=0 and all degrees of K' are at most -2.

Twist (1) by two. Since H0(D O(-2))=0, H0(K(2)) embeds in

    P tensor D=A+V+P+2D.

Its constant summand contributes

    D tensor A=A+V+P+D.

Thus H0(K'(2)) is either zero or a single D. Because its degrees are now at most -2, h0(K'(2))<=rank K'=4; D has dimension five. Hence H0(K'(2))=0. All four degrees of K' are at most -3, and their sum is -12, so every one is exactly -3.

Write K'=R4 O(-3). From (6) and H0(K(1))=S+T6, equation (7) gives H1(K(1))=S. On the other hand the constant D contributes no H1 at twist one and H1(O(-2))=1, so H1(K(1))=R4. Therefore R4=S, proving case II.

## 6. Contribution and boundary

The actual embedding into the trivial first-cup source, combined with the newly identified rank-five preimage bundle, excludes the P-zero locus of the residual extension. It then leaves just two full equivariant splitting types for K, rather than merely a two-dimensional Ext space or rank/degree information.

The remaining D-channel scalar distinguishes the types. Neither its value nor the rank of the actual secondary boundary is selected. In both cases the exact square subbundle A O(-6) and its nonsplit extension data remain actual maps; an isomorphism type for K does not split that sequence or replace those maps by arbitrary representatives. No opposite-pencil C splitting, vertex scalar, global odd-quadric section, source pair cut or algebraicity conclusion follows.
