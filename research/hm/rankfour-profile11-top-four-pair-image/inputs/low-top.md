# The actual short rank-four quotient has an ordinary degree at least three

## 1. Conditional statement and source boundary

Work over C on the original physical binary-icosahedral parameter line P(W*), with G=SL2(F5), the fixed determinant identification, and the ACTUAL saturated inclusion

    0 -> E -> H O -> Q -> 0,   dim H=30,
    rank E=17, rank S=13, deg E=deg S=-54, S=Q*.

Suppose the actual second fundamental form has generic rank four and maximal ordered plateau (1,1). Set K=E^-, L=S^-, A_q=E/K and B=S/L. Then ranks K,L,A_q,B are 13,9,4,4. The endpoint derivatives have rank at most three. Let a=deg A_q, b=deg B. The actual transposed derivative maps give coherent sheaf injections

    A_q -> B*(-2),   B -> A_q*(-2),
    t=-8-a-b>=0.

Their images need not be saturated; t is not assumed zero. Only the global bounds top E<=-2 and top S<=-1 are used. The claim is:

    max ordinary degree(A_q) >= 3.                         (T)

Thus every actual maximal rank-four profile (1,1) whose primal quotient has all ordinary degrees at most two is excluded, uniformly over all four actual source types and every determinant defect. This is a structural sublocus exclusion, not a full profile closure, a new global rank bound, or an assertion that any surviving splitting is realized.

The eight complete immutable originals in INPUTS.json are retained with URL, commit, Git blob, byte length and SHA256. The ACTUAL, ambient-Gauss and strict-top inputs at db51525015bb7c5e825833d550d08dedf6f6ea96 provide the actual inclusion and derivative conventions. PR1171 at 8497b6e793f36c14448fecdf88d209971273e069 states the arbitrary-rank plateau construction and ranks, retaining its actual geometric prerequisites. Its separate rank>=4 hypothesis is unnecessary here because rank four is assumed.

PR1123 at 504b7eb800407dfc7e6340c98c72cdd553939f54 supplies the necessary four actual E sources below. PR1140 at 7a2488bcd36d95f79b5198001111b1a31fe5c3ba supplies the actual cubic visibility and kernel alternatives, independently of the derivative rank. PR1182 at ca0f8d4caec9cc07f97d7f719992375483245b55 supplies the coherent-image capacity argument; Section 2 below proves precisely the three-column version used here. No rank-three source ledger, quotient enumeration, profile exclusion, or actual-source transfer from such a ledger is imported.

Write A_std=Sym2 W, S4=Sym3 W, D=Sym4 W, T6=Sym5 W. V is the other three-space, P the even four-space, and W' the other odd doublet. A_q is never the representation A_std. The four sources are

    E_D=D O(-2)+(W'+T6)O(-3)+V O(-4)+O(-8),
    E_P=P O(-2)+(W'+T6)O(-3)+V O(-4)+W' O(-5),
    E_V=V O(-2)+(W'+T6)O(-3)+2V O(-4),
    E_Z=(W'+2T6)O(-3)+V O(-4).

The imported actual visibility says W'+2T6 embeds in H0(A_q(3)). The possible H0(K(3)) are 0 or S4 in source D, 0 or W' in source P, and zero in V and Z. These are coefficient-space conclusions, not fiber-rank assertions.

## 2. Actual endpoint capacity and a sign restriction

For F0=E or S, recursively form actual saturated derivative kernels F(j+1)=Fj^-. Put C=F0/F1 and Gj=Fj/F(j+1), j>=1. Differentiation gives actual coherent-image injections

    Gj -> G(j-1)(-2) -> ... -> C(-2j).

Consequently qj=rank Gj is nonincreasing and at most three. All Fj lie in the negative F0, and a nonzero saturated horizontal subbundle of the constant ambient would be constant in characteristic zero. Thus a nonzero Fj cannot have zero derivative; the chain terminates at zero, with sum qj=rank F1=n and deg F1=sum deg Gj.

If lambda1>=lambda2>=lambda3 are the top three ordinary degrees of C, exterior powers of these coherent injections give

    deg F1 <= max sum_(i=1..3)[hi lambdai-hi(hi+1)],       (1)
    h1>=h2>=h3>=0, h1+h2+h3=n.

Here hi counts j with qj>=i. Neither saturation of the images in C(-2j) nor a splitting of the connection is asserted. For n=13 the minimum of sum hi(hi+1) is 70, attained at (5,4,4); for n=9 it is 36, attained at (3,3,3).

Let u and v be the maximum and minimum ordinary degrees of A_q. Applying (1) to K gives

    -54-a <= 13u-70,  hence a+13u>=16.                  (2)

The sheaf injection B->A_q*(-2) bounds every B degree above by -2-v. Applying (1) to L yields

    -54-b <= 9(-2-v)-36,  hence b>=9v.

Together with a+b=-8-t, this gives

    a+9v<=-8-t.                                        (3)

If v>=0 then a>=0, contradicting (3); therefore v<=-1. If u<=0, (2) is impossible. If u=1, the four degrees and v<=-1 give a<=2 and then a+13u<=15, again contradicting (2). Thus

    u>=2 and v<=-1.                                    (4)

The final proof only needs (4), not any equality case or zero-defect assertion.

## 3. Exhaust the low-top possibilities by three proper coefficient mechanisms

Suppose for contradiction u<=2. Then u=2 by (4). Every A_q degree is at least -8 because E(8) is globally generated and A_q(8) is its actual quotient. Equivariant Birkhoff splitting and the center-even actual ambient require even coefficient irreducibles at even degrees and odd ones at odd degrees. Rank four permits only irreducible coefficient blocks of dimensions one, two, three or four.

First discard every dimension-four coefficient block: it fills the whole rank-four quotient, making all ordinary degrees equal, contrary to u>=2 and v<0. Among the remaining dimension-one, two or three blocks R O(e) with -8<=e<=2, the only ways for W' to occur in R tensor Sym^(e+3) W are

    W' O(-3),  V O(0),  A_std O(2).                    (5)

Negative symmetric indices contribute zero. This is a fixed small representation calculation, not a search of bundle candidates. A recurrence from the nine-vertex McKay graph verifies all relevant products through symmetric degree five. Scalar blocks contribute only Sym1 W, Sym3 W or Sym5 W, none containing W'. The two-dimensional products at e=-1,1 are T6 or W+S4 or S4+T6. At three dimensions the only additional W' contributions are the displayed V O and A_std O(2). Whole dimension-four coefficient blocks were excluded before this calculation.

Now use both required T6 copies and the rank budget:

1. If W' O(-3) occurs, it supplies W' but no T6. The remaining rank two must supply two T6 copies. A doublet block of degree at most one supplies at most one, while a scalar of degree at most two supplies T6 only at degree two. Hence necessarily

       A_q=W' O(-3)+2O(2).                             (6)

2. V O contributes W'+S4+T6. The remaining scalar must be O(2) to supply the second T6. This makes every degree nonnegative, contradicting (4).

3. A_std O(2) contributes W'+S4+2T6. Its remaining scalar O(e) has e<=-2 by (4) and even parity. The fixed source Hom test gives

       Hom_G(E,O(e))=0 for e=-6,-4,-2,
       Hom_G(E,O(-8))=C only for E=E_D,                (7)

and that last Hom comes solely from the displayed O(-8). Thus the only actual possibility is

       E=E_D,  A_q=A_std O(2)+O(-8).                  (8)

This argument leaves exactly the two written shapes (6),(8), derived symbolically from coefficient visibility, rank, parity and actual source Hom. It does not enumerate the global quotient domain.

## 4. The first shape violates primal endpoint capacity

For (6), a=-2 and deg K=-52. Its top three degrees are 2,2,-3. With z=h3 and h1+h2=13-z, the expression in (1) is

    13-5z-(h1^2+h2^2+z^2)
      <= -143/2+8z-(3/2)z^2
       = -365/6-(3/2)(z-8/3)^2.

It is an integer, so Cap13(A_q)<=-61. Equality is attained at heights (5,5,3), but equality is not needed: -52<=-61 is impossible. No determinant defect or dual saturation has been discarded.

## 5. The second shape forces a forbidden actual quartic coefficient multiplicity

Assume (8), and write E=E' + O(-8), where

    E'=D O(-2)+(W'+T6)O(-3)+V O(-4).

The O(-8) projection of the actual quotient E->A_q can come only from the source O(-8), by degree. Surjectivity makes that scalar nonzero. Hence the actual kernel K lies in E', and restriction gives an exact sequence

    0 -> K -> E' -> A_std O(2) -> 0.                   (9)

This is ordinary cancellation in the actual quotient map, not a horizontal decomposition of the ambient connection.

We first show H0(K(3))=0. The imported cubic-kernel theorem says its only possible nonzero representation is S4. If it were S4, its evaluation would give a nonzero bundle inclusion S4 O(-3)->K->E. Since K has top<=-3, these cubic sections form an actual top splitting subbundle. Its projection to all E summands except D O(-2) vanishes, by degree or irreducible inequivalence. The space

    Hom_G(S4 O(-3),D O(-2))=Hom_G(S4,D tensor W)

is one-dimensional because D tensor W=S4+T6. The canonical binary evaluation sequence is

    0 -> S4 O(-3) -> D O(-2) -> O(2) -> 0.             (10)

Thus its image is exactly the kernel in (10), up to a nonzero scalar. Since the actual quotient kills that image, its D-row factors through O(2). But

    Hom_G(O(2), A_std O(2)+O(-8))=0.

The whole D-row would vanish, putting D O(-2) into K and contradicting H0(K(2))=0. This proves H0(K(3))=0.

Now K has rank13, degree -52 and all ordinary degrees at most -4. Therefore every degree equals -4, so K=R O(-4). Twisting (9) by four and taking Euler characters determines R exactly. All E'(4) and A_std O(6) degrees are nonnegative, and K(4) is constant, so

    R= D tensor Sym2 W + (W'+T6) tensor W + V
        - A_std tensor Sym6 W
      = A_std+2V+P.                                   (11)

The ACTUAL derivative of K lands in (E/K)(-2)=A_q(-2). Its scalar O(-10) component is zero by degree, hence it lands in A_std O. The strict-top lemma for the saturated negative bundle K in the original constant ambient gives an injective coefficient map

    A_std+2V+P = H0(K(4)) -> H0(A_std O(4))
              = A_std tensor Sym4 W
              = A_std+D+V+P.                          (12)

This is impossible because the source has two V copies and the target only one. The coefficient injection follows from the actual derivative and the horizontal-negative-subbundle contradiction; no ordinary summand is assumed horizontal. Therefore (8) is impossible.

## 6. Contribution and limits

Both necessary low-top shapes have now been excluded, proving (T) uniformly over the actual sources and all original defects. This is stronger than a familiar capacity restatement: capacity and double-channel visibility reduce a whole degree-bounded sublocus to two shapes, and an actual source-kernel/derivative argument eliminates the last one.

The proof does not close maximal rank-four profile (1,1), remove a whole coarse rank-four label, or improve the global generic-rank>=4 bound. It does not settle the (1,2), (2,1), or (3,1) lanes. It makes no maximal-rank, square-surjectivity, full-adjoint, smoothing, algebraicity or original-repair claim. All original actual-geometric and source-theorem premises remain imported; exact character arithmetic is not proof-assistant certification of those premises.

No selected actual HM/source coefficients, parameters, points, jets, tensors, instance matrices/ranks/scans, historical enumeration or broad candidate search is used. The small universal checks only verify the displayed representation identities, four scalar Hom degrees, rank/degree arithmetic, and quadratic capacity identity.
