# A noncube leading cubic excludes the common-direction source branch

## Statement and dependencies

Work over k=C(L) with S=k[X,Y], a regular pair f∈S3, g∈S5, and u∈k×. Fix any first-normal nilpotent lift T of n=u[[fg,−f²],[g²,−fg]], not necessarily the canonical lift. Write N=n+qT and N*N=q²d2 Id+q³d3 Id+O(q4). Let V=(S/(f))8 and d=[d2]≠0. The zero-leading-scalar source map K:S4→V is the k-linear map of PR747, with consistent fixed-T coefficients.

The new theorem is:

    image(K)⊂k d implies f is a cube of a linear form up to scalar
    after extension to an algebraic closure of k.                 (1)

Equivalently, every nontriple cubic divisor excludes the image-line condition in PR761's common-direction certificate. This includes cubics with a double and a distinct simple factor; square-freeness is unnecessary. No claim that the actual cubic is or is not a cube is made here.

Dependencies:
- [PR729, c384ae419983a5031af19c37674df020de1aa5da](https://github.com/Akilleez-QA/read-em-and-weep/blob/c384ae419983a5031af19c37674df020de1aa5da/research/hm/firstnormal-scalar-slope/PROOF.md): exact factorization, lift independence and nonvanishing of d, and its universal formula below.
- [PR747, 0a0ee30a5142477e54245b7c6f22d561abb4f5f1](https://github.com/Akilleez-QA/read-em-and-weep/blob/0a0ee30a5142477e54245b7c6f22d561abb4f5f1/research/hm/source-family-fourth-square-exclusion/PROOF.md): k-linear source construction and actual canonical compatibility.
- [PR760, d798dceb77b94b5dbb9457fb303984e595ce1874](https://github.com/Akilleez-QA/read-em-and-weep/blob/d798dceb77b94b5dbb9457fb303984e595ce1874/research/hm/rational-pole-strata/PROOF.md): proper exceptional-source locus versus common-direction dichotomy.
- [PR761, 9303e3fc336aea18b776005d7c9df3bd9ce9fc1f](https://github.com/Akilleez-QA/read-em-and-weep/blob/9303e3fc336aea18b776005d7c9df3bd9ce9fc1f/research/hm/common-direction-certificate/PROOF.md): common direction requires image(K|H)⊂k d.
- [PR763, 5b897b592113d756c16443977a9b1252f2160c03](https://github.com/Akilleez-QA/read-em-and-weep/blob/5b897b592113d756c16443977a9b1252f2160c03/research/hm/explicit-trace-functional/PROOF.md), the first-ideal operator theorem: for every r∈S9 and every nilpotent first-normal T, ℒ_T(fr)=[τ2(f,r)]/352; also tr(nV_h)≡0 mod f for V_h=[q³](h*N).

Here H is the constant five-dimensional positive source space, whose k-extension is S4. The map in (1) is the extension of the fixed-frame C-linear source map; no selected global source is substituted.

## 1. A universal two-dimensional source restriction

For every formal linear form ell∈S1, put h=f ell. This is a universal identity on a k-linear source subspace, not an evaluation at an actual source.

In a formal chart X coprime to f, use t=Y/X and denote f,ell,d2 by F,L,D. Choose the chart abstractly so that F has degree exactly three; this is possible over the infinite field k. PR729 and the operator theorem give

    K(f ell)=[B1(f ell,d2)−τ2(f,ell d2)/352],          (2)

because f ell d3 is divisible by f and tr(nV_h) vanishes modulo f. The first-ideal formula holds for every T, so there is no omitted canonical-to-actual lift correction.

The B1 denominator for degrees 4 and 8 is 462. Formal differentiation, reduced modulo F, gives

    τ2(f ell,d2) ≡ −42F′L D′+56F″L D+112F′L′D,
    τ2(f,ell d2) ≡ −32F′L D′−32F′L′D+72F″L D.

Substitution in (2) cancels D′ exactly and yields

    K(f ell)=d( F′L′/3−F″L/12 ) in k[t]/(F).         (3)

The equality uses the chart identification of V with k[t]/(F). It is not an equality of homogeneous forms of different degrees. Since only the residue D mod F survives, (3) is valid independently of the representative of d2 and for every nilpotent first-normal lift.

## 2. The image-line condition forces a one-dimensional multiplication image

Write F=c3 t³+c2 t²+c1 t+c0, c3≠0. Its formal derivatives give

    F″=6c3 t+2c2,
    4F′−tF″=6c3 t²+6c2 t+4c1.

Thus 1, F″, 4F′−tF″ are a basis of R=k[t]/(F): they have distinct degrees 0,1,2 and nonzero leading coefficients. This statement uses only the unspecified cubic's degree, not a rank evaluation of an actual matrix.

If image(K)⊂k d, apply the universal identity (3) to the coefficient basis L=1,t of all linear forms. It gives

    d F″ ∈ k d,
    d(4F′−tF″) ∈ k d.

Together with d∈k d and the displayed basis, these imply

    dR=k d,     dim_k(dR)=1.                          (4)

The last equality uses d≠0. This is a conditional deduction, not an actual rank measurement.

If one assumes merely that the actual C-linear image K(H) lies in k d, the same conclusion follows: H spans S4 over k and K extends k-linearly. Thus use of the formal subspace fS1 does not presume that f ell is a constant global source, nor require selecting an actual source.

## 3. Multiplication by d can have one-dimensional image only for a triple cubic

PR729 gives the universal residue formula

    d=(u²G²/48)Q mod F,
    Q=3(F″)²−8F′F‴.                                 (5)

The factors u and G are units in R, by u≠0 and regularity of (f,g). Hence dim(dR)=dim(QR). For a polynomial F of degree three,

    dim_k(QR)=3−deg gcd(F,Q).                         (6)

Indeed multiplication by Q has kernel represented by multiples of F/gcd(F,Q), and that kernel has dimension deg gcd(F,Q). This is an algebraic identity over k, unchanged by field extension.

Translate the formal variable to depress the arbitrary cubic and write F=a(t³+p t+q), with a≠0. This is an invertible universal coordinate transformation, not substitution of a model or actual coefficient values. Then

    Q=−12a²(3t²+4p).

Its degree is exactly two. By (4) and (6), gcd(F,Q) has degree two, so 3t²+4p divides t³+p t+q. Polynomial division is explicit:

    t³+p t+q = (t/3)(3t²+4p)−(p/3)t+q.

The remainder vanishes if and only if p=q=0. Therefore F=a t³ in this translated formal frame, so its divisor is triple. This proves (1). Conversely a triple cubic has dim(dR)=1, so this necessary condition cannot itself exclude that remaining stratum; no sufficiency for image(K)⊂k d is asserted.

## 4. Contribution to the source frontier and limits

If the actual leading cubic is structurally known to have a nontriple divisor, the common-direction alternative of PR760 is impossible: it requires image(K|H)⊂k d, contradicted by (1). In that conditional case the modular exceptional-source locus is proper closed, so a generic positive source has no nonzero negative direction with vanishing modular class. This implication is a family-level result, not a choice or evaluation of a source pair.

The remaining possible common-direction branch is now confined to the triple-cubic stratum. Determining whether the actual f lies there is a separate structural dependency. The theorem does not claim an actual noncube test has been performed, does not decide values at selected actual source pairs, and does not identify beta4 or establish algebraicity. No actual coefficients, roots, source points, derivatives, matrices, ranks, or selected models were evaluated; the only computations are the displayed bounded free-symbol identities.
