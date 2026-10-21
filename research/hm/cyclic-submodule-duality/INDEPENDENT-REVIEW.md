# Independent mathematical review

## Verdict and exact artifact

**PASS, conditional on the pinned original-module inputs.**

Reviewed `PROOF.md`, SHA-256:

`34658ec85774965116b66a1d27ba3f292865700cc961b32e71f202b627f9e1e4`.

This is an independent mathematical audit, not formal proof-assistant verification. The review checked the actual trace compatibility in PR491, commit e9ed26058f69f3b96bdcdf920cb638e9dd68def8, and the uniform column-quotient statement in PR511, commit 55bc80b2cb660edd741c93747df7304ee51a061e. The Hilbert function of the scalar algebra is used as the pinned PR500 input, not reproved here.

## Independent checks

1. **The two cyclic objects are distinct.** Quotienting the degree-zero presentation of H by the generator w in ker(lambda) gives H/Sw=S/J_lambda after choosing the remaining generator. Subtracting its Hilbert function from H gives Sw=(1,5,15,20,10,2), not (1,5,5). The generation-plus-perfect-pairing argument excludes lower-degree socle in H; taking the submodule Sw then gives its socle exactly H_5. The level type-two assertion follows.

2. **The dual evaluation map is identified, not guessed.** Write E=K/I, where K=Ann_S(w). The exact sequence E -> R -> H -> H/Sw dualizes to a sequence whose last cokernel is D_5(E). Under the pairing identification H=D_5(H), the dual map sends h to the functional r -> b(rw,h). The PR491 formula Phi(wh)(r)=b(rw,h) identifies this map with multiplication by w in Sym^2_S(H). Consequently D_5(E)=Sym^2_S(H)/(wH). The kernel of Sym^2(H) -> Sym^2(H/Sw) is precisely the image of (Sw)H=wH. Finally Sym^2_S(S/J_lambda) is S/J_lambda as a module after a generator choice. These natural maps justify the asserted module duality.

3. **The colon identity has the correct direction.** Faithful vector-space duality preserves annihilators, giving Ann_S(E)=J_lambda. By definition Ann_S(K/I)=(I:K). No double-annihilator conclusion follows in a non-Gorenstein scalar algebra. The proof correctly excludes (I:J_lambda)=K using their different degree-five components. The additional map f mod I -> fv, for a complement v of w, really is injective and S-linear; balance puts its image in (Sw)^perp. Equal graded dimensions prove surjectivity of this already constructed map, rather than substituting for a module map.

4. **Coisotropic reduction is valid.** Exact pairing duality gives (Sw)^perp=D_5(H/Sw), supported in degrees 3 through 5. The same degree range is contained in Sw, so (Sw)^perp is a submodule of Sw. Nondegeneracy of the ambient pairing makes it exactly the radical of the restricted pairing. The quotient is still cyclic and has a perfect balanced total-degree-five pairing. Its Hilbert function is (1,5,15,15,5,1). Generation and pairing exclude lower socle, and its degree-five component is one-dimensional, establishing the Gorenstein claim. The Hilbert function equals the compressed bound min(dim S_d,dim S_(5-d)).

5. **The quotient ideal is the annihilator of the actual square.** For homogeneous f of degree d<=5, Phi(fw^2) is zero exactly when b(fw,qw)=0 for every q of degree 5-d. These qw span the only degree of Sw that can pair with fw. Hence Ann_S(w^2) consists exactly of those f with fw in (Sw)^perp. For d>5 both conditions hold automatically. This proves equality of graded ideals, not only equality of quotient Hilbert functions. In particular the associated quintic functional is nonzero: otherwise w would lie in (Sw)^perp, which has no degree-zero component.

6. **The filtration is correctly graded.** Multiplication by w identifies T_w/K with (Sw)^perp, while the preceding duality identifies K/I with D_5(A_lambda). Each has Hilbert function (0,0,0,5,5,1). Thus T_w/I has Hilbert function (0,0,0,10,10,2), squares to zero by degree support, and has quotient R/(T_w/I) of length 42. No splitting of this extension is needed or implied.

## Scope

No correction was required. All conclusions are structural and conditional on the cited pairing, presentation, and Hilbert-function inputs. No actual HM/source-instance evaluation, matrix rank calculation, coefficient search, or large computation was performed. The original fixed-pair first-order residual, higher-order lifting, and algebraicity remain unresolved; this review does not upgrade any of those claims.
